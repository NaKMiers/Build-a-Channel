# Asset Manifest

Video: `Why Countries Fight to Host the World Cup (and Lose Billions)`
Scope: Sections 1-9 (ALL) - from each `visual-plan/section-XX-*/section-XX-*-visual-plan.md`
Updated: 2026-07-06 (visual-implement: Sections 4-9 run - poses copied, 50 generate prompts written,
38 browse bases sourced + 1 generate fallback `tv-wall-glow`; Sections 1-3 runs 2026-07-02..07-06)

Status legend: `done` (file present) / `prompt-ready / awaiting generation` (owner pastes the
prompt into ChatGPT, attaches the named reference, drops the PNG into `assets/` under the exact
filename) / `reused` (already existed).

## Section 1 Manifest


| Done | Filename                                     | Type                | Used in scenes                             | Description                                                                                                                                                              | Prompt / Source                                                             | Status                               |
| ---- | -------------------------------------------- | ------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- | ------------------------------------ |
| [ ]  | `trophy-gold-parody.png`                     | generate            | 1.1, 1.2, 1.3, 1.5, 1.6 (+ later sections) | VIDEO HERO: parody golden trophy (gold globe on fluted cup, dark plinth), isolated, transparent                                                                          | Prompt G1 below                                                             | `prompt-ready / awaiting generation` |
| [ ]  | `receipt-endless-roll.png`                   | generate            | 1.3, 1.6, 1.7 (+ later sections)           | VIDEO MOTIF: long white receipt strip, faint unreadable print, one curl, transparent                                                                                     | Prompt G2 below                                                             | `prompt-ready / awaiting generation` |
| [ ]  | `wit-fan-flag-cheer.png`                     | generate (NEW pose) | 1.1                                        | WIT as euphoric fan: teal scarf + small plain teal pennant, huge cheer                                                                                                   | Prompt G3 below (attach `_origin_.png`)                                     | `prompt-ready / awaiting generation` |
| [ ]  | `wit-fan-frozen-mid-cheer.png`               | generate (NEW pose) | 1.3                                        | same fan kit + pose, face flipped to blank dread + sweat drop                                                                                                            | Prompt G4 below (attach `_origin_.png` + finished `wit-fan-flag-cheer.png`) | `prompt-ready / awaiting generation` |
|      | `poses/skeptical_side_eye_doubtful.png`      | pose                | 1.2                                        | library pose copy                                                                                                                                                        | `.agents/_shared/assets/wit/poses/`                                         | `done`                               |
|      | `poses/pondering_skeptical_hand_on_chin.png` | pose                | 1.4                                        | library pose copy                                                                                                                                                        | same                                                                        | `done`                               |
|      | `poses/deadpan_unimpressed_half_lidded.png`  | pose                | 1.5                                        | library pose copy                                                                                                                                                        | same                                                                        | `done`                               |
|      | `poses/hand_on_cheek_surprised_curious.png`  | pose                | 1.6                                        | library pose copy                                                                                                                                                        | same                                                                        | `done`                               |
|      | `poses/pointing_up_curious_open_mouth.png`   | pose                | 1.7                                        | library pose copy                                                                                                                                                        | same                                                                        | `done`                               |
|      | `poses/_origin_.png`                         | pose (reference)    | generation handoff only                    | canonical neutral identity - attach when generating G3/G4                                                                                                                | same                                                                        | `done`                               |
|      | `stadium-fireworks-1.jpg`                    | browse-real-photo   | 1.1                                        | giant multicolor festival firework over a glittering night town (celebration-night base; trophy+confetti+WINNER carry the "won the Cup" meaning)                         | see ATTRIBUTION.md (CC BY 4.0)                                              | `done`                               |
|      | `podium-spotlight-1.jpg`                     | browse-real-photo   | 1.2                                        | single spotlight beam cutting through darkness; trophy sits at the beam's landing                                                                                        | see ATTRIBUTION.md (CC BY 2.0)                                              | `done`                               |
|      | `world-map-vintage-1.jpg`                    | browse-real-photo   | 1.3                                        | 1550s parchment mappemonde (Jomard/Henri II); vertical fold seam near center - crop right-of-seam or hide seam behind the trophy podium                                  | see ATTRIBUTION.md (PD)                                                     | `done`                               |
|      | `ledger-red-pen-1.jpg`                       | browse-real-photo   | 1.4                                        | blank aged ledger page, red center rule, alphabet index tabs (no pen/figures in photo - the handwritten verdict + CSS red marks carry the scene; filename kept per plan) | see ATTRIBUTION.md (PD)                                                     | `done`                               |
|      | `desk-darkwood-1.jpg`                        | browse-real-photo   | 1.5                                        | dark wood planks with moody spotlight vignette (960w preview - swap if soft at 1920)                                                                                     | see ATTRIBUTION.md (CC0)                                                    | `done`                               |
|      | `gold-bokeh-black-1.jpg`                     | browse-real-photo   | 1.6                                        | warm gold string-light bokeh on dark, luxury feel (960w - bokeh upscales safely)                                                                                         | see ATTRIBUTION.md (CC0)                                                    | `done`                               |
|      | `curtain-dark-1.jpg`                         | browse-real-photo   | 1.7                                        | dark red stage curtain, moody; grade darker + heavy vignette at render for the near-black focus beat                                                                     | see ATTRIBUTION.md (CC0)                                                    | `done`                               |


Render gate: Section 1 render is BLOCKED until the four `generate` PNGs are dropped into
`assets/` under their exact filenames.

## Section 1 Generation Prompts



### G1 - `trophy-gold-parody.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a golden championship
trophy with an ORIGINAL, generic design. Structure: a smooth polished gold globe (a
plain sphere with very faint engraved continent outlines) resting on top of a tall
fluted golden cup body with two small elegant curved handles, standing on a short round
dark-bronze plinth. Style: glossy photorealistic studio-product look, warm rich gold
tones, one soft white specular highlight on the upper-left of the globe, gentle
reflections on the cup flutes. Framing: perfectly centered, the whole trophy visible
from top to base, generous transparent margin on all sides. Do NOT include: any text,
numbers, logos, brand marks, flags, ribbons, confetti, background elements, people, or
hands. IMPORTANT: do NOT reproduce or imitate the real FIFA World Cup trophy (no
spiraling human figures holding up a globe, no green stone rings at the base) - this
must read as a clearly different, generic fantasy "world trophy".
```



### G2 - `receipt-endless-roll.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a very long white paper
shop receipt unspooling from a small loose paper roll at the top and flowing downward
like a ribbon, making one soft S-curve, and ending in a dotted tear-off edge at the
bottom. The paper carries faint, generic, light-gray print: thin row lines and small
blurred item-and-price shapes that are clearly NOT readable as real words or numbers.
Style: clean photorealistic paper look, crisp white, very soft shading inside the curves
only, no cast shadow outside the paper. Framing: the full strip visible, centered,
generous transparent margin. Do NOT include: readable text, real numbers, logos,
barcodes, QR codes, hands, a table, or any background.
```



### G3 - `wit-fan-flag-cheer.png` (NEW WIT pose)

Attach: the mascot neutral pose (`assets/poses/_origin_.png`)

```text
Use the attached character as the EXACT reference for identity, proportions, line
weight, and color: a round bald white-headed cartoon character with a thick uniform
black outline, big rectangular glasses with dot eyes, and expressive eyebrows. Draw the
SAME character - keep the glasses, head shape, and outline identical.

