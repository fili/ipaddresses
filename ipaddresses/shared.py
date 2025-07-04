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

"""Shared constants and functions between CLI and GUI modules."""

import socket
import urllib.request


def get_private_ip():
    """Get the machine's private IP address."""
    return socket.gethostbyname(socket.gethostname())


def get_public_ip():
    """Fetch the machine's public IP address."""
    try:
        with urllib.request.urlopen("https://ip.app/", timeout=5) as response:
            return response.read().strip().decode("utf-8")
    except Exception as e:
        raise RuntimeError(f"Failed to fetch public IP: {e}")


if __name__ == '__main__':
    pass
