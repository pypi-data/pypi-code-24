from setuptools import setup, find_packages
import os
import argaeus


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


if os.path.isfile(os.path.join(os.path.dirname(__file__), 'README.md')):
    from pypandoc import convert
    readme_rst = convert(os.path.join(os.path.dirname(__file__), 'README.md'), 'rst')
    with open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'w') as out:
        out.write(readme_rst + '\n')

setup(
    name='Argaeus',
    version=argaeus.version,
    packages=find_packages(),
    license='MIT license',
    long_description=read('README.rst'),
    description='GUI (display and gui-logic) for a thermostat - to be used in combination with pelops/copreus and '
                'pelops/alcathous',
    url='https://gitlab.com/pelops/argaeus/',
    author='Tobias Gawron-Deutsch',
    author_email='tobias@strix.at',
    keywords='mqtt device driver rpi raspberry pi',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: No Input/Output (Daemon)",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "Topic :: Home Automation",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.5',
    install_requires=[
        "paho-mqtt",
        "pyyaml"
    ],
    entry_points={
        'console_scripts': [
            'argaeus = argaeus.gui:standalone',
        ]
    },

)
