# md2html

Convert Markdown files to styled, self-contained HTML — via CLI or a live Flask preview app.

## Features

- Converts `.md` files to standalone HTML with CSS embedded inline (no external dependencies in output)
- Batch conversion via glob patterns (`*.md`)
- Live preview app with instant rendering as you switch files or themes
- Two built-in CSS themes: light and dark (Catppuccin Mocha)
- Drop any `.css` file in the project directory and it appears in the theme dropdown automatically
- Web view (continuous scroll) and Page view (A4 paper simulation) toggle
- Print button that sends the rendered document directly to the browser print dialog
- Tables render with headers and zebra striping; never split across printed pages
- Markdown extensions: tables, fenced code blocks, table of contents, attribute lists

## Requirements

- Python 3.12+
- `markdown`
- `flask`

## Setup

```bash
git clone <repo-url>
cd md2html
python3 -m venv venv
source venv/bin/activate
pip install markdown flask
```

## CLI Usage

Convert a single file:

```bash
python md2html.py report.md
# Output: report.html
```

Embed a CSS theme:

```bash
python md2html.py report.md --css style.css
```

Specify output path:

```bash
python md2html.py report.md --css style.css -o dist/report.html
```

Batch convert all Markdown files in the current directory:

```bash
python md2html.py "*.md" --css style.css
```

Each converted file prints a confirmation line:

```
  report.md -> report.html
  notes.md -> notes.html
```

The output HTML is fully self-contained — CSS is embedded in a `<style>` tag, so files can be emailed or shared without any accompanying assets.

## Flask Preview App

Start the server:

```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

**Sidebar controls:**

| Control | Description |
|---------|-------------|
| Load File | Opens a file picker for `.md` files; renders instantly on selection |
| Style | Dropdown of all `*.css` files in the project directory |
| Web / Page | Toggle between view modes (see below) |
| Print | Opens the browser print dialog for the rendered document |

**Web view** — standard continuous scroll, respects the CSS `max-width` and body styles.

**Page view** — renders the document on a simulated A4 page (white on grey background, box shadow). Useful for checking how a document will look when printed before committing.

## CSS Themes

### `style.css` — Light

Clean sans-serif, centred at 860px max-width. Table headers use a dark navy background (`#003366`) with white text. Alternating row shading. Subtle horizontal rules and blockquote accents.

### `style_dark.css` — Dark (Catppuccin Mocha)

Dark background (`#1e1e2e`), soft text (`#cdd6f4`). Headings use purple (h1), blue (h2), and cyan (h3) from the Catppuccin Mocha palette. Table headers use a dark surface. Code blocks on near-black background.

### Adding your own theme

Drop any `.css` file into the project directory. It will appear in the Style dropdown the next time you load the app (no restart needed — the list is read on each page load). The CSS is embedded inline into the rendered HTML, so the output file is self-contained regardless of which theme you choose.

## Markdown Table Format

Tables use standard pipe syntax with an alignment row:

```
| Column A | Column B | Column C |
|----------|----------|----------|
| Value 1  | Value 2  | Value 3  |
| Value 4  | Value 5  | Value 6  |
```

The first row becomes the styled header. Alignment markers (`:---`, `:---:`, `---:`) are supported.

## Project Structure

```
md2html/
├── app.py              # Flask preview server
├── md2html.py          # CLI converter
├── style.css           # Light theme
├── style_dark.css      # Dark theme (Catppuccin Mocha)
├── templates/
│   └── index.html      # Flask UI template
└── venv/               # Python virtual environment
```

## License

MIT
