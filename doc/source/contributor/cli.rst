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

When using Keycloak instead of Keystone use the os-auth-type ``vitrage-keycloak``
and supply username, password, realm_name, endpoint, auth_url, openid_client_id.

The parameters can be supplied in command line e.g --username,--realm-name
or as environment variables with the prefix ``VITRAGE_`` e.g ``VITRAGE_REALM_NAME``

You'll find complete documentation on the shell by running
``vitrage help``::

  vitrage help
  usage: vitrage [--version] [-v | -q] [--log-file LOG_FILE] [-h] [--debug]
               [--vitrage-api-version VITRAGE_API_VERSION]
               [--profile HMAC_KEY] [--os-region-name <auth-region-name>]
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
               [--os-user-id OS_USER_ID] [--os-username OS_USERNAME]
               [--os-user-domain-id OS_USER_DOMAIN_ID]
               [--os-user-domain-name OS_USER_DOMAIN_NAME]
               [--os-password OS_PASSWORD] [--endpoint ENDPOINT]

  Vitrage command line interface

  optional arguments:
    --version             show program's version number and exit
    -v, --verbose         Increase verbosity of output. Can be repeated.
    -q, --quiet           Suppress output except warnings and errors.
    --log-file LOG_FILE   Specify a file to log output. Disabled by default.
    -h, --help            Show help message and exit.
    --debug               Show tracebacks on errors.
    --vitrage-api-version VITRAGE_API_VERSION
                          Defaults to env[VITRAGE_API_VERSION] or 1.
    --profile HMAC_KEY    HMAC key to use for encrypting context data for
                          performance profiling of request. This key should be
                          the value of the HMAC key configured for the
                          osprofiler middleware in Vitrage api; it is specified
                          in the Vitrage configuration file
                          at"/etc/vitrage/vitrage.conf". Without the key,
                          profiling will not be triggered even if osprofiler is
                          enabled on the server side.
    --os-region-name <auth-region-name>
                          Authentication region name (Env: OS_REGION_NAME)
    --os-interface <interface>
                          Select an interface type. Valid interface types:
                          [admin, public, internal]. (Env: OS_INTERFACE)
    --os-auth-type <name>, --os-auth-plugin <name>
                          Authentication type to use
    --endpoint ENDPOINT   Vitrage endpoint (Env: VITRAGE_ENDPOINT)

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
    --os-username OS_USERNAME, --os-user-name OS_USERNAME
                          Username
    --os-user-domain-id OS_USER_DOMAIN_ID
                          User's domain id
    --os-user-domain-name OS_USER_DOMAIN_NAME
                          User's domain name
    --os-password OS_PASSWORD
                          User's password

  Commands:
    alarm count     Show a count of all alarms
    alarm list      List all alarms
    alarm show      Show an alarm
    complete        print bash completion command (cliff)
    event post      Post an event to Vitrage
    healthcheck     Check api health status
    help            print detailed help for another command (cliff)
    rca show        Show the Root Cause Analysis for a certain alarm
    resource count  Show a count of all resources
    resource list   List resources
    resource show   Show a resource
    service list    List all services
    template add    Add a template
    template delete Delete a template
    template list   List all templates
    template show   Show a template
    template validate Validate a template file
    topology show   Show the topology of the system
    webhook add     Add a new webhook to the database
    webhook delete  Delete a webhook
    webhook list    List all webhooks in the database
    webhook show    Show a webhook

Bash Completion
---------------
Basic command tab completion can be enabled by sourcing the bash completion script.
::

  source /usr/local/share/vitrage.bash_completion


Topology Example
----------------
Note:  To see complete usage: 'vitrage help' and 'vitrage help <command>'

topology show
^^^^^^^^^^^^^
::

 vitrage topology show

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

rca show
^^^^^^^^
::

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

