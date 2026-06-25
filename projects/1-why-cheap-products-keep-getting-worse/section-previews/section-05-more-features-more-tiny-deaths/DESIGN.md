# DESIGN

Project:
`Why Cheap Products Keep Getting Worse`

Composition:
`Section05MoreFeaturesMoreTinyDeaths`

## Remake From Scratch (2026-06-21)

Rebuilt the composition fresh and voice-synced. 2 big scenes: one real fridge (`fridge.jpg`) persisting 0-29.52 that gains a staggered feature pile (`SCREENS / SENSORS / WATER LINES / ICE DISPENSER / SOFTWARE / + OPINIONS`) into "A SMALL TECHNOLOGY COMMITTEE", then a real control board (`circuit-board.jpg`) 29.52-34.704 for the failure payoff `HARDER + MORE EXPENSIVE TO FIX`. 3 WIT beats: `awkward-celebration` (features good) / `confused` (committee) / `money-panic` (expensive fix). Removed an unneeded stray brand-mask.

Timing is `whisper-derived`: audio transcribed with `transformers.js` (`@xenova/whisper-tiny.en`, WASM); word timings in `voiceover/section-05-.../section-05-word-timings.json`; every scene cut + reveal pinned to real word times. Verified lint 0 / validate 0 / inspect 0 (8 samples); snapshot QA confirms the feature pile builds in sync with the spoken list. Synced to `hyperframes/review/section-05.html` and the unified full video (`hyperframes/full-video/compositions/section-05.html`, audio stripped; S5 duration unchanged so offsets are unaffected).

## Style Prompt

Real-photo recovery remake for the "more complicated products" section. Match the stronger Section 1 / Section 8 grammar: one large real texture per scene, sparse handwritten labels, red evidence marks only where they point to a real object, and WIT as a large emotional character rather than a small neutral sticker.

This remake intentionally supersedes the earlier CSS-only Section 5 direction. The old synthetic fridge/circuit-board mockup made the section feel too normal and too crowded.

## Scene Grammar

- Scene 1: real lived-in kitchen/fridge photo, fair setup, `COMPLICATED IS NOT BAD`
- Scene 2: same real fridge photo cropped closer, `BE COLD` baseline versus feature overload
- Scene 3: real appliance circuit-board photo, tiny failure point and repair-cost payoff

## Colors

- Paper background: `#f3ead5`
- Ink: `#17120f`
- Cream label: `#fff8df`
- Feature yellow: `#efc640`
- Soft blue: `#d9edf2`
- Soft green: `#dcefcf`
- Red markup: `#8a1b16`
- Red label fill: `#fff0e8`
- Warm shadow: `rgba(29, 20, 13, 0.22)`

## Typography

- Handwritten labels: local `PatrickHand`, loaded from `assets/fonts/patrick-hand-latin.woff2`
- Labels stay uppercase, sparse, and large enough to read in contact-sheet review.

## Motion

- Static hard cuts only.
- Timed cue clips hard-show on spoken beats.
- No decorative transitions, no fly-in parade, and no MP4/WebM export unless explicitly requested.

## WIT Direction

- Use stronger approved WIT poses: price-tag suspicion, phone panic, trapped-by-app-screen, and money panic.
- WIT appears as a main character on emotional beats, not as a corner decoration.
- Do not place labels over WIT's face, glasses, head, shoulders, phone, or money props.

## What Not To Do

- Do not revive the rejected CSS-only fridge/circuit-board composition.
- Do not use the logo-heavy water dispenser or branded control panel photos directly.
- Do not claim the real fridge photo depicts a failed product; it is only a generic lived-in appliance texture.
- Do not scatter many small feature cards across the frame.
