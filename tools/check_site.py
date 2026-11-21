#!/usr/bin/env python3
"""Checks the static JARVIS site in ./site. Exit code 1 means a problem. Standard library only, offline."""
import re, sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "site"
problems = []
pages = sorted(SITE.glob("*.html"))
if not pages:
    problems.append("no html pages found in site/")
BAD_WORDS = ["guaranteed", "risk-free", "risk free", "get rich", "passive income", "100% win"]
SECRET = re.compile(r"(token|secret|passw(or)?d|api[_-]?key|client[_-]?id)\s*[:=]\s*[\"']?[A-Za-z0-9_\-]{12,}", re.I)
for page in pages:
    text = page.read_text(encoding="utf-8")
    low = text.lower()
    name = page.name
    for needle, why in (('<html lang="', "missing lang"), ("<title>", "missing title"), ('name="viewport"', "missing viewport"), ("Not financial advice", "missing disclaimer"), ('class="skip"', "missing skip link")):
        if needle not in text:
            problems.append(f"{name}: {why}")
    if low.count("<h1") != 1:
        problems.append(f"{name}: needs exactly one h1 (found {low.count('<h1')})")
    if "<script" in low:
        problems.append(f"{name}: scripts are not allowed")
    for attr, url in re.findall(r'(href|src)="([^"]*)"', text):
        if re.match(r"^(https?:)?//", url):
            problems.append(f"{name}: external reference {url}")
        elif url.startswith(("#", "mailto:")):
            continue
        elif not (SITE / url.split("#")[0]).exists():
            problems.append(f"{name}: broken link {url}")
    for word in BAD_WORDS:
        if word in low:
            problems.append(f"{name}: promotional claim '{word}'")
    if SECRET.search(text):
        problems.append(f"{name}: looks like a credential")
    if re.search(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", text):
        problems.append(f"{name}: emoji found")
css = SITE / "styles.css"
if not css.exists():
    problems.append("styles.css is missing")
elif re.search(r"(@import|url\(\s*[\"']?https?:)", css.read_text(encoding="utf-8")):
    problems.append("styles.css makes external requests")
if problems:
    print("SITE CHECK FAILED")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print(f"Site check passed: {len(pages)} pages, no external requests, no scripts, disclaimer present.")
