# Section 1 Render — Design

Video: `Why Everyone Pretends To Be Busy`
Section: `Section 1: Hook: The Busy Trap`
Composition id: `Section01Hook`
Duration: `21.056s` (matches voiceover MP3)
Port: `1001`

## Big Scenes (3)

1. `scene-a-calendar` (0–11.0s, track 1): bright wall-calendar photo = "the overload"
2. `scene-b-desk` (10.95–16.06s, track 3): calm minimal desk = "sit quietly and think"
3. `scene-c-cage` (16.02–21.056s, track 4): cooler calendar + CSS vertical cage bars = "looking busy = trapped" (intentional A/C bookend)

## Cues (8, track 2, pinned to word timings)

| Cue | Start | Voice cue (word) | Content | Motion |
|---|--:|---|---|---|
| 1 | 0.30 | "Here's a" | REAL WORK folder | hard-show |
| 2 | 2.50 / 4.32 | "less time" / "important" | contradiction label + emphasis pulse | hard-show + pulse |
| 3 | 5.48–8.14 | "full calendar"/"inbox"/"phone"/"panic" | URGENT, 99+, red dots, GIANT panic WIT | smash + staggered show |
| 4 | 9.18 | "this person matters" | "THIS PERSON MATTERS" label | hard-show |
| 5 | 11.10 / 11.48 | "sit quietly" | cut to desk; thinking WIT; THINKING... | hard-show |
| 6 | 13.34 / 14.32 / 14.90 | "lazy" / "asleep" | deadpan WIT; LAZY? stamp; (OR ASLEEP) | hard-show + stamp smash |
| 7 | 16.40 / 19.12 | "everyone gets busy" / "looking" | cut to cage; trapped WIT; LOOKING BUSY | hard-show |
| 8 | 20.02 | "There is a difference" | dry button label | small smash |

## WIT (4 beats, shared poses)

- C3 `wit-pose-holding-phone-panic.png` — giant ~1/2 frame, lower-right half-body rise
- C5 `wit-pose-thinking.png` — ~1/3 frame, lower-left
- C6 `wit-pose-deadpan-side-eye.png` — ~1/2 frame, lower-right side peek
- C7 `wit-pose-trapped-by-app-screen.png` — ~1/2 frame, centered behind cage bars (pose is WIT inside a phone outline → reinforces theme)

All faces/glasses fully in frame; only lower body exits the bottom edge. WIT in front of cage bars so bars never cross the face.

## Style

- Handwritten labels (PatrickHandLocal local woff2), cream/blue/yellow cards, red markup for URGENT/LAZY?/contradiction.
- Hard-show is default; impact (smash/pulse) only on "important", URGENT, LAZY?, and the final button.
- Scene grades: A bright, B calm, C cool/dark — differentiates the A/C calendar bookend.

## Checks

- lint: 0 errors, 1 non-blocking warning (track 2 density = 8 cues; intentional for this hook)
- validate: 0 errors (contrast warnings are timeline-sampled on hidden cues; labels have solid light backgrounds and read clearly in snapshots)
- snapshots verified: 0.8/4.4/7.6/9.6/11.7/14.6/17.0/19.4/20.4s
