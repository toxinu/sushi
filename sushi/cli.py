#!/usr/bin/env python
# coding: utf-8

import sys

from sushi.core import logger
from sushi.core import conf

from sushi.templates import TemplatesManager
from sushi.unbundler import unbundle
from sushi.unbundler import run_modules
from sushi.starter import Starter
from sushi.tools import confirm

from sushi.exceptions import *

from licenses import Licenses

class Cli(object):
	def __init__(self, *args, **kwargs):
		self.args = kwargs
		logger.disabled = False
	
	def start(self):

		###################
		# starte          #
		###################
		starter = Starter()
		if starter.check():
			if confirm():
				starter.run()
			else:
				print('Abort.')

		###################
		# init            #
		###################
		if self.args.get('init', False):
			path = self.args.get('<path>')
			template = self.args.get('--template', False)
			if not template:
				template = conf.get('settings', 'template', 'default')
			logger.info(' :: Unbundle your project')
			logger.info(' :: Template: %s' % template)
			try:
				unbundle(template, path)
			except Exception as err:
				logger.error('Error: %s' % err)
				sys.exit(1)
			logger.info(' :: Run modules')
			run_modules(template, path)
		###################
		# add             #
		###################
		elif self.args.get('add', False):
			path = self.args.get('<path>')
			logger.info(' :: Add %s into sushi templates' % path)
			manager = TemplatesManager()
			try:
				manager.add(path)
			except Exception as err:
				logger.error('Error: %s' % err)
				sys.exit(1)
		###################
		# del             #
		###################
		elif self.args.get('del', False):
			name = self.args.get('<name>')
			logger.info(' :: Delete %s from sushi templates' % name)
			if confirm():
				manager = TemplatesManager()
				try:
					manager.delete(name)
					logger.info(' :: Done')
				except Exception as err:
					logger.error('Error: %s' % err)
					sys.exit(1)
			else:
				print('Abort.')
				sys.exit(1)
		###################
		# list            #
		###################
		elif self.args.get('list', False):
			manager = TemplatesManager()
			templates = manager.list()
			if not templates:
				logger.info(' :: No templates installed')
				sys.exit(1)
			logger.info(' :: All templates')
			for template in templates:
				if template == conf.get('settings', 'template'):
					logger.info('    - %s (default)' % template)
				else:
					logger.info('    - %s' % template)
		###################
		# licenses        #
		###################
		elif self.args.get('licenses', False):
			licenses = Licenses()
			for license in licenses:
				logger.info(' - %s' % license)			