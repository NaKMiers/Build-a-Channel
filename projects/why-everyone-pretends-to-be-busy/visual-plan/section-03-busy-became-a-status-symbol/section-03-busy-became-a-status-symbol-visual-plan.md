# Section 3 Visual Plan

Video: `Why Everyone Pretends To Be Busy`
Section: `Section 3: Busy Became A Status Symbol`
Status: `revised (v2) — expanded to 5 scenes + varied WIT`

> REVISION 2026-06-22 (per user review): expanded from 3 big scenes to **5** so no scene overstays.
> - Scene A (trophy) now ends after "...important" (~8.4s); a NEW Scene B (coffee-chat, `base-coffee.jpg`) carries "how are you? Busy / not an emotion / everyone tired" (8.4–15.72).
> - The meeting room is split: Scene D (meeting, `base-meeting.jpg`, 26.06–32.42 "responsible/needed/valuable") + a NEW Scene E (wall clock, `base-clock.jpg`, 32.42–45.077 "meetings about meetings / near the work").
> - Scene C (beach) unchanged.
> - WIT poses diversified to 6 distinct: awkward-celebration (C1), talking-front (C3), confused (C4), suspicious (C5), facepalm (C8), tiny-defeated (C9). Replaced the repeated deadpan-side-eye.
> The cue timeline below still applies (cue starts unchanged); the scene base under C3/C4 is now coffee, and under C8/C9 is now the clock. See the render IMPLEMENTATION.md for the as-built 5-scene track map.

## Section Goal

Show the first reason: busy became a status symbol. Saying "I'm so busy" really means "please notice I'm important." It's reflexive, not an emotion; it's even culturally relative (some brag about leisure, some about having no free time); and "needed = valuable" pushes people to fill the day with meetings about meetings until the job is just proving you're near the work.

## Source Inputs

- Voiceover: `voiceover/section-03-busy-became-a-status-symbol/scratch-audio/...david23-am_eric-0.84.mp3` (45.077s, 0.84)
- Word timings: `voiceover/section-03-busy-became-a-status-symbol/section-03-word-timings.json` (generated; cue times REAL)

## Visual Direction

