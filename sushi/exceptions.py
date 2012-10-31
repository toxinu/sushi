# coding: utf-8

# CookbookException
class CookbookException(RuntimeError):
	""" Cookbook Error """

class CookbookError(CookbookException):
	def __init__(self, value):
		self.parameter = value
	def __str__(self):
		return repr(self.parameter)

# RecipesManagerException
class RecipesManagerException(RuntimeError):
	""" RecipesManager Error """

class RecipesManagerError(RecipesManagerException):
	def __init__(self, value):
		self.parameter = value
	def __str__(self):
		return repr(self.parameter)

# Unbundler
class UnbundlerException(RuntimeError):
	""" Unbundler Error """

class UnbundlerError(UnbundlerException):
	def __init__(self, value):
		self.parameter = value
	def __str__(self):
		return repr(self.parameter)

# Starter
class StarterException(RuntimeError):
	""" Starter Error """

class StarterError(StarterException):
	def __init__(self, value):
		self.parameter = value
	def __str__(self):
		return repr(self.parameter)