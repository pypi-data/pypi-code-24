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


class CallableContactsDiagnostic(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CallableContactsDiagnostic - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'attempt_limits': 'UriReference',
            'dnc_lists': 'list[UriReference]',
            'callable_time_set': 'UriReference',
            'rule_sets': 'list[UriReference]'
        }

        self.attribute_map = {
            'attempt_limits': 'attemptLimits',
            'dnc_lists': 'dncLists',
            'callable_time_set': 'callableTimeSet',
            'rule_sets': 'ruleSets'
        }

        self._attempt_limits = None
        self._dnc_lists = None
        self._callable_time_set = None
        self._rule_sets = None

    @property
    def attempt_limits(self):
        """
        Gets the attempt_limits of this CallableContactsDiagnostic.
        Attempt limits for the campaign's contact list

        :return: The attempt_limits of this CallableContactsDiagnostic.
        :rtype: UriReference
        """
        return self._attempt_limits

    @attempt_limits.setter
    def attempt_limits(self, attempt_limits):
        """
        Sets the attempt_limits of this CallableContactsDiagnostic.
        Attempt limits for the campaign's contact list

        :param attempt_limits: The attempt_limits of this CallableContactsDiagnostic.
        :type: UriReference
        """
        
        self._attempt_limits = attempt_limits

    @property
    def dnc_lists(self):
        """
        Gets the dnc_lists of this CallableContactsDiagnostic.
        Do not call lists for the campaign

        :return: The dnc_lists of this CallableContactsDiagnostic.
        :rtype: list[UriReference]
        """
        return self._dnc_lists

    @dnc_lists.setter
    def dnc_lists(self, dnc_lists):
        """
        Sets the dnc_lists of this CallableContactsDiagnostic.
        Do not call lists for the campaign

        :param dnc_lists: The dnc_lists of this CallableContactsDiagnostic.
        :type: list[UriReference]
        """
        
        self._dnc_lists = dnc_lists

    @property
    def callable_time_set(self):
        """
        Gets the callable_time_set of this CallableContactsDiagnostic.
        Callable time sets for the campaign

        :return: The callable_time_set of this CallableContactsDiagnostic.
        :rtype: UriReference
        """
        return self._callable_time_set

    @callable_time_set.setter
    def callable_time_set(self, callable_time_set):
        """
        Sets the callable_time_set of this CallableContactsDiagnostic.
        Callable time sets for the campaign

        :param callable_time_set: The callable_time_set of this CallableContactsDiagnostic.
        :type: UriReference
        """
        
        self._callable_time_set = callable_time_set

    @property
    def rule_sets(self):
        """
        Gets the rule_sets of this CallableContactsDiagnostic.
        Rule sets for the campaign

        :return: The rule_sets of this CallableContactsDiagnostic.
        :rtype: list[UriReference]
        """
        return self._rule_sets

    @rule_sets.setter
    def rule_sets(self, rule_sets):
        """
        Sets the rule_sets of this CallableContactsDiagnostic.
        Rule sets for the campaign

        :param rule_sets: The rule_sets of this CallableContactsDiagnostic.
        :type: list[UriReference]
        """
        
        self._rule_sets = rule_sets

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

