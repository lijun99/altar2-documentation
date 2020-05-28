# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('../products/debug-shared-linux-x86_64/packages/'))
# sys.path.insert(0, os.path.abspath('../../pyre/products/debug-shared-linux-x86_64/packages/'))

# -- Project information -----------------------------------------------------

project = 'AlTar'
copyright = '2013-2020 ParaSim Inc., 2010-2020 California Institute of Technology.'
author = 'AlTar Development Team'

# The full version, including alpha/beta/rc tags
release = '2.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc', # import the modules
    'sphinx.ext.autosectionlabel', # auto label sections
    'sphinx.ext.extlinks', # for shared external links
    'nbsphinx', # include jupyter notebooks
    'recommonmark',
    #'m2r', # include markdown
    'sphinx.ext.mathjax', # render math via JavaScript, another option is sphinx.ext.imgmath
]

# needed for readthedocs
master_doc = 'index'


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build',
                    'Thumbs.db', '.DS_Store',
                    'api-gen', # ignore api reference generators
                    '**.ipynb_checkpoints', # jupyter notebook progress
                    ]

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

# for markdown
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

mathjax_config = {
    'TeX': {'equationNumbers': {'autoNumber': 'AMS', 'useLabelIds': True}},
}

# -- Common used hyperlinks ---------------------------------------------------
# altar_ will be converted to <a href="https://github.com/AlTarFramework/altar">altar</a>
rst_epilog = """
.. _altar: https://github.com/AlTarFramework/altar
.. _AlTar: https://github.com/AlTarFramework/altar
.. _altar cuda branch: https://github.com/lijun99/altar
.. _AlTar Documentation: https://altar.readthedocs.io
.. _pyre: https://github.com/pyre/pyre
.. _pyre cuda branch: https://github.com/lijun99/pyre
.. _pyre Documentation: https://pyre-doc.readthedocs.io
.. _mm: https://github.com/aivazis/mm
.. _config.mm: https://github.com/lijun99/altar2-documentation/tree/cuda/config.mm
"""

# --- external links --------------
# 'altar': ('link', prefix)
extlinks = {
    'altar_src': ('https://github.com/lijun99/altar/tree/cuda/%s', None),
    'pyre_src': ('https://github.com/lijun99/pyre/tree/cuda/%s', None),
    'altar_doc_src': ('https://github.com/lijun99/altar2-documentation/tree/cuda/%s', None),
    'tutorials': ('https://github.com/lijun99/altar2-documentation/tree/cuda/jupyter/%s', 'Tutorials:')
}

# --- latex pdf ---------
latex_engine = 'xelatex'
latex_elements = {
}
#latex_show_urls = 'footnote'
