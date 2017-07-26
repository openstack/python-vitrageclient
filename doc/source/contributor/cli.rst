..
      Licensed under the Apache License, Version 2.0 (the "License"); you may
      not use this file except in compliance with the License. You may obtain
      a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

      Unless required by applicable law or agreed to in writing, software
      distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
      License for the specific language governing permissions and limitations
      under the License.



================
Command-line API
================
Installing this distribution gets you a shell command, ``vitrage``, that you
can use to interact with the Vitrage API server.

Usage:
  vitrage

  vitrage help

  vitrage help <command>


Environmental Variables
-----------------------

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
     alarm list     List alarms on entity
     complete       print bash completion command
     help           print detailed help for another command
     rca show       Show an RCA
     resource list  List resources
     resource show  Show a resource
     topology show  Show the topology of the system


Bash Completion
---------------
Basic command tab completion can be enabled by sourcing the bash completion script.
::

  source /usr/local/share/vitrage.bash_completion


Topology Example
----------------
Note:  To see complete usage: 'vitrage help' and 'vitrage help <command>'

topology show::

 {
  "directed": true,
  "graph": {},
  "nodes": [
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "vm-8",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "ACTIVE",
      "project_id": "0683517e1e354d2ba25cba6937f44e79",
      "type": "nova.instance",
      "id": "20d12a8a-ea9a-89c6-5947-83bea959362e",
      "vitrage_id": "RESOURCE:nova.instance:20d12a8a-ea9a-89c6-5947-83bea959362e"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "vm-2",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "ACTIVE",
      "project_id": "0683517e1e354d2ba25cba6937f44e79",
      "type": "nova.instance",
      "id": "dc35fa2f-4515-1653-ef6b-03b471bb395b",
      "vitrage_id": "RESOURCE:nova.instance:dc35fa2f-4515-1653-ef6b-03b471bb395b"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "vm-13",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "ACTIVE",
      "project_id": "0683517e1e354d2ba25cba6937f44e79",
      "type": "nova.instance",
      "id": "9879cf5a-bdcf-3651-3017-961ed887ec86",
      "vitrage_id": "RESOURCE:nova.instance:9879cf5a-bdcf-3651-3017-961ed887ec86"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "vm-10",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "ACTIVE",
      "project_id": "0683517e1e354d2ba25cba6937f44e79",
      "type": "nova.instance",
      "id": "fe124f4b-9ed7-4591-fcd1-803cf5c33cb1",
      "vitrage_id": "RESOURCE:nova.instance:fe124f4b-9ed7-4591-fcd1-803cf5c33cb1"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "vm-11",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "ACTIVE",
      "project_id": "0683517e1e354d2ba25cba6937f44e79",
      "type": "nova.instance",
      "id": "f2e48a97-7350-061e-12d3-84c6dc3e67c0",
      "vitrage_id": "RESOURCE:nova.instance:f2e48a97-7350-061e-12d3-84c6dc3e67c0"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "host-2",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "available",
      "type": "nova.host",
      "id": "host-2",
      "vitrage_id": "RESOURCE:nova.host:host-2"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "host-3",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "available",
      "type": "nova.host",
      "id": "host-3",
      "vitrage_id": "RESOURCE:nova.host:host-3"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "host-0",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "available",
      "type": "nova.host",
      "id": "host-0",
      "vitrage_id": "RESOURCE:nova.host:host-0"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "host-1",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "available",
      "type": "nova.host",
      "id": "host-1",
      "vitrage_id": "RESOURCE:nova.host:host-1"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "vm-9",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "ACTIVE",
      "project_id": "0683517e1e354d2ba25cba6937f44e79",
      "type": "nova.instance",
      "id": "275097cf-954e-8e24-b185-9514e24b8591",
      "vitrage_id": "RESOURCE:nova.instance:275097cf-954e-8e24-b185-9514e24b8591"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "vm-1",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "ACTIVE",
      "project_id": "0683517e1e354d2ba25cba6937f44e79",
      "type": "nova.instance",
      "id": "a0f0805f-c804-cffe-c25a-1b38f555ed68",
      "vitrage_id": "RESOURCE:nova.instance:a0f0805f-c804-cffe-c25a-1b38f555ed68"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "vm-14",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "ACTIVE",
      "project_id": "0683517e1e354d2ba25cba6937f44e79",
      "type": "nova.instance",
      "id": "56af57d2-34a4-19b1-5106-b613637a11a7",
      "vitrage_id": "RESOURCE:nova.instance:56af57d2-34a4-19b1-5106-b613637a11a7"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "zone-1",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "available",
      "type": "nova.zone",
      "id": "zone-1",
      "vitrage_id": "RESOURCE:nova.zone:zone-1"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "vm-3",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "ACTIVE",
      "project_id": "0683517e1e354d2ba25cba6937f44e79",
      "type": "nova.instance",
      "id": "16e14c58-d254-2bec-53e4-c766e48810aa",
      "vitrage_id": "RESOURCE:nova.instance:16e14c58-d254-2bec-53e4-c766e48810aa"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "vm-7",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "ACTIVE",
      "project_id": "0683517e1e354d2ba25cba6937f44e79",
      "type": "nova.instance",
      "id": "f35a1e10-74ff-7332-8edf-83cd6ffcb2de",
      "vitrage_id": "RESOURCE:nova.instance:f35a1e10-74ff-7332-8edf-83cd6ffcb2de"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "vm-4",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "ACTIVE",
      "project_id": "0683517e1e354d2ba25cba6937f44e79",
      "type": "nova.instance",
      "id": "ea8a450e-cab1-2272-f431-494b40c5c378",
      "vitrage_id": "RESOURCE:nova.instance:ea8a450e-cab1-2272-f431-494b40c5c378"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "vm-6",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "ACTIVE",
      "project_id": "0683517e1e354d2ba25cba6937f44e79",
      "type": "nova.instance",
      "id": "6e42bdc3-b776-1b2c-2c7d-b7a8bb98f721",
      "vitrage_id": "RESOURCE:nova.instance:6e42bdc3-b776-1b2c-2c7d-b7a8bb98f721"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "vm-5",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "ACTIVE",
      "project_id": "0683517e1e354d2ba25cba6937f44e79",
      "type": "nova.instance",
      "id": "8c951613-c660-87c0-c18b-0fa3293ce8d8",
      "vitrage_id": "RESOURCE:nova.instance:8c951613-c660-87c0-c18b-0fa3293ce8d8"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "zone-0",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "available",
      "type": "nova.zone",
      "id": "zone-0",
      "vitrage_id": "RESOURCE:nova.zone:zone-0"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "vm-0",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "ACTIVE",
      "project_id": "0683517e1e354d2ba25cba6937f44e79",
      "type": "nova.instance",
      "id": "78353ce4-2710-49b5-1341-b8cbb6000ebc",
      "vitrage_id": "RESOURCE:nova.instance:78353ce4-2710-49b5-1341-b8cbb6000ebc"
    },TODO
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "vm-12",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "state": "ACTIVE",
      "project_id": "0683517e1e354d2ba25cba6937f44e79",
      "type": "nova.instance",
      "id": "35bf479a-75d9-80a9-874e-d3b50fb2dd2e",
      "vitrage_id": "RESOURCE:nova.instance:35bf479a-75d9-80a9-874e-d3b50fb2dd2e"
    },
    {
      "category": "RESOURCE",
      "is_placeholder": false,
      "is_deleted": false,
      "name": "openstack.node",
      "type": "openstack.node",
      "id": "openstack.node",
      "vitrage_id": "RESOURCE:openstack.node"
    }
  ],
  "links": [
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 3,
      "key": "contains",
      "source": 5
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 1,
      "key": "contains",
      "source": 5
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 16,
      "key": "contains",
      "source": 5
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 11,
      "key": "contains",
      "source": 5
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 13,
      "key": "contains",
      "source": 6
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 4,
      "key": "contains",
      "source": 6
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 14,
      "key": "contains",
      "source": 6
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 20,
      "key": "contains",
      "source": 7
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 0,
      "key": "contains",
      "source": 7
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 19,
      "key": "contains",
      "source": 7
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 15,
      "key": "contains",
      "source": 7
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 9,
      "key": "contains",
      "source": 8
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 10,
      "key": "contains",
      "source": 8
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 2,
      "key": "contains",
      "source": 8
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 17,
      "key": "contains",
      "source": 8
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 6,
      "key": "contains",
      "source": 12
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 8,
      "key": "contains",
      "source": 12
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 5,
      "key": "contains",
      "source": 18
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 7,
      "key": "contains",
      "source": 18
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 18,
      "key": "contains",
      "source": 21
    },
    {
      "relationship_name": "contains",
      "is_deleted": false,
      "target": 12,
      "key": "contains",
      "source": 21
    }
  ],
  "multigraph": true
 }

