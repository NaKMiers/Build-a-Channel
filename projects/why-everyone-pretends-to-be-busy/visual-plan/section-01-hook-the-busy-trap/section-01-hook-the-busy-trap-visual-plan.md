# Section 1 Visual Plan

Video:
`Why Everyone Pretends To Be Busy`

Section:
`Section 1: Hook: The Busy Trap`

Status:
`revised (v3) — scene bases are real-world CC0 photos (work desk / minimal desk / cooled desk + cage)`

> FINAL base decision (2026-06-22): after the flat-illustration attempt below was also rejected,
> bases are clean real-world CC0 stock photos sourced via Openverse: `base-deskwork.jpg` (Scene A),
> `base-deskcalm.jpg` (Scene B), `base-deskwork-cage.jpg` (Scene C, cooled + bars). Motif shifted
> from a literal calendar to the work desk (no clean people-free calendar photo findable). See
> ATTRIBUTION.md and the render IMPLEMENTATION.md.

## Asset-Base Revision (2026-06-21)

The first render used real public-domain photos (a dated, dingy 2007 wall calendar + an awkward
overhead desk). The user rejected them as "filthy and bad." No image-generation tool is available
this session, and clean brand-free/people-free real photos of "busy calendar / quiet desk" were not
findable on Commons. Because the channel identity is bold flat 2D illustration (not photoreal), the
three scene bases are rebuilt as clean, crafted **flat-illustrated self-made bases** — a justified
self-made descriptive base per the Real Scene Base Rule (NOT bare gradients: each is a fully drawn
calendar wall / desk room / cage). Scene structure, cue order, WIT poses, and word-timed cue timing
are unchanged.

- Scene A base: flat-illustrated FULL calendar wall (cream paper, thick ink grid, header band,
  weekday row, day numbers, many cells packed with colored event chips = overbooked, one red-circled day).
- Scene B base: flat-illustrated calm desk room (soft wall + warm wood desk, notebook, pen, mug, plant, empty space).
- Scene C base: same calendar wall (callback) with a cool/dark veil + vertical cage bars.
- Old photo bases kept on disk as `inspiration only` (`assets/visual-references/section-01-hook-the-busy-trap/`).

## Section Goal

In ~21s, show the contradiction of the whole video: looking busy reads as important, while real work and quiet thinking read as lazy. Establish the recurring motif (the calendar that fills up and then becomes a cage) and put WIT inside the system as the victim.

## Source Inputs

- Script: `02-script.md` Section 1
- Voiceover: `voiceover/section-01-hook-the-busy-trap/scratch-audio/section-01-hook-the-busy-trap-david23-am_eric-0.84.mp3`
- Script promise: title/thumbnail "Why Everyone Pretends To Be Busy" / trapped-by-calendar
- Section duration: `21.056s` (no word-timings JSON; cue times are `estimated` from duration + marked-script beats)

## Narration

```text
Here is a strange rule about modern life.
The less time you have for real work, the more important you look.
A full calendar, a loud inbox, a phone making tiny panic sounds. People see that and think, this person matters.
But sit quietly and think about one hard problem, and people assume you are lazy. Or asleep with your eyes open.
So everyone gets busy. Or at least, everyone gets very good at looking busy. There is a difference.
```

## Visual Direction

- Big-scene/cue rhythm: 3 big scenes, 7 cue states (within the 20-25s hook default)
- Big scene rhythm: overload (calendar) -> quiet contrast (desk) -> cage (calendar callback)
- Cue-state count: 7
- Main visual metaphor: the calendar that fills with fake urgency, then closes into a cage
- WIT emotional path: panicked (overload) -> calm/thinking, then judged -> trapped
- WIT density: 4 beats total (A:1, B:2, C:1)
- Motion density: mostly hard-show; impact reserved for the contradiction label, URGENT swarm, LAZY? stamp, and the cage slam
- Real-life texture: real public-domain wall calendar + minimal desk photos as scene bases
- Real image references: 2 safe-asset PD bases (calendar, minimal desk); see reference board
- Generated/support assets: none (no image-gen tool); overlays built in HyperFrames
- Viewer attention strategy: open inside the situation; topic object on screen by 3s; contradiction by ~5s; WIT emotion by ~8s; motif payoff by the cage
- Retention risk: a hook about an abstract idea ("busy") can feel like a lecture
- Visual fix: anchor every beat to one concrete object (calendar, desk, folder) and let WIT carry the feeling
- Red markup: red URGENT dots, red contradiction "?", red LAZY? stamp — each targets a specific object
- Motion rule: ordinary labels hard-show on the spoken beat; impact only on emphasis/proof/cage

