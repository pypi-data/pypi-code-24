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


class ConnectivityParameters(Model):
    """Parameters that determine how the connectivity check will be performed.

    All required parameters must be populated in order to send to Azure.

    :param source: Required.
    :type source: ~azure.mgmt.network.v2017_11_01.models.ConnectivitySource
    :param destination: Required.
    :type destination:
     ~azure.mgmt.network.v2017_11_01.models.ConnectivityDestination
    """

    _validation = {
        'source': {'required': True},
        'destination': {'required': True},
    }

    _attribute_map = {
        'source': {'key': 'source', 'type': 'ConnectivitySource'},
        'destination': {'key': 'destination', 'type': 'ConnectivityDestination'},
    }

    def __init__(self, *, source, destination, **kwargs) -> None:
        super(ConnectivityParameters, self).__init__(**kwargs)
        self.source = source
        self.destination = destination
