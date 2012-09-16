#!/usr/bin/env python
# coding: utf-8

import os
import sys
import tarfile
import shutil
import requests
import tempfile

from sushi.core import conf
from sushi.core import logger
from sushi.exceptions import *


class RecipesManager(object):
	def __init__(self):
		pass

	def list(self):
		return os.listdir(conf.get('paths', 'sushi_recipes'))

	def add(self, path):
		src = path
		dst = conf.get('paths', 'sushi_recipes')
		http_handler = False
		file_handler = False

		# Http handler
		if src[:5] == 'http+':
			http_handler = True
			url = src[5:]
			f = tempfile.NamedTemporaryFile(delete=False)
			src = f.name
			logger.info('    -> Download file')
			f = open(src, 'w')
			data = requests.get(url).content
			f.write(data)
			f.close()
		else:
			file_handler = True
			
		# File
		if not os.path.isfile(src):
			raise RecipesManagerException('Recipe is not gzipped tar file')

		# Open tarfile
		if tarfile.is_tarfile(src):
			tar = tarfile.open(src, 'r:gz')
			tar.extractall(dst)
		else:
			raise RecipesManagerException('Recipe is not gzipped tar file')

		if http_handler:
			logger.info('    -> Clean')
			os.remove(src)

	def delete(self, name):
		if name not in self.list():
			raise RecipesManagerException('Recipe %s not installed' % name)
		dst = os.path.join(conf.get('paths', 'sushi_recipes'), name)
		shutil.rmtree(dst)

	def get(self, name):
		if name not in self.list():
			raise RecipesManagerException('Recipe %s not available' % name)
		return os.path.join(conf.get('paths', 'sushi_recipes'), name)
