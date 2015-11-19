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

from v1 import topology
from vitrageclient import client


class Client(object):
    DEFAULT_HEADERS = {
        "Accept": "application/json",
    }

    def __init__(self, session=None, service_type='rca', **kwargs):
        self._set_default_headers(kwargs)
        self._api = client.VitrageClient(session, service_type=service_type,
                                         **kwargs)
        self.topology = topology.Topology(self._api)

    def _set_default_headers(self, kwargs):
        headers = kwargs.get('headers', {})
        for k, v in self.DEFAULT_HEADERS.items():
            if k not in headers:
                headers[k] = v
        kwargs['headers'] = headers
        return kwargs
