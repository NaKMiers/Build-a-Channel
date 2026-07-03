# Section 9 Visual Plan - Outro: The Cheapest Host On Earth

Video: `Why Countries Fight to Host the World Cup (and Lose Billions)`
Section: `Section 9: Outro: The Cheapest Host On Earth`
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

- Section goal: land the owner's standing outro device - the animated interactive UI
  mockup - as an earned CTA: the channel is the one host on Earth whose receipt reads
  `$0.00`. Retire the receipt motif with its final green print, let a parody "WhyTube"
  card physically perform the like-click and the subscribe-flip, and exit on a dry
  consultant joke. Light, warm, throwaway charm; zero begging, zero fake metrics.
- Duration: `17.877s` (real audio duration; the section is the video's tail after S8's
  calm payoff)
- Timing source: `voiceover/section-09-outro/section-09-word-timings.json`
  (whisper-tiny.en, generated 2026-07-02). Whisper mishearings do not affect timestamps:
  token "explains"@6.32 = script "explained", tokens "100"@9.94 + "%"@10.38 = script
  "one hundred percent". CLAMP: whisper's final "it." runs to 20.2s - the last scene's
  end is clamped to the real `17.877s`.
- Scene count: `2` (target 2-3). Scene 9.2 runs 12.22s - deliberately past the ~10s
  base guideline because the interactive card must hold its clicked state on ONE
  continuous scene (owner-confirmed animated-UI device rule); it stays visibly alive via
  a two-phase push-in at Subscribe@11.32 and ten word-pinned events (precedent: S1.6
  two-phase single scene).
- Scene-type rotation: 9.1 object-hero motif finale (the trophy prints its LAST receipt
  line) -> 9.2 animated interactive UI mockup (two-phase continuous card).
- Mascot arc in this section: WIT sits out 9.1 entirely (the trophy and receipt carry
  the gag) -> one single chill appearance in 9.2 as the "light CTA host" of the master
  arc: a peace-sign peek from behind the parody card on the consultant punchline.

## Scenes

### Scene 9.1 - "By the way, hosting THIS channel costs you nothing. No stadiums. No taxes. No receipt."

- **Local time:** `0.00-5.66` (By@0.00, THIS@1.16, channel@1.52, costs@1.82,
  nothing@2.34, stadiums@3.24, taxes@4.24, receipt@5.12)
- **Role:** the motif finale + the premise of the CTA. S8 ended on the receipt still
  printing quietly in grey-blue; hard cut to warmth: the same trophy prints ONE last
  line - and for the first time all video the total is green. Pays off the S1 hook title
  ("The Trophy Prints A Receipt") and sets up "the cheapest host on Earth" so the like
  and subscribe in 9.2 feel earned, not begged for.
- **Composition / layout:** full-bleed real photo base: a warm-lit wooden cafe counter
  at soft evening glow (fresh file, no people, no brands). Counter surface line at ~62%
  y. The parody golden trophy (REUSED file) stands right-of-center (58-80% x, 26-78% y)
  like a customer settling its tab, warm cozy grade, soft glint. From the slot at its
  dark plinth, the motif receipt (REUSED file) rises and arcs up-left in a gentle
  S-curve; its readable face hangs flat toward camera at 14-52% x, 16-72% y - big
  enough to read on a phone. CSS print lines land on the blank strip top-to-bottom.
  Z-order: base < receipt strip < trophy < print-line text. All receipt text sits above
  the bottom subtitle-safe zone (nothing below ~76% y).
- **Elements:**
  - *Base (full-bleed):* warm wooden cafe counter, soft amber evening light from the
    left, shallow-focus warm bokeh behind, one out-of-focus empty cup far left; bright
    (~0.8), no dark scrim, no logos, no hands, no people.
  - *Trophy (right-of-center, ~22% frame width):* the video's hero parody trophy - gold
    globe on the fluted cup, dark plinth. Warmest, friendliest grade it has had all
    video; one soft specular glint. The receipt slot at the plinth base is where the
    strip emerges - same printer language as S1.3.
  - *Receipt (readable face 14-52% x, 16-72% y):* the endless-receipt asset, composited
    with one gentle curl near the slot, face flat to camera. CSS-overlaid print in a
    faint dot-matrix style (consistent with the item lines it carried in S3/S4/S6):
    header `HOSTING: THIS CHANNEL` in dark grey; item lines with dotted leaders
    `STADIUMS ............ $0` and `TAXES ............ $0` - the `$0` amounts in green
    ink (the first green this receipt has ever printed); then a double rule and a fat
    final line `TOTAL: $0.00` in bold green, slightly larger. At 5.45 the strip TEARS
    just below the TOTAL line: the printed stub drops ~20px, rotates ~2deg, and settles
    flat; the slot goes still.
