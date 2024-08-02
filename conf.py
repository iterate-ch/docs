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
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Cyberduck Help'
copyright = '2022 iterate GmbH'
author = 'iterate GmbH'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	"sphinx_rtd_theme",
	"sphinx_tabs.tabs",
	"myst_parser",
	"sphinx_rtd_dark_mode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
	'style_nav_header_background': '#5a5a5a',
	'style_external_links': True,
	'vcs_pageview_mode': 'edit',

	# Toc options
    'includehidden': True,
    'titles_only': False,
}
html_favicon = '_static/favicon.ico'
html_logo = 'cyberduck-icon-64.png'
html_context = {
	"display_github": True, # Add 'Edit on Github' link instead of 'View page source'
	"github_user": "iterate-ch",
	"github_repo": "docs",
	"github_version": "main",
	"conf_py_path": "/"
}
html_show_sourcelink = False
html_show_sphinx = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

master_doc = 'index'
myst_heading_anchors = 4
myst_enable_extensions = [
	"html_image",
	"colon_fence"
]

default_dark_mode = False
