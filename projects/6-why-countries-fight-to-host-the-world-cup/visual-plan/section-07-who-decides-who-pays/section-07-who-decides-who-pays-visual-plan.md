# Section 7 Visual Plan - Who Decides Is Not Who Pays

Video: `Why Countries Fight to Host the World Cup (and Lose Billions)`
Section: `Section 7: Who Decides Is Not Who Pays`
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

- Section goal: land the real answer of the video - prestige is bought by the people who
  decide and paid by the people who don't - then prove it three ways: referendums kill
  bids when payers vote, LA 1984 profited by being banned from spending, and 2026 still
  bills US cities $100M+ each despite building nothing. The map joke splits the two idea
  runs as a clean breathing gag.
- Duration: `66.987s` (audio `scratch-audio/section-07-who-decides-who-pays-david23-am_eric-0.81.mp3`)
- Timing source: `voiceover/section-07-who-decides-who-pays/section-07-word-timings.json`
  (whisper-tiny.en, generated 2026-07-02). Clamp the final scene's end to the real
  `66.987s` audio duration - whisper's last-word end overshoots. Mishearings do not
  affect timestamps: "bitter" = "bidder", "2,000-34" = "2034", "It's Los Angeles" =
  "was Los Angeles", "Build nothing will still pay" = "Build nothing. Still pay.".
  KNOWN JSON DEFECT: the tail is non-monotonic - after `with@63.18-63.50` whisper jumps
  backward (assigns 60.51+ to the last eight words). Fix used here: keep that tail
  block's internal spacing and shift it forward by +2.99s so "no" starts at 63.50; all
  tail cues below are marked with `~` (interpolated): no@~63.50, share@~63.78,
  ticket@~64.26, money@~64.42, Build@~65.04, nothing@~65.34, Still@~66.04, pay@~66.34,
  clamped end 66.987.
- Scene count: `9` (a visible change every ~5-9s; longest base 9.32s)
- Scene-type rotation: 7.1 two-phase question + split mechanism board -> 7.2 glamour
  photo-op gag -> 7.3 map gag + timeline -> 7.4 mechanism form board -> 7.5 ballot
  evidence tally -> 7.6 object-hero meter -> 7.7 evidence pair shelf -> 7.8 parody ad
  UI -> 7.9 payoff board
- Mascot arc in this section: confused shrug (why fight?) -> dry smirk at the photo-op ->
  deadpan map pointer -> uneasy chin-hold at the invented number -> furious NO with the
  voters -> flattest deadpan at the applause -> approving OK for LA 1984 -> smug
  ad-salesman lean -> resigned smiling shrug ("still pay")

## Scenes

### Scene 7.1 - "So if the bill is this predictable, why do countries still fight? Because of the oldest trick in economics: the people who decide are not the people who pay."

- **Local time:** `0.00-8.78` (fight?@3.30, Because@3.66, economics@5.10, decide@6.66, pay@8.18)
- **Role:** bridge out of S6's morning-after into the section question, then answer it
  immediately with the section thesis as one picture: deciders on one side, payers on the
  other. Two-phase scene. Links forward: the suited trio introduced here stars in 7.2 and
  exits in 7.3; the tiny taxpayer-WITs are the "you pay" face of the whole section.
- **Composition / layout:** full-bleed real photo base: a frayed tug-of-war rope pulled
  tight across the frame on a ~15deg diagonal, knot near center, bright daylight (~0.8).
  Phase A (0.00-3.66): WIT GIANT dead center (30-70% x, head ~10% from top, hips cropped),
  chalk question line upper-left. Phase B (3.66-8.78): a vintage ribbon banner unrolls
  top-center (25-75% x, 4-12% y); two torn-paper panels slide in flanking WIT: LEFT panel
  (2-28% x, 22-72% y) and RIGHT panel (72-98% x, 20-78% y). Z-order: base -> rope -> panels
  -> WIT -> banner/tags.
- **Elements:**
  - *Base (full-bleed):* one thick frayed tug-of-war rope stretched taut, diagonal, no
    hands or people, sunlit neutral ground behind - "countries still fight" made literal.
  - *Ribbon banner (top-center):* vintage unrolling ribbon, cream lettering on deep teal:
    `THE OLDEST TRICK IN ECONOMICS`.
  - *Left panel "DECIDES" (2-28% x):* torn-paper card containing the generic suited trio
    behind a small wooden podium (faceless featureless heads, dark suits - no real
    people), one hand mid-wave; green torn-paper tag `DECIDES` pinned to the panel top.
  - *Right panel "PAYS" (72-98% x):* torn-paper card containing the receipt conveyor
    machine angled down-right, the endless receipt strip flowing off its belt and down
    onto THREE tiny taxpayer-WITs below (same new pose asset placed at 3 slightly
    different scales/rotations = a crowd), arms up catching the paper; red torn-paper tag
    `PAYS` pinned to the panel top.
- **Mascot:** pose `shrug_confused_flat_mouth` (library); placement CENTER GIANT, ~1/2
  frame height, hips cropped, head ~10% from top; facing camera; expression: blank-eyed
  shrug - in phase A it reads "why?!", in phase B the same shrug reads "that is just how
  it works".
- **On-screen text:** `why still FIGHT?` - white chalk handwriting, upper-left (8-34% x,
  10-22% y), 2deg tilt, hard-shows on fight?@3.30. Banner `THE OLDEST TRICK IN ECONOMICS`
  unrolls on economics@5.10. Tag `DECIDES` (green) with the left panel on decide@6.66.
  Tag `PAYS` (red) with the right panel on pay@8.18.
- **Emotion:** puzzled question flipping into a dry "oh - THAT old trick" realization.
- **Insight / joke:** the whole section in one frame: podium people wave, tiny yous catch
  the paper. The rope carries the "fight" without a single fist.
- **Linkage / eye path:** WIT center -> banner top -> left DECIDES panel -> across WIT's
  shrug -> right PAYS panel, where the receipt physically pours onto the tiny WITs. The
  rope diagonal underlines the whole standoff.
