# Section 1 Visual Plan - Hook: The Trophy Prints A Receipt

Video: `Why Countries Fight to Host the World Cup (and Lose Billions)`
Section: `Section 1: Hook: The Trophy Prints A Receipt`
Status: `draft visual plan for approval`

## Video-Level Direction (for context - keep identical to master)

- Audience: `A2-C1 English learners (interesting-English advantage)`
- Renderer: `HyperFrames (composited from pre-made assets)`
- Visual grammar: `real / real-looking base + mascot drawn on top; new scene ~per sentence; vary everything`
- Mascot character: `WIT - round bald head, big rectangular glasses, expressive; big and high (giant on emotional beats), varied side/scale/pose per scene`
- Tone on screen: `savage-but-clean; edge aimed at FIFA / consultants / incentives, never a nation or its fans`
- Recurring motif: `the endless receipt (born in this hook, returns all video); secondary: the white-elephant feeding bowl (S6)`
- Scene-type rotation in use: `wide celebration / object hero close-up / wide gag + motif birth / evidence board / checklist device / glamour reveal / mascot-only focus`
- Pose library: `.agents/_shared/assets/wit/poses/` (palette; this plan invents 2 NEW fan poses)
- Safety: `parody trophy (NOT the real FIFA trophy sculpture - it is copyrighted artwork); no real country flags on WIT (nationality-neutral fan gear); no real people`

## Section Overview

- Section goal: open the paradox (countries fight to lose billions), name the World Cup in
  the first 2 seconds, give birth to the receipt motif, and land the hook question.
