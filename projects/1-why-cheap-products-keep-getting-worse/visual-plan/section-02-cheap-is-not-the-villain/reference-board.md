# Section 2 Reference Board

## Reference Pass Status

- Status: `completed - revised real-world plus generated support pass`
- Browsed references: `Pexels source pages, existing local real images from the first Section 2 pass`
- Real images saved: `4 section-specific real-world images plus 1 real-world contact sheet`
- Generated images: `2 generated support bases plus 1 improved mixed contact sheet`
- Inspected local assets: `current project WIT pose manifest; existing Section 2 render output and asset usage`
- Prompt-only fallbacks: `0`
- Fallback reason: `project-local gstack browse previously failed to start within 15s and global gstack browse was not installed, so source-page web search and direct source downloads were used for real references. Built-in image generation was available and used for the two visual gaps.`

## Critical Self-Check

- Previous weakness: `real images alone were not enough for Section 2 because the fair comparison and missing-tomorrow cutaway were left as render inventions.`
- End-viewer risk: `the viewer might understand the words but not remember the reframe if the final product cutaway looks like a generic diagram.`
- Improvement: `keep real tags, receipts, boxes, and jacket photos for familiar texture; use generated support bases for the exact two scenes that need controlled, render-ready composition.`
- Render consequence: `render should no longer invent the two-box layout, product cutaway angle, empty compartment shape, or label-safe areas.`
- Production rule for this section: `generated images are support bases, not the whole reference layer; all labels, arrows, prices, slot names, and jokes must still be added in HyperFrames.`

## Search / Browse Notes

- Project-local browse command attempted in prior Section 2 run: `.agents/skills/browse/dist/browse.exe status`
- Result: `Server failed to start within 15s`
- Global fallback check in prior run: `$env:USERPROFILE\.Codex\skills\gstack\browse\dist\browse.exe` and lowercase `.codex` equivalent
- Result: `global browse not installed`
- Real-reference direction: use ordinary tags, product boxes, receipt paper, and a jacket silhouette so the section still feels like shopping life, not a generated-only diagram.
- Generated-support direction: use generated images only for the clean two-box comparison base and the missing-tomorrow cutaway base, because these were the exact places where render previously had to invent too much.

## References

| Ref | Type | Source | Classification | Why useful | Attention / editor use | Use in production | Saved path |
|---|---|---|---|---|---|---|---|
| Improved Section 2 contact sheet | Mixed real/generated contact sheet | Created locally from saved real and generated references | `safe asset / internal reference` | Shows the complete visual system: real texture plus two controlled generated support bases. | Use as the main planning audit before rerendering Section 2. | Internal reference only. | `assets/visual-references/section-02-cheap-is-not-the-villain/section-02-improved-reference-contact-sheet.png` |
| Real-world reference contact sheet | Real web-image contact sheet | Created locally from downloaded real photos | `safe asset / internal reference` | Preserves the real texture baseline from the first reference pass. | Use to keep the generated support bases from feeling sterile. | Internal reference only. | `assets/visual-references/section-02-cheap-is-not-the-villain/real-world/section-02-real-world-reference-contact-sheet.png` |
| Blank paper tag | Real internet photo | Pexels, Miguel A. Padrinan, `White Tag With String and Black Background`, https://www.pexels.com/photo/white-tag-with-string-and-black-background-1111320/ | `safe asset` | Clean tag texture for the opening correction board and small side tag. | Keeps `CHEAP != BAD` feeling like a physical shopping correction. | Direct crop candidate; add all text in HyperFrames. | `assets/visual-references/section-02-cheap-is-not-the-villain/real-world/real-blank-tag-pexels-padrinan.jpg` |
| Real receipt texture | Real internet photo | Pexels, Towfiqu barbhuiya, `Close-up of a Receipt`, https://www.pexels.com/photo/close-up-of-a-receipt-14647295/ | `mockup target` | Gives the `emotionally expensive` joke real paper/cost texture. | Use only as texture guidance or cropped/covered mockup. | Do not expose source numbers; add fake receipt text in HyperFrames. | `assets/visual-references/section-02-cheap-is-not-the-villain/real-world/real-receipt-pexels-towfiqu-barbhuiya.jpg` |
| Real stacked boxes | Real internet photo | Pexels, Dalila Dalprat, `Stacked White Cardboard Boxes`, https://www.pexels.com/photo/stacked-white-cardboard-boxes-10938208/ | `safe asset / mockup target` | Good real cardboard/product-box texture, but vertical and less useful as the final scene base. | Use for texture, lighting, and box material realism. | Secondary reference; generated two-box image is better as the render base. | `assets/visual-references/section-02-cheap-is-not-the-villain/real-world/real-plain-white-boxes-pexels-dalprat.jpg` |
| Black jacket on hanger | Real internet photo | Pexels, Konstantin Mishchenko, `Person Holding Black Jacket With Hanger`, https://www.pexels.com/photo/person-holding-black-jacket-with-hanger-14990381/ | `mockup target` | Provides jacket silhouette and fabric logic for the joke. | Use to build a simple jacket overlay, not as a direct pasted photo. | Do not use directly because the source includes a hand and collar label. | `assets/visual-references/section-02-cheap-is-not-the-villain/real-world/real-black-jacket-hanger-pexels-mishchenko.jpg` |
| Generated two-box comparison base | Generated support image | Built-in `image_gen`, saved locally | `safe generated support base` | Gives render a clean horizontal two-box layout with label-safe negative space. | Use as the preferred base for Big Scene 2 because it is exactly framed for the section. | Direct production candidate if render uses it with HyperFrames labels and WIT overlay. | `assets/visual-references/section-02-cheap-is-not-the-villain/generated/fair-comparison-two-boxes-generated.png` |
| Generated missing-tomorrow cutaway base | Generated support image | Built-in `image_gen`, saved locally | `safe generated support base` | Gives render a specific product-shell cutaway with four empty compartments. | Use as the preferred base for Big Scene 3; this solves the biggest prior ambiguity. | Direct production candidate if render adds labels, slot dimming, marks, and WIT in HyperFrames. | `assets/visual-references/section-02-cheap-is-not-the-villain/generated/missing-tomorrow-cutaway-generated.png` |
| Current WIT pose set | Local reusable channel asset | `projects/1-why-cheap-products-keep-getting-worse/assets/wit/manifest.json` | `safe asset` | WIT carries fairness, suspicion, deadpan jacket judgment, and repeat-buyer fatigue. | WIT should be large and emotionally readable, not decorative. | Use exact listed PNGs only. | `assets/wit/` |