- **Mascot:** none - WIT deliberately sits this beat out (single-WIT-appearance rule
  for this outro; the trophy and the dying receipt ARE the characters here). His one
  appearance is saved for the punchline scene 9.2.
- **On-screen text:** all of it lives ON the receipt, printing line by line:
  `HOSTING: THIS CHANNEL` (dark grey dot-matrix header) on channel@1.52;
  `STADIUMS ............ $0` on stadiums@3.24; `TAXES ............ $0` on taxes@4.24;
  double rule + `TOTAL: $0.00` (bold green, larger) on receipt@5.12. No handwritten
  labels - the receipt is the single clean device of the beat.
- **Emotion:** cozy relief - after eight sections of bills, the first receipt that
  costs the viewer nothing. A warm exhale.
- **Insight / joke:** the motif retires itself: the trophy that printed billions all
  video prints its last line, and the total is `$0.00` - "no receipt" delivered BY the
  receipt. Every amount all video was a cost; the only green number is the free one.
- **Linkage / eye path:** trophy (right, familiar hero) -> down to the slot at its
  plinth -> up the strip to the readable face (left) -> lines read top-to-bottom as
  they print -> the eye is parked on `TOTAL: $0.00` when the tear-off drops.
- **Show-as-you-say:** hard cut at By@0.00 - base + trophy + blank receipt already in
  place, the S8 printer tick-tick continuing quietly (continuity); header line
  hard-shows with a printer chirp + 2% paper-advance nudge on channel@1.52; item line 1
  hard-shows (chirp + nudge) on stadiums@3.24; item line 2 hard-shows (chirp + nudge)
  on taxes@4.24; `TOTAL: $0.00` is the impact beat on receipt@5.12 - scale-punch
  1.15 -> 1.0 with a brief green flash; the tick SFX stops DEAD at 5.30 and the strip
  tears free at 5.45 (paper-rip, stub settles). Hold the still frame to 5.66.
