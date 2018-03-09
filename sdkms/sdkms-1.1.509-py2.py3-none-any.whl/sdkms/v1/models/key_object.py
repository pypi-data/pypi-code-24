# coding: utf-8

"""
    Fortanix SDKMS REST API

    This is a set of REST APIs for accessing the Fortanix Self-Defending Key Management System. This includes APIs for managing accounts, and for performing cryptographic and key management operations. 

    OpenAPI spec version: 1.0.0-20171218
    Contact: support@fortanix.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re




# NOTE: This class is auto generated by the swagger code generator program.
# Do not edit the class manually.
class KeyObject(object):
    """
    @undocumented: swagger_types
    @undocumented: attribute_map
    @undocumented: to_dict
    @undocumented: to_str
    @undocumented: __repr__
    @undocumented: __eq__
    @undocumented: __ne__
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'description': 'str',
        'key_size': 'int',
        'elliptic_curve': 'EllipticCurve',
        'acct_id': 'str',
        'group_id': 'str',
        'creator': 'CreatorType',
        'kid': 'str',
        'obj_type': 'ObjectType',
        'key_ops': 'list[KeyOperations]',
        'attributes': 'KeyAttributes',
        'custom_metadata': 'dict(str, str)',
        'origin': 'ObjectOrigin',
        'pub_key': 'bytearray',
        'value': 'bytearray',
        'enabled': 'bool',
        'created_at': 'str',
        'lastused_at': 'str',
        'transient_key': 'str',
        'never_exportable': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'key_size': 'key_size',
        'elliptic_curve': 'elliptic_curve',
        'acct_id': 'acct_id',
        'group_id': 'group_id',
        'creator': 'creator',
        'kid': 'kid',
        'obj_type': 'obj_type',
        'key_ops': 'key_ops',
        'attributes': 'attributes',
        'custom_metadata': 'custom_metadata',
        'origin': 'origin',
        'pub_key': 'pub_key',
        'value': 'value',
        'enabled': 'enabled',
        'created_at': 'created_at',
        'lastused_at': 'lastused_at',
        'transient_key': 'transient_key',
        'never_exportable': 'never_exportable'
    }

    def __init__(self, name=None, description=None, key_size=None, elliptic_curve=None, acct_id=None, group_id=None, creator=None, kid=None, obj_type=None, key_ops=None, attributes=None, custom_metadata=None, origin=None, pub_key=None, value=None, enabled=None, created_at=None, lastused_at=None, transient_key=None, never_exportable=None):
        """
        KeyObject - a model defined in Swagger
        """

        self._name = None
        self._description = None
        self._key_size = None
        self._elliptic_curve = None
        self._acct_id = None
        self._group_id = None
        self._creator = None
        self._kid = None
        self._obj_type = None
        self._key_ops = None
        self._attributes = None
        self._custom_metadata = None
        self._origin = None
        self._pub_key = None
        self._value = None
        self._enabled = None
        self._created_at = None
        self._lastused_at = None
        self._transient_key = None
        self._never_exportable = None

        self.name = name
        if description is not None:
          self.description = description
        if key_size is not None:
          self.key_size = key_size
        if elliptic_curve is not None:
          self.elliptic_curve = elliptic_curve
        self.acct_id = acct_id
        if group_id is not None:
          self.group_id = group_id
        self.creator = creator
        if kid is not None:
          self.kid = kid
        self.obj_type = obj_type
        if key_ops is not None:
          self.key_ops = key_ops
        if attributes is not None:
          self.attributes = attributes
        if custom_metadata is not None:
          self.custom_metadata = custom_metadata
        self.origin = origin
        if pub_key is not None:
          self.pub_key = pub_key
        if value is not None:
          self.value = value
        self.enabled = enabled
        self.created_at = created_at
        self.lastused_at = lastused_at
        if transient_key is not None:
          self.transient_key = transient_key
        self.never_exportable = never_exportable

    @property
    def name(self):
        """
        Gets the name of this KeyObject.
        Name of the security object.

        Type: L{str}
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this KeyObject.
        Name of the security object.
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this KeyObject.
        Description of the security object.

        Type: L{str}
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this KeyObject.
        Description of the security object.
        """

        self._description = description

    @property
    def key_size(self):
        """
        Gets the key_size of this KeyObject.
        For objects which are not elliptic curves, this is the size in bits (not bytes) of the object. This field is not returned for elliptic curves. 

        Type: L{int}
        """
        return self._key_size

    @key_size.setter
    def key_size(self, key_size):
        """
        Sets the key_size of this KeyObject.
        For objects which are not elliptic curves, this is the size in bits (not bytes) of the object. This field is not returned for elliptic curves. 
        """

        self._key_size = key_size

    @property
    def elliptic_curve(self):
        """
        Gets the elliptic_curve of this KeyObject.

        Type: L{EllipticCurve}
        """
        return self._elliptic_curve

    @elliptic_curve.setter
    def elliptic_curve(self, elliptic_curve):
        """
        Sets the elliptic_curve of this KeyObject.
        """

        self._elliptic_curve = elliptic_curve

    @property
    def acct_id(self):
        """
        Gets the acct_id of this KeyObject.
        Account ID of the account this security object belongs to.

        Type: L{str}
        """
        return self._acct_id

    @acct_id.setter
    def acct_id(self, acct_id):
        """
        Sets the acct_id of this KeyObject.
        Account ID of the account this security object belongs to.
        """

        self._acct_id = acct_id

    @property
    def group_id(self):
        """
        Gets the group_id of this KeyObject.
        Group ID of the security group that this security object belongs to.

        Type: L{str}
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this KeyObject.
        Group ID of the security group that this security object belongs to.
        """

        self._group_id = group_id

    @property
    def creator(self):
        """
        Gets the creator of this KeyObject.

        Type: L{CreatorType}
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """
        Sets the creator of this KeyObject.
        """

        self._creator = creator

    @property
    def kid(self):
        """
        Gets the kid of this KeyObject.
        Key ID uniquely identifying this security object.

        Type: L{str}
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        """
        Sets the kid of this KeyObject.
        Key ID uniquely identifying this security object.
        """

        self._kid = kid

    @property
    def obj_type(self):
        """
        Gets the obj_type of this KeyObject.

        Type: L{ObjectType}
        """
        return self._obj_type

    @obj_type.setter
    def obj_type(self, obj_type):
        """
        Sets the obj_type of this KeyObject.
        """

        self._obj_type = obj_type

    @property
    def key_ops(self):
        """
        Gets the key_ops of this KeyObject.
        Array of key operations enabled for this security object. 

        Type: list[L{KeyOperations}]
        """
        return self._key_ops

    @key_ops.setter
    def key_ops(self, key_ops):
        """
        Sets the key_ops of this KeyObject.
        Array of key operations enabled for this security object. 
        """

        self._key_ops = key_ops

    @property
    def attributes(self):
        """
        Gets the attributes of this KeyObject.

        Type: L{KeyAttributes}
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this KeyObject.
        """

        self._attributes = attributes

    @property
    def custom_metadata(self):
        """
        Gets the custom_metadata of this KeyObject.
        User-defined metadata for this key. Stored as key-value pairs.

        Type: map[L{str}]
        """
        return self._custom_metadata

    @custom_metadata.setter
    def custom_metadata(self, custom_metadata):
        """
        Sets the custom_metadata of this KeyObject.
        User-defined metadata for this key. Stored as key-value pairs.
        """

        self._custom_metadata = custom_metadata

    @property
    def origin(self):
        """
        Gets the origin of this KeyObject.

        Type: L{ObjectOrigin}
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """
        Sets the origin of this KeyObject.
        """

        self._origin = origin

    @property
    def pub_key(self):
        """
        Gets the pub_key of this KeyObject.
        This field is returned only for asymmetric keys. It contains the public key.

        Type: L{bytearray}
        """
        return self._pub_key

    @pub_key.setter
    def pub_key(self, pub_key):
        """
        Sets the pub_key of this KeyObject.
        This field is returned only for asymmetric keys. It contains the public key.
        """

        if not isinstance(pub_key, bytearray):
            raise ValueError("Invalid value for `pub_key`, `pub_key` must be a bytearray")
        self._pub_key = pub_key

    @property
    def value(self):
        """
        Gets the value of this KeyObject.
        This field is returned only for opaque and secret objects. It contains the contents of the object.

        Type: L{bytearray}
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this KeyObject.
        This field is returned only for opaque and secret objects. It contains the contents of the object.
        """

        if not isinstance(value, bytearray):
            raise ValueError("Invalid value for `value`, `value` must be a bytearray")
        self._value = value

    @property
    def enabled(self):
        """
        Gets the enabled of this KeyObject.
        Whether this security object has cryptographic operations enabled.

        Type: L{bool}
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this KeyObject.
        Whether this security object has cryptographic operations enabled.
        """

        self._enabled = enabled

    @property
    def created_at(self):
        """
        Gets the created_at of this KeyObject.
        When this security object was created.

        Type: L{str}
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this KeyObject.
        When this security object was created.
        """

        self._created_at = created_at

    @property
    def lastused_at(self):
        """
        Gets the lastused_at of this KeyObject.
        When this security object was last used.

        Type: L{str}
        """
        return self._lastused_at

    @lastused_at.setter
    def lastused_at(self, lastused_at):
        """
        Sets the lastused_at of this KeyObject.
        When this security object was last used.
        """

        self._lastused_at = lastused_at

    @property
    def transient_key(self):
        """
        Gets the transient_key of this KeyObject.
        Transient key blob.

        Type: L{str}
        """
        return self._transient_key

    @transient_key.setter
    def transient_key(self, transient_key):
        """
        Sets the transient_key of this KeyObject.
        Transient key blob.
        """

        self._transient_key = transient_key

    @property
    def never_exportable(self):
        """
        Gets the never_exportable of this KeyObject.
        True if this key's operations have never contained EXPORT.

        Type: L{bool}
        """
        return self._never_exportable

    @never_exportable.setter
    def never_exportable(self, never_exportable):
        """
        Sets the never_exportable of this KeyObject.
        True if this key's operations have never contained EXPORT.
        """

        self._never_exportable = never_exportable

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
        if not isinstance(other, KeyObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

