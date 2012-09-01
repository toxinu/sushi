#!/usr/bin/env python
# coding: utf-8

import os
import sys
import tarfile
import shutil

from sushi.core import conf

class TemplatesManager(object):
	def __init__(self):
		pass

	def list(self):
		return os.listdir(conf.get('paths', 'sushi_templates'))

	def add(self, path):
		src = path
		dst = conf.get('paths', 'sushi_templates')

		# Open tarfile
		tar = tarfile.open(src, 'r:gz')
		if tarfile.is_tarfile(src):
			tar.extractall(dst)
		else:
			raise Exception('Archive invalid (not a tarfile)')

	def delete(self, name):
		dst = os.path.join(conf.get('paths', 'sushi_templates'), name)
		shutil.rmtree(dst)
