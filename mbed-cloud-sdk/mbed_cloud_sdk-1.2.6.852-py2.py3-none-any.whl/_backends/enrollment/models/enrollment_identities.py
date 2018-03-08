# coding: utf-8

"""
    Enrollment API

    Mbed Cloud Connect Enrollment Service allows users to claim the ownership of a device which is not yet assigned to an account. A device without an assigned account can be a device purchased from the open market (OEM dealer) or a device trasferred from an account to another. More information in [Device overship: First-to-claim](TODO: link needed) document. 

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class EnrollmentIdentities(object):
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
        'after': 'str',
        'has_more': 'bool',
        'total_count': 'int',
        'object': 'str',
        'limit': 'int',
        'data': 'list[EnrollmentIdentity]',
        'order': 'str'
    }

    attribute_map = {
        'after': 'after',
        'has_more': 'has_more',
        'total_count': 'total_count',
        'object': 'object',
        'limit': 'limit',
        'data': 'data',
        'order': 'order'
    }

    def __init__(self, after=None, has_more=None, total_count=None, object=None, limit=None, data=None, order='ASC'):
        """
        EnrollmentIdentities - a model defined in Swagger
        """

        self._after = after
        self._has_more = has_more
        self._total_count = total_count
        self._object = object
        self._limit = limit
        self._data = data
        self._order = order
        self.discriminator = None

    @property
    def after(self):
        """
        Gets the after of this EnrollmentIdentities.
        muuid

        :return: The after of this EnrollmentIdentities.
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """
        Sets the after of this EnrollmentIdentities.
        muuid

        :param after: The after of this EnrollmentIdentities.
        :type: str
        """
        if after is None:
            raise ValueError("Invalid value for `after`, must not be `None`")
        if after is not None and not re.search('^[A-Za-z0-9]{32}', after):
            raise ValueError("Invalid value for `after`, must be a follow pattern or equal to `/^[A-Za-z0-9]{32}/`")

        self._after = after

    @property
    def has_more(self):
        """
        Gets the has_more of this EnrollmentIdentities.

        :return: The has_more of this EnrollmentIdentities.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more):
        """
        Sets the has_more of this EnrollmentIdentities.

        :param has_more: The has_more of this EnrollmentIdentities.
        :type: bool
        """
        if has_more is None:
            raise ValueError("Invalid value for `has_more`, must not be `None`")

        self._has_more = has_more

    @property
    def total_count(self):
        """
        Gets the total_count of this EnrollmentIdentities.

        :return: The total_count of this EnrollmentIdentities.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this EnrollmentIdentities.

        :param total_count: The total_count of this EnrollmentIdentities.
        :type: int
        """
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")
        if total_count is not None and total_count < 1:
            raise ValueError("Invalid value for `total_count`, must be a value greater than or equal to `1`")

        self._total_count = total_count

    @property
    def object(self):
        """
        Gets the object of this EnrollmentIdentities.

        :return: The object of this EnrollmentIdentities.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this EnrollmentIdentities.

        :param object: The object of this EnrollmentIdentities.
        :type: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")
        allowed_values = ["list"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def limit(self):
        """
        Gets the limit of this EnrollmentIdentities.
        Range 2-1000, or default.

        :return: The limit of this EnrollmentIdentities.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this EnrollmentIdentities.
        Range 2-1000, or default.

        :param limit: The limit of this EnrollmentIdentities.
        :type: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")
        if limit is not None and limit > 1000:
            raise ValueError("Invalid value for `limit`, must be a value less than or equal to `1000`")
        if limit is not None and limit < 2:
            raise ValueError("Invalid value for `limit`, must be a value greater than or equal to `2`")

        self._limit = limit

    @property
    def data(self):
        """
        Gets the data of this EnrollmentIdentities.

        :return: The data of this EnrollmentIdentities.
        :rtype: list[EnrollmentIdentity]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this EnrollmentIdentities.

        :param data: The data of this EnrollmentIdentities.
        :type: list[EnrollmentIdentity]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def order(self):
        """
        Gets the order of this EnrollmentIdentities.

        :return: The order of this EnrollmentIdentities.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this EnrollmentIdentities.

        :param order: The order of this EnrollmentIdentities.
        :type: str
        """
        if order is None:
            raise ValueError("Invalid value for `order`, must not be `None`")
        allowed_values = ["ASC", "DESC"]
        if order not in allowed_values:
            raise ValueError(
                "Invalid value for `order` ({0}), must be one of {1}"
                .format(order, allowed_values)
            )

        self._order = order

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
        if not isinstance(other, EnrollmentIdentities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
