from __future__ import absolute_import, unicode_literals

import six
from oauthlib.oauth2 import OAuth2Error

from rest_framework import status


class InvalidLoginError(OAuth2Error):
    """
    Generic exception for a failed login attempt through OAuth2. This exception
    will result in a 400 Bad Request error in the OAuth API.
    """

    def __init__(self, message):
        """
        Initializes this error with the given error message.

        :param message: The error message describing this exception.
        """
        super(Exception, self).__init__(message)

    @property
    def twotuples(self):
        """
        Returns a list of tuples that will be converted to the error response.
        This method override the ``two_tuples`` method from ``OAuth2Error``.
        """
        return [("detail", six.text_type(self))]
