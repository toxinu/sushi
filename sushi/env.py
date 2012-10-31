#!/usr/bin/env python
# coding: utf-8

import getpass
import datetime


from sushi.core import conf

from licenses import Licenses

def get_env(name):
	licenses = Licenses()
	now = datetime.datetime.now()
	extras = ['firstname', 'lastname', 'email']

	d = {	'license':	conf.get('settings', 'license'),
			'license_content': licenses[conf.get('settings', 'license')]['url'],
			'username': getpass.getuser(),
			'module': name.lower().replace('-', '_'),				
			'app': name,
			'year': now.year,
			'day': now.day,
			'month': now.month,
			'hour': now.hour,
			'minute': now.minute,
			'second': now.second,
			'date': now.strftime("%Y-%m-%d %H:%M")
	}

	for extra in extras:
		if conf.has_option('settings', extra):
			d[extra] = conf.get('settings', extra)
		else:
			d[extra] = '## Set %s' % extra

	return d