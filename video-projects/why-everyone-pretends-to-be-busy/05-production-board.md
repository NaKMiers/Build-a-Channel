# 05 Production Board

Video: `Why Everyone Pretends To Be Busy`

Status: `Step 11.1 - Section 1 Hook HyperFrames build ready for review`

Scope:
only Section 1 is planned here. Do not implement Section 2 until Section 1 is built, reviewed, and approved.

## Section 1 Summary

Section:
`Hook`

Estimated runtime:
`0:00-0:25`

Narration word count:
`82`

Purpose:
show WIT trying to do one real task, then getting attacked by fake urgency until he learns to look busy.

Main visual promise:
`REAL WORK` gets buried by calendar, inbox, phone, and social judgment.

Packaging connection:
the first `10` seconds must justify the thumbnail: WIT trapped by a calendar cage and fake emergencies.

Real-world texture rule:
Section 1 must use actual real-world photo layers first, not only vector/CSS shapes. Use [source-notes.md](assets/section-01-hook/source-notes.md), especially the real photo crops in `assets/section-01-hook/real-world/`. Generated images are fallback/support layers for impossible joke visuals, not the main evidence layer.

## Section 1 Narration

```text
Here is something weird about modern life.

The less time you have to do real work, the more professional you look.

If your calendar is full, your inbox is exploding, and your phone keeps making tiny panic noises, people assume you are important.

But if you sit quietly and think about one hard problem, people may assume you are lazy. Or unemployed. Or having a small spiritual crisis.

So everyone becomes busy. Or at least, everyone becomes very good at looking busy.
```

## Scene Data Plan

Timing source:
estimated word timings from [word-performance-map.json](voiceover/word-performance-map.json).

Replace these timings after Section 1 voice generation and forced alignment.

| Board ID | Start | Duration | Narration Cue | Board Type | On-Screen Text | Visual | WIT Action | Audio / Timing Notes |
|---|---:|---:|---|---|---|---|---|---|
| `hook-real-work-desk` | `0.00` | `2.23` | `Here is something weird about modern life.` | situation | `REAL WORK` | Use `real-world/home-office-laptop-desk-crop-real-cc0.jpg` as the real desk/laptop background. Add WIT and a clean `REAL WORK` card on top. | WIT sits ready to work, neutral but alert. | Start cleanly; no long opening breath. |
| `hook-calendar-closes-in` | `2.23` | `2.22` | `The less time you have to do real work` | suspicion | `LESS TIME` | Use `real-world/wall-calendar-board-crop-real-cc-by-sa.jpg` as the real calendar texture. Add extra calendar blocks as overlays forming a cage. | WIT notices the blocks closing in. | Calendar blocks should pop in on `less time`, not before. |
| `hook-professional-badge` | `4.45` | `1.53` | `the more professional you look` | correction | `PROFESSIONAL?` | Use `real-world/wall-calendar-board-crop-real-cc-by-sa.jpg`, now with fake badge/tie/checkmark pasted over WIT. Keep it collage-like, not polished. | WIT looks confused, not proud. | Red question mark appears on `professional`. |
| `hook-fake-emergency-stack` | `5.98` | `4.52` | `calendar is full... inbox is exploding... phone... panic noises` | evidence | `BUSY?` | Use `real-world/phone-laptop-desk-crop-real-cc0.jpg` as the real phone/laptop desk texture. Add generic inbox panel, calendar card, and notification bubbles. | WIT gets buried, small panic shake. | One object appears per list item: calendar, inbox, phone, panic bubbles. Topic and contradiction must be clear before `0:10`. |
| `hook-important-medal` | `10.50` | `1.69` | `people assume you are important` | reaction | `IMPORTANT` | Tiny anonymous crowd applauds. Medal appears over trapped WIT. | WIT is trapped but receives a medal anyway. | Medal lands on `important`. Keep the joke dry, not celebratory. |
| `hook-quiet-thinking-judged` | `12.19` | `4.54` | `But if you sit quietly... people may assume you are lazy` | before_after | `LAZY?` | Use `real-world/desk-laptop-calculator-real-cc0.jpg` or `real-world/home-office-laptop-desk-crop-real-cc0.jpg` as calm desk texture. Add generated `quiet-task-judgment-generated.png` only as a support overlay if needed for arrows. | Quiet WIT thinks; society judges him. | Do not make quiet WIT look lazy. Make him clearly thinking about a hard task. |
| `hook-wrong-labels` | `16.73` | `2.87` | `Or unemployed. Or having a small spiritual crisis.` | reaction | `NOT WORKING?` | Continue `generated/quiet-task-judgment-generated.png`. Add stamp-like paper labels over the real desk texture. | WIT stares deadpan. | Wrong labels stamp one by one; keep the deadpan beat short. |
| `hook-looking-busy` | `19.60` | `4.49` | `So everyone becomes busy... looking busy.` | payoff | `LOOKING BUSY` | Return to `real-world/home-office-laptop-desk-crop-real-cc0.jpg`, but now add messy notification/calendar overlays. `REAL WORK` remains untouched. | WIT types seriously into an empty document. | End with hard cut readiness for Section 2. `REAL WORK` must still be visible and untouched. |

