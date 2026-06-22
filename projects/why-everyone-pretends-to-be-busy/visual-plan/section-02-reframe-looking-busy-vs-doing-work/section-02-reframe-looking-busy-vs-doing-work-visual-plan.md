# Section 2 Visual Plan

Video:
`Why Everyone Pretends To Be Busy`

Section:
`Section 2: Reframe: Looking Busy vs Doing Work`

Status:
`draft visual plan for approval`

## Section Goal

Reframe the topic: this is not about lazy people — modern life rewards the *look* of work over the work itself. Make the contrast visible: busy work is easy to see (typing, meetings, serious screens); real work (thinking) is invisible and hides.

## Source Inputs

- Script: `02-script.md` Section 2
- Voiceover: `voiceover/section-02-reframe-looking-busy-vs-doing-work/scratch-audio/...david23-am_eric-0.84.mp3` (28.949s, 0.84 plain)
- Word timings: `voiceover/section-02-reframe-looking-busy-vs-doing-work/section-02-word-timings.json` (generated; cue times are REAL, not estimated)

## Narration

```text
Now, this is not a video about lazy people hiding from work. That is a different, smaller problem.
This is about something stranger. Modern life often rewards the look of work more than the work itself.
Because real progress is hard to see. Thinking looks like nothing. Solving a problem in your head looks like nothing.
But busy is easy to see. You can see meetings. You can see fast typing. You can see a serious face staring at a screen.
So we trust the things we can see, and we quietly ignore the things we cannot. Which is a problem, because the real work usually hides in the part you cannot see.
```

## Visual Direction

- Big-scene/cue rhythm: 4 big scenes, 6 cue states
- Main visual metaphor: VISIBLE busy work (typing / meeting room) vs INVISIBLE real work (quiet desk)
- WIT emotional path: thinking (real work) → performing visible busy → dry/deadpan conclusion
- WIT density: 3 beats (B:1, C:1, D:1); Scene A is label-only (breathing)
- Motion density: hard-show default; impact only on the thesis "> THE WORK ITSELF" and the staggered visible-list reveals
- Real bases: 4 distinct CC0 photos via Openverse — typing hands (A), blank notebook on dark wood (B), empty meeting room (C), glowing bulb on black (D). No people in any base.
- All four scenes are visually distinct (no reuse). B and D were originally a reused S1 desk; replaced with notebook + bulb per user review for variety.

## Big Scene Plan

| Big Scene | Local Time | Voice Range | Persistent Base Visual | Why This Scene Exists | When To Cut Away | Reference Basis | Asset Path |
|---|---:|---|---|---|---|---|---|
| A — The look of work | 0:00-9.64 | "Now, this is not… the work itself." | Hands typing on a laptop (base-typing), warm | Establish: not laziness; modern life rewards the *look* of work | When narration turns to "real progress is hard to see" | CC0 StockSnap (Openverse) | `assets/visual-references/section-02-reframe-looking-busy-vs-doing-work/base-typing.jpg` |
| B — Thinking is invisible | 9.64-14.30 | "Because real progress is hard to see… looks like nothing." | Blank open notebook + coffee on dark wood (base-think), top-down | Real work / thinking looks like nothing (blank page) | When narration lists visible things | CC0 rawpixel (Openverse) | `.../base-think.jpg` |
| C — You can see busy | 14.30-19.84 | "But busy is easy to see… staring at a screen." | Empty modern meeting room (base-meeting) | The visible world: meetings, typing, serious screens | When narration concludes about trust | CC0 rawpixel (Openverse) | `.../base-meeting.jpg` |
| D — Real work hides | 19.84-28.949 | "So we trust the things we can see… part you cannot see." | Single glowing filament bulb on black (base-idea) | Conclusion: real work hides "in the part you cannot see" (the idea) | End of section | CC0 StockSnap (Openverse) | `.../base-idea.jpg` |

## Cue State Timeline

Timing from `section-02-word-timings.json` (real word starts).

