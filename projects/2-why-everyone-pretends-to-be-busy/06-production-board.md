# 06 Production Board

Video: `Why Everyone Pretends To Be Busy`

Status: `section render in progress`

Source skill: `render`

Source files:

- `02-script.md`
- `04-voiceover.md`
- `05-visual-plan.md`

## Port Map

| Target | Port | Studio URL | Direct Composition URL | Status |
|---|---:|---|---|---|
| Unified preview | 1000 | http://localhost:1000/#project/full-video | http://localhost:1000/api/projects/full-video/preview/comp/index.html | running (combined) |
| Section 1 | 1001 | http://localhost:1001/#project/Build%20a%20Channel | http://localhost:1001/api/projects/Build%20a%20Channel/preview/comp/index.html | running |
| Section 2 | 1002 | http://localhost:1002/#project/Build%20a%20Channel | http://localhost:1002/api/projects/Build%20a%20Channel/preview/comp/index.html | running |
| Section 3 | 1003 | http://localhost:1003/#project/Build%20a%20Channel | http://localhost:1003/api/projects/Build%20a%20Channel/preview/comp/index.html | running |
| Section 4 | 1004 | http://localhost:1004/#project/Build%20a%20Channel | http://localhost:1004/api/projects/Build%20a%20Channel/preview/comp/index.html | running |
| Section 5 | 1005 | http://localhost:1005/#project/section-05-visible-work-beats-quiet-thinking | http://localhost:1005/api/projects/section-05-visible-work-beats-quiet-thinking/preview/comp/index.html | running |
| Section 6 | 1006 | http://localhost:1006/#project/section-06-im-busy-is-a-shield | http://localhost:1006/api/projects/section-06-im-busy-is-a-shield/preview/comp/index.html | running |
| Section 7 | 1007 | http://localhost:1007/#project/section-07-payoff-activity-is-not-value | http://localhost:1007/api/projects/section-07-payoff-activity-is-not-value/preview/comp/index.html | running |

Note: the preview server resolves the project id/title from the launch context. Sections 1-4 resolved to the workspace root name (`Build a Channel`); Section 5's server resolved to the section folder id (`section-05-visible-work-beats-quiet-thinking`) - use whichever the server's `/api/projects` reports. Both forms point `dir` at the section folder.

## Section Render Index

| # | Section | Status | Port | Preview project | Source | Checks | Export file | Notes |
|--:|---|---|--:|---|---|---|---|---|
| 1 | Hook: The Busy Trap | rebuilt v2 - ready for review | 1001 | `section-previews/section-01-hook-the-busy-trap/` | visual plan (v2) + existing word timings | lint 0 err / validate 0 err / snapshots ok | none (no export requested) | REMADE to new standard: 4 scenes (warm desk / real-UI busy-signals / minimal / caged desk), real bg every scene + real-UI calendar+inbox+phone, big+high WIT (4 poses). Audio still 0.84 (mismatch flagged) |
| 2 | Reframe: Looking Busy vs Doing Work | rebuilt v2 - ready for review | 1002 | `section-previews/section-02-reframe-looking-busy-vs-doing-work/` | visual plan (v2) + existing word timings | lint 0 err / validate 0 err / snapshots ok | none | REMADE to new standard: 4 scenes (office / bulb / typing+Meet-grid / bulb), real bg every scene + real-UI Meet grid, GIANT WIT (4 poses). Audio still 0.84 (mismatch flagged) |
| 3 | Busy Became A Status Symbol | rebuilt v2 - ready for review | 1003 | `section-previews/section-03-busy-became-a-status-symbol/` | visual plan (v2) + existing word timings | lint 0 err / validate 0 err / snapshots ok | none | REMADE to new standard: 6 scenes (trophy/chat/emotions-board/beach+calendar/dark-wood/meeting-room), real bg every scene + real-UI chat & calendar, GIANT WIT (6 poses). Audio still 0.84 (mismatch flagged) |
| 4 | Your Apps Invented Emergencies | built - ready for review | 1004 | `section-previews/section-04-your-apps-invented-emergencies/` | visual plan + generated word timings | lint 0 err / validate 0 err / snapshots ok | none | 5 scenes (iPhone notifs/app grid/alarm/chat/fridge); REAL app icons (user-approved); 5 WIT poses |
| 5 | Visible Work Beats Quiet Thinking | built - ready for review | 1005 | `section-previews/section-05-visible-work-beats-quiet-thinking/` | visual plan + generated word timings | lint 0 err / validate 0 err / snapshots ok | none | 5 scenes (Meet grid/wall/poll/Trello/Sheets-on-stage); REAL-UI (Meet/Trello/Sheets icons, user-preferred); 5 WIT poses |
| 6 | "I'm Busy" Is A Shield | built - ready for review | 1006 | `section-previews/section-06-im-busy-is-a-shield/` | visual plan + generated word timings | lint 0 err / validate 0 err / snapshots ok | none | 5 scenes (shield/1:1 chat/sticky-notes/meeting room/group chat); REAL photo backgrounds + real-UI chat; 5 WIT poses |
| 7 | Payoff: Activity Is Not Value | built - ready for review | 1007 | `section-previews/section-07-payoff-activity-is-not-value/` | visual plan + generated word timings | lint 0 err / validate 0 err / snapshots ok | none | 5 scenes (ACTIVITY≠VALUE/contrast/3-rows/honest chat/calendar-with-WiFi); REAL photo backgrounds + real-UI; 5 WIT poses |

