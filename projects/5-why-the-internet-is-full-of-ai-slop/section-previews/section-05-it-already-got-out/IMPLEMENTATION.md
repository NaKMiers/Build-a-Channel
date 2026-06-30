# Section 5 Render Implementation

Video:
`Why The Internet Is Full Of Garbage Now`

Section:
`Section 5: It Already Got Out`

Status:
`built, ready for review` (preview only; no MP4 export requested)

## Result

- Preview project: `section-previews/section-05-it-already-got-out/`
- Source: `visual-plan` S5 + REAL word timings (`voiceover/section-05-it-already-got-out/section-05-word-timings.json`)
- Port: `1005`
- Studio URL: `http://localhost:1005/#project/Build%20a%20Channel`
- Direct composition URL: `http://localhost:1005/api/projects/Build%20a%20Channel/preview/comp/index.html`
- Runtime: `53.739s` (root `data-duration`, matches the section voiceover)
- Voiceover: `section-05.mp3`, wired as `<audio data-track-index="30">`
- Composition id: `Section05GotOut`

## Word Timings (generated, not estimated)

Generated with the transformers.js / whisper-tiny.en recipe (ffmpeg static -> 16 kHz mono f32 ->
gen script) and pinned every `data-start` + GSAP reveal to actual word starts. Output:
`voiceover/section-05-it-already-got-out/section-05-word-timings.json` (159 words; clean, monotonic).
Whisper tail-glitch: the last word "inbox." transcribed an end of `56.52`, past the real audio; the
root duration is clamped to the real `53.739s` and the final icon pop pinned to `53.00` (inside the
real audio).

## Big Scene / Cue Plan Implemented (7 scenes, one per domain beat, each its own track + crossfade)

| Scene | Start | Voice cue (word @ s) | Big scene | What changes | Motion | WIT | Flood |
|---:|---:|---|---|---|---|---|---:|
| 5.1 | 0.00 | "It got out." 2.98 | living-room scroll + slop bursting from a phone | aside "not just funny Facebook pics..." 0.66, "it got out." 2.98 | title=smash, aside hard-show | `worried_uneasy_wide_eyes` R, ~1140 | 13% |
| 5.2 | 3.90 | "Music." 4.00 | empty concert hall + uncanny AI band | "Music." 4.00, band hard-show, "1,000,000 LISTENERS" card 6.44, "0 REAL MEMBERS" 11.94 | dom=pop, card+stamp=smash | `skeptical_side_eye_doubtful` R, ~1120 | 19% |
| 5.3 | 12.70 | "Books." 12.84 | forest floor + AI mushroom guide book | "Books." 12.84, "AI foraging guide" chip 13.82, skull + "can actually KILL you." 20.48 | dom=pop, guide hard-show, skull+kill=smash | `panic_hands_on_cheeks_scream` L, ~1080 | 27% |
| 5.4 | 21.10 | "Kids." 21.26 | living room + kid-video thumbnail grid | "Kids." 21.26, grid 21.40, "40%" 24.00, 4 SLOP stamps 26.80/27.30/27.70/28.14, "40 out of every 100" 28.60 | dom=pop, 40%=smash, SLOP=staggered pops, cap hard-show | `annoyed_disgusted_open_frown` L, ~1080 | 35% |
| 5.5 | 29.95 | "six legged horses" 31.54 | living room + garish six-legged AI horse | horse hard-show, "6 LEGS?!" 31.54, "A B C ?" 33.50 | legs+abc=smash | `cringe_uneasy_drool` R, ~1080 | 43% |
| 5.6 | 34.90 | "Even your job." 35.08 | office desk + glossy workslop document | "Even your job." 35.08, doc hard-show, "looks great. says nothing." 40.12, "WORKSLOPPED" 42.28, "~2 HOURS to clean up" 46.14 | dom=pop, nothing/hours=smash, stamp=smash | `exhausted_dead_inside_eye_bags` R, ~1080 | 53% |
| 5.7 | 47.66 | "congratulations." 48.08 | grey-sludge flood peaks + WIT drowning, holding one real photo | "congratulations." 48.08, 4 bobbing domain icons feed 50.44 / music 50.92 / tablet 51.58 / inbox 53.00 | grats=smash, icons=staggered pops | `swimming_underwater_goggles_cap` CENTER, ~980 | 66% |

Section motif: **THE GREY-SLUDGE FLOOD** (`grey-sludge-flood-1.jpg` callback from S1/S2). The `.flood`
waterline rises scene by scene (13 / 19 / 27 / 35 / 43 / 53 / 66 %) so the screen literally fills with
slop as the narration lists each domain, then peaks at 5.7 with WIT drowning while holding one real
photo (`real-photo-lifeline.png`) above the water.

## Render Review-Prevention Pass

