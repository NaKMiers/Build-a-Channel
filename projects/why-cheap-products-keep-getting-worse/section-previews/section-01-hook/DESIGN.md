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
- Element entrances are short fade/fly-ins, usually `0.18-0.34s`, and never change the semantic cue start.
- Cue layers explicitly hide animated elements at cue start before animating them in, so delayed entrances do not appear early.
- Do not add decorative fly-outs before spoken ideas finish; cue removal stays timing-driven.
- The chair scene holds across the setup, parts, purchase, and first week.
- The broken-leg scene holds across legal creak, loose screw, and career-options leg.
- The cost scene holds across the true-cost receipt and final `FUTURE NOT INCLUDED` payoff.
- Keep cue count low for a short hook; current approved direction uses `7` cue states over `21.205s`.
- Red markup must point to the actual object it explains; no decorative rectangles or marks.
- WIT must be large enough for the facial emotion to read in Studio and exported MP4 frames.
- If an animation creates a voice/visual mismatch, revert that animation before adding more motion.

## What Not To Do

- Do not draw WIT in HTML, CSS, or SVG.
- Do not use fake stick figures.
- Do not crowd boards with extra props.
- Do not make the hook feel like presentation slides.
- Do not follow the old visual plan for this remake.
