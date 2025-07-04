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

"""Localization module."""

import locale
import sys


def sys_lang():
    """Get system language."""
    lang = locale.getdefaultlocale()
    if lang and 'pt_' in lang[0].lower():
        return 'PT'
    return 'EN'


LANG = sys_lang()

FS_ENC = sys.getfilesystemencoding()
INPUT_ENC = sys.stdin.encoding
UTF_ENC = 'utf-8'

if LANG == 'PT':
    ABOUT = 'Sobre'
    BANNER = (
        ' não tem QUALQUER GARANTIA. É software livre e você está '
        'autorizado a redistribui-lo dentro de certas condições.'
    )
    EXIT = 'Sair'
    FILE = 'Ficheiro'
    HELP = 'Ajuda'
    PRESS_ANY_KEY = 'Prima qualquer tecla para continuar...'
    PRIVATE_IP = 'IP privado: '
    PUBLIC_IP = 'IP público: '
    VERSION = 'Versão'
    VERSION_WITH_SPACES = ' versão '
    WIN_TITLE = 'Endereços IP'
    WRONG_ARG = 'Erro: argumento incorreto '
else:
    ABOUT = 'About'
    BANNER = (
        ' comes with ABSOLUTELY NO WARRANTY. This is free software, '
        'and you are welcome to redistribute it under certain conditions.'
    )
    EXIT = 'Exit'
    FILE = 'File'
    HELP = 'Help'
    PRESS_ANY_KEY = 'Press any key to continue...'
    PRIVATE_IP = 'Private IP: '
    PUBLIC_IP = 'Public IP: '
    VERSION = 'Version'
    VERSION_WITH_SPACES = ' version '
    WIN_TITLE = 'IP addresses'
    WRONG_ARG = 'Err: incorrect argument '


if __name__ == '__main__':
    pass
