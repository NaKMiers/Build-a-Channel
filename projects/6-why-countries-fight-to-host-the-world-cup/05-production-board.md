# 05 Production Board

Video: `Why Countries Fight to Host the World Cup (and Lose Billions)`

Status: `all 9 sections built - awaiting owner review`

Source skill: `render`

Source files:

- `02-script.md`
- `03-voiceover.md`
- `04-visual-plan.md`
- `assets/asset-manifest.md` (all Section 1 assets `done` at gate time)

## Port Map


| Target                                | Port | Studio URL                                              | Direct Composition URL                                                              | Status                                  |
| ------------------------------------- | ---- | ------------------------------------------------------- | ----------------------------------------------------------------------------------- | --------------------------------------- |
| Unified preview                       | 1000 | `http://localhost:1000/#project/full-video`             | `http://localhost:1000/api/projects/full-video/preview/comp/index.html`             | running (combine 2026-07-07)            |
| Section 1 Hook                        | 1001 | `http://localhost:1001/#project/1-hook`                 | `http://localhost:1001/api/projects/1-hook/preview/comp/index.html`                 | stopped (owner request 2026-07-07)      |
| Section 2 Reframe                     | 1002 | `http://localhost:1002/#project/2-reframe`              | `http://localhost:1002/api/projects/2-reframe/preview/comp/index.html`              | stopped (owner request 2026-07-07)      |
| Section 3 Promise Machine             | 1003 | `http://localhost:1003/#project/3-promise-machine`      | `http://localhost:1003/api/projects/3-promise-machine/preview/comp/index.html`      | stopped (owner shutdown-all 2026-07-07) |
| Section 4 FIFA Keeps The Money        | 1004 | `http://localhost:1004/#project/4-fifa-keeps-the-money` | `http://localhost:1004/api/projects/4-fifa-keeps-the-money/preview/comp/index.html` | stopped (owner shutdown-all 2026-07-07) |
| Section 5 The Three Drains            | 1005 | `http://localhost:1005/#project/5-three-drains`         | `http://localhost:1005/api/projects/5-three-drains/preview/comp/index.html`         | stopped (owner shutdown-all 2026-07-07) |
| Section 6 The Morning After           | 1006 | `http://localhost:1006/#project/6-morning-after`        | `http://localhost:1006/api/projects/6-morning-after/preview/comp/index.html`        | stopped (owner shutdown-all 2026-07-07) |
| Section 7 Who Decides Is Not Who Pays | 1007 | `http://localhost:1007/#project/7-who-decides-who-pays` | `http://localhost:1007/api/projects/7-who-decides-who-pays/preview/comp/index.html` | stopped (owner shutdown-all 2026-07-07) |
| Section 8 Payoff: Check The Receipt   | 1008 | `http://localhost:1008/#project/8-payoff`               | `http://localhost:1008/api/projects/8-payoff/preview/comp/index.html`               | stopped (owner shutdown-all 2026-07-07) |
| Section 9 Outro                       | 1009 | `http://localhost:1009/#project/9-outro`                | `http://localhost:1009/api/projects/9-outro/preview/comp/index.html`                | stopped (owner shutdown-all 2026-07-07) |




## Section Render Index


