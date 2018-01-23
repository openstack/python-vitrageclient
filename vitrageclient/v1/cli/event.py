# Copyright 2017 - Nokia Corporation
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

import json

import argparse
from cliff import command
from datetime import datetime
from iso8601 import iso8601
from iso8601 import ParseError


# noinspection PyAbstractClass
class EventPost(command.Command):
    """Post an event to Vitrage"""

    @staticmethod
    def iso8601(argument_value):
        try:
            if argument_value:
                iso8601.parse_date(argument_value)
        except ParseError:
            msg = "%s must be an iso8601 date" % argument_value
            raise argparse.ArgumentTypeError(msg)

    def get_parser(self, prog_name):
        parser = super(EventPost, self).get_parser(prog_name)

        parser.add_argument('--type',
                            required=True,
                            help='The type of the event')

        parser.add_argument('--time',
                            default='',
                            type=self.iso8601,
                            help='The timestamp of the event in ISO 8601 '
                                 'format: YYYY-MM-DDTHH:MM:SS.mmmmmm. '
                                 'If not specified, the current time is used')

        parser.add_argument('--details',
                            default='{}',
                            help='A json string with the event details')

        return parser

    def take_action(self, parsed_args):

        if parsed_args.time:
            event_time = parsed_args.time
        else:
            event_time = datetime.now().isoformat()

        event_type = parsed_args.type
        details = parsed_args.details

        self.app.client.event.post(event_time=event_time,
                                   event_type=event_type,
                                   details=json.loads(details))
