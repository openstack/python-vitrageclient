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


"""
Vitrage command line interface
"""

from __future__ import print_function

from cliff import app
from cliff import commandmanager

import sys
from v1 import topology
from vitrageclient import __version__


class VitrageCommandManager(commandmanager.CommandManager):
    COMMANDS = {
        "topology list": topology.TopologyList,
        "topology show": topology.TopologyShow,
    }

    def load_commands(self, namespace):
        for k, v in self.COMMANDS.items():
            self.add_command(k, v)


class VitrageShell(app.App):
    def __init__(self):
        super(VitrageShell, self).__init__(
            description=__doc__,
            version=__version__,
            command_manager=VitrageCommandManager(None),
            deferred_help=True,
        )

    def run(self, args):
        pass


def main(args=None):
    try:
        if args is None:
            args = sys.argv[1:]
        return VitrageShell().run(args)
    except KeyboardInterrupt:
        print("... terminating vitrage client", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