| #   | Section                                | Status                          | Port | Preview project                    | Source                                                     | Checks                                                                                                     | Export file          | Notes                                                                                                                                                                                                                        |
| --- | -------------------------------------- | ------------------------------- | ---- | ---------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Hook: The Trophy Prints A Receipt      | `built - awaiting owner review` | 1001 | `previews/1-hook/`                 | section-01-hook visual plan + word timings                 | lint 0 err / validate 0 err / inspect 0 issues / snapshot QA passed                                        | none (not requested) | 7 scenes, 35.904s; receipt motif born at 10.26                                                                                                                                                                               |
| 2   | Reframe: A Purchase, Not An Investment | `built - awaiting owner review` | 1002 | `previews/2-reframe/`              | section-02-reframe visual plan + word timings              | lint 0 err / validate 0 err / inspect 0 issues / snapshot QA passed (3 rounds)                             | none (not requested) | 5 scenes, 33.728s; trophy hero returns; pose substitution + derived wallet cutout documented in IMPLEMENTATION.md                                                                                                            |
| 3   | The Promise Machine                    | `built - awaiting owner review` | 1003 | `previews/3-promise-machine/`      | section-03-promise-machine visual plan + word timings      | lint 0 err / validate 0 err (0 contrast warns) / inspect 0 issues / snapshot QA passed (3 rounds)          | none (not requested) | 8 scenes, 60.779s; receipt motif returns; NEW hypnotized-numbers pose; mailbox generate-fallback per manifest; render adjustments in IMPLEMENTATION.md                                                                       |
| 4   | FIFA Keeps The Money                   | `built - awaiting owner review` | 1004 | `previews/4-fifa-keeps-the-money/` | section-04-fifa-keeps-the-money visual plan + word timings | lint 0 err / validate 0 err 0 warn / inspect 0 issues / snapshot QA passed (4 rounds)                      | none (not requested) | 9 scenes, 62.101s; arrow direction language born; gold safe + cash bundle heroes; 2 NEW WIT poses; final payoff cue estimated ~61.40 (whisper tail regression, per plan)                                                     |
| 5   | The Three Drains                       | `built - awaiting owner review` | 1005 | `previews/5-three-drains/`         | section-05-three-drains visual plan + word timings         | lint 0 err / validate 0 err 0 warn / inspect 0 issues / snapshot QA passed (6 rounds)                      | none (not requested) | 7 scenes, 55.851s; drain-grate hero x4, shrinking boom-pile running gag; flock freeze [beat] -> ZURICH payoff; 1 NEW WIT pose (minister)                                                                                     |
| 6   | The Morning After                      | `built - awaiting owner review` | 1006 | `previews/6-morning-after/`        | section-06-morning-after visual plan + word timings        | lint 0 err / validate 0 err / inspect 0 issues / snapshot QA passed (2 rounds)                             | none (not requested) | 8 scenes, 61.44s; elephant-stadium pet HERO + MAINTENANCE bowl motif (returns 6.7); receipt motif prints the white-elephant line; 2 NEW WIT poses (party-hat feeder, magnifier); corrupt "Mars." timestamp bypassed per plan |
| 7   | Who Decides Is Not Who Pays            | `built - awaiting owner review` | 1007 | `previews/7-who-decides-who-pays/` | section-07 visual plan + word timings                      | lint 0 err (5 documented warns) / validate 0 err 0 warn / inspect 0 issues / snapshot QA passed (7 fixes)  | none (not requested) | 9 scenes, 66.987s; ~69 cues; giant WIT alternating sides C-R-L-R-L-R-L-R-L; whisper tail non-monotonic (words 206-216) -> final cues on the plan's +2.99s shift; 3 tiny taxpayer WITs as PAYS-panel props                    |
| 8   | Payoff: Check The Receipt              | `built - awaiting owner review` | 1008 | `previews/8-payoff/`               | section-08 visual plan + word timings                      | lint 0 err (3 motif-reuse warns) / validate 0 err 0 warn / inspect 0 issues / snapshot QA passed (5 fixes) | none (not requested) | 6 calm scenes, 39.573s; ~35 cues; 1 WIT per scene, no pose repeats; Christmas mantel neutralized by chimney-breast crop + cool grade + CSS shelf; 8.5 thesis receipt panel per chip rule                                     |
| 9   | Outro: The Cheapest Host On Earth      | `built - awaiting owner review` | 1009 | `previews/9-outro/`                | section-09 visual plan + word timings                      | lint 0 err (8 documented warns) / validate 0 err / inspect 0 issues / snapshot QA passed (4 fixes)         | none (not requested) | 2 scenes, 17.877s; motif retirement receipt prints TOTAL: $0.00; interactive CSS/SVG WhyTube card (LIKE click @8.22, SUBSCRIBE click @11.32 + confetti); giant peace-sign WIT + CONSULTANT-FREE stamp                        |




## Shared Asset Rules

- Video-level assets: `projects/6-why-countries-fight-to-host-the-world-cup/assets/` (single source of truth; poses in `assets/poses/`)
- Section asset junction rule: preview-local `assets` is a SYMLINK to `../../assets` (works on this Linux box; HTTP 200 verified). Fonts live in shared `assets/fonts/patrick-hand-latin.woff2`.
- Attribution file: `assets/ATTRIBUTION.md`
- Section voiceover mp3 is copied next to each section `index.html` (relative `src`).



## Active Section Notes

