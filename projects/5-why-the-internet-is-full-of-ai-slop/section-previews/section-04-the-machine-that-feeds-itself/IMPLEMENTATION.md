# Section 4 Render Implementation

Video:
`Why The Internet Is Full Of Garbage Now`

Section:
`Section 4: The Machine That Feeds Itself`

Status:
`built, ready for review` (preview only; no MP4 export requested)

## Result

- Preview project: `section-previews/section-04-the-machine-that-feeds-itself/`
- Source: `visual-plan` S4 + REAL word timings (`voiceover/section-04-the-machine-that-feeds-itself/section-04-word-timings.json`)
- Port: `1004`
- Studio URL: `http://localhost:1004/#project/Build%20a%20Channel`
- Direct composition URL: `http://localhost:1004/api/projects/Build%20a%20Channel/preview/comp/index.html`
- Runtime: `52.971s` (root `data-duration`, matches the section voiceover)
- Voiceover: `section-04.mp3` (am_eric / David23 / 0.80), wired as `<audio data-track-index="30">`
- Visual plan: `visual-plan/section-04-the-machine-that-feeds-itself/section-04-the-machine-that-feeds-itself-visual-plan.md`
- Composition id: `Section04Machine`

## Word Timings (generated, not estimated)

The visual plan shipped with ESTIMATED times (no word-timings JSON). Per the Voice-Sync Timing
Contract, I GENERATED real word timings with the transformers.js / whisper-tiny.en recipe (ffmpeg
static -> 16 kHz mono f32 -> `gen-s04.mjs`) and pinned every `data-start` + GSAP reveal to actual word
starts. Output: `voiceover/section-04-the-machine-that-feeds-itself/section-04-word-timings.json`
(173 words; clean, monotonic; one harmless whisper duplication of "engagement just means clicks"
around 20-22s that does not affect the pinned cues; last word "floods." ends 53.84 in the transcript,
clamped to the real 52.971s audio).

## Big Scene / Cue Plan Implemented (9 scenes, one per beat, each its own track + crossfade)

| Scene | Start | Voice cue (word @ s) | Big scene | What changes | Motion | WIT | 
|---:|---:|---|---|---|---|---|
| 4.1 | 0.00 | "Follow the money" 3.12 | dark machine hall, engine in silhouette | FOLLOW THE MONEY 3.12, coin trail 3.52, "(slowly)" 3.88, "the whole engine ->" 5.22 | follow=smash, rest hard-show | `smug_sly_smirk_leaning` L, ~1150 |
| 4.2 | 5.84 | "step one" 6.04 | vintage film set + old-cost pile | STEP1+pile 6.04, EXPENSIVE 8.06, writer/camera/musician/time 9.28/9.90/10.42/11.12 | step=pop, EXPENSIVE=smash, list hard-show | `presenting_open_palm_talking` R, ~1120 |
| 4.3 | 11.18 | "a prompt" 12.06 | clean bright desk + prompt box | "now: a prompt+10s" 12.06, "cost dropping" 13.56, $0 14.86 | $0=smash, rest hard-show | `sly_scheming_twiddling_fingers` L, ~1050 |
| 4.4 | 15.18 | "step two" 15.38 | casino floor + engagement slot machine | STEP2 15.38, struck "NOT...GOOD" 17.80, PAID for ENGAGEMENT 19.06, clicks/likes/time 21.48/22.16/22.64 | step+chips=pop, ENGAGEMENT=smash | `boss_suit_sunglasses_sparkle` R, ~980 |
| 4.5 | 23.42 | "attention" 24.02 | dark spotlight stage + balance scale | ATTENTION, 24.02, "not quality." 24.74 | ATTENTION=smash | `lecturing_finger_raised_eyes_closed` CL, ~900 |
| 4.6 | 25.66 | "step 3" 25.86 | wall of CRT screens + cannon | STEP3 25.86, struck "1 great thing" 27.64, FLOOD THE ZONE+cannon+barrage 29.92, "post 1,000" 30.90, VIRAL 33.00 | flood=smash, viral=pop | `manic_gleeful_googly_eyes` CR, ~1080 |
| 4.7 | 33.68 | "step 4" 33.88 | mission-control wall + blindfold robot | STEP4 33.88, "algorithm is BLIND" 36.66, CAN'T TELL 37.66, 2x SERVED 39.02/39.30 | stamps=smash | `annoyed_disgusted_open_frown` R, ~1030 |
| 4.8 | 40.38 | "step 5" 40.58 | machine hall LIT + engine roaring (callback) | STEP5 40.58, "slop -> money" 41.84, "-> MORE slop" 43.50, THE MACHINE FEEDS ITSELF 44.64 | payoff=smash | `shocked_sweating_dismayed` R, ~940 |
| 4.9 | 46.60 | "whole engine" 47.52 | lit engine + sludge overflow (S1-2 flood callback) | THE WHOLE ENGINE 47.52, 3 verdict stamps 48.04/48.86/49.98, "of course it floods." + sludge 51.86 | stamps=smash | `deadpan_unimpressed_half_lidded` CL, ~1050 |