- 3 big scenes, 9 cue states
- Metaphor: busy = a trophy you show off; the cultural opposite brag (beach vs no-free-time); the empty meeting room where "near the work" replaces the work
- WIT path: proud show-off → deadpan → suspicious → facepalm/deadpan
- WIT density: 5 beats (A:2, B:1, C:2)
- Motion: hard-show default; impact on "= NOTICE I'M IMPORTANT", "SAME PLANET OPPOSITE BRAG", "PROVING YOU'RE NEAR THE WORK"
- Bases: 3 distinct — trophy (illustration hero on a warm award-stage backdrop), beach hammock (CC0 photo), meeting room (CC0 photo, distinct from S2's)

## Big Scene Plan

| Big Scene | Local Time | Voice Range | Persistent Base | Why | Reference |
|---|---:|---|---|---|---|
| A — Busy is a trophy | 0:00-15.72 | "The first reason… because everyone is tired" | Gold trophy hero on a warm award-spotlight backdrop | Busy = status symbol = "notice I'm important"; the reflexive "busy" | CC0 trophy PNG (rawpixel) + CSS stage |
| B — Opposite brag | 15.72-26.06 | "it is not the same everywhere… Same planet, opposite brag" | Beach resort hammock | Some cultures brag leisure, some brag no-free-time | CC0 photo (rawpixel) |
| C — Near the work | 26.06-45.077 | "busy sounds responsible… proving you are near the work" | Empty modern meeting room | Needed=valuable → fill day with meetings → "near the work" | CC0 photo (rawpixel), distinct from S2 |

## Cue State Timeline (word-timed)

| Cue | Time | Voice cue (word@s) | Scene | Change | Motion | WIT | Label |
|---|---:|---|---|---|---|---|---|
| C1 | 0.0-2.8 | "busy became"@1.48 | A | trophy + label; WIT shows off | hard-show | awkward-celebration | BUSY = STATUS SYMBOL |
| C2 | 2.8-8.4 | "I'm so busy"@3.8 / "important"@7.84 | A | I'M SO BUSY then = NOTICE I'M IMPORTANT | hard-show + smash | — | I'M SO BUSY / = NOTICE I'M IMPORTANT |
| C3 | 8.4-12.48 | "how are you"@11.34 / "busy"@11.98 | A | speech bubbles | hard-show | — | "HOW ARE YOU?" / "BUSY." |
| C4 | 12.48-15.72 | "emotion"@13.32 / "tired"@15.28 | A | NOT AN EMOTION + WE'RE ALL TIRED; WIT deadpan | hard-show | deadpan-side-eye | (NOT AN EMOTION) / WE'RE ALL TIRED |
| C5 | 15.72-21.1 | "long holidays"@19 | B | cut to beach; SOME BRAG: LONG HOLIDAYS; WIT suspicious | transition + hard-show | suspicious | SOME BRAG: LONG HOLIDAYS |
| C6 | 21.1-26.06 | "no free time"@22.6 / "opposite brag"@24.98 | B | OTHERS BRAG: NO FREE TIME + SAME PLANET, OPPOSITE BRAG | hard-show + smash | — | OTHERS BRAG: NO FREE TIME / SAME PLANET, OPPOSITE BRAG |
| C7 | 26.06-32.42 | "responsible"@26.4 / "needed"@27.68 / "valuable"@31.84 | C | cut to meeting; staggered RESPONSIBLE → NEEDED → VALUABLE | transition + staggered hard-show | — | RESPONSIBLE / NEEDED / VALUABLE |
| C8 | 32.42-39.0 | "meetings"@36.96 | C | MEETINGS ABOUT MEETINGS; WIT facepalm | hard-show | facepalm | MEETINGS ABOUT MEETINGS |
| C9 | 39.0-45.077 | "near the work"@43.75 | C | PROVING YOU'RE NEAR THE WORK; WIT deadpan | smash | deadpan-side-eye | PROVING YOU'RE NEAR THE WORK |

## WIT Pose Plan

| Cue | Pose File | Placement / Scale | Why |
|---|---|---|---|
| C1 | `wit-pose-awkward-celebration.png` | right, ~1/2 frame | showing off "busy" like a prize |
| C4 | `wit-pose-deadpan-side-eye.png` | right side peek, ~1/2 frame | "busy" isn't an emotion |
| C5 | `wit-pose-suspicious.png` | left, ~1/2 frame | side-eye at the opposite brag |
| C8 | `wit-pose-facepalm.png` | right, ~1/2 frame | meetings about meetings |
| C9 | `wit-pose-deadpan-side-eye.png` | right side peek, ~1/2 frame | dry "near the work" payoff |

Density: A:2, B:1, C:2 (5 total for 45s). Faces safe; labels in upper zones, WIT lower/side.

## Reference And Asset Plan

| Asset | Source / Status | Use |
|---|---|---|
| base-trophy.png | CC0 rawpixel (transparent) | Scene A hero on CSS warm stage |
| base-beach.jpg | CC0 rawpixel | Scene B base |
| base-meeting.jpg | CC0 rawpixel | Scene C base |
| 4 WIT poses | shared manifest | C1/C4/C5/C8/C9 |

Note: trophy is a clean illustration PNG (no clean "status" photo found); used as the descriptive hero on a warm award-spotlight backdrop (justified self-made stage, not a bare gradient). Fits the channel's illustration-over-photo style.

## HyperFrames Guidance

- 1920x1080; 3 scenes (tracks 1/3/4), 9 cues (track 2); audio 45.077s.
- All cue starts pinned to word-timings; 0.2s scene-cut fades; impact only on the 3 emphasis labels.
- WIT ~1/2 frame, faces safe; labels upper, WIT lower/side; subtitle-safe lower margin.
- Must not invent: bases, WIT poses, label text, word-timed cue order. Render decides pixel coords/easing/grading + the Scene A stage backdrop.
- Suggested QA snapshots: 1.6 / 7.6 / 11.8 / 14.8 / 19.5 / 24.8 / 28.5 / 37.0 / 43.5s.

## Approval Checks
- reference pass done (Openverse CC0, viewed); bases brand/people-free
- 3 distinct bases; WIT has a job each beat; labels short/learner-friendly
- word-timed; ready for HyperFrames