- Duration: `35.904s` (audio `section-01-hook-david23-am_eric-0.81.mp3`)
- Timing source: `voiceover/section-01-hook/section-01-word-timings.json` (whisper-tiny.en,
  generated 2026-07-02; monotonic, no backward jumps; clamp root duration to the real
  `35.904s` - whisper's last-word end runs to 36.44). Whisper mishearings ("governments'
  bag" = "beg", "Chinese, golden, beautifuls" = "Shiny. Golden. Beautiful.") do not affect
  the timestamps.
- Scene count: `7` (a visible change every ~4-6s)
- Scene-type rotation: 1.1 wide celebration -> 1.2 object hero -> 1.3 wide gag/motif birth
  -> 1.4 evidence board -> 1.5 checklist device -> 1.6 glamour reveal -> 1.7 mascot-only focus
- Mascot arc in this section: euphoric fan -> suspicious squint -> FROZEN mid-cheer (the
  money shot) -> pondering -> signature deadpan -> curious peek -> direct rhetorical challenge

## Scenes

### Scene 1.1 - "Every four years, one lucky country - this time, three - wins the World Cup. The trophy. The party."

- **Local time:** `0.00-5.80` (Every@0.00, three@2.92, Cup@4.18, trophy@4.74, party@5.26)
- **Role:** instant topic + celebration high the rest of the hook will invert. Links
  forward: this exact trophy gets a price tag in 1.2.
- **Composition / layout:** full-bleed real photo base: a giant multicolor festival
  firework bursting over a glittering night town (sourced; no identifiable people).
  Horizon ~65%. The parody golden trophy floats center-right
  (55-75% x, 25-80% y, drop shadow, slight upward glow). WIT giant on the LEFT (0-38% x,
  bottom-anchored high: head ~12% from top, legs cropped). Confetti (CSS, namespaced
  `.cfp`) falls across the top third. `WINNER!` stamp lands top-right (70-92% x, 8-18% y).
- **Elements:**
  - *Base (full-bleed):* one giant multicolor festival firework over a glittering night
    town - dark blue sky, vivid burst center-high; bright enough to read (grade ~0.8
    brightness, no dark scrim). Sourcing note (2026-07-02): no stadium in frame - the
    trophy, confetti, and `WINNER!` stamp carry the "won the World Cup" meaning.
  - *Trophy (center-right, ~28% width):* the video's hero object - a PARODY golden trophy:
    a plain golden globe sitting on a tall fluted gold cup body (deliberately NOT the real
    FIFA trophy sculpture); polished, one white specular glint; sits on a small dark
    plinth.
  - *Confetti:* sparse CSS confetti strips (gold/red/teal), top 35% of frame only.
  - *`WINNER!` stamp:* red handwritten stamp style, 4deg tilt, stamps in on Cup@4.18.
- **Mascot:** pose `NEW: wit-fan-flag-cheer.png` - WIT as a football fan: plain teal fan
  scarf (no real flag/colors of any country), one arm pumping a small blank teal pennant,
  huge open-mouth cheer, eyes squeezed happy. Placement LEFT, scale ~1/2 frame height
  (giant), bottom-cropped at the knees, facing right toward the trophy.
- **On-screen text:** `WINNER!` (red stamp, top-right, tilt 4deg) on Cup@4.18. Nothing else -
  the celebration is the message.
- **Emotion:** pure euphoria - the feeling every bidding country is chasing.
- **Insight / joke:** none yet; this is the setup being built up to be knocked down.
- **Linkage / eye path:** WIT (left, cheering) -> trophy (center-right) -> `WINNER!` stamp
  (top-right). Left-to-right rising diagonal = triumph.
- **Show-as-you-say:** base + WIT + trophy visible from 0.00 (cold open, already mid-party);
  confetti loops continuously; `WINNER!` stamps (impact) on Cup@4.18; small trophy shine
  sweep on trophy@4.74; one extra confetti burst on party@5.26.
- **Sound:** crowd-cheer swell under 0-2s (ducked low), confetti pop on party@5.26.
- **Color / contrast:** warm gold + night blue; trophy gold is the brightest object.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `stadium-fireworks-1.jpg` | browse-real-photo | fireworks over a stadium exterior at night, no people, warm gold bursts on dark blue sky | full-bleed base | new |
| `trophy-gold-parody.png` | generate | parody golden trophy: plain golden globe on a fluted gold cup body with small dark plinth, isolated, transparent bg - clearly NOT the real FIFA design | center-right ~28% width, floats with shadow | new (VIDEO HERO - reused all video) |
| `wit-fan-flag-cheer.png` | generate | NEW WIT pose: fan scarf (plain teal), pumping a small blank teal pennant, huge open-mouth cheer, eyes-closed joy - nationality-neutral | left, ~1/2 frame, knees cropped | new (fan-kit WIT, reused in 1.3 variant) |

### Scene 1.2 - "And a very strange prize: the chance to lose billions of dollars."

- **Local time:** `5.86-9.60` (prize@6.72, chance@7.76, dollars@8.98)
- **Role:** the twist - same trophy, new meaning. First contradiction beat (title promise).
- **Composition / layout:** hard cut to an object-hero close-up: dark spotlit podium photo
  base (single spotlight cone from top). The trophy (REUSED file) large center (35-65% x,
  15-85% y). A big handwritten paper price tag hangs from the trophy's neck on a string
  (swings in at 45-75% x, 40-62% y). WIT peeks from the RIGHT edge (78-100% x), closeup.
- **Elements:**
  - *Base (full-bleed):* dark stage/podium under one spotlight - moody but readable
    (~0.75 brightness in the cone).
  - *Trophy:* same `trophy-gold-parody.png`, now reads colder - slight cool grade,
    the glint gone.
  - *Price tag:* cream paper tag, rough string, handwritten text (see below); swings 3
    degrees; drop shadow.
- **Mascot:** pose `skeptical_side_eye_doubtful` (library); placement RIGHT edge peek,
  ~1/3 frame, cropped at chest (head+glasses fully inside frame), facing left at the tag;
  expression: half-lidded doubt.
- **On-screen text:** tag line 1 `1st PRIZE:` (black handwritten) appears with the tag on
  prize@6.72; tag line 2 flips/stamps below in red on dollars@8.98: `LOSE BILLIONS`.
- **Emotion:** suspicion; the smile dropping off the party.
- **Insight / joke:** the prize IS the bill - the entire video in one tag.
- **Linkage / eye path:** trophy (center) -> tag (hanging off it) -> WIT's doubting face
  (right). The tag physically connects prize and price.
- **Show-as-you-say:** cut lands on "And a very strange"@5.86 (music drops out); tag swings
  in (hard-show + pendulum settle) on prize@6.72; `LOSE BILLIONS` stamps (impact) on
  dollars@8.98; WIT hard-shows on chance@7.76.
- **Sound:** party audio cuts dead at 5.86 (the silence IS the joke); paper "fwip" on the
  tag; soft stamp thud on dollars.
- **Color / contrast:** cold spotlight gray + gold; the red `LOSE BILLIONS` is the only red
  in frame.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `podium-spotlight-1.jpg` | browse-real-photo | dark stage or podium under a single spotlight cone, no people | full-bleed base | new |
| `trophy-gold-parody.png` | reuse | the hero trophy, cool grade | center ~30% width | reuse (1.1) |
| `pose skeptical_side_eye_doubtful.png` | pose | library pose, right-edge closeup peek | right edge, ~1/3 frame, chest crop | reuse (library) |

### Scene 1.3 - "And countries FIGHT for this. Presidents fly to Zurich. Ministers film promo videos. Entire governments beg."

- **Local time:** `9.66-16.00` (fight@10.26, Zurich@12.16, promo@13.50, beg@15.66)
- **Role:** the absurdity montage + THE MOTIF IS BORN: the receipt starts printing at
  fight@10.26 and never stops for the rest of the video.
- **Composition / layout:** wide gag scene on a vintage world-map photo base. Trophy
  (reused) sits on a small podium center (42-58% x, 30-62% y). From its base, the RECEIPT
  begins to print and snake toward the lower-left, growing longer on each beat (by 16.00
  it reaches ~40% of frame width). WIT stands mid-frame-left (8-40% x), FROZEN mid-cheer as
  the receipt rolls over his feet at ~10.4. Three mini gag chips pop along the TOP band
  (12-88% x, 8-22% y), one per spoken beat, left to right.
- **Elements:**
  - *Base (full-bleed):* aged paper world map, warm parchment tones (~0.8 brightness) -
    literally "countries". Sourcing note (2026-07-02): the sourced map has a vertical
    fold seam near center - hide it behind the trophy podium or crop to one side.
  - *Receipt:* white paper roll unspooling from the trophy plinth; visible generic
    printed lines (no readable text - real text lands in later sections); curls once.
  - *Gag chip 1 (on Zurich@12.16):* small card: a tiny paper plane arcing toward a dot
    labeled `Zurich` (SVG plane icon, not emoji).
  - *Gag chip 2 (on promo@13.50):* small card: a film clapperboard icon labeled `promo video`.
  - *Gag chip 3 (on beg@15.66):* small card: two clasped begging hands icon labeled
    `pretty please` (handwritten).
- **Mascot:** pose `NEW: wit-fan-frozen-mid-cheer.png` - the SAME fan-kit WIT from 1.1
  (same teal scarf + pennant, arms still up) but face flipped to blank wide-eyed dread,
  tiny sweat drop, colors slightly desaturated. Placement mid-left, ~2/5 frame, knees
  cropped, facing camera. The joy/pose mismatch IS the gag.
- **On-screen text:** `they FIGHT for this` - red handwritten, underlined, lower-center
  (safe above subtitle zone), hard-shows on fight@10.26. Chip labels as above.
- **Emotion:** comic disbelief - the party face has not caught up with the bill.
- **Insight / joke:** governments compete for the thing the tag just said loses billions;
  the receipt motif is now alive.
- **Linkage / eye path:** frozen WIT (left) -> receipt at his feet -> up the receipt to the
  trophy (center) -> chip row (top) reading left-to-right with the narration.
- **Show-as-you-say:** cut on "And countries"@9.66; `they FIGHT for this` on fight@10.26 +
  receipt printer STARTS (continuous slow crawl, printer-tick SFX); chips pop (impact,
  small) at 12.16 / 13.50 / 15.66; WIT visible from cut, receipt touches his feet ~10.4.
- **Sound:** receipt printer tick-tick loop from 10.26 (quiet, recurring signature SFX);
  soft pops for chips.
- **Color / contrast:** warm parchment base; white receipt pops; red label is the anchor.
- **WIT density note:** WIT appears but does not move after the freeze - the receipt and
  chips carry the beats (breathing room per rhythm rule).

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `world-map-vintage-1.jpg` | browse-real-photo | aged parchment world map, warm tones, no modern borders emphasis, no flags | full-bleed base | new |
| `trophy-gold-parody.png` | reuse | hero trophy on small podium | center ~20% width | reuse (1.1) |
| `receipt-endless-roll.png` | generate | long white receipt paper strip, generic faint print lines, one soft curl, isolated on transparent bg (text-free so CSS can overlay items later) | unspools trophy base -> lower-left | new (VIDEO MOTIF - reused all video) |
| `wit-fan-frozen-mid-cheer.png` | generate | NEW WIT pose: identical fan kit to `wit-fan-flag-cheer` (teal scarf + pennant, arms up) but blank wide-eyed dread face + sweat drop, slightly desaturated | mid-left, ~2/5 frame, knees cropped | new (callback variant of 1.1 pose) |

### Scene 1.4 - "Which is strange. Because hosting the World Cup almost never makes money."

- **Local time:** `16.06-19.70` (strange@16.32, hosting@17.22, money@19.10)
- **Role:** the suspicious detail said plainly - the title's claim, on an evidence surface.
- **Composition / layout:** evidence-board scene: real photo base of a blank aged ledger
  page with a red center rule and alphabet index tabs (top-down scan). A big handwritten verdict is scrawled
  across the ledger's right page (50-92% x, 30-55% y). WIT sits at the RIGHT-bottom
  (60-100% x), ~2/5 frame, chest-up, as if he just wrote it.
- **Elements:**
  - *Base (full-bleed):* blank aged ledger page - cream paper, faint ruled lines, one red
    vertical center rule, alphabet index tabs on the right edge; bright (~0.85).
    Sourcing note (2026-07-02): no pen or printed figures in the photo - the handwritten
    verdict and CSS red marks carry the scene.
  - *Verdict text:* handwritten marker, two lines (see On-screen text), the word `NEVER`
    double-underlined in red.
- **Mascot:** pose `pondering_skeptical_hand_on_chin` (library); placement bottom-right,
  ~2/5 frame, torso crop at desk line; facing the written verdict; expression: weighing
  the claim.
- **On-screen text:** line 1 `hosting the World Cup` (black handwritten) on hosting@17.22;
  line 2 `almost NEVER makes money` (black, `NEVER` red double-underline) on never@18.56
  with the underline scribbling on money@19.10.
- **Emotion:** "wait, that's true?" - the viewer's own suspicion given a surface.
- **Insight / joke:** dry fact as graffiti on the accounting book itself.
- **Linkage / eye path:** ledger numbers (left) -> scrawled verdict (right) -> WIT's chin-
  scratch below it.
- **Show-as-you-say:** cut on "Which is strange"@16.06; line 1 hard-shows @17.22; line 2
  hard-shows @18.56; red underline scribbles (impact) on money@19.10.
- **Sound:** marker squeak on the underline; receipt tick continues faintly.
- **Color / contrast:** paper white + ink black; single red accent on `NEVER`.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `ledger-red-pen-1.jpg` | browse-real-photo | open accounting ledger with columns of figures and a red pen on it, top-down, no hands/brands | full-bleed base | new |
| `pose pondering_skeptical_hand_on_chin.png` | pose | library pose | bottom-right, ~2/5 frame, torso crop | reuse (library) |

### Scene 1.5 - "Economists know it. Politicians know it. Even the trophy knows it."

- **Local time:** `19.76-23.85` (Economists@19.76, politicians@21.54, Even@22.12, knows@22.92)
- **Role:** comic escalation of consensus, ending on the section's silliest gag (the trophy
  itself agrees).
