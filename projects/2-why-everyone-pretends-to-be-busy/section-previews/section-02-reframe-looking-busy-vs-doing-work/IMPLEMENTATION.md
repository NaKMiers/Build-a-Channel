# Section 2 Render Implementation (v2 remake from scratch)

Composition: `Section02Reframe` · 1920x1080 · 29.02s · port 1002

## Build summary
Remade from scratch to the new standard (real photo base every scene + real-UI + GIANT high WIT),
replacing the v1 build. 4 scenes on tracks 1/3/4/5, 4 cue groups on track 2, audio on track 10.
Cues pinned to existing `section-02-word-timings.json` (0.84, 29.02s; words array clean - the
duplicated tail was only in the transcript string).

## Scenes
1. **A - not lazy** (0–5.94): base-workplace (office interior); NOT LAZY PEOPLE@1.50 + (different, smaller problem)@4.46; giant WIT talking-front.
2. **B - the look of work** (5.88–14.62): base-idea (bulb); SOMETHING STRANGER@5.98 → REWARDS THE LOOK ＞ THE WORK@7.72 → THINKING = LOOKS LIKE NOTHING@12.02; giant WIT thinking.
3. **C - busy is easy to see** (14.58–20.24): base-typing + CSS Google Meet grid (meet icon + initials tiles)@16.06; EASY TO SEE@14.80 + MEETINGS@16.06 / TYPING@17.20 / A SERIOUS FACE@18.32 (staggered); giant WIT typing-on-laptop.
4. **D - real work hides** (20.18–29.02): base-idea-d (bulb returns); WE TRUST WHAT WE SEE@20.40 → IGNORE WHAT WE CAN'T@22.22 → red circle on bulb + REAL WORK HIDES HERE@26.98; giant WIT deadpan-side-eye.

## WIT (giant + high)
All four ≈1/2 frame: side width ~1300–1340, `bottom:-350`; heads inside the top edge, legs cropped;
labels placed left/top so the giant WIT covers nothing.

## QA
- `hyperframes lint`: 0 errors (1 advisory `timeline_track_too_dense`).
- `hyperframes validate`: 0 errors (contrast advisories are fixed-sample off-screen measurements, as in other sections).
- `hyperframes snapshot --at 1.6,4.6,7.8,12.5,15.5,18.5,21,23,27.5`: all 4 scenes verified; Meet grid reads clean; bulb bookend + red circle land; giant WIT clear in every frame.

## Notes
- Reused base-typing + base-idea (960px, good); base-idea copied to base-idea-d.jpg for D (avoids duplicate-media). Added base-workplace.jpg (CC0 StockSnap). meet.png reused from S5 (editorial).
- DROPPED v1 low-res assets base-meeting.jpg + base-think.jpg (~250px); rejected marble flat-lays (too like S5/S7).
- Audio 0.84 (plain) vs Sections 4–7 at 0.86 - FLAGGED; if regenerated, regenerate word-timings + re-pin.
- No MP4/WebM exported (not requested).
