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
from datetime import datetime
import mock
from testtools import ExpectedException

from vitrageclient.tests.cli.base import CliTestCase
from vitrageclient.v1.cli.event import EventPost


# noinspection PyAttributeOutsideInit
class EventPostTest(CliTestCase):

    def setUp(self):
        super(EventPostTest, self).setUp()
        self.app = mock.Mock()
        self.event_post = EventPost(self.app, mock.Mock())

    def test_parsing_iso8601_with_not_a_date_string(self):
        self.assertRaises(ArgumentTypeError, self.event_post.iso8601, 'bla')

    def test_parsing_iso8601_in_a_good_format(self):
        self.event_post.iso8601('2014-12-13T12:44:21.123456')

    def test_iso8601_parsing_with_wrong_date_format(self):
        self.assertRaises(ArgumentTypeError, self.event_post.iso8601,
                          '2014/12/13 12:44:21')

    @mock.patch.object(ArgumentParser, "error")
    def test_parser_event_post_with_not_a_date_string(self, mock_parser):
        mock_parser.side_effect = self._my_parser_error_func
        parser = self.event_post.get_parser('vitrage event post')

        # noinspection PyCallByClass
        with ExpectedException(ArgumentTypeError,
                               'argument --time: -5 must be an iso8601 date'):
            parser.parse_args(args=['--type', 'bla',
                                    '--time', '-5',
                                    '--details', 'blabla'])

    @mock.patch.object(ArgumentParser, "error")
    def test_parser_event_post_type_required(self, mock_parser):
        mock_parser.side_effect = self._my_parser_error_func
        parser = self.event_post.get_parser('vitrage event post')

        # noinspection PyCallByClass
        with ExpectedException(ArgumentTypeError, r'.*--type'):
            parser.parse_args(args=['--details', 'blabla'])

    @mock.patch('vitrageclient.v1.cli.event.datetime')
    def test_parser_event_post_without_time_uses_time_now(self, dt_mock):
        current_time = datetime.now()
        dt_mock.now.return_value = current_time
        iso_time = current_time.isoformat()
        parser = self.event_post.get_parser('vitrage event post')
        args = parser.parse_args(args=['--type', 'bla',
                                       '--details', '{"blabla":[]}'
                                       ])

        with mock.patch.object(self.app.client.event, 'post') as poster_mock:
            self.event_post.take_action(args)

            poster_mock.assert_called_with(event_time=iso_time,
                                           details={'blabla': []},
                                           event_type='bla')
