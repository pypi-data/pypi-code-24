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


class GroupSummary(object):
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
        'user_count': 'int',
        'account_id': 'str',
        'created_at': 'datetime',
        'object': 'str',
        'updated_at': 'datetime',
        'etag': 'str',
        'apikey_count': 'int',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'user_count': 'user_count',
        'account_id': 'account_id',
        'created_at': 'created_at',
        'object': 'object',
        'updated_at': 'updated_at',
        'etag': 'etag',
        'apikey_count': 'apikey_count',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, user_count=None, account_id=None, created_at=None, object=None, updated_at=None, etag=None, apikey_count=None, id=None, name=None):
        """
        GroupSummary - a model defined in Swagger
        """

        self._user_count = user_count
        self._account_id = account_id
        self._created_at = created_at
        self._object = object
        self._updated_at = updated_at
        self._etag = etag
        self._apikey_count = apikey_count
        self._id = id
        self._name = name
        self.discriminator = None

    @property
    def user_count(self):
        """
        Gets the user_count of this GroupSummary.
        The number of users in this group.

        :return: The user_count of this GroupSummary.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """
        Sets the user_count of this GroupSummary.
        The number of users in this group.

        :param user_count: The user_count of this GroupSummary.
        :type: int
        """
        if user_count is None:
            raise ValueError("Invalid value for `user_count`, must not be `None`")

        self._user_count = user_count

    @property
    def account_id(self):
        """
        Gets the account_id of this GroupSummary.
        The UUID of the account this group belongs to.

        :return: The account_id of this GroupSummary.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this GroupSummary.
        The UUID of the account this group belongs to.

        :param account_id: The account_id of this GroupSummary.
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")

        self._account_id = account_id

    @property
    def created_at(self):
        """
        Gets the created_at of this GroupSummary.
        Creation UTC time RFC3339.

        :return: The created_at of this GroupSummary.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this GroupSummary.
        Creation UTC time RFC3339.

        :param created_at: The created_at of this GroupSummary.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def object(self):
        """
        Gets the object of this GroupSummary.
        Entity name: always 'group'

        :return: The object of this GroupSummary.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this GroupSummary.
        Entity name: always 'group'

        :param object: The object of this GroupSummary.
        :type: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")
        allowed_values = ["group"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def updated_at(self):
        """
        Gets the updated_at of this GroupSummary.
        Last update UTC time RFC3339.

        :return: The updated_at of this GroupSummary.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this GroupSummary.
        Last update UTC time RFC3339.

        :param updated_at: The updated_at of this GroupSummary.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def etag(self):
        """
        Gets the etag of this GroupSummary.
        API resource entity version.

        :return: The etag of this GroupSummary.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this GroupSummary.
        API resource entity version.

        :param etag: The etag of this GroupSummary.
        :type: str
        """
        if etag is None:
            raise ValueError("Invalid value for `etag`, must not be `None`")

        self._etag = etag

    @property
    def apikey_count(self):
        """
        Gets the apikey_count of this GroupSummary.
        The number of API keys in this group.

        :return: The apikey_count of this GroupSummary.
        :rtype: int
        """
        return self._apikey_count

    @apikey_count.setter
    def apikey_count(self, apikey_count):
        """
        Sets the apikey_count of this GroupSummary.
        The number of API keys in this group.

        :param apikey_count: The apikey_count of this GroupSummary.
        :type: int
        """
        if apikey_count is None:
            raise ValueError("Invalid value for `apikey_count`, must not be `None`")

        self._apikey_count = apikey_count

    @property
    def id(self):
        """
        Gets the id of this GroupSummary.
        The UUID of the group.

        :return: The id of this GroupSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GroupSummary.
        The UUID of the group.

        :param id: The id of this GroupSummary.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this GroupSummary.
        The name of the group.

        :return: The name of this GroupSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GroupSummary.
        The name of the group.

        :param name: The name of this GroupSummary.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

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
        if not isinstance(other, GroupSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
