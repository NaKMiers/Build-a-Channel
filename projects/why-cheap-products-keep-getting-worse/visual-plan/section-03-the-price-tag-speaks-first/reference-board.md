# Section 3 Reference Board

## Reference Pass Status

- Status: `completed - existing sourced real references plus generated support bases; Scene 3 direct use revised after review`
- Browsed references: `0 fresh browsed pages; used previously sourced local Pexels references already saved in the project`
- Real images saved: `3 sourced real-world references copied into this section folder`
- Generated images: `2 generated support bases plus 1 mixed contact sheet`
- Inspected local assets: `project WIT pose manifest; Section 2 real-world references; generated Section 3 images`
- Prompt-only fallbacks: `0`
- Fallback reason: `not applicable; generated images were materialized and saved. Fresh browsing was not necessary because the project already had sourced, inspected, ordinary shopping-object references for tags, receipts, and boxes.`

## End-State Self-Check

- Final viewer memory target: `the visible price talks loudly while future cost hides behind it`
- Best paused frame: `a big yellow price tag on a plain box, with smaller hidden future tags around the edges and WIT noticing the trap`
- Real-reference limit: `the real tag, receipt, and box photos provide material texture but do not create the exact hidden-future composition`
- Generated-support fix: `use generated support bases for the two build-critical scenes: hidden future tags and visible shopping promises`
- Render consequence: `render should keep the tag stack and final hidden-tag reveal, but Scene 3 should use a distinct checkout promise arena instead of another tabletop/tag photo`
- Text rule: `all prices, future-cost labels, sale jokes, and red marks must be added in HyperFrames, not baked into the images`

## Search / Browse Notes

- Existing real-reference sources were copied from the Section 2 real-world reference set because they are already saved, inspected, and source-noted in this project.
- The real blank tag supports the opening price-tag texture and dark negative space.
- The real receipt texture supports the wallet/future-cost consequence without using real receipt numbers directly.
- The real plain boxes support cardboard/material realism for generated and HyperFrames-built product scenes.
- Generated support was used only after the real-reference pass identified the actual missing production bases.

## References

| Ref | Type | Source | Classification | Why useful | Attention / editor use | Use in production | Saved path |
|---|---|---|---|---|---|---|---|
| Section 3 contact sheet | Mixed local/generated contact sheet | Created locally from Section 3 references | `safe asset / internal reference` | Shows the visual mix for the whole section: real tag, receipt, boxes, hidden future tag base, and visible promise base. | Use as the visual audit before render. | Internal reference only. | `assets/visual-references/section-03-the-price-tag-speaks-first/section-03-reference-contact-sheet.png` |
| Real blank tag | Real internet photo | Pexels, Miguel A. Padrinan, `White Tag With String and Black Background`, https://www.pexels.com/photo/white-tag-with-string-and-black-background-1111320/ | `safe asset` | Gives physical price-tag paper, string, and dark negative space. | Keeps the opening close to real shopping life. | Direct crop candidate or texture reference; add all text in HyperFrames. | `assets/visual-references/section-03-the-price-tag-speaks-first/real-world/real-blank-tag-pexels-padrinan.jpg` |
| Real receipt texture | Real internet photo | Pexels, Towfiqu barbhuiya, `Close-up of a Receipt`, https://www.pexels.com/photo/close-up-of-a-receipt-14647295/ | `mockup target` | Gives paper/cost texture for `wallet` and `future cost` beats. | Use as texture guidance for fake receipt or future-cost slip. | Do not expose source numbers; rebuild receipt text in HyperFrames. | `assets/visual-references/section-03-the-price-tag-speaks-first/real-world/real-receipt-pexels-towfiqu-barbhuiya.jpg` |
| Real plain boxes | Real internet photo | Pexels, Dalila Dalprat, `Stacked White Cardboard Boxes`, https://www.pexels.com/photo/stacked-white-cardboard-boxes-10938208/ | `safe texture reference` | Provides generic product-box material and lighting. | Keeps generated product boxes from feeling too sterile. | Texture/reference only unless render needs a secondary box crop. | `assets/visual-references/section-03-the-price-tag-speaks-first/real-world/real-plain-white-boxes-pexels-dalprat.jpg` |
| Generated hidden future tags | Generated support image | Built-in image generation, saved locally | `safe generated support base` | Gives the exact end-state frame: big visible price tag hiding smaller tags behind it. | Use as the preferred base for Big Scenes 1, 2, and 4. | Direct production candidate with all text, WIT, and red marks added in HyperFrames. | `assets/visual-references/section-03-the-price-tag-speaks-first/generated/price-tag-hiding-future-tags-generated.png` |
| Generated visible shopping promises | Generated support image | Built-in image generation, saved locally | `safe generated support reference` | Gives a clean box with several blank tag/badge shapes for the visible competition list, but it is visually too close to the opening tabletop/tag setup. | Use only as a checked reference/fallback after the Scene 3 render review. | Not direct production in the revised Scene 3; the final scene is CSS-built in HyperFrames. | `assets/visual-references/section-03-the-price-tag-speaks-first/generated/visible-shopping-promises-generated.png` |
| Current WIT pose set | Local reusable channel asset | `projects/why-cheap-products-keep-getting-worse/assets/wit/manifest.json` | `safe asset` | WIT shows temptation, fast wallet approval, confusion, deadpan marketing judgment, and final defeat. | WIT should stay large and emotionally readable. | Use exact listed PNG pose files only. | `assets/wit/` |

