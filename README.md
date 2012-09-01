Sushi
=====

Description
-----------

Sushi is a modular Python bundler.  
Use [Jinja2][1] for file rendering.

Short preview
-------------

Install :

```pip install git+http://github.com/Socketubs/Sushi.git```

Download example template :

```wget https://github.com/Socketubs/Sushi/raw/master/templates/default.tar.gz
sushi add default.tar.gz
sushi list
 :: All packages
    - default (default)```

Create your package :

```sushi init my_package
 :: Unbundle your project
    - .gitignore
    - info.json
    - README.md
    - setup.py
    - __init__.py
    - cli.py
    - core.py
    - logger.py
    - __app__
 :: Run modules
    -> license
    -> git
Initialized empty Git repository in /Users/socketubs/Downloads/Tests/panda/my_package/.git/```

Configuration
-------------

Take a look at your configuration file: ```~/.sushi/sushi.conf```.

Create your own template
------------------------

This is a tree sample of template:
```default
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
└── setup.py```

There is just one keyword to know for filename:

And for file rendering:

<table>
  <tr>
    <th>Keywork</th><th>Value</th>
  </tr>
  <tr>
    <td>{{ name }}</td><td>Your app name</td>
  </tr>
  <tr>
    <td>{{ module }}</td><td>Your app name formated to be module</td>
  </tr>
  <tr>
    <td>{{ license }}</td><td>Your favorite license (according to <a href="http://licenses.opendefinition.org/licenses/groups/all.json">OpenDefinition</a></td>
  </tr>
  	<td>{{ license_content }}</td><td>Url to favorite license</td>
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

And every value you add to your configuration file under ``settings`` section.


[1]: http://jinja.pocoo.org