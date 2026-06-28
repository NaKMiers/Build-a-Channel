# Section 1 Hook - Design

Composition: `Section01Hook` (1920x1080, 31.253s). Audio: `section-01-hook.mp3` (am_eric / 0.80).

## Look
- Channel board style: real bright photo base per scene + giant keyed WIT mascot on top + handwritten labels.
- WIT varied per scene (side/scale/pose); faces uncropped; legs-only crop.
- Idea-devices vary: handwritten label, big question, green stamp, phone "post" card, real-UI news/band cards, big kinetic word + staccato chips.
- Recurring motif: grey-sludge flood (born S8, settles S9); Shrimp Jesus reused S5 -> S8.
- Bright bases (light edge vignette only; no heavy dark scrim). Red markup reserved for the "DIDN'T HAPPEN" tell.

## Timing
All reveals pinned to real word timings (`../../voiceover/section-01-hook/section-01-word-timings.json`).
Ordinary labels hard-show on the spoken word; reveals/emphasis use smash/pop.

## Fonts
Local `PatrickHandLocal` (`assets/fonts/patrick-hand-latin.woff2`) for handwritten labels; Segoe UI for UI/big words.

## Assets
Shared library via `./assets` junction. WIT poses are transparent cutouts in `assets/poses/` (the shared pose library is pre-keyed transparent).
