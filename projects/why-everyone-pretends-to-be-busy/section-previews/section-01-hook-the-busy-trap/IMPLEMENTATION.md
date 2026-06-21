# Section 1 Render Implementation

Video:
`Why Everyone Pretends To Be Busy`

Section:
`Section 1: Hook: The Busy Trap`

Status:
`section preview built — ready for review`

## Result

- Preview project: `section-previews/section-01-hook-the-busy-trap/`
- Source: `05-visual-plan.md` Section 1 + generated word timings
- Port: `1001`
- Studio URL: `http://localhost:1001/#project/Build%20a%20Channel`
- Direct composition URL: `http://localhost:1001/api/projects/Build%20a%20Channel/preview/comp/index.html`
- Runtime: `21.056s`
- Voiceover: `voiceover/section-01-hook-the-busy-trap/...david23-am_eric-0.84.mp3`
- Visual plan: `visual-plan/section-01-hook-the-busy-trap/section-01-hook-the-busy-trap-visual-plan.md`

## Big Scene / Cue Plan Implemented

| Cue | Local Time | Voice Cue | Big Scene | What Changes | Motion Type | WIT Placement / Crop Guard | Label / Markup | Sync Status |
|--:|--:|---|---|---|---|---|---|---|
| 1 | 0.30 | "Here's a" | A | REAL WORK folder | hard-show | — | REAL WORK | pinned |
| 2 | 2.50/4.32 | "less time"/"important" | A | contradiction label + pulse | hard-show+pulse | — | LESS TIME = MORE IMPORTANT? | pinned |
| 3 | 5.48–8.14 | "full calendar…panic" | A | URGENT/99+/dots + panic WIT | smash+staggered | giant ~1/2 frame, lower-right, face safe | URGENT, 99+ | pinned |
| 4 | 9.18 | "this person matters" | A | sarcastic label | hard-show | — | "THIS PERSON MATTERS" | pinned |
| 5 | 11.10/11.48 | "sit quietly" | B | cut to desk + thinking WIT | hard-show | ~1/3 frame, lower-left | THINKING... | pinned |
| 6 | 13.34/14.32/14.90 | "lazy"/"asleep" | B | deadpan WIT + LAZY? + (OR ASLEEP) | stamp smash | ~1/2 frame, lower-right, face safe | LAZY?, (OR ASLEEP) | pinned |
| 7 | 16.40/19.12 | "everyone gets busy"/"looking" | C | cut to cage + trapped WIT + label | hard-show | ~1/2 frame, centered behind bars, face safe | LOOKING BUSY | pinned |
| 8 | 20.02 | "There is a difference" | C | dry button | small smash | — | THERE IS A DIFFERENCE. | pinned |

## Render Review-Prevention Pass

- voice cue map completed: yes — built from generated `section-01-word-timings.json`
- big-scene sanity checked: yes (3 scenes; A/C calendar bookend, B contrast)
- cue density checked: yes (8 cues / 21s)
- motion density checked: yes (hard-show default; impact only on important/URGENT/LAZY?/button)
- WIT density: 4 beats (A1/B2/C1)
- WIT crop/collision checked: yes (faces in frame; labels clear of faces; verified in snapshots)
- markup target checked: yes (URGENT on calendar overload, LAZY? on the quiet scene, cage on calendar)
- scene differentiation checked: yes (A bright / B calm / C cool+bars)
- HyperFrames mechanics checked: yes (data attrs, audio clip, synchronous GSAP, deterministic)
- render decisions made beyond visual plan: tightened all cue times to generated word timings (plan times were `estimated`); discovered the dry button lands at ~19.96 (not ~18.8 as estimated) and re-pinned; enlarged panic WIT after first snapshot read small.

## Timing Source

- Generated `voiceover/section-01-hook-the-busy-trap/section-01-word-timings.json` via Whisper (`@xenova/transformers` `Xenova/whisper-tiny.en`, WASM) — the documented Windows recipe. First two model loads failed with "Unsupported model type" due to a partial download (ECONNRESET); a retry after the model fully cached succeeded. The final two words had a chunk-boundary timestamp glitch and were corrected by hand (a=20.46, difference.=20.58–21.0).

