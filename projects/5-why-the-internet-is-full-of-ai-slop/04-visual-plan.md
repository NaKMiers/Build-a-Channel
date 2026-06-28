# 04 Visual Plan (master)

Video: `Why The Internet Is Full Of Garbage Now`
Status: `master visual plan in progress`
Source skill: `visual-plan`
Source files: `02-script.md`, `03-voiceover.md`

## Video-Level Direction

- Audience: `A2-C1 English learners (interesting-English advantage)`
- Renderer: `HyperFrames (composited from pre-made assets)`
- Visual grammar: `real / real-looking base + mascot drawn on top; new scene ~per sentence; vary everything`
- Mascot character: `WIT - round bald white head, thick black outline, big rectangular glasses, dot eyes, flat white body. A real character with dry personality; big and high (1/3-1/2 frame), the soul of each scene. Poses ship on flat green #00B140 - chroma-key at render.`
- Tone on screen: `dry, savage-but-clean; edge aimed at the system/the feed, never the viewer; "garbage / slop / fake" carry the hook (strongest words kept out of the open)`
- Recurring motif: `the feed as a rising flood of grey sludge + WIT's glowing phone; the sludge is BORN in Section 1 (Scene 1.8) and should return at later beats (the spread, the payoff)`
- Scene-type rotation in use: `object-on-real-base / mascot-only focus / real-UI phone-or-card mockup / hero-evidence card / payoff-text`
- Pose library: `.agents/_shared/assets/wit/poses/` (palette; new poses may be invented)

## Section Index

| # | Section | Status | Duration | Scenes | Assets named | Section file |
|---:|---|---|---:|---:|---:|---|
| 1 | Hook: Is Any Of This Real? | planned | ~31.3s | 9 | 20 | `visual-plan/section-01-hook/section-01-hook-visual-plan.md` |
| 2 | It Has A Name: Slop | planned | ~36.7s | 8 | 14 | `visual-plan/section-02-it-has-a-name-slop/section-02-it-has-a-name-slop-visual-plan.md` |
| 3 | What Slop Actually Is | planned (v2 rebuild, generate-forward) | 40.7s | 9 | 10 generate + 8 browse + 9 poses | `visual-plan/section-03-what-slop-actually-is/section-03-what-slop-actually-is-visual-plan.md` |
| 4 | The Machine That Feeds Itself | not planned | 53.0s | - | - | - |
| 5 | It Already Got Out | not planned | 53.7s | - | - | - |
| 6 | It's Not AI's Fault (And Not A Plot) | not planned | 38.9s | - | - | - |
| 7 | Payoff: Attention In, Garbage Out | not planned | 43.4s | - | - | - |

## All Sections (scenes)

> Each section below is identical to its `visual-plan/section-XX-*/` file. Keep them in sync.

### Section 1: Hook: Is Any Of This Real?

Section goal: open a curiosity gap ("is any of this real?"), show the feed is full of fakes, name the
stakes, hand off to "why," and plant the sludge motif. Duration ~31.3s (audio 31.253s; scene times
ESTIMATED - no word-timings JSON yet). 9 scenes. Mascot arc: content scroll -> suspicious ->
calm/nostalgic -> deadpan -> cringe -> doubtful -> surprised -> drowning -> curious pivot.

#### Scene 1.1 - "Quick question. Pick up your phone, open any feed, and scroll for ten seconds."
- Time `0:00-0:05` (est). Role: cold-open instruction; establishes "your feed"; leads to the question.
- Layout: warm living-room real base; CSS feed phone floats center-right; giant WIT bottom-right holding phone; handwritten label upper-left.
- Base `couch-phone-evening-1.jpg` (browse). Mascot `holding_phone_pointing_smile.png` (right, ~1/2 frame, high), casual/absorbed scroll. Text `"scroll for 10 seconds"` upper-left on the cue.
- Show-as-you-say: base+WIT 0:00; feed slides up on "open any feed"; label on "scroll for ten seconds." SFX: soft scroll tick.

