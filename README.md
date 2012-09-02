# Sushi

## Presentation

Sushi is a modular Python bundler. But it's goal is not to give you the perfect template cause I don't know it but it's to create your own. 

Sushi add an easy to add module like auto ``git init`` (already in sushi) and more.

### Installation

```bash
pip install sushi
```

### Default template

First time you will run sushi, a starter will ask you if you want to download default template.
You can have many template has you want.

```
sushi list
 :: I think it's your first time with sushi
 :: Can I import default template for you ?
Confirm [y|N]: y
 :: Downloading
 :: Extracting
 :: Done
 :: All templates
    - default (default)
```

### First package

```bash
sushi init my_package
 :: Unbundle your project
 :: Run modules
    -> license
```

## Configuration

Take a look at your configuration file: ```~/.sushi/sushi.conf```.

## Create your own template

This is a tree sample of my advanced template:

```bash
default
├── .DS_Store
├── .gitignore
├── README.md
├── __app__
│   ├── .DS_Store
│   ├── __init__.py
│   ├── cli.py
│   ├── core.py
│   └── logger.py
├── bin
│   └── __app__
└── setup.py
```

You can find it [here][4].

There is just one keyword to know for filename: ``__app__`` will be replace by your formatted module name.

And for file rendering:

<table>
  <tr>
    <th>Keyword</th><th>Value</th>
  </tr>
  <tr>
    <td>{{ name }}</td><td>Your app name</td>
  </tr>
  <tr>
    <td>{{ module }}</td><td>Your app name formated to be a valid module</td>
  </tr>
  <tr>
    <td>{{ license }}</td><td>Your favorite license (according to <a href="http://licenses.opendefinition.org/licenses/groups/all.json">OpenDefinition</a>)</td>
  </tr>
  	<td>{{ license_content }}</td><td>Url to your favorite license</td>
  <tr>
    <td>{{ username }}</td><td>Operating system username</td><
  </tr>
  <tr>
    <td>{{ firstname }}</td><td>Your firstname</td><
  </tr>
  <tr>
    <td>{{ lastname }}</td><td>Your lastname</td><
  </tr>
  <tr>
    <td>{{ year }}</td><td>Now year</td><
  </tr>
  <tr>
    <td>{{ day }}</td><td>Now day</td><
  </tr>
  <tr>
    <td>{{ month }}</td><td>Now month</td><
  </tr>
  <tr>
    <td>{{ hour }}</td><td>Now hour</td><
  </tr>
  <tr>
    <td>{{ minute }}</td><td>Now minute</td><
  </tr>
  <tr>
    <td>{{ second }}</td><td>Now second</td><
  </tr>
  <tr>
    <td>{{ date }}</td><td>Now date (2012-09-01 16:55)</td><
  </tr>
</table>

And every values you can add to your configuration file under ``settings`` section.

Todo
----

* Better extension system
* Maybe create webservice for template hosting ?

License
-------

License is [AGPL3][2]. See [LICENSE][3].

[1]: http://jinja.pocoo.org
[2]: http://www.gnu.org/licenses/agpl.html
[3]: https://raw.github.com/Socketubs/Sushi/master/LICENSE
[4]: https://github.com/Socketubs/Sushi/raw/master/templates/advanced.tar.gz