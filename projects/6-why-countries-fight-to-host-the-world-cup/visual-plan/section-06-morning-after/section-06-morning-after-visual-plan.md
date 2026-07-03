# Section 6 Visual Plan - The Morning After

Video: `Why Countries Fight to Host the World Cup (and Lose Billions)`
Section: `Section 6: The Morning After`
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

- Section goal: show what the host keeps after the party - white elephants that must be
  fed. Gloss "white elephant" for learners, make the feeding literal (a stadium-pet with
  a `MAINTENANCE` bowl), land the three evidence gags (2015 buses, empty rainforest
  seats, birthday-party venue), put Cape Town on the fridge feeding schedule (and onto
  the receipt), and end HONESTLY on the recovery beat (concerts, ten years, Bruno Mars
  as a factual name only - lights, never a person).
- Duration: `61.44s` (audio `section-06-morning-after` voiceover)
- Timing source: `voiceover/section-06-morning-after/section-06-word-timings.json`
  (whisper-tiny.en, generated 2026-07-02). Clamp the final scene's end to the real audio
  duration `61.44s`. Whisper mishearings do not affect timestamps: "Bresylia" =
  "Brasilia", "in Zoe" = "Enzo", "It's" = "its". One corrupt entry: the final token
  "Mars." carries a backward-jump timestamp (52.24-52.92); treat "Mars" as starting at
  Bruno's end (60.86) and clamp the beat to 61.44.
- Scene count: `8` (a visible change every ~4-8s). Scene 6.5 is a deliberate two-phase
  single scene (11.42s total, slightly over the ~10s base guide) following the S1.6
  precedent: the phase-B seat-map board covers ~85% of the base at 36.70, so no visible
  composition holds longer than ~7.7s.
- Scene-type rotation: 6.1 aftermath wide -> 6.2 hero-creature gag + vocab card -> 6.3
  price-tag evidence board -> 6.4 dated evidence gag board -> 6.5 two-phase map + magnifier
  hunt -> 6.6 wide party gag -> 6.7 fridge-schedule device + receipt motif -> 6.8 recovery
  glow-up finale.
- Mascot arc in this section: yawning comedown -> deadpan party-hat feeder (the script's
  ~S6 WIT-emotion target) -> impressed-then-suspicious -> signature deadpan at the buses ->
  detective with a giant magnifier -> dry "great venue" OK sign -> dead-inside feeder ->
  relieved nonchalant shrug at the recovery.

## Scenes

### Scene 6.1 - "Then the tournament ends. The fans fly home. And the stadiums stay."

- **Local time:** `0.00-4.20` (Then@0.00, ends@0.76, fans@1.70, fly@1.92, home@2.20,
  stadiums@3.02, stay@3.42)
- **Role:** the comedown cut - S5 ended on "the money leaves with the guests"; this scene
  is the literal morning after. Sets up the whole section's subject (the leftover
  building) and hands off to 6.2's "perfect phrase" tease.
- **Composition / layout:** full-bleed real photo base: the inside of an empty stadium at
  dawn - long curved rows of empty colored seats, soft grey-blue morning light, nobody
  anywhere. Horizon (top of the stand) ~30% y. A drooping string of party pennants hangs
  across the top of the frame (10-90% x, 4-16% y), one end detached and sagging to ~30% y
  at the left. WIT stands LEFT (0-36% x), bottom-anchored high (head ~14% from top, waist
  crop), mid-yawn. Three small SVG paper planes arc up and out toward the top-right
  (55-90% x, 15-35% y) on the "fly home" beat. A red handwritten stamp `STILL HERE.` with
  a short hand-drawn arrow pointing down at the seats lands mid-right (58-86% x, 38-52% y).
- **Elements:**
  - *Base (full-bleed):* real empty stadium bowl at dawn, rows of plastic seats in
    repeating color blocks, cool grey-blue light but bright (~0.8, no dark scrim); zero
    people, zero banners with real branding.
  - *Drooping pennant string (top band):* generated isolated element - a string of small
    triangle party pennants in plain teal/gold/red (no country flags, no logos), the line
    sagging in the middle, the left end torn loose and dangling. Reads "the party is
    over" in one glance.
  - *Paper planes (CSS/SVG, ~55-90% x):* three tiny white folded-paper-plane icons (drawn
    SVG, not emoji) that launch one after another along a rising arc and shrink toward
    the top-right corner - the fans flying home. Each trails a 1px dotted line.
  - *`STILL HERE.` stamp:* red handwritten stamp style, 3deg tilt, with a rough
    hand-drawn arrow pointing down at the empty seats.
- **Mascot:** pose `sleepy_yawning_open_mouth` (library); placement LEFT, ~2/5 frame
  height, waist crop (head, glasses, torso fully inside frame); facing slightly right
  toward the seats; expression: eyes-closed mid-yawn - the hangover after S1's euphoria.
- **On-screen text:** `STILL HERE.` (red handwritten stamp + arrow, mid-right, 3deg tilt)
  lands on stay@3.42. Nothing else - the emptiness is the message. All text sits above
  the bottom subtitle-safe zone.
- **Emotion:** quiet comedown; the guests left and someone has to deal with the house.
- **Insight / joke:** the one thing that cannot fly home is the 44,000-seat building.
- **Linkage / eye path:** WIT's yawn (left) -> up the sagging pennant line -> paper planes
  exiting top-right -> down to the `STILL HERE.` stamp over the seats.
- **Show-as-you-say:** base + WIT + sagging pennants visible from 0.00 (hard cut from S5,
  already morning-after); one extra pennant tears loose and drops (small impact) on
  ends@0.76; the three paper planes launch (hard-show, staggered ~0.3s apart) from
  fly@1.92 through home@2.66; `STILL HERE.` stamps (impact) on stay@3.42; hold to 4.20.
- **Sound:** thin wind + one distant echoing seat-clack under 0-2s (ducked); soft paper
  "fwip" per plane; stamp thud on stay@3.42. The S5 party audio is already gone - the
  quiet IS the cut.
- **Color / contrast:** cool grey-blue dawn base (~0.8 brightness); the colored seat rows
  give it life; the red stamp is the only saturated accent.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `stadium-empty-seats-dawn-1.jpg` | browse-real-photo | empty stadium interior at dawn, curved rows of colored seats, cool morning light, no people, no readable ads | full-bleed base | new |
