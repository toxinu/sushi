# Sushi

## Presentation

Sushi is a special Python package cookchef. But it's goal is not to give you the perfect recipe cause it don't know it but it's to create your own favorite set of recipes. 

Sushi support helper(extensions) and there are easy to create. See [wiki][1]. There are already some extension, like ``git``, ``license``.

### Installation

```bash
pip install sushi
```

### Meet the cookchef

First time you will run sushi, your cookchef will ask you if you want to learn a basic __maki__ recipe.
You can learn how many recipes you want in your cookbook.

```
sushi cookbook
 :: I think it's your first time with sushi
 :: Can I suggest you simple maki recipe ?
Confirm [y|N]: y
 :: Searching
 :: Teaching
 :: Done
 :: Recipes
    -> maki (default)
```

### First sushi

```bash
 :: Craft your project
    -> Recipe: maki
 :: Call helpers
    -> license
 :: Done
```

## Configuration

Take a look at your configuration file: ```~/.sushi/sushi.conf```.

## Create your own recipe

Cookchef guide about how to create your own [here][4].

## Create your own helpers

Cookchef guide to about how to create your own [here][5].

Todo
----

* Maybe create webservice for template hosting ?

License
-------

License is [AGPL3][2]. See [LICENSE][3].

[1]: https://github.com/Socketubs/Sushi/wiki
[2]: https://github.com/Socketubs/Sushi/wiki/Recipes
[3]: https://github.com/Socketubs/Sushi/wiki/Helpers
[4]: http://www.gnu.org/licenses/agpl.html
[5]: https://raw.github.com/Socketubs/Sushi/master/LICENSE
