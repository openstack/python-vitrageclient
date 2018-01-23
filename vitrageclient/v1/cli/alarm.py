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
from cliff import show

from vitrageclient.common import utils


class AlarmList(lister.Lister):
    """List all alarms"""

    def get_parser(self, prog_name):
        parser = super(AlarmList, self).get_parser(prog_name)
        parser.add_argument("vitrage_id",
                            default='all',
                            nargs='?',
                            metavar="<vitrage id>",
                            help="Vitrage id of the affected resource")

        parser.add_argument('--all-tenants',
                            default=False,
                            dest='all_tenants',
                            action='store_true',
                            help='Shows alarms of all the tenants in the '
                                 'entity graph')

        return parser

    def take_action(self, parsed_args):
        vitrage_id = parsed_args.vitrage_id
        all_tenants = parsed_args.all_tenants

        alarms = utils.get_client(self).alarm.list(vitrage_id=vitrage_id,
                                                   all_tenants=all_tenants)
        return utils.list2cols_with_rename(
            (
                ('ID', 'vitrage_id'),
                ('Type', 'vitrage_type'),
                ('Name', 'name'),
                ('Resource Type', 'vitrage_resource_type'),
                ('Resource ID', 'vitrage_resource_id'),
                ('Severity', 'vitrage_operational_severity'),
                ('Update Time', 'update_timestamp'),
            ), alarms)


class AlarmShow(show.ShowOne):
    """Show an alarm"""

    def get_parser(self, prog_name):
        parser = super(AlarmShow, self).get_parser(prog_name)
        parser.add_argument("vitrage_id", help="Vitrage id of the alarm")
        return parser

    def take_action(self, parsed_args):
        vitrage_id = parsed_args.vitrage_id
        alarm = utils.get_client(self).alarm.get(vitrage_id=vitrage_id)
        return self.dict2columns(alarm)


# noinspection PyAbstractClass
class AlarmCount(show.ShowOne):
    """Show a count of all alarms"""

    def get_parser(self, prog_name):
        parser = super(AlarmCount, self).get_parser(prog_name)
        parser.add_argument('--all-tenants',
                            default=False,
                            dest='all_tenants',
                            action='store_true',
                            help='Shows counts for alarms of all '
                                 'the tenants')

        return parser

    @property
    def formatter_default(self):
        return 'json'

    def take_action(self, parsed_args):
        all_tenants = parsed_args.all_tenants

        counts = utils.get_client(self).alarm.count(
            all_tenants=all_tenants)

        return self.dict2columns(counts)
