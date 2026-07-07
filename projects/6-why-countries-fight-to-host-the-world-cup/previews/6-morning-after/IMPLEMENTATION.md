# Section 6 Render Implementation

Video:
`Why Countries Fight to Host the World Cup (and Lose Billions)`

Section:
`Section 6: The Morning After`

Status: `built - awaiting owner review`

## Result

- Preview project: `previews/6-morning-after/`
- Source: `visual-plan/section-06-morning-after/section-06-morning-after-visual-plan.md` (built 1:1)
- Port: `1006`
- Studio URL: `http://localhost:1006/#project/6-morning-after`
- Direct composition URL: `http://localhost:1006/api/projects/6-morning-after/preview/comp/index.html`
- Runtime: `61.44s`, 8 scenes (6.5 is the planned two-phase scene), composition `Section06MorningAfter`
- Voiceover: `./section-06-morning-after.mp3` (copy of the approved David23/am_eric 0.81 take)
- Visual plan: current (2026-07-02 word timings; plan cue times matched the JSON exactly)

## Voice Sync

Every `data-start` and GSAP reveal pinned to `section-06-word-timings.json`. Scripted
freeze 26.46-27.48 (the "Full of buses" beat) has no tweens. The corrupt final "Mars."
timestamp (backward jump to 52.24) is bypassed per the plan: star+tag on Bruno@60.60,
confetti at Bruno's end 60.86, scene clamped to 61.44. Hide-sets nudged 0.02-0.04s
after clip starts.

## Render decisions beyond the plan

- 6.6 center circle + spot drawn in CSS (manifest note: the sourced pitch photo has no
  center circle).
- 6.8 three CSS beam shafts added over the single-light stage photo; they flare on
  concerts@57.62 and again at the confetti pop.
- 6.5 lens read-through built as a white zoom inset aligned to the pose's magnifier
  glass (moved off WIT's face after snapshot QA); red fan cluster sits under it.
- 6.7 receipt gag line on a self-carried white mono chip (receipt PNG paper is ~37% of
  canvas width - too thin for cue text); red `???` is a separate handwritten span.
- 6.3 "no big football club" upgraded from bare white handwriting to a cream chip +
  larger crossed-out CSS ball (bare text was unreadable on the bright sky).
- 6.2 elephant re-grounded (+100px) after snapshot QA showed it floating above the
  grass band.
- 6.8 timeline year labels moved inside the clip-wiped container box (clip-path on the
  container was cutting the protruding "2014" label to "014").

## Motion classification

- Hard-show: card header + gloss rows (6.2), WIT entrances, tag/number (6.3), chips +
  survive note (6.6), schedule strokes 1-2 (6.7), banner + recover line (6.8), planes.
- Impact: STILL HERE stamp, elephant pop + dust, red FEEDING row + coin arc, ONE
  PROBLEM stamp, sparkle glints, date stamp, bus-row slides + airbrake squash,
  FINALLY FULL, ...of buses., tiny-stadium drop + leaf puff, counter lock, board
  slide-up, lens pop, private-row line, cake drop, `- 10 years` stroke, receipt print
  jolt, `???`, `"only" ten years`, star+tag, confetti.
- WIT: exactly 1 appearance per scene (8 total), varied side L-R-L-C-R-L-R-C and pose
  per plan; giant (~1/2 frame) on 6.2 / 6.7 / 6.8.

## Verification

- lint: 0 errors, 12 warnings (intentional: bus row file x3 + bowl reuse
  `duplicate_media_discovery_risk`; helper micro-sequence `overlapping_gsap_tweens`
  with `overwrite:"auto"`; file-size advisory)
- validate: 0 errors, 0 warnings, 35 contrast advisories (known false-positive class:
  text measured against the photo behind, ignoring the card's own opaque background)
- inspect: 0 layout issues (20 samples)
- snapshot QA: 43-frame contact sheets + 11-frame re-snap after fixes; all cue states
  verified readable, WIT face clear of text/props in every scene
- export: none (not requested)

## Assets

- Shared folder via `assets` symlink -> `../../assets` (HTTP 200 verified)
- All 25 referenced assets pre-made by visual-implement; alpha-extrema check: all real
  RGBA (no baked checkerboard this section); content bboxes measured before layout
- Attribution: `assets/ATTRIBUTION.md` (unchanged; no new sourcing this run)
