# md2html

Convert Markdown files to styled, self-contained HTML — via CLI or a live Flask preview app.

## Features

- Converts `.md` files to standalone HTML with CSS embedded inline (no external dependencies in output)
- Batch conversion via glob patterns (`*.md`)
- Live preview app with instant rendering as you switch files or themes
- Two built-in CSS themes: light and dark (Catppuccin Mocha)
- Drop any `.css` file in the project directory and it appears in the theme dropdown automatically
- Drag and drop `.md` files onto the preview panel
- Recent documents list (persists across sessions via localStorage, stores last used CSS per file)
- Web view (continuous scroll) and Page view (accurate A4 pagination via paged.js)
- Page margins: Small / Medium / Large
- Manual page break insertion — hover any heading in page view, click `↵ break` to force a break before it, click again to remove; Reset Breaks clears all at once
- Print button — both web and page view print via paged.js so output always matches page view
- TOC anchor links work within the preview iframe
- Scroll position preserved after re-renders
- Tables render with headers and zebra striping; header row repeats on each printed page
- Tables, callouts, and headings respect page break rules (no orphaned headings, no split callouts)
- Callouts: note, tip, warning, danger, important
- Strikethrough: `~~text~~`
- Dark terminal-style code blocks (light theme)
- Markdown extensions: tables, fenced code blocks, table of contents, attribute lists, admonitions, strikethrough

## Requirements

- Python 3.12+
- See `requirements.txt`

## Setup

```bash
git clone <repo-url>
cd md2html
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## CLI Usage

Convert a single file:

```bash
python md2html.py report.md
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

The output HTML is fully self-contained — CSS is embedded in a `<style>` tag, so files can be emailed or shared without any accompanying assets.

## Flask Preview App

Start the server:

```bash
python app.py
```

Then open `http://localhost:5000`.

**Sidebar controls:**

| Control | Description |
|---------|-------------|
| Load File | Opens a file picker for `.md` files; renders instantly on selection |
| Drag & drop | Drop any `.md` file onto the preview panel |
| Style | Dropdown of all `*.css` files in the project directory; remembered per document |
| Web / Page | Toggle between view modes |
| Page Margins | Small / Medium / Large — only visible in page view |
| Print | Prints via paged.js in both view modes so output always matches page view |
| Reset Breaks | Removes all manual page breaks from the document — page view only |
| Recent | Last 8 files; click to restore content and CSS |

**Web view** — continuous scroll with standard CSS. Hover headings to see page break controls (page view only).

**Page view** — content is reflowed into A4 page boxes by paged.js. What you see is exactly what prints.

### Inserting page breaks

Switch to page view. Hover over any heading — a small `↵ break` button appears inline. Click it to force a page break before that heading; it turns red and shows `✕ break` so you can toggle it back off. Click **Reset Breaks** to remove all forced breaks at once. Breaks are stored in the document and persist in the recent list.

## CSS Themes

### `style.css` — Light

Clean sans-serif, centred at 860px max-width. Navy table headers (`#003366`), zebra rows, terminal-style dark code blocks. Callout colours: blue (note), green (tip), amber (warning), red (danger), purple (important).

### `style_dark.css` — Dark (Catppuccin Mocha)

Dark background (`#1e1e2e`), soft text (`#cdd6f4`). Purple h1, blue h2, cyan h3. Automatically switched to light when entering page view (dark themes don't print well); restored when returning to web view.

### Adding your own theme

Drop any `.css` file into the project directory. It appears in the Style dropdown immediately — no restart needed.

## Callouts

Use `!!! type` syntax with 4-space indented content:

```
!!! note
    General information the reader should be aware of.

!!! tip
    Helpful suggestion or best practice.

!!! warning
    Something that could go wrong if the reader isn't careful.

!!! danger
    Critical: data loss, security risk, irreversible action.

!!! important
    Key decision or takeaway the reader must not miss.
```

## Markdown Table Format

```
| Column A | Column B | Column C |
|----------|----------|----------|
| Value    | Value    | Value    |
```

The first row becomes the styled header. The header row repeats at the top of each page when printing.

## Project Structure

```
md2html/
├── app.py              # Flask preview server
├── md2html.py          # CLI converter
├── requirements.txt    # Python dependencies
├── style.css           # Light theme
├── style_dark.css      # Dark theme (Catppuccin Mocha)
├── test.md             # Feature test document
├── templates/
│   └── index.html      # Flask UI template
└── venv/               # Python virtual environment
```

## License

MIT
