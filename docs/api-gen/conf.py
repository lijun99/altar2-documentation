# Configuration file for AlTar2 API generator with autoapi

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('../products/debug-shared-linux-x86_64/packages/'))
# sys.path.insert(0, os.path.abspath('../../pyre/products/debug-shared-linux-x86_64/packages/'))

# -- Project information -----------------------------------------------------

project = 'AlTar2 API'
copyright = '2020, AlTar Developers'
author = 'AlTar Developers'

# The full version, including alpha/beta/rc tags
release = '2.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'autoapi.extension',
    'sphinx.ext.napoleon', # Numpy and Google style docstrings
]

# Add any python package paths for autoapi
autoapi_type = 'python'
autoapi_keep_files = True
autoapi_root = 'api'
autoapi_dirs = ['../../../altar/products/debug-shared-linux-x86_64/packages/']
autoapi_generate_api_docs = True

# needed for readthedocs
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
