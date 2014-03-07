# -*- coding: utf-8 -*-


class CookbookException(RuntimeError):
    """ Cookbook Error """
    def __init__(self, value):
        self.message = value

    def __str__(self):
        return repr(self.message)


class CookbookNotFound(CookbookException):
    """ Cookbook not found """


class CookbookAlreadyExists(CookbookException):
    """ Cookbook already exists """


class CookbookBadURL(CookbookException):
    """ Cookbook bad URL """

class CookbookAddFailed(CookbookException):
    """ Cookbook add failed """

class CookbookUpdateFailed(CookbookException):
    """ Cookbook update failed """

class CookbookRemoveFailed(CookbookException):
    """ Cookbook remove failed """

# RecipesManagerException
class RecipesManagerException(RuntimeError):
    """ RecipesManager Error """
    def __init__(self, value):
        self.message = value
    def __str__(self):
        return repr(self.message)

class RecipesManagerError(RecipesManagerException):
    """ Generic Exception """

class RecipeAlreadyLearn(RecipesManagerException):
    """ Recipe already learned """

class RecipeUnvailable(RecipesManagerException):
    """ Recipe unvailable """

class RecipeUnmatched(RecipesManagerException):
    """ Recipe unmatched """

class RecipeBadNameFormat(RecipesManagerException):
    """ Recipe with wrong format """

# Unbundler
class UnbundlerException(RuntimeError):
    """ Unbundler Error """

class UnbundlerError(UnbundlerException):
    def __init__(self, value):
        self.message = value
    def __str__(self):
        return repr(self.message)

# Starter
class StarterException(RuntimeError):
    """ Starter Error """

class StarterError(StarterException):
    def __init__(self, value):
        self.message = value
    def __str__(self):
        return repr(self.message)