- Sections 7-9 were built in one PARALLEL run (2026-07-07, three concurrent agents, one per section); shared files (this board, asset-manifest, ATTRIBUTION, skill memory) were updated only by the orchestrator afterward. No derived assets were created by any of the three sections.
- Section 9: built 1:1 from the visual plan; cues pinned to `section-09-word-timings.json` (monotonic; whisper tail end 20.2 clamped to 17.877s). 9.1 receipt print text lives on a CSS receipt face (asset paper band is ~37% canvas width); 9.2 is one continuous interactive parody WhyTube card (CSS/SVG only, project-5 S8 CTA kit adapted): cursor clicks LIKE on "there"@8.22 and SUBSCRIBE on "Subscribe"@11.32 (cross-fades, bell, namespaced confetti), $0.00 tag on "free", stamp on "predict"; giant `peace_sign_calm_open_mouth` rises from the bottom edge beside the card with the CONSULTANT-FREE chest stamp. Render adjustments in `previews/9-outro/IMPLEMENTATION.md` (flash re-anchor, card raised for subtitle safety at the zoomed position, click point re-centered, stamp-tail backing). Known cosmetic: the shared trophy PNG carries a small baked dark dot on the globe (visible in close-ups since S1) - owner may want a touch-up.
- Section 8: built 1:1 from the visual plan; cues pinned to `section-08-word-timings.json` (monotonic; final token end 42.30 clamped to 39.573s). Render adjustments in `previews/8-payoff/IMPLEMENTATION.md`: Christmas-decorated `mantel-livingroom-1.jpg` neutralized (crop into the chimney breast, saturate 0.35 + cool tint, corner shade over a figurine sliver, trophy on a CSS floating shelf), 8.2 WIT flipped left to the real chair-at-right geometry, 8.4 tally card + green arrow carry the beat (base has scattered euro notes, no counting machine, per manifest note), 8.5 thesis text on a self-carried white receipt panel, 8.3 clip-path type-on replaced with per-line word-timed hard-shows (centered type-on clips half-words), tag texts anchored to measured tag faces.
- Section 7: built 1:1 from the visual plan; cues pinned to `section-07-word-timings.json`; whisper tail words 206-216 non-monotonic -> final four cues use the plan's +2.99s shift interpolation (ticket cross ~64.26 through receipt unroll ~66.34), end clamped to 66.987s. Render adjustments in `previews/7-who-decides-who-pays/IMPLEMENTATION.md`: 7.4 markup box moved to the empty prestige field, 7.5 detached CSS anger mark removed (pose carries the scream; pose catalog wrongly promises a mark), 7.6 needle patch rebuilt as blurred gradient, 7.2 bubble tail re-aimed at the suits trio, 7.9 stamp/stack/plate re-grounded, spreadsheet-context CSS behind the white-background calculator photo.
- Section 6: built 1:1 from the visual plan; all cues pinned to `section-06-word-timings.json` (plan times matched the JSON exactly; corrupt final "Mars." timestamp bypassed - confetti at Bruno's end 60.86, end clamped to 61.44s). Render-side adjustments in `previews/6-morning-after/IMPLEMENTATION.md`: CSS center circle/spot drawn on the 6.6 pitch (manifest note), CSS beam shafts over the 6.8 single-light stage photo, 6.5 lens inset re-aligned to the pose's glass, 6.7 receipt line on a white excerpt chip, 6.3 club line upgraded to a cream chip + CSS ball, 6.2 elephant re-grounded, 6.8 timeline labels moved inside the clip-wiped box.
- Section 5: built 1:1 from the visual plan; all cues pinned to `section-05-word-timings.json` (monotonic; end clamped to 55.851s). Render-side adjustments in `previews/5-three-drains/IMPLEMENTATION.md`: 5.1 all-ground confetti base + dark numbered chips on the grates, 5.2 black-wallet grade + labels onto dark leather, 5.4 U-turn rebuilt as a real loop path, 5.5 WIT re-anchored by snapshot measurement, mirrored wrappers for the hiding local / flying flock / walking guests, 5.6 flock freeze beat (no tweens 50.54-50.82), 5.7 bye. as cream chip.
- Section 4: built 1:1 from the visual plan; all cues pinned to `section-04-word-timings.json` (final three tokens regressed -> last payoff line estimated ~61.40, scene end clamped to 62.101s, per the plan's note). Render-side adjustments in `previews/4-fifa-keeps-the-money/IMPLEMENTATION.md`: 4.6 pose substitution (`rich_flex_gold_chain_sunglasses` pixels are the plain smirk again -> `boss_suit_sunglasses_sparkle` mirrored), 4.8 built to the real scale photo geometry (hanging left pan + flat right disc; no fake beam tilt; sack lands in the real pan), 4.5 safe among the foreground lupins (photo has no lawn), 4.4 ink pad is dark blue (manifest-accepted substitution), 4.5 pointing pose mirrored in a wrapper, 4.1 mayor pose wrapper-cropped at its baked desk edge.
- Section 3: built 1:1 from the visual plan; all cues pinned to `section-03-word-timings.json` (final token corrupted -> end clamped to 60.779s, per the plan's note). Render-side adjustments in `previews/3-promise-machine/IMPLEMENTATION.md`: receipt line on a white excerpt chip (receipt PNG paper is ~37% of canvas width), 3.3 balloon strings dropped, 3.7 WIT moved to frame-right with bottom crop (photo has no waist-height barrier for the planned behind-the-bar crop) + money cluster recentered, 3.8 deflated balloons rotated to lie in the confetti, 3.4 window haze over airline tails. Scene 3.6 uses the manifest-documented mailbox generate-fallback with a warm-graded `gold-bokeh-black-1.jpg` backdrop.
- Section 2: built 1:1 from the visual plan; cues pinned to `section-02-word-timings.json` first pass (whisper duplicate backward pass at words 91-109 skipped per the plan; end clamped to 33.728s). Render-side decisions in `previews/2-reframe/IMPLEMENTATION.md`: pose substitution (`rich_flex_gold_chain_sunglasses.png` pixels do not match its `pose.md` catalog entry - plain smirk, no chain/sunglasses; used `boss_suit_sunglasses_sparkle.png` instead, copied to `assets/poses/`), derived `assets/wallet-empty-cutout.png` (white studio bg keyed; `mix-blend-mode` is isolated in the capture path), 2.1 ribbon/sticker rearranged below the chip arc, 2.4 CSS boutique backdrop + counter line for the chest-up panic WIT.
- Section 1: built 1:1 from the visual plan; every cue pinned to `section-01-word-timings.json` (pre-existing, verified monotonic). Render-side deviations (map seam crop-out, receipt plinth pivot, pan distance -1100, S7 drape off the face) documented in `previews/1-hook/IMPLEMENTATION.md`.
- Known snapshot-tool artifact: first captured frame of a run can miss a late-decoding PNG (screenshot fallback mode). All elements verified present via re-snaps. Re-check if MP4 export is requested.
- Environment (Linux box, first render here): unprivileged port floor lowered to 1000 via `sudo sysctl -w net.ipv4.ip_unprivileged_port_start=1000` - NOT persistent across reboots; re-run before starting servers or persist in `/etc/sysctl.d/`.



## Caption Note (2026-07-08)

Captions completed for all 22 supported languages, exported to `output/captions/`.

- Timing base: `voiceover/combined-segments.json` (163 cues, English text taken verbatim from `02-script.md`, aligned to the real combined-audio word timings from an earlier pass of this project) - reused as-is, not re-transcribed.
- Prior partial run had exported 7 of 22 languages (arabic, chinese-simplified, chinese-traditional, english, french, german, italian). This run translated the remaining 15 (bangla, hindi, indonesian, japanese, korean, malayalam, polish, portuguese, russian, spanish, tamil, telugu, thai, turkish, vietnamese) cue-for-cue via 15 parallel translator subagents (163 cues each) and wrote each SRT via `write-translated-srt.mjs`, reusing the exact English timing.
- "FIFA" kept verbatim (transliterated where the language convention calls for it, e.g. Cyrillic); "World Cup" localized to each language's natural sports-media term; numbers/currency figures left unchanged.
- Verified: all 22 files in `output/captions/`, every language has the same cue count (163) and byte-identical timestamps vs `english.srt`, 0 empty cues, clean UTF-8 (Arabic/CJK/Indic/Thai render correctly, no mojibake). No duplicate root-level `output/captions.srt` (removed 2026-07-08 - `output/captions/english.srt` is the single English file).



## Stale / Regeneration Notes

- Combine and caption have both run (this board's Port Map / Section Render Index above predate that; update them if section-level details are needed again). Final MP4 exported 2026-07-08. Packaging has not run yet.



## Final Video Export (2026-07-08)

- Rendered the unified composition (`hyperframes/full-video/index.html`) to MP4 with `hyperframes@0.6.76 render` (Chrome + ffmpeg-static/ffprobe-static, since neither is on this box's PATH).
- Lint before render: 0 errors, 60 pre-existing per-section warnings (no combine-introduced issues).
- Output: `output/6-why-countries-fight-to-host-the-world-cup.mp4` - 1920x1080, h264/aac, 434.789s (matches `combined-voiceover.mp3` at 434.760s), 78,123,611 bytes (~74.5 MB).
- Verified by extracting a frame per section (via ffmpeg `-ss`) at each of the 9 mount offsets (0, 35.952, 69.744, 130.584, 192.744, 248.664, 310.152, 377.208, 416.832s) - all 9 rendered with real content (mascot, photos, WIT poses, on-screen text), none blank.
- The render log's `Sub-composition timelines not registered after 45000ms` warning is benign (documented in the combine skill's memory) - confirmed by the frame check above.
- `renders/` was empty after the move (no leftover scratch or `.gitkeep`) and was removed per the `.gitkeep` rule.



## Next Step Boundary

Next workflow step: `Packaging` (all 9 sections built, combine/caption/final-MP4-export complete; ALL preview servers stopped per owner shutdown-all 2026-07-07 - restart any section on demand with `npx --yes hyperframes@0.6.76 preview --port 100N` from its `previews/<N>-*/` folder; re-apply the sysctl port fix first if the box rebooted)

Do not continue into review, upload, or learning until the user asks for the next skill or explicitly requests that step.