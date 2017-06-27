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

import argparse

from oslotest import base


class CliTestCase(base.BaseTestCase):

    """Test case base class for all unit tests."""

    # original error method of argparse uses exit
    # I just want to raise an exception and get the error message
    # that exit outputs
    @staticmethod
    def _my_parser_error_func(message):
        raise argparse.ArgumentTypeError(message)
