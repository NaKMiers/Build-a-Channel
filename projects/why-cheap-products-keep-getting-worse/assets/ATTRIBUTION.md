# Production Asset Attribution

Video:
`Why Cheap Products Keep Getting Worse`

Scope:
`Current direct-production assets used by Render step for Sections 1-4`

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

### Reusable channel assets

- `wit/`
  Use: Sections `1-4` WIT poses
  Source: channel-approved shared WIT pose set via project junction to `.agents/_shared/assets/wit/poses/`
  Status: `safe channel asset`
- `voiceover/`
  Use: Sections `1-4` approved narration audio via project junction to `voiceover/`
  Status: `project-local approved audio source`
- `fonts/patrick-hand-latin.woff2`
  Use: Sections `1-4` handwritten labels
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

## Notes

- Section preview uses a minimal hardlinked working set from the project-level `assets` library because this Windows HyperFrames setup previously failed to serve junction-backed section assets.
- Generated images are controlled support bases, not direct replacements for reference research.
- Future sections should append only the assets they use directly in production.
