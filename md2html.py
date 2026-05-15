import argparse
import sys
from pathlib import Path

import markdown


def convert(md_path: Path, css_content: str | None, output_path: Path) -> None:
    md_text = md_path.read_text(encoding="utf-8")
    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "toc", "attr_list", "admonition", "pymdownx.tilde"],
        extension_configs={"toc": {"toc_depth": 2}},
    )
    style_tag = f"<style>\n{css_content}\n</style>" if css_content else ""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{md_path.stem}</title>
{style_tag}
</head>
<body>
<div class="container">
{html_body}
</div>
</body>
</html>"""
    output_path.write_text(html, encoding="utf-8")
    print(f"  {md_path} -> {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Markdown files to self-contained HTML.")
    parser.add_argument("input", help="Markdown file or glob pattern (e.g. '*.md')")
    parser.add_argument("--css", help="CSS file to embed in output")
    parser.add_argument("-o", "--output", help="Output path (single file only, ignored for globs)")
    args = parser.parse_args()

    css_content = Path(args.css).read_text(encoding="utf-8") if args.css else None

    input_path = Path(args.input)
    if "*" in args.input or "?" in args.input:
        base = input_path.parent if input_path.parent != Path(".") else Path(".")
        files = list(base.glob(input_path.name))
        if not files:
            print(f"No files matched: {args.input}", file=sys.stderr)
            sys.exit(1)
        for f in sorted(files):
            convert(f, css_content, f.with_suffix(".html"))
    else:
        if not input_path.exists():
            print(f"File not found: {args.input}", file=sys.stderr)
            sys.exit(1)
        out = Path(args.output) if args.output else input_path.with_suffix(".html")
        convert(input_path, css_content, out)


if __name__ == "__main__":
    main()
