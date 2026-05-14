# md2html — Claude Instructions

## What this project is

A Markdown-to-HTML converter with a Flask live preview app. The CLI (`md2html.py`) converts `.md` files to self-contained HTML with embedded CSS. The Flask app (`app.py`, port 5000) provides a live preview with theme switching, page/web view, and print support.

Always use the project venv: `venv/bin/python`.

## Converting a Markdown file to HTML

**Never output the converted HTML inline in the chat.** Use the CLI — it handles any file size instantly:

```bash
venv/bin/python md2html.py <file.md> --css style.css
# or with a custom output path:
venv/bin/python md2html.py <file.md> --css style.css -o <output.html>
# batch:
venv/bin/python md2html.py "*.md" --css style.css
```

If the user hasn't specified a CSS file, use `style.css` (light theme). Use `style_dark.css` only if explicitly requested.

## Enhancing a Markdown file before conversion

When the user asks you to convert a `.md` file, first read it and consider whether it would benefit from the enhancements below. Apply them if they clearly improve the document — don't add them for the sake of it.

### Callouts

Use these for anything that currently sits in a plain blockquote or is an important aside. Syntax requires 4-space indented content:

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

### Tables

Ensure any data presented as a list of items with consistent properties uses a pipe table instead:

```
| Column A | Column B | Column C |
|----------|----------|----------|
| Value    | Value    | Value    |
```

### Table of contents

Add `[TOC]` near the top of any document longer than roughly 3 sections. It auto-generates from headings.

### Heading hierarchy

Check that headings follow a logical hierarchy (H1 → H2 → H3). A document should have exactly one H1 (the title). Don't skip levels.

### Code blocks

Ensure all code samples use fenced blocks with a language hint:

````
```python
# code here
```
````

### Strikethrough

`~~text~~` renders as struck-through text.

## Workflow when asked to enhance a Markdown file

1. Read the file
2. Identify enhancements worth making (callouts, tables, TOC, heading fixes, code fences)
3. Edit the `.md` file in place with the improvements
4. Summarise what was changed — don't reproduce the file content in the chat

Do not ask for permission before making obvious improvements (adding a missing code fence language, promoting a blockquote to a callout). Do ask before restructuring headings or significantly rewriting content.

The user will run the CLI themselves, or ask separately for conversion. Do not run the CLI automatically after enhancing.

## Running the preview app

```bash
venv/bin/python app.py
# Open http://localhost:5000
```

The app auto-discovers any `*.css` files in the project directory — drop a new CSS file in and it appears in the Style dropdown immediately.
