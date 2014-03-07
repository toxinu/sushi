# -*- coding: utf-8 -*-
import os
import sys
import shutil
import codecs

from .core import conf
from .core import logger
from .tools import render
from .env import get_env
from .recipes import RecipesManager
from .exceptions import *


def unbundle(recipe, dst):
    manager = RecipesManager()
    recipe_dir = manager.get(recipe)

    if manager.name_handler(recipe) not in manager.list_available():
        raise UnbundlerException("Don't know this recipe.")

    env = get_env(dst)

    if os.path.exists(dst):
        raise UnbundlerException('Destination (%s) already exist' % dst)

    ##################
    # Copy every dir #
    ##################
    def ignore(folder, names):
        _res = []
        for n in names:
            if not os.path.isdir(os.path.join(folder, n)):
                if conf.has_option('settings', 'ignore'):
                    if n in conf.get('settings', 'ignore').split():
                        _res.append(n)
        return _res

    shutil.copytree(recipe_dir, dst, ignore=ignore)

    ############################################
    # Copy every file and render it on the fly #
    ############################################
    for path, dirs, files in os.walk(recipe_dir):
        for f in files:
            if conf.has_option('settings', 'ignore'):
                if f in conf.get('settings', 'ignore').split():
                    continue
            fdst = os.path.join(path.replace(recipe_dir, dst), f)
            try:
                with codecs.open(fdst, mode='w', encoding='utf-8') as r:
                    r.write(render(os.path.join(path, f), **env))
            except Exception as err:
                logger.info('      | Failed for %s (%s)' % (f, err))

    ######################################
    # Rename every __app__ to {{ name }} #
    ######################################
    for r, s, f in os.walk(dst):
        # Folders
        if "__app__" in s:
            os.rename(os.path.join(r, "__app__"),
                      os.path.join(r, env['app'].lower()))
    for r, s, f in os.walk(dst):
        # Files
        if "__app__" in f:
            os.rename(os.path.join(r, "__app__"),
                      os.path.join(r, env['app'].lower()))


def run_helpers(recipe, dst):
    for helper in conf.get('settings', 'helpers').split():
        try:
            logger.info('    -> %s' % helper)
            m = __import__('sushi_ext_%s' % helper)
            m = sys.modules['sushi_ext_%s' % helper]
            m.run(dst)
        except Exception as err:
            logger.info(' :: Helper %s not found (%s)' % (helper, err))