| `pennant-string-drooping.png` | generate | string of small plain teal/gold/red triangle party pennants, line sagging, left end torn loose and dangling, isolated on transparent bg | top band 10-90% x, sag to ~30% y left | new |
| `sleepy_yawning_open_mouth.png` | pose | library pose, morning-after yawn | left, ~2/5 frame, waist crop | reuse (library) |

### Scene 6.2 - "English has a perfect phrase for what happens next: a 'white elephant'. A huge, expensive thing you cannot really use - but you must keep feeding."

- **Local time:** `4.26-12.36` (English@4.26, phrase@5.20, next@6.18, white@7.10,
  elephant@7.38, huge@8.10, expensive@8.66, cannot@9.44, use@10.08, must@11.02,
  keep@11.22, feeding@11.54)
- **Role:** the section's HERO scene and the learner-vocab beat: "white elephant" glossed
  on first use (learner rule) and made literal as a pet that eats money. Births the
  feeding-bowl motif that returns in 6.7. Links back to 6.1 ("what happens next") and
  forward to every stadium on the feeding schedule.
- **Composition / layout:** full-bleed real photo base: a wide empty grass field under a
  bright morning sky - the pet's yard. Horizon ~55% y. The elephant-stadium creature
  stands LEFT-CENTER (6-54% x, 24-88% y), facing right. Its red feeding bowl sits on the
  grass in front of it (46-62% x, 72-92% y). WIT stands RIGHT (62-100% x), GIANT (~1/2
  frame, hip crop, head ~10% from top), party hat on, pouring a scoop of gold coins down
  toward the bowl. A cream dictionary card floats TOP-RIGHT (56-94% x, 8-44% y), above
  WIT's head and clear of his face.
- **Elements:**
  - *Base (full-bleed):* real empty grass field / park lawn, morning sun, soft clouds,
    no people, no buildings with branding; bright (~0.85).
  - *Elephant-stadium creature (left-center, ~48% width):* generated hero - a hybrid
    creature: the body is a round concrete stadium bowl (arched openings around the
    ring, a thin white roof rim), but it has a grey elephant head with a long trunk,
    two big floppy ears, four stumpy elephant legs, and small sad droopy eyes. Concrete-
    grey skin with faint seat-row stripes visible inside the bowl rim. It looks heavy,
    sweet, and useless - a pet nobody asked for.
  - *Feeding bowl (front of creature, ~16% width):* generated - an oversized red plastic
    pet bowl with `MAINTENANCE` hand-painted in white on the front, heaped with a mound
    of gold coins and two folded banknote corners sticking out. (Standalone asset - it
    returns in 6.7.)
  - *Dictionary card (top-right):* cream paper card, dog-eared corner, handwritten
    header `white elephant (noun)` with a small hand-drawn elephant doodle; three gloss
    rows below, each with a tiny hand-drawn icon: row 1 `huge` (up-arrows icon), row 2
    `expensive` (money-tag icon), row 3 `you cannot really use it` (crossed-out hand
    icon); a fourth red row at the bottom: `...but you must keep FEEDING it` with
    `FEEDING` double-underlined.
- **Mascot:** pose `NEW: wit-party-hat-feeding-scoop.png` - WIT in a small teal cone
  party hat with yellow polka dots (elastic strap under the chin - the party ended but
  the hat stayed on), face fully deadpan (half-lidded eyes, flat mouth), both hands
  gripping a big metal feed scoop heaped with gold coins, tilted mid-pour. Placement
  RIGHT, GIANT ~1/2 frame, hip crop, facing left toward the creature; expression:
  dead-eyed acceptance while feeding money to a building.
- **On-screen text:** dictionary card header `white elephant (noun)` (black handwritten)
  on phrase@5.20; row `huge` on huge@8.10; row `expensive` on expensive@8.66; row
  `you cannot really use it` on cannot@9.44 (fully readable by use@10.08); red row
  `...but you must keep FEEDING it` on feeding@11.54. All on the card, top-right, never
  over WIT's face.
- **Emotion:** absurd tenderness - the creature is adorable and financially fatal.
- **Insight / joke:** the vocab lesson IS the punchline: the definition of "white
  elephant" is a feeding schedule. Maintenance money = pet food.
- **Linkage / eye path:** card header (top-right) -> creature pop (left) -> gloss rows
  read downward -> down WIT's pouring scoop into the `MAINTENANCE` bowl at the
  creature's feet. The coins physically connect the definition to the cost.
- **Show-as-you-say:** hard cut on English@4.26 (base + empty yard); card frame + header
  hard-show on phrase@5.20; the creature POPS in (impact - the section's biggest
  entrance, small dust puff at its feet) on elephant@7.38; gloss rows hard-show on
  huge@8.10 / expensive@8.66 / cannot@9.44; WIT + scoop hard-show on must@11.02; bowl
  hard-shows with him; the scoop tilts and a short arc of coins clatters into the bowl
  (impact) on feeding@11.54, coin trickle loops quietly until 12.36.
- **Sound:** low comedy tuba blat + dust "whumpf" on the creature's pop (7.38); paper
  tick per gloss row; coin clatter on feeding@11.54, settling into a soft tick-tick
  trickle (foreshadows the receipt printer).
- **Color / contrast:** bright green grass + blue sky base; grey creature reads huge
  against it; the red bowl and the red `FEEDING` row are the matched accents.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `grass-field-morning-1.jpg` | browse-real-photo | wide empty grass field or park lawn, bright morning sky, no people, no signage | full-bleed base | new |