#### Scene 1.2 - "Now be honest: how much of that was actually made by a human?"
- Time `0:05-0:09.5` (est). Role: the curiosity gap snaps shut; mascot-only focus.
- Layout: near-empty dark phone-glow base; GIANT WIT centered, side-eye; big question top-center; `% HUMAN?` dial lower-right (subtitle-safe).
- Base `dark-room-phone-glow-1.jpg` (browse). Mascot `skeptical_side_eye_doubtful.png` (center, ~1/2 frame). Text `"how much is REAL?"` top-center on "be honest"; `% human?` dial on "made by a human."

#### Scene 1.3 - "Three years ago, the answer was easy. All of it."
- Time `0:09.5-0:13.5` (est). Role: calm nostalgic "before."
- Layout: warm older-laptop desk base; WIT left relaxed; `3 YEARS AGO` tag top-left; green `100% HUMAN` stamp center-right.
- Base `cozy-laptop-desk-1.jpg` (browse). Mascot `ok_hand_sign_content_closeup.png` (left). Text `"3 years ago"`, green stamp `"100% HUMAN"` impact on "All of it."

#### Scene 1.4 - "Today? Good luck."
- Time `0:13.5-0:16` (est). Role: hard turn; deadpan closeup; the joke is the flatness.
- Layout: cool phone-on-table base (soft blur); WIT center closeup deadpan (safe crop); `today...` upper-left then `good luck.` lower-right.
- Base `phone-on-table-screen-on-1.jpg` (browse). Mascot `deadpan_unimpressed_half_lidded.png` (center closeup). SFX: dry bonk/silence.

#### Scene 1.5 - "Because somewhere in that feed there is a photo of a shrimp shaped like Jesus,"
- Time `0:16-0:20` (est). Role: first fake; iconic absurd hero.
- Layout: living-room base; CSS phone post left-center showing Shrimp Jesus with absurd fake engagement; WIT right cringing; caption lower-center.
- Base `social-scroll-livingroom-1.jpg` (browse). Hero `shrimp-jesus.jpg` (browse, Commons; verify license). Mascot `cringe_uneasy_drool.png` (right). Text `"...a shrimp. as Jesus."` on "shaped like Jesus."

#### Scene 1.6 - "a news story about an event that never happened,"
- Time `0:20-0:23` (est). Role: second fake; real-UI fake-news card; WIT flips left.
- Layout: blurred newsroom base; fake news card center-right; red `DIDN'T HAPPEN` cross-out; WIT left doubtful.
- Base `newsroom-blur-1.jpg` (browse). Card `fake-news-card.png` (generate; or render-CSS real-UI). Mascot `pondering_skeptical_hand_on_chin.png` (left). Red markup on "never happened."

#### Scene 1.7 - "and a hit song by a band that does not exist."
- Time `0:23-0:26.5` (est). Role: third fake; real-UI music-app card; WIT flips right.
- Layout: blurred music base; dark artist card center with "1,000,000+ monthly listeners"; `0 REAL MEMBERS` tag; WIT right surprised.
- Base `music-studio-blur-1.jpg` (browse). Card `fake-band-card.png` (generate; or render-CSS real-UI). Mascot `mildly_surprised_hand_at_chin.png` (right). Text `"0 REAL MEMBERS"` on "does not exist."

#### Scene 1.8 - "The internet is filling up with garbage. Cheap, fake, mass-produced garbage. And the strange part is, nobody told it to."
- Time `0:26.5-0:30` (est). Role: motif birth + thesis; the sludge floods; giant WIT drowning.
- Layout: murky grey-sludge base rising from bottom; slop bits bob in it; GIANT WIT center sinking (swim pose, head/arms above the line); huge `GARBAGE` top; `cheap. fake. mass-produced.` chips one-per-word; `nobody told it to.` lower.
- Base `grey-sludge-flood-1.jpg` (browse). Mascot `swimming_underwater_goggles_cap.png` (center, ~1/2 frame). Reuse `shrimp-jesus.jpg`; add `ai-extra-fingers-hand.png` (browse Commons; verify license). SFX: low watery flood swell.

