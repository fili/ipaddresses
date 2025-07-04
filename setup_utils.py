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

"""Utility functions for setup, packaging, and distribution."""

import datetime as dt
import glob
import io
import os
import sys
import time
import zipfile as zip

import appinfo

UTF_ENC = 'utf-8'


def check_copyright():
    """Check copyright on files that have to be updated manually."""
    files = ['setup_utils.py', 'build.cmd', 'appinfo.py']
    update_required = 0
    for filename in files:
        if os.path.isfile(filename):
            with open(filename, encoding=UTF_ENC) as f_in:
                text = f_in.readlines()
            for line in text:
                if appinfo.COPYRIGHT in line:
                    break
                if 'Copyright 2009-' in line:
                    print(f'Copyright in {filename} is not updated.')
                    update_required += 1
                    break
    if update_required:
        sys.exit(1)


def update_copyright():
    """Update copyright on source and license files."""
    files = [f for f in glob.glob(
        '*.py') if f not in ['appinfo.py', 'setup_utils.py']]
    files += glob.glob(f'{appinfo.APP_NAME}/*.py')

    for filename in files:
        with open(filename, encoding=UTF_ENC) as f_in:
            text = f_in.readlines()
        new_text = ''
        changed = False
        for line in text:
            if not changed and appinfo.COPYRIGHT not in line and 'Copyright 2009-' in line:
                new_text += f'# {appinfo.COPYRIGHT}\n'
                changed = True
            else:
                new_text += line
        if changed:
            with open(filename, 'w', encoding=UTF_ENC) as f_out:
                f_out.writelines(new_text)

    # Update doc/conf.py
    filename = 'doc/conf.py'
    if os.path.isfile(filename):
        with open(filename, encoding=UTF_ENC) as f_in:
            text = f_in.readlines()
        new_text = ''
        changed = False
        doc_copyright = f"copyright = u'2009-{dt.date.today().year}, {appinfo.APP_AUTHOR}'"
        for line in text:
            if not changed and "copyright = u'2009-" in line and doc_copyright not in line:
                new_text += f"{doc_copyright}\n"
                changed = True
            else:
                new_text += line
        if changed:
            with open(filename, 'w', encoding=UTF_ENC) as f_out:
                f_out.writelines(new_text)

    # Update LICENSE.rst
    filename = 'LICENSE.rst'
    with open(filename, encoding=UTF_ENC) as f_in:
        text = f_in.readlines()
    new_text = ''
    changed = False
    for line in text:
        if not changed and appinfo.COPYRIGHT not in line and 'Copyright 2009-' in line:
            new_text += f'        {appinfo.COPYRIGHT}\n'
            changed = True
        else:
            new_text += line
    if changed:
        with open(filename, 'w', encoding=UTF_ENC) as f_out:
            f_out.writelines(new_text)


def sleep(seconds=5):
    """Pause for specified time."""
    time.sleep(seconds)


def app_name():
    """Write application name to text file."""
    with open('app_name.txt', 'w', encoding=UTF_ENC) as f_out:
        f_out.write(appinfo.APP_NAME)


def app_ver():
    """Write application version to text file if equal to ChangeLog.rst."""
    with open('ChangeLog.rst', encoding=UTF_ENC) as f_in:
        changelog_app_ver = f_in.readline().split()[0]
    if changelog_app_ver == appinfo.APP_VERSION:
        with open('app_ver.txt', 'w', encoding=UTF_ENC) as f_out:
            f_out.write(appinfo.APP_VERSION)
    else:
        print('ChangeLog.rst and appinfo.py are not in sync.')


def app_type():
    """Write application type (application or module) to text file."""
    with open('app_type.txt', 'w', encoding=UTF_ENC) as f_out:
        f_out.write(appinfo.APP_TYPE)


def py_ver():
    """Write Python version to text file."""
    with open('py_ver.txt', 'w', encoding=UTF_ENC) as f_out:
        f_out.write(f'{sys.version_info.major}.{sys.version_info.minor}')


def remove_copyright():
    """Remove Copyright from README.rst."""
    with open('README.rst', encoding=UTF_ENC) as f_in:
        text = f_in.readlines()
    new_text = ''.join(line for line in text if 'Copyright ' not in line)
    with open('README.rst', 'w', encoding=UTF_ENC) as f_out:
        f_out.writelines(new_text)


def prep_rst2pdf():
    """Remove parts of rST to create a better PDF."""
    for filename in ['index.ori', '../README.rst']:
        with open(filename, encoding=UTF_ENC) as f_in:
            lines = f_in.readlines()

        if 'index.ori' in filename:
            new_text = ''
            for line in lines:
                if 'Indices and tables' in line:
                    break
                new_text += line
            out_file = 'index.rst'
        else:
            new_text = ''.join(
                line for line in lines if '.. image:: ' not in line and '    :target: ' not in line
            )
            out_file = '../README.rst'

        with open(out_file, 'w', encoding=UTF_ENC) as f_out:
            f_out.writelines(new_text)