## Combine (full video)

- Status: `re-assembled from LATEST section code - unified preview on localhost:1000` (2026-06-22, `/combine` rerun).
- Rerun reason: the first combine sourced the review mirrors, which were stale for S3/S5/S6/S7 (later user/linter tweaks) and S4 (giant-WIT change landed after). Rebuilt sourcing each section's LIVE `section-previews/.../index.html`; re-synced all 7 mirrors to match; refreshed consolidated assets. Audio unchanged (no voiceover edits) so `combined-voiceover.mp3` (265.20s) + offsets were kept. Re-lint 0 err; per-section snapshots confirm latest code (S4 now giant-WIT + shifted app grid).
- Output: `hyperframes/full-video/` (parent `index.html` mounts `compositions/section-01..07.html` audio-stripped; consolidated `assets/` + `combined-voiceover.mp3` at root). Assembly-only - no section content changed, no MP4/WebM exported.
- Combined voiceover: 7 section mp3s concatenated (ffmpeg stream-copy) = **265.20s** (~4:25). Section offsets (actual mp3 durations): S1 0 / S2 21.120 / S3 50.136 / S4 95.280 / S5 137.472 / S6 180.384 / S7 218.424.
- Each section mounted on its own track (1–7); one combined `<audio>` on track 10. Lint 0 errors; per-section snapshots confirm all bases/real-UI/WIT resolve at root.
- NOTE: S1–S3 audio is 0.84, S4–S7 is 0.86 - the combined track therefore mixes the two deliveries. If S1–S3 voiceover is regenerated at 0.86, re-concatenate `combined-voiceover.mp3` and re-pin section offsets.

## Export (MP4)

- Status: `exported` (2026-06-22, explicit user request) → `renders/full-video.mp4`.
- Source: the unified `hyperframes/full-video/` composition (latest section code). Command: `hyperframes render . --quality standard --fps 30` with the static ffmpeg/ffprobe on PATH (`$TEMP/wiw-ffbin/`; HyperFrames needs FFmpeg to encode - it is NOT on the system PATH by default, so prepend the static-binary dir before `render`).
- Output: **30.5 MB · H.264 1920×1080 @30fps · AAC 48kHz stereo · 265.22s** (~4:25). 7,956 frames, 6 capture workers, hardware-GPU.
- QA: extracted frames at 8/60/110/186/240s - all render full content (incl. S4 giant-WIT app grid). 
- NOTE: combined track mixes 0.84 (S1–S3) + 0.86 (S4–S7) delivery; re-export after unifying audio if desired. Re-render at `--quality high` for a final master if wanted.
- MOVED (2026-06-22, `/combine` move-only): the exported video was moved from `renders/full-video.mp4` to `output/full-video.mp4`; empty `renders/` was removed. `output/` is the deliverables home.