RCA Example
-----------
Note:  To see complete usage: 'vitrage help' and 'vitrage help <command>'

rca show::

  vitrage rca show

  {
  "directed": true,
  "graph": {

  },
  "nodes": [
    {
      "category": "ALARM",
      "type": "nagios",
      "name": "CPU load",
      "state": "Active",
      "severity": "WARNING",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "info": "WARNING - 15min load 1.66 at 32 CPUs",
      "resource_type": "nova.host",
      "resource_name": "host-0",
      "resource_id": "host-0",
      "id": 0,
      "vitrage_id": "ALARM:nagios:host0:CPU load"
    },
    {
      "category": "ALARM",
      "type": "vitrage",
      "name": "Machine Suboptimal",
      "state": "Active",
      "severity": "WARNING",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "resource_type": "nova.instance",
      "resource_name": "vm0",
      "resource_id": "20d12a8a-ea9a-89c6-5947-83bea959362e",
      "id": 1,
      "vitrage_id": "ALARM:vitrage:vm0:Machine Suboptimal"
    },
    {
      "category": "ALARM",
      "type": "vitrage",
      "name": "Machine Suboptimal",
      "state": "Active",
      "severity": "WARNING",
      "update_timestamp": "2015-12-01T12:46:41Z",
      "resource_type": "nova.instance",
      "resource_name": "vm1",
      "resource_id": "275097cf-954e-8e24-b185-9514e24b8591",
      "id": 2,
      "vitrage_id": "ALARM:vitrage:vm1:Machine Suboptimal"
    }
  ],
  "links": [
    {
      "source": 0,
      "target": 1,
      "relationship": "causes"
    },
    {
      "source": 0,
      "target": 2,
      "relationship": "causes"
    }
  ],
  "multigraph": false,
  "inspected_index": 0
  }


