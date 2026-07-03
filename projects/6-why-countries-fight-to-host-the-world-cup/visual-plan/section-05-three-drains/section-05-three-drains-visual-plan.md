# Section 5 Visual Plan - The Three Drains

Video: `Why Countries Fight to Host the World Cup (and Lose Billions)`
Section: `Section 5: The Three Drains`
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

- Section goal: answer the obvious objection ("but fans spend money!") by conceding the
  true half, then showing WHERE the boom goes - down three labeled drains (substitution,
  crowding out, leakage), each drain visibly swallowing money ON its spoken word - and
  land the section mini-payoff: the party happens in your house, the money leaves with
  the guests.
- Duration: `55.851s` (audio `section-05-three-drains-david23-am_eric-0.81.mp3`)
- Timing source: `voiceover/section-05-three-drains/section-05-word-timings.json`
  (whisper-tiny.en, generated 2026-07-02; monotonic). Clamp the final scene's end to the
  real `55.851s` - whisper's last word ("guests") overshoots to 57.04. Whisper
  mishearings do not affect timestamps: "any W money" = "NEW money" (NEW@11.88), "$100" =
  "hundred dollars"@15.52, "100." = "a hundred"@17.86, "20%," = "twenty percent"@38.16,
  "towards" = "toward"@50.82.
- Scene count: `7` (a visible change every ~4-9s; scene 5.5 runs 10.56s as a deliberate
  two-phase evidence board with a spotlight shift mid-scene, so the frame still changes
  every ~4s inside it)
- Scene-type rotation: 5.1 wide gag two-phase (objection -> reveal) -> 5.2 mechanism
  board / object hero -> 5.3 wide gag (cinema) -> 5.4 mechanism board -> 5.5 evidence
  board two-phase -> 5.6 mechanism board / wide gag -> 5.7 payoff board (quiet button)
- Mascot arc in this section: cocky minister act (WIT plays the role) -> lecturing
  professor -> dry smirk at the seat gag -> local hiding behind the edge -> dismayed
  sweat at the -20% card -> full panic, hands on head, as the money flies to Zurich ->
  dead-inside resignation at the door (feeds the master arc note "horror at drains")
- Section running gag: `money-pile-party.png` (the "boom") is born in 5.1 at full size,
  then returns as a corner widget at ~70% (5.2), ~45% (5.4), and ~20% ghost (5.6) - the
  pile visibly shrinks as each drain drinks; by 5.7 it is gone and the last banknotes
  walk out the door. WIT watches it shrink; the drain gurgle SFX is the section's
  signature sound.

## Scenes

### Scene 5.1 - ""But wait," says every tourism minister. "The fans come! They spend real money!" True. Fans do come. They do spend. So where does the boom go? Down three drains."

- **Local time:** `0.00-9.44` (wait@0.34, minister@1.70, fans@2.78, money@3.98, True@4.56,
  come@5.54, spend@6.36, boom@7.38, Down@8.18, drains@8.68)
- **Role:** two-phase cold open. Phase A (0.00-4.56): the objection, performed by WIT in
  costume as the tourism minister. Phase B (4.56-9.44): the narrator concedes the true
  half with green checks, then the floor answers the question - three drains slam into
  the pavement under the money pile. Links back to S4's "one side gets the revenue" and
  forward: each numbered drain gets its own scene (5.2, 5.4, 5.6).
- **Composition / layout:** full-bleed real photo base: a bright, people-free city plaza
  strewn with confetti after a street party (ground fills the lower half; horizon ~55%).
  Minister-WIT stands LEFT (2-38% x, knees cropped at bottom edge, head ~14% from top).
  A white comic speech bubble top-center-right (42-86% x, 6-32% y), tail pointing to
  WIT's megaphone. The money pile drops center-right (48-78% x, 45-75% y) on its word.
  Three drain grates slam into the pavement in a bottom row (grate 1 at 14-36% x, grate 2
  at 40-62% x, grate 3 at 66-88% x; all 72-93% y), each with a small handwritten number
  tag (`1`, `2`, `3`) floating just above at ~66-70% y. Z-order: base < grates < pile <
  WIT < bubble/tags.
