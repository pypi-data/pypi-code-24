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


class AzureReachabilityReportLocation(Model):
    """Parameters that define a geographic location.

    All required parameters must be populated in order to send to Azure.

    :param country: Required. The name of the country.
    :type country: str
    :param state: The name of the state.
    :type state: str
    :param city: The name of the city or town.
    :type city: str
    """

    _validation = {
        'country': {'required': True},
    }

    _attribute_map = {
        'country': {'key': 'country', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'city': {'key': 'city', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AzureReachabilityReportLocation, self).__init__(**kwargs)
        self.country = kwargs.get('country', None)
        self.state = kwargs.get('state', None)
        self.city = kwargs.get('city', None)
