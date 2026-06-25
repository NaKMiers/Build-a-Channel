# Section 5 Reference Board

## Reference Pass Status

- Status: `completed with global gstack browse fallback`
- Browsed references: `4 Wikimedia Commons file pages inspected after project-local browse failed to start within its own 15s server timeout`
- Real images saved: `4`
- Generated images: `0`
- Inspected local assets: `project WIT manifest and downloaded reference images`
- Prompt-only fallbacks: `0 required`
- Fallback reason: `project-local browse binary existed but failed server startup; global gstack browse at C:\Users\Anpha Right Choice\.agents\skills\gstack\browse\dist\browse.exe worked and was used`

## Search / Browse Notes

- Searched Wikimedia Commons for `refrigerator`, `smart refrigerator screen`, `appliance control panel`, `circuit board appliance`, and `ice dispenser refrigerator`.
- Pexels search was attempted first, but the page stayed behind Cloudflare verification in headless mode.
- Wikimedia was preferred after that because file pages expose source, author, and license details.
- Downloaded images are reference assets, not automatic direct production assets.
- Real appliances with visible brand marks or page-level brand/failure claims should not be used directly in the video.
- The final render should use generic self-made HyperFrames fridge, control-panel, feature, and circuit-board mockups. Use the real images for silhouette, material, detail density, and texture.

## References

| Ref | Type | Source | Classification | Why useful | Attention / editor use | Use in production | Saved path |
|---|---|---|---|---|---|---|---|
| R1 | `real image` | Wikimedia Commons, Infrogmation of New Orleans, `US Domestic Refrigerator - Frigidaire.jpg`, https://commons.wikimedia.org/wiki/File:US_Domestic_Refrigerator_-_Frigidaire.jpg | `mockup target` | Real home-kitchen fridge silhouette and ordinary appliance scale. | Scene 2 simple fridge shape and kitchen context. | Do not use directly because the file page names a real brand and says the unit was defunct; rebuild as generic fridge. | `assets/visual-references/section-05-more-features-more-tiny-deaths/real-world/real-domestic-refrigerator-commons-infrogmation.jpg` |
| R2 | `real image` | Wikimedia Commons, Dave Matos, `A cold glass of water - GE Refrigerator - August 7, 2007.jpg`, https://commons.wikimedia.org/wiki/File:A_cold_glass_of_water_-_GE_Refrigerator_-_August_7,_2007.jpg | `inspiration only / mockup target` | Shows a useful water-dispenser feature as a real appliance detail. | Scene 1 useful-feature proof and Scene 2 dispenser module shape. | Do not use directly because of visible real logos, stickers, and hand/photo clutter; rebuild as generic no-logo dispenser. | `assets/visual-references/section-05-more-features-more-tiny-deaths/real-world/real-water-dispenser-refrigerator-commons-dave-matos.jpg` |
| R3 | `real image` | Wikimedia Commons, Phiarc, `Washing machine power module.jpg`, https://commons.wikimedia.org/wiki/File:Washing_machine_power_module.jpg | `mockup target / optional direct texture with attribution` | Clean circuit-board module with many small dependent parts. | Scene 3 failure-point texture and tiny-part logic. | Preferred use is a generic CSS/illustration circuit board. Direct cropped use is allowed only if render records CC BY-SA 4.0 attribution and avoids brand/product claims. | `assets/visual-references/section-05-more-features-more-tiny-deaths/real-world/real-appliance-power-module-commons-phiarc.jpg` |
| R4 | `real image` | Wikimedia Commons, Solomon203, `Sampo VM-C2066 control panel 20201031.jpg`, https://commons.wikimedia.org/wiki/File:Sampo_VM-C2066_control_panel_20201031.jpg | `inspiration only` | Worn appliance/control-panel texture, button spacing, and too-many-controls feeling. | Scene 2 modern fridge feature panel and Scene 3 committee board texture. | Do not use directly because of visible brand and non-English labels; rebuild generic buttons/icons. | `assets/visual-references/section-05-more-features-more-tiny-deaths/real-world/real-control-panel-commons-solomon203.jpg` |
| R5 | `local WIT assets` | Project WIT manifest, `assets/wit/manifest.json` | `safe channel asset` | Approved WIT poses for suspicion, confusion, and facepalm beats. | Emotional anchors only, not filler. | Direct WIT PNG overlays. | `assets/wit/` |

## Big Scene Reference Coverage

| Big Scene | Needed Visual Basis | Real / Local Reference | Generated Support | Production Decision | Remaining Gap |
|---|---|---|---|---|---|
| 1. Fair feature setup | A few useful features that do not make technology look bad. | R2 for dispenser usefulness, R4 for panel texture, R5 for WIT. | `none needed` | Build generic feature cards/icons in HyperFrames: safer appliance, better battery, gravity-surviving phone. | None if render keeps labels sparse and sincere. |
| 2. Simple fridge versus modern feature pile | One boring fridge with one job, next to a modern fridge that gains features and one silly opinion bubble. | R1 for fridge silhouette, R2 for dispenser module, R4 for buttons/panel. | `none needed` | Build two generic fridge illustrations in CSS/HTML; do not use real brand images directly. | Need screenshot QA so feature labels do not become a mini-card swarm. |
| 3. Technology committee and tiny failure | Internal board/control logic where one tiny part can make the whole product harder to fix. | R3 for circuit-board density, R4 for control-panel mood, R5 for WIT facepalm. | `none needed` | Build a generic circuit-board committee table in HyperFrames with one red failed part and one repair-cost tag. | Need final WIT/text collision check. |

## Image Generation Prompts

No generated images were needed for this run. The final Section 5 scene should be more controllable as HyperFrames-built generic objects because the script needs exact labels, feature grouping, and WIT-safe zones.

### Optional Prompt 1

```text
Realistic 16:9 clean editorial reference image of a generic modern refrigerator in a simple kitchen, no brand marks, no logos, one blank screen area, one blank water dispenser area, simple uncluttered composition, empty space on left for labels and right for a large cartoon character overlay, no text, no people, no private data, no watermark.
```

Negative prompt:

```text
text, logos, brand marks, real UI, barcode, people, hands, private home clutter, watermark, store aisle, product advertisement, readable labels
```

### Optional Prompt 2

```text
Realistic 16:9 close-up of a generic appliance circuit board on a clean white background, many tiny components, one small failed part visually isolated, no text, no logos, no brand marks, enough empty space for red markup and labels.
```

Negative prompt:

```text
text, logos, serial numbers, brand marks, readable labels, hands, tools, clutter, watermark, dramatic smoke, fire, broken glass
```

## Rejected References

- Pexels search results: rejected as a live source because Cloudflare verification blocked the headless browser session.
- Wikimedia `smart refrigerator screen` search result `This incredible house was featured in WIRED magazine`: rejected because it was not clearly a useful fridge/control reference for this section.
- Wikimedia `ice dispenser refrigerator` search result from an old publication scan: rejected because it did not support the modern feature/failure visual.
- Direct use of R1/R2/R4 in final frames: rejected because visible brands, stickers, or real-product context create unnecessary accusation and source-risk.
