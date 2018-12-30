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

    METADATA = ('name', 'project_id', 'update_timestamp')

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
        parser.add_argument('--filter',
                            metavar='<query>',
                            help='resource query')

        return parser

    def take_action(self, parsed_args):
        resource_type = parsed_args.resource_type
        all_tenants = parsed_args.all_tenants
        query = parsed_args.filter
        resources = utils.get_client(self).resource.list(
            resource_type=resource_type,
            all_tenants=all_tenants,
            query=query)
        # cluster, zone and host don't have "project_id" property
        # neutron.port don't have "name" property
        # cluster don't have "update_timestamp"
        for resource in resources:
            resource['metadata'] = \
                {item: resource[item] for item in self.METADATA
                 if item in resource}

        return utils.list2cols_with_rename(
            (
                ('ID', 'vitrage_id'),
                ('Type', 'vitrage_type'),
                ('Data Source ID', 'id'),
                ('State', 'vitrage_operational_state'),
                ('Metadata', 'metadata'),
            ), resources)


class ResourceCount(show.ShowOne):
    """Show a count of all resources"""

    def get_parser(self, prog_name):
        parser = super(ResourceCount, self).get_parser(prog_name)
        parser.add_argument('--type',
                            dest='resource_type',
                            metavar='<resource type>',
                            help='Type of resource')
        parser.add_argument('--all-tenants',
                            default=False,
                            dest='all_tenants',
                            action='store_true',
                            help='Shows resources of all the tenants')
        parser.add_argument('--filter',
                            metavar='<query>',
                            help='resource query'),
        parser.add_argument(
            '--group-by',
            dest='group_by',
            metavar='<group_by>',
            default='vitrage_type',
            help='A resource data field, to group by it\'s values'),
        return parser

    @property
    def formatter_default(self):
        return 'json'

    def take_action(self, parsed_args):
        resource_type = parsed_args.resource_type
        all_tenants = parsed_args.all_tenants
        query = parsed_args.filter
        group_by = parsed_args.group_by
        resource_count = utils.get_client(self).resource.count(
            resource_type=resource_type,
            all_tenants=all_tenants,
            query=query,
            group_by=group_by)

        return self.dict2columns(resource_count)
