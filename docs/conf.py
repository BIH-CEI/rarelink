import doctest
import os
import sys
import shutil
from docutils import nodes
from pathlib import Path
from docutils.parsers.rst import roles
try:
    import tomllib
except ImportError:
    import tomli as tomllib
    
src_path = os.path.abspath(os.path.join("..", "src"))
sys.path.insert(0, src_path)

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

src_path = os.path.abspath(os.path.join('..', 'src'))
sys.path.insert(0, src_path)

project = 'RareLink REDCap Documentation'
copyright = '2025, Berlin Institute of Health - Charité Universitätsmedizin Berlin'
author = 'Adam SL Graefe, Filip Rehburg, Samer Alkarkoukly, Alexander Bartschke\
            Daniel Danis, Ana Grönke, Miriam R Hübner, Steffen Sander, \
                Jana Zschüntzsch, Elisabeth F Nyoungui, Tatiana Kalashnikova, \
                    Beata Derfalvi, Nicola Wright, Susanna Wiegand, Peter Kühnen, \
                        Melissa A Haendel, Sylvia Thun, Peter N Robinson, Oya Beyan' 
          
root_dir = Path(__file__).resolve().parents[1]
pyproject_path = root_dir / "pyproject.toml"

with pyproject_path.open("rb") as f:
    pyproject = tomllib.load(f)

release = pyproject["project"]["version"]
version = ".".join(release.split(".")[:2])

docs_dir = Path(__file__).parent
static_dir = docs_dir / "_static"
static_dir.mkdir(exist_ok=True)

data_dict_version = release
data_dict_label = "v" + data_dict_version.replace(".", "_")

data_dict_src = (
    root_dir
    / "src"
    / "rarelink"
    / "rarelink_cdm"
    / f"rarelink_cdm_datadictionary - {data_dict_label}.csv"
)

data_dict_dst_name = f"rarelink_cdm_datadictionary - {data_dict_label}.csv"
data_dict_dst = static_dir / data_dict_dst_name

if data_dict_src.is_file():
    shutil.copy2(data_dict_src, data_dict_dst)
else:
    raise RuntimeError(
        f"Data dictionary not found for version {data_dict_version}: {data_dict_src}"
    )

# IMPORTANT: entire :download: role goes into ONE substitution
# Adjust ../../_static/ if this RST lives at a different depth
download_role = (
    f":download:`Download: RareLink-CDM Data Dictionary (v{data_dict_version}) "
    f"<../_static/{data_dict_dst_name}>`"
)

rst_prolog = f"""
.. |data_dict_download| replace:: {download_role}
"""


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

html_logo = "_static/res/rarelink_logo_w.png"

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

