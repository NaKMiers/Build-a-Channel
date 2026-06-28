# Section 5 Implementation - Visible Work Beats Quiet Thinking

Composition: `Section05Visible` · 1920x1080 · 42.859s · port 1005

## Build summary
- 5 scenes on tracks 1/3/4/6 (A/B/C/D/E use tracks 1,3,4,5,6), 9 cues on track 2, audio on track 10.
- Real-UI built in CSS with real app-icon PNGs (Meet / Trello / Sheets); one CC photo base (wall).
- GSAP timeline mirrors prior sections: `reveal` / `show` / `smash` helpers + two custom tweens
  (poll bar width growth; Trello card DOING→DONE translate).

## Scenes
1. **A - Google Meet call grid** (0–10.54): dark Meet UI, top bar w/ Meet icon, 6 tiles (initials avatars, no faces), speaking tile highlighted, control bar w/ red end-call.
2. **B - wall photo** (10.5–19.14): `base-wall.jpg` + shade; WIT thinking then deadpan.
3. **C - survey poll card** (19.1–25.8): Yes 15% / Not really 85% bars grow on cue; "- survey of managers".
4. **D - Trello board** (25.76–35.08): TO DO / DOING / DONE columns + cards; `.movecard` translates DOING→DONE (x:-520→0) over 1.5s at 30.56.
5. **E - Sheets on theater stage** (35.04–42.859): red curtains + spotlight + Q4_updates spreadsheet; gold ★ badge pops at 40.76.

## Cue timing (pinned to section-05-word-timings.json)
C1 0.0 · C2 3.48 · C3 10.5 · C4 13.8 · C5 19.1 · C6 25.76 · C7 28.9 · C8 35.04 · C9 37.28.
Label-on-word offsets: reply 3.54 / meetings 5.80 / circling 8.46 / thinking 11.40 / nothing 13.10 /
staring 17.10 / blinking 18.40 / can't-tell 20.16 / reward 24.40 / perform 27.88 / card-move 30.56 /
updates 33.20 / theater 36.22 / tickets 39.20 / star 40.76–40.90.

## QA
- `hyperframes lint`: 0 errors (1 advisory `timeline_track_too_dense`, same as prior sections).
- `hyperframes validate`: 0 errors; contrast advisories are fixed-sample-time measurements of
  off-screen elements (same pattern as prior sections); visible-time labels use cream/red/green
  cards with dark/contrasting text.
- `hyperframes snapshot --at 2,6,9,12.5,18,22,27.5,31.8,36.5,41.5`: all 5 scenes verified -
  Meet grid + label, REPLY/MEETINGS/CIRCLING labels, wall+THINKING, wall+STARING+deadpan,
  poll 15/85 bars, Trello board, card moved to DONE, Sheets+THEATER, TICKETS+THE STAR+defeated WIT.

## Fixes during build
- Track-2 float overlap (cue-6 ended at 28.900000000000002 vs cue-7 start 28.9) → cue-6 duration 3.14→3.12.

## v2 liveliness pass (owner: "missing some real-world images, not lively")
- Scenes A/C/D rebuilt: the CSS UI is wrapped in a floating `.screen` (1500x846, rounded, big drop
  shadow) over a real people-free CC desk photo (`.deskphoto`) + a radial `.deskscrim`. Reads as the
  app on a real screen on a real desk.
  - A: `base-desk-call.jpg` (white desk + MacBook); C: `base-desk-survey.jpg` (marble + iPad/notepad);
    D: `base-desk-board.jpg` (dark wood + "To Do List" notepad) - distinct surfaces, no faces.
- Internal UI rescaled to fit the 1500x846 window (meet tiles/avatars, poll card, kanban columns/cards).
- Trello `.movecard` columns rescaled → DOING→DONE translate offset updated x:-520→-460.
- Scene B (real wall) unchanged.
- v3 (owner: "last scene still not have background"): Scene E swapped CSS curtains/floor/stagebg for a
  real lit red theater-curtain photo (`base-stage.jpg`, CC0 Wikimedia, no people) + a `.stagescrim`
  vignette + the spotlight glow on the spreadsheet. Sheet + star + labels + WIT unchanged. So ALL
  five scenes now carry a real-world background.
- Re-lint 0 errors; re-snapshot confirms all five scenes (desks visible around each UI, card-move +
  star intact, real curtain behind the spreadsheet).
- Sources: desks = CC0 StockSnap; wall + stage curtain + icons = Wikimedia. People-free, editorial real-UI.

## Notes
- No MP4/WebM exported (not requested).
- Audio is 0.86 (pause-tuned), consistent with Sections 4–7.
- Real-UI illustration per standing owner preference (depict, not endorse; no private data / pixel-copied screenshots).