- **Composition / layout:** checklist-device scene: dark wood desk photo base. A cream
  "WHO KNOWS IT?" checklist card floats LEFT (8-45% x, 15-75% y) with three rows that
  stamp in one by one. The trophy (reused) stands RIGHT (60-85% x, 25-80% y) and gets
  googly CSS eyes + a tiny nod tilt on its beat. WIT closeup peeks bottom-center between
  them (35-62% x), head+shoulders.
- **Elements:**
  - *Base (full-bleed):* dark wooden desk surface, soft window light, nothing branded.
  - *Checklist card:* cream paper, handwritten header `WHO KNOWS IT?`; rows: `economists`,
    `politicians`, `the trophy` - each row gets a fat red `✓` stamp (drawn SVG check, not
    emoji) on its word.
  - *Trophy:* same hero file + two round white googly eyes (CSS circles with dark pupils)
    that pop on and blink once; 2deg nod tilt on knows@22.92.
- **Mascot:** pose `deadpan_unimpressed_half_lidded` (library, the signature deadpan);
  placement bottom-center closeup, ~1/3 frame, shoulders crop; facing camera dead-on while
  the absurdity happens beside him.
- **On-screen text:** the checklist rows (handwritten) as they stamp; no other text.
- **Emotion:** dry comedy - consensus so total even objects agree.
- **Insight / joke:** "even the trophy knows it" made literal with googly eyes.
- **Linkage / eye path:** card rows (left, reading down) -> across to the trophy's googly
  eyes (right) on the third row -> WIT's deadpan (center) as the button.
