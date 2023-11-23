===================
advent of code 2023
===================
.. image:: https://github.com/tyler-hoffman/aoc-2023/actions/workflows/poetry.yml/badge.svg

Python 3.12 edition

Notes on the repo
=================

* Package management is done with `Poetry <https://python-poetry.org/>`_
* Utils in the ``utils/`` directory can/should be used to bootstrap new directories/files for solutions
* Some parts of this repo are specific to the problems I receive (e.g. this won't entirely scale for non-me people)

  * utils in the ``utils/`` derectory require `advent-of-code-data <https://github.com/wimglenn/advent-of-code-data>`_, which relies on my session cookie. So don't use those unless you are me.
  * To make refactoring safer, after completing a problem, a test will be added asserting that my input produces the right output. If you aren't me, your input/output probably don't match.

* In terms of code structure, I treat the solution as a property of the problem and its inputs, modeled using dataclasses. Maybe kind of misusing them, but I kinda dig it.

Getting started
===============

#. Make sure you have `Poetry <https://python-poetry.org/>`_ installed
#. ``poetry install``
#. If you are using utils that use ``advent-of-code-data``, have my adventofcode session cookie stored in ``~/.config/aocd/token`` (note that this may be tricky if you are not me)

Commands to run
===============

+---------------------------------+-------------------------------------------------------------------------------------------------+
| Purpose                         | Command                                                                                         |
+=================================+=================================================================================================+
| Set up pre-commit hooks         | ``poetry run pre-commit install``                                                               |
+---------------------------------+-------------------------------------------------------------------------------------------------+
| Run all tests                   | ``poetry run pytest``                                                                           |
+---------------------------------+-------------------------------------------------------------------------------------------------+
| Run specific test file          | ``poetry run pytest <FILE>``                                                                    |
+---------------------------------+-------------------------------------------------------------------------------------------------+
| Format code                     | ``poetry run ruff format .``                                                                          |
+---------------------------------+-------------------------------------------------------------------------------------------------+
| Lint code                       | ``poetry run ruff check . --fix``                                                                         |
+---------------------------------+-------------------------------------------------------------------------------------------------+
| Typecheck                       | ``poetry run pyright .``                                                                        |
+---------------------------------+-------------------------------------------------------------------------------------------------+
| Run solution file               | ``poetry run python -m aoc_2023.day_<DAY>.<PART>``                                              |
+---------------------------------+-------------------------------------------------------------------------------------------------+
| Bootstrap files for new problem | ``poetry run python -m utils.create_files -d <DAY> -p <PART>``                                  |
+---------------------------------+-------------------------------------------------------------------------------------------------+
| Submit solution                 | ``poetry run python -m utils.submit -d <DAY> -p <PART>``                                        |
+---------------------------------+-------------------------------------------------------------------------------------------------+
Note: ``<DAY>`` above should use 2 digits, prepending a 0 for numbers below 10.

Handy Links
===========

* `AoC <https://adventofcode.com/2023>`_
* `Repo <https://github.com/tyler-hoffman/aoc-2023>`_

About those input.txt files...
==============================
I'm encrypting input files to respect `Eric's wishes <https://mobile.twitter.com/ericwastl/status/1465805354214830081>`_.
To do so, I'm using `git-crypt <https://github.com/AGWA/git-crypt>`_ with symmetric encryption. My key is stored locally, and for CI, I'm adding a base64 encoded string of the file as an environment variable. That gets decrypted and written to disk in CI so that it can run tests against my actual input. Like some other parts of this repo, this may make things hard if you are not me.