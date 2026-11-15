#!/usr/bin/env python3
"""Make web-ready WebP guitar photos.

Put the original photos (JPG/PNG/HEIC-converted) in assets/photos/originals/
named guitar-01.jpg ... guitar-10.jpg and hero.jpg, then run:

    python3 tools/optimize-photos.py

Outputs, for each original:
    assets/photos/<name>.webp       (max 1600px wide)
    assets/photos/<name>-800.webp
    assets/photos/<name>-480.webp
Needs Pillow:  python3 -m pip install pillow
"""
import pathlib, sys
from PIL import Image, ImageOps

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "photos" / "originals"
OUT = ROOT / "assets" / "photos"
SIZES = {"": 1600, "-800": 800, "-480": 480}

files = [p for p in SRC.iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}]
if not files:
    sys.exit(f"No photos found in {SRC}")
for p in sorted(files):
    im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
    for suffix, width in SIZES.items():
        w = min(width, im.width)
        resized = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        dest = OUT / f"{p.stem}{suffix}.webp"
        resized.save(dest, "WEBP", quality=82, method=6)
        print(f"{dest.relative_to(ROOT)}  {resized.width}x{resized.height}  {dest.stat().st_size // 1024} KB")
