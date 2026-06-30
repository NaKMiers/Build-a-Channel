# Section 7 Render Implementation

Video:
`Why The Internet Is Full Of Garbage Now`

Section:
`Section 7: Payoff - Attention In, Garbage Out`

Status:
`built, ready for review` (preview only; no MP4 export requested)

## Result

- Preview project: `section-previews/section-07-attention-in-garbage-out/`
- Source: `visual-plan` S7 + REAL word timings (`voiceover/section-07-attention-in-garbage-out/section-07-word-timings.json`)
- Port: `1007`
- Studio URL: `http://localhost:1007/`
- Direct composition URL: `http://localhost:1007/api/projects/section-07-attention-in-garbage-out/preview/comp/index.html`
- Runtime: `43.413s` (root `data-duration`, matches the section voiceover)
- Voiceover: `section-07.mp3` (am_eric / David23 / 0.80), wired as `<audio data-track-index="30">`
- Visual plan: `visual-plan/section-07-attention-in-garbage-out/section-07-attention-in-garbage-out-visual-plan.md`
- Composition id: `Section07Payoff`

## Word Timings (generated, not estimated)

Per the Voice-Sync Timing Contract, I GENERATED real word timings with the transformers.js /
whisper-tiny.en recipe (ffmpeg static -> 16 kHz mono f32 -> gen script) and pinned every `data-start` +
GSAP reveal to actual word starts. Output:
`voiceover/section-07-attention-in-garbage-out/section-07-word-timings.json`.

Two whisper artifacts handled:
- **Tail glitch** - the final word's end timestamp runs past the real audio, so the root duration is
  clamped to the real `43.413s`.
