# Section 1 Render Implementation

Video:
`Why Buy 1 Get 1 Free Beats 50% Off`

Section:
`Section 1: Hook: You're The Rabbit`

Status:
`section preview built, ready for review`

## Result

- Preview project: `section-previews/section-01-hook/`
- Source: `05-visual-plan.md` → `visual-plan/section-01-hook/`
- Port: `1001`
- Studio URL: `http://localhost:1001/#project/section-01-hook`
- Direct composition URL: `http://localhost:1001/api/projects/section-01-hook/preview/comp/index.html`
- Runtime: `23.019s`
- Voiceover: `voiceover/section-01-hook/scratch-audio/section-01-hook-david23-am_eric-0.82.mp3`
- Visual plan: `visual-plan/section-01-hook/section-01-hook-visual-plan.md`

## Big Scene / Cue Plan Implemented

| Cue | Local Time | Voice Cue | Big Scene | What Changes | Motion Type | WIT Placement / Crop Guard | Label / Markup | Sync Status |
|---:|---:|---|---|---|---|---|---|---|
| A1 | 0.30 | "Here is something…" | A cart | "Sounds impossible…" label | hard-show | — | label | pinned |
| A1w | 2.00 | "impossible" | A | WIT suspicion | hard-show | price-tag-suspicion, RIGHT ~1/3, legs crop only | — | pinned |
| A2a | 3.88 | "free" | A | FREE! sticker | impact (pop) | — | "FREE! $5/item" | word-pinned |
| A2b | 6.70 | "half price" | A | 50% OFF tag | hard-show | — | "50% OFF $5/item" | word-pinned |
| B1 | 7.72 | "Same product…" | B cash | strip | hard-show | — | "Same product · same shelf · $5 each" | word-pinned |
| B2 | 12.36 | "doubles" | B | profit meter +$1/+$2, bar grows, ×2 | impact | — | "+$1 / +$2 / ×2" | word-pinned |
| B3 | 13.94 | "surprise" | B | WIT panic | hard-show | hidden-fee-panic, LEFT ~1/2, meter cleared RIGHT | — | word-pinned |
| B3m | 14.98 | "the free one" | B | red ring on FREE bar | impact | — | red ring | word-pinned |
| C1 | 19.22 | "not generosity" | C magic | headline | hard-show | — | "not generosity." | word-pinned |
| C2 | 20.78 | "magic trick" | C | headline | impact (smash) | — | "A MAGIC TRICK." | word-pinned |
| C3 | 21.60 | (after "trick") | C | WIT betrayed rises | hard-show | betrayed, CENTER ~1/2, payoff text on LEFT clear of face | — | pinned |
| C4 | 22.48 | "rabbit" | C | payoff | impact (smash) | — | "YOU ARE THE RABBIT" | word-pinned |

## Render Review-Prevention Pass

- voice cue map completed: yes — built from `section-01-word-timings.json` (whisper-tiny.en via transformers.js; tail glitch on "and you are the rabbit" hand-corrected to 21.60–23.019)
- big-scene sanity checked: yes (3 scenes, persistent)
- cue density checked: yes (7 beats)
- motion density checked: yes (impact reserved for FREE/doubling/ring/magic-trick/rabbit)
- WIT density: 3 (1/scene), sides right→left→center
- WIT crop/collision checked: yes — faces/glasses/shoulders clear; only legs crop; text never covers WIT face
- markup target checked: yes — red ring targets the FREE profit bar only
- scene differentiation checked: yes (cart / cash / curtain)
- HyperFrames mechanics checked: lint/validate pass, deterministic GSAP, audio clip, sequential cue track
- render decisions made beyond visual plan: cut A→B at "Same" (7.60) and B→C at "not generosity" (18.94) from real word timings; extended Scene B to carry "stores would rather hand you a freebie than knock 50% off" on the profit meter

## Verification

- lint: 0 errors, 0 warnings
- validate: 0 errors, 0 warnings, 10 non-blocking WCAG contrast warnings (cream 50% OFF tag measured against dark scene; renders readable dark-on-cream)
- inspect: timeline registers `Section01Hook`
- direct preview screenshots/contact sheet: `snapshots/contact-sheet.jpg` at 4.0/7.0/8.5/12.8/14.5/15.3/20.0/21.2/22.8 — all cues land on their words, WIT reads, no bad crops/collisions
- export/render: not requested (no MP4)

## Notes

- Assets are a local working set (real folder, not junction — junctions 404 on this Windows HyperFrames setup). Bases: greengrocer storefront (CC0), rising coin stacks (CC0), red curtain (CC0), magic hat (CC BY-SA 3.0, credit "Magicianidris"). WIT from shared poses. Font PatrickHandLocal.
- Possible review polish: in the final frame WIT covers the hat, softening the literal "pulled from the hat" read; could nudge WIT to let the hat peek.

## 2026-06-24 Review Pass (owner feedback on Section 1)

Backup of pre-edit canonical: `manual-saves/index-before-review-edits-120335.html`. Re-verified: lint 0 / validate 0 (25 non-blocking contrast advisories, same class as before) / snapshots at 4.0, 12.8, 21.2, 22.8 reviewed.

1. **Scene A & B images replaced** (owner: "illustrative images for scene 1 and 2 aren't suitable"). Scene A `base-a-shopping-cart.jpg` → `base-a-store-greengrocer.jpg` (a clear store, colorful produce, brand-free/people-free, dark-left for labels). Scene B `base-b-cash-usd.jpg` → `base-b-profit-coins.jpg` (rising gold coin stacks = profit doubling, echoes the profit meter). `.photo.cart` brightness 0.66→0.82, `.photo.cash` 0.6→0.66. Both new bases CC0 (Openverse); see ATTRIBUTION.md. Review mirror + its working set synced.
2. **"Rabbit" payoff = WIT becomes the rabbit** (owner: "when the voice says rabbit it should have a rabbit image"). Scene C WIT wrapped in `.witwrap`; CSS bunny ears (`.ears`/`.ear`, white + black outline + pink inner, matching WIT) `pop()` in at 22.48 on the word "rabbit" — WIT literally is the rabbit. No external asset; on-brand flat style.
3. **Text margins widened** to a ~safe area (owner: "margin of text to edges should be further"). Top-edge labels 40/70/84 → 100/104; Scene C left 90 → 110.
4. **WIT enlarged** (owner: "make WIT bigger"). Scene A 900→1190, Scene B 1140→1360, Scene C 1000→1180. Heads stay in frame; only legs crop.
