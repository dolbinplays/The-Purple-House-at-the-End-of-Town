from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
PARTS = ROOT / "assets" / "sprites" / "witch_parts"
OUT = PARTS / "_rig_preview.png"


def paste_fit(dst, name, box):
    img = Image.open(PARTS / f"{name}.png").convert("RGBA")
    x, y, w, h = box
    img = img.resize((w, h), Image.Resampling.LANCZOS)
    dst.alpha_composite(img, (x, y))


def main():
    canvas = Image.new("RGBA", (180, 220), (30, 18, 35, 255))
    d = ImageDraw.Draw(canvas)
    d.ellipse((55, 178, 125, 202), fill=(0, 0, 0, 72))
    ox, oy = 90, 176
    paste_fit(canvas, "boots", (ox - 24, oy + 1, 48, 30))
    paste_fit(canvas, "hips", (ox - 31, oy - 28, 62, 38))
    paste_fit(canvas, "arm_right", (ox + 14, oy - 72, 33, 45))
    paste_fit(canvas, "arm_left", (ox - 47, oy - 74, 31, 45))
    paste_fit(canvas, "body", (ox - 37, oy - 83, 74, 66))
    paste_fit(canvas, "hair_back", (ox - 34, oy - 119, 68, 44))
    paste_fit(canvas, "face_open", (ox - 25, oy - 111, 50, 37))
    paste_fit(canvas, "bangs", (ox - 30, oy - 126, 60, 34))
    paste_fit(canvas, "hat", (ox - 50, oy - 153, 100, 54))
    canvas.save(OUT)


if __name__ == "__main__":
    main()
