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

Sushi support helper(extensions) and there are easy to create. See
`website`_. There are already some extension, like ``git``, ``license``.

Installation
~~~~~~~~~~~~

::

    pip install sushi

Meet the cookchef
~~~~~~~~~~~~~~~~~

First time you will run sushi, your cookchef will ask you if you want to
learn a **basic** recipe. You can learn how many recipes you want
in your cookbook.

::

    sushi cookbook
     :: I think it's your first time with sushi
     :: Can I suggest you simple basic recipe ?
    Confirm [y|N]: y
     :: Searching
     :: Teaching
     :: Done
     :: Recipes
        -> basic (default)

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

Cookchef guide about how to create your own `recipes`_.

Create your own helpers
-----------------------

Cookchef guide to about how to create your own `helpers`_.

License
-------

License is `AGPL3`_. See `LICENSE`_.

.. _website: http://sushi.socketubs.net/
.. _recipes: http://sushi.socketubs.net/recipes
.. _helpers: http://sushi.socketubs.net/helpers
.. _AGPL3: http://www.gnu.org/licenses/agpl.html
.. _LICENSE: https://raw.github.com/Socketubs/Sushi/master/LICENSE