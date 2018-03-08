# coding: utf-8

"""
    Account Management API

    API for managing accounts, users, creating API keys, uploading trusted certificates

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UserUpdateReq(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'phone_number': 'str',
        'username': 'str',
        'groups': 'list[str]',
        'is_marketing_accepted': 'bool',
        'user_properties': 'dict(str, dict(str, str))',
        'is_gtc_accepted': 'bool',
        'is_totp_enabled': 'bool',
        'status': 'str',
        'full_name': 'str',
        'address': 'str',
        'password': 'str',
        'email': 'str'
    }

    attribute_map = {
        'phone_number': 'phone_number',
        'username': 'username',
        'groups': 'groups',
        'is_marketing_accepted': 'is_marketing_accepted',
        'user_properties': 'user_properties',
        'is_gtc_accepted': 'is_gtc_accepted',
        'is_totp_enabled': 'is_totp_enabled',
        'status': 'status',
        'full_name': 'full_name',
        'address': 'address',
        'password': 'password',
        'email': 'email'
    }

    def __init__(self, phone_number=None, username=None, groups=None, is_marketing_accepted=None, user_properties=None, is_gtc_accepted=None, is_totp_enabled=None, status=None, full_name=None, address=None, password=None, email=None):
        """
        UserUpdateReq - a model defined in Swagger
        """

        self._phone_number = phone_number
        self._username = username
        self._groups = groups
        self._is_marketing_accepted = is_marketing_accepted
        self._user_properties = user_properties
        self._is_gtc_accepted = is_gtc_accepted
        self._is_totp_enabled = is_totp_enabled
        self._status = status
        self._full_name = full_name
        self._address = address
        self._password = password
        self._email = email
        self.discriminator = None

    @property
    def phone_number(self):
        """
        Gets the phone_number of this UserUpdateReq.
        Phone number, not longer than 100 characters.

        :return: The phone_number of this UserUpdateReq.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this UserUpdateReq.
        Phone number, not longer than 100 characters.

        :param phone_number: The phone_number of this UserUpdateReq.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def username(self):
        """
        Gets the username of this UserUpdateReq.
        A username containing alphanumerical letters and -,._@+= characters. It must be at least 4 but not more than 30 character long.

        :return: The username of this UserUpdateReq.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UserUpdateReq.
        A username containing alphanumerical letters and -,._@+= characters. It must be at least 4 but not more than 30 character long.

        :param username: The username of this UserUpdateReq.
        :type: str
        """

        self._username = username

    @property
    def groups(self):
        """
        Gets the groups of this UserUpdateReq.
        A list of group IDs this user belongs to.

        :return: The groups of this UserUpdateReq.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this UserUpdateReq.
        A list of group IDs this user belongs to.

        :param groups: The groups of this UserUpdateReq.
        :type: list[str]
        """

        self._groups = groups

    @property
    def is_marketing_accepted(self):
        """
        Gets the is_marketing_accepted of this UserUpdateReq.
        A flag indicating that receiving marketing information has been accepted.

        :return: The is_marketing_accepted of this UserUpdateReq.
        :rtype: bool
        """
        return self._is_marketing_accepted

    @is_marketing_accepted.setter
    def is_marketing_accepted(self, is_marketing_accepted):
        """
        Sets the is_marketing_accepted of this UserUpdateReq.
        A flag indicating that receiving marketing information has been accepted.

        :param is_marketing_accepted: The is_marketing_accepted of this UserUpdateReq.
        :type: bool
        """

        self._is_marketing_accepted = is_marketing_accepted

    @property
    def user_properties(self):
        """
        Gets the user_properties of this UserUpdateReq.
        User's account specific custom properties.

        :return: The user_properties of this UserUpdateReq.
        :rtype: dict(str, dict(str, str))
        """
        return self._user_properties

    @user_properties.setter
    def user_properties(self, user_properties):
        """
        Sets the user_properties of this UserUpdateReq.
        User's account specific custom properties.

        :param user_properties: The user_properties of this UserUpdateReq.
        :type: dict(str, dict(str, str))
        """

        self._user_properties = user_properties

    @property
    def is_gtc_accepted(self):
        """
        Gets the is_gtc_accepted of this UserUpdateReq.
        A flag indicating that the General Terms and Conditions has been accepted.

        :return: The is_gtc_accepted of this UserUpdateReq.
        :rtype: bool
        """
        return self._is_gtc_accepted

    @is_gtc_accepted.setter
    def is_gtc_accepted(self, is_gtc_accepted):
        """
        Sets the is_gtc_accepted of this UserUpdateReq.
        A flag indicating that the General Terms and Conditions has been accepted.

        :param is_gtc_accepted: The is_gtc_accepted of this UserUpdateReq.
        :type: bool
        """

        self._is_gtc_accepted = is_gtc_accepted

    @property
    def is_totp_enabled(self):
        """
        Gets the is_totp_enabled of this UserUpdateReq.
        A flag indicating whether 2-factor authentication (TOTP) has to be enabled or disabled.

        :return: The is_totp_enabled of this UserUpdateReq.
        :rtype: bool
        """
        return self._is_totp_enabled

    @is_totp_enabled.setter
    def is_totp_enabled(self, is_totp_enabled):
        """
        Sets the is_totp_enabled of this UserUpdateReq.
        A flag indicating whether 2-factor authentication (TOTP) has to be enabled or disabled.

        :param is_totp_enabled: The is_totp_enabled of this UserUpdateReq.
        :type: bool
        """

        self._is_totp_enabled = is_totp_enabled

    @property
    def status(self):
        """
        Gets the status of this UserUpdateReq.
        The status of the user.

        :return: The status of this UserUpdateReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this UserUpdateReq.
        The status of the user.

        :param status: The status of this UserUpdateReq.
        :type: str
        """

        self._status = status

    @property
    def full_name(self):
        """
        Gets the full_name of this UserUpdateReq.
        The full name of the user, not longer than 100 characters.

        :return: The full_name of this UserUpdateReq.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """
        Sets the full_name of this UserUpdateReq.
        The full name of the user, not longer than 100 characters.

        :param full_name: The full_name of this UserUpdateReq.
        :type: str
        """

        self._full_name = full_name

    @property
    def address(self):
        """
        Gets the address of this UserUpdateReq.
        Address, not longer than 100 characters.

        :return: The address of this UserUpdateReq.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this UserUpdateReq.
        Address, not longer than 100 characters.

        :param address: The address of this UserUpdateReq.
        :type: str
        """

        self._address = address

    @property
    def password(self):
        """
        Gets the password of this UserUpdateReq.
        The password when creating a new user. It will be generated when not present in the request.

        :return: The password of this UserUpdateReq.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UserUpdateReq.
        The password when creating a new user. It will be generated when not present in the request.

        :param password: The password of this UserUpdateReq.
        :type: str
        """

        self._password = password

    @property
    def email(self):
        """
        Gets the email of this UserUpdateReq.
        The email address, not longer than 254 characters.

        :return: The email of this UserUpdateReq.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UserUpdateReq.
        The email address, not longer than 254 characters.

        :param email: The email of this UserUpdateReq.
        :type: str
        """

        self._email = email

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, UserUpdateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