- **Show-as-you-say:** cut on Economists@19.76 with row 1 stamping immediately; row 2
  stamp (impact) on politicians@21.54; row 3 stamp + googly eyes pop + nod on
  trophy@22.66-knows@22.92; WIT hard-shows at 22.12 (arrives for the punchline).
- **Sound:** three stamp thuds; a tiny squeak-blink for the googly eyes.
- **Color / contrast:** cream card on dark wood; red checks pop; gold trophy warm.
- **WIT density note:** WIT enters only for the third beat - rows carry the first two.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `desk-darkwood-1.jpg` | browse-real-photo | dark wooden desk surface with soft side light, empty, no brands | full-bleed base | new |
| `trophy-gold-parody.png` | reuse | hero trophy + CSS googly eyes overlay (eyes are CSS, not baked in) | right ~25% width | reuse (1.1) |
| `pose deadpan_unimpressed_half_lidded.png` | pose | library signature deadpan closeup | bottom-center, ~1/3 frame, shoulders crop | reuse (library) |

### Scene 1.6 - "Look at it. Shiny. Golden. Beautiful. And behind it, a receipt. A very, very long receipt."

- **Local time:** `23.90-30.70` (Look@23.90, Shiny@25.24, Golden@25.44, Beautiful@25.98, behind@26.96, receipt@28.30, long receipt@29.80)
- **Role:** the glamour fake-out -> the reveal push. Pays off 1.2's tag with physical
  evidence; sets up the question.