- **Chunk-boundary reorder glitch (new)** - whisper reordered / mistimed the closing phrases ("you keep
  your eyes open" got pulled forward to ~35s, out of order). The real order is the weird-machine line
  (~41.9s) then the sign-off (~42.0-43.4s). The single final cue "keep your eyes open." is therefore
  pinned to `42.00` from the audio tail - the one deliberately estimated cue in the section, documented
  here.

## Big Scene / Cue Plan Implemented (7 scenes, one per beat, each its own track + crossfade)

| Scene | Start | Voice cue (word @ s) | Big scene | What changes | Motion | WIT |
|---:|---:|---|---|---|---|---|
| 7.1 | 0.00 | "why" 0.50 | dark machine hall + winding slop engine | "WHY?" 0.50, "full of garbage now..." aside 2.08 | WHY?=smash, aside hard-show | `pointing_up_curious_open_mouth` L, ~1080 |
| 7.2 | 2.70 | "evil" 3.82 | dark spotlight stage + slop-wins trophy podium | struck "AI IS EVIL" 3.82, struck "CONSPIRACY" 5.52, "pays for ATTENTION" 9.80, "slop wins." 13.80 | strikes=smash, pays hard-show, wins=smash | `eyes_closed_talking_open_palm` R, ~1040 |
| 7.3 | 14.30 | "Attention in" 14.48 | machine hall + engine (in/out) | "ATTENTION IN." 14.48, "GARBAGE OUT." 15.22 | in/out=smash (opposite slides) | `lecturing_finger_raised_eyes_closed` L, ~980 |
| 7.4 | 16.25 | "broken" 17.22 | machine hall + engine | struck "BROKEN" 17.22, green "WORKING PERFECTLY check" 19.12, "that is the problem." 20.18 | strike/check=smash, problem hard-show | `deadpan_unimpressed_half_lidded` R, ~1020 |
| 7.5 | 20.95 | "upgrade" 22.60 | evidence desk + THE TELLS checklist | "a small, useful upgrade." 22.60, "THE TELLS" 24.46, row1 six fingers 25.18, row2 too perfect 27.20, row3 too good to be true 29.52 | header=smash, rows=pop | `presenting_screen_announcing_open_mouth` L, ~1000 |
| 7.6 | 30.40 | "flood" 30.76 | bright calm window + receding flood | "you can't stop the flood." 30.76, "but stop being FOOLED." 32.58, "pay attention on purpose = you win." 37.00 | FOOLED/win=smash, line1 hard-show | `proud_explaining_hand_on_chest_hand_on_hip` C, ~980 |
| 7.7 | 39.30 | "weird machine" 39.76 | bright calm window + small engine tag | "we'll keep explaining the weird machine." 39.76, big "keep your eyes open." 42.00 (pinned from audio tail) | eyes=smash | `pointing_at_viewer_serious_accusing` R, ~1000 |

Arc device: this is the **payoff / thesis-landing** section. It recaps the question (WHY?), gives the
one-line answer (not evil, not a conspiracy - the internet pays for attention and slop wins), compresses
it to the title beat (ATTENTION IN / GARBAGE OUT), reframes (not broken, WORKING PERFECTLY - that is the
problem), hands the viewer the practical upgrade (THE TELLS checklist), then empowers + signs off (you
can't stop the flood but you can stop being fooled; keep your eyes open).

## Render Review-Prevention Pass

- voice cue map completed: yes (built from generated word-timings JSON; one cue documented as estimated - see reorder glitch)
- big-scene sanity checked: yes (one persistent big scene per beat; the slop engine recurs 7.1/7.3/7.4/7.7 as the through-line motif, the trophy podium is the 7.2 answer image)
- cue density checked: yes (each cue adds 1-2 meaningful changes)
- motion density checked: yes (ordinary labels hard-show; impact reserved for WHY?, the two strikes + slop wins, ATTENTION IN / GARBAGE OUT, BROKEN / WORKING PERFECTLY, THE TELLS + rows, FOOLED / you win, keep your eyes open)
- WIT density: 1 giant WIT per scene, varied pose + side (L/R/L/R/L/C/R); poses carry the curious -> explaining -> lecturing -> deadpan -> presenting -> proud -> direct-address arc
- WIT crop/collision checked: yes - faces/heads/glasses intact, legs-only crops; verified "WHY?" lands top-left clear of WIT (1.3s frame) and "slop wins." sits top-right clear of WIT (14.2s frame)
- markup target checked: struck cards / chip / checklist sit on the dark photo halves and device cards, never over WIT's face; trophy podium is center-stage, WIT pushed to the right edge
- scene differentiation checked: yes - 4 distinct bases (dark machine hall, dark spotlight stage, evidence desk, bright calm window) graded per mood
- HyperFrames mechanics checked: each scene own track, crossfade fadeIn, deterministic GSAP, audio clip, synchronous timeline registration

## Render decisions beyond the visual plan

- Generated real word-timings and pinned all cues (plan times were estimated); clamped the whisper tail to the real `43.413s` audio; the closing "keep your eyes open." cue is pinned to `42.00` from the audio tail because whisper reordered the final phrases (chunk-boundary reorder glitch).
- **Checkerboard-keyout fix (1 generate prop):** `slop-wins-trophy.png` was delivered as OPAQUE RGB with a baked transparency-checkerboard (alpha extrema 255,255). Keyed the checkerboard out to true alpha (same method as S5/S6: tone-mask `mn>=200 & (mx-mn)<=28` -> scipy connected components -> keep only border-touching components -> 1px dilation; cleared 60.2%, 9 components / 1 border-touching). Interior whites (trophy shine, the mascot's eyes/teeth) are non-border components and survive. Original backed up to `assets/_raw-checkerboard/`. Verified clean over a gray background.
- The CSS "argument graphics" (struck AI IS EVIL / CONSPIRACY / BROKEN cards with red strikethrough, the gold ATTENTION chip, the green WORKING PERFECTLY check, the in/out big words, THE TELLS checklist with two real AI-tell thumbnails + one CSS "headline" tile, the receding flood band) are render-built per the plan; this section leans on real bases + the recurring slop engine + the trophy hero plus CSS.

## Assets

- Shared asset folder: `projects/5-why-the-internet-is-full-of-ai-slop/assets/`
- Section assets: local `assets` junction -> `../../assets` (verified resolves; font + poses + props + bases all present)
- Generate props used: `slop-wins-trophy` (7.2)
- Recurring motif: `slop-engine-loop` (7.1 / 7.3 / 7.4 / 7.7)
- Tell thumbnails (reused): `ai-extra-fingers-hand`, `ai-influencer-perfect` (7.5)
- Photo bases used: `dark-machine-hall-1` (7.1 / 7.3 / 7.4), `dark-spotlight-stage-1` (7.2), `evidence-desk-1` (7.5), `bright-window-calm-1` (7.6 / 7.7)
- Poses (7 distinct): see the table above
- Attribution: `assets/ATTRIBUTION.md`

## Verification

- lint: `0 error(s), 3 warning(s)` - `duplicate_media_discovery_risk` (the slop engine reused across 7.1/7.3/7.4/7.7, the two machine-hall reuses, the two bright-window reuses). Intentional motif/base reuse; non-blocking.
- validate: `0 error(s), 0 warning(s)` (115 WCAG contrast advisories - the validator measures stylized text against the photo behind, ignoring each card's own opaque background; the struck cards / chip / green check / checklist all read fine in snapshots - same class as S1-S6)
- inspect: `0 layout issues across 18 sample(s)`
- direct preview snapshots: full pass across all 7 scenes + targeted re-snaps at 1.3s ("WHY?" landing) and 14.2s ("slop wins." placement) - both clear of WIT
- server: `http://localhost:1007/` responds `200`
- export/render: not requested (preview only)

## Notes

- No MP4/WebM exported (not requested).
- Word-timings file is the source of truth; if S7 script wording changes, regenerate timings and re-pin. The closing "keep your eyes open." cue is the one estimated pin (whisper reorder) - re-check it if the audio changes.
- Checkerboard-keyout original is kept in `assets/_raw-checkerboard/` in case a re-key is needed.