- **Show-as-you-say:** base + giant WIT from 0.00 (hard cut from S6); `why still FIGHT?`
  hard-shows on fight?@3.30; banner unrolls (impact) on economics@5.10; left panel slides
  in + settles (hard-show) with its green tag on decide@6.66; right panel slides in on
  pay@8.18 with red tag + conveyor starts + receipt crawl + tiny WITs pop (impact). All
  hold to the cut.
- **Sound:** low rope creak under phase A; soft whoosh per panel; the receipt printer
  tick-tick signature starts on pay@8.18 and runs under the scene.
- **Color / contrast:** sun-bleached rope neutrals; deep teal banner; the green/red tag
  pair is the only saturated color duel; white receipt pops inside the right panel.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `rope-tug-frayed-1.jpg` | browse-real-photo | one thick frayed tug-of-war rope pulled taut, diagonal, bright daylight, no people or hands | full-bleed base | new |
| `shrug_confused_flat_mouth.png` | pose | library pose, blank confused shrug | center giant, ~1/2 frame, hips crop | reuse (library) |
| `podium-suits-trio.png` | generate | three generic FACELESS suited figures (featureless blank heads, dark suits) behind one small wooden podium, one mid-wave - deliberately anonymous "deciders", isolated, transparent bg | inside left panel, ~20% frame width | new (reused 7.2, 7.3) |
| `receipt-conveyor-machine.png` | generate | chunky industrial conveyor-belt machine with rollers and a short output ramp, slightly cartoonish proportions, no branding, isolated, transparent bg | inside right panel, angled down-right, ~18% width | new |
| `receipt-endless-roll.png` | reuse | the video motif receipt strip, flowing over the conveyor belt and down | right panel, belt -> tiny WITs | reuse (S1.3) |
| `wit-tiny-taxpayer-catching-receipt.png` | generate | NEW WIT pose: tiny full-body WIT, both arms stretched up catching a falling receipt strip, overwhelmed wide eyes, one sweat drop, knees slightly buckled | right panel bottom, placed 3x at ~6-8% frame height each | new (NEW pose - section 7 signature) |

### Scene 7.2 - "The politician gets the good part now. The photos. The opening ceremony. The 'we put our country on the map' speech."

- **Local time:** `8.78-15.36` (now@10.44, photos@11.08, ceremony@12.22, we@13.14, speech@14.42)
- **Role:** show the decider's entire payoff - glamour, delivered immediately. Sets up the
  map joke (7.3) and the "gone" exit gag (7.3). The parody trophy returns as the photo-op
  prop.
- **Composition / layout:** full-bleed real photo base: a red carpet with gold stanchions
  and velvet rope leading to a low stage riser, no people (~0.75, warm). The suited trio
  (REUSED file) stands big center-left (18-56% x, 22-88% y) behind their podium; the
  parody trophy (REUSED) sits on the podium ledge (44-56% x, 40-56% y). Three
  polaroid-style photo cards snap into a top band (15-85% x, 6-26% y), left to right.
  Speech bubble at 40-72% x, 14-34% y. WIT closeup RIGHT (68-100% x). CSS camera-flash
  blooms fire from off-frame top corners.
- **Elements:**
  - *Base (full-bleed):* red carpet + gold stanchions to an empty little stage - the
    photo-op environment with nobody in it yet.
  - *Suited trio (center-left, ~38% width):* same faceless deciders, now hero-sized,
    mid-handshake and wave behind the podium.
  - *Trophy (podium ledge, ~10% width):* the hero parody trophy, warm grade, one glint.
  - *Polaroids (top band):* three white-framed instant-photo cards, each holding a
    slightly rotated re-crop of the same trio asset (composited by render, no new file);
    they overlap like a brag wall.
  - *Camera flashes:* two or three CSS white blooms per beat from off-frame - nobody is
    visibly taking the pictures, which is the point.
  - *Speech bubble:* white hand-drawn bubble from the center suit.
- **Mascot:** pose `unimpressed_smirk_closeup` (library); placement RIGHT, ~1/3 frame,
  chest crop (head + glasses fully inside frame); facing left at the show; expression:
  half-lidded dry "sure, buddy" smirk.
- **On-screen text:** small gold tag `the good part - NOW` near the podium base
  (24-44% x, 88%-> moved up to 74-84% y band, above subtitle zone) on now@10.44; speech
  bubble text `"WE PUT OUR COUNTRY ON THE MAP"` hand-lettered black on we@13.14. No
  polaroid captions - the frames alone read as vanity.
- **Emotion:** glossy self-congratulation vs one dry unimpressed witness.
- **Insight / joke:** the whole benefit is a photo-op; the flashes come from nowhere - who
  is even photographing? The trophy is a prop in someone else's album.
- **Linkage / eye path:** carpet lines lead to the trio -> trophy glint on the podium ->
  up to the polaroid brag wall (left to right with the narration) -> bubble -> WIT's
  smirk far right as the button.
- **Show-as-you-say:** cut on The@8.78 (base + trio + trophy + WIT all from cut); tag
  `the good part - NOW` hard-shows on now@10.44; polaroid 1 snaps + double flash (impact)
  on photos@11.08; polaroid 2 + flash on ceremony@12.22; speech bubble pops (impact) on
  we@13.14 and holds; polaroid 3 (a photo of the speech itself) + flash on speech@14.42.
- **Sound:** camera shutter + flash pops at 11.08 / 12.22 / 14.42; soft self-satisfied
  crowd murmur under; bubble boing at 13.14; receipt tick faint.
- **Color / contrast:** red carpet + gold stanchions warm; white polaroid frames and
  flash blooms pop; the bubble is the only pure-white text object.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `red-carpet-stanchions-1.jpg` | browse-real-photo | red carpet with gold stanchions and velvet rope leading to a small empty stage, no people, warm light | full-bleed base | new |
| `podium-suits-trio.png` | reuse | the faceless deciders, hero size, behind podium | center-left ~38% width | reuse (7.1) |
| `trophy-gold-parody.png` | reuse | the video hero parody trophy as photo-op prop | podium ledge, ~10% width | reuse (S1.1) |
| `unimpressed_smirk_closeup.png` | pose | library pose, dry witness | right, ~1/3 frame, chest crop | reuse (library) |

