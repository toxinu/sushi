#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

from sushi.core import logger
from sushi.core import conf

from sushi.recipes import RecipesManager
from sushi.cookbook import Cookbook
from sushi.unbundler import unbundle
from sushi.unbundler import run_helpers
from sushi.starter import Starter
from sushi.tools import confirm

from sushi.exceptions import *

from licenses import Licenses

class Cli(object):
    def __init__(self, *args, **kwargs):
        self.args = kwargs
        logger.disabled = False
    
    def start(self):
        ###################
        # craft           #
        ###################
        if self.args.get('craft', False):
            logger.info('==> Craft your project')
            path = self.args.get('<path>')
            recipe = self.args.get('--recipe', False)
            if not recipe:
                recipe = conf.get('settings', 'recipe', 'default')
            logger.info('  => Recipe: %s' % recipe)
            try:
                unbundle(recipe, path)
            except Exception as err:
                logger.info('Error: %s (%s)' % (err, recipe))
                sys.exit(1)
            logger.info('==> Call helpers')
            run_helpers(recipe, path)
            logger.info('==> Done')
        ###################
        # learn           #
        ###################
        elif self.args.get('learn', False):
            recipes = self.args.get('<name>')
            manager = RecipesManager()
            try:
                for recipe in recipes:
                    logger.info('==> Learn %s' % recipe)
                    manager.add(recipe)
            except RecipeAlreadyLearn as err:
                logger.error('Error: %s' % err)
                sys.exit(1)
            logger.info('==> Done')
        ###################
        # forget          #
        ###################
        elif self.args.get('forget', False):
            recipes = self.args.get('<name>')
            manager = RecipesManager()
            try:
                for recipe in recipes:
                    logger.info('==> Forget %s' % recipe)
                    manager.delete(recipe)
                logger.info('==> Done')
            except Exception as err:
                logger.error('Error: %s' % err)
                sys.exit(1)
        ###################
        # list            #
        ################### 
        elif self.args.get('list', False):
            manager = RecipesManager()
            recipes = manager.list()
            if not recipes:
                logger.info('==> No recipe learned')
                sys.exit(1)
            logger.info('==> Recipes learned')
            for recipe in recipes:
                logger.info(recipe)
            sys.exit(0)
        ###################
        # all             #
        ################### 
        elif self.args.get('all', False):
            manager = RecipesManager()
            recipes = manager.list_available()
            if not recipes:
                logger.info('==> No recipe available')
                sys.exit(1)
            logger.info('==> Recipes available')
            for recipe in recipes:
                logger.info(recipe)
            sys.exit(0)
        ###################
        # upgrade         #
        ################### 
        elif self.args.get('upgrade', False):
            cb = Cookbook()
            logger.info('==> Update cookbooks')
            cookbooks = cb.upgrade(ignore_errors=True)
        ###################
        # cookbook        #
        ###################
        elif self.args.get('cookbook', False):
            cb = Cookbook()
            cookbooks = cb.list()
            if not cookbooks:
                logger.info('==> No cookbooks registered')
                sys.exit(1)
            logger.info('==> Cookbooks')
            for cookbook in cookbooks:
                logger.info(cookbook)
            sys.exit(0)
        ###################
        # cookbook-add    #
        ###################
        elif self.args.get('cookbook-add', False):
            repo_name = self.args.get('<name>')
            logger.info('==> Add %s cookbook' % repo_name)
            cb = Cookbook()
            try:
                cb.add(repo_name)
                logger.info('==> Done')
            except CookbookException as err:
                logger.info('Error: %s' % err)
                sys.exit(1)
            sys.exit(0)
        ###################
        # cookbook-del    #
        ###################
        elif self.args.get('cookbook-del', False):
            repo_name = self.args.get('<name>')
            logger.info('==> Delete %s cookbook' % repo_name)
            cb = Cookbook()
            if confirm():
                try:
                    cb.remove(repo_name)
                    logger.info('==> Done')
                except CookbookException as err:
                    logger.info('Error: %s' % err)
                    sys.exit(1)
            else:
                print('Abort.')
                sys.exit(1)
            sys.exit(0)

        sys.exit(100)