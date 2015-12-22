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


# noinspection PyAbstractClass
class TopologyShow(show.ShowOne):
    """Show the topology of the system"""

    def get_parser(self, prog_name):
        parser = super(TopologyShow, self).get_parser(prog_name)
        parser.add_argument("--edges",
                            type=lambda s: [edge for edge in s.split(',')],
                            metavar="<edge type,edge type>",
                            help="list of edges type (separated by ',')")
        parser.add_argument("--vertices",
                            type=lambda s: [vertex for vertex in s.split(',')],
                            metavar="<vertex type,vertex type>",
                            help="list of vertices types (separated by ',')")
        parser.add_argument("--depth", type=int,
                            help="the depth of the topology")
        return parser

    def formatter_default(self):
        return "json"

    def take_action(self, parsed_args):
        topology = self.app.client.topology.get(edges=parsed_args.edges,
                                                vertices=parsed_args.vertices,
                                                depth=parsed_args.depth)
        return self.dict2columns(topology)
