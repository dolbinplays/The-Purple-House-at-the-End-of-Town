from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "assets" / "source" / "witch_parts_sheet.png"
OUT = ROOT / "assets" / "sprites" / "witch_parts"

PARTS = {
    "hat": (10, 38, 520, 307),
    "hair_back": (18, 333, 425, 585),
    "bangs": (510, 226, 790, 382),
    "face_open": (526, 382, 758, 553),
    "face_blink": (760, 382, 976, 553),
    "body": (265, 586, 610, 862),
    "hips": (245, 885, 520, 1060),
    "arm_left": (20, 615, 170, 762),
    "arm_right": (640, 600, 812, 785),
    "boots": (42, 1070, 240, 1195),
}


def part_mask(name, size):
    w, h = size
    mask = Image.new("L", size, 0)
    d = ImageDraw.Draw(mask)
    if name == "hat":
        d.ellipse((0, 148, 510, 267), fill=255)
        d.polygon([(35, 155), (118, 48), (254, 10), (420, 55), (486, 158)], fill=255)
        d.polygon([(20, 65), (84, 6), (154, 32), (98, 120)], fill=255)
    elif name == "hair_back":
        d.ellipse((8, 6, 405, 250), fill=255)
        d.polygon([(15, 118), (58, 24), (204, 4), (385, 62), (405, 222), (235, 252), (28, 226)], fill=255)
    elif name == "bangs":
        d.ellipse((5, 0, 275, 155), fill=255)
        d.rectangle((20, 72, 252, 154), fill=255)
    elif name in ("face_open", "face_blink"):
        d.ellipse((40, 0, w - 1, h - 4), fill=255)
        d.ellipse((0, 68, 58, 134), fill=255)
    elif name == "body":
        d.polygon([(64, 18), (192, 0), (284, 28), (340, 236), (276, 276), (42, 270), (0, 228), (30, 52)], fill=255)
        d.ellipse((0, 80, 105, 250), fill=255)
        d.ellipse((250, 75, 345, 245), fill=255)
    elif name == "hips":
        d.polygon([(22, 22), (198, 0), (270, 72), (264, 170), (38, 172), (0, 86)], fill=255)
    elif name == "arm_left":
        d.polygon([(24, 4), (88, 24), (142, 124), (92, 146), (26, 112), (0, 50)], fill=255)
        d.ellipse((82, 106, 150, 146), fill=255)
    elif name == "arm_right":
        d.polygon([(0, 74), (68, 0), (160, 24), (166, 150), (72, 185), (4, 142)], fill=255)
    elif name == "boots":
        d.rounded_rectangle((2, 4, 83, 122), radius=31, fill=255)
        d.rounded_rectangle((92, 0, 196, 122), radius=31, fill=255)
    else:
        d.rectangle((0, 0, w, h), fill=255)
    return mask.filter(ImageFilter.GaussianBlur(1.1))


def masked_crop(src, name, box):
    img = src.crop(box).convert("RGBA")
    img.putalpha(part_mask(name, img.size))
    bbox = img.getbbox()
    if bbox:
        pad = 2
        img = img.crop((
            max(0, bbox[0] - pad),
            max(0, bbox[1] - pad),
            min(img.width, bbox[2] + pad),
            min(img.height, bbox[3] + pad),
        ))
    return img


def make_preview(parts):
    cell_w, cell_h = 190, 160
    preview = Image.new("RGBA", (cell_w * 3, cell_h * 4), (30, 18, 35, 255))
    d = ImageDraw.Draw(preview)
    for idx, (name, im) in enumerate(parts.items()):
        x = (idx % 3) * cell_w
        y = (idx // 3) * cell_h
        d.text((x + 8, y + 8), name, fill=(245, 223, 174, 255))
        scale = min((cell_w - 24) / im.width, (cell_h - 34) / im.height, 1)
        sized = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.Resampling.LANCZOS)
        preview.alpha_composite(sized, (x + (cell_w - sized.width) // 2, y + 28 + (cell_h - 34 - sized.height) // 2))
    preview.save(OUT / "_preview.png")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    src = Image.open(SRC)
    made = {}
    for name, box in PARTS.items():
        part = masked_crop(src, name, box)
        part.save(OUT / f"{name}.png")
        made[name] = part
    make_preview(made)


if __name__ == "__main__":
    main()
