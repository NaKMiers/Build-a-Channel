# Section 6 Visual Plan

Video: `Why Everyone Pretends To Be Busy`
Section: `Section 6: "I'm Busy" Is A Shield`
Status: `draft visual plan for approval`

## Section Goal
Reason 4: "I'm busy" is a socially safe defense, not a moral failure. It deflects requests, it is often genuinely true (overloaded), and it slowly becomes the *only* acceptable way to say no - so everyone says it.

## Source Inputs
- Voiceover: `voiceover/section-06-im-busy-is-a-shield/scratch-audio/...david23-am_eric-0.86.mp3` (38.04s, 0.86)
- Word timings: `voiceover/section-06-.../section-06-word-timings.json` (generated; cue times REAL)

## Visual Direction (real backgrounds + real-UI, owner-preferred)
- 5 distinct scenes, each on a REAL people-free photo background (per owner: backgrounds make it lively).
- Real-UI where the script depicts messages: a 1:1 chat (B) and a group chat (E) built in CSS with a real Messenger icon.
- Central metaphor built in CSS over the real photo: a shield labeled `I'M BUSY` (A) and crossed-out speech bubbles (D).
- WIT path (5 distinct): deadpan-side-eye → facepalm → sleeping-burned-out → shocked → tiny-defeated.

## Big Scene Plan
| Scene | Time | Voice | Real base | Build on top |
|---|---:|---|---|---|
| A - THE SHIELD | 0:00–8.26 | "the fourth reason… it is a shield" + first 2 meanings | `base-office.jpg` (grey concrete desk, open space) | CSS shield `I'M BUSY`, WIT behind it, request bubbles bounce off |
| B - what it really means | 8.26–15.34 | "please stop asking… I have no idea what I'm doing, look calm" | `base-desk-chat.jpg` (warm wood + notepad) | real-UI 1:1 chat: incoming questions, calm "I'm busy" reply, red meaning captions |
| C - OVERLOADED (it's real) | 15.34–20.08 | "not always dishonest… really are overloaded. the shield is real" | `base-overloaded.jpg` (wall of sticky notes) | OVERLOADED stamp, WIT burned-out |
| D - what you can't say | 20.08–32.14 | "the only acceptable way to say no… too relaxed… too dangerous" | `base-meeting.jpg` (empty meeting room) | CSS speech bubbles: 2 struck-out + accepted `I'M BUSY ✓` |
| E - everyone nods | 32.14–38.04 | "everyone nods… busy or pretending or both" | `base-desk-group.jpg` (grey concrete + laptop/phone) | real-UI group chat full of "busy", WIT defeated, "OR BOTH" |

## Cue State Timeline (word-timed)
| Cue | Time | Voice cue (word@s) | Scene | Change | Motion | WIT |
|---|---:|---|---|---|---|---|
| C1 | 0–3.94 | "it is a shield"@3.52 | A | shield + WIT appear; label A SHIELD | hard-show | deadpan-side-eye |
| C2 | 4.38 | "cannot take on more"@4.38 | A | bubble "Can you take this on?" bounces; `= CAN'T TAKE MORE` | impact (bounce) | - |
| C3 | 6.22 | "make this decision"@6.22 | A | bubble "What should we do?"; `= WON'T DECIDE` | impact | - |
| C4 | 8.26 | "please stop asking"@9.08 | B | chat appears; incoming "Quick question?"; caption `STOP ASKING` | hard-show | - |
| C5 | 10.72 | "no idea…look calm"@13.9 | B | calm reply "I'm busy"; red caption `(= NO IDEA. STAY CALM.)` | hard-show | facepalm @12.86 |
| C6 | 15.34 | "not always dishonest"@15.34 | C | cut to sticky-note wall; label `NOT ALWAYS DISHONEST`; WIT | hard-show | sleeping-burned-out |
| C7 | 18.56 | "really are overloaded"@18.56 | C | `OVERLOADED` stamp | impact (stamp) | - |
| C8 | 19.28 | "the shield is real"@19.28 | C | label `THE SHIELD IS REAL` | hard-show | - |
| C9 | 20.08 | "only acceptable way to say no"@20.28 | D | cut to meeting room; label `THE ONLY OK "NO"` | hard-show | - |
| C10 | 25.98 | "quiet time to think"@25.98 / "suspiciously relaxed"@27.48 | D | bubble "I need quiet time to think" → `TOO RELAXED` stamp | impact | - |
| C11 | 30.04 | "this meeting could've been a message"@30.04 / "dangerous"@31.7 | D | bubble "this meeting could've been a message" → `TOO DANGEROUS`; accepted `I'M BUSY ✓` | impact | shocked @31.7 |
| C12 | 32.14 | "everyone nods"@34.08 | E | cut to group chat; "busy/swamped" replies stack | hard-show | - |
| C13 | 37.54 | "or both"@37.54 | E | label `OR BOTH`; WIT defeated | impact | tiny-defeated |

## Reference And Asset Plan
| Asset | Source | Class | Use |
|---|---|---|---|
| base-office.jpg | StockSnap CC0 | safe base | A shield backdrop |
| base-desk-chat.jpg | StockSnap CC0 | safe base | B 1:1 chat float |
| base-overloaded.jpg | Wikimedia CC BY 3.0 (sticky notes, WMF office) | safe base | C overload |
| base-meeting.jpg | rawpixel CC0 (empty conference room) | safe base | D speech bubbles |
| base-desk-group.jpg | StockSnap CC0 | safe base | E group chat float |
| icons/messenger.png | Wikimedia (Messenger logo) | real-UI icon | B + E chat headers (editorial) |
| 5 WIT poses | shared manifest | safe asset | C1/C5/C6/C11/C13 |

Rejected: ss-2FQ69FRGV6 (iiyama brand), ss-AWYUDM17G5 (Apple logo), ss-RVVFEKQTWA (too like S5 marble), Glasgow theatre (faces).

## HyperFrames Guidance
- 1920x1080; 5 scenes (tracks 1/3/4/5/6), 13 cues (track 2); audio 38.04s.
- Cue starts pinned to word-timings. Chat bubbles / speech bubbles / stamps reveal item-by-item on their spoken word, not all at scene start.
- Shield + speech bubbles + chat = CSS over the real photo; backgrounds get a light scrim so overlays read (do NOT gray-wash the photo).
- Float chat UI as a `.screen` over the real desk (Section-5 pattern); shield/speech-bubbles sit directly over the office/meeting photo.
- WIT ~1/3–1/2 frame on emotional beats, faces safe, not covering labels. Messenger icon used editorially.
- Must not invent: bases, label text, word-timed order, WIT poses.
- QA snapshots: 3.6 / 5 / 7 / 9.5 / 14 / 16 / 19 / 21 / 27.5 / 31.8 / 35 / 37.7s.

## Approval Checks
- WIT looks protected/overwhelmed, not smug; OVERLOADED corrects the "fake person" reading.
- "Or both" lands as the dry closer.
- 5 distinct real backgrounds; real-UI chat; word-timed; brand/people-safe.
