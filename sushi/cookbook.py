#!/usr/bin/env python
# coding: utf-8
import os
import git
import shutil

from sushi.core import logger

from sushi.core import conf
from sushi.exceptions import *

class Cookbook(object):
    def __init__(self):
        pass

    def upgrade(self, ignore_errors=False):
        for user in os.listdir(conf.get('paths', 'sushi_cookbooks')):
            for cookbook in os.listdir('%s/%s' % (conf.get('paths', 'sushi_cookbooks'), user)):
                os.chdir('%s/%s/%s' % (conf.get('paths', 'sushi_cookbooks'), user, cookbook))
                try:
                    logger.info(' - %s/%s' % (user, cookbook))
                    os.system('git pull')
                except:
                    if ignore_errors:
                        logger.info('Error: could not update %s/%s cookbook' % (user, cookbook))
                    else:
                        raise CookbookException('Could not update %s/%s cookbook' % (user, cookbook))
        logger.info('==> Done')

    def list(self):
        res = []
        for user in os.listdir(conf.get('paths', 'sushi_cookbooks')):
            for cookbook in os.listdir('%s/%s' % (conf.get('paths', 'sushi_cookbooks'), user)):
                res.append('%s/%s' % (user, cookbook))
        return res

    def add(self, repo_name):
        # repo_name = socketubs/sushi-recipes
        # renamed as socketubs-recipes

        if len(repo_name.split('/')) < 2:
            raise CookbookException('Bad cookbook url (socketubs/sushi-recipes)')
        if repo_name.split('/')[1].split('-')[0] != 'sushi':
            raise CookbookException('Bad cookbook url (socketubs/sushi-recipes)')

        url = "git://github.com/%s.git" % repo_name
        user = repo_name.split('/')[0].lower()
        repo_name = '-'.join(repo_name.split('/')[1].split('-')[1:]).lower()

        os.chdir(conf.get('paths', 'sushi_cookbooks'))
        if not os.path.exists(user):
            os.makedirs(user)
        else:
            if repo_name.split('-')[-1] in os.listdir(user):
                raise CookbookException('Cookbook already added')
        try:
            os.system('git clone %s %s/%s' % (url, user, repo_name))
        except Exception as err:
            if not os.listdir(user):
                os.remove(user)
            raise CookbookException('Failed to add this cookbook (%s/%s)\nError: %s' % (user, repo_name, err))

    def remove(self, repo_name):
        path = '%s/%s' % (conf.get('paths', 'sushi_cookbooks'), repo_name)
        if not os.path.exists(path):
            raise CookbookException('This cookbook not exist')

        shutil.rmtree(path, ignore_errors=True)

        if os.path.exists('%s/%s' % (conf.get('paths', 'sushi_recipes'), repo_name)):
            shutil.rmtree('%s/%s' % (conf.get('paths', 'sushi_recipes'), repo_name), ignore_errors=True)

    def get_recipes(self, cookbook_name):
        res = []
        for recipe in os.listdir('%s/%s' % (conf.get('paths', 'sushi_cookbooks'), cookbook_name)):
            if recipe != '.git':
                res.append(recipe)
        return res
