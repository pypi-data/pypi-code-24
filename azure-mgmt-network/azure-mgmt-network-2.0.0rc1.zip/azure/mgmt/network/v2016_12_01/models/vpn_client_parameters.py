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


class VpnClientParameters(Model):
    """VpnClientParameters.

    All required parameters must be populated in order to send to Azure.

    :param processor_architecture: Required. VPN client Processor
     Architecture. Possible values are: 'AMD64' and 'X86'. Possible values
     include: 'Amd64', 'X86'
    :type processor_architecture: str or
     ~azure.mgmt.network.v2016_12_01.models.ProcessorArchitecture
    """

    _validation = {
        'processor_architecture': {'required': True},
    }

    _attribute_map = {
        'processor_architecture': {'key': 'ProcessorArchitecture', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(VpnClientParameters, self).__init__(**kwargs)
        self.processor_architecture = kwargs.get('processor_architecture', None)
