# Section 5 Visual Plan

Video: `Why Buy 1 Get 1 Free Beats 50% Off`
Section: `Section 5: The Price Never Drops`
Status: `REMADE 2026-06-24 — fresh distinct retail bases + clean spaced text; see IMPLEMENTATION.md for as-built`

> Remake note: v1 lazily reused cash/coins/curtain from other sections and stacked overlapping text. As-built now uses 5 FRESH retail bases (shelf-tags → red sale store → boutique → aisle → clothing shop) with one clean hero device per beat, well-spaced and sequentially timed. The base table below reflects the original (money) plan; the shipped bases are in ATTRIBUTION.md / IMPLEMENTATION.md.

## Section Goal

Show anchoring: the price on the sign never drops. 50% off shrinks the perceived value ($10 → $5, "looks cheap forever"); BOGO keeps the proud $10 and adds a "bonus." Stores get the sale without admitting it's cheap, and they design the shape because you want the first one a lot and the second one barely at all.

## Source Inputs

- Script: `02-script.md` → Section 5
- Voiceover: `voiceover/section-05-the-price-never-drops/scratch-audio/...-0.82.mp3`
- Word timings: `voiceover/section-05-the-price-never-drops/section-05-word-timings.json` (tail `27.2s+` hand-estimated; whisper dropped it)
- Section duration: `36.416s`

## Narration

```text
Third trick, and it is the sneaky one. The price on the sign never drops.
Fifty percent off whispers: this thing is only really worth five bucks. And now five is the normal price in your head. The product looks cheap, forever.
Buy one, get one free keeps that proud ten-dollar price right there. The "real" price stays high. You just got a bonus on top.
Stores love that. They get the sale without admitting the thing is cheap.
And they pick this shape on purpose. You want the first one a lot, and the second one, eh, not really. At half price you would buy just one. So they do not drop the price. They shove a second one at you and charge full for the first.
```

## Visual Direction (subscription vivid-hook bar)

- 5 big scenes, ~13 cue beats; vivid dark money/curtain bases + giant CSS price-tag devices + GIANT WIT (~1280–1340px) varied per scene
- Bases: cash → coins → red curtain → cash → coins (dark grades, heavy scrim)
- Hero devices: "$10 never drops" tag + blocked down-arrow (A); $10→$5 shrink + "LOOKS CHEAP forever" (B); proud gold $10 + "+1 FREE bonus" (C); "Stores LOVE this" (D); FIRST-vs-SECOND want-meter + "FULL price for #1" stamp (E)
- WIT path: price-tag-suspicion → deadpan-side-eye → shocked → facepalm → empty-wallet
- Motion: hard-show + impact on the $5 shrink, the cheap-forever stamp, the bonus badge, the full-price stamp

## Big Scene Plan

| Scene | Local Time | Voice Range | Base | Hero Device | WIT |
|---|---:|---|---|---|---|
| A — the price never drops | 0.0–4.56 | "Third trick… never drops" | cash | "$10 on the sign" + blocked ↓ "never drops" | price-tag-suspicion R |
| B — 50% off shrinks value | 4.56–12.62 | "only worth five bucks… cheap forever" | coins | $10 struck → $5 "feels normal" + "LOOKS CHEAP forever" | deadpan-side-eye L |
| C — BOGO keeps proud price | 12.62–20.02 | "keeps that proud $10… a bonus on top" | red curtain | proud gold $10 "real price stays HIGH" + "+1 FREE bonus" | shocked C |
| D — stores love it | 20.02–23.68 | "Stores love that… without admitting it's cheap" | cash | "Stores LOVE this" + "a sale without admitting it's cheap" | facepalm R |
| E — designed shape | 23.68–36.416 | "want the first a lot, second eh… charge full for the first" | coins | FIRST (want a lot) vs SECOND (…eh) want-meter + "FULL price for #1" stamp | empty-wallet L |

## Cue Timeline (word-pinned; see IMPLEMENTATION.md for exact data-starts)

- "$10" tag @2.16; "never drops" + blocked arrow @3.24
- whisper @5.52; $10 struck @6.50; $5 "normal now" @8.80; "LOOKS CHEAP forever" @11.34
- proud $10 @12.88; "+1 FREE bonus" @18.48
- "Stores LOVE this" @20.02; "without admitting it's cheap" @21.74
- "shape on purpose" @23.68; FIRST want @25.74; SECOND eh @27.60; "FULL price for #1" @33.74

## HyperFrames Guidance

- Composition: `Section05Anchor`, 1920x1080, 36.416s, port 1005
- Devices: `.ptag` price tags (proud/small/struck), blocked `.arrow`+`.noband`, `.badge` bonus, `.want` meter, stamps
- WIT giant (~1280–1340px), anchored high, legs-only crop; devices arranged opposite WIT
- Must not invent: scene order, vivid bases, the price-tag/shrink/want-meter devices, WIT poses, word-pinned timing

## Approval Checks

- vivid dark bases per scene: yes
- giant kinetic hero device per beat: yes (price tags, shrink, want-meter)
- WIT giant + varied: yes (5 poses; sides R/L/C/R/L)
- word-pinned (tail hand-estimated, noted): yes
- anchoring reads (price never drops / shrink / proud): yes
- safe for learners: yes
- ready: yes (built + validated, 0 errors)
