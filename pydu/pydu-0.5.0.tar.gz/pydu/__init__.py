"""
Useful data structures, utils for Python.
"""
from __future__ import absolute_import

__version__ = '0.5.0'


# Set logging handler to avoid "No handler found" warnings.
import logging
from logging import NullHandler


logger = logging.getLogger(__name__)
logger.addHandler(NullHandler())
