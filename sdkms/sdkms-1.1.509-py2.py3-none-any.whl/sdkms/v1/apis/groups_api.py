# coding: utf-8

"""
    Fortanix SDKMS REST API

    This is a set of REST APIs for accessing the Fortanix Self-Defending Key Management System. This includes APIs for managing accounts, and for performing cryptographic and key management operations. 

    OpenAPI spec version: 1.0.0-20171218
    Contact: support@fortanix.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


# NOTE: This class is auto generated by the swagger code generator program.
# Do not edit the class manually.
# Ref: https://github.com/swagger-api/swagger-codegen
class GroupsApi(object):
    """
    @undocumented: create_group_with_http_info
    @undocumented: delete_group_with_http_info
    @undocumented: get_group_with_http_info
    @undocumented: get_groups_with_http_info
    @undocumented: update_group_with_http_info
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_group(self, body, async=False, **kwargs):
        """
        Create a new group with the specified properties.
        @type async: bool
        @param async: Whether the call should be performed asynchronously. (Default is False).
        @type body: L{GroupRequest}
        @param body: Name of group (required)
        @rtype: L{Group}
        @return:
        
        If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if async:
            return self.create_group_with_http_info(body, async=async, **kwargs)
        else:
            (data) = self.create_group_with_http_info(body, async=async, **kwargs)
            return data

    def create_group_with_http_info(self, body, async=False, **kwargs):
        """
        Create a new group with the specified properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True::
            >>> thread = api.create_group_with_http_info(body, async=True)
            >>> result = thread.get()

        @type async: bool
        @param async: Whether the call should be performed asynchronously. (Default is False).
        @type body: L{GroupRequest}
        @param body: Name of group (required)
        @rtype: L{Group}
        @return:

        If the method is called asynchronously, returns the request thread.
        """

        all_params = ['body']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_group`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['bearerToken']

        return self.api_client.call_api('/sys/v1/groups', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Group',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_group(self, group_id, async=False, **kwargs):
        """
        Remove a group from SDKMS.
        @type async: bool
        @param async: Whether the call should be performed asynchronously. (Default is False).
        @type group_id: L{str}
        @param group_id: Group Identifier (required)
        @rtype: None
        @return:
        
        If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if async:
            return self.delete_group_with_http_info(group_id, async=async, **kwargs)
        else:
            (data) = self.delete_group_with_http_info(group_id, async=async, **kwargs)
            return data

    def delete_group_with_http_info(self, group_id, async=False, **kwargs):
        """
        Remove a group from SDKMS.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True::
            >>> thread = api.delete_group_with_http_info(group_id, async=True)
            >>> result = thread.get()

        @type async: bool
        @param async: Whether the call should be performed asynchronously. (Default is False).
        @type group_id: L{str}
        @param group_id: Group Identifier (required)
        @rtype: None
        @return:

        If the method is called asynchronously, returns the request thread.
        """

        all_params = ['group_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `delete_group`")


        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group-id'] = params['group_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['bearerToken']

        return self.api_client.call_api('/sys/v1/groups/{group-id}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_group(self, group_id, async=False, **kwargs):
        """
        Look up a specific group by group ID.
        @type async: bool
        @param async: Whether the call should be performed asynchronously. (Default is False).
        @type group_id: L{str}
        @param group_id: Group Identifier (required)
        @rtype: L{Group}
        @return:
        
        If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if async:
            return self.get_group_with_http_info(group_id, async=async, **kwargs)
        else:
            (data) = self.get_group_with_http_info(group_id, async=async, **kwargs)
            return data

    def get_group_with_http_info(self, group_id, async=False, **kwargs):
        """
        Look up a specific group by group ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True::
            >>> thread = api.get_group_with_http_info(group_id, async=True)
            >>> result = thread.get()

        @type async: bool
        @param async: Whether the call should be performed asynchronously. (Default is False).
        @type group_id: L{str}
        @param group_id: Group Identifier (required)
        @rtype: L{Group}
        @return:

        If the method is called asynchronously, returns the request thread.
        """

        all_params = ['group_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_group`")


        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group-id'] = params['group_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['bearerToken']

        return self.api_client.call_api('/sys/v1/groups/{group-id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Group',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_groups(self, async=False, **kwargs):
        """
        Get detailed information about all groups the authenticated User or authenticated Application belongs to.
        @type async: bool
        @param async: Whether the call should be performed asynchronously. (Default is False).
        @rtype: list[L{Group}]
        @return:
        
        If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if async:
            return self.get_groups_with_http_info(async=async, **kwargs)
        else:
            (data) = self.get_groups_with_http_info(async=async, **kwargs)
            return data

    def get_groups_with_http_info(self, async=False, **kwargs):
        """
        Get detailed information about all groups the authenticated User or authenticated Application belongs to.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True::
            >>> thread = api.get_groups_with_http_info(async=True)
            >>> result = thread.get()

        @type async: bool
        @param async: Whether the call should be performed asynchronously. (Default is False).
        @rtype: list[L{Group}]
        @return:

        If the method is called asynchronously, returns the request thread.
        """

        all_params = []
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_groups" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['bearerToken']

        return self.api_client.call_api('/sys/v1/groups', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[Group]',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_group(self, group_id, body, async=False, **kwargs):
        """
        Change a group's properties.
        @type async: bool
        @param async: Whether the call should be performed asynchronously. (Default is False).
        @type group_id: L{str}
        @param group_id: Group Identifier (required)
        @type body: L{GroupRequest}
        @param body: Name of group (required)
        @rtype: L{Group}
        @return:
        
        If the method is called asynchronously, returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if async:
            return self.update_group_with_http_info(group_id, body, async=async, **kwargs)
        else:
            (data) = self.update_group_with_http_info(group_id, body, async=async, **kwargs)
            return data

    def update_group_with_http_info(self, group_id, body, async=False, **kwargs):
        """
        Change a group's properties.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True::
            >>> thread = api.update_group_with_http_info(group_id, body, async=True)
            >>> result = thread.get()

        @type async: bool
        @param async: Whether the call should be performed asynchronously. (Default is False).
        @type group_id: L{str}
        @param group_id: Group Identifier (required)
        @type body: L{GroupRequest}
        @param body: Name of group (required)
        @rtype: L{Group}
        @return:

        If the method is called asynchronously, returns the request thread.
        """

        all_params = ['group_id', 'body']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `update_group`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_group`")


        collection_formats = {}

        path_params = {}
        if 'group_id' in params:
            path_params['group-id'] = params['group_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['bearerToken']

        return self.api_client.call_api('/sys/v1/groups/{group-id}', 'PATCH',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Group',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