- **Composition / layout:** two-phase single scene. Phase A (23.90-26.80): trophy glamour
  hero on a gold-bokeh black background - trophy dead center (38-62% x, 12-88% y), three
  sparkle glints popping on the three adjectives. Phase B (26.88-30.70): the "camera"
  slides right (whole scene translates left ~35%): behind the trophy, the receipt (reused)
  is revealed piled in folds reaching off-frame right (55-100% x, 40-90% y), softly lit.
  WIT peeks in from the LEFT edge (0-20% x) during phase B only.
- **Elements:**
  - *Base (full-bleed):* black background with warm gold bokeh circles, luxury-ad feel
    (~0.75 brightness).
  - *Trophy:* same hero file, warmest grade of the section, strongest specular glint.
  - *Sparkle glints:* three 4-point star glints (CSS/SVG), one per adjective, at different
    spots on the trophy.
  - *Receipt pile:* same `receipt-endless-roll.png` composited into a layered zigzag pile
    (render stacks/rotates the same asset 3-4 times - no new file), plus a handwritten
    arrow label.
- **Mascot:** pose `hand_on_cheek_surprised_curious` (library); placement LEFT edge peek in
  phase B, ~1/3 frame, chest crop, facing right toward the receipt pile; expression:
  curious "ohh."
