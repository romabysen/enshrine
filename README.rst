Enshrine
++++++++

A simple file templating system built on `Jinja`_.
Because sometimes you just need to template some files.

Usage
=====

myvars.yaml:

.. code-block:: yaml

    ---
    var1: "test"
    var2: "other test"

mytemplate.ini.jinja:

.. code-block:: ini

    [something]
    some_thing: {{ var1 }}
    other_thing: {{ var2 }}

Output to stdout
----------------

.. code-block:: sh

    $ enshrine myvars.yaml mytemplate.ini.jinja

.. code-block:: ini

    [something]
    some_thing: test
    other_thing: other test

Output to a file
----------------

.. code-block:: sh

    $ enshrine -o myfile.ini myvars.yaml mytemplate.ini.json

Use some default variables
--------------------------

defaults.yaml:

.. code-block:: yaml

    ---
    var1: "default test"
    var2: "default other test"
    var3: "something else entirely"

mytemplate.ini.jinja:

.. code-block:: ini

    [something]
    some_thing: {{ var1 }}
    other_thing: {{ var2 }}
    else: {{ var3 }}

.. code-block:: sh

    $ enshrine defaults.yaml myvars.yaml mytemplate.ini.jinja

.. code-block:: ini

    [something]
    some_thing: test
    other_thing: other test
    else: something else entirely

Use some environment variables
------------------------------

envtemplate.ini.jinja:

.. code-block:: ini

    [something]
    some_thing: {{ var1 }}
    other_thing: {{ var2 }}
    env_thing: {{ env['MYVAR'] }}

.. code-block:: sh

    $ MYVAR="test value" enshrine myvars.yaml envmytemplate.ini.jinja

.. code-block:: ini

    [something]
    some_thing: test
    other_thing: other test
    env_thing: test value

Format JSON
-----------

myvars.yaml:

.. code-block:: yaml

    ---
    null_value: null
    a_list:
        - one
        - two
    an_object:
        "some": "thing"


json_template.json.jinja:

.. code-block::

    {
        "json_null": {{ null_value | to_json }},
        "json_list": {{ a_list | to_json }},
        "json_object": {{ an_object  | to_json }}
    }

.. code-block:: sh

    $ enshrine myvars.yaml json_template.json.jinja

.. code-block:: json

    {
        "json_null": null,
        "json_list": ["one", "two"],
        "json_object": {"some": "thing"}
    }

.. _Jinja: http://jinja.pocoo.org/