Total planned duration:
`24.085s`

## Cue-Critical Words

These words need visible support on or just before the spoken cue:

| Word / Phrase | Visual Support |
|---|---|
| `weird` | calm desk begins to feel suspicious |
| `real work` | `REAL WORK` task card |
| `less time` | calendar cage closes |
| `professional` | fake badge and `PROFESSIONAL?` label |
| `calendar` | calendar blocks |
| `inbox` | inbox panel |
| `phone` | phone with notification bubbles |
| `panic noises` | tiny panic bubbles / buzz marks |
| `important` | medal and crowd |
| `lazy` | red `LAZY?` judgment label |
| `busy` | busy cage / fake typing |
| `looking busy` | final `LOOKING BUSY` label |

## Section 1 Asset Plan

### WIT Poses

Use existing reusable poses if available. If exact pose does not exist, approximate with the closest WIT pose during the first rough pass.

| Needed Pose | Purpose |
|---|---|
| `neutral-sitting` | opening real work desk |
| `suspicious` | noticing calendar cage |
| `confused` | professional badge gag |
| `panic` or `trapped` | fake emergency stack |
| `deadpan` | wrong labels |
| `typing-serious` or `working` | looking busy payoff |

### UI / Object Assets

Use real raster image texture first, then add self-made vector/CSS objects in HyperFrames as labels, overlays, and jokes:

- `real-world/home-office-laptop-real-cc0.jpg`
- `real-world/home-office-laptop-desk-crop-real-cc0.jpg`
- `real-world/phone-laptop-desk-crop-real-cc0.jpg`
- `real-world/desk-laptop-calculator-real-cc0.jpg`
- `real-world/wall-calendar-board-crop-real-cc-by-sa.jpg`
- `generated/section-01-real-world-reference-contact-sheet.png`
- `generated/desk-laptop-task-card-generated.png`
- `generated/calendar-cage-generated.png`
- `generated/phone-notifications-generated.png`
- `generated/quiet-task-judgment-generated.png`

Create these as self-made vector/CSS overlays unless a reusable asset already exists:

- `task-card-real-work`
- `desk-laptop-simple`
- `calendar-block`
- `calendar-cage`
- `fake-inbox-panel`
- `phone-notification-panel`
- `notification-bubble`
- `panic-buzz-mark`
- `important-medal`
- `tiny-crowd-silhouettes`
- `red-judgment-arrow`
- `wrong-label-stamp`
- `empty-document`

### Labels

All labels should be handwritten-looking and large enough for mobile review:

