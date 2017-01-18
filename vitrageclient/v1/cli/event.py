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

from cliff import command
from datetime import datetime

from vitrageclient.common import exc


# noinspection PyAbstractClass
class EventPost(command.Command):
    """Show the event of the system"""

    def get_parser(self, prog_name):
        parser = super(EventPost, self).get_parser(prog_name)

        parser.add_argument('--type',
                            help='The type of the event')

        parser.add_argument('--time',
                            default='',
                            help='The timestamp of the event in ISO 8601 '
                                 'format: YYYY-MM-DDTHH:MM:SS.mmmmmm. '
                                 'If not specified, the current time is used')

        parser.add_argument('--details',
                            default='{}',
                            help='A json string with the event details')

        return parser

    def formatter_default(self):
        return 'json'

    def take_action(self, parsed_args):
        if not parsed_args.type:
            raise exc.CommandException(
                message='Missing event type, please add --type')

        if parsed_args.time:
            event_time = parsed_args.time
        else:
            event_time = datetime.now().isoformat()

        event_type = parsed_args.type
        details = parsed_args.details

        self.app.client.event.post(event_time=event_time,
                                   event_type=event_type,
                                   details=details)
