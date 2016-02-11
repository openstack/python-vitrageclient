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


# noinspection PyAbstractClass
class RcaShow(show.ShowOne):
    """Show an RCA"""

    def get_parser(self, prog_name):
        parser = super(RcaShow, self).get_parser(prog_name)
        parser.add_argument('alarm_id', help='ID of an alarm')
        return parser

    def formatter_default(self):
        return 'json'

    def take_action(self, parsed_args):
        alarm_id = parsed_args.alarm_id
        alarm = self.app.client.rca.get(alarm_id=alarm_id)
        return self.dict2columns(alarm)
