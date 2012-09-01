#!/usr/bin/env python
# coding: utf-8

import os

from ConfigParser import SafeConfigParser

from sushi.core import logger

default_conf = """[settings]
template = default
license  = agpl-v3
ignore   = .DS_Store
modules  = license"""

def get_conf():
	# Create paths
	user_home = os.getenv('HOME')
	sushi_path = os.path.join(user_home, '.sushi')
	sushi_conf = os.path.join(sushi_path, 'sushi.conf')
	sushi_templates = os.path.join(sushi_path, 'templates')

	if not os.path.exists(sushi_path):
		logger.info('Create sushi conf folder')
		os.makedirs(sushi_path)
		os.makedirs(sushi_templates)
		with open(sushi_conf, 'w') as f:
			f.write(default_conf)

	parser = SafeConfigParser()
	parser.read(sushi_conf)

	parser.add_section('paths')
	parser.set('paths', 'home', user_home)
	parser.set('paths', 'sushi', sushi_path)
	parser.set('paths', 'sushi_conf', sushi_conf)
	parser.set('paths', 'sushi_templates', sushi_templates)

	# Defaults
	if not parser.has_section('settings'):
		parser.add_section('settings')
	if not parser.has_option('settings', 'license'):
		parser.set('settings', 'license', 'agpl-v3')
	if not parser.has_option('settings', 'template'):
		parser.set('settings', 'template', 'default')
	if not parser.has_option('settings', 'ignore'):
		parser.set('settings', 'ignore', '.DS_Store')
	if not parser.has_option('settings', 'modules'):
		parser.set('settings', 'modules', '')

	return parser