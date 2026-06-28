# Section 4 Render Implementation

Video: `Why Everyone Pretends To Be Busy`
Section: `Section 4: Your Apps Invented Emergencies`
Status: `section preview built - ready for review (rebuilt v2)`

## Result
- Preview project: `section-previews/section-04-your-apps-invented-emergencies/`
- Port: `1004`
- Studio URL: `http://localhost:1004/#project/Build%20a%20Channel`
- Direct comp URL: `http://localhost:1004/api/projects/Build%20a%20Channel/preview/comp/index.html`
- Runtime: `42.133s` · Voiceover 0.86 pause-tuned
- Word timings: `voiceover/section-04-.../section-04-word-timings.json` (generated; all cues word-pinned)

## REBUILD v3 2026-06-22 (per user review - real app branding)
User approved REAL app branding for this section (overrides the default no-logos rule) and asked for:
(1) an iPhone notification screen instead of the blank phone; (2) real app icons (Gmail, Messenger,
To Do, Google Calendar) on the email/chat/task/calendar beats; (3) a better/suitable scene-2 image
(the red emergency button was unsuitable); (4) a non-white-phone visual for the reply/thumbs-up beat.

As-built (5 scenes):
- Scene 1 (0–12.96): CSS iPhone notification screen - notification cards INSIDE the phone with real icons (Gmail/Messenger/To Do/Calendar), revealing on each app word.
- Scene 2 (12.92–23.14): CSS app-icon overload grid - 6 real app icons (Gmail/Messenger/To Do/Calendar/WhatsApp/Slack) with red notification badges (12/99+/5/8/47/3) + FIVE APPS / URGENT / "please ignore" / BAD DESIGN.
- Scene 3 (23.1–27.66): fire alarm "ALERT" (kept) - EVERY PING = EMERGENCY?.
- Scene 4 (27.62–34.54): CSS Messenger-style chat - bubbles (Quick question? / REPLY / and this one? / REPLY AGAIN) + thumbs-up icon + PROGRESS?. Replaces the white phone.
- Scene 5 (34.5–42.133): fridge (kept) - REAL WORK / GOING BAD / SAD VEGETABLE.
- Accumulating UI (notifications, badges, chat bubbles) lives in the SCENE divs so it persists; cues hold labels + WIT. Pexels is 403-blocked from this IP; full-HD bases + real icons sourced from Wikimedia.

## (superseded) REBUILD 2026-06-22 v2
User rejected v1: app-sketch bases were "poor and vague," low-res (960px), didn't suit the script, and were repeated; only 3 distinct scenes for 42s. v2 fixes all three:
- DISTINCT full-HD (≥1920px) object photos that clearly match each beat (sourced Wikimedia @1920).
- No repeated images (phone is a non-consecutive callback: scene 1 apps vs scene 4 chat).
- 5 scenes (up from 3).

## Bases (full-HD, CC, brand-free)
- Scene 1 `base-phone.jpg` (0–12.96) - hand + blank phone; CSS app icons fill the screen (email→chat→task→calendar)
- Scene 2 `base-button.jpg` (12.92–23.14) - big red emergency button (vignette); FIVE APPS / red dots / 99 / URGENT / "PLEASE IGNORE" / BAD DESIGN
- Scene 3 `base-alarm.jpg` (23.1–27.66) - red fire alarm "ALERT"; EVERY PING = EMERGENCY?
- Scene 4 `base-phone-2.jpg` (27.62–34.54) - phone callback; CSS chat bubbles + 👍 + PROGRESS?
- Scene 5 `base-fridge.jpg` (34.5–42.133) - open fridge; REAL WORK / GOING BAD / A SAD VEGETABLE (red circle on the produce)
- tracks A=1,B=3,C=4,D=5,E=6; cues track 2. Notification chaos = CSS (no real app logos).

## WIT (5 distinct poses): suspicious (S1) → holding-phone-panic (S2) → trapped-by-app-screen (S3) → confused (S4) → tiny-defeated (S5).

## Verification
- lint 0 errors (2 non-blocking warnings: track-2 density, etc.)
- validate 0 errors (40 contrast warnings on timeline-sampled hidden cues, non-blocking)
- snapshots verified across all 5 scenes; full-HD bases, readable labels, 👍 renders, safe WIT crops, fridge circle on produce, no label/WIT collisions
- export: none

## Notes
- Sourcing: StockSnap/rawpixel only serve ≤960–1300px (below full-HD), so bases come from Wikimedia @1920. Branded phones (Blackview/LG) and people-laptops rejected.
- Delivery 0.86 (matches S5-7); S1-3 are 0.84 - whole-video unification still pending.
