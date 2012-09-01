#!/usr/bin/env python
# coding: utf-8

from jinja2 import Template

def render(template, **kwargs):
	t = Template(open(template).read())
	return t.render(**kwargs)		