# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VirtualCircuitPublicPrefix(object):

    def __init__(self, **kwargs):
        """
        Initializes a new VirtualCircuitPublicPrefix object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cidr_block:
            The value to assign to the cidr_block property of this VirtualCircuitPublicPrefix.
        :type cidr_block: str

        :param verification_state:
            The value to assign to the verification_state property of this VirtualCircuitPublicPrefix.
            Allowed values for this property are: "IN_PROGRESS", "COMPLETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type verification_state: str

        """
        self.swagger_types = {
            'cidr_block': 'str',
            'verification_state': 'str'
        }

        self.attribute_map = {
            'cidr_block': 'cidrBlock',
            'verification_state': 'verificationState'
        }

        self._cidr_block = None
        self._verification_state = None

    @property
    def cidr_block(self):
        """
        **[Required]** Gets the cidr_block of this VirtualCircuitPublicPrefix.
        Publix IP prefix (CIDR) that the customer specified.


        :return: The cidr_block of this VirtualCircuitPublicPrefix.
        :rtype: str
        """
        return self._cidr_block

    @cidr_block.setter
    def cidr_block(self, cidr_block):
        """
        Sets the cidr_block of this VirtualCircuitPublicPrefix.
        Publix IP prefix (CIDR) that the customer specified.


        :param cidr_block: The cidr_block of this VirtualCircuitPublicPrefix.
        :type: str
        """
        self._cidr_block = cidr_block

    @property
    def verification_state(self):
        """
        **[Required]** Gets the verification_state of this VirtualCircuitPublicPrefix.
        Oracle must verify that the customer owns the public IP prefix before traffic
        for that prefix can flow across the virtual circuit. Verification can take a
        few business days. `IN_PROGRESS` means Oracle is verifying the prefix. `COMPLETED`
        means verification succeeded. `FAILED` means verification failed and traffic for
        this prefix will not flow across the connection.

        Allowed values for this property are: "IN_PROGRESS", "COMPLETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The verification_state of this VirtualCircuitPublicPrefix.
        :rtype: str
        """
        return self._verification_state

    @verification_state.setter
    def verification_state(self, verification_state):
        """
        Sets the verification_state of this VirtualCircuitPublicPrefix.
        Oracle must verify that the customer owns the public IP prefix before traffic
        for that prefix can flow across the virtual circuit. Verification can take a
        few business days. `IN_PROGRESS` means Oracle is verifying the prefix. `COMPLETED`
        means verification succeeded. `FAILED` means verification failed and traffic for
        this prefix will not flow across the connection.


        :param verification_state: The verification_state of this VirtualCircuitPublicPrefix.
        :type: str
        """
        allowed_values = ["IN_PROGRESS", "COMPLETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(verification_state, allowed_values):
            verification_state = 'UNKNOWN_ENUM_VALUE'
        self._verification_state = verification_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