- voice cue map completed: yes (built from generated word-timings JSON)
- big-scene sanity checked: yes (one persistent big scene per domain beat; flood motif rises as a continuity device, not a crutch)
- cue density checked: yes (each cue adds 1-2 meaningful changes)
- motion density checked: yes (domain chips pop, ordinary labels hard-show; impact reserved for "it got out.", the listeners card + "0 REAL MEMBERS", "KILL you.", "40%" + the SLOP stamp barrage, "6 LEGS?!", "WORKSLOPPED" + "~2 HOURS", "congratulations." + the domain-icon payoff)
- WIT density: 1 giant WIT per scene, varied pose + side (R/R/L/L/R/R/CENTER), all ~1/3-1/2 frame
- WIT crop/collision checked: yes - faces/heads/glasses intact, legs-only crops; text placed opposite WIT; no text covers WIT face
- markup target checked: SLOP stamps land on the 4 `.slop` thumbnails; "6 LEGS?!" circle by the horse's legs; "0 REAL MEMBERS" under the listeners card
- scene differentiation checked: yes - 4 fresh photo bases + 2 reuse bases (S1 scroll, S1/S2 flood) + living-room-tv reused 5.4/5.5 (same room, different content)
- HyperFrames mechanics checked: each scene own track, crossfade fadeIn, deterministic GSAP, audio clip, synchronous timeline registration

## Render decisions beyond the visual plan

- Generated real word-timings and pinned all cues (plan times were estimated); clamped the whisper tail "inbox." (56.52) to the real `53.739s` audio.
- **Checkerboard-keyout fix (3 generated heroes):** `mushroom-guide-book.png`, `six-legged-horse-cartoon.png`, and `real-photo-lifeline.png` were delivered as OPAQUE RGB with a baked transparency-checkerboard pattern (alpha extrema 255,255), unlike the real-RGBA phone/document (alpha 0,255). Keyed the checkerboard out to true alpha (tone-mask: light AND neutral pixels -> `scipy.ndimage` connected components -> keep only border-touching components -> 1px dilation to swallow the antialiased fringe). Originals backed up to `assets/_raw-checkerboard/`. Verified clean via re-snapshot.
- **SLOP-stamp GSAP selector fix (5.4):** the first stamp tween used `.thumb.slop:nth-of-type(1)` which matched nothing (`:nth-of-type` counts by element TYPE (div), not by the `.slop` class). Removed the orphan tween, added `opacity:0` to the `.ss` default CSS so stamps stay hidden until they pop, and re-pinned the 4 working pops to `:nth-child(2/4/6/9) .ss` at 26.80 / 27.30 / 27.70 / 28.14. Re-validate confirmed the 2 "GSAP target not found" warnings are gone.
- Scene 5.6 base `office-desk-inbox-1.jpg` carries an incidental Apple logo on the monitor bezel (manifest-flagged). It is covered at render by the large `workslop-document.png` hero composited over the screen area (per the manifest's "cover with the CSS workslop-document at render" note).

## Assets

- Shared asset folder: `projects/5-why-the-internet-is-full-of-ai-slop/assets/`
- Section assets: local `assets` junction -> `../../assets` (verified resolves; font + poses + heroes + bases all present)
- Generated heroes used (6): `slop-bursting-phone`, `ai-band-uncanny`, `mushroom-guide-book`, `six-legged-horse-cartoon`, `workslop-document`, `real-photo-lifeline`
- Photo bases used (4 fresh): `music-stage-lights-1` (5.2), `forest-floor-mushrooms-1` (5.3), `living-room-tv-1` (5.4 + 5.5), `office-desk-inbox-1` (5.6)
- Cross-section reuse: `social-scroll-livingroom-1` (S1) -> 5.1; `grey-sludge-flood-1` (S1/S2 flood motif) -> 5.7 (+ the rising waterline 5.1-5.6)
- Poses (7 distinct): see the table above
- Render-CSS (no asset file): rising sludge waterline, music-app listeners card + "0 REAL MEMBERS", red skull + "KILL you.", kid-video thumbnail grid + SLOP stamps + "40%" + "40 out of every 100", "6 LEGS?!" circle + "A B C ?", "WORKSLOPPED" stamp + "~2 HOURS" clock, 4 bobbing domain icons (feed / music / tablet / inbox), "congratulations."
- Attribution: `assets/ATTRIBUTION.md`

## Verification

- lint: `0 error(s), 1 warning(s)` - `duplicate_media_discovery_risk` (`living-room-tv-1.jpg` reused 5.4/5.5; same room, different content). Intentional reuse; non-blocking.
- validate: `0 error(s), 0 warning(s)` (75 WCAG contrast advisories on stylized emphasis text over photos; mitigated by heavy text-shadow + side scrims; read fine in snapshots - same class as S1-S4). The 2 prior GSAP "target not found" warnings are resolved.
- inspect: `0 layout issues across 18 sample(s)`
- direct preview snapshots: per-scene QA across all 7 scenes + targeted re-snaps at 24.5s (no SLOP stamps yet) and 29.5s (all 4 SLOP stamps popped) confirming the selector fix; re-snaps of the 3 keyed heroes confirming clean transparency
- export/render: not requested (preview only)

## Notes

- No MP4/WebM exported (not requested).
- Word-timings file is the source of truth; if S5 script wording changes, regenerate timings and re-pin.
- Checkerboard-keyout originals are kept in `assets/_raw-checkerboard/` in case a re-key is needed.