resource list
^^^^^^^^^^^^^
::

  vitrage resource list
  +--------------------------------------+-------------------+--------------------------------------+------------+-------------------------------------------------------------------------------------------------------------------------------+
  | ID                                   | Type              | Data Source ID                       | State      | Metadata                                                                                                                      |
  +--------------------------------------+-------------------+--------------------------------------+------------+-------------------------------------------------------------------------------------------------------------------------------+
  | 786efe03-55ff-41b2-bdc1-6cd94bc355ad | nova.instance     | f3d6819a-5b52-4fae-93d4-ce58c263510b | SUBOPTIMAL | {'project_id': u'4437e14f56904650af9eef83dff35263', 'name': u'vm-0', 'update_timestamp': u'2018-01-03 09:06:06.339099+00:00'} |
  | d019ee2b-df2a-4c8f-bc59-f28a2296b0db | neutron.network   | dafa8864-a04c-4688-bab2-c6dc3ce5c31b | OK         | {'project_id': u'4437e14f56904650af9eef83dff35263', 'name': u'public', 'update_timestamp': u'2017-11-09T09:49:49Z'}           |
  | 772d627f-90d7-4c5e-8c18-6587fa5b88ee | neutron.port      | 75ff8ce5-26d9-4d77-875f-8d297918374c | OK         | {'project_id': u'4437e14f56904650af9eef83dff35263', 'update_timestamp': u'2017-11-28T11:50:23Z'}                              |
  | 4ac47cef-419f-4e4b-9590-22c10bbd21fd | nova.host         | compute-0-0                          | OK         | {'name': u'compute-0-0', 'update_timestamp': u'2018-01-03 09:06:06.851229+00:00'}                                             |
  | 99920528-2757-4fde-a2a0-3063bf0c4020 | openstack.cluster | OpenStack Cluster                    | OK         | {'name': u'openstack.cluster'}                                                                                                |
  | 374203a6-e7bc-4bd6-bc32-1137f4f3d234 | nova.zone         | nova                                 | OK         | {'name': u'nova', 'update_timestamp': u'2018-01-03 09:06:07.628148+00:00'}                                                    |
  +--------------------------------------+-------------------+--------------------------------------+------------+-------------------------------------------------------------------------------------------------------------------------------+

resource show
^^^^^^^^^^^^^
::

  vitrage resource show 786efe03-55ff-41b2-bdc1-6cd94bc355ad
  +---------------------------+--------------------------------------+
  | Field                     | Value                                |
  +---------------------------+--------------------------------------+
  | host_id                   | compute-0-0                          |
  | id                        | f3d6819a-5b52-4fae-93d4-ce58c263510b |
  | is_real_vitrage_id        | True                                 |
  | name                      | vm-0                                 |
  | project_id                | 4437e14f56904650af9eef83dff35263     |
  | state                     | ACTIVE                               |
  | update_timestamp          | 2018-01-03 09:06:06.339099+00:00     |
  | vitrage_aggregated_state  | SUBOPTIMAL                           |
  | vitrage_category          | RESOURCE                             |
  | vitrage_id                | 786efe03-55ff-41b2-bdc1-6cd94bc355ad |
  | vitrage_is_deleted        | False                                |
  | vitrage_is_placeholder    | False                                |
  | vitrage_operational_state | SUBOPTIMAL                           |
  | vitrage_sample_timestamp  | 2018-01-03 09:06:06.339099+00:00     |
  | vitrage_state             | SUBOPTIMAL                           |
  | vitrage_type              | nova.instance                        |
  +---------------------------+--------------------------------------+

resource count
^^^^^^^^^^^^^^
::

  vitrage resource count
  {
  "nova.instance": 394,
  "openstack.cluster": 1,
  "cinder.volume": 405,
  "nova.host": 16,
  "neutron.network": 7,
  "neutron.port": 1127,
  "nova.zone": 3,
  "tripleo.controller": 3
  }

  vitrage resource count --type nova.instance --group-by state
  {
  "ACTIVE": 359,
  "ERROR": 27,
  "SUBOPTIMAL": 8
  }


