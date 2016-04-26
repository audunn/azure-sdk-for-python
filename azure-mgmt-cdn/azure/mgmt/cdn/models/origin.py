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

from .resource import Resource


class Origin(Resource):
    """
    CDN origin is the source of the content being delivered via CDN. When the
    edge nodes represented by an endpoint do not have the requested content
    cached, they attempt to fetch it from one or more of the configured
    origins.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param host_name: The address of the origin. Domain names, IPv4
     addresses, and IPv6 addresses are supported.
    :type host_name: str
    :param http_port: The value of the HTTP port. Must be between 1 and 65535.
    :type http_port: int
    :param https_port: The value of the https port. Must be between 1 and
     65535.
    :type https_port: int
    :ivar resource_state: Resource status of the origin. Possible values
     include: 'Creating', 'Active', 'Deleting'
    :vartype resource_state: str
    :param provisioning_state: Provisioning status of the origin. Possible
     values include: 'Creating', 'Succeeded', 'Failed'
    :type provisioning_state: str
    """ 

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'host_name': {'required': True},
        'resource_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'host_name': {'key': 'properties.hostName', 'type': 'str'},
        'http_port': {'key': 'properties.httpPort', 'type': 'int'},
        'https_port': {'key': 'properties.httpsPort', 'type': 'int'},
        'resource_state': {'key': 'properties.resourceState', 'type': 'OriginResourceState'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'ProvisioningState'},
    }

    def __init__(self, host_name, http_port=None, https_port=None, provisioning_state=None):
        super(Origin, self).__init__()
        self.host_name = host_name
        self.http_port = http_port
        self.https_port = https_port
        self.resource_state = None
        self.provisioning_state = provisioning_state
