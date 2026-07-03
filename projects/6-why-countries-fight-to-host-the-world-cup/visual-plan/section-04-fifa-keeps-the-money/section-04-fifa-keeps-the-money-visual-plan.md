# Section 4 Visual Plan - FIFA Keeps The Money

Video: `Why Countries Fight to Host the World Cup (and Lose Billions)`
Section: `Section 4: FIFA Keeps The Money`
Status: `draft visual plan for approval`

## Video-Level Direction (for context - keep identical to master)

- Audience: `A2-C1 English learners (interesting-English advantage)`
- Renderer: `HyperFrames (composited from pre-made assets)`
- Visual grammar: `real / real-looking base + mascot drawn on top; new scene ~per sentence; vary everything`
- Mascot character: `WIT - round bald head, big rectangular glasses, expressive; big and high (giant on emotional beats), varied side/scale/pose per scene`
- Tone on screen: `savage-but-clean; edge aimed at FIFA / consultants / incentives, never a nation or its fans`
- Recurring motif: `the endless receipt (born in the S1 hook at fight@10.26, returns all video, final close-up in S8); secondary: the white-elephant feeding bowl (S6)`
- Scene-type rotation in use: `wide gag / object hero close-up / evidence board / checklist device / glamour reveal / mascot-only focus / animated interactive UI (S9 outro)`
- Pose library: `.agents/_shared/assets/wit/poses/` (palette; S1 invents 2 NEW fan poses)
- Safety: `parody trophy (NOT the real FIFA trophy sculpture - copyrighted artwork); nationality-neutral fan gear (no real flags); no real people; edge at institutions only`

## Section Overview

- Section goal: read FIFA's contract out loud and make the one-way money flow visible:
  revenue arrows run INTO FIFA, bill arrows run ONTO the host. Land the tax-exemption
  deadpan, the chess-club sign gag, the $7.5B -> $13B money counter, the honest fairness
  beat, and close on the auction image (the winner pays, the auctioneer keeps the money).
- Duration: `62.101s` (audio `section-04-fifa-keeps-the-money` voiceover)
- Timing source: `voiceover/section-04-fifa-keeps-the-money/section-04-word-timings.json`
  (whisper-tiny.en, generated 2026-07-02). One defect: the FINAL THREE tokens "keeps the
  money." jumped backward (53.44-54.82 - a whisper monotonicity error); by position they
  follow `auctioneer@60.86-61.32`, so they are estimated at ~61.32-62.10 and the final
  scene's end is CLAMPED to the real audio duration `62.101s`. All other timestamps are
  monotonic and used as-is. Whisper punctuation quirks ("earth" lowercase, "$4 billion"
  tokenized as `$4` + `billion`) do not affect timing.
- Scene count: `9` (target was ~8; the section's sentence beats at 62.1s cannot merge to
  8 without one base holding ~11s, so the two long money beats split at their natural
  sentence boundaries - every base stays under ~10.1s, a visible change every ~3-10s)
- Scene-type rotation: 4.1 wide signing gag -> 4.2 contract evidence board -> 4.3 red-arrow
  bills board + receipt motif -> 4.4 document close-up + stamp -> 4.5 postcard establishing
  gag -> 4.6 object-hero sign gag -> 4.7 money-counter device board -> 4.8 balance-scale
  mechanism board -> 4.9 wide auction payoff
- Arrow direction language (starts here, stays consistent all video): GREEN arrows =
  money flowing to FIFA, always drawn LEFT-to-RIGHT, always ending at FIFA's gold safe.
  RED arrows = bills flowing to the host, always drawn RIGHT-to-LEFT, always ending at
  WIT / the host side. Green thickens as revenue numbers grow; red never shrinks.
- Mascot arc in this section: carefree mayor signing without reading (pen smoking) ->
  dry smirk at the pattern -> sweating as the bills slide in -> signature deadpan at
  "All of them" -> globe-pointing Zurich gloss -> gold-chain flex as the "rich chess
  club" -> stunned counter-watching -> calm palm-open concession -> the auction winner
  holding the paddle and the bill.

## Scenes

### Scene 4.1 - "Then comes the contract. Before you host, you sign. Let us read it together."

- **Local time:** `0.00-3.98` (Then@0.00, contract@0.82, sign@2.32, read@3.02, together@3.32)
- **Role:** hard pivot from S3's popped promises to paperwork. Introduces the contract
  stack that scenes 4.2-4.4 will "read", and mayor-WIT who signs it blind - the human
  half of the whole section.
- **Composition / layout:** full-bleed real photo base: a long dark-wood boardroom table
  with empty leather chairs, warm window light (bright ~0.75, no scrim). Table surface
  line ~62% y. The fat contract stack (generated, isolated) slams down center-left
  (22-48% x, 34-78% y) with a paper-dust puff. Mayor-WIT sits CENTER behind the table
  (34-68% x, head ~10% from top, torso behind the stack's top edge, legs hidden by the
  table), pen in hand, already signing. A yellow "SIGN HERE" tab sticks out of the
  stack's side. A small handwritten note floats upper-right (66-92% x, 14-26% y).
- **Elements:**
  - *Base (full-bleed):* empty corporate boardroom, long dark table, leather chairs both
    sides, warm daylight from tall windows - no people, no logos, no screens. Sourcing
    note: pick a frame where the table's far edge sits low enough to seat WIT behind it.
  - *Contract stack (center-left, ~26% width):* generated hero - a fat, slightly askew
    stack of white A4 contracts about 15 pages visible on the side, top page blank
    (text-free asset so CSS overlays the title). CSS typed legal-serif cover label
    `GOVERNMENT GUARANTEES` in a thin double-rule box sits on the top page, 2deg tilt.
  - *SIGN HERE tab:* small yellow plastic-flag tab (CSS) poking from the stack's right
    side at ~60% of stack height, red arrow printed on it pointing at the signature line.
  - *Handwritten note (upper-right):* cream sticky note, black handwriting
    `(he did not read it)` with a thin arrow drawn down toward WIT's pen hand.
- **Mascot:** pose `NEW: wit-mayor-signing.png` - WIT wearing a plain teal mayoral sash
  (blank - no insignia, no flag colors), eyes closed in carefree bliss, big content
  smile, one hand pressing a page flat, the other scribbling with a fountain pen whose
  tip trails a thin gray smoke wisp (the pen is literally overheating). Placement
  CENTER behind the table, scale ~2/5 frame (head + glasses + sash fully inside frame,
  lower body hidden by the table edge); facing slightly down-left at the page; expression:
  blissfully unbothered.
- **On-screen text:** `GOVERNMENT GUARANTEES` (typed legal serif, black on the white top
  page, double-rule box, 2deg tilt) lands with the stack on contract@0.82. `SIGN HERE`
  (tiny red print on the yellow tab) flips out on sign@2.32. `(he did not read it)`
  (black handwriting on cream sticky) hard-shows on together@3.32. All text sits above
  the bottom subtitle-safe zone.
- **Emotion:** cheerful doom - the happiest anyone has ever been while losing billions.
- **Insight / joke:** the narrator says "let us read it together" while the only person
  who should read it is signing with his eyes closed.
