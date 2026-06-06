# 13 Section 03 Implementation

Video:
`Why Everyone Pretends To Be Busy`

Section:
`03 Busy Became Status`

Status:
`draft implemented for review`

## Result

Composition:
`Section03BusyStatus`

Runtime:
`46.763s`

Preview rule:
Section 3 is separated from Section 1 and Section 2 for review.
Do not assemble sections into one long composition until the user asks after all sections are approved.

Voice:
`section-03-busy-status-young-fast-am_adam-1.05.mp3`

## Board Plan Implemented

| Board | Local Time | Visual |
|---|---:|---|
| `status-became-status` | `0.000-4.700` | Status-desk image, `BUSY = STATUS`, medal, WIT confused |
| `status-important` | `4.700-13.200` | `"I'm so busy"` translated into `PLEASE UNDERSTAND: IMPORTANT` |
| `status-nobody-asked` | `13.200-17.000` | Small-talk table, `How are you?` / `Busy.`, `NOBODY ASKED` |
| `status-busy-emotion` | `17.000-21.000` | Deadpan emotion list: happy, sad, busy crossed out, `NOT AN EMOTION` |
| `status-demand-value` | `21.000-30.200` | Demand corkboard, value ladder, `DEMAND = VALUE` |
| `status-professional-network` | `30.200-36.300` | Generic professional network screen, no real logo, `PUT IT ON PRO NETWORK` |
| `status-meeting-tower` | `36.300-43.000` | Meeting/document tower, meetings/calls/updates/planning docs tags |
| `status-near-work` | `43.000-46.763` | Near-the-work desk, `NEAR THE WORK`, actual work remains pending |

## Asset Direction

Used generated project-owned Section 3 images instead of external downloads because browsing did not surface clean useful sources and this section needed logo-free professional/status imagery.

Generated images live in:
`assets/section-03-busy-status/generated`

Source notes:
`assets/section-03-busy-status/source-notes.md`

## Style

- Static boards only.
- Hard cuts only.
- No transition overlays.
- No real app logos.
- No real LinkedIn logo.
- Handwritten labels stay large and readable.
- WIT is socially trapped, not lazy.

## Verification

`npm run check` in `section-previews/section-03-busy-status`:

- lint passes with warnings
- validate passes, no console errors
- inspect passes, `0` layout issues

`npm run check` in `hyperframes` after mirroring Section 3:

- lint passes with warnings
- validate passes, no console errors
- inspect passes, `0` layout issues

Known warnings:

- duplicate media discovery warning from reused static board image
- dense track warning because the `8` static Section 3 boards are inline for easier timing review

## Section Storage

- Active Section 3 preview source: `section-previews/section-03-busy-status/index.html`
- Canonical standalone source: `hyperframes/review/section-03.html`
- Mirrored current HyperFrames source: `hyperframes/index.html`

## Preview

Studio:
`http://localhost:3023/#project/section-03-busy-status`

Direct composition:
`http://localhost:3023/api/projects/section-03-busy-status/preview/comp/index.html`
