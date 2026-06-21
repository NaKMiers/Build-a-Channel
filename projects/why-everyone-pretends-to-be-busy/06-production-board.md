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
| Unified preview | 1000 | | | reserved |
| Section 1 | 1001 | http://localhost:1001/#project/Build%20a%20Channel | http://localhost:1001/api/projects/Build%20a%20Channel/preview/comp/index.html | running |

Note: the preview server resolves the project id/title to the workspace root name (`Build a Channel`) while `dir` points to the section folder — documented HyperFrames behavior on this setup.

## Section Render Index

| # | Section | Status | Port | Preview project | Source | Checks | Export file | Notes |
|--:|---|---|--:|---|---|---|---|---|
| 1 | Hook: The Busy Trap | built — ready for review | 1001 | `section-previews/section-01-hook-the-busy-trap/` | visual plan + generated word timings | lint 0 err / validate 0 err / snapshots ok | none (no export requested) | 3 scenes, 8 cues, 4 WIT beats |
| 2 | Reframe | not rendered | 1002 | — | — | — | — | voiceover 0.84 |
| 3 | Busy Became A Status Symbol | not rendered | 1003 | — | — | — | — | voiceover 0.84 |
| 4 | Your Apps Invented Emergencies | not rendered | 1004 | — | — | — | — | voiceover 0.86 |
| 5 | Visible Work Beats Quiet Thinking | not rendered | 1005 | — | — | — | — | voiceover 0.86 |
| 6 | "I'm Busy" Is A Shield | not rendered | 1006 | — | — | — | — | voiceover 0.86 |
| 7 | Payoff: Activity Is Not Value | not rendered | 1007 | — | — | — | — | voiceover 0.86 |

## Shared Asset Rules

- Video-level assets: `projects/why-everyone-pretends-to-be-busy/assets/` (fonts/, wit/, visual-references/, thumbnails/)
- Section asset junction rule: junctions fail to serve under HyperFrames CLI on this Windows setup, so each section preview uses a minimal COPIED `assets/` working set (documented exception, per render memory).
- Attribution file: `assets/visual-references/section-01-hook-the-busy-trap/ATTRIBUTION.md` (Public Domain bases, brand-free, people-free)

## Active Section Notes

- Section 1 motif: calendar fills with fake urgency (Scene A) → quiet desk reads as "lazy" (Scene B) → calendar becomes a cage with WIT trapped inside a phone screen (Scene C). A/C share the calendar base as an intentional bookend (distinct grades + cage bars).
- Scene bases (final, 2026-06-22): clean real-world CC0 stock photos sourced via Openverse — `base-deskwork.jpg` (Scene A warm work desk), `base-deskcalm.jpg` (Scene B bright minimal desk), `base-deskwork-cage.jpg` (Scene C cooled + cage bars). Motif shifted from literal calendar to work-desk (no clean people-free calendar photo findable). Iteration history: dingy PD photos (rejected) → flat-illustrated CSS (rejected) → CC0 real photos (current). No image generator available. Cue timing/WIT unchanged. See section IMPLEMENTATION.md + ATTRIBUTION.md.
- All cue times pinned to generated `section-01-word-timings.json`. The dry button "There is a difference." lands at ~19.96–21.0 (later than the visual plan's estimate).
- WIT: 4 beats, each ≥1/3 frame, faces safe, no label/face collisions, verified in snapshots.
- No MP4/WebM exported (not requested).

## Stale / Regeneration Notes

- Section 1 render is current against its voiceover (0.84) and visual plan.
- Sections 2-7 not rendered.
- Delivery mismatch: Section 1 audio is plain/0.84; Sections 4-7 are pause-tuned/0.86. If Section 1 audio is regenerated at 0.86, the duration changes — regenerate word timings and re-pin Section 1 cues, then re-snapshot.

## Next Step Boundary

Next workflow step: `Review`

Do not continue into review, upload, or learning until the user asks for the next skill or explicitly requests that step.