| `elephant-stadium-pet.png` | generate | hybrid pet creature: round concrete stadium-bowl body with arched openings and thin roof rim, grey elephant head with trunk, floppy ears, stumpy legs, small sad droopy eyes, isolated on transparent bg | left-center, ~48% width | new (SECTION HERO) |
| `feeding-bowl-maintenance.png` | generate | oversized red plastic pet bowl, `MAINTENANCE` hand-painted in white on the front, heaped with gold coins and two folded banknotes, isolated on transparent bg | front of creature, ~16% width | new (returns in 6.7) |
| `wit-party-hat-feeding-scoop.png` | generate | NEW WIT pose: teal polka-dot cone party hat with chin strap, deadpan half-lidded face with flat mouth, both hands gripping a big metal feed scoop heaped with gold coins, tilted mid-pour, full body | right, ~1/2 frame, hip crop | new (script's S6 WIT beat; thumbnail candidate) |

### Scene 6.3 - "Brasilia built a stadium that cost at least five hundred fifty million dollars. Beautiful. Enormous. One problem: the city has no big football club."

- **Local time:** `12.36-20.50` (Brasilia@12.36, cost@13.64, least@14.04, $550@14.40,
  million@14.90, Beautiful@16.06, enormous@16.92, problem@17.78, club@19.66)
- **Role:** first case study - the glamour build-up (beautiful, enormous) that 6.4 will
  puncture with buses. The "at least" hedge stays visibly on the label (honesty rail).
- **Composition / layout:** full-bleed real photo base: a monumental modern stadium
  exterior in bright daylight - tall white concrete columns around a round bowl, heroic
  low angle, empty plaza in front. WIT stands LEFT (0-30% x), ~1/3 frame, chest crop.
  A big paper price tag hangs from the top edge on a string (28-52% x, 8-40% y),
  swinging in above WIT's head. A yellow tape-measure strip stretches horizontally
  mid-right (48-96% x, 46-54% y). A red `ONE PROBLEM` stamp hits TOP-RIGHT (64-92% x,
  10-26% y) with a handwritten line under it (64-94% x, 27-38% y).
- **Elements:**
  - *Base (full-bleed):* real modern stadium exterior, white columns, blue sky, bright
    (~0.85), no people, no visible club/sponsor branding (crop or choose clean angle).
  - *Price tag (hanging, ~22% width):* cream paper tag on a rough string from the top
    edge; handwritten: line 1 `AT LEAST` (red, underlined - the hedge is the headline),
    line 2 `$550,000,000` (big black). Swings 3deg and settles.
  - *Tape-measure strip:* a yellow measuring-tape graphic (CSS) that unrolls left-to-
    right across the columns with tick marks and the word `ENORMOUS` printed along it.
  - *`ONE PROBLEM` stamp + line:* red handwritten stamp, 4deg tilt; below it a black
    handwritten line `no big football club` with a small hand-drawn football (SVG)
    crossed out in red.
  - *Sparkle glints:* two 4-point star glints (CSS/SVG) popping on the columns during
    "Beautiful."
- **Mascot:** pose `mildly_surprised_hand_at_chin` (library); placement LEFT, ~1/3 frame,
  chest crop (head + glasses inside frame); facing right, up at the building; expression:
  small impressed "o" with a hint of doubt - admiring the thing he will soon pity.
- **On-screen text:** tag `AT LEAST` / `$550,000,000` (handwritten, cream tag) on
  least@14.04 with the number landing on $550@14.40; `ENORMOUS` (printed on the tape)
  on enormous@16.92; `ONE PROBLEM` (red stamp) on problem@17.78; `no big football club`
  (black handwritten + crossed-out ball) on club@19.66. All above the subtitle zone.
- **Emotion:** admiration curdling into suspicion.
- **Insight / joke:** the spec sheet is perfect except for the one line that matters -
  nobody local to play in it.
- **Linkage / eye path:** WIT looking up (left) -> price tag above him -> along the tape
  measure right -> up to the `ONE PROBLEM` stamp and its handwritten reason.
- **Show-as-you-say:** hard cut on Brasilia@12.36 (base + WIT already in frame); tag
  swings in (hard-show + pendulum settle) on least@14.04, the `$550,000,000` line
  inking on $550@14.40; two sparkle glints pop (small impacts) on Beautiful@16.06; tape
  unrolls (0.5s zip) on enormous@16.92; `ONE PROBLEM` stamps (impact) on problem@17.78;
  the reason line handwrites itself + ball crossed out on club@19.66.
- **Sound:** tag "fwip" + string creak; luxury "ting" per glint; tape-measure zip on
  16.92; stamp thud on 17.78; marker squeak on 19.66.
- **Color / contrast:** white concrete + blue sky, sun-bright; the cream tag and yellow
  tape carry the info; red stamp is the loudest object.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `stadium-modern-exterior-1.jpg` | browse-real-photo | monumental modern stadium exterior, white concrete columns, bright daylight, empty plaza, no people, no readable branding | full-bleed base | new |
| `mildly_surprised_hand_at_chin.png` | pose | library pose, impressed-but-doubtful | left, ~1/3 frame, chest crop | reuse (library) |

### Scene 6.4 - "So by 2015, its parking lot was being used... by city buses. Rows of them. The stadium was finally full. Full of buses."

- **Local time:** `20.50-29.00` (by@20.58, 2015@20.80, parking@22.46, used@23.46,
  By(buses)@24.20, buses@24.72, rows@25.36, them@25.76, finally@27.48, full@27.54,
  full-of@27.88, buses@28.32)
- **Role:** the section's biggest laugh line, staged as a DATED evidence gag. HONESTY
  RAILS: the year `2015` is stamped on screen for the whole beat, the framing is
  past-tense ("back in 2015"), and the stadium stands clean and intact in the
  background - never abandoned, never ruined. 6.8 will close the arc with its recovery.
- **Composition / layout:** full-bleed real photo base: a vast empty stadium parking lot -
  fresh asphalt, painted white stall lines receding to the back, the stadium's curved
  roofline visible along the top edge (intact, well-kept). Horizon ~28% y. A big date
  stamp sits TOP-LEFT (6-26% x, 8-24% y): small handwritten `back in` above a big red
  `2015`. Three rows of city buses slide in across the middle band (10-90% x, 34-62% y),
  each row slightly higher and smaller (perspective). A green `FINALLY FULL` stamp hits
  TOP-RIGHT (62-92% x, 10-24% y), with a red handwritten `...of buses.` scribbled under
  it (66-92% x, 25-33% y). WIT rises bottom-CENTER (34-66% x), closeup, shoulders crop.
- **Elements:**
  - *Base (full-bleed):* real empty stadium parking lot, white stall lines, daylight,
    the stadium's clean curved roof in the background top edge; bright (~0.8); no
    people, no license plates readable.
  - *Date stamp (top-left):* rubber-stamp style: tiny handwritten `back in` + big red
    `2015` in a rough rectangle, 3deg tilt. Stamps on 2015@20.80 and STAYS until the
    scene ends (the honesty anchor).
  - *Bus rows (middle band):* generated isolated element - ONE side-angle row of five
    identical plain city buses (white bodies, single teal stripe, no operator names, no
    plates), parked nose-to-tail. Render composites the SAME file three times as
    receding rows (scaled ~100% / 82% / 66%), sliding in from the right one per beat.
  - *`FINALLY FULL` stamp + scribble:* green stamp, 4deg tilt; the red handwritten
    `...of buses.` scrawls beneath it a beat later - the two-part punchline mirrors the
    narration's beat.
- **Mascot:** pose `deadpan_unimpressed_half_lidded` (library - the signature deadpan);
  placement bottom-CENTER closeup, ~1/3 frame, shoulders crop, head safely inside frame;
  facing camera dead-on while the buses park behind him; expression: flat-mouthed
  half-lidded "...great."
- **On-screen text:** `back in` + `2015` (stamp, top-left) on 2015@20.80; `FINALLY FULL`
  (green stamp, top-right) on full@27.54; `...of buses.` (red handwritten) on
  buses@28.32. Nothing in the lower subtitle zone.
- **Emotion:** deadpan absurdity - a $550M building winning at bus storage.
- **Insight / joke:** "full" was technically achieved; the script's `[beat]` before
  "Full of buses" gets real air (buses stop moving, half-second stillness, then the
  scribble lands).
- **Linkage / eye path:** date stamp (top-left) -> bus rows sliding in (middle,
  right-to-left motion) -> up to `FINALLY FULL` (top-right) -> its red correction ->
  down to WIT's dead stare (bottom-center).
- **Show-as-you-say:** hard cut on "so by"@20.50; date stamp (impact) on 2015@20.80;
  base + stadium roof visible from cut; WIT hard-shows on By@24.20 (arriving for the
  punchline); bus row 1 slides in (hard-show + airbrake settle) on buses@24.72; row 2 on
  rows@25.36; row 3 on them@25.76; all motion freezes 26.46-27.48 (the beat of air);
  `FINALLY FULL` stamps (impact) on full@27.54; `...of buses.` scribbles (impact) on
  buses@28.32; hold to 29.00.
- **Sound:** low diesel idle fading in from 24.20; an airbrake "pshhh" as each row
  settles; total silence in the 26.5-27.5 gap; stamp thud on 27.54; marker squeak +
  one final short airbrake on 28.32.
- **Color / contrast:** grey asphalt + white lines keep the frame calm; white-teal buses
  read instantly; red date + green stamp are the two anchors, deliberately at opposite
  corners.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `stadium-parking-lot-1.jpg` | browse-real-photo | vast empty stadium parking lot with painted stall lines, stadium roofline in background, daylight, no people, no readable plates | full-bleed base | new |
| `bus-row-parked.png` | generate | one row of five identical plain city buses, white with a single teal stripe, no operator names or plates, parked nose-to-tail, slight side angle, isolated on transparent bg | middle band; composited 3x as receding rows | new |
| `deadpan_unimpressed_half_lidded.png` | pose | library signature deadpan closeup | bottom-center, ~1/3 frame, shoulders crop | reuse (library) |

### Scene 6.5 - "Manaus built a stadium for about three hundred million dollars in the middle of the rainforest. After the Cup, some matches drew fewer than one thousand fans. In forty-four thousand seats. Every fan could have a private row."

- **Local time:** `29.00-40.42` (Manaus@29.00, stadium@29.72, about@30.24, $300@30.54,
  middle@32.12, forest@32.80, After@33.36, cup@33.86, matches@34.36, fewer@34.92,
  1,000@35.46-35.96, fans@35.96, in@36.34, 44@36.70, ,000@37.22, seats@37.68,
  Every@38.44, fan@38.72, private@39.72, row@39.72-40.42)
- **Role:** second case study, staged as a deliberate TWO-PHASE single scene (S1.6
  precedent): phase A drops a tiny stadium into an ocean of jungle; phase B is the
  seat-map takeover where a magnifying glass hunts for the fans. The base file persists
  11.42s but is ~85% covered from 36.70, so no visible composition holds longer than
  ~7.7s. Hedge "about" stays on the label.
- **Composition / layout:** Phase A (29.00-36.70): full-bleed real photo base - aerial
  view of dense green rainforest canopy with a brown river bend, no clearings with
  buildings. A small white stadium bowl drops into dead center (42-58% x, 42-62% y)
  with a paper tag swinging off it (55-72% x, 34-46% y). A handwritten margin note with
  a curved arrow sits top-left (8-34% x, 10-24% y). A counter card pops top-right
  (66-94% x, 10-26% y). Phase B (36.70-40.42): a huge white seat-map board slides up
  covering 7-93% x, 8-90% y (rainforest visible only at the edges); WIT rises RIGHT
  (62-100% x, ~2/5 frame, hip crop) holding a giant magnifying glass over the map's
  lower-left corner.
- **Elements:**
  - *Base (full-bleed):* real aerial rainforest canopy, saturated greens, a river bend
    for depth; bright (~0.8); no people, no structures.
  - *Tiny stadium (center, ~16% width):* generated - a small generic round white arena
    bowl seen from a 3/4 aerial angle, thin white lattice rim, clearly a stadium,
    clearly NOT any real venue's exact design. Drops in with a small leaf-puff (CSS
    particles, namespaced `.leafp`).
  - *Price tag (off the stadium):* cream paper tag, string to the stadium rim,
    handwritten `about $300,000,000` - "about" underlined in red (the hedge stays).
  - *Margin note (top-left):* black handwritten `actual middle of the rainforest` with
    a long curved hand-drawn arrow poking the stadium.
  - *Counter card (top-right):* small white ticket-stub-shaped card: printed header
    `FANS AT SOME MATCHES` and a big red odometer-style number that rolls down and
    stops at `< 1,000`.
  - *Seat-map board (phase B, ~85% of frame):* CSS/SVG evidence board - a top-down oval
    stadium seat map: thousands of tiny grey seat dots in concentric arcs, a green
    pitch rectangle in the middle, printed header `44,000 SEATS`. In the lower-left
    arc, a tiny cluster of ~12 red dots - the fans. One outer arc row highlights green
    with a small handwritten `every fan: a private row` beside it.
  - *Magnifier read-through:* through WIT's lens, the red-dot cluster appears enlarged
    (a circular zoom inset aligned to the lens).
