import os
import sys

sys.path.insert(0, os.path.abspath('../'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints'
]

html_theme = 'furo'

# -- Project information -----------------------------------------------------

project = 'QA Engineer Case'
author = 'Ibrahim Emre Yaz'

release = '1.0.0'

# note to self:
# command to use create doc: sphinx-build -M html . build
