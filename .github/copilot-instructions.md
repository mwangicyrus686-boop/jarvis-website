# Instructions for GitHub Copilot in this repository

This repository is the public preview website for the JARVIS Trading Workshop. It is plain static HTML and CSS in `site/`.

Rules
- Keep it static: no frameworks, no JavaScript, no build step, no third-party requests (fonts, scripts, analytics, images from other hosts).
- Never add credentials, tokens, account IDs, client IDs, databases, logs or any JARVIS application code to this repository.
- Do not describe JARVIS as profitable, guaranteed, risk-free or as having a trading edge. Real trading is disabled and the site must keep saying so. Keep the footer disclaimer on every page.
- Sample data must stay clearly labelled as sample or preview. Controls that only work in the local app stay disabled.
- Keep it accessible: one h1 per page, real links and buttons, visible focus, text contrast of at least 4.5:1, a working skip link.
- Run `python3 tools/check_site.py` before every commit. It must pass.
- Ask before pushing, changing repository settings, or adding any dependency or workflow.
