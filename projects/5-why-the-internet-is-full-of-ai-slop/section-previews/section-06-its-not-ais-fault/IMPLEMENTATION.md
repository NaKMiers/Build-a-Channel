# Section 6 Render Implementation

Video:
`Why The Internet Is Full Of Garbage Now`

Section:
`Section 6: It's Not AI's Fault (And Not A Plot)`

Status:
`built, ready for review` (preview only; no MP4 export requested)

## Result

- Preview project: `section-previews/section-06-its-not-ais-fault/`
- Source: `visual-plan` S6 + REAL word timings (`voiceover/section-06-its-not-ais-fault/section-06-word-timings.json`)
- Port: `1006`
- Studio URL: `http://localhost:1006/#project/Build%20a%20Channel`
- Direct composition URL: `http://localhost:1006/api/projects/Build%20a%20Channel/preview/comp/index.html`
- Runtime: `38.933s` (root `data-duration`, matches the section voiceover)
- Voiceover: `section-06.mp3` (am_eric / David23 / 0.80), wired as `<audio data-track-index="30">`
- Visual plan: `visual-plan/section-06-its-not-ais-fault/section-06-its-not-ais-fault-visual-plan.md`
- Composition id: `Section06NotFault`

## Word Timings (generated, not estimated)

The visual plan shipped with ESTIMATED times (no word-timings JSON). Per the Voice-Sync Timing
Contract, I GENERATED real word timings with the transformers.js / whisper-tiny.en recipe (ffmpeg
static -> 16 kHz mono f32 -> gen script) and pinned every `data-start` + GSAP reveal to actual word
starts. Output: `voiceover/section-06-its-not-ais-fault/section-06-word-timings.json` (123 words; clean,
monotonic; last word "incentive." has a whisper tail-glitch end of `47.96` while its start `38.32` is
correct, so the root duration is clamped to the real `38.933s` audio and the final cue is pinned to
`38.32`).

## Big Scene / Cue Plan Implemented (7 scenes, one per beat, each its own track + crossfade)

| Scene | Start | Voice cue (word @ s) | Big scene | What changes | Motion | WIT |
|---:|---:|---|---|---|---|---|
| 6.1 | 0.00 | "fair" 0.82 | courtroom + level balance scale | "let's be fair." 0.82, "(this gets interesting)" aside 3.30 | fair=smash, aside hard-show | `hand_on_cheek_pondering_eyes_closed` L, ~1120 |
| 6.2 | 4.10 | "Not all AI...slop" 4.32 | clinic scan room + scan screen (AI helper) + artist easel | doctor "NOT SLOP" check 8.72, easel + artist "NOT SLOP" check 10.86 | checks=smash, easel=pop | `doctor_coat_stethoscope_listening` C, ~1060 |
| 6.3 | 11.55 | "low effort" 12.32 | workbench tools (the innocent tool) | "SLOP = LOW EFFORT" 12.32, "x HIGH VOLUME" 13.20, "not about the tool." 14.42 | formula=smash, HV=pop, tool hard-show | `pointing_up_curious_open_mouth` R, ~1080 |
| 6.4 | 15.30 | "Dead Internet Theory" 20.44 | S2 conspiracy corkboard (callback) + tinfoil hat | tinfoil hat 16.98, "DEAD INTERNET THEORY" 20.44, "govt bots -> control your mind" note 24.50 | title=smash, hat=pop, note hard-show | `pondering_skeptical_hand_on_chin` L, ~1080 |
| 6.5 | 26.60 | "Relax." 26.76 | corkboard darkened + giant red X | "Relax." 26.76, red X + "it's dumber than that." 27.60 | X=smash, line=smash | `unimpressed_smirk_closeup` L, ~1040 |
| 6.6 | 28.60 | "Nobody is in charge" 28.70 | empty boardroom + empty villain throne + unpressed button | "NOBODY IS IN CHARGE" 28.70, "no villain pressed a button" 30.08, glowing $ + "the money rewards it." 33.52 | charge/villain/$=smash, money hard-show | `shrug_both_hands_up_smile` L, ~1060 |
| 6.7 | 34.55 | "uncomfortable part" 35.68 | dark stage + gold $ shrugging off handcuffs (callback base S4.5) | "the uncomfortable part..." 35.68, "YOU CANNOT" 36.78, "ARREST" 37.38, "AN INCENTIVE." 38.32 | payoff lines=smash (slower) | `proud_explaining_hand_on_chest_hand_on_hip` L, ~1020 |

Tone device: this is the **fair/calm turn** - bright-but-neutral bases, level balance scale, two green
`NOT SLOP` checks, a clean formula, then the conspiracy is NAMED (DEAD INTERNET THEORY corkboard) and
PUNCTURED (giant red X + "it's dumber than that."), landing on the real cause (no villain, the money
rewards it) and the dry closer "YOU CANNOT ARREST AN INCENTIVE."

