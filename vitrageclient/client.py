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

from vitrageclient import exceptions as exc

from keystoneauth1 import adapter as keystoneauth
from oslo_utils import importutils

profiler_web = importutils.try_import('osprofiler.web')


# noinspection PyPep8Naming
def Client(version, *args, **kwargs):
    module = importutils.import_versioned_module('vitrageclient',
                                                 version, 'client')
    client_class = getattr(module, 'Client')
    return client_class(*args, **kwargs)


class VitrageClient(keystoneauth.Adapter):
    def request(self, url, method, **kwargs):
        headers = kwargs.setdefault('headers', {})
        headers.setdefault('Accept', 'application/json')

        if profiler_web:
            # no header will be added if profiler is not initialized
            headers.update(profiler_web.get_trace_id_headers())

        raise_exc = kwargs.pop('raise_exc', True)
        resp = super(VitrageClient, self).request(url, method,
                                                  raise_exc=False,
                                                  **kwargs)

        if raise_exc and resp.status_code >= 400:
            raise exc.from_response(resp, url, method)
        return resp