- **Elements:**
  - *Base (full-bleed):* real empty city plaza or pedestrian street covered in colorful
    confetti and a few fallen paper streamers, bright daylight (~0.8 brightness), no
    people, no flags, no shop brands. The morning-after party floor gives the drains a
    natural home.
  - *Speech bubble (top-center-right):* classic white comic bubble, thin black outline,
    slight 2deg tilt. Text builds in three handwritten lines (see On-screen text). Two
    fat green check stamps (drawn SVG checks, not emoji) land ON the bubble's claim lines
    during phase B, plus a green handwritten `TRUE` stamp on the bubble's top edge.
  - *Money pile (center-right, ~26% width):* the section's running-gag hero - a mound of
    parody banknotes (generic teal-and-cream "play money", no real currency design) with
    confetti bits stuck on top; drops in with a bounce and a small confetti puff. A tiny
    handwritten tag `the "boom"` hangs off its left side.
  - *Three drain grates (bottom row, each ~20% width):* the same generated ornate
    cast-iron grate composited three times - round, heavy, slightly menacing storm-drain
    grate with thick bars and a blank curved plate at its top edge (plate text stays
    empty here; the names are revealed in each drain's own scene). Each slams in with
    dust kick and a number tag above it.
- **Mascot:** pose `NEW: wit-minister-sash-shouting.png` - WIT as the tourism minister:
  plain dark suit jacket, a wide diagonal pageant-style sash (blank teal, no country
  colors), one hand raised holding a small white megaphone, mouth wide open mid-shout,
  eyebrows indignant. Placement LEFT, scale ~2/5 frame height, knees cropped, facing
  right toward the bubble and pile. He stays frozen mid-shout through phase B while the
  checks and drains undercut him - the frozen protest IS the gag.
- **On-screen text:** bubble line 1 `But wait -` (black handwritten) on wait@0.34; small
  handwritten tag under WIT `every tourism minister` on minister@1.70; bubble line 2
  `The fans come!` on fans@2.78; bubble line 3 `They spend real money!` on real@3.72.
  Phase B: green `TRUE` stamp on True@4.56; green check on line 2 on come@5.54; green
  check on line 3 on spend@6.36; tag `the "boom"` with the pile on boom@7.38; number tags
  `1` `2` `3` with the grates at 8.68/8.98/9.24.
- **Emotion:** cocky official confidence, punctured in real time - concession, then dread.
- **Insight / joke:** the narrator AGREES with the minister (both checks are real), and
  the floor still opens - being right about fans coming does not save the boom.
- **Linkage / eye path:** WIT's megaphone (left) -> up the bubble tail to the claim ->
  checks land, eye drops with the falling pile (center-right) -> down to the three grates
  reading `1 2 3` left-to-right, ready for the section to walk them.
- **Show-as-you-say:** base + minister-WIT visible from 0.00 (cold open mid-shout);
  bubble frame pops (impact, boing) on wait@0.34; `every tourism minister` tag hard-shows
  on minister@1.70; bubble lines 2-3 hard-show on fans@2.78 / real@3.72; `TRUE` stamp
  (impact) on True@4.56; check stamps (impact, thud) on come@5.54 and spend@6.36; money
  pile drops (impact, bounce + confetti puff) on boom@7.38; low rumble starts on
  Down@8.18; three grates slam in staggered (impact x3) at drains@8.68, 8.98, 9.24 with
  number tags; hard cut out at 9.44.
- **Sound:** distant festive street ambience under phase A (ducked); megaphone squawk on
  wait@0.34; two stamp thuds; soft heavy thump for the pile; rumble + three metal clangs
  for the grates; the first faint drain gurgle teased under the cut.
- **Color / contrast:** bright confetti multicolor on warm gray pavement; teal-cream pile
  is the brightest object; the iron grates are the only dark, cold shapes in frame -
  three holes in a party.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `confetti-plaza-1.jpg` | browse-real-photo | bright people-free city plaza or pedestrian street strewn with confetti and paper streamers after a party, daylight, no brands/flags | full-bleed base | new |
| `wit-minister-sash-shouting.png` | generate | NEW WIT pose: dark suit jacket + blank teal pageant sash, small white megaphone raised, mouth wide open mid-shout, indignant brows - the tourism minister act | left, ~2/5 frame, knees cropped | new (this section only) |
| `money-pile-party.png` | generate | mound of parody teal-and-cream banknotes ("play money", no real currency design) with confetti bits on top, isolated, transparent bg | center-right ~26% width | new (SECTION RUNNING GAG - shrinks in 5.2/5.4/5.6) |
| `drain-grate-ornate.png` | generate | ornate round cast-iron storm-drain grate, thick menacing bars, blank curved name plate at top edge, slight 3D depth, isolated, transparent bg (plate text-free so CSS labels each drain later) | bottom row, 3 copies ~20% width each | new (reused 5.2/5.4/5.6) |

### Scene 5.2 - "Drain one: substitution. Locals do not spend NEW money during the Cup. They move money they already had."

- **Local time:** `9.44-15.36` (drain@9.44, one@9.68, substitution@10.24, locals@11.06,
  not@11.44, NEW@11.88, Cup@13.24, move@13.94, already@14.60, had@14.94)
- **Role:** mechanism board #1 - the speak-the-mechanism beat for substitution. The first
  numbered drain from 5.1 returns huge and drinks its first bills ON its word. Links
  forward: the cinema gag in 5.3 is this mechanism made literal.
- **Composition / layout:** full-bleed real photo base: a giant open leather wallet
  shot close-up on a table, bills visible in its fold (bright, ~0.8). The drain grate
  (REUSED file) sits LARGE center-left (16-52% x, 44-92% y), as if installed in the
  wallet's leather - a drain in your wallet. Its plate carries the drain name (CSS,
  revealed on the word). Three single banknotes tip out of the wallet fold and slide
  down the grate on substitution@10.24. WIT GIANT on the RIGHT (56-100% x, head ~10%
  from top, hips cropped). Cross-out device top-LEFT (6-42% x, 8-26% y). The shrunken
  money pile floats top-center (44-58% x, 5-18% y) at ~70% of its 5.1 size, tiny tag
  attached. Z-order: base < grate < sliding bills < pile < WIT < text devices.
- **Elements:**
  - *Base (full-bleed):* real worn brown leather wallet, open, photographed close so its
    fold crosses the frame diagonally; a few generic bill edges peek out; warm bright
    light, no logos, no cards with names.
  - *Drain grate (center-left, ~36% width):* same grate file, now huge; its blank plate
    gets a handwritten label in two steps (see On-screen text). A faint dark suction
    shading under the bars (CSS radial) sells the "down" on the swallow beat.
  - *Sliding bills (x3):* the single crisp parody banknote composited three times,
    staggered; they tip over the wallet fold's edge and slide bar-ward one after another
    during 10.24-11.06, the last one flipping vertical as it drops in.
  - *Cross-out device (top-left):* handwritten `NEW money?` in black; a fat red X
    scribbles across `NEW` on its word; then `moved money` stamps beneath in darker
    teal, and a red underline scrubs under it on "already had".
  - *Money pile widget (top-center):* the 5.1 pile at ~70% scale, tag `the "boom"`
    now smaller - the first visible shrink.
- **Mascot:** pose `lecturing_finger_raised_eyes_closed` (library); placement RIGHT,
  GIANT ~1/2 frame height, hips cropped, head high inside frame; facing left toward the
  grate; expression: eyes-closed professor delivering the definition - calm authority
  while the wallet drains.
- **On-screen text:** plate line `DRAIN 1:` (handwritten, chalk-white on the grate plate)
  on drain@9.44; plate word `SUBSTITUTION` stamps (impact) on substitution@10.24;
  `NEW money?` hard-shows on not@11.44; red X across `NEW` scribbles on NEW@11.88;
  `moved money` stamps on move@13.94; red underline scrubs on already@14.60-had@15.36.
- **Emotion:** clinical "let me show you" - the first cold mechanism after the party.
- **Insight / joke:** the drain is installed inside the viewer's own wallet - substitution
  is not the city losing money, it is YOUR money changing exits.
- **Linkage / eye path:** plate label (center-left) -> bills sliding down into the bars ->
  up to WIT's raised finger (right) -> his finger points toward the top-left cross-out
  where the definition is corrected -> pile widget above quietly smaller.
