# -*- coding: utf-8 -*-

from __future__ import unicode_literals

try:
    import numpy_sugar
    version = numpy_sugar.__version__
except ImportError:
    version = 'unknown'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
]
napoleon_google_docstring = True
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'numpy-sugar'
copyright = '2016, Danilo Horta'
author = 'Danilo Horta'
release = version
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'default'
htmlhelp_basename = 'numpy_sugardoc'
latex_elements = {}
latex_documents = [
    (master_doc, 'numpy-sugar.tex', 'numpy-sugar Documentation',
     'Danilo Horta', 'manual'),
]
man_pages = [
    (master_doc, 'numpy-sugar', 'numpy-sugar Documentation',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'numpy-sugar', 'numpy-sugar Documentation',
     author, 'numpy-sugar', 'One line description of project.',
     'Miscellaneous'),
]
intersphinx_mapping = {
    'python': ('http://docs.python.org/', None),
    'numpy': ('http://docs.scipy.org/doc/numpy/', None),
    'scipy': ('http://docs.scipy.org/doc/scipy/reference/', None),
}
