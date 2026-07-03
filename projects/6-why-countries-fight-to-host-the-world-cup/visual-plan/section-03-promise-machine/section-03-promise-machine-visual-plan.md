# Section 3 Visual Plan - The Promise Machine

Video: `Why Countries Fight to Host the World Cup (and Lose Billions)`
Section: `Section 3: The Promise Machine`
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

- Section goal: show the inflated-forecast machine that sells every bid - consultants
  produce a glossy "economic impact study" (a horoscope with a spreadsheet), two verified
  reality checks pop the promises (Brazil 2014 jobs, South Africa 2010 visitors, the
  per-tourist bill, the $100 -> $2.50 math), and land the payoff: impact studies are
  advertisements, and only economists re-read them.
- Duration: `60.779s` (audio: section 3 voiceover; real duration from timings meta)
- Timing source: `voiceover/section-03-promise-machine/section-03-word-timings.json`
  (whisper-tiny.en, generated 2026-07-02). Tokens were mapped to the real script words by
  position; mishearings do not affect the timestamps: "Before" heard as "For"/"for"
  (@3.30, @13.82, @21.10), "Bold. Before 2010." merged as "bold for 2010", "per extra
  tourist" heard as "for extra tourists", "And Brazil?" heard as "in Brazil". One
  corrupted token: the final word "problem." carries a backward-jump start (51.04) - its
  true position follows the@60.06-60.30, so the section END IS CLAMPED to the real audio
  duration `60.779s`.
- Scene count: `8` (a visible change every ~3.5-9.5s; no base held longer than ~9.5s)
- Scene-type rotation: 3.1 wide gag / contraption hero -> 3.2 object-hero document reveal
  -> 3.3 sky spectacle (balloon inflation) -> 3.4 evidence pop beat -> 3.5 evidence object
  + price tag -> 3.6 quick absurd-solution gag -> 3.7 visual-math operation board -> 3.8
  morning-after payoff board
- Mascot arc in this section: mock-grand showman (introducing the machine) -> dry smirk at
  the "science" -> HYPNOTIZED by rising numbers (the section money shot, NEW pose) ->
  smug reality-auditor with the pin -> bill shock at the suitcase tag -> shruggy
  "might as well" pragmatist -> dead-inside stare at two small coins -> the studious
  economist who actually re-reads the horoscope.

## Scenes

### Scene 3.1 - "Every bid starts the same way: with the promise machine. Before a country bids, someone hires consultants."

- **Local time:** `0.00-5.80` (Every@0.00, promise@2.34, machine@2.62, Before(For)@3.30,
  hires@4.54, consultants@4.94-5.82)
- **Role:** cold-open the section title as a literal object - a carnival "promise machine" -
  and immediately undercut it: the first thing the machine prints is a consulting bill on
  the video's receipt motif. Links forward: the machine's glossy output (the study
  document) becomes the hero of 3.2.
- **Composition / layout:** full-bleed real photo base: a vintage fairground at dusk,
  strings of warm glowing bulbs, people-free (~0.75 brightness, no dark scrim). Horizon
  ~60%. The promise machine stands CENTER-RIGHT (52-82% x, 20-90% y), a tall
  fortune-teller-style brass cabinet with a soft drop shadow. The receipt (reused motif
  file) prints from the machine's front slot and unspools down-left (slot at ~58% x,
  ~62% y; paper hangs across 40-62% x, 34-74% y). WIT giant on the LEFT (0-36% x,
  bottom-anchored high: head ~12% from top, knees cropped). Z-order: base < machine <
  receipt < WIT < text overlays.
- **Elements:**
  - *Base (full-bleed):* vintage fairground / carnival midway at dusk - warm bulb strings,
    striped booth edges blurred in the background, empty of people; bright and inviting so
    the machine reads as an attraction, not a horror prop.
  - *Promise machine (center-right, ~30% width):* a bespoke brass fortune-teller-style
    cabinet: glass dome on top with gold sparkles swirling inside, ornate scrollwork
    sides, a big side crank (right side), a coin slot, and a wide front output slot.
    A small engraved-look brass plaque (CSS, engraved lettering) sits on its front:
    `THE PROMISE MACHINE`, appearing on machine@2.62. The crank turns one slow rotation
    starting promise@2.34 (the machine "runs").
  - *Receipt (motif):* the endless receipt file unspools from the output slot on
    hires@4.54; one line item types onto it (CSS text on top of the asset, letter-by-
    letter): `1x OPTIMISM (CONSULTING) ......... $2,000,000`, fully readable by
    consultants@5.40. The paper strip stays above the subtitle-safe zone.
- **Mascot:** pose `proud_explaining_hand_on_chest_hand_on_hip` (library); placement LEFT,
  scale ~1/2 frame height (giant), knees cropped, facing right toward the machine;
  expression: eyes-closed mock-grand pride - a showman presenting his ridiculous
  invention.
- **On-screen text:** `THE PROMISE MACHINE` (engraved brass plaque style, on the cabinet
  front, straight, appears with a small glint on machine@2.62);
  `1x OPTIMISM (CONSULTING) ......... $2,000,000` (thin receipt-printer monospace, black
  on the white receipt strip, types on from hires@4.54, readable by 5.40).
- **Emotion:** mock-grand theater - "step right up" energy hiding a scam.
- **Insight / joke:** the machine that sells the bid produces exactly one product: a bill.
  The consultants get paid before a single tourist lands.
- **Linkage / eye path:** WIT's chest-proud gesture (left) -> the machine's glowing dome
  (center-right) -> down the crank to the output slot -> down the receipt to the
  $2,000,000 line. A left-to-right, then downward "follow the money" path.
- **Show-as-you-say:** base + WIT + machine visible from 0.00 (cold open); plaque glints in
  (hard-show + glint) on machine@2.62; crank turns from promise@2.34; receipt starts
  printing (impact - the motif SFX returns) on hires@4.54; the line item finishes typing
  by consultants@5.40 and holds.
- **Sound:** faint carnival music-box plink under 0-3s (low); crank ratchet on
  promise@2.34; the signature receipt printer tick-tick starts on hires@4.54; a soft
  cash-register "ka-ching" as the $2,000,000 resolves.