- **Mascot:** pose `NEW: wit-magnifying-glass-search.png` - WIT leaning forward, both
  hands gripping a giant round magnifying glass (black frame, grey glass, long black
  handle), ONE eye comically enlarged through the lens, eyebrows up, small "o" mouth -
  full detective concentration. Placement RIGHT (phase B only), ~2/5 frame, hip crop,
  facing down-left over the map; expression: earnest hunt for an audience.
- **On-screen text:** tag `about $300,000,000` (handwritten, "about" red-underlined) on
  about@30.24-$300@30.54; `actual middle of the rainforest` (handwritten + arrow) on
  middle@32.12 (fully readable by forest@33.36); counter header + `< 1,000` (printed
  card, red number) rolling on fewer@34.92 and stopping on fans@35.96; board header
  `44,000 SEATS` on 44@36.70 (number completes on ,000@37.22, "SEATS" inks on
  seats@37.68); `every fan: a private row` (green handwritten) on private@39.72.
- **Emotion:** cosmic mismatch - a cathedral of seats, an audience that fits in a bus.
- **Insight / joke:** the search itself is the gag: you need a magnifying glass to find
  the crowd; the "private row" reframe makes emptiness sound like luxury.
- **Linkage / eye path:** phase A: margin note (top-left) -> arrow down to the tiny
  stadium -> tag -> counter (top-right). Phase B: board header (top) -> down the dot
  arcs -> WIT's lens on the red cluster -> the green private-row line beside it.
