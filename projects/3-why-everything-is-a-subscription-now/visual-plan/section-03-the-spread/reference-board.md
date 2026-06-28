# Section 3 Reference Board (2026-06-23)

Visual reference pass for Section 3. All real bases sourced via the Openverse API + WordPress Photo
Directory and VIEWED on the pixels before selection. One fresh vivid object base per scene; brand/people-free
(the car has a small head-unit logo, covered in render).

## Reference Pass Status

- Status: `complete (real images via Openverse / rawpixel / StockSnap; viewed before selection)`
- Real bases saved: 5 (1 is a covered mockup target)
- Generated images: none (no generator connected)
- Prompt-only fallbacks: none

## Big-scene bases

| Scene | Base | What it shows | Why it fits | Source / license |
|---|---|---|---|---|
| BS1 software | base-desk.jpg | a laptop on a light-wood desk, empty right | "the program you used to buy in a box became a monthly plan" - software | CC0, StockSnap (Openverse) "Top Workspace" (no visible logo) |
| BS2 streaming | base-tv-room.jpg | a real living room with a flat TV | "your screens joined the party… rent a giant library" | CC0, rawpixel (Openverse) "Living room modern" |
| BS3 five subs | base-cash.jpg | a spread of euro banknotes | "five subscriptions… bigger than the old cable bill" - money | CC0, rawpixel (Openverse) euro banknotes |
| BS4 dungeon | base-jail.jpg | a jail corridor of cells | "we escaped one dungeon and built five smaller ones" | CC0, rawpixel (Openverse) jail cells |
| BS5 car | base-car.jpg | a modern car interior (seat + console) | "carmakers put heated seats behind a monthly fee" | CC0, rawpixel (Openverse) modern car interior - `mockup target`: small "Blaupunkt" head-unit logo covered by the CSS seat panel + giant WIT |

## Inspected and rejected

- StockSnap "Laptop Computer" / "Developer Code" / iMac "Seo Computer" - Apple logos (+ a person). reject.
- 2020 MG ZS interior - MG steering-wheel logo + showroom people. reject.
- Original modern-car-interior with a prominent "BLAUPUNKT" head unit - used only as the BS5 base with the logo covered; classified `mockup target`.
- Sterile cash-fan-on-white ($20s) - objects-on-white; used the textured euro spread instead.
- Wikimedia antique/vintage car interiors + medieval junk - dingy/off-tone. reject.

## CSS idea-devices (built on the bases)

software window (greys + padlock + ransom), streaming-tile wall (vanishes) + POV card, 5 subscription tiles,
"5 subs > CABLE" comparison + dungeon labels, heated-seat button + padlock + "$/mo", EXPIRED system banner
(running-gag callback). Real-UI per the owner's standing preference.

## WIT poses used (shared manifest)

hidden-fee-panic (software), shocked (vanish), trapped-by-app-screen (dungeon), deadpan-side-eye (warm-bottom gag).
All verified transparent. AVOIDED: `typing-on-laptop` and `money-panic` - both have a baked BLACK background.
