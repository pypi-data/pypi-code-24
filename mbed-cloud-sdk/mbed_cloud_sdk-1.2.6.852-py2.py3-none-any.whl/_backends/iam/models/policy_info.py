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


class PolicyInfo(object):
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
        'valid_until': 'datetime',
        'grant_expires_in': 'int',
        'updated_at': 'datetime',
        'actions': 'dict(str, bool)',
        'tag': 'str',
        'apikeys': 'list[str]',
        'id': 'str',
        'users': 'list[str]',
        'valid_from': 'datetime',
        'etag': 'str',
        'account_id': 'str',
        'conditions': 'list[str]',
        'resources': 'list[str]',
        'status': 'str',
        'description': 'str',
        'object': 'str',
        'groups': 'list[str]',
        'not_actions': 'list[str]',
        'not_resources': 'list[str]',
        'name': 'str',
        'created_at': 'datetime',
        'error_message': 'str',
        'not_conditions': 'list[str]'
    }

    attribute_map = {
        'valid_until': 'valid_until',
        'grant_expires_in': 'grant_expires_in',
        'updated_at': 'updated_at',
        'actions': 'actions',
        'tag': 'tag',
        'apikeys': 'apikeys',
        'id': 'id',
        'users': 'users',
        'valid_from': 'valid_from',
        'etag': 'etag',
        'account_id': 'account_id',
        'conditions': 'conditions',
        'resources': 'resources',
        'status': 'status',
        'description': 'description',
        'object': 'object',
        'groups': 'groups',
        'not_actions': 'notActions',
        'not_resources': 'notResources',
        'name': 'name',
        'created_at': 'created_at',
        'error_message': 'error_message',
        'not_conditions': 'notConditions'
    }

    def __init__(self, valid_until=None, grant_expires_in=None, updated_at=None, actions=None, tag=None, apikeys=None, id=None, users=None, valid_from=None, etag=None, account_id=None, conditions=None, resources=None, status=None, description=None, object=None, groups=None, not_actions=None, not_resources=None, name=None, created_at=None, error_message=None, not_conditions=None):
        """
        PolicyInfo - a model defined in Swagger
        """

        self._valid_until = valid_until
        self._grant_expires_in = grant_expires_in
        self._updated_at = updated_at
        self._actions = actions
        self._tag = tag
        self._apikeys = apikeys
        self._id = id
        self._users = users
        self._valid_from = valid_from
        self._etag = etag
        self._account_id = account_id
        self._conditions = conditions
        self._resources = resources
        self._status = status
        self._description = description
        self._object = object
        self._groups = groups
        self._not_actions = not_actions
        self._not_resources = not_resources
        self._name = name
        self._created_at = created_at
        self._error_message = error_message
        self._not_conditions = not_conditions
        self.discriminator = None

    @property
    def valid_until(self):
        """
        Gets the valid_until of this PolicyInfo.
        Specifies the date and time until the policy is valid.

        :return: The valid_until of this PolicyInfo.
        :rtype: datetime
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """
        Sets the valid_until of this PolicyInfo.
        Specifies the date and time until the policy is valid.

        :param valid_until: The valid_until of this PolicyInfo.
        :type: datetime
        """

        self._valid_until = valid_until

    @property
    def grant_expires_in(self):
        """
        Gets the grant_expires_in of this PolicyInfo.
        Specifies the value in seconds for how long an authorization result is valid.

        :return: The grant_expires_in of this PolicyInfo.
        :rtype: int
        """
        return self._grant_expires_in

    @grant_expires_in.setter
    def grant_expires_in(self, grant_expires_in):
        """
        Sets the grant_expires_in of this PolicyInfo.
        Specifies the value in seconds for how long an authorization result is valid.

        :param grant_expires_in: The grant_expires_in of this PolicyInfo.
        :type: int
        """

        self._grant_expires_in = grant_expires_in

    @property
    def updated_at(self):
        """
        Gets the updated_at of this PolicyInfo.
        Last update UTC time RFC3339.

        :return: The updated_at of this PolicyInfo.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this PolicyInfo.
        Last update UTC time RFC3339.

        :param updated_at: The updated_at of this PolicyInfo.
        :type: datetime
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")

        self._updated_at = updated_at

    @property
    def actions(self):
        """
        Gets the actions of this PolicyInfo.
        List of actions.

        :return: The actions of this PolicyInfo.
        :rtype: dict(str, bool)
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this PolicyInfo.
        List of actions.

        :param actions: The actions of this PolicyInfo.
        :type: dict(str, bool)
        """
        if actions is None:
            raise ValueError("Invalid value for `actions`, must not be `None`")

        self._actions = actions

    @property
    def tag(self):
        """
        Gets the tag of this PolicyInfo.
        Policy tag that can be used for various purposes to be able to distinguish between policies.

        :return: The tag of this PolicyInfo.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this PolicyInfo.
        Policy tag that can be used for various purposes to be able to distinguish between policies.

        :param tag: The tag of this PolicyInfo.
        :type: str
        """

        self._tag = tag

    @property
    def apikeys(self):
        """
        Gets the apikeys of this PolicyInfo.
        List of API key IDs this policy is attached to.

        :return: The apikeys of this PolicyInfo.
        :rtype: list[str]
        """
        return self._apikeys

    @apikeys.setter
    def apikeys(self, apikeys):
        """
        Sets the apikeys of this PolicyInfo.
        List of API key IDs this policy is attached to.

        :param apikeys: The apikeys of this PolicyInfo.
        :type: list[str]
        """

        self._apikeys = apikeys

    @property
    def id(self):
        """
        Gets the id of this PolicyInfo.
        Entity ID.

        :return: The id of this PolicyInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PolicyInfo.
        Entity ID.

        :param id: The id of this PolicyInfo.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def users(self):
        """
        Gets the users of this PolicyInfo.
        List of user IDs this policy is attached to.

        :return: The users of this PolicyInfo.
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """
        Sets the users of this PolicyInfo.
        List of user IDs this policy is attached to.

        :param users: The users of this PolicyInfo.
        :type: list[str]
        """

        self._users = users

    @property
    def valid_from(self):
        """
        Gets the valid_from of this PolicyInfo.
        Specifies the date and time when the policy will become valid.

        :return: The valid_from of this PolicyInfo.
        :rtype: datetime
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """
        Sets the valid_from of this PolicyInfo.
        Specifies the date and time when the policy will become valid.

        :param valid_from: The valid_from of this PolicyInfo.
        :type: datetime
        """

        self._valid_from = valid_from

    @property
    def etag(self):
        """
        Gets the etag of this PolicyInfo.
        API resource entity version.

        :return: The etag of this PolicyInfo.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this PolicyInfo.
        API resource entity version.

        :param etag: The etag of this PolicyInfo.
        :type: str
        """
        if etag is None:
            raise ValueError("Invalid value for `etag`, must not be `None`")

        self._etag = etag

    @property
    def account_id(self):
        """
        Gets the account_id of this PolicyInfo.
        The UUID of the account.

        :return: The account_id of this PolicyInfo.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this PolicyInfo.
        The UUID of the account.

        :param account_id: The account_id of this PolicyInfo.
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")

        self._account_id = account_id

    @property
    def conditions(self):
        """
        Gets the conditions of this PolicyInfo.
        List of conditions.

        :return: The conditions of this PolicyInfo.
        :rtype: list[str]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this PolicyInfo.
        List of conditions.

        :param conditions: The conditions of this PolicyInfo.
        :type: list[str]
        """
        if conditions is None:
            raise ValueError("Invalid value for `conditions`, must not be `None`")

        self._conditions = conditions

    @property
    def resources(self):
        """
        Gets the resources of this PolicyInfo.
        List of resources.

        :return: The resources of this PolicyInfo.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this PolicyInfo.
        List of resources.

        :param resources: The resources of this PolicyInfo.
        :type: list[str]
        """
        if resources is None:
            raise ValueError("Invalid value for `resources`, must not be `None`")

        self._resources = resources

    @property
    def status(self):
        """
        Gets the status of this PolicyInfo.
        The status of this policy.

        :return: The status of this PolicyInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this PolicyInfo.
        The status of this policy.

        :param status: The status of this PolicyInfo.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        allowed_values = ["ACTIVE", "INACTIVE"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def description(self):
        """
        Gets the description of this PolicyInfo.
        The description of this policy.

        :return: The description of this PolicyInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PolicyInfo.
        The description of this policy.

        :param description: The description of this PolicyInfo.
        :type: str
        """

        self._description = description

    @property
    def object(self):
        """
        Gets the object of this PolicyInfo.
        Entity name: always 'policy'

        :return: The object of this PolicyInfo.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this PolicyInfo.
        Entity name: always 'policy'

        :param object: The object of this PolicyInfo.
        :type: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")
        allowed_values = ["policy"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def groups(self):
        """
        Gets the groups of this PolicyInfo.
        List of group IDs this policy is attached to.

        :return: The groups of this PolicyInfo.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this PolicyInfo.
        List of group IDs this policy is attached to.

        :param groups: The groups of this PolicyInfo.
        :type: list[str]
        """

        self._groups = groups

    @property
    def not_actions(self):
        """
        Gets the not_actions of this PolicyInfo.
        List of not_actions.

        :return: The not_actions of this PolicyInfo.
        :rtype: list[str]
        """
        return self._not_actions

    @not_actions.setter
    def not_actions(self, not_actions):
        """
        Sets the not_actions of this PolicyInfo.
        List of not_actions.

        :param not_actions: The not_actions of this PolicyInfo.
        :type: list[str]
        """
        if not_actions is None:
            raise ValueError("Invalid value for `not_actions`, must not be `None`")

        self._not_actions = not_actions

    @property
    def not_resources(self):
        """
        Gets the not_resources of this PolicyInfo.
        List of not_resources.

        :return: The not_resources of this PolicyInfo.
        :rtype: list[str]
        """
        return self._not_resources

    @not_resources.setter
    def not_resources(self, not_resources):
        """
        Sets the not_resources of this PolicyInfo.
        List of not_resources.

        :param not_resources: The not_resources of this PolicyInfo.
        :type: list[str]
        """
        if not_resources is None:
            raise ValueError("Invalid value for `not_resources`, must not be `None`")

        self._not_resources = not_resources

    @property
    def name(self):
        """
        Gets the name of this PolicyInfo.
        The name of this policy.

        :return: The name of this PolicyInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PolicyInfo.
        The name of this policy.

        :param name: The name of this PolicyInfo.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def created_at(self):
        """
        Gets the created_at of this PolicyInfo.
        Creation UTC time RFC3339.

        :return: The created_at of this PolicyInfo.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this PolicyInfo.
        Creation UTC time RFC3339.

        :param created_at: The created_at of this PolicyInfo.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def error_message(self):
        """
        Gets the error_message of this PolicyInfo.
        Custom error message returned when this policy matches with not allowed result.

        :return: The error_message of this PolicyInfo.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this PolicyInfo.
        Custom error message returned when this policy matches with not allowed result.

        :param error_message: The error_message of this PolicyInfo.
        :type: str
        """

        self._error_message = error_message

    @property
    def not_conditions(self):
        """
        Gets the not_conditions of this PolicyInfo.
        List of not_conditions.

        :return: The not_conditions of this PolicyInfo.
        :rtype: list[str]
        """
        return self._not_conditions

    @not_conditions.setter
    def not_conditions(self, not_conditions):
        """
        Sets the not_conditions of this PolicyInfo.
        List of not_conditions.

        :param not_conditions: The not_conditions of this PolicyInfo.
        :type: list[str]
        """
        if not_conditions is None:
            raise ValueError("Invalid value for `not_conditions`, must not be `None`")

        self._not_conditions = not_conditions

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
        if not isinstance(other, PolicyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
