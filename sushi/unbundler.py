#!/usr/bin/env python
# coding: utf-8

import os
import sys

from sushi.core import conf
from sushi.core import logger
from sushi.tools import render
from sushi.env import get_env

def unbundle(template, dst):
	env = get_env(dst)
	template_dir = os.path.join(conf.get('paths', 'sushi_templates'), template)

	if os.path.exists(dst):
		logger.info(' :: Destination (%s) already exist' % dst)
		sys.exit(1)
	os.makedirs(dst)
	for (path, dirs, files) in os.walk(template_dir):
		for d in dirs:
			os.makedirs(os.path.join(dst, d))

		dst_path = path.replace(template_dir, dst)
		for f in files:
			if f in conf.get('settings', 'ignore').split():
				continue
			logger.info(' - %s' % f)
			logger.debug(' - %s (%s)(%s)' % (f, path, dst_path))
			try:
				with open(os.path.join(dst_path, f), 'w') as r:
					r.write(render(os.path.join(path, f), **env))
			except Exception as err:
				logger.info('   | Failed for %s (%s)' % (f, err))

	for (path, dirs, files) in os.walk(dst):
		for d in dirs:
			if d == '__app__':
				src = os.path.join(path, d)
				dst = os.path.join(path, env['module'])
				os.rename(src, dst)

def run_modules(template, dst):
	for module in conf.get('settings', 'modules').split():
		try:
			logger.info(module)
			m = __import__('sushi.extra.%s' % module)
			m.run(dst)
		except Exception as err:
			logger.info(' :: Module %s not found (%s)' % (module, err))
