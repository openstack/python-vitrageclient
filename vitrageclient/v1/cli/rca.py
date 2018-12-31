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

from cliff import show
from vitrageclient.common import utils


# noinspection PyAbstractClass
class RcaShow(show.ShowOne):
    """Show the Root Cause Analysis for a certain alarm"""

    def get_parser(self, prog_name):
        parser = super(RcaShow, self).get_parser(prog_name)
        parser.add_argument('alarm_vitrage_id',
                            help='ID of an alarm')

        parser.add_argument('--all-tenants',
                            default=False,
                            dest='all_tenants',
                            action='store_true',
                            help='Shows alarms of all the tenants for the RCA')

        return parser

    @property
    def formatter_namespace(self):
        return 'vitrageclient.formatter.show'

    @property
    def formatter_default(self):
        return 'json'

    def take_action(self, parsed_args):
        alarm_id = parsed_args.alarm_vitrage_id
        all_tenants = parsed_args.all_tenants

        alarm = utils.get_client(self).rca.get(alarm_id=alarm_id,
                                               all_tenants=all_tenants)

        return self.dict2columns(alarm)
