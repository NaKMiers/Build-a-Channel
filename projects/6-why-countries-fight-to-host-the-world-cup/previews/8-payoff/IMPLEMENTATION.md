# Section 8 Render Implementation

Video:
`Why Countries Fight to Host the World Cup (and Lose Billions)`

Section:
`Section 8: Payoff: Check The Receipt`

Status: `built - awaiting owner review`

## Result

- Preview project: `previews/8-payoff/`
- Source: `visual-plan/section-08-payoff/section-08-payoff-visual-plan.md` (built 1:1 with documented adaptations)
- Port: `1008`
- Studio URL: `http://localhost:1008/#project/8-payoff`
- Direct composition URL: `http://localhost:1008/api/projects/8-payoff/preview/comp/index.html`
- Runtime: `39.573s`, 6 scenes, composition `Section08Payoff`
- Voiceover: `./section-08-payoff.mp3` (copy of the approved David23/am_eric 0.81 take)
- Visual plan: current (2026-07-02 word timings; every plan-pinned cue time matched the JSON exactly)

## Voice Sync

Every `data-start` and GSAP reveal pinned to `section-08-word-timings.json`. Timings are
monotonic (no chunk-seam reorder this section); the only anomaly is the known long tail -
"receipt." token ends 42.30, so scene 8.6 is clamped to the real audio duration 39.573
and the final nod/tick land at receipt@39.20. Hide-sets nudged 0.02-0.16s after clip
starts. Scene cuts: 9.82 / 14.76 / 20.22 / 26.46 / 34.34, each scene clip on its own track.

## Render decisions beyond the plan

- Christmas-mantel neutralized by cropping into the stone chimney breast + hard grey-blue
  grade + corner shade over the figurine sliver; trophy stands on a CSS floating shelf
  because the photo's real shelf sits too high in any full-bleed crop (both 8.1 and 8.6).
- 8.2 adapted to the real photo geometry: chair is at the right edge, so WIT peeks from
  the LEFT (mirrored `skeptical_side_eye_doubtful`), and the receipt lands ON the empty
  chair seat (funnier + ties to the OUT OF OFFICE stamp; plan's desk landing had no desk
  space at that x). Stamp given a translucent cream backing (red-on-black chair fails).
- 8.3 `wit-selfie-stick-calm` mirrored (drawn stick-up-left; plan wants up-right); the
  correction block is a cream chip (white handwriting on pale sky fails the chip rule);
  camera caption = two hard-show lines after the clip-path type-on clipped centered text
  mid-word in snapshot QA.
- 8.4 has no counting machine in the sourced base (euro notes substitution per manifest);
  tally card + green arrow + white `MONEY -> FIFA` chip carry the beat; arrow shortened in
  layout so the head stops 40px clear of WIT's face.
- 8.5 thesis frame: all must-read receipt text on a self-carried white panel that the
  asset strip visually feeds into (receipt paper too thin to carry text - S6 lesson);
  items split into name row + dotted-leader price row so 30px courier fits the panel.

## Motion classification

- Static: bases, WIT poses (except 8.6 nod), trophy, shelf, receipt initial states,
  marker, ghost lines.
- Hard-show: question line, price card, jar+label, planner label+arrow, correction line 1,
  NEVER line, caption lines, tally card, sub-line, item 1, item 2, NAME line, arrow label.
- Impact (calm budget): red cross-stroke, OUT OF OFFICE stamp, strike, sticker slap,
  shutter blink, FIFA arrow sweep, 8.6 question pop, NAME red-circle pop, tally pops.
- Motion: receipt sway loop (finite yoyo x6), tag soft-drops, receipt slide+flop (8.2),
  screen wake fade, panel judders (printer ticks), scrawl write-on (clip-path 1.5s),
  marker nudge, two WIT nods (wrapper rotation), balloon bob.
- WIT: exactly 1 per scene (6 total); sides L / L-edge / CL / R / BL / R; giant (~1/2
  frame) in 8.1, 8.3, 8.6; intentional edge peeks in 8.2 / 8.5 and a 2/5-frame closeup in
  8.4 where the evidence is the star. Two NEW poses used (selfie stick, resigned nod).

## Snapshot QA defects found and fixed

1. Tag texts rendered near the string knot and tag 3 (CENTER OF THE WORLD) ran off the
   right edge - text anchored to the tag face (top 150), tags re-spaced 1400/1560/1688.
2. Red Christmas-bow sliver at the right frame edge + garland fronds at top - base window
   shifted (origin 49.4%/21% -> 47%/26%).
3. 8.2 receipt roll edge visible at the right frame edge before its cue - hide offset
   x:860 -> x:1060.
4. 8.3 camera caption type-on clipped centered two-line text mid-word ("worlc/expensi") -
   replaced with two word-timed hard-show lines (18.54 / 19.10).
5. 8.6 question block overlapped the trophy + receipt roll - left shelf assembly moved
   down 130px, question tightened (font 100, top 108); verified 20px clearance.

## Verification

- lint: 0 errors, 3 warnings (intentional motif reuse: receipt x4, trophy x3, mantel base
  x2 - `duplicate_media_discovery_risk`, documented)
- validate: 0 errors, 0 warnings, 50 contrast advisories (known false-positive class:
  text measured against the photo behind, ignoring the card/chip's own opaque background)
- inspect: 0 layout issues (23 samples)
- snapshot QA: 35-frame full cue sweep + 10-frame re-snap after fixes; every cue state
  readable, WIT face clear of text/props in all six scenes, cue-critical text above the
  subtitle zone (lowest: tag texts ~885, scrawl ~876)
- export: none (not requested)

## Assets

- Shared folder via `assets` symlink -> `../../assets` (serves fine on this Linux box)
- All 18 referenced assets pre-made by visual-implement and verified on disk; alpha
  extrema check: all real RGBA (no baked checkerboard); content bboxes measured before
  layout (receipt 37%w, balloon 33%w, poses 34-70%w); every pose PNG viewed before use
- No new assets derived this run; attribution unchanged (`assets/ATTRIBUTION.md`)
