# -*- coding: utf-8 -*-
import os
import shutil

from .core import logger
from .core import conf
from .exceptions import *


class Cookbook(object):
    def __init__(self):
        pass

    def upgrade(self, ignore_errors=False):
        for user in os.listdir(conf.get('paths', 'sushi_cookbooks')):
            for cookbook in os.listdir(os.path.join(
                    conf.get('paths', 'sushi_cookbooks'), user)):
                os.chdir(os.path.join(
                    conf.get('paths', 'sushi_cookbooks'), user, cookbook))
                try:
                    logger.info(' - %s/%s' % (user, cookbook))
                    os.system('git pull')
                except:
                    if ignore_errors:
                        logger.info(
                            'Error: could not update %s/%s cookbook' % (
                                user, cookbook))
                    else:
                        raise CookbookUpdateFailed(
                            'Could not update %s/%s cookbook' % (
                                user, cookbook))
        logger.info('==> Done')

    def list(self):
        res = []
        for user in os.listdir(conf.get('paths', 'sushi_cookbooks')):
            for cookbook in os.listdir(os.path.join(
                    conf.get('paths', 'sushi_cookbooks'), user)):
                res.append('%s/%s' % (user, cookbook))
        return res

    def add(self, repo_name):
        # repo_name = socketubs/sushi-recipes
        # renamed as socketubs-recipes

        if len(repo_name.split('/')) < 2:
            raise CookbookBadURL('Bad cookbook url (socketubs/sushi-recipes)')
        if repo_name.split('/')[1].split('-')[0] != 'sushi':
            raise CookbookBadURL('Bad cookbook url (socketubs/sushi-recipes)')

        url = "https://github.com/%s.git" % repo_name
        user = repo_name.split('/')[0].lower()
        repo_name = '-'.join(repo_name.split('/')[1].split('-')[1:]).lower()

        os.chdir(conf.get('paths', 'sushi_cookbooks'))
        if not os.path.exists(user):
            os.makedirs(user)
        else:
            if repo_name.split('-')[-1] in os.listdir(user):
                raise CookbookAlreadyExists('Cookbook already added')

        return_code = os.system('git clone %s %s' % (
            url, os.path.join(user, repo_name)))
        if return_code >= 1:
            if not os.listdir(user):
                shutil.rmtree(user, ignore_errors=True)
            raise CookbookAddFailed(
                'Failed to add this cookbook (%s)\n!! Return code: %s' % (
                    os.path.join(user, repo_name), return_code))

    def remove(self, repo_name):
        path = '%s/%s' % (conf.get('paths', 'sushi_cookbooks'), repo_name)
        if not os.path.exists(path):
            raise CookbookRemoveFailed('This cookbook not exists')

        shutil.rmtree(path, ignore_errors=True)

        if os.path.exists(os.path.join(conf.get(
                'paths', 'sushi_recipes'), repo_name)):
            shutil.rmtree(os.path.join(conf.get(
                'paths', 'sushi_recipes'), repo_name), ignore_errors=True)

    def get_recipes(self, cookbook_name):
        res = []
        if not os.path.exists(os.path.join(conf.get(
                'paths', 'sushi_cookbooks'), cookbook_name)):
            raise CookbookNotFound('This cookbook does not exists')
        for recipe in os.listdir(os.path.join(
                conf.get('paths', 'sushi_cookbooks'), cookbook_name)):
            if recipe != '.git':
                res.append(recipe)
        return res
