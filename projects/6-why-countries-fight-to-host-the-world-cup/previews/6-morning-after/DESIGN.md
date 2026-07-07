# Section 6 - The Morning After - Design

Video: `Why Countries Fight to Host the World Cup (and Lose Billions)`
Composition: `Section06MorningAfter` - 1920x1080, `61.44s`, port `1006`.

## Structure (8 scenes, 1:1 from the section visual plan)

| Scene | Time | Base | Idea |
|---|---|---|---|
| 6.1 | 0.00-4.26 | `stadium-empty-seats-dawn-1.jpg` (cool grade) | comedown: drooping pennants, paper planes fly home, `STILL HERE.` stamp, yawning WIT left |
| 6.2 | 4.26-12.36 | `grass-field-morning-1.jpg` | HERO: elephant-stadium pet pops in, dictionary card glosses "white elephant" row by row, giant party-hat WIT pours coins into the `MAINTENANCE` bowl |
| 6.3 | 12.36-20.50 | `stadium-modern-exterior-1.jpg` | Brasilia: hanging `AT LEAST $550,000,000` tag, sparkle glints, `ENORMOUS` tape, `ONE PROBLEM` stamp + crossed-out ball |
| 6.4 | 20.50-29.00 | `stadium-parking-lot-1.jpg` | `back in 2015` stamp, 3 bus rows slide in (one file x3), scripted freeze 26.46-27.48, `FINALLY FULL` / `...of buses.`, deadpan WIT closeup |
| 6.5 | 29.00-40.42 | `rainforest-aerial-1.jpg` | two-phase: tiny stadium drops into jungle + tag + note + odometer counter; then 44,000-seat map board slides up, WIT + magnifier, lens inset finds 12 red fans, green private row |
| 6.6 | 40.42-48.00 | `pitch-center-circle-1.jpg` + CSS center circle/spot | booking chips, cake drops on the center spot, pink icing `Happy birthday, Enzo`, OK-sign WIT, `great venue.` |
| 6.7 | 48.00-53.80 | `kitchen-bright-1.jpg` | fridge + `FEEDING SCHEDULE` card (red Cape Town entry in 3 strokes), reused bowl, receipt motif prints `1x WHITE ELEPHANT ... $???` |
| 6.8 | 53.80-61.44 | `concert-stage-lights-1.jpg` + CSS beams | `TO BE FAIR...` banner, recovery line, mic glint, 2014-2024 timeline, `"only" ten years`, `2024: Bruno Mars` star tag, confetti at 60.86 |

## Key render-side decisions (documented per skill rules)

- `pitch-center-circle-1.jpg` has no real center circle (manifest note) - the white
  center circle + spot are drawn in CSS under the cake.
- `concert-stage-lights-1.jpg` is a single hue-shifted beam head - three CSS beam
  shafts were added so "big concerts" reads; they flare on concerts@57.62.
- The corrupt whisper timestamp for the final "Mars." (backward jump to 52.24) is
  bypassed per the plan: star+tag pinned to Bruno@60.60, confetti at Bruno's end
  60.86, scene clamped to the real audio duration 61.44.
- The 6.5 magnifier read-through is a white lens inset (z above WIT) aligned to the
  pose's glass; the red fan cluster sits under it on the seat map.
- The 6.7 receipt gag line sits on a self-carried white mono chip (the receipt strip
  content is only ~37% of its canvas width - too thin to carry cue text).
- Bus rows / bowl / receipt reuse single files by design (motif rule); the
  `duplicate_media_discovery_risk` lint warnings are intentional and documented.

## Timing

All `data-start` values and every GSAP reveal are pinned to
`voiceover/section-06-morning-after/section-06-word-timings.json`. Scripted freeze
(the "Full of buses" beat of air) is 26.46-27.48: no tweens in that window. Hide-sets
are nudged 0.02-0.04s after clip starts (validator boundary rule).
