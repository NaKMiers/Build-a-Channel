# Production Asset Attribution

Video:
`Why Cheap Products Keep Getting Worse`

Scope:
`Current direct-production assets used by Render step for Sections 1-6`

## Direct Production Assets

### Generated support assets

- `visual-references/section-01-hook/generated/chair-price-tag-generated.png`
  Use: Boards `1`, `2`, `4`
  Status: `safe generated support asset`
- `visual-references/section-01-hook/generated/hidden-future-tag-generated.png`
  Use: Boards `3`, `5`
  Status: `safe generated support asset`
- `visual-references/section-01-hook/generated/wobbly-leg-loose-screw-generated.png`
  Use: Board `6`
  Status: `safe generated support asset`
- `visual-references/section-01-hook/generated/price-tag-receipt-generated.png`
  Use: Board `7` base
  Status: `safe generated support asset`
- `visual-references/section-02-cheap-is-not-the-villain/generated/fair-comparison-two-boxes-generated.png`
  Use: Section `2`, Big Scene `2`, two-box comparison base
  Status: `safe generated support asset`
- `visual-references/section-02-cheap-is-not-the-villain/generated/missing-tomorrow-cutaway-generated.png`
  Use: Section `2`, Big Scene `3`, missing-tomorrow cutaway base
  Status: `safe generated support asset`
- `visual-references/section-03-the-price-tag-speaks-first/generated/price-tag-hiding-future-tags-generated.png`
  Use: Section `3`, Big Scenes `1`, `2`, and `4`, visible price tag hiding future-cost tags
  Status: `safe generated support asset`

### Self-made HyperFrames / CSS assets

- Section `5` handwritten labels, red break/failure marks, generic screen box, cold-breath cue, and feature/speech panels
  Use: Section `5`, cue overlays on real photo bases
  Source: built directly in `section-previews/section-05-more-features-more-tiny-deaths/index.html` from the script, Section 1/8 render grammar, and Section 5 reference board
  Status: `self-made safe production overlays; no real app UI or real product claim is added`
- Section `6` handwritten repair labels, sticky blockers, repair bill, checklist, speech bubble, and simplified phone future label
  Use: Section `6`, cue overlays on real/photo texture bases
  Source: built directly in `section-previews/section-06-repair-gets-a-security-system/index.html` from the script, Section 6 visual plan, Section 6 reference board, and render-side quality pass
  Status: `self-made safe production overlays; no real invoice, official EU label, QR code, or government logo is exposed`

### Real direct-use assets

