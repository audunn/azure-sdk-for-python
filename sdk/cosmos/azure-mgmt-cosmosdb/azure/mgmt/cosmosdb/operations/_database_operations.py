# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class DatabaseOperations(object):
    """DatabaseOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.cosmosdb.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_metrics(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        database_rid,  # type: str
        filter,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.MetricListResult"]
        """Retrieves the metrics determined by the given filter for the given database account and
        database.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param account_name: Cosmos DB database account name.
        :type account_name: str
        :param database_rid: Cosmos DB database rid.
        :type database_rid: str
        :param filter: An OData filter expression that describes a subset of metrics to return. The
         parameters that can be filtered are name.value (name of the metric, can have an or of multiple
         names), startTime, endTime, and timeGrain. The supported operator is eq.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either MetricListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.cosmosdb.models.MetricListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.MetricListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-15"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_metrics.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'accountName': self._serialize.url("account_name", account_name, 'str', max_length=50, min_length=3, pattern=r'^[a-z0-9]+(-[a-z0-9]+)*'),
                    'databaseRid': self._serialize.url("database_rid", database_rid, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('MetricListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_metrics.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/metrics'}  # type: ignore

    def list_usages(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        database_rid,  # type: str
        filter=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.UsagesResult"]
        """Retrieves the usages (most recent data) for the given database.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param account_name: Cosmos DB database account name.
        :type account_name: str
        :param database_rid: Cosmos DB database rid.
        :type database_rid: str
        :param filter: An OData filter expression that describes a subset of usages to return. The
         supported parameter is name.value (name of the metric, can have an or of multiple names).
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either UsagesResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.cosmosdb.models.UsagesResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.UsagesResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-15"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_usages.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'accountName': self._serialize.url("account_name", account_name, 'str', max_length=50, min_length=3, pattern=r'^[a-z0-9]+(-[a-z0-9]+)*'),
                    'databaseRid': self._serialize.url("database_rid", database_rid, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('UsagesResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_usages.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/usages'}  # type: ignore

    def list_metric_definitions(
        self,
        resource_group_name,  # type: str
        account_name,  # type: str
        database_rid,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.MetricDefinitionsListResult"]
        """Retrieves metric definitions for the given database.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param account_name: Cosmos DB database account name.
        :type account_name: str
        :param database_rid: Cosmos DB database rid.
        :type database_rid: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either MetricDefinitionsListResult or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.cosmosdb.models.MetricDefinitionsListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.MetricDefinitionsListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-03-15"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_metric_definitions.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
                    'accountName': self._serialize.url("account_name", account_name, 'str', max_length=50, min_length=3, pattern=r'^[a-z0-9]+(-[a-z0-9]+)*'),
                    'databaseRid': self._serialize.url("database_rid", database_rid, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('MetricDefinitionsListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_metric_definitions.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/databases/{databaseRid}/metricDefinitions'}  # type: ignore
