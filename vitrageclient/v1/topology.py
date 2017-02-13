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
    URL = 'v1/topology/'

    def __init__(self, api):
        self.api = api

    def get(self,
            limit=None,
            graph_type='graph',
            query=None,
            root=None,
            all_tenants=False):
        """Get a topology

        :param root:  the root of the topology graph
        :param query: the query filter for the topology
        :param graph_type: graph can be tree or graph
        :param limit: the depth of the topology graph
        :param all_tenants: show entities in graph of all tenants
        """

        params = dict(depth=limit,
                      graph_type=graph_type,
                      query=query,
                      root=root,
                      all_tenants=all_tenants)
        return self.api.post(self.URL, json=params).json()