- **Linkage / eye path:** stack slam (center-left) -> up the SIGN HERE tab to WIT's
  smoking pen (center) -> the sticky note's arrow pointing back down at him (upper-right).
- **Show-as-you-say:** base + WIT visible from 0.00 (already mid-signature, pen scribble
  loop + smoke wisp drifting); contract stack SLAMS in (impact, dust puff, screen nudge
  1%) on contract@0.82 with its cover label; SIGN HERE tab flips out (small impact) on
  sign@2.32; sticky note hard-shows on together@3.32; hold to 3.98, hard cut.
- **Sound:** heavy paper THUD on contract@0.82; continuous faint pen-scratch loop; a tiny
  sizzle under the smoke wisp; page-flip on sign@2.32.
- **Color / contrast:** warm wood browns + white paper; the yellow tab and teal sash are
  the only saturated accents; WIT's white face pops against the dark chairs.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `boardroom-table-1.jpg` | browse-real-photo | long dark-wood boardroom table with empty leather chairs, warm daylight, no people/brands/screens | full-bleed base | new |
| `contract-stack-guarantees.png` | generate | fat slightly-askew stack of white contract pages (~15 visible on the side), top page blank so CSS can title it, isolated, transparent bg | center-left ~26% width, slams onto table | new (returns in 4.4 close-up logic; S7 candidate) |
| `wit-mayor-signing.png` | generate | NEW WIT pose: plain teal mayoral sash (no insignia), eyes-closed blissful smile, one hand flat on a page, other hand signing with a fountain pen trailing a thin smoke wisp | center behind table, ~2/5 frame, lower body hidden by table edge | new (mayor kit; S7 taxpayer-contrast candidate) |

### Scene 4.2 - "FIFA keeps the TV money. FIFA keeps the sponsor money. FIFA keeps the ticket money. Feel free to spot the pattern."

- **Local time:** `4.04-10.14` (FIFA@4.04, TV@4.64, money@4.84, FIFA@5.56, sponsor@6.14,
  money@6.40, FIFA@7.18, ticket@7.92, money@7.92-8.72, Feel@8.72, spot@9.24, pattern@9.68)
- **Role:** the actual "reading" - three identical clauses stamp in like a legal drumbeat,
  and the GREEN ARROW direction language is born on the pattern line.
- **Composition / layout:** full-bleed real photo base: a dark wall of glowing blank TV
  screens (electronics-wall look, ~0.7 brightness, screens plain white-blue glow, no
  logos). A white parody contract page card floats LEFT (6-46% x, 16-78% y, drop shadow,
  1deg tilt) with three clause rows that appear one by one. FIFA's fat gold safe
  (generated) sits upper-RIGHT (68-92% x, 14-44% y) on a glass shelf line. The green
  arrow draws from the card's top-right corner to the safe's door (48-68% x, ~26% y).
  WIT peeks bottom-RIGHT (66-100% x), closeup, under the safe.
- **Elements:**
  - *Base (full-bleed):* wall of switched-on TVs in a dark showroom - rows of bright
    rectangles, all screens blank glow (brand-free, content-free). It literally IS
    "the TV money" wallpaper.
  - *Contract page card (left):* white paper card, typed legal serif, header
    `WHAT FIFA KEEPS` in small caps with a thin rule; three numbered clause rows (text
    below); each row gets a green highlighter swipe across "FIFA keeps"; on the pattern
    beat a red marker circles the three "FIFA"s and links them with one shaky red line.
  - *Gold safe (upper-right, ~22% width):* generated hero - a fat, gleaming gold safe
    with slightly bulging sides (visibly overstuffed), round black dial, door seam
    bowing outward; one white specular glint.
  - *Green arrow:* CSS/SVG arrow, ~12px thick (its THINNEST state all video - it will
    grow in 4.7), drawing left-to-right from the card to the safe door; small label
    riding on it (text below).
  - *Cash bundles:* three generated banknote bundles (generic green paper bands, no real
    currency faces) that launch from the card and fly along the arrow into the safe,
    one per "money." beat; the safe jiggles 1deg on each hit.
- **Mascot:** pose `unimpressed_smirk_closeup` (library); placement bottom-RIGHT closeup
  peek, ~1/3 frame, cropped at the chest (head + glasses fully inside frame); facing
  left toward the clause card; expression: dry half-lidded "of course it does."
- **On-screen text:** clause rows (typed, black): `1. FIFA keeps the TV money.` on
  FIFA@4.04, `2. FIFA keeps the sponsor money.` on FIFA@5.56, `3. FIFA keeps the ticket
  money.` on FIFA@7.18; green highlighter swipes across "FIFA keeps" on TV@4.64 /
  sponsor@6.14 / ticket@7.92; arrow label `MONEY -> FIFA` (green handwritten, riding the
  arrow) on pattern@9.68; red handwritten `spot the pattern` with the circling marker on
  spot@9.24. All rows sit above the subtitle-safe zone.
- **Emotion:** dry legal comedy - the same sentence three times IS the joke.
- **Insight / joke:** the contract has one clause wearing three hats; the highlighter
  does the "spotting" before the narrator finishes offering.
- **Linkage / eye path:** clause rows (left, reading down like a real contract) -> red
  circles link the three FIFAs -> up the green arrow -> into the safe (upper-right) ->
  down to WIT's smirk (bottom-right).
- **Show-as-you-say:** cut on FIFA@4.04 with the card + row 1 hard-showing together;
  highlighter swipe 1 on TV@4.64; bundle 1 flies into the safe as "money."@4.84 lands
  (safe jiggle); row 2 hard-shows on FIFA@5.56, swipe 2 on sponsor@6.14, bundle 2 on
  money@6.40; row 3 on FIFA@7.18, swipe 3 on ticket@7.92, bundle 3 launches as
  "money."@7.92 finishes (lands by ~8.4); red marker circles + `spot the pattern` scribble
  on spot@9.24; green arrow draws + `MONEY -> FIFA` label (impact) on pattern@9.68; WIT
  visible from the cut, one slow blink on Feel@8.72.
- **Sound:** typewriter clack per clause row; highlighter squeak per swipe; three soft
  cash whooshes + a muffled clink inside the safe per bundle; marker scribble on 9.24.
- **Color / contrast:** cool blue-white TV glow vs warm gold safe; green highlighter and
  green arrow own the "money" color from here on; the red marker is the only red.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `tv-wall-glow-1.jpg` | browse-real-photo | dark wall of switched-on TV screens, blank white-blue glow, no logos/content/people | full-bleed base | new |
| `gold-safe-fat.png` | generate | fat gleaming gold safe with slightly bulging sides and bowing door seam (overstuffed), round black dial, isolated, transparent bg | upper-right ~22% width | new (SECTION HERO - reused 4.5, 4.7; shared-asset candidate for S5/S8) |
| `cash-bundle-generic.png` | generate | single banknote bundle, generic green bills with a plain paper band, NO real currency faces/marks, isolated, transparent bg | flies along the green arrow, ~7% width | new (reused 4.7, 4.9) |
| `pose unimpressed_smirk_closeup.png` | pose | library dry-smirk closeup | bottom-right, ~1/3 frame, chest crop | reuse (library) |

