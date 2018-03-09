#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-12-1
Desc    :   
"""
import os
from pip.req import parse_requirements
from pip.download import PipSession
from setuptools import setup

__version__ = "0.4.0"
__author__ = "windprog"
__author_email__ = "windprog@gmail.com"
__description__ = "gunicorn wrapper. support worker"
__title__ = 'rest-utils'
__url__ = "https://github.com/windprog/rest-utils"

req = os.path.join(os.path.dirname(__file__), 'requirements.txt')
install_reqs = parse_requirements(req, session=PipSession())
install_requires = [str(ir.req) for ir in install_reqs]

setup(
    name=__title__,
    version=__version__,
    description=__description__,
    url=__url__,
    author=__author__,
    author_email=__author_email__,
    packages=['rest_utils', 'rest_utils.worker'],
    install_requires=install_requires,
    data_files=[(".", ['requirements.txt'])],  # save requirements.txt to install package
)
