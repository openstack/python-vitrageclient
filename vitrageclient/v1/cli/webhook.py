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
    """Show a webhook """

    def get_parser(self, prog_name):
        parser = super(WebhookShow, self).get_parser(prog_name)
        parser.add_argument('id', help='id of webhook to show')
        return parser

    def take_action(self, parsed_args):
        id = parsed_args.id
        webhook = utils.get_client(self).webhook.show(id=id)
        return self.dict2columns(webhook)


class WebhookList(lister.Lister):
    """List all webhooks in the database"""

    POST_PROPS = \
        (
            ('ID', 'id'),
            ('Created At', 'created_at'),
            ('Project ID', 'project_id'),
            ('URL', 'url'),
            ('Headers', 'headers'),
            ('Filter', 'regex_filter')
        )

    def get_parser(self, prog_name):
        parser = super(WebhookList, self).get_parser(prog_name)
        parser.add_argument('--all-tenants',
                            default=False,
                            dest='all_tenants',
                            action='store_true',
                            help='Shows webhooks of all the tenants')
        return parser

    def take_action(self, parsed_args):
        all_tenants = parsed_args.all_tenants
        webhooks = utils.get_client(self).webhook.list(all_tenants=all_tenants)

        return utils.list2cols_with_rename(self.POST_PROPS, webhooks)


class WebhookAdd(show.ShowOne):
    """Add a new webhook to the database"""
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
    """Delete a webhook """

    def get_parser(self, prog_name):
        parser = super(WebhookDelete, self).get_parser(prog_name)
        parser.add_argument('id', help='id of webhook to delete')
        return parser

    def take_action(self, parsed_args):
        id = parsed_args.id
        result = utils.get_client(self).webhook.delete(id=id)
        return self.dict2columns(result)
