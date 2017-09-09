#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages
from setuptools import setup

import ast
import re

# get version from __version__ variable in RestApiz/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('RestApiz/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
    'pymysql', 'Flask', 'flask-cors',
]

setup_requirements = [
    'pytest-runner',
    'pymysql',
    'Flask>=0.10.1',
    'flask-cors',
    # TODO(shridarpatil): put setup requirements (distutils extensions, etc.)
]

test_requirements = [
    'pytest',
    'pymysql',
    'Flask>=0.10.1',
    'flask-cors',
    # TODO: put package test requirements here
]

github_url = 'https://github.com/shridarpatil/RestApiz'
download_url = github_url + '/archive/' + version + '.tar.gz'

setup(
    name='RestApiz',
    version=version,
    description="Create rest api's dynamically within no time.",
    long_description=readme + '\n\n' + history,
    author="Shridhar Patil",
    author_email='shridharpatil2792@gmail.com',
    url=github_url,
    download_url=download_url,
    packages=find_packages(include=("RestApiz", "dashboard",)),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='RestApiz',
    entry_points={
        'console_scripts': [
            'restapi=dashboard.cli:main'
        ]
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