Service Examples
----------------
Note:  To see complete usage: 'vitrage help' and 'vitrage help <command>'

service list
^^^^^^^^^^^^

A list of all vitrage services and their status::

 vitrage service list
 +----------------------------------+------------+--------------+---------------------------+
 | Name                             | Process Id | Hostname     | Created At                |
 +----------------------------------+------------+--------------+---------------------------+
 | ApiWorker worker(0)              |      23161 | controller-1 | 2019-02-10T11:07:15+00:00 |
 | EvaluatorWorker worker(0)        |      23153 | controller-1 | 2019-02-10T11:07:15+00:00 |
 | EvaluatorWorker worker(1)        |      23155 | controller-1 | 2019-02-10T11:07:15+00:00 |
 | EvaluatorWorker worker(2)        |      23157 | controller-1 | 2019-02-10T11:07:15+00:00 |
 | EvaluatorWorker worker(3)        |      23158 | controller-1 | 2019-02-10T11:07:15+00:00 |
 | MachineLearningService worker(0) |      23366 | controller-1 | 2019-02-10T11:07:33+00:00 |
 | PersistorService worker(0)       |      23475 | controller-1 | 2019-02-10T11:07:35+00:00 |
 | SnmpParsingService worker(0)     |      23164 | controller-1 | 2019-02-10T11:07:15+00:00 |
 | vitrageuWSGI worker 1            |      25698 | controller-1 | 2019-02-10T11:14:30+00:00 |
 | vitrageuWSGI worker 2            |      25699 | controller-1 | 2019-02-10T11:14:30+00:00 |
 | VitrageNotifierService worker(0) |      23352 | controller-1 | 2019-02-10T11:07:32+00:00 |
 +----------------------------------+------------+--------------+---------------------------+


Alarms Examples
---------------
Note:  To see complete usage: 'vitrage help' and 'vitrage help <command>'

alarm list
^^^^^^^^^^

A list of all alarms (default limit of 1000 alarms)::

  vitrage alarm list
  +--------------------------------------+---------+----------------------------------------+---------------+--------------------------------------+----------+----------------------+
  | ID                                   | Type    | Name                                   | Resource Type | Resource ID                          | Severity | Update Time          |
  +--------------------------------------+---------+----------------------------------------+---------------+--------------------------------------+----------+----------------------+
  | f85ed0d2-3e28-47f9-9231-6fa72d6c882d | vitrage | VM network problem 3                   | nova.instance | 786efe03-55ff-41b2-bdc1-6cd94bc355ad | CRITICAL | 2018-01-03T07:52:06Z |
  | 868b252a-4053-431c-a6d3-7cdabd91edd8 | zabbix  | Lack of free swap space on compute-0-0 | nova.host     | 4ac47cef-419f-4e4b-9590-22c10bbd21fd | WARNING  | 2017-11-09T11:24:30Z |
  | c1ab17d4-8b6b-4d12-a4ec-3150bb89a5a5 | zabbix  | Too many processes on compute-0-0      | nova.host     | 4ac47cef-419f-4e4b-9590-22c10bbd21fd | WARNING  | 2017-11-09T11:25:12Z |
  | 7468b7f5-5a89-49ee-b408-3cfafd68290a | zabbix  | Public interface down on compute-0-0   | nova.host     | 4ac47cef-419f-4e4b-9590-22c10bbd21fd | CRITICAL | 2017-12-13T07:34:08Z |
  | 608366ed-a737-4aab-a58f-8673a589e3aa | vitrage | VM network problem 2                   | nova.instance | 786efe03-55ff-41b2-bdc1-6cd94bc355ad | CRITICAL | 2018-01-03T07:52:06Z |
  +--------------------------------------+---------+----------------------------------------+---------------+--------------------------------------+----------+----------------------+

