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



### `fake-news-card.png` ✅

> Attach: none. Create a single, clean, ISOLATED illustration of a generic online news-article card on a FULLY TRANSPARENT background, flat modern web-UI style. The white rounded card contains, top to bottom: a rectangular thumbnail image area showing a slightly TOO-perfect, uncanny AI-style photo of a crowded street parade with subtly wrong details (a warped face in the distance, an impossible building); a bold black headline reading "Crowds Gather For Parade That Was Never Scheduled"; one short grey subheading bar; a faint source row = a small grey circle avatar + a short grey bar (NO real logo, NO brand name); and a small timestamp "2h ago". Rounded corners, soft drop shadow. Do NOT include: any real news-outlet name or logo, any watermark, any readable real brand, any UI chrome outside the card, any border. High resolution, sharp, isolated element only.



### `fake-band-card.png` ✅

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

### `slop-machine.png` ✅

> Attach: none. A single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with a thick uniform black outline. A grotesque industrial CONTENT-GRINDER machine: a big funnel/hopper on top, a toothy grinder mouth in the middle, and a conveyor spout at the bottom extruding lumpy grey sausage-like "slop" into a small overflowing bin. Pipes, rivets, a couple of dials. Slightly cartoon-menacing but funny. Do NOT include: any background, any text/labels, any logo, any human. Sharp, high-res, isolated object only.



### `ai-influencer-perfect.png` ✅

> Attach: none. A single ISOLATED cutout on a FULLY TRANSPARENT background. A photorealistic but UNCANNY "AI influencer" head-and-shoulders portrait of a non-existent person: flawless plastic-smooth skin, too-symmetrical face, glossy studio lighting, a faint over-perfect sparkle. It should look impressive at a glance. Do NOT include: any background, any text, any watermark, any logo, any real or recognizable person. High-res, isolated subject only.



### `ai-influencer-melting.png` ✅

> Attach: none. A single ISOLATED cutout on a FULLY TRANSPARENT background. The SAME uncanny AI influencer as a "glitched" version: features melting and smearing, one eye drifting, datamosh/jpeg artifacts, and one hand raised showing SIX or SEVEN messy fingers. Horror-funny, clearly "AI gone wrong." Do NOT include: any background, any text, any watermark, any real person. High-res, isolated subject only.



### `gibberish-melting-sign.png` ✅

> Attach: none. A single ISOLATED cutout on a FULLY TRANSPARENT background. A glowing neon/shop SIGN whose letters are garbled, half-melted nonsense (fake words like "GRAND OPNEING", "DLISCOUNTS", "50%FRE"), letters dripping and warped, a few backwards. Looks AI-generated. Do NOT include: any background wall, any real brand, any watermark, any human. High-res, isolated sign only.



### `coca-coola-ad-fail.png` ✅

> Attach: none. A single ISOLATED cutout on a FULLY TRANSPARENT background, glossy holiday-ad style. A cheesy AI-generated festive soda advertisement: a GENERIC red soda can (no real brand), a slightly deformed jolly cartoon santa with a wrong-fingered mitten, and bold cursive misspelled text "Coca-Coola". Clearly a parody/AI fail. Do NOT include: the real Coca-Cola logo or any real trademark/brand, any real person, any background, any watermark. High-res, isolated ad graphic only.



### `cost-crush-pile.png` ✅

> Attach: none. A single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with thick black outline. A towering avalanche/heap tumbling downward, built from melting CLOCKS, staring disembodied EYEBALLS, and cracked HEARTS all jumbled together (representing "time, attention, trust"). It should look like it is crashing down to crush something below. Do NOT include: any background, any text, any logo, any human. High-res, isolated pile only.



### `slop-firehose.png` ✅

> Attach: none. A single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with thick black outline. A giant industrial FIRE HOSE / fat pipe nozzle blasting a powerful torrent/spray of lumpy grey sludge out to one side under high pressure. Dynamic motion. Do NOT include: any background, any text, any logo, any human. High-res, isolated object only.



### `slop-clone.png` ✅

> Attach: none. A single ISOLATED illustration on a FULLY TRANSPARENT background, flat 2D cartoon with thick black outline. ONE featureless grey blob "person": a generic grey humanoid silhouette-blob with a blank face and a single dead identical smile - the "identical fake person." Plain, mass-produced look. Do NOT include: any background, any text, any logo, any real person. High-res, single isolated figure only.



### `certified-slop-stamp.png` ✅

> Attach: none. A single ISOLATED illustration on a FULLY TRANSPARENT background. A big red rubber STAMP impression reading "CERTIFIED SLOP" in bold distressed uppercase inside a red double-ring border, slightly rotated, ink-textured. Do NOT include: any background, any extra text, any logo, any human. High-res, isolated stamp only.



### `robot-human-mask.png` **✅**

> Attach: none. A single ISOLATED cutout on a FULLY TRANSPARENT background. A creepy chrome animatronic ROBOT holding a flimsy, thin HUMAN face-MASK slightly away from its own mechanical face, mouth-hole wide open as if SCREAMING, leaning toward a vintage microphone. Unsettling but a little comedic. Do NOT include: any background, any text, any logo, any real identifiable person. High-res, isolated subject (robot + mask + mic) only.



## Sections 4-7

`not planned yet`.