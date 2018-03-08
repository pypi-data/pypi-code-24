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


class SecurityGroupViewResult(Model):
    """The information about security rules applied to the specified VM.

    :param network_interfaces: List of network interfaces on the specified VM.
    :type network_interfaces:
     list[~azure.mgmt.network.v2016_09_01.models.SecurityGroupNetworkInterface]
    """

    _attribute_map = {
        'network_interfaces': {'key': 'networkInterfaces', 'type': '[SecurityGroupNetworkInterface]'},
    }

    def __init__(self, **kwargs):
        super(SecurityGroupViewResult, self).__init__(**kwargs)
        self.network_interfaces = kwargs.get('network_interfaces', None)