A list of all alarms on the given resource::

  vitrage alarm list 52b466ba-ef98-4bf5-93d8-5c3ca680fe01
  +--------------------------------------+---------+---------------+---------------+--------------------------------------+----------+----------------------+
  | ID                                   | Type    | Name          | Resource Type | Resource ID                          | Severity | Update Time          |
  +--------------------------------------+---------+---------------+---------------+--------------------------------------+----------+----------------------+
  | 3c1dda08-2c95-49f1-9155-35e5512a6f38 | vitrage | Instance down | nova.instance | 52b466ba-ef98-4bf5-93d8-5c3ca680fe01 | CRITICAL | 2018-07-22T11:42:57Z |
  +--------------------------------------+---------+---------------+---------------+--------------------------------------+----------+----------------------+

A list of ``limit`` number of alarms::

  vitrage alarm list --limit 2
  +--------------------------------------+---------+---------------+---------------+--------------------------------------+----------+----------------------------+
  |  ID                                  | Type    | Name          | Resource Type | Resource ID                          | Severity | Update Time                |
  +--------------------------------------+---------+---------------+---------------+--------------------------------------+----------+----------------------------+
  | f85ed0d2-3e28-47f9-9231-6fa72d6c882d | vitrage | Instance down | nova.instance | 52b466ba-ef98-4bf5-93d8-5c3ca680fe01 | CRITICAL | 2018-07-19 14:53:24.741108 |
  | 868b252a-4053-431c-a6d3-7cdabd91edd8 | vitrage | Instance down | nova.instance | 4ac47cef-419f-4e4b-9590-22c10bbd21fd | CRITICAL | 2018-07-19 14:53:24.773490 |
  +--------------------------------------+---------+---------------+---------------+--------------------------------------+----------+----------------------------+

Paging. Get next alarms, from ``marker`` which is a vitrage_id::

  vitrage alarm list --limit 2 --marker 868b252a-4053-431c-a6d3-7cdabd91edd8
  +--------------------------------------+---------+---------------+---------------+--------------------------------------+----------+----------------------------+
  |  ID                                  | Type    | Name          | Resource Type | Resource ID                          | Severity | Update Time                |
  +--------------------------------------+---------+---------------+---------------+--------------------------------------+----------+----------------------------+
  | c1ab17d4-8b6b-4d12-a4ec-3150bb89a5a5 | vitrage | Instance down | nova.instance | 52b466ba-ef98-4bf5-93d8-5c3ca680fe01 | CRITICAL | 2018-07-19 14:53:24.801490 |
  | 7468b7f5-5a89-49ee-b408-3cfafd68290a | vitrage | Instance down | nova.instance | 4ac47cef-419f-4e4b-9590-22c10bbd21fd | CRITICAL | 2018-07-19 14:53:24.828359 |
  +--------------------------------------+---------+---------------+---------------+--------------------------------------+----------+----------------------------+

alarm history
^^^^^^^^^^^^^

A list of all alarms that were active during the time frame of ``start`` and ``end``::

  vitrage alarm history --start '2018-07-22 14:10:40.087709' --end '2018-07-23 16:10:41.354102' --limit 3
  +--------------------------------------+---------+---------------+---------------+--------------------------------------+----------+----------------------------+----------------------------+
  |  ID                                  | Type    | Name          | Resource Type | Resource ID                          | Severity | Start Time                 | End Time                   |
  +--------------------------------------+---------+---------------+---------------+--------------------------------------+----------+----------------------------+----------------------------+
  | f85ed0d2-3e28-47f9-9231-6fa72d6c882d | vitrage | Instance down | nova.instance | 4ac47cef-419f-4e4b-9590-22c10bbd21fd | CRITICAL | 2018-07-19 14:53:24.741108 | 2018-07-22 14:53:24.741108 |
  | 868b252a-4053-431c-a6d3-7cdabd91edd8 | vitrage | Instance down | nova.instance | 786efe03-55ff-41b2-bdc1-6cd94bc355ad | CRITICAL | 2018-07-19 14:53:24.773490 |                            |
  | c1ab17d4-8b6b-4d12-a4ec-3150bb89a5a5 | vitrage | Instance down | nova.instance | 52b466ba-ef98-4bf5-93d8-5c3ca680fe01 | CRITICAL | 2018-07-23 02:10:41.354102 |
  +--------------------------------------+---------+---------------+---------------+--------------------------------------+----------+----------------------------+----------------------------+

