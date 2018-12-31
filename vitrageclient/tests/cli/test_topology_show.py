# Copyright 2017 Nokia
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
from argparse import ArgumentParser
from argparse import ArgumentTypeError

import json

# noinspection PyPackageRequirements
import mock
# noinspection PyPackageRequirements
import six
from testtools import ExpectedException

from vitrageclient.common.formatters import DOTFormatter
from vitrageclient.tests.cli.base import CliTestCase
from vitrageclient.v1.cli.topology import TopologyShow

JSON_DATA = '''
{
  "directed": true,
  "graph": {},
  "links": [
    {
      "key": "contains",
      "source": 0,
      "vitrage_is_deleted": false,
      "relationship_type": "contains",
      "target": 2
    },
    {
      "key": "contains",
      "source": 1,
      "vitrage_is_deleted": false,
      "relationship_type": "contains",
      "target": 0
    }
  ],
  "multigraph": true,
  "nodes": [
    {
      "id": "nova",
      "vitrage_sample_timestamp": "2018-12-31T13:44:03Z",
      "vitrage_datasource_name": "nova.zone",
      "vitrage_operational_state": "OK",
      "name": "nova",
      "state": "available",
      "update_timestamp": "2018-12-31T13:44:03Z",
      "is_real_vitrage_id": true,
      "vitrage_id": "05a19de3-e929-4730-ad81-10fa57dcfa0a",
      "vitrage_aggregated_state": "AVAILABLE",
      "vitrage_type": "nova.zone",
      "vitrage_is_deleted": false,
      "graph_index": 0,
      "vitrage_category": "RESOURCE",
      "vitrage_cached_id": "125f1d8c4451a6385cc2cfa2b0ba45be",
      "vitrage_is_placeholder": false
    },
    {
      "id": "OpenStack Cluster",
      "vitrage_sample_timestamp": "2018-12-31T13:44:03Z",
      "vitrage_operational_state": "OK",
      "name": "openstack.cluster",
      "state": "available",
      "graph_index": 1,
      "vitrage_id": "070c413e-5a8c-4823-ae20-af44936de2a0",
      "vitrage_aggregated_state": "AVAILABLE",
      "vitrage_type": "openstack.cluster",
      "is_real_vitrage_id": true,
      "vitrage_category": "RESOURCE",
      "vitrage_cached_id": "3c7f9d22d9dd1615a00404f86cb3e289",
      "vitrage_is_deleted": false,
      "vitrage_is_placeholder": false
    },
    {
      "id": "ebarilan-devstack",
      "vitrage_sample_timestamp": "2018-12-31T13:44:03Z",
      "vitrage_datasource_name": "nova.host",
      "vitrage_operational_state": "OK",
      "name": "ebarilan-devstack",
      "state": "available",
      "update_timestamp": "2018-12-31T13:44:03Z",
      "is_real_vitrage_id": true,
      "vitrage_id": "10da4fa2-397f-4b2e-a43b-937e11ab7daf",
      "vitrage_aggregated_state": "AVAILABLE",
      "vitrage_type": "nova.host",
      "vitrage_is_deleted": false,
      "graph_index": 2,
      "vitrage_category": "RESOURCE",
      "vitrage_cached_id": "9ae4db6fb920e19cb5c57a428b29eb59",
      "vitrage_is_placeholder": false
    },
    {
      "id": "b36b4d7a-b309-4b02-9662-5abd79741750",
      "vitrage_sample_timestamp": "2018-12-31T13:44:04Z",
      "vitrage_datasource_name": "cinder.volume",
      "project_id": "210140f1f5a94af99e0adf79a883b75a",
      "vitrage_operational_state": "OK",
      "vitrage_aggregated_state": "AVAILABLE",
      "vitrage_is_placeholder": false,
      "state": "available",
      "attachments": [],
      "graph_index": 3,
      "vitrage_id": "f0ca9fac-3ebd-4748-97ba-e93a7e7108aa",
      "size": 1,
      "vitrage_type": "cinder.volume",
      "vitrage_is_deleted": false,
      "vitrage_category": "RESOURCE",
      "vitrage_cached_id": "f998c5f7bf1851e17e3eea902800a7df",
      "update_timestamp": "2018-12-31T08:43:32Z",
      "is_real_vitrage_id": true,
      "volume_type": "lvmdriver-1"
    },
    {
      "id": "cebf5d5b-d7b1-4cfb-86fa-f660306b4c1a",
      "vitrage_sample_timestamp": "2018-12-31T13:44:04Z",
      "vitrage_datasource_name": "neutron.network",
      "project_id": "210140f1f5a94af99e0adf79a883b75a",
      "vitrage_operational_state": "OK",
      "vitrage_category": "RESOURCE",
      "vitrage_is_placeholder": false,
      "state": "ACTIVE",
      "update_timestamp": "2018-12-30T08:30:33Z",
      "is_real_vitrage_id": true,
      "vitrage_id": "eea46e33-81dc-4430-a771-852bac37b43d",
      "vitrage_aggregated_state": "ACTIVE",
      "vitrage_type": "neutron.network",
      "vitrage_is_deleted": false,
      "graph_index": 4,
      "name": "public",
      "vitrage_cached_id": "a0eeca0ab2c865915e23319a2e6d0fd7"
    }
  ],
  "raw": true
}

'''
DOT_DATA = '''\
digraph  {
0 [id=nova, is_real_vitrage_id=True, label="nova\\nnova.zone", state=available, update_timestamp="2018-12-31T13:44:03Z", vitrage_aggregated_state=AVAILABLE, vitrage_cached_id="125f1d8c4451a6385cc2cfa2b0ba45be", vitrage_category=RESOURCE, vitrage_datasource_name="nova.zone", vitrage_id="05a19de3-e929-4730-ad81-10fa57dcfa0a", vitrage_is_deleted=False, vitrage_is_placeholder=False, vitrage_operational_state=OK, vitrage_sample_timestamp="2018-12-31T13:44:03Z", vitrage_type="nova.zone"];
1 [id="OpenStack Cluster", is_real_vitrage_id=True, label="openstack.cluster", state=available, vitrage_aggregated_state=AVAILABLE, vitrage_cached_id="3c7f9d22d9dd1615a00404f86cb3e289", vitrage_category=RESOURCE, vitrage_id="070c413e-5a8c-4823-ae20-af44936de2a0", vitrage_is_deleted=False, vitrage_is_placeholder=False, vitrage_operational_state=OK, vitrage_sample_timestamp="2018-12-31T13:44:03Z", vitrage_type="openstack.cluster"];
2 [id="ebarilan-devstack", is_real_vitrage_id=True, label="ebarilan-devstack\\nnova.host", state=available, update_timestamp="2018-12-31T13:44:03Z", vitrage_aggregated_state=AVAILABLE, vitrage_cached_id="9ae4db6fb920e19cb5c57a428b29eb59", vitrage_category=RESOURCE, vitrage_datasource_name="nova.host", vitrage_id="10da4fa2-397f-4b2e-a43b-937e11ab7daf", vitrage_is_deleted=False, vitrage_is_placeholder=False, vitrage_operational_state=OK, vitrage_sample_timestamp="2018-12-31T13:44:03Z", vitrage_type="nova.host"];
3 [attachments="[]", id="b36b4d7a-b309-4b02-9662-5abd79741750", is_real_vitrage_id=True, label="cinder.volume", project_id="210140f1f5a94af99e0adf79a883b75a", size=1, state=available, update_timestamp="2018-12-31T08:43:32Z", vitrage_aggregated_state=AVAILABLE, vitrage_cached_id=f998c5f7bf1851e17e3eea902800a7df, vitrage_category=RESOURCE, vitrage_datasource_name="cinder.volume", vitrage_id="f0ca9fac-3ebd-4748-97ba-e93a7e7108aa", vitrage_is_deleted=False, vitrage_is_placeholder=False, vitrage_operational_state=OK, vitrage_sample_timestamp="2018-12-31T13:44:04Z", vitrage_type="cinder.volume", volume_type="lvmdriver-1"];
4 [id="cebf5d5b-d7b1-4cfb-86fa-f660306b4c1a", is_real_vitrage_id=True, label="public\\nneutron.network", project_id="210140f1f5a94af99e0adf79a883b75a", state=ACTIVE, update_timestamp="2018-12-30T08:30:33Z", vitrage_aggregated_state=ACTIVE, vitrage_cached_id=a0eeca0ab2c865915e23319a2e6d0fd7, vitrage_category=RESOURCE, vitrage_datasource_name="neutron.network", vitrage_id="eea46e33-81dc-4430-a771-852bac37b43d", vitrage_is_deleted=False, vitrage_is_placeholder=False, vitrage_operational_state=OK, vitrage_sample_timestamp="2018-12-31T13:44:04Z", vitrage_type="neutron.network"];
0 -> 2  [key=contains, label=contains, vitrage_is_deleted=False];
1 -> 0  [key=contains, label=contains, vitrage_is_deleted=False];
}
'''  # noqa


