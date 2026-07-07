# Section 3 Render Implementation

Video:
`Why Countries Fight to Host the World Cup (and Lose Billions)`

Section:
`Section 3: The Promise Machine`

Status: `built - awaiting owner review`

## Result

- Preview project: `previews/3-promise-machine/`
- Source: `previews/3-promise-machine/index.html` (composition `Section03PromiseMachine`)
- Port: `1003`
- Studio URL: `http://localhost:1003/#project/3-promise-machine`
- Direct composition URL: `http://localhost:1003/api/projects/3-promise-machine/preview/comp/index.html`
- Runtime: `60.779s` (end clamped to real audio; the timings JSON's final token "problem." has a corrupted backward timestamp, as documented in the visual plan)
- Voiceover: `section-03-promise-machine.mp3` (copy of `voiceover/section-03-promise-machine/scratch-audio/section-03-promise-machine-david23-am_eric-0.81.mp3`)
- Visual plan: `visual-plan/section-03-promise-machine/section-03-promise-machine-visual-plan.md` (followed 1:1; render-side adjustments below)

## Render Review-Prevention Pass

- voice cue map completed: yes, from `section-03-word-timings.json`; all 8 scene cuts + ~40 cues pinned to word starts; scene boundaries 5.82 / 13.82 / 21.10 / 30.20 / 38.58 / 42.08 / 51.30
- big-scene sanity checked: 8 persistent scenes, one main idea each; longest base hold 9.5s
- cue density checked: matches the plan's show-as-you-say lists; nothing moves during both [slower] echo beats (3.5 restamp excepted per plan; 3.7 fully frozen)
- motion density checked: ordinary labels/tabs/chips hard-show; impact reserved for stamps, the pop, the X, coin drops, and payoff text
- WIT density: exactly 1 WIT per scene (8 total, incl. the NEW hypnotized-numbers pose - the section money shot)
- WIT crop/collision checked: all crops intentional (knees/waist/chest/legs-only); no face/head/shoulder cuts; pin moved OFF WIT's face (was resting on his glasses in QA round 1); no text over WIT faces; verified across 3 snapshot rounds
- markup target checked: `EVERY YEAR` stamps the teal balloon; `PER TOURIST` stamps the tag lower edge (echo separated below, no stacked text); red circle rings the `ADVERTISEMENTS.` stamp exactly; X covers the sticky note
- scene differentiation checked: 8 fresh bases, none reused within the section or from S1/S2 (the 3.6 warm bokeh backdrop is a graded reuse of the S1 `gold-bokeh-black-1.jpg` file per the manifest's documented mailbox fallback - different section, different grade)
- HyperFrames mechanics checked: per-scene clips on own tracks (1-8), audio track 30, deterministic GSAP registered synchronously, off-canvas WIT with allow-overflow + `overflow:visible`
- render decisions made beyond visual plan:
  1. 3.1 receipt line: the receipt PNG's paper is only ~37% of its canvas width, so the printed strip cannot carry readable text. The strip prints from the slot (motif intact) and the line item `1x OPTIMISM (CONSULTING) ... $2,000,000` types onto a white receipt-excerpt chip beside the slot. The plan's "crank turns one rotation" is approximated by a gentle machine rock (crank is baked into the PNG).
  2. 3.3 balloon-to-document strings dropped: static string lines crossed WIT and pointed at nothing during inflation scaling; the balloons' own PNG strings + the document at bottom carry the linkage.
  3. 3.7 WIT placement: the turnstile photo has no barrier at frame center, so the plan's "waist-cropped behind the turnstile bar" read as a floating half-body in QA. WIT stands at frame right, legs cropped by the frame bottom, looking down at the coins; money cluster (coins, ghost note, bracket) moved center-right to sit under his gaze.
  4. 3.8 deflated balloons: `balloon-deflated-grey.png` is a hanging-format asset (tall narrow content), rotated ~±95deg to lie in the confetti.
  5. 3.4 window band: airline tails in `airport-arrivals-1.jpg` obscured with a soft white-blue haze overlay (backdrop-filter is unreliable in the capture path).

## Verification

- lint: 0 errors, 4 warnings - 2x `duplicate_media_discovery_risk` (intentional reuse: `coin-gold-one.png` double-drop in-scene, balloons across 3.3/3.4, deflated balloon x2) + 2x `overlapping_gsap_tweens` on pop-scrap bits (same-time set+to with `overwrite:"auto"`, intentional burst)
- validate: 0 errors, 0 contrast warnings ("25 text elements pass WCAG AA")
- inspect: 0 layout issues across 38 cue-timed samples
- snapshot QA: 3 rounds (39-frame full pass + 13-frame fix pass + final 38-frame record). Fixes: 3.1 receipt geometry + readable line chip + warm base grade + plaque fit; 3.3 stray strings removed, `Bold.` enlarged; 3.4 pin rest point moved off WIT's face; 3.5 echo stamp separated (no stacked text); 3.7 WIT restructure + money cluster; 3.8 deflated balloons repositioned (lying), reading WIT enlarged
- export/render: not requested; no MP4/WebM created

## Notes

- Preview project id resolves to the folder name `3-promise-machine` (confirmed via `/api/projects`).
- Servers 1001/1002 remain stopped per owner request (2026-07-07); only 1003 was started for this run.