alarm show
^^^^^^^^^^
::

  vitrage alarm show f85ed0d2-3e28-47f9-9231-6fa72d6c882d
  +------------------------------+--------------------------------------+
  | Field                        | Value                                |
  +------------------------------+--------------------------------------+
  | name                         | VM network problem 3                 |
  | resource_id                  | 786efe03-55ff-41b2-bdc1-6cd94bc355ad |
  | severity                     | critical                             |
  | state                        | Active                               |
  | update_timestamp             | 2018-01-03T07:52:06Z                 |
  | vitrage_aggregated_severity  | CRITICAL                             |
  | vitrage_category             | ALARM                                |
  | vitrage_id                   | f85ed0d2-3e28-47f9-9231-6fa72d6c882d |
  | vitrage_is_deleted           | False                                |
  | vitrage_is_placeholder       | False                                |
  | vitrage_operational_severity | CRITICAL                             |
  | vitrage_resource_id          | 786efe03-55ff-41b2-bdc1-6cd94bc355ad |
  | vitrage_resource_type        | nova.instance                        |
  | vitrage_sample_timestamp     | 2018-01-03 07:52:06.306507+00:00     |
  | vitrage_type                 | vitrage                              |
  +------------------------------+--------------------------------------+

alarm count
^^^^^^^^^^^
::

  vitrage alarm count

  {
    "WARNING": 2,
    "SEVERE": 0,
    "CRITICAL": 7,
    "OK": 0,
    "N/A": 0
  }


Template Examples
-----------------
**Note:** for templates version 2 --type <template type> is not required.
Template type is specified in the metadata section.

template validate
^^^^^^^^^^^^^^^^^
::

  vitrage template validate --path /home/stack/my_template.yaml --type standard

  Valid types are: standard, definition and equivalence

  {
    "results": [
      {
        "status": "validation OK",
        "file path": "/home/stack/my_template.yaml",
        "status code": 0,
        "message": "Template validation is OK",
        "description": "Template validation"
      }
    ]
  }

  vitrage template validate --path /home/stack/my_template_with_typo.yaml --type standard
  {
    "results": [
      {
        "status": "validation failed",
        "file path": "/home/stack/my_template_with_typo.yaml",
        "status code": 3,
        "message": "template_id does not appear in the definition block. template id: aaalarm",
        "description": "Template content validation"
      }
    ]
  }

template list
^^^^^^^^^^^^^
::

  vitrage template list
  +--------------------------------------+-----------------------------------------+--------+---------------------------+---------------------+-------------+
  | UUID                                 | Name                                    | Status | Status details            | Date                | Type        |
  +--------------------------------------+-----------------------------------------+--------+---------------------------+---------------------+-------------+
  | ae3c0752-1df9-408c-89d5-8b32b86f403f | host_disk_io_overloaded_usage_scenarios | ACTIVE | Template validation is OK | 2018-01-23 10:14:05 | standard    |
  | f254edb0-53cb-4552-969b-bdad24a14a03 | ceph_health_is_not_ok_scenarios         | ACTIVE | Template validation is OK | 2018-01-23 10:20:29 | standard    |
  | bf405cfa-3f19-4761-9329-6e48f21cd466 | basic_def_template                      | ACTIVE | Template validation is OK | 2018-01-23 10:20:56 | definition  |
  | 7b5d6ca8-9ee0-4388-8c91-819b8786b78e | zabbix_host_equivalence                 | ACTIVE | No Validation             | 2018-01-23 10:21:13 | equivalence |
  +--------------------------------------+-----------------------------------------+--------+---------------------------+---------------------+-------------+