## Big Scene Plan

| Big Scene | Local Time | Voice Range | Persistent Base Visual | Why This Scene Exists | When To Cut Away | Reference Basis | Asset Path / Prompt |
|---|---:|---|---|---|---|---|---|
| A — The overload | 0:00-0:08.5 | "Here is a strange rule…" → "…this person matters." | Wall-calendar photo, bright; cells fill red; a small ignored `REAL WORK` folder bottom-left | Establish topic + contradiction: a full calendar reads as "important" | When narration turns to quiet thinking | PD wall calendar | `assets/visual-references/section-01-hook-the-busy-trap/sceneC-wall-calendar.jpg` |
| B — Sit quietly and think | 0:08.5-0:15.0 | "But sit quietly and think…" → "…asleep with your eyes open." | Minimal quiet desk photo (notebook, pencils, cup), calm empty space | Contrast: quiet real thinking reads as "lazy" | When narration concludes "everyone gets busy" | PD minimal desk | `assets/visual-references/section-01-hook-the-busy-trap/sceneB-minimal-desk.jpg` |
| C — The calendar cage | 0:15.0-0:21.056 | "So everyone gets busy…" → "There is a difference." | Wall-calendar photo (callback), cooler grade; grid lines become vertical cage bars | Payoff motif: looking busy = trapped; sets the channel's recurring cage | End of section | PD wall calendar (intentional bookend callback) | `assets/visual-references/section-01-hook-the-busy-trap/sceneC-wall-calendar.jpg` |

## Cue State Timeline

Timing = `estimated` (no word-timings JSON for this section).

| Cue | Local Time | Voice Cue | Big Scene | What Changes On Screen | What Stays | Motion Type | WIT Pose / Size / Safe Crop | Label / Markup | Asset Need | Why This Cue Exists |
|---|---:|---|---|---|---|---|---|---|---|---|
| C1 | 0:00-0:02.2 | "Here is a strange rule about modern life." | A | Calendar base in; small `REAL WORK` folder appears bottom-left | Calendar base | hard-show | none | `REAL WORK` (handwritten, small) | calendar base | Show topic object by 3s; plant the thing that gets ignored |
| C2 | 0:02.2-0:05.5 | "The less time you have for real work, the more important you look." | A | A few calendar cells flip red; red question label punches in | Calendar, REAL WORK folder | impact (on "more important") | none | `LESS TIME = MORE IMPORTANT?` (red) | calendar base | State the contradiction by ~5s |
| C3 | 0:05.5-0:08.5 | "A full calendar, a loud inbox, a phone making tiny panic sounds… this person matters." | A | Red URGENT dots swarm; `99+` inbox badge + `!!!` ping cards pile on; WIT rises panicked | Calendar (now busy/red) | impact | `holding-phone-panic` — GIANT, ~1/2 frame, lower-right half-body rise; face/glasses fully in frame | `URGENT` ×, `99+`, `!!!` | calendar base + WIT png | WIT emotion by ~8s; overload peak |
| C4 | 0:08.5-0:12.0 | "But sit quietly and think about one hard problem," | B | Hard cut to calm minimal desk; WIT thinking; `THINKING…` label | Desk base | transition (cut) + hard-show | `thinking` — medium, ~1/3 frame, seated-left; head/shoulders safe | `THINKING…` (handwritten) | desk base + WIT png | Visual reset; show quiet real work |
| C5 | 0:12.0-0:15.0 | "and people assume you are lazy. Or asleep with your eyes open." | B | Red `LAZY?` stamp slaps over the calm scene; WIT deadpan reaction | Desk base | impact (stamp on "lazy") | `deadpan-side-eye` — GIANT, ~1/2 frame, side peek; face fully in frame | `LAZY?` (red stamp) | desk base + WIT png | Land the unfair judgment; dry joke |
| C6 | 0:15.0-0:18.8 | "So everyone gets busy. Or at least, everyone gets very good at looking busy." | C | Hard cut to calendar; vertical cage bars slam down over the grid; WIT trapped behind bars | Calendar base (cooler) | transition + impact (cage slam) | `trapped-by-app-screen` — GIANT, ~1/2 frame, centered behind bars; face/hands gripping, fully in frame | `LOOKING BUSY` (handwritten) | calendar base + WIT png | Payoff motif: busy = trapped |
| C7 | 0:18.8-0:21.056 | "There is a difference." | C | Dry button label appears; everything else holds still | Calendar cage + trapped WIT | hard-show | `trapped-by-app-screen` persists (no new WIT) | `There is a difference.` (handwritten, upper area) | — | Dry section button; lead into Section 2 |

