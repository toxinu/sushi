#!/usr/bin/env python
# coding: utf-8

import os
import sys

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
	os.makedirs(dst)
	for (path, dirs, files) in os.walk(recipe_dir):
		for d in dirs:
			os.makedirs(os.path.join(dst, d))

		dst_path = path.replace(recipe_dir, dst)
		for f in files:
			dst_file = os.path.join(dst_path, f)
			if f in conf.get('settings', 'ignore').split():
				continue
			if f == '__app__':
				dst_file = os.path.join(dst_path, env['name'])
			try:
				with open(dst_file, 'w') as r:
					r.write(render(os.path.join(path, f), **env))
			except Exception as err:
				logger.info('      | Failed for %s (%s)' % (f, err))

	for (path, dirs, files) in os.walk(dst):
		for d in dirs:
			if d == '__app__':
				src = os.path.join(path, d)
				dst = os.path.join(path, env['module'])
				os.rename(src, dst)

def run_modules(recipe, dst):
	for module in conf.get('settings', 'modules').split():
		try:
			logger.info('    -> %s' % module)
			m = __import__('sushi.ext.%s' % module)
			m = sys.modules['sushi.ext.%s' % module]
			m.run(dst)
		except Exception as err:
			logger.info(' :: Module %s not found (%s)' % (module, err))
