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


class ExpressRouteCircuitArpTable(Model):
    """The ARP table associated with the ExpressRouteCircuit.

    :param ip_address: The IP address.
    :type ip_address: str
    :param mac_address: The MAC address.
    :type mac_address: str
    """

    _attribute_map = {
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
        'mac_address': {'key': 'macAddress', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExpressRouteCircuitArpTable, self).__init__(**kwargs)
        self.ip_address = kwargs.get('ip_address', None)
        self.mac_address = kwargs.get('mac_address', None)
