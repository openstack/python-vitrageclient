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

from cliff import lister

from vitrageclient.common import utils


class AlarmList(lister.Lister):
    """List alarms on entity"""

    def get_parser(self, prog_name):
        parser = super(AlarmList, self).get_parser(prog_name)
        parser.add_argument("vitrage_id",
                            default='all',
                            nargs='?',
                            metavar="<vitrage id>",
                            help="Vitrage id of the affected resource")

        parser.add_argument('--all-tenants',
                            metavar='<0|1>',
                            nargs='?',
                            type=int,
                            const=1,
                            default=0,
                            dest='all_tenants',
                            help='Shows alarms of all the tenants in the '
                                 'entity graph')

        return parser

    def take_action(self, parsed_args):
        vitrage_id = parsed_args.vitrage_id
        all_tenants = parsed_args.all_tenants

        alarms = utils.get_client(self).alarm.list(vitrage_id=vitrage_id,
                                                   all_tenants=all_tenants)
        return utils.list2cols(('vitrage_id',
                                'type',
                                'name',
                                'resource_type',
                                'resource_id',
                                'aggregated_severity',
                                'operational_severity',
                                'update_timestamp'), alarms)