- **Show-as-you-say:** hard cut on Manaus@29.00 (base alone - one breath of pure
  jungle); tiny stadium drops (impact + leaf puff) on stadium@29.72; tag swings in
  (hard-show) on about@30.24; margin note handwrites on middle@32.12; counter card pops
  (hard-show) on fewer@34.92, number rolls and locks (impact) on fans@35.96; seat-map
  board slides up (0.5s ease, hard-show) on 44@36.70; header completes on seats@37.68;
  WIT + magnifier rise (hard-show) on Every@38.44; the lens zoom-inset reveals the red
  dots (impact + ding) on fan@38.72; green row highlight + `every fan: a private row`
  (impact) on private@39.72; hold to 40.42.
- **Sound:** jungle bird ambience under phase A (quiet); soft "whump" + leaf rustle on
  29.72; odometer clicks rolling to 35.96; paper slide on 36.70; a tiny triumphant
  "found them" ding on 38.72; marker squeak on 39.72.
- **Color / contrast:** phase A: saturated green ocean, tiny white stadium is the only
  bright object (the point). Phase B: clean white board, grey dots, one red cluster and
  one green row - the whole story in three colors.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `rainforest-aerial-1.jpg` | browse-real-photo | aerial view of dense rainforest canopy with a river bend, saturated green, no clearings or buildings, no people | full-bleed base | new |
| `stadium-bowl-tiny.png` | generate | small generic round white arena bowl, 3/4 aerial angle, thin white lattice rim, generic design (not any real venue), isolated on transparent bg | center, ~16% width | new |
| `wit-magnifying-glass-search.png` | generate | NEW WIT pose: leaning forward, both hands gripping a giant round magnifying glass with long black handle, one eye hugely enlarged through the lens, eyebrows up, small "o" mouth, full body | right (phase B), ~2/5 frame, hip crop | new |

### Scene 6.6 - "Another stadium started hosting weddings and children's birthday parties to survive. Happy birthday, Enzo. Great venue."

- **Local time:** `40.42-48.00` (Another@40.42, hosting@41.50, weddings@41.90,
  children's@42.72, birthday-parties@43.50, survive@44.36, Happy@45.34,
  birthday@45.36, Enzo@46.18 (whisper heard "in Zoe"), great@46.86, venue@47.16)
- **Role:** third case study - the survival pivot played sweet: a 40,000-seat venue
  doing a child's birthday. "Enzo" is fictional (script humor safety). Links the
  absurdity chain from buses -> empty rows -> party rentals, and tees up 6.7's "on the
  feeding schedule too".
- **Composition / layout:** full-bleed real photo base: a real football pitch at ground
  level, the white center circle and center spot in frame, empty stands blurred in the
  background. Horizon ~40% y. The birthday cake sits ON the center spot (44-60% x,
  54-80% y). Two small booking chips pop along the TOP band: `weddings` (14-34% x,
  8-20% y) and `birthday parties` (38-62% x, 8-20% y). A red handwritten note
  `...to survive.` hangs under the chips (38-60% x, 22-30% y). Pink icing-style cursive
  writes across the upper-right sky (58-94% x, 12-30% y): `Happy birthday, Enzo`. WIT
  peeks LEFT (0-30% x), closeup, shoulders crop. Four pastel CSS balloons drift up the
  far edges (namespaced `.blnp`).
- **Elements:**
  - *Base (full-bleed):* real grass pitch with white center circle, empty blurred
    stands behind, daylight, bright (~0.85), no people, no club marks.
  - *Birthday cake (center spot, ~14% width):* generated - a small round white-frosted
    birthday cake with pastel sprinkles and exactly ONE lit candle, sitting on a paper
    plate. The tiny cake on the huge center spot IS the composition's joke.
  - *Booking chips (top band):* two small white rounded booking-card chips, each with a
    drawn SVG icon: two interlocked gold rings + `weddings`; a balloon icon +
    `birthday parties`. Flat printed style, like a venue's rental menu.
  - *`...to survive.` note:* red handwritten, small, underlined once.
  - *Icing cursive:* `Happy birthday, Enzo` in thick pink piped-icing lettering with a
    slight sheen, written on as if squeezed from a piping bag.
  - *Balloons (CSS):* four pastel balloon circles with 1px strings, drifting slowly up
    the left and right edges - background decoration only.
- **Mascot:** pose `ok_hand_sign_content_closeup` (library); placement LEFT, ~1/3 frame,
  shoulders crop; facing camera with a slight angle toward the cake; expression:
  content half-lidded approval, OK-sign raised - the driest possible "Great venue."
- **On-screen text:** chip `weddings` on weddings@41.90; chip `birthday parties` on
  parties@43.50; `...to survive.` (red handwritten) on survive@44.36; `Happy birthday,
  Enzo` (pink icing cursive, writes left-to-right over ~1s) starting Happy@45.34;
  `great venue.` (small black handwritten, lower-right of the cake at ~62-78% x,
  70-78% y, above the subtitle zone) on venue@47.16.
- **Emotion:** absurd sweetness with a straight face.
- **Insight / joke:** the scale gap - a national monument moonlighting as a kids'
  party room; the deadpan `[deadpan]` read of "Happy birthday, Enzo" gets a matching
  deadpan OK-sign.
