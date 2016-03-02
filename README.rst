Python bindings to the Vitrage API
==================================

This is a client library for Vitrage built to interface with the Vitrage API
. It
provides a Python API (the ``vitrageclient`` module) and a command-line tool
(``vitrage``).


.. contents:: Contents:
   :local:

Ubuntu Install
--------------
Requires:
  - pip - version >= 1.4.  python get-pip.py

See versions on PYPI:
  https://pypi.python.org/pypi/python-vitrageclient/

Install It:
  - sudo pip install python-vitrageclient

Alternative Manual Install Steps:
  - cd to your python-vitrageclient repo
  - sudo pip install -r requirements.txt
  - python setup.py install

Building and Packaging
----------------------
Install the tool dependencies
    sudo apt-get install python-pip python-virtualenv

In the python-vitrageclient source directory
    virtualenv --no-site-packages .venv

    source ./.venv/bin/activate

    pip install wheel

    python setup.py bdist_wheel

    pip install $(ls -1rt dist/*.whl | tail -1) --upgrade

Command-line API
----------------
Installing this distribution gets you a shell command, ``vitrage``, that you
can use to interact with the Vitrage API server.

Usage:
  vitrage

  vitrage help

  vitrage help <command>


Environmental Variables
~~~~~~~~~~~~~~~~~~~~~~~

Environmental variables can be sourced, or optionally passed in as CLI arguments.
It is easiest to source them first and then use the CLI.

When using Keystone to obtain the token and endpoint::

  export OS_USERNAME=
  export OS_PASSWORD=
  export OS_USER_DOMAIN_NAME=
  export OS_PROJECT_NAME=
  export OS_AUTH_URL=
  export OS_REGION_NAME=

When OS_USER_DOMAIN_NAME is not set, then 'Default' is assumed. Alternatively IDs can be used instead of names.

You'll find complete documentation on the shell by running
``vitrage help``::

  usage: vitrage [--version] [-v | -q] [--log-file LOG_FILE] [-h] [--debug]
               [--os-region-name <auth-region-name>]
               [--os-interface <interface>] [--insecure]
               [--os-cacert <ca-certificate>] [--os-cert <certificate>]
               [--os-key <key>] [--timeout <seconds>] [--os-auth-type <name>]
               [--os-auth-url OS_AUTH_URL] [--os-domain-id OS_DOMAIN_ID]
               [--os-domain-name OS_DOMAIN_NAME]
               [--os-project-id OS_PROJECT_ID]
               [--os-project-name OS_PROJECT_NAME]
               [--os-project-domain-id OS_PROJECT_DOMAIN_ID]
               [--os-project-domain-name OS_PROJECT_DOMAIN_NAME]
               [--os-trust-id OS_TRUST_ID]
               [--os-default-domain-id OS_DEFAULT_DOMAIN_ID]
               [--os-default-domain-name OS_DEFAULT_DOMAIN_NAME]
               [--os-user-id OS_USER_ID] [--os-user-name OS_USERNAME]
               [--os-user-domain-id OS_USER_DOMAIN_ID]
               [--os-user-domain-name OS_USER_DOMAIN_NAME]
               [--os-password OS_PASSWORD]
               [--vitrage-api-version VITRAGE_API_VERSION]

   Vitrage command line interface

   optional arguments:
     --version             show program's version number and exit
     -v, --verbose         Increase verbosity of output. Can be repeated.
     -q, --quiet           Suppress output except warnings and errors.
     --log-file LOG_FILE   Specify a file to log output. Disabled by default.
     -h, --help            Show help message and exit.
     --debug               Show tracebacks on errors.
     --os-region-name <auth-region-name>
                           Authentication region name (Env: OS_REGION_NAME)
     --os-interface <interface>
                           Select an interface type. Valid interface types:
                           [admin, public, internal]. (Env: OS_INTERFACE)
     --os-auth-type <name>, --os-auth-plugin <name>
                           Authentication type to use
     --vitrage-api-version VITRAGE_API_VERSION
                           Defaults to env[VITRAGE_API_VERSION] or 1.

   API Connection Options:
     Options controlling the HTTP API Connections

     --insecure            Explicitly allow client to perform "insecure" TLS
                           (https) requests. The server's certificate will not be
                           verified against any certificate authorities. This
                           option should be used with caution.
     --os-cacert <ca-certificate>
                           Specify a CA bundle file to use in verifying a TLS
                           (https) server certificate. Defaults to
                           env[OS_CACERT].
     --os-cert <certificate>
                           Defaults to env[OS_CERT].
     --os-key <key>        Defaults to env[OS_KEY].
     --timeout <seconds>   Set request timeout (in seconds).

   Authentication Options:
     Options specific to the password plugin.

     --os-auth-url OS_AUTH_URL
                           Authentication URL
     --os-domain-id OS_DOMAIN_ID
                           Domain ID to scope to
     --os-domain-name OS_DOMAIN_NAME
                           Domain name to scope to
     --os-project-id OS_PROJECT_ID, --os-tenant-id OS_PROJECT_ID
                           Project ID to scope to
     --os-project-name OS_PROJECT_NAME, --os-tenant-name OS_PROJECT_NAME
                           Project name to scope to
     --os-project-domain-id OS_PROJECT_DOMAIN_ID
                           Domain ID containing project
     --os-project-domain-name OS_PROJECT_DOMAIN_NAME
                           Domain name containing project
     --os-trust-id OS_TRUST_ID
                           Trust ID
     --os-default-domain-id OS_DEFAULT_DOMAIN_ID
                           Optional domain ID to use with v3 and v2 parameters.
                           It will be used for both the user and project domain
                           in v3 and ignored in v2 authentication.
     --os-default-domain-name OS_DEFAULT_DOMAIN_NAME
                           Optional domain name to use with v3 API and v2
                           parameters. It will be used for both the user and
                           project domain in v3 and ignored in v2 authentication.
     --os-user-id OS_USER_ID
                           User id
     --os-user-name OS_USERNAME, --os-username OS_USERNAME
                           Username
     --os-user-domain-id OS_USER_DOMAIN_ID
                           User's domain id
     --os-user-domain-name OS_USER_DOMAIN_NAME
                           User's domain name
     --os-password OS_PASSWORD
                           User's password

   Commands:
     alarms list    List alarms on entity
     complete       print bash completion command
     help           print detailed help for another command
     rca show       Show an RCA
     resource list  List resources
     resource show  Show a resource
     topology show  Show the topology of the system


Bash Completion
~~~~~~~~~~~~~~~
Basic command tab completion can be enabled by sourcing the bash completion script.
::

  source /usr/local/share/vitrage.bash_completion


Topology Example
~~~~~~~~~~~~~~~~
Note:  To see complete usage: 'vitrage help' and 'vitrage help <command>'

topology show::

  TODO


RCA Example
~~~~~~~~~~~
Note:  To see complete usage: 'vitrage help' and 'vitrage help <command>'

rca show::

  vitrage rca show

  TODO



Resources Examples
~~~~~~~~~~~~~~~~~~
Note:  To see complete usage: 'vitrage help' and 'vitrage help <command>'

resource show::

 vitrage resource show

 TODO

resource list::

  vitrage resource list

  TODO

Alarms Examples
~~~~~~~~~~~~~~~
Note:  To see complete usage: 'vitrage help' and 'vitrage help <command>'

alarms list::

  vitrage alarms list
  TODO

Python API
----------

There's also a complete Python API.

In order to use the python api directly, you must pass in a valid auth token and
vitrage api endpoint, or you can pass in the credentials required by the
keystone client and let the Python API do the authentication.  The user can obtain the token
and endpoint using the keystone client api:
http://docs.openstack.org/developer/python-keystoneclient/.
The service catalog name for our API endpoint is "rca".

Start using the vitrageclient API by constructing the vitrageclient client
.Client class.
The Client class is used to call all vitrage-api commands

The api_version matches the version of the Vitrage API.  Currently it is 'v1_0'.


Example::

  TODO




License
-------

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied.
See the License for the specific language governing permissions and
limitations under the License.
