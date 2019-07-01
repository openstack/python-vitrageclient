# Copyright 2016 Nokia
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


"""
Vitrage command line interface
"""

from __future__ import print_function

import logging
import os
import sys
import warnings

from cliff import app
from cliff import commandmanager
from keystoneauth1 import loading
from oslo_utils import importutils

from vitrageclient import __version__
from vitrageclient import auth
from vitrageclient import client

from vitrageclient.v1.cli import alarm
from vitrageclient.v1.cli import event
from vitrageclient.v1.cli import healthcheck
from vitrageclient.v1.cli import rca
from vitrageclient.v1.cli import resource
from vitrageclient.v1.cli import service
from vitrageclient.v1.cli import status
from vitrageclient.v1.cli import template
from vitrageclient.v1.cli import topology
from vitrageclient.v1.cli import webhook


profiler = importutils.try_import('osprofiler.profiler')


class VitrageCommandManager(commandmanager.CommandManager):
    COMMANDS = {
        'topology show': topology.TopologyShow,
        'resource show': resource.ResourceShow,
        'resource list': resource.ResourceList,
        'resource count': resource.ResourceCount,
        'alarm list': alarm.AlarmList,
        'alarm history': alarm.AlarmHistory,
        'alarm show': alarm.AlarmShow,
        'alarm count': alarm.AlarmCount,
        'rca show': rca.RcaShow,
        'template validate': template.TemplateValidate,
        'template list': template.TemplateList,
        'template versions': template.TemplateVersions,
        'template show': template.TemplateShow,
        'template add': template.TemplateAdd,
        'template delete': template.TemplateDelete,
        'event post': event.EventPost,
        'healthcheck': healthcheck.HealthCheck,
        'webhook delete': webhook.WebhookDelete,
        'webhook add': webhook.WebhookAdd,
        'webhook list': webhook.WebhookList,
        'webhook show': webhook.WebhookShow,
        'service list': service.ServiceList,
        'status': status.Status,
    }

    def load_commands(self, namespace):
        for k, v in self.COMMANDS.items():
            self.add_command(k, v)


