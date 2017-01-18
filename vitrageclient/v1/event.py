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


class Event(object):
    URL = 'v1/event/'

    def __init__(self, api):
        self.api = api

    def post(self, event_time, event_type, details):
        """Post an event """

        params = dict(time=event_time,
                      type=event_type,
                      details=details)
        self.api.post(self.URL, json=params)
