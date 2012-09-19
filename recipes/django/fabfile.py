import os
import sys
from fabric.api import task, local

@task
def update_requirements(env):
	virtualenv('pip install -r requirements/%s.txt' % env)

@task
def runserver(env, ip='127.0.0.1', port=8000):
	virtualenv('python manage.py runserver %s:%s --settings=\'{{ name }}.settings.%s\'' % (ip, port, env))

@task
def syncdb(env):
	virtualenv('python manage.py syncdb --settings=\'{{ name }}.settings.%s\'' % env)

def virtualenv(command):
	if not os.path.exists('venv'):
		print(' :: I need a virtualenv (venv). Use init_venv.')
		sys.exit(1) 
        local('source venv/bin/activate && ' + command)

@task
def init_venv():
	local('virtualenv venv')
