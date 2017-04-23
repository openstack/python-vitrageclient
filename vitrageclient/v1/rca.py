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


class Rca(object):
    url = 'v1/rca/'

    def __init__(self, api):
        self.api = api

    def get(self, alarm_id, all_tenants=False):
        """Get RCA for an alarm

        :param all_tenants: should return all tenants rca
        :param alarm_id: the id of the alarm
        """
        params = dict(alarm_id=alarm_id,
                      all_tenants=all_tenants)
        return self.api.get(self.url, params=params).json()
