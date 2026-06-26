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

extensions = ["sphinx_copybutton","sphinx.ext.githubpages"]

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
    "show_toc_level": 2,
    "extra_footer": "<div>AMALIA: Assistente Multimodal Automático de Linguagem com IA<br>Todos os materiais estão disponíveis de acordo com a licença Apache 2.0</div>",
}
html_favicon = '_static/favicon.png'
html_js_files = [
    (
        "https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@7.2.0/js/brands.min.js",
        {"defer": "defer"},
    ),
]

from docutils import nodes
import json
import os


def collect_global_sections(app, doctree, docname):
    if not hasattr(app, 'global_sections'):
        app.global_sections = {}

    headings = []
    # Recursively find all section blocks
    for node in doctree.findall(nodes.section):
        title_node = node.next_node(nodes.title)
        if title_node:
            # Correctly walk up the tree using the singular .parent attribute
            depth = 0
            current = node
            while current.parent is not None:
                if isinstance(current.parent, nodes.section):
                    depth += 1
                current = current.parent

            headings.append({
                'title': title_node.astext(),
                'id': node.get('ids')[0] if node.get('ids') else '',
                'level': depth  # Top-level H1 will be 0, H2 will be 1, H3 will be 2
            })

    # Pop off the H1 main page title
    if headings:
        headings.pop(0)

    app.global_sections[docname] = headings


def write_global_sections_json(app, exception):
    if exception is None:
        json_path = os.path.join(app.outdir, "_static", "global_sections.json")
        os.makedirs(os.path.dirname(json_path), exist_ok=True)
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(app.global_sections, f)


def setup(app):
    app.connect("doctree-resolved", collect_global_sections)
    app.connect("build-finished", write_global_sections_json)