### Scene 7.3 - "The country was already on the map. And the bill arrives five or ten years later - when that politician is gone."

- **Local time:** `15.36-21.04` (already@15.98, map@16.54, bill@17.36, five@17.86, later@18.94, gone@20.68)
- **Role:** the breathing gag between the two idea runs (the map joke, planned as a clean
  single-device beat), then the delayed-bill mechanic and the exit gag in the same frame.
- **Composition / layout:** full-bleed real photo base: a bright colored school atlas
  double-page spread, top-down (~0.85 - the brightest paper of the section). A hand-drawn
  red arrow lands center, tip at ~52% x, 46% y. WIT LEFT (0-36% x, ~2/5 frame, waist
  crop). Phase 2: the bill envelope slides onto the lower-right map area (58-84% x,
  52-76% y); the suited trio (REUSED, small, desaturated) stands at the right edge
  (84-100% x, 40-72% y) and shuffles off-frame on its beat.
- **Elements:**
  - *Base (full-bleed):* colored atlas spread - seas, borders, place labels readable as
    texture only (real printed map, no emphasis on any one country).
  - *Arrow + tag:* thick hand-drawn red arrow pointing at an unremarkable spot, with the
    handwritten tag (see text below) - the script's signature gag device.
  - *Bill envelope (58-84% x):* worn white paper envelope with one red diagonal corner
    stripe; a red CSS stamp and a handwritten date line land on it.
  - *Exiting trio (right edge):* same trio file, ~16% width, desaturated to gray,
    sliding right out of frame.
- **Mascot:** pose `pointing_at_globe_explaining` (library - the map pose); placement
  LEFT, ~2/5 frame, waist crop; facing right at the arrow; expression: neutral "o" mouth
  deadpan - delivering the joke completely straight.
- **On-screen text:** `you are here (already)` - red handwriting beside the arrow; the
  `you are here` part hard-shows on already@15.98, the `(already)` scribbles on
  map@16.54. Envelope stamp `THE BILL` (red) on bill@17.36; handwritten line
  `+5-10 YEARS LATER` under the envelope on five@17.86 (finishes writing by later@18.94).
  Tiny gray tag `gone.` beside the exiting trio on gone@20.68.
- **Emotion:** dry gag relief, then a small returning dread as the envelope lands.
- **Insight / joke:** the literal answer to "put us on the map" - the country is already
  printed there. Then the accountability gap: the bill lands exactly as the deciders
  leave the frame.
- **Linkage / eye path:** WIT's pointing finger -> red arrow -> map spot -> down-right to
  the envelope (cause and cost on the same map) -> the gray trio exiting right. Envelope
  arriving and trio leaving are opposite motions telling the whole story.
- **Show-as-you-say:** hard cut on The@15.36 (base + WIT from cut); arrow +
  `you are here` hard-show on already@15.98; `(already)` scribble (small impact) on
  map@16.54; envelope slides in (impact thud) on bill@17.36; `+5-10 YEARS LATER` writes
  from five@17.86; trio visible desaturated from 19.36, slides off + `gone.` tag on
  gone@20.68.
- **Sound:** marker squeak (arrow, 15.98); paper thud (envelope, 17.36); pencil scratch
  (17.86); tiny footsteps-shuffle + soft door click on gone@20.68; receipt tick faint.
- **Color / contrast:** bright atlas blues/greens/creams; red arrow + red stamp are the
  only accents; the desaturated gray trio reads as "already history".

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `map-atlas-colored-1.jpg` | browse-real-photo | bright colored school atlas double-page spread, top-down, real printed map, no country emphasized, no flags | full-bleed base | new |
| `pointing_at_globe_explaining.png` | pose | library map-pointing pose | left, ~2/5 frame, waist crop | reuse (library) |
| `bill-envelope-overdue.png` | generate | worn white paper envelope, slightly dog-eared, one red diagonal corner stripe, no text baked in (CSS adds stamp + date), isolated, transparent bg | lower-right map area, ~24% width, floats with shadow | new |
| `podium-suits-trio.png` | reuse | the deciders, small + desaturated by render, exiting | right edge, ~16% width | reuse (7.1) |

### Scene 7.4 - "You cannot put prestige in a budget. So the impact study invents a number that CAN go in a budget. That is the whole machine."

- **Local time:** `21.06-27.82` (prestige@21.86, budget@22.52, invents@24.10, number@24.60, budget2@25.68, machine@27.00)
- **Role:** mechanism board - WHY impact studies exist. Pays off S3's promise machine in
  one image: the unmeasurable thing gets swapped for an invented measurable one.
- **Composition / layout:** full-bleed real photo base: a chunky desk calculator lying on
  printed spreadsheet pages, top-down (~0.8). A CSS "CITY BUDGET" form card floats LEFT
  (6-44% x, 16-80% y): cream paper look, ruled rows of small boxes, one big highlighted
  empty box at ~24-40% x, 26-42% y. The glowing crown hovers over that box, gets
  rejected, then a rubber stamp slams an invented number into it. WIT RIGHT (62-100% x,
  ~2/5 frame, waist crop). Gear tag top-center (36-64% x, 6-16% y).
- **Elements:**
  - *Base (full-bleed):* big-buttoned desk calculator on spreadsheet printouts - the
    budget world where only numbers are allowed to exist.
  - *Form card (CSS device, LEFT):* header `CITY BUDGET`, ruled rows, one big empty box
    outlined in yellow highlight - the box everything fights over.
  - *Prestige crown:* small radiant golden crown with a soft gold aura, hovering and
    bobbing over the box; on rejection it bounces off, dims, and drops below the card.
  - *Rejection marks:* red dashed outline around the box + a red buzz tag.
  - *Rubber stamp:* classic wood-handle red rubber stamp swinging in from off-frame
    right, with a small CSS side tag `IMPACT STUDY` on its handle.
