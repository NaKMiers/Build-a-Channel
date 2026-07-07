# Section 5 Render Implementation

Video:
`Why Countries Fight to Host the World Cup (and Lose Billions)`

Section:
`Section 5: The Three Drains`

Status: `built - awaiting owner review`

## Result

- Preview project: `previews/5-three-drains/`
- Source: `visual-plan/section-05-three-drains/section-05-three-drains-visual-plan.md` (built 1:1; render-side adjustments below)
- Port: `1005`
- Studio URL: `http://localhost:1005/#project/5-three-drains`
- Direct composition URL: `http://localhost:1005/api/projects/5-three-drains/preview/comp/index.html`
- Runtime: `55.851s`, 7 scenes (tracks 1-7), audio track 30
- Voiceover: `section-05-three-drains-david23-am_eric-0.81.mp3` (copied sibling)
- Visual plan: current vs voiceover and 04-visual-plan.md

## Voice Sync

All cues pinned to `voiceover/section-05-three-drains/section-05-word-timings.json` (173 words,
monotonic). Whisper mishearings do not affect timestamps (plan documents them: "any W money" =
NEW@11.88 etc.). Final scene end clamped to the real audio duration 55.851s (whisper's last word
overshoots to 57.04).

## Render-side adjustments vs the visual plan (documented decisions)

1. **5.1 base geometry**: `confetti-plaza-1.jpg` is an all-ground macro of a confetti-strewn street
   (no horizon). Built as a pure party-floor stage - grates slam onto the confetti, bubble in the
   clear asphalt upper area. Reads exactly as "the morning-after party floor".
2. **5.1 number tags**: bare white numbers were unreadable on confetti; built as dark circle chips
   with white numerals sitting ON each grate (readability rule).
