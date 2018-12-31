#  Copyright 2018 - Nokia Corporation
#  #
#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#  #
#       http://www.apache.org/licenses/LICENSE-2.0
#  #
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.
from cliff.formatters import base

from networkx.drawing.nx_pydot import write_dot
from networkx.readwrite import json_graph

import networkx as nx


class DOTFormatter(base.SingleFormatter):
    def add_argument_group(self, parser):
        pass

    def emit_one(self, column_names, data, stdout, parsed_args):
        data = {n: i for n, i in zip(column_names, data)}

        # pydot doesn't like the name property
        # use label instead
        self._relabel(data)

        if nx.__version__ >= '2.0':
            graph = json_graph.node_link_graph(
                data, attrs={'name': 'graph_index'})
        else:
            graph = json_graph.node_link_graph(data)

        write_dot(graph, stdout)

    @staticmethod
    def _relabel(data):
        for node in data['nodes']:
            name = node.pop('name', None)
            v_type = node['vitrage_type']
            if name and name != v_type:
                # if name and type the same
                # dont print twice its redundant
                # e.g openstack.cluster
                node[u'label'] = name + '\n' + v_type
            else:
                node[u'label'] = v_type

        # change the relationship_type to label
        # so we will see it in dot visualizer
        for node in data['links']:
            node[u'label'] = node.pop('relationship_type')
