# Section 1 Reference Board

## Reference Pass Status

- Status: `complete (real images sourced via Openverse; viewed before selection)`
- Browsed references: Openverse API queries (smartphone blank screen, workspace desk, devices flat lay, smart-home)
- Real images saved: 2 safe assets + 2 inspiration-only
- Generated images: none (no image generator connected this session)
- Inspected local assets: shared WIT pose library
- Prompt-only fallbacks: none
- Fallback reason: n/a

## Search / Browse Notes

- Openverse API works on this network (search engines bot-blocked); `size=large` filter returns 0 — omit it and filter width in `node`.
- Flickr `_k`(2048)/`_h`(1600) often 404 for these photos; `_b`(1024) is reliable. StockSnap CDN size paths beyond 960w returned HTML, not image.
- Standing preference applied: build the phone bank-app screen and the device screens in CSS (real-UI illustration) over a real photo base, rather than relying on a perfect stock screenshot.

## References

| Ref | Type | Source | Classification | Why useful | Attention / editor use | Use in production | Saved path |
|---|---|---|---|---|---|---|---|
| base-phone-blank-inhand.jpg | real photo | Flickr CC0 48124824108 | safe asset | blank phone screens, real hand, lifelike | hosts the CSS bank-app statement for BS1 | yes (BS1 base / phone texture) | assets/visual-references/section-01-hook/base-phone-blank-inhand.jpg |
| base-desk-devices.jpg | real photo | Flickr CC BY 6916063044 | safe asset | real lived-in desk + laptop, people/brand-free | base for BS2/BS3 device spread; float CSS screens | yes (BS2/BS3 base) | assets/visual-references/section-01-hook/base-desk-devices.jpg |
| insp-gear-flatlay.jpg | real photo | StockSnap CC0 Z5IW9QEFL6 | inspiration only | layout of phone+watch+laptop devices | composition reference for device spread | no (Apple ⌘ keys + Field Notes brand, sterile white) | assets/visual-references/section-01-hook/insp-gear-flatlay.jpg |
| insp-phone-instagram.jpg | real photo | Flickr CC0 48846003727 | inspiration only | real hand-holding-phone framing | framing ref for phone-in-hand | no (real Instagram UI/brand on screen) | assets/visual-references/section-01-hook/insp-phone-instagram.jpg |
| WIT pose library | local PNGs | .agents/_shared/assets/wit/poses | safe asset | suspicious / shocked / deadpan / trapped poses | emotional subject each big scene | yes | .agents/_shared/assets/wit/poses/ |

## Big Scene Reference Coverage

| Big Scene | Needed Visual Basis | Real / Local Reference | Generated Support | Production Decision | Remaining Gap |
|---|---|---|---|---|---|
| BS1 Phone bank-app | phone screen showing monthly charges | base-phone-blank-inhand.jpg | CSS-built bank statement UI | real phone base + CSS UI overlay | none (UI is CSS) |
| BS2 Screens that own you | desk with multiple devices flicking on | base-desk-devices.jpg | CSS device screens (laptop/TV/watch/car) + charge chips | real desk base + CSS screens | car-screen is CSS only (fine) |
| BS3 Payoff "you rent your whole life" | WIT as emotional subject over devices | base-desk-devices.jpg (darkened) + WIT trapped pose | CSS padlock/charge chips + payoff label | real desk base + giant WIT + CSS overlays | none |

## Image Generation Prompts

Not used — no generator connected. If one becomes available, a clean brand-free "single smartphone face-up on a dark wood desk, blank screen, top-down, soft light, no logos" would improve BS1; until then the CC0 blank-screen phone + CSS UI is the plan.

## Rejected References

- insp-gear-flatlay.jpg (Apple ⌘ keyboard + Field Notes branding; sterile objects-on-white)
- insp-phone-instagram.jpg (real Instagram app UI on screen = brand/content)
