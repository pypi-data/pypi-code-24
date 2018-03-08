# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .image_source_details import ImageSourceDetails
from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageSourceViaObjectStorageTupleDetails(ImageSourceDetails):

    def __init__(self, **kwargs):
        """
        Initializes a new ImageSourceViaObjectStorageTupleDetails object with values from values from keyword arguments. The default value of the :py:attr:`~oraclebmc.core.models.ImageSourceViaObjectStorageTupleDetails.source_type` attribute
        of this class is ``objectStorageTuple`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_image_type:
            The value to assign to the source_image_type property of this ImageSourceViaObjectStorageTupleDetails.
            Allowed values for this property are: "QCOW2", "VMDK"
        :type source_image_type: str

        :param source_type:
            The value to assign to the source_type property of this ImageSourceViaObjectStorageTupleDetails.
        :type source_type: str

        :param bucket_name:
            The value to assign to the bucket_name property of this ImageSourceViaObjectStorageTupleDetails.
        :type bucket_name: str

        :param namespace_name:
            The value to assign to the namespace_name property of this ImageSourceViaObjectStorageTupleDetails.
        :type namespace_name: str

        :param object_name:
            The value to assign to the object_name property of this ImageSourceViaObjectStorageTupleDetails.
        :type object_name: str

        """
        self.swagger_types = {
            'source_image_type': 'str',
            'source_type': 'str',
            'bucket_name': 'str',
            'namespace_name': 'str',
            'object_name': 'str'
        }

        self.attribute_map = {
            'source_image_type': 'sourceImageType',
            'source_type': 'sourceType',
            'bucket_name': 'bucketName',
            'namespace_name': 'namespaceName',
            'object_name': 'objectName'
        }

        self._source_image_type = None
        self._source_type = None
        self._bucket_name = None
        self._namespace_name = None
        self._object_name = None
        self._source_type = 'objectStorageTuple'

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage bucket for the image.


        :return: The bucket_name of this ImageSourceViaObjectStorageTupleDetails.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage bucket for the image.


        :param bucket_name: The bucket_name of this ImageSourceViaObjectStorageTupleDetails.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def namespace_name(self):
        """
        **[Required]** Gets the namespace_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage namespace for the image.


        :return: The namespace_name of this ImageSourceViaObjectStorageTupleDetails.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        """
        Sets the namespace_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage namespace for the image.


        :param namespace_name: The namespace_name of this ImageSourceViaObjectStorageTupleDetails.
        :type: str
        """
        self._namespace_name = namespace_name

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage name for the image.


        :return: The object_name of this ImageSourceViaObjectStorageTupleDetails.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this ImageSourceViaObjectStorageTupleDetails.
        The Object Storage name for the image.


        :param object_name: The object_name of this ImageSourceViaObjectStorageTupleDetails.
        :type: str
        """
        self._object_name = object_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