- **Sound:** the receipt printer tick-tick (the video's signature SFX) carries over the
  cut, quiet; one chirp per printed line; a slightly grander chirp + soft "ding" on the
  TOTAL; tick stops mid-tick at 5.30; paper rip at 5.45; beat of silence into the cut.
- **Color / contrast:** warm amber wood + gold trophy; the white receipt is the
  brightest surface; green `$0` amounts are the only saturated accent - deliberately
  the inverse of every red cost stamp in the video.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `cafe-counter-warm-1.jpg` | browse-real-photo | warm-lit wooden cafe counter at soft evening glow, amber side light, warm bokeh behind, one out-of-focus cup, no people/brands/logos | full-bleed base | new |
| `trophy-gold-parody.png` | reuse | hero parody trophy, warmest grade, printing its final receipt line from the plinth slot | right-of-center, ~22% frame width | reuse (S1 hero) |
| `receipt-endless-roll.png` | reuse | motif receipt strip, one curl at the slot, readable face flat to camera; all print lines are CSS overlays (asset stays text-free) | rises from trophy plinth, face at 14-52% x, 16-72% y | reuse (S1 motif - final appearance) |

### Scene 9.2 - "If this explained something, the like button is right there. It is free, and we keep one hundred percent of it. Subscribe for more stories about money and where it actually goes. No consultants were hired to predict you will enjoy it."

- **Local time:** `5.66-17.877` (If@5.66, something@6.60, like@7.30, there@8.22,
  free@8.92, hundred@9.94 (token "100"), Subscribe@11.32, money@12.86, goes@14.22,
  consultants@15.48, predict@16.66, enjoy@17.32; whisper's final "it." end 20.2 is
  CLAMPED to the real section end 17.877)
- **Role:** the channel's signature outro device - the UI performs the CTA so the
  narrator never has to beg. ONE continuous two-phase scene: Phase A (5.66-11.32) the
  card appears and the cursor clicks LIKE; Phase B (11.32-17.877) a +6% push-in as
  SUBSCRIBE flips, confetti pops, the toast lands, WIT makes his single appearance, and
  the consultant stamp buttons the video. The card holds every flipped state to the end
  - nothing resets.
- **Composition / layout:** full-bleed real photo base: a cozy lamp-lit wooden desk at
  evening (fresh file - NOT 9.1's cafe counter, NOT S1.5's dark desk). Desk surface
  line ~66% y. A white parody "WhyTube" video card floats left-center (6-58% x,
  10-80% y) with a soft drop shadow, perfectly straight. WIT hides BEHIND the card's
  right edge until 15.48, then peeks out at 55-90% x (head at 60-78% x, 20-42% y).
  Handwritten annotation zone top-right (64-90% x, 8-18% y). Stamp zone lower-right
  (62-86% x, 62-74% y). SVG cursor travels on the topmost layer. Z-order: base < WIT
  (behind card) < card < tag/annotation/toast/confetti < stamp < cursor. All
  cue-critical text stays above ~80% y (subtitle-safe).
- **Elements:**
  - *Base (full-bleed):* cozy warm home desk in the evening - wooden desktop, one warm
    lamp glow from the right, small potted plant silhouette, soft golden bokeh
    background; bright (~0.75-0.8), inviting, no people, no brands.
  - *WhyTube card (6-58% x, 10-80% y):* white rounded card (soft 16px-style corners),
    parody UI with our own branding only. Top ~55% of the card: thumbnail art - deep
    navy panel with the tiny parody trophy (REUSED file, ~8% frame width) lit by a
    small warm spotlight and a tiny white CSS receipt doodle curling from its base (a
    wink at 9.1). Below: video title in dark ink across max two lines: `Why Countries
    Fight to Host the World Cup`; channel row: circular amber avatar with a hand-drawn
    white `W` monogram (CSS - deliberately NOT the WIT face, so WIT appears exactly
    once), channel name `Why It Works`, and a grey NON-NUMERIC sub-line `stories about
    money` (where a real card would show a subscriber count - there is none); action
    row: LIKE pill (light grey, dark SVG thumb-up outline icon + word `LIKE`) on the
    left, red SUBSCRIBE pill (white text) on the right. No view counts, no subscriber
    counts, no duration chip - zero numeric UI lines.
  - *SVG cursor:* drawn white arrow cursor with black outline and soft shadow, ~4%
    frame height; slides in from the bottom-right corner along a lazy arc; emits a thin
    expanding click-ring on each press.
  - *LIKE flip state:* on click the pill squash-stretch BOINGS, fills blue, the thumb
    icon tips up 15deg and turns white.
  - *$0.00 tag:* a small green SVG price tag (tag shape, hole + short string) swings
    out and hangs off the LIKE pill's corner, printed `$0.00` - the only thing in the
    whole video with a price tag of zero.
  - *Annotation:* handwritten amber marker `100% ours` top-right with a curved
    hand-drawn arrow down-left to the blue LIKE pill (editorial annotation outside the
    card, quoting the narration - not a UI metric).
  - *SUBSCRIBE flip state:* pill boings and flips red -> light grey, dark text
    `SUBSCRIBED`, and a small SVG bell icon pops in beside the text with a 10deg ring
    wiggle.
  - *Confetti (namespaced `.cfp`):* ~14 small CSS strips and dots (gold/teal/red)
    bursting from the SUBSCRIBE pill, falling ~100px and fading inside 0.8s - localized,
    not full-frame.
  - *Toast:* dark rounded chip with white text `Welcome to the channel!`, sliding up
    over the card's bottom-center (inside card width, fully above 80% y).
  - *Stamp:* green rubber-stamp style rounded rectangle, slightly distressed edges,
    6deg tilt, reading `CONSULTANT-FREE` - certification-label parody (like a food
    label), lower-right zone.
- **Mascot:** pose `peace_sign_calm_open_mouth` (library); placement: peek from BEHIND
  the card's right edge, body 55-90% x, torso half-occluded by the card, head + glasses
  + peace-sign hand fully visible at 60-78% x from 20% y down; scale ~2/5 frame height;
  facing camera; expression: calm open-mouth chill - the zero-pressure "light CTA host"
  of the master arc. His face never covers the card's buttons or toast; the stamp lands
  below his hand, never on his face. This is WIT's ONLY appearance in the section.
- **On-screen text:** card UI text as above (`Why Countries Fight to Host the World
  Cup`, `Why It Works`, `stories about money`, `LIKE`, `SUBSCRIBE` -> `SUBSCRIBED`);
  green tag `$0.00` on free@8.92; handwritten amber `100% ours` + arrow on hundred@9.94;
  toast `Welcome to the channel!` at 11.62; marker underline swipe beneath `stories
  about money` on money@12.86; green stamp `CONSULTANT-FREE` on predict@16.66. All SVG/
  CSS lettering and icons - no emoji glyphs anywhere.
- **Emotion:** warm, cheeky, zero-pressure - the CTA as a friendly demo, not a plea.
- **Insight / joke:** the UI does the asking so the narrator keeps his dry dignity; the
  like button is literally the only item in the video whose price tag reads `$0.00`;
  and the video's villain - the consultant - exits as a parody certification stamp:
  this outro is officially `CONSULTANT-FREE`.
- **Linkage / eye path:** the cursor IS the eye-leader: enters bottom-right -> LIKE
  pill (click, blue) -> the green tag swings the eye to the price joke -> the
  hand-drawn arrow lifts it to `100% ours` (top-right) -> cursor dives to SUBSCRIBE
  (click, confetti, toast below) -> WIT's head rises behind the card's right edge ->
  the stamp thuds in just under his peace sign as the button of the whole video.
- **Show-as-you-say:** hard cut at If@5.66 - base + card pop in together (0.3s soft
  scale-in, whoosh; card in default state: grey LIKE, red SUBSCRIBE); cursor slides in
  from bottom-right starting on something@6.60, easing along its arc to hover the LIKE
  pill by 7.92; CLICK on there@8.22 (impact: click-ring + boing + blue fill + thumb
  tip); `$0.00` tag swings out (small impact, "fwip") on free@8.92; `100% ours`
  annotation + arrow hard-show with a quick scribble on hundred@9.94; Phase B begins on
  Subscribe@11.32 - cursor darts to SUBSCRIBE, CLICK (impact: boing, red flips to grey
  `SUBSCRIBED`, bell pops in with a ring wiggle, `.cfp` confetti bursts) while the
  whole composition eases into a +6% push-in over 0.8s; toast `Welcome to the channel!`
  slides up at 11.62 (end of the spoken word "Subscribe"); marker underline swipes
  under `stories about money` on money@12.86; the bell gives one tiny wiggle + soft
  ding on goes@14.22; WIT peeks up from behind the card's right edge (0.4s ease, his
  single entrance) on consultants@15.48; `CONSULTANT-FREE` stamp lands (impact, thud)
  on predict@16.66; everything HOLDS in final state - blue like, grey SUBSCRIBED, bell,
  tag, toast, stamp, WIT - to the clamped end at 17.877.
