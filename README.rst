========================
Team and repository tags
========================

.. image:: https://governance.openstack.org/tc/badges/python-vitrageclient.svg
    :target: https://governance.openstack.org/tc/reference/tags/index.html

.. Change things from this point on

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
At the moment only manual install is available

Manual Install Steps:
  - cd to your python-vitrageclient repo
  - sudo pip install -r requirements.txt
  - python setup.py install

Building and Packaging
----------------------
Install the tool dependencies

::

    sudo apt-get install python-pip python-virtualenv


In the python-vitrageclient source directory

::

    virtualenv --no-site-packages .venv

    source ./.venv/bin/activate

    pip install wheel

    python setup.py bdist_wheel

    pip install $(ls -1rt dist/*.whl | tail -1) --upgrade


References
----------

Detailed documentation for the CLI see `CLI Spec <https://opendev.org/openstack/python-vitrageclient/src/branch/master/doc/source/contributor/cli.rst>`_