## Big Scene Reference Coverage

| Big Scene | Needed Visual Basis | Real / Local Reference | Generated Support | Production Decision | Remaining Gap |
|---|---|---|---|---|---|
| 1. Price speaks first | One dominant price tag attached to a normal product, with room for WIT and wallet labels. | Real blank tag, real plain box texture. | `price-tag-hiding-future-tags-generated.png` | Use generated hidden-tag base as the preferred scene base; real tag remains the texture/reference fallback. | None. |
| 2. Future cost is quiet | Same product, but small future tags become noticeable behind the loud price. | Real receipt texture for future-cost slip. | `price-tag-hiding-future-tags-generated.png` | Keep the same base and reveal labels on hidden tags in HyperFrames. | None. |
| 3. Visible things compete | Plain product surrounded by multiple visible shopping promises. | Real tag/box references. | `visible-shopping-promises-generated.png` inspected as fallback only. | Build a CSS checkout promise arena because the generated visible-promises base looked too similar to Scene 1. | Keep it generic; do not add real logos, store UI, or app screenshots. |
| 4. Tomorrow becomes negotiable | Return to the hidden-tag base and expose the small future tags as the thing that gets negotiated. | Real receipt texture and box texture. | `price-tag-hiding-future-tags-generated.png` | Use the same base as a memory callback; reveal hidden tags and final `TOMORROW` label. | None. |

## Image Generation Prompts

### Prompt 1 - Generated Hidden Future Tags

```text
Use case: Why It Works section visual reference for a 16:9 no-face explainer video.
Create a clean realistic editorial product-photo style image: one plain generic product box on a warm neutral desk, with one large blank bright yellow price tag hanging in front of the box and several smaller blank muted paper tags partly hidden behind it like layered evidence. The large front tag should dominate the composition and cover most of the smaller tags. The smaller tags should be visible enough around the edges to show there is hidden information behind the main price. No readable text, no numbers, no logos, no brand marks, no people, no hands, no watermark.
Composition: landscape 16:9, product and large tag centered-left, empty dark/warm negative space on the right for a WIT character and handwritten labels. The small hidden tags should sit behind and around the big tag, not scattered randomly. Realistic paper/cardboard texture, soft natural light, subtle shadows, simple uncluttered background.
Mood: ordinary shopping object becoming suspicious; clear, simple, slightly funny, not luxury, not sci-fi.
```

Negative prompt:

```text
readable text, numbers, currency symbols, logos, store names, brand marks, hands, people, watermarks, clutter, complex product details, exact real product packaging, creator-style imitation
```

Saved output, now reference-only after render review:

```text
assets/visual-references/section-03-the-price-tag-speaks-first/generated/price-tag-hiding-future-tags-generated.png
```

### Prompt 2 - Generated Visible Shopping Promises

```text
Use case: Why It Works section visual reference for a 16:9 no-face explainer video.
Create a clean realistic editorial product-photo style image: a plain generic product box on a warm desk surrounded by several blank attention tags and simple blank delivery/feature/sale-style stickers, all with no text. One large blank price tag should be most visible, while three or four smaller blank tags/badges around it suggest visible shopping promises such as fast delivery, new color, extra feature, and sale sticker, but without any words, numbers, logos, icons, or brand marks. Leave generous empty space for HyperFrames handwritten labels.
Composition: landscape 16:9, product box centered, tags arranged in a tidy semicircle around it, enough negative space at lower right for a WIT character. Warm paper/cardboard texture, soft natural light, simple uncluttered background, realistic shadows.
Mood: visible things competing for attention at checkout, ordinary and slightly absurd; not a store screenshot, not an app UI.
```

Negative prompt:

```text
readable text, numbers, currency symbols, logos, brand marks, store names, real product packaging, people, hands, watermark, clutter, app screens, copied creator frame
```

Saved output:

```text
assets/visual-references/section-03-the-price-tag-speaks-first/generated/visible-shopping-promises-generated.png
```

## Rejected References

- Fresh real store screenshots are rejected for this section because they add brand/logo risk and are unnecessary for a generic price-tag mechanism.
- Direct use of real receipt text is rejected because the source numbers are irrelevant and may distract; use fake receipt labels in HyperFrames.
- A generated-only plan is rejected because the section still needs real tag, receipt, and box texture to feel like ordinary shopping life.
- Prompt-only support is rejected because image generation was available and the two support bases were saved.