- **Mascot:** pose `mildly_surprised_hand_at_chin` (library); placement RIGHT, ~2/5
  frame, waist crop; facing left at the form; expression: small surprised "o" with a
  hint of doubt - "huh, so THAT is why".
- **On-screen text:** red buzz tag `DOES NOT FIT` beside the box on budget@22.52; stamped
  number `+$9.9 BILLION*` inside the box on number@24.60 (obviously-parody figure);
  small handwritten footnote `*number invented` at the card's lower edge (~74% y, above
  subtitle zone) on budget2@25.68; gear tag `THE WHOLE MACHINE` (three small drawn SVG
  gears + handwriting, top-center) on machine@27.00.
- **Emotion:** uneasy comprehension - it is silly AND it works.
- **Insight / joke:** prestige literally will not fit in a form box, so a consultant
  stamp fills it with a made-up number that does. The suspicious-asterisk pattern
  carries the honesty ("*number invented").
- **Linkage / eye path:** crown hovers over the exact box the stamp later fills - same
  spot, two attempts, one absurd success. WIT watches the box; the gear tag crowns the
  card as "the machine" gets named.
- **Show-as-you-say:** cut on You@21.06 (base + form card + hovering crown + WIT from
  cut); crown bounce-off + red dashed outline + `DOES NOT FIT` buzz (impact) on
  budget@22.52; crown dims and drops; stamp arm swings in on invents@24.10; stamp slams
  (impact) leaving `+$9.9 BILLION*` on number@24.60; footnote scribbles on budget2@25.68;
  `THE WHOLE MACHINE` gear tag (small impact) on machine@27.00.
- **Sound:** wrong-answer buzzer on 22.52; heavy stamp thunk on 24.60; pencil scratch on
  25.68; three quick gear clicks on 27.00.
- **Color / contrast:** paper cream + calculator gray neutrals; the gold crown glow is
  the single warm accent; red stamp/buzz marks pop against the pale form.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `calculator-spreadsheet-1.jpg` | browse-real-photo | chunky desk calculator lying on printed spreadsheet pages, top-down, no hands, no brand visible | full-bleed base | new |
| `prestige-crown-glow.png` | generate | small radiant golden crown with a soft warm glow aura, slightly cartoonish, isolated, transparent bg | hovers over form box, ~12% width | new |
| `rubber-stamp-red.png` | generate | classic wooden-handle rubber stamp with red base, angled mid-slam, no text baked in, isolated, transparent bg | swings in from right onto the form box, ~16% width | new |
| `mildly_surprised_hand_at_chin.png` | pose | library pose, doubtful "huh" | right, ~2/5 frame, waist crop | reuse (library) |

### Scene 7.5 - "And when regular people get an actual vote? They say no. Since 2013, at least half a dozen Olympic bids have died in public votes."

- **Local time:** `27.82-34.94` (vote@29.40, no@30.38, 2013@31.04, dozen@32.56, Olympic@32.82, died@33.64, votes@34.34)
- **Role:** the evidence counterfactual - when the payers hold the pen, the answer is no.
  Loudest beat of the section; WIT finally speaks for the taxpayers.
- **Composition / layout:** full-bleed real photo base: a real polling booth with a
  pleated navy privacy curtain (~0.75). Ballot box hero center-right (50-78% x,
  34-86% y). Six mini ballot cards pop one after another into a fanned arc above the box
  (44-88% x, 10-28% y), then visually rain toward the slot. Tally painted on the box's
  front face (54-74% x, 56-74% y). WIT GIANT LEFT (0-38% x, hips crop). Red speech stamp
  at 36-48% x, 22-34% y.
- **Elements:**
  - *Base (full-bleed):* empty voting booth, pleated curtain, small shelf - democracy's
    furniture, nobody in it (the people are represented by WIT).
  - *Ballot box (center-right, ~28% width):* classic wooden ballot box, brass slot on
    top, one small brass padlock on the front hasp.
  - *Six ballot cards (CSS):* white cards, slight rotations, each carrying a fat red
    `NO` stamp; they pop sequentially and hang in a fanned arc pointing at the slot.
  - *Tally plate (CSS, on box face):* chalk-style lettering painted onto the box front:
    `SINCE 2013: 6+ OLYMPIC BIDS - DEAD`, with a small handwritten `at least` squeezed
    above the `6+` (the honesty hedge, visible).
- **Mascot:** pose `furious_shouting_anger_mark` (library); placement LEFT GIANT, ~1/2
  frame, hips crop, head ~12% from top; facing right toward the box; expression:
  mid-shout fury with anger mark - the people's NO given a face.
- **On-screen text:** big red stamp-style `NO.` beside WIT's mouth (clear of his face) on
  no@30.38; the six `NO` ballots pop from 2013@31.04 roughly every 0.65s (31.04, 31.70,
  32.40, 33.10, 33.70, last on votes@34.34); box tally `SINCE 2013: 6+ OLYMPIC BIDS -
  DEAD` paints on dozen@32.56 with the word `OLYMPIC` underlined in red on Olympic@32.82;
  `at least` handwritten on the same beat.
- **Emotion:** righteous and loud - the one moment the section gives the payers a voice.
- **Insight / joke:** democracy as a horror movie for bid committees: six little NOs
  raining into a locked box. The dry twist: the tally is written like a scoreboard.
- **Linkage / eye path:** WIT's shout (left) -> the `NO.` stamp it produces -> the ballot
  arc flying right toward the slot -> the running tally on the box face. Cause -> paper ->
  score.
- **Show-as-you-say:** cut on And@27.82 (base + box + giant WIT from cut); `NO.` stamp
  (impact) on no@30.38; ballots pop sequentially from 2013@31.04, one every ~0.65s, the
  sixth landing on votes@34.34; tally paints on dozen@32.56; red `OLYMPIC` underline
  scribbles on Olympic@32.82.
- **Sound:** deep stamp thud on 30.38; six quick paper thwips; chalk squeak for the
  tally; receipt tick paused (this scene belongs to the voters).
