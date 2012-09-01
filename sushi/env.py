#!/usr/bin/env python
# coding: utf-8

import getpass
import datetime


from sushi.core import conf

from licenses import Licenses

def get_env(name):
	licenses = Licenses()
	now = datetime.datetime.now()

	return {'license':	conf.get('settings', 'license'),
			'license_content': licenses[conf.get('settings', 'license')]['url'],
			'username': getpass.getuser(),
			'module': name.lower().replace('-', '_'),
			'name': name,
			'year': now.year,
			'day': now.day,
			'month': now.month,
			'hour': now.hour,
			'minute': now.minute,
			'second': now.second,
			'date': now.strftime("%Y-%m-%d %H:%M")
	}
