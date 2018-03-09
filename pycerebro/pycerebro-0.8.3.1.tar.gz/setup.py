#!/usr/bin/env python3
# Copyright 2017 CerebroData Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

import ez_setup
ez_setup.use_setuptools()

import sys
from os.path import dirname, exists, join
from setuptools import setup, find_packages, Extension
import versioneer  # noqa

if not exists((join(dirname(__file__), 'cerebro', 'thrift', 'RecordService.thrift'))):
    print("thrift files not present. Run build.sh from this folder.")
    sys.exit(1)

def readme():
    with open('README.rst', 'r') as ip:
        return ip.read()

reqs = ['six', 'bitarray', 'thriftpy>=0.3.9']

setup(
    name='pycerebro',
    maintainer='Cerebro Development Team',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Python client for the Cerebro Data Access Service',
    long_description=readme(),
    packages = find_packages(exclude=['cerebro.RecordService',
                                      'cerebro.RecordService.*',
                                      'cerebro.CerebroRecorService',
                                      'cerebro.CerebroRecorService.*']),
    package_data={'cerebro': ['thrift/*.thrift']},
    install_requires=reqs,
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    zip_safe=False)
