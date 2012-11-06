#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass
import datetime

from sushi.core import conf

from licenses import Licenses

def get_env(name):
    licenses = Licenses()
    now = datetime.datetime.now()
    extras = [u'firstname', u'lastname', u'email']

    d = {   u'username': unicode(getpass.getuser()),
            u'app': unicode(name),
            u'year': unicode(now.year),
            u'day': unicode(now.day),
            u'month': unicode(now.month),
            u'hour': unicode(now.hour),
            u'minute': unicode(now.minute),
            u'second': unicode(now.second),
            u'date': unicode(now.strftime("%Y-%m-%d %H:%M"))
    }

    for extra in extras:
        if conf.has_option('settings', extra):
            d[extra] = conf.get('settings', extra).decode('utf-8')
        else:
            d[extra] = '## Set %s' % extra

    return d