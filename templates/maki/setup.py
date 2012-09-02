#!/usr/bin/env python
# coding: utf-8

import os
import sys

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(
	name			= '{{ name }}',
	version			= '0.1',
	description 	= '## Set description',
	long_description= open('README.md').read(), 
	license 		= open('LICENSE').read(),
	author 			= '{{ username }}',
	author_email 	= '{{ email }}',
	url 			= '## Set url',
	keywords 		= '## Set keywords',
	packages 		= ['{{ name }}'],
	install_requires= [],
	classifiers		= (
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7')
)
