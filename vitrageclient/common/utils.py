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
import time


def args_to_dict(args, attrs):
    return {(attr, value)
            for attr, value in [(attr, getattr(args, attr)) for attr in attrs]
            if value is not None}


def list2cols(cols, objs):
    return cols, [tuple([o[k] for k in cols])
                  for o in objs]


def list2cols_with_rename(names_and_keys, objs):
    cols = [i[0] for i in names_and_keys]
    keys = [i[1] for i in names_and_keys]
    return cols, [tuple([o.get(k, '') for k in keys])
                  for o in objs]


def get_client(obj):
    if hasattr(obj.app, 'client_manager'):
        return obj.app.client_manager.rca
    else:
        return obj.app.client


def wait_for_action_to_end(timeout, func, **kwargs):
    count = 0
    while count < timeout:
        if func(**kwargs):
            return True
        count += 1
        time.sleep(1)
    return False


def find_template_with_uuid(uuid, templates):
    return next(
        (
            template
            for template in templates
            if template['uuid'] == uuid
        ), None
    )