## Assets

- Shared asset folder: `projects/why-everyone-pretends-to-be-busy/assets/` (canonical: fonts/, wit/, visual-references/)
- Section assets: local `assets/` working set copied into the preview (NOT a junction). Junctions fail to serve under HyperFrames CLI on this Windows setup (documented in render memory), so a minimal copied working set is used: fonts/patrick-hand-latin.woff2, wit/ (4 poses), visual-references/section-01-.../ (2 calendar variants + minimal desk).
- Attribution: `assets/visual-references/section-01-hook-the-busy-trap/ATTRIBUTION.md` (both bases Public Domain, brand-free, people-free)

## Verification

- lint: 0 errors, 1 non-blocking warning (track-2 density = 8 cues, intentional)
- validate: 0 errors (35 contrast warnings are timeline-sampled against hidden cues / dark root; labels have solid light backgrounds and read clearly in snapshots — non-blocking)
- inspect: package.json `inspect --at` set to cue/reveal points
- direct preview snapshots/contact sheet: `snapshots/contact-sheet.jpg` + key frames at 7.6 / 15.0 / 19.4s
- export/render: not requested (no MP4/WebM created)

## Scene-Base Revision (2026-06-21)

User rejected the first render's real photo bases (dingy 2007 wall calendar + overhead desk) as
"filthy and bad." No image-generation tool is available this session and clean brand/people-free
real photos were not findable, so all three scene bases were rebuilt as clean **flat-illustrated
self-made bases** (channel identity is bold flat 2D illustration, not photoreal):

- Scene A/C: CSS calendar wall (`.cal-wall`) — cream paper, thick ink grid, header band, weekday
  row, day numbers, cells packed with colored event chips (reads as overbooked). Scene C adds a
  cool veil + vertical cage bars.
- Scene B: CSS desk room (`.desk-scene`) — wall + warm wood desk, notebook, pen, mug, plant, empty calm space.

Cue order, WIT poses, and all word-timed cue timing are UNCHANGED. The old photos remain on disk
as `inspiration only` but are no longer referenced by the composition. Re-verified: lint 0 errors,
validate 0 errors (contrast warnings are timeline-sampled on the many small calendar cells, non-blocking),
contact sheet at 0.8/4.4/7.6/9.6/12.0/14.6/17.5/20.4s confirms clean bases, readable labels, and
safe WIT crops.

## Scene-Base Revision 2 (2026-06-22) — FINAL: real-world CC0 photos

User rejected the flat-illustrated CSS bases ("use real images or generated images instead of
this... find real-world images"). No image generator is connected, so bases were sourced as clean
real-world CC0 stock photos via the Openverse API (Pexels/Bing/Google were bot-blocked):

- Scene A (overload): `base-deskwork.jpg` — warm wood desk (coffee, notebook, pen, generic laptop), CC0 StockSnap. Overload conveyed by overlays (URGENT/99+/dots) + panic WIT.
- Scene B (quiet): `base-deskcalm.jpg` — bright minimal white desk (frame, glasses, notepad, plant), CC0 StockSnap. Distinct cool/white palette.
- Scene C (cage): `base-deskwork-cage.jpg` (copy of A) cooled + cage bars = "trapped at the busy desk" (A→C bookend).

Both viewed for brand/people safety (none). The motif shifted from a literal calendar to the
work-desk (no clean people-free calendar photo was findable). Cue order, WIT, and word-timed
timing unchanged. lint 0 errors; validate 0 errors (30 non-blocking contrast warnings). Contact
sheet at 0.8/4.4/7.6/12.0/14.8/17.5s confirms clean bases. The earlier CSS-illustration base is
superseded.

## Notes

- Voiceover delivery mismatch flagged upstream: Section 1 audio is plain/0.84; Sections 4-7 are pause-tuned/0.86. If S1 audio is re-rendered at 0.86, regenerate word timings and re-pin cues (duration will change).
