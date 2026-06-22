# Section 2 Render Implementation

Video: `Why Everyone Pretends To Be Busy`
Section: `Section 2: Reframe: Looking Busy vs Doing Work`
Status: `section preview built — ready for review`

## Result
- Preview project: `section-previews/section-02-reframe-looking-busy-vs-doing-work/`
- Port: `1002`
- Studio URL: `http://localhost:1002/#project/Build%20a%20Channel`
- Direct comp URL: `http://localhost:1002/api/projects/Build%20a%20Channel/preview/comp/index.html`
- Runtime: `28.949s`
- Voiceover: `voiceover/section-02-.../...david23-am_eric-0.84.mp3` (0.84 plain)
- Visual plan: `visual-plan/section-02-reframe-looking-busy-vs-doing-work/`

## Timing Source
Generated `voiceover/section-02-.../section-02-word-timings.json` via Whisper (transformers.js,
whisper-tiny.en). Tail had a chunk-boundary duplication (section ~29s, near the 30s chunk); cleaned
to 113 monotonic words ending "see." @ 28.85. Every cue/reveal pinned to real word starts.

## Bases (real CC0 photos via Openverse — per updated visual-plan sourcing)
- Scene A: `base-typing.jpg` (CC0 StockSnap) — hands on laptop, no face, no logo
- Scene B: `base-think.jpg` (CC0 rawpixel) — blank open notebook + coffee on dark wood, top-down
- Scene C: `base-meeting.jpg` (CC0 rawpixel) — empty meeting room, no people
- Scene D: `base-idea.jpg` (CC0 StockSnap) — single glowing filament bulb on black
- assets are a COPIED local working set (junctions fail under HyperFrames CLI on this Windows setup)
- REVISION 2026-06-22: Scenes B and D originally reused S1's minimal white desk (identical to each other); replaced with distinct base-think (notebook) and base-idea (bulb) per user review for variety. All 4 bases now distinct.

## Render Review-Prevention Pass
- voice cue map from word-timings: yes
- big-scene rhythm: 4 distinct ideas (typing/quiet/meeting/quiet); B+D quiet bookend (intentional)
- cue density: 6 cues / 29s
- motion: hard-show default; smash only on "> THE WORK ITSELF" and "IGNORE WHAT WE CAN'T"
- WIT density: 3 beats (A:0, B:1, C:1, D:1); ~1/2 frame; faces safe; labels in separate zones
- markup: labels explain the beat; no decorative marks
- scene differentiation: typing / quiet / meeting / quiet(callback)
- mechanics: scenes on tracks 1/3/4/5, cues on track 2 (sequential, no overlap), deterministic GSAP

## Verification
- lint: 0 errors, 1 non-blocking warning (track-2 density = 6 cues)
- validate: 0 errors
- snapshots: contact sheet + 7 frames; clean bases, readable labels, safe WIT crops
- export: none (not requested)

## Notes
- Motif note: like S1, the literal "calendar" isn't shown (no clean people-free calendar photo); the reframe is carried by typing/meeting/quiet-desk photos + labels.
- WIT typing pose at C4 is cropped to torso/head (laptop below frame edge) — reads as "WIT at the visible-work scene"; acceptable.
- Delivery: S2 audio is 0.84 plain (matches S1); S4-7 are 0.86 pause-tuned. Whole-video delivery unification still pending per 04-voiceover.md.
