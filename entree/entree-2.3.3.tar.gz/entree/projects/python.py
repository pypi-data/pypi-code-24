'''
.. module:: entree.projects.python
.. moduleauthor:: Julien Spronck
.. created:: Feb 2018

Module for Python projects
'''

import os
from entree.projects.base import ProjectBase

__version__ = '0.0'

FILEPATH, FILEBASE = os.path.split(__file__)

PROJECT_TYPE = os.path.splitext(FILEBASE)[0]
PROJECT_LONG_NAME = 'Python'
TEMPLATE_DIR = 'python'
SINGLE_FILE = os.path.join(TEMPLATE_DIR, 'src', '__init___py.template')
REPLACE = {
    'unittest_py.template': 'test_{{ modname }}.py',
    'src': '{{ modname }}'
}


class Python(ProjectBase):
    '''Class for Python projects

    Class attributes:
        project_type (str): project type (e.g. flask)
        project_long_name (str): long name for a project (e.g. 'Large Flask')
        template_dir (str): path to the project template directory relative to
            the template root directory
        single_file (str): path to a single file that you want to create in
            single-file mode relative to the template root directory
        replace (dict, default=None): dictionary mapping template file
            names that should be replaced when creating the files. For
            example, {'unittest_py.template': 'test_project.py'}
        version (str): version number
    '''
    project_type = PROJECT_TYPE
    project_long_name = PROJECT_LONG_NAME
    template_dir = TEMPLATE_DIR
    single_file = SINGLE_FILE
    replace = REPLACE
    version = __version__
