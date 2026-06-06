# 07 Section 01 Replan

Video:
`Why Everyone Pretends To Be Busy`

Section:
`01 Hook`

Status:
`review fix plan before Section01Hook rebuild`

Timing source:
`voiceover/section-01-hook/section-01-voice-performance-map.json`

Accepted audio:
`voiceover/section-01-hook/scratch-audio/section-01-hook-young-fast-am_adam-1.05.mp3`

Duration:
`24.085s`

## Review Fix Principle

The section should now be built as cue-driven evidence boards:

```text
real-world image or generated real-looking image -> WIT reaction -> cue-timed label -> tiny joke motion
```

Timing comes from the voice, not from transition rhythm.

Implementation order:

1. remove the old repeated paper-snap transition layer
2. retime cue-critical text and objects to the spoken words
3. use one continuous board when the background is the same
4. reintroduce only short, content-specific transitions where the background actually changes

## Sentence And Visual Groups

| Group | Time | Spoken Script | Visual Job | WIT Pose | Image Use | On-Screen Text / Marks | Animation | Transition Decision |
|---:|---:|---|---|---|---|---|---|---|
| 1 | `0.00-2.23` | `Here is something weird about modern life.` | Show a normal desk, then make it suspicious. The joke is that normal adult life already looks like a crime scene if labeled correctly. | `neutral-default`, lightly alert | Real desk photo as background. Add generated desk/task image as a small evidence-photo texture only if the frame needs extra lived-in detail. | `WEIRD?` on `weird` at `0.926`; small note `modern life` around `1.46`; keep `REAL WORK` visible but not too loud yet. | WIT enters calmly, `WEIRD?` stamps in, tiny red arrow points toward the laptop/task. | Start clean. No opening transition. |
| 2 | `2.23-4.51` | `The less time you have to do real work,` | Turn the calendar into pressure. The viewer should see time shrinking before the sentence finishes. | `suspicious-detective` | Real wall-calendar background plus generated `calendar-cage-generated.png` as a real-looking paper-cage cutout. | `LESS TIME` at `2.481`; `REAL WORK` at `3.783`; red squeeze marks around the task card. | Calendar blocks pop around WIT on `less time`; the real-work card gets boxed in on `real work`. | Background changes from desk to calendar, so use a quick calendar-card slam transition before this board. |
| 3 | `4.51-5.98` | `the more professional you look.` | Same calendar pressure becomes fake status. Do not change background; the joke is the same clutter suddenly being respected. | `confused` or same WIT with fake tie/badge | Same real wall-calendar background and same generated calendar-cage cutout. | `PROFESSIONAL?` at `4.961`; oversized badge/tie appears after the word lands. | Fake badge pops on WIT; tie drops in a little too dramatically. | No transition because this is the same calendar world. |
| 4 | `5.98-10.64` | `If your calendar is full, your inbox is exploding, and your phone keeps making tiny panic noises,` | Make the list physical: calendar card, inbox card, phone notification image, then panic marks. | `phone-bill-panic` | Real phone/laptop desk background plus generated `phone-notifications-generated.png` as a photo cutout. | `CALENDAR` at `6.464`; `INBOX` at `7.582`; `PHONE` at `8.949`; `tiny panic` at `9.942`. | Each object appears exactly on the named word; phone buzzes briefly on `panic noises`; WIT shakes only during the panic phrase. | Background changes from calendar to phone desk, so use a short phone-buzz transition before this board. |
| 5 | `10.64-12.19` | `people assume you are important.` | Convert fake emergency into social approval. The viewer should feel the unfairness: nothing improved, but the busy person gets a medal. | `shocked` | Same real phone/laptop desk background and notification cutout. | `IMPORTANT` at `11.601`; small medal text `very needed`; tiny crowd silhouettes. | Crowd appears on `people assume`; medal stamps on `important`. | No transition because the background is the same phone desk. |
| 6 | `12.19-16.73` | `But if you sit quietly and think about one hard problem, people may assume you are lazy.` | Abruptly calm the frame. Quiet thinking should look productive but socially suspicious. | `thinking` | Real calm desk/laptop/calculator background plus generated `quiet-task-judgment-generated.png` as a judgment-arrow cutout. | `HARD PROBLEM` around `14.389`; `LAZY?` at `16.266`; red arrows point at WIT, not the task. | The board enters quietly. Task card appears early; judgment arrows and `LAZY?` wait until the voice says the judgment. | Background changes from phone chaos to calm desk, so use a brief quiet-paper blink transition. |
| 7 | `16.73-19.60` | `Or unemployed. Or having a small spiritual crisis.` | Deadpan pile-on. Same calm thinking frame gets absurd wrong labels. | `tiny-defeated` | Same calm desk and same judgment cutout. | `UNEMPLOYED?` at `17.114`; `NO OUTPUT` between labels as a small joke; `SPIRITUAL CRISIS?` at `18.879`. | Wrong labels stamp one by one, flat and quick. | No transition because this is the same judgment world. |
| 8 | `19.60-24.085` | `So everyone becomes busy. Or at least, everyone becomes very good at looking busy.` | Pay off the hook: the solution is not work, it is performance. Keep `REAL WORK` untouched while fake visible activity blooms around it. | `typing-on-laptop` | Return to real desk/laptop background. Add generated phone-notification image as a small side cutout and generated desk/task image as texture if needed. | `BUSY` at `20.600`; `empty doc` visible; `LOOKING BUSY` at `23.266`; `REAL WORK` still untouched. | Busy props appear on `busy`; WIT types into empty doc; final label lands on `looking busy`. | Background changes from calm desk to busy desk, so use a red `BUSY` stamp transition before this board. |

