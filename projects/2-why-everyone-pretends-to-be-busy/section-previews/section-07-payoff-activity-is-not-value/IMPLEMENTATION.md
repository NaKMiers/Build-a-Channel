# Section 7 Implementation - Payoff: Activity Is Not Value

Composition: `Section07Payoff` · 1920x1080 · 46.78s · port 1007

## Build summary
- 5 scenes on tracks 1/3/4/5/6, 5 cue groups on track 2, audio on track 10.
- Real photo bases (hands OK) + real-UI boards/chat/calendar built in CSS on top.
- Closes on a real-UI Google Calendar packed with red "urgent" events = "a calendar with Wi-Fi."
- GSAP reveal/show/smash; scene-internal builds revealed at word times; cue WIT/stamps/boards shown on their words.

## Scenes
1. **A - the question** (0–6.24): base-question; `ACTIVITY ≠ VALUE` board; ≠ smashes on "value"@4.36; WIT thinking.
2. **B - rewarded vs needed** (6.2–18.34): base-busy (hands typing); red REWARDED labels (AVAILABLE@6.52/FAST@7.0/OVERLOADED@7.6) vs green REAL WORK NEEDS (FOCUS@10.38/QUIET@10.5/TIME@10.94) + NOT LAZY@12.62 + BUSY=SAFER THAN THOUGHTFUL@14.78; WIT talking-front.
3. **C - everyone joins in** (18.3–27.04): base-culture; 3 rows HIGHLIGHT≠LEARN@19.56 / REPLY≠SOLVE@21.64 / ORGANIZE≠MAKE@24.48; WIT typing-on-laptop.
4. **D - the honest version** (27.0–38.54): base-busy-d + chat `.screen`; struck reply "I'm protecting my attention from pointless noise"@28.3 + TOO HONEST FOR A TUESDAY stamp@32.0 + "Busy." sent@33.2 → BE HONEST ABOUT WHAT MATTERS board@36.58; WIT deadpan-side-eye.
5. **E - a calendar with Wi-Fi** (38.5–46.78): base-question-e + CSS Google Calendar (gcal icon) filling with red URGENT events@38.8–40.6; EVERYTHING URGENT = NOTHING IS@39.0; final A CALENDAR WITH WI-FI@45.40; WIT trapped-by-app-screen.

## Word timings
- Generated this run (whisper); the tail had a chunk-boundary glitch (words 154–164 jumped back to ~40s) - re-timed monotonically so "…you are not lazy. You are just trapped in a calendar with Wi-Fi" runs 43.56→46.78. All cues pinned to the fixed JSON.

## QA
- `hyperframes lint`: 0 errors (1 advisory `timeline_track_too_dense`, same as prior sections).
- `hyperframes validate`: 0 errors; contrast advisories are fixed-sample-time measurements of off-screen elements (same pattern as prior sections).
- `hyperframes snapshot --at 4.5,8,11.5,15.5,20.5,25,31.5,37,41,45.8`: all 5 scenes verified - ACTIVITY≠VALUE board, rewarded/needed contrast, 3 ≠ rows, honest-struck vs Busy. chat + BE HONEST board, packed Google Calendar + A CALENDAR WITH WI-FI + trapped WIT.

## Fixes during build
- duplicate_media_discovery_risk (base-busy reused in B+D; base-question in A+E) → copied to `base-busy-d.jpg` / `base-question-e.jpg` for the reuse scenes.
- WIT raised (owner: "WIT in all scenes is too low / covered by the frame"): bottom offsets changed from ~-560/-600 to ~-250/-300 (widths trimmed to ~640–880) so head+torso+arms sit inside the frame with only legs cropped; horizontals nudged to stay clear of labels. Re-lint 0 err, re-snapshot confirms full upper body visible in all 5 scenes.
- WIT enlarged (owner: "make WIT bigger; re-arrange other items if covered"): widths now ~900–1180 (giant). Re-arranged to clear it: A board moved up-left (left:46%/top:33%); B WIT centered-bottom with NOT LAZY/BUSY=SAFER moved to top-center and the two label columns kept at the sides; C WIT bigger on the right (≠ rows stay left); D WIT moved to the LEFT (chat bubbles are right-aligned) and TOO HONEST stamp moved to the right; E WIT bigger center-left, calendar shrunk to 920 and shifted right (left:63%), EVERYTHING URGENT + A CALENDAR WITH WI-FI moved to the right. Re-lint 0 err, snapshots confirm no label/UI is covered.

## Notes
- Bases reused in D/E are non-adjacent and the UI dominates the frame; A/B/C bases distinct. Payoff deliberately ties the calendar motif together.
- Sources: base-question/base-busy = CC0 StockSnap; base-culture = Wikimedia CC BY 2.0; gcal icon = Wikimedia. People-free (hands OK), editorial real-UI.
- No MP4/WebM exported (not requested).
