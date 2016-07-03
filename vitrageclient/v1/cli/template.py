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

from cliff import lister
from cliff import show
from oslo_log import log

from vitrageclient.common.exc import CommandException
from vitrageclient.common import utils

LOG = log.getLogger(__name__)


# noinspection PyAbstractClass
class TemplateValidate(show.ShowOne):

    def get_parser(self, prog_name):
        parser = super(TemplateValidate, self).get_parser(prog_name)
        parser.add_argument('--path', help='full path for template file or '
                                           'templates dir)')
        return parser

    def formatter_default(self):
        return 'json'

    def take_action(self, parsed_args):

        if not parsed_args.path:
            raise CommandException(message='No path requested, add --path')

        if parsed_args.path:
            result = self.app.client.template.validate(path=parsed_args.path)

        return self.dict2columns(result)


class TemplateList(lister.Lister):
    """Template list"""

    def get_parser(self, prog_name):
        parser = super(TemplateList, self).get_parser(prog_name)
        return parser

    def take_action(self, parsed_args):
        templates = self.app.client.template.list()
        return utils.list2cols(('uuid',
                                'name',
                                'status',
                                'status details',
                                'date'), templates)


class TemplateShow(show.ShowOne):
    """Template show"""

    def get_parser(self, prog_name):
        parser = super(TemplateShow, self).get_parser(prog_name)
        parser.add_argument('uuid', help='Template UUID')
        return parser

    def formatter_default(self):
        return 'json'

    def take_action(self, parsed_args):
        uuid = parsed_args.uuid
        template = self.app.client.template.show(uuid=uuid)
        return self.dict2columns(template)
