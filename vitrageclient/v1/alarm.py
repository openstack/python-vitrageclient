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


class Alarm(object):
    url = 'v1/alarm/'

    def __init__(self, api):
        self.api = api

    def list(self, vitrage_id, all_tenants=False,
             limit=1000,
             sort_by=['start_timestamp', 'vitrage_id'],
             sort_dirs=['asc', 'asc'],
             filter_by=None,
             filter_vals=None,
             next_page=True,
             marker=None):
        """Get a all alarms on entity

        :param all_tenants: should return all tenants alarms
        :param vitrage_id: the id for the entity
        :param limit: number of rows in page.
        :param sort_by: array of attributes by which results should be sorted
        :param sort_dirs: per-column array of sort_dirs,
        corresponding to sort_keys ('asc' or 'desc')
        :param filter_by: array of attributes by which results will be filtered
        :param filter_vals: array of filter values corresponding to filter_by
        :param next_page: True if next page was requested, False if previouse
        :param marker: if next_page is True,
        vitrage_id of last row in current page is needed,
        else, vitrage_id of first row in current page.
        marker=None if the request is for the first page.
        """

        params = dict(vitrage_id=vitrage_id,
                      all_tenants=all_tenants,
                      limit=limit,
                      sort_by=sort_by,
                      sort_dirs=sort_dirs,
                      filter_by=filter_by,
                      filter_vals=filter_vals,
                      next_page=next_page,
                      marker=marker
                      )
        return self.api.get(self.url, params=params).json()

    def history(self, all_tenants=False,
                start=None,
                end=None,
                limit=1000,
                sort_by=('start_timestamp', 'vitrage_id'),
                sort_dirs=('asc', 'asc'),
                filter_by=None,
                filter_vals=None,
                next_page=True,
                marker=None):
        """Get the alarm history

        :param all_tenants: should return all tenants alarms
        :param start: start of time frame.
        :param end: end of time frame.
        :param limit: number of rows in page.
        :param sort_by: array of attributes by which results should be sorted
        :param sort_dirs: per-column array of sort_dirs,
        corresponding to sort_keys ('asc' or 'desc')
        :param filter_by: array of attributes by which results will be filtered
        :param filter_vals: array of filter values corresponding to filter_by
        :param next_page: True if next page was requested, False if previouse
        :param marker: if next_page is True,
        vitrage_id of last row in current page is needed,
        else, vitrage_id of first row in current page.
        marker=None if the request is for the first page.
        """

        params = dict(all_tenants=all_tenants,
                      start=start,
                      end=end,
                      limit=limit,
                      sort_by=sort_by,
                      sort_dirs=sort_dirs,
                      filter_by=filter_by,
                      filter_vals=filter_vals,
                      next_page=next_page,
                      marker=marker
                      )
        return self.api.get(self.url + 'history/', params=params).json()

    def get(self, vitrage_id):
        """Get an alarm

        :param vitrage_id: the vitrage_id of the alarm
        """
        url = self.url + vitrage_id
        return self.api.get(url).json()

    def count(self, all_tenants=False):
        """Get a count of all alarms present

        :param all_tenants: should return all tenants alarms
        """
        params = dict(all_tenants=all_tenants)
        return self.api.get(self.url + 'count/', params=params).json()
