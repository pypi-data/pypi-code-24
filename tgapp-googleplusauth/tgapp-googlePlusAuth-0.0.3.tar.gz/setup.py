# -*- coding: utf-8 -*-
import sys, os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

install_requires=[
    "six",
    "TurboGears2 >= 2.1.4",
    "tgext.pluggable"
]

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''

setup(
    name='tgapp-googlePlusAuth',
    version='0.0.3',
    description='Google Authentication for TurboGears2',
    long_description=README,
    author='AXANT',
    author_email='tech@axant.it',
    url='https://github.com/axant/tgapp-googleplusauth',
    keywords='turbogears2.application',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=install_requires,
    include_package_data=True,
    package_data={'googleplusauth': [
        'i18n/*/LC_MESSAGES/*.mo',
        'templates/*/*',
        'public/*/*'
    ]},
    message_extractors={'googleplusauth': [
            ('**.py', 'python', None),
            ('templates/**.html', 'genshi', None),
            ('public/**', 'ignore', None)
    ]},
    entry_points="""
    """,
    zip_safe=False
)