New pose: the character as an ecstatic sports fan mid-cheer. One arm punched high into
the air waving a SMALL plain teal pennant flag on a short stick (a simple solid teal
triangle - NOT any real country's flag, no emblem, no stripes). The other hand is a
fist pumped at chest height. Mouth wide open in a huge joyful cheer, eyes squeezed shut
with joy, eyebrows high. Two or three small motion lines near the raised arm. Costume:
ONLY a plain solid-teal scarf around the neck; everything else stays the plain white
body with no clothes.

CRITICAL colors: the head, body, and hands are SOLID OPAQUE BRIGHT WHITE (#FFFFFF)
inside the black outline. Do NOT render the character as a black or grey silhouette.
Make the background transparent ONLY outside the black outline - the white inside the
outline must stay opaque.

Framing: FULL BODY from head to feet, centered, generous margin. Output: a single PNG
with a fully transparent background, no ground shadow, no text, no logos.
```



### G4 - `wit-fan-frozen-mid-cheer.png` (NEW WIT pose)

Attach: TWO images - (1) the mascot neutral pose (`assets/poses/_origin_.png`),
(2) the finished `wit-fan-flag-cheer.png` (generate G3 first)

```text
Attached are TWO images of the same cartoon mascot: image 1 is the neutral identity
reference; image 2 is the mascot as a cheering sports fan (teal scarf, small teal
pennant flag). Draw the SAME mascot with the SAME identity as image 1 (round bald white
head, thick uniform black outline, big rectangular glasses, dot eyes) wearing the EXACT
same costume as image 2 (same plain teal scarf, same small plain teal pennant on a
stick) and holding the SAME body pose as image 2 (one arm still punched high with the
pennant, other fist still raised at chest height).

BUT the celebration has died on his face: eyes now wide OPEN and blank with small dot
pupils, eyebrows raised in dread, mouth reduced to a tiny flat line, one large sweat
drop on the temple. The body is stiff and frozen mid-cheer - a joyful pose with a
horrified face. Add two tiny tension marks near the head. Slightly reduce the color
saturation of the scarf and pennant (about 20% duller than image 2).

CRITICAL colors: head, body, and hands SOLID OPAQUE BRIGHT WHITE (#FFFFFF) inside the
black outline; background transparent ONLY outside the outline; never a silhouette.

Framing: FULL BODY head to feet, same scale and line weight as image 2, centered,
generous margin. Output: a single PNG with a fully transparent background, no ground
shadow, no text, no logos.
```



## Section 2 Manifest

Scope: Section 2 (Reframe: A Purchase, Not An Investment) - from
`visual-plan/section-02-reframe/section-02-reframe-visual-plan.md`. Section 2 uses NO receipt
motif; the trophy hero returns (reused from Section 1).


| Done | Filename                                        | Type                | Used in scenes              | Description                                                                                                                                                                                                            | Prompt / Source                            | Status                                                |
| ---- | ----------------------------------------------- | ------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ----------------------------------------------------- |
|      | `trophy-gold-parody.png`                        | reuse (video hero)  | 2.4, 2.5 (first made in S1) | shared-registry parody trophy - same file as Section 1 (Prompt G1)                                                                                                                                                     | S1 Prompt G1; one PNG serves all sections  | `prompt-ready / awaiting generation` (shared with S1) |
| [ ]  | `red-supercar-generic.png`                      | generate            | 2.3, 2.4                    | generic red wedge supercar, glossy cherry red, badge-free, isolated with soft shadow, ZERO real marque cues                                                                                                            | Prompt S2-G1 below                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `price-tag-blank.png`                           | generate            | 2.4, 2.5                    | blank cream paper swing/price tag on a rough string, one soft bend, TEXT-FREE (CSS supplies STATUS / BILLIONS... / PRESTIGE...)                                                                                        | Prompt S2-G2 below                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `credit-card-taxpayer.png`                      | generate            | 2.4                         | oversized parody credit card, gold-tinted, generic chip, embossed `TAXPAYER`, NO network logos/holograms                                                                                                               | Prompt S2-G3 below                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `wit-pool-float-shades.png`                     | generate (NEW pose) | 2.1                         | WIT as vacation believer: teal swim ring, black sunglasses, tiny umbrella drink, blissful open-mouth smile                                                                                                             | Prompt S2-G4 below (attach `_origin_.png`) | `prompt-ready / awaiting generation`                  |
|      | `poses/lecturing_finger_raised_eyes_closed.png` | pose                | 2.2                         | library truth-teller pose copy                                                                                                                                                                                         | `.agents/_shared/assets/wit/poses/`        | `done`                                                |
|      | `poses/rich_flex_gold_chain_sunglasses.png`     | pose                | 2.3                         | library flex pose copy                                                                                                                                                                                                 | same                                       | `done`                                                |
|      | `poses/panic_hands_on_cheeks_scream.png`        | pose                | 2.4                         | library peak-panic pose copy                                                                                                                                                                                           | same                                       | `done`                                                |
|      | `poses/skeptical_side_eye_doubtful.png`         | pose                | 2.5                         | library squint pose (already copied in S1.2 - same file keeps WIT consistent)                                                                                                                                          | same                                       | `done` (reused)                                       |
|      | `resort-pool-1.jpg`                             | browse-real-photo   | 2.1                         | sunny tropical resort pool, turquoise water, empty loungers, palms, no people, no brand signage (portrait original cropped to 16:9, left edge trimmed to drop one sunbather)                                           | see ATTRIBUTION.md (CC0)                   | `done`                                                |
|      | `calculator-desk-1.jpg`                         | browse-real-photo   | 2.2                         | clean brand-free desktop calculator, no hands/people, isolated on a plain dark surface (base has no white paper; render supplies the CSS white paper sheets for the INVESTMENT?/PURCHASE markup + red display overlay) | see ATTRIBUTION.md (CC0)                   | `done`                                                |
|      | `showroom-floor-1.jpg`                          | browse-real-photo   | 2.3                         | glossy pale reflective lobby floor, floor-to-ceiling daylight windows, no cars/dealer logos/people (chrome bollards in mid-ground are minor and sit behind the composited car)                                         | see ATTRIBUTION.md (CC0)                   | `done`                                                |
|      | `marble-counter-1.jpg`                          | browse-real-photo   | 2.4                         | clean white-gray Carrara marble surface (cropped from a flat-lay's prop-free right region, upscaled to 1920x1080 - soft, low-frequency veining tolerates it; render adds the boutique blurred backdrop)                | see ATTRIBUTION.md (CC0)                   | `done`                                                |
|      | `wallet-empty-1.jpg`                            | browse-real-photo   | 2.5                         | open empty brown leather wallet, card slots visibly empty, no brand, isolated on white studio bg (render places it on warm wood - e.g. grade or reuse `desk-darkwood-1.jpg` as the table)                              | see ATTRIBUTION.md (CC0)                   | `done`                                                |


Render gate: Section 2 render is BLOCKED until the four Section-2 `generate` PNGs
(`red-supercar-generic.png`, `price-tag-blank.png`, `credit-card-taxpayer.png`,
`wit-pool-float-shades.png`) AND the shared `trophy-gold-parody.png` are dropped into
`assets/` under their exact filenames.

Sourcing notes (Section 2 browse pass, 2026-07-06): calculator/marble/showroom/pool blind
picks failed the pixel check often (people, brands - Canon/Sharp, currency portraits, a
blurred person in a marble-counter background, a crowded water park). Every accepted base was
Read-verified people-free + brand-free. Two plan-differences were accepted and are covered by
render: the calculator base has no white paper (render draws the paper), and the wallet is on a
white studio bg (render places it on wood). These are consistent with the master; no scene
meaning changes.

## Section 2 Generation Prompts



### S2-G1 - `red-supercar-generic.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a modern high-performance
two-door sports supercar with an ORIGINAL, generic design, shown in a three-quarter front
view (front and one side visible). Body: low, wide, and aggressive with a smooth wedge
profile, glossy cherry-red paint with soft studio reflections, a plain badge-free nose, slim
dark headlights, a subtle front splitter, and plain dark multi-spoke wheels with dark tinted
windows. Style: glossy photorealistic studio-product render, one soft white specular highlight
along the top body line, sitting on its own soft contact shadow directly under the car.
Framing: the whole car visible from bumper to bumper, centered, generous transparent margin on
all sides. Do NOT include: any text, numbers, brand names, manufacturer emblems or logos,
license plate text, a prancing-horse or bull or any real marque badge, dealership signage,
people, hands, or any background. IMPORTANT: this must read as a clearly ORIGINAL, generic
"expensive red supercar" - do NOT reproduce or imitate any real Ferrari, Lamborghini, or other
identifiable production model or its trademarked details.
```



### S2-G2 - `price-tag-blank.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single blank retail swing
price tag (a small rectangular cream-white card, one rounded corner with a metal-rimmed hole)
hanging from a short length of thin rough natural string that makes one soft loop at the top.
The tag hangs at a slight tilt and has one gentle bend/curl in the card so it looks like real
paper. Style: clean photorealistic paper look, soft warm cream tone, very subtle shading and a
faint self-shadow inside the curl only, no cast shadow outside the tag. Framing: the whole tag
and its string loop visible, centered, generous transparent margin. IMPORTANT: the card face
must be COMPLETELY BLANK - do NOT include any text, letters, numbers, prices, currency symbols,
barcodes, QR codes, logos, or printed lines (on-screen words are added later). Do NOT include
hands, a product, a table, or any background.
```



### S2-G3 - `credit-card-taxpayer.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single oversized generic
credit card shown at a slight three-quarter angle. Design: rounded-corner rectangular plastic
card with a warm gold-tinted brushed-metal finish, a small plain square gold EMV chip on the
left, and one line of raised EMBOSSED capital letters reading exactly `TAXPAYER` across the
lower half (the letters catch a soft light along their raised edges). Style: glossy
photorealistic product render with soft reflections and one gentle specular highlight, sitting
on its own soft contact shadow. Framing: the whole card visible, centered, generous transparent
margin. The ONLY text anywhere on the card is the single embossed word `TAXPAYER`. Do NOT
include: any bank name, any payment-network logo or symbol (no Visa, Mastercard, Amex, or any
circles/logos), no hologram, no real or fake card numbers, no expiry date, no signature strip
text, no magnetic stripe text, no people, no hands, and no background.
```



### S2-G4 - `wit-pool-float-shades.png` (NEW WIT pose)

Attach: the mascot neutral pose (`assets/poses/_origin_.png`)

```text
Use the attached character as the EXACT reference for identity, proportions, line weight, and
color: a round bald white-headed cartoon character with a thick uniform black outline, big
rectangular glasses, dot eyes, and expressive eyebrows. Draw the SAME character - keep the head
shape and outline identical.

New pose: the character on holiday, lounging happily inside a plain solid-teal inflatable swim
ring that sits around his middle (as if floating). He wears simple black sunglasses over his
big rectangular glasses (the glasses frames still visible), a relaxed open-mouth blissful smile,
eyebrows raised in contentment. One hand holds a tiny tropical drink in a small glass with a
little paper cocktail umbrella and a straw; the other arm rests lazily on the swim ring. His
short legs stick out forward, relaxed. Add two or three tiny sparkle/relaxation marks near his
head. Costume: ONLY the black sunglasses and the teal swim ring - everything else stays the
plain white body with no clothes.

CRITICAL colors: the head, body, arms, and hands are SOLID OPAQUE BRIGHT WHITE (#FFFFFF) inside
the black outline. Do NOT render the character as a black or grey silhouette. Make the
background transparent ONLY outside the black outline - the white inside the outline must stay
opaque. Do NOT draw any water, pool, or ground - the swim ring and character float on a fully
transparent background.

Framing: FULL BODY head to feet, centered, generous margin. Output: a single PNG with a fully
transparent background, no ground shadow, no text, no logos.
```



## Section 3 Manifest

Scope: Section 3 (The Promise Machine) - from
`visual-plan/section-03-promise-machine/section-03-promise-machine-visual-plan.md`. 8 scenes.
The receipt motif returns (reuse from S1). Note: the planned browse base `mailbox-red-1.jpg`
was switched to a GENERATE isolated element `mailbox-red-generic.png` (documented fallback -
every real red postbox carries a national emblem / royal cypher / postal branding, which the
plan bans; a generic generated postbox is brand-safe and controllable). Render supplies the
sunny-street bokeh backdrop behind it (CSS warm bokeh, or a softened reuse of
`gold-bokeh-black-1.jpg` graded warm/bright).


| Done | Filename                                               | Type                            | Used in scenes | Description                                                                                                                                                   | Prompt / Source                      | Status                                                |
| ---- | ------------------------------------------------------ | ------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ----------------------------------------------------- |
|      | `receipt-endless-roll.png`                             | reuse (video motif)             | 3.1            | endless receipt (born S1.3); OPTIMISM $2,000,000 line item is CSS on top                                                                                      | S1 Prompt G2; shared motif file      | `prompt-ready / awaiting generation` (shared with S1) |
| [ ]  | `promise-machine-contraption.png`                      | generate                        | 3.1            | brass fortune-teller carnival cabinet: glass dome + gold sparkles, scrollwork, side crank, coin slot, wide output slot; blank front (plaque is CSS); isolated | Prompt S3-G1                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `impact-study-document.png`                            | generate                        | 3.2, 3.3, 3.8  | glossy parody report: navy cover, gold title `ECONOMIC IMPACT STUDY`, gold rule, firm mark `Big Numbers & Partners`; isolated                                 | Prompt S3-G2                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `horoscope-spreadsheet-scroll.png`                     | generate                        | 3.2, 3.8       | midnight-purple scroll, gold zodiac-glyph ring, body = ruled spreadsheet grid + faint numbers + gold constellation lines; isolated                            | Prompt S3-G3                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `balloon-shiny-gold.png`                               | generate                        | 3.3, 3.4       | glossy round gold party balloon, white highlight, short string, BLANK surface (labels are CSS); isolated                                                      | Prompt S3-G4                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `balloon-shiny-teal.png`                               | generate                        | 3.3, 3.4       | glossy round teal party balloon, same style, blank, string; isolated                                                                                          | Prompt S3-G5                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `wit-hypnotized-numbers.png`                           | generate (NEW pose)             | 3.3            | WIT full body, head up, awed "o" mouth, pupils replaced by rising-digit streams + upward spiral inside the glasses; no costume                                | Prompt S3-G6 (attach `_origin_.png`) | `prompt-ready / awaiting generation`                  |
| [ ]  | `red-pushpin-giant.png`                                | generate                        | 3.4            | oversized red pushpin: glossy round red head, steel needle, point leading; isolated                                                                           | Prompt S3-G7                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `suitcase-vintage-tourist.png`                         | generate                        | 3.5            | worn vintage leather suitcase, brass corners, a few generic shape stickers (sun, wave, mountain - no flags/brands/city names); isolated                       | Prompt S3-G8                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `airmail-envelope-ticket.png`                          | generate                        | 3.6            | white airmail envelope (red-blue chevron border, plain `AIR MAIL`), generic parody `BOARDING PASS` ticket poking out (plane silhouette, no airline); isolated | Prompt S3-G9                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `banknote-hundred-parody.png`                          | generate                        | 3.7            | generic parody banknote: mint-green, `100` corners, laurel-wreathed globe center oval (no person, not a real currency), guilloche border; isolated            | Prompt S3-G10                        | `prompt-ready / awaiting generation`                  |
| [ ]  | `coin-gold-one.png`                                    | generate                        | 3.7 (x2)       | single gold coin embossed `1`, slight perspective, soft shine; isolated                                                                                       | Prompt S3-G11                        | `prompt-ready / awaiting generation`                  |
| [ ]  | `coin-gold-half.png`                                   | generate                        | 3.7            | half-sized gold coin embossed `50`, same style; isolated                                                                                                      | Prompt S3-G12                        | `prompt-ready / awaiting generation`                  |
| [ ]  | `mailbox-red-generic.png`                              | generate (fallback, was browse) | 3.6            | generic bright red street postbox, NO national emblem / royal cypher / postal branding / text; isolated, transparent (render adds the sunny bokeh backdrop)   | Prompt S3-G13                        | `prompt-ready / awaiting generation`                  |
|      | `poses/proud_explaining_hand_on_chest_hand_on_hip.png` | pose                            | 3.1            | library mock-grand showman                                                                                                                                    | `.agents/_shared/assets/wit/poses/`  | `done`                                                |
|      | `poses/unimpressed_smirk_closeup.png`                  | pose                            | 3.2            | library dry-smirk closeup                                                                                                                                     | same                                 | `done`                                                |
|      | `poses/smug_raised_eyebrow_smirk.png`                  | pose                            | 3.4            | library reality-auditor smirk                                                                                                                                 | same                                 | `done`                                                |
|      | `poses/shocked_sweating_dismayed.png`                  | pose                            | 3.5            | library bill-shock reaction                                                                                                                                   | same                                 | `done`                                                |
|      | `poses/shrug_both_hands_up_smile.png`                  | pose                            | 3.6            | library nonchalant shrug                                                                                                                                      | same                                 | `done`                                                |
|      | `poses/exhausted_dead_inside_eye_bags.png`             | pose                            | 3.7            | library dead-inside stare                                                                                                                                     | same                                 | `done`                                                |
|      | `poses/reading_book_round_glasses_studious.png`        | pose                            | 3.8            | library studious economist                                                                                                                                    | same                                 | `done`                                                |
|      | `fairground-lights-1.jpg`                              | browse-real-photo               | 3.1            | glowing carnival booth at dusk, people-free (cropped from a midway shot), bulb strings; render blurs as background                                            | see ATTRIBUTION.md (CC BY 2.0)       | `done`                                                |
|      | `marble-boardroom-1.jpg`                               | browse-real-photo               | 3.2            | dark green-black marble texture; render adds warm spotlight pool                                                                                              | see ATTRIBUTION.md (CC BY 2.0)       | `done`                                                |
|      | `blue-sky-clouds-1.jpg`                                | browse-real-photo               | 3.3            | bright blue sky + puffy cumulus, no ground/people                                                                                                             | see ATTRIBUTION.md (CC0)             | `done`                                                |
|      | `airport-arrivals-1.jpg`                               | browse-real-photo               | 3.4            | empty gate lounge, no people; distant Delta tails through window (render blurs the window band)                                                               | see ATTRIBUTION.md (CC0)             | `done`                                                |
|      | `baggage-carousel-1.jpg`                               | browse-real-photo               | 3.5            | empty baggage carousel belt curving through frame, no signage                                                                                                 | see ATTRIBUTION.md (CC0)             | `done`                                                |
|      | `stadium-turnstile-1.jpg`                              | browse-real-photo               | 3.7            | metro turnstile row (substitutes for stadium turnstiles), people-free, no brand                                                                               | see ATTRIBUTION.md (CC0)             | `done`                                                |
|      | `party-aftermath-1.jpg`                                | browse-real-photo               | 3.8            | confetti + streamers on the ground, no people/brands (concrete; render warm-grades + adds deflated balloons)                                                  | see ATTRIBUTION.md (CC BY 2.0)       | `done`                                                |


Render gate: Section 3 render is BLOCKED until the 13 Section-3 `generate` PNGs (S3-G1..G13)
AND the shared `receipt-endless-roll.png` are dropped into `assets/` under their exact
filenames.

Sourcing notes (Section 3 browse pass, 2026-07-06): several bases needed re-sourcing after
the pixel check rejected people (fairground midway, subway/airport crowds, a person at the
turnstiles), airline liveries, and national/postal branding (Japan Post mark, UK Royal Mail
E-II-R cypher). Accepted substitutions, all Read-verified: a metro turnstile row stands in for
stadium turnstiles; an empty gate lounge (distant liveries blurred at render) stands in for the
arrivals hall; a confetti-on-concrete shot stands in for the wood party floor; the fairground is
a cropped people-free booth; the mailbox became a generated generic postbox (no branding). None
change scene meaning. Title-keyword traps recurred (a "1 06 Red letterbox" result was a
brand-covered cricket stadium).

## Section 3 Generation Prompts



### S3-G1 - `promise-machine-contraption.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: an ornate antique carnival
fortune-teller machine cabinet (like a vintage "ask the oracle" arcade booth), standing
upright. Structure: a tall rectangular wooden-and-brass cabinet with a domed glass top; inside
the glass dome are swirling gold sparkles and soft light. The body has ornate gold scrollwork
on the corners, a large decorative side crank handle on the right side, a small round coin slot,
and a wide horizontal output slot across the lower front. Leave the flat front panel BLANK (a
title plaque is added later). Style: warm photorealistic product render, polished brass and
deep-red lacquered wood, soft golden glow from the dome, gentle reflections, sitting on its own
soft contact shadow. Framing: the whole cabinet visible top to base, centered, generous
transparent margin. Do NOT include: any text, letters, numbers, logos, brand names, a fortune-
teller puppet or face, people, hands, a floor, or any background.
```



### S3-G2 - `impact-study-document.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a thick, glossy premium report /
bound document standing slightly propped up at a shallow three-quarter angle. Cover: deep navy
blue with a subtle linen texture, a big gold-embossed serif title reading exactly `ECONOMIC
IMPACT STUDY` across the upper half, a thin horizontal gold rule beneath it, and a small gold
line of text near the bottom reading exactly `Big Numbers & Partners`. Style: photorealistic
product render, luxurious, with a soft gold foil sheen along the title and gentle page-edge
thickness showing it is a thick report, sitting on its own soft contact shadow. Framing: the
whole document visible, centered, generous transparent margin. The ONLY text is the embossed
`ECONOMIC IMPACT STUDY` and `Big Numbers & Partners`. Do NOT include: any real company name or
logo, any other text or numbers, people, hands, a desk, or any background.
```



### S3-G3 - `horoscope-spreadsheet-scroll.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: an unrolled vertical paper scroll,
hanging open. The scroll paper is a deep midnight-purple parchment. Across the very TOP is a
decorative gold ring/band of GENERIC astrology star-sign style glyphs (invented zodiac-like
symbols, simple gold line icons - NOT real trademarked symbols). The main BODY of the scroll is
a ruled spreadsheet: a faint grid of rectangular cells filled with tiny, faint, blurred gray
numbers that are NOT readable as real figures, and thin gold "constellation" lines connecting
some cells to others like a star chart, with small gold star dots at the joins. The bottom edge
curls slightly. Style: photorealistic paper with soft shading in the curl, mystical but paper-
real. Framing: the full open scroll visible top to bottom, centered, generous transparent
margin. Do NOT include: any readable words or real numbers, real zodiac/brand symbols, people,
hands, or any background.
```



### S3-G4 - `balloon-shiny-gold.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single glossy round helium party
balloon in rich metallic GOLD, with one soft white specular highlight on its upper-left, a small
knotted neck at the bottom, and a short thin curling string hanging down from the knot. Style:
clean photorealistic, smooth reflective surface, subtle soft shadow only where the string curls.
The balloon surface is completely BLANK (no print). Framing: the whole balloon and its string
visible, centered, generous transparent margin. Do NOT include: any text, numbers, logos,
patterns, faces, people, hands, or any background.
```



### S3-G5 - `balloon-shiny-teal.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single glossy round helium party
balloon in bright TEAL, with one soft white specular highlight on its upper-left, a small knotted
neck at the bottom, and a short thin curling string hanging down from the knot. Style: clean
photorealistic, smooth reflective surface, subtle soft shadow only where the string curls. The
balloon surface is completely BLANK (no print). Framing: the whole balloon and its string
visible, centered, generous transparent margin. Do NOT include: any text, numbers, logos,
patterns, faces, people, hands, or any background.
```



### S3-G6 - `wit-hypnotized-numbers.png` (NEW WIT pose)

Attach: the mascot neutral pose (`assets/poses/_origin_.png`)

```text
Use the attached character as the EXACT reference for identity, proportions, line weight, and
color: a round bald white-headed cartoon character with a thick uniform black outline, big
rectangular glasses, dot eyes, and expressive eyebrows. Draw the SAME character - keep the head
shape and outline identical.

New pose: the character is hypnotized, gazing UP in wonder. His head is tilted up and back
slightly, his mouth is a small open awed "o", and his eyebrows are raised high. INSIDE the two
big rectangular glasses lenses, replace the normal dot eyes with tiny upward-rising streams of
small numbers (little ascending digits like 1 2 3 9) and a thin upward spiral in each lens - as
if numbers are floating up and hypnotizing him. Both hands are raised slightly, loose and
mesmerized. No costume - plain white body.

CRITICAL colors: the head, body, and hands are SOLID OPAQUE BRIGHT WHITE (#FFFFFF) inside the
black outline. Do NOT render the character as a black or grey silhouette. Make the background
transparent ONLY outside the black outline - the white inside the outline must stay opaque. The
only small digits allowed anywhere are the tiny number streams INSIDE the glasses lenses.

Framing: FULL BODY head to feet, centered, generous margin. Output: a single PNG with a fully
transparent background, no ground shadow, no text (other than the tiny in-lens digits), no logos.
```



### S3-G7 - `red-pushpin-giant.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single oversized push-pin / map
tack shown at a slight three-quarter angle with the sharp point leading toward the lower-left.
It has a glossy round bright-red plastic head/grip and a shiny polished steel needle. Style:
photorealistic product render, one soft white highlight on the red head, subtle reflection on
the steel, sitting on its own faint soft shadow. Framing: the whole pushpin visible, centered,
generous transparent margin. Do NOT include: any text, numbers, logos, a board or surface,
people, hands, or any background.
```



### S3-G8 - `suitcase-vintage-tourist.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single worn vintage tan leather
suitcase, closed, standing at a slight three-quarter angle, with brass corner caps, two leather
straps with buckles, and a top handle. On its side are a FEW simple generic travel stickers
using only plain flat shapes - a yellow sun, a blue wave, a green mountain triangle - as small
rounded stickers. Style: photorealistic, warm worn leather with soft scuffs, gentle studio light,
sitting on its own soft contact shadow. Framing: the whole suitcase visible, centered, generous
transparent margin. IMPORTANT: the stickers are plain abstract shapes only. Do NOT include: any
national flags, country or city names, brand logos, real place names, any text or numbers,
people, hands, or any background.
```



### S3-G9 - `airmail-envelope-ticket.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single classic white airmail
envelope shown at a slight angle, with the traditional red-and-blue diagonal chevron stripe
border around its edges and small plain lettering reading exactly `AIR MAIL` in the upper-left.
The envelope flap is open at the top and a generic parody boarding-pass ticket is poking out of
it: a small cream ticket stub with the plain words `BOARDING PASS`, a simple flat airplane
silhouette icon, and a couple of faint blank lines (no real numbers). Style: photorealistic
paper, soft shadow where the ticket overlaps the envelope, sitting on its own faint contact
shadow. Framing: the whole envelope and protruding ticket visible, centered, generous transparent
margin. The ONLY text is `AIR MAIL` and `BOARDING PASS`. Do NOT include: any airline name or
logo, real flight numbers, barcodes, a real destination, people, hands, or any background.
```



### S3-G10 - `banknote-hundred-parody.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single generic parody banknote
lying flat, face up, in a landscape orientation. Design: mint-green colour, a large numeral
`100` printed in each of the four corners, an ornate oval frame in the CENTER containing a
laurel-wreathed GLOBE (a simple engraved-style world globe ringed by laurel leaves - NOT any real
person, portrait, or building), and a fine decorative guilloche (swirl) border around the whole
note. Style: photorealistic printed-paper look with fine engraved line detail, subtle paper
texture, soft even light. Framing: the whole note visible, centered, generous transparent margin.
IMPORTANT: this is an ORIGINAL fictional banknote - do NOT reproduce any real currency (no real
US dollar design, no real portrait, no Federal Reserve or country text, no real serial numbers).
The only text is the corner `100` numerals. Do NOT include: people, portraits, hands, or any
background.
```



### S3-G11 - `coin-gold-one.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single shiny gold coin shown at a
slight three-quarter tilt (a low-angle so it reads as a thick round coin), with a plain milled
edge and a large embossed numeral `1` in the center of its face inside a simple raised rim.
Style: photorealistic polished gold with a soft warm highlight and gentle reflection, sitting on
its own faint contact shadow. Framing: the whole coin visible, centered, generous transparent
margin. The ONLY marking is the embossed `1`. Do NOT include: any other text, words, real
currency design, a face or portrait, people, hands, or any background.
```



### S3-G12 - `coin-gold-half.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single shiny gold coin, clearly
SMALLER and thinner-looking than a normal coin (a "half" token), shown at a slight three-quarter
tilt, with a plain milled edge and a large embossed numeral `50` in the center of its face inside
a simple raised rim. Style: photorealistic polished gold with a soft warm highlight and gentle
reflection, sitting on its own faint contact shadow. Framing: the whole coin visible, centered,
generous transparent margin. The ONLY marking is the embossed `50`. Do NOT include: any other
text, words, real currency design, a face or portrait, people, hands, or any background.
```



### S3-G13 - `mailbox-red-generic.png` (fallback: was the browse base `mailbox-red-1.jpg`)

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single generic bright red street
letter-drop postbox / mailbox on a short post, shown at a slight three-quarter angle. Shape: a
simple modern rounded rectangular red box with a horizontal letter slot near the top and a small
closed collection door on the front, mounted on a single dark grey pole. Style: clean
photorealistic, smooth glossy red paint with one soft highlight, sitting on its own soft contact
shadow. IMPORTANT: the postbox is COMPLETELY UNBRANDED - do NOT include any national postal
emblem, royal cypher (no crowns, no letters like E-II-R), postal-service name, collection-time
label, logo, or any text or numbers anywhere on it. Framing: the whole postbox and its post
visible, centered, generous transparent margin. Do NOT include: people, hands, a street, or any
background.
```



## Section 4 Manifest

Scope: Section 4 (FIFA Keeps The Money) - from
`visual-plan/section-04-fifa-keeps-the-money/section-04-fifa-keeps-the-money-visual-plan.md`. 9 scenes.
Introduces the arrow-direction language, the overstuffed gold safe, and generic cash bundles.
`receipt-endless-roll.png` (reuse from S1) prints `16x STADIUM (RETROFIT) ......... $???` in 4.3;
`trophy-gold-parody.png` (reuse from S1) is the auction lot in 4.9.


| Done | Filename                                    | Type                            | Used in scenes   | Description                                                                                                         | Prompt / Source                            | Status                                                |
| ---- | ------------------------------------------- | ------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ----------------------------------------------------- |
| [ ]  | `contract-stack-guarantees.png`             | generate                        | 4.1              | fat askew stack of ~15 white contract pages, blank top page (CSS titles it), isolated                               | Prompt S4-G1                               | `prompt-ready / awaiting generation`                  |
| [ ]  | `wit-mayor-signing.png`                     | generate (NEW pose)             | 4.1              | WIT: blank teal mayoral sash, eyes-closed bliss, signing with a smoking fountain pen                                | Prompt S4-G2 (attach `_origin_.png`)       | `prompt-ready / awaiting generation`                  |
| [ ]  | `gold-safe-fat.png`                         | generate                        | 4.2, 4.5, 4.7    | overstuffed gold safe, bulging sides + bowing door seam, round black dial, isolated                                 | Prompt S4-G3                               | `prompt-ready / awaiting generation`                  |
| [ ]  | `cash-bundle-generic.png`                   | generate                        | 4.2, 4.7, 4.9    | single banknote bundle, generic green bills + plain band, NO real currency, isolated                                | Prompt S4-G4                               | `prompt-ready / awaiting generation`                  |
| [ ]  | `wood-sign-hanging-blank.png`               | generate                        | 4.6              | blank rustic wooden hanging signboard on two ropes, text-free (CSS writes on it), isolated                          | Prompt S4-G5                               | `prompt-ready / awaiting generation`                  |
| [ ]  | `gold-bar-single.png`                       | generate                        | 4.6 (x4 stacked) | single gleaming gold bar, blank raised panel (no text), isolated - render stacks copies                             | Prompt S4-G6                               | `prompt-ready / awaiting generation`                  |
| [ ]  | `money-sack-gold.png`                       | generate                        | 4.8              | fat tied gold-tinted canvas money sack, plain embossed `$` only, isolated                                           | Prompt S4-G7                               | `prompt-ready / awaiting generation`                  |
| [ ]  | `auctioneer-at-podium.png`                  | generate                        | 4.9              | FACELESS suited figure behind a wooden podium, sweeping a money-rake, isolated (institution, not a person)          | Prompt S4-G8                               | `prompt-ready / awaiting generation`                  |
| [ ]  | `wit-auction-winner-paddle.png`             | generate (NEW pose)             | 4.9              | WIT: blank white bidding paddle raised, long folded bill over forearm, proud-but-terrified                          | Prompt S4-G9 (attach `_origin_.png`)       | `prompt-ready / awaiting generation`                  |
|      | `trophy-gold-parody.png`                    | reuse (shared)                  | 4.9              | video hero trophy as the auction lot                                                                                | S1 Prompt G1 (one PNG serves all sections) | `prompt-ready / awaiting generation` (shared with S1) |
|      | `receipt-endless-roll.png`                  | reuse (shared)                  | 4.3              | video motif receipt; CSS prints `16x STADIUM (RETROFIT) ......... $???`                                             | S1 Prompt G2                               | `prompt-ready / awaiting generation` (shared with S1) |
|      | `poses/unimpressed_smirk_closeup.png`       | pose                            | 4.2              | library dry-smirk closeup                                                                                           | `.agents/_shared/assets/wit/poses/`        | `done` (reused)                                       |
|      | `poses/shocked_sweating_dismayed.png`       | pose                            | 4.3              | library dismay pose                                                                                                 | same                                       | `done` (reused)                                       |
|      | `poses/deadpan_unimpressed_half_lidded.png` | pose                            | 4.4              | library signature deadpan                                                                                           | same                                       | `done` (reused)                                       |
|      | `poses/pointing_at_globe_explaining.png`    | pose                            | 4.5              | library geography/pointing pose                                                                                     | same                                       | `done`                                                |
|      | `poses/rich_flex_gold_chain_sunglasses.png` | pose                            | 4.6              | library flex pose                                                                                                   | same                                       | `done` (reused)                                       |
|      | `poses/mildly_surprised_hand_at_chin.png`   | pose                            | 4.7              | library impressed-against-his-will pose                                                                             | same                                       | `done`                                                |
|      | `poses/eyes_closed_talking_open_palm.png`   | pose                            | 4.8              | library calm-concession pose                                                                                        | same                                       | `done`                                                |
|      | `boardroom-table-1.jpg`                     | browse-real-photo               | 4.1              | long dark-wood boardroom table, empty leather chairs, warm daylight, no people/brands                               | see ATTRIBUTION.md                         | `done`                                                |
| [ ]  | `tv-wall-glow-1.jpg`                        | generate (fallback, was browse) | 4.2              | full-frame dark wall of glowing blank white-blue TV screens, no logos/content/people (no license-safe photo exists) | Prompt S4-G10 below                        | `prompt-ready / awaiting generation`                  |
|      | `stadium-construction-crane-1.jpg`          | browse-real-photo               | 4.3              | stadium concrete bowl under construction, tower cranes at dusk, no workers/logos                                    | see ATTRIBUTION.md                         | `done`                                                |
|      | `rubber-stamp-ink-1.jpg`                    | browse-real-photo               | 4.4              | wooden rubber stamp on a red ink pad, bright desk, no readable stamp face/brands                                    | see ATTRIBUTION.md                         | `done`                                                |
|      | `alpine-lake-town-1.jpg`                    | browse-real-photo               | 4.5              | bright alpine lake + peaks + small town; GENERIC (no landmarks), no flags, people-free                              | see ATTRIBUTION.md                         | `done`                                                |
|      | `chessboard-closeup-1.jpg`                  | browse-real-photo               | 4.6              | wooden chessboard mid-game, warm shallow focus, no hands/brands                                                     | see ATTRIBUTION.md                         | `done`                                                |
|      | `vault-door-1.jpg`                          | browse-real-photo               | 4.7              | massive round steel bank vault door, ajar, cool metal, no bank brands/people                                        | see ATTRIBUTION.md                         | `done`                                                |
|      | `balance-scale-brass-1.jpg`                 | browse-real-photo               | 4.8              | antique brass two-pan balance scale on wood, both pans level, no brands                                             | see ATTRIBUTION.md                         | `done`                                                |
|      | `auction-gavel-1.jpg`                       | browse-real-photo               | 4.9              | wooden auctioneer gavel on sound block, warm spotlight, dark room, no people/branding                               | see ATTRIBUTION.md                         | `done`                                                |


Render gate: Section 4 render is BLOCKED until the 9 Section-4 `generate` PNGs (S4-G1..G9), the
`tv-wall-glow-1.jpg` fallback (S4-G10, or a CSS glowing-panel grid built at render), the two shared
reuses (`trophy-gold-parody.png`, `receipt-endless-roll.png`), and the 8 sourced browse bases are in
`assets/`.

Sourcing notes (Section 4 browse pass): 8 of 9 bases sourced license-safe + Read-verified (Openverse
Cloudflare-blocked most of the session, so mostly Wikimedia Commons + rawpixel). Accepted substitutions,
all people/brand-free: `rubber-stamp-ink-1` ink pad reads dark blue not red; `alpine-lake-town-1` is a
pristine natural alpine lake (Lake Tekapo) with NO lakeside town in frame; `balance-scale-brass-1` pans
are not perfectly level (CSS overlays supply the tilt); `stadium-construction-crane-1` cropped to drop
contractor logos; `boardroom-table-1` chairs are black mesh not leather. `tv-wall-glow-1.jpg` could NOT
be sourced license-safe (every screen-wall had faces / readable content / brand logos / QR codes), so it
is a generate fallback (S4-G10).

## Section 4 Generation Prompts



### S4-G1 - `contract-stack-guarantees.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a fat, slightly askew stack of white
A4 legal contract pages, about fifteen pages visible along the side edge, squared but leaning a
little. The TOP page is completely BLANK white (no text at all) so a title can be added later. Show
the paper thickness on the side (many thin page lines) and one slightly dog-eared corner so it reads
as a heavy document. Style: clean photorealistic paper, soft top-down studio light, a faint soft
contact shadow directly under the stack. Framing: the whole stack visible, centered, generous
transparent margin on all sides. Do NOT include: any text, letters, numbers, titles, logos, stamps,
paperclips, a desk, hands, people, or any background.
```



### S4-G2 - `wit-mayor-signing.png` (NEW WIT pose)

Attach: the mascot neutral pose (`assets/poses/_origin_.png`)

```text
Use the attached character as the EXACT reference for identity, proportions, line weight, and color:
a round bald white-headed cartoon character with a thick uniform black outline, big rectangular
glasses with dot eyes, and expressive eyebrows. Draw the SAME character - keep the glasses, head
shape, and outline identical.

New pose: the character as a carefree mayor signing a document. He wears ONLY a wide diagonal
pageant-style sash across his chest in plain solid teal (completely blank - no words, no insignia, no
flag colors or stripes); everything else stays the plain white body with no clothes. His eyes are
closed in blissful contentment with a big happy smile and relaxed high eyebrows. One hand presses
flat on a sheet of paper; the other hand holds a fountain pen mid-signature, and a thin wisp of grey
smoke trails up from the overworked pen tip. Two tiny motion lines by the signing hand.

CRITICAL colors: the head, body, and hands are SOLID OPAQUE BRIGHT WHITE (#FFFFFF) inside the black
outline; only the sash is teal. Do NOT render the character as a black or grey silhouette. Make the
background transparent ONLY outside the black outline - the white inside the outline must stay opaque.

Framing: FULL BODY head to feet, centered, generous margin. Output: a single PNG with a fully
transparent background, no ground shadow, no text, no logos.
```



### S4-G3 - `gold-safe-fat.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a fat, gleaming gold safe that is
comically OVERSTUFFED - its sides bulge outward slightly and the door seam bows outward as if it can
barely contain what is inside. It has a round black combination dial in the center, a small chrome
handle, and thick rounded corners. Style: glossy photorealistic metal render, warm rich gold tones,
one soft white specular highlight on the upper-left, gentle reflections, sitting on its own soft
contact shadow. Framing: the whole safe visible, centered, generous transparent margin. Do NOT
include: any text, numbers, brand names, logos, a keyhole, money spilling out, people, hands, a floor,
or any background.
```



### S4-G4 - `cash-bundle-generic.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single neat bundle of banknotes held
together by one plain paper band around the middle. The bills are a GENERIC light-green colour with
only faint blank rectangular panels and simple scroll edges - NO faces, NO portraits, NO numbers, NO
real currency design of any country. Style: photorealistic paper money, soft even light, subtle edge
shadows between the notes, a faint soft contact shadow under the bundle. Framing: the whole bundle
visible at a slight three-quarter angle, centered, generous transparent margin. Do NOT include: any
readable numbers, currency symbols, real or fake portraits, serial numbers, real-money watermarks,
bank names, logos, hands, or any background.
```



### S4-G5 - `wood-sign-hanging-blank.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a blank rustic wooden hanging signboard
with rounded corners and visible wood grain, suspended from TWO short ropes that meet above it (the
ropes are part of the asset, ending in small loops at the top). The board face is COMPLETELY BLANK
(no text or paint) so writing can be added later. Style: warm photorealistic weathered wood, soft
daylight, gentle shadow in the rope grooves, a faint soft shadow under the board. Framing: the whole
sign and both ropes visible, centered, generous transparent margin. Do NOT include: any text, letters,
numbers, painted words, logos, a wall, a building, people, hands, or any background.
```



### S4-G6 - `gold-bar-single.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single gleaming gold bullion bar
(ingot) shown at a slight three-quarter angle so its top face and one long side are visible, with a
plain rectangular RAISED panel stamped on the top face but NO text or numbers inside that panel.
Style: glossy photorealistic polished gold, one soft warm specular highlight along the top edge,
gentle reflection, sitting on its own faint contact shadow. Framing: the whole bar visible, centered,
generous transparent margin (this single bar will be copied and stacked later). Do NOT include: any
text, numbers, weight or purity marks, logos, other bars, people, hands, or any background.
```



### S4-G7 - `money-sack-gold.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a fat round canvas money sack tied at
the neck with a short rope, bulging full and heavy, in a warm gold-tinted cream canvas. On its front
is ONE large embossed generic dollar-style `$` symbol (a plain currency symbol only - not any real
currency design). Style: photorealistic soft cloth with gentle folds, a soft shadow in the tied neck,
one soft highlight, sitting on its own soft contact shadow - it should look genuinely heavy. Framing:
the whole sack visible, centered, generous transparent margin. Do NOT include: any other text,
numbers, real currency designs, brand names, logos, spilling coins, people, hands, or any background.
```



### S4-G8 - `auctioneer-at-podium.png`

Attach: none

```text
Create ONE isolated figure on a fully transparent background: a generic FACELESS person in a dark
business suit standing behind a wooden auction lectern/podium. The head is a smooth, completely
FEATURELESS blank ovoid - NO eyes, nose, mouth, hair, or any facial features at all (it must read as
an anonymous "institution", not a real person). One arm is mid-sweep, using a wide flat wooden
money-rake to pull loose banknotes toward itself across the podium top. Style: clean flat-shaded
semi-realistic illustration, muted charcoal suit, warm wood podium, a soft contact shadow under the
podium. Framing: the figure from roughly the knees up plus the podium, centered, generous transparent
margin. Do NOT include: any facial features, hair, skin detail, a real person's likeness, text,
numbers, brand names, logos, auction-house signage, other people, or any background.
```



### S4-G9 - `wit-auction-winner-paddle.png` (NEW WIT pose)

Attach: the mascot neutral pose (`assets/poses/_origin_.png`)

```text
Use the attached character as the EXACT reference for identity, proportions, line weight, and color:
a round bald white-headed cartoon character with a thick uniform black outline, big rectangular
glasses with dot eyes, and expressive eyebrows. Draw the SAME character - keep the glasses, head
shape, and outline identical.

New pose: the character as an auction's winning bidder, proud and terrified at once. One arm is raised
high holding a blank white rectangular bidding paddle on a short stick (NO number or text on the
paddle). The other arm cradles an absurdly long folded paper bill/invoice that spills and drapes over
his forearm. His chest is puffed proud, but his eyes are wide and worried and one large sweat drop
sits on his temple. No costume - plain white body.

CRITICAL colors: the head, body, arms, and hands are SOLID OPAQUE BRIGHT WHITE (#FFFFFF) inside the
black outline. Do NOT render the character as a black or grey silhouette. Make the background
transparent ONLY outside the black outline - the white inside the outline must stay opaque.

Framing: FULL BODY head to feet, centered, generous margin. Output: a single PNG with a fully
transparent background, no ground shadow, no text (the paddle and bill stay blank), no logos.
```



### S4-G10 - `tv-wall-glow-1.jpg` (fallback: was a browse base, unsourceable license-safe)

Attach: none. NOTE: this is a full-frame 16:9 BACKGROUND image (not a transparent cutout). Alternatively,
render can build this wall in CSS as a grid of glowing panels over a dark base - if so, this PNG/JPG is
optional.

```text
Create a full-frame 16:9 background image: a dark electronics-showroom wall completely filled with a
neat grid of switched-on flat TV/monitor screens, viewed straight on. Every screen shows only a plain,
soft WHITE-BLUE glow (blank - no picture, no content, no channel, no text). The screens sit in thin dark
bezels against a dark wall, and their combined glow lights the scene at a moderate, readable brightness.
Style: photorealistic, cool blue-white light, gentle reflections, slight vignette at the edges. Do NOT
include: any logos, brand names, on-screen pictures or video, text, numbers, prices, odds, QR codes,
sports or news content, people, faces, hands, or reflections of people. Every screen must stay a plain
blank glowing rectangle.
```



## Section 5 Manifest

Scope: Section 5 (The Three Drains) - from
`visual-plan/section-05-three-drains/section-05-three-drains-visual-plan.md`. 7 scenes.
`drain-grate-ornate.png` is ONE file labeled by CSS across 5.1/5.2/5.4/5.6; `money-pile-party.png`
shrinks across scenes; `banknote-single-crisp.png` recurs; `receipt-endless-roll.png` (reuse from S1)
pins to the door in 5.7.


| Done | Filename                                        | Type                | Used in scenes          | Description                                                                                                            | Prompt / Source                      | Status                                                |
| ---- | ----------------------------------------------- | ------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ----------------------------------------------------- |
| [ ]  | `wit-minister-sash-shouting.png`                | generate (NEW pose) | 5.1                     | WIT: dark suit jacket + blank teal pageant sash + white megaphone, mouth open mid-shout                                | Prompt S5-G1 (attach `_origin_.png`) | `prompt-ready / awaiting generation`                  |
| [ ]  | `money-pile-party.png`                          | generate            | 5.1, 5.2, 5.4, 5.6      | mound of parody teal-cream play-money + confetti (NO real currency), isolated - shrinks by CSS scale                   | Prompt S5-G2                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `drain-grate-ornate.png`                        | generate            | 5.1 (x3), 5.2, 5.4, 5.6 | ornate round cast-iron storm-drain grate, blank curved name plate (CSS labels it), isolated                            | Prompt S5-G3                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `banknote-single-crisp.png`                     | generate            | 5.2, 5.4, 5.5, 5.6      | one crisp parody teal-cream banknote, generic ornament, NO real currency, isolated                                     | Prompt S5-G4                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `banknote-seated-fan.png`                       | generate            | 5.3 (x4)                | parody banknote folded to sit upright like a tiny flat spectator, isolated                                             | Prompt S5-G5                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `ticket-match-stub.png`                         | generate            | 5.3                     | blank sports match ticket stub, perforated edge, empty boxes (CSS text), isolated                                      | Prompt S5-G6                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `ticket-cinema-stub.png`                        | generate            | 5.3                     | blank cinema ticket stub, film-strip edge, empty price box (CSS text), isolated                                        | Prompt S5-G7                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `shopfront-mobbed.png`                          | generate            | 5.5                     | festive shop facade: open door, bunting, packed window, bursting register, bag queue (NO people), blank sign, isolated | Prompt S5-G8                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `shopfront-empty-cobwebs.png`                   | generate            | 5.5                     | grey shuttered shop facade, cobwebs, empty tip jar, same style as the mobbed one, isolated                             | Prompt S5-G9                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `signpost-zurich.png`                           | generate            | 5.6                     | rustic wooden signpost, ONE blank right-arrow plank (CSS labels ZURICH), isolated                                      | Prompt S5-G10                        | `prompt-ready / awaiting generation`                  |
| [ ]  | `banknote-flying-flock.png`                     | generate            | 5.6 (x2)                | 2-3 parody banknotes mid-flight with motion curl, like startled birds, isolated                                        | Prompt S5-G11                        | `prompt-ready / awaiting generation`                  |
| [ ]  | `banknote-walking-guest.png`                    | generate            | 5.7 (x3)                | parody banknote with cartoon legs mid-stride carrying a tiny suitcase, isolated                                        | Prompt S5-G12                        | `prompt-ready / awaiting generation`                  |
|      | `receipt-endless-roll.png`                      | reuse (shared)      | 5.7                     | video motif receipt pinned to the door face (no CSS items this section)                                                | S1 Prompt G2                         | `prompt-ready / awaiting generation` (shared with S1) |
|      | `poses/lecturing_finger_raised_eyes_closed.png` | pose                | 5.2                     | library professor pose                                                                                                 | `.agents/_shared/assets/wit/poses/`  | `done` (reused)                                       |
|      | `poses/unimpressed_smirk_closeup.png`           | pose                | 5.3                     | library dry-smirk closeup                                                                                              | same                                 | `done` (reused)                                       |
|      | `poses/worried_uneasy_wide_eyes.png`            | pose                | 5.4                     | library uneasy wide-eyes (hiding local)                                                                                | same                                 | `done`                                                |
|      | `poses/shocked_sweating_dismayed.png`           | pose                | 5.5                     | library dismay pose                                                                                                    | same                                 | `done` (reused)                                       |
|      | `poses/panic_hands_on_cheeks_scream.png`        | pose                | 5.6                     | library full-panic scream                                                                                              | same                                 | `done` (reused)                                       |
|      | `poses/exhausted_dead_inside_eye_bags.png`      | pose                | 5.7                     | library dead-inside pose                                                                                               | same                                 | `done` (reused)                                       |
|      | `confetti-plaza-1.jpg`                          | browse-real-photo   | 5.1                     | bright people-free plaza/street strewn with confetti + streamers, no brands/flags                                      | see ATTRIBUTION.md                   | `done`                                                |
|      | `wallet-open-1.jpg`                             | browse-real-photo   | 5.2                     | worn brown leather wallet open in close-up, generic bill edges, warm light, no logos/cards                             | see ATTRIBUTION.md                   | `done`                                                |
|      | `cinema-red-seats-1.jpg`                        | browse-real-photo   | 5.3                     | empty cinema auditorium, red velvet seat rows, warm screen glow, no people/brands                                      | see ATTRIBUTION.md                   | `done`                                                |
|      | `suitcase-stack-1.jpg`                          | browse-real-photo   | 5.4                     | wall of stacked colorful vintage suitcases, tightly packed, no brand stickers/people                                   | see ATTRIBUTION.md                   | `done`                                                |
|      | `cobblestone-street-1.jpg`                      | browse-real-photo   | 5.5                     | bright people-free cobblestone shopping street, plain building faces, no readable signs                                | see ATTRIBUTION.md                   | `done`                                                |
|      | `stadium-exterior-day-1.jpg`                    | browse-real-photo   | 5.6                     | modern stadium exterior by day, empty forecourt, no people, no readable sponsor boards                                 | see ATTRIBUTION.md                   | `done`                                                |
|      | `front-door-balloons-1.jpg`                     | browse-real-photo   | 5.7                     | house front door with party balloons + doorstep confetti, morning light, no people/house number                        | see ATTRIBUTION.md                   | `done`                                                |


Render gate: Section 5 render is BLOCKED until the 12 Section-5 `generate` PNGs (S5-G1..G12), the
shared `receipt-endless-roll.png`, and all 7 browse bases are in `assets/`.

Sourcing notes (Section 5 browse pass): all 7 sourced license-safe + Read-verified (Openverse
Cloudflare-blocked; used Wikimedia / rawpixel / Flickr). SUBSTITUTION: `wallet-open-1` is an open EMPTY
BLACK wallet (no license-safe brown open wallet without real currency / a person existed). FLAG:
`suitcase-stack-1` carries vintage decorative hotel labels (HOTEL ATLANTA / BEAU SITE PARIS / METROPOLE)

- defunct-hotel period stickers, judged period decoration not active brands (owner call). `stadium-exterior-day-1`,
`confetti-plaza-1`, `cinema-red-seats-1` are ~1024w upscales (soft - swap if needed). Need upload credit
(CC-BY/BY-SA): confetti-plaza-1, cobblestone-street-1 (SA), front-door-balloons-1 (SA), wallet-open-1.



## Section 5 Generation Prompts



### S5-G1 - `wit-minister-sash-shouting.png` (NEW WIT pose)

Attach: the mascot neutral pose (`assets/poses/_origin_.png`)

```text
Use the attached character as the EXACT reference for identity, proportions, line weight, and color:
a round bald white-headed cartoon character with a thick uniform black outline, big rectangular
glasses with dot eyes, and expressive eyebrows. Draw the SAME character - keep the glasses, head
shape, and outline identical.

New pose: the character as an indignant tourism minister mid-shout. He wears a plain dark charcoal
business suit jacket (open, over the white body) and a wide diagonal pageant-style sash in plain solid
teal (completely blank - no words, insignia, flag colors, or stripes). One hand is raised holding a
small white megaphone up near his mouth; his mouth is wide open mid-shout; his eyebrows are pushed
together, indignant. Two or three small motion lines near the megaphone.

CRITICAL colors: the head and hands are SOLID OPAQUE BRIGHT WHITE (#FFFFFF) inside the black outline;
the suit jacket is dark charcoal; the sash is teal; the megaphone is white. Do NOT render the white
head/hands as a black or grey silhouette, and do NOT let the transparency step key out the white head.
Make the background transparent ONLY outside the black outline - the white inside the outline must
stay opaque.

Framing: FULL BODY head to feet, centered, generous margin. Output: a single PNG with a fully
transparent background, no ground shadow, no text, no logos.
```



### S5-G2 - `money-pile-party.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a rounded mound/pile of parody
banknotes - loose "play money" bills in soft teal and cream with only faint blank panels and simple
scroll edges (NO faces, NO real numbers, NO real currency design), heaped together with a few
colourful confetti bits and paper-streamer curls stuck on top. Style: photorealistic paper with soft
shading between the bills, one gentle highlight on top, a soft contact shadow under the mound.
Framing: the whole pile visible, centered, generous transparent margin. Do NOT include: readable
numbers, currency symbols, real or fake portraits, brand names, logos, coins, a table, people, hands,
or any background.
```



### S5-G3 - `drain-grate-ornate.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: an ornate round cast-iron storm-drain
grate seen from a slightly raised three-quarter angle so it reads with a little 3D depth (a shallow
dark opening visible under the bars). It has thick, heavy, slightly menacing radial bars and a
decorative circular border, plus a BLANK curved name-plate panel along its top edge (empty - no text).
Style: photorealistic dark weathered cast iron with subtle rust and one soft highlight, a faint soft
shadow under the rim. Framing: the whole grate visible, centered, generous transparent margin. Do NOT
include: any text, letters, numbers, city names, logos, water, a road surface, people, hands, or any
background.
```



### S5-G4 - `banknote-single-crisp.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single crisp parody banknote lying
flat at a slight angle, in soft teal-and-cream, with only faint blank panels, a simple centered oval
frame (empty), and plain decorative scroll edges - NO faces, NO portraits, NO numbers, NO real
currency design of any country. Style: photorealistic crisp paper money, soft even light, one subtle
highlight, a faint soft contact shadow. Framing: the whole note visible, centered, generous
transparent margin. Do NOT include: readable numbers, currency symbols, real or fake portraits,
serial numbers, bank names, logos, other notes, people, hands, or any background.
```



### S5-G5 - `banknote-seated-fan.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single parody banknote folded across
its middle so it stands upright and "sits" like a tiny flat spectator, leaning back slightly. Same
generic teal-and-cream play-money look (faint blank panels, simple scroll edges, NO faces, NO numbers,
NO real currency design). Style: photorealistic paper with a soft crease shadow at the fold and a
faint contact shadow under it. Framing: the whole folded note visible, centered, generous transparent
margin. Do NOT include: readable numbers, currency symbols, portraits, a seat, a chair, brand names,
logos, people, hands, or any background.
```



### S5-G6 - `ticket-match-stub.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single blank sports-match ticket stub,
a small rectangular card with a perforated tear edge down one side and a couple of empty rectangular
boxes (for seat/row) drawn as plain outlines only. The whole face is otherwise BLANK (text is added
later). Style: clean photorealistic cardstock, soft even light, a faint soft contact shadow. Framing:
the whole stub visible at a slight tilt, centered, generous transparent margin. Do NOT include: any
words, numbers, prices, barcodes, QR codes, team names, logos, seat numbers, people, hands, or any
background.
```



### S5-G7 - `ticket-cinema-stub.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single blank cinema/movie ticket stub,
a small rectangular card with a decorative film-strip edge (a row of small squares) down one side and
one empty rectangular price box outlined in plain lines. The face is otherwise BLANK (text is added
later). Style: clean photorealistic cardstock in a warm cream tone, soft light, a faint soft contact
shadow. Framing: the whole stub visible at a slight tilt, centered, generous transparent margin. Do
NOT include: any words, numbers, prices, barcodes, QR codes, film titles, logos, seat numbers, people,
hands, or any background.
```



### S5-G8 - `shopfront-mobbed.png`

Attach: none

```text
Create ONE isolated element on a fully transparent background: a single small festive SHOP FACADE
(storefront), front-on, looking busy and thriving but with NO people at all. Details: an open door, a
striped awning with small teal-and-gold triangular bunting strung across the top, a display window
piled with folded scarves and goods, a cash register on the counter inside with its drawer bursting
with generic banknotes, and a neat row of shopping bags lined up by the door. The sign board above the
door is BLANK (no brand or text). A little confetti rests on the awning. Style: warm
photorealistic-but-slightly-cartoonish shop, bright cheerful light, a soft contact shadow along its
base. Framing: the whole facade visible like a stage flat, centered, generous transparent margin. Do
NOT include: any people, faces, readable text, shop names, real brand logos, prices, a street or
neighbouring buildings, or any background.
```



### S5-G9 - `shopfront-empty-cobwebs.png`

Attach: none

```text
Create ONE isolated element on a fully transparent background: a single small shuttered, dead SHOP
FACADE (storefront), front-on, in the SAME architectural style and proportions as a thriving
neighbouring shop but clearly abandoned: a metal roller shutter pulled half-down over the door, a
faded drooping awning, grey cobwebs in one upper door corner, a lonely leaning broom, and an empty tip
jar on the step. The sign board above is BLANK and grimy (no brand or text). Style: desaturated grey
photorealistic-but-slightly-cartoonish shop, flat dull light, a soft contact shadow along its base.
Framing: the whole facade visible like a stage flat, centered, generous transparent margin. Do NOT
include: any people, faces, readable text, shop names, real brand logos, a street or neighbouring
buildings, or any background.
```



### S5-G10 - `signpost-zurich.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a rustic wooden signpost - a single
vertical wooden post with ONE horizontal arrow-shaped plank pointing to the RIGHT near the top. The
plank face is COMPLETELY BLANK (no text - a place name is added later). Style: warm photorealistic
weathered wood with visible grain and a couple of nail heads, soft daylight, a faint soft shadow at
the base of the post. Framing: the whole signpost visible, centered, generous transparent margin. Do
NOT include: any text, letters, place names, numbers, extra arrows or planks, logos, grass, a road,
people, hands, or any background.
```



### S5-G11 - `banknote-flying-flock.png`

Attach: none

```text
Create ONE isolated element on a fully transparent background: a small loose flock of two or three
parody banknotes caught mid-flight, curled and tilted at different angles with gentle motion so they
look like startled birds flapping away. Same generic teal-and-cream play-money look (faint blank
panels, simple scroll edges, NO faces, NO numbers, NO real currency design). Add a few tiny motion
lines behind them. Style: photorealistic paper with soft shading, no cast shadow (they are airborne).
Framing: the little flock grouped and visible, centered, generous transparent margin. Do NOT include:
readable numbers, currency symbols, portraits, real birds, brand names, logos, a sky, people, hands,
or any background.
```



### S5-G12 - `banknote-walking-guest.png`

Attach: none

```text
Create ONE isolated element on a fully transparent background: a single parody banknote given little
cartoon legs and small feet, walking mid-stride as if leaving, and carrying a tiny suitcase in one
small cartoon hand. Same generic teal-and-cream play-money look (faint blank panels, simple scroll
edges, NO faces, NO numbers, NO real currency design). Style: photorealistic paper body with simple
clean cartoon legs and arm in a thin black outline, a soft contact shadow under the feet. Framing: the
whole walking note visible in side profile facing right, centered, generous transparent margin. Do
NOT include: readable numbers, currency symbols, portraits, a face on the note, brand names, logos, a
floor or street, other characters, or any background.
```



## Section 6 Manifest

Scope: Section 6 (The Morning After) - from
`visual-plan/section-06-morning-after/section-06-morning-after-visual-plan.md`. 8 scenes.
Introduces the elephant-stadium pet + the `MAINTENANCE` feeding bowl (secondary motif, returns 6.7);
`receipt-endless-roll.png` (reuse from S1) prints `1x WHITE ELEPHANT (FEEDING, ANNUAL) ......... $???`
in 6.7. The bus row is ONE file composited 3x.


| Done | Filename                                    | Type                | Used in scenes | Description                                                                                            | Prompt / Source                      | Status                                                |
| ---- | ------------------------------------------- | ------------------- | -------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------ | ----------------------------------------------------- |
| [ ]  | `pennant-string-drooping.png`               | generate            | 6.1            | string of plain teal/gold/red triangle pennants, sagging, left end torn loose, isolated                | Prompt S6-G1                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `elephant-stadium-pet.png`                  | generate            | 6.2            | hybrid pet: concrete stadium-bowl body + grey elephant head/trunk/ears/legs, sad droopy eyes, isolated | Prompt S6-G2                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `feeding-bowl-maintenance.png`              | generate            | 6.2, 6.7       | oversized red pet bowl, white `MAINTENANCE` painted on front, heaped with gold coins, isolated         | Prompt S6-G3                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `wit-party-hat-feeding-scoop.png`           | generate (NEW pose) | 6.2            | WIT: teal polka-dot party hat + chin strap, deadpan, gripping a coin-heaped feed scoop mid-pour        | Prompt S6-G4 (attach `_origin_.png`) | `prompt-ready / awaiting generation`                  |
| [ ]  | `bus-row-parked.png`                        | generate            | 6.4 (x3 rows)  | one row of 5 plain white/teal-stripe buses, no names/plates, nose-to-tail, isolated                    | Prompt S6-G5                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `stadium-bowl-tiny.png`                     | generate            | 6.5            | small generic round white arena bowl, 3/4 aerial, generic (not any real venue), isolated               | Prompt S6-G6                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `wit-magnifying-glass-search.png`           | generate (NEW pose) | 6.5            | WIT: leaning forward with a giant magnifying glass, one eye hugely enlarged through the lens           | Prompt S6-G7 (attach `_origin_.png`) | `prompt-ready / awaiting generation`                  |
| [ ]  | `birthday-cake-one-candle.png`              | generate            | 6.6            | small white-frosted birthday cake, pastel sprinkles, ONE lit candle, on a paper plate, isolated        | Prompt S6-G8                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `fridge-white-magnets.png`                  | generate            | 6.7            | plain white two-door fridge, blank door + a few round magnets (CSS card sits on top), isolated         | Prompt S6-G9                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `microphone-stand-gold.png`                 | generate            | 6.8            | classic round-head gold microphone on a black stand, one glint, isolated                               | Prompt S6-G10                        | `prompt-ready / awaiting generation`                  |
|      | `receipt-endless-roll.png`                  | reuse (shared)      | 6.7            | video motif receipt; CSS prints `1x WHITE ELEPHANT (FEEDING, ANNUAL) ......... $???`                   | S1 Prompt G2                         | `prompt-ready / awaiting generation` (shared with S1) |
|      | `poses/sleepy_yawning_open_mouth.png`       | pose                | 6.1            | library morning-after yawn                                                                             | `.agents/_shared/assets/wit/poses/`  | `done`                                                |
|      | `poses/mildly_surprised_hand_at_chin.png`   | pose                | 6.3            | library impressed-but-doubtful                                                                         | same                                 | `done` (reused)                                       |
|      | `poses/deadpan_unimpressed_half_lidded.png` | pose                | 6.4            | library signature deadpan                                                                              | same                                 | `done` (reused)                                       |
|      | `poses/ok_hand_sign_content_closeup.png`    | pose                | 6.6            | library dry OK-sign approval                                                                           | same                                 | `done`                                                |
|      | `poses/exhausted_dead_inside_eye_bags.png`  | pose                | 6.7            | library dead-inside fatigue                                                                            | same                                 | `done` (reused)                                       |
|      | `poses/shrug_both_hands_up_smile.png`       | pose                | 6.8            | library relieved shrug                                                                                 | same                                 | `done` (reused)                                       |
|      | `stadium-empty-seats-dawn-1.jpg`            | browse-real-photo   | 6.1            | empty stadium interior at dawn, curved colored seat rows, cool light, no people/ads                    | see ATTRIBUTION.md                   | `done`                                                |
|      | `grass-field-morning-1.jpg`                 | browse-real-photo   | 6.2            | wide empty grass field/park lawn, bright morning sky, no people/signage                                | see ATTRIBUTION.md                   | `done`                                                |
|      | `stadium-modern-exterior-1.jpg`             | browse-real-photo   | 6.3            | monumental modern stadium exterior, white columns, empty plaza, no people/branding                     | see ATTRIBUTION.md                   | `done`                                                |
|      | `stadium-parking-lot-1.jpg`                 | browse-real-photo   | 6.4            | vast empty stadium parking lot, painted lines, roofline in bg, no people/plates                        | see ATTRIBUTION.md                   | `done`                                                |
|      | `rainforest-aerial-1.jpg`                   | browse-real-photo   | 6.5            | aerial dense rainforest canopy + river bend, no clearings/buildings/people                             | see ATTRIBUTION.md                   | `done`                                                |
|      | `pitch-center-circle-1.jpg`                 | browse-real-photo   | 6.6            | football pitch at ground level, white center circle, empty blurred stands, no people/marks             | see ATTRIBUTION.md                   | `done`                                                |
|      | `kitchen-bright-1.jpg`                      | browse-real-photo   | 6.7            | bright kitchen, counter + tiles + window light, no people/appliance brands                             | see ATTRIBUTION.md                   | `done`                                                |
|      | `concert-stage-lights-1.jpg`                | browse-real-photo   | 6.8            | concert stage lighting rig at night, magenta/violet beams + haze, empty stage, no people/marks         | see ATTRIBUTION.md                   | `done`                                                |


Render gate: Section 6 render is BLOCKED until the 10 Section-6 `generate` PNGs (S6-G1..G10), the
shared `receipt-endless-roll.png`, and all 8 browse bases are in `assets/`.

Sourcing notes (Section 6 browse pass): all 8 from Wikimedia Commons (Openverse + rawpixel blocked) -
ALL 8 are CC-BY/BY-SA and need upload credit. SUBSTITUTIONS: `stadium-modern-exterior-1` is the real
(beige-columned) Petrovskiy Stadium, water/hoardings cropped, small illegible club flags remain;
`pitch-center-circle-1` has NO center circle/spot (none existed license-safe) - RENDER must draw the CSS
center circle + spot for the 6.6 cake gag; `concert-stage-lights-1` is a single stage-light beam
hue-shifted green->magenta to match the palette. `stadium-empty-seats-dawn-1` cropped so the Munich venue
is not identifiable.

## Section 6 Generation Prompts



### S6-G1 - `pennant-string-drooping.png`

Attach: none

```text
Create ONE isolated element on a fully transparent background: a single horizontal string of small
triangular party pennant flags (bunting) in plain solid colours - alternating teal, gold, and red
triangles, no patterns on them. The string SAGS in the middle and the LEFT end has come loose and
dangles down limply, so the whole thing reads as "the party is over". Style: clean photorealistic
fabric triangles with a soft cloth texture, gentle soft shadows, hanging on a thin cord. Framing: the
whole string visible left to right, centered, generous transparent margin. Do NOT include: any
national or country flags, flag emblems, text, numbers, logos, a wall or ceiling, people, hands, or
any background.
```



### S6-G2 - `elephant-stadium-pet.png`

Attach: none

```text
Create ONE isolated creature on a fully transparent background: a whimsical hybrid pet that is half
sports stadium, half elephant. Its BODY is a large round concrete stadium bowl (an oval arena with
arched openings around the outside ring and a thin white roof rim, with faint seat-row stripes visible
inside the rim). From this stadium body sprout a grey ELEPHANT head with a long curling trunk and two
big floppy ears at the front, four short stumpy elephant legs underneath, and small sad droopy eyes.
Concrete-grey skin overall. It should look heavy, sweet, and useless - a giant pet nobody asked for.
Style: soft photorealistic-but-cartoonish 3D, gentle daylight, a soft contact shadow under its feet.
Framing: the whole creature visible facing slightly right, centered, generous transparent margin. Do
NOT include: any text, numbers, team or sponsor names, logos, a real stadium's identifiable design,
people, spectators, a field, ground scenery, or any background.
```



### S6-G3 - `feeding-bowl-maintenance.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: an oversized red plastic pet feeding
bowl, seen slightly from above, with the single word `MAINTENANCE` hand-painted in white block letters
across the front of the bowl. It is heaped with a mound of shiny gold coins, with two folded banknote
corners poking out of the pile. Style: glossy photorealistic red plastic with one soft highlight, warm
gold coins, a soft contact shadow under the bowl. Framing: the whole bowl visible, centered, generous
transparent margin. The ONLY text is the white `MAINTENANCE` on the bowl. Do NOT include: any other
text, numbers, real currency designs on the coins, brand names, logos, pet food, a floor, people,
hands, or any background.
```



### S6-G4 - `wit-party-hat-feeding-scoop.png` (NEW WIT pose)

Attach: the mascot neutral pose (`assets/poses/_origin_.png`)

```text
Use the attached character as the EXACT reference for identity, proportions, line weight, and color:
a round bald white-headed cartoon character with a thick uniform black outline, big rectangular
glasses with dot eyes, and expressive eyebrows. Draw the SAME character - keep the glasses, head
shape, and outline identical.

New pose: WIT wearing a small teal cone party hat with yellow polka dots and a thin elastic strap
under his chin (the party ended but the hat stayed on). His face is fully DEADPAN - half-lidded eyes
and a flat straight mouth. Both hands grip a big metal feed scoop heaped with gold coins, tilted
mid-pour as a few coins begin to spill from its lip. No other costume; plain white body.

CRITICAL colors: the head, body, and hands are SOLID OPAQUE BRIGHT WHITE (#FFFFFF) inside the black
outline; only the party hat (teal + yellow dots) and the gold coins carry color. Do NOT render the
character as a black or grey silhouette. Make the background transparent ONLY outside the black
outline - the white inside the outline must stay opaque.

Framing: FULL BODY head to feet, centered, generous margin. Output: a single PNG with a fully
transparent background, no ground shadow, no text, no logos.
```



### S6-G5 - `bus-row-parked.png`

Attach: none

```text
Create ONE isolated element on a fully transparent background: a single row of five identical plain
city buses parked nose-to-tail, viewed from a slight side angle so they recede gently to one side.
Each bus is a plain white body with ONE simple horizontal teal stripe along the side, plain dark
windows, and blank destination panels - completely generic. NO operator names, route numbers,
adverts, or licence plates anywhere. Style: clean photorealistic-but-simple vehicles, soft daylight, a
soft contact shadow under the row. Framing: the whole row of five visible, centered, generous
transparent margin (this row will be duplicated to make more rows later). Do NOT include: any text,
route numbers, licence plates, operator or brand names, adverts, logos, people, a road, a parking lot,
or any background.
```



### S6-G6 - `stadium-bowl-tiny.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a small generic round white sports
arena/stadium bowl seen from a three-quarter AERIAL angle (looking down at it), with a thin white
lattice roof rim around the top and a hint of green pitch in the middle. It clearly reads as a modern
stadium but is a GENERIC invented design, not any real venue. Style: clean photorealistic-but-simple
3D, soft daylight, a faint soft shadow directly under it. Framing: the whole little stadium visible,
centered, generous transparent margin. Do NOT include: any text, numbers, team or sponsor names,
logos, a real stadium's identifiable shape, surrounding land, people, or any background.
```



### S6-G7 - `wit-magnifying-glass-search.png` (NEW WIT pose)

Attach: the mascot neutral pose (`assets/poses/_origin_.png`)

```text
Use the attached character as the EXACT reference for identity, proportions, line weight, and color:
a round bald white-headed cartoon character with a thick uniform black outline, big rectangular
glasses with dot eyes, and expressive eyebrows. Draw the SAME character - keep the glasses, head
shape, and outline identical.

New pose: WIT leaning forward in detective concentration, both hands gripping a giant round magnifying
glass (thick black frame, pale grey glass, long black handle) held up in front of one side of his
face. The eye seen THROUGH the lens is comically enlarged; his eyebrows are raised and his mouth is a
small open "o". No costume; plain white body.

CRITICAL colors: the head, body, and hands are SOLID OPAQUE BRIGHT WHITE (#FFFFFF) inside the black
outline. Do NOT render the character as a black or grey silhouette. Make the background transparent
ONLY outside the black outline - the white inside the outline must stay opaque.

Framing: FULL BODY head to feet, centered, generous margin. Output: a single PNG with a fully
transparent background, no ground shadow, no text, no logos.
```



### S6-G8 - `birthday-cake-one-candle.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a small round birthday cake with smooth
white frosting and a scatter of pastel sprinkles, topped with exactly ONE lit candle with a small
warm flame, sitting on a simple round paper plate. Style: cheerful photorealistic cake, soft even
light, a faint soft contact shadow under the plate. Framing: the whole cake and plate visible,
centered, generous transparent margin. Do NOT include: any text, writing on the cake, numbers, more
than one candle, logos, a table, people, hands, or any background.
```



### S6-G9 - `fridge-white-magnets.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a plain white two-door refrigerator,
front-on, with slightly rounded corners and a clean BLANK door (no brand mark). A few small colourful
round magnets are stuck on the upper door; the door is otherwise empty so notes can be added later.
Style: clean photorealistic matte-white appliance, soft even light, one gentle highlight down one
edge, a soft contact shadow at the base. Framing: the whole fridge visible, centered, generous
transparent margin. Do NOT include: any text, numbers, brand names, logos, a control panel with words,
a kitchen, people, hands, or any background.
```



### S6-G10 - `microphone-stand-gold.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a classic round-head stage microphone in
polished GOLD mounted on a slim black microphone stand with a round base. One soft white specular
glint on the mic head. Style: glossy photorealistic metal, warm gold on the mic and matte black on the
stand, a faint soft contact shadow under the base. Framing: the whole mic and upper stand visible
(upright), centered, generous transparent margin. Do NOT include: any text, numbers, brand names,
logos, cables draped around, a stage, a person, hands, or any background.
```



## Section 7 Manifest

Scope: Section 7 (Who Decides Is Not Who Pays) - from
`visual-plan/section-07-who-decides-who-pays/section-07-who-decides-who-pays-visual-plan.md`. 9 scenes.
`podium-suits-trio.png` (faceless deciders) recurs 7.1/7.2/7.3; `trophy-gold-parody.png` and
`receipt-endless-roll.png` reuse from S1. New section-signature pose: the tiny taxpayer-WIT.


| Done | Filename                                    | Type                | Used in scenes | Description                                                                                                            | Prompt / Source                      | Status                                                |
| ---- | ------------------------------------------- | ------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ----------------------------------------------------- |
| [ ]  | `podium-suits-trio.png`                     | generate            | 7.1, 7.2, 7.3  | three FACELESS suited figures (blank heads) behind one wooden podium, one mid-wave, isolated                           | Prompt S7-G1                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `receipt-conveyor-machine.png`              | generate            | 7.1            | chunky industrial conveyor-belt machine with rollers + output ramp, unbranded, isolated                                | Prompt S7-G2                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `wit-tiny-taxpayer-catching-receipt.png`    | generate (NEW pose) | 7.1 (x3)       | tiny full-body WIT, arms up catching a falling receipt strip, overwhelmed, one sweat drop                              | Prompt S7-G3 (attach `_origin_.png`) | `prompt-ready / awaiting generation`                  |
| [ ]  | `bill-envelope-overdue.png`                 | generate            | 7.3            | worn white envelope, one red diagonal corner stripe, text-free (CSS adds stamp/date), isolated                         | Prompt S7-G4                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `prestige-crown-glow.png`                   | generate            | 7.4            | small radiant golden crown with a soft warm glow aura + sparkles, isolated                                             | Prompt S7-G5                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `rubber-stamp-red.png`                      | generate            | 7.4            | wooden-handle rubber stamp with red base, mid-slam, blank rubber face (CSS text), isolated                             | Prompt S7-G6                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `ballot-box-wood.png`                       | generate            | 7.5            | classic wooden ballot box, brass top slot + small brass padlock, isolated                                              | Prompt S7-G7                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `applause-meter-dial.png`                   | generate            | 7.6            | vintage carnival applause-o-meter, half-circle cream dial + brass rim + red needle, blank plate (CSS labels), isolated | Prompt S7-G8                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `wallet-padlocked-city.png`                 | generate            | 7.7            | fat brown wallet wrapped in a steel chain + chunky brass padlock, isolated                                             | Prompt S7-G9                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `surplus-jar-coins.png`                     | generate            | 7.7            | clear glass jar full of gold coins, paper lid tied with string, label-free (CSS labels), isolated                      | Prompt S7-G10                        | `prompt-ready / awaiting generation`                  |
| [ ]  | `clickbait-ad-card.png`                     | generate            | 7.8            | parody 2000s popup-ad card, garish magenta/cyan border, starburst, fake X, blank center (CSS copy), isolated           | Prompt S7-G11                        | `prompt-ready / awaiting generation`                  |
| [ ]  | `bill-stack-invoices.png`                   | generate            | 7.9            | thick stack of white invoices, ruffled edges, one red rubber band, faint unreadable print, isolated                    | Prompt S7-G12                        | `prompt-ready / awaiting generation`                  |
|      | `trophy-gold-parody.png`                    | reuse (shared)      | 7.2            | video hero trophy as photo-op prop                                                                                     | S1 Prompt G1                         | `prompt-ready / awaiting generation` (shared with S1) |
|      | `receipt-endless-roll.png`                  | reuse (shared)      | 7.1, 7.9       | video motif receipt: conveyor feed (7.1) + closing bottom roll (7.9)                                                   | S1 Prompt G2                         | `prompt-ready / awaiting generation` (shared with S1) |
|      | `poses/shrug_confused_flat_mouth.png`       | pose                | 7.1            | library blank confused shrug                                                                                           | `.agents/_shared/assets/wit/poses/`  | `done`                                                |
|      | `poses/unimpressed_smirk_closeup.png`       | pose                | 7.2            | library dry witness                                                                                                    | same                                 | `done` (reused)                                       |
|      | `poses/pointing_at_globe_explaining.png`    | pose                | 7.3            | library map-pointing pose                                                                                              | same                                 | `done` (reused)                                       |
|      | `poses/mildly_surprised_hand_at_chin.png`   | pose                | 7.4            | library doubtful "huh"                                                                                                 | same                                 | `done` (reused)                                       |
|      | `poses/furious_shouting_anger_mark.png`     | pose                | 7.5            | library mid-shout fury                                                                                                 | same                                 | `done`                                                |
|      | `poses/deadpan_unimpressed_half_lidded.png` | pose                | 7.6            | library signature deadpan                                                                                              | same                                 | `done` (reused)                                       |
|      | `poses/ok_hand_sign_content_closeup.png`    | pose                | 7.7            | library content approval                                                                                               | same                                 | `done` (reused)                                       |
|      | `poses/smug_sly_smirk_leaning.png`          | pose                | 7.8            | library salesman lean                                                                                                  | same                                 | `done`                                                |
|      | `poses/shrug_both_hands_up_smile.png`       | pose                | 7.9            | library resigned smiling shrug                                                                                         | same                                 | `done` (reused)                                       |
|      | `rope-tug-frayed-1.jpg`                     | browse-real-photo   | 7.1            | one thick frayed tug-of-war rope pulled taut, diagonal, no people/hands                                                | see ATTRIBUTION.md                   | `done`                                                |
|      | `red-carpet-stanchions-1.jpg`               | browse-real-photo   | 7.2            | red carpet + gold stanchions to a small empty stage, no people, warm light                                             | see ATTRIBUTION.md                   | `done`                                                |
|      | `map-atlas-colored-1.jpg`                   | browse-real-photo   | 7.3            | bright colored school atlas double-page spread, top-down, no country emphasized, no flags                              | see ATTRIBUTION.md                   | `done`                                                |
|      | `calculator-spreadsheet-1.jpg`              | browse-real-photo   | 7.4            | chunky desk calculator on printed spreadsheet pages, top-down, no hands/brand                                          | see ATTRIBUTION.md                   | `done`                                                |
|      | `voting-booth-1.jpg`                        | browse-real-photo   | 7.5            | polling booth with pleated navy privacy curtain + shelf, empty, no people/signage                                      | see ATTRIBUTION.md                   | `done`                                                |
|      | `auditorium-seats-1.jpg`                    | browse-real-photo   | 7.6            | rows of empty red auditorium seats, soft focus, no people/venue branding                                               | see ATTRIBUTION.md                   | `done`                                                |
|      | `palm-trees-sky-1.jpg`                      | browse-real-photo   | 7.7            | tall palm trees against clean blue sunny sky, low angle, no buildings/people/landmarks                                 | see ATTRIBUTION.md                   | `done`                                                |
|      | `crt-monitor-retro-1.jpg`                   | browse-real-photo   | 7.8            | retro beige CRT monitor on a desk, screen glowing blank, no brand/people                                               | see ATTRIBUTION.md                   | `done`                                                |
|      | `city-hall-columns-1.jpg`                   | browse-real-photo   | 7.9            | generic stone civic building facade with columns, straight-on, no landmark/signage/people                              | see ATTRIBUTION.md                   | `done`                                                |


Render gate: Section 7 render is BLOCKED until the 12 Section-7 `generate` PNGs (S7-G1..G12), the two
shared reuses (`trophy-gold-parody.png`, `receipt-endless-roll.png`), and all 9 browse bases are in
`assets/`.

Sourcing notes (Section 7 browse pass): all 9 from Wikimedia Commons (Openverse blocked). SUBSTITUTIONS:
`calculator-spreadsheet-1` is a vintage printing calculator on plain white (NO spreadsheet pages, brand
patched) - render supplies the spreadsheet context; `red-carpet-stanchions-1` is gold stanchions + red
velvet ropes only (no full carpet/stage); `voting-booth-1` is empty grey privacy-screen booths (not a
navy pleated curtain). `crt-monitor-retro-1` screen shows a benign retro GEM desktop (no brands) - render
composites the ad card over it. Need upload credit (CC-BY/BY-SA): auditorium-seats-1, crt-monitor-retro-1
(SA), red-carpet-stanchions-1, rope-tug-frayed-1 (SA), voting-booth-1.

## Section 7 Generation Prompts



### S7-G1 - `podium-suits-trio.png`

Attach: none

```text
Create ONE isolated element on a fully transparent background: three generic FACELESS figures in dark
business suits standing close together behind one small wooden lectern/podium. Each head is a smooth,
completely FEATURELESS blank ovoid - NO eyes, nose, mouth, or hair at all (they must read as anonymous
"officials", not real people). The centre figure has one hand raised mid-wave; the others stand
formally. Style: clean flat-shaded semi-realistic illustration, muted charcoal/navy suits, a warm wood
podium, a soft contact shadow along the base. Framing: the three figures from roughly the knees up
plus the podium, centered, generous transparent margin. Do NOT include: any facial features, hair,
skin detail, real people's likenesses, text, numbers, brand names, logos, flags, other people, or any
background.
```



### S7-G2 - `receipt-conveyor-machine.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a chunky industrial conveyor-belt machine
with a short flat belt on top running between two rollers and a small output ramp at one end, on stubby
legs. Slightly cartoonish but sturdy proportions, plain metal panels. The machine is completely
UNBRANDED and text-free. Style: photorealistic-but-simple painted metal in a neutral grey-green, soft
light, gentle reflections, a soft contact shadow underneath. Framing: the whole machine visible at a
slight three-quarter angle facing down-right, centered, generous transparent margin. Do NOT include:
any text, numbers, brand names, logos, control labels, paper on the belt, people, hands, or any
background.
```



### S7-G3 - `wit-tiny-taxpayer-catching-receipt.png` (NEW WIT pose)

Attach: the mascot neutral pose (`assets/poses/_origin_.png`)

```text
Use the attached character as the EXACT reference for identity, proportions, line weight, and color:
a round bald white-headed cartoon character with a thick uniform black outline, big rectangular
glasses with dot eyes, and expressive eyebrows. Draw the SAME character - keep the glasses, head
shape, and outline identical.

New pose: a small full-body WIT with both arms stretched straight up overhead, trying to catch a long
paper receipt strip falling toward him from above (the falling receipt strip is part of the image,
coming down into his hands). His eyes are wide and overwhelmed, one sweat drop on his temple, and his
knees are slightly buckled under the weight. No costume; plain white body. Keep the whole figure
compact and centered, because it will be placed small and repeated.

CRITICAL colors: the head, body, arms, and hands are SOLID OPAQUE BRIGHT WHITE (#FFFFFF) inside the
black outline; the receipt is white paper. Do NOT render the character as a black or grey silhouette.
Make the background transparent ONLY outside the black outline - the white inside the outline must stay
opaque.

Framing: FULL BODY head to feet, centered, generous margin. Output: a single PNG with a fully
transparent background, no ground shadow, no readable text on the receipt, no logos.
```



### S7-G4 - `bill-envelope-overdue.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single worn white paper envelope,
slightly dog-eared, lying at a slight angle, with ONE red diagonal stripe printed across one corner
(like an airmail/urgent corner) but otherwise completely BLANK (no stamp, no address, no text - these
are added later). Style: photorealistic paper with a soft crease or two and a faint soft contact
shadow. Framing: the whole envelope visible, centered, generous transparent margin. Do NOT include:
any text, addresses, stamps, postmarks, numbers, logos, a mailbox, a desk, people, hands, or any
background.
```



### S7-G5 - `prestige-crown-glow.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a small radiant golden crown (a simple
classic five-point crown with a couple of tiny gem dots) surrounded by a soft warm golden glow/aura
and a few tiny sparkles. Slightly cartoonish and magical. Style: glossy photorealistic gold with a
soft luminous halo, one bright highlight, floating (no ground shadow). Framing: the whole crown and
its glow visible, centered, generous transparent margin. Do NOT include: any text, numbers, brand
names, logos, a head, a cushion, people, hands, or any background.
```



### S7-G6 - `rubber-stamp-red.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a classic office rubber stamp with a
turned WOODEN handle and a red rubber base, shown at a dynamic angle as if mid-slam (tilted, coming
down). The rubber face is BLANK (no words - text is added later). Add a tiny hint of red ink on the
rubber edge. Style: photorealistic wood and red rubber, soft light, one highlight on the handle, crisp
edges. Framing: the whole stamp visible, centered, generous transparent margin. Do NOT include: any
text, letters, numbers, logos, an ink pad, paper, people, hands, or any background.
```



### S7-G7 - `ballot-box-wood.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a classic wooden ballot box - a warm
wooden cube with a brass slot on the top and one small brass padlock on a hasp on the front. Style:
photorealistic polished wood with visible grain, brass fittings with a soft glint, a soft contact
shadow under the box. Framing: the whole box visible at a slight three-quarter angle, centered,
generous transparent margin. The front face is otherwise BLANK (any tally text is added later). Do NOT
include: any text, numbers, party names, logos, ballots sticking out, people, hands, or any background.
```



### S7-G8 - `applause-meter-dial.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a vintage carnival "applause-o-meter"
gauge: a half-circle (semicircular) cream dial face with a brass rim and a single slim red needle
resting near the far left, mounted on a small stand with a BLANK rectangular base plate. The dial face
and base plate are TEXT-FREE (all labels are added later). Style: warm photorealistic brass and cream
with a soft highlight, a soft contact shadow under the stand. Framing: the whole meter and stand
visible, centered, generous transparent margin. Do NOT include: any text, numbers, tick labels, brand
names, logos, people, hands, or any background.
```



### S7-G9 - `wallet-padlocked-city.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a fat brown leather wallet wrapped
tightly around its middle with a steel chain, closed shut with one chunky brass padlock at the front -
clearly impossible to open. Slightly cartoonish heft. Style: photorealistic worn brown leather with
stitching, a steel chain with soft metallic glints, a brass padlock with one highlight, a soft contact
shadow under the wallet. Framing: the whole wallet, chain, and padlock visible, centered, generous
transparent margin. Do NOT include: any text, numbers, card logos, brand names, money sticking out, a
keyhole with a key, people, hands, or any background.
```



### S7-G10 - `surplus-jar-coins.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a clear glass jar filled with shiny GOLD
coins, its mouth covered by a round paper lid tied on with a short length of string. The coins are
plain and generic (no text, no faces). The jar surface is otherwise LABEL-FREE (a label is added
later). Style: photorealistic clear glass with soft reflections and gold coins glowing warm inside, a
soft contact shadow under the jar. Framing: the whole jar visible, centered, generous transparent
margin. Do NOT include: any text, numbers, real currency designs, brand names, logos, a table, people,
hands, or any background.
```



### S7-G11 - `clickbait-ad-card.png`

Attach: none

```text
Create ONE isolated element on a fully transparent background: a deliberately garish early-2000s style
pop-up advertisement CARD/frame. It has a thick, ugly gradient border in clashing magenta and cyan, a
small pointed starburst shape in the top-left corner, a fake grey `X` close-button mark in the
top-right corner, and a BLANK cream rectangular panel filling the center (all ad copy is added later,
so the center stays empty). Style: flat web-graphic look, slightly cheesy, crisp edges, a faint drop
shadow behind the card. Framing: the whole ad card visible, centered, generous transparent margin. Do
NOT include: any text, words, numbers, real brand names, real logos, photos of people, a webpage or
browser behind it, or any background.
```



### S7-G12 - `bill-stack-invoices.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a thick stack of white paper invoices
with slightly ruffled, uneven edges, bound together by one red rubber band around the middle. The
papers carry only FAINT, BLURRED, UNREADABLE grey print lines (clearly not real words or numbers).
Style: photorealistic paper with soft edge shadows between the sheets and a soft contact shadow under
the stack. Framing: the whole stack visible at a slight angle, centered, generous transparent margin.
Do NOT include: any readable text, real numbers, prices, logos, brand names, a desk, people, hands, or
any background.
```



## Section 8 Manifest

Scope: Section 8 (Payoff: Check The Receipt) - from
`visual-plan/section-08-payoff/section-08-payoff-visual-plan.md`. 6 calm scenes. Heavy reuse of the two
shared-registry assets: `trophy-gold-parody.png` (desaturated souvenir grade) and `receipt-endless-roll.png`
(the 8.5 close-up is the video's thesis frame). `mantel-livingroom-1.jpg` is fresh in 8.1 and reused in
8.6 (deliberate open/close callback). `tag-paper-string.png` is one file composited 3x in 8.1.


| Done | Filename                                  | Type                | Used in scenes                  | Description                                                                                               | Prompt / Source                      | Status                                                |
| ---- | ----------------------------------------- | ------------------- | ------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------ | ----------------------------------------------------- |
| [ ]  | `tag-paper-string.png`                    | generate            | 8.1 (x3)                        | single blank cream luggage-style paper tag on rough string (CSS text; composited 3x), isolated            | Prompt S8-G1                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `coin-jar-glass.png`                      | generate            | 8.2                             | clear glass jar half full of assorted coins, no lid, label-free (CSS label), isolated                     | Prompt S8-G2                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `phone-frame-plain.png`                   | generate            | 8.3                             | large plain portrait smartphone, blank dark screen, slim selfie-stick clamp on bottom, no logos, isolated | Prompt S8-G3                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `wit-selfie-stick-calm.png`               | generate (NEW pose) | 8.3                             | WIT: full body, one arm up holding a selfie stick with a small dark phone, calm faint smile, eyes up      | Prompt S8-G4 (attach `_origin_.png`) | `prompt-ready / awaiting generation`                  |
| [ ]  | `marker-red-uncapped.png`                 | generate            | 8.5                             | red marker pen, cap off, isolated                                                                         | Prompt S8-G5                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `balloon-deflated-grey.png`               | generate            | 8.6                             | single grey half-deflated wrinkled party balloon on a thin string, isolated                               | Prompt S8-G6                         | `prompt-ready / awaiting generation`                  |
| [ ]  | `wit-calm-resigned-nod.png`               | generate (NEW pose) | 8.6                             | WIT: relaxed, eyes gently closed, small knowing smile, chin dipped, holding a small blank ticket stub     | Prompt S8-G7 (attach `_origin_.png`) | `prompt-ready / awaiting generation`                  |
|      | `trophy-gold-parody.png`                  | reuse (shared)      | 8.1, 8.3 (in phone screen), 8.6 | video hero trophy, desaturated souvenir grade                                                             | S1 Prompt G1                         | `prompt-ready / awaiting generation` (shared with S1) |
|      | `receipt-endless-roll.png`                | reuse (shared)      | 8.1, 8.2, 8.5, 8.6              | video motif receipt; 8.5 close-up is the thesis frame (all item/name text is CSS)                         | S1 Prompt G2                         | `prompt-ready / awaiting generation` (shared with S1) |
|      | `poses/eyes_closed_talking_open_palm.png` | pose                | 8.1                             | library calm matter-of-fact narration                                                                     | `.agents/_shared/assets/wit/poses/`  | `done` (reused)                                       |
|      | `poses/skeptical_side_eye_doubtful.png`   | pose                | 8.2                             | library half-lidded side-eye                                                                              | same                                 | `done` (reused)                                       |
|      | `poses/unimpressed_smirk_closeup.png`     | pose                | 8.4                             | library dry smirk closeup                                                                                 | same                                 | `done` (reused)                                       |
|      | `poses/mildly_surprised_hand_at_chin.png` | pose                | 8.5                             | library "reading the bill" pose                                                                           | same                                 | `done` (reused)                                       |
|      | `mantel-livingroom-1.jpg`                 | browse-real-photo   | 8.1, 8.6                        | quiet living-room fireplace mantel, pale wall, soft light, no people/brands/framed faces                  | see ATTRIBUTION.md                   | `done`                                                |
|      | `office-empty-chair-1.jpg`                | browse-real-photo   | 8.2                             | empty executive office, desk + empty leather chair slightly turned, no people/brands/papers               | see ATTRIBUTION.md                   | `done`                                                |
|      | `overlook-railing-dusk-1.jpg`             | browse-real-photo   | 8.3                             | scenic overlook railing at dusk, wide grey-blue sky, distant lights, no people/landmark                   | see ATTRIBUTION.md                   | `done`                                                |
|      | `cash-counter-machine-1.jpg`              | browse-real-photo   | 8.4                             | currency-counting machine mid-count, fanned notes, plain counter, no hands/brands/readable portraits      | see ATTRIBUTION.md                   | `done`                                                |
|      | `coffee-table-lamp-1.jpg`                 | browse-real-photo   | 8.5                             | dark wooden coffee table at night under one warm lamp pool, blurred quiet room, no people/brands          | see ATTRIBUTION.md                   | `done`                                                |


Render gate: Section 8 render is BLOCKED until the 7 Section-8 `generate` PNGs (S8-G1..G7), the two
shared reuses (`trophy-gold-parody.png`, `receipt-endless-roll.png`), and all 5 browse bases are in
`assets/`.

Sourcing notes (Section 8 browse pass): Openverse only reachable via WebFetch this session; most bases
are Flickr CC-BY ~1024w upscaled (soft - swap if any reads soft at 1920). SUBSTITUTIONS:
`cash-counter-machine-1` is clean scattered Euro notes (no license-safe brandless / portrait-free counting
MACHINE existed); `coffee-table-lamp-1` (the 8.5 THESIS-FRAME base) is a warm wooden tabletop + bokeh (no
"dark table under a warm lamp pool" existed). CAVEAT: `mantel-livingroom-1` (used 8.1 + 8.6) is
CHRISTMAS-decorated (red bows / garland) - render should grade hard grey-blue + crop to the clear shelf,
or owner replaces it. Need upload credit (CC-BY): cash-counter-machine-1, office-empty-chair-1,
coffee-table-lamp-1, overlook-railing-dusk-1. mantel-livingroom-1 is CC0.

## Section 8 Generation Prompts



### S8-G1 - `tag-paper-string.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single blank cream paper luggage-style
tag (a small rectangle with one rounded corner and a punched hole with a metal rim) hanging from a
short length of rough natural string looped through the hole. The tag has one gentle bend so it looks
like real paper, and its face is COMPLETELY BLANK (text is added later). Style: photorealistic warm
cream paper, a faint self-shadow in the bend, a soft contact shadow. Framing: the whole tag and string
visible at a slight tilt, centered, generous transparent margin (it will be copied a few times). Do
NOT include: any text, letters, numbers, prices, barcodes, logos, a product, a table, people, hands,
or any background.
```



### S8-G2 - `coin-jar-glass.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a clear glass jar about half full of
assorted loose coins (plain, generic silver-and-gold coins, no text or faces on them), with no lid.
The jar surface is LABEL-FREE (a small label is added later). Style: photorealistic clear glass with
soft highlights and reflections, coins with a gentle metallic glint, a soft contact shadow under the
jar. Framing: the whole jar visible, centered, generous transparent margin. Do NOT include: any text,
numbers, real currency designs, brand names, logos, a table, people, hands, or any background.
```



### S8-G3 - `phone-frame-plain.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a large plain modern smartphone held in
portrait orientation, with a thin dark bezel and a completely BLANK dark (off) screen (screen content
is added later). A slim selfie-stick clamp grips its bottom edge (part of the asset). No logos
anywhere. Style: clean photorealistic glossy phone with one soft reflection down the screen glass, a
faint soft contact shadow. Framing: the whole phone and the clamp visible at a slight tilt, centered,
generous transparent margin. Do NOT include: any brand names, logos, app icons, on-screen content,
text, numbers, camera-bump detail suggesting a real model, a hand, a person, or any background.
```



### S8-G4 - `wit-selfie-stick-calm.png` (NEW WIT pose)

Attach: the mascot neutral pose (`assets/poses/_origin_.png`)

```text
Use the attached character as the EXACT reference for identity, proportions, line weight, and color:
a round bald white-headed cartoon character with a thick uniform black outline, big rectangular
glasses with dot eyes, and expressive eyebrows. Draw the SAME character - keep the glasses, head
shape, and outline identical.

New pose: full-body WIT holding a selfie stick. His right arm extends up and forward holding a selfie
stick with a small dark smartphone clamped at its far end (the phone is part of the asset). His left
arm rests relaxed at his side. His chin is slightly raised and his eyes are open, looking up toward
the phone, with a calm faint gentle smile - the serenity of someone happily spending too much on a
photo. No costume; plain white body.

CRITICAL colors: the head, body, arms, and hands are SOLID OPAQUE BRIGHT WHITE (#FFFFFF) inside the
black outline; the selfie stick and phone are dark grey. Do NOT render the character as a black or
grey silhouette. Make the background transparent ONLY outside the black outline - the white inside the
outline must stay opaque.

Framing: FULL BODY head to feet, centered, generous margin. Output: a single PNG with a fully
transparent background, no ground shadow, no text, no logos.
```



### S8-G5 - `marker-red-uncapped.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single red marker pen lying at a slight
angle with its cap OFF (the separate cap resting nearby), the felt tip exposed. Style: clean
photorealistic plastic marker with a soft highlight along the barrel, a faint soft contact shadow.
Framing: the whole marker and its cap visible, centered, generous transparent margin. Do NOT include:
any text, brand names, logos, numbers, writing, paper, a desk, people, hands, or any background.
```



### S8-G6 - `balloon-deflated-grey.png`

Attach: none

```text
Create ONE isolated object on a fully transparent background: a single grey party balloon that is
half-deflated and wrinkled, sagging and soft, hanging from a thin limp string - the sad end of a
party. Style: photorealistic soft rubber with dull matte grey and gentle wrinkles, one faint
highlight, no cast shadow (it hangs). Framing: the whole droopy balloon and its string visible,
centered, generous transparent margin. Do NOT include: any text, numbers, patterns, faces, logos,
other balloons, a wall or ceiling, people, hands, or any background.
```



### S8-G7 - `wit-calm-resigned-nod.png` (NEW WIT pose)

Attach: the mascot neutral pose (`assets/poses/_origin_.png`)

```text
Use the attached character as the EXACT reference for identity, proportions, line weight, and color:
a round bald white-headed cartoon character with a thick uniform black outline, big rectangular
glasses with dot eyes, and expressive eyebrows. Draw the SAME character - keep the glasses, head
shape, and outline identical.

New pose: full-body WIT, shoulders relaxed, eyes gently closed, a small knowing closed-mouth smile,
chin dipped slightly as if mid-nod. One hand is raised to chest height holding a small blank paper
ticket stub between thumb and forefinger (the ticket has no text). The other arm hangs loose at his
side. Calm and resigned, not sad. No costume; plain white body.

CRITICAL colors: the head, body, arms, and hands are SOLID OPAQUE BRIGHT WHITE (#FFFFFF) inside the
black outline; the ticket stub is plain cream paper. Do NOT render the character as a black or grey
silhouette. Make the background transparent ONLY outside the black outline - the white inside the
outline must stay opaque.

Framing: FULL BODY head to feet, centered, generous margin. Output: a single PNG with a fully
transparent background, no ground shadow, no text on the ticket, no logos.
```



## Section 9 Manifest

Scope: Section 9 (Outro) - from `visual-plan/section-09-outro/section-09-outro-visual-plan.md`.
NO new `generate` assets: the outro is built from the two shared-registry reuses (trophy + receipt,
their FINAL appearances), one library pose, two fresh browse bases, and an animated-interactive
subscribe UI built entirely in CSS at render (no PNG needed). All receipt/card text is CSS overlay.


| Done | Filename                               | Type              | Used in scenes            | Description                                                                                                  | Prompt / Source                     | Status                                                |
| ---- | -------------------------------------- | ----------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------- | ----------------------------------------------------- |
|      | `trophy-gold-parody.png`               | reuse (shared)    | 9.1, 9.2 (card thumbnail) | video hero trophy, warmest grade; final two appearances                                                      | S1 Prompt G1                        | `prompt-ready / awaiting generation` (shared with S1) |
|      | `receipt-endless-roll.png`             | reuse (shared)    | 9.1                       | video motif receipt, final appearance; CSS prints `TOTAL: $0.00` + tear-off                                  | S1 Prompt G2                        | `prompt-ready / awaiting generation` (shared with S1) |
|      | `poses/peace_sign_calm_open_mouth.png` | pose              | 9.x                       | library calm peace-sign sign-off pose                                                                        | `.agents/_shared/assets/wit/poses/` | `done`                                                |
|      | `cafe-counter-warm-1.jpg`              | browse-real-photo | 9.1                       | warm-lit wooden cafe counter, amber side light, warm bokeh, one out-of-focus cup, no people/brands           | see ATTRIBUTION.md                  | `done`                                                |
|      | `desk-cozy-evening-1.jpg`              | browse-real-photo | 9.2                       | cozy lamp-lit wooden home desk at evening, warm glow, small plant silhouette, golden bokeh, no people/brands | see ATTRIBUTION.md                  | `done`                                                |


Render gate: Section 9 render is BLOCKED until the two shared reuses (`trophy-gold-parody.png`,
`receipt-endless-roll.png`) and both browse bases are in `assets/`. The subscribe UI is CSS - no asset
file. (`peace_sign_calm_open_mouth.png` pose is already copied.)

Sourcing notes (Section 9 browse pass): both from StockSnap (CC0, no credit needed). SUBSTITUTION:
`desk-cozy-evening-1` is a warm lamp-lit home console (not a work-desk) but hits the cues (lamp glow from
the right, fern silhouette, golden bokeh); minor low-frame book spines sit under the render card zone.
Both are 960w upscales (soft - swap if needed).

## Cross-Section Shared Registry (reuse - do NOT re-prompt)

One PNG per subject serves every section. These already have prompts earlier in this manifest; when a
section says `reuse`, the SAME file is used - never regenerate a second copy.


| Filename                       | Prompt home     | Used across                                    |
| ------------------------------ | --------------- | ---------------------------------------------- |
| `trophy-gold-parody.png`       | S1 Prompt G1    | S1, S2, S4.9, S7.2, S8.1/8.3/8.6, S9.1/9.2     |
| `receipt-endless-roll.png`     | S1 Prompt G2    | S1, S3.1, S4.3, S5.7, S6.7, S7.1/7.9, S8, S9.1 |
| `gold-safe-fat.png`            | S4 Prompt S4-G3 | S4.2, S4.5, S4.7                               |
| `cash-bundle-generic.png`      | S4 Prompt S4-G4 | S4.2, S4.7, S4.9                               |
| `drain-grate-ornate.png`       | S5 Prompt S5-G3 | S5.1 (x3), S5.2, S5.4, S5.6                    |
| `money-pile-party.png`         | S5 Prompt S5-G2 | S5.1, S5.2, S5.4, S5.6                         |
| `banknote-single-crisp.png`    | S5 Prompt S5-G4 | S5.2, S5.4, S5.5, S5.6                         |
| `feeding-bowl-maintenance.png` | S6 Prompt S6-G3 | S6.2, S6.7                                     |
| `podium-suits-trio.png`        | S7 Prompt S7-G1 | S7.1, S7.2, S7.3                               |
| `tag-paper-string.png`         | S8 Prompt S8-G1 | S8.1 (x3)                                      |


