#!/usr/bin/env python
# coding: utf-8

import sys

from sushi.core import logger
from sushi.core import conf

from sushi.templates import TemplatesManager
from sushi.unbundler import unbundle
from sushi.unbundler import run_modules

from licenses import Licenses

class Cli(object):
	def __init__(self, *args, **kwargs):
		self.args = kwargs
		logger.disabled = False
	
	def start(self):
		if self.args.get('init', False):
			path = self.args.get('<name>')
			template = self.args.get('--template', False)
			if not template:
				template = conf.get('settings', 'template', 'default')
			unbundle(template, path)
			run_modules(template, path)
		elif self.args.get('add', False):
			path = self.args.get('<path>')
			logger.info(' :: Add %s into sushi packages' % path)
			manager = TemplatesManager()
			manager.add(path)
		elif self.args.get('del', False):
			name = self.args.get('<name>')
			logger.info(' :: Delete %s from sushi packages' % name)
			manager = TemplatesManager()
			manager.delete(name)
		elif self.args.get('list', False):
			manager = TemplatesManager()
			templates = manager.list()
			if not templates:
				logger.info(' :: No templates installed')
				sys.exit(1)
			logger.info(' :: All packages')
			for template in templates:
				if template == conf.get('settings', 'template'):
					logger.info('    - %s (default)' % template)
				else:
					logger.info('    - %s' % template)
		elif self.args.get('licenses', False):
			licenses = Licenses()
			for license in licenses:
				logger.info(' - %s' % license)			