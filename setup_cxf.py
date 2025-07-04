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

"""Setup script for building a cx_Freeze Windows executable."""

import os
import sys
import glob
import io

from cx_Freeze import setup, Executable
import appinfo

UTF_ENC = 'utf-8'

# Load long description from README
DESC = LONG_DESC = ''
if os.path.isfile(appinfo.README_FILE):
    with io.open(appinfo.README_FILE, encoding=UTF_ENC) as f:
        LONG_DESC = f.read()
        DESC = LONG_DESC.split('\n')[3] if len(
            LONG_DESC.split('\n')) > 3 else ''

# Application structure
APP_DIR = appinfo.APP_NAME
SCRIPT = os.path.join(APP_DIR, f"{appinfo.APP_NAME}.py")
TARGET_NAME = f"{appinfo.APP_NAME}.exe"

# Data files (non-Python files)
DATA_FILES = glob.glob(os.path.join(APP_DIR, '*.txt'))

# Optionally include documentation files
DOC_DIR = os.path.join(APP_DIR, 'doc')
if os.path.isdir(DOC_DIR):
    DATA_FILES += glob.glob(os.path.join(DOC_DIR, '*'))

# Base for GUI or CLI
BASE = 'Win32GUI' if sys.platform == 'win32' else None

# Build options
OPTIONS = {
    'compressed': True,
    'include_files': DATA_FILES,
    # 'excludes': ['tkinter'],  # example
    # 'includes': ['atexit'],  # example
    # 'packages': [],  # example
}

# Ensure modules in APP_DIR are discoverable
sys.path.insert(1, APP_DIR)

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

    executables=[
        Executable(
            script=SCRIPT,
            base=BASE,
            targetName=TARGET_NAME,
            # icon=f"{appinfo.APP_NAME}.ico",
            compress=True,
        )
    ],

    options={
        'build_exe': OPTIONS
    },
)