- **Color / contrast:** navy curtain + warm wood box; the red NO stamps dominate - the
  reddest frame of the section by design.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `voting-booth-1.jpg` | browse-real-photo | real polling booth with pleated navy privacy curtain and small shelf, empty, no people, no signage | full-bleed base | new |
| `ballot-box-wood.png` | generate | classic wooden ballot box with brass top slot and one small brass padlock on the front hasp, warm wood, isolated, transparent bg | center-right, ~28% width | new |
| `furious_shouting_anger_mark.png` | pose | library pose, mid-shout fury | left giant, ~1/2 frame, hips crop | reuse (library) |

### Scene 7.6 - "And the 2034 World Cup had exactly one bidder. It was approved by applause."

- **Local time:** `34.94-40.32` (2034 spans 35.40-36.28, Cup@36.74, one@37.64, bidder@37.94, approved@38.82, applause@39.46)
- **Role:** the contrast gag - votes kill bids, so the system removed the vote. The
  section's driest absurdity peak, played completely straight.
- **Composition / layout:** full-bleed real photo base: empty auditorium rows of red
  seats, soft focus (~0.75). Applause meter hero center (36-66% x, 22-78% y): a
  carnival-style half-circle dial gauge on a stand. A white perforated ticket stub card
  leans left of the meter (24-38% x, 34-48% y). WIT closeup RIGHT (66-100% x, ~1/3
  frame, chest crop). Two pathetic confetti bits fall on the final beat.
- **Elements:**
  - *Base (full-bleed):* rows of empty red auditorium seats receding - an approval with
    no audience in sight.
  - *Applause meter (center, ~30% width):* vintage carnival applause-o-meter: brass rim,
    cream dial face, red needle resting at the far LEFT; CSS adds the dial-face zone
    text and the base plate text (asset itself is text-free).
  - *Dial face zones (CSS):* small `meh` zone at the left end, glowing `APPROVED` zone
    at the far right end.
  - *Base plate (CSS):* engraved-style plate on the meter stand: `2034 WORLD CUP`.
  - *Ticket stub card (CSS):* white card with perforated edge: `BIDDERS: 1` (the `1`
    stamps separately).
- **Mascot:** pose `deadpan_unimpressed_half_lidded` (library - the signature deadpan);
  placement RIGHT closeup, ~1/3 frame, chest crop; facing CAMERA dead-on (not the
  meter); expression: flattest half-lidded stare while the needle celebrates beside him.
- **On-screen text:** plate `2034 WORLD CUP` hard-shows as the year finishes at
  -34@35.84; stub `BIDDERS:` hard-shows on one@37.64, its `1` stamps (impact) on
  bidder@37.94; small gray tag `(by acclamation)` under the plate on approved@38.82;
  `APPROVED` zone glows as the needle hits it on applause@39.46.
- **Emotion:** dry to the point of frozen - absurdity narrating itself.
- **Insight / joke:** an applause-o-meter as the entire democratic process; one ticket
  stub is the whole "field of bidders"; exactly two confetti bits fall - the celebration
  budget of a foregone conclusion.
- **Linkage / eye path:** stub (left) -> meter dial (center) -> needle sweeping right ->
  WIT's unmoved face (far right). The more the needle celebrates, the flatter WIT gets -
  a straight left-to-right irony gradient.
- **Show-as-you-say:** cut on and@34.94 (base + meter + resting needle + WIT from cut);
  plate `2034 WORLD CUP` on -34@35.84 (hard-show); stub on one@37.64, `1` stamps on
  bidder@37.94 (impact); `(by acclamation)` tag on approved@38.82; needle sweeps hard
  right + `APPROVED` glow + two confetti bits (impact) on applause@39.46; hold to cut.
- **Sound:** slow needle creak-sweep into a thin, short canned applause burst on 39.46 -
  the thinness IS the joke; receipt tick still paused.
- **Color / contrast:** soft red seats; cream dial + brass rim warm; the single glowing
  `APPROVED` is the only bright accent.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `auditorium-seats-1.jpg` | browse-real-photo | rows of empty red auditorium seats, soft focus, no people, no venue branding | full-bleed base | new |
| `applause-meter-dial.png` | generate | vintage carnival applause-o-meter: half-circle cream dial face, brass rim, red needle, small stand with a blank base plate, text-free (CSS adds all labels), isolated, transparent bg | center, ~30% width | new |
| `deadpan_unimpressed_half_lidded.png` | pose | library signature deadpan closeup | right, ~1/3 frame, chest crop | reuse (library) |

### Scene 7.7 - "One of the only hosts that ever clearly made a profit was Los Angeles, 1984 - the Olympics. A public vote had banned the city from spending taxpayer money."

- **Local time:** `40.32-49.36` (only@40.84, profit@42.78, Angeles@43.68, 1984@44.36, Olympics@45.64, vote@46.78, banned@47.24, taxpayer@48.38, money@48.86)
- **Role:** the exception that proves the thesis - an evidence-pair beat: the rule (no
  taxpayer money) and the result (a surplus jar), side by side.
- **Composition / layout:** full-bleed real photo base: sunny palm trees against a clean
  blue sky, low angle (~0.85 - the LA feeling without any landmark). A thin CSS shelf
  line at 74% y carries two hero objects: padlocked wallet LEFT-CENTER (26-48% x,
  42-74% y) and surplus jar RIGHT-CENTER (52-72% x, 36-74% y). A sun-bleached cloth
  banner arcs across the top (20-80% x, 8-20% y) with a small pinned tag. WIT LEFT edge
  (0-26% x, ~1/3 frame, chest crop).
- **Elements:**
  - *Base (full-bleed):* two or three tall palm trees on blue sky, sunny, no buildings,
    no people - a nationality-free "LA vibe".
  - *Padlocked wallet (~20% width):* fat brown leather wallet wrapped tight in a steel
    chain with a chunky brass padlock - the city's money, physically unopenable.
  - *Surplus jar (~18% width):* clear glass jar filled with gold coins, paper lid tied
    with string; CSS labels attach beneath it.
  - *Banner (top):* sun-bleached cloth banner, hand-painted lettering (see text); a
    small paper tag pinned to its right corner.
