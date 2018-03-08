# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sub_resource import SubResource


class ApplicationGatewayRedirectConfiguration(SubResource):
    """Redirect configuration of an application gateway.

    :param id: Resource ID.
    :type id: str
    :param redirect_type: Supported http redirection types - Permanent,
     Temporary, Found, SeeOther. Possible values include: 'Permanent', 'Found',
     'SeeOther', 'Temporary'
    :type redirect_type: str or
     ~azure.mgmt.network.v2017_10_01.models.ApplicationGatewayRedirectType
    :param target_listener: Reference to a listener to redirect the request
     to.
    :type target_listener: ~azure.mgmt.network.v2017_10_01.models.SubResource
    :param target_url: Url to redirect the request to.
    :type target_url: str
    :param include_path: Include path in the redirected url.
    :type include_path: bool
    :param include_query_string: Include query string in the redirected url.
    :type include_query_string: bool
    :param request_routing_rules: Request routing specifying redirect
     configuration.
    :type request_routing_rules:
     list[~azure.mgmt.network.v2017_10_01.models.SubResource]
    :param url_path_maps: Url path maps specifying default redirect
     configuration.
    :type url_path_maps:
     list[~azure.mgmt.network.v2017_10_01.models.SubResource]
    :param path_rules: Path rules specifying redirect configuration.
    :type path_rules: list[~azure.mgmt.network.v2017_10_01.models.SubResource]
    :param name: Name of the resource that is unique within a resource group.
     This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    :param type: Type of the resource.
    :type type: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'redirect_type': {'key': 'properties.redirectType', 'type': 'str'},
        'target_listener': {'key': 'properties.targetListener', 'type': 'SubResource'},
        'target_url': {'key': 'properties.targetUrl', 'type': 'str'},
        'include_path': {'key': 'properties.includePath', 'type': 'bool'},
        'include_query_string': {'key': 'properties.includeQueryString', 'type': 'bool'},
        'request_routing_rules': {'key': 'properties.requestRoutingRules', 'type': '[SubResource]'},
        'url_path_maps': {'key': 'properties.urlPathMaps', 'type': '[SubResource]'},
        'path_rules': {'key': 'properties.pathRules', 'type': '[SubResource]'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, redirect_type=None, target_listener=None, target_url: str=None, include_path: bool=None, include_query_string: bool=None, request_routing_rules=None, url_path_maps=None, path_rules=None, name: str=None, etag: str=None, type: str=None, **kwargs) -> None:
        super(ApplicationGatewayRedirectConfiguration, self).__init__(id=id, **kwargs)
        self.redirect_type = redirect_type
        self.target_listener = target_listener
        self.target_url = target_url
        self.include_path = include_path
        self.include_query_string = include_query_string
        self.request_routing_rules = request_routing_rules
        self.url_path_maps = url_path_maps
        self.path_rules = path_rules
        self.name = name
        self.etag = etag
        self.type = type
