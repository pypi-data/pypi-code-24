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


class ShrinkageOverride(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ShrinkageOverride - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'interval_index': 'int',
            'shrinkage_percent': 'float'
        }

        self.attribute_map = {
            'interval_index': 'intervalIndex',
            'shrinkage_percent': 'shrinkagePercent'
        }

        self._interval_index = None
        self._shrinkage_percent = None

    @property
    def interval_index(self):
        """
        Gets the interval_index of this ShrinkageOverride.
        Index of shrinkage override interval. Starting index is 0 and indexes are based on 15 minute intervals for a 7 day week

        :return: The interval_index of this ShrinkageOverride.
        :rtype: int
        """
        return self._interval_index

    @interval_index.setter
    def interval_index(self, interval_index):
        """
        Sets the interval_index of this ShrinkageOverride.
        Index of shrinkage override interval. Starting index is 0 and indexes are based on 15 minute intervals for a 7 day week

        :param interval_index: The interval_index of this ShrinkageOverride.
        :type: int
        """
        
        self._interval_index = interval_index

    @property
    def shrinkage_percent(self):
        """
        Gets the shrinkage_percent of this ShrinkageOverride.
        Shrinkage override percent. Setting a null value will reset the interval to the default

        :return: The shrinkage_percent of this ShrinkageOverride.
        :rtype: float
        """
        return self._shrinkage_percent

    @shrinkage_percent.setter
    def shrinkage_percent(self, shrinkage_percent):
        """
        Sets the shrinkage_percent of this ShrinkageOverride.
        Shrinkage override percent. Setting a null value will reset the interval to the default

        :param shrinkage_percent: The shrinkage_percent of this ShrinkageOverride.
        :type: float
        """
        
        self._shrinkage_percent = shrinkage_percent

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

