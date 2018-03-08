# coding: utf-8

"""
    Update Service API

    This is the API documentation for the Mbed deployment service, which is part of the update service.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FirmwareManifestGteLteFilter(object):
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
        'timestamp': 'datetime',
        'created_at': 'datetime',
        'etag': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'created_at': 'created_at',
        'etag': 'etag',
        'updated_at': 'updated_at'
    }

    def __init__(self, timestamp=None, created_at=None, etag=None, updated_at=None):
        """
        FirmwareManifestGteLteFilter - a model defined in Swagger
        """

        self._timestamp = timestamp
        self._created_at = created_at
        self._etag = etag
        self._updated_at = updated_at
        self.discriminator = None

    @property
    def timestamp(self):
        """
        Gets the timestamp of this FirmwareManifestGteLteFilter.

        :return: The timestamp of this FirmwareManifestGteLteFilter.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this FirmwareManifestGteLteFilter.

        :param timestamp: The timestamp of this FirmwareManifestGteLteFilter.
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def created_at(self):
        """
        Gets the created_at of this FirmwareManifestGteLteFilter.

        :return: The created_at of this FirmwareManifestGteLteFilter.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this FirmwareManifestGteLteFilter.

        :param created_at: The created_at of this FirmwareManifestGteLteFilter.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def etag(self):
        """
        Gets the etag of this FirmwareManifestGteLteFilter.

        :return: The etag of this FirmwareManifestGteLteFilter.
        :rtype: datetime
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this FirmwareManifestGteLteFilter.

        :param etag: The etag of this FirmwareManifestGteLteFilter.
        :type: datetime
        """

        self._etag = etag

    @property
    def updated_at(self):
        """
        Gets the updated_at of this FirmwareManifestGteLteFilter.

        :return: The updated_at of this FirmwareManifestGteLteFilter.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this FirmwareManifestGteLteFilter.

        :param updated_at: The updated_at of this FirmwareManifestGteLteFilter.
        :type: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, FirmwareManifestGteLteFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
