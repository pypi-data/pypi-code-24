# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class DomainOrganizationRoleUpdate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DomainOrganizationRoleUpdate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'description': 'str',
            'default_role_id': 'str',
            'permissions': 'list[str]',
            'permission_policies': 'list[DomainPermissionPolicy]',
            'user_count': 'int',
            'role_needs_update': 'bool',
            'default': 'bool',
            'base': 'bool',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'default_role_id': 'defaultRoleId',
            'permissions': 'permissions',
            'permission_policies': 'permissionPolicies',
            'user_count': 'userCount',
            'role_needs_update': 'roleNeedsUpdate',
            'default': 'default',
            'base': 'base',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._name = None
        self._description = None
        self._default_role_id = None
        self._permissions = None
        self._permission_policies = None
        self._user_count = None
        self._role_needs_update = None
        self._default = None
        self._base = None
        self._self_uri = None

    @property
    def id(self):
        """
        Gets the id of this DomainOrganizationRoleUpdate.
        The globally unique identifier for the object.

        :return: The id of this DomainOrganizationRoleUpdate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DomainOrganizationRoleUpdate.
        The globally unique identifier for the object.

        :param id: The id of this DomainOrganizationRoleUpdate.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this DomainOrganizationRoleUpdate.
        The name of the role

        :return: The name of this DomainOrganizationRoleUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DomainOrganizationRoleUpdate.
        The name of the role

        :param name: The name of this DomainOrganizationRoleUpdate.
        :type: str
        """
        
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this DomainOrganizationRoleUpdate.


        :return: The description of this DomainOrganizationRoleUpdate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DomainOrganizationRoleUpdate.


        :param description: The description of this DomainOrganizationRoleUpdate.
        :type: str
        """
        
        self._description = description

    @property
    def default_role_id(self):
        """
        Gets the default_role_id of this DomainOrganizationRoleUpdate.


        :return: The default_role_id of this DomainOrganizationRoleUpdate.
        :rtype: str
        """
        return self._default_role_id

    @default_role_id.setter
    def default_role_id(self, default_role_id):
        """
        Sets the default_role_id of this DomainOrganizationRoleUpdate.


        :param default_role_id: The default_role_id of this DomainOrganizationRoleUpdate.
        :type: str
        """
        
        self._default_role_id = default_role_id

    @property
    def permissions(self):
        """
        Gets the permissions of this DomainOrganizationRoleUpdate.


        :return: The permissions of this DomainOrganizationRoleUpdate.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this DomainOrganizationRoleUpdate.


        :param permissions: The permissions of this DomainOrganizationRoleUpdate.
        :type: list[str]
        """
        
        self._permissions = permissions

    @property
    def permission_policies(self):
        """
        Gets the permission_policies of this DomainOrganizationRoleUpdate.


        :return: The permission_policies of this DomainOrganizationRoleUpdate.
        :rtype: list[DomainPermissionPolicy]
        """
        return self._permission_policies

    @permission_policies.setter
    def permission_policies(self, permission_policies):
        """
        Sets the permission_policies of this DomainOrganizationRoleUpdate.


        :param permission_policies: The permission_policies of this DomainOrganizationRoleUpdate.
        :type: list[DomainPermissionPolicy]
        """
        
        self._permission_policies = permission_policies

    @property
    def user_count(self):
        """
        Gets the user_count of this DomainOrganizationRoleUpdate.


        :return: The user_count of this DomainOrganizationRoleUpdate.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """
        Sets the user_count of this DomainOrganizationRoleUpdate.


        :param user_count: The user_count of this DomainOrganizationRoleUpdate.
        :type: int
        """
        
        self._user_count = user_count

    @property
    def role_needs_update(self):
        """
        Gets the role_needs_update of this DomainOrganizationRoleUpdate.
        Optional unless patch operation.

        :return: The role_needs_update of this DomainOrganizationRoleUpdate.
        :rtype: bool
        """
        return self._role_needs_update

    @role_needs_update.setter
    def role_needs_update(self, role_needs_update):
        """
        Sets the role_needs_update of this DomainOrganizationRoleUpdate.
        Optional unless patch operation.

        :param role_needs_update: The role_needs_update of this DomainOrganizationRoleUpdate.
        :type: bool
        """
        
        self._role_needs_update = role_needs_update

    @property
    def default(self):
        """
        Gets the default of this DomainOrganizationRoleUpdate.


        :return: The default of this DomainOrganizationRoleUpdate.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this DomainOrganizationRoleUpdate.


        :param default: The default of this DomainOrganizationRoleUpdate.
        :type: bool
        """
        
        self._default = default

    @property
    def base(self):
        """
        Gets the base of this DomainOrganizationRoleUpdate.


        :return: The base of this DomainOrganizationRoleUpdate.
        :rtype: bool
        """
        return self._base

    @base.setter
    def base(self, base):
        """
        Sets the base of this DomainOrganizationRoleUpdate.


        :param base: The base of this DomainOrganizationRoleUpdate.
        :type: bool
        """
        
        self._base = base

    @property
    def self_uri(self):
        """
        Gets the self_uri of this DomainOrganizationRoleUpdate.
        The URI for this object

        :return: The self_uri of this DomainOrganizationRoleUpdate.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri):
        """
        Sets the self_uri of this DomainOrganizationRoleUpdate.
        The URI for this object

        :param self_uri: The self_uri of this DomainOrganizationRoleUpdate.
        :type: str
        """
        
        self._self_uri = self_uri

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

