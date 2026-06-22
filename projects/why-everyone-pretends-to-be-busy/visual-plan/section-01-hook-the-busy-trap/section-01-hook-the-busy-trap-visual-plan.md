# Section 1 Visual Plan (remade from scratch)

Video: `Why Everyone Pretends To Be Busy`
Section: `Section 1: Hook: The Busy Trap`
Status: `draft visual plan for approval (v2 — new standard: real bg every scene + real-UI + big/high WIT)`

## Section Goal
Open inside the situation and make the title promise visible fast: the less time you have for real work, the more important you look. Busy *signals* (calendar/inbox/phone) read as "this person matters"; quiet thinking reads as "lazy." Land the dry button: there is a difference between being busy and looking busy.

## Source Inputs
- Voiceover: `voiceover/section-01-.../...david23-am_eric-0.84.mp3` (21.12s, 0.84)
- Word timings: `voiceover/section-01-.../section-01-word-timings.json` (existing; cue times REAL)
- NOTE: this section's audio is 0.84 (plain); Sections 4–7 are 0.86 (pause-tuned). Delivery mismatch flagged — see chat. Visual cues are pinned to the current 0.84 timings; if voiceover is regenerated at 0.86 the cues must be re-pinned.

## Visual Direction (new standard)
- 4 scenes, each on a REAL people-free photo base; the busy-signals beat uses REAL-UI (packed calendar, unread inbox, phone panic notifications) built in CSS with real icons.
- WIT BIG (≈1/3–1/2 frame) and HIGH (head+torso inside frame, legs cropped); labels arranged around it.
- WIT path (4 distinct): typing-on-laptop → holding-phone-panic → deadpan-side-eye → suspicious.

## Big Scene Plan
| Scene | Time | Voice | Real base | Build |
|---|---:|---|---|---|
| A — the strange rule | 0:00–5.24 | "here's a strange rule… the less time for real work, the more important you look" | base-deskwork.jpg (warm desk, real work) | labels A STRANGE RULE + LESS REAL WORK = LOOK MORE IMPORTANT; WIT working |
| B — the busy signals | 5.24–11.0 | "a full calendar, a loud inbox, a phone making tiny panic sounds… this person matters" | base-busy-signals.jpg (bright flat-lay + phone) | REAL-UI: packed calendar / unread inbox / phone panic notifications; THIS PERSON MATTERS |
| C — quiet = lazy | 11.0–16.06 | "but sit quietly and think… people assume you are lazy. or asleep with your eyes open" | base-deskcalm.jpg (bright minimal desk) | THINK QUIETLY → LAZY? / ASLEEP — EYES OPEN; WIT deadpan |
| D — looking busy / the difference | 16.06–21.0 | "everyone gets busy… very good at looking busy. there is a difference" | base-deskwork-cage.jpg (warm desk, cooled + CSS cage bars; callback to A) | LOOKING BUSY → THERE IS A DIFFERENCE; WIT suspicious |

## Cue State Timeline (word-timed)
| Cue | Time | Voice cue (word@s) | Scene | Change | Motion | WIT |
|---|---:|---|---|---|---|---|
| C1 | 0–2.34 | "a strange rule"@0.58 | A | label A STRANGE RULE; WIT working | hard-show | typing-on-laptop @0.4 |
| C2 | 2.34 | real work@3.48 / important@4.32 | A | LESS REAL WORK = LOOK MORE IMPORTANT | hard-show | — |
| C3 | 5.24 | calendar@5.76 | B | packed CALENDAR card pops | impact | holding-phone-panic @5.5 |
| C4 | 6.64 | inbox@6.64 / phone@7.3 | B | unread INBOX card + phone PANIC notifications pop | impact | — |
| C5 | 10.64 | "this person matters"@10.64 | B | THIS PERSON MATTERS ✓ | hard-show | — |
| C6 | 11.0 | sit quietly@11.3 / think@11.98 | C | cut to quiet desk; THINK QUIETLY; WIT | hard-show | deadpan-side-eye @11.2 |
| C7 | 14.32 | lazy@14.32 / asleep…eyes open@14.9 | C | LAZY? then ASLEEP — EYES OPEN | impact | — |
| C8 | 16.06 | everyone gets busy@16.34 | D | cut to caged desk; EVERYONE GETS BUSY | hard-show | suspicious @16.3 |
| C9 | 19.12 | "looking busy"@19.12 | D | GOOD AT LOOKING BUSY | hard-show | — |
| C10 | 20.58 | "there is a difference"@20.58 | D | THERE IS A DIFFERENCE | impact | — |

## Reference And Asset Plan
| Asset | Source | Class | Use |
|---|---|---|---|
| base-deskwork.jpg | CC0 StockSnap (warm desk + coffee + notebook) | safe base | A (+ D regrade) |
| base-busy-signals.jpg | CC0 StockSnap (bright flat-lay + phone) | safe base | B |
| base-deskcalm.jpg | CC0 StockSnap (bright minimal desk) | safe base | C |
| base-deskwork-cage.jpg | CC0 StockSnap (warm desk, cooled grade) | safe base | D (+ CSS cage bars) |
| icons/gcal.png, gmail.png | Wikimedia (Google Calendar / Gmail logos) | real-UI icon | B (editorial) |
| 4 WIT poses | shared manifest | safe asset | C1/C3/C6/C8 |

## HyperFrames Guidance
- 1920x1080; 4 scenes (tracks 1/3/4/5), 10 cues (track 2); audio 21.12s.
- Cue starts pinned to word-timings; the 3 busy-signal UI cards pop on calendar/inbox/phone words.
- Real-UI (calendar/inbox/phone) = CSS over the real flat-lay photo with real icons; light scrim only.
- WIT big + high (bottom≈-280…-330, width ~1000–1180); arrange labels to the opposite side/top so WIT is never covered or lowered. D adds CSS cage bars over the warm desk as the trapped/callback motif.
- Must not invent: bases, label text (use script wording "a loud inbox", not the whisper "allowed"), word-timed order, WIT poses.
- QA snapshots: 1.5 / 4.5 / 6.5 / 8 / 10.7 / 12.5 / 15 / 17 / 19.5 / 20.8s.

## Approval Checks
- Title promise ("looking busy") clear by ~second 5; real-UI signals land on their words.
- WIT big and high in every scene; labels arranged around it.
- Dry button "There is a difference" lands at ~20.6s. Real bg every scene; brand/people-safe.
