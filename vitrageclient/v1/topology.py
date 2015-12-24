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


class Topology(object):
    URL = "v1/topology/"

    def __init__(self, api):
        self.api = api

    def get(self, edges=None, vertices=None, depth=None, graph_type='graph'):
        """Get a topology

        :param graph_type: graph can be tree or graph
        :param depth: the depth of the topology graph
        :param vertices: list of vertices types
        :param edges: list of edges type
        """

        params = dict(edges=edges, vertices=vertices, depth=depth,
                      graph_type=graph_type)
        return self.api.get(self.URL, params=params).json()
