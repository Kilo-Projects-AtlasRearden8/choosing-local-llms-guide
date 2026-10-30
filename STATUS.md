# STATUS

## What was built

A beginner manual for choosing and running local LLMs with Ollama, delivered in two editions:

- **`docs/`** — Markdown manual (9 sections): welcome, what is Ollama, model sizes, hardware needs, installing Ollama, running your first model, privacy, model-selection worksheet, FAQ.
- **`static/`** — Self-contained HTML website (10 pages + CSS + JS) mirroring the docs, with a printable one-page model-selection worksheet and a print button.
- **`LICENSE`** — MIT License, copyright line exactly: `Copyright (c) 2026 Asdale Dynamics, LLC`.
- **`README.md`** — Project overview crediting Asdale Dynamics, LLC.
- **`scripts/verify.py`** — Verification script checking files, links, credits, license, no secrets, no `.github/workflows`.
- **`STATUS.md`** — This file.

Files (23 total): LICENSE, README.md, STATUS.md, scripts/verify.py, 9 docs/ markdown files, 10 static/ HTML files, static/css/style.css, static/js/app.js.

## Who it's for

Dylan Asdale, registered nurse turned AI author and founder of Asdale Dynamics, LLC (Indiana, formed October 2026). Beginner-friendly AI education in plain English, step by step, never condescending.

## How to run it

- **Markdown edition:** Open any file in `docs/` with a Markdown reader or text editor.
- **HTML edition:** Open `static/index.html` in any web browser. All pages work offline.
- **Print the worksheet:** Open `static/worksheet.html` and click "Print this worksheet" (or Ctrl+P / Cmd+P). Designed to print cleanly on one sheet.
- **Verify:** `python3 scripts/verify.py`

## Verification results

Ran `python3 scripts/verify.py` — all checks passed, 0 errors, 0 warnings:

- LICENSE present with exact MIT copyright line
- README.md and all docs/static pages credit Asdale Dynamics, LLC
- All 10 HTML pages have `<title>`, link CSS and JS, credits present
- All internal links resolve; no broken links
- Worksheet has print styles and a print button
- No secrets, API keys, or private keys in any file
- No `.github/workflows` directory

## Known gaps

- Ollama itself is not installed in this repo (it's a guide, not software to run here); the verification checks the guide files, not Ollama operation.
- No automated HTML render test beyond link resolution; open `static/index.html` in a browser to visually confirm.
- No `.github` folder at all (workflows deliberately absent per instructions).
- No git remote configured (intended: never push, never create remote repos).

## Credit

Published by Asdale Dynamics, LLC. MIT License. Copyright (c) 2026 Asdale Dynamics, LLC.
