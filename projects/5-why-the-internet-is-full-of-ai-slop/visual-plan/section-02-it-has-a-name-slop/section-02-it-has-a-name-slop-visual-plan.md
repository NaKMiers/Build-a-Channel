# Section 2 Visual Plan - It Has A Name: Slop

Video: `Why The Internet Is Full Of Garbage Now`
Section: `Section 2: It Has A Name: Slop`
Status: `draft visual plan for approval`

## Video-Level Direction (for context - keep identical to master)

- Audience: A2-C1 English learners (interesting-English advantage).
- Renderer: HyperFrames (composited from pre-made assets).
- Visual grammar: real / real-looking bright base + mascot drawn on top; a new scene roughly per sentence; vary everything (base, WIT side/scale/pose, idea-device).
- Mascot: WIT - round bald white head, thick black outline, big rectangular glasses, dot eyes, flat white body. Big and high (1/3-1/2 frame), real personality. Poses are TRANSPARENT cutouts in `assets/poses/` (used directly, no keying).
- Tone on screen: dry, savage-but-clean; edge aimed at the system, never the viewer.
- Recurring motif: the feed as a rising flood of grey sludge ("slop"); born in S1 (Scene 1.8), NAMED here in S2, returns later.
- Scene-type rotation: motif-base+stamp / object-hero (pig) / real-UI card / crossed-cliché / mascot-only focus / crossed-cliché / money-contrast / motif payoff.
- Pose library: `.agents/_shared/assets/wit/poses/` (transparent; new poses may be invented).

## Section Overview

- Section goal: give the phenomenon a NAME ("slop", Word of the Year), then reframe - it is NOT "AI is evil" or a master plan; it is cheap content + pay-for-attention. End on the flood "still rising."
- Duration: `~36.7s` (audio `section-02-...-0.80.mp3`, 36.715s). No word-timings JSON yet, so scene times are ESTIMATED; render will generate word timings and re-pin.
- Scene count: `8`
- Scene-type rotation: 2.1 motif+SLOP stamp / 2.2 pig-trough object hero / 2.3 dictionary real-UI card / 2.4 crossed "evil robots" cliché / 2.5 deadpan mascot-only / 2.6 crossed "master plan" board / 2.7 money attention-vs-quality / 2.8 flood payoff.
- Mascot arc: announcing -> disgusted -> proud/matter-of-fact -> dismissive -> deadpan -> skeptical -> teaching -> uneasy at the rising flood.

## Scenes

### Scene 2.1 - "This stuff actually has a name now. We call it slop."

- **Local time:** `0:00-0:04.6` (estimated)
- **Role:** Continues directly from S1's flood; names it. The "SLOP" reveal is the hero. Bridges S1->S2.
- **Composition / layout:** The grey-sludge motif base (darkened so white reads, per S1 feedback). WIT right, presenting toward center-left. A huge handwritten/stamp word "SLOP" slams center over the sludge. Small lead-in label top-left.
- **Elements:**
  - *Base (full frame):* `grey-sludge-flood-1.jpg` (reuse from S1, graded darker ~0.5) - motif continuity.
  - *Big word (center):* "SLOP" - giant, bold, stamped.
  - *Lead-in label (top-left):* handwritten "it finally has a name..."
  - *WIT right:* see Mascot.
- **Mascot:** pose `presenting_open_palm_talking.png`; placement right, scale ~1/2 frame, high anchor, facing left toward the word; expression matter-of-fact presenting.
- **On-screen text:** `"it finally has a name..."` handwritten cream, top-left, on "a name now"; `"SLOP"` huge yellow-with-dark-outline, center, slams on "slop" (~3.8).
- **Emotion:** the murk from S1 gets a label - a small "aha."
- **Insight / joke:** the gross flood you just saw? It has an official, perfect name.
- **Linkage / eye path:** lead-in (top-left) -> SLOP (center) -> WIT presenting (right).
- **Show-as-you-say:** base+WIT from 0:00; lead-in on "a name now"; "SLOP" smash on "slop."
- **Sound:** a wet "splat"/stamp on SLOP.
- **Color / contrast:** dark sludge; SLOP pops yellow; WIT white reads on the darkened base.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `grey-sludge-flood-1.jpg` | reuse | murky grey/green sludge (the motif), graded darker | base, full frame | reuse (S1) |
| `presenting_open_palm_talking.png` | pose | WIT presenting, open palm, talking | right, ~1/2 frame | reuse (library) |

