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


class ServerFarmWithRichSku(Resource):
    """
    App Service Plan Model

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource Id
    :type id: str
    :param name: Resource Name
    :type name: str
    :param kind: Kind of resource
    :type kind: str
    :param location: Resource Location
    :type location: str
    :param type: Resource type
    :type type: str
    :param tags: Resource tags
    :type tags: dict
    :param server_farm_with_rich_sku_name: Name for the App Service Plan
    :type server_farm_with_rich_sku_name: str
    :param worker_tier_name: Target worker tier assigned to the App Service
     Plan
    :type worker_tier_name: str
    :ivar status: App Service Plan Status. Possible values include: 'Ready',
     'Pending'
    :vartype status: str
    :ivar subscription: App Service Plan Subscription
    :vartype subscription: str
    :param admin_site_name: App Service Plan administration site
    :type admin_site_name: str
    :param hosting_environment_profile: Specification for the hosting
     environment (App Service Environment) to use for the App Service Plan
    :type hosting_environment_profile: :class:`HostingEnvironmentProfile
     <azure.mgmt.web.models.HostingEnvironmentProfile>`
    :param maximum_number_of_workers: Maximum number of instances that can be
     assigned to this App Service Plan
    :type maximum_number_of_workers: int
    :ivar geo_region: Geographical location for the App Service Plan
    :vartype geo_region: str
    :param per_site_scaling: If True apps assigned to this App Service Plan
     can be scaled independently
     If False apps assigned to this App Service Plan will scale to
     all instances of the plan
    :type per_site_scaling: bool
    :ivar number_of_sites: Number of web apps assigned to this App Service
     Plan
    :vartype number_of_sites: int
    :ivar resource_group: Resource group of the serverfarm
    :vartype resource_group: str
    :param sku:
    :type sku: :class:`SkuDescription <azure.mgmt.web.models.SkuDescription>`
    """ 

    _validation = {
        'location': {'required': True},
        'status': {'readonly': True},
        'subscription': {'readonly': True},
        'geo_region': {'readonly': True},
        'number_of_sites': {'readonly': True},
        'resource_group': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'server_farm_with_rich_sku_name': {'key': 'properties.name', 'type': 'str'},
        'worker_tier_name': {'key': 'properties.workerTierName', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'StatusOptions'},
        'subscription': {'key': 'properties.subscription', 'type': 'str'},
        'admin_site_name': {'key': 'properties.adminSiteName', 'type': 'str'},
        'hosting_environment_profile': {'key': 'properties.hostingEnvironmentProfile', 'type': 'HostingEnvironmentProfile'},
        'maximum_number_of_workers': {'key': 'properties.maximumNumberOfWorkers', 'type': 'int'},
        'geo_region': {'key': 'properties.geoRegion', 'type': 'str'},
        'per_site_scaling': {'key': 'properties.perSiteScaling', 'type': 'bool'},
        'number_of_sites': {'key': 'properties.numberOfSites', 'type': 'int'},
        'resource_group': {'key': 'properties.resourceGroup', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'SkuDescription'},
    }

    def __init__(self, location, id=None, name=None, kind=None, type=None, tags=None, server_farm_with_rich_sku_name=None, worker_tier_name=None, admin_site_name=None, hosting_environment_profile=None, maximum_number_of_workers=None, per_site_scaling=None, sku=None):
        super(ServerFarmWithRichSku, self).__init__(id=id, name=name, kind=kind, location=location, type=type, tags=tags)
        self.server_farm_with_rich_sku_name = server_farm_with_rich_sku_name
        self.worker_tier_name = worker_tier_name
        self.status = None
        self.subscription = None
        self.admin_site_name = admin_site_name
        self.hosting_environment_profile = hosting_environment_profile
        self.maximum_number_of_workers = maximum_number_of_workers
        self.geo_region = None
        self.per_site_scaling = per_site_scaling
        self.number_of_sites = None
        self.resource_group = None
        self.sku = sku
