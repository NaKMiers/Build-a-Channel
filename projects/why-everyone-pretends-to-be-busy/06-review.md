# 06 Review

Video:
`Why Everyone Pretends To Be Busy`

## Section 1 Hook

Status:
`Section 1 static-board remake accepted by user`

Composition:
`Section01Hook`

Preview:
`http://localhost:3021/#project/section-01-hook`

Direct composition:
`http://localhost:3021/api/projects/section-01-hook/preview/comp/index.html`

Timing:
`24.085s`

Accepted voice:
`section-01-hook-young-fast-am_adam-1.05.mp3`

## Review Artifacts

- Contact sheet: [section01-contact-sheet.jpg](hyperframes/qa/section01-contact-sheet.jpg)
- HyperFrames source: [index.html](hyperframes/index.html)
- Design rules: [DESIGN.md](hyperframes/DESIGN.md)
- Attribution notes: [ATTRIBUTION.md](hyperframes/assets/ATTRIBUTION.md)

## Current Pass Notes

- Section 1 was simplified in [08-section-01-simple-remake.md](08-section-01-simple-remake.md).
- The animated cue-by-cue pass from [07-section-01-replan.md](07-section-01-replan.md) was replaced because it felt too busy for a `24s` hook.
- The section now uses `8` static boards with hard cuts only.
- All transition overlays were removed.
- In-board animation was removed; labels and props are visible as static paused-frame jokes.
- Real-world photos remain the base layer, with only one generated notification-photo cutout retained for the busy proof board.
- `REAL WORK` remains visible and untouched by the final board.
- No real app logos are used.
- Only one audio preview file is kept: MP3.

## Accepted Section 1 Lesson

User review:
`Ok now it's good`

What worked:

- `8` static boards over `24.085s`
- hard cuts only
- no transition overlays
- no in-board animation
- one main joke or evidence object per board
- real-world photo texture plus WIT plus short handwritten labels
- generated image use kept to one clear support job instead of a moving collage

What not to repeat:

- do not abuse transitions or micro-animations in short sections
- do not make many objects appear and disappear over a few seconds
- do not treat every spoken word as a new visual event
- do not build a short hook like a dashboard with calendar, inbox, phone, badges, stamps, arrows, and WIT motion all competing
- do not add transitions just because the background changes if the cut itself is clear

Future Section 1 rule:
start from simple Casually Explained-style static boards, then add motion only if a paused-frame joke is already clear and the user asks for more energy.

## Static Board Snapshot Review

Latest cue-frame contact sheet:
[section01-contact-sheet.jpg](hyperframes/qa/section01-contact-sheet.jpg)

Snapshot frames checked:

- `0.9s`: weird desk
- `3.3s`: less time
- `5.2s`: professional
- `8.0s`: busy proof
- `11.4s`: important
- `14.4s`: quiet thinking
- `18.0s`: wrong labels
- `22.0s`: looking busy

## Verification

`npm run check` result:

- lint: passes with warnings
- validate: passes, no console errors, all text passes WCAG AA
- inspect: passes, `0` layout issues

Known warnings:

- duplicate media discovery warning from reused real-world photos
- dense track warning because the `8` static Section 1 boards are inline for easier timing review

Render status:
draft MP4 render is blocked by missing FFmpeg on PATH.

## Section 2 Reframe

Status:
`draft implemented for user review`

Composition:
`Section02Reframe`

Timing:
`0.000-23.900s`

Voice:
`section-02-reframe-young-fast-am_adam-1.05.mp3`

Implementation note:
[10-section-02-implementation.md](10-section-02-implementation.md)

Current pass notes:

- Active Section 2 HyperFrames preview runs separately from Section 1.
- Section 1 remains accepted and is stored separately for later assembly.
- Section 2 uses `7` static boards with hard cuts only.
- No transition overlays or in-board animation were added.
- Real-world photos are reused as visual evidence.
- WIT is used to correct the `lazy people` misunderstanding, compare appearance vs work, show visible busyness, and land `THINKING = WORK`.

Verification:

- `npm run check` passes.
- explicit midpoint inspect at `1.4,4.6,7.9,11.8,14.6,18.0,22.0` passes with `0` layout issues.

Section storage:

- Section 1 preview source: [index.html](section-previews/section-01-hook/index.html), currently Section 1 only.
- Section 2 preview source: [index.html](section-previews/section-02-reframe/index.html), currently Section 2 only.
- Canonical HyperFrames source: [index.html](hyperframes/index.html), currently Section 3 only.
- Standalone Section 1 source: [section-01.html](hyperframes/review/section-01.html).
- Standalone Section 2 source: [section-02.html](hyperframes/review/section-02.html).
- Standalone Section 3 source: [section-03.html](hyperframes/review/section-03.html).
- Do not assemble sections into one long composition until the user asks after all sections are approved.

Preview URLs:

- Section 1 Studio: `http://localhost:3021/#project/section-01-hook`
- Section 2 Studio: `http://localhost:3022/#project/section-02-reframe`
- Section 3 Studio: `http://localhost:3023/#project/section-03-busy-status`
- Section 1 direct composition: `http://localhost:3021/api/projects/section-01-hook/preview/comp/index.html`
- Section 2 direct composition: `http://localhost:3022/api/projects/section-02-reframe/preview/comp/index.html`
- Section 3 direct composition: `http://localhost:3023/api/projects/section-03-busy-status/preview/comp/index.html`

## Section 3 Busy Became Status

Status:
`draft implemented for user review`

Composition:
`Section03BusyStatus`

Timing:
`0.000-46.763s`

Voice:
`section-03-busy-status-young-fast-am_adam-1.05.mp3`

Implementation note:
[13-section-03-implementation.md](13-section-03-implementation.md)

Current pass notes:

- Active Section 3 HyperFrames preview runs separately from Section 1 and Section 2.
- Section 3 uses `8` static boards with hard cuts only.
- Generated project-owned images are used for status-desk, small-talk, demand-value, generic professional-network, meeting-tower, and near-the-work boards.
- No real LinkedIn logo or real app logo is used.
- WIT shows social pressure and work-performance absurdity, not laziness.
- Final board lands `NEAR THE WORK`.

Verification:

- `npm run check` passes in `section-previews/section-03-busy-status`.
- `npm run check` passes in `hyperframes` after mirroring Section 3.
- Both checks report `0` layout issues.

## Two-Port Section Preview

Status:
`configured as separate HyperFrames preview projects; restart the servers from the new projects path before review`

Section 1 source:
[index.html](section-previews/section-01-hook/index.html)

Section 1 preview:
`http://localhost:3021/#project/section-01-hook`

Section 2 source:
[index.html](section-previews/section-02-reframe/index.html)

Section 2 preview:
`http://localhost:3022/#project/section-02-reframe`

Section 3 source:
[index.html](section-previews/section-03-busy-status/index.html)

Section 3 preview:
`http://localhost:3023/#project/section-03-busy-status`

Direct composition checks:

- Section 1: `http://localhost:3021/api/projects/section-01-hook/preview/comp/index.html`
- Section 2: `http://localhost:3022/api/projects/section-02-reframe/preview/comp/index.html`
- Section 3: `http://localhost:3023/api/projects/section-03-busy-status/preview/comp/index.html`

Reason:
the user wants sections reviewed separately.
Do not place Section 2 after Section 1 in one long composition until all sections are approved and the user explicitly asks for assembly.

Operational rule for this video:
each section should run as its own HyperFrames preview project on its own port during review.
Do not use one shared Studio project to switch sections, because the default `index.html` route can make both section links appear to show the same section.
