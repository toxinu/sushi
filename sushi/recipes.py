# -*- coding: utf-8 -*-
import os
import shutil

from .core import conf
from .cookbook import Cookbook
from .exceptions import *


class RecipesManager(object):
    def __init__(self):
        pass

    def name_handler(self, name):
        cb = Cookbook()

        if '/' in name:
            if len(name.split('/')) < 3:
                raise RecipeBadNameFormat(
                    'Recipe name incorrect (socketubs/recipes/basic)')
            recipe = name.split('/')[-1].lower()
            user = name.split('/')[0].lower()
            cookbook_name = name.split('/')[1].lower()
            cookbook = '%s/%s' % (user, cookbook_name)

            if not recipe in cb.get_recipes(cookbook):
                raise RecipeUnmatched('Not recipe found')
            recipe = '%s/%s' % (cookbook, recipe)
        else:
            recipe = name
            results = []

            for cookbook in cb.list():
                if recipe in cb.get_recipes(cookbook):
                    results.append('%s/%s' % (cookbook, recipe))

            if not results:
                raise RecipeUnvailable('Not recipe found')

            if len(results) > 1:
                founds = '\n'.join(results)
                raise RecipeUnmatched(
                    'Many results found, please give me cookbook.\n\n%s\n' % founds)
            recipe = results[0]

        return recipe

    def list_available(self):
        res = []
        root = conf.get('paths', 'sushi_cookbooks')
        for user in os.listdir(root):
            for cookbook in os.listdir('%s/%s' % (root, user)):
                for recipe in os.listdir('%s/%s/%s' % (root, user, cookbook)):
                    if recipe != '.git':
                        res.append('%s/%s/%s' % (user, cookbook, recipe))
        return res

    def list(self):
        root = conf.get('paths', 'sushi_recipes')
        res = []
        for user in os.listdir(root):
            for cookbook in os.listdir('%s/%s' % (root, user)):
                for recipe in os.listdir('%s/%s/%s' % (root, user, cookbook)):
                    res.append('%s/%s/%s' % (user, cookbook, recipe))
        return res

    def add(self, name):
        recipe = self.name_handler(name)

        src_repo = '%s/%s' % (conf.get('paths', 'sushi_cookbooks'), '/'.join(recipe.split('/')[:-1]))
        dst_repo = '%s/%s' % (conf.get('paths', 'sushi_recipes'), '/'.join(recipe.split('/')[:-1]))
        src_recipe = '%s/%s' % (src_repo, recipe.split('/')[-1])
        dst_recipe = '%s/%s' % (dst_repo, recipe.split('/')[-1])

        # recipe: socketubs/recipes/django
        # src_repo: /Users/socketubs/.sushi/cookbooks/socketubs-recipes
        # dst_repo: /Users/socketubs/.sushi/recipes/socketubs-recipes
        # src_recipe: src_repo + /django
        # dst_recipe: dst_repo _ /django

        if not os.path.exists(dst_repo):
            os.makedirs(dst_repo)

        try:
            os.symlink(os.path.join(src_recipe, 'content'), dst_recipe)
        except OSError:
            raise RecipeAlreadyLearn('Recipe %s already learned' % recipe)

    def delete(self, name):
        recipe = self.name_handler(name)

        dst_user = '%s/%s' % (conf.get('paths', 'sushi_recipes'), recipe.split('/')[0])
        dst_repo = '%s/%s' % (conf.get('paths', 'sushi_recipes'), '/'.join(recipe.split('/')[:-1]))
        dst_recipe = '%s/%s' % (dst_repo, recipe.split('/')[-1])

        try:
            os.remove(dst_recipe)
            if not os.listdir(dst_repo):
                shutil.rmtree(dst_repo)
                if not os.listdir(dst_user):
                    shutil.rmtree(dst_user)
        except:
            raise RecipeUnmatched("Nothing to forget.")

    def get(self, name):
        recipe = self.name_handler(name)
        if recipe not in self.list():
            raise RecipeUnvailable("Recipe not learned")
        return os.path.join(conf.get('paths', 'sushi_recipes'), recipe)
