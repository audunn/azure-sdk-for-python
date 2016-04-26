# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobProperties(Model):
    """JobProperties

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param start_time: Gets or sets the job start time.
    :type start_time: datetime
    :param action: Gets or sets the job action.
    :type action: :class:`JobAction <azure.mgmt.scheduler.models.JobAction>`
    :param recurrence: Gets or sets the job recurrence.
    :type recurrence: :class:`JobRecurrence
     <azure.mgmt.scheduler.models.JobRecurrence>`
    :param state: Gets or set the job state. Possible values include:
     'Enabled', 'Disabled', 'Faulted', 'Completed'
    :type state: str
    :ivar status: Gets the job status.
    :vartype status: :class:`JobStatus
     <azure.mgmt.scheduler.models.JobStatus>`
    """ 

    _validation = {
        'status': {'readonly': True},
    }

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'action': {'key': 'action', 'type': 'JobAction'},
        'recurrence': {'key': 'recurrence', 'type': 'JobRecurrence'},
        'state': {'key': 'state', 'type': 'JobState'},
        'status': {'key': 'status', 'type': 'JobStatus'},
    }

    def __init__(self, start_time=None, action=None, recurrence=None, state=None):
        self.start_time = start_time
        self.action = action
        self.recurrence = recurrence
        self.state = state
        self.status = None
