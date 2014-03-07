# -*- coding: utf-8 -*-
import sys
import getpass
import datetime

from .core import conf

if sys.version_info[0] == 3:
    s = str
else:
    s = unicode


def get_env(name):
    now = datetime.datetime.now()
    extras = [u'firstname', u'lastname', u'email']

    d = {
        u'username': s(getpass.getuser()),
        u'app': s(name),
        u'year': s(now.year),
        u'day': s(now.day),
        u'month': s(now.month),
        u'hour': s(now.hour),
        u'minute': s(now.minute),
        u'second': s(now.second),
        u'date': s(now.strftime("%Y-%m-%d %H:%M"))}

    for extra in extras:
        if conf.has_option('settings', extra):
            d[extra] = conf.get('settings', extra).decode('utf-8')
        else:
            d[extra] = '## Set %s' % extra

    return d
