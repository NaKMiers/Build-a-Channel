# Asset Manifest

Video: `4 Reasons You Can't Get Your First Job`
Scope: Section 1 only, scenes 1.1-1.6
Updated: 2026-07-20

Status legend: `done` means the exact file is present and has been checked on pixels. `reused`
means one existing file intentionally serves more than one scene.

## Section 1 Manifest

| Done | Filename | Type | Used in scenes | Description | Prompt / Source | Status |
|---|---|---|---|---|---|---|
| [x] | `graduation-diploma-desk-photo.png` | generate fallback | 1.1 | Photorealistic graduation cap and blank diploma on warm wood, with clean left space | Prompt G5 below | `done` |
| [x] | `wit-graduate-proud-diploma.png` | generate, NEW WIT pose | 1.1 | Proud graduate WIT with cap, stole, blank diploma, and blank resume | Prompt G1 below | `done` |
| [x] | `blank-laptop-job-search-desk-photo.png` | browse-real-photo | 1.2 | Bright desk with open laptop on the left and no people, logo, or account data | See `ATTRIBUTION.md` | `done` |
| [x] | `generic-job-listing-card-blank.png` | generate | 1.2, 1.3, 1.4 | Text-free fictional job-listing card with blank UI regions | Prompt G2 below | `done`, reused |
| [x] | `job-board-cork-closeup-photo.png` | browse-real-photo | 1.3 | Warm cork-board texture with no readable notes, people, or brands | See `ATTRIBUTION.md` | `done` |
| [x] | `poses/shocked_panicked_at_laptop.png` | pose | 1.3 | Exact WIT library pose, shocked at laptop | Shared WIT pose library | `done` |
| [x] | `empty-office-reception-floor-photo.png` | browse-real-photo | 1.4 | Bright reception crop with desk, reflective floor, and no visible people or signage | See `ATTRIBUTION.md` | `done` |
| [x] | `experience-receipt-blank.png` | generate | 1.4, planned later reuse | Text-free cream receipt with faint rules and one empty checkbox | Prompt G3 below | `done` |
| [x] | `empty-concrete-stairwell-photo.png` | browse-real-photo | 1.5 | Empty painted stairwell with strong repeated climbing lines | See `ATTRIBUTION.md` | `done` |
| [x] | `career-ladder-rung-blank.png` | generate | 1.5, 1.6, planned later reuse | Single warm-yellow modular rung with dark end caps | Prompt G4 below | `done`, reused |
| [x] | `poses/deadpan_unimpressed_half_lidded.png` | pose | 1.5 | Exact WIT library deadpan pose | Shared WIT pose library | `done` |
| [x] | `bright-office-doorway-photo.png` | browse-real-photo | 1.6 | Empty bright office corridor with a clear doorway route target | See `ATTRIBUTION.md` | `done` |
| [x] | `poses/presenting_open_palm_talking.png` | pose | 1.6 | Exact WIT library presenter pose | Shared WIT pose library | `done` |

Render gate: all 13 unique Section 1 assets are present under their exact planned filenames.

## Implementation Notes

- `graduation-diploma-desk-photo.png` is a generated photorealistic fallback. No public image
  found during sourcing met all constraints at once: cap, blank diploma, no person, no private
  text, no school branding, landscape framing, and a clean left overlay zone.
- `blank-laptop-job-search-desk-photo.png` contains a non-branded miniature motorbike on the
  right side. Keep `GOOD.` in the upper-right light area and cover the laptop screen with the
  generated listing card.
- `empty-office-reception-floor-photo.png` is cropped from the source to remove both hotel staff.
  It has a reflective floor and curved reception counter, but not the originally imagined circular
  floor inlay. Build the document loop with CSS/SVG in the open central region.
- `empty-concrete-stairwell-photo.png` is a clean painted interior rather than exposed raw concrete.
- `bright-office-doorway-photo.png` uses an empty office corridor and doorway as the route target;
  renderer lighting may warm the target slightly without altering the source file.

## Generation Prompts

### G1 - `wit-graduate-proud-diploma.png`

Attach: `.agents/_shared/assets/wit/poses/_origin_.png`

```text
Use the attached mascot as the exact identity reference: the same round bald white head,
thick uniform black outline, large rectangular black glasses, dot eyes, expressive eyebrows,
compact white body, proportions, and line weight. Draw the same WIT character as a proud new
graduate. Add a plain dark-teal mortarboard and a short matching stole with no crest, words,
logo, or decoration. One raised hand holds a blank rolled cream diploma. The other hand holds
one blank white resume page with no text or symbols. Give WIT bright relieved eyes, raised
eyebrows, and a cheerful open smile. Full body, centered, generous margin, no ground shadow.
The head, body, arms, hands, and legs must remain solid opaque bright white inside the black
outline. Output one isolated character on a fully transparent background. No scenery, caption,
letters, numbers, watermark, extra objects, or second character.
```

### G2 - `generic-job-listing-card-blank.png`

Attach: none

```text
Create one isolated fictional job-listing card on a fully transparent background. Use an
original cream and charcoal interface frame with softly rounded corners, a thin charcoal border,
one blank teal pill near the top, one wide blank title bar, and four short abstract horizontal
rules below. Every region must be text-free so HyperFrames can add CSS wording later. Keep the
design generic and clearly unrelated to any real hiring platform. Front-facing, crisp edges,
subtle paper/UI depth, centered, generous transparent margin. Do not include words, letters,
numbers, company names, logos, avatars, icons copied from a platform, buttons with text,
watermarks, hands, devices, scenery, or a cast background.
```

### G3 - `experience-receipt-blank.png`

Attach: none

```text
Create one isolated vertical cream paper receipt on a fully transparent background. Give it a
slightly torn top and bottom edge, gentle paper texture, five faint horizontal rule marks, and
one empty square checkbox. Leave all wording areas blank for CSS text. Keep the receipt mostly
flat and readable with only a soft natural bend and subtle internal shading. Center the entire
object with generous transparent margin. Do not include readable text, letters, numbers, prices,
logos, barcodes, QR codes, stamps, handwriting, hands, desk, scenery, or external cast shadow.
```

### G4 - `career-ladder-rung-blank.png`

Attach: none

```text
Create one isolated horizontal ladder rung on a fully transparent background. It is a simple
warm-yellow painted wooden rung with a softly worn surface and small dark-charcoal metal end caps.
Show the rung straight-on with modest realistic depth, clean silhouette, and no rails attached.
The object must be modular so identical copies can form a straight ladder or a circular ladder.
Center it with generous transparent margin. Do not include words, labels, numbers, logos,
symbols, screws forming a face, hands, character, ladder rails, wall, floor, scenery, or watermark.
```

### G5 - `graduation-diploma-desk-photo.png` (browse fallback)

Attach: none

```text
Create a photorealistic 16:9 editorial still-life photograph for a video background asset. A
plain dark-teal graduation mortarboard and a blank rolled cream diploma tied with a simple teal
ribbon rest on a bright, lightly worn honey-colored wooden desk. No people, no hands, no school
crest, no logos, no brand marks, no readable text, no letters, no numbers, no watermark. Place
the cap and diploma center-right. Preserve a clean, softly lit open area on the left for a
character overlay. Natural morning window light, believable shadows, lived-in but uncluttered
surface, documentary stock-photography realism, high detail, neutral color grade. This is only a
background/source photograph, not a finished scene: do not add captions, UI, characters,
stickers, borders, or graphic overlays.
```

