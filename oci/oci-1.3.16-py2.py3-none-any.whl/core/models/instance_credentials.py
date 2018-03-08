# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceCredentials(object):

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceCredentials object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param password:
            The value to assign to the password property of this InstanceCredentials.
        :type password: str

        :param username:
            The value to assign to the username property of this InstanceCredentials.
        :type username: str

        """
        self.swagger_types = {
            'password': 'str',
            'username': 'str'
        }

        self.attribute_map = {
            'password': 'password',
            'username': 'username'
        }

        self._password = None
        self._username = None

    @property
    def password(self):
        """
        **[Required]** Gets the password of this InstanceCredentials.
        The password for the username.


        :return: The password of this InstanceCredentials.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this InstanceCredentials.
        The password for the username.


        :param password: The password of this InstanceCredentials.
        :type: str
        """
        self._password = password

    @property
    def username(self):
        """
        **[Required]** Gets the username of this InstanceCredentials.
        The username.


        :return: The username of this InstanceCredentials.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this InstanceCredentials.
        The username.


        :param username: The username of this InstanceCredentials.
        :type: str
        """
        self._username = username

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
