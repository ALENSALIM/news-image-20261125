[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/ALENSALIM/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/ALENSALIM/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

# The World in One Picture — Wednesday 25 November 2026

A single 1024x1024 newspaper front page that sums up the world's news for Wednesday, 25 November 2026. Drawn entirely in code (Pillow, no network, no photos, no external assets) so the program is fully deterministic: run it twice and the PNG bytes are identical.

## The paper

Masthead THE DAILY GLOBE, in large white serif capitals on a deep navy band across the top, with dateline "WEDNESDAY, 25 NOVEMBER 2026" and tagline "One day. One page. The whole world." A thin red rule under the masthead. Warm off-white paper; black serif headlines, small red sans-serif capitals for kickers and section labels, dark grey sans-serif body text.

## Lead story (top, full width, the biggest block on the page)

**MARKETS**

# HUANG'S $1 TRILLION DAY

"Nvidia soars 31.5% as its board brings back Jensen Huang — the biggest one-day gain ever recorded."

Nvidia's board voted unanimously on Monday 23 November to reinstate Jensen Huang as chief executive, twelve days after he stepped down. The shares closed 31.5% higher at $165.05, adding about $950 billion in market value.

Graphic: a drawn line chart on the right of the lead block, titled "NVDA — THE COMEBACK", showing the share price falling from about $240 in early October to $126 on Friday 20 November, then spiking steeply to $165 on Monday 23 November. Three stat chips under the chart: "+31.5% IN A DAY", "$165.05 CLOSE", "+$950BN VALUE".

## Second row — two columns

**WAR IN UKRAINE**

### KYIV CLAIMS SHIP STRIKE AS PUTIN VOWS REVENGE

Zelenskiy confirmed Ukraine's drone strike on a Russian ship in the Gulf of Finland. Putin vowed retaliation for strikes on oil plants.

**MIDDLE EAST**

### HOUTHIS HIT RIYADH TOWER; 11 INJURED

A Houthi drone attack on a tower in Riyadh injured eleven people. Houthis are 60 km from Aden, but Yemen's army says the city will hold.

## Third row — three columns

**TECHNOLOGY**

### HUAWEI GUILTY OF TRADE-SECRET THEFT

US jury: Huawei guilty of trade-secret theft, cleared of racketeering.

**WASHINGTON**

### CIA AND SPY CHIEF'S OFFICE BREACHED

CIA and spy chief's office hit by a breach of unclassified data.

**THANKSGIVING**

### TRUMP PARDONS FREEDOM AND FEATHERS

Trump spared turkeys Freedom and Feathers, then honoured Giuliani.

## Bottom strip — IN BRIEF

A ruled strip with five one-line items:

- **NEPAL** — A 5.6-magnitude earthquake hits Koshi Province near the Chinese border.
- **CRICKET** — England beat Australia by eight wickets in the second T20I to level the series.
- **INDIA** — BJP and Akali Dal announce an alliance for the 2027 Punjab elections after a six-year split.
- **CULTURE** — Grand Theft Auto VI, released 19 November, dominates the global games conversation.
- **TODAY** — 25 November is the International Day for the Elimination of Violence against Women.

"All stories reported 24–25 November 2026. The Daily Globe — one page, the whole world."

## How it runs

main.py (repo root) writes exactly one file, /output/entry.png (1024x1024, PNG, under 1 MiB). It never deletes the output folder itself — it only clears files inside it — because the grader runs it as sandbox user 65534. All drawing lives in draw.py. No network, no randomness, no timestamps in the image, so two runs produce byte-identical output.

Entry for the make.fun news-image-20261125 bounty — see the bounty page at https://make.fun/bounty/news-image-20261125.
