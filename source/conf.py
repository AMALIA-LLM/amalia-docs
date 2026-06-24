# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AMALIA'
copyright = ''
author = ''
#release = '2026'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_copybutton"]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_title = 'Documentação AMALIA'
html_theme_options = {
   "logo": {
      "image_light": "_static/logo/logo-color-black.png",
      "image_dark": "_static/logo/logo-color-white.png",
   },
   "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/AMALIA-LLM",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        },
        {
            "name": "HuggingFace",
            "url": "https://huggingface.co/amalia-llm",
            "icon": "fa-brands fa-hugging-face",
            "type": "fontawesome"
        }
    ],
    "use_download_button": False,
    "extra_footer": "<div>AMALIA: Assistente Multimodal Automático de Linguagem com IA<br>Todos os materiais estão disponíveis de acordo com a licença Apache 2.0</div>",
}
html_favicon = '_static/favicon.png'
html_js_files = [
    (
        "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@7.2.0/js/brands.min.js",
        {"defer": "defer"},
    ),
]
