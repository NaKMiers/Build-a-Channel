# Section 1 Render Implementation

Video:
`Why Countries Fight to Host the World Cup (and Lose Billions)`

Section:
`Section 1: Hook: The Trophy Prints A Receipt`

Status: `built + QA-passed, preview live, awaiting owner review`

## Result

- Preview project: `previews/1-hook/` (NEW-project folder convention)
- Source: `visual-plan/section-01-hook/section-01-hook-visual-plan.md` (followed 1:1)
- Port: `1001`
- Studio URL: `http://localhost:1001/#project/1-hook`
- Direct composition URL: `http://localhost:1001/api/projects/1-hook/preview/comp/index.html`
- Runtime: `35.904s` (root data-duration clamped to real audio; whisper last-word end runs to 36.44)
- Voiceover: `section-01-hook.mp3` (copy of owner-locked `scratch-audio/section-01-hook-david23-am_eric-0.81.mp3`)
- Visual plan: all 7 scenes implemented as planned; render-side deviations listed below

## Big Scene / Cue Plan Implemented

| Cue | Local Time | Voice Cue | Big Scene | What Changes | Motion Type | WIT Placement / Crop Guard | Label / Markup | Sync Status |
|---:|---:|---|---|---|---|---|---|---|
| 1 | 0.00 | "Every four years" | 1.1 fireworks night town | cold open: WIT + trophy + confetti drift | static + drift | fan-cheer giant left, knees crop | - | word-pinned |
| 2 | 4.18 | "Cup" | 1.1 | `WINNER!` stamp | impact (smash) | - | red stamp top-right | word-pinned |
| 3 | 4.74 | "trophy" | 1.1 | glint pop on globe | small impact | - | - | word-pinned |
| 4 | 5.26 | "party" | 1.1 | extra confetti burst (6 pcs) | pop | - | - | word-pinned |
| 5 | 5.86 | "And a very strange" | 1.2 spotlight podium | hard cut; trophy cold grade | hard cut | - | - | word-pinned |
| 6 | 6.72 | "prize" | 1.2 | price tag swings in + settles | reveal + pendulum | - | `1st PRIZE:` | word-pinned |
| 7 | 7.76 | "chance" | 1.2 | WIT right-edge peek | hard-show | skeptical peek, chest crop, head inside | - | word-pinned |
| 8 | 8.98 | "dollars" | 1.2 | `LOSE BILLIONS` stamps on tag | impact | - | red stamp line | word-pinned |
| 9 | 9.66 | "and countries" | 1.3 vintage map | hard cut; trophy on plinth; frozen WIT | hard cut | frozen mid-cheer mid-left | - | word-pinned |
| 10 | 10.26 | "fight" | 1.3 | label + receipt printer starts (5.6s crawl) | hard-show + clip-path wipe | - | `they FIGHT for this` | word-pinned |
| 11 | 12.16 | "Zurich" | 1.3 | gag chip 1 (paper plane) | pop | - | `Zurich` | word-pinned |
| 12 | 13.50 | "promo" | 1.3 | gag chip 2 (clapperboard) | pop | - | `promo video` | word-pinned |
| 13 | 15.66 | "beg" | 1.3 | gag chip 3 (clasped hands) | pop | - | `pretty please` | word-pinned |
| 14 | 16.06 | "which is strange" | 1.4 ledger | hard cut; pondering WIT | hard cut | bottom-right, torso crop | - | word-pinned |
| 15 | 17.22 | "hosting" | 1.4 | verdict line 1 | hard-show | - | ink handwriting | word-pinned |
| 16 | 18.56 | "never" | 1.4 | verdict line 2 (`NEVER` red) | hard-show | - | ink + red | word-pinned |
| 17 | 19.10 | "money" | 1.4 | double underline scribbles | impact (scaleX) | - | red bars tied to span | word-pinned |
| 18 | 19.76 | "Economists" | 1.5 dark desk | hard cut; row 1 stamps | hard cut + smash | - | checklist card | word-pinned |
| 19 | 21.54 | "politicians" | 1.5 | row 2 stamps | smash | - | - | word-pinned |
| 20 | 22.12 | "Even" | 1.5 | deadpan WIT arrives | hard-show | center closeup, shoulders crop | - | word-pinned |
| 21 | 22.66-22.92 | "trophy knows" | 1.5 | row 3 + googly eyes pop + nod + blink | pop + rotate | - | - | word-pinned |
| 22 | 23.90 | "Look at it" | 1.6 gold bokeh | hard cut; glamour trophy | hard cut | - | - | word-pinned |
| 23 | 25.24/25.44/25.98 | "Shiny/Golden/Beautiful" | 1.6 | 3 sparkle glints | pops | - | - | word-pinned |
| 24 | 26.96 | "behind" | 1.6 | pan x:-1100 reveals receipt pile | 0.6s ease pan | curious peek left edge @27.30 | - | word-pinned |
| 25 | 28.30 | "receipt" | 1.6 | `the bill` label + arrow | hard-show | - | red label + SVG arrow | word-pinned |
| 26 | 29.80 | "long receipt" | 1.6 | extra fold flops onto pile | impact | - | - | word-pinned |
| 27 | 30.78 | "So here" | 1.7 dark curtain | hard cut; giant WIT + receipt drape | hard cut | center giant, hips crop, face clear | - | word-pinned |
| 28 | 33.48 | "money" | 1.7 | `loses money` + red strike | hard-show + scaleX | - | white hand + red bar | word-pinned |
| 29 | 34.38 | "why" | 1.7 | `...so why PAY?` | impact pop | - | warm white, `PAY?` underlined | word-pinned |

