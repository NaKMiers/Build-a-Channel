# 06 Production Board

Video: `Why Everything Is a Subscription Now`

Status: `section render in progress (Section 1 built + previewing)`

Source skill: `render`

Renderer: `HyperFrames 0.6.76`

## Port Map

| Section | Port | Studio URL | Comp URL |
| ------- | ---- | ---------- | -------- |
| 1 Hook | 1001 | `http://localhost:1001/#project/Build%20a%20Channel` | `http://localhost:1001/api/projects/Build%20a%20Channel/preview/comp/index.html` |

(Project id resolves to `Build a Channel` on this setup; build URLs from `/api/projects`, not the folder name.)

## Section Render Index

| # | Section | Status | Duration | Port | Big Scenes | Cues | Preview |
| --: | --- | --- | --: | --: | --: | --: | --- |
| 1 | Hook: It's More Than You Think | built · previewing · awaiting review | 23.509s | 1001 | 3 | 7 | `section-previews/section-01-hook/index.html` |
| 2 | Reframe | not rendered | 39.787s | 1002 | — | — | — |
| 3 | The Spread | not rendered | 54.165s | 1003 | — | — | — |
| 4 | Why Companies Love It | not rendered | 51.093s | 1004 | — | — | — |
| 5 | The Free Trial | not rendered | 53.867s | 1005 | — | — | — |
| 6 | Easy In, No Way Out | not rendered | 53.013s | 1006 | — | — | — |
| 7 | Payoff | not rendered | 54.101s | 1007 | — | — | — |

## Section 1 Build Record

- Preview project: `section-previews/section-01-hook/`
- Composition: `Section01Hook` (1920x1080, duration 23.509s)
- Audio: `section-01-hook-david23-am_eric-0.8.mp3` (sibling copy)
- Word timings: `voiceover/section-01-hook/section-01-word-timings.json` (whisper-tiny.en; tail hand-corrected)
- Assets: local working set (`assets/fonts`, `assets/wit` ×4 poses, `assets/visual-references/section-01-hook` ×3 photos). Junctions 404 with the CLI here, so a minimal copy set is used. Source library + attribution remain at `assets/`.
- Bases: `base-phone-blank-inhand.jpg` (CC0), `base-desk-devices.jpg` / `-dim.jpg` (CC BY) — see `assets/visual-references/section-01-hook/ATTRIBUTION.md`.
- WIT poses: suspicious, shocked, deadpan-side-eye, trapped-by-app-screen (shared library).
- Checks: `lint` 0/0; `validate` 0 errors / 0 warnings / 80 non-blocking contrast warnings; `snapshot` QA at 2.5/6.0/8.5/13.0/17.9/18.3/21.0.
- Review mirror: `hyperframes/review/section-01.html`.
- No MP4/WebM exported (not requested).

## Stale / Regeneration Notes

- Only Section 1 is rendered. Sections 2-7 are `not rendered`.
- No `07-review.md` / `08-upload.md` / `09-self-learning.md` exist yet — nothing downstream is stale.
- If `02-script.md`, the Section 1 voiceover, or the Section 1 visual plan changes, this render becomes stale and must be rebuilt.

## Next Step Boundary

Next workflow step: `Review` (Section 1).

Do not continue into review, upload, or learning until the user asks. Sections 2-7 still need visual-plan + render.
