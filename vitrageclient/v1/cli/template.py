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

import sys

from cliff import command
from cliff import lister
from cliff import show
from oslo_log import log

from vitrageclient.common import utils
from vitrageclient.common.utils import find_template_with_uuid

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


class TemplateVersions(lister.Lister):
    """List all template versions"""

    def get_parser(self, prog_name):
        parser = super(TemplateVersions, self).get_parser(prog_name)
        return parser

    def take_action(self, parsed_args):
        templates = utils.get_client(self).template.versions()
        return utils.list2cols_with_rename(
            (
                ('Version', 'version'),
                ('Status', 'status'),
            ), templates)


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
        parser.add_argument('id', help='Template UUID or Name')
        return parser

    @property
    def formatter_default(self):
        return 'yaml'

    def take_action(self, parsed_args):
        _id = parsed_args.id
        template = utils.get_client(self).template.show(_id=_id)
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

        parser.add_argument('--wait',
                            type=int,
                            default=None,
                            nargs='?',
                            const=sys.maxsize,
                            help='Wait until template is ACTIVE or in ERROR'
                                 ' default is to wait forever '
                                 'else number of seconds'
                            )

        parser.add_argument('--overwrite',
                            default=False,
                            action='store_true',
                            help='If template exists by name overwrite it'
                            )

        return parser

    def take_action(self, parsed_args):
        path = parsed_args.path
        template_type = parsed_args.type
        cli_param_list = parsed_args.params
        params = _parse_template_params(cli_param_list)
        wait = parsed_args.wait
        overwrite = parsed_args.overwrite

        templates = utils.get_client(self).template.add(
            path=path, template_type=template_type, params=params,
            overwrite=overwrite)

        if wait:
            utils.wait_for_action_to_end(wait,
                                         self._check_finished_loading,
                                         templates=templates)

        return utils.list2cols_with_rename(
            (
                ('UUID', 'uuid'),
                ('Name', 'name'),
                ('Status', 'status'),
                ('Status details', 'status details'),
                ('Date', 'date'),
                ('Type', 'type'),
            ), templates)

    def _check_finished_loading(self, templates):
        if all(
                (
                    template['status'] == 'ERROR'
                    for template in templates
                )
        ):
            return True

        try:
            api_templates = utils.get_client(self).template.list()
            self._update_templates_status(api_templates, templates)
            if any(
                    (
                        template['status'] == 'LOADING'
                        for template in templates
                    )
            ):
                return False
            return True
        except Exception:
            return True

    @staticmethod
    def _update_templates_status(api_templates, templates):
        for template in templates:
            uuid = template.get('uuid')
            if uuid:
                api_template = find_template_with_uuid(uuid, api_templates)
                if api_template:
                    template['status'] = api_template['status']


class TemplateDelete(command.Command):
    """Delete a template"""

    def get_parser(self, prog_name):
        parser = super(TemplateDelete, self).get_parser(prog_name)
        parser.add_argument('id',
                            help='<ID or Name> of a template',
                            nargs='+')
        parser.add_argument('--wait',
                            type=int,
                            default=None,
                            nargs='?',
                            const=sys.maxsize,
                            help='Wait until template is DELETED or in ERROR'
                            ' default is to wait forever else number of '
                                 'seconds'
                            )
        return parser

    @property
    def formatter_default(self):
        return 'json'

    def take_action(self, parsed_args):
        ids = parsed_args.id
        wait = parsed_args.wait
        utils.get_client(self).template.delete(ids=ids)
        if wait:
            utils.wait_for_action_to_end(wait,
                                         self._check_deleted,
                                         ids=ids)

    def _check_deleted(self, ids):
        for _id in ids:
            try:
                utils.get_client(self).template.show(_id)
            except Exception:  # if deleted we get exception
                pass
            else:
                return False
        return True
