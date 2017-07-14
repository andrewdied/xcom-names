========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/xcom-names/badge/?style=flat
    :target: https://readthedocs.org/projects/xcom-names
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/andrewdied/xcom-names.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/andrewdied/xcom-names

.. |codecov| image:: https://codecov.io/github/andrewdied/xcom-names/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/andrewdied/xcom-names

.. |version| image:: https://img.shields.io/pypi/v/XCOMnames.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/XCOMnames

.. |commits-since| image:: https://img.shields.io/github/commits-since/andrewdied/xcom-names/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/andrewdied/xcom-names/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/XCOMnames.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/XCOMnames

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/XCOMnames.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/XCOMnames

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/XCOMnames.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/XCOMnames


.. end-badges

A generator of XCOM mission names, like Operation WAILING PARAMOUR.

* Free software: MIT license

Installation
============

::

    pip install XCOMnames

Documentation
=============

https://xcom-names.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