## WIT Pose Plan

WIT source: shared manifest `.agents/_shared/assets/wit/poses/` (project has no local WIT folder).

| Cue | Time | Emotion | Pose File | Placement / Scale | Safe Crop / Margin | Why WIT Is Needed |
|---|---:|---|---|---|---|---|
| C3 | 0:05.5-0:08.5 | panic / overwhelmed | `wit-pose-holding-phone-panic.png` | Lower-right, half-body rise from bottom edge, ~1/2 frame | Lower body may exit bottom; face/glasses/hands fully inside | Overload peak — WIT feels the fake urgency |
| C4 | 0:08.5-0:12.0 | calm / focused | `wit-pose-thinking.png` | Left third, seated, ~1/3 frame | Head/shoulders safe; no edge crop on face | Show quiet real thinking as the contrast |
| C5 | 0:12.0-0:15.0 | dry / unimpressed | `wit-pose-deadpan-side-eye.png` | Right side peek, ~1/2 frame | Side peek; face/glasses fully in frame | React to the unfair "lazy" judgment |
| C6 | 0:15.0-0:18.8 | trapped | `wit-pose-trapped-by-app-screen.png` | Centered behind cage bars, ~1/2 frame | Face + gripping hands fully in frame; bars overlay, not crossing face | Payoff: looking busy = trapped |

WIT density note:
- Total WIT beats: 4
- WIT beats per big scene: A=1, B=2, C=1
- Any big scene above 2 WIT beats: none
- Cue states intentionally without WIT: C1, C2 (build the calendar/contradiction), C7 (text button; trapped WIT from C6 persists but is not a new beat)

## Markup And Label Plan

| Cue | Time | Text / Markup | Motion Type | Target Object | Why It Helps | Avoid / Do Not Use |
|---|---:|---|---|---|---|---|
| C1 | 0:00 | `REAL WORK` | hard-show | The small folder bottom-left | Plants the thing that gets ignored | Don't bury it in the subtitle zone |
| C2 | 0:02.2 | `LESS TIME = MORE IMPORTANT?` (red) | impact | The reddening calendar | Names the contradiction | Keep ≤ one line; readable on mobile |
| C3 | 0:05.5 | `URGENT` ×, `99+`, `!!!` | impact | Calendar cells / inbox / phone | Shows the fake-emergency overload | No real app logos; generic badges only |
| C5 | 0:12.0 | `LAZY?` (red stamp) | impact | Over the calm desk / near WIT | Lands the unfair judgment | Stamp must not cover WIT's face |
| C6 | 0:15.0 | `LOOKING BUSY` + cage bars | impact | The calendar grid | Turns the grid into a prison | Bars must not cross WIT's face |
| C7 | 0:18.8 | `There is a difference.` | hard-show | Upper area, clear of WIT | Dry button; sets up the reframe | Don't cover trapped WIT's expression |

## Reference And Asset Plan

| Asset | Type | Source / Status | Use | Safety | Saved Path / Prompt |
|---|---|---|---|---|---|
| Wall calendar | Real photo | Commons PD (Claudio Elias) | Scene A + C base (bookend) | Safe (PD, brand-free, people-free) | `assets/visual-references/section-01-hook-the-busy-trap/sceneC-wall-calendar.jpg` |
| Minimal desk | Real photo | Commons PD (USVI gov) | Scene B base | Safe (PD, brand-free, people-free) | `assets/visual-references/section-01-hook-the-busy-trap/sceneB-minimal-desk.jpg` |
| Cluttered desk | Real photo | Commons PD (EFTA) | Mood/composition only | Inspiration only (Logitech+Casio brands) | `assets/visual-references/section-01-hook-the-busy-trap/sceneA-cluttered-desk.jpg` |
| WIT poses | PNG | shared `.agents/_shared/assets/wit/poses/` | C3/C4/C5/C6 | Safe (channel asset) | 4 pose files named above |

## Visual Resource Usage Map

| Resource | Used In Big Scenes / Cues | What It Supplies | When It Appears | Where On Screen / Crop | How It Is Used | Production Decision |
|---|---|---|---|---|---|---|
| sceneC-wall-calendar.jpg | A (C1-C3), C (C6-C7) | The calendar motif / grid | 0:00 and 0:15 | Full-frame `cover`; A bright, C cooler with cage bars | Direct base, graded differently per scene | Direct asset |
| sceneB-minimal-desk.jpg | B (C4-C5) | Calm quiet workspace | 0:08.5 | Full-frame `cover` | Direct base | Direct asset |
| wit-pose-holding-phone-panic.png | A (C3) | Overload emotion | 0:05.5 | Lower-right half-body, ~1/2 frame | Overlay, behind labels | Direct asset |
| wit-pose-thinking.png | B (C4) | Focus emotion | 0:08.5 | Left third, ~1/3 frame | Overlay | Direct asset |
| wit-pose-deadpan-side-eye.png | B (C5) | Dry reaction | 0:12.0 | Right side peek, ~1/2 frame | Overlay | Direct asset |
| wit-pose-trapped-by-app-screen.png | C (C6-C7) | Trapped payoff | 0:15.0 | Centered behind bars, ~1/2 frame | Overlay behind cage bars | Direct asset |

