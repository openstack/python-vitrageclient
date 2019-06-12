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

    def versions(self):
        """Get templates versions"""
        return self.api.get(self.url + 'versions').json()

    def show(self, _id):
        """Show template content"""

        url = self.url + _id
        return self.api.get(url).json()

    def add(self, path=None, template_type=None,
            params=None, template_str=None, overwrite=False):
        """Add a new template

        :param path: (optional) The template file path or templates dir path
        :param template_type: (optional) The template type, in case it is not
        written inside the template metadata section
        :param params: (optional) Actual values for the template parameters
        :param template_str: (optional) A string representation of the template
        :param overwrite: (optional) overwrite the template if exists
        yaml
        Either path or template_str must exist (but not both)

        :return:
        """
        files_content = \
            self._load_template(path=path, template_str=template_str)
        api_params = dict(templates=files_content,
                          template_type=template_type,
                          params=params, overwrite=overwrite)
        return self.api.put(self.url, json=api_params).json()

    def delete(self, ids):
        """Delete existing"""
        params = dict(id=ids)
        return self.api.delete(self.url, json=params).json()

    def validate(self, path=None, template_type=None,
                 params=None, template_str=None):
        """Template validation

        Make sure that the template file is correct in terms of syntax
        and content.
        It is possible to pass a specific file path in order to validate one
        template, or directory path for validation of several templates (the
        directory must contain only templates)

        :param path: (optional) The template file path or templates dir path
        :param template_type: (optional) The template type, in case it is not
        written inside the template metadata section
        :param params: (optional) Actual values for the template parameters
        :param template_str: (optional) A string representation of the template
        yaml
        Either path or template_str must exist (but not both)

        :return:
        """
        files_content = \
            self._load_template(path=path, template_str=template_str)
        api_params = dict(templates=files_content,
                          template_type=template_type,
                          params=params)
        return self.api.post(self.url, json=api_params).json()

    @classmethod
    def _load_yaml_files(cls, path):
        if os.path.isdir(path):

            files_content = []
            for file_name in os.listdir(path):

                file_path = '%s/%s' % (path, file_name)
                if os.path.isfile(file_path):
                    template = cls._load_yaml_file(file_path)
                    files_content.append((file_path, template))
        else:
            files_content = [(path, cls._load_yaml_file(path))]

        return files_content

    @classmethod
    def _load_yaml_file(cls, path):
        with open(path, 'r') as stream:
            return cls._load_yaml(stream)

    @classmethod
    def _load_yaml(cls, yaml_content):
        try:
            return yaml_utils.load(yaml_content)
        except ValueError as e:
            message = 'Could not load template: %s. Reason: %s' \
                      % (yaml_content, e)
            raise exc.CommandError(message)

    @classmethod
    def _load_template(cls, path, template_str):
        if path:
            files_content = cls._load_yaml_files(path)
        elif template_str:
            files_content = [(None, cls._load_yaml(template_str))]
        else:
            raise exc.CommandError(
                'Add template API must be called with either \'path\' or '
                '\'template_str\'')

        return files_content
