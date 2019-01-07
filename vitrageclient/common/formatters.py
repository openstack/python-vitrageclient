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
import abc
from cliff.formatters import base
import six

from networkx.drawing.nx_pydot import write_dot
from networkx.readwrite.graphml import GraphMLWriter
from networkx.readwrite import json_graph

import networkx as nx


@six.add_metaclass(abc.ABCMeta)
class GraphFormatter(base.SingleFormatter):
    def add_argument_group(self, parser):
        pass

    def emit_one(self, column_names, data, stdout, _=None):
        data = {n: i for n, i in zip(column_names, data)}

        # vitrage properties are not standard
        # to convert with networkx we need to
        # use the standard properties
        # some converters have issues with multigraph
        # so disable it (currently we don't have real multigraphs)
        self._reformat(data)

        if nx.__version__ >= '2.0':
            graph = json_graph.node_link_graph(
                data, attrs={'name': 'graph_index'})
        else:
            graph = json_graph.node_link_graph(data)

        self._write_format(graph, stdout)

    @staticmethod
    def _reformat(data):
        for node in data['nodes']:
            name = node.pop('name', None)
            v_type = node['vitrage_type']
            if name and name != v_type:
                # if name and type the same
                # don't print twice its redundant
                # e.g openstack.cluster
                node[u'label'] = name + '\n' + v_type
            else:
                node[u'label'] = v_type

            # type list is not supported in some
            # formats
            GraphFormatter._list2str(node)

        data['multigraph'] = False

        for node in data['links']:
            node[u'label'] = node.pop('relationship_type')
            # used only in multigraph
            node.pop('key')

    @staticmethod
    def _list2str(node):
        for k, v in node.items():
            if type(v) == list:
                node[k] = str(v)

    @abc.abstractmethod
    def _write_format(self, graph, stdout):
        pass


class DOTFormatter(GraphFormatter):

    def _write_format(self, graph, stdout):
        write_dot(graph, stdout)


class GraphMLFormatter(GraphFormatter):

    def _write_format(self, graph, stdout):
        writer = GraphMLWriter(graph=graph)
        writer.dump(stdout)
