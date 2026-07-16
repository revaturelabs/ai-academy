# Publishing AI Academy to GitHub Pages

This repo is configured to publish as a Jekyll site on GitHub Pages. No content
files were modified — the site is driven entirely by `_config.yml` and the
GitHub Pages default plugins.

## Site URL

Once Pages is enabled, the site will be served at:

> **https://revaturelabs.github.io/ai-academy/**

## One-time setup on GitHub (repo Settings)

GitHub Pages must be turned on in the repository — this cannot be done from a
commit; a maintainer has to click it once:

1. Go to **Settings → Pages**.
2. Under **Build and deployment → Source**, choose **Deploy from a branch**.
3. Set **Branch** to `main` (or whichever branch holds the merged content) and
   **Folder** to `/ (root)`, then **Save**.
4. Wait ~1–2 minutes for the first build, then open the site URL above.

> If you publish from a branch other than `main`, or under a different repo
> name / custom domain, update `baseurl` (and `url`) in `_config.yml` to match,
> otherwise the theme CSS and internal links will 404.

## How it works (no content edits needed)

GitHub Pages auto-enables a set of plugins that make the existing Markdown work
as-is:

| Plugin | What it does here |
| --- | --- |
| `jekyll-optional-front-matter` | Renders the ~389 `reading.md` files that have **no** YAML front matter |
| `jekyll-relative-links` | Rewrites `[text](../foo/reading.md)` links to the generated `.html` URLs, so the in-page **Prev / TOC / Next** navigation keeps working |
| `jekyll-readme-index` | Serves each folder's `README.md` as that folder's index page (so `CIT/` and `Cresent/Technical/` become browsable indexes) |
| `jekyll-titles-from-headings` | Uses each page's first heading as its HTML `<title>` |
| `jekyll-default-layout` | Applies the theme layout to pages without front matter |

The landing page is `index.md`; the theme is `jekyll-theme-cayman`.

## Preview locally (optional)

Requires Ruby + Bundler.

```bash
bundle install
bundle exec jekyll serve --baseurl ""
```

Then open http://localhost:4000/ . (The empty `--baseurl ""` override lets you
browse locally at the root; production uses `/ai-academy`.)

## Changing the look

- **Theme:** change `theme:` in `_config.yml` to any
  [supported GitHub Pages theme](https://pages.github.com/themes/) (e.g.
  `minima`, `jekyll-theme-minimal`, `jekyll-theme-slate`).
- **Title / description:** edit the top of `_config.yml`.
- **Landing page:** edit `index.md`.
