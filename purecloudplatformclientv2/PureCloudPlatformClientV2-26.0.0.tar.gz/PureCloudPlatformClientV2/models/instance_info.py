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


class InstanceInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        InstanceInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'state': 'str',
            'edge': 'Edge',
            'assigned_phone_count': 'int',
            'ami': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'state': 'state',
            'edge': 'edge',
            'assigned_phone_count': 'assignedPhoneCount',
            'ami': 'ami'
        }

        self._id = None
        self._state = None
        self._edge = None
        self._assigned_phone_count = None
        self._ami = None

    @property
    def id(self):
        """
        Gets the id of this InstanceInfo.
        Id of the ec2 instance.

        :return: The id of this InstanceInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InstanceInfo.
        Id of the ec2 instance.

        :param id: The id of this InstanceInfo.
        :type: str
        """
        
        self._id = id

    @property
    def state(self):
        """
        Gets the state of this InstanceInfo.
        State of the instance in AWS

        :return: The state of this InstanceInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this InstanceInfo.
        State of the instance in AWS

        :param state: The state of this InstanceInfo.
        :type: str
        """
        allowed_values = ["rebooting", "pending", "running", "terminated", "stopping", "stopped"]
        if state.lower() not in map(str.lower, allowed_values):
            # print "Invalid value for state -> " + state
            self._state = "outdated_sdk_version"
        else:
            self._state = state

    @property
    def edge(self):
        """
        Gets the edge of this InstanceInfo.
        Edge object that the instance is associated with.

        :return: The edge of this InstanceInfo.
        :rtype: Edge
        """
        return self._edge

    @edge.setter
    def edge(self, edge):
        """
        Sets the edge of this InstanceInfo.
        Edge object that the instance is associated with.

        :param edge: The edge of this InstanceInfo.
        :type: Edge
        """
        
        self._edge = edge

    @property
    def assigned_phone_count(self):
        """
        Gets the assigned_phone_count of this InstanceInfo.
        Number of phones assigned to the edge.

        :return: The assigned_phone_count of this InstanceInfo.
        :rtype: int
        """
        return self._assigned_phone_count

    @assigned_phone_count.setter
    def assigned_phone_count(self, assigned_phone_count):
        """
        Sets the assigned_phone_count of this InstanceInfo.
        Number of phones assigned to the edge.

        :param assigned_phone_count: The assigned_phone_count of this InstanceInfo.
        :type: int
        """
        
        self._assigned_phone_count = assigned_phone_count

    @property
    def ami(self):
        """
        Gets the ami of this InstanceInfo.
        The image id of the instance.

        :return: The ami of this InstanceInfo.
        :rtype: str
        """
        return self._ami

    @ami.setter
    def ami(self, ami):
        """
        Sets the ami of this InstanceInfo.
        The image id of the instance.

        :param ami: The ami of this InstanceInfo.
        :type: str
        """
        
        self._ami = ami

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

