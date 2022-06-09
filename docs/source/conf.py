# Configuration file for the Sphinx documentation builder.


import os
import sys

import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath(".."))
sys.path.append(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "readthedocs.settings.dev")

# Load Django after sys.path and configuration setup
# isort: split
import django

django.setup()

sys.path.append(os.path.abspath("_ext"))

# -- Project information

project = 'Fittrix'
copyright = '2022, fittrix'
author = 'minarae'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.httpdomain',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_context = {
   "display_github": False, # Add 'Edit on Github' link instead of 'View page source'
   "last_updated": True,
   "commit": False,
}