##############
flake8-helper
##############

.. start short_desc

**A helper library for Flake8 plugins.**

.. end short_desc


.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs| |docs_check|
	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos| |coveralls|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Anaconda
	  - |conda-version| |conda-platform|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |docs| image:: https://img.shields.io/readthedocs/flake8-helper/latest?logo=read-the-docs
	:target: https://flake8-helper.readthedocs.io/en/latest
	:alt: Documentation Build Status

.. |docs_check| image:: https://github.com/domdfcoding/flake8-helper/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/flake8-helper/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |actions_linux| image:: https://github.com/domdfcoding/flake8-helper/workflows/Linux/badge.svg
	:target: https://github.com/domdfcoding/flake8-helper/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/domdfcoding/flake8-helper/workflows/Windows/badge.svg
	:target: https://github.com/domdfcoding/flake8-helper/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/domdfcoding/flake8-helper/workflows/macOS/badge.svg
	:target: https://github.com/domdfcoding/flake8-helper/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/domdfcoding/flake8-helper/workflows/Flake8/badge.svg
	:target: https://github.com/domdfcoding/flake8-helper/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/domdfcoding/flake8-helper/workflows/mypy/badge.svg
	:target: https://github.com/domdfcoding/flake8-helper/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://requires.io/github/domdfcoding/flake8-helper/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/flake8-helper/requirements/?branch=master
	:alt: Requirements Status

.. |coveralls| image:: https://img.shields.io/coveralls/github/domdfcoding/flake8-helper/master?logo=coveralls
	:target: https://coveralls.io/github/domdfcoding/flake8-helper?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/flake8-helper?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/flake8-helper
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/flake8-helper
	:target: https://pypi.org/project/flake8-helper/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/flake8-helper?logo=python&logoColor=white
	:target: https://pypi.org/project/flake8-helper/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/flake8-helper
	:target: https://pypi.org/project/flake8-helper/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/flake8-helper
	:target: https://pypi.org/project/flake8-helper/
	:alt: PyPI - Wheel

.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/flake8-helper?logo=anaconda
	:target: https://anaconda.org/domdfcoding/flake8-helper
	:alt: Conda - Package Version

.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/flake8-helper?label=conda%7Cplatform
	:target: https://anaconda.org/domdfcoding/flake8-helper
	:alt: Conda - Platform

.. |license| image:: https://img.shields.io/github/license/domdfcoding/flake8-helper
	:target: https://github.com/domdfcoding/flake8-helper/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/flake8-helper
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/flake8-helper/v0.1.1
	:target: https://github.com/domdfcoding/flake8-helper/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/flake8-helper
	:target: https://github.com/domdfcoding/flake8-helper/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2021
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/flake8-helper
	:target: https://pypi.org/project/flake8-helper/
	:alt: PyPI - Downloads

.. end shields

Installation
--------------

.. start installation

``flake8-helper`` can be installed from PyPI or Anaconda.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install flake8-helper

To install with ``conda``:

	* First add the required channels

	.. code-block:: bash

		$ conda config --add channels https://conda.anaconda.org/conda-forge
		$ conda config --add channels https://conda.anaconda.org/domdfcoding

	* Then install

	.. code-block:: bash

		$ conda install flake8-helper

.. end installation