- **Linkage / eye path:** chips (top-left to top-center, reading order) -> red survival
  note under them -> down to the tiny cake on the center spot -> up-right along the
  icing greeting -> back to WIT's OK sign (left) for the button.
- **Show-as-you-say:** hard cut on Another@40.42 (base + balloons already drifting);
  chip `weddings` pops (hard-show) on weddings@41.90; chip `birthday parties` pops
  (hard-show) on parties@43.50; cake drops onto the center spot (impact - the candle
  flame flickers on) right after, on to@44.00; `...to survive.` handwrites on
  survive@44.36; icing cursive pipes on from Happy@45.34 (finishes ~46.4); WIT
  hard-shows on great@46.86; `great venue.` inks + a tiny glint on his OK sign (small
  impact) on venue@47.16; hold to 48.00.
- **Sound:** one weak, sad party-blower "pfff" on parties@43.50; a soft "fss" as the
  candle lights (~44.1); icing squeeze sound under the cursive; tiny "ting" on the OK
  glint at 47.16.
- **Emotion note:** all edge stays on the economics; the party itself is depicted
  affectionately (no mockery of families or the country).
- **Color / contrast:** green pitch + white circle base; pastel chips and balloons keep
  it light; the pink icing line is the warmest element; red survival note is the one
  sharp accent.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `pitch-center-circle-1.jpg` | browse-real-photo | real football pitch at ground level, white center circle and spot, empty blurred stands behind, daylight, no people, no club marks | full-bleed base | new |
| `birthday-cake-one-candle.png` | generate | small round white-frosted birthday cake with pastel sprinkles and one lit candle, on a paper plate, isolated on transparent bg | on the center spot, ~14% width | new |
| `ok_hand_sign_content_closeup.png` | pose | library pose, dry OK-sign approval | left, ~1/3 frame, shoulders crop | reuse (library) |

### Scene 6.7 - "And Cape Town's stadium lost millions every year for about a decade. It is on the feeding schedule too."

- **Local time:** `48.00-53.80` (Cape@48.14, Town@48.34, Stadium@48.72, lost@49.04,
  millions@49.48, year@50.22, decade@51.20, feeding@52.56, schedule@52.78, too@53.28)
- **Role:** the feeding metaphor becomes a household chore: the fridge schedule from the
  script's visual goal, with Cape Town as the REQUIRED last entry, printing straight
  onto the video's receipt motif (the section's receipt gag). Pays off 6.2's bowl.
- **Composition / layout:** full-bleed real photo base: a bright real kitchen (counter,
  tiles, window light), people-free. A white fridge stands LEFT-CENTER (14-46% x,
  16-92% y) with colorful magnet dots (CSS) pinning a cream schedule card to its door
  (18-42% x, 24-62% y). The feeding bowl (REUSED file) sits on the floor at the
  fridge's base (30-46% x, 80-95% y - decorative floor zone, not cue-critical). The
  receipt (REUSED file) snakes out from under the fridge door across the floor toward
  the lower-right (44-88% x, 68-88% y), its printed gag line sitting at ~70% y, above
  the subtitle zone. WIT stands RIGHT (58-100% x), GIANT ~1/2 frame, hip crop.
- **Elements:**
  - *Base (full-bleed):* real bright kitchen, white cabinets, tiled wall, morning
    window light (~0.85); no people, no appliance brand marks readable.
  - *Fridge (left-center, ~30% width):* generated - a plain white two-door fridge,
    slightly rounded corners, clean door (no brand), a few colorful round magnets
    already on it. Blank enough that the schedule card and CSS text carry the scene.
  - *Feeding schedule card (on the fridge door):* cream paper card (CSS text so the
    entries can reveal on cue): printed header `FEEDING SCHEDULE` with a small
    hand-drawn elephant doodle (callback to 6.2); two greyed handwritten rows already
    filled: `BRASILIA - bus era - fed`, `MANAUS - private rows - fed`; the LAST entry
    handwrites itself in red: `CAPE TOWN - millions/yr - 10 years` (the exact required
    wording).
  - *Receipt (floor, reused motif):* `receipt-endless-roll.png` unspooling from under
    the fridge door; CSS text prints one item line in receipt type:
    `1x WHITE ELEPHANT (FEEDING, ANNUAL) ......... $???` - the `???` scrawled in red
    handwriting (the required handwritten question mark).
  - *Feeding bowl (floor, reused):* the same red `MAINTENANCE` bowl from 6.2, now
    half-empty - the feeding continues.
- **Mascot:** pose `exhausted_dead_inside_eye_bags` (library); placement RIGHT, GIANT
  ~1/2 frame, hip crop, head ~10% from top; facing left at the fridge; expression: grey
  dead-inside eye bags - a decade of feeding duty in one face.
- **On-screen text:** schedule header `FEEDING SCHEDULE` + greyed rows visible from the
  cut; red last entry `CAPE TOWN - millions/yr - 10 years` handwrites across
  Town@48.34 (name), millions@49.48 (`millions/yr`), decade@51.20 (`10 years`); receipt
  line `1x WHITE ELEPHANT (FEEDING, ANNUAL) ......... $???` prints on feeding@52.56
  with the red `???` scrawling on too@53.28.
- **Emotion:** domestic dread - the white elephant lives here now, and it eats yearly.
- **Insight / joke:** a national stadium reduced to a chore on the fridge, between
  grocery lists; the bill line literally cannot state a number (`$???`).
- **Linkage / eye path:** fridge card rows (left, reading down to the new red entry) ->
  down the fridge to the bowl -> along the receipt to the printing `$???` -> up to
  WIT's exhausted face (right). The receipt physically connects schedule to bill.
- **Show-as-you-say:** hard cut on "and Cape"@48.00 (base + fridge + card + greyed rows +
  bowl + WIT all present - a lived-in kitchen); red entry handwrites in three strokes:
  `CAPE TOWN` on Town@48.34 (hard-show), `- millions/yr` on millions@49.48 (hard-show),
  `- 10 years` on decade@51.20 (small impact - the pen presses harder); the receipt
  jolts forward and PRINTS the white-elephant line (impact + printer tick, the motif
  SFX) on feeding@52.56; red `???` scrawls (impact) on too@53.28; hold to 53.80.
- **Sound:** low fridge hum under the whole scene; marker squeak per handwritten stroke;
  the signature receipt printer tick-tick on 52.56; a heavier squeak for the `???`.
