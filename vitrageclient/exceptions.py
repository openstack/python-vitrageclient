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
import json


class CommandError(Exception):
    pass


class ClientException(Exception):
    """The base exception class for all exceptions this library raises."""
    message = 'Unknown Error'

    # noinspection PyMissingConstructor
    def __init__(self, code, message=None, request_id=None,
                 url=None, method=None):
        self.code = code
        self.message = message or self.__class__.message
        self.request_id = request_id
        self.url = url
        self.method = method

    def __str__(self):
        formatted_string = '%s (HTTP %s)' % (self.message, self.code)
        if self.request_id:
            formatted_string += ' (Request-ID: %s)' % self.request_id

        return formatted_string


def from_response(resp, url, method):
    msg = None
    if resp.text:
        try:
            body = json.loads(resp.text)
            msg = body.get('description', None)
        except Exception as e:
            print('get msg failed, resp.text:%s, e:%s ' % (resp.text, e))

    return ClientException(resp.status_code, message=msg,
                           url=url, method=method)
