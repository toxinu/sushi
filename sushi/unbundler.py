#!/usr/bin/env python
# coding: utf-8

import os
import sys
import shutil

from sushi.core import conf
from sushi.core import logger
from sushi.tools import render
from sushi.env import get_env
from sushi.recipes import RecipesManager

from sushi.exceptions import *

def unbundle(recipe, dst):
	manager = RecipesManager()
	recipe_dir = manager.get(recipe)

	env = get_env(dst)

	if os.path.exists(dst):
		raise UnbundlerException('Destination (%s) already exist' % dst)

	##################
	# Copy every dir #
	##################
	def ignore(folder, names):
		return [n for n in names if
			not os.path.isdir(os.path.join(folder, n)) and
			n in conf.get('settings', 'ignore').split()]

	shutil.copytree(recipe_dir, dst, ignore=ignore)

	############################################
	# Copy every file and render it on the fly #
	############################################
	for path, dirs, files in os.walk(recipe_dir):
		for f in files:
			fdst = os.path.join(path.replace(recipe_dir, dst), f)
			try:
				with open(fdst, 'w') as r:
					r.write(render(os.path.join(path, f), **env))
			except Exception as err:
				logger.info('      | Failed for %s (%s)' % (f, err))

	######################################
	# Rename every __app__ to {{ name }} #
	######################################
	for r,s,f in os.walk(dst):
		# Folders
		if "__app__" in s:
			os.rename(os.path.join(r, "__app__"), os.path.join(r, env['name']))
		# Files
		if "__app__" in f:
			os.rename(os.path.join(r, "__app__", os.path.join(r, env['name'])))

def run_helpers(recipe, dst):
	for helper in conf.get('settings', 'helpers').split():
		try:
			logger.info('    -> %s' % helper)
			m = __import__('sushi_ext_%s' % helper)
			m = sys.modules['sushi_ext_%s' % helper]
			m.run(dst)
		except Exception as err:
			logger.info(' :: Helper %s not found (%s)' % (helper, err))