- **On-screen text:** `the bill` - small red handwritten label + hand-drawn arrow pointing
  at the pile, hard-shows on receipt@28.30; nothing during the glamour phase (let the
  object be beautiful).
- **Emotion:** seduction, then the flip to "oh no, it's still printing."
- **Insight / joke:** luxury-commercial grammar interrupted by paperwork.
- **Linkage / eye path:** phase A locks eyes center on the trophy; phase B drags the eye
  right along the receipt folds; WIT's peek re-anchors left before the cut.
- **Show-as-you-say:** glints pop (small impacts) on Shiny@25.24 / Golden@25.44 /
  Beautiful@25.98; the slide/reveal begins exactly on behind@26.96 (0.6s ease); `the bill`
  label on receipt@28.30; a second receipt fold flops onto the pile (small impact) on the
  second "receipt"@29.80.
- **Sound:** soft luxury "ting" per glint; paper flop on 29.80; printer tick still under.
- **Color / contrast:** black + gold glamour vs flat white paper - the receipt is
  deliberately the least glamorous object in frame.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `gold-bokeh-black-1.jpg` | browse-real-photo | black background with warm gold bokeh light circles, luxury feel, no objects/people | full-bleed base | new |
| `trophy-gold-parody.png` | reuse | hero trophy, warmest grade | center ~28% width (phase A) | reuse (1.1) |
| `receipt-endless-roll.png` | reuse | receipt asset stacked/rotated into a folded pile by render | right half, phase B | reuse (1.3) |
| `pose hand_on_cheek_surprised_curious.png` | pose | library pose, left-edge peek | left edge, ~1/3 frame, chest crop | reuse (library) |

### Scene 1.7 - "So here is today's question: if hosting loses money, why does everyone want to pay?"

- **Local time:** `30.78-35.90` (question@31.76, If@32.58, money@33.48, why@34.38, pay@35.52; clamp scene end to 35.904)
- **Role:** mascot-only focus beat - the channel's "listen to this line" device. Plants the
  question the payoff (S8) answers; hard cut to S2 after.
- **Composition / layout:** near-empty frame: heavy dark vignette over a barely-visible
  dark curtain photo base. WIT GIANT dead center (30-70% x, head ~8% from top, hips
  cropped at bottom edge), the receipt (reused) draped once over his shoulder like a
  scarf - the motif literally follows him. Two stacked handwritten lines appear high-left
  and high-right of his head (both above 60% y line, clear of his face).
- **Elements:**
  - *Base (full-bleed):* dark theater curtain photo, vignetted to ~near-black at edges
    (deliberate quiet after 6 busy scenes - the justified minimal beat).
  - *Receipt drape:* same receipt file, one strip over WIT's left shoulder, subtly
    swaying 1deg.
- **Mascot:** pose `pointing_up_curious_open_mouth` (library - the rhetorical-question
  pose); placement CENTER GIANT, ~1/2+ frame, hips cropped; facing camera; expression:
  one eyebrow up, finger raised - directly challenging the viewer.
- **On-screen text:** line 1 `loses money` (white handwritten, upper-LEFT of WIT's head,
  red strike under it) on money@33.48; line 2 `...so why PAY?` (bigger, warm white, upper-
  RIGHT, `PAY?` underlined) on why@34.38. Both clear of WIT's face and above the subtitle
  zone.
- **Emotion:** curiosity locked in - the viewer now owns the question.
- **Insight / joke:** none - clean thesis beat (rhythm rule: dense scenes, then a clean
  mascot beat to land the point).
