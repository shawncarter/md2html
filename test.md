# Markdown Feature Test

This document exercises all supported Markdown features and is designed to test page-break behaviour across different table sizes, headings, and content types.

---

## Table of Contents

[TOC]

---

## Typography

Normal paragraph text with **bold**, *italic*, ***bold italic***, and `inline code`. You can also use ~~strikethrough~~ if needed.

> This is a blockquote. It might contain an important note, a quote from a stakeholder, or a callout for the reader's attention.
>
> It can span multiple paragraphs.

This is text after the blockquote, followed by a horizontal rule.

---

## Lists

### Unordered

- Alpha team deliverables
- Beta team deliverables
  - Sub-item one
  - Sub-item two
    - Nested further
- Gamma team deliverables

### Ordered

1. Gather requirements
2. Draft technical spec
3. Review with stakeholders
   1. Schedule review meeting
   2. Incorporate feedback
4. Begin implementation
5. QA and sign-off

### Mixed

- Phase 1
    1. Discovery
    2. Planning
- Phase 2
    1. Development
    2. Testing

---

## Code Blocks

### Python

```python
def convert_markdown(content: str, css: str | None = None) -> str:
    import markdown
    html_body = markdown.markdown(
        content,
        extensions=["tables", "fenced_code", "toc", "attr_list"],
    )
    style = f"<style>{css}</style>" if css else ""
    return f"<!DOCTYPE html><html><head>{style}</head><body>{html_body}</body></html>"
```

### Bash

```bash
# Convert all markdown files in the current directory
python md2html.py "*.md" --css style.css

# Single file with custom output path
python md2html.py report.md --css style.css -o dist/report.html
```

### JSON

```json
{
  "project": "md2html",
  "version": "1.0.0",
  "extensions": ["tables", "fenced_code", "toc", "attr_list"],
  "themes": ["style.css", "style_dark.css"]
}
```

---

## Small Table

This table is small and will always fit on a single page alongside surrounding content.

| Setting   | Value        |
|-----------|--------------|
| Page size | A4           |
| Font      | system-ui    |
| Max width | 860px        |
| Themes    | Light / Dark |

---

## Medium Table — Sprint Status

This table is large enough to be noticeable but should fit on one page. It tests heading-to-table orphan rules — the heading above should never appear alone at the bottom of a page without at least the table header following it.

| Task ID | Description                          | Owner   | Priority | Status      | Due        |
|---------|--------------------------------------|---------|----------|-------------|------------|
| T-001   | Redesign auth flow                   | Alice   | High     | In Progress | 2026-05-20 |
| T-002   | Migrate legacy API endpoints         | Bob     | High     | Blocked     | 2026-05-18 |
| T-003   | Write unit tests for billing module  | Carol   | Medium   | Done        | 2026-05-15 |
| T-004   | Set up staging environment           | Dave    | High     | In Progress | 2026-05-22 |
| T-005   | Security audit — user data           | Eve     | Critical | Not Started | 2026-05-30 |
| T-006   | Update onboarding documentation      | Frank   | Low      | Done        | 2026-05-12 |
| T-007   | Performance profiling — dashboard    | Alice   | Medium   | In Progress | 2026-05-25 |
| T-008   | Fix pagination bug in reports view   | Bob     | High     | Done        | 2026-05-14 |
| T-009   | Integrate new payment gateway        | Carol   | Critical | Blocked     | 2026-05-28 |
| T-010   | Refactor notification service        | Dave    | Low      | Not Started | 2026-06-05 |
| T-011   | Load test checkout flow              | Eve     | High     | In Progress | 2026-05-27 |
| T-012   | Archive old audit logs               | Frank   | Low      | Done        | 2026-05-10 |

---

## Large Table — Multi-Page Test

This table has enough rows to span more than one page. It tests that:

- The table header row repeats correctly at the top of each page
- No single row is split across a page break
- The heading and introductory paragraph above are not stranded alone at the bottom of a page