Resources Examples
------------------
Note:  To see complete usage: 'vitrage help' and 'vitrage help <command>'

resource show::

 vitrage resource show

 TODO

resource list::

  vitrage resource list

  TODO

Alarms Examples
---------------
Note:  To see complete usage: 'vitrage help' and 'vitrage help <command>'

alarm list::

  vitrage alarm list
  +---------+--------------------+---------------+--------------------------------------+----------+----------------------+
  | type    | name               | resource_type | resource_id                          | severity | update_timestamp     |
  +---------+--------------------+---------------+--------------------------------------+----------+----------------------+
  | nagios  | CPU load           | nova.host     | host-0                               | WARNING  | 2015-12-01T12:46:41Z |
  | vitrage | Machine Suboptimal | nova.instance | 20d12a8a-ea9a-89c6-5947-83bea959362e | WARNING  | 2015-12-01T12:46:41Z |
  | vitrage | Machine Suboptimal | nova.instance | 275097cf-954e-8e24-b185-9514e24b8591 | WARNING  | 2015-12-01T12:46:41Z |
  | aodh    | Memory overload    | nova.host     | host-0                               | WARNING  | 2015-12-01T12:46:41Z |
  +---------+--------------------+---------------+--------------------------------------+----------+----------------------+

Python API
----------

There's also a complete Python API.

In order to use the python api directly, you can pass in the credentials using
the keystoneauth1 client library

Start using the vitrageclient API by constructing the vitrageclient client
.Client class.
The Client class is used to call all vitrage-api commands

The api_version matches the version of the Vitrage API.  Currently it is 'v1_0'.


Example::

  from vitrageclient import client
  from keystoneauth1.identity.generic.password import Password
  from keystoneauth1.session import Session

  auth = Password(auth_url='http://135.248.18.224:5000/v2.0',
  username='admin',password='password',project_name='admin')
  session = Session(auth=auth,timeout=600)
  myclient = client.Client('1',session=session)
  myclient.topology.get()

