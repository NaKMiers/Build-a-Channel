# DESIGN

Project:
`Why Cheap Products Keep Getting Worse`

Composition:
`Section01Hook`

## Style Prompt

Simple funny explainer hook in the spirit of sparse illustrated narration: a few connected big scenes, small cue changes inside each scene, hard cuts only, large handwritten labels, real channel WIT PNGs only on emotional beats, and no corporate slide layout.

## Colors

- Paper background: `#f2eadb`
- Ink: `#17120f`
- Sale yellow: `#efc63d`
- Red markup: `#7d1714`
- Soft blue: `#d8e7ee`
- Warm shadow: `rgba(45, 29, 16, 0.24)`

## Typography

- Handwritten labels: local `PatrickHand`, loaded from `assets/fonts/patrick-hand-latin.woff2`
- Small utility text: `Bahnschrift`

## Motion

- Minimal motion pass added after static timing approval.
- Scene transitions use only short incoming fade/blur/scale settles at `8.400s` and `16.400s`.
- Most cue text and WIT blocks should hard-show at the spoken word or phrase they support. Do not animate every block just because it appears.
- Keep impact animation for emphasized beats only: `$9`, `SOLD`, screw evidence, and final `FUTURE NOT INCLUDED`.
- Do not batch all blocks at the cue start. `$9`, `4 LEGS + 1 SEAT`, confidence, buy/calendar/fine labels, legal creak, screw/leg/career labels, true-cost, and final payoff should appear sequentially as the voice reaches them.
- Cue layers explicitly hide animated elements at cue start before animating them in, so delayed entrances do not appear early.
- If an off-edge WIT pose or delayed overlay leaks into the next cue, add a hard `tl.set(..., { opacity: 0 }, cueEnd)` cleanup at the cue boundary.
- Do not add decorative fly-outs before spoken ideas finish; cue removal stays timing-driven.
- The chair scene holds across the setup, parts, purchase, and first week.
- The broken-leg scene holds across legal creak, loose screw, and career-options leg.
- The cost scene holds across the true-cost receipt and final `FUTURE NOT INCLUDED` payoff.
- Keep cue count low for a short hook; current approved direction uses `7` cue states over `21.205s`.
- Red markup must point to the actual object it explains; no decorative rectangles or marks.
- WIT must be large enough for the facial emotion to read in Studio, direct preview screenshots, and exported MP4 frames when export is explicitly requested. Section 1 targets roughly `1/3` to `1/2` frame emotional reads when WIT appears.
- WIT placement should carry the emotion of the beat, not default to a lower corner. Good placements include giant lower-edge peeks, right/left edge half-body entrances, hiding behind foreground objects, and behind-label/tag framing, as long as text remains readable.
- Do not overuse WIT. For this `21.205s` section, keep WIT to `1-2` emotional beats per big scene; text, props, and markup should carry explanatory cues between WIT moments.
- Do not let WIT look accidentally broken: avoid cropped faces, cropped heads, and cropped shoulders unless the crop is an intentional edge-peek composition and the expression still reads clearly.
- If an animation creates a voice/visual mismatch, revert that animation before adding more motion.

## What Not To Do

- Do not draw WIT in HTML, CSS, or SVG.
- Do not use fake stick figures.
- Do not crowd boards with extra props.
- Do not make the hook feel like presentation slides.
- Do not follow the old visual plan for this remake.
