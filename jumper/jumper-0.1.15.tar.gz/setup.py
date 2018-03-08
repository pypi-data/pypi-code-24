"""
:license: Apache 2.0, see LICENSE.txt for more details.
:license: Apache 2.0, see LICENSE for more details.
"""
import os
from setuptools import setup, find_packages
from os import path

here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, 'jumper', '__version__.py'), 'r') as f:
    exec(f.read(), about)
print(about)
version = about['__version__']

setup(
    name='jumper',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,

    description="SDK for using Jumper's emulator",
    # long_description=long_description,

    # The project's main homepage.
    url='https://vlab.jumper.io',

    # Author details
    author='Jumper Labs Ltd.',
    author_email='info@jumper.io',

    # Choose your license
    license='Apache 2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        # 'Intended Audience :: Developers',
        # 'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        # 'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # 'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    packages=['jumper'],
    package_dir={'jumper': 'jumper'},

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['future', 'timeout-decorator', 'requests', 'termcolor', 'terminaltables'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['sphinx', 'nose', 'sphinx-bootstrap-theme', 'sphinx_rtd_theme', 'twine', 'wheel']
    },

    # project only runs on certain Python versions (2.7)
    python_requires='==2.7.*',

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #     'sample': ['package_data.dat'],
    # },
    package_data={'jumper': ['LICENSE.txt', 'NOTICE.txt', 'hci/hci', 'hci/peripherals.json', 'hci/program.bin', 'hci/instructions.so', 'default_bsp.json']},
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'jumper = jumper.__main__:main',
        ]
    }
)
