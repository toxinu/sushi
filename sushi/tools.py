#!/usr/bin/env python
# coding: utf-8

from jinja2 import Template

def render(template, **kwargs):
	t = Template(open(template).read())
	return t.render(**kwargs)

def confirm(prompt=None, resp=False):
	try:
		if prompt is None:
			prompt = 'Confirm'

		if resp:
			prompt = '%s [%s|%s]: ' % (prompt, 'n', 'Y')
		else:
			prompt = '%s [%s|%s]: ' % (prompt, 'y', 'N')
		
		while True:
			ans = raw_input(prompt)
			if not ans:
				return resp
			if ans == 'y' or ans == 'Y':
				return True
			if ans == 'n' or ans == 'N':
				return False
			else:
				return False
	except KeyboardInterrupt:
		stream_logger.info('\nAbort.')
		sys.exit(1)