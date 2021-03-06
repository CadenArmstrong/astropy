# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
#
# Astropy shared Sphinx settings.  These settings are shared between
# astropy itself and affiliated packages.
#
# Note that not all possible configuration values are present in this file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import warnings
from os import path
from distutils.version import LooseVersion
import re

from ..utils.compat import subprocess


# -- General configuration ----------------------------------------------------

# Some of the docs require the autodoc special-members option, in 1.1.
# If using graphviz 2.30 or later, Sphinx < 1.2b2 will not work with
# it.  Unfortunately, there are other problems with Sphinx 1.2b2, so
# we need to use "dev" until a release is made post 1.2b2.  If
# affiliated packages don't want this automatic determination, they
# may simply override needs_sphinx in their local conf.py.

def get_graphviz_version():
    try:
        output = subprocess.check_output(
            ['dot', '-V'], stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True)
    except subprocess.CalledProcessError:
        return '0'
    tokens = output.split()
    for token in tokens:
        if re.match(b'[0-9.]+', token):
            return token.decode('ascii')
    return '0'

graphviz_found = LooseVersion(get_graphviz_version())
graphviz_broken = LooseVersion('0.30')

if graphviz_found >= graphviz_broken:
    needs_sphinx = '1.2'
else:
    needs_sphinx = '1.1'

# Configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('http://docs.python.org/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
    'scipy': ('http://docs.scipy.org/doc/scipy/reference/', None),
    'matplotlib': ('http://matplotlib.sourceforge.net/', None),
    'astropy': ('http://docs.astropy.org/en/stable/', None),
    'h5py': ('http://docs.h5py.org/en/latest/', None)
    }

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# The reST default role (used for this markup: `text`) to use for all
# documents. Set to the "smart" one.
default_role = 'obj'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# This is added to the end of RST files - a good place to put substitutions to
# be used globally.
rst_epilog = """
.. _Astropy: http://astropy.org
"""


# -- Project information ------------------------------------------------------

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Settings for extensions and extension options ----------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.pngmath',
    'sphinx.ext.inheritance_diagram',
    'astropy.sphinx.ext.numpydoc',
    'astropy.sphinx.ext.astropyautosummary',
    'astropy.sphinx.ext.automodsumm',
    'astropy.sphinx.ext.automodapi',
    'astropy.sphinx.ext.tocdepthfix',
    'astropy.sphinx.ext.doctest',
    'astropy.sphinx.ext.changelog_links',
    'astropy.sphinx.ext.viewcode',  # Use patched version of viewcode
    'astropy.sphinx.ext.smart_resolver'
    ]

# Above, we use a patched version of viewcode rather than 'sphinx.ext.viewcode'
# This can be changed to the sphinx version once the following issue is fixed
# in sphinx:
# https://bitbucket.org/birkenfeld/sphinx/issue/623/
# extension-viewcode-fails-with-function

try:
    import matplotlib.sphinxext.plot_directive
    extensions += [matplotlib.sphinxext.plot_directive.__name__]
# AttributeError is checked here in case matplotlib is installed but
# Sphinx isn't.  Note that this module is imported by the config file
# generator, even if we're not building the docs.
except (ImportError, AttributeError):
    warnings.warn(
        "matplotlib's plot_directive could not be imported. " +
        "Inline plots will not be included in the output")

# Don't show summaries of the members in each class along with the
# class' docstring
numpydoc_show_class_members = False

autosummary_generate = True

automodapi_toctreedirnm = 'api'


# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [path.abspath(path.join(path.dirname(__file__), 'themes'))]

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'bootstrap-astropy'

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': ['localtoc.html'],
    'search': [],
    'genindex': [],
    'py-modindex': [],
}

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'astropy_logo.ico'  # included in the bootstrap-astropy theme

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%d %b %Y'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# -- Options for LaTeX output ------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = True

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Additional stuff for the LaTeX preamble.
latex_preamble = r"""
% Use a more modern-looking monospace font
\usepackage{inconsolata}

% The enumitem package provides unlimited nesting of lists and enums.
% Sphinx may use this in the future, in which case this can be removed.
% See https://bitbucket.org/birkenfeld/sphinx/issue/777/latex-output-too-deeply-nested
\usepackage{enumitem}
\setlistdepth{15}

% In the parameters section, place a newline after the Parameters
% header.  (This is stolen directly from Numpy's conf.py, since it
% affects Numpy-style docstrings).
\usepackage{expdlist}
\let\latexdescription=\description
\def\description{\latexdescription{}{} \breaklabel}

% Support the superscript Unicode numbers used by the "unicode" units
% formatter
\DeclareUnicodeCharacter{2070}{\ensuremath{^0}}
\DeclareUnicodeCharacter{00B9}{\ensuremath{^1}}
\DeclareUnicodeCharacter{00B2}{\ensuremath{^2}}
\DeclareUnicodeCharacter{00B3}{\ensuremath{^3}}
\DeclareUnicodeCharacter{2074}{\ensuremath{^4}}
\DeclareUnicodeCharacter{2075}{\ensuremath{^5}}
\DeclareUnicodeCharacter{2076}{\ensuremath{^6}}
\DeclareUnicodeCharacter{2077}{\ensuremath{^7}}
\DeclareUnicodeCharacter{2078}{\ensuremath{^8}}
\DeclareUnicodeCharacter{2079}{\ensuremath{^9}}
\DeclareUnicodeCharacter{207B}{\ensuremath{^-}}
\DeclareUnicodeCharacter{00B0}{\ensuremath{^{\circ}}}
\DeclareUnicodeCharacter{2032}{\ensuremath{^{\prime}}}
\DeclareUnicodeCharacter{2033}{\ensuremath{^{\prime\prime}}}

% Make the "warning" and "notes" sections use a sans-serif font to
% make them stand out more.
\renewenvironment{notice}[2]{
  \def\py@noticetype{#1}
  \csname py@noticestart@#1\endcsname
  \textsf{\textbf{#2}}
}{\csname py@noticeend@\py@noticetype\endcsname}
"""

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# -- Options for the linkcheck builder ----------------------------------------

# A timeout value, in seconds, for the linkcheck builder
linkcheck_timeout = 60
