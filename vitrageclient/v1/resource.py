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


class Resource(object):
    url = 'v1/resources/'

    def __init__(self, api):
        self.api = api

    def list(self, resource_type=None):
        """Get a all resources

        :param resource_type: the type for the resources
        """
        params = dict(resource_type=resource_type)
        return self.api.get(self.url, params=params).json()

    def get(self, resource_id):
        """Get a resource

        :param resource_id: the id of the resource
        """
        url = self.url + resource_id
        return self.api.get(url).json()
