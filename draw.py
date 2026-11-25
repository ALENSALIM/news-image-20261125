"""Draw the front page for Wednesday 25 November 2026.

Everything is drawn in code with Pillow: no network, no photos, no
external assets, no randomness and no timestamps, so two runs produce
byte-identical PNG output. Layout follows README.md (the prose brief).

Layout flows top to bottom: each block starts below the previous
block's measured end, so wrapped text can never overlap the next
block. Two/three-column rows start below the tallest column.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

PAPER = (247, 242, 231)
INK = (20, 20, 20)
NAVY = (14, 42, 74)
RED = (160, 30, 34)
GRAY = (85, 85, 85)
RULE = (150, 142, 126)
CHART_BG = (238, 233, 220)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, f, max_width):
    """Wrap text into lines that fit max_width, measured with font f."""
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        cur = words[0]
        for word in words[1:]:
            trial = cur + " " + word
            if d.textlength(trial, font=f) <= max_width:
                cur = trial
            else:
                lines.append(cur)
                cur = word
        lines.append(cur)
    return lines


def para(d, x, y, text, f, color, max_width, leading):
    """Draw wrapped paragraph; return y just below the last line."""
    for line in wrap(d, text, f, max_width):
        d.text((x, y), line, font=f, fill=color)
        y += leading
    return y


def kicker(d, x, y, text, size=18):
    d.text((x, y), text, font=font(SANS_BOLD, size), fill=RED)
    return y + size + 6


def rule(d, x0, x1, y, width=2, color=RULE):
    d.line([(x0, y), (x1, y)], fill=color, width=width)


def draw_chart(d, x0, y0, x1, y1):
    """NVDA comeback line chart inside the given box."""
    d.rectangle([x0, y0, x1, y1], fill=CHART_BG, outline=RULE, width=2)
    d.text((x0 + 14, y0 + 10), "NVDA - THE COMEBACK",
           font=font(SANS_BOLD, 16), fill=INK)
    px0, px1 = x0 + 48, x1 - 16
    py0, py1 = y0 + 48, y1 - 42

    def py(price):
        return py1 - (price - 100) / 150.0 * (py1 - py0)

    for price in (100, 150, 200, 250):
        yy = py(price)
        d.line([(px0, yy), (px1, yy)], fill=(200, 194, 178), width=1)
        d.text((x0 + 8, yy - 7), "$%d" % price,
               font=font(SANS, 12), fill=GRAY)
    d.line([(px0, py1), (px1, py1)], fill=GRAY, width=2)
    pts = [(0.06, 240), (0.30, 205), (0.52, 168), (0.74, 126), (0.94, 165)]
    xy = [(px0 + f * (px1 - px0), py(p)) for f, p in pts]
    d.line(xy, fill=RED, width=4, joint="curve")
    for (fx, price), (cx, cy) in zip(pts, xy):
        d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=RED,
                  outline=(255, 255, 255), width=2)
    lab = font(SANS_BOLD, 14)
    d.text((xy[0][0] - 18, xy[0][1] - 24), "$240", font=lab, fill=RED)
    d.text((xy[3][0] - 14, xy[3][1] + 10), "$126", font=lab, fill=RED)
    d.text((xy[4][0] - 40, xy[4][1] - 24), "$165", font=lab, fill=RED)
    xf = font(SANS, 12)
    d.text((px0 + 0.06 * (px1 - px0) - 14, py1 + 8), "6 OCT",
           font=xf, fill=GRAY)
    d.text((px0 + 0.52 * (px1 - px0) - 16, py1 + 8), "12 NOV",
           font=xf, fill=GRAY)
    d.text((px0 + 0.94 * (px1 - px0) - 16, py1 + 8), "23 NOV",
           font=xf, fill=GRAY)
    note = "FRI 20 NOV: $126"
    nf = font(SANS_BOLD, 12)
    d.text((x1 - 8 - d.textlength(note, font=nf), py1 + 24),
           note, font=nf, fill=GRAY)


def build_image():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 36          # left margin
    rx = 988         # right edge

    # ---- Masthead ----
    d.rectangle([0, 0, W, 118], fill=NAVY)
    title = "THE DAILY GLOBE"
    tf = font(SERIF_BOLD, 62)
    d.text(((W - d.textlength(title, font=tf)) / 2, 12), title,
           font=tf, fill=(255, 255, 255))
    df = font(SANS, 16)
    d.text((mx, 92), "WEDNESDAY, 25 NOVEMBER 2026", font=df,
           fill=(220, 225, 235))
    tag = "ONE DAY  ·  ONE PAGE  ·  THE WHOLE WORLD"
    d.text((rx - d.textlength(tag, font=df), 92), tag, font=df,
           fill=(220, 225, 235))
    d.rectangle([0, 118, W, 122], fill=RED)

    # ---- Lead story: Nvidia / Huang ----
    y = kicker(d, mx, 134, "MARKETS", 18)
    y = para(d, mx, y, "HUANG'S $1 TRILLION DAY",
             font(SERIF_BOLD, 56), INK, 600, 58)
    y = para(d, mx, y + 10,
             "Nvidia soars 31.5% as its board brings back Jensen Huang "
             "- the biggest one-day gain ever recorded.",
             font(SERIF, 22), INK, 600, 27)
    y = para(d, mx, y + 8,
             "Nvidia's board voted unanimously on Monday to reinstate "
             "Jensen Huang as chief executive, twelve days after he "
             "stepped down. Shares closed 31.5% higher at $165.05, "
             "adding about $950 billion in value.",
             font(SANS, 19), (50, 50, 50), 600, 24)
    draw_chart(d, 656, 148, 988, 402)

    # Stat chips under the lead block
    chips = ["+31.5%  IN A DAY", "$165.05  CLOSE", "+$950BN  ADDED"]
    chip_y = max(y + 12, 414)
    cw = 304
    for i, chip in enumerate(chips):
        cx0 = mx + i * (cw + 20)
        d.rounded_rectangle([cx0, chip_y, cx0 + cw, chip_y + 34],
                            radius=6, fill=NAVY)
        cf = font(SANS_BOLD, 17)
        d.text((cx0 + (cw - d.textlength(chip, font=cf)) / 2, chip_y + 9),
               chip, font=cf, fill=(255, 255, 255))
    rule(d, mx, rx, chip_y + 46)

    # ---- Second row: two columns ----
    y = chip_y + 58
    col_w = 464
    cols2 = [
        (mx, "WAR IN UKRAINE",
         "KYIV CLAIMS SHIP STRIKE AS PUTIN VOWS REVENGE",
         "Zelenskiy confirmed Ukraine's drone strike on a Russian "
         "ship in the Gulf of Finland. Putin vowed retaliation for "
         "strikes on oil plants."),
        (524, "MIDDLE EAST",
         "HOUTHIS HIT RIYADH TOWER; 11 INJURED",
         "A Houthi drone attack on a tower in Riyadh injured eleven "
         "people. Houthis are 60 km from Aden, but Yemen's army says "
         "the city will hold."),
    ]
    row_end = y
    for x, kick, head, body in cols2:
        cy = kicker(d, x, y, kick, 17)
        cy = para(d, x, cy, head, font(SERIF_BOLD, 30), INK, col_w, 34)
        cy = para(d, x, cy + 6, body, font(SANS, 19), (50, 50, 50),
                  col_w, 23)
        row_end = max(row_end, cy)
    rule(d, mx, rx, row_end + 12)

    # ---- Third row: three columns ----
    y = row_end + 24
    cols3 = [
        (mx, "TECHNOLOGY", "HUAWEI GUILTY OF TRADE-SECRET THEFT",
         "US jury: Huawei guilty of trade-secret theft, cleared of "
         "racketeering."),
        (362, "WASHINGTON", "CIA AND SPY CHIEF'S OFFICE BREACHED",
         "CIA and spy chief's office hit by a breach of unclassified "
         "data."),
        (688, "THANKSGIVING", "TRUMP PARDONS FREEDOM AND FEATHERS",
         "Trump spared turkeys Freedom and Feathers, then honoured "
         "Giuliani."),
    ]
    row_end = y
    for x, kick, head, body in cols3:
        cy = kicker(d, x, y, kick, 15)
        cy = para(d, x, cy, head, font(SERIF_BOLD, 20), INK, 300, 24)
        cy = para(d, x, cy + 4, body, font(SANS, 16), (50, 50, 50),
                  300, 20)
        row_end = max(row_end, cy)
    rule(d, mx, rx, row_end + 10)

    # ---- In Brief strip ----
    y = row_end + 20
    d.text((mx, y), "IN BRIEF  —  ALL STORIES REPORTED 24-25 NOVEMBER 2026",
           font=font(SANS_BOLD, 15), fill=RED)
    briefs = [
        ("NEPAL", "5.6-magnitude quake hits Koshi Province, near the China border."),
        ("CRICKET", "England beat Australia by 8 wickets in the 2nd T20I."),
        ("INDIA", "BJP and Akali Dal reunite for the 2027 Punjab elections."),
        ("CULTURE", "GTA VI, out 19 November, dominates the games world."),
        ("TODAY", "International Day for the Elimination of Violence against Women."),
    ]
    bf = font(SANS, 15)
    bf_bold = font(SANS_BOLD, 15)
    y += 22
    for label, text in briefs:
        d.text((mx, y), label + "  —  ", font=bf_bold, fill=INK)
        d.text((mx + d.textlength(label + "  —  ", font=bf_bold), y),
               text, font=bf, fill=(50, 50, 50))
        y += 17
    foot = "The Daily Globe — one page, the whole world."
    ff = font(SANS, 12)
    d.text(((W - d.textlength(foot, font=ff)) / 2, y + 12),
           foot, font=ff, fill=GRAY)
    assert y + 12 + 12 <= H, "layout overflow: footer at %d" % y

    return img


if __name__ == "__main__":
    build_image().save("/tmp/preview-20261125.png")