## Caption (SRT)

- Status: `exported` (2026-06-22, `/caption`) → `output/captions.srt`.
- Source audio: `hyperframes/full-video/combined-voiceover.mp3` (transcribed 265.14s → 966 Whisper words via `Xenova/whisper-tiny.en`). Word timings saved at `voiceover/combined-word-timings.json`.
- Method: cue TEXT from `02-script.md` narration (stage directions like `[deadpan]`/`[beat]` stripped); timing from real word-level transcription; Needleman-Wunsch alignment (967 cue tokens ↔ 966 hyp tokens). 94 cues, 0 overlaps, monotonic.
- Tail fix: whisper-tiny glitched the final words (timestamps jumped backwards near 257–261s), clamping the last cue short at 262.1s. Extended cue 94 end to 265.0s (≈ audio end) so the final line "...a calendar with Wi-Fi." holds through the end.
- Upload: YouTube Studio → Subtitles → Add → Upload file (with timing). Tied to this combined audio; re-sync if the uploaded video's pacing changes.

## Shared Asset Rules

- Video-level assets: `projects/2-why-everyone-pretends-to-be-busy/assets/` (fonts/, wit/, visual-references/, thumbnails/)
- Section asset junction rule: junctions fail to serve under HyperFrames CLI on this Windows setup, so each section preview uses a minimal COPIED `assets/` working set (documented exception, per render memory).
- Attribution file: `assets/visual-references/section-01-hook-the-busy-trap/ATTRIBUTION.md` (Public Domain bases, brand-free, people-free)

## Active Section Notes

- Section 1 REBUILT v2 (2026-06-22, owner: "remake this section from scratch"): now 4 scenes on the new standard - A warm work desk ("a strange rule" + the rule), B bright flat-lay + REAL-UI busy-signals (packed Google Calendar card + Gmail inbox-47 card + phone panic notifications, "this person matters"), C minimal desk ("quiet = lazy / asleep with eyes open"), D the warm desk returns cooled + CSS cage bars ("looking busy / there is a difference", callback to A). Real photo base every scene; big+high WIT (typing → phone-panic → deadpan → suspicious). Cues pinned to existing `section-01-word-timings.json`. Audio still 0.84 (plain) vs 0.86 elsewhere - FLAGGED; re-pin if regenerated. Mirror `hyperframes/review/section-01.html` synced. The v1 notes below are superseded.

- Section 3 REBUILT v2 (2026-06-22, owner: "remake this section from scratch"): 6 scenes on the new standard - A gold trophy ("busy = status symbol"), B hands-at-laptop + real-UI chat ("I'm so busy = please notice I'm important"), C grey desk + CSS EMOTIONS board ("Busy?" added = not an emotion), D tropical beach + real-UI packed calendar ("long holidays vs no free time = opposite brag"), E dark-wood hands ("busy sounds responsible/needed → feels valuable"), F meeting room + real-UI calendar of meetings-about-meetings ("proving you're near the work"). Real photo base every scene; GIANT high WIT (6 poses: awkward-celebration → talking → deadpan → suspicious → thinking → tiny-defeated). Cues pinned to existing `section-03-word-timings.json` (0.84). DROPPED v1 low-res bases (~250px); reused HD trophy + 3 clean cross-section bases (S6/S7) + 2 fresh. Audio 0.84 vs 0.86 elsewhere - FLAGGED. Mirror `hyperframes/review/section-03.html` synced.

