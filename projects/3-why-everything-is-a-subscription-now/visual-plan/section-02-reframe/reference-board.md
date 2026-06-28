# Section 2 Reference Board (REMADE 2026-06-23)

Visual reference pass for the Section 2 remake. All real images sourced via the Openverse API and
VIEWED on the pixels before selection (Google/Bing/Pexels are bot-blocked on this network; no image
generator is connected). One fresh vivid object base per scene, brand-free and people-free.

## Reference Pass Status

- Status: `complete (real images via Openverse + WordPress Photo Directory; viewed before selection)`
- Real images saved: 5 safe-asset bases (1 is a copy of the phone for the BS3 callback) + 2 inspiration-only
- Generated images: none (no generator connected)
- Prompt-only fallbacks: none

## Big-scene bases (safe assets)

| Scene | Base | What it shows | Why it describes the voice | Source / license |
|---|---|---|---|---|
| BS1 defuse | base-apps-phone.jpg | hands tapping a phone full of glowing app icons | "your phone full of subscriptions; some are useful" - the apps ARE the subject (review fix; the aurora night-phone read as a travel photo) | CC0 1.0, rawpixel (Openverse) "Social media applications mobile screen" |
| BS2 OWN | base-vinyl.jpg | warm crates of vinyl records in a shop | "we used to own things" - physical media you bought once and kept | CC0 1.0, StockSnap (Openverse) DPMX3QCLBT "Vinyl Music" |
| BS3 RENT | base-phone-rent.jpg | the glowing phone again (cool grade + CSS paywall) | "a subscription is different - you rent access" - the same device, now rented | CC0 1.0 (copy of base-night-phone) |
| BS4 LOCK | base-padlock.jpg | a steel padlock + chain on a green metal gate | "miss a payment… a little padlock appears" - the lock, literally | CC0 1.0, WordPress Photo Directory "Metal Door With Security Lock" |
| BS5 question | base-devices-flatlay.jpg | laptop, phone, tablet on wood, blank screens, empty right | "your apps, your shows, your software…" - every device; empty area for tags + WIT | CC0 1.0, StockSnap (Openverse) PJN9GAS0FE "Workspace Office" |

## Composition / idea-device references (build-from)

- Section 1 approved build (`section-previews/section-01-hook/index.html`) - the standing template +
  reusable CSS kit (app tiles, system banner, padlock `.lockicon`, payoff). `inspiration only` for layout; copy/adapt the CSS.
- Real-UI illustration (owner standing preference) - the subscription paywall card, the receipt card,
  the lock-screen card, and the green app tiles are CSS real-UI built on top of the photo bases.

## Big Scene Reference Coverage

| Big Scene | Needed Visual Basis | Real Reference | CSS Support | Decision |
|---|---|---|---|---|
| BS1 defuse | phone, "calm down" | base-night-phone (normal) | struck RANT banner, app tiles + ✓ | real base + CSS |
| BS2 OWN | physical owned things | base-vinyl (warm) | green OWN stamp, receipt card | real base + CSS + WIT |
| BS3 RENT | same device, subscription | base-phone-rent (cool) | paywall card, OWN→RENT swap, toggle | real base + CSS |
| BS4 LOCK | the device locks | base-padlock (dark) | MISS A PAYMENT banner, lock-screen card | real base + CSS + giant WIT |
| BS5 question | everything you own | base-devices-flatlay | kinetic headline, RENT tags, payoff | real base + CSS + WIT |

## Inspected and rejected

- cand-laptop / cand-code (StockSnap "Laptop Computer" / "Developer Code") - `reject`: visible Apple logo + a blurred person (no-face channel).
- "three combination padlocks" (pd.w.org) - `reject`: Master Lock branding on the body.
- cand-vinyl-rawpixel (small vinyl stack on white) - `reject`: sterile objects-on-white.
- antique/medieval padlocks (Wikimedia) - `reject`: dingy, antique; off-tone for a modern subscription video.
- insp-vinyl-albums.jpg, insp-car-proton.jpg - kept `inspiration only` (album-cover copyright / Proton logo + distant people); not used directly.

## WIT poses used (shared manifest)

facepalm (defuse), thinking (own), betrayed (lock peak), suspicious (question) - full-body transparent
PNGs; placed giant + high, varied side/scale per scene. `money-panic` avoided (baked black background).