- **Show-as-you-say:** hard cut on drain@9.44 with base + grate + `DRAIN 1:` plate + pile
  widget already placed (hard-show); `SUBSTITUTION` stamps (impact) on substitution@10.24
  as the three bills tip and slide down the grate 10.24-11.06 (first full drain gurgle);
  WIT hard-shows on locals@11.06; `NEW money?` on not@11.44 (hard-show); red X (impact,
  marker squeak) on NEW@11.88; `moved money` stamp (impact) on move@13.94; underline
  scrub on already@14.60; hold, cut at 15.36.
- **Sound:** deep drain gurgle-slurp as the bills go down (the section's signature SFX,
  first full use); paper slither; marker squeak on the X; soft stamp on `moved money`.
- **Color / contrast:** warm leather browns; cold iron grate is the dark anchor; red X
  and red underline are the only reds; teal bills pop against the brown.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `wallet-open-1.jpg` | browse-real-photo | worn brown leather wallet open in close-up, generic bill edges in the fold, warm bright light, no logos/cards | full-bleed base | new |
| `drain-grate-ornate.png` | reuse | the drain grate, huge, plate labeled by CSS | center-left ~36% width | reuse (5.1) |
| `banknote-single-crisp.png` | generate | one crisp parody teal-and-cream banknote, generic ornament, no real currency design, isolated, transparent bg | 3 staggered copies sliding into the grate | new (reused 5.4/5.5/5.6) |
| `money-pile-party.png` | reuse | the boom pile at ~70% scale - first shrink | top-center widget | reuse (5.1) |
| `lecturing_finger_raised_eyes_closed.png` | pose | library professor pose, eyes-closed definition delivery | right, ~1/2 frame giant, hips crop | reuse (library) |

### Scene 5.3 - "The hundred dollars you spend on a match ticket is a hundred you do not spend at the cinema. The city did not get richer. The money just changed seats."

- **Local time:** `15.36-23.36` (hundred dollars@15.52, match@16.82, ticket@16.98,
  a hundred@17.86, cinema@19.28, city@20.14, richer@20.94, just@21.88, changed@22.16,
  seats@22.54)
- **Role:** the substitution mechanism made literal - the money-in-cinema-seats gag the
  line begs for. Pays off 5.2's definition with a picture a learner can retell.
- **Composition / layout:** full-bleed real photo base: an empty cinema auditorium, rows
  of red seats filling the lower two thirds, screen glow at top (~0.75 brightness, still
  readable). FOUR parody banknotes sit upright IN the seats like little audience members,
  spread across the center band (28-72% x, 46-68% y). Ticket devices float in the top
  band: match ticket stub top-LEFT (8-34% x, 9-28% y), cinema ticket stub top-RIGHT
  (66-92% x, 9-28% y), and a `$100` price chip that lands on the match stub. A small
  `CITY TOTAL` meter card top-center (40-60% x, 7-22% y). WIT peeks bottom-CENTER
  (36-64% x, shoulders crop at bottom edge). Handwritten gag label sits right of WIT
  (66-90% x, 60-68% y), above the subtitle-safe zone. Z-order: base < seated bills <
  WIT < tickets/meter/labels.
- **Elements:**
  - *Base (full-bleed):* real empty cinema hall, red velvet seats in rows, warm screen
    spill from the top; no people, no branded screen content.
  - *Seated banknotes (x4):* the section's silliest hero - a parody banknote folded at
    its middle so it "sits" upright in a seat like a tiny flat spectator, slight lean.
    Composited four times in different seats. On the payoff word, ONE of them hops in an
    arc from its seat to an empty seat two places over and settles.
  - *Match ticket stub (top-left):* generated blank sports-ticket stub (perforated edge,
    seat/row boxes empty), labeled by CSS `MATCH` in handwriting; the `$100` chip - a
    small cream price chip with `$100` handwritten - slams onto it.
  - *Cinema ticket stub (top-right):* generated blank cinema stub with film-strip edge
    styling, CSS label `CINEMA`; where its price should be there is a dashed empty chip
    outline and a red handwritten `-$100`.
  - *`CITY TOTAL` meter (top-center):* small cream card with a drawn半round gauge - a
    needle wobbles and settles dead-center on a handwritten `same` (not richer, not
    poorer).
- **Mascot:** pose `unimpressed_smirk_closeup` (library); placement bottom-CENTER peek,
  ~1/3 frame, shoulders crop; facing camera dead-on; expression: half-lidded dry smirk -
  the "that is it, that is the whole trick" face while the bill hops behind him.
- **On-screen text:** `$100` chip (handwritten, cream chip) on hundred dollars@15.52;
  `MATCH` label with its stub on match@16.82; chip slams onto the match stub on
  a hundred@17.86; `CINEMA` stub + dashed slot + red `-$100` on cinema@19.28;
  `CITY TOTAL` card on city@20.14 with the needle settling on `same` at richer@20.94;
  gag label `changed seats.` (black handwriting, small arrow to the hopping bill) on
  seats@22.54.
- **Emotion:** dry amusement - the math is a shrug, the visual is a hop.
- **Insight / joke:** the same hundred literally changes seats: cinema seat to stadium
  seat. The city's gauge does not move. Learners can screenshot this one frame and
  retell the whole mechanism.
- **Linkage / eye path:** `$100` chip (top-center) -> lands left on MATCH -> dashes
  right to the CINEMA hole (-$100) -> down the center to the flat gauge -> the hopping
  banknote in the seats -> WIT's smirk under it as the button.
- **Show-as-you-say:** hard cut on The@15.36 with base + four seated banknotes already
  in place (they are set dressing until the gag activates - funnier when paused); `$100`
  chip pops (impact) on hundred dollars@15.52; match stub hard-shows on match@16.82;
  chip slides and slams onto the stub (impact) on a hundred@17.86; cinema stub + dashed
  slot + `-$100` hard-show on cinema@19.28; `CITY TOTAL` card hard-shows on city@20.14,
  needle wobbles and settles (small impact) on richer@20.94; WIT hard-shows on
  just@21.88; one seated banknote hops two seats over (arc, boing) on changed@22.16
  through seats@23.36, with `changed seats.` label on seats@22.54; cut at 23.36.