- **Mascot:** pose `ok_hand_sign_content_closeup` (library); placement LEFT edge, ~1/3
  frame, chest crop; facing right at the jar; expression: content OK-sign approval - the
  only approving WIT of the section, reserved for the payers' one win.
- **On-screen text:** small black handwritten hedge `one of the only ones - ever` above
  the jar position on only@40.84 (the honesty rail, visible); jar label `LA 1984 -
  ORGANIZERS' PROFIT` under the jar on profit@42.78 (the `LA 1984` part re-inks bolder
  on 1984@44.36); pinned tag `THE OLYMPICS` on Olympics@45.64; banner `PUBLIC VOTE: NO
  TAXPAYER $$` unfurls on vote@46.78.
- **Emotion:** relief and approval - one clean win, and it belongs to the people who
  vote.
- **Insight / joke:** the winning strategy on display is a wallet you physically cannot
  open. Profit by prohibition.
- **Linkage / eye path:** banner (the rule) sits above both objects; wallet (the rule
  enforced) left; jar (the result) right; WIT's OK sign aims at the jar. Left-to-right:
  rule -> lock -> profit.
- **Show-as-you-say:** cut on one@40.32 (base + WIT + empty shelf from cut); hedge line
  hard-shows on only@40.84; jar pops with coin clink (impact) + `ORGANIZERS' PROFIT`
  label on profit@42.78; `LA 1984` re-inks on 1984@44.36; `THE OLYMPICS` tag pins on
  Olympics@45.64; banner unfurls on vote@46.78; wallet slams onto the shelf + padlock
  clicks shut (impact) on taxpayer@48.38-money@48.86.
- **Sound:** coin clink on 42.78; cloth snap on 46.78; heavy padlock click on 48.38;
  faint gull-free breeze under (keep it generic).
- **Color / contrast:** blue sky + green palms - brightest base of the section; gold
  coins are the warm accent; the brown chained wallet reads heavy and final.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `palm-trees-sky-1.jpg` | browse-real-photo | tall palm trees against clean blue sunny sky, low angle, no buildings, no people, no landmarks | full-bleed base | new |
| `wallet-padlocked-city.png` | generate | fat brown leather wallet wrapped tight in a steel chain with a chunky brass padlock, slightly cartoonish heft, isolated, transparent bg | left-center on shelf, ~20% width | new |
| `surplus-jar-coins.png` | generate | clear glass jar full of gold coins, paper lid tied with string, label-free (CSS adds labels), isolated, transparent bg | right-center on shelf, ~18% width | new |
| `ok_hand_sign_content_closeup.png` | pose | library pose, content approval | left edge, ~1/3 frame, chest crop | reuse (library) |

### Scene 7.8 - "So the organizers made a profit using one weird trick: not spending any. Even 2026 proves it. The USA, Mexico and Canada built zero new stadiums."

- **Local time:** `49.36-58.68` (organizers@49.94, weird@51.70, trick@52.02, not@52.62, any@53.16, 2026@54.02, proves@55.00, zero@57.56, stadiums@58.24)
- **Role:** the meme-format punchline (approved "one weird trick" clickbait parody) plus
  the fast-forward proof: 2026 ran the same trick on stadiums. Two-beat scene, one base.
- **Composition / layout:** full-bleed real photo base: a retro beige CRT computer
  monitor on a desk, screen toward camera (~0.75). The parody ad card floats slightly
  larger than the screen (30-72% x, 18-76% y). On the 2026 beat a second, smaller dark
  counter card pops lower-left (6-30% x, 48-72% y). WIT CENTER-RIGHT (62-100% x, ~2/5
  frame, waist crop), one elbow leaning on the ad card's top-right corner.
- **Elements:**
  - *Base (full-bleed):* chunky beige CRT monitor + keyboard edge on a desk, powered-on
    glow - the natural habitat of the clickbait ad.
  - *Clickbait ad card (~42% width):* parody popup ad: garish magenta/cyan gradient
    border, a starburst top-left, blank cream center panel, fake `X` close button
    top-right corner - deliberately ugly 2000s web energy; all text lands via CSS.
  - *Ad text (CSS):* small header `ECONOMISTS HATE THIS`; giant middle line `ONE WEIRD
    TRICK`; starburst text `100% LEGAL`; then a red-on-white punch sticker slaps across
    the middle at 3deg tilt: `NOT SPENDING ANY.`
  - *Counter card (CSS, lower-left):* dark card with odometer-style white digit wheels:
    `NEW STADIUMS BUILT:` and rolling digits that slam to a dead `0`; small tag beneath:
    `USA - MEXICO - CANADA` (text only - no flags anywhere).
- **Mascot:** pose `smug_sly_smirk_leaning` (library); placement CENTER-RIGHT, ~2/5
  frame, waist crop, leaning on the ad card corner; facing camera; expression: sly
  salesman smirk - WIT owns the one honest ad in history.
- **On-screen text:** `ECONOMISTS HATE THIS` on organizers@49.94; `ONE WEIRD TRICK` big
  on weird@51.70; starburst `100% LEGAL` on trick@52.02; sticker `NOT SPENDING ANY.`
  slaps (impact) on not@52.62 (fully readable by any@53.16); counter card pops on
  2026@54.02 with digits whirring; digits slam to `0` (impact) on zero@57.56; tag
  `USA - MEXICO - CANADA` on stadiums@58.24.
- **Emotion:** smug comedy - the scam-ad format telling the truth for once.
- **Insight / joke:** the one weird trick that actually works is refusing to spend; and
  2026's counter proves the trick aged well - which makes 7.9's bill even funnier.
  Bonus micro-gag: the fake `X` button wiggles when the sticker slaps - you cannot close
  this ad.
- **Linkage / eye path:** ad headline (center) -> punch sticker -> down-left to the
  counter card (the "customer testimonial") -> its country tag. WIT leans on the ad like
  the guy who posted it.
