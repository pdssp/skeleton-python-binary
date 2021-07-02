.. highlight:: shell

===============================
{{ cookiecutter.project_name }}
===============================

.. image:: https://img.shields.io/github/v/tag/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}
.. image:: https://img.shields.io/github/v/release/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}?include_prereleases
{% if cookiecutter.add_pyup_badge == 'y' %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}
{% endif %}
.. image https://img.shields.io/github/downloads/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}/total
.. image https://img.shields.io/github/issues-raw/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}
.. image https://img.shields.io/github/issues-pr-raw/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}
.. image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
   :target: https://github.com/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}/graphs/commit-activity
.. image https://img.shields.io/github/license/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}
.. image https://img.shields.io/github/forks/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}?style=social


{{ cookiecutter.project_short_description }}


Stable release
--------------

To install {{ cookiecutter.project_name }}, run this command in your terminal:

.. code-block:: console

    $ pip install {{ cookiecutter.project_slug }}

This is the preferred method to install {{ cookiecutter.project_name }}, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for {{ cookiecutter.project_name }} can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL https://github.com/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ make  # install in the system root
    $ make user # or Install for non-root usage


.. _Github repo: https://github.com/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}
.. _tarball: https://github.com/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}/tarball/master



Development
-----------

.. code-block:: console

        $ git clone https://github.com/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}
        $ cd {{ cookiecutter.project_slug }}
        $ make prepare-dev
        $ source .{{ cookiecutter.project_slug }}
        $ make install-dev


To get more information about the preconfigured tasks:

.. code-block:: console

        $ make help

Usage
-----

To use {{ cookiecutter.project_name }} in a project::

    import {{ cookiecutter.project_slug }}



Run tests
---------

.. code-block:: console

        $make tests



Author
------
👤 **{{ cookiecutter.full_name }}**



🤝 Contributing
---------------
Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}/issues). You can also take a look at the [contributing guide](https://github.com/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}/blob/master/CONTRIBUTING.rst)


📝 License
----------
This project is [{{ cookiecutter.open_source_license }}](https://github.com/pole-surfaces-planetaires/{{ cookiecutter.project_slug }}/blob/master/LICENSE) licensed.
