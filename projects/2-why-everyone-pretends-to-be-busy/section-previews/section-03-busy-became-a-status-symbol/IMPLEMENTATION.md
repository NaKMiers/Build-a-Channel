# Section 3 Render Implementation (v2 remake from scratch)

Composition: `Section03Status` · 1920x1080 · 45.14s · port 1003

## Build summary
Remade from scratch to the new standard (real photo base every scene + real-UI + GIANT high WIT),
replacing the v1 build (5 scenes). 6 scenes on tracks 1/3/4/5/6/7, 6 cue groups on track 2, audio on
track 10. Cues pinned to existing `section-03-word-timings.json` (0.84, 45.14s; clean).

## Scenes
1. **A - status symbol** (0–4.12): base-trophy; BUSY = STATUS SYMBOL@2.48; giant WIT awkward-celebration.
2. **B - I'm so busy = important** (4.06–11.04): base-busychat + CSS chat "I'm so busy!! 😩"@4.30 → red "(= please notice I'm important)"@7.84; giant WIT talking-front.
3. **C - busy isn't an emotion** (11.0–17.04): base-emotions + CSS EMOTIONS board (Happy/Sad/Angry/Tired + Busy?@11.98) → NOT AN EMOTION@13.32 → (everyone's tired)@15.28; giant WIT deadpan-side-eye.
4. **D - opposite brag** (17.0–25.46): base-holiday (beach); LONG HOLIDAYS · FREE AFTERNOONS@19.34 → CSS packed-calendar + NO FREE TIME@23.06 → OPPOSITE BRAG@25.42; giant WIT suspicious (centered).
5. **E - busy sounds good** (25.42–33.36): base-sounds (dark-wood hands); RESPONSIBLE@26.40 → NEEDED@27.68 → LINED UP WAITING@29.80 → = FEELS VALUABLE@31.84 (staggered); giant WIT thinking.
6. **F - near the work** (33.32–45.14): base-nearwork (meeting room) + CSS calendar of "meeting about the meeting" events@36.96; MEETINGS ABOUT MEETINGS@36.96 → PROVING YOU'RE NEAR THE WORK@43.75; giant WIT tiny-defeated.

## WIT (giant + high)
All six ≈1/2 frame, `bottom:-350`, heads inside the top edge, legs cropped; labels placed to the
opposite side/top so the giant WIT covers nothing. 6 distinct poses.

## QA
- `hyperframes lint`: 0 errors (1 advisory `timeline_track_too_dense`).
- `hyperframes validate`: 0 errors (contrast advisories are fixed-sample off-screen measurements, as in other sections).
- `hyperframes snapshot --at 2.6,8,14,20,24,28,31,37,44`: all 6 scenes verified - emotions board, beach+calendar contrast, staggered "busy sounds" labels, meetings calendar + payoff; giant WIT clear everywhere.

## Fixes during build
- gcal icon reused in D + F → copied to `gcal2.png` for F (avoids duplicate-media).

## Notes
- Reused HD base-trophy (S3); 2 fresh (base-holiday beach, base-busychat); 3 clean HD cross-section bases (base-emotions ← S6 grey desk, base-sounds ← S7 dark wood, base-nearwork ← S6 meeting room) on non-adjacent surfaces. Messenger/Calendar icons reused (editorial).
- DROPPED v1 low-res bases base-beach/base-meeting/base-clock/base-coffee (~250px).
- Audio 0.84 (plain) vs Sections 4–7 at 0.86 - FLAGGED; if regenerated, regenerate word-timings + re-pin.
- No MP4/WebM exported (not requested).
