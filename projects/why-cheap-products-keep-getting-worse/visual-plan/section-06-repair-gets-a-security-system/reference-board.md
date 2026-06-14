# Section 6 Reference Board

## Reference Pass Status

- Status: `completed with global gstack browse fallback`
- Browsed references: `4 source pages inspected after project-local browse failed its own server startup check`
- Real images saved: `4`
- Generated images: `0`
- Inspected local assets: `project WIT manifest and downloaded reference images`
- Prompt-only fallbacks: `0 required`
- Fallback reason: `project-local browse binary existed but failed to start; global gstack browse at C:\Users\hello\.agents\skills\gstack\browse\dist\browse.exe worked and was used`

## Search / Browse Notes

- Searched Wikimedia Commons for `smartphone repair` and `precision screwdriver electronics`.
- Inspected Wikimedia file pages for the opened phone, repair lab, and precision screwdriver set to confirm author/license/source notes.
- Inspected the European Commission Energy Efficient Products smartphone/tablet page for the official repairability-label proof beat.
- Downloaded images are references first, not automatic production assets.
- Final render should use generic self-made HyperFrames repair doors, locks, phone panels, bills, and labels. This avoids brand claims, official-label copying, and private-data risk.

## References

| Ref | Type | Source | Classification | Why useful | Attention / editor use | Use in production | Saved path |
|---|---|---|---|---|---|---|---|
| R1 | `real image` | Wikimedia Commons, Triskal, `SHIFT6mq Repair.jpg`, https://commons.wikimedia.org/wiki/File:SHIFT6mq_Repair.jpg, CC BY-SA 4.0 | `mockup target / inspiration only` | Shows a real opened phone with battery, display, screws, and repair tool layout. | Scenes 1, 3, and 4: phone internals, screws, open-device silhouette. | Do not use directly by default because visible `shift` branding appears on battery/tool. Translate into generic no-logo device. | `assets/visual-references/section-06-repair-gets-a-security-system/real-world/phone-repair-shift6mq-cc-by-sa-4.jpg` |
| R2 | `real image` | Wikimedia Commons, Redaktion NdW / Alena Zielinski, `Repair Lab (48115819418).jpg`, https://commons.wikimedia.org/wiki/File:Repair_Lab_(48115819418).jpg, CC BY 2.0 | `inspiration only` | Shows a real repair-table situation with people, tools, parts, and workbench context. | Scene 1 repair-door world and Scene 3 local repair shop question. | Do not use directly because of visible people, clothing marks, cups, and event clutter. | `assets/visual-references/section-06-repair-gets-a-security-system/real-world/repair-lab-workbench-cc-by-2.jpg` |
| R3 | `real image` | Wikimedia Commons, oomlout, `Precision Screwdriver Set 2.jpg`, https://commons.wikimedia.org/wiki/File:Precision_Screwdriver_Set_2.jpg, CC BY-SA 2.0 | `direct asset candidate / mockup target` | Clean tool silhouettes on a mostly white background. | Scene 1 `SPECIAL TOOL` lock and optional tiny tool in WIT hand. | Prefer CSS/trace. Direct crop is acceptable only if render records attribution. | `assets/visual-references/section-06-repair-gets-a-security-system/real-world/precision-screwdriver-set-cc-by-sa-2.jpg` |
| R4 | `official page / visual reference` | European Commission Energy Efficient Products, `Smartphones and Tablets`, https://energy-efficient-products.ec.europa.eu/product-list/smartphones-and-tablets_en | `mockup target / inspiration only` | Supports the policy proof: repairability class, battery endurance, spare parts, software/firmware access, and labels can be required for certain products. | Scene 4 simplified repairability-label proof. | Do not copy directly. Build a simplified fake no-logo label with fewer fields and handwritten overlays. | `assets/visual-references/section-06-repair-gets-a-security-system/policy/smartphones-tablets-energy-label-eu-reference.png` |
| R5 | `local WIT assets` | Project WIT manifest, `assets/wit/manifest.json` | `safe channel asset` | Provides exact approved WIT pose filenames. | Suspicious repairer, locked-out owner, final deadpan future check. | Direct WIT PNG overlays. | `assets/wit/` |

## Big Scene Reference Coverage

| Big Scene | Needed Visual Basis | Real / Local Reference | Generated Support | Production Decision | Remaining Gap |
|---|---|---|---|---|---|
| 1. Repair door becomes a security system | Door, locks, tools, bill/new-box comparison, real repair texture. | R1 for opened phone, R2 for repair-table context, R3 for tool silhouette, R5 for WIT. | `none needed` | Build generic CSS/HTML repair door, locks, repair bill, and product box. | Render must keep lock labels readable and avoid crowded lock pile. |
| 2. You own it, but not enough | Locked product close-up and giant locked-out WIT. | R1 for product panel idea, R5 for WIT. | `none needed` | Build a generic locked panel and speech bubble. | Need screenshot QA that bubble does not cover WIT face. |
| 3. Repairability means easy to fix | Clean definition/checklist and generic phone/device outline. | R1 for open-device layout, R2 for local repair context. | `none needed` | Build a generic checklist with no WIT so the definition breathes. | Need text-size check for `REPAIRABILITY = EASY TO FIX`. |
| 4. Society asks the phone to have a future | Simplified policy label, generic phone, final deadpan WIT. | R4 for official repairability-label concept, R5 for WIT. | `none needed` | Build a simplified no-logo label card and final future tag in HyperFrames. | Need to avoid copying official label design too literally. |

## Image Generation Prompts

No generated images were needed for this run. The final section should be more controllable as HyperFrames-built generic objects because the visuals need exact labels, locks, WIT-safe zones, and no brand or official-label copying risk.

### Optional Prompt 1

```text
Realistic 16:9 clean editorial reference image of a generic opened smartphone on a neutral repair mat, simple visible battery and screws, no brand marks, no logos, no serial numbers, no readable text, empty space on left and right for labels and a cartoon character overlay, soft natural lighting.
```

Negative prompt:

```text
text, logos, brand marks, QR codes, serial numbers, private data, hands, people, watermark, official label design, dramatic sparks, broken glass
```

### Optional Prompt 2

```text
Realistic 16:9 clean editorial reference image of a generic product repair door with several simple padlocks, one blank repair bill, one plain new product box, no text, no logos, no brand marks, uncluttered flat-lay composition, large empty label-safe areas.
```

Negative prompt:

```text
text, logos, brand marks, readable invoices, real prices, QR codes, people, store labels, official government label, watermark
```

## Rejected References

- Direct use of R1: rejected by default because the phone/battery/tool include visible `shift` branding; use as a mockup target instead.
- Direct use of R2: rejected because people, clothing marks, cups, and event clutter would distract from the simple section metaphor.
- Direct use of R4: rejected because the final render should not copy an official EU energy-label graphic, QR code, logo, or exact layout.
- Wikimedia search results unrelated to repair/product tools: rejected as noisy search output.
- Prompt-only reference fallback: not used because live browse and local asset inspection succeeded.
