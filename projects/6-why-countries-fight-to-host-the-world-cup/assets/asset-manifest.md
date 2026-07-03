# Asset Manifest

Video: `Why Countries Fight to Host the World Cup (and Lose Billions)`
Scope: Section 1 (Hook) - from `visual-plan/section-01-hook/section-01-hook-visual-plan.md`
Updated: 2026-07-02 (visual-implement, Section 1 run)

Status legend: `done` (file present) / `prompt-ready / awaiting generation` (owner pastes the
prompt into ChatGPT, attaches the named reference, drops the PNG into `assets/` under the exact
filename) / `reused` (already existed).

## Manifest

| Filename | Type | Used in scenes | Description | Prompt / Source | Status |
|---|---|---|---|---|---|
| `trophy-gold-parody.png` | generate | 1.1, 1.2, 1.3, 1.5, 1.6 (+ later sections) | VIDEO HERO: parody golden trophy (gold globe on fluted cup, dark plinth), isolated, transparent | Prompt G1 below | `prompt-ready / awaiting generation` |
| `receipt-endless-roll.png` | generate | 1.3, 1.6, 1.7 (+ later sections) | VIDEO MOTIF: long white receipt strip, faint unreadable print, one curl, transparent | Prompt G2 below | `prompt-ready / awaiting generation` |
| `wit-fan-flag-cheer.png` | generate (NEW pose) | 1.1 | WIT as euphoric fan: teal scarf + small plain teal pennant, huge cheer | Prompt G3 below (attach `_origin_.png`) | `prompt-ready / awaiting generation` |
| `wit-fan-frozen-mid-cheer.png` | generate (NEW pose) | 1.3 | same fan kit + pose, face flipped to blank dread + sweat drop | Prompt G4 below (attach `_origin_.png` + finished `wit-fan-flag-cheer.png`) | `prompt-ready / awaiting generation` |
| `poses/skeptical_side_eye_doubtful.png` | pose | 1.2 | library pose copy | `.agents/_shared/assets/wit/poses/` | `done` |
| `poses/pondering_skeptical_hand_on_chin.png` | pose | 1.4 | library pose copy | same | `done` |
| `poses/deadpan_unimpressed_half_lidded.png` | pose | 1.5 | library pose copy | same | `done` |
| `poses/hand_on_cheek_surprised_curious.png` | pose | 1.6 | library pose copy | same | `done` |
| `poses/pointing_up_curious_open_mouth.png` | pose | 1.7 | library pose copy | same | `done` |
| `poses/_origin_.png` | pose (reference) | generation handoff only | canonical neutral identity - attach when generating G3/G4 | same | `done` |
| `stadium-fireworks-1.jpg` | browse-real-photo | 1.1 | giant multicolor festival firework over a glittering night town (celebration-night base; trophy+confetti+WINNER carry the "won the Cup" meaning) | see ATTRIBUTION.md (CC BY 4.0) | `done` |
| `podium-spotlight-1.jpg` | browse-real-photo | 1.2 | single spotlight beam cutting through darkness; trophy sits at the beam's landing | see ATTRIBUTION.md (CC BY 2.0) | `done` |
| `world-map-vintage-1.jpg` | browse-real-photo | 1.3 | 1550s parchment mappemonde (Jomard/Henri II); vertical fold seam near center - crop right-of-seam or hide seam behind the trophy podium | see ATTRIBUTION.md (PD) | `done` |
| `ledger-red-pen-1.jpg` | browse-real-photo | 1.4 | blank aged ledger page, red center rule, alphabet index tabs (no pen/figures in photo - the handwritten verdict + CSS red marks carry the scene; filename kept per plan) | see ATTRIBUTION.md (PD) | `done` |
| `desk-darkwood-1.jpg` | browse-real-photo | 1.5 | dark wood planks with moody spotlight vignette (960w preview - swap if soft at 1920) | see ATTRIBUTION.md (CC0) | `done` |
| `gold-bokeh-black-1.jpg` | browse-real-photo | 1.6 | warm gold string-light bokeh on dark, luxury feel (960w - bokeh upscales safely) | see ATTRIBUTION.md (CC0) | `done` |
| `curtain-dark-1.jpg` | browse-real-photo | 1.7 | dark red stage curtain, moody; grade darker + heavy vignette at render for the near-black focus beat | see ATTRIBUTION.md (CC0) | `done` |

Render gate: Section 1 render is BLOCKED until the four `generate` PNGs are dropped into
`assets/` under their exact filenames.

## Generation Prompts

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
