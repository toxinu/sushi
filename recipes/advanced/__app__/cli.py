#!/usr/bin/env python
# coding: utf-8

import sys

from {{ module }}.core import stream_logger

class Cli(object):
	def __init__(self, *args, **kwargs):
		self.args = kwargs
		stream_logger.disabled = False

	def start(self):
		pass