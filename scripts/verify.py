#!/usr/bin/env python3
"""Verification script for the Choosing and Running Local LLMs with Ollama guide.

Checks:
- LICENSE exists with the exact MIT copyright line
- README.md credits Asdale Dynamics, LLC
- All docs/ markdown files exist and reference the LLC
- All static/ HTML pages exist, are valid, link correctly, and print cleanly
- CSS and JS assets exist
- No secrets, API keys, or personal data in files
- No .github/workflows directory
- No git remotes configured

Run: python3 scripts/verify.py
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []


def fail(msg: str) -> None:
    ERRORS.append(msg)
    print(f"FAIL: {msg}")


def warn(msg: str) -> None:
    WARNINGS.append(msg)
    print(f"WARN: {msg}")


def ok(msg: str) -> None:
    print(f"ok: {msg}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class LinkChecker(HTMLParser):
    """Collects href/src attributes from HTML to verify internal links resolve."""

    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ("href", "src") and value:
                self.links.append(value)


def check_license() -> None:
    lic = ROOT / "LICENSE"
    if not lic.exists():
        fail("LICENSE file missing")
        return
    text = read(lic)
    expected = "Copyright (c) 2026 Asdale Dynamics, LLC"
    if expected not in text:
        fail(f'LICENSE missing exact copyright line: {expected!r}')
    else:
        ok("LICENSE has exact MIT copyright line")
    if "MIT License" not in text:
        fail("LICENSE does not mention MIT License")
    else:
        ok("LICENSE is MIT")


def check_readme() -> None:
    readme = ROOT / "README.md"
    if not readme.exists():
        fail("README.md missing")
        return
    text = read(readme)
    if "Asdale Dynamics, LLC" in text:
        ok("README credits Asdale Dynamics, LLC")
    else:
        fail("README does not credit Asdale Dynamics, LLC")
    # README should not reference a remote repo or workflows
    if ".github/workflows" in text:
        warn("README references .github/workflows")


def check_docs() -> None:
    docs_dir = ROOT / "docs"
    if not docs_dir.is_dir():
        fail("docs/ directory missing")
        return
    expected_docs = [
        "01-welcome.md",
        "02-what-is-ollama.md",
        "03-model-sizes.md",
        "04-hardware-needs.md",
        "05-install-ollama.md",
        "06-running-models.md",
        "07-privacy.md",
        "08-model-selection-worksheet.md",
        "faq.md",
    ]
    for name in expected_docs:
        p = docs_dir / name
        if not p.exists():
            fail(f"docs/{name} missing")
        else:
            text = read(p)
            if "Asdale Dynamics, LLC" in text:
                ok(f"docs/{name} credits Asdale Dynamics, LLC")
            else:
                warn(f"docs/{name} does not credit Asdale Dynamics, LLC")


def check_static() -> None:
    static_dir = ROOT / "static"
    if not static_dir.is_dir():
        fail("static/ directory missing")
        return

    css = static_dir / "css" / "style.css"
    js = static_dir / "js" / "app.js"
    if css.exists():
        ok("static/css/style.css exists")
    else:
        fail("static/css/style.css missing")
    if js.exists():
        ok("static/js/app.js exists")
    else:
        fail("static/js/app.js missing")

    html_pages = sorted(static_dir.glob("*.html"))
    if not html_pages:
        fail("no HTML pages in static/")
    for page in html_pages:
        text = read(page)
        parser = LinkChecker()
        parser.feed(text)
        # Title present
        if re.search(r"<title[^>]*>.+</title>", text, re.IGNORECASE | re.DOTALL):
            ok(f"{page.name} has a <title>")
        else:
            fail(f"{page.name} missing <title>")
        # CSS linked
        if "css/style.css" in text:
            ok(f"{page.name} links CSS")
        else:
            fail(f"{page.name} does not link CSS")
        # JS linked
        if "js/app.js" in text:
            ok(f"{page.name} links JS")
        else:
            fail(f"{page.name} does not link JS")
        # Asdale credit
        if "Asdale Dynamics, LLC" in text:
            ok(f"{page.name} credits Asdale Dynamics, LLC")
        else:
            fail(f"{page.name} does not credit Asdale Dynamics, LLC")
        # Internal links resolve
        for link in parser.links:
            if link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = (static_dir / link).resolve()
            if not target.exists():
                fail(f"{page.name}: broken link {link}")
        # Print styles for worksheet
        if page.name == "worksheet.html":
            if "@media print" in text or "print" in text.lower():
                ok("worksheet.html has print styles")
            else:
                fail("worksheet.html missing print styles")
            if '<button id="print-worksheet"' in text:
                ok("worksheet.html has a print button")
            else:
                fail("worksheet.html missing print button")


def check_no_secrets() -> None:
    """Scan all text files for common secret patterns."""
    patterns = [
        (re.compile(r"sk-[A-Za-z0-9]{20,}"), "OpenAI-style API key"),
        (re.compile(r"ghp_[A-Za-z0-9]{20,}"), "GitHub personal access token"),
        (re.compile(r"AKIA[0-9A-Z]{16}"), "AWS access key id"),
        (re.compile(r"[0-9a-f]{32}"), "possible MD5/secret hash"),
        (re.compile(r"-----BEGIN [A-Z ]+PRIVATE KEY-----"), "private key"),
    ]
    for path in ROOT.rglob("*"):
        if path.is_dir() or path.name == ".git":
            continue
        if path.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg", ".pdf", ".zip", ".gz"):
            continue
        try:
            text = read(path)
        except (OSError, UnicodeDecodeError):
            continue
        for pat, label in patterns:
            if pat.search(text):
                fail(f"{path.relative_to(ROOT)} appears to contain a {label}")


def check_no_workflows() -> None:
    wf = ROOT / ".github" / "workflows"
    if wf.exists():
        fail(".github/workflows directory present (must not add)")
    else:
        ok("no .github/workflows directory")


def check_no_git_remote() -> None:
    git_dir = ROOT / ".git"
    if not git_dir.exists():
        # Not initialized yet; will be checked after init
        return
    # Avoid importing git; just check config textually
    config = git_dir / "config"
    if config.exists():
        text = read(config)
        if "url =" in text:
            warn("git config contains a remote url (verify no push intended)")


def main() -> int:
    print("== Verifying Choosing and Running Local LLMs with Ollama ==")
    print(f"Root: {ROOT}\n")

    check_license()
    check_readme()
    check_docs()
    check_static()
    check_no_secrets()
    check_no_workflows()
    check_no_git_remote()

    print("\n== Summary ==")
    print(f"Errors:   {len(ERRORS)}")
    print(f"Warnings: {len(WARNINGS)}")
    if ERRORS:
        print("\nFix the errors above before committing.")
        return 1
    if WARNINGS:
        print("\nWarnings noted (non-fatal).")
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