## Big Scene Reference Coverage

| Big Scene | Needed Visual Basis | Real / Local Reference | Generated Support | Production Decision | Remaining Gap |
|---|---|---|---|---|---|
| 1. Cheap is accused, then corrected | Physical tag plus receipt/cost texture. | Real blank tag, real receipt texture. | Not needed. | Use real tag crop and self-made receipt overlay; opening should feel real, not generated. | None. |
| 2. Fair comparison and jacket joke | Two generic products in a clean horizontal comparison layout. | Real box texture, jacket silhouette reference. | `fair-comparison-two-boxes-generated.png` | Use generated two-box base as the scene base; add generic jacket overlay and all labels in HyperFrames. | None, but jacket must be rebuilt or simplified, not pasted from source photo. |
| 3. Missing tomorrow cutaway | Normal product with four clear internal future slots. | Real box texture for material realism. | `missing-tomorrow-cutaway-generated.png` | Use generated cutaway base as the scene base; slots dim one by one with HyperFrames labels/marks. | None; render must avoid turning this into a flat diagram. |

## Image Generation Prompts

### Prompt 1 - Generated Two-Box Comparison Base

```text
Use case: product-mockup
Asset type: Why It Works section visual reference, 16:9 video frame
Primary request: Create a clean photorealistic reference image showing two plain generic product boxes on a warm desk for a fair comparison scene. The left box should look modest and affordable; the right box should be similar but slightly larger and suitable for a later jacket overlay. No readable text, no labels, no logos, no brand marks, no people, no hands, no watermark.
Scene/backdrop: warm neutral tabletop with simple paper/cardboard texture, soft natural light, subtle real-world shadows.
Subject: two blank generic product boxes, not specific to any brand or category.
Composition/framing: landscape 16:9, boxes centered with enough empty space above and below for later handwritten labels and WIT character overlays; left box on the left third, right box on the center-right.
Style/medium: polished real-world editorial product-photo reference, realistic but simple.
Lighting/mood: warm, clear, slightly humorous but not cartoonish.
Constraints: no text or symbols baked into the image; keep the background uncluttered; leave label-safe negative space; avoid luxury branding cues.
```

Negative prompt:

```text
brand logos, readable text, store names, real product names, people, hands, watermark, copied creator frame, luxury brand design, cluttered background
```

Saved output:

```text
assets/visual-references/section-02-cheap-is-not-the-villain/generated/fair-comparison-two-boxes-generated.png
```

### Prompt 2 - Generated Missing-Tomorrow Cutaway Base

```text
Use case: product-mockup
Asset type: Why It Works section visual reference, 16:9 video frame
Primary request: Create a clean photorealistic reference image of one plain generic product box or small appliance shell opened like a simple cutaway, showing four blank internal compartments. The outside should look normal and ordinary, while the inside feels slightly empty, as if future parts are missing. No readable text, no labels, no logos, no brand marks, no people, no hands, no watermark.
Scene/backdrop: warm neutral desk or tabletop, simple cardboard/plastic material, soft natural light, real-world shadows.
Subject: generic normal product shell with one side opened, four clear empty compartments inside.
Composition/framing: landscape 16:9, product centered-left, enough empty space above and right for handwritten labels, red callouts, and a WIT character overlay.
Style/medium: polished realistic editorial product reference, clean and controlled, not sci-fi, not technical blueprint.
Lighting/mood: warm, suspicious, mildly funny but still realistic.
Constraints: no text anywhere in the image; no logos; no brand cues; no complex electronics; keep compartments readable as simple empty future slots; no x-ray effect; no clutter.
```

Negative prompt:

```text
readable text, logos, real product details, brand marks, complex electronics, sci-fi x-ray, clutter, people, hands, watermarks
```

Saved output:

```text
assets/visual-references/section-02-cheap-is-not-the-villain/generated/missing-tomorrow-cutaway-generated.png
```

## Rejected References

- Real store/product screenshots remain rejected because they add brand accusation and copyright risk.
- Real luxury packaging references remain rejected because the section should not imply expensive always means deceptive.
- Direct use of the jacket photo is rejected for production because the source has a visible hand and collar label; use it only for silhouette/fabric reference.
- The previous plan's prompt-only optional support assets are now superseded because the two needed support bases were actually generated and saved.
- A generated-only plan is rejected: the section still needs real tag, receipt, box, and jacket references so it feels close to ordinary shopping.
