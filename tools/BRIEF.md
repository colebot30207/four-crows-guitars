# Claude Code brief — The Four Crows Guitars website

Paste this into Claude Code as the first message, from inside an empty project folder.

---

## What we're building
A static marketing site for **The Four Crows Guitars**, an online guitar store. Nothing is sold on this site. Every "buy" action links to the Reverb shop: https://reverb.com/shop/thefourcrows

Client: Philip Sjostedt. I'm the developer (Cole). I host and maintain it.

## Tech + hosting constraints
- Plain HTML, CSS and a little vanilla JS. No framework, no build step, no backend.
- Hosting: **Porkbun Static Hosting** connected to a GitHub repo via Porkbun's GitHub Connect. Porkbun serves the repo root, so `index.html` must sit at the **root of the repo**, not in a `/dist` or `/public` folder.
- Must be fully responsive (phone first) and fast. Compress all images (WebP, max ~1600px wide, with sensible `srcset` sizes).
- Good basic SEO: title, meta description, Open Graph tags with a share image, favicon from the logo, `sitemap.xml`, `robots.txt`.

## Pages / sections (single page is fine)
1. **Header** — logo, nav (Collection, About), "Shop on Reverb" button.
2. **Hero** — headline, 1–2 lines of copy, button to the Reverb shop, one strong guitar photo.
3. **Collection** — a grid of **10 guitars** from the photos in `/assets/photos`. Each card: photo + guitar name. **Every card links to the main Reverb shop URL above, not to a specific listing** (the guitars aren't listed individually on Reverb). Open in a new tab.
4. **About** — short story section. Leave clearly marked placeholder text for Philip to supply.
5. **Closing CTA** — "Ready to find your next guitar?" + Reverb button.
6. **Footer** — © year, contact email placeholder.

## Brand
- Logo files are in `/assets/logo`. They are **black only**. The design is dark (near-black background, warm off-white text, brass/amber accent), so **create a white knockout version** of the logo (white on transparent, as SVG if possible, otherwise PNG) and use that on dark backgrounds. Keep the original black version for the favicon and any light areas.
- Use the stacked logo where there's room and the horizontal logo in the header.
- Typography: a bold serif or condensed display face for headings that suits the logo, and a clean sans for body copy (Google Fonts is fine).
- No stock-photo filler, no lorem ipsum, no invented facts. Where info is missing, use a visible `[PLACEHOLDER: …]`.

## Files I'm providing
- `/assets/logo/` — Philip's logo files
- `/assets/photos/` — the 10 guitar photos (from his Dropbox)
- Guitar names, if any: in `/assets/guitars.txt` (otherwise use the photo file names as temporary labels)

## Workflow
1. Look at the assets first, then propose the layout in a few lines before writing code.
2. Build the site, then start a local preview server so I can check it on desktop and phone width.
3. Initialize git, write a short README (how to edit a guitar card, how to deploy), and push to a new GitHub repo named `four-crows-guitars`. I'll connect that repo in Porkbun.
4. Give me a checklist of anything I need to do in Porkbun (domain, Static Hosting, GitHub Connect, SSL) and anything still waiting on Philip.