- `visual-references/section-01-hook/real-world/real-receipt-pexels-towfiqu-barbhuiya.jpg`
  Use: Board `7` proof photo inset
  Source: [Pexels - Close Up of a Receipt](https://www.pexels.com/photo/close-up-of-a-receipt-14647295/)
  Creator: `Towfiqu barbhuiya`
  Terms checked: `Pexels License`
  Safe-use note: direct inset use with overlay labels; do not rely on source numbers as final text
- `visual-references/section-01-hook/real-world/real-blank-tag-pexels-padrinan.jpg`
  Use: Board `8` final hero frame
  Source: [Pexels - White Tag With String and Black Background](https://www.pexels.com/photo/white-tag-with-string-and-black-background-1111320/)
  Creator: `Miguel A. Padrinan`
  Terms checked: `Pexels License`
  Safe-use note: all final label/stamp text added in HyperFrames
- `visual-references/section-02-cheap-is-not-the-villain/real-world/real-blank-tag-pexels-padrinan.jpg`
  Use: Section `2`, Big Scene `1`, blank price-tag texture for `CHEAP != BAD`
  Source: [Pexels - White Tag With String and Black Background](https://www.pexels.com/photo/white-tag-with-string-and-black-background-1111320/)
  Creator: `Miguel A. Padrinan`
  Terms checked: `Pexels License`
  Safe-use note: all labels and correction marks added in HyperFrames
- `visual-references/section-04-the-boring-parts-disappear/real-world/real-sewing-machine-stitching-fabric-pexels-shoreline-vehicles.jpg`
  Use: Section `4`, Big Scene `1`, fabric/stitching background for `BORING FUTURE`
  Source: [Pexels - Close-up of Sewing Machine Stitching Fabric](https://www.pexels.com/photo/close-up-of-sewing-machine-stitching-fabric-30902519/)
  Creator: `shoreline vehicles`
  Terms checked: `Pexels License`
  Safe-use note: direct background with all labels and jokes added in HyperFrames
- `visual-references/section-04-the-boring-parts-disappear/real-world/real-screwdriver-bits-pexels-roseson-studios.jpg`
  Use: Section `4`, Big Scene `2`, repair-table / screwdriver background for `REPAIRABLE`
  Source: [Pexels - Close-up of a Screwdriver](https://www.pexels.com/photo/close-up-of-a-screwdriver-20874131/)
  Creator: `Roseson Studios`
  Terms checked: `Pexels License`
  Safe-use note: direct background with generic device/printer overlays and labels added in HyperFrames
- `visual-references/section-04-the-boring-parts-disappear/real-world/real-cardboard-boxes-pexels-harper-sunday.jpg`
  Use: Section `4`, Big Scene `3`, cardboard/product-box background for final `LESS FUTURE BUILT IN` payoff
  Source: [Pexels - Close-up of Cardboard Boxes and Lids](https://www.pexels.com/photo/close-up-of-cardboard-boxes-and-lids-17260157/)
  Creator: `Harper Sunday`
  Terms checked: `Pexels License`
  Safe-use note: direct background with final product box, WIT, and labels added in HyperFrames
- `visual-references/section-05-more-features-more-tiny-deaths/real-world/real-domestic-refrigerator-commons-infrogmation.jpg`
  Use: Section `5`, Big Scenes `1` and `2`, real lived-in kitchen/fridge background
  Source: [Wikimedia Commons - US Domestic Refrigerator - Frigidaire.jpg](https://commons.wikimedia.org/wiki/File:US_Domestic_Refrigerator_-_Frigidaire.jpg)
  Creator: `Infrogmation of New Orleans`
  Terms checked: `CC BY-SA 4.0`
  Safe-use note: direct background use only as generic fridge/kitchen texture; no claim that this real model failed or represents the criticized product
- `visual-references/section-05-more-features-more-tiny-deaths/real-world/real-appliance-power-module-commons-phiarc.jpg`
  Use: Section `5`, Big Scene `3`, real appliance circuit-board / tiny-failure background
  Source: [Wikimedia Commons - Washing machine power module.jpg](https://commons.wikimedia.org/wiki/File:Washing_machine_power_module.jpg)
  Creator: `Phiarc`
  Terms checked: `CC BY-SA 4.0`
  Safe-use note: direct background use with generic red target and repair-cost labels; no brand/product failure claim
- `assets/section-06/phone-repair-table.jpg`
  Copied from: `visual-references/section-06-repair-gets-a-security-system/real-world/phone-repair-shift6mq-cc-by-sa-4.jpg`
  Use: Section `6`, Big Scenes `1` and `2`, opened phone repair-table background
  Source: [Wikimedia Commons - SHIFT6mq Repair.jpg](https://commons.wikimedia.org/wiki/File:SHIFT6mq_Repair.jpg)
  Creator: `Triskal`
  Terms checked: `CC BY-SA 4.0`
  Safe-use note: direct background use only as generic repair-table texture; visible source-product markings are not claims that the pictured product is defective, cheap, blocked, or criticized
- `assets/section-06/precision-screwdrivers.jpg`
  Copied from: `visual-references/section-06-repair-gets-a-security-system/real-world/precision-screwdriver-set-cc-by-sa-2.jpg`
  Use: Section `6`, Big Scene `3`, repairability/tool background
  Source: [Wikimedia Commons - Precision Screwdriver Set 2.jpg](https://commons.wikimedia.org/wiki/File:Precision_Screwdriver_Set_2.jpg)
  Creator: `oomlout`
  Terms checked: `CC BY-SA 2.0`
  Safe-use note: direct tool-background use with generic repairability labels added in HyperFrames
- `assets/section-06/cardboard-boxes.jpg`
  Copied from: `visual-references/section-08-payoff/real-world/real-cardboard-boxes-pexels-harper-sunday.jpg`
  Use: Section `6`, Big Scene `4`, cardboard/future-label payoff background
  Source: [Pexels - Close-up of Cardboard Boxes and Lids](https://www.pexels.com/photo/close-up-of-cardboard-boxes-and-lids-17260157/)
  Creator: `Harper Sunday`
  Terms checked: `Pexels License`
  Safe-use note: direct texture background with all labels and jokes added in HyperFrames

### Reusable channel assets

- `wit/`
  Use: Sections `1-6` WIT poses
  Source: channel-approved shared WIT pose set via project junction to `.agents/_shared/assets/wit/poses/`
  Status: `safe channel asset`
- `voiceover/`
  Use: Sections `1-6` approved narration audio via project junction to `voiceover/`
  Status: `project-local approved audio source`
- `fonts/patrick-hand-latin.woff2`
  Use: Sections `1-6` handwritten labels
  Source: copied from existing project-local channel font asset in `projects/why-everyone-pretends-to-be-busy/assets/fonts/`
  Status: `project-local reusable font asset`

## Reference-Only Assets Not Used Directly In Final Boards

- `visual-references/section-01-hook/real-world/real-tag-on-object-unsplash-kelly-sikkema.jpg`
  Status: `mockup target`
- `visual-references/section-01-hook/real-world/real-torn-swivel-chair-wikimedia.jpg`
  Status: `inspiration only`
- `visual-references/section-01-hook/real-world/real-broken-office-chair-cc-by-sa-2.jpg`
  Status: `inspiration only`
- `visual-references/section-02-cheap-is-not-the-villain/real-world/real-black-jacket-hanger-pexels-mishchenko.jpg`
  Status: `mockup target`; jacket was rebuilt generically in HyperFrames
- `visual-references/section-02-cheap-is-not-the-villain/real-world/real-receipt-pexels-towfiqu-barbhuiya.jpg`
  Status: `mockup target`; receipt was rebuilt generically in HyperFrames
- `visual-references/section-02-cheap-is-not-the-villain/real-world/real-plain-white-boxes-pexels-dalprat.jpg`
  Status: `safe texture reference`; superseded by generated two-box comparison and generated cutaway bases in the revised Section 2 render
- `visual-references/section-03-the-price-tag-speaks-first/real-world/real-blank-tag-pexels-padrinan.jpg`
  Status: `safe texture reference`; Section 3 used generated hidden-tag base directly after real tag texture was inspected
- `visual-references/section-03-the-price-tag-speaks-first/real-world/real-receipt-pexels-towfiqu-barbhuiya.jpg`
  Status: `mockup target`; Section 3 rebuilt cost/wallet labels in HyperFrames and did not expose source receipt numbers
- `visual-references/section-03-the-price-tag-speaks-first/real-world/real-plain-white-boxes-pexels-dalprat.jpg`
  Status: `safe texture reference`; Section 3 Scene 3 used this only as material guidance for a CSS-built checkout promise arena
- `visual-references/section-03-the-price-tag-speaks-first/generated/visible-shopping-promises-generated.png`
  Status: `safe generated support reference`; inspected and intentionally skipped for direct use in revised Section 3 because it repeated the same tabletop/tag visual language as Scene 1
- `visual-references/section-04-the-boring-parts-disappear/real-world/real-rustic-hinge-pexels-brett-sayles.jpg`
  Status: `mockup target`; hinge shape reference only, not used directly in the simplified remake
- `visual-references/section-04-the-boring-parts-disappear/real-world/real-phone-battery-repair-pexels-harry-tucker.jpg`
  Status: `mockup target`; phone/device repair layout reference only, not used directly because of visible device marks and UI/text
- `visual-references/section-04-the-boring-parts-disappear/real-world/real-printer-repair-pexels-bulat843.jpg`
  Status: `inspiration only`; printer/workbench reference only, not used directly because it contains a real person, visible workshop text, and too much clutter
- `visual-references/section-04-the-boring-parts-disappear/section-04-reference-contact-sheet.png`
  Status: `internal reference board`; not used directly in final video
- `visual-references/section-05-more-features-more-tiny-deaths/real-world/real-water-dispenser-refrigerator-commons-dave-matos.jpg`
  Source: Wikimedia Commons, Dave Matos, `A cold glass of water - GE Refrigerator - August 7, 2007.jpg`
  Status: `inspiration only / mockup target`; not used directly because of visible logos, stickers, hand, and photo clutter
- `visual-references/section-05-more-features-more-tiny-deaths/real-world/real-control-panel-commons-solomon203.jpg`
  Source: Wikimedia Commons, Solomon203, `Sampo VM-C2066 control panel 20201031.jpg`
  Status: `inspiration only`; not used directly because of visible brand and labels
- `visual-references/section-06-repair-gets-a-security-system/real-world/repair-lab-workbench-cc-by-2.jpg`
  Source: Wikimedia Commons, Redaktion NdW / Alena Zielinski, `Repair Lab (48115819418).jpg`
  Status: `inspiration only`; not used directly because it includes visible people, event/workbench clutter, cups, and clothing marks
- `visual-references/section-06-repair-gets-a-security-system/policy/smartphones-tablets-energy-label-eu-reference.png`
  Source: European Commission Energy Efficient Products, `Smartphones and Tablets`
  Status: `mockup target / inspiration only`; not used directly because Section 6 uses a simplified no-logo fake phone future label

## Notes

- Section preview uses a minimal hardlinked working set from the project-level `assets` library because this Windows HyperFrames setup previously failed to serve junction-backed section assets.
- Generated images are controlled support bases, not direct replacements for reference research.
- Future sections should append only the assets they use directly in production.