class VitrageShell(app.App):
    def __init__(self):
        super(VitrageShell, self).__init__(
            description=__doc__,
            version=__version__,
            command_manager=VitrageCommandManager('vitrageclient'),
            deferred_help=True)

        self._client = None

    def build_option_parser(self, description, version, **argparse_kwargs):
        """Return an argparse option parser for this application.

        Subclasses may override this method to extend
        the parser with more global options.

        :param description: full description of the application
        :paramtype description: str
        :param version: version number for the application
        :paramtype version: str
        :param argparse_kwargs: extra keyword argument passed to the
                                ArgumentParser constructor
        :paramtype extra_kwargs: dict
        """

        parser = super(VitrageShell, self).build_option_parser(
            description, version, argparse_kwargs={'allow_abbrev': False})

        parser.add_argument('--vitrage-api-version',
                            default=os.environ.get('VITRAGE_API_VERSION', '1'),
                            help='Defaults to env[VITRAGE_API_VERSION] or 1.')

        if profiler:
            parser.add_argument(
                '--profile',
                metavar='HMAC_KEY',
                default=os.environ.get('OS_PROFILE'),
                help='HMAC key to use for encrypting context '
                     'data for performance profiling of request. '
                     'This key should be the value of the HMAC '
                     'key configured for the osprofiler '
                     'middleware in Vitrage api; it is specified '
                     'in the Vitrage configuration file at'
                     '"/etc/vitrage/vitrage.conf". Without the '
                     'key, profiling will not be triggered even '
                     'if osprofiler is enabled on the server '
                     'side.')

        plugin = self.register_keyauth_argparse_arguments(parser)

        if not isinstance(plugin, (auth.VitrageNoAuthLoader,
                                   auth.VitrageKeycloakLoader)):
            parser.add_argument('--endpoint',
                                default=os.environ.get('VITRAGE_ENDPOINT'),
                                help='Vitrage endpoint (Env: VITRAGE_ENDPOINT)'
                                )

        return parser

    @staticmethod
    def register_keyauth_argparse_arguments(parser):
        parser.add_argument(
            '--os-region-name',
            metavar='<auth-region-name>',
            dest='region_name',
            default=os.environ.get('OS_REGION_NAME'),
            help='Authentication region name (Env: OS_REGION_NAME)')
        parser.add_argument(
            '--os-interface',
            metavar='<interface>',
            dest='interface',
            choices=['admin', 'public', 'internal'],
            default=os.environ.get('OS_INTERFACE'),
            help='Select an interface type.'
                 ' Valid interface types: [admin, public, internal].'
                 ' (Env: OS_INTERFACE)')

        loading.register_session_argparse_arguments(parser=parser)

        return loading.register_auth_argparse_arguments(parser=parser,
                                                        argv=sys.argv,
                                                        default='password')

    @property
    def client(self):
        if self._client is None:
            if hasattr(self.options, "endpoint"):
                endpoint_override = self.options.endpoint
            else:
                endpoint_override = None

            if profiler and self.options.profile:
                # Initialize the root of the future trace: the created trace
                # ID will be used as the very first parent to which all
                # related traces will be bound to. The given HMAC key must
                # correspond to the one set in vitrage api vitrage.conf,
                # otherwise the latter will fail to check the request
                # signature and will skip initialization of osprofiler on the
                # server side.
                profiler.init(self.options.profile)

            auth_plugin = loading.load_auth_from_argparse_arguments(
                self.options)
            session = loading.load_session_from_argparse_arguments(
                self.options, auth=auth_plugin)

            # noinspection PyAttributeOutsideInit
            self._client = client.Client(
                self.options.vitrage_api_version,
                session=session,
                interface=self.options.interface,
                region_name=self.options.region_name,
                endpoint_override=endpoint_override)

        return self._client

    def configure_logging(self):
        if self.options.debug:
            self._set_debug_logging_messages()

        super(VitrageShell, self).configure_logging()
        root_logger = logging.getLogger('')

        self._configure_logging_messages(root_logger)
        self._hide_useless_logging_messages()

    def _set_debug_logging_messages(self):
        self.options.verbose_level = 3

    def _configure_logging_messages(self, root_logger):
        if self.options.verbose_level == 0:
            self._set_quiet_logging_messages(root_logger)
        elif self.options.verbose_level == 1:
            self._set_default_logging_messages(root_logger)
        elif self.options.verbose_level == 2:
            self._set_verbose_logging_messages(root_logger)
        elif self.options.verbose_level >= 3:
            self._set_double_verbose_logging_messages(root_logger)

    @staticmethod
    def _set_double_verbose_logging_messages(root_logger):
        root_logger.setLevel(logging.DEBUG)

    @staticmethod
    def _set_verbose_logging_messages(root_logger):
        root_logger.setLevel(logging.INFO)
        warnings.simplefilter("once")

    @staticmethod
    def _set_default_logging_messages(root_logger):
        root_logger.setLevel(logging.WARNING)
        warnings.simplefilter("ignore")

    @staticmethod
    def _set_quiet_logging_messages(root_logger):
        root_logger.setLevel(logging.ERROR)
        warnings.simplefilter("ignore")

    def _hide_useless_logging_messages(self):
        requests_log = logging.getLogger('requests')
        cliff_log = logging.getLogger('cliff')
        stevedore_log = logging.getLogger('stevedore')
        iso8601_log = logging.getLogger('iso8601')
        cliff_log.setLevel(logging.ERROR)
        stevedore_log.setLevel(logging.ERROR)
        iso8601_log.setLevel(logging.ERROR)
        if self.options.debug:
            requests_log.setLevel(logging.DEBUG)
        else:
            requests_log.setLevel(logging.ERROR)


def main(args=None):
    try:
        if args is None:
            args = sys.argv[1:]
        result = VitrageShell().run(args)
        if profiler and '--profile' in args:
            trace_id = profiler.get().get_base_id()
            print("\n\nTo display trace use the command:\n\n"
                  "  osprofiler trace show --html %s " % trace_id)
        return result
    except KeyboardInterrupt:
        print('... terminating vitrage client', file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