- **Color / contrast:** warm dusk amber + brass gold; the white receipt strip is the
  brightest object; the black $ line is the anchor.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `fairground-lights-1.jpg` | browse-real-photo | vintage fairground / carnival midway at dusk, glowing bulb strings, no people, no readable brand signs | full-bleed base | new |
| `promise-machine-contraption.png` | generate | fortune-teller-style brass carnival cabinet: glass dome with gold sparkles, ornate scrollwork, big side crank, coin slot, wide front output slot; blank front panel (plaque text is CSS); isolated, transparent bg | center-right, ~30% width, 20-90% y | new (section hero) |
| `receipt-endless-roll.png` | reuse | endless receipt motif; the OPTIMISM line item is CSS text on top | unspools from machine slot, 40-62% x, 34-74% y | reuse (S1.3 motif) |
| `proud_explaining_hand_on_chest_hand_on_hip.png` | pose | library pose - mock-grand showman presenting | left, ~1/2 frame, knees crop | reuse (library) |

### Scene 3.2 - "The consultants produce a big shiny document called an 'economic impact study'. Which sounds scientific. It is a horoscope with a spreadsheet."

- **Local time:** `5.82-13.80` (consultants@6.12, shiny@7.30, document@7.56, economic@8.70,
  study@9.62, scientific@10.62, It@11.78, horoscope@12.28, spreadsheet@13.06-13.82)
- **Role:** object-hero reveal of the section's key prop (the glossy parody study), then
  the [deadpan] joke made literal: the "science" is astrology in a grid. Links back: this
  document is what 3.1's machine printed; links forward: balloons inflate out of it in 3.3.
- **Composition / layout:** full-bleed real photo base: a dark polished marble boardroom
  tabletop at a shallow angle, one warm spotlight pool center (~0.75 brightness in the
  pool). The glossy study document stands LEFT (8-38% x, 18-84% y), leaning slightly as if
  propped, drop shadow. A holographic foil sticker slaps onto its top corner (30-42% x,
  22-32% y). The horoscope-spreadsheet scroll unrolls CENTER-RIGHT (42-74% x, 14-82% y).
  WIT peeks in from the RIGHT edge (74-100% x), chest-up closeup. Z-order: base <
  document < scroll < WIT < sticker/text.
- **Elements:**
  - *Base (full-bleed):* dark green-black marble table surface, soft warm spotlight,
    expensive-consultancy mood; nothing branded, no papers in the photo.
  - *Study document (left, ~28% width):* a thick glossy report with a deep navy cover,
    big gold-embossed serif title `ECONOMIC IMPACT STUDY`, a thin gold rule, and the
    parody firm mark `Big Numbers & Partners` small at the bottom; a gold foil sheen
    sweeps across the cover once on shiny@7.30.
  - *Foil sticker:* round holographic "quality seal" sticker reading `100% SCIENTIFIC*`
    (with a real asterisk) slaps onto the document's top-right corner on scientific@10.62;
    the asterisk is the setup the scroll pays off.
  - *Horoscope-spreadsheet scroll (center-right, ~30% width):* a midnight-purple parchment
    scroll, top edge crowned with a gold zodiac ring (generic star-sign glyphs), but the
    body is a spreadsheet: ruled grid cells filled with tiny faint numbers, thin gold
    constellation lines connecting random cells like star charts. It unrolls downward
    (impact) on horoscope@12.28.
- **Mascot:** pose `unimpressed_smirk_closeup` (library); placement RIGHT edge peek, ~1/3
  frame, chest crop (head + glasses fully inside frame), facing left at the scroll;
  expression: half-lidded dry smirk - the [deadpan] line owner.
- **On-screen text:** `ECONOMIC IMPACT STUDY` + `Big Numbers & Partners` (gold embossed
  serif, part of the document cover, visible from its entrance); `100% SCIENTIFIC*`
  (holographic sticker, 8deg tilt, slaps on scientific@10.62). No other text - the scroll
  is the punchline, not a caption.
- **Emotion:** dry skepticism - luxury packaging around fortune-telling.
- **Insight / joke:** "sounds scientific" is doing all the work; the reveal shows the
  actual genre: astrology with cells. The asterisk on the sticker quietly admits it.
- **Linkage / eye path:** document title (left) -> foil sticker (its corner) -> across to
  the unrolled scroll (center-right) -> WIT's smirk (right edge). Left-to-right, ending
  on the deadpan face as the audio lands "spreadsheet".
- **Show-as-you-say:** hard cut on The@5.82; document slides up into frame (hard-show +
  settle) on document@7.56 with the gold sheen on shiny@7.30 running as it arrives;
  sticker slaps (impact) on scientific@10.62; WIT hard-shows on It@11.78; scroll unrolls
  (impact) on horoscope@12.28 and its grid body is fully visible by spreadsheet@13.06.
- **Sound:** paper-slide whoosh for the document; foil "shing" on shiny@7.30; wet sticker
  squelch on scientific; a mystic chime + dry paper unroll on horoscope@12.28; receipt
  tick from 3.1 fades out under this scene.
- **Color / contrast:** dark marble + navy/gold luxury vs the purple starfield scroll;
  the holographic sticker is the brightest highlight.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `marble-boardroom-1.jpg` | browse-real-photo | dark polished marble tabletop, single warm spotlight pool, empty, no brands/people | full-bleed base | new |
| `impact-study-document.png` | generate | thick glossy parody report: deep navy cover, gold-embossed title `ECONOMIC IMPACT STUDY`, thin gold rule, small firm mark `Big Numbers & Partners`; isolated, transparent bg | left, ~28% width, 18-84% y | new (section key prop - reused 3.3, 3.8) |
| `horoscope-spreadsheet-scroll.png` | generate | midnight-purple parchment scroll, gold zodiac-glyph ring at top, body = ruled spreadsheet grid with tiny faint numbers + thin gold constellation lines linking cells; isolated, transparent bg | center-right, ~30% width, 14-82% y | new (reused 3.8) |
| `unimpressed_smirk_closeup.png` | pose | library dry-smirk closeup for the deadpan joke | right edge, ~1/3 frame, chest crop | reuse (library) |

### Scene 3.3 - "Before 2014, Brazil's study promised a boost worth billions, plus around three point six million jobs. Every year. [beat] Bold."

- **Local time:** `13.82-21.08` (Before(For)@13.82, 2014@14.00, promised@15.84,
  billions@16.90, jobs@19.30-19.80, Every@19.80, year@20.18, Bold@20.66-21.10)
