# Section 4 Visual Plan

Video: `Why Everyone Pretends To Be Busy`
Section: `Section 4: Your Apps Invented Emergencies`
Status: `revised (v3) - real app branding, iPhone/grid/chat screens`

> REVISION v3 2026-06-22 (per user review): user approved REAL app branding for this section
> (overrides the no-logos default). 5 scenes: (1) CSS iPhone notification screen with real app icons
> (Gmail/Messenger/To Do/Google Calendar) in notification cards; (2) app-icon overload grid (6 real
> icons + red badges) replacing the rejected emergency button; (3) fire alarm (kept); (4) Messenger
> chat conversation (bubbles + thumbs-up) replacing the white phone; (5) fridge (kept). Real app
> icons + thumbs-up icon from Wikimedia Commons; photo bases (alarm, fridge) full-HD. Pexels 403-blocked.
> WIT: suspicious → phone-panic → trapped-by-app → confused → tiny-defeated. See render IMPLEMENTATION.md.

> REVISION 2026-06-22 (per user review): v1's app-sketch bases were vague, low-res (960px), didn't
> suit the script, and repeated; only 3 distinct scenes. v2 rebuilds with DISTINCT full-HD (≥1920px)
> object photos that clearly match each beat, sourced from Wikimedia @1920 (StockSnap/rawpixel max
> ~960–1300px). 5 scenes, no repeats (phone = non-consecutive callback):
> 1. hand + blank phone (CSS app icons fill the screen) - "the apps"
> 2. big red emergency button - "everything is URGENT" (FIVE APPS / red dots / 99 / bad design)
> 3. red fire alarm "ALERT" - "every ping = a real emergency"
> 4. phone callback (CSS chat bubbles + 👍) - "reply / progress?"
> 5. open fridge - "a sad vegetable at the back"
> WIT: suspicious → phone-panic → trapped-by-app → confused → tiny-defeated (5 distinct).
> The cue word-timings below still hold; see render IMPLEMENTATION.md for the as-built 5-scene map.

## Section Goal
Show the second reason: modern tools manufacture fake urgency. Apps pile on (email→chat→task→calendar), everything gets a red dot / number / URGENT, the brain treats every ping as an emergency and files a thumbs-up under "progress" - while the one task that matters rots like a sad vegetable at the back of the fridge.

## Source Inputs
- Voiceover: `.../section-04-...david23-am_eric-0.86.mp3` (42.133s, 0.86 pause-tuned)
- Word timings: `voiceover/section-04-.../section-04-word-timings.json` (generated; cue times REAL)

## Visual Direction
- 4 big scenes, 9 cues. The notification chaos is CSS-built (generic red dots / badges / URGENT / chat bubbles) - channel rule: NO real app logos.
- Metaphor: the fake-emergency machine; the neglected real task = a sad vegetable in the fridge.
- WIT path: typing (calm work) → phone-panic (overload) → trapped-by-app (every ping = emergency) → tiny-defeated (the rotting task). 4 distinct poses.
- Bases (CC0 real photos via Openverse): app-sketch wireframe (A + C callback), dark laptop on black (B, great for red dots), open fridge (D punchline).
- Motion: hard-show default; impact (smash/stamp) on URGENT, BAD DESIGN, PROGRESS?, SAD VEGETABLE.

## Big Scene Plan
| Scene | Local Time | Voice | Base | Why | Reference |
|---|---:|---|---|---|---|
| A - the app pile | 0:00-12.96 | "tools invented emergencies… task app is confusing" | app-sketch wireframe (`base-appsketch.jpg`) | apps multiply: email→chat→task→calendar | CC0 StockSnap |
| B - everything is urgent | 12.96-23.14 | "five apps interrupting… is bad design" | dark laptop on black (`base-laptop.jpg`) | red dot/number/URGENT overload | CC0 StockSnap |
| C - every ping = emergency | 23.14-34.54 | "your brain starts treating… under progress" | app-sketch wireframe (callback) | reply/reply/thumbs-up = "progress" | CC0 StockSnap |
| D - the sad vegetable | 34.54-42.133 | "the one task that matters… back of the fridge" | open fridge (`base-fridge.jpg`) | the neglected real task rots | CC0 Wikimedia |

