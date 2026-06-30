# Asset Manifest - Why The Internet Is Full Of Garbage Now

Source of truth for `render`. Sections 1 + 2 + 3 implemented `2026-06-28` by `visual-implement`.
Image assets are ISOLATED elements saved in `assets/`; poses in `assets/poses/` (transparent RGBA cutouts,
use directly). Browsed real photos: licenses in `ATTRIBUTION.md`.

## Section 1: Hook - assets


| Filename                         | Type              | Used in scenes | Description                                                                                                                                                     | Prompt (if generate) | Source/License                                               | Status                                                                                      |
| -------------------------------- | ----------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| `couch-phone-evening-1.jpg`      | browse-real-photo | 1.1            | warm lamp-lit living room, no faces/brands                                                                                                                      | -                    | rawpixel CC0 1.0 (see ATTRIBUTION)                           | done (verified: clean, warm; ~1024px preview)                                               |
| `dark-room-phone-glow-1.jpg`     | browse-real-photo | 1.2            | a hand holding a device in a very dark room (hand only, no face)                                                                                                | -                    | rawpixel CC0 1.0                                             | done (verified: moody/dark, hand ok; reads "device in the dark" more than "screen glow")    |
| `cozy-laptop-desk-1.jpg`         | browse-real-photo | 1.3            | laptop + coffee on a warm wooden desk                                                                                                                           | -                    | rawpixel CC0 1.0 (Markus Spiske)                             | done (not eyeballed; low risk)                                                              |
| `phone-on-table-screen-on-1.jpg` | browse-real-photo | 1.4            | a tablet showing a generic analytics dashboard on a wood desk, no faces                                                                                         | -                    | stocksnap CC0 1.0 (WDnet Studio)                             | done (verified: clean, no brand/face; 960px)                                                |
| `social-scroll-livingroom-1.jpg` | browse-real-photo | 1.5            | clean modern living room (leather sofa, yellow chairs, plant), no faces/brands                                                                                  | -                    | stocksnap CC0 1.0 (Dan Gold)                                 | done (verified: clean modern; 960px)                                                        |
| `shrimp-jesus.jpg`               | browse-real-photo | 1.5, 1.8       | the iconic Facebook AI-slop "Shrimp Jesus" image                                                                                                                | -                    | Wikimedia Commons, **Public Domain**                         | done (1900x1140)                                                                            |
| `newsroom-blur-1.jpg`            | browse-real-photo | 1.6            | press / newspaper backdrop                                                                                                                                      | -                    | rawpixel CC0 1.0                                             | done (not eyeballed; low risk)                                                              |
| `fake-news-card.png`             | generate          | 1.6            | isolated fake news-article card (vague AI headline re an event that never happened + uncanny AI thumbnail), transparent bg, NO real outlet branding             | see prompt below     | -                                                            | render-CSS preferred (build as real-UI); PNG fallback `prompt-ready / awaiting generation`  |
| `music-studio-blur-1.jpg`        | browse-real-photo | 1.7            | recording-studio mixing console close-up, people-free                                                                                                           | -                    | Wikimedia Commons CC0 1.0 (g_sakketos)                       | done (verified: people-free; **SSL/XLogic branding visible - blur/crop or swap at render**) |
| `fake-band-card.png`             | generate          | 1.7            | isolated fake music-app artist card (invented band, uncanny AI promo photo, "1,000,000+ monthly listeners", play bar), transparent bg, NO real Spotify branding | see prompt below     | -                                                            | render-CSS preferred (build as real-UI); PNG fallback `prompt-ready / awaiting generation`  |
| `grey-sludge-flood-1.jpg`        | browse-real-photo | 1.8, 1.9       | murky grey/green water surface (the garbage-flood motif)                                                                                                        | -                    | Wikimedia Commons CC0 1.0 (Merstel007, "Preuves flottantes") | done (4000x3000 full-res)                                                                   |
| `ai-extra-fingers-hand.png`      | browse-real-photo | 1.8            | AI-generated hand with extra/wrong fingers (a slop "tell")                                                                                                      | -                    | Wikimedia Commons, **Public Domain**                         | done (512x704)                                                                              |




### Poses used (in `assets/poses/`, copied from library)