- `REAL WORK`
- `LESS TIME`
- `PROFESSIONAL?`
- `BUSY?`
- `IMPORTANT`
- `LAZY?`
- `NOT WORKING?`
- `LOOKING BUSY`

## HyperFrames Implementation Notes

Recommended board elements:

```html
<section
  class="board board--situation"
  data-board-id="hook-real-work-desk"
  data-board-type="situation"
  data-start="0.00"
  data-duration="2.23"
>
```

Create Section 1 as its own composition first:

```text
Composition: Section01Hook
Target duration: 24.085s
```

Later, the same boards can be reused inside:

```text
Composition: FullVideo
```

Do not build later sections in this pass.

## Voiceover

Voice:
`David23`

Pacing:
young, dry, clear, faster hook pacing.

Estimated Section 1 duration:
`24-25s`

Generation rule:
generate only Section 1 voice first. Do not generate full-video voiceover until Section 1 pacing and tone are approved.

Pronunciation notes:

- `professional`: clear, slightly dry emphasis
- `panic noises`: light comic emphasis, not cartoonish
- `spiritual crisis`: flat deadpan
- `looking busy`: dry payoff

Optional fillers:
disabled for Section 1.

Reason:
the hook should be clean and easy for English learners. Use breath and pauses instead of spoken fillers.

Step 10.1 status:
voice-test package implemented in [voiceover/section-01-hook/README.md](voiceover/section-01-hook/README.md).

Scratch pacing audio:

- `voiceover/section-01-hook/scratch-audio/section-01-hook-young-fast-am_adam-1.05.mp3`

Important:
this scratch file uses `am_adam`, not approved `David23` / `am_eric`, because the local HyperFrames TTS voice list does not currently expose `am_eric`.
Use it for timing and young-tone direction only.
Keep only one preview audio file in the folder; do not store both MP3 and WAV unless there is a specific production need.

Current timing recommendation:
retime Section 1 boards around `24.085s`.

## Review Checklist For Section 1

- [ ] Hook shows the topic by second `3`.
- [ ] Contradiction appears by second `5`.
- [ ] WIT's emotional position is clear by second `8`.
- [ ] Thumbnail promise is paid off by second `10`.
- [ ] `REAL WORK` remains visible and untouched.
- [ ] WIT does not look lazy before the system attacks him.
- [ ] Labels are readable at mobile size.
- [ ] No real app logos are used.
- [ ] Cue-critical labels appear on or just before the spoken cue.
- [ ] Punchline labels are not visible too early.
- [ ] The final board leads naturally into Section 2.

## Section 1 Approval Gate

Section 1 can move to implementation when:

```text
Production board: approved
Voice test plan: approved
Assets: feasible with existing WIT/CSS/vector objects
No unresolved hook logic issues
```

Section 1 can move to Section 2 only after:

```text
Section01Hook is built
Section01Hook is previewed
timing/layout/joke fixes are applied
the user approves Section 1
```

## Step 11.1 Implementation Result

HyperFrames project:
[hyperframes](hyperframes)

Composition:
`Section01Hook`

Duration:
`24.085s`

Accepted voice timing source:
`hyperframes/assets/voiceover/section-01-hook-young-fast-am_adam-1.05.mp3`

Preview:
`http://localhost:3017/#project/hyperframes`

Direct composition preview:
`http://localhost:3017/api/projects/hyperframes/preview/comp/index.html`

Paused-frame QA:
`hyperframes/qa/section01-contact-sheet.jpg`

HyperFrames check:
`npm run check` passes with `0` errors and `0` layout issues.

Remaining warnings:

- duplicate media discovery warning from reused real-world photo assets
- dense track warning from keeping Section 1 boards inline instead of splitting into sub-compositions
- dense transition track warning from keeping paper-snap transitions inline

Render note:
draft MP4 render was attempted, but local rendering is blocked because FFmpeg is not installed on PATH.
The HyperFrames Studio preview is the current Section 1 review surface.
