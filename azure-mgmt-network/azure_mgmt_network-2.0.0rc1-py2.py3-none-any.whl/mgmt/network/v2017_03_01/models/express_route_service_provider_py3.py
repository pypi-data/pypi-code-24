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

from .resource import Resource


class ExpressRouteServiceProvider(Resource):
    """A ExpressRouteResourceProvider object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param peering_locations: Get a list of peering locations.
    :type peering_locations: list[str]
    :param bandwidths_offered: Gets bandwidths offered.
    :type bandwidths_offered:
     list[~azure.mgmt.network.v2017_03_01.models.ExpressRouteServiceProviderBandwidthsOffered]
    :param provisioning_state: Gets the provisioning state of the resource.
    :type provisioning_state: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'peering_locations': {'key': 'properties.peeringLocations', 'type': '[str]'},
        'bandwidths_offered': {'key': 'properties.bandwidthsOffered', 'type': '[ExpressRouteServiceProviderBandwidthsOffered]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, location: str=None, tags=None, peering_locations=None, bandwidths_offered=None, provisioning_state: str=None, **kwargs) -> None:
        super(ExpressRouteServiceProvider, self).__init__(id=id, location=location, tags=tags, **kwargs)
        self.peering_locations = peering_locations
        self.bandwidths_offered = bandwidths_offered
        self.provisioning_state = provisioning_state
