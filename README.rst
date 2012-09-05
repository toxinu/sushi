Sushi
=====

Presentation
------------

Sushi is a special Python package cookchef. But it’s goal is not to give
you the perfect recipe cause it don’t know it but it’s to create your
own favorite set of recipes.

Sushi support helper(extensions) and there are easy to create. See
`website`_. There are already some extension, like ``git``, ``license``.

Installation
~~~~~~~~~~~~

::

    pip install sushi

Meet the cookchef
~~~~~~~~~~~~~~~~~

First time you will run sushi, your cookchef will ask you if you want to
learn a basic **maki** recipe. You can learn how many recipes you want
in your cookbook.

::

    sushi cookbook
     :: I think it's your first time with sushi
     :: Can I suggest you simple maki recipe ?
    Confirm [y|N]: y
     :: Searching
     :: Teaching
     :: Done
     :: Recipes
        -> maki (default)

First sushi
~~~~~~~~~~~

::

    sushi craft my_sushi
     :: Craft your project
        -> Recipe: maki
     :: Call helpers
        -> license
     :: Done

Configuration
-------------

Take a look at your configuration file: ``~/.sushi/sushi.conf``.

Create your own recipe
----------------------

Cookchef guide about how to create your own `here`_.

Create your own helpers
-----------------------

Cookchef guide to about how to create your own `here`_.

Todo
----

-  Maybe create webservice for template hosting ?

License
-------

License is `AGPL3`_. See `LICENSE`_.

.. _website: http://sushi.socketubs.net/
.. _here: http://sushi.socketubs.net/recipes
.. _here: http://sushi.socketubs.net/helpers
.. _AGPL3: http://www.gnu.org/licenses/agpl.html
.. _LICENSE: https://raw.github.com/Socketubs/Sushi/master/LICENSE