- **Role:** case study 1 (Brazil) - the promises INFLATE. This is the section's WIT money
  shot: hypnotized by rising numbers. Links back: the balloons rise out of 3.2's document;
  links forward: 3.4 brings the pin.
- **Composition / layout:** full-bleed real photo base: bright blue sky with puffy white
  cumulus clouds (~0.85 brightness). The study document (reused) lies open at BOTTOM-CENTER
  (34-66% x, 78-100% y, bottom-cropped - decorative anchor only, nothing cue-critical down
  there). Two balloons rise from it on strings: a gold balloon upper-LEFT (6-32% x,
  12-52% y) and a bigger teal balloon upper-RIGHT (60-90% x, 10-56% y). WIT GIANT
  dead-center (34-66% x, head ~10% from top, hips cropped), looking UP. A manila case-file
  tab sits top-left (4-22% x, 5-11% y). Z-order: base < document < strings < balloons <
  WIT < stamps/labels.
- **Elements:**
  - *Base (full-bleed):* clean bright daytime sky, scattered cumulus clouds, sun high -
    promises float in advertising heaven.
  - *Study document (bottom-center):* same navy-gold report, lying open flat, both balloon
    strings tied to its spine - the promises literally come out of the study.
  - *Gold balloon (upper-left, ~24% width):* glossy round gold balloon, one white specular
    highlight, string down to the document. CSS label centered on it in bold handwritten
    black: `A BOOST WORTH BILLIONS`. It inflates from small (30% scale) to full between
    promised@15.84 and billions@17.54.
  - *Teal balloon (upper-right, ~28% width):* same glossy style, teal, slightly BIGGER
    than the gold one. CSS label: `3.6 MILLION JOBS`. Inflates from jobs@19.30 with a
    squeak. A red rubber stamp `EVERY YEAR` slams diagonally (8deg) across its lower
    half on year@20.18.
  - *Case-file tab:* small manila folder tab, typewriter-style text `BRAZIL, 2014`,
    hard-shows on 2014@14.00 (evidence chip - its twin returns in 3.4/3.5).
  - *"Bold." script:* small red handwritten word `Bold.` with a firm period, mid-frame
    between the balloons (42-56% x, 30-38% y), clear of WIT's face, on Bold@20.66.
- **Mascot:** pose `NEW: wit-hypnotized-numbers.png` - WIT full-body, head tilted up
  toward the balloons, mouth slightly open in a small awed "o", and inside his big
  rectangular glasses the pupils are replaced by tiny rising number streams (little
  ascending digits + a thin upward spiral) - hypnotized by the forecast. No costume.
  Placement CENTER GIANT, ~1/2+ frame, hips cropped, facing up-right toward the bigger
  teal balloon; expression: glassy wonder.
- **On-screen text:** `BRAZIL, 2014` (typewriter on manila tab, top-left, on 2014@14.00);
  `A BOOST WORTH BILLIONS` (bold handwritten black on the gold balloon, appears with the
  balloon); `3.6 MILLION JOBS` (bold handwritten black on the teal balloon, appears with
  the balloon); `EVERY YEAR` (red rubber stamp, 8deg tilt, on year@20.18); `Bold.` (small
  red handwritten script + period, mid-frame, on Bold@20.66).
- **Emotion:** seduction - the pitch working perfectly on WIT (and on the viewer).
- **Insight / joke:** the numbers are balloons: impressive, rising, and full of air. The
  narrator's one-word "Bold." undercuts the whole sky.
- **Linkage / eye path:** tab (top-left) -> gold balloon -> down the strings to the
  document -> up to the bigger teal balloon -> the `EVERY YEAR` stamp -> the tiny `Bold.`
  -> WIT's number-filled glasses in the center. Everything points up; only "Bold." points
  back down.
- **Show-as-you-say:** hard cut on Before@13.82 with base + document + WIT; tab hard-shows
  on 2014@14.00; gold balloon inflates (squeak, continuous) promised@15.84 -> full on
  billions@17.54; teal balloon inflates on jobs@19.30 (bigger, faster squeak); `EVERY
  YEAR` stamps (impact) on year@20.18; `Bold.` hard-shows (small pop) on Bold@20.66;
  hold the sky to 21.08.
- **Sound:** two balloon-squeak inflations (pitched up for the bigger one); stamp thud on
  year@20.18; a faint dreamy shimmer under WIT's hypnosis; tiny dry "tick" on Bold.
- **Color / contrast:** bright sky blue + white clouds; gold and teal balloons pop hard;
  the only reds are the stamp and "Bold." - the skeptic's color.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `blue-sky-clouds-1.jpg` | browse-real-photo | bright blue daytime sky with puffy cumulus clouds, no ground objects, no people | full-bleed base | new |
| `impact-study-document.png` | reuse | the study lying open, balloon strings tied to its spine | bottom-center, 34-66% x, bottom-cropped | reuse (3.2) |
| `balloon-shiny-gold.png` | generate | glossy round gold party balloon with white specular highlight and short string, BLANK surface (labels are CSS); isolated, transparent bg | upper-left, ~24% width | new (reused 3.4 giant) |
| `balloon-shiny-teal.png` | generate | glossy round teal party balloon, same style, blank, with string; isolated, transparent bg | upper-right, ~28% width | new (reused 3.4 small) |
| `wit-hypnotized-numbers.png` | generate | NEW WIT pose: full body, head tilted up, small awed "o" mouth, pupils replaced by tiny rising digit streams + thin upward spiral inside the glasses - hypnotized by numbers; no costume | center giant, ~1/2+ frame, hips crop | new (NEW pose - section money shot) |

### Scene 3.4 - "Before 2010, South Africa was told to expect almost five hundred thousand foreign visitors. About three hundred thousand actually came for the Cup."

- **Local time:** `21.10-30.18` (Before(for)@21.10, 2010@21.48, South@22.60, expect@24.00,
  almost@24.34, 500,000@24.82-26.00, visitors@26.32, About@27.36, 300,000@27.64-28.68,
  actually@28.68, came@29.06, Cup@29.60-30.20)
- **Role:** case study 2 (South Africa) - the red pin arrives and reality pops the
  promise. First on-screen promised-vs-actual pair. Links back: same balloon language as
  3.3; links forward: 3.5 counts what each real tourist cost.
