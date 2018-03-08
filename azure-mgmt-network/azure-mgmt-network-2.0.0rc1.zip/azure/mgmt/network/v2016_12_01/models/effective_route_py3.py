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


class EffectiveRoute(Model):
    """Effective Route.

    :param name: The name of the user defined route. This is optional.
    :type name: str
    :param source: Who created the route. Possible values are: 'Unknown',
     'User', 'VirtualNetworkGateway', and 'Default'. Possible values include:
     'Unknown', 'User', 'VirtualNetworkGateway', 'Default'
    :type source: str or
     ~azure.mgmt.network.v2016_12_01.models.EffectiveRouteSource
    :param state: The value of effective route. Possible values are: 'Active'
     and 'Invalid'. Possible values include: 'Active', 'Invalid'
    :type state: str or
     ~azure.mgmt.network.v2016_12_01.models.EffectiveRouteState
    :param address_prefix: The address prefixes of the effective routes in
     CIDR notation.
    :type address_prefix: list[str]
    :param next_hop_ip_address: The IP address of the next hop of the
     effective route.
    :type next_hop_ip_address: list[str]
    :param next_hop_type: The type of Azure hop the packet should be sent to.
     Possible values are: 'VirtualNetworkGateway', 'VnetLocal', 'Internet',
     'VirtualAppliance', and 'None'. Possible values include:
     'VirtualNetworkGateway', 'VnetLocal', 'Internet', 'VirtualAppliance',
     'None'
    :type next_hop_type: str or
     ~azure.mgmt.network.v2016_12_01.models.RouteNextHopType
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'address_prefix': {'key': 'addressPrefix', 'type': '[str]'},
        'next_hop_ip_address': {'key': 'nextHopIpAddress', 'type': '[str]'},
        'next_hop_type': {'key': 'nextHopType', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, source=None, state=None, address_prefix=None, next_hop_ip_address=None, next_hop_type=None, **kwargs) -> None:
        super(EffectiveRoute, self).__init__(**kwargs)
        self.name = name
        self.source = source
        self.state = state
        self.address_prefix = address_prefix
        self.next_hop_ip_address = next_hop_ip_address
        self.next_hop_type = next_hop_type
