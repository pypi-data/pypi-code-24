# -*- coding:utf-8 -*-

from setuptools import setup
from setuptools import find_packages

setup(
    name='TkToolsD',
    version=open('version.txt').read(),
    description=(
        'Some usefull tk widgets like: ImageView, ScrollView.'
    ),
    long_description=open('README.rst').read(),
    author='dekiven',
    author_email='dekiven@163.com',
    # maintainer='<维护人员的名字>',
    # maintainer_email='<维护人员的邮件地址',
    license='BSD License',
    packages=find_packages(),
    install_requires=[
    	'Pillow',
    	# 'other>=1.1'
    ],
    platforms=["all"],
    data_files=[
        'version.txt',
    ],
    url='https://www.baidu.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)