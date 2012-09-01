#!/usr/bin/env python
# coding: utf-8

from sushi.core import conf

from licenses import Licenses

def run(dst):
	licenses = Licenses()
	license = conf.get('settings', 'license')
	dst = os.path.join(dst, 'LICENSE')

	with open(dst, 'w') as l:
		l.write(licenses[license]['url'])