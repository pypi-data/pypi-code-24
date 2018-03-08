# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    # Application name:
    name="corpussearch",

    # Version number (initial):
    version="0.0.4",

    # Application author details:
    author="Malte Vogl",
    author_email="mvogl@mpiwg-berlin.mpg.de",

    # Packages
    packages=find_packages(exclude=('tests')),

    # Include additional files into the package
    include_package_data=True,

    url='https://github.com/TOPOI-DH/corpussearch/',

    # Details

    license=license,
    description="Tools for loading and analyzing large text corpora.",

    long_description=readme,

    classifiers=[
        # How mature is this project?
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Indexing',
        # Pick your license as you wish
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        # Specify the Python versions you support here.
        'Programming Language :: Python :: 3',
    ],
    project_urls={
        'Home': 'https://github.com/TOPOI-DH/corpussearch/',
        'Tracker': 'https://github.com/TOPOI-DH/corpussearch/issues',
        'Download': 'https://github.com/TOPOI-DH/corpussearch/archive/0.0.4.tar.gz',
    },

    python_requires='>=3',

    # Dependent packages (distributions)
    install_requires=[
        "pandas",
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