(The "SLOP" word is a render CSS big-word, not a stored asset.)

### Scene 2.2 - "Slop. Like the grey mush you pour into a pig trough."

- **Local time:** `0:04.6-0:09.2` (estimated)
- **Role:** Literal, funny definition - real pig slop. Distinct object hero.
- **Composition / layout:** A real photo of a pig at a trough (or a slop bucket) fills frame. WIT left, looking at it with disgust. A handwritten arrow+label "grey mush" points at the trough.
- **Elements:**
  - *Base (full frame):* `pig-trough-slop-1.jpg` - a real pig eating from a trough / a bucket of pig slop, no faces, bright.
  - *Label + arrow:* handwritten "grey mush" with an arrow to the trough.
  - *WIT left:* see Mascot.
- **Mascot:** pose `annoyed_disgusted_open_frown.png`; placement left, scale ~1/2 frame, high anchor, facing right; expression disgust ("ugh").
- **On-screen text:** `"grey mush"` handwritten cream + red arrow to the trough, on "grey mush"; optional small `"(yes, pig slop)"` on "pig trough."
- **Emotion:** comedic disgust; the word's origin is literally pig food.
- **Insight / joke:** "slop" isn't a metaphor we softened - it's pig-trough mush.
- **Linkage / eye path:** WIT disgust (left) -> arrow -> trough (center/right).
- **Show-as-you-say:** base+WIT from 0:04.6; "grey mush" + arrow on "grey mush"; "(yes, pig slop)" on "pig trough."
- **Sound:** a comedic "slop"/squelch.
- **Color / contrast:** earthy farm tones; cream label + red arrow pop.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `pig-trough-slop-1.jpg` | browse-real-photo | real pig at a trough / bucket of pig slop, no faces, full-HD, CC0 | base, full frame | new |
| `annoyed_disgusted_open_frown.png` | pose | WIT disgusted, open frown | left, ~1/2 frame | reuse (library) |

### Scene 2.3 - "And that is not an insult I invented - 'slop' was literally named Word of the Year in 2025."

- **Local time:** `0:09.2-0:15.2` (estimated)
- **Role:** Credibility - it's an official word, not the narrator being rude. Real-UI dictionary card.
- **Composition / layout:** A real open-dictionary / book photo base. A clean "Word of the Year 2025" dictionary-entry card floats center-right. WIT right, proud/matter-of-fact. A gold "2025" badge.
- **Elements:**
  - *Base (full frame):* `dictionary-open-1.jpg` - a real open dictionary / book page, warm, no faces.
  - *Dictionary card (center, CSS real-UI):* `slop` entry - "slop /slɒp/ noun - low-effort mass-produced content" + a banner "WORD OF THE YEAR 2025."
  - *WIT right:* see Mascot.
- **Mascot:** pose `proud_explaining_hand_on_chest_hand_on_hip.png`; placement right, scale ~1/2 frame, high anchor, facing left; expression mock-proud ("it's official").
- **On-screen text:** dictionary card text (CSS); gold badge `"WORD OF THE YEAR 2025"` lands on "Word of the Year"; the word `slop` highlights on "slop."
- **Emotion:** dry vindication - the dictionary agrees.
- **Insight / joke:** this is a real, awarded word, not a cheap jab.
- **Linkage / eye path:** dictionary card (center) -> gold badge -> WIT proud (right).
- **Show-as-you-say:** base+WIT from 0:09.2; card on "not an insult I invented"; gold badge smash on "Word of the Year"; "2025" pulse on "2025."
- **Sound:** a light "ding"/page flip.
- **Color / contrast:** warm paper; the gold WotY badge pops.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `dictionary-open-1.jpg` | browse-real-photo | real open dictionary / book page, warm, no faces, full-HD, CC0 | base, full frame | new |
| `proud_explaining_hand_on_chest_hand_on_hip.png` | pose | WIT mock-proud, hand on chest | right, ~1/2 frame | reuse (library) |

