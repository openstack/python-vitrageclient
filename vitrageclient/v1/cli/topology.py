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

from cliff import show
from vitrageclient.common import exc
from vitrageclient.common import utils


# noinspection PyAbstractClass
class TopologyShow(show.ShowOne):
    """Show the topology of the system"""

    def get_parser(self, prog_name):
        parser = super(TopologyShow, self).get_parser(prog_name)
        parser.add_argument('--filter',
                            metavar='<query>',
                            help='query for the graph)')

        parser.add_argument('--limit',
                            type=int,
                            metavar='<depth>',
                            help='the depth of the topology graph')

        parser.add_argument('--root',
                            help='the root of the topology graph')

        parser.add_argument('--graph-type',
                            choices=['tree', 'graph'],
                            default='graph',
                            dest='type',
                            help='graph type. '
                                 'Valid graph types: [tree, graph]')

        parser.add_argument('--all-tenants',
                            metavar='<0|1>',
                            nargs='?',
                            type=int,
                            const=1,
                            default=0,
                            dest='all_tenants',
                            help='Shows entities of all the tenants in the '
                                 'entity graph')

        return parser

    def formatter_default(self):
        return 'json'

    def take_action(self, parsed_args):
        limit = parsed_args.limit
        graph_type = parsed_args.type
        query = parsed_args.filter
        root = parsed_args.root
        all_tenants = parsed_args.all_tenants

        if graph_type == 'graph' and limit is not None and root is None:
            raise exc.CommandException(
                message="Graph-type 'graph' requires a 'root' with 'limit'.")

        topology = utils.get_client(self).topology.get(limit=limit,
                                                       graph_type=graph_type,
                                                       query=query,
                                                       root=root,
                                                       all_tenants=all_tenants)
        return self.dict2columns(topology)
