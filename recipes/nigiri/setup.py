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
	name			= '{{ name }}',
	version			= '0.1',
	description 	= '## Set description',
	long_description= open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(), 
	license 		= open('LICENSE').read(),
	author 			= '{{ username }}',
	author_email 	= '{{ email }}',
	url 			= '## Set url',
	keywords 		= '## Set keywords',
	packages 		= ['{{ module }}'],
	scripts 		= ['scripts/{{ name }}'],
	install_requires= ['docopt==0.5.0'],
	classifiers		= (
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7')
)