(The dictionary "slop" entry + WotY badge are render CSS real-UI, not stored assets.)

### Scene 2.4 - "Now, one thing to get straight right away. This is not a video about how AI is evil and the robots are coming."

- **Local time:** `0:15.2-0:20.8` (estimated)
- **Role:** Knock down the wrong frame (sci-fi AI panic). Crossed-cliché scene.
- **Composition / layout:** A real photo of a cheesy vintage toy robot (the "evil robots" cliché) as base/hero. A big red cross-out over a handwritten "AI = EVIL ROBOTS" label. WIT center, waving it off.
- **Elements:**
  - *Base (full frame):* `toy-robot-1.jpg` - a real vintage tin/toy robot, fun, no faces, bright.
  - *Crossed label:* handwritten "AI = EVIL ROBOTS" with a big red X / cross-out.
  - *WIT center:* see Mascot.
- **Mascot:** pose `eyes_closed_talking_open_palm.png`; placement center (slightly left), scale ~1/2 frame, high anchor; expression calm dismissal ("not that").
- **On-screen text:** `"AI = EVIL ROBOTS"` handwritten, then a red cross-out strikes through it on "the robots are coming"; small `"nope"` near WIT.
- **Emotion:** reassuring, dry - we're not doing the scary-robot story.
- **Insight / joke:** the obvious panic take is the wrong one.
- **Linkage / eye path:** toy robot (base) -> crossed label (center) -> WIT waving off.
- **Show-as-you-say:** base+WIT from 0:15.2; "AI = EVIL ROBOTS" on "AI is evil"; red cross-out smash on "robots are coming"; "nope" deadpan.
- **Sound:** a red-marker scribble on the cross-out.
- **Color / contrast:** retro metal robot; red cross-out is the only red, pops.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `toy-robot-1.jpg` | browse-real-photo | real vintage tin/toy robot, fun, no faces, full-HD, CC0 | base, full frame | new |
| `eyes_closed_talking_open_palm.png` | pose | WIT calm, open palm, "not that" | center, ~1/2 frame | reuse (library) |

### Scene 2.5 - "That's a different video."

- **Local time:** `0:20.8-0:23.0` (estimated)
- **Role:** Dry punchline. Mascot-only focus beat (rhythm reset).
- **Composition / layout:** Near-black: the sludge base darkened heavily (or a dark vignette). WIT center closeup, deadpan. One small caption.
- **Elements:**
  - *Base (full frame):* `grey-sludge-flood-1.jpg` (reuse, graded very dark) - keeps motif but reads near-black for a clean focus beat.
  - *WIT center closeup:* see Mascot.
  - *Caption:* small handwritten "(that's a different video.)"
- **Mascot:** pose `deadpan_unimpressed_half_lidded.png`; placement center, closeup ~1/2-2/3 frame, safe crop (no face cut); expression flat deadpan.
- **On-screen text:** `"(that's a different video.)"` handwritten, lower-center (subtitle-safe), hard-shows on the line.
- **Emotion:** dry comedy; a beat of stillness.
- **Insight / joke:** the flat throwaway dismissal of the robot-apocalypse genre.
- **Linkage / eye path:** WIT deadpan (center) -> caption (below).
- **Show-as-you-say:** cut to WIT closeup on "That's"; caption hard-shows on "different video."
- **Sound:** dry silence / a single soft tick.
- **Color / contrast:** near-black; WIT white dominant.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `grey-sludge-flood-1.jpg` | reuse | sludge base graded very dark for a focus beat | base, full frame | reuse (S1/2.1) |
| `deadpan_unimpressed_half_lidded.png` | pose | WIT flat deadpan | center closeup, safe crop | reuse (library) |

### Scene 2.6 - "This is about something quieter, and honestly dumber. The internet did not get worse because of some master plan."