- **Sound:** cinema room tone (quiet); chip slam thud; paper dashes; a tiny springy
  "boing" for the seat hop; no music swell - dry beat.
- **Color / contrast:** red seat rows dominate; teal bills pop against red; cream chips
  and card read bright; the only red TEXT is `-$100`.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `cinema-red-seats-1.jpg` | browse-real-photo | real empty cinema auditorium, rows of red velvet seats, warm screen glow, no people/brands | full-bleed base | new |
| `banknote-seated-fan.png` | generate | parody teal-and-cream banknote folded to sit upright like a tiny flat spectator, slight lean, isolated, transparent bg | 4 copies in the seat rows, center band | new (this scene's hero) |
| `ticket-match-stub.png` | generate | blank sports match ticket stub, perforated edge, empty seat/row boxes, isolated, transparent bg (text via CSS) | top-left ~26% width | new |
| `ticket-cinema-stub.png` | generate | blank cinema ticket stub with film-strip edge styling, empty price box, isolated, transparent bg (text via CSS) | top-right ~26% width | new |
| `unimpressed_smirk_closeup.png` | pose | library dry-smirk closeup | bottom-center, ~1/3 frame, shoulders crop | reuse (library) |

### Scene 5.4 - "Drain two: crowding out. Big event, big crowds, big prices. So the normal tourists look at the chaos and say "maybe next year". And locals hide at home."

- **Local time:** `23.36-31.94` (drain@23.36, two@23.54, crowding@24.10, out@24.48,
  event@24.98, crowds@25.56, prices@26.20, tourists@27.48, chaos@28.40, maybe@29.60,
  locals@30.54, hide@30.76, home@31.22)
- **Role:** mechanism board #2 - crowding out. The second drain drinks ON its word, then
  the two escape routes play out: tourists U-turn, locals hide. Links forward: 5.5 shows
  the 2026 evidence for exactly this.
- **Composition / layout:** full-bleed real photo base: a wall of stacked colorful
  vintage suitcases filling the frame (bright, ~0.8) - the tourists who are about to
  turn around. Drain grate (REUSED) bottom-RIGHT (56-88% x, 60-94% y), plate labeled on
  the word, two bills sliding in. Three red surge tags stamp in a rising diagonal
  cascade top-left toward center (tag 1 at 8-26% x, 22-30% y; tag 2 at 20-40% x,
  14-24% y; tag 3 at 34-58% x, 6-18% y), each bigger than the last. A white U-turn
  arrow (drawn SVG) sweeps over the suitcase wall center (30-58% x, 34-56% y). A
  handwritten luggage tag `maybe next year` hangs on a suitcase handle at (34-52% x,
  56-66% y). WIT peeks from the LEFT edge (0-18% x, 30-100% y), hiding. The money pile
  widget sits top-RIGHT corner (80-96% x, 5-16% y) at ~45% scale. Z-order: base < grate
  < bills < arrow < tags < luggage tag < WIT < labels.
- **Elements:**
  - *Base (full-bleed):* real stack/wall of colorful vintage suitcases (teal, mustard,
    brown), tightly packed, bright daylight; no airline stickers with real brands, no
    people.
  - *Drain grate (bottom-right, ~30% width):* same grate file; plate gets `DRAIN 2:`
    then `CROWDING OUT`; two single banknotes slide down during the label word; faint
    suction shading again.
  - *Surge tags (x3):* red swing-tags (string + tag shape, drawn), handwritten white
    text `BIG EVENT`, `BIG CROWDS`, `BIG PRICES`; each stamps in bigger and steeper -
    a rising price staircase.
  - *U-turn arrow:* thick white hand-drawn arrow that enters from the right, loops, and
    exits right - a tourist path turning around; draws on over ~0.7s.
  - *Luggage tag:* cream paper luggage tag, rough string, handwritten `maybe next year`,
    swings 3deg after popping.
  - *Money pile widget (top-right):* the boom pile at ~45% scale, tag now reads just
    `boom` - visibly less of it.
- **Mascot:** pose `worried_uneasy_wide_eyes` (library); placement LEFT edge peek
  (deliberate intentional edge crop - one shoulder and half the body outside frame),
  ~1/3 frame, facing right, wide uneasy eyes scanning the chaos; a small handwritten tag
  `locals` with a short arrow points at him. He IS the local hiding at home.
- **On-screen text:** plate `DRAIN 2:` on drain@23.36; plate `CROWDING OUT` stamps on
  crowding@24.10; `BIG EVENT` on event@24.98; `BIG CROWDS` on crowds@25.56; `BIG PRICES`
  on prices@26.20; luggage tag `maybe next year` on maybe@29.60; `locals` tag + arrow on
  hide@30.76. Everything handwritten; the three surge tags are the only red text.
- **Emotion:** rising squeeze - prices climbing the frame while everyone backs away.
- **Insight / joke:** the drain sits among the suitcases: the "extra visitors" ARE the
  drain - and the one local in frame is hiding behind the picture's own edge.
- **Linkage / eye path:** plate label (bottom-right) -> up the rising red tag staircase
  left-to-center -> the U-turn arrow loops the eye back right -> down to the luggage tag
  answer -> WIT peeking at the far left edge, tagged `locals`.
- **Show-as-you-say:** hard cut on drain@23.36 with base + grate + `DRAIN 2:` plate +
  pile widget (hard-show); `CROWDING OUT` stamps (impact) on crowding@24.10 as two bills
  slide down 24.10-24.88 (gurgle #2, slightly louder); surge tags stamp (impact thud
  x3, rising pitch) on event@24.98 / crowds@25.56 / prices@26.20; U-turn arrow draws on
  look@27.86-chaos@28.62; luggage tag pops + swings (paper fwip) on maybe@29.60; WIT
  hard-shows peeking on locals@30.54 with `locals` tag + arrow on hide@30.76; hold,
  cut at 31.94.
- **Sound:** crowd murmur rising under the three tag thuds, cut dead after prices@26.92
  (the silence = tourists leaving); gurgle #2 on the swallow; paper fwip; a tiny
  door-creak as WIT peeks in.
- **Color / contrast:** warm suitcase multicolor; three red tags form the loudest shapes;
  the grate is again the only cold dark object; WIT's white face pops at the bright left
  edge.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `suitcase-stack-1.jpg` | browse-real-photo | wall of stacked colorful vintage suitcases, tightly packed, bright daylight, no brand stickers/people | full-bleed base | new |
| `drain-grate-ornate.png` | reuse | the drain grate, plate labeled by CSS | bottom-right ~30% width | reuse (5.1) |
| `banknote-single-crisp.png` | reuse | 2 copies sliding into the grate | into grate, bottom-right | reuse (5.2) |
| `money-pile-party.png` | reuse | the boom pile at ~45% scale - second shrink | top-right widget | reuse (5.1) |
| `worried_uneasy_wide_eyes.png` | pose | library uneasy wide-eyes, used as the hiding local | left edge peek, ~1/3 frame, half-body outside frame | reuse (library) |

### Scene 5.5 - "Right now, in 2026, some fan-zone streets are having record days - while shops a few blocks away are down around twenty percent. The party does not spread. It just moves money around."

- **Local time:** `31.94-42.50` (2026@32.72, streets@34.32, record@35.00, days@35.36,
  while@35.76, shops@36.14, down@37.62, twenty percent@38.16, party@39.34, spread@40.10,
  moves@41.20, around@41.80) - 10.56s, run as a deliberate two-phase evidence board:
  phase A left shopfront (31.94-35.76), phase B right shopfront (35.76-39.10), verdict
  overlay (39.10-42.50).
- **Role:** the evidence board for crowding out - the live 2026 receipt for 5.4's claim.
  The one dated, hedged, real-world beat of the section; the honesty rails live on the
  cards. Links back: same mechanism as 5.4; links forward: "moves money around" tees up
  leakage asking where it finally goes.
- **Composition / layout:** full-bleed real photo base: a bright, people-free cobblestone
  shopping street receding gently (horizon ~45%, ~0.8 brightness). Two generated
  shopfront elements sit side by side on it like stage flats: the mobbed one LEFT
  (6-46% x, 30-84% y), the dead one RIGHT (54-94% x, 30-84% y). Red `2026` date stamp
  top-left corner (7-17% x, 7-15% y). Score card A floats above the left shop (9-43% x,
  15-27% y); score card B above the right shop (57-91% x, 15-27% y). A warm spotlight
  glow (CSS radial) sits on the left shop in phase A and slides to the right shop at the
  phase break. Verdict phase: a thick hand-drawn arrow arcs from the right shopfront
  over to the left one (40-64% x, 34-46% y apex) with a single banknote sliding along
  it; a two-part handwritten verdict line sits center (32-68% x, 62-70% y), above the
  subtitle-safe zone. WIT bottom-RIGHT corner (72-100% x, 52-100% y, chest crop),
  under card B. Z-order: base < shopfronts < spotlight < WIT < arrow/bill < cards/stamp.
- **Elements:**
  - *Base (full-bleed):* real cobblestone street with plain building faces, bright
    daylight, no people, no readable shop signs.
  - *Mobbed shopfront (left, ~40% width):* generated festive shop facade - door flung
    open, teal-and-gold bunting, scarves piled in the window, a cash register drawer
    bursting with bills, a queue of shopping bags lined up at the door (objects imply
    the crowd - no people), confetti on its awning. Blank sign board (no brand).
  - *Dead shopfront (right, ~40% width):* generated gray shuttered shop facade - metal
    shutter half down, faded awning, cobwebs across the door corner, a leaning `dust`
    broom, an empty tip jar on the step. Same architectural style as its neighbor -
    clearly the same street.
  - *Score card A (over left shop):* cream evidence card, handwritten: line 1
    `some fan-zone streets:` (small), line 2 `RECORD DAYS` (big, teal, up arrow). The
    word "some" stays - honesty rail.
  - *Score card B (over right shop):* cream evidence card, handwritten: line 1
    `shops a few blocks away:` (small), line 2 `down ~20%` (big, red, down arrow). The
    `~` carries "around" - honesty rail.
  - *`2026` stamp:* red date stamp, 4deg tilt - dates the whole board.
  - *Verdict arrow + bill:* thick black hand-drawn arc from right shop to left shop; one
    parody banknote slides along it; under it the verdict line in two sequential parts:
    `does not spread -` then `just moves around`.
- **Mascot:** pose `shocked_sweating_dismayed` (library); placement bottom-RIGHT corner,
  ~1/3 frame, chest crop; facing left, up toward card B; expression: wide eyes + sweat
  drop - dismay at the -20% landing right above him.
- **On-screen text:** `2026` red stamp on 2026@32.72; card A frame + line 1 on
  streets@34.32, `RECORD DAYS` stamps on record@35.00; card B frame + line 1 on
  shops@36.14, `down ~20%` stamps (impact) on twenty percent@38.16; verdict part 1
  `does not spread -` on spread@40.10; part 2 `just moves around` on moves@41.20.
- **Emotion:** the fun drains out mid-scene - party on the left, cobwebs on the right,
  and the viewer realizes both are the same street this year.
- **Insight / joke:** the "boom" is a spotlight, not a sunrise: it lights one block and
  darkens the next. The arrow literally carries the same bill from the dead shop to the
  busy one.
- **Linkage / eye path:** `2026` stamp (top-left) anchors the date -> left shop + RECORD
  DAYS under the warm spotlight -> the spotlight itself slides right on "while" ->
  cobwebs + `down ~20%` -> WIT's dismay under it -> the verdict arrow drags the eye back
  left along the sliding bill -> verdict line center.
- **Show-as-you-say:** hard cut on Right@31.94 with base + both shopfronts + spotlight
  on the LEFT shop (hard-show; the two flats are the stage); `2026` stamps (impact) on
  2026@32.72; card A hard-shows on streets@34.32; `RECORD DAYS` stamps + a small
  confetti tick over the left awning on record@35.00; PHASE BREAK on while@35.76 - the
  spotlight glow slides right (0.5s ease) and the left shop cools slightly; card B
  hard-shows on shops@36.14; WIT hard-shows on down@37.62; `down ~20%` stamps (impact)
  on twenty percent@38.16 with a dust puff off the shutter; verdict arrow draws on
  spread@40.10 with part 1 of the line; banknote slides along the arrow on moves@41.20
  through around@42.50 with part 2; cut at 42.50.
- **Sound:** faint street party hubbub under phase A (left-panned), crossfades to hollow
  wind + a creaking shutter in phase B (right-panned); stamp thuds on 2026 and -20%;
  soft whoosh as the bill rides the arrow.
- **Color / contrast:** the frame is split warm/cold: gold-teal festivity left, desaturated
  gray right; both cards cream; red exists only in `2026` and `down ~20%`.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `cobblestone-street-1.jpg` | browse-real-photo | bright people-free cobblestone shopping street, plain building faces, no readable signs | full-bleed base | new |
| `shopfront-mobbed.png` | generate | festive shop facade: open door, teal-gold bunting, window piled with scarves, register drawer bursting with bills, queue of shopping bags (no people), blank sign board, isolated, transparent bg | left ~40% width | new |
| `shopfront-empty-cobwebs.png` | generate | gray shuttered shop facade, half-down metal shutter, faded awning, cobwebs on the door corner, empty tip jar on the step, same style as the mobbed one, isolated, transparent bg | right ~40% width | new |
| `banknote-single-crisp.png` | reuse | 1 copy sliding along the verdict arrow | along arrow arc, center | reuse (5.2) |
| `shocked_sweating_dismayed.png` | pose | library dismayed sweat-drop pose | bottom-right, ~1/3 frame, chest crop | reuse (library) |

### Scene 5.6 - "Drain three: leakage. The money spent inside the stadium - tickets, food, sponsor stuff - does not stay in town. It leaks. Mostly toward Zurich."

- **Local time:** `42.50-51.98` (drain@42.50, three@42.80, leakage@43.32, spent@44.38,
  stadium@45.30, tickets@45.72, food@46.58, sponsor@46.86, stuff@47.22, stay@48.58,
  town@49.00, leaks@49.68, [beat]@50.54-50.82, Zurich@51.24)
- **Role:** mechanism board #3 and the section's emotional peak - the last drain drinks,
  then the money physically flies out of the stadium toward the ZURICH signpost, paying
  off Section 4's "FIFA lives in Zurich" gloss. WIT hits full panic (the master arc's
  "horror at drains" money shot).
