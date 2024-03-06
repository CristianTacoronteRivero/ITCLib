# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import subprocess
sys.path.insert(0, os.path.abspath('../src'))

# Ejecutar el comando "ls -la" y capturar la salida
result = subprocess.run(['ls', '-la'], capture_output=True, text=True)

# Imprimir la salida estándar (stdout)
print(result.stdout)

project = 'ITCLib'
copyright = '2024, Cristian Tacoronte Rivero'
author = 'Cristian Tacoronte Rivero'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    # añade otras extensiones aquí
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
