import doctest
import os
import sys

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.insert(0, src_path)

project = 'template_for_python_projects'
copyright = '2024, test'
author = 'test'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

# -- Autodoc setup ------------------------------------------------------------

autodoc_member_order = 'bysource'

# -- Doctest setup ------------------------------------------------------------

doctest_path = [src_path]
doctest_test_doctest_blocks = ""

# code to be executed before each doctest block
doctest_global_setup = """ 
import numpy as np
"""

doctest_default_flags = (doctest.REPORT_ONLY_FIRST_FAILURE
                         | doctest.ELLIPSIS
                         | doctest.IGNORE_EXCEPTION_DETAIL
                         | doctest.DONT_ACCEPT_TRUE_FOR_1)


# -- Intersphinx setup --------------------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    # TODO - change to stable when we arrive there
    "pandas": ("https://pandas.pydata.org/pandas-docs/version/2.0.0/", None),
    "requests": ("https://docs.python-requests.org/en/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy-1.11.0/", None),
    "statsmodels": ("https://www.statsmodels.org/stable/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # experiment with this
html_static_path = ['_static']
