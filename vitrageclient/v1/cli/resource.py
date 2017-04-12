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

from vitrageclient.common import utils


# noinspection PyAbstractClass
class ResourceShow(show.ShowOne):
    """Show a resource"""

    def get_parser(self, prog_name):
        parser = super(ResourceShow, self).get_parser(prog_name)
        parser.add_argument('vitrage_id', help='vitrage_id of a resource')
        return parser

    def take_action(self, parsed_args):
        vitrage_id = parsed_args.vitrage_id
        resource = utils.get_client(self).resource.get(vitrage_id=vitrage_id)
        return self.dict2columns(resource)


class ResourceList(lister.Lister):
    """List resources"""

    def get_parser(self, prog_name):
        parser = super(ResourceList, self).get_parser(prog_name)
        parser.add_argument('--type',
                            dest='resource_type',
                            metavar='<resource type>',
                            help='Type of resource')
        parser.add_argument('--all-tenants',
                            default=False,
                            dest='all_tenants',
                            action='store_true',
                            help='Shows resources of all the tenants')

        return parser

    def take_action(self, parsed_args):
        resource_type = parsed_args.resource_type
        all_tenants = parsed_args.all_tenants
        resources = utils.get_client(self).resource.list(
            resource_type=resource_type,
            all_tenants=all_tenants)
        return utils.list2cols(('vitrage_id',
                                'type',
                                'name',
                                'id',
                                'state',
                                'project_id'), resources)
