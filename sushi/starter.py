#!/usr/bin/env python
# coding: utf-8

import os
import requests
import tarfile

from sushi.core import logger
from sushi.core import conf
from sushi.recipes import RecipesManager
from sushi.tools import confirm

class Starter(object):
	def __init__(self):
		self.manager = RecipesManager()

	def check(self):
		if not self.manager.list():
			logger.info(" :: I think it's your first time with sushi")
			logger.info(" :: Can I suggest you simple maki recipe ?")
			return True
		return False

	def run(self):
		url = 'https://github.com/Socketubs/Sushi/raw/master/recipes/maki.tar.gz'

		logger.info(' :: Downloading')
		r = requests.get(url, prefetch=False)
		r.raise_for_status()

		src = os.path.join(conf.get('paths', 'sushi_recipes'), 'maki.tar.gz')
		dst = conf.get('paths', 'sushi_recipes')

		with open(src, 'w') as f:
			for buf in r.iter_content(1024):
				if buf:
					f.write(buf)

		logger.info(' :: Extracting')
		# Open tarfile
		tar = tarfile.open(src, 'r:gz')
		if tarfile.is_tarfile(src):
			tar.extractall(dst)
		else:
			raise Exception('Archive invalid (not a gzipped tarfile)')

		# Remove archive
		os.remove(src)
		logger.info(' :: Done')
