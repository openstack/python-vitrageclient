# Copyright 2016 - Nokia Corporation
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
import re

import argparse
from cliff import command
from cliff import lister
from cliff import show

from vitrageclient.common import utils

from oslo_log import log

LOG = log.getLogger(__name__)


def _parse_template_params(cli_param_list):
    return dict(cli_param.split('=', 1) for cli_param in cli_param_list) \
        if cli_param_list else {}


# noinspection PyAbstractClass
class TemplateValidate(show.ShowOne):
    """Validate a template file"""

    def get_parser(self, prog_name):
        parser = super(TemplateValidate, self).get_parser(prog_name)
        parser.add_argument('--path',
                            required=True,
                            help='full path for template file or templates dir'
                            )
        parser.add_argument('--type',
                            choices=['standard', 'definition', 'equivalence'],
                            help='Template type. Valid types:'
                                 '[standard, definition, equivalence]')
        parser.add_argument('--params', nargs='+',
                            help='Actual values for parameters of the '
                                 'template. Several key=value pairs may be '
                                 'used, for example: --params '
                                 'template_name=cpu_problem '
                                 'alarm_name=\'High CPU Load\'')
        return parser

    @property
    def formatter_default(self):
        return 'json'

    def take_action(self, parsed_args):

        cli_param_list = parsed_args.params
        params = _parse_template_params(cli_param_list)

        result = utils.get_client(self).template.validate(
            path=parsed_args.path,
            template_type=parsed_args.type,
            params=params)

        return self.dict2columns(result)


class TemplateList(lister.Lister):
    """List all templates"""

    def get_parser(self, prog_name):
        parser = super(TemplateList, self).get_parser(prog_name)
        return parser

    def take_action(self, parsed_args):
        templates = utils.get_client(self).template.list()
        return utils.list2cols_with_rename(
            (
                ('UUID', 'uuid'),
                ('Name', 'name'),
                ('Status', 'status'),
                ('Status details', 'status details'),
                ('Date', 'date'),
                ('Type', 'type'),
            ), templates)


class TemplateShow(show.ShowOne):
    """Show a template"""

    def get_parser(self, prog_name):
        parser = super(TemplateShow, self).get_parser(prog_name)
        parser.add_argument('uuid', help='Template UUID')
        return parser

    @property
    def formatter_default(self):
        return 'json'

    def take_action(self, parsed_args):
        uuid = parsed_args.uuid
        template = utils.get_client(self).template.show(uuid=uuid)
        return self.dict2columns(template)


class TemplateAdd(lister.Lister):
    """Add a template

    support 3 types of templates:
    standard, definition, equivalence
    """

    def get_parser(self, prog_name):
        parser = super(TemplateAdd, self).get_parser(prog_name)
        parser.add_argument('--path',
                            required=True,
                            help='full path for template file or templates dir'
                            )
        parser.add_argument('--type',
                            choices=['standard', 'definition', 'equivalence'],
                            help='Template type. Valid types:'
                                 '[standard, definition, equivalence]')
        parser.add_argument('--params', nargs='+',
                            help='Actual values for parameters of the '
                                 'template. Several key=value pairs may be '
                                 'used, for example: --params '
                                 'template_name=cpu_problem '
                                 'alarm_name=\'High CPU Load\'')
        return parser

    def take_action(self, parsed_args):
        path = parsed_args.path
        template_type = parsed_args.type
        cli_param_list = parsed_args.params
        params = _parse_template_params(cli_param_list)

        templates = utils.get_client(self).template.add(
            path=path, template_type=template_type, params=params)

        return utils.list2cols_with_rename(
            (
                ('UUID', 'uuid'),
                ('Name', 'name'),
                ('Status', 'status'),
                ('Status details', 'status details'),
                ('Date', 'date'),
                ('Type', 'type'),
            ), templates)


class TemplateDelete(command.Command):
    """Delete a template"""

    def get_parser(self, prog_name):
        parser = super(TemplateDelete, self).get_parser(prog_name)
        parser.add_argument('uuid',
                            help='ID of a template',
                            nargs='+',
                            type=TemplateDelete.vaild_uuid)
        return parser

    @property
    def formatter_default(self):
        return 'json'

    def take_action(self, parsed_args):
        uuid = parsed_args.uuid
        utils.get_client(self).template.delete(uuid=uuid)

    @staticmethod
    def vaild_uuid(uuids):
        rege = '^[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}$'
        if type(uuids) != list:
            uuids = [uuids]
        for uuid in uuids:
            if not re.match(rege, uuid):
                raise argparse.ArgumentTypeError("Not a uuid format")
        return uuids
