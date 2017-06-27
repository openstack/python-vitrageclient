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

# noinspection PyPackageRequirements
import mock
# noinspection PyPackageRequirements
from testtools import ExpectedException

from vitrageclient.tests.cli.base import CliTestCase
from vitrageclient.v1.cli.topology import TopologyShow


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