- **Color / contrast:** bright white kitchen keeps it honest and readable; the red
  schedule entry and red `???` are the twin accents; the warm white receipt pops
  against the floor tiles.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `kitchen-bright-1.jpg` | browse-real-photo | bright real kitchen with counter, tiled wall, window light, no people, no readable appliance brands | full-bleed base | new |
| `fridge-white-magnets.png` | generate | plain white two-door fridge, no brand, clean door with a few colorful round magnets, isolated on transparent bg (door kept blank so the CSS schedule card sits on top) | left-center, ~30% width | new |
| `receipt-endless-roll.png` | reuse | the video's receipt motif, unspooling from under the fridge; CSS prints the white-elephant item line | floor, 44-88% x, toward lower-right | reuse (S1 motif) |
| `feeding-bowl-maintenance.png` | reuse | the red MAINTENANCE bowl from 6.2, now half-empty | floor at fridge base | reuse (6.2) |
| `exhausted_dead_inside_eye_bags.png` | pose | library pose, decade-of-feeding fatigue | right, ~1/2 frame, hip crop | reuse (library) |

### Scene 6.8 - "To be fair, some of them recover. The Brasilia stadium does big concerts now. It only took ten years. And Bruno Mars."

- **Local time:** `53.80-61.44` (fair@54.18, recover@54.90, Brasilia@56.06,
  concerts@57.62, now@57.92, only@58.98, took@59.32, 10@59.50, years@59.86,
  Bruno@60.60, Mars@~60.86 (JSON's "Mars." timestamp is corrupt - a backward jump to
  52.24 - so the beat is pinned to Bruno@60.60 and its end); scene end CLAMPED to the
  real audio duration `61.44` (whisper's last-word end is unreliable here)
- **Role:** the REQUIRED honesty beat: the recovery. The section must not end on decay -
  the same Brasilia stadium from 6.3/6.4 comes back to life under concert lights.
  "Bruno Mars" is a neutral factual reference (he really played it, 2024): shown ONLY as
  lights, confetti, a microphone, and a name tag on a timeline - never a person. Hands
  off to S7's "so why do countries still fight?".
- **Composition / layout:** full-bleed real photo base: a concert stage rig at night -
  colorful magenta/violet light beams cutting through haze, an empty lit stage, zero
  people. A white ribbon banner floats TOP-CENTER (30-70% x, 6-16% y). A green
  handwritten line sits under it (32-68% x, 18-26% y). A gold microphone on a stand
  rises stage-center-LEFT (18-34% x, 40-86% y). A hand-drawn timeline strip runs
  mid-frame (14-70% x, 56-64% y): `2014` at the left end, `2024` at the right, ten tick
  marks between; the 2024 end sprouts a star + tag. WIT stands CENTER (32-68% x), GIANT
  ~1/2 frame, hips crop, head ~9% from top - between banner above and timeline below,
  covering neither.
- **Elements:**
  - *Base (full-bleed):* real concert stage lighting rig at night, magenta/violet
    beams, haze, empty stage, no people, no performer branding; graded bright enough
    to read (~0.7 - the brightest of the dark bases, beams carry the light).
  - *Ribbon banner (top-center):* clean white ribbon with printed `TO BE FAIR...` -
    the honesty device gets its own furniture.
  - *Green line:* handwritten `some of them recover` with a single underline.
  - *Gold microphone (left, ~10% width):* generated - a classic round-head microphone
    in polished gold on a black mic stand, one specular glint - "big concerts" as an
    object, no person implied at it.
  - *Timeline strip:* hand-drawn black line with ten tick marks that draw left-to-right
    fast; `2014` and `2024` handwritten at the ends; above the middle, red handwritten
    `only ten years` with cheeky quote marks around `only`; the 2024 tick sprouts a
    gold star with a small printed tag `2024: Bruno Mars` (factual name text only -
    no face, no figure).
  - *Confetti burst (CSS, namespaced `.cfp6`):* one gold confetti pop at the very end -
    the party is finally, honestly, earned.
- **Mascot:** pose `shrug_both_hands_up_smile` (library); placement CENTER, GIANT ~1/2
  frame, hips crop; facing camera; expression: relaxed smile, both palms up - "it
  worked out. Eventually." The nonchalant shrug IS the "It only took ten years" read.
- **On-screen text:** `TO BE FAIR...` (printed, white ribbon banner) on fair@54.18;
  `some of them recover` (green handwritten, underlined) on recover@54.90; `only ten
  years` (red handwritten, quotes on `only`) on years@59.86; timeline year labels
  `2014` / `2024` as the strip draws from took@59.32; tag `2024: Bruno Mars` (small
  printed tag on the gold star) on Bruno@60.60. All text above the subtitle zone and
  clear of WIT's face.
- **Emotion:** genuine relief with an eyebrow raised - happy ending, absurd timeline.
- **Insight / joke:** the recovery is real AND the joke: a decade plus a global pop tour
  is what it takes to make the purchase useful. Honesty rails satisfied: not abandoned,
  recovery on screen, dated, factual.
- **Linkage / eye path:** banner (top) -> green line under it -> WIT's open-palm shrug
  (center) -> down to the timeline drawing left-to-right -> the gold star + name tag at
  2024 -> the mic glowing left as the lights flare.
- **Show-as-you-say:** hard cut on "to be"@53.80 (base beams sweeping slowly, mic
  already on stage); `TO BE FAIR...` banner unfurls (hard-show) on fair@54.18; green
  line handwrites on recover@54.90; the beams flare brighter + mic glint (small impact)
  on concerts@57.62-now@57.92; WIT hard-shows on only@58.98 (arriving for the dry
  line); timeline strip draws its ticks rapidly from took@59.32 to years@59.86; `only
  ten years` inks (impact) on years@59.86; gold star + `2024: Bruno Mars` tag pop
  (impact) on Bruno@60.60; one gold confetti burst + full beam flare (impact) at 60.86
  (Bruno's word end - the corrupt "Mars" stamp is not used); hold bright to 61.44, hard
  cut out to S7.
- **Sound:** a warm synth-pad swell rising from 53.80 (no crowd - the honesty: lights,
  not hype); light-whoosh per beam flare; quick tick-tick-tick as the timeline draws;
  confetti pop at 60.86; everything cuts dead at 61.44.
- **Color / contrast:** magenta/violet beams on near-black, the gold mic and gold star
  are the warm anchors; white banner reads first; WIT's white body glows center - the
  section ends on its brightest, warmest frame.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `concert-stage-lights-1.jpg` | browse-real-photo | concert stage lighting rig at night, magenta/violet beams through haze, empty stage, no people, no performer or brand marks | full-bleed base | new |
| `microphone-stand-gold.png` | generate | classic round-head gold microphone on a black mic stand, polished with one specular glint, isolated on transparent bg | stage-center-left, ~10% width | new |
| `shrug_both_hands_up_smile.png` | pose | library pose, nonchalant relieved shrug | center, ~1/2 frame, hips crop | reuse (library) |

## Section Asset Summary

| Filename | Type | First scene | Reused in | Notes |
|---|---|---|---|---|
| `elephant-stadium-pet.png` | generate | 6.2 | - | SECTION HERO - stadium-bodied elephant pet; thumbnail candidate |
| `feeding-bowl-maintenance.png` | generate | 6.2 | 6.7 | red MAINTENANCE bowl; the section's secondary motif object |
| `wit-party-hat-feeding-scoop.png` | generate (NEW pose) | 6.2 | - | the script's S6 WIT arc beat (party hat + deadpan + feeding); thumbnail candidate |
| `wit-magnifying-glass-search.png` | generate (NEW pose) | 6.5 | - | detective hunt for fans on the seat map |
| `pennant-string-drooping.png` | generate | 6.1 | - | party's-over prop, plain colors, no country flags |
| `bus-row-parked.png` | generate | 6.4 | - | one row of 5 plain buses; composited 3x for "rows of them" |
| `stadium-bowl-tiny.png` | generate | 6.5 | - | generic tiny arena, deliberately not any real venue's design |
| `birthday-cake-one-candle.png` | generate | 6.6 | - | one candle, on the center spot |
| `fridge-white-magnets.png` | generate | 6.7 | - | blank door - CSS schedule card carries the text |
| `microphone-stand-gold.png` | generate | 6.8 | - | "big concerts" object; no person implied |
| `receipt-endless-roll.png` | reuse | 6.7 | - | VIDEO MOTIF (born S1.3); prints `1x WHITE ELEPHANT (FEEDING, ANNUAL) ......... $???` |
| `stadium-empty-seats-dawn-1.jpg` | browse-real-photo | 6.1 | - | empty seats at dawn; no people |
| `grass-field-morning-1.jpg` | browse-real-photo | 6.2 | - | the pet's yard |
| `stadium-modern-exterior-1.jpg` | browse-real-photo | 6.3 | - | monumental white columns, clean of branding |
| `stadium-parking-lot-1.jpg` | browse-real-photo | 6.4 | - | stadium roofline visible + intact (honesty: not abandoned) |
| `rainforest-aerial-1.jpg` | browse-real-photo | 6.5 | - | canopy + river bend, no structures |
| `pitch-center-circle-1.jpg` | browse-real-photo | 6.6 | - | center circle carries the cake gag |
| `kitchen-bright-1.jpg` | browse-real-photo | 6.7 | - | bright, people-free, brand-free |
| `concert-stage-lights-1.jpg` | browse-real-photo | 6.8 | - | beams + haze, explicitly people-free |
| library poses (6) | pose | 6.1/6.3/6.4/6.6/6.7/6.8 | - | sleepy_yawning_open_mouth, mildly_surprised_hand_at_chin, deadpan_unimpressed_half_lidded, ok_hand_sign_content_closeup, exhausted_dead_inside_eye_bags, shrug_both_hands_up_smile |

## Approval Checks

- each scene picturable from text alone: yes - every scene specifies base, element
  positions in %, z-order by description, mascot pose/scale/crop/facing, exact text,
  and per-word timing.
- ~one scene per sentence, scene-types varied: yes - 8 scenes over 61.44s; rotation
  runs aftermath wide -> creature gag + vocab card -> price-tag board -> dated evidence
  gag -> two-phase map hunt -> party gag -> fridge device + receipt -> recovery finale.
  Scene 6.5 is a declared two-phase single scene (11.42s; visible composition changes
  fully at 36.70, so no visible frame holds longer than ~7.7s).
- every scene has a real/real-looking base: yes - 8 fresh people-free, brand-free photo
  bases, one per scene, none reused, all bright (~0.7-0.85, no heavy dark scrims).
- mascot big/high with a specific pose+expression per scene: yes - 8 distinct poses
  (6 library + 2 new), no repeats in-section, side rotation L-R-L-C-R-L-R-C (never the
  same side twice in a row), giant ~1/2-frame on the emotional beats (6.2, 6.7, 6.8),
  minimum ~1/3 elsewhere, always anchored high (head + glasses + torso inside frame).
- show-as-you-say timeline present per scene: yes - every entrance pinned to a real
  word@time from the section JSON, each marked hard-show or impact; final scene end
  clamped to 61.44 and the corrupt "Mars." timestamp explicitly bypassed.
- every asset has type + description + filename + layout: yes - per-scene tables plus
  the summary table above.
- repeated subjects reuse the same filename: yes - `receipt-endless-roll.png` (shared
  registry, untouched name), `feeding-bowl-maintenance.png` (6.2 -> 6.7), and the bus
  row composited 3x from one file.
- public figures handled as caricature/parody, punching up: yes by absence - no real
  people appear; "Bruno Mars" exists only as factual text on a dated timeline tag plus
  lights/mic/confetti (script's real-name rule); "Enzo" is fictional; all edge aims at
  the incentive system, never a nation or its fans.
- no image-generation prompts written here: yes - descriptions only; prompts are
  visual-implement's job.
- in sync with master `04-visual-plan.md`: pending - this section file is written
  first; the master-assembler must paste this block into the master's "All Sections"
  and update the Section Index row for Section 6 (this file does not edit the master).
- section honesty rails (script approval checks): yes - "white elephant" glossed on
  first use (6.2 dictionary card); the bus story is past tense with `back in 2015`
  stamped on screen for the whole beat and the stadium shown intact (6.4); the stadium
  is never depicted as abandoned or demolished anywhere; the recovery beat is a full
  scene (6.8) with `TO BE FAIR...` banner and dated timeline; cost hedges kept on
  labels (`AT LEAST $550,000,000`, `about $300,000,000`, `millions/yr`); the required
  receipt line prints with a handwritten `???` (6.7); the required fridge entry reads
  exactly `CAPE TOWN - millions/yr - 10 years` (6.7).
