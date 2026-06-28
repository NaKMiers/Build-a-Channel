# Section 1 Render Implementation (v2 remake from scratch)

Composition: `Section01Hook` · 1920x1080 · 21.12s · port 1001

## Build summary
Remade from scratch to the new standard (real photo base every scene + real-UI + big/high WIT),
replacing the v1 build (3 scenes, smaller/lower WIT). 4 scenes on tracks 1/3/4/5, 4 cue groups on
track 2, audio on track 10. Cues pinned to existing `section-01-word-timings.json` (0.84, 21.12s).

## Scenes
1. **A - the strange rule** (0–5.30): base-deskwork; A STRANGE RULE@0.58 + LESS REAL WORK = LOOK MORE IMPORTANT@3.48; WIT typing-on-laptop (big, high).
2. **B - busy signals (real-UI)** (5.24–11.04): base-busy-signals; CSS calendar card (gcal icon + red events)@5.76, Gmail inbox card (unread 47 + rows)@6.64, phone panic notifs@7.30/8.14; THIS PERSON MATTERS@10.64 (top-center, clears WIT); WIT holding-phone-panic centered-bottom (big, high).
3. **C - quiet = lazy** (11.0–16.10): base-deskcalm; THINK QUIETLY@11.30 → LAZY?@14.32 → ASLEEP - EYES OPEN@14.90; WIT deadpan-side-eye (big, high, right).
4. **D - looking busy / the difference** (16.06–21.12): base-deskwork-cage + CSS cage bars that bounce-slam down on "everyone gets busy"@16.40–17.0; EVERYONE GETS BUSY@16.34 → GOOD AT LOOKING BUSY@19.12 → THERE IS A DIFFERENCE@20.58; WIT suspicious (big, high, right).

## WIT (new standard: big + high) - enlarged to GIANT (owner: "make the WIT bigger, I love giant WIT")
All four WIT are now GIANT (≈1/2 frame): side WIT width ~1340–1380 (`bottom:-350…-360`), centered B
width ~1140 (`bottom:-330`). Heads remain comfortably inside the top edge; only legs crop. Labels/cards
arranged to the opposite side/top so the giant WIT covers nothing ("THIS PERSON MATTERS" sits above the
centered B WIT; A/C/D labels sit left of the right-side WIT). Snapshots 4.5/8.5/10.7/15/20.8 verified.

## QA
- `hyperframes lint`: 0 errors (1 advisory `timeline_track_too_dense`).
- `hyperframes validate`: 0 errors; contrast advisories are fixed-sample-time off-screen measurements (same as other sections).
- `hyperframes snapshot`: all 4 scenes verified; B's real-UI overload reads clean; "THIS PERSON MATTERS" moved to top so the centered WIT clears it; cage bars + dry button land in D.

## Notes
- Audio is 0.84 (plain) while Sections 4–7 are 0.86 (pause-tuned) - delivery mismatch FLAGGED to owner; if regenerated at 0.86, regenerate word-timings and re-pin all cues.
- Reused approved v1 CC0 desks (deskwork / deskcalm / deskwork-cage); added base-busy-signals.jpg (CC0 StockSnap). gcal/gmail icons reused from S4 (editorial). v1 leftover assets (sceneB-minimal-desk, sceneC-wall-calendar*) are now unused.
- No MP4/WebM exported (not requested).
