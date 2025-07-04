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

"""Application basic information."""

import datetime as dt

APP_NAME = 'ipaddresses'
APP_VERSION = '0.0.2'
APP_LICENSE = 'GNU General Public License v2 or later (GPLv2+)'
APP_AUTHOR = 'Joao Carlos Roseta Matos'
APP_EMAIL = 'jcrmatos@gmail.com'
APP_URL = 'https://github.com/jcrmatos/ipaddresses'
APP_KEYWORDS = 'ip address private public'

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Environment :: MacOS X',
    'Environment :: Other Environment',
    'Environment :: Win32 (MS Windows)',
    'Environment :: X11 Applications',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
    'Natural Language :: English',
    'Natural Language :: Portuguese',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Programming Language :: Python :: 3.13',
    'Topic :: System :: Networking'
]

COPYRIGHT = f'Copyright 2009-{dt.date.today().year} {APP_AUTHOR}'

APP_TYPE = 'application'  # could also be 'module'

README_FILE = 'README.rst'
REQUIREMENTS_FILE = 'requirements.txt'