- **Show-as-you-say:** cut on So@49.36 (base + empty ad frame + WIT from cut); ad text
  beats as above; `X` wiggle micro-gag at 52.62; counter card (hard-show) at 54.02,
  odometer whirs through proves@55.00, slams `0` (impact) on zero@57.56; country tag
  hard-shows on stadiums@58.24.
- **Sound:** short retro blip on card pop (generic, non-branded); sticker slap on 52.62;
  odometer whir 54.02-57.56 ending in a clunk on zero; receipt tick returns quietly.
- **Color / contrast:** beige CRT neutrals; the ad border is deliberately garish
  magenta/cyan; sticker red; dark counter card with white digits pops lower-left.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `crt-monitor-retro-1.jpg` | browse-real-photo | retro beige CRT computer monitor on a desk, screen glowing blank, no brand marks, no people | full-bleed base | new |
| `clickbait-ad-card.png` | generate | parody 2000s popup-ad card: garish magenta/cyan gradient border, starburst top-left, blank cream center panel, fake X close button - text-free (CSS adds all copy), isolated, transparent bg | center, ~42% width, floats over CRT screen | new |
| `smug_sly_smirk_leaning.png` | pose | library pose, salesman lean | center-right, ~2/5 frame, waist crop | reuse (library) |

### Scene 7.9 - "And in the US, host cities are still paying a hundred million dollars or more. Each. With no share of the ticket money. Build nothing. Still pay."

- **Local time:** `58.68-66.987` (US@59.34, $100@61.04, million@61.46, Each@62.86; tail
  interpolated after the JSON's backward jump: ticket@~64.26, money@~64.42, Build@~65.04,
  Still@~66.04, pay@~66.34; scene end clamped to the real 66.987)
