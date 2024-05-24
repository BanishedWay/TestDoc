# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "测试文档"
copyright = "2024, Albert"
author = "Albert"
release = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxcontrib.napoleon",
    "sphinxcontrib.apidoc",
    "sphinx.ext.viewcode",
    "m2r2",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "zh_CN"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ["_static"]

source_suffix = [".rst", ".md"]

import os
import sys

project_path = "../mymodule"
sys.path.insert(0, os.path.abspath(project_path))

apidoc_module_dir = project_path
apidoc_output_dir = "python_apis"
# apidoc_excluded_paths = ["tests"]
apidoc_separate_modules = True

master_doc = "index"
