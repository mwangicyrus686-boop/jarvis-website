# Prompt for GitHub Copilot: review and publish the JARVIS website

Copilot cannot see the Claude chat. Open the `jarvis-website` folder in VS Code, open Copilot Chat in agent mode, and paste the prompt below. Copilot will also read `.github/copilot-instructions.md` from the folder.

```text
This repository is a static preview website for a project called JARVIS (a research and paper-trading workshop for Deriv demo accounts). Help me publish it with GitHub Pages.

Hard rules:
1. Do not add, request, print or guess any credentials, tokens, account IDs or API keys, and do not add any JARVIS application code, database or logs to this repository.
2. Keep the site static: no JavaScript, no frameworks, no third-party requests. Do not change what the pages claim. Do not describe JARVIS as profitable or risk-free. Keep the disclaimer on every page.
3. Ask me before you run git push, change repository settings, or add any file or dependency I did not ask for.

Tasks, in order:
1. Read .github/copilot-instructions.md and README.md.
2. Run `python tools/check_site.py`. If it fails, show me the problems and propose minimal fixes. Do not weaken the checker.
3. Review the five pages in site/ for accessibility (one h1, focus visibility, contrast of at least 4.5:1, a working skip link) and for broken links. List findings before editing anything.
4. Run `git status` and confirm that no .env, .db, log or token file would be committed.
5. Help me initialise the repository, commit, and, after I confirm, push to a new repository named jarvis-website on main.
6. Remind me to set Settings > Pages > Source to "GitHub Actions" (you cannot do this for me), then help me read the Actions run.
7. When the deployment finishes, give me the site URL and a checklist to open each page.

Finish by listing anything you changed and anything you could not verify.
```

What Copilot cannot do for you: turn on GitHub Pages in the repository settings, and confirm the live site looks right in your browser. Do those two steps yourself.
