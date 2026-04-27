#!/usr/bin/env python3
"""Render the circle-of-life diagram as a PNG using Pillow."""

from PIL import Image, ImageDraw, ImageFont
import math, os

W, H = 1170, 830
img = Image.new("RGB", (W, H), "#FAFAFA")
draw = ImageDraw.Draw(img)

# Try to load a font, fall back to default
try:
    font_title = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
    font_bold  = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 17)
    font_norm  = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 14)
except:
    font_title = font_bold = font_norm = ImageFont.load_default()

# ── Stages: (label, emoji, fill, outline, cx, cy) ──────────────────────────
stages = [
    ("Birth",          "👶", "#fff2cc", "#d6b656",  585, 140),
    ("Early\nChildhood","👧", "#dae8fc", "#6c8ebf",  820, 240),
    ("Girlhood",       "🌼", "#d5e8d4", "#82b366",  900, 390),
    ("Adolescence",    "🌟", "#ffe6cc", "#d79b00",  820, 540),
    ("Young\nWoman",   "🌸", "#f8cecc", "#b85450",  585, 630),
    ("Motherhood",     "🤰", "#e1d5e7", "#9673a6",  350, 540),
    ("Elder /\nWisdom","🧓", "#f0e6ff", "#7a4f9a",  270, 390),
    ("New\nGeneration","✨", "#fff2cc", "#d6b656",  350, 240),
]

rx, ry = 85, 48   # ellipse radii

def ellipse_point(cx, cy, angle_deg):
    a = math.radians(angle_deg)
    return cx + rx * math.cos(a), cy + ry * math.sin(a)

# ── Draw arrows between stages ──────────────────────────────────────────────
arrow_colors = ["#d6b656","#6c8ebf","#82b366","#d79b00","#b85450","#9673a6","#7a4f9a","#d6b656"]

def draw_arrow(p1, p2, color):
    draw.line([p1, p2], fill=color, width=3)
    # arrowhead
    dx, dy = p2[0]-p1[0], p2[1]-p1[1]
    length = math.hypot(dx, dy) or 1
    ux, uy = dx/length, dy/length
    lx, ly = -uy*8, ux*8
    tip = p2
    b1 = (tip[0] - ux*16 + lx, tip[1] - uy*16 + ly)
    b2 = (tip[0] - ux*16 - lx, tip[1] - uy*16 - ly)
    draw.polygon([tip, b1, b2], fill=color)

for i in range(len(stages)):
    s1 = stages[i]
    s2 = stages[(i+1) % len(stages)]
    # find exit angle from s1 toward s2 center
    dx, dy = s2[5]-s1[5], s2[4]-s1[4]  # note: positions are (cx,cy) at indices 4,5
    # Re-index: stages tuple is (label, emoji, fill, outline, cx, cy)
    cx1, cy1 = s1[4], s1[5]
    cx2, cy2 = s2[4], s2[5]
    dx, dy = cx2-cx1, cy2-cy1
    angle_out = math.degrees(math.atan2(dy, dx))
    angle_in  = math.degrees(math.atan2(-dy, -dx))
    p1 = ellipse_point(cx1, cy1, angle_out)
    p2 = ellipse_point(cx2, cy2, angle_in)
    draw_arrow(p1, p2, arrow_colors[i])

# ── Draw stage ellipses ──────────────────────────────────────────────────────
for label, emoji, fill, outline, cx, cy in stages:
    bbox = [cx-rx, cy-ry, cx+rx, cy+ry]
    draw.ellipse(bbox, fill=fill, outline=outline, width=3)
    # label (split on \n)
    lines = label.split("\n")
    line_h = 18
    total_h = len(lines) * line_h
    for j, line in enumerate(lines):
        tw = draw.textlength(line, font=font_bold)
        tx = cx - tw/2
        ty = cy - total_h/2 + j*line_h
        draw.text((tx, ty), line, fill="#333333", font=font_bold)

# ── Title ────────────────────────────────────────────────────────────────────
title = "The Circle of Life"
tw = draw.textlength(title, font=font_title)
draw.text(((W-tw)/2, 30), title, fill="#4A235A", font=font_title)

# ── Save ─────────────────────────────────────────────────────────────────────
out = os.path.join(os.path.dirname(__file__), "circle_of_life.png")
img.save(out, "PNG")
print(f"Saved: {out}  ({W}×{H})")
