#!/usr/bin/env python
# coding: utf-8

import os
import sys

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

if sys.argv[-1] == 'publish':
	os.system('python setup.py sdist upload')
	sys.exit()

setup(
	name='sushi',
	version='0.2.1',
	description='Python package bundler',
	long_description=open('README.md').read(),
	license=open("LICENSE").read(),
	author="Geoffrey Lehee",
	author_email="geoffrey@lehee.name",
	url='https://github.com/socketubs/Sushi/',
	keywords="sushi package python linux",
	packages = ['sushi'],
	scripts=['scripts/sushi'],
	install_requires=[	'jinja2==2.6',
						'docopt==0.5.0',
						'requests==0.13.8',
						'sushi-git',
						'sushi-license'],
	dependency_links = ['https://github.com/Socketubs/Sushi-git/tarball/master#egg=sushi-git',
						'https://github.com/Socketubs/Sushi-license/tarball/master#egg=sushi-license'],
	classifiers=(
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7')
)