## Render Review-Prevention Pass

- voice cue map completed: yes - built from `section-01-word-timings.json` (existing, monotonic; plan's pinned times verified against the JSON word-by-word)
- big-scene sanity checked: yes - 7 distinct bases, no repeated layout in consecutive scenes
- cue density checked: yes - 29 reveals / 35.9s but grouped per scene; ordinary labels hard-show, impacts only on emphasis
- motion density checked: yes - one continuous motion max per scene (confetti drift / receipt crawl / pan)
- WIT density: 7 appearances over 7 scenes (1 per big scene; plan-directed)
- WIT crop/collision checked: yes - all faces/heads/shoulders in frame; S7 drape moved OFF the face (was covering the mouth in first snapshot); text zones kept clear of WIT faces both ways
- markup target checked: yes - underlines/strikes are span-tied bars; `the bill` arrow points into the CSS-controlled pile; no rings on photos
- scene differentiation checked: yes - trophy reuse is the intended hero motif; each scene re-grades it
- HyperFrames mechanics checked: scenes on tracks 1-7 (no same-track overlap), audio track 30, cue elements have CSS `opacity:0` defaults, no percentage-translate on smashed elements, no emoji glyphs (SVG icons for plane/clapper/hands/checks/arrow), off-canvas WIT via `data-layout-allow-overflow` + `overflow:visible`
- render decisions made beyond visual plan (documented deviations):
  1. Map fold seam: plan said hide behind podium; the seam extended above/below it, so the base uses `transform:scale(2.09)` (left-region crop) + sepia warm grade - seam fully out of frame.
  2. S3 receipt: rwrap pivots at top-center on the plinth (rotate 35deg) with taller plinth so the strip visibly prints FROM the podium and rolls over WIT's feet.
  3. S6 pan is x:-1100 (not ~-670) so the fold pile stays fully off-frame during the glamour phase; trophy exits almost fully - the receipt + label carry phase B per plan intent.
  4. S7 receipt drape sits across shoulder/chest (rotate 60deg) - first placement covered WIT's mouth; fixed via snapshot QA.

## Verification

- lint: 0 errors, 2 warnings (`duplicate_media_discovery_risk` for trophy x5 / receipt x6 - intentional hero/motif reuse)
- validate: 0 errors, 0 warnings, 40 contrast advisories (ink text on cream cards measured against the photo behind the card - known non-blocking class)
- inspect: 0 layout issues across 10 samples
- snapshots: full 23-frame contact-sheet pass + targeted re-snaps after fixes (receipt pivot, fold pile, drape, map grade)
- snapshot tool artifact (NOT a composition bug): in screenshot-fallback mode the FIRST captured frame can miss a late-decoding PNG (trophy missing at first frame in 3 runs, pose missing once mid-run); re-snapshots confirm all elements render. Watch for this if an MP4 export is ever requested.
- export/render: NOT created (no explicit export request)

## Environment notes (first render on the Linux box)

- Ports below 1024 are privileged on Linux; fixed via `sudo sysctl -w net.ipv4.ip_unprivileged_port_start=1000` (non-persistent - re-run after reboot or persist in /etc/sysctl.d).
- The preview-local `assets` is a plain symlink to `../../assets` and the CLI serves it fine (HTTP 200) - the Windows junction/hardlink workaround is NOT needed here.
- Preview project id resolves to the FOLDER name `1-hook` (checked via /api/projects).
- GSAP CDN script carries SRI (`integrity` + `crossorigin`).