- Section 2 REBUILT v2 (2026-06-22, owner: "remake this section from scratch"): 4 scenes on the new standard - A modern office interior ("not lazy people"), B glowing bulb on black ("rewards the look of work / thinking looks like nothing"), C hands-typing + REAL-UI Google Meet grid ("busy is easy to see: meetings/typing/serious face"), D bulb returns + red circle ("we trust what we see / real work hides here"). Real photo base every scene; GIANT high WIT (talking → thinking → typing → deadpan). Bulb = B↔D bookend. Cues pinned to existing `section-02-word-timings.json` (0.84). DROPPED v1 low-res base-meeting/base-think (~250px). Audio 0.84 vs 0.86 elsewhere - FLAGGED. Mirror `hyperframes/review/section-02.html` synced.

- Section 1 motif: calendar fills with fake urgency (Scene A) → quiet desk reads as "lazy" (Scene B) → calendar becomes a cage with WIT trapped inside a phone screen (Scene C). A/C share the calendar base as an intentional bookend (distinct grades + cage bars).
- Scene bases (final, 2026-06-22): clean real-world CC0 stock photos sourced via Openverse - `base-deskwork.jpg` (Scene A warm work desk), `base-deskcalm.jpg` (Scene B bright minimal desk), `base-deskwork-cage.jpg` (Scene C cooled + cage bars). Motif shifted from literal calendar to work-desk (no clean people-free calendar photo findable). Iteration history: dingy PD photos (rejected) → flat-illustrated CSS (rejected) → CC0 real photos (current). No image generator available. Cue timing/WIT unchanged. See section IMPLEMENTATION.md + ATTRIBUTION.md.
- All cue times pinned to generated `section-01-word-timings.json`. The dry button "There is a difference." lands at ~19.96–21.0 (later than the visual plan's estimate).
- WIT: 4 beats, each ≥1/3 frame, faces safe, no label/face collisions, verified in snapshots.
- No MP4/WebM exported (not requested).

- Section 5 motif (real-UI, owner-preferred): visible work = rewarded. Scene A Google Meet call grid (reply / meetings / "just circling back") → Scene B empty-room wall photo ("staring at a wall, possibly blinking", WIT thinking→deadpan) → Scene C survey poll card (Yes 15% / Not really 85%, "managers can't tell") → Scene D Trello Kanban where a card visibly moves DOING→DONE ("move a task column to column" @30.56, "updates about future updates", WIT facepalm) → Scene E Google Sheets spreadsheet spotlit on a theater stage with red curtains ("productivity theater", "the star ★" pops @40.76, WIT tiny-defeated).
- Meet/Trello/Sheets built in CSS with real icon PNGs (Wikimedia); editorial depiction, no faces (initials avatars), no pixel-copied screenshots, no private data - per standing owner real-UI preference (2026-06-22).
- v2 liveliness pass (owner: "missing some real-world images, not lively"): scenes A/C/D now float the UI as a screen over REAL people-free CC desk photos - A white desk + MacBook (`base-desk-call.jpg`), C marble + iPad (`base-desk-survey.jpg`), D dark wood + "To Do List" notepad (`base-desk-board.jpg`); distinct surfaces, CC0 StockSnap.
- v3 (owner: "last scene still not have background"): Scene E swapped CSS curtains for a REAL lit red theater-curtain photo (`base-stage.jpg`, CC0 Wikimedia, no people) + spotlight on the spreadsheet. ALL five scenes now have a real-world background (A/C/D/E real photos + B wall). Re-lint 0 err, re-snapshot ok, review mirror (`hyperframes/review/section-05.html` + `base-stage.jpg`) synced.

- Section 7 motif (PAYOFF - real backgrounds + real-UI, calmer): Scene A real "?"-note desk + `ACTIVITY ≠ VALUE` board (WIT thinking) → Scene B real hands-typing desk + REWARDED (AVAILABLE/FAST/OVERLOADED) vs REAL WORK NEEDS (FOCUS/QUIET/TIME) + NOT LAZY / BUSY=SAFER THAN THOUGHTFUL (WIT talking) → Scene C real warm office + HIGHLIGHT≠LEARN / REPLY≠SOLVE / ORGANIZE≠MAKE (WIT typing) → Scene D real-UI chat: honest reply struck + "TOO HONEST FOR A TUESDAY" → "Busy." → `BE HONEST ABOUT WHAT MATTERS` (WIT deadpan) → Scene E real-UI Google Calendar packed with red "urgent" events + `A CALENDAR WITH WI-FI` (WIT trapped). Ties the calendar motif together as the closer.
- Word-timings JSON generated this run; whisper tail glitch (last sentence jumped back ~40s) was re-timed monotonically (43.56→46.78). 3 distinct real bases (?-note / hands-typing / warm office); D/E reuse base-busy-d / base-question-e non-adjacently with the UI dominating; gcal icon reused from S4 (editorial). 5 distinct WIT poses. Re-lint 0 err, snapshots ok, mirror (`hyperframes/review/section-07.html`) synced.
- No MP4/WebM exported (not requested).

- Section 6 motif (real backgrounds + real-UI, owner-preferred): "I'm busy" is a shield. Scene A real office desk + CSS shield `I'M BUSY` deflecting request bubbles (WIT deadpan) → Scene B real wood desk + real-UI 1:1 Messenger chat ("I'm busy" reply, "= NO IDEA, STAY CALM", WIT facepalm) → Scene C real sticky-note wall + OVERLOADED stamp + "THE SHIELD IS REAL" (WIT burned-out) → Scene D real empty meeting room + two struck speech bubbles ("I need quiet time" = TOO RELAXED @27.48, "this meeting could've been a message" = TOO DANGEROUS @31.70, WIT shocked) → Scene E real desk + real-UI group chat full of "busy" + "OR BOTH" (WIT tiny-defeated).
- 5 distinct real photo backgrounds (office / wood desk / sticky-note wall / meeting room / grey desk), all people-free; chat built in CSS with the real Messenger icon (editorial). 5 distinct WIT poses. All cues pinned to generated `section-06-word-timings.json` (0.86 audio, 38.04s). Word-timings JSON was generated this run (was missing). Re-lint 0 err, snapshots ok, mirror (`hyperframes/review/section-06.html`) synced.
- No MP4/WebM exported (not requested).
- 5 distinct WIT poses: typing → thinking → deadpan-side-eye → facepalm → tiny-defeated. All cues pinned to `section-05-word-timings.json` (0.86 audio, 42.859s). Two custom tweens: poll bars grow (15/85), Trello card translates DOING→DONE over 1.5s.
- No MP4/WebM exported (not requested).

## Stale / Regeneration Notes

- Section 1 render is current against its voiceover (0.84) and visual plan.
- Sections 2-7 not rendered.
- Delivery mismatch: Section 1 audio is plain/0.84; Sections 4-7 are pause-tuned/0.86. If Section 1 audio is regenerated at 0.86, the duration changes - regenerate word timings and re-pin Section 1 cues, then re-snapshot.

## Caption (2026-06-25)

- Multi-language captions exported to `output/captions/` - **22 languages**, one `<language>.srt` each (arabic, bangla, chinese-simplified, chinese-traditional, english, french, german, hindi, indonesian, italian, japanese, korean, malayalam, polish, portuguese, russian, spanish, tamil, telugu, thai, turkish, vietnamese).
- Timing base: the verified English `output/captions.srt` (94 cues, first `00:00:00,380`, last ends `00:04:25,000` == combined audio `265s`; the whisper tail-glitch fix is already baked into this verified file). Parsed into a per-cue `_segments.json`; every language reuses that exact timing - translations only swap text, never the timestamps.
- Each non-English track is a per-cue translation (exactly 94 cues, same order; "Wi-Fi"/tech terms preserved) written via `write-translated-srt.mjs`.
- Verified: all 22 files have 94 cues with **byte-identical timestamps** to `english.srt` (0 mismatches); non-Latin scripts (Arabic, CJK, Indic, Thai, Cyrillic) render clean UTF-8, no mojibake. Compatibility `output/captions.srt` (English) left in place.

## Next Step Boundary

Next workflow step: `Review`

Do not continue into review, upload, or learning until the user asks for the next skill or explicitly requests that step.
