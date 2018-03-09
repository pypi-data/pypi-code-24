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


class EncodingSignedUrls(object):
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
        'signed_urls': 'list[str]'
    }

    attribute_map = {
        'signed_urls': 'signed_urls'
    }

    def __init__(self, signed_urls=None):  # noqa: E501
        """EncodingSignedUrls - a model defined in Swagger"""  # noqa: E501

        self._signed_urls = None
        self.discriminator = None

        if signed_urls is not None:
            self.signed_urls = signed_urls

    @property
    def signed_urls(self):
        """Gets the signed_urls of this EncodingSignedUrls.  # noqa: E501

        A list of signed URLs pointing to the encoding's outputs.  # noqa: E501

        :return: The signed_urls of this EncodingSignedUrls.  # noqa: E501
        :rtype: list[str]
        """
        return self._signed_urls

    @signed_urls.setter
    def signed_urls(self, signed_urls):
        """Sets the signed_urls of this EncodingSignedUrls.

        A list of signed URLs pointing to the encoding's outputs.  # noqa: E501

        :param signed_urls: The signed_urls of this EncodingSignedUrls.  # noqa: E501
        :type: list[str]
        """

        self._signed_urls = signed_urls

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
        if not isinstance(other, EncodingSignedUrls):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
