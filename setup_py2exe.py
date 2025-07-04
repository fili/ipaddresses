#!/usr/bin/env python3

# Copyright 2009-2015 Joao Carlos Roseta Matos
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Setup script for building a py2exe Windows executable."""

import os
import sys
import glob
import io

from setuptools import setup, find_packages
import py2exe  # Must follow setuptools import

import appinfo

UTF_ENC = 'utf-8'

# Read long description from README file
DESC = LONG_DESC = ''
if os.path.isfile(appinfo.README_FILE):
    with io.open(appinfo.README_FILE, encoding=UTF_ENC) as f:
        LONG_DESC = f.read()
        DESC = LONG_DESC.split('\n')[3] if len(
            LONG_DESC.split('\n')) > 3 else ''

# Read dependencies
REQUIREMENTS = []
if os.path.isfile(appinfo.REQUIREMENTS_FILE):
    with io.open(appinfo.REQUIREMENTS_FILE, encoding=UTF_ENC) as f:
        REQUIREMENTS = f.read().splitlines()

# Script and data setup
PATH = appinfo.APP_NAME + '/'
SCRIPT = PATH + appinfo.APP_NAME + '.py'

DATA_FILES = [('', glob.glob(PATH + '*.txt'))]

# Include documentation files if they exist
doc_path = os.path.join(PATH, 'doc')
if os.path.isdir(doc_path):
    DATA_FILES.extend([
        ('doc', glob.glob(os.path.join(doc_path, '*'))),
        ('doc/_modules', glob.glob(os.path.join(doc_path, '_modules', '*.*'))),
        ('doc/_sources', glob.glob(os.path.join(doc_path, '_sources', '*.*'))),
        ('doc/_static', glob.glob(os.path.join(doc_path, '_static', '*.*')))
    ])

# Py2exe options
OPTIONS = {
    'py2exe': {
        'compressed': True,
        'ascii': False,
        # Customize if needed:
        # 'packages': ['colorama'],
        # 'includes': ['colorama'],
        # 'bundle_files': 1,
        # 'excludes': ['doctest', 'pdb', 'unittest', 'difflib', ...]
    }
}

# Add module directory to path for py2exe to discover packages
sys.path.insert(1, appinfo.APP_NAME)

setup(
    name=appinfo.APP_NAME,
    version=appinfo.APP_VERSION,
    description=DESC,
    long_description=LONG_DESC,
    license=appinfo.APP_LICENSE,
    url=appinfo.APP_URL,
    author=appinfo.APP_AUTHOR,
    author_email=appinfo.APP_EMAIL,
    classifiers=appinfo.CLASSIFIERS,
    keywords=appinfo.APP_KEYWORDS,

    packages=find_packages(),
    install_requires=REQUIREMENTS,
    console=[SCRIPT],
    options=OPTIONS,
    data_files=DATA_FILES,
    # Optional GUI build:
    # windows=[{
    #     'script': SCRIPT,
    #     'icon_resources': [(0, f"{appinfo.APP_NAME}.ico")]
    # }],
)