## Cue State Timeline (word-timed)
| Cue | Time | Voice cue (word@s) | Scene | Change | Motion | WIT | Label |
|---|---:|---|---|---|---|---|---|
| C1 | 0–3.54 | "tools invented emergencies"@1.32 | A | label + WIT typing; first red dots | hard-show | typing-on-laptop | TOOLS INVENTED EMERGENCIES |
| C2 | 3.54–12.96 | email@3.54 / chat@5.8 / task@7.5 / calendar@10.16 | A | staggered app labels pile up | staggered hard-show | - | EMAIL → CHAT APPS → TASK APPS → CALENDAR APPS |
| C3 | 12.96–16.32 | "five apps"@14.46 | B | cut to laptop; FIVE APPS; WIT panic | transition + hard-show | holding-phone-panic | FIVE APPS INTERRUPTING |
| C4 | 16.32–19.58 | red dot@16.94 / number@18.08 / urgent@19.12 | B | red dots swarm + "99" + URGENT (smash) | staggered + smash | - | URGENT / 99 / red dots |
| C5 | 19.58–23.14 | "bad design"@22.3 | B | dry note + BAD DESIGN stamp | hard-show + stamp | - | "PLEASE IGNORE TIL NEXT WEEK?" / BAD DESIGN |
| C6 | 23.14–27.66 | "real emergency"@26.06 | C | cut to app sketch; EVERY PING = EMERGENCY?; WIT trapped | transition + hard-show | trapped-by-app-screen | EVERY PING = EMERGENCY? |
| C7 | 27.66–30.78 | "lands you reply"@28.06 / "reply again"@30.02 | C | chat bubbles REPLY / REPLY (staggered) | staggered hard-show | - | REPLY → REPLY |
| C8 | 30.78–34.54 | "thumbs up"@31.32 / "progress"@33.42 | C | 👍 + PROGRESS? (smash) | hard-show + smash | - | 👍 / PROGRESS? |
| C9 | 34.54–42.133 | task matters@35.12 / going bad@39.14 / sad vegetable@40.26 | D | cut to fridge; REAL WORK tag on lonely greens + GOING BAD + SAD VEGETABLE; WIT defeated | transition + hard-show | tiny-defeated | REAL WORK / STILL HERE / GOING BAD / SAD VEGETABLE |

## WIT Pose Plan
| Cue | Pose | Placement/Scale | Why |
|---|---|---|---|
| C1 | typing-on-laptop | lower-right ~1/2 | calm work before chaos |
| C3 | holding-phone-panic | lower-right ~1/2 | overload panic |
| C6 | trapped-by-app-screen | center ~1/2 | trapped by notifications |
| C9 | tiny-defeated | lower-right ~1/2 | the neglected task / defeat |
Density: 4 beats, 1 per scene. Faces safe; labels in their own zones.

## Reference And Asset Plan
| Asset | Source/Status | Use |
|---|---|---|
| base-appsketch.jpg | CC0 StockSnap | Scene A + C (app callback) |
| base-laptop.jpg | CC0 StockSnap | Scene B (dark, for red dots) |
| base-fridge.jpg | CC0 Wikimedia | Scene D punchline |
| 4 WIT poses | shared manifest | C1/C3/C6/C9 |
Notification chaos (red dots, 99 badge, URGENT, chat bubbles, thumbs-up) = CSS, brand-free (no real app logos).

## HyperFrames Guidance
- 1920x1080; 4 scenes (tracks 1/3/4/5), 9 cues (track 2); audio 42.133s.
- Cue starts pinned to word-timings; 0.2s scene fades; impact on URGENT/BAD DESIGN/PROGRESS?/SAD VEGETABLE.
- WIT ~1/2 frame, faces safe; labels upper/side, subtitle-safe.
- Must not invent: bases, WIT poses, label text, word-timed order. No real app logos - overlays are generic CSS.
- QA snapshots: 1.6 / 8.0 / 14.5 / 18.5 / 21.5 / 25.5 / 29.5 / 32.5 / 40.0s.

## Approval Checks
- reference pass done (Openverse CC0, viewed); bases brand/people-free; rejected branded/watermarked options
- A/C app-sketch is an intentional callback (non-consecutive); B and D distinct
- WIT varied (4 poses); word-timed; ready for HyperFrames
