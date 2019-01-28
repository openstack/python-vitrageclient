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

from vitrageclient.common import yaml_utils
from vitrageclient import exceptions as exc


class Template(object):

    url = 'v1/template/'

    def __init__(self, api):
        self.api = api

    def list(self):
        """Get templates list"""
        return self.api.get(self.url).json()

    def show(self, uuid):
        """Show template content"""

        url = self.url + uuid
        return self.api.get(url).json()

    def add(self, path, template_type=None, params=None):
        """Add a new template"""

        files_content = self._load_yaml_files(path)
        api_params = dict(templates=files_content,
                          template_type=template_type,
                          params=params)
        return self.api.put(self.url, json=api_params).json()

    def delete(self, uuid):
        """Delete existing"""
        params = dict(uuid=uuid)
        return self.api.delete(self.url, json=params).json()

    def validate(self, path, template_type=None, params=None):
        """Template validation

        Make sure that the template file is correct in terms of syntax
        and content.
        It is possible to pass a specific file path in order to validate one
        template, or directory path for validation of several templates (the
        directory must contain only templates)

        :param path: the template file path or templates dir path
        :param template_type: type of templates ('standard','definition',...)
        :param params: (optional) actual values for the template parameters
        """

        files_content = self._load_yaml_files(path)
        api_params = dict(templates=files_content,
                          template_type=template_type,
                          params=params)
        return self.api.post(self.url, json=api_params).json()

    def _load_yaml_files(self, path):
        if os.path.isdir(path):

            files_content = []
            for file_name in os.listdir(path):

                file_path = '%s/%s' % (path, file_name)
                if os.path.isfile(file_path):
                    template = self._load_yaml_file(file_path)
                    files_content.append((file_path, template))
        else:
            files_content = [(path, self._load_yaml_file(path))]

        return files_content

    @staticmethod
    def _load_yaml_file(path):

        with open(path, 'r') as stream:
            try:
                return yaml_utils.load(stream)
            except ValueError as e:
                message = 'Could not load template file: %s. Reason: %s' \
                          % (path, e.message)
                raise exc.CommandError(message)
