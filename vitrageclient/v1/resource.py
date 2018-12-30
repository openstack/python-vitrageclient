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

    def list(self, resource_type=None, all_tenants=False, query=None):
        """Get a all resources

        :param all_tenants: should return all tenants resources
        :param resource_type: the type for the resources
        :param query: the query filter for the vertices
        """
        params = dict(resource_type=resource_type, all_tenants=all_tenants,
                      query=query)
        return self.api.post(self.url, json=params).json()

    def get(self, vitrage_id):
        """Get a resource

        :param vitrage_id: the vitrage_id of the resource
        """
        url = self.url + vitrage_id
        return self.api.get(url).json()

    def count(self, resource_type=None, all_tenants=False, query=None,
              group_by=None):
        """Get a count of all resources

        :param all_tenants: should return all tenants resources
        :param resource_type: the type for the resources
        :param query: the query filter for the vertices
        :param group_by: a property name to group by it's values
        """
        params = dict(resource_type=resource_type, all_tenants=all_tenants,
                      query=query, group_by=group_by)
        return self.api.post(self.url + 'count/', json=params).json()