3. **5.2 base**: sourced wallet is BLACK leather (manifest-accepted substitution vs "worn brown");
   graded brightness 1.35, all text moved onto the dark leather zone and `NEW money?` given
   white handwriting (black was invisible on the photo's white surround at the planned position).
4. **5.4 U-turn arrow**: built as a real U-turn path (in-line from right, half-circle loop,
   out-line + arrowhead exiting right) - the first dome-arc attempt read as a rainbow, not a turn.
5. **5.5 WIT position**: the pose rendered ~150px lower than the bbox math suggested; measured from
   the snapshot and re-anchored (top 560 -> 420) so head+shoulders sit under card B (chest crop).
6. **Mirrored assets** (wrapper flip on the inner img so GSAP tweens never touch scaleX(-1)):
   `worried_uneasy_wide_eyes` (5.4 - eyes must scan right), `banknote-flying-flock` (5.6 - flies
   right to Zurich), `banknote-walking-guest` x3 (5.7 - exits right).
7. **5.6 freeze beat**: the flock has NO tweens between 50.54-50.82 (the scripted [beat]) - it
   hangs mid-air, then swooshes past the ZURICH plank on its word. Hard kill on flock 2 at 51.96
   (lint gsap_exit_missing_hard_kill fix).
8. **5.7 `bye.`**: white handwriting fell on the bright window; built as the standard cream chip.

## Big Scene / Cue Plan Implemented

| Cue | Time | Voice cue | What happens | Motion |
|---:|---:|---|---|---|
| 5.1 | 0.00 | (cold open) | plaza + minister-WIT mid-shout | static |
| | 0.34/1.70 | wait/minister | bubble pops + line 1; `every tourism minister` tag | impact/hard-show |
| | 2.78/3.72 | fans/real | bubble lines 2-3 | hard-show |
| | 4.56/5.54/6.36 | True/come/spend | TRUE stamp; green checks on both claims | impact x3 |
| | 7.38 | boom | money pile drops + bounce + `the "boom"` tag | impact |
| | 8.68/8.98/9.24 | drains | three grates slam + numbered chips + dust | impact x3 |
| 5.2 | 9.44 | drain one | wallet + grate + `DRAIN 1:` + pile widget (70%) at cut | hard-show |
| | 10.24 | substitution | `SUBSTITUTION` stamps; 3 bills tip + slide into the bars | impact + slides |
| | 11.06/11.44 | locals/not | WIT professor; `NEW money?` | hard-show |
| | 11.88/13.94/14.60 | NEW/move/already | red X strokes; `moved money` stamp; underline scrub | impact/draw |
| 5.3 | 15.36 | The | cinema + 4 seated banknotes (set dressing) | static |
| | 15.52/16.82/17.86 | $100/match/100 | $100 chip pops; MATCH stub; chip slides + slams onto stub | pop/slam |
| | 19.28 | cinema | CINEMA stub + dashed slot + red -$100 | hard-show |
| | 20.14/20.94 | city/richer | CITY TOTAL gauge; needle wobbles, settles on `same` | wobble |
| | 21.88/22.16/22.54 | just/changed/seats | WIT smirk; bill hops two seats; `changed seats.` + arrow | arc boing |
| 5.4 | 23.36 | drain two | suitcases + grate + `DRAIN 2:` + pile (45%) | hard-show |
| | 24.10 | crowding | `CROWDING OUT` stamps + 2 bills slide | impact |
| | 24.98-26.20 | event/crowds/prices | BIG EVENT/CROWDS/PRICES rising cascade | impact x3 |
| | 27.86/29.60 | look/maybe | U-turn arrow draws; `maybe next year` luggage tag + swing | draw/pop |
| | 30.54/30.76 | locals/hide | WIT edge-peek + `locals` tag + arrow | hard-show |
| 5.5 | 31.94 | Right now | street + both shopfronts + spotlight LEFT | hard-show |
| | 32.72/34.32/35.00 | 2026/streets/record | 2026 stamp; card A; RECORD DAYS | impact |
| | 35.76 | while | spotlight slides right; left shop cools | slide |
| | 36.14/37.62/38.16 | shops/down/20% | card B; WIT dismay; `down ~20%` + shutter dust | impact |
| | 40.10/41.20 | spread/moves | verdict arc draws + line 1; bill rides arc + line 2 | draw/flight |
| 5.6 | 42.50 | drain three | stadium + grate + `DRAIN 3:` + pile (20%) | hard-show |
| | 43.32 | leakage | `LEAKAGE` stamps + 2 bills slide | impact |
| | 45.72-46.86 | tickets/food/sponsor | 3 item chips pop | pop x3 |
| | 47.94 | does | WIT panic GIANT | hard-show |
| | 49.68 | leaks | flock launches (mirrored), pile fades to 40% | flight |
| | 50.54-50.82 | [beat] | flock FREEZES mid-air (no tweens) | freeze |
| | 50.82/51.24 | mostly/Zurich | signpost slams; `ZURICH` stamps; flock swooshes off-frame | impact/exit |
| 5.7 | 51.98 | So | door + receipt strip + gray WIT at cut; quiet | static |
| | 52.16 | party | confetti bits drift off the step | drift |
| | 54.62 | leaves | 3 walking-guest bills march right; `bye.` chip | march |
| | 55.32 | guests | receipt gives one soft flap; hold to 55.851 | flap |

## Render Review-Prevention Pass

- voice cue map completed: yes (JSON timestamps, monotonic; end clamped)
- big-scene sanity: 7 persistent bases; 5.5 two-phase inside one base per plan
- cue density: 1-2 changes per beat; lists staggered per word
- motion density: hard-show default; impact reserved for stamps/slams/pops/payoffs
- WIT density: 1 pose per scene, no repeats, sides L/R/C/L/R/L/R per plan
- WIT crop/collision: minister knees-crop; 5.4 half-out edge peek intentional (expression reads);
  5.6 chips nudged clear of panic hands; 5.5 anchored by measurement; no face/prop crops
- markup targets: checks land on the claim lines; X on `NEW`; circles none; numbers on grates
- scene differentiation: 7 fresh bases, none reused in-section or cross-section
- HyperFrames mechanics: per-scene tracks 1-7, audio 30; deterministic GSAP; cue sets 0.02s+ off
  clip boundaries; allow-overflow + overflow:visible on off-canvas WIT/prop wrappers; no rotate+scale(0)
  inline transforms; no fromTo from-only properties
- decisions beyond plan: 8 documented above

## Verification

- lint: 0 errors, 9 warnings (intentional duplicate media for grate x3 + pile x4 + bill reuse;
  file-size advisory) - non-blocking
- validate: 0 errors, 0 warnings, 15 contrast advisories (validator measures text against the photo
  behind, ignoring solid chip/card backgrounds) - non-blocking
- inspect: 0 layout issues across 59 samples
- snapshot QA: 6 rounds, all 7 scenes at ~45 cue timestamps; defects found+fixed: 5.1 unreadable
  number tags + pile/number collision, 5.2 faint plate labels + white-on-white NEW money?, 5.4
  dome-arc U-turn rebuilt as a real U-turn path, 5.5 WIT too low, 5.6 chips at WIT's hand, 5.7
  bye. on the window + bill spacing/march distance
- export: none (not requested)

## Notes

- Preview server on port 1005 (sysctl unprivileged-port floor at 1000 in effect this boot).
- Suitcase base carries vintage hotel labels (Hotel Atlanta etc.) - period luggage decals, not
  modern brands; accepted per manifest sourcing notes.
