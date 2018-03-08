# coding: utf-8

"""
    Connect API

    Mbed Cloud Connect API allows web applications to communicate with devices. You can subscribe to device resources and read/write values to them. mbed Cloud Connect makes connectivity to devices easy by queuing requests and caching resource values.

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient


class ResourcesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v2_endpoints_device_id_resource_path_delete(self, device_id, _resource_path, **kwargs):
        """
        Delete a resource path
        A request to delete a resource path must be handled by both Mbed Cloud Client and Mbed Cloud Connect.  All resource APIs are asynchronous. These APIs respond only if the device is turned on and connected to Mbed Cloud Connect and there is an active notification channel.  **Example usage:**      curl -X DELETE \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/{resourcePath} \\       -H 'authorization: Bearer {api-key}' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.v2_endpoints_device_id_resource_path_delete(device_id, _resource_path, async=True)
        >>> result = thread.get()

        :param async bool
        :param str device_id: A unique Mbed Cloud device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: The URL of the resource.  (required)
        :param bool no_resp: <br/><br/><b>Non-confirmable requests</b><br/>  All resource APIs have the parameter noResp. If you make a request with `noResp=true`, Mbed Cloud Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.v2_endpoints_device_id_resource_path_delete_with_http_info(device_id, _resource_path, **kwargs)
        else:
            (data) = self.v2_endpoints_device_id_resource_path_delete_with_http_info(device_id, _resource_path, **kwargs)
            return data

    def v2_endpoints_device_id_resource_path_delete_with_http_info(self, device_id, _resource_path, **kwargs):
        """
        Delete a resource path
        A request to delete a resource path must be handled by both Mbed Cloud Client and Mbed Cloud Connect.  All resource APIs are asynchronous. These APIs respond only if the device is turned on and connected to Mbed Cloud Connect and there is an active notification channel.  **Example usage:**      curl -X DELETE \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/{resourcePath} \\       -H 'authorization: Bearer {api-key}' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.v2_endpoints_device_id_resource_path_delete_with_http_info(device_id, _resource_path, async=True)
        >>> result = thread.get()

        :param async bool
        :param str device_id: A unique Mbed Cloud device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: The URL of the resource.  (required)
        :param bool no_resp: <br/><br/><b>Non-confirmable requests</b><br/>  All resource APIs have the parameter noResp. If you make a request with `noResp=true`, Mbed Cloud Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', '_resource_path', 'no_resp']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_endpoints_device_id_resource_path_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `v2_endpoints_device_id_resource_path_delete`")
        # verify the required parameter '_resource_path' is set
        if ('_resource_path' not in params) or (params['_resource_path'] is None):
            raise ValueError("Missing the required parameter `_resource_path` when calling `v2_endpoints_device_id_resource_path_delete`")


        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['device-id'] = params['device_id']
        if '_resource_path' in params:
            path_params['resourcePath'] = params['_resource_path']

        query_params = []
        if 'no_resp' in params:
            query_params.append(('noResp', params['no_resp']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api('/v2/endpoints/{device-id}/{resourcePath}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AsyncID',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def v2_endpoints_device_id_resource_path_get(self, device_id, _resource_path, **kwargs):
        """
        Read from a resource
        Requests the resource value and when the response is available, an `AsyncIDResponse` json object is received in the notification channel. The preferred way to get resource values is to use [subscribe](/docs/v1.2/service-api-references/connect-api.html#v2-notification-callback) and [callback](/docs/v1.2/service-api-references/connect-api.html#v2-notification-callback) methods. See more about [reading from a resource](/docs/v1.2/collecting/handling-resources-from-a-web-application.html#the-read-operation).  All resource APIs are asynchronous. These APIs only respond if the device is turned on and connected to Mbed Cloud Connect.  Please refer to [Lightweigth Machine to Machine Technical specification](http://www.openmobilealliance.org/release/LightweightM2M/V1_0-20170208-A/OMA-TS-LightweightM2M-V1_0-20170208-A.pdf) for more inforamtion.  **Example usage:**      curl -X GET \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/{resourcePath} \\       -H 'authorization: Bearer {api-key}'        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.v2_endpoints_device_id_resource_path_get(device_id, _resource_path, async=True)
        >>> result = thread.get()

        :param async bool
        :param str device_id: Unique Mbed Cloud device ID for the endpoint. Note that the ID needs to be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: The URL of the resource.  (required)
        :param bool cache_only: If true, the response comes only from the cache. Default: false. Mbed Cloud Connect caches the received resource values for the time of [max_age](/docs/v1.2/collecting/working-with-the-resources.html#working-with-the-server-cache) defined in the client side. 
        :param bool no_resp: <br/><br/><b>Non-confirmable requests</b><br/>  All resource APIs have the parameter `noResp`. If a request is made with `noResp=true`, Mbed Cloud Connect makes a CoAP  non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back  an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol  does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code  `409 Conflict`. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.v2_endpoints_device_id_resource_path_get_with_http_info(device_id, _resource_path, **kwargs)
        else:
            (data) = self.v2_endpoints_device_id_resource_path_get_with_http_info(device_id, _resource_path, **kwargs)
            return data

    def v2_endpoints_device_id_resource_path_get_with_http_info(self, device_id, _resource_path, **kwargs):
        """
        Read from a resource
        Requests the resource value and when the response is available, an `AsyncIDResponse` json object is received in the notification channel. The preferred way to get resource values is to use [subscribe](/docs/v1.2/service-api-references/connect-api.html#v2-notification-callback) and [callback](/docs/v1.2/service-api-references/connect-api.html#v2-notification-callback) methods. See more about [reading from a resource](/docs/v1.2/collecting/handling-resources-from-a-web-application.html#the-read-operation).  All resource APIs are asynchronous. These APIs only respond if the device is turned on and connected to Mbed Cloud Connect.  Please refer to [Lightweigth Machine to Machine Technical specification](http://www.openmobilealliance.org/release/LightweightM2M/V1_0-20170208-A/OMA-TS-LightweightM2M-V1_0-20170208-A.pdf) for more inforamtion.  **Example usage:**      curl -X GET \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/{resourcePath} \\       -H 'authorization: Bearer {api-key}'        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.v2_endpoints_device_id_resource_path_get_with_http_info(device_id, _resource_path, async=True)
        >>> result = thread.get()

        :param async bool
        :param str device_id: Unique Mbed Cloud device ID for the endpoint. Note that the ID needs to be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: The URL of the resource.  (required)
        :param bool cache_only: If true, the response comes only from the cache. Default: false. Mbed Cloud Connect caches the received resource values for the time of [max_age](/docs/v1.2/collecting/working-with-the-resources.html#working-with-the-server-cache) defined in the client side. 
        :param bool no_resp: <br/><br/><b>Non-confirmable requests</b><br/>  All resource APIs have the parameter `noResp`. If a request is made with `noResp=true`, Mbed Cloud Connect makes a CoAP  non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back  an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol  does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code  `409 Conflict`. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', '_resource_path', 'cache_only', 'no_resp']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_endpoints_device_id_resource_path_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `v2_endpoints_device_id_resource_path_get`")
        # verify the required parameter '_resource_path' is set
        if ('_resource_path' not in params) or (params['_resource_path'] is None):
            raise ValueError("Missing the required parameter `_resource_path` when calling `v2_endpoints_device_id_resource_path_get`")


        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['device-id'] = params['device_id']
        if '_resource_path' in params:
            path_params['resourcePath'] = params['_resource_path']

        query_params = []
        if 'cache_only' in params:
            query_params.append(('cacheOnly', params['cache_only']))
        if 'no_resp' in params:
            query_params.append(('noResp', params['no_resp']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api('/v2/endpoints/{device-id}/{resourcePath}', 'GET',
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

    def v2_endpoints_device_id_resource_path_post(self, device_id, _resource_path, **kwargs):
        """
        Execute a function on a Resource or create new Object instance
        With this API, you can [execute a function](/docs/v1.2/collecting/handling-resources-from-a-web-application.html#the-execute-operation)  on an existing resource and create new Object instance to the device. The resource-path does not have to exist - it can be  created by the call. The maximum length of resource-path is 255 characters.  All resource APIs are asynchronous. These APIs respond only if the device is turned on and connected to Mbed Cloud Connect and there is an active notification channel.  **Example usage:**  This example resets the min and max values of the [temperature sensor](http://www.openmobilealliance.org/tech/profiles/lwm2m/3303.xml) instance 0 by executing the Resource 5605 'Reset Min and Max Measured Values'.          curl -X POST \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/3303/0/5605 \\       -H 'authorization: Bearer {api-key}' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.v2_endpoints_device_id_resource_path_post(device_id, _resource_path, async=True)
        >>> result = thread.get()

        :param async bool
        :param str device_id: A unique Mbed Cloud device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: The URL of the resource. (required)
        :param str resource_function: This value is not needed. Most of the time resources do not accept a function but they have their own functions predefined. You can use this to trigger them.  If a function is included, the body of this request is passed as a char* to the function in Mbed Cloud Client. 
        :param bool no_resp: <br/><br/><b>Non-confirmable requests</b><br/>  All resource APIs have the parameter noResp. If you make a request with `noResp=true`, Mbed Cloud Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.v2_endpoints_device_id_resource_path_post_with_http_info(device_id, _resource_path, **kwargs)
        else:
            (data) = self.v2_endpoints_device_id_resource_path_post_with_http_info(device_id, _resource_path, **kwargs)
            return data

    def v2_endpoints_device_id_resource_path_post_with_http_info(self, device_id, _resource_path, **kwargs):
        """
        Execute a function on a Resource or create new Object instance
        With this API, you can [execute a function](/docs/v1.2/collecting/handling-resources-from-a-web-application.html#the-execute-operation)  on an existing resource and create new Object instance to the device. The resource-path does not have to exist - it can be  created by the call. The maximum length of resource-path is 255 characters.  All resource APIs are asynchronous. These APIs respond only if the device is turned on and connected to Mbed Cloud Connect and there is an active notification channel.  **Example usage:**  This example resets the min and max values of the [temperature sensor](http://www.openmobilealliance.org/tech/profiles/lwm2m/3303.xml) instance 0 by executing the Resource 5605 'Reset Min and Max Measured Values'.          curl -X POST \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/3303/0/5605 \\       -H 'authorization: Bearer {api-key}' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.v2_endpoints_device_id_resource_path_post_with_http_info(device_id, _resource_path, async=True)
        >>> result = thread.get()

        :param async bool
        :param str device_id: A unique Mbed Cloud device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: The URL of the resource. (required)
        :param str resource_function: This value is not needed. Most of the time resources do not accept a function but they have their own functions predefined. You can use this to trigger them.  If a function is included, the body of this request is passed as a char* to the function in Mbed Cloud Client. 
        :param bool no_resp: <br/><br/><b>Non-confirmable requests</b><br/>  All resource APIs have the parameter noResp. If you make a request with `noResp=true`, Mbed Cloud Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', '_resource_path', 'resource_function', 'no_resp']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_endpoints_device_id_resource_path_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `v2_endpoints_device_id_resource_path_post`")
        # verify the required parameter '_resource_path' is set
        if ('_resource_path' not in params) or (params['_resource_path'] is None):
            raise ValueError("Missing the required parameter `_resource_path` when calling `v2_endpoints_device_id_resource_path_post`")


        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['device-id'] = params['device_id']
        if '_resource_path' in params:
            path_params['resourcePath'] = params['_resource_path']

        query_params = []
        if 'no_resp' in params:
            query_params.append(('noResp', params['no_resp']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'resource_function' in params:
            body_params = params['resource_function']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['text/plain', 'application/xml', 'application/octet-stream', 'application/exi', 'application/json', 'application/link-format', 'application/senml+json', 'application/nanoservice-tlv', 'application/vnd.oma.lwm2m+text', 'application/vnd.oma.lwm2m+opaq', 'application/vnd.oma.lwm2m+tlv', 'application/vnd.oma.lwm2m+json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api('/v2/endpoints/{device-id}/{resourcePath}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AsyncID',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def v2_endpoints_device_id_resource_path_put(self, device_id, _resource_path, resource_value, **kwargs):
        """
        Write to a resource or use write-attributes for a resource
        With this API, you can [write a new value to existing resources](/docs/v1.2/collecting/handling-resources-from-a-web-application.html#the-write-operation) or [use the write-attributes](/docs/v1.2/collecting/subscribing-to-resource-changes-from-a-web-application.html#notification-rules) for a resource.  This API can also be used to transfer files to the device. Mbed Cloud Connect LwM2M server implements the Option 1 from RFC7959. The maximum block size is 1024 bytes. The block size versus transferred file size is something to note in low quality networks. The customer application needs to know what type of file is transferred (for example txt) and the payload can be encrypted by the customer. The maximum size of payload is 1048576 bytes.  All resource APIs are asynchronous. These APIs respond only if the device is turned on and connected to Mbed Cloud Connect and there is an active notification channel.  **Example usage:**  This example sets the alarm on a buzzer. The command writes the [Buzzer](http://www.openmobilealliance.org/tech/profiles/lwm2m/3338.xml) instance 0, \"On/Off\" boolean resource to '1'.      curl -X PUT \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/3338/0/5850 -H \"content-type: text/plain\" \\       -H 'authorization: Bearer {api-key}' -d '1' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.v2_endpoints_device_id_resource_path_put(device_id, _resource_path, resource_value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str device_id: A unique Mbed Cloud device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: Resource URL. (required)
        :param str resource_value: The value to be set to the resource.  (required)
        :param bool no_resp: <br/><br/><b>Non-confirmable requests</b><br/>  All resource APIs have the parameter noResp. If you make a request with `noResp=true`, Mbed Cloud Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.v2_endpoints_device_id_resource_path_put_with_http_info(device_id, _resource_path, resource_value, **kwargs)
        else:
            (data) = self.v2_endpoints_device_id_resource_path_put_with_http_info(device_id, _resource_path, resource_value, **kwargs)
            return data

    def v2_endpoints_device_id_resource_path_put_with_http_info(self, device_id, _resource_path, resource_value, **kwargs):
        """
        Write to a resource or use write-attributes for a resource
        With this API, you can [write a new value to existing resources](/docs/v1.2/collecting/handling-resources-from-a-web-application.html#the-write-operation) or [use the write-attributes](/docs/v1.2/collecting/subscribing-to-resource-changes-from-a-web-application.html#notification-rules) for a resource.  This API can also be used to transfer files to the device. Mbed Cloud Connect LwM2M server implements the Option 1 from RFC7959. The maximum block size is 1024 bytes. The block size versus transferred file size is something to note in low quality networks. The customer application needs to know what type of file is transferred (for example txt) and the payload can be encrypted by the customer. The maximum size of payload is 1048576 bytes.  All resource APIs are asynchronous. These APIs respond only if the device is turned on and connected to Mbed Cloud Connect and there is an active notification channel.  **Example usage:**  This example sets the alarm on a buzzer. The command writes the [Buzzer](http://www.openmobilealliance.org/tech/profiles/lwm2m/3338.xml) instance 0, \"On/Off\" boolean resource to '1'.      curl -X PUT \\       https://api.us-east-1.mbedcloud.com/v2/endpoints/{device-id}/3338/0/5850 -H \"content-type: text/plain\" \\       -H 'authorization: Bearer {api-key}' -d '1' 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.v2_endpoints_device_id_resource_path_put_with_http_info(device_id, _resource_path, resource_value, async=True)
        >>> result = thread.get()

        :param async bool
        :param str device_id: A unique Mbed Cloud device ID for the endpoint. Note that the ID must be an exact match. You cannot use wildcards here.  (required)
        :param str _resource_path: Resource URL. (required)
        :param str resource_value: The value to be set to the resource.  (required)
        :param bool no_resp: <br/><br/><b>Non-confirmable requests</b><br/>  All resource APIs have the parameter noResp. If you make a request with `noResp=true`, Mbed Cloud Connect makes a CoAP non-confirmable request to the device. Such requests are not guaranteed to arrive in the device, and you do not get back an async-response-id.  If calls with this parameter enabled succeed, they return with the status code `204 No Content`. If the underlying protocol does not support non-confirmable requests, or if the endpoint is registered in queue mode, the response is status code `409 Conflict`. 
        :return: AsyncID
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id', '_resource_path', 'resource_value', 'no_resp']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_endpoints_device_id_resource_path_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `v2_endpoints_device_id_resource_path_put`")
        # verify the required parameter '_resource_path' is set
        if ('_resource_path' not in params) or (params['_resource_path'] is None):
            raise ValueError("Missing the required parameter `_resource_path` when calling `v2_endpoints_device_id_resource_path_put`")
        # verify the required parameter 'resource_value' is set
        if ('resource_value' not in params) or (params['resource_value'] is None):
            raise ValueError("Missing the required parameter `resource_value` when calling `v2_endpoints_device_id_resource_path_put`")


        collection_formats = {}

        path_params = {}
        if 'device_id' in params:
            path_params['device-id'] = params['device_id']
        if '_resource_path' in params:
            path_params['resourcePath'] = params['_resource_path']

        query_params = []
        if 'no_resp' in params:
            query_params.append(('noResp', params['no_resp']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'resource_value' in params:
            body_params = params['resource_value']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['text/plain', 'application/xml', 'application/octet-stream', 'application/exi', 'application/json', 'application/link-format', 'application/senml+json', 'application/nanoservice-tlv', 'application/vnd.oma.lwm2m+text', 'application/vnd.oma.lwm2m+opaq', 'application/vnd.oma.lwm2m+tlv', 'application/vnd.oma.lwm2m+json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return self.api_client.call_api('/v2/endpoints/{device-id}/{resourcePath}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AsyncID',
                                        auth_settings=auth_settings,
                                        async=params.get('async'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