| Pose file                              | Scene | Library source                                                                                             |
| -------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------- |
| `holding_phone_pointing_smile.png`     | 1.1   | `.agents/_shared/assets/wit/poses/` (substituted for plan's `holding_phone_looking_content` - not on disk) |
| `skeptical_side_eye_doubtful.png`      | 1.2   | library                                                                                                    |
| `ok_hand_sign_content_closeup.png`     | 1.3   | library (substituted for plan's `ok_hand_sign_content_relaxed` - not on disk)                              |
| `deadpan_unimpressed_half_lidded.png`  | 1.4   | library                                                                                                    |
| `cringe_uneasy_drool.png`              | 1.5   | library                                                                                                    |
| `pondering_skeptical_hand_on_chin.png` | 1.6   | library                                                                                                    |
| `mildly_surprised_hand_at_chin.png`    | 1.7   | library                                                                                                    |
| `swimming_underwater_goggles_cap.png`  | 1.8   | library                                                                                                    |
| `pointing_up_curious_open_mouth.png`   | 1.9   | library                                                                                                    |




## Generate prompts (paste into ChatGPT; these cards are PNG fallbacks if not built as render-CSS)

- [x] `fake-news-card.png`

> Attach: none. Create a single, clean, ISOLATED illustration of a generic online news-article card on a FULLY TRANSPARENT background, flat modern web-UI style. The white rounded card contains, top to bottom: a rectangular thumbnail image area showing a slightly TOO-perfect, uncanny AI-style photo of a crowded street parade with subtly wrong details (a warped face in the distance, an impossible building); a bold black headline reading "Crowds Gather For Parade That Was Never Scheduled"; one short grey subheading bar; a faint source row = a small grey circle avatar + a short grey bar (NO real logo, NO brand name); and a small timestamp "2h ago". Rounded corners, soft drop shadow. Do NOT include: any real news-outlet name or logo, any watermark, any readable real brand, any UI chrome outside the card, any border. High resolution, sharp, isolated element only.

- [x] `fake-band-card.png`

> Attach: none. Create a single, clean, ISOLATED illustration of a generic music-streaming "artist" card on a FULLY TRANSPARENT background, flat modern DARK-UI style. The dark rounded panel contains: a square artist photo (a slightly too-smooth, uncanny AI-style promo photo of a generic four-piece indie band with subtly wrong hands and faces); an invented band name "THE VELVET HOURS" in bold white; a line reading "1,042,318 monthly listeners" in light grey; a round green play button; and a thin play/progress bar. Do NOT include: the real Spotify logo or name, any real brand, any real person's likeness, any watermark, any extra text. High resolution, sharp, isolated element only.



## Notes for render

- The two cards are best built as CSS real-UI (owner's standing preference) directly in the render; the
PNG prompts above are only a fallback if a generated image is preferred. If built in CSS, the two
`.png` filenames stay reserved/unused.
- Most real bases are Openverse preview-res (~960-1024px); `grey-sludge-flood-1.jpg`, `music-studio-blur-1.jpg`,
and `shrimp-jesus.jpg` are full-res. If a preview base looks soft at 1920, swap to a full-res source.
- `music-studio-blur-1.jpg` has visible SSL/XLogic branding - keep it heavily blurred/cropped behind the
card, or swap to a brand-free music base (e.g. vinyl records, headphones on dark).
- All real photos are CC0/Public Domain; attribution recorded in `ATTRIBUTION.md`.



## Section 2: It Has A Name: Slop - assets (implemented 2026-06-28)


| Filename                    | Type              | Used in scenes | Description                                                   | Source/License                         | Status       |
| --------------------------- | ----------------- | -------------- | ------------------------------------------------------------- | -------------------------------------- | ------------ |
| `grey-sludge-flood-1.jpg`   | reuse             | 2.1, 2.5, 2.8  | the slop/flood motif base (graded per scene)                  | already in assets/ (S1)                | done (reuse) |
| `pig-trough-slop-1.jpg`     | browse-real-photo | 2.2            | real pig (clear, lying in pen), no faces                      | Wikimedia/Flickr CC0 (see ATTRIBUTION) | done         |
| `dictionary-open-1.jpg`     | browse-real-photo | 2.3            | real open OED-style dictionary, no faces                      | Wikimedia CC BY-SA 4.0                 | done         |
| `toy-robot-1.jpg`           | browse-real-photo | 2.4            | real vintage black/red tin toy robot, no faces                | Wikimedia CC BY-SA 3.0                 | done         |
| `corkboard-redstring-1.jpg` | browse-real-photo | 2.6            | real cork board + red pin + blank note (render adds string/X) | rawpixel CC0 1.0                       | done         |
| `coins-pile-1.jpg`          | browse-real-photo | 2.7            | real pile of coins, bright, no faces                          | rawpixel CC0 1.0                       | done         |


Section 2 poses (library, transparent - copy directly to `assets/poses/`): `presenting_open_palm_talking`,
`annoyed_disgusted_open_frown`, `proud_explaining_hand_on_chest_hand_on_hip`, `eyes_closed_talking_open_palm`,
`deadpan_unimpressed_half_lidded` (have), `skeptical_side_eye_doubtful` (have),
`lecturing_finger_raised_eyes_closed`, `worried_uneasy_wide_eyes`.
Section 2 render-CSS (no asset file): "SLOP" stamp, dictionary entry + WotY badge, "AI = EVIL ROBOTS"
crossed label, "A MASTER PLAN" crossed label, ATTENTION-vs-QUALITY chips, "STILL RISING".

## Section 3: What Slop Actually Is - assets (v2 REBUILD 2026-06-28, generate-forward, no sludge)

GENERATE heroes (write prompts in visual-implement -> owner generates in ChatGPT + drops in; ISOLATED
elements, transparent bg, NOT pre-composed scenes):


| Filename                     | Type     | Used in scenes | Description                                                                            | Status                             |
| ---------------------------- | -------- | -------------- | -------------------------------------------------------------------------------------- | ---------------------------------- |
| `slop-machine.png`           | generate | 3.1, 3.8       | surreal content-grinder (brain in -> grey slop out); section motif                     | prompt-ready / awaiting generation |
| `ai-influencer-perfect.png`  | generate | 3.2            | uncanny too-perfect AI influencer headshot (non-existent person)                       | prompt-ready / awaiting generation |
| `ai-influencer-melting.png`  | generate | 3.3            | the same influencer glitching/melting, 6-7 finger hand                                 | prompt-ready / awaiting generation |
| `gibberish-melting-sign.png` | generate | 3.4            | neon shop sign with garbled melting nonsense letters                                   | prompt-ready / awaiting generation |
| `coca-coola-ad-fail.png`     | generate | 3.5            | cheesy AI holiday soda ad, deformed santa, cursive "Coca-Coola" (parody, NO real logo) | prompt-ready / awaiting generation |
| `cost-crush-pile.png`        | generate | 3.6            | avalanche of melting clocks + eyeballs + cracked hearts                                | prompt-ready / awaiting generation |
| `slop-firehose.png`          | generate | 3.7            | giant hose/pipe blasting a torrent of grey sludge                                      | prompt-ready / awaiting generation |
| `slop-clone.png`             | generate | 3.7            | one identical featureless grey "fake person" blob (tiled)                              | prompt-ready / awaiting generation |
| `certified-slop-stamp.png`   | generate | 3.8            | big red wooden "CERTIFIED SLOP" rubber stamp                                           | prompt-ready / awaiting generation |
| `robot-human-mask.png`       | generate | 3.9            | chrome robot holding a flimsy human mask, screaming into a mic (payoff)                | prompt-ready / awaiting generation |


FRESH browse bases (no faces, full-HD; CC0/CC with attribution):


| Filename                 | Type              | Used in scenes | Description                               | Status |
| ------------------------ | ----------------- | -------------- | ----------------------------------------- | ------ |
| `factory-interior-1.jpg` | browse-real-photo | 3.1, 3.8       | grimy real factory/industrial interior    | done   |
| `studio-backdrop-1.jpg`  | browse-real-photo | 3.2, 3.3       | glossy seamless studio backdrop           | done   |
| `night-storefront-1.jpg` | browse-real-photo | 3.4            | real night street/storefront              | done   |
| `holiday-street-1.jpg`   | browse-real-photo | 3.5            | real festive holiday street/market lights | done   |
| `server-room-1.jpg`      | browse-real-photo | 3.6            | real server room / data center aisle      | done   |
| `pipes-industrial-1.jpg` | browse-real-photo | 3.7            | real industrial pipes/valves              | done   |
| `dark-stage-mic-1.jpg`   | browse-real-photo | 3.9            | real dark stage w/ spotlight + microphone | done   |


Section 3 poses (library, transparent - copy directly): `presenting_screen_announcing_open_mouth`,
`delighted_blushing_sparkle_eyes`, `panic_hands_on_cheeks_scream`, `shrug_confused_flat_mouth`,
`big_open_mouth_laugh_presenting_closeup`, `lying_down_fainted_dead`, `shocked_sweating_dismayed`,
`smug_raised_eyebrow_smirk`, `deadpan_unimpressed_half_lidded`.
Section 3 render-CSS: "3 THINGS" / marks / red tell-circles / checks / "10,000+" counter / maker+cost
labels (time/attention/trust) / volume-MAX meter / "AT FULL VOLUME".

ORPHANED by the v2 rebuild (v1 used them; v2 does not - keep unless owner asks to delete; do NOT reuse as a crutch):
`gallery-wall-1.jpg`, `ai-face-does-not-exist.png`, `holiday-bokeh-red-1.jpg`, `hourglass-time-1.jpg`.
(`grey-sludge-flood-1.jpg`, `ai-extra-fingers-hand.png`, `shrimp-jesus.jpg` remain used by S1/S2.)

## Section 3 generate prompts (paste each into ChatGPT, save the PNG to `assets/<filename>`)

All ISOLATED elements on a FULLY TRANSPARENT background (a single subject, no scene, no real logos, no
real identifiable people, no watermark). "Channel cartoon" = flat 2D, thick uniform black outline, flat
fills, bold and readable (so it sits next to the white WIT mascot).

- [x] `slop-machine.png`

> Attach: none. A single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with a thick uniform black outline. A grotesque industrial CONTENT-GRINDER machine: a big funnel/hopper on top, a toothy grinder mouth in the middle, and a conveyor spout at the bottom extruding lumpy grey sausage-like "slop" into a small overflowing bin. Pipes, rivets, a couple of dials. Slightly cartoon-menacing but funny. Do NOT include: any background, any text/labels, any logo, any human. Sharp, high-res, isolated object only.

- [x] `ai-influencer-perfect.png`

> Attach: none. A single ISOLATED cutout on a FULLY TRANSPARENT background. A photorealistic but UNCANNY "AI influencer" head-and-shoulders portrait of a non-existent person: flawless plastic-smooth skin, too-symmetrical face, glossy studio lighting, a faint over-perfect sparkle. It should look impressive at a glance. Do NOT include: any background, any text, any watermark, any logo, any real or recognizable person. High-res, isolated subject only.

- [x] `ai-influencer-melting.png`

> Attach: none. A single ISOLATED cutout on a FULLY TRANSPARENT background. The SAME uncanny AI influencer as a "glitched" version: features melting and smearing, one eye drifting, datamosh/jpeg artifacts, and one hand raised showing SIX or SEVEN messy fingers. Horror-funny, clearly "AI gone wrong." Do NOT include: any background, any text, any watermark, any real person. High-res, isolated subject only.

- [x] `gibberish-melting-sign.png`

> Attach: none. A single ISOLATED cutout on a FULLY TRANSPARENT background. A glowing neon/shop SIGN whose letters are garbled, half-melted nonsense (fake words like "GRAND OPNEING", "DLISCOUNTS", "50%FRE"), letters dripping and warped, a few backwards. Looks AI-generated. Do NOT include: any background wall, any real brand, any watermark, any human. High-res, isolated sign only.

- [x] `coca-coola-ad-fail.png`

> Attach: none. A single ISOLATED cutout on a FULLY TRANSPARENT background, glossy holiday-ad style. A cheesy AI-generated festive soda advertisement: a GENERIC red soda can (no real brand), a slightly deformed jolly cartoon santa with a wrong-fingered mitten, and bold cursive misspelled text "Coca-Coola". Clearly a parody/AI fail. Do NOT include: the real Coca-Cola logo or any real trademark/brand, any real person, any background, any watermark. High-res, isolated ad graphic only.

- [x] `cost-crush-pile.png`

> Attach: none. A single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with thick black outline. A towering avalanche/heap tumbling downward, built from melting CLOCKS, staring disembodied EYEBALLS, and cracked HEARTS all jumbled together (representing "time, attention, trust"). It should look like it is crashing down to crush something below. Do NOT include: any background, any text, any logo, any human. High-res, isolated pile only.

- [x] `slop-firehose.png`

> Attach: none. A single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with thick black outline. A giant industrial FIRE HOSE / fat pipe nozzle blasting a powerful torrent/spray of lumpy grey sludge out to one side under high pressure. Dynamic motion. Do NOT include: any background, any text, any logo, any human. High-res, isolated object only.

- [x] `slop-clone.png`

> Attach: none. A single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with thick black outline. ONE featureless grey blob "person": a generic grey humanoid silhouette-blob with a blank face and a single dead identical smile - the "identical fake person." Plain, mass-produced look. Do NOT include: any background, any text, any logo, any real person. High-res, single isolated figure only.

- [x] `certified-slop-stamp.png`

> Attach: none. A single ISOLATED illustration on a FULLY TRANSPARENT background. A big red rubber STAMP impression reading "CERTIFIED SLOP" in bold distressed uppercase inside a red double-ring border, slightly rotated, ink-textured. Do NOT include: any background, any extra text, any logo, any human. High-res, isolated stamp only.

- [x] `robot-human-mask.png`

> Attach: none. A single ISOLATED cutout on a FULLY TRANSPARENT background. A creepy chrome animatronic ROBOT holding a flimsy, thin HUMAN face-MASK slightly away from its own mechanical face, mouth-hole wide open as if SCREAMING, leaning toward a vintage microphone. Unsettling but a little comedic. Do NOT include: any background, any text, any logo, any real identifiable person. High-res, isolated subject (robot + mask + mic) only.



## Section 4: The Machine That Feeds Itself - assets (implemented 2026-06-28, generate-forward)

The mechanism core. Section motif = THE SELF-FEEDING ENGINE (`slop-engine-loop.png`), a callback to S3's
slop-machine. No image generator connected -> the 8 GENERATE heroes are GENERATED + composited in render S4 (2026-06-30) (owner pastes each prompt into ChatGPT, drops the PNG into `assets/<filename>`). The 7 browse
bases are sourced + verified (people-free). Poses copied. `slop-clone.png` reused from S3.

### Browse bases (done; licenses in ATTRIBUTION.md)


| Filename                     | Type              | Used in       | Description                                                                                                                       | Status                                                           |
| ---------------------------- | ----------------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `dark-machine-hall-1.jpg`    | browse-real-photo | 4.1, 4.8, 4.9 | real pump/valve machine room (white pipes, blue pump, gauges, valve wheels), people-free; grade DARK at render                    | done (verified; rawpixel preview ~1024px - swap if soft at 1920) |
| `vintage-film-set-1.jpg`     | browse-real-photo | 4.2           | vintage film camera + clapperboard + "SCENARIO" notebook on warm wood, people-free; generic film text (no brand)                  | done (verified; rawpixel preview-res)                            |
| `clean-bright-desk-1.jpg`    | browse-real-photo | 4.3           | clean bright desk + laptop + plant, people-free; **DELL logo on the laptop bezel - crop/blur at render**                          | done (verified; stocksnap 960w - swap if soft)                   |
| `casino-slot-machines-1.jpg` | browse-real-photo | 4.4           | a row of casino slot machines, vivid; **crop the far-left background (tiny distant blurred shapes); slot-game titles incidental** | done (verified; rawpixel preview-res)                            |
| `dark-spotlight-stage-1.jpg` | browse-real-photo | 4.5           | red theatre curtain in an arch with a central spotlight glow, people-free; clean negative space for the pivot text                | done (verified; rawpixel preview-res)                            |
| `wall-of-screens-grid-1.jpg` | browse-real-photo | 4.6           | a wall stack of glowing vintage CRT TVs (a wall of feeds), people-free; minor vintage SONY/PHILCO labels (incidental)             | done (verified; Wikimedia full-res 4256x2832)                    |
| `cctv-control-room-1.jpg`    | browse-real-photo | 4.7           | a NASA-style mission-control console wall (monitors, headsets, blue light), people-free, brand-free                               | done (verified; rawpixel preview-res)                            |




### Generate heroes (DONE - generated + composited in render S4 2026-06-30)


| Filename                      | Type     | Used in       | Description                                                                                       | Status                             |
| ----------------------------- | -------- | ------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------- |
| `slop-engine-loop.png`        | generate | 4.1, 4.8, 4.9 | the self-feeding engine (prompt in -> slop out -> coins -> return pipe loops back); section motif | done (generated; composited in render S4 2026-06-30) |
| `money-trail-coins.png`       | generate | 4.1           | a glowing curving trail of gold coins ("follow the money")                                        | done (generated; composited in render S4 2026-06-30) |
| `old-creation-cost-pile.png`  | generate | 4.2           | a stacked pile: film camera + typewriter + guitar + hourglass + "$$$" tag                         | done (generated; composited in render S4 2026-06-30) |
| `prompt-box-instant.png`      | generate | 4.3           | a glowing AI prompt box extruding an instant content card + a small stopwatch                     | done (generated; composited in render S4 2026-06-30) |
| `engagement-slot-machine.png` | generate | 4.4           | a slot machine with like/click/clock reels, coins pouring out                                     | done (generated; composited in render S4 2026-06-30) |
| `attention-quality-scale.png` | generate | 4.5           | a balance scale: attention pan (eyes/likes/play) crashes down, quality pan (a medal) flies up     | done (generated; composited in render S4 2026-06-30) |
| `flood-the-zone-cannon.png`   | generate | 4.6           | a cannon blasting a barrage of identical blank grey post-cards                                    | done (generated; composited in render S4 2026-06-30) |
| `blindfold-sorter-robot.png`  | generate | 4.7           | a blindfolded sorter robot stamping two identical items the same                                  | done (generated; composited in render S4 2026-06-30) |


Reuse: `slop-clone.png` (from S3 3.7) -> 4.6 (tiled barrage) / 4.7 (the belt blob). Already in `assets/`.

Section 4 poses (library, transparent - copied directly to `assets/poses/`): `smug_sly_smirk_leaning`,
`presenting_open_palm_talking` (have), `sly_scheming_twiddling_fingers`, `boss_suit_sunglasses_sparkle`,
`lecturing_finger_raised_eyes_closed` (have), `manic_gleeful_googly_eyes`, `annoyed_disgusted_open_frown`
(have), `shocked_sweating_dismayed` (have), `deadpan_unimpressed_half_lidded` (have). All 9 present.

Section 4 render-CSS (no asset file): numbered STEP chips, the loop-ring HUD, the `$$$ -> $0` counter +
`10s` timer, engagement chips (clicks/likes/time spent), struck `GOOD/QUALITY` + `ENGAGEMENT =`,
"ATTENTION, not quality", the `VIRAL` card, `1 vs 1,000` labels, `CAN'T TELL` + `✓ SERVED` tags, the loop
labels (slop -> $ -> more slop), "THE MACHINE FEEDS ITSELF", the 3 verdict stamps
(CHEAP TO MAKE / PAID BY ATTENTION / IMPOSSIBLE TO FILTER), "of course it floods.", and the grey sludge overflow.

## Section 4 generate prompts (paste each into ChatGPT, save the PNG to `assets/<filename>`)

All ISOLATED elements on a FULLY TRANSPARENT background (a single subject, no scene, no real logos, no
real people, no watermark). "Channel cartoon" = flat 2D, thick uniform black outline, flat fills, bold and
readable so it sits next to the white WIT mascot. All on-screen wording is added in render (CSS), so the
assets themselves stay text-free.

- [x] `slop-engine-loop.png`

> Attach: none. Create a single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with a thick uniform black outline and flat color fills (no gradients, no shading). Subject: a grotesque circular "self-feeding" content machine drawn as ONE connected contraption forming a closed loop: a funnel/hopper at the top-left (where a glowing rectangular "prompt" would drop in), a central grinder/gears box, a conveyor belt at the bottom extruding lumpy grey sausage-like "slop" into a small bin, a coin chute on the right spitting gold coins, and a big curved return pipe that arcs from the coin chute all the way back up to the funnel so the whole machine is a circle. Add rivets, two round gauges, and small steam/motion puffs. Slightly menacing but funny. Composition: roughly circular, centered, generous margin. Do NOT include: any background, any text/letters/numbers/labels, any logo or brand, any human or face, any watermark, any gradient. Output: one high-resolution PNG, fully transparent background, isolated object only.

- [x] `money-trail-coins.png`

> Attach: none. Create a single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with a thick uniform black outline and flat fills. Subject: a curving trail/stream of shiny gold coins flowing from the lower-left up toward the upper-right (a "follow the money" path), the coins overlapping along the curve, larger in front and smaller toward the back, with a couple of faint glowing footstep marks among them. A simple "$" symbol embossed on the coins is fine; no other text. Do NOT include: any background, any words/letters/numbers (besides the "$" on coins), any logo or brand, any human, any watermark, any gradient. Output: one high-resolution PNG, fully transparent background, isolated element only.

- [x] `old-creation-cost-pile.png`

> Attach: none. Create a single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with a thick uniform black outline and flat fills. Subject: a tidy stacked PILE representing "expensive old-school content creation": a vintage movie film camera, an old typewriter, an electric guitar, and a large hourglass, stacked and leaning together, bound with a paper price tag that shows three dollar signs "$$$". Each object clearly recognizable; bold and readable. Do NOT include: any background, any text other than the "$$$" on the tag, any brand or logo, any human, any watermark, any gradient. Output: one high-resolution PNG, fully transparent background, isolated element only.

- [x] `prompt-box-instant.png`

> Attach: none. Create a single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with a thick uniform black outline and flat fills. Subject: a glowing rounded chat/AI "prompt" input box (an empty text field with a blinking cursor line and a small sparkle), instantly extruding a tiny finished "content" card out of its right side; beside it a small stopwatch/timer. Convey "instant and almost effortless". Do NOT include: any readable text/words/letters/numbers (the input box and timer faces are blank/iconic only), any brand or logo or app name, any human, any background, any watermark, any gradient. Output: one high-resolution PNG, fully transparent background, isolated element only.

- [x] `engagement-slot-machine.png`

> Attach: none. Create a single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with a thick uniform black outline and flat fills. Subject: a classic slot machine with a lever on the side and three reel windows across the middle, each reel showing one simple ICON - reel 1 a heart (a "like"), reel 2 a mouse-cursor/click arrow, reel 3 a clock - and a tray at the bottom overflowing with gold coins. Bright and a little tacky; bold and readable. Do NOT include: any text/words/letters/numbers, any brand or logo, any human, any background, any watermark, any gradient. Output: one high-resolution PNG, fully transparent background, isolated element only.

- [x] `attention-quality-scale.png`

> Attach: none. Create a single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with a thick uniform black outline and flat fills. Subject: a classic two-pan balance scale tipped strongly to one side: the LEFT pan is crammed full and crashing DOWN under a heavy pile of glowing cartoon eyeballs, heart "like" icons, and triangular play-buttons; the RIGHT pan holds a single small gold medal and flies UP high because it weighs almost nothing. The imbalance is dramatic and obvious. Do NOT include: any text/words/letters/numbers, any brand or logo, any real human face (the eyeballs are simple cartoon eyes, not a realistic face), any background, any watermark, any gradient. Output: one high-resolution PNG, fully transparent background, isolated element only.

- [x] `flood-the-zone-cannon.png`

> Attach: none. Create a single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with a thick uniform black outline and flat fills. Subject: a cartoon cannon (or catapult) tilted up and mid-blast, firing a wide spray/barrage of many IDENTICAL small blank grey rounded rectangular cards (like a flurry of identical posts) up and out to the right, with a puff of smoke at the muzzle. All the cards are the same plain grey, scattering in an arc. Do NOT include: any text/words/letters/numbers on the cards, any brand or logo, any human, any background, any watermark, any gradient. Output: one high-resolution PNG, fully transparent background, isolated element only.

- [x] `blindfold-sorter-robot.png`

> Attach: none. Create a single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with a thick uniform black outline and flat fills. Subject: a friendly but clueless boxy gatekeeper robot wearing a BLINDFOLD over its single camera-eye (or its eye drawn as a grey "no-signal" X), holding up a big blank rubber STAMP in one hand, standing behind a small conveyor belt that carries two identical-looking items it is about to stamp the same way. Convey "it cannot tell the difference". Bold and readable. Do NOT include: any text/words/letters/numbers (the stamp face is blank), any brand or logo, any realistic human face (it is clearly a machine), any background, any watermark, any gradient. Output: one high-resolution PNG, fully transparent background, isolated element only.



## Section 5: It Already Got Out - assets (implemented 2026-06-28, generate-forward)

The spread montage; the GREY-SLUDGE FLOOD motif returns (reuse `grey-sludge-flood-1.jpg`). All 6 GENERATE
heroes are now generated and composited in the render S5 build (2026-06-30). 4 fresh browse bases sourced +
verified. 2 reuse bases verified. All 7 poses already in `assets/poses/`.

### Browse bases (done; licenses in ATTRIBUTION.md)


| Filename                       | Type              | Used in  | Description                                                                                                                                                                                          | Status                                         |
| ------------------------------ | ----------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| `music-stage-lights-1.jpg`     | browse-real-photo | 5.2      | a grand empty concert hall (rows of empty seats, orchestra setup on stage), people-free, no real-artist name                                                                                         | done (verified; rawpixel preview-res ~1024)    |
| `forest-floor-mushrooms-1.jpg` | browse-real-photo | 5.3      | a mossy tree stump with a cluster of small brown mushrooms, blurred forest bg, people-free, no text                                                                                                  | done (verified; rawpixel preview-res)          |
| `living-room-tv-1.jpg`         | browse-real-photo | 5.4, 5.5 | a clean modern living room with a black TV (screen OFF) on a stand, lamp, coffee table; people-free, brand-free; float the kids-screen UI on the black TV                                            | done (verified; rawpixel preview-res)          |
| `office-desk-inbox-1.jpg`      | browse-real-photo | 5.6      | a clean bright modern desk by a city window with a monitor + keyboard + mouse; **Apple logo on the monitor bezel + Apple peripherals - crop/blur or cover with the CSS workslop-document at render** | done (verified; stocksnap 960w - swap if soft) |




### Generate heroes (done; generated + composited in render S5, 2026-06-30)


| Filename                       | Type     | Used in | Description                                                                         | Status                                                          |
| ------------------------------ | -------- | ------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| `slop-bursting-phone.png`      | generate | 5.1     | a phone with grey sludge gushing/overflowing out of its screen                      | done (generated; real RGBA; composited in render S5 2026-06-30) |
| `ai-band-uncanny.png`          | generate | 5.2     | an uncanny 4-piece AI "band" promo (non-existent people, wrong hands)               | done (generated; composited in render S5 2026-06-30)            |
| `mushroom-guide-book.png`      | generate | 5.3     | an AI mushroom-foraging guide book with a subtly-wrong AI mushroom on the cover     | done (generated; checkerboard keyed to true alpha; raw in `_raw-checkerboard/`; composited in render S5 2026-06-30) |
| `six-legged-horse-cartoon.png` | generate | 5.5     | a garish low-quality AI kids-cartoon horse with SIX legs, dead eyes                 | done (generated; checkerboard keyed to true alpha; raw in `_raw-checkerboard/`; composited in render S5 2026-06-30) |
| `workslop-document.png`        | generate | 5.6     | a glossy official-looking AI document whose body text is meaningless wavy filler    | done (generated; real RGBA; covers the 5.6 base Apple logo; composited in render S5 2026-06-30) |
| `real-photo-lifeline.png`      | generate | 5.7     | one ordinary framed real-looking snapshot (the one real thing held above the flood) | done (generated; checkerboard keyed to true alpha; raw in `_raw-checkerboard/`; composited in render S5 2026-06-30) |


Reuse: `social-scroll-livingroom-1.jpg` (S1) -> 5.1; `grey-sludge-flood-1.jpg` (S1/S2 flood motif) -> 5.7
(and the rising sludge water-line 5.1-5.6). Both already in `assets/`.

Section 5 poses (library, transparent - all already in `assets/poses/`): `worried_uneasy_wide_eyes`,
`skeptical_side_eye_doubtful`, `panic_hands_on_cheeks_scream`, `annoyed_disgusted_open_frown`,
`cringe_uneasy_drool`, `exhausted_dead_inside_eye_bags`, `swimming_underwater_goggles_cap`.

Section 5 render-CSS (no asset file): the rising grey sludge water-line, the music-app listeners card +
`0 REAL MEMBERS`, the red `DANGER` skull + `can actually KILL you`, the kid-video thumbnail grid + `SLOP`
stamps + giant `40%` + `40 out of every 100`, the `6 LEGS?!` circle + `A B C ?`, the `WORKSLOPPED` stamp +
`~2 HOURS` clock, the four bobbing domain icons (feed / music / tablet / inbox) + labels, and
`congratulations.`.

## Section 5 generate prompts (paste each into ChatGPT, save the PNG to `assets/<filename>`)

All ISOLATED elements on a FULLY TRANSPARENT background (a single subject, no scene, no real logos, no real
identifiable people, no watermark). On-screen wording is added in render (CSS), so the assets stay text-free.

- [x] `slop-bursting-phone.png`

> Attach: none. Create a single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with a thick uniform black outline and flat fills. Subject: a modern smartphone tilted at an angle with a thick gush of lumpy grey sludge BURSTING and overflowing out of its screen and pouring down past the bottom edge of the phone. The dramatic sludge overflow is the focus. Do NOT include: any background, any text/letters/numbers, any brand or logo or app icons (blank phone), any human, any watermark, any gradient. Output: one high-resolution PNG, fully transparent background, isolated object only.

- [x] `ai-band-uncanny.png`

> Attach: none. Create a single ISOLATED cutout on a FULLY TRANSPARENT background. A photorealistic but UNCANNY band promo photo of a FOUR-member music group of NON-EXISTENT people: too-smooth plastic skin, slightly-too-symmetrical faces, dead-perfect lighting, and subtly WRONG details (one hand with an extra finger, a guitar neck that melts/bends oddly), posed like a press shot. It should clearly look AI-generated and a little "off". Do NOT include: any real or recognizable person, any text/band name/letters, any brand or logo, any background, any watermark. Output: one high-resolution PNG, fully transparent background, isolated group cutout only.

- [x] `mushroom-guide-book.png`

> Attach: none. Create a single ISOLATED object on a FULLY TRANSPARENT background. A glossy paperback field-guide book, standing and angled, whose cover is dominated by a large photo of a SINGLE mushroom that looks subtly WRONG / AI-generated (impossible gills, a smeared melting cap, a faint extra stem). It should read as a cheap, AI-made foraging guide. Keep the title area blank/abstract (no readable words). Do NOT include: any readable title text/letters/author name, any real brand or publisher logo, any human, any background, any watermark. Output: one high-resolution PNG, fully transparent background, isolated book only.

- [x] `six-legged-horse-cartoon.png`

> Attach: none. Create a single ISOLATED illustration on a FULLY TRANSPARENT background, in a GARISH low-quality kids-cartoon style (over-bright clashing colors, slightly off proportions, dead glassy eyes) that deliberately looks like cheap AI "educational" content. Subject: a cartoon horse that clearly has SIX legs, standing and smiling blankly. Do NOT include: any text/letters/numbers, any brand or logo, any real/recognizable character likeness, any background, any watermark. Output: one high-resolution PNG, fully transparent background, isolated character only.

- [x] `workslop-document.png`

> Attach: none. Create a single ISOLATED object on a FULLY TRANSPARENT background. A glossy, official-looking business document / report page (or a small neat stack), beautifully formatted with headings, little charts, and bullet points - but all the "text" is meaningless wavy placeholder lines and the charts are nonsense. It should look impressive at a glance yet clearly say nothing. Do NOT include: any readable real words/letters/numbers (all text is abstract wavy lines), any brand or logo, any human, any background, any watermark. Output: one high-resolution PNG, fully transparent background, isolated document only.

- [x] `real-photo-lifeline.png`

> Attach: none. Create a single ISOLATED object on a FULLY TRANSPARENT background. One ordinary framed photograph in a simple white-border instant-photo / Polaroid-style frame, held upright, containing a warm, genuine, slightly imperfect real-looking snapshot (for example a candid outdoor moment, a sunset, or a pet) - it represents "the one real thing". Do NOT include: any readable text/letters, any brand or logo, any identifiable real person's face (keep any people distant, small, or back-turned, or show no people), any background outside the frame, any watermark. Output: one high-resolution PNG, fully transparent background, isolated framed photo only.



## Section 6: It's Not AI's Fault (And Not A Plot) - assets (implemented 2026-06-29, the honest turn)

Calmer "argument" section: real bases + CSS graphics + a few generated props. All 4 GENERATE props are
now generated and composited in the render S6 build (2026-06-30). 4 fresh browse bases sourced +
verified. 2 reuse bases verified. Poses copied (one substitution).



### Browse bases (done; licenses in ATTRIBUTION.md)


| Filename                 | Type              | Used in | Description                                                                                                                        | Status                                                |
| ------------------------ | ----------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `courtroom-1.jpg`        | browse-real-photo | 6.1     | a wooden courtroom judge's bench + arched paneled backdrop, people-free, brand-free, no text                                       | done (verified; rawpixel preview-res)                 |
| `clinic-scan-room-1.jpg` | browse-real-photo | 6.2     | an MRI/CT scan room (scanner + table + monitors), people-free; **faint Hitachi label on the scanner - minor, crop/blur if needed** | done (verified; rawpixel editor_1024, un-watermarked) |
| `workbench-tools-1.jpg`  | browse-real-photo | 6.3     | a dim garage workbench (drill press, vice, buckets, tools, brick wall), people-free; "the tool"                                    | done (verified; stocksnap 960w)                       |
| `empty-boardroom-1.jpg`  | browse-real-photo | 6.6     | a modern EMPTY boardroom (long table, chairs, off-screen TV, big windows), people-free, brand-free                                 | done (verified; rawpixel preview-res)                 |




### Generate props (done; generated + composited in render S6, 2026-06-30)


| Filename                   | Type     | Used in | Description                                                  | Status                             |
| -------------------------- | -------- | ------- | ------------------------------------------------------------ | ---------------------------------- |
| `artist-easel.png`         | generate | 6.2     | a simple artist's easel + canvas + palette + brush           | done (generated; checkerboard keyed to true alpha; raw in `_raw-checkerboard/`; composited in render S6 2026-06-30) |
| `tinfoil-hat.png`          | generate | 6.4     | a crumpled tinfoil "conspiracy" hat (empty)                  | done (generated; real RGBA; composited in render S6 2026-06-30) |
| `empty-villain-throne.png` | generate | 6.6     | an ominous empty villain throne with an unpressed red button | done (generated; checkerboard keyed to true alpha; raw in `_raw-checkerboard/`; composited in render S6 2026-06-30) |
| `uncuffable-incentive.png` | generate | 6.7     | a glowing gold `$` coin shrugging off a pair of handcuffs    | done (generated; checkerboard keyed to true alpha; raw in `_raw-checkerboard/`; composited in render S6 2026-06-30) |


Reuse: `corkboard-redstring-1.jpg` (S2 conspiracy board) -> 6.4, 6.5; `dark-spotlight-stage-1.jpg` (S4.5)
-> 6.7. Both already in `assets/`.

Section 6 poses (library, transparent - all now in `assets/poses/`): `hand_on_cheek_pondering_eyes_closed`
(SUBSTITUTE - the plan's `talking_hand_at_chin_eyes_closed` is listed in pose.md but is NOT on disk in the
library; synced into the S6 plan + master), `doctor_coat_stethoscope_listening`,
`pointing_up_curious_open_mouth`, `pondering_skeptical_hand_on_chin`, `unimpressed_smirk_closeup`,
`shrug_both_hands_up_smile`, `proud_explaining_hand_on_chest_hand_on_hip`.

Section 6 render-CSS (no asset file): the level balance scale + `let's be fair.`, the green `NOT SLOP`
checks + scan/AI badge, the `SLOP = LOW EFFORT x HIGH VOLUME` formula, `DEAD INTERNET THEORY` + red string

- `govt bots` note, the big red `X` + `it's dumber than that.`, `NOBODY IS IN CHARGE` / `NO VILLAIN` +
glowing `$`, and `YOU CANNOT ARREST AN INCENTIVE`.



## Section 6 generate prompts (paste each into ChatGPT, save the PNG to `assets/<filename>`)

All ISOLATED elements on a FULLY TRANSPARENT background, flat 2D cartoon (thick uniform black outline, flat
fills), bold and readable next to the white WIT mascot. On-screen wording is render CSS, so assets stay
text-free.

- [x] `artist-easel.png`

> Attach: none. Create a single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with a thick uniform black outline and flat fills. Subject: a simple wooden artist's easel holding a small blank canvas, with a paint palette and a brush leaning against it. Clean and friendly. Do NOT include: any background, any text/letters/numbers, any brand or logo, any human, any watermark, any gradient. Output: one high-resolution PNG, fully transparent background, isolated object only.

- [x] `tinfoil-hat.png`

> Attach: none. Create a single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with a thick uniform black outline and flat fills. Subject: a crumpled cone-shaped hat folded out of shiny aluminium/tin foil - the classic "conspiracy theorist" tinfoil hat - with creased reflective facets. It is empty (no head wearing it). Do NOT include: any background, any text/letters/numbers, any brand or logo, any human or head, any watermark, any gradient. Output: one high-resolution PNG, fully transparent background, isolated object only.

- [x] `empty-villain-throne.png`

> Attach: none. Create a single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with a thick uniform black outline and flat fills. Subject: an ominous oversized villain's throne (a tall spiky gothic back, dark with a red cushion), clearly UNOCCUPIED, with a big round red push-button on the right armrest that nobody is pressing. Convey "nobody is in charge". Do NOT include: any background, any text/letters/numbers, any brand or logo, any human or figure (the throne is empty), any watermark, any gradient. Output: one high-resolution PNG, fully transparent background, isolated object only.

- [x] `uncuffable-incentive.png`

> Attach: none. Create a single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with a thick uniform black outline and flat fills. Subject: a glowing gold dollar-sign ($) coin/medallion, smug and untouchable, with a pair of metal police HANDCUFFS bouncing and slipping off it and flying away (it cannot be arrested), plus small motion lines and a shine. A simple "$" on the coin is fine; no other text. Do NOT include: any background, any words/letters/numbers (besides the "$"), any brand or logo, any human, any watermark, any gradient. Output: one high-resolution PNG, fully transparent background, isolated object only.



## Section 7: Payoff: Attention In, Garbage Out - assets (implemented 2026-06-29, callback-heavy recap)

The calm payoff; deliberately CALLBACK-heavy (reuses the S4 engine + earlier tells). No image generator
connected -> the 1 GENERATE hero is `prompt-ready / awaiting generation`. 2 fresh browse bases sourced +
verified. Reuses verified on disk (incl. `slop-engine-loop.png`, now generated).

### Browse bases (done; licenses in ATTRIBUTION.md)


| Filename                   | Type              | Used in  | Description                                                                                                             | Status                                                                                                |
| -------------------------- | ----------------- | -------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `evidence-desk-1.jpg`      | browse-real-photo | 7.5      | an open book + a magnifying glass + a fountain pen + globes (a "study / examine the tells" desk), people-free, no brand | done (verified; rawpixel preview-res; book has incidental foreign text, covered by the CSS checklist) |
| `bright-window-calm-1.jpg` | browse-real-photo | 7.6, 7.7 | a single leafy plant in a vase against a soft bright window (calm, clear), people-free, brand-free, no text             | done (verified; rawpixel preview-res)                                                                 |




### Generate hero (prompt-ready / awaiting generation)


| Filename               | Type     | Used in | Description                                                                                           | Status                             |
| ---------------------- | -------- | ------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------- |
| `slop-wins-trophy.png` | generate | 7.2     | a grey slop blob on a #1 winner's podium holding up an ATTENTION trophy, a sad "quality" figure below | done (render 2026-06-30); delivered opaque RGB w/ baked checkerboard -> keyed out to true alpha (raw in `_raw-checkerboard/`) |


Reuse (all verified present in `assets/`): `dark-spotlight-stage-1.jpg` (S4 stage) -> 7.2 (base swap -
clean people-free award-podium photos were all real athletes); `dark-machine-hall-1.jpg` + `slop-engine-loop.png`
(S4 engine) -> 7.1, 7.3, 7.4, 7.7; `ai-extra-fingers-hand.png` (S1) -> 7.5 tell #1; `ai-influencer-perfect.png`
(S3) -> 7.5 tell #2.

Section 7 poses (library, transparent - all now in `assets/poses/`): `pointing_up_curious_open_mouth`,
`eyes_closed_talking_open_palm`, `lecturing_finger_raised_eyes_closed`, `deadpan_unimpressed_half_lidded`,
`presenting_screen_announcing_open_mouth`, `proud_explaining_hand_on_chest_hand_on_hip`,
`pointing_at_viewer_serious_accusing`.

Section 7 render-CSS (no asset file): `WHY?`, struck `AI IS EVIL`/`CONSPIRACY` + `pays for ATTENTION` +
`slop wins`, big `ATTENTION IN.` / `GARBAGE OUT.`, struck `BROKEN` + green `WORKING PERFECTLY ✓` +
`that is the problem.`, the `THE TELLS` checklist + the too-good headline card, the receding flood +
empowerment text + glasses glint, `we'll keep explaining the weird machine`, big `keep your eyes open.`.

## Section 7 generate prompt (paste into ChatGPT, save the PNG to `assets/<filename>`)

- [x] `slop-wins-trophy.png`

> Attach: none. Create a single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with a thick uniform black outline and flat fills. Subject: a grey blob "slop" creature (a featureless grey humanoid blob with a dumb grin) standing triumphantly on the tall #1 step of a three-step winner's podium, holding up a shiny gold trophy; on a lower step, a small sad, dull figure slumps (representing the "quality" that lost). Convey "the worthless thing won". Do NOT include: any text/letters/numbers, any brand or logo, any real person, any background, any watermark, any gradient. Output: one high-resolution PNG, fully transparent background, isolated group only.

## Section 8: Outro: Like, Share, Subscribe - assets (v2 gamified CTA rebuild 2026-06-30)

Short ~8s outro end-card. NO new generate or browse assets - the entire fake-YouTube card, mouse cursor,
buttons, and confetti are render-CSS/SVG; it reuses the calm base + 2 library poses.

Reuse (all verified present in `assets/`):
- `bright-window-calm-1.jpg` -> the single continuous scene (calm close).
- `channel-avatar.png` -> copied in from `.agents/_shared/assets/brand/channel-avatar.png` (the real WIT
  channel avatar, yellow circle) for the card's channel-row avatar (replaces the old "W" text circle).

Section 8 poses (library, transparent - in `assets/poses/`): `enthusiastic_point_big_smile` (CTA, points
at the card), `peace_sign_calm_open_mouth` (sign-off).

Section 8 render-CSS/SVG (no asset file): the entire fake YouTube card (WhyTube logo, video thumbnail,
title, gold "W" avatar, channel row, the `SUBSCRIBE`->`SUBSCRIBED` button + bell, the `LIKE`->Liked +
`SHARE` pills), an inline-SVG mouse cursor, a confetti burst (12 CSS squares), the glow ring, the "Link
copied!" toast, `"if this helped..."`, `"see you in the next one."`, and the `WHY IT WORKS` wordmark. All
icons are CSS shapes (thumb / arrow / bell), NOT emoji glyphs (emoji do not render in snapshot Chromium).

No generate prompts and no ATTRIBUTION rows for Section 8 (zero new generated/browsed assets).