## HyperFrames Guidance

- Composition target: 1920x1080, 16:9
- Big scene count: 3
- Cue state count: 7
- Scene components: PD photo base (full-frame cover) + handwritten labels + red markup + WIT PNG overlay + calendar-cell/cage CSS overlays
- Timing notes: estimated from 21.056s audio; align to the MP3 on build. Topic by 3s, contradiction by ~5s, WIT by ~8s.
- Motion density rule: hard-show ordinary labels; impact only on C2 contradiction, C3 URGENT swarm, C5 LAZY? stamp, C6 cage slam
- Text style: handwritten labels/captions; red marker for URGENT/LAZY?/contradiction
- Asset paths: see Reference And Asset Plan
- Audio sync notes: section MP3 at 0.84 (21.056s) — note this section is currently plain/0.84 while S4-7 are 0.86 pause-tuned (delivery mismatch flagged in 04-voiceover.md)
- WIT pose files: holding-phone-panic, thinking, deadpan-side-eye, trapped-by-app-screen (shared poses)
- WIT density: 4 beats (A1/B2/C1)
- WIT scale and crop guards: emotional beats ~1/2 frame; never crop face/glasses/head/shoulders; only lower-body/edge peeks allowed
- No-WIT breathing beats: C1, C2, C7
- Suggested inspect timestamps: 0:01, 0:04, 0:07, 0:10, 0:13, 0:17, 0:20
- Suggested screenshot/contact-sheet QA timestamps: 0:07 (panic WIT ≥1/3 frame, no logos), 0:13 (LAZY? stamp not on WIT face), 0:17 (cage bars not across WIT face), 0:20 (button text clear of WIT)
- Suggested MP4 QA frame timestamps: only if export explicitly requested
- Build risks: brand leakage if a real phone photo is added (use generic badges only); cage bars overlapping WIT face; labels drifting into subtitle zone
- Must not invent: scene bases (provided), WIT poses (named), label text (provided), cue timing order (provided), motion types (provided), motif (calendar→cage). HyperFrames decides only exact pixel coordinates, easing curves, and grading to match the audio.

## Review-Prevention Checklist

- voice sync mapped to phrase cues: yes (each cue cites its phrase)
- big-scene rhythm avoids unrelated rapid boards: yes (3 scenes, motif-linked)
- cue density stays readable: yes (7 cues / 21s)
- motion density uses hard-show by default: yes
- impact motion reserved for emphasis: yes (C2/C3/C5/C6)
- WIT rhythm not overused: yes (4 beats)
- WIT size readable: yes (≥1/3, emotional beats ~1/2)
- WIT crop safe: yes (only lower-body/edge peeks)
- WIT does not cover text/evidence: yes (separate label zones; C7 text upper, WIT lower/center)
- red markup targets exact objects: yes
- scene bases visually differentiated: yes (A bright calendar, B calm desk, C cool calendar-cage; A/C reuse is an intentional bookend)
- render does not need to invent timing/layout/assets: correct

## Approval Checks

- visual reference pass completed: yes (4 real refs, 2 safe-asset bases, viewed)
- what/when/how clear: yes
- big scenes grouped, not one full scene per sentence: yes
- cue states low enough for section duration: yes
- attention reason per big scene / cue state: yes
- label readable: yes (short, handwritten)
- WIT has a clear job: yes (panic / think / dry / trapped)
- WIT pose files named: yes
- WIT facial emotion large enough: yes (≥1/3 frame)
- WIT face/head/shoulder crop safe: yes
- WIT density counted and justified: yes (4; A1/B2/C1)
- no-WIT breathing beats planned: yes (C1/C2/C7)
- red markup points to exact object: yes
- ordinary labels hard-show unless emphasis needs impact motion: yes
- impact animation reserved for emphasized spoken beats: yes
- real-life asset explains, not decorates: yes (calendar = motif, desk = contrast)
- title-thumbnail promise still being paid off: yes (trapped-by-calendar payoff)
- safe for English learners: yes (short labels, one idea per beat)
- ready for HyperFrames: yes
