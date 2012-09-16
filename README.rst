Sushi
=====

Presentation
------------

Sushi is Python package builder. Enough to create same package structure everytime. Create custom recipes for Flask, Django, etc...

- Deploy the same everytime
- Make specific recipe for Flask, Django, ...
- Use helpers to not waste time
- Auto ``virtualenv`` for best dev
- Auto ``git init`` your package
- And more !

Sushi support helper(extensions) and there are easy to create. There are already some extension, like ``git``, ``license``.

Installation
~~~~~~~~~~~~

::

    pip install sushi

Meet the cookchef
~~~~~~~~~~~~~~~~~

If it's the first time your run Sushi, your cookbook is certainly empty. You
can easily learn a basic recipe like that:

::

    sushi learn http+https://github.com/Socketubs/Sushi/raw/master/recipes/basic.tar.gz
     :: Learn given recipe
        -> Download file
        -> Clean
    :: Done

First sushi
~~~~~~~~~~~

::

    sushi craft My-Package 
     :: Craft your project
        -> Recipe: advanced
     :: Call helpers
        -> license
        -> git
    Initialized empty Git repository in /Users/socketubs/My-Package/.git/
        -> virtualenv
     :: Done

Configuration
-------------

Take a look at your configuration file: ``~/.sushi/sushi.conf``.

Create your own recipe
----------------------

Description
===========

Recipes are simple ``.tar.gz`` archives with a basic python package
structure but with ``Jinja2`` code inside your files.

How to
======

This is a tree sample of my **`advanced <https://github.com/Socketubs/Sushi/tree/master/recipes/advanced>`_** recipe:

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

Take a quicklook of this **`recipes <https://github.com/Socketubs/Sushi/tree/master/recipes/advanced>`_** files.

There is just one keyword to know for filename: ``__app__`` will be
replace by your formatted module name.

And for file rendering:

.. raw:: html

   <table class="table table-bordered">

.. raw:: html

   <thead>

.. raw:: html

   <tr>

.. raw:: html

   <th>

Keyword

.. raw:: html

   </th>

.. raw:: html

   <th>

Value

.. raw:: html

   </th>

.. raw:: html

   </tr>

.. raw:: html

   </thead>

.. raw:: html

   <tbody>

.. raw:: html

   <tr>

.. raw:: html

   <td>

{% raw %}{{ name }}{% endraw %}

.. raw:: html

   </td>

.. raw:: html

   <td>

Your app name

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

{% raw %}{{ module }}{% endraw %}

.. raw:: html

   </td>

.. raw:: html

   <td>

Your app name formated to be a valid module

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

{% raw %}{{ license }}{% endraw %}

.. raw:: html

   </td>

.. raw:: html

   <td>

Your favorite license (according to `OpenDefinition <http://licenses.opendefinition.org/licenses/groups/all.json>`_)

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <td>

{% raw %}{{ license\_content }}{% endraw %}

.. raw:: html

   </td>

.. raw:: html

   <td>

Url to your favorite license

.. raw:: html

   </td>

.. raw:: html

   <tr>

.. raw:: html

   <td>

{% raw %}{{ username }}{% endraw %}

.. raw:: html

   </td>

.. raw:: html

   <td>

Operating system username

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

{% raw %}{{ firstname }}{% endraw %}

.. raw:: html

   </td>

.. raw:: html

   <td>

Your firstname

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

{% raw %}{{ lastname }}{% endraw %}

.. raw:: html

   </td>

.. raw:: html

   <td>

Your lastname

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

{% raw %}{{ year }}{% endraw %}

.. raw:: html

   </td>

.. raw:: html

   <td>

Now year

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

{% raw %}{{ day }}{% endraw %}

.. raw:: html

   </td>

.. raw:: html

   <td>

Now day

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

{% raw %}{{ month }}{% endraw %}

.. raw:: html

   </td>

.. raw:: html

   <td>

Now month

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

{% raw %}{{ hour }}{% endraw %}

.. raw:: html

   </td>

.. raw:: html

   <td>

Now hour

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

{% raw %}{{ minute }}{% endraw %}

.. raw:: html

   </td>

.. raw:: html

   <td>

Now minute

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

{% raw %}{{ second }}{% endraw %}

.. raw:: html

   </td>

.. raw:: html

   <td>

Now second

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

{% raw %}{{ date }}{% endraw %}

.. raw:: html

   </td>

.. raw:: html

   <td>

Now date (2012-09-01 16:55)

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </tbody>

.. raw:: html

   </table>

.. raw:: html

   </p>

And every values you can add to your configuration file under
``settings`` section.
 By the way, Sushi use **`Jinja2 <http://jinja.pocoo.org>`_** for rendering.

Create your own helpers
-----------------------

Description
===========

Helpers are Sushi extensions, they will be run **after** complete
rendering of your recipes.

How to
======

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

Examples
========

There is one sushi recipe for helper that you can found `here <https://github.com/Socketubs/Sushi/raw/master/recipes/helper.tar.gz>`_.

You can find two examples on Github.

-  `Sushi-git <https://github.com/Socketubs/Sushi-git>`_
-  `Sushi-license <https://github.com/Socketubs/Sushi-license>`_

License
-------

License is `AGPL3`_. See `LICENSE`_.

.. _recipes: http://sushi.socketubs.net/recipes
.. _helpers: http://sushi.socketubs.net/helpers
.. _AGPL3: http://www.gnu.org/licenses/agpl.html
.. _LICENSE: https://raw.github.com/Socketubs/Sushi/master/LICENSE