# noinspection PyAttributeOutsideInit
class TopologyShowTest(CliTestCase):

    def setUp(self):
        super(TopologyShowTest, self).setUp()
        self.topology_show = TopologyShow(mock.Mock(), mock.Mock())

    def test_positive_integer_validation_with_negative(self):
        self.assertRaises(ArgumentTypeError,
                          self.topology_show.positive_non_zero_int, -1)

    def test_positive_integer_validation_with_zero(self):
        self.assertRaises(ArgumentTypeError,
                          self.topology_show.positive_non_zero_int, 0)

    def test_positive_integer_validation_with_string(self):
        self.assertRaises(ArgumentTypeError,
                          self.topology_show.positive_non_zero_int, 'bla')

    def test_positive_integer_validation_with_positive(self):
        self.topology_show.positive_non_zero_int(1)

    @mock.patch.object(ArgumentParser, "error")
    def test_parser_topology_limit_with_a_negative_number(self, mock_parser):
        mock_parser.side_effect = self._my_parser_error_func
        parser = self.topology_show.get_parser('vitrage topology show')

        with ExpectedException(ArgumentTypeError,
                               'argument --limit: -5 must be greater than 0'):
            parser.parse_args(args=['--filter', 'bla',
                                    '--limit', '-5',
                                    '--root', 'blabla',
                                    '--graph-type', 'tree'])

    @mock.patch.object(ArgumentParser, "error")
    def test_parser_topology_limit_with_a_string(self, mock_parser):
        mock_parser.side_effect = self._my_parser_error_func
        parser = self.topology_show.get_parser('vitrage topology show')

        with ExpectedException(ArgumentTypeError,
                               'argument --limit: spam must be an integer'):
            parser.parse_args(args=['--filter', 'bla',
                                    '--limit', 'spam',
                                    '--root', 'blabla',
                                    '--graph-type', 'tree'])

    def test_dot_emitter(self):
        def dict2columns(data):
            return zip(*sorted(data.items()))

        out = six.StringIO()
        formatter = DOTFormatter()
        topology = json.loads(JSON_DATA)
        columns, topology = dict2columns(topology)

        formatter.emit_one(columns, topology, out, None)

        self.assertEqual(DOT_DATA, out.getvalue())
