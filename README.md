# The Four Crows Guitars — website

Static marketing site for [The Four Crows Guitars](https://reverb.com/shop/thefourcrows), Doylestown PA.
Nothing is sold here; every "Shop on Reverb" button links to the Reverb shop.

Plain HTML + CSS + a little vanilla JS. No build step. `index.html` is at the repo root so Porkbun Static Hosting can serve it directly.

```
index.html          the whole site (one page)
styles.css          styles (phone-first)
script.js           mobile menu, footer year, (no fallback tiles any more — every card needs a photo)
robots.txt / sitemap.xml
assets/logo/        black + white logo PNGs (+ original PDFs)
assets/img/         favicons, apple-touch-icon, og-image.jpg (share image)
assets/photos/      guitar photos (WebP) — see below
tools/optimize-photos.py   makes the WebP sizes from originals
```

## Adding / editing a guitar card

1. Put the original photo in `assets/photos/originals/` named `guitar-01.jpg` … `guitar-12.jpg` (and `hero.jpg` for the big hero image). Originals are git-ignored.
2. Run the optimizer (needs Python 3 + Pillow: `python3 -m pip install pillow`):

   ```bash
   python3 tools/optimize-photos.py
   ```

   It writes `guitar-01.webp`, `guitar-01-800.webp` and `guitar-01-480.webp` (max 1600px wide) into `assets/photos/`.
3. In `index.html`, find the matching `<li class="card">` and change:
   - the `<h3>` text → guitar name
   - the `alt="…"` → one-line description of the guitar
4. Commit and push. Done.

To add a 13th guitar, copy a whole `<li class="card">…</li>` block and bump the number.

## Deploying

Live at <https://thefourcrowsguitars.com> (domain registered at Porkbun, hosted on Netlify — site `four-crows-guitars`, site id `0ce44339-d5a4-4ce8-9898-a3f64e916bc4`). Porkbun DNS: ALIAS apex → `apex-loadbalancer.netlify.com`, CNAME `www` → `four-crows-guitars.netlify.app`. Let's Encrypt cert auto-renews; HTTPS is forced.

Deploys are pushed from this folder with the Netlify CLI (no build step):

```bash
git add -A
git commit -m "Update guitar cards"
git push
```

```bash
npx -y netlify-cli deploy --prod --dir . --site 0ce44339-d5a4-4ce8-9898-a3f64e916bc4
```

Optional: link the GitHub repo in the Netlify dashboard (Project configuration → Build & deploy → Link repository) and every push to `main` deploys on its own; the CLI step is then unnecessary.

Local preview (any static server works):

```bash
python3 -m http.server 8921
```

then open <http://localhost:8921>.

## Netlify badge

The free-plan "Powered by Netlify" badge is switched off via the site setting `built_with_badge_enabled: false` (set with `netlify api updateSite`).