## Transition Pass

Remove:

- the old identical `transition-snap` clips at every scene boundary
- any transition between calendar pressure and professional status
- any transition between fake emergency and important medal
- any transition between quiet thinking and wrong labels

Use only:

| Boundary | Transition | Reason |
|---|---|---|
| `desk -> calendar` | quick calendar-card slam | the calendar begins attacking the time cue |
| `calendar -> phone desk` | short phone-buzz smear | the narration moves into fake emergency objects |
| `phone desk -> quiet desk` | quiet paper blink | the scene needs a sudden silence contrast |
| `quiet desk -> looking busy desk` | red `BUSY` stamp | the payoff becomes a performance |

These transitions must stay under `0.16s` and must not cover cue-critical labels.

## Asset Use

Use these existing assets before browsing for more:

- `real-world/home-office-laptop-desk-crop-real-cc0.jpg`
- `real-world/wall-calendar-board-crop-real-cc-by-sa.jpg`
- `real-world/phone-laptop-desk-crop-real-cc0.jpg`
- `real-world/desk-laptop-calculator-real-cc0.jpg`
- `generated/calendar-cage-generated.png`
- `generated/phone-notifications-generated.png`
- `generated/quiet-task-judgment-generated.png`
- `generated/desk-laptop-task-card-generated.png`

No new internet asset is required for this pass because the existing real-world and generated assets already cover every visual beat in Section 1.

## Cue-Critical Labels

These must appear on the spoken cue, not as part of a generic scene entrance:

| Cue | Time |
|---|---:|
| `WEIRD?` | `0.926` |
| `LESS TIME` | `2.481` |
| `REAL WORK` | `3.783` |
| `PROFESSIONAL?` | `4.961` |
| `CALENDAR` | `6.464` |
| `INBOX` | `7.582` |
| `PHONE` | `8.949` |
| `tiny panic` | `9.942` |
| `IMPORTANT` | `11.601` |
| `HARD PROBLEM` | `14.389` |
| `LAZY?` | `16.266` |
| `UNEMPLOYED?` | `17.114` |
| `SPIRITUAL CRISIS?` | `18.879` |
| `BUSY` | `20.600` |
| `LOOKING BUSY` | `23.266` |

## Approval Checks

- `REAL WORK` is visible early and remains untouched at the payoff.
- WIT is never shown as lazy before the judgment label appears.
- Each real or generated image has a clear job, not just background decoration.
- Same-background beats are handled inside one board without transition.
- Labels are readable on the cue frame and do not cover the main evidence.
- The section is still funny when paused every `3-5s`.
