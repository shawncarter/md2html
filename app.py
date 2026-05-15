from flask import Flask, render_template, request, jsonify
import markdown
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).parent

MD_EXTENSIONS = ['tables', 'fenced_code', 'toc', 'attr_list', 'admonition', 'pymdownx.tilde']
MD_EXT_CONFIGS = {'toc': {'toc_depth': 2}}


def load_css(filename):
    if not filename:
        return ''
    try:
        return (BASE_DIR / filename).read_text(encoding='utf-8')
    except Exception:
        return ''


@app.route('/')
def index():
    css_files = sorted(p.name for p in BASE_DIR.glob('*.css'))
    return render_template('index.html', css_files=css_files)


@app.route('/render', methods=['POST'])
def render():
    data = request.get_json(silent=True) or {}
    html = markdown.markdown(data.get('content', ''), extensions=MD_EXTENSIONS, extension_configs=MD_EXT_CONFIGS)
    return jsonify({'html': html, 'css': load_css(data.get('css', ''))})


@app.route('/save', methods=['POST'])
def save():
    data = request.get_json(silent=True) or {}
    content = data.get('content', '')
    css_content = load_css(data.get('css', ''))
    stem = Path(data.get('filename', 'output.md')).stem
    html_body = markdown.markdown(content, extensions=MD_EXTENSIONS, extension_configs=MD_EXT_CONFIGS)
    style_tag = f"<style>\n{css_content}\n</style>" if css_content else ""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{stem}</title>
{style_tag}
</head>
<body>
<div class="container">
{html_body}
</div>
</body>
</html>"""
    out = BASE_DIR / f"{stem}.html"
    out.write_text(html, encoding='utf-8')
    return jsonify({'saved': out.name})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