- **Local time:** `0:23.0-0:28.6` (estimated)
- **Role:** Reject the conspiracy/"master plan" frame. Crossed-cliché board.
- **Composition / layout:** A real photo of a cork "conspiracy board" (pins + red string) as base. A handwritten "MASTER PLAN?" label gets a red cross-out. WIT left, skeptical.
- **Elements:**
  - *Base (full frame):* `corkboard-redstring-1.jpg` - a real cork board with pins and red string (the conspiracy-board trope), no faces.
  - *Crossed label:* handwritten "A MASTER PLAN" with a red cross-out.
  - *WIT left:* see Mascot.
- **Mascot:** pose `skeptical_side_eye_doubtful.png`; placement left, scale ~1/2 frame, high anchor, facing right; expression "nope, not a plot."
- **On-screen text:** `"A MASTER PLAN"` handwritten, then red cross-out on "some master plan"; small `"quieter + dumber"` near WIT on "quieter, and honestly dumber."
- **Emotion:** debunking, dry - the boring truth, not a thriller.
- **Insight / joke:** no shadowy villain; it's dumber than a conspiracy.
- **Linkage / eye path:** WIT skeptical (left) -> conspiracy board + crossed label (center/right).
- **Show-as-you-say:** base+WIT from 0:23.0; "quieter + dumber" on "quieter, and honestly dumber"; "A MASTER PLAN" + red cross-out on "some master plan."
- **Sound:** marker scribble on cross-out.
- **Color / contrast:** corkboard browns; red string + red cross-out pop.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `corkboard-redstring-1.jpg` | browse-real-photo | real cork board with pins + red string (conspiracy-board trope), no faces, full-HD, CC0 | base, full frame | new |
| `skeptical_side_eye_doubtful.png` | pose | WIT skeptical side-eye | left, ~1/2 frame | reuse (library) |

### Scene 2.7 - "It got worse because making fake content became almost free - and the internet pays you for attention, not for quality."

