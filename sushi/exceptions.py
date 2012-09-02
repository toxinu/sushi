# coding: utf-8

# TemplatesManagerException
class TemplatesManagerException(RuntimeError):
	""" TemplatesManager Error """

class TemplatesManagerError(TemplatesManagerException):
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