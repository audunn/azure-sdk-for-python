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

from enum import Enum


class JobResourceType(Enum):

    vertex_resource = "VertexResource"
    statistics_resource = "StatisticsResource"


class CompileMode(Enum):

    semantic = "Semantic"
    full = "Full"
    single_box = "SingleBox"


class SeverityTypes(Enum):

    warning = "Warning"
    error = "Error"


class JobType(Enum):

    usql = "USql"
    hive = "Hive"


class JobState(Enum):

    accepted = "Accepted"
    compiling = "Compiling"
    ended = "Ended"
    new = "New"
    queued = "Queued"
    running = "Running"
    scheduling = "Scheduling"
    starting = "Starting"
    paused = "Paused"
    waiting_for_capacity = "WaitingForCapacity"


class JobResult(Enum):

    none = "None"
    succeeded = "Succeeded"
    cancelled = "Cancelled"
    failed = "Failed"
