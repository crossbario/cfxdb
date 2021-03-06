# -*- coding: utf-8 -*-

import sys
import os
import shlex
import time

try:
    import sphinx_rtd_theme
except ImportError:
    sphinx_rtd_theme = None

try:
    from sphinxcontrib import spelling
except ImportError:
    spelling = None

# monkey-patch txaio so that we can "use" both twisted *and* asyncio,
# at least at import time -- this is so the autodoc stuff can
# successfully import autobahn.twisted.* as well as autobahn.asyncio.*
# (usually, you can only import one or the other in a single Python
# interpreter)
import txaio

def use_tx():
  "monkey-patched for doc-building"
  from txaio import tx
  txaio._use_framework(tx)

def use_aio():
  "monkey-patched for doc-building"
  from txaio import aio
  txaio._use_framework(aio)

txaio.use_twisted = use_tx
txaio.use_asyncio = use_aio


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('./_extensions'))
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'cfxdb'
author = 'Crossbar.io Project'
language = 'en'

this_year = '{0}'.format(time.strftime('%Y'))
if this_year != '2018':
    copyright = '2018-{0}, Crossbar.io Technologies GmbH'.format(this_year)
else:
    copyright = '2018, Crossbar.io Technologies GmbH'

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
with open(os.path.join(base_dir, "cfxdb", "_version.py")) as f:
   exec(f.read())

version = release = __version__


# -- General configuration ---------------------------------------------------

# Check if we are building on readthedocs
RTD_BUILD = os.environ.get('READTHEDOCS', None) == 'True'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.images',
    'sphinx.ext.ifconfig',
    'sphinx.ext.todo',
    'sphinx.ext.doctest',
    'sphinxcontrib.spelling',
]

intersphinx_mapping = {
   'py3': ('https://docs.python.org/3', None),
   'python': ('https://docs.python.org/3', None),
   'rtd': ('https://docs.readthedocs.io/en/latest/', None),
   'txaio': ('https://txaio.readthedocs.io/en/latest/', None),
   'autobahn': ('https://autobahn.readthedocs.io/en/latest/', None),
   'zlmdb': ('https://zlmdb.readthedocs.io/en/latest/', None),
}

# extensions not available on RTD
if spelling is not None:
    extensions.append('sphinxcontrib.spelling')

spelling_lang = 'en_US'
spelling_show_suggestions = False
spelling_word_list_filename = 'spelling_wordlist.txt'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = '.rst'
master_doc = 'contents'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'contents'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
if sphinx_rtd_theme:
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
else:
    html_theme = "default"
pygments_style = 'sphinx'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, maps document names to template names.
# Show full, global TOC in sidebar
# http://stackoverflow.com/a/19007358
# http://sphinx-doc.org/config.html#confval-html_sidebars
html_sidebars = {
    '**': [
        'globaltoc.html',
        'relations.html',
        'sourcelink.html',
        'searchbox.html'
    ],
}
