import doctest
import os
import sys
from docutils import nodes
from docutils.parsers.rst import roles

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.insert(0, src_path)

project = 'RareLink REDCap Documentation'
copyright = '2024, Berlin Institute of Health - Charité Universitätsmedizin Berlin'
author = 'Adam SL Graefe, Filip Rehburg, Samer Alkarkoukly, Alexander Bartschke\
            Daniel Danis, Ana Grönke, Miriam R Hübner, Steffen Sander, \
                Jana Zschüntzsch, Elisabeth F Nyoungui, Tatiana Kalashnikova, \
                    Beata Derfalvi, Nicola Wright, Susanna Wiegand, Peter Kühnen, \
                        Melissa A Haendel, Sylvia Thun, Peter N Robinson, Oya Beyan' 
          
release = '2.0.4'

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

html_css_files = [
    'custom.css',
]
html_js_files = ['custom.js']

templates_path = ['_templates']
exclude_patterns = ['_build', 
                    'Thumbs.db', 
                    '.DS_Store',
                    "3_0_install_file.rst",
                    "4_0_guide_file.rst",
                    "2_0_framework_file.rst",
                    "1_0_background_file.rst",  
]
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
    "pandas": ("https://pandas.pydata.org/pandas-docs/version/2.0.2/", None),
    "requests": ("https://docs.python-requests.org/en/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy-1.11.0/", None),
    "statsmodels": ("https://www.statsmodels.org/stable/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # experiment with this
html_static_path = ['_static']

html_logo = "_static/res/rarelink_logo_no_background.png"

html_theme_options = {
    # Collapse all navigation entries by default
    "collapse_navigation": False,
    # Disable sticky navigation (sidebar won't follow as you scroll)
    "sticky_navigation": False,
    # Limit the depth of the sidebar tree
    "navigation_depth": 2,
    # Show only the titles (no sub-headings in the sidebar)
    "titles_only": False,
    # show logo and version
    "logo_only": True,       
    "display_version": True,
}


def custom_literal_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    """Custom role for styled literals."""
    node = nodes.literal(text, text)
    node['classes'].append('literal-custom')
    return [node], []

roles.register_local_role('literal_custom', custom_literal_role)

