# Section 5 Visual Plan

Video: `Why Everyone Pretends To Be Busy`
Section: `Section 5: Visible Work Beats Quiet Thinking`
Status: `draft visual plan for approval`

## Section Goal
Show the third reason: visible work is easier to reward than quiet thinking. Replies, meetings, and "just circling back" are seen; two hours of thinking looks like nothing. Managers reward visible motion, so people perform motion (move task cards, updates about updates) - "productivity theater," whose star is a spreadsheet.

## Source Inputs
- Voiceover: `.../section-05-...david23-am_eric-0.86.mp3` (42.859s, 0.86)
- Word timings: `voiceover/section-05-.../section-05-word-timings.json` (generated; cue times REAL)

## Visual Direction (real-UI illustration - owner-preferred)
- 5 big scenes, 9 cues. Leans into REAL UI the script names: a Google Meet call grid, a Trello Kanban board (move a task column to column), a Google Sheets spreadsheet ("the star is a spreadsheet").
- WIT path: typing → thinking → deadpan ("possibly blinking") → facepalm → tiny-defeated (5 distinct).
- Real app icons (Meet, Trello, Sheets) in CSS UI mockups; one real photo (empty room wall) for "staring at a wall."

## Big Scene Plan
| Scene | Time | Voice | Base | Real-UI |
|---|---:|---|---|---|
| A - visible = rewarded | 0:00-10.5 | "visible work is easier to reward… definitely see it" | CSS Google Meet call grid | Meet icon + video tiles; REPLY FAST / MEETINGS / "JUST CIRCLING BACK" |
| B - thinking looks like nothing | 10.5-19.1 | "spend two hours thinking… possibly blinking" | empty-room wall photo (`base-wall.jpg`) | WIT staring; THINKING / LOOKS LIKE NOTHING / POSSIBLY BLINKING |
| C - managers can't tell | 19.1-25.76 | "a survey where most managers admitted… reward what they can see" | CSS survey/poll card | "Can you tell who's productive?" Yes 15% / Not really 85% |
| D - performing motion | 25.76-35.04 | "what they can see is motion… updates about future updates" | CSS Trello Kanban board | Trello icon; card moves DOING→DONE; UPDATES ABOUT FUTURE UPDATES |
| E - productivity theater | 35.04-42.859 | "productivity theater… the star of the show is a spreadsheet" | CSS theater stage + Google Sheets spreadsheet | Sheets icon spreadsheet spotlit on stage = "the star" |

## Cue State Timeline (word-timed)
| Cue | Time | Voice cue (word@s) | Scene | Change | WIT | Label |
|---|---:|---|---|---|---|---|
| C1 | 0–3.48 | "visible work…reward"@1.4 | A | Meet grid + label; WIT typing | typing-on-laptop | VISIBLE WORK = EASY TO REWARD |
| C2 | 3.48–10.5 | reply@3.48 / meeting@5.72 / circling back@8.4 | A | staggered REPLY FAST → MEETINGS → "JUST CIRCLING BACK" + PEOPLE SEE IT | - | (3 labels) |
| C3 | 10.5–13.8 | thinking@11.34 / nothing@13.06 | B | cut to wall; WIT thinking; THINKING / LOOKS LIKE NOTHING | thinking | THINKING… / (LOOKS LIKE NOTHING) |
| C4 | 13.8–19.1 | staring at a wall@17.06 / possibly blinking@18.36 | B | WIT deadpan staring; labels | deadpan-side-eye | STARING AT A WALL / POSSIBLY BLINKING |
| C5 | 19.1–25.76 | most managers@20.16 / reward what they see@24.4 | C | poll card; bars; reward label | - | MOST MANAGERS: CAN'T TELL / REWARD WHAT THEY SEE |
| C6 | 25.76–28.9 | motion@26.68 / performing motion@27.88 | D | cut to Kanban; PERFORM MOTION? | - | PERFORM MOTION? |
| C7 | 28.9–35.04 | move a task…another column@30.56–32.3 / future updates@33.14 | D | task card animates DOING→DONE; WIT facepalm; UPDATES ABOUT FUTURE UPDATES | facepalm | UPDATES ABOUT FUTURE UPDATES |
| C8 | 35.04–37.28 | productivity theater@36.22 | E | cut to stage+spreadsheet; label | - | PRODUCTIVITY THEATER |
| C9 | 37.28–42.859 | tickets paid in stress@39.2 / star…spreadsheet@40.76 | E | spotlight on spreadsheet "THE STAR"; WIT defeated | tiny-defeated | TICKETS: PAID IN STRESS / THE STAR ★ |

## Reference And Asset Plan
| Asset | Source | Use |
|---|---|---|
| icons/meet.png | Wikimedia (Google Meet) | Scene A call-grid header |
| icons/trello.png | Wikimedia (Trello) | Scene D board header |
| icons/sheets.png | Wikimedia (Google Sheets) | Scene E spreadsheet |
| base-wall.jpg | Wikimedia (empty room) CC | Scene B "staring at a wall" |
| 5 WIT poses | shared manifest | C1/C3/C4/C7/C9 |
Real-UI per owner preference; Meet grid / poll / Kanban / spreadsheet+stage built in CSS with real icons.

## HyperFrames Guidance
- 1920x1080; 5 scenes (tracks 1/3/4/5/6), 9 cues (track 2); audio 42.859s.
- Cue starts pinned to word-timings; the Kanban card move (D) animates on "move a task from one column to another" (30.56–32.3).
- Accumulating UI lives in the scene divs; cues hold labels + WIT. WIT ~1/2 frame, faces safe.
- Must not invent: bases, real icons, label text, word-timed order.
- QA snapshots: 2 / 6 / 9 / 12.5 / 18 / 22 / 27.5 / 31.5 / 36.5 / 41s.

## Approval Checks
- real-UI illustration (Meet/Trello/Sheets) per owner preference; brand used editorially
- 5 distinct scenes; WIT varied (5 poses); word-timed; ready for HyperFrames
