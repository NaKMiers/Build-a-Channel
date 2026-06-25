# Section 6 Reference Board

## Reference Pass Status

- Status: `completed earlier and reconstructed from surviving saved assets`
- Browsed references: `4 references were browsed and saved during the original remade Section 6 pass (2 Wikimedia Commons photos, 1 EU repairability/energy label, 1 CC0 airport-security image)`
- Real images saved: `4` (2 used directly as graded photo bases, 2 used as inspiration)
- Generated images: `0`
- Inspected local assets: `shared WIT manifest; surviving review-mirror render at hyperframes/review/section-06.html and its photo bases`
- Prompt-only fallbacks: `0 required`
- Fallback reason: `none; saved references and the approved render survived, so this board documents the real assets rather than re-browsing`

## Search / Browse Notes

- The repair workbench and precision-tool photos came from Wikimedia Commons file pages, which expose source, author, and license.
- Real device/tool brand marks were not used: the repair-table base is brand-masked in HyperFrames, and the screwdriver base is graded and generic.
- The EU repairability/energy label was used only to understand what a real "future label" looks like; the on-screen `FUTURE LABEL` card is a generic rebuild, not the official label.
- The airport-security image seeded the section's defining metaphor (belt, scanner, trays); all checkpoint parts are rebuilt generically in CSS.
- All locks, bills, boxes, cards, checklist, mystery machine, and fake phone are self-made CSS so labels and timing stay controlled and brand-safe.

## References

| Ref | Type | Source | Classification | Why useful | Attention / editor use | Use in production | Saved path |
|---|---|---|---|---|---|---|---|
| R1 | `real image` | Wikimedia Commons, `SHIFT6mq Repair.jpg`, Triskal, `CC BY-SA 4.0` | `safe asset` | Real phone-repair workbench texture: tools, exposed board, bench mess. | Scene 1 base under the REPAIR CHECKPOINT metaphor. | Direct graded use with brand masks over battery/tool marks; record CC BY-SA 4.0 attribution. | `assets/visual-references/section-06-repair-gets-a-security-system/real-world/phone-repair-table-commons-triskal-cc-by-sa-4.jpg` -> graded `assets/section-06/repair-checkpoint-photo-base.jpg` |
| R2 | `real image` | Wikimedia Commons, `Precision Screwdriver Set 2.jpg`, oomlout, `CC BY-SA 2.0` | `safe asset` | Real precision-screwdriver set: the "special tool" idea made physical. | Scene 3 base under the repairability definition/checklist. | Direct graded use; record CC BY-SA 2.0 attribution. | `assets/visual-references/section-06-repair-gets-a-security-system/real-world/precision-screwdriver-set-commons-oomlout-cc-by-sa-2.jpg` -> graded `assets/section-06/precision-screwdriver-photo-base.jpg` |
| R3 | `real reference image` | EU smartphone/tablet energy + repairability label reference | `inspiration only` | Shows what an official repairability/future label looks like (rows, pills, grades). | Scene 4 inspiration for the generic `FUTURE LABEL` card. | Do not reproduce the official EU layout/marks; rebuild as a generic policy card. | `assets/visual-references/section-06-repair-gets-a-security-system/policy/smartphones-tablets-energy-label-eu-reference.png` |
| R4 | `real reference image` | Airport security checkpoint, `CC0` | `inspiration only` | Belt + scanner + tray composition for the checkpoint metaphor. | Scene 1 metaphor seed: barriers become security trays. | Rebuilt generically in CSS (belt, scanner arch, trays); not used directly. | `assets/visual-references/section-06-repair-gets-a-security-system/metaphor/airport-security-check-cc0-inspiration.png` |
| R5 | `local WIT assets` | Shared approved WIT manifest, `.agents/_shared/assets/wit/poses/manifest.json` | `safe channel asset` | Suspicious, trapped, and deadpan poses for the locked-out arc. | Emotional anchors for cues 1-3, 5, 8 only. | Direct WIT PNG overlays. | `assets/wit/wit-pose-suspicious.png`, `assets/wit/wit-pose-trapped-by-app-screen.png`, `assets/wit/wit-pose-deadpan-side-eye.png` |

## Big Scene Reference Coverage

| Big Scene | Needed Visual Basis | Real / Local Reference | Generated Support | Production Decision | Remaining Gap |
|---|---|---|---|---|---|
| 1. Repair Checkpoint | A real repair bench + a security-checkpoint composition. | R1 (repair bench) + R4 (airport security metaphor) + R5 (suspicious WIT). | `none` | Graded brand-masked R1 photo base + generic CSS belt/scanner/trays/shortcut lane. | Keep WIT face clear of the lower-left edge crop. |
| 2. Cost + Ownership Lock | A repair bill vs new box and a locked product. | R5 (trapped WIT). | `none` | Self-made CSS bill, box, stamp, locked product, padlock, glass panel. | Relationship note must not cover the trapped WIT face behind glass. |
| 3. Repairability Test | A real precision tool + a clean definition/checklist. | R2 (precision screwdriver). | `none` | Graded R2 photo base + CSS definition card, checklist, mystery machine. | Keep the definition reading as plain English, not a lesson. |
| 4. Future Label | What a repairability/future label looks like + a payoff frame. | R3 (EU label inspiration) + R5 (deadpan WIT). | `none` | Generic CSS `FUTURE LABEL` card + fake phone + PLEASE HAVE A FUTURE tag. | Keep the card generic; keep the final tag above the subtitle zone. |

## Image Generation Prompts

No generated images were needed. Section 6 uses two graded real photo bases plus fully self-made CSS objects, which keeps labels, the checkpoint metaphor, and WIT-safe zones under exact control with no brand risk.

### Optional Prompt 1 (only if a clean repair-bench base is ever needed without attribution)

```text
Realistic 16:9 editorial photo of a generic electronics repair workbench, neutral tools and an opened device board, simple uncluttered composition, soft even light, empty space on the left for labels and lower-left for a large cartoon character, no brand marks, no logos, no readable text, no people, no watermark.
```

Negative prompt:

```text
text, logos, brand marks, real UI, serial numbers, barcodes, people, hands, private data, watermark, store shelves, advertisement, dramatic lighting
```

## Rejected References

- Direct, unmasked use of R1/R2: rejected because real device/tool brand marks must not appear; bases are graded and brand-masked.
- Reproducing the official EU repairability/energy label (R3) on screen: rejected to avoid implying an official rating; the on-screen card is a generic rebuild.
- Direct use of the airport-security photo (R4): rejected; the checkpoint is rebuilt as generic CSS so it reads as a metaphor, not a real airport.
