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

from vitrageclient.exc import ClientException


class HealthCheck(object):
    URL = 'healthcheck/'
    STATUS_CODE_OK = 200

    def __init__(self, api):
        self.api = api

    def get(self):
        """Get healthcheck result"""
        try:
            resp = self.api.get(self.URL)
        except ClientException as e:
            return {"passed": False,
                    "message": e.message,
                    "url": e.url,
                    "status_code": e.code}

        return {"passed": resp.status_code == self.STATUS_CODE_OK,
                "status_code": resp.status_code}