- **Composition / layout:** full-bleed real photo base: a modern stadium exterior in
  bright daylight, shot from street level, the bowl's roofline crossing the upper third
  (~0.8 brightness, no people, no sponsor boards readable). Drain grate (REUSED)
  bottom-center-left (26-54% x, 62-94% y), plate labeled on the word, bills sliding in.
  Three white item chips pop in a row over the stadium (chip 1 at 20-32% x, chip 2 at
  34-44% x, chip 3 at 46-62% x; all 20-30% y). The banknote flock launches from the
  roofline (~35% x, 30% y) and arcs up-right toward the signpost. Wooden signpost RIGHT
  (74-96% x, 28-80% y), one blank arrow plank pointing right, labeled on its word. WIT
  GIANT on the LEFT (0-34% x, head ~10% from top, hips cropped). The money pile widget
  top-center (44-56% x, 5-15% y) at ~20% scale, fading. Z-order: base < grate < WIT <
  flock < signpost < chips/labels.
- **Elements:**
  - *Base (full-bleed):* real stadium exterior, daytime, concrete-and-glass curve, empty
    forecourt; deliberately a DIFFERENT file and mood from S1's night fireworks shot.
  - *Drain grate (bottom-center-left, ~28% width):* same grate file, third and last
    label: `DRAIN 3:` then `LEAKAGE`; two bills slide down on the word; the suction
    shading is strongest here.
  - *Item chips (x3):* small white rounded chips, handwritten black text: `tickets`,
    `food`, `sponsor stuff` - the things bought inside the stadium, popping left to
    right on their words.
  - *Banknote flock:* generated element of 2-3 parody banknotes mid-flight with motion
    curl (like startled birds); composited twice along the arc. It launches on "leaks",
    FREEZES mid-air during the scripted beat (50.54-50.82), then swooshes past the
    signpost and off-frame on "Zurich" - the pause makes the punchline.
  - *Signpost (right, ~22% width):* generated rustic wooden signpost, one blank arrow
    plank pointing right, isolated; the plank gets a handwritten `ZURICH` label (CSS) on
    its word; slams in with a dust kick.
  - *Money pile widget (top-center):* the boom pile at ~20% scale - nearly gone; it
    drops to ~40% opacity when "leaks" is spoken.
