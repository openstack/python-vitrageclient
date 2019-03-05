# Copyright 2019 - Nokia
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

import mock
from oslotest import base

from vitrageclient import exceptions as exc
from vitrageclient.tests.utils import get_resources_dir
from vitrageclient.v1.template import Template

TEMPLATE_STRING = """
metadata:
 version: 3
 name: template1
 description: simple template
 type: standard
entities:
 alarm:
  name: cpu problem
 host:
  type: nova.host
scenarios:
 - condition: alarm [ on ] host
   actions:
     - set_state:
        state: ERROR
        target: host
"""


class TestTemplate(base.BaseTestCase):

    def test_validate_by_path(self):
        template_path = get_resources_dir() + '/template1.yaml'
        template = Template(mock.Mock())
        template.validate(path=template_path)

    def test_validate_by_nonexisting_path(self):
        template = Template(mock.Mock())
        self.assertRaises(IOError, template.validate,
                          path='non_existing_template_path.yaml')

    def test_validate_by_template(self):
        template = Template(mock.Mock())
        template.validate(template_str=TEMPLATE_STRING)

    def test_validate_by_nothing(self):
        template = Template(mock.Mock())
        self.assertRaises(exc.CommandError, template.validate)

    def test_add_by_path(self):
        template_path = get_resources_dir() + '/template1.yaml'
        template = Template(mock.Mock())
        template.add(path=template_path)

    def test_add_by_nonexisting_path(self):
        template = Template(mock.Mock())
        self.assertRaises(IOError, template.add,
                          path='non_existing_template_path.yaml')

    def test_add_by_template(self):
        template = Template(mock.Mock())
        template.add(template_str=TEMPLATE_STRING)

    def test_add_by_nothing(self):
        template = Template(mock.Mock())
        self.assertRaises(exc.CommandError, template.add)