| Cue | Local Time | Voice Cue (word @ s) | Big Scene | What Changes | What Stays | Motion | WIT | Label / Markup | Why |
|---|---:|---|---|---|---|---|---|---|---|
| C1 | 0.0-3.2 | "lazy" @1.5 | A | `NOT LAZY PEOPLE` label hard-shows | typing base | hard-show | none | NOT LAZY PEOPLE | correct the misconception |
| C2 | 3.2-9.64 | "look" @7.72 / "more than" @8.42 | A | `THE LOOK OF WORK` then `> THE WORK ITSELF` (impact) | typing base | hard-show + impact | none | THE LOOK OF WORK / > THE WORK ITSELF | the thesis |
| C3 | 9.64-14.30 | "hard to see" @10.8 / "nothing" @12.02 | B | cut to quiet desk; WIT thinking; `REAL PROGRESS: HARD TO SEE` then `LOOKS LIKE NOTHING` | quiet base | transition + hard-show | `thinking` giant | REAL PROGRESS: HARD TO SEE / LOOKS LIKE NOTHING | thinking is invisible |
| C4 | 14.30-19.84 | "meetings"@16.06 / "fast typing"@16.9 / "serious face"@18.32 | C | cut to meeting room; staggered `MEETINGS` → `FAST TYPING` → `SERIOUS FACE` + WIT typing | meeting base | transition + staggered hard-show | `typing-on-laptop` | MEETINGS / FAST TYPING / SERIOUS FACE | the visible world is easy to see |
| C5 | 19.84-24.30 | "trust"@20.18 / "ignore"@22.22 | D | cut to quiet desk; `WE TRUST WHAT WE SEE` then `IGNORE WHAT WE CAN'T` | quiet base | transition + hard-show | none | WE TRUST WHAT WE SEE / IGNORE WHAT WE CAN'T | the bias |
| C6 | 24.30-28.949 | "real work usually hides"@26.02 / "cannot see"@27.92 | D | `REAL WORK HIDES HERE` + WIT deadpan; hold to end | quiet base | hard-show | `deadpan-side-eye` giant | REAL WORK HIDES HERE | dry conclusion / payoff |

## WIT Pose Plan

Shared manifest `.agents/_shared/assets/wit/poses/`.

| Cue | Time | Emotion | Pose File | Placement / Scale | Safe Crop | Why |
|---|---:|---|---|---|---|---|
| C3 | 9.8-14.3 | focused / quiet | `wit-pose-thinking.png` | lower-left, ~1/2 frame | head/shoulders safe | real thinking = invisible work |
| C4 | 14.5-19.84 | performing busy | `wit-pose-typing-on-laptop.png` | lower-right, ~1/2 frame | face/hands safe | embody visible busy |
| C6 | 26.0-28.949 | dry / deadpan | `wit-pose-deadpan-side-eye.png` | lower-right side peek, ~1/2 frame | face/glasses safe | dry "real work hides" button |

WIT density note: 3 beats (A:0, B:1, C:1, D:1). Scene A is label-only breathing. None over 1 per scene.

## Reference And Asset Plan

| Asset | Type | Source / Status | Use | Safety |
|---|---|---|---|---|
| base-typing.jpg | CC0 photo | StockSnap via Openverse | Scene A base | safe (no face; generic laptop, no visible logo) |
| base-think.jpg | CC0 photo | rawpixel via Openverse | Scene B base | safe (no people, no brand) — blank notebook on dark wood |
| base-meeting.jpg | CC0 photo | rawpixel via Openverse | Scene C base | safe (no people, no brand) |
| base-idea.jpg | CC0 photo | StockSnap via Openverse | Scene D base | safe (no people, no brand) — glowing bulb on black |
| 3 WIT poses | PNG | shared WIT manifest | C3/C4/C6 | safe channel asset |

## HyperFrames Guidance

- Composition 1920x1080; 4 scenes (tracks 1/3/4/5), 6 cues (track 2); audio 28.949s.
- All cue `data-start` pinned to word-timings; quick 0.2s opacity fades on scene-base cuts; impact only on `> THE WORK ITSELF` and the visible-list reveals (each staggered to its word).
- WIT ~1/2 frame on its beats; faces safe; labels in their own zones (top), WIT lower — no collision.
- Subtitle-safe: keep labels in the upper/mid area.
- Must not invent: bases (provided), WIT poses (named), label text (provided), cue timing (word-timed), scene order. Render decides only pixel coords/easing/grading.
- Suggested QA snapshots: 1.6 / 8.0 / 11.5 / 16.5 / 20.5 / 26.5s.

## Review-Prevention Checklist

- voice sync: yes (word-timed)
- big-scene rhythm: 4 distinct ideas, base held per idea
- cue density: 6 cues / 29s — low
- motion: hard-show default; impact reserved
- WIT rhythm: 3 beats, ≤1/scene
- WIT size/crop: ~1/2 frame, faces safe
- WIT/text collision: separate zones
- scene differentiation: typing / quiet / meeting / quiet(callback)
- render needs no invention: correct

## Approval Checks

- visual reference pass: done (Openverse CC0, viewed)
- bases brand-free/people-free: yes
- contrast visible-vs-invisible is clear: yes
- WIT has a job each beat: yes
- learner-friendly, short labels: yes
- ready for HyperFrames: yes
