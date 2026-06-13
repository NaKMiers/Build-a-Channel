# Section 4 Reference Board

## Reference Pass Status

- Status: `completed with fallback sourcing; simplified-remake decisions added after render rejection`
- Browsed references: `6 source pages inspected through sourced web lookup after project-local browse failed startup twice and global gstack browse was not installed`
- Real images saved: `6`
- Generated images: `0`
- Inspected local assets: `shared WIT manifest and saved Section 4 contact sheet`
- Prompt-only fallbacks: `0 required`
- Fallback reason: `project-local gstack browse binary was present but could not start its server within its own 15s limit on repeated attempts; global gstack browse was not installed`

## Search / Browse Notes

- Searched for real visual bases around `stitching`, `hinge`, `screwdriver`, `battery repair`, `printer repair`, and `cardboard product box`.
- Preferred Pexels pages because the source pages expose creator names, free-use status, and direct image download URLs.
- Pexels license page was checked as the source-license baseline: https://www.pexels.com/license/
- Downloaded references are not automatically final production assets. Each item below is classified before use.
- Phone and printer images are useful references but should not be used directly because the phone image contains recognizable device branding/UI text and the printer image contains a person/workshop text/clutter.
- Remake decision: the rejected Section 4 render direction used too many labels and object cards. The simplified remake uses only three direct background candidates: fabric/stitching, screwdriver/repair table, and cardboard/product box. Phone and printer references stay mockup/inspiration only.

## References

| Ref | Type | Source | Classification | Why useful | Attention / editor use | Use in production | Saved path |
|---|---|---|---|---|---|---|---|
| R1 | `real image` | Pexels, shoreline vehicles, `Close-up of Sewing Machine Stitching Fabric`, https://www.pexels.com/photo/close-up-of-sewing-machine-stitching-fabric-30902519/ | `safe asset candidate` | Shows stitching as a real, boring, physical quality piece. | Use for fabric/stitching texture and machine detail in Scene 1. | Direct crop candidate or texture reference; add labels in HyperFrames. | `assets/visual-references/section-04-the-boring-parts-disappear/real-world/real-sewing-machine-stitching-fabric-pexels-shoreline-vehicles.jpg` |
| R2 | `real image` | Pexels, Brett Sayles, `Close up of Hinge on Wooden Planks`, https://www.pexels.com/photo/close-up-of-hinge-on-wooden-planks-17503605/ | `mockup target` | Gives hinge shape, screw placement, and movement point. | Use to build a simplified hinge card that can carry the joke. | Do not make the scene about old doors; rebuild as generic hinge piece. | `assets/visual-references/section-04-the-boring-parts-disappear/real-world/real-rustic-hinge-pexels-brett-sayles.jpg` |
| R3 | `real image` | Pexels, Roseson Studios, `Close-up of a Screwdriver`, https://www.pexels.com/photo/close-up-of-a-screwdriver-20874131/ | `safe asset candidate` | Clear normal screwdriver and bit shapes against white space. | Supports the `normal screwdriver` vs `secret handshake` joke. | Direct crop candidate or simplified prop source. | `assets/visual-references/section-04-the-boring-parts-disappear/real-world/real-screwdriver-bits-pexels-roseson-studios.jpg` |
| R4 | `real image` | Pexels, Harry Tucker, `DIY iPhone Repair with Tools and Laptop`, https://www.pexels.com/photo/diy-iphone-repair-with-tools-and-laptop-32942100/ | `mockup target` | Shows open device, battery, tools, and repair-table layout. | Supports the replaceable battery cue and repair table scene. | Do not use directly because of real Apple/device marks and readable UI/text; rebuild generic device. | `assets/visual-references/section-04-the-boring-parts-disappear/real-world/real-phone-battery-repair-pexels-harry-tucker.jpg` |
| R5 | `real image` | Pexels, Bulat843, `Technician Repairing Printer in Workshop`, https://www.pexels.com/photo/technician-repairing-printer-in-workshop-32588544/ | `inspiration only / mockup target` | Gives a real printer/electronics repair bench feeling. | Supports the `already repairing a printer` aside. | Do not use directly due visible person, workshop text, and clutter; rebuild generic printer bench. | `assets/visual-references/section-04-the-boring-parts-disappear/real-world/real-printer-repair-pexels-bulat843.jpg` |
| R6 | `real image` | Pexels, Harper Sunday, `Close-up of Cardboard Boxes and Lids`, https://www.pexels.com/photo/close-up-of-cardboard-boxes-and-lids-17260157/ | `safe asset candidate` | Neutral complete-looking product/package texture with label-safe area. | Supports final complete-outside product shell. | Direct crop or texture reference; all labels/cutaway added in HyperFrames. | `assets/visual-references/section-04-the-boring-parts-disappear/real-world/real-cardboard-boxes-pexels-harper-sunday.jpg` |
| R7 | `local contact sheet` | Created locally from R1-R6 | `safe internal reference` | Shows all reference roles together for visual differentiation. | Use before render to avoid repeating Section 3 tabletop/tag scene language. | Not used directly in final video. | `assets/visual-references/section-04-the-boring-parts-disappear/section-04-reference-contact-sheet.png` |
| R8 | `local WIT assets` | Shared WIT manifest, `.agents/_shared/assets/wit/poses/manifest.json` | `safe channel asset` | Provides approved WIT pose filenames. | Use only selected poses: suspicious, thinking, betrayed. | Direct WIT PNG overlays. | `.agents/_shared/assets/wit/poses/` |

