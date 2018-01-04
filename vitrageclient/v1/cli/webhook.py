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

from cliff import lister
from cliff import show

from vitrageclient.common import utils


# noinspection PyAbstractClass
class WebhookShow(show.ShowOne):
    """Show a webhook destination with "id" """

    def get_parser(self, prog_name):
        parser = super(WebhookShow, self).get_parser(prog_name)
        parser.add_argument('id', help='id of webhook to show')
        return parser

    def take_action(self, parsed_args):
        id = parsed_args.id
        post_registration = utils.get_client(self).webhook.show(id=id)
        return self.dict2columns(post_registration)


class WebhookList(lister.Lister):
    """List all webhook destinations in DB"""

    POST_PROPS = \
        ('created_at', 'id', 'url', 'headers', 'regex_filter')

    def get_parser(self, prog_name):
        parser = super(WebhookList, self).get_parser(prog_name)

        return parser

    def take_action(self, parsed_args):
        post_registrations = utils.get_client(self).webhook.list()

        return utils.list2cols(self.POST_PROPS, post_registrations)


class WebhookAdd(show.ShowOne):
    """Add a new webhook registration to DB"""
    def get_parser(self, prog_name):
        parser = super(WebhookAdd, self).get_parser(prog_name)
        parser.add_argument('--url',
                            required=True,
                            help='url to post to'
                            )
        parser.add_argument('--regex_filter',
                            required=False,
                            help='a regular expression json specifying alarm '
                                 'filters'
                            )
        parser.add_argument('--headers',
                            required=False,
                            help='json to be included in the request header'
                            )

        return parser

    def take_action(self, parsed_args):
        result = utils.get_client(self).webhook.add(
            url=parsed_args.url,
            regex_filter=parsed_args.regex_filter,
            headers=parsed_args.headers)

        return self.dict2columns(result)


class WebhookDelete(show.ShowOne):
    """Delete a webhook destination with "id" """

    def get_parser(self, prog_name):
        parser = super(WebhookDelete, self).get_parser(prog_name)
        parser.add_argument('id', help='id of webhook to delete')
        return parser

    def take_action(self, parsed_args):
        id = parsed_args.id
        result = utils.get_client(self).webhook.delete(id=id)
        return self.dict2columns(result)
