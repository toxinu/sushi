# -*- coding: utf-8 -*-
import os
import codecs

try:
    from ConfigParser import SafeConfigParser
except ImportError:
    from configparser import SafeConfigParser

from .core import logger

default_conf = """[settings]
recipe   = basic
license  = agpl-v3

helpers  = """


def get_conf():
    # Create paths
    user_home = os.getenv('HOME')
    sushi_path = os.path.join(user_home, '.sushi')
    sushi_conf = os.path.join(sushi_path, 'sushi.conf')
    sushi_recipes = os.path.join(sushi_path, 'recipes')
    sushi_cookbooks = os.path.join(sushi_path, 'cookbooks')

    if not os.path.exists(sushi_path):
        logger.info('Create sushi conf folder')
        os.makedirs(sushi_path)
        os.makedirs(sushi_recipes)
        os.makedirs(sushi_cookbooks)
        with codecs.open(sushi_conf, mode='w', encoding='utf-8') as f:
            f.write(default_conf)

    parser = SafeConfigParser()
    parser.read(sushi_conf)

    parser.add_section('paths')
    parser.set('paths', 'home', user_home)
    parser.set('paths', 'sushi', sushi_path)
    parser.set('paths', 'sushi_conf', sushi_conf)
    parser.set('paths', 'sushi_recipes', sushi_recipes)
    parser.set('paths', 'sushi_cookbooks', sushi_cookbooks)

    # Defaults
    if not parser.has_section('settings'):
        parser.add_section('settings')
    if not parser.has_option('settings', 'license'):
        parser.set('settings', 'license', 'agpl-v3')
    if not parser.has_option('settings', 'recipe'):
        parser.set('settings', 'recipe', 'default')
    if not parser.has_option('settings', 'helpers'):
        parser.set('settings', 'helpers', '')

    return parser