- **Sound:** card pop whoosh at 5.66; faint cursor glide; click + boing at 8.22; tag
  "fwip" at 8.92; marker scribble at 9.94; click + flip + confetti pop + toast swoosh
  at 11.32-11.62; underline squeak at 12.86; tiny bell ding at 14.22; stamp thud at
  16.66. A gentle warm outro music bed fades in under the voice from 11.32 and out at
  17.877; the voice stays on top throughout.
- **Color / contrast:** warm amber desk + clean white card; the blue LIKE fill and the
  red-to-grey SUBSCRIBE flip are the state-change accents; green appears exactly twice
  (`$0.00` tag, `CONSULTANT-FREE` stamp) rhyming with 9.1's green total; confetti is
  sparse gold/teal/red; WIT's white face pops against the warm bokeh.

**Assets:**

| Filename | Type | Description (NO prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `desk-cozy-evening-1.jpg` | browse-real-photo | cozy lamp-lit wooden home desk at evening, warm glow from the right, small plant silhouette, golden bokeh, no people/brands | full-bleed base | new |
| `trophy-gold-parody.png` | reuse | tiny hero trophy inside the parody card's navy thumbnail art, small warm spotlight | inside card thumbnail, ~8% frame width | reuse (9.1 / S1 hero) |
| `pose peace_sign_calm_open_mouth.png` | pose | library chill sign-off pose, single WIT appearance, peeking from behind the card | right of card, ~2/5 frame, torso half-occluded by card | reuse (library) |

## Section Asset Summary

| Filename | Type | First scene | Reused in | Notes |
|---|---|---|---|---|
| `cafe-counter-warm-1.jpg` | browse-real-photo | 9.1 | - | warm cafe counter; deliberately NOT a living-room/mantel subject (S8 owns that) |
| `trophy-gold-parody.png` | reuse | 9.1 | 9.2 (card thumbnail) | VIDEO HERO from S1; final two appearances |
| `receipt-endless-roll.png` | reuse | 9.1 | - | VIDEO MOTIF from S1; final print `TOTAL: $0.00` + tear-off retires it; all print text is CSS |
| `desk-cozy-evening-1.jpg` | browse-real-photo | 9.2 | - | cozy warm desk behind the floating UI card (fresh file, this section only) |
| `pose peace_sign_calm_open_mouth.png` | pose | 9.2 | - | WIT's single Section 9 appearance; library pose |

All interactive UI parts of 9.2 (card, buttons, SVG cursor, click rings, `$0.00` tag,
toast, bell, confetti `.cfp`, stamps, annotations) are CSS/SVG built at render time per
the animated-interactive-UI device rules - no image files, no emoji glyphs.

## Approval Checks

- each scene picturable from text alone: yes - both scenes specify base, positions in
  %, z-order, every element's look, and every state change with its exact trigger word.
- ~one scene per sentence, scene-types varied: yes with one documented exception - 9.1
  covers the four short opening sentences as one printing device (one thought: "hosting
  this channel is free"); 9.2 is the owner's continuous interactive-UI scene and runs
  12.22s past the ~10s guideline BECAUSE the card must hold its clicked state on one
  continuous scene (device rule; two-phase push-in at 11.32 keeps it alive). Types: object-hero
  motif finale vs animated interactive UI - fully distinct.
- every scene has a real/real-looking base: yes - `cafe-counter-warm-1.jpg` (9.1) and
  `desk-cozy-evening-1.jpg` (9.2), both fresh, people-free, brand-free, bright
  (~0.75-0.8, no dark scrims).
- mascot big/high with a specific pose+expression per scene: 9.2 yes - ~2/5 frame peek,
  head + glasses + peace hand fully inside frame, calm open-mouth expression. 9.1 has
  NO WIT by design (section spec: WIT appears exactly once in this outro; props carry
  9.1).
- show-as-you-say timeline present per scene: yes - every entrance is pinned to a real
  whisper timestamp and marked hard-show vs impact; final scene end clamped to 17.877s.
- every asset has type + description + filename + layout: yes - see per-scene tables
  and the summary.
- repeated subjects reuse the same filename: yes - `trophy-gold-parody.png` and
  `receipt-endless-roll.png` are reused by their exact registry filenames; no renames,
  no recreations.
- public figures handled as caricature/parody, punching up: no public figures appear;
  the parody targets are the consultant-as-role (stamp) and platform UI conventions
  ("WhyTube", own branding only). Script approval rails honored: CTA earned by the
  hosting/receipt metaphor, like + subscribe named simply, no begging, and NO fake
  numbers - the card carries zero numeric UI lines (non-numeric `stories about money`
  where a count would sit); the only numerals on screen are `$0.00` / `$0` (the
  scripted joke) and the handwritten `100% ours` annotation quoting the narration
  (editorial note, not a metric).
- no image-generation prompts written here: correct - descriptions only; prompt writing
  belongs to visual-implement.
- in sync with master `04-visual-plan.md`: pending - this section file is the source
  slice; the master-assembler pastes it into the master (this task does not edit the
  master). Continuity hooks match the master's stated plan: receipt final S9 print
  `TOTAL: $0.00`, trophy reuse, WIT as "light CTA host".
