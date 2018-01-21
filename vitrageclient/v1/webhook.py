# Copyright 2017 - ZTE Corporation
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


class Webhook(object):

    url = 'v1/webhook/'

    def __init__(self, api):
        self.api = api

    def list(self, all_tenants=False):
        """Get webhook list"""
        params = dict(all_tenants=all_tenants)
        return self.api.get(self.url, params=params).json()

    def show(self, id):
        """Show specific webhook

        :param id: id of registration to show
        """

        url = self.url + id
        return self.api.get(url).json()

    def add(self, url, regex_filter=None, headers=None):
        """Add a webhook to the DB


        :param url: url to register in the DB
        :param regex_filter: a optional regular expression dict to filter
        alarms
        :param headers: optional headers to attach to requests
        """

        params = dict(url=url, regex_filter=regex_filter,
                      headers=headers)

        return self.api.post(self.url, json=params).json()

    def delete(self, id):
        """delete a webhook from the DB


        :param id: id of webhook to delete
        """

        url = self.url + id

        return self.api.delete(url).json()
