#!/usr/bin/env python
# coding: utf-8

import sys
import os

from sushi.core import logger
from sushi.core import conf

from sushi.recipes import RecipesManager
from sushi.unbundler import unbundle
from sushi.unbundler import run_helpers
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
		# starter         #
		###################
#		starter = Starter()
#		if starter.check():
#			if confirm():
#				try:
#					starter.run()
#				except Exception as err:
#					logger.info(err)
#					sys.exit(1)
#			else:
#				print('Abort.')

		###################
		# init            #
		###################
		if self.args.get('craft', False):
			logger.info(' :: Craft your project')
			path = self.args.get('<path>')
			recipe = self.args.get('--recipe', False)
			if not recipe:
				recipe = conf.get('settings', 'recipe', 'default')
			logger.info('    -> Recipe: %s' % recipe)
			try:
				unbundle(recipe, path)
			except Exception as err:
				logger.info('Error: %s' % err)
				sys.exit(1)
			logger.info(' :: Call helpers')
			run_helpers(recipe, path)
			logger.info(' :: Done')
		###################
		# learn           #
		###################
		elif self.args.get('learn', False):
			path = self.args.get('<path>')
			logger.info(' :: Learn given recipe')
			manager = RecipesManager()
			try:
				manager.add(path)
			except Exception as err:
				logger.error('Error: %s' % err)
				sys.exit(1)
			logger.info(' :: Done')
		###################
		# forget          #
		###################
		elif self.args.get('forget', False):
			name = self.args.get('<name>')
			logger.info(' :: Forget %s recipe' % name)
			if confirm():
				manager = RecipesManager()
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
		# cookbook        #
		###################
		elif self.args.get('cookbook', False):
			manager = RecipesManager()
			recipes = manager.list()
			if not recipes:
				logger.info(' :: No recipe learned')
				sys.exit(1)
			logger.info(' :: Recipes')
			for recipe in recipes:
				if recipe == conf.get('settings', 'recipe'):
					logger.info('    -> %s (default)' % recipe)
				else:
					logger.info('    -> %s' % recipe)
		###################
		# licenses        #
		###################
		elif self.args.get('licenses', False):
			licenses = Licenses()
			for license in licenses:
				logger.info(' - %s' % license)			