#### Scene 1.9 - "Let's find out why."
- Time `0:30-0:31.3` (est). Role: button/pivot; mascot-only focus; energy reset.
- Layout: settled darker grade of the sludge base (continuity); WIT center pointing up curious; big `WHY?`.
- Base `grey-sludge-flood-1.jpg` (reuse, settled grade). Mascot `pointing_up_curious_open_mouth.png` (center). Text `"WHY?"` on "why." SFX: upward whoosh into Section 2.

Section 1 asset list: see `visual-plan/section-01-hook/section-01-hook-visual-plan.md` (Section Asset
Summary) - 12 image assets (8 real bases incl. 1 reused, 2 Commons AI-slop images, 2 generate cards)
+ 9 library poses. Full per-scene detail (composition %, elements, emotion, linkage, sound, color,
asset table) lives in the section file and is the source of truth; this master block is its synced summary.

### Section 2: It Has A Name: Slop

Section goal: NAME the phenomenon ("slop", Word of the Year), then reframe - not "AI is evil", not a
master plan; it's cheap content + pay-for-attention. End on the flood "still rising." Duration ~36.7s
(scene times ESTIMATED; render will pin to word timings). 8 scenes. Mascot arc: announcing -> disgusted
-> proud -> dismissive -> deadpan -> skeptical -> teaching -> uneasy. Full detail in the section file.

- 2.1 `0:00-4.6` "...we call it slop." - sludge motif base (reuse, darker) + WIT presenting (right); "SLOP" stamp smash on "slop".
- 2.2 `4.6-9.2` "...grey mush you pour into a pig trough." - `pig-trough-slop-1.jpg` + WIT disgust (left); "grey mush" arrow.
- 2.3 `9.2-15.2` "...Word of the Year in 2025." - `dictionary-open-1.jpg` + CSS dictionary entry + gold WotY badge; WIT proud (right).
- 2.4 `15.2-20.8` "...AI is evil and the robots are coming." - `toy-robot-1.jpg` + "AI = EVIL ROBOTS" red cross-out; WIT waving off (center).
- 2.5 `20.8-23.0` "That's a different video." - sludge (reuse, very dark) mascot-only deadpan closeup; caption.
- 2.6 `23.0-28.6` "...not because of some master plan." - `corkboard-redstring-1.jpg` conspiracy board + "A MASTER PLAN" red cross-out; WIT skeptical (left).
- 2.7 `28.6-34.8` "...pays you for attention, not for quality." - `coins-pile-1.jpg` + CSS `ATTENTION=PAID` vs greyed `QUALITY`; WIT teaching (right).
- 2.8 `34.8-36.7` "So a flood started. And it is still rising." - sludge motif (reuse), rising overlay + giant WIT uneasy (center); "STILL RISING" smash.

Section 2 assets: 5 new browse photos (pig-trough, dictionary, toy-robot, corkboard-redstring, coins-pile)
+ reuse `grey-sludge-flood-1.jpg` (motif) + 8 library poses; dictionary card / WotY badge / ATTENTION-vs-QUALITY
/ crossed-cliché labels are render-CSS. Full per-scene detail in the section file (source of truth).

### Section 3: What Slop Actually Is (v2 REBUILD - generate-forward, no sludge)

REBUILT 2026-06-28 (owner-directed): v1 over-reused the sludge and leaned on browsed/old photos. v2 is
wild + GENERATE-FORWARD with a bespoke surreal hero per scene; the section's new motif is THE SLOP
MACHINE (a content-grinder), NOT the sludge. Timing pinned to REAL word-timings. 9 scenes. Mascot arc:
announcer -> sarcastic awe -> horror -> baffled -> howling laugh -> flattened -> blasted -> smug -> deadpan.

