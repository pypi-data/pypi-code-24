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

from msrest.serialization import Model


class ApplicationGatewayBackendHealthHttpSettings(Model):
    """Application gateway BackendHealthHttp settings.

    :param backend_http_settings: Reference of an
     ApplicationGatewayBackendHttpSettings resource.
    :type backend_http_settings:
     ~azure.mgmt.network.v2017_10_01.models.ApplicationGatewayBackendHttpSettings
    :param servers: List of ApplicationGatewayBackendHealthServer resources.
    :type servers:
     list[~azure.mgmt.network.v2017_10_01.models.ApplicationGatewayBackendHealthServer]
    """

    _attribute_map = {
        'backend_http_settings': {'key': 'backendHttpSettings', 'type': 'ApplicationGatewayBackendHttpSettings'},
        'servers': {'key': 'servers', 'type': '[ApplicationGatewayBackendHealthServer]'},
    }

    def __init__(self, **kwargs):
        super(ApplicationGatewayBackendHealthHttpSettings, self).__init__(**kwargs)
        self.backend_http_settings = kwargs.get('backend_http_settings', None)
        self.servers = kwargs.get('servers', None)
