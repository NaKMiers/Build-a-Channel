# 05 Production Board

Video: `4 Reasons You Can't Get Your First Job Anymore`

Status: `Section 1 built + QA-passed - awaiting owner review`

Source skill: `render`

Source files:

- `02-script.md`
- `03-voiceover.md`
- `04-visual-plan.md`
- `assets/asset-manifest.md`

## Port Map

| Target | Port | Studio URL | Direct Composition URL | Status |
|---|---:|---|---|---|
| Unified preview | 1000 | `http://localhost:1000/#project/full-video` | `http://localhost:1000/api/projects/full-video/preview/comp/index.html` | reserved, not running |
| Section 1: The Ladder Is A Circle | 1001 | `http://localhost:1001/#project/1-the-ladder-is-a-circle` | `http://localhost:1001/api/projects/1-the-ladder-is-a-circle/preview/comp/index.html` | running |

## Section Render Index

| # | Section | Status | Port | Preview Project | Checks | Export | Notes |
|---:|---|---|---:|---|---|---|---|
| 1 | Hook: The Ladder Is A Circle | `built - awaiting owner review` | 1001 | `previews/1-the-ladder-is-a-circle/` | lint 0 err / validate 0 err / inspect 0 issues / targeted Scene 1.4 and 1.6 remake QA passed | none, not requested | 6 scenes, 19.226s; ladder-to-circle hero motif born; Scenes 1.4 and 1.6 remade |
| 2 | Reason 1: The Rung Is A Ghost | `not rendered` | 1002 | - | - | - | not requested |
| 3 | Reason 2: AI Takes The Practice Rung | `not rendered` | 1003 | - | - | - | not requested |
| 4 | Reason 3: Entry-Level Moved Upstairs | `not rendered` | 1004 | - | - | - | not requested |
| 5 | Reason 4: The Door Barely Moves | `not rendered` | 1005 | - | - | - | not requested |
| 6 | The Risk Receipt Loop | `not rendered` | 1006 | - | - | - | not requested |
| 7 | How To Test A Rung | `not rendered` | 1007 | - | - | - | not requested |
| 8 | Payoff: Check Before You Climb | `not rendered` | 1008 | - | - | - | not requested |
| 9 | Outro: No Experience Required | `not rendered` | 1009 | - | - | - | not requested |

## Shared Asset Rules

- Video-level source of truth: `projects/7-why-you-cant-get-your-first-job/assets/`.
- Section preview `assets` is a symlink to `../../assets`; attribution remains in `assets/ATTRIBUTION.md`.
- Patrick Hand is served locally from `assets/fonts/patrick-hand-latin.woff2`.
- Section 1 audio is a local hardlink beside `index.html`, using the approved Alan file.
- No new composed scene images were made during render. HyperFrames composites the pre-made isolated assets and CSS/SVG markup at runtime.

## Active Section Notes

- Section 1 follows exact word timings. Owner Studio adjustments in Scene 1.3 were restored; Scenes 1.4 and 1.6 override their rejected visual-plan directions. Details are in `previews/1-the-ladder-is-a-circle/IMPLEMENTATION.md`.
- Scene 1.2 uses blur plus a cream focus wash because the supplied laptop photo includes a distracting decorative motorcycle.
- Scene 1.5 was QA-corrected so the straight state reads as a real ladder with visible rung gaps before it morphs into the circle.
- Scene 1.4 went through two recoveries. The chaotic receipt/card/two-arrow loop was first simplified, then the owner clarified that the actual monotonous frame was at `0:09`. The final replacement uses one quiet office corridor and one access-control door: `EXPERIENCE` pass to `JOB`, then `JOB` pass to `EXPERIENCE`.
- Scene 1.6 was completely remade after owner feedback that the presenter, ring, four tabs, fake doorway, and route cluster felt strange and messy. The replacement has no WIT and no ring: one enlarged real stairwell callback plus one promise headline with four hard-show cue groups.
- Existing manual Studio adjustments in Scenes 1-5 were preserved. The removed `s3-three` timeline target was reconciled with the owner's combined `3 YEARS` element.
- The approved narration places the four-reason promise at `15.84s`. This is preserved as upstream-approved timing, not changed at render.
- Linux port floor was lowered to `1000` for this session with `net.ipv4.ip_unprivileged_port_start=1000`. The setting may need to be re-applied after reboot.

## Stale / Regeneration Notes

- No downstream section render, Review, Combine, Caption, Packaging, or final export existed when Section 1 was built, so nothing downstream was made stale or removed.
- Rerunning script, Section 1 voiceover, word timing, visual plan, or Section 1 assets will make this preview stale.

## Next Step Boundary

Next workflow step for this section: `Review`.

Do not export, continue to Section 2, combine, caption, package, upload, or update learning until the user asks for that step.
