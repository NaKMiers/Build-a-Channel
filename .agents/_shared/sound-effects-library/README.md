# Sound Effects Library

Classification: `Core`

Purpose:
define the reusable `Why It Works` sound effect families, naming rules, source rules, and usage limits.

This folder is for channel-wide reusable sound effects only.
One-off effects for a specific future video should live inside that video's own HyperFrames assets folder.

## Core Rule

`Sound effects are punctuation, not animation.`

Use them to make a joke, reveal, or system action land.
Do not use them to make every board feel busy.

## Library Status

This README defines the approved channel-wide library structure.

Reusable audio files can be added later when they are self-made, generated, licensed, or otherwise clearly safe for YouTube use.

## Recommended Folder Shape

```text
.agents/_shared/sound-effects-library/
  README.md
  receipt-printer/
  phone/
  notification/
  marker/
  cash-register/
  paper/
  lock/
  timer/
  keyboard/
  ui/
  source-notes/
```

Only create subfolders when reusable audio files are actually added.

## Naming Rules

Use clear lowercase filenames:

```text
<family>-<variant>-<duration-or-style>.<ext>
```

Examples:

```text
receipt-printer-short-01.wav
phone-buzz-soft-01.wav
notification-pop-tiny-01.wav
marker-scribble-red-01.wav
cash-register-tiny-01.wav
paper-slap-soft-01.wav
lock-click-small-01.wav
timer-jump-short-01.wav
```

Avoid names like:

- `funny sound.mp3`
- `sfx final final.wav`
- `whoosh.wav`
- `download123.mp3`

## Approved Families

| Family | Use For | Default Treatment | Avoid |
| --- | --- | --- | --- |
| `receipt-printer` | bills, hidden costs, fake invoices | short, dry, low volume | long printing loops under narration |
| `phone-buzz` | phone attention, app interruption | soft buzz, one or two pulses | harsh vibration that masks words |
| `notification-pop` | app popups, small reveals | tiny and light | bright game-like reward sounds |
| `marker-scribble` | red corrections, cross-outs, suspicious labels | rough and short | loud squeaky marker effects |
| `cash-register` | tiny money joke, fake payment moment | small, almost pathetic | casino or arcade energy |
| `paper-slap` | documents, bills, bureaucracy | soft paper hit | huge impact sounds |
| `lock-click` | lock-in, subscription trap, account trap | small click | horror or prison-door sounds |
| `timer-jump` | lost time, wasted minutes, countdown jokes | short tick or jump | tense thriller countdowns |
| `keyboard-tap` | forms, fake dashboards, business language | a few quiet taps | long typing beds |
| `ui-error` | failed plan, fake app warning | tiny error beep | loud system alert |
| `stamp-thud` | fake official label, approval, rejection | dry low thud | dramatic trailer hit |
| `page-flip` | quick explanation shift, document reveal | fast and quiet | big paper swishes |

## Usage Limits

Default limits for future videos:

- no effect on ordinary board cuts
- no effect on every text reveal
- no more than `1` effect in a dense narration sentence
- no more than `2` stacked effects unless the stack itself is the joke
- repeat a signature effect only when the repeated joke is intentional

If the timeline feels busy, remove effects before removing narration clarity.

## Placement Rules

Good placements:

- exactly when the red marker line appears
- just after a fake receipt starts printing
- on a phone buzz that interrupts WIT
- when a lock icon closes
- when a timer jumps from `5 minutes` to `2 hours`
- when a label gets stamped with a dumb official name

Bad placements:

- under a key phrase English learners need to hear
- before the viewer sees the visual cause
- after the joke has already passed
- on every WIT reaction
- on every transition

## Volume And Mix Rules

Effects should be:

- lower than narration
- short enough to disappear quickly
- readable without being exciting
- quieter during dense explanation
- placed between words when possible

If an effect makes the viewer notice the edit more than the joke, it is too loud, too long, or unnecessary.

## Source Notes

For every reusable audio file added later, add a short source note in `source-notes/`.

Use this template:

```text
# <filename>

Family:
Source:
Creator:
License/usage terms:
Download or creation date:
Edited by:
Edits made:
Safe for YouTube use: Yes/No
Notes:
```

Do not add unclear copyrighted sounds, ripped game sounds, recognizable app sounds, commercial jingles, or meme audio without explicit approval.

## HyperFrames Use

For future videos:

1. copy only the needed reusable effects into the video's `hyperframes/assets/` folder
2. keep the render self-contained
3. document the copied file in that video's source notes
4. mix against the actual narration, not against silence

Do not edit existing `projects/` unless the user explicitly asks to apply this system to a specific video.
