# Sphinx configuration file for Proto2Prod docs
import os
import sys
sys.path.insert(0, os.path.abspath('src'))

project = 'Proto2Prod Documentation'
extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'alabaster'
