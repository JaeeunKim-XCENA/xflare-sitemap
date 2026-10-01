#!/usr/bin/env python3
"""Derive the per-theme logo variants from xflare-logo.png.

The source is a white + yellow mark on solid black. Over black every pixel is
color * alpha, so the brightest channel recovers alpha and dividing it out
recovers the color. The result is cropped to the mark; the light-theme variant
repaints the white letters in the page's text color and keeps the yellow.

Rerun after replacing xflare-logo.png:  python3 make_logos.py
"""

from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "xflare-logo.png"
ON_DARK = HERE / "xflare-logo-on-dark.png"
ON_LIGHT = HERE / "xflare-logo-on-light.png"

LIGHT_INK = np.array([0x15, 0x17, 0x1C], dtype=np.float64)
# JPEG-ish noise in the black field would otherwise widen the crop box.
CROP_ALPHA_MIN = 8


def main() -> None:
    rgb = np.asarray(Image.open(SOURCE).convert("RGB"), dtype=np.float64)
    alpha = rgb.max(axis=2)
    color = np.divide(rgb * 255, alpha[..., None], out=np.zeros_like(rgb), where=alpha[..., None] > 0)

    # 1 for white letters, 0 for the saturated yellow chevrons.
    whiteness = (color.min(axis=2) / 255)[..., None]
    ink = whiteness * LIGHT_INK + (1 - whiteness) * color

    ys, xs = np.nonzero(alpha >= CROP_ALPHA_MIN)
    crop = (slice(ys.min(), ys.max() + 1), slice(xs.min(), xs.max() + 1))

    for path, fill in ((ON_DARK, color), (ON_LIGHT, ink)):
        rgba = np.dstack([fill, alpha])[crop]
        Image.fromarray(rgba.round().clip(0, 255).astype(np.uint8), "RGBA").save(path, optimize=True)
        print(f"wrote {path.name} {rgba.shape[1]}x{rgba.shape[0]}")


if __name__ == "__main__":
    main()