template show
^^^^^^^^^^^^^
::

  vitrage template show 72f47086-366f-44d1-b88f-e420a8bc8ff0
  returns a loaded template as json

 Note: You can use template name instead of id

template add
^^^^^^^^^^^^
::

  For template of version 2:
  vitrage template add --path /etc/vitrage/templates/host_disk_io_usage_scenarios.yaml

  For template of version 1 (old):
  vitrage template add --path /etc/vitrage/templates/host_disk_io_usage_scenarios.yaml --type standard

  Valid types are: standard, definition and equivalence

  You can add --wait [SECONDS]  which will block until template completes loading

  +--------------------------------------+-----------------------------------------+---------+---------------------------+----------------------------+----------+
  | UUID                                 | Name                                    | Status  | Status details            | Date                       | Type     |
  +--------------------------------------+-----------------------------------------+---------+---------------------------+----------------------------+----------+
  | ae3c0752-1df9-408c-89d5-8b32b86f403f | host_disk_io_overloaded_usage_scenarios | LOADING | Template validation is OK | 2018-01-23 10:14:05.135990 | standard |
  +--------------------------------------+-----------------------------------------+---------+---------------------------+----------------------------+----------+

template delete
^^^^^^^^^^^^^^^
::

  vitrage template delete ae3c0752-1df9-408c-89d5-8b32b86f403f

 For deleting multiple templates:
  vitrage template delete ae3c0752-1df9-408c-89d5-8b32b86f403f f254edb0-53cb-4552-969b-bdad24a14a03

 You can add --wait [SECONDS]  which will block until template is deleted

 Note: You can use template name instead of id


Templates with parameters
^^^^^^^^^^^^^^^^^^^^^^^^^
::

  vitrage template validate --path ./with_single_param.yaml
  {
    "results": [
      {
        "status": "validation failed",
        "file path": "with_single_param.yaml",
        "status code": 163,
        "message": "Failed to resolve parameter",
        "description": "Template content validation"
      }
    ]
  }

  vitrage template validate --path ./with_single_param.yaml --params alarm_name=Alarm1
  {
    "results": [
      {
        "status": "validation OK",
        "file path": "with_single_param.yaml",
        "status code": 0,
        "message": "Template validation is OK",
        "description": "Template validation"
      }
    ]
  }

  vitrage template add --path ./with_single_param.yaml
  +--------------------------------------+-------------------+--------+-----------------------------+----------------------------+----------+
  | UUID                                 | Name              | Status | Status details              | Date                       | Type     |
  +--------------------------------------+-------------------+--------+-----------------------------+----------------------------+----------+
  | d785f6d4-123b-4271-80cf-c5d9c21adb12 | with_single_param | ERROR  | Failed to resolve parameter | 2019-02-11 11:44:50.916064 | standard |
  +--------------------------------------+-------------------+--------+-----------------------------+----------------------------+----------+

  vitrage template add --path with_params.yaml --params template_name=Template1 alarm_name=Alarm2
  +--------------------------------------+-----------+---------+---------------------------+----------------------------+----------+
  | UUID                                 | Name      | Status  | Status details            | Date                       | Type     |
  +--------------------------------------+-----------+---------+---------------------------+----------------------------+----------+
  | 1a18a38b-99ee-4835-964d-a3fe2f17d4cd | Template1 | LOADING | Template validation is OK | 2019-02-11 11:57:31.077176 | standard |
  +--------------------------------------+-----------+---------+---------------------------+----------------------------+----------+

template versions
^^^^^^^^^^^^^^^^^
::

  vitrage template versions

  +---------+-----------+
  | Version | Status    |
  +---------+-----------+
  | v1      | SUPPORTED |
  | v2      | SUPPORTED |
  | v3      | CURRENT   |
  +---------+-----------+