- **Local time:** `0:28.6-0:34.8` (estimated)
- **Role:** The real reason (preview of S4's thesis). Money / attention-vs-quality contrast. Key line.
- **Composition / layout:** A real pile-of-money/coins photo base. A CSS contrast device center: `ATTENTION = PAID` (with a coin) vs `QUALITY = ignored` (greyed/crossed). WIT right, teaching (finger raised).
- **Elements:**
  - *Base (full frame):* `coins-pile-1.jpg` - a real pile of coins / cash, bright, no faces.
  - *Contrast device (center, CSS):* two stacked chips - `ATTENTION` lit with a coin + `PAID`; `QUALITY` greyed with a small `ignored`.
  - *Small label:* "fake content = almost free."
  - *WIT right:* see Mascot.
- **Mascot:** pose `lecturing_finger_raised_eyes_closed.png`; placement right, scale ~1/2 frame, high anchor, facing left; expression mock-authoritative ("here's the actual reason").
- **On-screen text:** `"almost FREE to make"` on "almost free"; `ATTENTION = PAID` lights on "pays you for attention"; `QUALITY` greys/crosses on "not for quality."
- **Emotion:** the click of understanding - it's an incentive, not evil.
- **Insight / joke:** the platform pays for eyeballs, so junk that grabs eyeballs wins.
- **Linkage / eye path:** "almost free" -> ATTENTION=PAID (lit) -> QUALITY (greyed) -> WIT teaching (right).
- **Show-as-you-say:** base+WIT from 0:28.6; "almost FREE" on "almost free"; ATTENTION chip on "attention"; QUALITY grey/cross on "not for quality."
- **Sound:** a coin "cha-ching" on ATTENTION; a dull thud on QUALITY.
- **Color / contrast:** gold coins; ATTENTION chip gold-lit, QUALITY desaturated.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `coins-pile-1.jpg` | browse-real-photo | real pile of coins / cash, bright, no faces, full-HD, CC0 | base, full frame | new |
| `lecturing_finger_raised_eyes_closed.png` | pose | WIT mock-authoritative, finger raised | right, ~1/2 frame | reuse (library) |

(The ATTENTION/QUALITY contrast chips are render CSS, not stored assets.)

### Scene 2.8 - "So a flood started. And it is still rising."

- **Local time:** `0:34.8-0:36.7` (estimated)
- **Role:** Motif payoff - the flood rises; bridges into the rest of the video. Giant WIT.
- **Composition / layout:** The grey-sludge motif base; a sludge gradient rises higher than in S1. WIT center, GIANT, uneasy as the level climbs. Big "STILL RISING" + a small rising level marker.
- **Elements:**
  - *Base (full frame):* `grey-sludge-flood-1.jpg` (reuse) - the flood, rising overlay higher.
  - *Rising sludge overlay:* taller than S1's.
  - *Big text:* "STILL RISING."
  - *WIT center:* see Mascot.
- **Mascot:** pose `worried_uneasy_wide_eyes.png`; placement center, GIANT (~1/2 frame), high anchor (head clear), facing viewer; expression uneasy as the sludge climbs.
- **On-screen text:** `"a flood started"` on "a flood started"; `"STILL RISING"` big, lands on "still rising" (smash); the rising overlay climbs on the line.
- **Emotion:** dread building - this is just the beginning.
- **Insight / joke:** naming it didn't stop it; it's growing.
- **Linkage / eye path:** "a flood started" -> rising sludge -> WIT uneasy (center) -> "STILL RISING."
- **Show-as-you-say:** base+WIT from 0:34.8; "a flood started" on the words; sludge climbs + "STILL RISING" smash on "still rising."
- **Sound:** a low rising water swell into Section 3.
- **Color / contrast:** dark sludge; "STILL RISING" pops yellow; WIT white reads on the darkened base.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `grey-sludge-flood-1.jpg` | reuse | the sludge-flood motif base, rising overlay | base, full frame | reuse (S1/2.1/2.5) |
| `worried_uneasy_wide_eyes.png` | pose | WIT uneasy, wide eyes | center, ~1/2 frame | reuse (library) |

## Section Asset Summary

| Filename | Type | First scene | Reused in | Notes |
|---|---|---|---|---|
| `grey-sludge-flood-1.jpg` | reuse | 2.1 | 2.5, 2.8 | the slop/flood MOTIF (carried from S1); graded differently per scene |
| `pig-trough-slop-1.jpg` | browse-real-photo | 2.2 | - | literal "pig slop" hero |
| `dictionary-open-1.jpg` | browse-real-photo | 2.3 | - | Word-of-the-Year base |
| `toy-robot-1.jpg` | browse-real-photo | 2.4 | - | "evil robots" cliché (crossed out) |
| `corkboard-redstring-1.jpg` | browse-real-photo | 2.6 | - | conspiracy "master plan" board (crossed out) |
| `coins-pile-1.jpg` | browse-real-photo | 2.7 | - | money / attention-is-paid base |
| `presenting_open_palm_talking.png` | pose | 2.1 | - | library |
| `annoyed_disgusted_open_frown.png` | pose | 2.2 | - | library |
| `proud_explaining_hand_on_chest_hand_on_hip.png` | pose | 2.3 | - | library |
| `eyes_closed_talking_open_palm.png` | pose | 2.4 | - | library |
| `deadpan_unimpressed_half_lidded.png` | pose | 2.5 | - | library (also S1) |
| `skeptical_side_eye_doubtful.png` | pose | 2.6 | - | library (also S1) |
| `lecturing_finger_raised_eyes_closed.png` | pose | 2.7 | - | library |
| `worried_uneasy_wide_eyes.png` | pose | 2.8 | - | library |

## Approval Checks

- each scene picturable from text alone: yes
- ~one scene per sentence, scene-types varied: yes (8 scenes, rotated types)
- every scene has a real/real-looking base: yes (5 new photos + the sludge motif; no bare gradients)
- mascot big/high with a specific pose+expression per scene: yes (varied side/scale/pose)
- show-as-you-say timeline present per scene: yes (timing ESTIMATED - render will pin to word timings)
- every asset has type + description + filename + layout: yes
- repeated subjects reuse the same filename: yes (grey-sludge-flood across 2.1/2.5/2.8 as the motif, graded differently)
- public figures handled as caricature/parody, punching up: n/a (none)
- no image-generation prompts written here: correct (descriptions only)
- in sync with master `04-visual-plan.md`: yes
