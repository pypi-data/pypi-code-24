# coding: utf-8

"""
    Flip API

    Description  # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: cloudsupport@telestream.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UpdateEncodingBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'profile_id': 'str',
        'profile_name': 'str'
    }

    attribute_map = {
        'profile_id': 'profile_id',
        'profile_name': 'profile_name'
    }

    def __init__(self, profile_id=None, profile_name=None):  # noqa: E501
        """UpdateEncodingBody - a model defined in Swagger"""  # noqa: E501

        self._profile_id = None
        self._profile_name = None
        self.discriminator = None

        if profile_id is not None:
            self.profile_id = profile_id
        if profile_name is not None:
            self.profile_name = profile_name

    @property
    def profile_id(self):
        """Gets the profile_id of this UpdateEncodingBody.  # noqa: E501

        Id of a Profile that will be used for encoding.  # noqa: E501

        :return: The profile_id of this UpdateEncodingBody.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this UpdateEncodingBody.

        Id of a Profile that will be used for encoding.  # noqa: E501

        :param profile_id: The profile_id of this UpdateEncodingBody.  # noqa: E501
        :type: str
        """

        self._profile_id = profile_id

    @property
    def profile_name(self):
        """Gets the profile_name of this UpdateEncodingBody.  # noqa: E501

        A name of a Profile that will be used for encoding.  # noqa: E501

        :return: The profile_name of this UpdateEncodingBody.  # noqa: E501
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """Sets the profile_name of this UpdateEncodingBody.

        A name of a Profile that will be used for encoding.  # noqa: E501

        :param profile_name: The profile_name of this UpdateEncodingBody.  # noqa: E501
        :type: str
        """

        self._profile_name = profile_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateEncodingBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