### Scene 4.3 - "The host pays for the stadiums. The security. The transport. The fan zones."

- **Local time:** `10.14-14.58` (host@10.30, pays@10.54, stadiums@11.16, security@12.04,
  transport@12.88, fan@13.78, zones@14.02)
- **Role:** the mirror image of 4.2 - the RED arrow is born, running the opposite way,
  and the receipt motif returns to print this section's required line.
- **Composition / layout:** full-bleed real photo base: a stadium under construction -
  concrete bowl skeleton, two tower cranes against a dusk-orange sky (bright ~0.7, no
  workers, no branded hoardings). Horizon ~58%. The red arrow draws from upper-RIGHT
  (88% x, 18% y) down-left to WIT at lower-LEFT, ~16px thick. Four paper bill chips
  slide down the arrow one per beat and pile beside WIT (18-40% x, 46-66% y). The
  receipt (REUSED file) curls out from under the chip pile toward center-bottom
  (30-58% x, 62-78% y) and prints its line. WIT giant LEFT (0-36% x, head ~12% from
  top, knees cropped).
- **Elements:**
  - *Base (full-bleed):* stadium construction site at dusk - raw concrete tiers, crane
    silhouettes, warm sky. Sourcing note: no readable contractor logos on cranes or
    fencing; crop or pick accordingly.
  - *Red arrow:* CSS/SVG, drawing RIGHT-to-LEFT (bills flow onto the host - opposite
    direction to 4.2's green, same visual grammar); label riding on it (text below).
  - *Bill chips (4):* white invoice-style paper chips with a red top stripe, typed
    labels (text below), each sliding down the arrow with a slight tumble and landing
    with a paper slap, stacking into a messy pile at WIT's side.
  - *Receipt:* same `receipt-endless-roll.png` strip, unrolling ~26% of frame width from
    under the chip pile; CSS mono-font line prints onto it character-by-character.
- **Mascot:** pose `shocked_sweating_dismayed` (library); placement LEFT giant, ~1/2
  frame (emotional beat), knees cropped, head high; facing right at the incoming arrow;
  expression: wide eyes, square open mouth, sweat drop - the mayor's bliss from 4.1 is
  gone.
- **On-screen text:** arrow label `BILLS -> HOST` (red handwritten, riding the red arrow)
  on pays@10.54; chip labels (typed): `STADIUMS` on stadiums@11.16, `SECURITY` on
  security@12.04, `TRANSPORT` on transport@12.88, `FAN ZONES` on fan@13.78; receipt
  line (mono print, dark gray): `16x STADIUM (RETROFIT) ......... $???` printing from
  stadiums@11.16 and finishing by zones@14.02. Receipt text sits at ~62-70% y - above
  the subtitle-safe zone.
- **Emotion:** dawning horror - the other half of the contract arrives physically.
- **Insight / joke:** FIFA's clauses were nouns it KEEPS; the host's clauses are nouns
  it PAYS - and the price on the biggest item is literally unknown (`$???`).
- **Linkage / eye path:** red arrow enters from FIFA's corner (upper-right, where the
  safe sat in 4.2 - spatial callback) -> chips slide down it -> pile at WIT's feet ->
  receipt curling out below with the running total that has no total.
- **Show-as-you-say:** cut on "The host"@10.14 with base + WIT + the arrow already
  drawing; `BILLS -> HOST` label (impact) on pays@10.54; chip 1 + receipt printer STARTS
  (tick SFX) on stadiums@11.16; chip 2 (impact) on security@12.04; chip 3 on
  transport@12.88; chip 4 on fan@13.78, settling by zones@14.02; WIT's sweat drop
  slides on zones@14.02; hard cut at 14.58.
- **Sound:** low whoosh for the red arrow; four paper slaps (rising pitch as the pile
  grows); the signature receipt printer tick-tick from 11.16; distant construction
  clank once under 13s.
- **Color / contrast:** dusk orange + raw concrete gray; the red arrow and red chip
  stripes own "bills"; the white receipt pops at the bottom; WIT's white face is the
  brightest emotional point.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `stadium-construction-crane-1.jpg` | browse-real-photo | stadium concrete bowl under construction with tower cranes at dusk, no workers, no contractor logos | full-bleed base | new |
| `receipt-endless-roll.png` | reuse | the video's receipt motif; CSS prints the STADIUM (RETROFIT) line onto it | curls from chip pile, ~26% width, 62-78% y | reuse (S1 motif) |
| `pose shocked_sweating_dismayed.png` | pose | library dismay pose, giant | left, ~1/2 frame, knees crop | reuse (library) |

### Scene 4.4 - "Oh, and guarantee number three: your government promises FIFA an exemption from taxes - meaning FIFA pays none. Not some taxes. All of them."

- **Local time:** `14.58-23.20` (Oh@14.58, guarantee@15.00, three@15.64, government@16.38,
  promises@16.72, exemption@17.92, taxes@18.40, meaning@19.40, none@20.28, some@21.10,
  taxes@21.32, All@22.08, them@22.56)
- **Role:** the section's verified centerpiece clause, read straight off the page - the
  highlight + stamp treatment makes the legal line feel physical. WIT's signature
  deadpan lands the [deadpan] voice direction.
- **Composition / layout:** full-bleed real photo base: a big wooden-handled rubber stamp
  resting on a red ink pad on a bright desk, shot at a low angle (bright ~0.8) - the
  scene's own device echoed in the base. A wide contract close-up strip (paper texture,
  CSS type) spans the top (8-92% x, 14-40% y, 1deg tilt, drop shadow). Three small paper
  tax tags hang in a row mid-frame (14-52% x, 46-58% y). A giant red grunge stamp mark
  lands over the strip's right end (60-88% x, 20-44% y). WIT giant CENTER-RIGHT
  (48-92% x, head ~14% from top, shoulders crop), face clear of all text.
