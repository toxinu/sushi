Sushi
=====

Sushi is package builder based on template. Enough to create same package structure every time. Create custom recipes for Flask, Django or every BoilerPlate you want!

Sushi can learn/unlearn/upgrade every recipes you want. Like package manager for recipes.
You have to give every cookbook (repository) you want to Sushi and all it's recipes will be available to you.

And of course you can very easily create your own cookbook cause they are *Github* repositories.

Features
--------

- Create template for everything based on Jinja2
- Deploy the same everytime
- Make specific recipe for Flask, Django, ...
- Use helpers (plugins) to not waste time
- Auto ``git init`` your package

Sushi support helper(extensions) and there are easy to create. There are already some extension, like ``git``.

Quick start
-----------

Installation
~~~~~~~~~~~~

::

    pip install sushi

Meet the cookchef
~~~~~~~~~~~~~~~~~

If it's the first time your run Sushi, your cookbook must be empty.
You can add my personnal cookbook to your in order to discover sushi:

::

    Sushi » sushi cookbook-add socketubs/sushi-recipes
    ==> Add socketubs/sushi-recipes cookbook
    Cloning into 'socketubs/recipes'...
    remote: Counting objects: 126, done.
    remote: Compressing objects: 100% (84/84), done.
    remote: Total 126 (delta 46), reused 108 (delta 28)
    Receiving objects: 100% (126/126), 44.95 KiB, done.
    Resolving deltas: 100% (46/46), done.
    ==> Done

First recipe
~~~~~~~~~~~~

List all recipes available on my cookbook:

::

    Sushi » sushi all
    ==> Recipes available
    socketubs/recipes/advanced
    socketubs/recipes/basic
    socketubs/recipes/django
    socketubs/recipes/flask
    socketubs/recipes/helper

And learn the ``basic`` one for example.

::

    Sushi » sushi learn basic
    ==> Learn given recipe
    ==> Done

Deploy it !

:: 

    Tests » sushi craft MyApp --recipe=basic
    ==> Craft your project
      => Recipe: basic
    ==> Call helpers
    ==> Done

Configuration
-------------

Take a look at your configuration file: ``~/.sushi/sushi.conf``.

Create your own recipe
----------------------

Description
~~~~~~~~~~~

If you want to create your own recipe, you have to create a pull request on my cookbook or create your own cookbook on __Github__.  


Recipes are simple ``folder`` archives with a basic
structure but with ``Jinja2`` code inside your files.

How to
~~~~~~

This is a tree sample of my `advanced <https://github.com/socketubs/sushi-recipes/tree/master/advanced>`_ recipe:

::

    tree advanced
    advanced
    ├── .gitignore
    ├── README.md
    ├── __app__
    │   ├── __init__.py
    │   ├── cli.py
    │   ├── core.py
    │   └── logger.py
    ├── bin
    │   └── __app__
    └── setup.py

All files will be parsed by __Jinja2__ and all tags listed below will be replaced.


There is just one keyword to know for filename: ``__app__`` will be
replace by your formatted module name.


And for file rendering:

=====================  =============
Keyword                Value 
---------------------  -------------
{{ app }}              Your app name 
{{ license }}          Your favorite license (according to `OpenDefinition <http://licenses.opendefinition.org/licenses/groups/all.json>`_) 
{{ license_content }}  Url to favorite license 
{{ username }}         Operating system username
{{ firstname }}        Your firstname
{{ lastname }}         Your lastname
{{ year }}             Year
{{ day }}              Day
{{ month }}            Month
{{ hour }}             Hour
{{ minute }}           Minute
{{ second }}           Second
{{ date }}             Date (2012-09-01 16:55)
=====================  =============

And every values you can add to your configuration file under
``settings`` section.

Create your own helpers [REWRITE]
---------------------------------

Description
~~~~~~~~~~~

Helpers are Sushi extensions, they will be run **after** complete
rendering of your recipes.

How to
~~~~~~

You module name must be ``sushi_ext_name`` and it will be call like that
``sushi_ext_name.run(dst)``, wich ``dst`` is the path where recipe will
be renderer.

Your helper can use ``sushi.core`` api like that:

::

    >>> from sushi.core import conf
    >>> conf.get('settings', 'license')
    'agpl-v3'
    >>> conf.get('paths', 'sushi_recipes')
    '/Users/socketubs/.sushi/recipes'
    >>> from sushi.env import get_env
    >>> get_env('my_package')
    {'username': 'socketubs',
     'license_content': u'http://www.opensource.org/licenses/agpl-v3.html',
     'hour': 21, 'day': 2, 'minute': 0, 'month': 9, 'second': 4, 'year': 2012,
     'firstname': '## Set firstname',
     'lastname': '## Set lastname',
     'module': 'my_package',
     'date': '2012-09-02 21:00',
     'name': 'my_package',
     'license': 'agpl-v3',
     'email': '## Set email'}
            

And of course ``conf`` object is ``ConfigParser``, so you can ask your
helper users to set variables in their configuration file.

Example
~~~~~~~

You can find an example on Github.

-  `sushi-git <https://github.com/socketubs/sushi-git>`_

License
-------

License is `AGPL3`_. See `LICENSE`_.

.. _recipes: http://sushi.socketubs.net/recipes
.. _helpers: http://sushi.socketubs.net/helpers
.. _AGPL3: http://www.gnu.org/licenses/agpl.html
.. _LICENSE: https://raw.github.com/socketubs/sushi/master/LICENSE
