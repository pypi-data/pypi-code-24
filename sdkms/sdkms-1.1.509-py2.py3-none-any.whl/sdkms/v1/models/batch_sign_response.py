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
from .base_list_object import BaseListObject

class BatchSignResponse(BaseListObject):
    """
    

    This class BatchSignResponse denotes list of BatchSignResponseInner
    In python subclassing a list is not recommended, hence this class stores the list of BatchSignResponseInner as its parameter.

    Initialize object: batch_sign_response = BatchSignResponse()
    Add object to BatchSignResponse object: batch_sign_response.append(BatchSignResponseInner())
    Insert object to BatchSignResponse object at index: batch_sign_response.insert(1, BatchSignResponseInner())
    Delete an object from BatchSignResponse object at index: batch_sign_response.remove(1)
    Get the list of BatchSignResponseInner: list()

    This class serializes as a list of BatchSignResponseInner.
    """

    inner_type = 'BatchSignResponseInner'

    def __init__(self):
        self._list = []

    def __getitem__(self, item):
        return self._list.__getitem__(item)

    def append(self, element):
        self._list.append(element)

    def insert(self, index, element):
        self._list.insert(index, element)   

    def remove(self, index):
        self._list.remove(index)

    @property
    def list(self):
        return self._list

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self._list)
 
    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()



