# Section 8 Reference Board

## Reference Pass Status

- Status: `completed with local sourced-reference fallback`
- Browsed references: `0 fresh pages; project-local browse failed its 15s startup check and global gstack browse was not installed`
- Real images saved: `4 copied from already sourced project reference assets`
- Generated images: `3 copied from already inspected generated support assets`
- Inspected local assets: `Section 1, 2, 3, and 4 reference assets plus shared WIT manifest`
- Prompt-only fallbacks: `0 required`
- Fallback reason: `fresh browsing was unavailable in this environment; the project already contains sourced and inspected real references for blank tags, receipts, product boxes, and cardboard textures that directly cover Section 8`

## Search / Browse Notes

- Attempted to start the project-local browse binary at `.agents/skills/browse/dist/browse.exe`; it failed to start within its own 15s limit.
- Checked for a global gstack browse binary under the user profile; none was installed.
- Reused previously sourced local references with preserved source notes from earlier project boards instead of doing unsourced image grabbing.
- Selected assets were copied into `assets/visual-references/section-08-payoff/` so Section 8 has a self-contained reference folder.
- Direct use is allowed only for safe generated support bases or safe real texture/background candidates. Real receipt numbers must not be exposed.

## References

| Ref | Type | Source | Classification | Why useful | Attention / editor use | Use in production | Saved path |
|---|---|---|---|---|---|---|---|
| R1 | `generated support image` | Prior Section 3 image generation, `price-tag-hiding-future-tags-generated.png` | `safe generated support base` | Product box, dominant yellow tag, and hidden tags already express the whole video motif. | Best opening callback for `why worse?` and `price you see today`. | Direct Big Scene 1 base; add all labels in HyperFrames. | `assets/visual-references/section-08-payoff/generated/price-tag-hiding-future-tags-generated.png` |
| R2 | `generated support image` | Prior Section 1 image generation, `price-tag-receipt-generated.png` | `safe generated support base` | Blank tag, blank receipt, pen, screw, and table give the exact real-price composition. | Best base for the receipt line-item scene. | Direct Big Scene 2 base; all receipt text created in HyperFrames. | `assets/visual-references/section-08-payoff/generated/price-tag-receipt-generated.png` |
| R3 | `real image` | Pexels, Miguel A. Padrinan, `White Tag With String and Black Background`, https://www.pexels.com/photo/white-tag-with-string-and-black-background-1111320/ | `safe asset candidate` | Clean blank tag shape, string, paper texture, and negative space. | Reference for final question tag and physical tag scale. | Direct crop candidate or CSS tag reference; add all text in HyperFrames. | `assets/visual-references/section-08-payoff/real-world/real-blank-tag-pexels-padrinan.jpg` |
| R4 | `real image` | Pexels, Towfiqu barbhuiya, `Close-up of a Receipt`, https://www.pexels.com/photo/close-up-of-a-receipt-14647295/ | `mockup target` | Real receipt texture and cost-paper feeling. | Keeps `real price` scene from feeling like a flat spreadsheet. | Do not expose source numbers; use as texture guidance or fully covered crop only. | `assets/visual-references/section-08-payoff/real-world/real-receipt-pexels-towfiqu-barbhuiya.jpg` |
| R5 | `real image` | Pexels, Dalila Dalprat, `Stacked White Cardboard Boxes`, https://www.pexels.com/photo/stacked-white-cardboard-boxes-10938208/ | `safe texture reference` | Simple product-box geometry and clean negative space. | Backup product-box reference for Big Scene 3. | Use as texture/reference, not required if cardboard boxes read better. | `assets/visual-references/section-08-payoff/real-world/real-plain-white-boxes-pexels-dalprat.jpg` |
| R6 | `real image` | Pexels, Harper Sunday, `Close-up of Cardboard Boxes and Lids`, https://www.pexels.com/photo/close-up-of-cardboard-boxes-and-lids-17260157/ | `safe asset candidate` | Warm cardboard/product-box texture with calmer end-screen feeling. | Best final-scene texture for `How much future is included?`. | Direct background candidate or texture reference; add final tag in HyperFrames. | `assets/visual-references/section-08-payoff/real-world/real-cardboard-boxes-pexels-harper-sunday.jpg` |
| R7 | `generated support image` | Prior Section 2 image generation, `missing-tomorrow-cutaway-generated.png` | `fallback / reference only` | Shows missing future as empty compartments, useful as a callback. | Optional small insert if the final question needs visual memory. | Do not use as main Big Scene 3 because Section 2 already owns this visual language. | `assets/visual-references/section-08-payoff/generated/missing-tomorrow-cutaway-generated.png` |
| R8 | `local WIT assets` | Shared/project WIT manifest | `safe channel asset` | Approved WIT pose filenames for final emotional beats. | Use suspicion, evidence, and deadpan evaluator beats. | Direct WIT overlays only. | `.agents/_shared/assets/wit/poses/` or project `assets/wit/` |

## Big Scene Reference Coverage

| Big Scene | Needed Visual Basis | Real / Local Reference | Generated Support | Production Decision | Remaining Gap |
|---|---|---|---|---|---|
| 1. Callback question and fair correction | Product/price tag with hidden future still visible. | R3, R5. | R1. | Use R1 as direct base; add correction labels and WIT in HyperFrames. | None. |
| 2. Real price receipt | Blank receipt/tag composition with room for fake line items. | R4. | R2. | Use R2 as direct base; use R4 only for receipt texture safety/reference. | None, as long as render does not expose real receipt numbers. |
| 3. Better question | Calm product/cardboard background and a large final tag. | R3, R5, R6. | R1 as callback, R7 fallback only. | Use R6 or CSS product/tag built from R3/R6; final text in HyperFrames. | Need screenshot QA to ensure final tag does not cover WIT face. |

## Image Generation Prompts

No new generated images were needed. Existing generated support bases already cover the required Section 8 compositions and were copied into the Section 8 reference folder.

### Optional Prompt 1

```text
Realistic 16:9 editorial product-photo reference for a YouTube explainer ending. A plain cardboard product box on a warm wooden table with one large blank cream paper tag tied to it, no readable text, no logos, no brand marks, no people, no private data. Calm final-frame mood, label-safe empty space on the left and center, room on the right for a large cartoon character overlay, natural light, clean composition.
```

Negative prompt:

```text
text, logos, brand marks, barcodes, shipping labels, hands, people, busy store aisle, watermark, distorted product, fake readable words
```

### Optional Prompt 2

```text
Realistic 16:9 overhead warm wooden tabletop with one blank yellow price tag, one long blank receipt, a small screw, and a pen, clean evidence-board composition, no text, no logos, no watermarks, no people, enough blank receipt space for later handwritten labels.
```

Negative prompt:

```text
text, numbers, logos, trademarks, readable receipt details, hands, people, clutter, watermark, brand marks
```

## Rejected References

- Fresh web image search: skipped after project-local browse failed startup and global gstack browse was not installed.
- Direct use of the real receipt source photo as visible receipt content: rejected because source numbers/text would distract and could create unnecessary authenticity risk.
- `missing-tomorrow-cutaway-generated.png` as a main Scene 3 base: rejected because it would make the payoff look too much like Section 2 instead of a calmer final question.
- `visible-shopping-promises-generated.png` from Section 3: rejected for Section 8 because it repeats the earlier tabletop/tag language without adding the final buying-question payoff.
