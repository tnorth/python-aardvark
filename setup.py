#!/usr/bin/env python

from setuptools import setup, find_packages
from subprocess import Popen, PIPE

def get_git_version():
    try:
        p = Popen(['git', 'describe', '--tags', '--always', '--dirty'],
                stdout=PIPE, stderr=PIPE)
        p.stderr.close()
        if p.wait() == 0:
            return p.stdout.readlines()[0].strip()
    except:
        pass
    raise AssertionError('Could not find the version number')

def main():
    version = get_git_version()

    with open('pyaardvark/version.py', 'w') as f:
        f.write('# This file was autogenerated by setup.py\n')
        f.write('__version__ = \'%s\'\n' % (version,))

    setup(name = 'pyaardvark',
            version = version,
            description = 'Totalphase Aardvark library',
            author_email = 'michael.walle@kontron.com',
            packages = find_packages(),
            license = 'LGPLv2+',
            classifiers = [
                'Development Status :: 4 - Beta',
                'Environment :: Console',
                'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
                'Natural Language :: English',
                'Operating System :: OS Independent',
                'Programming Language :: Python :: 2',
                'Programming Language :: Python :: 2.7',
                'Topic :: Software Development :: Libraries :: Python Modules',
            ],
            package_data = {
                'pyaardvark.ext':
                    ['aardvark.so', 'LICENSE.txt']
            },
            entry_points = {
                'console_scripts': [
                    'aardvark = pyaardvark.cli_tool:main',
                ]
            }
    )

if __name__ == '__main__':
    main()
