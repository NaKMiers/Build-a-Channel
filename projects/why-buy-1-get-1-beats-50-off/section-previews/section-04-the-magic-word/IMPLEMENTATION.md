# Section 4 Render Implementation

Video: `Why Buy 1 Get 1 Free Beats 50% Off`
Section: `Section 4: The Magic Word`
Status: `built to subscription vivid-hook bar, ready for review`

## Result

- Preview project: `section-previews/section-04-the-magic-word/`
- Composition: `Section04Magic`
- Port: `1004`
- Studio URL: `http://localhost:1004/#project/section-04-the-magic-word`
- Direct composition URL: `http://localhost:1004/api/projects/section-04-the-magic-word/preview/comp/index.html`
- Runtime: `37.099s`
- Word timings: `voiceover/section-04-the-magic-word/section-04-word-timings.json`

## Big Scene / Cue Plan Implemented

| Cue | Time | Voice Cue | Scene | What Changes | Motion | WIT | Sync |
|---:|---:|---|---|---|---|---|---|
| A1 | 0.40 | "the magic word" | A brain | label | hard-show | holding-phone-panic R ~1120 | word |
| A2 | 1.12 | "free" | A | giant glowing FREE (300px) | impact | - | word |
| A3 | 3.06 | "a little stupid" | A | "brain → a little stupid" | hard-show | - | word |
| B1 | 5.32 | "stop doing math" | B coins | "5 + 5 = …" | hard-show | confused L ~1120 | word |
| B2 | 5.84 | (math switches off) | B | BRAIN OFF badge | impact | - | word |
| B3 | 7.78 | "do I even want a second one?" | B | "?" toast | pop | - | word |
| C1 | 9.66 | "Dan Ariely" | C gift | ZERO-PRICE EFFECT caption | hard-show | awkward-celebration C ~1180 | word |
| C2 | 14.34 | "free feels like a gift" | C | "FREE feels like a GIFT" | impact | - | word |
| C3 | 16.48 | "switch our brains off" | C | "brains OFF" badge | impact | - | word |
| D1 | 17.95 | "fifty percent off is a number" | D cash | blue NUMBER card | hard-show | suspicious R ~980 | word |
| D2 | 21.36 | "free is a feeling … yells yes" | D | red FEELING card + "YES!" | impact | - | word |
| E1 | 26.66 | "not a discount … a word" | E coins | "not a ~discount~ - a WORD" | hard-show | betrayed R ~1150 | word |
| E2 | 30.28 | "stapling a full-price purchase" | E | "FREE + a FULL-PRICE purchase" | hard-show | - | word |
| E3 | 33.24 | "a free shampoo" | E | hostage photo (framed shampoo) | pop | - | word |
| E4 | 35.36 / 36.50 | "with a hostage" | E | rope + "HOSTAGE / full price paid" ransom | impact | - | word |

## Render Review-Prevention Pass

- voice cue map: built from `section-04-word-timings.json`
- subscription bar applied UP FRONT: vivid dark bases (brightness 0.42–0.6) + giant kinetic devices + giant WIT + 5 scenes + motion
- WIT density: 5 (1/scene), giant ~980–1180px, poses holding-phone-panic/confused/awkward-celebration/suspicious/betrayed; sides r/l/c/r/r (D/E share right but differ in pose+scale)
- emoji guard: removed a 🎁 glyph (Kokoro/Chromium snapshot doesn't render emoji) - "a GIFT" is text only
- collisions: devices arranged opposite each WIT; checked in contact sheets - clear
- HyperFrames mechanics: lint 0 errors (2 advisory), validate 0 errors, deterministic GSAP, sequential cue track, audio clip

## Verification

- lint: 0 errors, 2 warnings (timeline_track_too_dense advisory)
- validate: 0 errors, 0 warnings, 15 non-blocking contrast advisories
- contact sheets: `snapshots/contact-sheet-1.jpg` + `-2.jpg` at 12 timestamps - FREE/devices/WIT all read, hostage punchline lands, no bad crops
- export/render: not requested (no MP4)

## Notes

- Bases: brain (CC0), coins (CC0, B+E), gift boxes (CC0), cash (CC0); shampoo prop (CC0 illustration) used as a white-bordered hostage photo. WIT shared poses. Local working-set assets.
- First section built to the hardened SKILL bar without a rejection pass.
- 2026-06-24: owner asked to make WIT bigger → enlarged all 5 to ~1280–1340px (A 1120→1340, B 1120→1340, C 1180→1320, D 980→1280, E 1150→1340), anchors `bottom -350…-360`; heads stay in frame, legs crop, devices re-checked clear. Re-validated 0 errors; mirror synced.
