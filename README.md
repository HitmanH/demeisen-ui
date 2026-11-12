# Demeisen UI

The shared look for Demeisen apps (CRM, intranet and future ones): colours, type, header, buttons, forms,
tables, pills, tiles and messages, plus the Demeisen logo. Plain CSS with no build step, so it works in a
single-page app and in server-rendered pages alike. Light and dark mode follow the device setting
(force one with `<html data-theme="light|dark">`).

## Contents

- `dist/demeisen.css`: the stylesheet.
- `dist/assets/logo-mark.png`: the logo mark (transparent; drawn in the text colour so it suits both themes).
- `dist/assets/favicon.png`: browser tab icon.
- `examples/index.html`: every component on one page. Open it in a browser.
- `vendor.sh`: copies a tagged version into an app.

## Using it in an app

Each app keeps its **own copy of a fixed version**, so it never depends on this repo or a Demeisen server at runtime:

```
./vendor.sh v1.0.0 ../my-app/static/ui
```

Then in the page:

```html
<link rel="icon" href="/static/ui/assets/favicon.png">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,600&display=swap">
<link rel="stylesheet" href="/static/ui/demeisen.css">

<header class="top"><div class="wrap">
  <a class="brand" href="/"><i class="brand-mark" aria-hidden="true"></i>Demeisen <span>Intranet</span></a>
  <nav class="tabs"><a href="/" aria-current="page">Home</a> …</nav>
  <div class="top-right"><nav class="apps"><a href="…" aria-current="true">Intranet</a><a href="…">CRM</a></nav> …</div>
</div></header>
<main><div class="wrap"> … </div></main>
```

To update an app, run `vendor.sh` with the newer tag and commit the copy in that app.

## Rebranding (for another organisation)

Replace `dist/assets/logo-mark.png` and `favicon.png`, change the brand name in your header markup, and override
any colour variables (`--accent`, `--bg`, …) in a small stylesheet loaded after `demeisen.css`. Fonts load from
Google Fonts; to avoid that, drop the font link and the system fonts are used instead.

## Releasing

Change files in `dist/`, check `examples/index.html` in light and dark mode, bump the version in the header comment
of `demeisen.css`, then tag: `git tag v1.1.0 && git push --tags`.