## Big Scene Reference Coverage

| Big Scene | Needed Visual Basis | Real / Local Reference | Generated Support | Production Decision | Remaining Gap |
|---|---|---|---|---|---|
| 1. The boring future tray | Product cutaway plus fabric, stitching, hinge pieces. | R1, R2, R6, R7. | `none needed` | Build in HyperFrames as CSS tray/cards, optionally use texture crops. | No gap if render follows the exact tray/card layout. |
| 2. The repair-friendly parts table | Generic open device, replaceable battery, normal screwdriver, spare-part drawer. | R3, R4, R6, R7. | `none needed` | Rebuild generic device and drawer; do not use phone image directly. | Render must avoid real phone branding. |
| 3. The unglamorous printer person | Store quote plus generic printer repair bench. | R5, R7, WIT pose `wit-pose-thinking.png`. | `none needed` | Rebuild generic printer bench in HyperFrames. | Need to keep clutter simple enough for labels. |
| 4. Complete outside, missing inside | Complete product/package exterior that reveals missing internal slots. | R6, R7, WIT pose `wit-pose-betrayed.png`. | `none needed` | CSS product shell/cutaway with texture influence. | Final WIT/text collision must be checked in screenshots. |

## Image Generation Prompts

No generated images were needed for this run because the visual plan uses locally saved real references plus CSS/HTML bases that keep labels, cutaways, missing slots, and WIT zones controllable. If render later needs a controlled production-safe base, use these optional prompts and save generated outputs under this section asset folder.

### Optional Prompt 1

```text
Realistic 16:9 product cutaway on a clean neutral tabletop, generic plain consumer product shell opened to reveal empty internal slots, small removable objects representing fabric strip, stitching strip, hinge, battery, screw, and spare part, simple uncluttered composition, empty space on top and right for labels, no text, no logos, no watermarks, no brand marks, no people.
```

Negative prompt:

```text
text, logos, trademarks, brand marks, readable labels, hands, people, clutter, dramatic lighting, busy store aisle, smartphone brand, printer brand, watermark
```

### Optional Prompt 2

```text
Realistic 16:9 plain cardboard product box that looks complete from the outside, partially opened as a clean cutaway with missing internal component slots, neutral beige background, label-safe area, simple product texture, no text, no logos, no watermarks, no brand marks, no private data.
```

Negative prompt:

```text
text, logos, brand packaging, barcodes, shipping labels, people, hands, clutter, watermark, photorealistic brand objects
```

## Rejected References

- `DepositPhotos printer repair` from image search: rejected because license/source fit was weaker than Pexels and the image felt like generic stock.
- `Pikbest denim texture` from image search: rejected because licensing and reuse conditions were less clean than Pexels for this workflow.
- Direct use of the Pexels phone repair image: rejected for direct production because visible Apple/device marks and UI/text would create unnecessary brand/source risk.
- Direct use of the Pexels printer repair image: rejected for direct production because it includes a real person, visible workshop text, and too much clutter for a clean joke frame.