- **Elements:**
  - *Base (full-bleed):* wooden rubber stamp + red ink pad on a bright desk, shallow
    depth of field, nothing branded. Sourcing note: generic stamp face - no readable
    words on the rubber.
  - *Contract strip (top):* cream paper band styled like a magnified contract line;
    small-caps header `GOVERNMENT GUARANTEE No. 3` left-aligned; body line in legal
    serif: `...a full exemption from ALL taxes...`; a yellow highlighter swipe crosses
    the body line; a red hand-drawn circle wraps `No. 3`.
  - *Tax tags (3):* small manila luggage-style tags, each typed `TAX`, hanging on short
    strings from the strip's bottom edge; one red X sweep slashes all three at once on
    the payoff word.
  - *Red stamp mark:* big grunge-edged rounded rectangle, semi-transparent red ink:
    `PAYS: $0` - it slams ONTO the contract strip (scoped to this contract, matching the
    narration's in-line gloss).
- **Mascot:** pose `deadpan_unimpressed_half_lidded` (library - the signature deadpan);
  placement CENTER-RIGHT giant, ~1/2 frame, shoulders crop, head high; facing camera
  dead-on; expression: half-lidded, flat mouth - the [deadpan] beat made visible.
- **On-screen text:** `GOVERNMENT GUARANTEE No. 3` (typed small caps) hard-shows with
  the strip on guarantee@15.00; red circle around `No. 3` on three@15.64; body line
  `...a full exemption from ALL taxes...` types on promises@16.72 with the yellow
  highlighter swiping left-to-right on exemption@17.92; red grunge stamp `PAYS: $0`
  slams (impact) on none@20.28; the three `TAX` tags hard-show on some@21.10 and take
  one red X sweep (impact) on All@22.08; red handwritten `ALL of them.` pops beside
  WIT's head - upper-left of his face, never covering it - on them@22.56.
- **Emotion:** disbelief flattening into deadpan - the joke is how calmly it is said.
- **Insight / joke:** a government "promise" that promises to collect nothing; the base
  photo is a stamp because the whole clause is one rubber-stamp away from law.
- **Linkage / eye path:** header (top-left) -> highlighter swipe along the clause ->
  stamp slam at its right end -> down the hanging TAX tags as they are crossed -> WIT's
  unmoved face beside them.
- **Show-as-you-say:** cut on Oh@14.58 (base + WIT already present, strip empty paper);
  header on guarantee@15.00; red circle on three@15.64; clause types from promises@16.72;
  highlighter swipe (squeak) on exemption@17.92; `PAYS: $0` stamp (impact, 1% frame
  shake) on none@20.28; TAX tags on some@21.10; red X sweep (impact) on All@22.08;
  `ALL of them.` pop on them@22.56; hold to 23.20.
- **Sound:** typewriter clacks; highlighter squeak; one massive stamp THUD on 20.28
  (deepest hit of the section so far); a lighter triple-thud as the X crosses the tags
  on 22.08; silence under WIT's deadpan.
- **Color / contrast:** bright desk neutrals + cream paper; yellow highlight vs red
  stamp ink - red is reserved for the exemption payoff; WIT stays black-and-white calm
  in a scene full of alarm colors.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `rubber-stamp-ink-1.jpg` | browse-real-photo | wooden rubber stamp on a red ink pad, bright desk, shallow focus, no readable stamp face, no brands | full-bleed base | new |
| `pose deadpan_unimpressed_half_lidded.png` | pose | library signature deadpan, giant | center-right, ~1/2 frame, shoulders crop | reuse (library; also used S1.5 - consistent callback face) |

### Scene 4.5 - "By the way, FIFA lives in Zurich, Switzerland. And legally, FIFA is a non-profit."

- **Local time:** `23.20-27.76` (by@23.20, way@23.44, lives@23.90, Zurich@24.50,
  Switzerland@25.16, legally@25.76, non-profit@26.80-27.76)
- **Role:** the geography gloss the script planted for B1 learners (S5's "mostly toward
  Zurich" punchline depends on it), played as a picture postcard - plus the "non-profit"
  label that sets up the chess-club gag next scene.
- **Composition / layout:** full-bleed real photo base: a bright alpine lake with snowy
  peaks and a small lakeside town (postcard-pretty, ~0.85 brightness). A white postcard
  border frames the whole scene (CSS inset frame, ~2% thick) with a typed caption strip
  bottom-left (8-40% x, 74-80% y - above the subtitle zone). The gold safe (REUSED)
  sits small on the lakeshore lawn (58-72% x, 52-68% y) with a tiny drawn chimney puff
  and a doormat - it "lives" here. A blue ribbon rosette badge stamps upper-right
  (70-90% x, 12-30% y). WIT LEFT (2-40% x, ~2/5 frame, hips crop).
- **Elements:**
  - *Base (full-bleed):* generic alpine lake + mountains + lakeside rooftops - bright,
    calendar-photo feel. Sourcing note: generic Swiss-look scenery, NO identifiable
    landmark, NO flags, no readable signage, people-free (or people too distant to
    identify - prefer none).
  - *Postcard frame + caption:* clean white border all around; typed postcard-serif
    caption on a white strip: `Zurich, Switzerland` with a small drawn stamp corner
    upper-right of the frame (plain, no country marks).
  - *Gold safe (small, ~14% width):* same overstuffed safe from 4.2, now domesticated:
    a CSS doormat rectangle in front (`HOME` in tiny type) and a hand-drawn arrow tag.
  - *Rosette badge:* blue prize-ribbon rosette (SVG, award-style) with white text ring.
- **Mascot:** pose `pointing_at_globe_explaining` (library - the macro/geography pose);
  placement LEFT, ~2/5 frame, hips crop; facing right, pointing toward the safe on the
  lakeshore; expression: neutral teacher "o" mouth.
- **On-screen text:** postcard caption `Zurich, Switzerland` (typed postcard serif,
  bottom-left strip) on Zurich@24.50; handwritten tag `FIFA lives here` with a short
  arrow to the safe on lives@23.90; rosette badge text `NON-PROFIT` (white on blue
  ribbon, official award styling) stamps on non-profit@26.80.
- **Emotion:** sweet travel-brochure calm - deliberately too pleasant, so the absurdity
  ("a non-profit with a safe") reads as dry.
- **Insight / joke:** the world's richest sports body "lives" in a postcard, and its
  legal costume is an award ribbon that says NON-PROFIT while its house is a safe.
- **Linkage / eye path:** WIT's pointing finger (left) -> the safe with its doormat
  (center-right) -> up to the NON-PROFIT rosette (upper-right) -> caption strip anchors
  the geography (bottom-left).
- **Show-as-you-say:** cut on "by the way"@23.20 - postcard frame + base + WIT hard-show
  together (the frame makes the cut feel like a slide change); `FIFA lives here` tag on
  lives@23.90; caption `Zurich, Switzerland` types on Zurich@24.50, finishing on
  Switzerland@25.16; rosette badge stamps (impact, small ribbon flutter) on
  non-profit@26.80; hold to 27.76.
- **Sound:** one soft slide-projector click on the cut; a gentle "ding" with the rosette;
  faint alpine breeze under the beat.
- **Color / contrast:** bright blue lake + white peaks; gold safe is the warm anomaly in
  a cool scene; blue rosette reads official; no red anywhere (calm before the gag).

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `alpine-lake-town-1.jpg` | browse-real-photo | bright alpine lake, snowy peaks, small lakeside town; generic (no landmarks), no flags, people-free | full-bleed base | new |
| `gold-safe-fat.png` | reuse | the overstuffed gold safe, now small on the lakeshore with a CSS doormat | center-right ~14% width | reuse (4.2) |
| `pose pointing_at_globe_explaining.png` | pose | library geography/pointing pose | left, ~2/5 frame, hips crop | reuse (library) |

### Scene 4.6 - "It sits in the same legal category as a local chess club. A chess club with around four billion dollars in reserves."

- **Local time:** `27.76-34.18` (sits@27.76, category@28.82, chess@30.04, club@30.38,
  chess(2)@31.18, club(2)@31.46, around@31.82, $4@32.12, billion@32.40, reserves@33.22,
  scene ends 34.18)
- **Role:** the script's required sign gag, built progressively on its exact words - the
  section's biggest laugh and the "non-profit" payoff.
- **Composition / layout:** full-bleed real photo base: a wooden chessboard close-up with
  carved pieces, shallow depth, warm window light (~0.8). Board surface fills the lower
  half; blurred pieces rise mid-frame. The blank wooden hanging sign (generated) swings
  in top-CENTER-LEFT on two ropes (20-58% x, 10-46% y). A mini stack of gold bars
  (generated single bar, render stacks 4 copies brick-style) materializes on the board
  among the pawns (56-74% x, 54-72% y). WIT RIGHT (60-100% x, ~1/2 frame, hips crop).
- **Elements:**
  - *Base (full-bleed):* wooden chessboard with pieces mid-game, warm tones, shallow
    focus, no hands, no branding.
  - *Hanging sign:* generated blank wooden signboard with rounded corners and two ropes
    from the top edge (text-free asset - all writing is CSS so it can build in steps);
    it swings 2deg after entering.
  - *Sign writing (CSS, in three steps):* white hand-painted letters `CHESS CLUB`; then
    a fat red cross-out stroke through it with `FIFA` scrawled in red above; then a
    smaller white handwritten line beneath: `$4B IN RESERVES`.
  - *Gold bar stack:* one generated gold bar, composited 4x into a small brick pile;
    each bar has a plain rectangular stamp shape (no text) and one glint.
- **Mascot:** pose `rich_flex_gold_chain_sunglasses` (library - the flex caricature);
  placement RIGHT, ~1/2 frame giant (emotional/gag beat), hips crop, head high; facing
  camera; expression: sunglasses, gold chain, smug - WIT as the "local chess club
  member" who is suspiciously rich.
- **On-screen text:** on the sign only (one clean device): `CHESS CLUB` (white
  hand-painted) writes on chess@30.04-club@30.38; red cross-out stroke + red scrawled
  `FIFA` above (impact) on chess(2)@31.18; `$4B IN RESERVES` (white handwritten, smaller)
  writes beneath on reserves@33.22. Nothing else - the sign carries the whole beat.
- **Emotion:** the laugh beat - legal absurdity made of wood and paint.
- **Insight / joke:** the sign is edited live exactly as the sentence corrects itself:
  category -> club -> the four-billion-dollar footnote; the gold bars sitting among
  pawns say the rest.
- **Linkage / eye path:** sign (top-left) -> cross-out drags the eye to the red FIFA ->
  down the ropes to the gold bars among the pawns (center) -> WIT's gold chain (right)
  rhymes with the bars.
- **Show-as-you-say:** cut on sits@27.76 - base + WIT + empty sign swinging in (rope
  creak); `CHESS CLUB` paints on chess@30.04; cross-out + `FIFA` slam (impact, sign
  kicks 3deg) on chess(2)@31.18; gold bars pile up bar-by-bar (4 quick plinks) from
  $4@32.12 to billion@32.40; `$4B IN RESERVES` writes on reserves@33.22; sign settles;
  hold to 34.18.
- **Sound:** rope creak on entry; brush-stroke swish for the painting; a blunt marker
  squeak for the cross-out; four rising coin plinks for the bars; WIT's chain gives one
  tiny jingle on 33.22.
- **Color / contrast:** warm browns of board and sign; white paint text; the red
  cross-out is the scene's only red; gold bars + gold chain glow as the punchline color.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `chessboard-closeup-1.jpg` | browse-real-photo | wooden chessboard with carved pieces mid-game, warm light, shallow focus, no hands/brands | full-bleed base | new |
| `wood-sign-hanging-blank.png` | generate | blank wooden hanging signboard on two ropes, rounded corners, rustic grain, text-free so CSS writes on it in steps, isolated, transparent bg | top-center-left, ~38% width, swings 2deg | new |
| `gold-bar-single.png` | generate | single gleaming gold bar with plain rectangular stamp shape (no text), isolated, transparent bg - render stacks copies | on the board, 4-copy brick pile ~18% width | new (reused 4.8 concept-free; S8 candidate) |
| `pose rich_flex_gold_chain_sunglasses.png` | pose | library flex pose - WIT as the rich club member | right, ~1/2 frame, hips crop | reuse (library) |

### Scene 4.7 - "The four years around the Qatar World Cup brought FIFA about seven and a half billion dollars in revenue. For the four years around this one, FIFA expects around thirteen billion."

- **Local time:** `34.18-43.54` (four@34.34, Qatar@35.42, Cup@36.00, brought@36.34,
  FIFA@36.86, $7@37.56, .5@37.82, billion@38.20, revenue@39.12, for@39.46, four(2)@39.98,
  this@40.72, one@41.00, expects@41.76, around@42.18, $13@42.56, billion.@43.04, scene
  ends 43.54)
- **Role:** the numbers beat - the money counter device the whole section was built
  around: the counter ticks $7.5B then re-ticks to $13B, the green arrow visibly
  thickens, and every number wears the label the narration gives it (revenue / expects).
- **Composition / layout:** full-bleed real photo base: a massive round steel bank vault
  door, slightly ajar, brushed metal, cool light (~0.7, still readable). The LED money
  counter panel floats top-CENTER (26-74% x, 10-30% y): black panel, green digital
  digits, a label plate beneath the digits. The green arrow - now returning from 4.2,
  twice as thick (~28px) - pumps left-to-right across mid-frame (8-64% x, ~46% y) into
  the gold safe (REUSED) sitting in the vault doorway RIGHT (66-90% x, 36-66% y). Cash
  bundles (REUSED) flow along the arrow in a steady stream. WIT LEFT (0-32% x, ~1/3
  frame, chest crop).
- **Elements:**
  - *Base (full-bleed):* huge circular vault door with spoke handle, ajar into darkness,
    cool steel tones - "where the money actually goes" as architecture.
  - *LED counter panel:* black rounded panel with green 7-segment digits, ticking in
    abbreviated phone-readable format (`$0.0B` -> `$7.5B`, later `$7.5B` -> `$13B`); a
    metal label plate below the digits swaps its engraved text on the honest word; a
    small typed sub-chip under the plate names the period.
  - *Green arrow (thickened, step 2 of 3):* same grammar as 4.2 but ~2x thicker; it
    visibly WIDENS once during the scene (see timing); bundles ride it every ~0.5s.
  - *Gold safe:* same overstuffed safe, door now cracked open with green glow inside,
    wedged in the vault doorway - a safe inside a vault (hoarding squared).
- **Mascot:** pose `mildly_surprised_hand_at_chin` (library); placement LEFT, ~1/3 frame,
  chest crop; facing right, watching the counter; expression: small "o" mouth, hand at
  chin - impressed against his will.
- **On-screen text:** label plate `REVENUE` (engraved metal type) hard-shows with the
  panel on brought@36.34; sub-chip `the four years around the QATAR World Cup` (typed,
  small) on Qatar@35.42; digits tick `$0.0B -> $7.5B` from $7@37.56, settling exactly on
  revenue@39.12; sub-chip swaps to `the four years around THIS one` on this@40.72; label
  plate flips `REVENUE -> EXPECTS` (mechanical flap) on expects@41.76; digits re-tick
  `$7.5B -> $13B` from $13@42.56, settling on billion.@43.04. All text top half, clear
  of the subtitle zone.
- **Emotion:** scale-shock delivered by machine - no jokes, just the meter running.
- **Insight / joke:** the honesty IS the device: the plate physically flips from
  REVENUE to EXPECTS because the narration changes verbs - the counter never claims
  more than the sentence does.
- **Linkage / eye path:** WIT's gaze (left) -> counter digits (top-center) -> down to
  the arrow stream -> into the glowing safe in the vault door (right) - money entering
  storage that is already inside storage.
- **Show-as-you-say:** cut on "The four years"@34.18 with base + WIT + thin arrow +
  bundle stream already flowing; sub-chip on Qatar@35.42; counter panel + `REVENUE`
  plate hard-show on brought@36.34; digits tick from $7@37.56 (rapid register ticks),
  settle on revenue@39.12 as the arrow WIDENS step one (soft deep whoosh); sub-chip
  swap on this@40.72; plate flips to `EXPECTS` on expects@41.76; digits re-tick from
  $13@42.56, settle on billion.@43.04 as the arrow widens again (step two) and the
  bundle stream doubles; hold to 43.54, hard cut.
- **Sound:** rapid cash-register tick during both counts; two deep whooshes as the arrow
  widens; muffled clink-clink inside the safe under the stream; low vault-room hum.
- **Color / contrast:** cold steel blue-gray everywhere; the green digits, green arrow,
  and green safe-glow are the only saturated color - money owns the frame's color.
- **WIT density note:** WIT holds one pose all scene - the counter, plate flip, and
  arrow carry all four beats (rhythm rule: device scene, mascot as witness).

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `vault-door-1.jpg` | browse-real-photo | massive round steel bank vault door, slightly ajar, cool brushed metal, no people/bank brands | full-bleed base | new |
| `gold-safe-fat.png` | reuse | the overstuffed safe, door cracked, green glow inside (glow is CSS) | right, in vault doorway, ~20% width | reuse (4.2, 4.5) |
| `cash-bundle-generic.png` | reuse | bundle stream riding the green arrow, ~6% width each | along arrow, every ~0.5s | reuse (4.2) |
| `pose mildly_surprised_hand_at_chin.png` | pose | library impressed-against-his-will pose | left, ~1/3 frame, chest crop | reuse (library) |

### Scene 4.8 - "On track for its biggest payday ever. To be fair, FIFA does pay for some things. Prize money. Running the tournament. What it does not pay for is your police, your trains, and your stadium."

- **Local time:** `43.62-53.70` (On@43.62, track@43.78, biggest@44.44, payday@44.82,
  ever@45.14, fair@46.16, does@46.66, pay@46.94, things@47.58, prize@48.46, money@48.76,
  running@49.08, tournament@49.38, not@50.32, pay(2)@50.56, police@51.62, trains@52.18,
  stadium@52.94, scene ends 53.70)
- **Role:** the payday climax hands straight into the script's required fairness beat -
  a balance scale shows FIFA really does pay some things, and the asymmetry stays
  visible without claiming a zero.
- **Composition / layout:** full-bleed real photo base: an antique brass balance scale
  on a wooden desk, warm side light (~0.75). The real scale sits center (34-66% x,
  26-78% y); CSS pan overlays sit on both pans so items can land. A gold foil banner
  unfurls across the top (14-86% x, 6-16% y). LEFT pan (36-48% x): one fat gold money
  sack (generated) slams it down. RIGHT pan (52-64% x): small green chips land gently.
  Below the right pan, a small cardboard tray sits on the desk (58-78% x, 66-78% y).
  WIT RIGHT (64-100% x, ~2/5 frame, torso crop at desk line).
- **Elements:**
  - *Base (full-bleed):* brass two-pan balance scale, warm wood desk, plain backdrop, no
    brands. Sourcing note: pick a frame with both pans clearly visible and roughly level
    so the CSS tilt reads.
  - *Gold banner:* foil-textured ribbon banner, dovetail ends, engraved-style text
    (below); one shimmer sweep on entry.
  - *Money sack:* generated fat canvas sack, gold-tinted, tied neck, plain `$` symbol
    embossed (generic currency symbol, no real currency design); lands with weight -
    left pan slams down ~14deg and the whole scale beam tilts (CSS transform on the
    overlay pans; base photo static, the drawn beam-line overlay sells the tilt).
  - *Green chips (2):* small mint-green rounded chips, typed labels; they land on the
    right pan which barely dips (~2deg) - the comic physics of the fairness beat.
  - *Red tags (3):* invoice-red tags, typed labels, each with a thin cross-mark; each
    one BOUNCES off the right pan (boing) and drops into the cardboard tray below.
  - *Tray:* plain cardboard tray, handwritten side label (below).
- **Mascot:** pose `eyes_closed_talking_open_palm` (library - calm matter-of-fact
  concession); placement RIGHT, ~2/5 frame, torso crop; facing left toward the scale,
  open palm presenting it; expression: eyes closed, even-handed "to be fair" energy.
- **On-screen text:** banner `BIGGEST PAYDAY EVER` (engraved gold serif) unfurls on
  payday@44.82; handwritten cream aside `to be fair...` (small, upper-left, 8-24% x,
  20-26% y) on fair@46.16; pan plate `FIFA DOES PAY:` (small typed plate above right
  pan) on does@46.66; green chips `PRIZE MONEY` on prize@48.46 and `RUNNING THE
  TOURNAMENT` on running@49.08; red tags `YOUR POLICE` on police@51.62, `YOUR TRAINS` on
  trains@52.18, `YOUR STADIUM` on stadium@52.94; tray label `HOST PAYS THESE`
  (handwritten, on the tray's front face) hard-shows as the first tag lands in it
  (~51.9). All cue text above the subtitle-safe zone except the tray label, which is
  decorative-supporting and sits at ~74% y.
- **Emotion:** gloat, then a breath of honesty - the scale keeps both true at once.
- **Insight / joke:** FIFA's side of the scale is one sack that outweighs everything;
  the three "not pay" tags do not even get to STAY on the scale - they bounce to the
  host's tray. Asymmetry, not a zero.
- **Linkage / eye path:** banner (top) -> sack slamming the left pan -> across the beam
  to the small green chips (right pan) -> the red tags bouncing off into the tray below
  -> WIT's open palm presenting the whole physics lesson.
- **Show-as-you-say:** cut on On@43.62 (base + WIT + level scale); banner unfurls
  (impact, shimmer) on payday@44.82; money sack drops (impact - heavy clunk, left pan
  slams, beam tilts) on ever@45.14; `to be fair...` aside on fair@46.16; `FIFA DOES
  PAY:` plate on does@46.66; chip 1 (soft tink, right pan dips 2deg) on prize@48.46;
  chip 2 on running@49.08; tag 1 bounces off + lands in tray on police@51.62; tag 2 on
  trains@52.18; tag 3 (impact - the section's last red hit) on stadium@52.94; hold to
  53.70, hard cut.
- **Sound:** banner shimmer ting; one heavy sack CLUNK + scale creak on 45.14; two tiny
  chip tinks; three cartoon boings falling in pitch as tags bounce out; paper flop per
  tray landing.
- **Color / contrast:** warm brass + wood; gold sack and gold banner = FIFA's side;
  mint-green chips small and polite; the red tags are the loudest color and they end up
  OFF the scale - the color story tells the asymmetry.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `balance-scale-brass-1.jpg` | browse-real-photo | antique brass two-pan balance scale on wooden desk, warm light, both pans visible and level, no brands | full-bleed base | new |
| `money-sack-gold.png` | generate | fat tied canvas money sack, gold-tinted, plain embossed `$` symbol (generic, no real currency design), isolated, transparent bg | left pan, ~16% width | new |
| `pose eyes_closed_talking_open_palm.png` | pose | library calm concession pose | right, ~2/5 frame, torso crop | reuse (library) |

### Scene 4.9 - "So one side gets the revenue. The other side gets the bills. FIFA invented the only auction on Earth where the winner pays... and the auctioneer keeps the money."

- **Local time:** `53.70-62.101` (So@53.70, side@54.10, revenue@54.82, other@55.48,
  bills@56.44, FIFA@57.22, invented@57.34, auction@58.30, earth@58.86, winner@59.82,
  pays@59.84, auctioneer@60.86-61.32; "keeps the money." estimated ~61.32-62.10 - the
  JSON's final three tokens regressed (whisper error), so they are pinned by position
  after auctioneer@61.32; scene end CLAMPED to 62.101)
- **Role:** section payoff - the two arrows get their one-line recap, then the whole
  contract becomes one picture: an auction where winning costs you and the man with the
  gavel pockets the room.
- **Composition / layout:** full-bleed real photo base: a wooden auctioneer's gavel on
  its sound block, warm spotlight, dark blurred room behind (~0.7, readable). The
  auctioneer (generated faceless suit, behind a wooden podium) stands RIGHT (62-94% x,
  22-84% y); the parody trophy (REUSED) sits on the podium top as the lot (70-84% x,
  14-34% y); a cash pile (REUSED bundle, stacked 5 copies) sits swept-together at the
  podium's base (64-88% x, 66-80% y). WIT the winning bidder stands LEFT-of-center
  (18-52% x, ~2/5 frame, knees crop), paddle raised. Two small recap arrows cross the
  top band (green: 12-44% x at ~12% y pointing right; red: 56-88% x at ~20% y pointing
  left). Payoff text lands mid-left and mid-right (see below), clear of both faces.
- **Elements:**
  - *Base (full-bleed):* wooden gavel on sound block under a warm spotlight, auction-room
    dark behind, no people, no house branding.
  - *Auctioneer (generated, ~30% width):* generic FACELESS suited figure - smooth blank
    head (no features at all - reads as "the institution", not a person), dark suit,
    standing behind a wooden auction podium; one arm mid-sweep, pulling banknotes toward
    itself with a wide wooden money-rake.
  - *Trophy:* same `trophy-gold-parody.png`, small, on the podium top with a paper lot
    tag hanging off it (typed `LOT No. 1: HOSTING RIGHTS`).
  - *Cash pile:* `cash-bundle-generic.png` composited 5x into a swept heap at the
    podium's base (render stacks/rotates the same asset - no new file).
  - *Recap arrows:* the section's two arrows, mini versions, same grammar: green
    left-to-right toward the auctioneer, red right-to-left toward WIT; each carries its
    one-word label.
- **Mascot:** pose `NEW: wit-auction-winner-paddle.png` - WIT holding a blank white
  bidding paddle high in one hand, the other arm cradling an absurdly long folded paper
  bill spilling over his forearm; proud chest, but wide worried eyes and one sweat drop -
  a winner realizing what winning means. Placement LEFT-of-center, ~2/5 frame, knees
  crop, head high; facing camera; expression: proud-and-terrified at once.
- **On-screen text:** green arrow label `REVENUE` (green handwritten, riding the green
  arrow) on revenue@54.82; red arrow label `BILLS` (red handwritten, riding the red
  arrow) on bills@56.44; lot tag `LOT No. 1: HOSTING RIGHTS` (typed auction-catalog
  card, on the trophy's tag) hard-shows on auction@58.30; payoff line 1 `the WINNER
  pays` (white handwritten, mid-left at 16-44% x, 28-36% y, above WIT's paddle, never
  on his face) on pays@59.84; payoff line 2 `the AUCTIONEER keeps the money` (warm
  white handwritten, mid-right at 56-92% x, 36-44% y, above the cash pile, clear of the
  podium) at ~61.40 (estimated - see Local time note). Both payoff lines above the
  subtitle-safe zone.
- **Emotion:** the trap closes with a smile - dry, final, quotable.
- **Insight / joke:** an auction is the one place "winner pays" sounds normal - until
  you notice the auctioneer is also the seller, the tax office, and the bank.
- **Linkage / eye path:** green arrow (top-left) flows right into the auctioneer's rake;
  red arrow (top-right) flows left onto WIT's bill-loaded arm; then the diagonal: WIT's
  raised paddle (left) -> gavel base (center) -> trophy lot on the podium -> the cash
  heap being raked in (right).
- **Show-as-you-say:** cut on So@53.70 - base + WIT + auctioneer + trophy + cash heap
  all present (the auction is already over; this is the settling of accounts); green
  mini-arrow draws + `REVENUE` on revenue@54.82; red mini-arrow draws + `BILLS`
  (impact) on bills@56.44; lot tag hard-shows + GAVEL BANG (SFX + two drawn motion
  lines above the base gavel) on auction@58.30; `the WINNER pays` (impact) on
  pays@59.84; the auctioneer's rake completes one slow sweep from earth@58.86 to
  ~61.3; `the AUCTIONEER keeps the money` (impact - final beat) at ~61.40 (estimated);
  hold on the full frozen tableau to 62.101, hard cut to Section 5.
- **Sound:** low room murmur under the recap; one clean GAVEL BANG on 58.30 (the
  section's signature final hit); paper-scrape as the rake sweeps; a single soft
  register "cha-ching" under the last payoff line; all sound out by 62.0 - the cut to
  S5 lands on silence.
- **Color / contrast:** warm spotlight amber + dark room; green and red arrows make
  their final, smallest appearance; the trophy's gold and the cash heap glow on the
  auctioneer's side; WIT's white paddle is the brightest object on the losing side.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `auction-gavel-1.jpg` | browse-real-photo | wooden auctioneer gavel on sound block, warm spotlight, dark blurred room, no people/branding | full-bleed base | new |
| `auctioneer-at-podium.png` | generate | generic faceless suited figure (smooth featureless head) behind a wooden auction podium, one arm sweeping a wide wooden money-rake toward itself, isolated, transparent bg | right, ~30% width | new |
| `trophy-gold-parody.png` | reuse | the video hero trophy as the auction lot | on podium top, ~10% width | reuse (S1 hero) |
| `cash-bundle-generic.png` | reuse | 5 copies stacked/rotated into a swept cash heap by render | podium base, ~20% width heap | reuse (4.2, 4.7) |
| `wit-auction-winner-paddle.png` | generate | NEW WIT pose: blank white bidding paddle raised high, other arm cradling an absurdly long folded paper bill, proud chest, wide worried eyes, one sweat drop | left-of-center, ~2/5 frame, knees crop | new (payoff pose; S8 callback candidate) |

## Section Asset Summary

| Filename | Type | First scene | Reused in | Notes |
|---|---|---|---|---|
| `contract-stack-guarantees.png` | generate | 4.1 | - | fat contract stack, text-free top page (CSS titles it); S7 podium-prop candidate |
| `wit-mayor-signing.png` | generate (NEW pose) | 4.1 | - | teal sash (blank), smoking pen baked into pose; mayor kit |
| `gold-safe-fat.png` | generate | 4.2 | 4.5, 4.7 | SECTION HERO - overstuffed gold safe; shared-asset candidate for S5 (leakage to Zurich) and S8 |
| `cash-bundle-generic.png` | generate | 4.2 | 4.7, 4.9 | generic green bundle, NO real currency design; render stacks copies for piles |
| `wood-sign-hanging-blank.png` | generate | 4.6 | - | text-free wooden sign; CSS builds the CHESS CLUB / FIFA / $4B gag in steps |
| `gold-bar-single.png` | generate | 4.6 | - | render stacks 4 copies; S8 mantel candidate |
| `money-sack-gold.png` | generate | 4.8 | - | plain `$` emboss only, no real currency design |
| `auctioneer-at-podium.png` | generate | 4.9 | - | FACELESS suit + podium + money-rake; institution, not a person |
| `wit-auction-winner-paddle.png` | generate (NEW pose) | 4.9 | - | winner-pays payoff pose; S8 callback candidate |
| `trophy-gold-parody.png` | reuse (shared) | 4.9 | - | video hero trophy as the auction lot |
| `receipt-endless-roll.png` | reuse (shared) | 4.3 | - | prints `16x STADIUM (RETROFIT) ......... $???` (required section gag) |
| `boardroom-table-1.jpg` | browse-real-photo | 4.1 | - | empty boardroom, no people/brands |
| `tv-wall-glow-1.jpg` | browse-real-photo | 4.2 | - | blank glowing TV wall, brand-free |
| `stadium-construction-crane-1.jpg` | browse-real-photo | 4.3 | - | stadium bowl + cranes at dusk, no workers/logos |
| `rubber-stamp-ink-1.jpg` | browse-real-photo | 4.4 | - | stamp + red ink pad, no readable stamp face |
| `alpine-lake-town-1.jpg` | browse-real-photo | 4.5 | - | generic Swiss-look lake town, NO landmarks/flags/people |
| `chessboard-closeup-1.jpg` | browse-real-photo | 4.6 | - | wooden chessboard mid-game, no hands |
| `vault-door-1.jpg` | browse-real-photo | 4.7 | - | round steel vault door, ajar, no bank brands |
| `balance-scale-brass-1.jpg` | browse-real-photo | 4.8 | - | brass two-pan scale, pans level (CSS tilts overlays) |
| `auction-gavel-1.jpg` | browse-real-photo | 4.9 | - | gavel on sound block, warm spotlight |
| library poses (7) | pose | 4.2/4.3/4.4/4.5/4.6/4.7/4.8 | - | unimpressed_smirk_closeup, shocked_sweating_dismayed, deadpan_unimpressed_half_lidded, pointing_at_globe_explaining, rich_flex_gold_chain_sunglasses, mildly_surprised_hand_at_chin, eyes_closed_talking_open_palm |

## Approval Checks

- each scene picturable from text alone: yes - every scene names its base photo subject,
  element positions in %, entrance order, and device behavior; a reader can draw each
  frame.
- ~one scene per sentence, scene-types varied: yes - 9 scenes across 62.1s (target was
  ~8; two long money beats split at sentence boundaries to keep every base under ~10.1s;
  no two adjacent scenes share a type).
- every scene has a real/real-looking base: yes - 9 fresh people-free, brand-free photo
  bases (boardroom, TV wall, construction cranes, rubber stamp, alpine lake, chessboard,
  vault door, brass scale, gavel), all bright ~0.7-0.85, none reused within the section
  or from other sections.
- mascot big/high with a specific pose+expression per scene: yes - WIT in all 9 scenes,
  1/3 to 1/2 frame, head always high with only lower body cropped; 7 distinct library
  poses + 2 NEW poses; no pose repeats inside the section; side sequence
  center/right/left/center-right/left/right/left/right/left-center never parks twice.
- show-as-you-say timeline present per scene: yes - every entrance pinned to a real
  word@time from the JSON, hard-show vs impact marked; the final three words' regressed
  timestamps are flagged and estimated by position, and the last scene is clamped to
  62.101s.
- every asset has type + description + filename + layout: yes - per-scene tables plus
  the summary table above.
- repeated subjects reuse the same filename: yes - `trophy-gold-parody.png` and
  `receipt-endless-roll.png` reused from the shared registry (not recreated);
  `gold-safe-fat.png` and `cash-bundle-generic.png` reused by filename within the
  section.
- public figures handled as caricature/parody, punching up: no public figures appear -
  the auctioneer is a fully faceless generic suit (the institution), all other roles are
  WIT; edge aims at FIFA-as-institution only, never a nation.
- no image-generation prompts written here: correct - descriptions only; prompts are
  visual-implement's job.
- in sync with master `04-visual-plan.md`: pending - the master still lists Section 4 as
  `not planned`; the master-assembler should paste this section's scenes and update the
  Section Index row (9 scenes, 21 assets named) plus Cross-Section Continuity
  (receipt line printed in 4.3; trophy reused in 4.9; new shared candidates
  `gold-safe-fat.png`, `cash-bundle-generic.png`, `gold-bar-single.png`; arrow direction
  language defined here).

## Honesty rails obeyed (script Approval checks)

- Green/red arrow direction language starts here and is defined for the whole video
  (green left-to-right into FIFA's safe; red right-to-left onto the host).
- Zurich glossed on screen exactly as spoken (`Zurich, Switzerland` postcard caption).
- Exemption disambiguated: the `PAYS: $0` stamp lands ON the contract strip (scoped to
  the host-country guarantee, matching "meaning FIFA pays none" - no claim that FIFA
  pays no tax anywhere).
- No "cycle" jargon on screen - sub-chips say "the four years around..." as spoken.
- Numbers labeled as narrated: $7.5B under `REVENUE`, $13B only after the plate flips to
  `EXPECTS`; the banner says `BIGGEST PAYDAY EVER` only on the "on track" line.
- Fairness beat is visible and physical: green chips (`PRIZE MONEY`, `RUNNING THE
  TOURNAMENT`) really land on FIFA's paying pan - asymmetry shown, not a zero.
- Receipt gag printed exactly: `16x STADIUM (RETROFIT) ......... $???`.
