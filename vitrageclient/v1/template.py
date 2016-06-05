# Copyright 2016 - Nokia Corporation
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
import os
from vitrageclient.common.exc import CommandException
from vitrageclient.common import yaml_utils


class Template(object):

    URL = 'v1/template/'

    def __init__(self, api):
        self.api = api

    def validate(self, path=None):
        """Template validation

        :param path: the YAML file path
        """

        if os.path.isdir(path):
            pass
        else:
            template_def = self.load_template_definition(path)

        params = dict(template_def=template_def)

        return self.api.post(self.URL, json=params).json()

    @staticmethod
    def load_template_definition(path):

        with open(path, 'r') as stream:
            try:
                return yaml_utils.load(stream)
            except ValueError as e:
                message = 'Could not load template. Reason: %s' % e.message
                raise CommandException(message=message)
