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

"""
Show private and public IP addresses.

If there are any command line arguments it calls the CLI module.
Otherwise the GUI module.
See usage.txt for command line usage.
"""

import sys

import cli
import gui_tk_func as gui


def main():
    """Start CLI or GUI."""
    args = sys.argv[1:]
    if args and args[0].lower() in ['-g', '--gui']:
        gui.start()
    else:
        cli.start(args)


if __name__ == '__main__':
    sys.exit(main())
