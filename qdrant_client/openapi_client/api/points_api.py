# coding: utf-8

"""
    Qdrant API

    API description for Qdrant vector search engine. Describes CRUD and search operations on collections of points (vectors with payload).  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Contact: andrey@vasnetsov.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.collection_update_operations import CollectionUpdateOperations
from openapi_client.model.error_response import ErrorResponse
from openapi_client.model.inline_response2003 import InlineResponse2003
from openapi_client.model.inline_response2004 import InlineResponse2004
from openapi_client.model.inline_response2005 import InlineResponse2005
from openapi_client.model.inline_response2006 import InlineResponse2006
from openapi_client.model.point_request import PointRequest
from openapi_client.model.search_request import SearchRequest


class PointsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_point(
            self,
            name,
            id,
            **kwargs
        ):
            """Retrieve point by id  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_point(name, id, async_req=True)
            >>> result = thread.get()

            Args:
                name (str): Name of the collection to retrieve from
                id (int): Id of the point

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                InlineResponse2004
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['name'] = \
                name
            kwargs['id'] = \
                id
            return self.call_with_http_info(**kwargs)

        self.get_point = Endpoint(
            settings={
                'response_type': (InlineResponse2004,),
                'auth': [],
                'endpoint_path': '/collections/{name}/points/{id}',
                'operation_id': 'get_point',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'name',
                    'id',
                ],
                'required': [
                    'name',
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'name':
                        (str,),
                    'id':
                        (int,),
                },
                'attribute_map': {
                    'name': 'name',
                    'id': 'id',
                },
                'location_map': {
                    'name': 'path',
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_point
        )

        def __get_points(
            self,
            name,
            **kwargs
        ):
            """Retrieve points by ids  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_points(name, async_req=True)
            >>> result = thread.get()

            Args:
                name (str): Name of the collection to retrieve from

            Keyword Args:
                point_request (PointRequest): List of points to retrieve. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                InlineResponse2005
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['name'] = \
                name
            return self.call_with_http_info(**kwargs)

        self.get_points = Endpoint(
            settings={
                'response_type': (InlineResponse2005,),
                'auth': [],
                'endpoint_path': '/collections/{name}/points',
                'operation_id': 'get_points',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'name',
                    'point_request',
                ],
                'required': [
                    'name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'name':
                        (str,),
                    'point_request':
                        (PointRequest,),
                },
                'attribute_map': {
                    'name': 'name',
                },
                'location_map': {
                    'name': 'path',
                    'point_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__get_points
        )

        def __search_points(
            self,
            name,
            **kwargs
        ):
            """Search points  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.search_points(name, async_req=True)
            >>> result = thread.get()

            Args:
                name (str): Name of the collection to search in

            Keyword Args:
                search_request (SearchRequest): Search request with optional filtering. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                InlineResponse2006
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['name'] = \
                name
            return self.call_with_http_info(**kwargs)

        self.search_points = Endpoint(
            settings={
                'response_type': (InlineResponse2006,),
                'auth': [],
                'endpoint_path': '/collections/{name}/points/search',
                'operation_id': 'search_points',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'name',
                    'search_request',
                ],
                'required': [
                    'name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'name':
                        (str,),
                    'search_request':
                        (SearchRequest,),
                },
                'attribute_map': {
                    'name': 'name',
                },
                'location_map': {
                    'name': 'path',
                    'search_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__search_points
        )

        def __update_points(
            self,
            name,
            **kwargs
        ):
            """Update points in collection  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_points(name, async_req=True)
            >>> result = thread.get()

            Args:
                name (str): Name of the collection to search in

            Keyword Args:
                collection_update_operations (CollectionUpdateOperations): Points update operations. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                InlineResponse2003
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['name'] = \
                name
            return self.call_with_http_info(**kwargs)

        self.update_points = Endpoint(
            settings={
                'response_type': (InlineResponse2003,),
                'auth': [],
                'endpoint_path': '/collections/{name}',
                'operation_id': 'update_points',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'name',
                    'collection_update_operations',
                ],
                'required': [
                    'name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'name':
                        (str,),
                    'collection_update_operations':
                        (CollectionUpdateOperations,),
                },
                'attribute_map': {
                    'name': 'name',
                },
                'location_map': {
                    'name': 'path',
                    'collection_update_operations': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_points
        )
