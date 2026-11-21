# JARVIS website (preview)

A plain static preview of the JARVIS Trading Workshop: Home, Dashboard, Strategy Lab, Bots, Builder, Methodology, Safety and Integrations pages. The pages show sample data and a design only. The working JARVIS app runs locally and is not part of this repository. Demo accounts and paper trading only; not financial advice.

## Folder layout
- `site/`: the website (8 HTML pages, `styles.css`, `.nojekyll`). This is the only folder that gets published.
- `tools/check_site.py`: offline checks (links, no scripts or external requests, disclaimer, no credentials). It runs before every deploy.
- `.github/workflows/pages.yml`: checks the site and deploys `site/` to GitHub Pages on every push to `main`.
- `.github/copilot-instructions.md`: the rules GitHub Copilot follows in this repository.

## Preview on your PC (Command Prompt)
```bat
cd /d C:\path\to\jarvis-website
python tools\check_site.py
python -m http.server -d site 8000
```
Open http://127.0.0.1:8000 and press Ctrl+C in the window to stop.

## Publish with GitHub Pages
1. On github.com create a new repository named `jarvis-website`. Pages sites are public on the internet, and on a free plan the repository must be public too, so publish only what you are happy to show everyone.
2. Push the folder (the repository URL is shown on the new repository's page):
```bat
cd /d C:\path\to\jarvis-website
git init
git add .
git status
git commit -m "JARVIS website preview"
git branch -M main
git remote add origin https://github.com/YOUR-USER/jarvis-website.git
git push -u origin main
```
Read the `git status` list before committing. It must contain no `.env`, no `.db` file and no tokens (`.gitignore` blocks the usual ones).
3. In the repository open Settings, then Pages, and under Build and deployment set Source to GitHub Actions.
4. Open the Actions tab and wait for "Check and deploy the JARVIS website" to finish. The site address appears in the run summary, normally `https://YOUR-USER.github.io/jarvis-website/`.
5. Open every page of the live address and confirm the links work.

If the check step fails, the log lists exactly what to fix; nothing is published until it passes.
