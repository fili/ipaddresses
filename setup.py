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

"""Setup for source, wheel, and other distribution formats."""

import os
import io
from setuptools import setup, find_packages
import appinfo

UTF_ENC = 'utf-8'

# Load long description from README file
DESC = LONG_DESC = ''
if os.path.isfile(appinfo.README_FILE):
    with io.open(appinfo.README_FILE, encoding=UTF_ENC) as f_in:
        LONG_DESC = f_in.read()
        DESC = LONG_DESC.split('\n')[3] if len(
            LONG_DESC.split('\n')) > 3 else ''

# Load requirements
REQUIREMENTS = []
if os.path.isfile(appinfo.REQUIREMENTS_FILE):
    with io.open(appinfo.REQUIREMENTS_FILE, encoding=UTF_ENC) as f_in:
        REQUIREMENTS = f_in.read().splitlines()

# CLI entry point
ENTRY_POINTS = {
    'console_scripts': [
        f"{appinfo.APP_NAME}={appinfo.APP_NAME}.{appinfo.APP_NAME}:main"
    ],
    # GUI entry point example (commented):
    # 'gui_scripts': [f"{appinfo.APP_NAME}_gui={appinfo.APP_NAME}.{appinfo.APP_NAME}:start"]
}

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
    include_package_data=True,
    install_requires=REQUIREMENTS,
    entry_points=ENTRY_POINTS,
)
