import doctest
import os
import sys

# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.insert(0, src_path)


project = 'Ontology-Based Rare Disease Common Data Model (RD CDM)'
copyright = 'Berlin Institute of Health, Charité Universitätsmedizin Berlin'
author = 'Adam SL Graefe'
release = '2.0.0'

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
html_css_files = [
    'custom.css',  # Include your custom CSS
]