## Render Review-Prevention Pass

- voice cue map completed: yes (built from generated word-timings JSON)
- big-scene sanity checked: yes (one persistent big scene per beat; the corkboard recurs 6.4->6.5 as the conspiracy callback)
- cue density checked: yes (each cue adds 1-2 meaningful changes)
- motion density checked: yes (ordinary labels + the formula tail / money line hard-show; impact reserved for "fair", the NOT SLOP checks, the formula, the conspiracy title, the red X, NOBODY IS IN CHARGE / NO VILLAIN / $, and the payoff lines)
- WIT density: 1 giant WIT per scene, varied pose + side (L/C/R/L/L/L/L); poses carry the fair->skeptical->deadpan->shrug->calm arc
- WIT crop/collision checked: yes - faces/heads/glasses intact, legs-only crops; fixed three collisions found in QA (see below)
- markup target checked: red X crosses the conspiracy board (not WIT's face); green checks sit by the doctor scan / artist easel; pinnote pinned on the corkboard
- scene differentiation checked: yes - 4 fresh photo bases (courtroom / clinic / workbench / boardroom) + 2 reuse bases (corkboard S2, dark stage S4.5)
- HyperFrames mechanics checked: each scene own track, crossfade fadeIn, deterministic GSAP, audio clip, synchronous timeline registration

## Render decisions beyond the visual plan

- Generated real word-timings and pinned all cues (plan times were estimated); clamped the whisper tail "incentive." (47.96) to the real `38.933s` audio.
- **Checkerboard-keyout fix (3 generate props):** `artist-easel.png`, `empty-villain-throne.png`, and `uncuffable-incentive.png` were delivered as OPAQUE RGB with a baked transparency-checkerboard (alpha extrema 255,255), while `tinfoil-hat.png` was real RGBA. Keyed the checkerboard out to true alpha (same S5 method: tone-mask `mn>=200 & (mx-mn)<=28` -> scipy connected components -> keep only border-touching components -> 1px dilation). Interior whites (the easel canvas, the coin's glow halo + sparkles) are non-border components and survive. Originals backed up to `assets/_raw-checkerboard/`. Verified clean over a gray background.
- **Three WIT-collision fixes after first snapshot QA:** (6.5) the giant red X was centered over WIT's deadpan face - moved the X right (`left:58%`) onto the board and WIT to `left:-200px` so the deadpan expression (the joke) reads; (6.6) "the money rewards it." sat on WIT's white body and near the subtitle edge - moved to the dark boardroom floor center (`left:600px; bottom:120px`); (6.7) the 3 payoff lines overlapped WIT's face on the left - shifted to `left:560px` and WIT to `left:-320px`, coin nudged to `right:200px; top:130px`.
- The CSS "argument graphics" (balance scale, NOT SLOP checks, scan screen + AI badge, formula card, DEAD INTERNET THEORY title, pinned bots note, big red X, glowing $) are render-built per the plan; this section deliberately leans on real bases + CSS over generated heroes.

## Assets

- Shared asset folder: `projects/5-why-the-internet-is-full-of-ai-slop/assets/`
- Section assets: local `assets` junction -> `../../assets` (verified resolves; font + poses + props + bases all present)
- Generate props used (4): `artist-easel`, `tinfoil-hat`, `empty-villain-throne`, `uncuffable-incentive`
- Photo bases used (4 fresh): `courtroom-1` (6.1), `clinic-scan-room-1` (6.2), `workbench-tools-1` (6.3), `empty-boardroom-1` (6.6)
- Cross-section reuse: `corkboard-redstring-1` (S2 conspiracy board) -> 6.4 + 6.5; `dark-spotlight-stage-1` (S4.5) -> 6.7
- Poses (7 distinct): see the table above
- Attribution: `assets/ATTRIBUTION.md`

## Verification

- lint: `0 error(s), 1 warning(s)` - `duplicate_media_discovery_risk` (`corkboard-redstring-1.jpg` reused 6.4/6.5; same board, crossed out). Intentional reuse; non-blocking.
- validate: `0 error(s), 0 warning(s)` (20 WCAG contrast advisories - the validator measures stylized text against the photo behind, ignoring each device card's own opaque background; the AI badge / green check / pinnote / handwritten tool label all read fine in snapshots - same class as S1-S5)
- inspect: `0 layout issues across 14 sample(s)`
- direct preview snapshots: 12-frame pass across all 7 scenes + targeted re-snaps of 6.5 / 6.6 / 6.7 after the three WIT-collision fixes
- export/render: not requested (preview only)

## Notes

- No MP4/WebM exported (not requested).
- Word-timings file is the source of truth; if S6 script wording changes, regenerate timings and re-pin.
- Checkerboard-keyout originals are kept in `assets/_raw-checkerboard/` in case a re-key is needed.