- **Role:** the 2026 twist lands in full + the pre-payoff mini-payoff ("Build nothing.
  Still pay.") - the payoff board that hands the section to S8.
- **Composition / layout:** full-bleed real photo base: a generic stone city-hall facade
  with columns, straight-on, no landmark (~0.75). Bill stack hero RIGHT-CENTER (56-82% x,
  34-78% y) sitting on the steps. Counter callback card top-right (80-97% x, 8-20% y).
  Crossed ticket icon mid-frame (38-52% x, 30-44% y). WIT GIANT CENTER-LEFT (8-46% x,
  hips crop, head ~12% from top, head band ~10-26% x). Torn-paper payoff card top-center-
  right (34-76% x, 6-20% y), clear of WIT's face. The endless receipt strip (reuse)
  unrolls along the very bottom (80-92% y, decorative only).
- **Elements:**
  - *Base (full-bleed):* generic columned stone facade - "the city" as an institution,
    no identifiable building.
  - *Bill stack (~24% width):* thick stack of white paper invoices bound with a red
    rubber band, edges ruffled; a CSS label plate leans against it.
  - *Label plate (CSS):* `US CITIES: $100M+` with a separate huge tilted red rubber-stamp
    overlay `EACH.` half on the plate, half on the stack.
  - *Crossed ticket (CSS/SVG):* one drawn admission-ticket icon with a fat red X through
    it + small tag `share of ticket money: none`.
  - *Counter callback (CSS):* small dark card from 7.8, now static: `NEW STADIUMS: 0` -
    continuity between the two 2026 beats.
  - *Payoff card:* torn-paper cream card, two-line hand lettering: `BUILD NOTHING.` then
    `STILL PAY.` (the second line slams in red).
  - *Receipt strip:* the motif rolls quietly along the bottom edge on the final beat -
    the section's last word belongs to the receipt.
- **Mascot:** pose `shrug_both_hands_up_smile` (library); placement CENTER-LEFT GIANT,
  ~1/2 frame, hips crop; facing camera; expression: resigned smiling shrug - "that is
  the system, folks". The section's thesis, embodied.
- **On-screen text:** `US CITIES:` paints on the plate on US@59.34; `$100M+` ticks on
  $100@61.04 (readable by million@61.46); giant red stamp `EACH.` (impact) on Each@62.86;
  ticket icon + `share of ticket money: none` hard-show on ticket@~64.26; payoff card
  `BUILD NOTHING.` on Build@~65.04, `STILL PAY.` slams (impact) on Still@~66.04; counter
  callback `NEW STADIUMS: 0` visible from the cut. All cue-critical text sits above the
  subtitle-safe zone; only the decorative receipt lives at the bottom edge.
- **Emotion:** wry resignation - even the best-case year proves the thesis.
- **Insight / joke:** the cities finally did everything right - built nothing - and the
  bill still came. The receipt rolls anyway.
- **Linkage / eye path:** WIT's open shrug hands the eye to the bill stack (right); the
  `EACH.` stamp welds the price to the stack; the crossed ticket floats between WIT and
  the stack - the money that will never arrive; the payoff card crowns the frame; the
  receipt underlines the floor and carries the motif into S8.
- **Show-as-you-say:** cut on And@58.68 (base + giant WIT + bill stack + counter callback
  from cut); `US CITIES:` on US@59.34; `$100M+` on $100@61.04 (small impact tick);
  `EACH.` stamp (impact) on Each@62.86; ticket icon + `none` tag on ticket@~64.26
  (interpolated tail); `BUILD NOTHING.` hard-shows ~65.04; `STILL PAY.` slams (impact)
  ~66.04; receipt strip unrolls along the bottom from pay@~66.34 with the printer tick
  returning; hold to 66.987, hard cut to S8.
- **Sound:** paper thump on 61.04; heavy stamp thud on 62.86; a dry, dampened "no-sale"
  cash-register clack on the crossed ticket (~64.26); printer tick-tick resumes on
  ~66.34 as the audio handoff into S8.
- **Color / contrast:** stone gray base; the white invoice stack is the brightest
  object; red stamp + red X accents; cream payoff card with black + red lettering.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `city-hall-columns-1.jpg` | browse-real-photo | generic stone civic building facade with columns, straight-on, no landmark, no signage, no people | full-bleed base | new |
| `bill-stack-invoices.png` | generate | thick stack of white paper invoices with ruffled edges, bound by one red rubber band, faint unreadable print, isolated, transparent bg | right-center on steps, ~24% width | new |
| `shrug_both_hands_up_smile.png` | pose | library pose, resigned smiling shrug | center-left giant, ~1/2 frame, hips crop | reuse (library) |
| `receipt-endless-roll.png` | reuse | the motif strip, rolling along the bottom edge on the final beat | bottom band 80-92% y, decorative | reuse (S1.3, 7.1) |

## Section Asset Summary

| Filename | Type | First scene | Reused in | Notes |
|---|---|---|---|---|
| `wit-tiny-taxpayer-catching-receipt.png` | generate (NEW pose) | 7.1 | placed 3x in 7.1 (crowd) | section 7 signature; strong shared-registry candidate for S8 |
| `podium-suits-trio.png` | generate | 7.1 | 7.2 (hero), 7.3 (desaturated exit) | the faceless deciders - featureless heads, no real people |
| `receipt-conveyor-machine.png` | generate | 7.1 | - | script-suggested bespoke hero |
| `bill-envelope-overdue.png` | generate | 7.3 | - | text-free; CSS adds stamp + date |
| `prestige-crown-glow.png` | generate | 7.4 | - | prestige made physical |
| `rubber-stamp-red.png` | generate | 7.4 | - | text-free; CSS tags it IMPACT STUDY |
| `ballot-box-wood.png` | generate | 7.5 | - | script-suggested bespoke hero |
| `applause-meter-dial.png` | generate | 7.6 | - | text-free; CSS adds 2034/APPROVED labels |
| `wallet-padlocked-city.png` | generate | 7.7 | - | script-suggested bespoke hero |
| `surplus-jar-coins.png` | generate | 7.7 | - | label-free; CSS adds LA 1984 labels |
| `clickbait-ad-card.png` | generate | 7.8 | - | text-free parody ad frame; CSS adds all copy |
| `bill-stack-invoices.png` | generate | 7.9 | - | print must stay unreadable |
| `trophy-gold-parody.png` | reuse | 7.2 | - | VIDEO HERO from S1; photo-op prop |
| `receipt-endless-roll.png` | reuse | 7.1 | 7.9 | VIDEO MOTIF from S1; conveyor feed + closing roll |
| `rope-tug-frayed-1.jpg` | browse-real-photo | 7.1 | - | no hands/people |
| `red-carpet-stanchions-1.jpg` | browse-real-photo | 7.2 | - | empty photo-op stage |
| `map-atlas-colored-1.jpg` | browse-real-photo | 7.3 | - | DISTINCT from S1's vintage parchment map; bright modern atlas |
| `calculator-spreadsheet-1.jpg` | browse-real-photo | 7.4 | - | no brand on calculator |
| `voting-booth-1.jpg` | browse-real-photo | 7.5 | - | empty booth, no signage |
| `auditorium-seats-1.jpg` | browse-real-photo | 7.6 | - | no venue branding |
| `palm-trees-sky-1.jpg` | browse-real-photo | 7.7 | - | LA vibe, no landmarks |
| `crt-monitor-retro-1.jpg` | browse-real-photo | 7.8 | - | no brand marks |
| `city-hall-columns-1.jpg` | browse-real-photo | 7.9 | - | generic civic facade, no landmark |
| library poses (9) | pose | 7.1-7.9 | - | shrug_confused_flat_mouth, unimpressed_smirk_closeup, pointing_at_globe_explaining, mildly_surprised_hand_at_chin, furious_shouting_anger_mark, deadpan_unimpressed_half_lidded, ok_hand_sign_content_closeup, smug_sly_smirk_leaning, shrug_both_hands_up_smile |

## Approval Checks

- each scene picturable from text alone: yes - every scene fixes the base photo, element
  positions in %, z-order, exact text, and entrance beats.
- ~one scene per sentence, scene-types varied: yes - 9 scenes over 66.987s; two-beat
  scenes (7.1, 7.3, 7.8, 7.9) are marked and each stays under ~9.4s on one base; rotation
  runs question board -> photo-op gag -> map gag -> form board -> ballot tally -> meter
  hero -> evidence pair -> parody ad -> payoff board.
- every scene has a real/real-looking base: yes - 9 fresh people-free, brand-free photo
  bases, all bright (~0.75-0.85), none reused from other sections, none repeated inside
  this section.
- mascot big/high with a specific pose+expression per scene: yes - giant on 7.1/7.5/7.9,
  minimum ~1/3 elsewhere; head + glasses + torso always inside frame, only legs crop; no
  pose repeats within the section; sides run C-R-L-R-L-R-L-CR-CL (never the same side
  twice in a row).
- show-as-you-say timeline present per scene: yes - every entrance pinned to a
  word@time; hard-show vs impact marked; the 7.9 tail cues are explicitly flagged as
  interpolated (~) because of the JSON's non-monotonic tail, and the scene end is clamped
  to the real 66.987s.
- every asset has type + description + filename + layout: yes - per-scene tables plus the
  section summary; 12 generate, 9 browse bases, 2 registry reuses, 9 library poses, 1 new
  WIT pose.
- repeated subjects reuse the same filename: yes - `trophy-gold-parody.png` and
  `receipt-endless-roll.png` reused from the shared registry unchanged;
  `podium-suits-trio.png` reused across 7.1/7.2/7.3 for decider continuity.
- public figures handled as caricature/parody, punching up: no public figures at all -
  the deciders are faceless generic suited figures; edge aims at incentives and
  institutions; honesty rails visible on screen (OLYMPIC bids tally, `US CITIES` scope,
  `one of the only ones - ever` hedge, `ORGANIZERS' PROFIT` framing, `THE OLYMPICS` tag,
  `*number invented` asterisk, `(by acclamation)` tag).
- no image-generation prompts written here: correct - descriptions only; prompts are
  visual-implement's job.
- in sync with master `04-visual-plan.md`: pending - master currently holds Section 1
  only; the master-assembler must paste this section block into `## All Sections` and
  update the Section Index row (Section 7: planned, 66.987s, 9 scenes, 24 assets named).
