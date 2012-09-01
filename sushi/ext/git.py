#!/usr/bin/env python
# coding: utf-8

import os
import subprocess

def run(dst):
	popen = subprocess.Popen(['git', 'init', dst])
	popen.wait()
	