Event Examples
--------------

To create an alarm on a host, field ``status`` should be ``down``::

  vitrage event post --type 'just.another.alarm.name' --details '{"hostname": "compute-0-0","source": "sample_monitor","cause": "another alarm","severity": "critical","status":"down","monitor_id": "sample monitor","monitor_event_id": "456"}'


To remove the created host alarm, field ``status`` should be ``up``::

  vitrage event post --type 'just.another.alarm.name' --details '{"hostname": "compute-0-0","source": "sample_monitor","cause": "another alarm","severity": "critical","status":"up","monitor_id": "sample monitor","monitor_event_id": "456"}'


Webhook Example
---------------
Note:  To see complete usage: 'vitrage help' and 'vitrage help <command>'

webhook list
^^^^^^^^^^^^
::

    vitrage webhook list

    +--------------------------------------+----------------------------+----------------------------------+---------------------------+--------------------------------------+------------------------+
    | ID                                   | Created At                 | Project ID                       | URL                       | Headers                              | Filter                 |
    +--------------------------------------+----------------------------+----------------------------------+---------------------------+--------------------------------------+------------------------+
    | 1e35dddf-ab0b-46ec-b0cc-0cf48129fc43 | 2018-01-10T14:27:09.000000 | dbec2ffbf3844eaa9d3c75dabf5777d8 | https://www.myurl.com     | {'content-type': 'application/json'} | {'vitrage_type': '.*'} |
    | bdc9edfa-d18c-4a18-9e03-2beb51402be0 | 2018-01-10T14:29:04.000000 | dbec2ffbf3844eaa9d3c75dabf5777d8 | https://hookb.in/Z1dxPre8 |                                      |                        |
    +--------------------------------------+----------------------------+----------------------------------+---------------------------+--------------------------------------+------------------------+


webhook show
^^^^^^^^^^^^
::

 vitrage webhook show c35caf11-f34d-440e-a804-0c1a4fdfb95b

    +--------------+--------------------------------------+
    | Field        | Value                                |
    +--------------+--------------------------------------+
    | created_at   | 2018-01-04T12:27:47.000000           |
    | headers      | None                                 |
    | id           | c35caf11-f34d-440e-a804-0c1a4fdfb95b |
    | regex_filter | {'name':'e2e.*'}                     |
    | updated_at   | None                                 |
    | url          | https://requestb.in/tq3fkvtq         |
    +--------------+--------------------------------------+

webhook delete
^^^^^^^^^^^^^^
::

    vitrage webhook delete c35caf11-f34d-440e-a804-0c1a4fdfb95b

    +---------+------------------------------------------------------+
    | Field   | Value                                                |
    +---------+------------------------------------------------------+
    | SUCCESS | Webhook c35caf11-f34d-440e-a804-0c1a4fdfb95b deleted |
    +---------+------------------------------------------------------+


webhook add
^^^^^^^^^^^
::

    vitrage webhook add --url https://www.myurl.com --headers
    "{'content-type': 'application/json'}" --regex_filter "{'vitrage_type':'.*'}"

    +--------------+--------------------------------------+
    | Field        | Value                                |
    +--------------+--------------------------------------+
    | created_at   | 2018-01-04 14:32:23.489253           |
    | headers      | {'content-type': 'application/json'} |
    | id           | 2bd3ba88-f1fc-4917-bb69-bf0d1ff02d35 |
    | regex_filter | {'vitrage_type': '.*'}               |
    | url          | https://www.myurl.com                |
    +--------------+--------------------------------------+


Status Example
--------------
::
    vitrage status

    +--------+-------+
    | Field  | Value |
    +--------+-------+
    | reason | OK    |
    +--------+-------+

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


If using Keycloak then for auth parameter use ``VitrageKeycloakPlugin`` class
instead of ``Password`` and supply the relevant parameters.