- 3.1 `0-2.96` "...three things." - factory base + GEN `slop-machine` (brain in, grey slop out); WIT announcing (right); "3 THINGS".
- 3.2 `2.96-6.80` "...looks fine." - studio + GEN `ai-influencer-perfect` (flawless plastic); WIT mock-awe (left); "1. LOOKS FINE".
- 3.3 `6.80-9.80` "...falls apart. six fingers." - studio (reuse) + GEN `ai-influencer-melting` (same shot glitching, 6 fingers) + red circle; WIT horror (right).
- 3.4 `9.80-11.10` "gibberish." - night storefront + GEN `gibberish-melting-sign`; WIT baffled (left).
- 3.5 `11.10-17.48` "...'Coca-Coola.'" - holiday street + GEN `coca-coola-ad-fail` (parody, no real logo) + red circle; WIT howling (right).
- 3.6 `17.48-25.94` "...costs you everything." - server room + GEN `cost-crush-pile` (clocks/eyes/hearts avalanche) CRUSHING WIT (`lying_down_fainted_dead`, center); time/attention/trust labels.
- 3.7 `25.94-33.22` "...made by the thousand... fire hose." - pipes + GEN `slop-firehose` + GEN `slop-clone` (tiled) + "10,000+"; WIT blasted (center-right).
- 3.8 `33.22-37.26` "...That is slop." - factory callback + reuse `slop-machine` + GEN `certified-slop-stamp`; WIT smug (right).
- 3.9 `37.26-40.704` "a machine pretending to be a person, at full volume." - dark stage + GEN `robot-human-mask` (robot in human mask screaming into a mic) + volume-MAX; WIT deadpan (bottom-left).

Section 3 assets: 10 GENERATE heroes (slop-machine, ai-influencer-perfect/melting, gibberish-melting-sign,
coca-coola-ad-fail, cost-crush-pile, slop-firehose, slop-clone, certified-slop-stamp, robot-human-mask) +
8 FRESH browse bases + 9 library poses. NO sludge. CSS: "3 THINGS", marks, red circles, checks, counters,
maker/cost labels, volume meter. Full detail in the section file.

### Section 4: The Machine That Feeds Itself
`not planned`

### Section 5: It Already Got Out
`not planned`

### Section 6: It's Not AI's Fault (And Not A Plot)
`not planned`

### Section 7: Payoff: Attention In, Garbage Out
`not planned`

## Cross-Section Continuity

- Reused assets (filename -> scenes): `shrimp-jesus.jpg` -> 1.5, 1.8; `ai-extra-fingers-hand.png` -> 1.8; `grey-sludge-flood-1.jpg` -> 1.8, 1.9, 2.1, 2.5, 2.8 (the flood motif in S1-S2 ONLY; deliberately NOT used in S3 after the overuse note). S3 v2 has its own motif `slop-machine.png` -> 3.1, 3.8; `studio-backdrop-1.jpg` -> 3.2, 3.3; `factory-interior-1.jpg` -> 3.1, 3.8.
- Motif discipline (owner-directed 2026-06-28): do NOT reuse one base across many sections as a crutch. Each section earns its own bold imagery; the flood/sludge stays an S1-S2 device, not a universal background.
- Recurring motif / callback scenes: the grey-sludge flood (born 1.8) should return for Section 5 ("It
  Already Got Out") and the Section 7 payoff; WIT's glowing phone recurs through the feed scenes.
- Mascot emotional arc across the video (planned): hook = suspicion -> drowning -> curiosity; body should
  build to unimpressed-at-the-machine (S4), drowning again (S5), pointing-at-the-culprit (S6), tired-but-clear (S7).

## Stale / Regeneration Notes

- Sections 1, 2, and 3 are planned. Sections 4-7 are `not planned`.
- STALE (S3 v2 rebuild 2026-06-28): the existing Section 3 render (`section-previews/section-03-what-slop-actually-is/`) is now STALE - rerun `visual-implement section 3` then `render section 3`. The S3 v1 browse assets `gallery-wall-1.jpg`, `ai-face-does-not-exist.png`, `hourglass-time-1.jpg`, `holiday-bokeh-red-1.jpg` are now ORPHANED (v2 does not use them); remove only on explicit request.
- Section 2 downstream not yet created: its new assets (`assets/`) and its render (`section-previews/section-02-*/`). Run `visual-implement section 2` then `render section 2`.
- Downstream for Section 1 (not yet created): implemented assets in `assets/`, `05-production-board.md`,
  `section-previews/section-01-hook/`, `hyperframes/`, `renders/`, `06-review.md`, `07-upload.md`,
  `08-self-learning.md`. None exist yet, so nothing is stale.

## Next Step Boundary

Next workflow step: `visual-implement` (creates the assets named here for Section 1), then `render`.
