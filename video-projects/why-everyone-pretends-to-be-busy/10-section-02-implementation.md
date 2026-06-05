# 10 Section 02 Implementation

Video:
`Why Everyone Pretends To Be Busy`

Section:
`02 Reframe`

Status:
`draft implemented for review`

## Result

Composition:
`Section02Reframe`

Runtime:
`23.9s`

Preview rule:
Section 2 is separated from Section 1 for review.
Do not assemble sections into one long composition until the user asks after all sections are approved.

Voice:
`section-02-reframe-young-fast-am_adam-1.05.mp3`

## Board Plan Implemented

| Board | Local Time | Visual |
|---|---:|---|
| `reframe-not-lazy` | `0.00-3.65` | Real desk photo, crossed-out `lazy?`, `NOT LAZY`, WIT correcting the misunderstanding |
| `reframe-different-problem` | `3.65-5.70` | Same desk photo, `different problem`, small `not this video` note |
| `reframe-appearance-vs-work` | `5.70-10.25` | Calendar photo, split board, `APPEARANCE > WORK?` |
| `reframe-progress-hidden` | `10.25-13.30` | Calm desk photo, `REAL PROGRESS` partly covered by random paper |
| `reframe-busy-visible` | `13.30-16.00` | Phone/laptop photo, `VERY VISIBLE`, a few busy evidence tags |
| `reframe-visible-examples` | `16.00-20.10` | Desk photo, `SERIOUS TYPING`, meetings/messages/professional face tags |
| `reframe-thinking-work` | `20.10-23.90` | Calm desk photo, WIT thinking, `THINKING = WORK` |

## Style

- Static boards only.
- Hard cuts only.
- No transition overlays.
- No word-by-word label pop-ins.
- Real-life photos reused as evidence.
- WIT does not look lazy; WIT corrects, compares, searches, reacts, types seriously, then thinks.

## Verification

`npm run check`:

- lint passes with warnings
- validate passes, no console errors
- inspect passes, `0` layout issues

Explicit Section 2 midpoint inspect:

```text
npx --yes hyperframes@0.6.69 inspect --at 1.4,4.6,7.9,11.8,14.6,18.0,22.0
```

Result:
`0 layout issues across 7 sample(s)`

Known warnings:

- duplicate media discovery warning from reused real-world photos
- dense track warning because the `7` static Section 2 boards are inline for easier timing review

## Section Storage

- Active review file: `hyperframes/index.html` contains Section 2 only.
- Standalone Section 1 source: `hyperframes/review/section-01.html`
- Standalone Section 2 source: `hyperframes/review/section-02.html`
- Assemble sections later only after user approval.

## Review Focus

Ask the user to review:

- whether the `lazy people` correction feels clear
- whether `APPEARANCE > WORK?` lands as the main reframe
- whether `THINKING = WORK` feels valuable, not boring
- whether the section remains simple enough compared with the accepted Section 1 style