- **Composition / layout:** full-bleed real photo base: an empty airport arrivals hall in
  morning light - glass, gates, a wide clean floor, no people (~0.8 brightness). A GIANT
  gold balloon (reused file) floats CENTER-RIGHT (48-86% x, 8-64% y), string trailing
  down. WIT stands LEFT (0-34% x, waist crop, head ~14% from top). The giant red pushpin
  flies in along a line from WIT's side to the balloon. After the pop, a small teal
  balloon (reused file at ~35% scale) bobs LOW-RIGHT (62-80% x, 48-70% y). Manila tab
  top-left (4-24% x, 5-11% y). Z-order: base < balloons < pin < WIT < labels; CSS pop
  scraps (namespaced `.pop-bits`) above all briefly.
- **Elements:**
  - *Base (full-bleed):* bright empty airport arrivals hall - the place half a million
    visitors were supposed to walk through; its emptiness is the quiet joke.
  - *Giant gold balloon (center-right, ~38% width):* the same gold balloon file scaled
    giant; inflates from 55% to full between expect@24.00 and visitors@26.32. CSS label
    in bold handwritten black: `ALMOST 500,000 VISITORS`.
  - *Red pushpin (from left, ~14% width):* a bespoke oversized red pushpin - glossy round
    red head, steel needle - flies in point-first from WIT's raised hand line on
    About@27.36 and strikes the balloon on actually@28.68.
  - *Pop scraps:* 6-8 gold CSS shreds (namespaced) burst outward for ~0.4s on the pop,
    then fall away.
  - *Small teal balloon (low-right, ~13% width):* the teal file small and slightly
    under-inflated-looking (rendered at reduced scale + 6deg sag tilt), bobbing gently.
    CSS label in smaller handwriting: `ABOUT 300,000 CAME`.
  - *Case-file tab:* manila tab, typewriter text `SOUTH AFRICA, 2010`, hard-shows on
    2010@21.48 (twin of 3.3's tab).
- **Mascot:** pose `smug_raised_eyebrow_smirk` (library); placement LEFT, ~2/5 frame,
  waist crop, facing right toward the balloon; expression: one raised eyebrow, smirk -
  the reality auditor who just threw the pin.
- **On-screen text:** `SOUTH AFRICA, 2010` (typewriter on manila tab, top-left, on
  2010@21.48); `ALMOST 500,000 VISITORS` (bold handwritten black on the giant balloon,
  grows with it from expect@24.00); `ABOUT 300,000 CAME` (smaller handwritten black on
  the small teal balloon, on came@29.06). Hedges "ALMOST" / "ABOUT" and the word "CAME"
  are kept - the labels never say tourists did not come.
- **Emotion:** the smirk of arithmetic - watching a promise meet a pin.
- **Insight / joke:** promised vs actual as balloon physics: the forecast is huge and
  shiny; reality is smaller, lower, and slightly saggy - but it exists.
- **Linkage / eye path:** tab (top-left) -> giant balloon label (center-right) -> the
  pin's flight line from WIT (left) -> POP -> drop down-right to the small balloon's
  `ABOUT 300,000 CAME`. Diagonal down-right = deflation.
- **Show-as-you-say:** hard cut on Before@21.10; tab hard-shows on 2010@21.48; giant
  balloon inflates expect@24.00 -> visitors@26.32 (label scales with it); pin flies
  (fast, 0.3s) on About@27.36 and strikes on actually@28.68 (impact: pop + scraps +
  balloon and label vanish); small teal balloon bobs up (hard-show + gentle bounce) with
  its label on came@29.06; hold through Cup@29.60 to 30.18.
- **Sound:** balloon-stretch creak during the giant inflation; a sharp POP on
  actually@28.68 (kept under the voice); a small sad squeak-bounce for the little
  balloon; airport room tone very low throughout.
- **Color / contrast:** cool glass-and-daylight base; gold balloon dominates until the
  pop; after it, the small teal balloon is deliberately the only saturated object left.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `airport-arrivals-1.jpg` | browse-real-photo | empty airport arrivals hall, morning light, glass and gates, no people, no airline logos readable | full-bleed base | new |
| `balloon-shiny-gold.png` | reuse | giant scale = the 500,000 promise | center-right, ~38% width | reuse (3.3) |
| `red-pushpin-giant.png` | generate | oversized red pushpin: glossy round red head, steel needle, slight perspective, point leading; isolated, transparent bg | flies left -> center-right, ~14% width | new |
| `balloon-shiny-teal.png` | reuse | small scale + sag tilt = the 300,000 reality | low-right, ~13% width | reuse (3.3) |
| `smug_raised_eyebrow_smirk.png` | pose | library reality-auditor smirk | left, ~2/5 frame, waist crop | reuse (library) |

### Scene 3.5 - "And when economists counted South Africa's real gain in tourists, the bill came to thousands of dollars of public money per extra tourist. [slower] Per tourist."

- **Local time:** `30.20-38.56` (economists@30.50, counted@30.94, Africa's@31.84,
  tourists@33.14, bill@34.04, thousands@34.64, public@35.76, money@35.98,
  per(for)@36.56, tourist@37.88-38.58)
- **Role:** the per-tourist bill made physical - one real tourist's suitcase wearing a
  price tag like a luxury item. Links back: continues the South Africa case (same manila
  tab); links forward: sets up 3.6's "cheaper to mail tickets" absurdity.
- **Composition / layout:** full-bleed real photo base: an empty baggage-claim carousel
  hall, the steel belt curving through frame (~0.75 brightness). A vintage leather
  suitcase rides the belt CENTER (36-68% x, 36-78% y), drop shadow. A giant cream swing
  tag tied to its handle flips up to CENTER-RIGHT (52-84% x, 24-58% y - above the
  subtitle zone). WIT stands RIGHT (64-100% x, chest crop) leaning in over the belt.
  Manila tab top-left (4-20% x, 5-11% y). Z-order: base < suitcase < tag < WIT < stamp.
- **Elements:**
  - *Base (full-bleed):* people-free baggage-claim hall, steel carousel belt, cool
    industrial light - where the "extra tourist" actually arrives.
  - *Suitcase (center, ~30% width):* worn vintage leather suitcase with brass corners and
    a few GENERIC travel stickers (plain shapes: a sun, a wave, a mountain - no flags, no
    brands, no city names). It slides in from the left along the belt at the cut and
    stops center.
  - *Giant swing tag:* cream paper tag, rough string to the handle, big handwritten black
    text: `PUBLIC MONEY: THOUSANDS OF $` (line 1). A red rubber stamp slams across the
    tag's lower third on per@36.56: `PER TOURIST` - restamping a second time, slightly
    offset and darker, on the echo tourist@37.88 (the [slower] beat gets its own visual
    echo).
- **Mascot:** pose `shocked_sweating_dismayed` (library); placement RIGHT, ~2/5 frame,
  chest crop, facing left down at the tag; expression: wide eyes, square mouth, sweat
  drop - reading the bill.
- **On-screen text:** `SOUTH AFRICA` (typewriter on manila tab, top-left, hard-shows on
  Africa's@31.84 - re-anchoring the math to the right country); `PUBLIC MONEY:
  THOUSANDS OF $` (big handwritten black on the cream tag, on thousands@34.64);
  `PER TOURIST` (red stamp, 6deg tilt, on per@36.56; second offset stamp on
  tourist@37.88). No exact figure is invented - the narration says "thousands", the tag
  says "THOUSANDS".
- **Emotion:** sticker shock - the quiet horror of unit economics.
- **Insight / joke:** one suitcase, priced like a car: the cost of buying a single extra
  tourist with public money.
- **Linkage / eye path:** tab (top-left) -> suitcase sliding to center -> up the string to
  the giant tag -> the red `PER TOURIST` stamp -> WIT's sweating face beside it. The
  string physically ties the tourist to the bill.
- **Show-as-you-say:** hard cut on And@30.20 with base + belt; suitcase slides in
  (continuous, settles) economists@30.50 -> counted@30.94; tab hard-shows on
  Africa's@31.84; WIT hard-shows on bill@34.04; tag flips up (impact) with line 1 on
  thousands@34.64; `PER TOURIST` stamps (impact) on per@36.56; echo stamp (smaller
  impact) on tourist@37.88; hold to 38.56.
- **Sound:** low carousel rumble loop; case thump as it settles; paper flip for the tag;
  two heavy stamp thuds (the second softer); WIT's tiny gulp on bill@34.04.
- **Color / contrast:** cool steel grays make the warm leather suitcase and cream tag
  pop; red stamps are the only red in frame.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `baggage-carousel-1.jpg` | browse-real-photo | empty airport baggage-claim carousel, steel belt curving through frame, no people, no airline branding | full-bleed base | new |
| `suitcase-vintage-tourist.png` | generate | worn vintage leather suitcase, brass corners, a few generic shape travel stickers (sun, wave, mountain - no flags/brands/city names); isolated, transparent bg | center, ~30% width, on the belt | new |
| `shocked_sweating_dismayed.png` | pose | library bill-shock reaction | right, ~2/5 frame, chest crop | reuse (library) |

### Scene 3.6 - "[beat] At that price, it is cheaper to mail strangers free plane tickets."

- **Local time:** `38.58-42.06` (At@38.58, price@38.92, cheaper@39.50, mail@39.94,
  strangers@40.22, plane@41.04, tickets@41.32-42.08)
- **Role:** the fast absurd-solution gag - a 3.5s palate cleanser between the two math
  beats. Links back: answers 3.5's per-tourist price; links forward: 3.7 does the same
  math to Brazil.
- **Composition / layout:** full-bleed real photo base: a bright red street postbox,
  closeup, on a sunny street with soft bokeh behind (~0.8 brightness). The postbox body
  fills RIGHT-CENTER (44-84% x, 18-100% y). An airmail envelope with a plane ticket
  poking out floats above the slot (46-74% x, 16-44% y), tilted 10deg, descending toward
  the slot. WIT giant LEFT (2-36% x, knees crop, head ~12% from top). A green stamp sits
  top-left of the envelope's path (10-38% x, 12-28% y). Z-order: base < WIT < envelope <
  stamp.
- **Elements:**
  - *Base (full-bleed):* cheerful red postbox closeup, sunny street bokeh - the "solution"
    infrastructure. Sourcing note: pick a GENERIC postbox with no royal cypher, national
    emblem, or postal-brand lettering visible (crop or angle away if needed).
  - *Airmail envelope (center-right, ~26% width):* classic white envelope with red-blue
    chevron airmail border, `AIR MAIL` in plain stamp lettering, and a generic parody
    plane ticket poking out of the open flap (plain `BOARDING PASS` text, a simple plane
    silhouette, no airline). It descends toward the postbox slot from mail@39.94,
    reaching the slot lip by tickets@41.32 and dropping in with a final flick.
  - *Green stamp:* rubber stamp `CHEAPER` with a hand-drawn check mark, green ink, 6deg
    tilt, slams on cheaper@39.50.
- **Mascot:** pose `shrug_both_hands_up_smile` (library); placement LEFT, ~1/2 frame
  (giant), knees crop, facing camera; expression: relaxed both-hands-up shrug - "at that
  price? honestly, might as well."
- **On-screen text:** `CHEAPER` + check mark (green rubber stamp, top-left, on
  cheaper@39.50); `AIR MAIL` and `BOARDING PASS` (plain print, part of the envelope
  asset). Nothing else - the gag is the object.
- **Emotion:** comic resignation - the joke solution that is genuinely better value.
- **Insight / joke:** the math is so bad that random generosity beats the official plan;
  a national tourism strategy replaced by a mailbox.
- **Linkage / eye path:** WIT's shrug (left) -> the green `CHEAPER` stamp above -> follow
  the envelope's fall (center) -> into the postbox slot (right). One clean diagonal
  drop.
- **Show-as-you-say:** hard cut on At@38.58 with base + WIT already shrugging; `CHEAPER`
  stamps (impact) on cheaper@39.50; envelope appears top-center (hard-show) and starts
  its descent on mail@39.94; it drops into the slot (small impact + flap) on
  tickets@41.32-42.06.
- **Sound:** stamp thunk; a soft whoosh for the envelope; a paper "flump" + tiny cheerful
  ding as it lands in the slot; sunny street ambience very low.
- **Color / contrast:** postbox red + envelope white dominate; the green stamp is the
  only green in frame (verdict color vs red cost stamps of 3.5).

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `mailbox-red-1.jpg` | browse-real-photo | bright red street postbox closeup, sunny bokeh street, no people, no postal branding/royal cypher visible | full-bleed base | new |
| `airmail-envelope-ticket.png` | generate | white envelope with red-blue chevron airmail border, `AIR MAIL` plain lettering, generic parody `BOARDING PASS` ticket poking out (plane silhouette, no airline); isolated, transparent bg | center-right, ~26% width, descending to slot | new |
| `shrug_both_hands_up_smile.png` | pose | library nonchalant shrug | left, ~1/2 frame, knees crop | reuse (library) |

### Scene 3.7 - "And Brazil? For every hundred dollars Brazil spent on its World Cup, tourist money brought back about two dollars fifty. [slower] Two dollars fifty. Out of one hundred."

- **Local time:** `42.08-51.28` (Brazil@42.38, every@43.02, hundred@43.34, spent@44.38,
  Cup@45.36, brought@46.48, about@47.32, two@47.70, dollars@48.02, fifty@48.26,
  two(echo)@48.94, fifty(echo)@49.56, out@50.06, hundred@50.62-51.30)
- **Role:** the section's REQUIRED visual-math operation: $100 goes in, $2.50 comes out -
  shown as a physical size transaction at a stadium turnstile, never as a bare number.
  Links back: same "what came back" question as 3.4-3.5, now for Brazil; links forward:
  3.8 explains WHY the numbers were wrong.
- **Composition / layout:** full-bleed real photo base: a row of stadium entrance
  turnstiles, straight-on, people-free (~0.75 brightness). The parody $100 banknote
  starts LARGE at LEFT (6-40% x, 30-58% y). The center turnstile arm sits at 44-58% x.
  Two gold coins + one half coin land small at RIGHT (64-78% x, 56-70% y). WIT GIANT
  CENTER (34-66% x), waist-cropped BEHIND the turnstile bar, head ~10% from top, looking
  down at the coins. Label chips sit under the note (10-34% x, 62-70% y) and under the
  coins (60-82% x, 74-80% y - still above the subtitle zone). Z-order: base < WIT <
  turnstile line of the photo < note/coins < chips/bracket.
- **Elements:**
  - *Base (full-bleed):* clean stadium turnstile row - the exact doorway Brazil's money
    walked through.
  - *Parody $100 note (left, ~34% width):* generic mint-green banknote, big `100` in the
    corners, a laurel-wreathed GLOBE in the center oval (no person, no real currency
    design), ornate guilloche border - own design. On Cup@45.36 it slides right and
    SQUEEZES through the turnstile slot (squash + shrink animation as it passes,
    0.8s), vanishing behind the arm.
  - *Coins (right):* what comes out the other side: one large gold coin embossed `1`
    drops on two@47.70; a second identical coin drops on dollars@48.02; a visibly
    half-sized coin embossed `50` drops on fifty@48.26. Each lands with a bounce and
    settles - together they are comically tiny next to where the note stood.
  - *Ghost note:* on out@50.06, a pale ghost outline of the full-size $100 note fades in
    around the coins at the SAME footprint the real note had (scaled to sit behind the
    coins, 56-90% x, 40-72% y) - the coins fill ~2% of its area. A hand-drawn bracket
    with the label `OUT OF ONE HUNDRED` draws under it on hundred@50.62.
  - *Label chips:* small torn-paper chips, handwritten black: `SPENT: $100` under the
    note on spent@44.38; `BACK: $2.50` under the coins on fifty@48.26.
- **Mascot:** pose `exhausted_dead_inside_eye_bags` (library); placement CENTER GIANT,
  ~1/2 frame, waist crop behind the turnstile bar; facing down-right at the coins;
  expression: gray-faded dead-inside stare - the [slower] echo plays over his silence.
- **On-screen text:** `SPENT: $100` (handwritten black chip, under the note, on
  spent@44.38); `BACK: $2.50` (handwritten black chip, under the coins, on fifty@48.26);
  `OUT OF ONE HUNDRED` (handwritten black on a hand-drawn bracket under the ghost note,
  on hundred@50.62). The math on screen is exactly the narration's math - nothing added.
- **Emotion:** deflation - the slow, silent kind. The echo line lands on a frozen frame.
- **Insight / joke:** the "return on investment" is physically visible: a banknote goes
  through the turnstile and comes back as pocket change. The ghost outline makes the
  missing $97.50 visible without saying a word.
- **Linkage / eye path:** big note + `SPENT: $100` (left) -> through the turnstile
  (center, under WIT's dead stare) -> tiny coins + `BACK: $2.50` (right) -> the ghost
  note swallowing them -> bracket `OUT OF ONE HUNDRED`. Left-to-right shrinkage IS the
  sentence.
- **Show-as-you-say:** hard cut on And(in)@42.08 with base + WIT + note already in frame;
  `SPENT: $100` chip hard-shows on spent@44.38; the note squeezes through the turnstile
  on Cup@45.36 (continuous 0.8s squash); coins drop (three small impacts) on two@47.70 /
  dollars@48.02 / fifty@48.26 with `BACK: $2.50` on the last; during the echo
  (48.94-50.06) NOTHING moves - held frame under the slowed voice; ghost note fades in
  on out@50.06; bracket + `OUT OF ONE HUNDRED` draws on hundred@50.62; hold to 51.28.
- **Sound:** turnstile clunk-ratchet as the note squeezes through; three coin clinks
  (descending pitch); total silence under the echo lines except the voice; a soft airy
  "haaa" (deflating) as the ghost note appears.
- **Color / contrast:** neutral steel base; mint-green note vs tiny warm gold coins; the
  ghost note is a pale outline - the frame's emptiest and loudest element.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `stadium-turnstile-1.jpg` | browse-real-photo | row of stadium entrance turnstiles, straight-on, people-free, no club/brand signage | full-bleed base | new |
| `banknote-hundred-parody.png` | generate | generic parody banknote: mint-green, `100` in corners, laurel-wreathed globe in the center oval (no person, not any real currency design), guilloche border; isolated, transparent bg | left, ~34% width; squeezes through turnstile; returns as pale ghost outline right | new |
| `coin-gold-one.png` | generate | single gold coin embossed `1`, slight perspective, soft shine; isolated, transparent bg | right, ~7% width each, two drops | new (used twice in-scene) |
| `coin-gold-half.png` | generate | half-sized gold coin embossed `50`, same style; isolated, transparent bg | right, ~4% width | new |
| `exhausted_dead_inside_eye_bags.png` | pose | library dead-inside stare for the math payoff | center giant, ~1/2 frame, waist crop behind turnstile | reuse (library) |

### Scene 3.8 - "Because impact studies are not predictions. They are advertisements. Nobody re-reads the horoscope after the party. [beat] Well. Economists do. That is the problem."

- **Local time:** `51.30-60.779` (because@51.30, studies@51.92, not@52.60,
  predictions@52.82, advertisements@54.10-55.30, nobody@55.30, horoscope@56.44,
  party@57.80, Well@58.08, economists@58.82, do@59.02, That@59.72, the@60.06-60.30,
  problem clamped to end@60.779 - the JSON's "problem." token carries a corrupted
  backward timestamp)
- **Role:** section payoff board - the reclassification (prediction -> advertisement) and
  the morning-after button: only economists re-read the horoscope. Links back: the study
  document and the horoscope scroll return from 3.2; links forward: hard cut into
  Section 4's contract.
- **Composition / layout:** full-bleed real photo base: a morning-after party floor -
  wooden floorboards strewn with confetti, streamers, and a couple of deflated balloons,
  soft daylight from a window (~0.75 brightness). The study document (reused) lies flat
  CENTER-LEFT (12-46% x, 40-84% y), slightly angled. A cream sticky note sits above it
  (16-38% x, 24-36% y). The horoscope scroll (reused) lies half-rolled LOW-RIGHT
  (56-84% x, 52-86% y) among the confetti. WIT sits RIGHT (58-100% x, torso crop,
  head ~16% from top) bent over the scroll, an SVG magnifier over it. Z-order: base <
  scroll < document < WIT < magnifier < sticky/stamp/markup.
- **Elements:**
  - *Base (full-bleed):* real morning-after party floor - confetti and deflated balloons
    on wood, quiet daylight; a deliberate callback to 3.3's inflated balloons, now dead
    on the floor.
  - *Study document (center-left, ~30% width):* the same navy-gold report, now lying
    abandoned on the floor; a red rubber stamp slams diagonally (10deg) across its whole
    cover on advertisements@54.10: `ADVERTISEMENTS.`
  - *Sticky note:* cream square sticky note, handwritten black `PREDICTIONS?`, hard-shows
    on studies@51.92; a fat red hand-drawn X scribbles over it on predictions@52.82.
  - *Horoscope scroll (low-right, ~26% width):* the same purple scroll, half-rolled and
    crumpled among the confetti - the horoscope after the party.
  - *Magnifying glass (SVG, drawn element - not an asset):* a hand-drawn-style SVG brass
    magnifier, lens ~10% of frame width, hovers over the scroll's grid cells on
    economists@58.82 with a subtle lens-zoom of the cells beneath it; a thin red
    hand-drawn circle draws around the `ADVERTISEMENTS.` stamp on That@59.72.
- **Mascot:** pose `reading_book_round_glasses_studious` (library); placement RIGHT,
  ~2/5 frame, torso crop, facing down-left toward the scroll; expression: studious calm -
  WIT as the economist, the only person still reading.
- **On-screen text:** `PREDICTIONS?` (handwritten black on cream sticky note, on
  studies@51.92, X-ed out in red on predictions@52.82); `ADVERTISEMENTS.` (big red rubber
  stamp with a period, 10deg tilt, across the document cover, on advertisements@54.10).
  No text in the final 5s - the button plays on objects and WIT alone.
- **Emotion:** quiet clarity after the noise - the joke turns true.
- **Insight / joke:** the genre correction in one stamp: studies are ads. Then the tag:
  the only re-reader is the economist - and by then the money is spent. The dead balloons
  on the floor ARE 3.3's promises.
- **Linkage / eye path:** sticky `PREDICTIONS?` (upper-left) -> red X -> down to the
  stamped `ADVERTISEMENTS.` on the document -> right along the confetti to the crumpled
  scroll -> WIT's magnifier over it -> back to the red circle on the stamp for the final
  word. A full loop that ends on the verdict.
- **Show-as-you-say:** hard cut on because@51.30 with base + document + scroll + WIT
  visible (the party is already over); sticky note hard-shows on studies@51.92; red X
  scribbles (impact) on predictions@52.82; `ADVERTISEMENTS.` stamps (big impact) on
  advertisements@54.10; nothing new during "nobody re-reads..." (55.30-58.08 - held
  quiet frame); magnifier drifts in over the scroll (soft hard-show + lens shimmer) on
  economists@58.82; red circle draws around the stamp on That@59.72; hold, then hard cut
  out at the clamped section end 60.779.
- **Sound:** near-quiet morning room tone; sticky-note squelch; marker squeak for the X;
  one heavy stamp thud on advertisements@54.10; a single page rustle + soft "hm" chime
  on economists@58.82; silence into the cut.
- **Color / contrast:** muted morning wood + faded confetti; the red stamp and red X are
  the only saturated reds - the verdict owns the frame.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `party-aftermath-1.jpg` | browse-real-photo | morning-after party floor: confetti, streamers, deflated balloons on wooden floorboards, soft daylight, no people | full-bleed base | new |
| `impact-study-document.png` | reuse | the study abandoned on the floor, stamp is CSS on top | center-left, ~30% width, 40-84% y | reuse (3.2, 3.3) |
| `horoscope-spreadsheet-scroll.png` | reuse | half-rolled, crumpled among confetti | low-right, ~26% width | reuse (3.2) |
| `reading_book_round_glasses_studious.png` | pose | library studious pose - WIT as the economist re-reading | right, ~2/5 frame, torso crop | reuse (library) |

## Section Asset Summary

| Filename | Type | First scene | Reused in | Notes |
|---|---|---|---|---|
| `promise-machine-contraption.png` | generate | 3.1 | - | section hero contraption; plaque text is CSS |
| `receipt-endless-roll.png` | reuse | 3.1 | - | VIDEO MOTIF (born S1.3); OPTIMISM $2,000,000 line is CSS on top |
| `impact-study-document.png` | generate | 3.2 | 3.3, 3.8 | section key prop; parody firm `Big Numbers & Partners` |
| `horoscope-spreadsheet-scroll.png` | generate | 3.2 | 3.8 | the "horoscope with a spreadsheet" made literal |
| `balloon-shiny-gold.png` | generate | 3.3 | 3.4 (giant) | blank surface - all number labels are CSS |
| `balloon-shiny-teal.png` | generate | 3.3 | 3.4 (small, sagged) | blank surface - all number labels are CSS |
| `wit-hypnotized-numbers.png` | generate (NEW pose) | 3.3 | - | section money shot: rising-digit pupils; thumbnail candidate |
| `red-pushpin-giant.png` | generate | 3.4 | - | the reality pin |
| `suitcase-vintage-tourist.png` | generate | 3.5 | - | generic stickers only - no flags/brands/city names |
| `airmail-envelope-ticket.png` | generate | 3.6 | - | parody BOARDING PASS, no airline |
| `banknote-hundred-parody.png` | generate | 3.7 | - | own design, globe center, no person, not a real currency |
| `coin-gold-one.png` | generate | 3.7 | - | used twice in-scene (two drops) |
| `coin-gold-half.png` | generate | 3.7 | - | the "fifty" half coin |
| `fairground-lights-1.jpg` | browse-real-photo | 3.1 | - | dusk carnival, no people/brands |
| `marble-boardroom-1.jpg` | browse-real-photo | 3.2 | - | consultancy luxury surface |
| `blue-sky-clouds-1.jpg` | browse-real-photo | 3.3 | - | promise heaven |
| `airport-arrivals-1.jpg` | browse-real-photo | 3.4 | - | empty arrivals = the missing visitors |
| `baggage-carousel-1.jpg` | browse-real-photo | 3.5 | - | no airline branding |
| `mailbox-red-1.jpg` | browse-real-photo | 3.6 | - | generic postbox, no cypher/branding |
| `stadium-turnstile-1.jpg` | browse-real-photo | 3.7 | - | the money's doorway |
| `party-aftermath-1.jpg` | browse-real-photo | 3.8 | - | dead balloons = 3.3 callback |
| library poses (7) | pose | 3.1/3.2/3.4/3.5/3.6/3.7/3.8 | - | proud_explaining_hand_on_chest_hand_on_hip, unimpressed_smirk_closeup, smug_raised_eyebrow_smirk, shocked_sweating_dismayed, shrug_both_hands_up_smile, exhausted_dead_inside_eye_bags, reading_book_round_glasses_studious |

## Approval Checks

- each scene picturable from text alone: yes - every scene names the base photo, every
  element's position in %, z-order, entrance word@time, and the mascot's pose, side,
  scale, crop, and expression.
- ~one scene per sentence, scene-types varied: yes - 8 scenes over 60.779s, one per beat
  (the two-sentence beats 3.2/3.4/3.7 stay single-idea); rotation runs contraption gag ->
  document reveal -> balloon spectacle -> pop evidence -> price-tag evidence -> quick gag
  -> math operation -> payoff board; longest base hold is 9.5s.
- every scene has a real/real-looking base: yes - 8 FRESH people-free, brand-free photo
  bases (fairground, marble table, sky, arrivals hall, baggage carousel, postbox,
  turnstiles, party-aftermath floor), all ~0.75-0.85 brightness, none reused from Section
  1 or within this section.
- mascot big/high with a specific pose+expression per scene: yes - WIT in all 8 scenes,
  giant (~1/2) in 3.1/3.3/3.6/3.7 and ~1/3-2/5 elsewhere, always head-high with only
  legs/waist cropping; side order left -> right -> center -> left -> right -> left ->
  center -> right (never the same side twice in a row); no pose repeats within the
  section; one NEW pose invented (`wit-hypnotized-numbers`).
- show-as-you-say timeline present per scene: yes - every entrance is pinned to a real
  whisper word@time and marked hard-show vs impact; the final scene end is clamped to the
  real 60.779s audio (the JSON's last token has a corrupted backward timestamp, noted).
- every asset has type + description + filename + layout: yes - per-scene tables plus the
  dedup summary; 12 generate (incl. the new pose), 8 browse bases, 1 registry reuse,
  7 library poses.
- repeated subjects reuse the same filename: yes - `receipt-endless-roll.png` (shared
  registry, not renamed), `impact-study-document.png` (3.2/3.3/3.8),
  `horoscope-spreadsheet-scroll.png` (3.2/3.8), both balloons (3.3/3.4),
  `banknote-hundred-parody.png` ghost reuse and `coin-gold-one.png` double-drop are
  in-scene reuses of one file.
- public figures handled as caricature/parody, punching up: n/a-safe - no real people
  anywhere; the parody targets are consultants-as-role ("Big Numbers & Partners") and the
  incentive system; the banknote, ticket, postbox, and suitcase are all generic/parody
  with no real brands, flags, currencies, or airlines.
- no image-generation prompts written here: correct - descriptions only; prompt writing
  is visual-implement's job.
- in sync with master `04-visual-plan.md`: pending - the master currently lists Section 3
  as `not planned`; the master-assembler must paste this section block in and update the
  Section Index row (8 scenes, 28 assets named, duration 60.779s).

## Honesty Rails (from script Approval check - verified)

- One number per beat, each on a prop: billions + 3.6M jobs on balloons (3.3), 500K vs
  300K on balloons (3.4), "thousands per tourist" on the suitcase tag (3.5), $100 vs
  $2.50 on note/coins (3.7), $2,000,000 on the receipt (3.1).
- On-screen numbers match narration EXACTLY - hedges kept ("ALMOST 500,000", "ABOUT
  300,000", "THOUSANDS OF $", "ABOUT" spoken for $2.50 while chips carry the plain
  figures the narration states); no stats added anywhere.
- South Africa labels say `ABOUT 300,000 CAME` - never "tourists didn't come"; the
  per-tourist bill scene re-anchors `SOUTH AFRICA` on its tab.
- The $2.50 math is a physical operation (note squeezes through a turnstile, coins drop,
  ghost-note size comparison), not a bare number.
- Receipt gag present exactly as scripted: `1x OPTIMISM (CONSULTING) ......... $2,000,000`
  printed by the promise machine in 3.1, item text as CSS on the shared receipt asset.
