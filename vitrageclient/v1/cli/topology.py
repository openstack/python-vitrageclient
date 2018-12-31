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

import argparse

from cliff import show

from vitrageclient.common import utils
from vitrageclient import exceptions as exc


# noinspection PyAbstractClass
class TopologyShow(show.ShowOne):
    """Show the topology of the system"""

    @staticmethod
    def positive_non_zero_int(argument_value):
        if argument_value is None:
            return None
        try:
            value = int(argument_value)
        except ValueError:
            msg = "%s must be an integer" % argument_value
            raise argparse.ArgumentTypeError(msg)
        if value <= 0:
            msg = "%s must be greater than 0" % argument_value
            raise argparse.ArgumentTypeError(msg)
        return value

    def get_parser(self, prog_name):
        parser = super(TopologyShow, self).get_parser(prog_name)
        parser.add_argument('--filter',
                            metavar='<query>',
                            help='query for the graph)')

        parser.add_argument('--limit',
                            type=self.positive_non_zero_int,
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
                            default=False,
                            dest='all_tenants',
                            action='store_true',
                            help='Shows entities of all the tenants in the '
                                 'entity graph')

        return parser

    @property
    def formatter_namespace(self):
        return 'vitrageclient.formatter.show'

    @property
    def formatter_default(self):
        return 'json'

    def take_action(self, parsed_args):
        limit = parsed_args.limit
        graph_type = parsed_args.type
        query = parsed_args.filter
        root = parsed_args.root
        all_tenants = parsed_args.all_tenants

        if graph_type == 'graph' and limit is not None and root is None:
            raise exc.CommandError("Graph-type 'graph' "
                                   "requires a 'root' with 'limit'.")

        topology = utils.get_client(self).topology.get(limit=limit,
                                                       graph_type=graph_type,
                                                       query=query,
                                                       root=root,
                                                       all_tenants=all_tenants)
        return self.dict2columns(topology)
