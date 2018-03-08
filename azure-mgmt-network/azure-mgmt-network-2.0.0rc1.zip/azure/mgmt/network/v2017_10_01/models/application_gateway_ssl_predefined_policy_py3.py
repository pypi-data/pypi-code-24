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


class ApplicationGatewaySslPredefinedPolicy(SubResource):
    """An Ssl predefined policy.

    :param id: Resource ID.
    :type id: str
    :param name: Name of Ssl predefined policy.
    :type name: str
    :param cipher_suites: Ssl cipher suites to be enabled in the specified
     order for application gateway.
    :type cipher_suites: list[str or
     ~azure.mgmt.network.v2017_10_01.models.ApplicationGatewaySslCipherSuite]
    :param min_protocol_version: Minimum version of Ssl protocol to be
     supported on application gateway. Possible values include: 'TLSv1_0',
     'TLSv1_1', 'TLSv1_2'
    :type min_protocol_version: str or
     ~azure.mgmt.network.v2017_10_01.models.ApplicationGatewaySslProtocol
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'cipher_suites': {'key': 'properties.cipherSuites', 'type': '[str]'},
        'min_protocol_version': {'key': 'properties.minProtocolVersion', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, name: str=None, cipher_suites=None, min_protocol_version=None, **kwargs) -> None:
        super(ApplicationGatewaySslPredefinedPolicy, self).__init__(id=id, **kwargs)
        self.name = name
        self.cipher_suites = cipher_suites
        self.min_protocol_version = min_protocol_version
