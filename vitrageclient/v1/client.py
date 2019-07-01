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
import logging

from vitrageclient import client

from vitrageclient.v1 import alarm
from vitrageclient.v1 import event
from vitrageclient.v1 import healthcheck
from vitrageclient.v1 import rca
from vitrageclient.v1 import resource
from vitrageclient.v1 import service
from vitrageclient.v1 import status
from vitrageclient.v1 import template
from vitrageclient.v1 import topology
from vitrageclient.v1 import webhook


class Client(object):

    def __init__(self, session=None, service_type='rca', **kwargs):
        logger = logging.getLogger(__name__)
        self._api = client.VitrageClient(session, service_type=service_type,
                                         logger=logger, **kwargs)
        self.topology = topology.Topology(self._api)
        self.resource = resource.Resource(self._api)
        self.alarm = alarm.Alarm(self._api)
        self.rca = rca.Rca(self._api)
        self.template = template.Template(self._api)
        self.event = event.Event(self._api)
        self.healthcheck = healthcheck.HealthCheck(self._api)
        self.webhook = webhook.Webhook(self._api)
        self.service = service.Service(self._api)
        self.status = status.Status(self._api)
