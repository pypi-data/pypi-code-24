# Copyright 2018, afpro <admin@afpro.net>.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========================================================================
__all__ = [
    'file_lines_generator',
]


def file_lines_generator(path: 'str', with_eol=False):
    """
    read lines from file
    :param path: path
    :param with_eol: where line with '\n' suffix
    :return: file line generator
    """
    with open(path) as fp:
        while True:
            line = fp.readline()
            if len(line) == 0:
                break
            if with_eol:
                yield line
            else:
                yield line[:-1]