| Server        | Region   | CPU % | Mem % | Disk % | Req/s  | Err/s | Status   |
|---------------|----------|-------|-------|--------|--------|-------|----------|
| web-01        | EU-West  | 34    | 61    | 42     | 1,240  | 0.1   | Healthy  |
| web-02        | EU-West  | 41    | 58    | 44     | 1,180  | 0.2   | Healthy  |
| web-03        | EU-West  | 29    | 55    | 41     | 980    | 0.0   | Healthy  |
| web-04        | US-East  | 72    | 80    | 60     | 2,100  | 1.4   | Warning  |
| web-05        | US-East  | 68    | 77    | 58     | 1,950  | 0.9   | Warning  |
| web-06        | US-East  | 55    | 70    | 52     | 1,620  | 0.3   | Healthy  |
| web-07        | AP-South | 22    | 45    | 38     | 640    | 0.0   | Healthy  |
| web-08        | AP-South | 19    | 42    | 36     | 590    | 0.0   | Healthy  |
| api-01        | EU-West  | 88    | 91    | 55     | 3,400  | 4.2   | Critical |
| api-02        | EU-West  | 45    | 66    | 48     | 1,700  | 0.4   | Healthy  |
| api-03        | US-East  | 51    | 69    | 51     | 1,850  | 0.6   | Healthy  |
| api-04        | US-East  | 60    | 74    | 54     | 2,050  | 1.1   | Warning  |
| api-05        | AP-South | 38    | 60    | 44     | 1,100  | 0.2   | Healthy  |
| db-primary    | EU-West  | 76    | 88    | 71     | 890    | 0.0   | Warning  |
| db-replica-01 | EU-West  | 32    | 72    | 68     | 420    | 0.0   | Healthy  |
| db-replica-02 | US-East  | 28    | 69    | 65     | 380    | 0.0   | Healthy  |
| db-replica-03 | AP-South | 24    | 65    | 62     | 310    | 0.0   | Healthy  |
| cache-01      | EU-West  | 14    | 92    | 12     | 8,400  | 0.0   | Healthy  |
| cache-02      | US-East  | 16    | 89    | 11     | 7,900  | 0.0   | Healthy  |
| cache-03      | AP-South | 11    | 84    | 10     | 5,200  | 0.0   | Healthy  |
| queue-01      | EU-West  | 42    | 55    | 38     | 620    | 0.1   | Healthy  |
| queue-02      | US-East  | 48    | 58    | 41     | 710    | 0.2   | Healthy  |
| worker-01     | EU-West  | 95    | 78    | 48     | 0      | 0.0   | Critical |
| worker-02     | EU-West  | 91    | 75    | 46     | 0      | 0.0   | Critical |
| worker-03     | US-East  | 44    | 60    | 43     | 0      | 0.0   | Healthy  |
| worker-04     | US-East  | 39    | 57    | 41     | 0      | 0.0   | Healthy  |
| worker-05     | AP-South | 28    | 51    | 37     | 0      | 0.0   | Healthy  |
| cdn-edge-01   | EU-West  | 18    | 30    | 22     | 12,400 | 0.0   | Healthy  |
| cdn-edge-02   | US-East  | 21    | 33    | 24     | 14,200 | 0.1   | Healthy  |
| cdn-edge-03   | AP-South | 15    | 28    | 20     | 9,800  | 0.0   | Healthy  |
| monitor-01    | EU-West  | 8     | 40    | 55     | 0      | 0.0   | Healthy  |
| bastion-01    | EU-West  | 2     | 18    | 14     | 0      | 0.0   | Healthy  |

---

## Callouts

Callouts use the `!!! type` syntax with 4-space indented content.

!!! note
    This is a **note** callout. Use it for general information the reader should be aware of.

!!! tip
    This is a **tip** callout. Use it for helpful suggestions or best practices.

!!! warning
    This is a **warning** callout. Use it when something could go wrong if the reader isn't careful.

!!! danger
    This is a **danger** callout. Use it for critical information — data loss, security risk, irreversible actions.

!!! important
    This is an **important** callout. Use it for key takeaways or decisions the reader must not miss.

---

## Observations

### Action Items

1. Page the on-call engineer for `worker-01` and `worker-02`
2. Review `api-01` connection pool settings
3. Schedule a capacity review for EU-West — three services are in warning or critical state
4. `web-04` and `web-05` have elevated error rates — check application logs

---

## Links

- [Python Markdown library](https://python-markdown.github.io/)
- [paged.js documentation](https://pagedjs.org/documentation/)
- [Catppuccin colour palette](https://catppuccin.com/)
- [Flask documentation](https://flask.palletsprojects.com/)