- **Mascot:** pose `panic_hands_on_cheeks_scream` (library); placement LEFT, GIANT ~1/2
  frame height, hips cropped, head high; facing right, watching the flock escape;
  expression: full Home-Alone scream - this is the section's WIT-emotion peak and the
  script's "WIT watches the pile shrink, hands on head" beat.
- **On-screen text:** plate `DRAIN 3:` on drain@42.50; plate `LEAKAGE` stamps on
  leakage@43.32; chips `tickets` / `food` / `sponsor stuff` on tickets@45.72 /
  food@46.58 / sponsor@46.86; plank label `ZURICH` (handwritten, with a small drawn
  right-arrow) stamps on Zurich@51.24. No other text - the flying money is the sentence.
- **Emotion:** horror played for laughs - the money is literally migrating.
- **Insight / joke:** "it leaks" becomes a flock of banknotes flying away like birds in
  autumn, and the [beat] freeze mid-air turns the geography lesson into a punchline:
  they were waiting for directions.
- **Linkage / eye path:** plate label (bottom-left) -> chips read left-to-right over the
  stadium -> the flock launches off the roofline and drags the eye up-right -> the
  ZURICH plank names the destination -> back down to WIT screaming at the far left.
- **Show-as-you-say:** hard cut on drain@42.50 with base + grate + `DRAIN 3:` plate +
  pile widget (hard-show); `LEAKAGE` stamps (impact) on leakage@43.32 as two bills slide
  down 43.32-44.14 (gurgle #3, deepest and longest); chips pop (small impacts) at
  45.72 / 46.58 / 46.86; WIT hard-shows GIANT on does@47.94; flock launches on
  leaks@49.68 (wing-flutter paper sound), pile widget fades to 40% opacity; flock
  FREEZES mid-arc 50.54-50.82 (all SFX stop - audible absence); signpost slams in
  (impact) on mostly@50.82; `ZURICH` plank label stamps on Zurich@51.24 as the flock
  swooshes past it off-frame right; cut at 51.98.
- **Sound:** gurgle #3; three chip pops; paper wing-flutter for the flock; total silence
  in the freeze beat; wood thunk for the signpost; a small whoosh as the flock exits.
- **Color / contrast:** cool concrete blues and grays; teal bills read clearly against
  the sky; the wooden signpost is the only warm brown; WIT's white panic face is the
  brightest emotional point.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `stadium-exterior-day-1.jpg` | browse-real-photo | modern stadium exterior from street level, bright daylight, empty forecourt, no people, no readable sponsor boards (different file/mood from S1's night shot) | full-bleed base | new |
| `drain-grate-ornate.png` | reuse | the drain grate, final label by CSS | bottom-center-left ~28% width | reuse (5.1) |
| `banknote-single-crisp.png` | reuse | 2 copies sliding into the grate | into grate | reuse (5.2) |
| `banknote-flying-flock.png` | generate | 2-3 parody teal-and-cream banknotes mid-flight with motion curl, like startled birds, isolated, transparent bg | launches roofline, arcs up-right, 2 copies staggered | new |
| `signpost-zurich.png` | generate | rustic wooden signpost with ONE blank arrow plank pointing right, isolated, transparent bg (plank text via CSS) | right ~22% width | new |
| `money-pile-party.png` | reuse | the boom pile at ~20% scale, fades to 40% opacity - final shrink | top-center widget | reuse (5.1) |
| `panic_hands_on_cheeks_scream.png` | pose | library full-panic scream - the section's WIT peak | left, ~1/2 frame giant, hips crop | reuse (library) |

### Scene 5.7 - "So the party happens in your house. And the money leaves with the guests."

- **Local time:** `51.98-55.851` (party@52.16, happens@52.46, your@53.02, house@53.24,
  leaves@54.62, guests@55.32; clamp scene end to 55.851 - whisper's "guests" runs to
  57.04)
- **Role:** the section mini-payoff, played quiet after the 5.6 chaos (dense scenes,
  then a clean button). Compresses all three drains into one domestic image and hands
  the baton to Section 6 ("Then the tournament ends...").
- **Composition / layout:** near-still frame: full-bleed real photo base of a house
  front door with party balloons tied to the handle and confetti on the doorstep,
  bright morning light (~0.8). The door sits center-LEFT (24-58% x, 20-92% y). THREE
  walking-guest banknotes march out of the doorway single-file toward frame right along
  the bottom third (path from ~40% x to ~85% x at 62-80% y), staggered sizes. The
  endless receipt (REUSED motif) hangs pinned to the door face, unfurling one strip down
  it (34-46% x, 30-78% y). WIT stands RIGHT (60-96% x, ~2/5 frame, knees cropped),
  watching them go. One small handwritten word floats above the marching bills
  (66-80% x, 50-58% y), above the subtitle-safe zone. Z-order: base < receipt < bills <
  WIT < text.
- **Elements:**
  - *Base (full-bleed):* real front door of an ordinary house, party balloons tied to
    the handle, confetti scattered on the step, warm bright morning light; no people,
    no house number readable.
  - *Walking-guest banknotes (x3):* the section's last hero - a parody banknote with
    little cartoon legs, mid-stride, carrying a tiny suitcase. Composited three times,
    single-file, each slightly smaller toward frame right (leaving in perspective).
  - *Receipt strip:* the video motif `receipt-endless-roll.png`, one strip pinned high
    on the door face, unfurling down it with a soft flap - the guests take the money and
    leave the receipt. No CSS items on it this section; its presence IS the line.
  - *Handwritten word:* a tiny dry `bye.` above the marching bills - the section's
    deadpan button (the walking bills already say the sentence; the text just waves).
- **Mascot:** pose `exhausted_dead_inside_eye_bags` (library); placement RIGHT, ~2/5
  frame, knees cropped; facing left toward the door and the departing bills; expression:
  gray-graded dead-inside eye bags - the host the morning after, resigned. Quietest WIT
  of the section on purpose.
- **On-screen text:** `bye.` (small black handwriting) on leaves@54.62. Nothing else -
  the payoff is the image.
- **Emotion:** deflated calm - the party is over, the house is yours, the money is not.
- **Insight / joke:** the whole section in one frame: your door, their suitcases. The
  guests leave with the money and the receipt stays pinned to YOUR door.
- **Linkage / eye path:** door + balloons (center-left) -> the receipt strip hanging on
  it -> the three bills marching right in a line -> `bye.` -> WIT's dead-inside face
  watching them go. Left-to-right exit = the money's direction all section.
- **Show-as-you-say:** hard cut on So@51.98 - base + WIT + receipt already in place
  (hard-show; the drain gurgle from 5.6 stops dead, quiet room tone); a single confetti
  bit drifts off the doorstep on party@52.16; the three walking banknotes step out of
  the doorway and start marching (impact entrance, tiny footstep taps) on leaves@54.62;
  `bye.` hard-shows on leaves@54.62; the receipt strip gives one soft flap on
  guests@55.32; hold the final frame to 55.851, hard cut to Section 6.
- **Sound:** near-silence - room tone, three or four tiny paper footstep taps, one soft
  paper flap for the receipt; no music. The quiet IS the morning after.
- **Color / contrast:** warm door wood + pastel balloons; teal bills pop as they exit;
  WIT is deliberately the grayest element in the frame; white receipt strip reads
  bright against the door.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `front-door-balloons-1.jpg` | browse-real-photo | real house front door with party balloons tied to the handle and confetti on the step, bright morning light, no people, no readable house number | full-bleed base | new |
| `banknote-walking-guest.png` | generate | parody teal-and-cream banknote with little cartoon legs mid-stride, carrying a tiny suitcase, isolated, transparent bg | 3 copies single-file, doorway to frame right, bottom third | new |
| `receipt-endless-roll.png` | reuse | the video motif receipt, one strip pinned to the door face, unfurling down | on door face, 34-46% x | reuse (S1.3) |
| `exhausted_dead_inside_eye_bags.png` | pose | library dead-inside morning-after pose | right, ~2/5 frame, knees crop | reuse (library) |

## Section Asset Summary

| Filename | Type | First scene | Reused in | Notes |
|---|---|---|---|---|
| `drain-grate-ornate.png` | generate | 5.1 (x3 copies) | 5.2, 5.4, 5.6 | SECTION HERO; blank plate - each drain named by CSS label on its spoken word |
| `money-pile-party.png` | generate | 5.1 | 5.2 (~70%), 5.4 (~45%), 5.6 (~20%, fading) | the "boom" running gag - shrinks every drain scene, gone by 5.7 |
| `banknote-single-crisp.png` | generate | 5.2 | 5.4, 5.5, 5.6 | generic parody bill for all slides/swallows; no real currency design |
| `banknote-seated-fan.png` | generate | 5.3 | - | folded bill sitting upright in a cinema seat; one copy hops on "changed seats" |
| `banknote-flying-flock.png` | generate | 5.6 | - | bills as startled birds; freezes mid-air on the [beat], exits on "Zurich" |
| `banknote-walking-guest.png` | generate | 5.7 | - | bill with legs + tiny suitcase; the guests leaving |
| `ticket-match-stub.png` | generate | 5.3 | - | blank stub, `MATCH` + $100 chip via CSS |
| `ticket-cinema-stub.png` | generate | 5.3 | - | blank stub, `CINEMA` + dashed -$100 slot via CSS |
| `shopfront-mobbed.png` | generate | 5.5 | - | festive facade, crowd implied by objects only (no people) |
| `shopfront-empty-cobwebs.png` | generate | 5.5 | - | shuttered facade with cobwebs; same style as its neighbor |
| `signpost-zurich.png` | generate | 5.6 | - | blank arrow plank; `ZURICH` label via CSS on its word |
| `wit-minister-sash-shouting.png` | generate (NEW pose) | 5.1 | - | WIT as the tourism minister: suit + blank teal sash + megaphone |
| `receipt-endless-roll.png` | reuse | 5.7 | - | VIDEO MOTIF from S1.3; pinned to the door, no CSS items this section |
| `confetti-plaza-1.jpg` | browse-real-photo | 5.1 | - | party-morning plaza floor; home for the three grates |
| `wallet-open-1.jpg` | browse-real-photo | 5.2 | - | the drain is installed in YOUR wallet |
| `cinema-red-seats-1.jpg` | browse-real-photo | 5.3 | - | red seat rows; the seat-hop gag stage |
| `suitcase-stack-1.jpg` | browse-real-photo | 5.4 | - | tourists about to U-turn; no brand stickers |
| `cobblestone-street-1.jpg` | browse-real-photo | 5.5 | - | neutral street stage for the two shopfront flats |
| `stadium-exterior-day-1.jpg` | browse-real-photo | 5.6 | - | day exterior - distinct from S1's night fireworks file |
| `front-door-balloons-1.jpg` | browse-real-photo | 5.7 | - | the party in YOUR house |
| library poses (6) | pose | 5.2-5.7 | - | lecturing_finger_raised_eyes_closed, unimpressed_smirk_closeup, worried_uneasy_wide_eyes, shocked_sweating_dismayed, panic_hands_on_cheeks_scream, exhausted_dead_inside_eye_bags |

## Approval Checks

- each scene picturable from text alone: yes - every scene lists base, element positions
  in %, z-order, entrances with word@time, and WIT pose/side/scale/crop/expression.
- ~one scene per sentence, scene-types varied: yes - 7 scenes over 55.851s; rotation is
  wide gag -> mechanism board -> wide gag -> mechanism board -> evidence board ->
  mechanism/gag peak -> quiet payoff. Scene 5.5 runs 10.56s (slightly over the ~10s
  guideline) as a deliberate two-phase evidence board with a spotlight slide at
  while@35.76 and a verdict-arrow phase at spread@40.10, so the frame changes every ~4s
  inside it; every other scene is 3.9-9.5s.
- every scene has a real/real-looking base: yes - 7 FRESH people-free, brand-free photo
  bases (confetti plaza, open wallet, cinema seats, suitcase wall, cobblestone street,
  stadium exterior by day, balloon front door), none reused within the section, none
  shared with other sections' files, all kept bright (~0.75-0.8, no heavy scrims).
- mascot big/high with a specific pose+expression per scene: yes - WIT in all 7 scenes,
  one beat each, no pose repeated, sides rotate L/R/C/L/R/L/R (never the same side twice
  in a row), scales 1/3 to 1/2 with giant anchors in 5.2 and 5.6, head+glasses always
  inside frame, only legs/edge crops (5.4's half-out edge peek is intentional and the
  expression still reads).
- show-as-you-say timeline present per scene: yes - every entrance is pinned to a real
  whisper timestamp with hard-show vs impact marked; each drain visibly swallows bills
  ON its name word (substitution@10.24, crowding@24.10, leakage@43.32); the final scene
  is clamped to the real 55.851s audio end.
- every asset has type + description + filename + layout: yes - per-scene tables plus
  the summary table; 12 generate, 7 browse bases, 1 shared-registry reuse, 6 library
  poses.
- repeated subjects reuse the same filename: yes - `drain-grate-ornate.png` is ONE file
  labeled by CSS across all four drain appearances; `money-pile-party.png` and
  `banknote-single-crisp.png` recur by filename; `receipt-endless-roll.png` and the pose
  files reuse the registry names unchanged.
- public figures handled as caricature/parody, punching up: no real people appear at
  all - "every tourism minister" is WIT in a generic sash costume (role, not a person);
  edge is aimed at the incentive system, never a nation or its fans; the 2026 evidence
  keeps the script's hedges on screen (`some fan-zone streets`, `down ~20%`, dated
  `2026`); banknotes are parody play money, no real currency or brands, no real flags.
- no image-generation prompts written here: correct - descriptions only; prompts are
  visual-implement's job.
- in sync with master `04-visual-plan.md`: pending - the master currently lists Section
  5 as `not planned`; the master-assembler should paste this section block in and update
  the Section Index row (7 scenes, 26 asset rows in summary, duration 55.851s).
