from flask import Flask, render_template, request, jsonify
import markdown
from pathlib import Path

app = Flask(__name__)
BASE_DIR = Path(__file__).parent


@app.route('/')
def index():
    css_files = sorted(p.name for p in BASE_DIR.glob('*.css'))
    return render_template('index.html', css_files=css_files)


@app.route('/render', methods=['POST'])
def render():
    data = request.get_json(silent=True) or {}
    content = data.get('content', '')
    css_filename = data.get('css', '')
    css_content = ''
    if css_filename:
        css_path = BASE_DIR / css_filename
        try:
            css_content = css_path.read_text(encoding='utf-8')
        except Exception:
            pass
    html = markdown.markdown(content, extensions=['tables', 'fenced_code', 'toc', 'attr_list', 'admonition', 'pymdownx.tilde'])
    return jsonify({'html': html, 'css': css_content})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
