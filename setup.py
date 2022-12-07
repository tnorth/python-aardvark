#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import subprocess

name = 'pyaardvark'
version_py = os.path.join(os.path.dirname(__file__), name, 'version.py')
def git_pep440_version():
    full = subprocess.check_output(
            ['git', 'describe', '--tags', '--always', '--dirty=.dirty'],
            stderr=subprocess.STDOUT).decode().strip()
    tag = subprocess.check_output(
            ['git', 'describe', '--tags', '--always', '--abbrev=0'],
            stderr=subprocess.STDOUT).decode().strip()
    tail = full[len(tag):]
    return tag + tail.replace('-', '.dev', 1).replace('-', '+', 1)

try:
    version = git_pep440_version()
    with open(version_py, 'w') as f:
        f.write('# This file was autogenerated by setup.py\n')
        f.write('__version__ = \'%s\'\n' % (version,))
except (OSError, subprocess.CalledProcessError, IOError) as e:
    try:
        with open(version_py, 'r') as f:
            d = dict()
            exec(f.read(), d)
            version = d['__version__']
    except IOError:
        version = 'unknown'

with open('README.rst') as f:
    readme = f.read()

setup(name = name,
        version = version,
        description = 'Total Phase Aardvark library',
        long_description = readme,
        author = 'Michael Walle',
        author_email = 'michael.walle@kontron.com',
        packages = find_packages(),
        url = 'http://github.com/kontron/python-aardvark',
        license = 'LGPLv2+',
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        entry_points = {
            'console_scripts': [
                'aardvark = pyaardvark.cli_tool:main',
            ]
        },
        test_suite = 'tests',
        include_package_data = True,
        install_requires = ['future'],
)