Continuity device: a **loop-ring HUD** (top-right, `#hud`, own track) lights one node per Step
(6.04 / 15.38 / 25.86 / 33.88 / 40.58) and shows a green check on "the machine feeds itself" (44.64).

Section motif: **THE SELF-FEEDING ENGINE** (`slop-engine-loop.png`) - dormant/silhouette at 4.1,
lit + roaring at 4.8 (loop closes), labeled "THE WHOLE ENGINE" at 4.9. `dark-machine-hall-1.jpg` is
the shared motif base (graded dark at 4.1, lit-warm at 4.8/4.9).

## Render Review-Prevention Pass

- voice cue map completed: yes (built from generated word-timings JSON)
- big-scene sanity checked: yes (one persistent big scene per beat; engine motif recurs as a callback, not a crutch)
- cue density checked: yes (each cue adds 1-2 meaningful changes)
- motion density checked: yes (ordinary labels + list items hard-show; impact reserved for STEP pops, $0, ATTENTION, FLOOD THE ZONE, the payoff, SERVED + verdict stamps)
- WIT density: 1 giant WIT per scene, varied pose + side (L/R/L/R/CL/CR/R/R/CL), all ~1/3-1/2 frame
- WIT crop/collision checked: yes - faces/heads/glasses intact, legs-only crops; text placed opposite WIT; no text covers WIT face
- markup target checked: SERVED stamps land on the robot's two belt boxes; CAN'T TELL on the readout; no decorative marks
- scene differentiation checked: yes - 7 distinct fresh photo bases + the deliberate engine-hall callback
- HyperFrames mechanics checked: each scene own track, crossfade fadeIn, deterministic GSAP, audio clip, synchronous timeline registration

## Render decisions beyond the visual plan

- Generated real word-timings and re-pinned all cues (plan times were estimated).
- Scene 4.4 text was rebalanced (PAID for ENGAGEMENT reduced 120->74px, moved left of the boss WIT) to stop right-edge overflow / WIT-face collision; chips placed in a clear row above the slot machine.
- Scene 4.3 `clean-bright-desk-1.jpg` carries an incidental **DELL** bezel logo (manifest-flagged). It can't be cropped out (laptop is central), so it is covered with a small black bezel-matching CSS patch (z-index 3). Documented per the All Assets / brand-safety rules.
- Loop-ring HUD continuity device implemented as a full-composition overlay (the plan called for it; kept small, top-right, away from STEP chips/labels).
- Owner review fix (2026-06-30): at 0:44 the 4.8 "slop -> money" / "-> MORE slop" labels were white text on the white WIT mascot (vague). Rebuilt as dark gold-bordered `.flowchip` loop-flow chips in the top-center band, clear of WIT's face.

## Assets

- Shared asset folder: `projects/5-why-the-internet-is-full-of-ai-slop/assets/`
- Section assets: local `assets` junction -> `../../assets` (verified resolves; font + poses + heroes + bases all present)
- Generated heroes used (8): `slop-engine-loop`, `money-trail-coins`, `old-creation-cost-pile`, `prompt-box-instant`, `engagement-slot-machine`, `attention-quality-scale`, `flood-the-zone-cannon`, `blindfold-sorter-robot`
- Photo bases used (7): `dark-machine-hall-1`, `vintage-film-set-1`, `clean-bright-desk-1`, `casino-slot-machines-1`, `dark-spotlight-stage-1`, `wall-of-screens-grid-1`, `cctv-control-room-1`
- Cross-section reuse: `slop-clone.png` (from S3) tiled 6x as the flood-the-zone barrage
- Poses (9 distinct): see the table above
- Attribution: `assets/ATTRIBUTION.md`

## Verification

- lint: `0 error(s), 2 warning(s)` - both `duplicate_media_discovery_risk` (engine reused 3x as the motif; slop-clone tiled 6x as the barrage). Intentional reuse; non-blocking.
- validate: `0 error(s), 0 warning(s)` (150 WCAG contrast advisories on stylized emphasis text over photos; mitigated by heavy text-shadow + side scrims; read fine in snapshots - same class as S1-S3)
- inspect: `0 layout issues across 15 sample(s)`
- direct preview screenshots/contact sheet: 18-frame contact sheet QA + targeted re-snaps of scenes 3/4/9 after fixes
- export/render: not requested (preview only)

## Notes

- No MP4/WebM exported (not requested).
- Word-timings file is the source of truth; if S4 script wording changes, regenerate timings and re-pin.
