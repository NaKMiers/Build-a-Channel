# Section 4 Why Companies Love It — Implementation Notes (2026-06-23)

## Build

- Created on the S1–S3 pattern + CSS kit (scenes on tracks 1/3/4/5/6/7 with cross-fades, cues on track 2, audio track 10, GSAP show/hide/smash/pop/reveal, `window.__timelines["Section04Why"]`).
- 6 distinct vivid object bases; varied CSS idea-devices (gold coins, rising geyser, stack, rain, kinetic words, calendar rings, payoff); 4 giant WIT beats varied by side/pose.
- Assets materialized as a local working set under `assets/` (junctions 404 with the CLI on this box): fonts, 4 WIT PNGs, 6 base files, the section mp3.

## Word timings

- None existed → GENERATED via transformers.js whisper-tiny.en. 172 words. A chunk-boundary BACKWARD-jump glitch around 24–26s (the "worth a little / pays every month" line re-emitted with bad timestamps); pinned cues to the CLEAN word starts instead. Tail "trap." ends ~51.46 → composition capped at 51.093.

## Build gotchas

- Reused bases trip `duplicate_media_discovery_risk`: cash (BS1+BS4) and coffee (BS2+BS3) each got a 2nd filename copy (`base-cash-lot.jpg`, `base-coffee-machine.jpg`).
- S5 first build overlapped the centered `RECURRING` word with the centered confused WIT → moved WIT to the LEFT and all text/rings to the RIGHT half (clean split).
- S2 sleeping-burned-out WIT enlarged to width 1340 (was reading small).
- No emoji glyphs — coins are CSS circles with `$`; calendar marks are CSS red rings.

## Review fix (2026-06-23, round 2)

- BS5 had 4 red rings floating on the calendar that circled nothing (reviewer: "the circles don't circle anything"). Replaced them with a meaningful real-UI device: an `AUTO-PAY · THE SAME CHARGE, EVERY MONTH` statement card whose identical `−$9.99` rows (Jan/Feb/Mar/Apr) pop in one-per-beat — that visibly demonstrates "recurring" instead of decorative circles. Layout unchanged otherwise (WIT confused left, RECURRING + card + FORGETFULNESS on the right). Re-checked lint/validate/inspect clean; snapshots 35.5/38.5 verified.

## Checks

- `lint`: 0 errors, 1 non-blocking warning (`timeline_track_too_dense`: 6 cues on track 2).
- `validate`: 0 errors, 0 warnings, 30 non-blocking contrast advisories.
- `inspect --at 3.5,9.8,17.0,27.2,33.6,37.0,45.2,50.5`: 0 layout issues.
- `snapshot` (same): all beats verified — distinct bases, varied idea-devices, giant WIT, no collisions; S5 split clean.

## Server

- `http://localhost:1004/#project/Build%20a%20Channel`
- `http://localhost:1004/api/projects/Build%20a%20Channel/preview/comp/index.html`

## Not done (by rule)

- No MP4/WebM export (not requested).
