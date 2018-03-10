#!/usr/bin/env python


from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def get_version():
    with open(path.join(here, "chimera_utils/version.py"), encoding = 'utf-8') as hin:
        for line in hin:
            if line.startswith("__version__"):
                version = line.partition('=')[2]
                return version.strip().strip('\'"')
    raise ValueError('Could not find version.')

setup(
    name = 'chimera_utils',
    version = get_version(),
    description='Python tools for processing chimeric reads and lists of gene fusions.',
    url = 'https://github.com/friend1ws/chimera_utils',
    author = 'Yuichi Shiraishi',
    author_email = 'friend1ws@gamil.com',
    license = 'GPLv3',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],

    packages = find_packages(exclude = ['tests']),

    install_requires = ["annot_utils", "fusionfusion", "pysam"],
    entry_points = {'console_scripts': ['chimera_utils = chimera_utils:main']}

)

