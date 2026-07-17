# Publishing this site to GitHub Pages

This repo is set up to build with **Jekyll on GitHub Pages**. No content files
were edited — a small set of config files (`_config.yml`, `index.md`, `Gemfile`)
turns the existing Markdown readings into a browsable website.

**Live URL (once Pages is enabled):** <https://revaturelabs.github.io/ai-academy/>

## Scope

Only the **Crescent — AI Native Engineering Foundations** track is published.
The CIT track is intentionally hidden (see the `exclude:` list in
`_config.yml`), but the CIT diagram **image** files (`*.png`, `*.mmd`) are kept
in the build because several Crescent "Part B" readings embed them.

## One-time setup: turn on GitHub Pages

This is a repo-settings action (needs repo admin). After the Jekyll files are
pushed to the `Test` branch:

1. Go to **<https://github.com/revaturelabs/ai-academy>** → **Settings** → **Pages**.
2. Under **Build and deployment → Source**, choose **Deploy from a branch**.
3. Set **Branch** to **`Test`** and folder to **`/ (root)`**, then **Save**.
4. Wait ~1–2 minutes for the first build. GitHub shows the live URL at the top
   of the Pages settings page, and the **Actions** tab shows the "pages build
   and deployment" run (green check = success, red X = build error).
5. Open <https://revaturelabs.github.io/ai-academy/>.

> To publish from `main` instead, merge these files into `main` and pick that
> branch in step 3. If you do, no other change is needed.

## Preview locally (optional)

Requires Ruby. From the repo root:

```bash
bundle install
bundle exec jekyll serve --baseurl ""
# open http://127.0.0.1:4000/
```

## How it works

`_config.yml` enables GitHub-Pages-supported plugins so nothing in `content/`
had to change:

| Plugin | What it does here |
|---|---|
| `jekyll-optional-front-matter` | Renders `reading.md` files that have no YAML front matter |
| `jekyll-relative-links` | Rewrites `[text](../foo/reading.md)` links to the built `.html` URLs, so Prev / TOC / Next nav works |
| `jekyll-readme-index` | Serves each folder's `README.md` as its index — `Cresent/Technical/README.md` becomes the curriculum index |
| `jekyll-titles-from-headings` | Uses each page's first heading as its title |
| `jekyll-default-layout` | Applies the theme layout to pages without front matter |
| `jekyll-seo-tag` | Adds meta tags for search/social |
