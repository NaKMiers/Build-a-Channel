# Section 1 Render Implementation

Video: `4 Reasons You Can't Get Your First Job Anymore`

Section: `Section 1: Hook: The Ladder Is A Circle`

Status: `built + QA-passed, preview live, awaiting owner review`

## Result

- Preview project: `previews/1-the-ladder-is-a-circle/`
- Source visual plan: `visual-plan/section-01-the-ladder-is-a-circle/section-01-the-ladder-is-a-circle-visual-plan.md`
- Word timing source: `voiceover/section-01-the-ladder-is-a-circle/section-01-word-timings.json`
- Port: `1001`
- Studio URL: `http://localhost:1001/#project/1-the-ladder-is-a-circle`
- Direct composition URL: `http://localhost:1001/api/projects/1-the-ladder-is-a-circle/preview/comp/index.html`
- Composition id: `Section01LadderCircle`
- Runtime: `19.226s`, clamped to the approved Alan voiceover
- Visual structure: `6` hard-cut scenes on tracks `1-6`; narration on track `30`
- Audio: approved Alan narration only. No extra sound assets were supplied, so no unlisted SFX were invented.

## Big Scene Plan Implemented

| Scene | Local Time | Narration | Visual Result | Main Motion |
|---:|---:|---|---|---|
| 1.1 | `0.00-1.36` | You just graduated. | Proud graduate WIT, diploma still life, `GRADUATED` stamp | one paper-forward beat and stamp impact |
| 1.2 | `1.36-4.96` | You find an entry-level job listing. Good. | Fictional job card, cursor click, teal `ENTRY-LEVEL`, green `GOOD.` | cursor travel, click state, one confirmation pop |
| 1.3 | `4.96-7.62` | Three years of experience required. | Same card pinned to cork, panicked WIT, manually combined `3 YEARS` treatment | hard-show requirement text |
| 1.4 | `7.62-12.34` | Experience for job, job for experience. | One access door switches from an `EXPERIENCE` pass opening `JOB` to a `JOB` pass opening `EXPERIENCE` | phrase-timed hard-shows only |
| 1.5 | `12.34-15.84` | The career ladder is now a circle. | Normal ladder behind giant deadpan WIT bends into a closed ring | rung and rail morph from straight to circular |
| 1.6 | `15.84-19.226` | Four reasons and how to get in. | Clean stairwell callback with one large promise headline and no WIT | four hard-show cue groups, no decorative motion |

## Cue Map

| Time | Voice Cue | Visual Cue |
|---:|---|---|
| `0.44` | graduated | `GRADUATED` stamp lands |
| `1.56` | find | job card hard-shows |
| `2.02` | entry | cursor clicks and pill flips teal |
| `2.42` | job | `JUNIOR ANALYST` appears |
| `3.90` | Good | green `GOOD.` card pops |
| `4.96` | Three | owner-combined `3 YEARS` treatment hard-shows |
| `5.66-6.08` | experience / required | remaining requirement text and red underline complete |
| `7.96-8.88` | experience / job | `EXPERIENCE` pass enters the red reader, then the door receives its `JOB` plate |
| `9.54` | You | first credential and destination clear from the same access mechanism |
| `10.18-10.72` | job / experience | `JOB` pass enters the reader, then the door receives its `EXPERIENCE` plate |
| `13.62` | ladder | complete straight ladder appears |
| `13.90-14.60` | is now a circle | ladder bends and closes; badge lands on `circle` |
| `16.18` | four | giant red `4 REASONS` hard-shows |
| `16.78` | you | `YOU CAN'T GET` hard-shows |
| `17.38` | your | `YOUR FIRST JOB` hard-shows as one cream destination strip |
| `18.40` | how | `HOW TO GET IN` hard-shows as one teal route strip pointing toward the real stairs |

## Review-Prevention Pass

- Exact word cue map: yes, verified against the 51-token monotonic timing JSON.
- Big-scene differentiation: yes, five distinct bases plus one intentional stairwell callback for the final promise reset.
- WIT density: three appearances across six scenes. Scene 1.6 removes the presenter pose entirely.
- WIT crop and face safety: yes, all faces and glasses stay clear; only intentional lower-body crops remain.
- Motion density: one primary motion idea per scene; remade Scenes 1.4 and 1.6 use hard-shows only after the owner rejected their dense multi-device versions.
- Cue defaults: animated labels and morph rungs are hidden in CSS before their cue, including exact-seek safety at `12.34`.
- Scene transition language: six hard cuts, matching the hook's fast dry rhythm.
- Asset gate: all required files resolve through the preview-local `assets -> ../../assets` symlink. Reused job-card and ladder-rung nodes are intentional motif reuse.
- Phone-size readability: checked from the final contact sheets; cue-critical text sits on cream or teal backing.

## Render-Side Adjustments

1. Scene 1.2's supplied desk photo contains a large decorative motorcycle. A soft background blur and rightward cream wash suppress it so the job card and `GOOD.` remain the immediate hierarchy.
2. Scene 1.4 went through two recoveries. The first rejected version used a receipt, job card, two arrows, and floral lobby and felt extremely chaotic. The simplified equation board then felt too monotonous at the owner-corrected `0:09` timestamp. The current version preserves one active direction at a time but physicalizes it as a credential pass, red reader, and destination door grounded in the real office corridor.
3. Scene 1.5 uses wide but vertically compressed rung copies for the straight state. This preserves visible gaps between rungs behind giant WIT, then restores each rung to normal proportions during the circular morph.
4. Scene 1.6 was completely remade after owner review. The rejected version combined a presenter WIT, an open ladder ring, six rung props, four numbered tabs, a fake doorway, three text devices, and a route arrow inside only `3.386s`. The replacement discards that scene plan and uses one real stairwell callback plus a single left-aligned promise headline built in four hard-show cue groups.
5. Existing owner Studio adjustments in Scenes 1-5 were preserved from the live `index.html`. The Scene 1.3 timeline was minimally reconciled with the manually combined `3 YEARS` text so validation no longer targets a removed element.
6. The approved audio places the promise at `15.84s`. The render preserves that locked upstream timing; moving it earlier requires a script, voiceover, timing, and visual-plan rerun.

## Verification

- Lint: `0 errors`, `2 warnings`. The warnings are intentional duplicate-media notices for the reused listing card and repeated ladder rung.
- Validate: `0 errors`, `0 warnings`, `20` contrast advisories only. Direct cue snapshots confirm the flagged handwritten and cream-card states remain readable.
- Inspect: `0 layout issues` across `23` explicit timestamps.
- Snapshot QA: restored Scene 1.3 was rechecked at `7.0s` in a non-first capture position and contains the original card, WIT, and Studio offset. Scene 1.4 was checked across `9` states from `7.7-12.2s`; only one credential and one destination label are visible at a time, the reader remains stable, and all text is collision-free. Scene 1.6 was checked at `15.9`, `16.3`, `16.9`, `17.5`, `18.5`, and `19.05s`; the final state is collision-free and contains no WIT, ring, tabs, or fake door.
- Snapshot fallback note: the first frame of an earlier targeted run briefly missed one late-decoding WIT PNG. A re-snap and the final full run confirmed the asset is present. This is a capture-tool race, not a composition defect.
- MP4/WebM export: `not created`, because export was not requested.