def create_doc_zip():
    """Create doc.zip to publish in PyPI."""
    doc_path = os.path.join(appinfo.APP_NAME, 'doc')
    with zip.ZipFile('pythonhosted.org/doc.zip', 'w') as archive:
        for root, _, files in os.walk(doc_path):
            for file_ in files:
                if '.pdf' not in file_:
                    pathname = os.path.join(root, file_)
                    arcname = os.path.relpath(pathname, doc_path)
                    archive.write(pathname, arcname)


def upd_usage_in_readme():
    """Update usage in README.rst."""
    usage_path = os.path.join(appinfo.APP_NAME, 'usage.txt')
    if os.path.isfile(usage_path):
        with open(usage_path, encoding=UTF_ENC) as f_in:
            usage_text = f_in.read().lstrip('\n')

        with open('README.rst', encoding=UTF_ENC) as f_in:
            text = f_in.readlines()

        new_text = ''
        usage_section = False
        changed = False
        for line in text:
            if 'usage: ' in line:
                usage_section = True
                new_text += usage_text + '\n'
                changed = True
            elif usage_section and 'Resources' not in line:
                continue
            elif usage_section and 'Resources' in line:
                usage_section = False
                new_text += line
            else:
                new_text += line

        if changed:
            with open('README.rst', 'w', encoding=UTF_ENC) as f_out:
                f_out.writelines(new_text)


def change_sphinx_theme():
    """Change Sphinx theme according to version."""
    try:
        import sphinx
        sphinx_ver = int(sphinx.__version__.replace('.', ''))
        conf_file = 'doc/conf.py'
        with open(conf_file, encoding=UTF_ENC) as f_in:
            text = f_in.readlines()

        new_text = ''
        changed = False
        for line in text:
            if "html_theme = 'default'" in line and sphinx_ver >= 131:
                new_text += "html_theme = 'alabaster'\n"
                changed = True
            elif "html_theme = 'alabaster'" in line and sphinx_ver < 131:
                new_text += "html_theme = 'default'\n"
                changed = True
            else:
                new_text += line

        if changed:
            with open(conf_file, 'w', encoding=UTF_ENC) as f_out:
                f_out.writelines(new_text)

    except ImportError:
        pass


def comment_import_for_py2exe(filename):
    """Comment out unicode_literals import for py2exe build."""
    with open(filename, encoding=UTF_ENC) as f_in:
        lines = f_in.readlines()

    new_text = ''
    for line in lines:
        if '                        unicode_literals)' in line:
            new_text += '                        )  # unicode_literals)\n'
        else:
            new_text += line

    with open(filename, 'w', encoding=UTF_ENC) as f_out:
        f_out.writelines(new_text)


def uncomment_import_for_py2exe(filename):
    """Uncomment unicode_literals import for other builds."""
    with open(filename, encoding=UTF_ENC) as f_in:
        lines = f_in.readlines()

    new_text = ''
    for line in lines:
        if '                        )  # unicode_literals)' in line:
            new_text += '                        unicode_literals)\n'
        else:
            new_text += line

    with open(filename, 'w', encoding=UTF_ENC) as f_out:
        f_out.writelines(new_text)


def collect_to_do():
    """Collect ToDo notes from source files and update README.rst."""
    files = glob.glob(f'{appinfo.APP_NAME}/*.py')
    to_do_list = []
    for filename in files:
        with open(filename, encoding=UTF_ENC) as f_in:
            lines = f_in.readlines()
        for line in lines:
            if '# ToDo: ' in line:
                note = line.split('# ToDo: ', 1)[-1].lstrip()
                to_do_list.append(f'{os.path.basename(filename)}: {note}')

    to_do_text = ''.join(to_do_list)

    with open('README.rst', encoding=UTF_ENC) as f_in:
        lines = f_in.readlines()

    new_text = ''
    to_do_section = False
    changed = False
    for line in lines:
        if '**To do**' in line:
            to_do_section = True
            new_text += '**To do**\n\n' + to_do_text + '\n'
            changed = True
        elif to_do_section and 'Installation' not in line:
            continue
        elif to_do_section and 'Installation' in line:
            to_do_section = False
            new_text += line
        else:
            new_text += line

    if changed:
        with open('README.rst', 'w', encoding=UTF_ENC) as f_out:
            f_out.writelines(new_text)


if __name__ == '__main__':
    eval(sys.argv[1])
