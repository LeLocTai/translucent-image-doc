#!/usr/bin/env python3
# -*- coding: utf-8 -*-

extensions = []

templates_path = ['_templates']
source_suffix = '.rst'
# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Translucent Image'
copyright = '2017, Le Tai'
author = 'Le Tai'

version = '2.0'
release = '2.0'

language = 'en'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

html_static_path = ['_static']