- **Linkage / eye path:** WIT's raised finger points up between the two text lines: face ->
  left line -> right line.
- **Show-as-you-say:** cut on "So here"@30.78 (all SFX stop; receipt tick stops mid-tick -
  audible absence); line 1 on money@33.48 (hard-show); line 2 on why@34.38 (impact pop);
  hold to 35.904, hard cut out.
- **Sound:** silence except the voice (first fully quiet beat of the video).
- **Color / contrast:** near-black frame, white WIT, two white text lines - maximum
  contrast, phone-readable.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `curtain-dark-1.jpg` | browse-real-photo | dark theater curtain, heavy folds, very low key, no people | full-bleed base, strong vignette | new |
| `pose pointing_up_curious_open_mouth.png` | pose | library rhetorical-question pose | center giant, ~1/2+ frame, hips crop | reuse (library) |
| `receipt-endless-roll.png` | reuse | one strip draped over WIT's shoulder | over left shoulder | reuse (1.3) |

## Section Asset Summary

| Filename | Type | First scene | Reused in | Notes |
|---|---|---|---|---|
| `trophy-gold-parody.png` | generate | 1.1 | 1.2, 1.3, 1.5, 1.6 (+ later sections) | VIDEO HERO object; parody design, NOT the real FIFA trophy |
| `receipt-endless-roll.png` | generate | 1.3 | 1.6, 1.7 (+ all later sections) | VIDEO MOTIF; text-free so CSS overlays items later |
| `wit-fan-flag-cheer.png` | generate (NEW pose) | 1.1 | S1 thumbnail candidate | nationality-neutral teal fan kit |
| `wit-fan-frozen-mid-cheer.png` | generate (NEW pose) | 1.3 | - | same fan kit, dread face - the money shot |
| `stadium-fireworks-1.jpg` | browse-real-photo | 1.1 | - | no people |
| `podium-spotlight-1.jpg` | browse-real-photo | 1.2 | - | - |
| `world-map-vintage-1.jpg` | browse-real-photo | 1.3 | - | parchment map = "countries" |
| `ledger-red-pen-1.jpg` | browse-real-photo | 1.4 | - | no hands/brands |
| `desk-darkwood-1.jpg` | browse-real-photo | 1.5 | - | - |
| `gold-bokeh-black-1.jpg` | browse-real-photo | 1.6 | - | luxury grammar |
| `curtain-dark-1.jpg` | browse-real-photo | 1.7 | - | near-black focus beat |
| library poses (5) | pose | 1.2/1.4/1.5/1.6/1.7 | - | skeptical_side_eye_doubtful, pondering_skeptical_hand_on_chin, deadpan_unimpressed_half_lidded, hand_on_cheek_surprised_curious, pointing_up_curious_open_mouth |

## Approval Checks

- each scene picturable from text alone: yes - composition %, element details, grades given
- ~one scene per sentence, scene-types varied: yes - 7 scenes / 36s, 7 distinct types, no
  repeated layout in consecutive scenes
- every scene has a real/real-looking base: yes - 7 distinct real photo bases (1.7's
  near-black curtain is the deliberate minimal focus beat)
- mascot big/high with a specific pose+expression per scene: yes - giant left / right peek /
  mid-left frozen / bottom-right / center closeup / left peek / center giant; 2 NEW poses +
  5 distinct library poses, no repeats
- show-as-you-say timeline present per scene: yes - every entrance pinned to a real
  whisper word timestamp; hard-show vs impact marked
- every asset has type + description + filename + layout: yes
- repeated subjects reuse the same filename: yes - trophy x5, receipt x3, fan kit shared
  across the two NEW poses
- public figures handled as caricature/parody, punching up: n/a - no real people; parody
  trophy avoids the copyrighted FIFA sculpture; WIT fan kit is nationality-neutral
- no image-generation prompts written here: correct - descriptions only
- in sync with master `04-visual-plan.md`: yes (written same run)
