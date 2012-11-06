# -*- coding: utf-8 -*-
import sys
import codecs

from sushi.core import logger
from jinja2 import Template


def render(recipe, **kwargs):
    t = Template(codecs.open(recipe, mode='r', encoding='utf-8').read())
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
        logger.info('\nAbort.')
        sys.exit(1)
