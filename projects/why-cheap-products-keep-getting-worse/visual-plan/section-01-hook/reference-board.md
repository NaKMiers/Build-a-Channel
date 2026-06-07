# Section 1 Reference Board

## Reference Pass Status

- Status: `completed - real-image-first pass`
- Browsed references: `Pexels, Unsplash, Wikimedia Commons, plus source/license pages`
- Real images saved: `5 downloaded real-world photos plus 1 real-world contact sheet`
- Generated images: `4 support/mockup PNGs plus 1 generated contact sheet`
- Inspected local assets: `current WIT pose manifest`
- Prompt-only fallbacks: `0`
- Fallback reason: `project-local gstack browse failed to start and global gstack browse was not installed, so web search/source pages were used as the browsing fallback. Real images were downloaded only from sources with visible reuse terms or clear source pages.`

## Search / Browse Notes

- Project-local browse command attempted: `.agents/skills/browse/dist/browse.exe status`
- Result: `Server failed to start within 15s`
- Global fallback check: `$env:USERPROFILE\.Codex\skills\gstack\browse\dist\browse.exe`
- Result: `not installed`
- Real-image direction: use ordinary tags, receipts, and damaged chairs so the hook feels close to real viewer life instead of purely generated.
- Production decision: use real photos for texture, proof, material detail, and viewer closeness; use generated images only where the scene needs a clean generic chair setup, no readable text, no logos, or controlled blank spaces for HyperFrames overlays.

## References

| Ref | Type | Source | Classification | Why useful | Attention / editor use | Use in production | Saved path |
|---|---|---|---|---|---|---|---|
| Real-world reference contact sheet | Real web-image contact sheet | Created locally from downloaded real photos | `safe asset / internal reference` | One board shows the real texture standard: blank tag, tag-on-object, torn chair, broken chair, receipt. | Use as the editor overview before HyperFrames build. | Use as internal reference; crop individual assets when needed. | `assets/visual-references/section-01-hook/real-world/section-01-real-world-reference-contact-sheet.png` |
| Blank paper tag on dark textile | Real internet photo | Pexels, Miguel A. Padrinan, `White Tag With String and Black Background` | `safe asset` | Clean blank tag with real paper/string texture and large copy space. | Best real source for the hidden `FUTURE NOT INCLUDED` tag feeling. | Direct crop candidate; add all text in HyperFrames. | `assets/visual-references/section-01-hook/real-world/real-blank-tag-pexels-padrinan.jpg` |
| Tag hanging on object near chair | Real internet photo | Unsplash, Kelly Sikkema | `mockup target` | Real hanging tag composition near furniture-like shapes; feels like something in a room. | Use for how the tag should hang, swing, and catch attention. | Use as inspiration/mockup target; cover or avoid existing tag text if used. | `assets/visual-references/section-01-hook/real-world/real-tag-on-object-unsplash-kelly-sikkema.jpg` |
| Torn swivel chair close-up | Real internet photo | Wikimedia Commons, Almanta, CC BY-SA 4.0 | `inspiration only` | Shows real worn seat material, torn seams, tape, and lived-in damage. | Failure texture for the chair becoming nervous. | Do not use directly unless attribution/share-alike handling is accepted. | `assets/visual-references/section-01-hook/real-world/real-torn-swivel-chair-wikimedia.jpg` |
| Broken office chair outdoors | Real internet photo | Wikimedia Commons / Flickr, Alan Stanton, CC BY-SA 2.0 | `inspiration only` | A broken chair in a normal public space feels absurd and very real. | Reality check: broken cheap things look embarrassing, not cinematic. | Use as failure inspiration only; background is too noisy for hook boards. | `assets/visual-references/section-01-hook/real-world/real-broken-office-chair-cc-by-sa-2.jpg` |
| Real receipt close-up | Real internet photo | Pexels, Towfiqu barbhuiya | `mockup target` | Real receipt texture and shallow-focus cost detail. | Board 7 should feel like actual hidden cost evidence, not a fake spreadsheet. | Use direct crop only if readable numbers are covered/blurred; otherwise recreate. | `assets/visual-references/section-01-hook/real-world/real-receipt-pexels-towfiqu-barbhuiya.jpg` |
| Chair with blank yellow price tag | Generated support image | Image generation, saved locally | `safe asset` | Clean generic chair setup with no brands/logos/text. | Opening production base if the real references are too specific or noisy. | Use as controlled production texture, informed by real references. | `assets/visual-references/section-01-hook/generated/chair-price-tag-generated.png` |
| Hidden blank paper tag under chair | Generated support image | Image generation, saved locally | `safe asset` | Gives the exact under-chair reveal composition the real web photos do not provide. | Suspicion beat: viewer discovers the hidden future label. | Use as controlled production texture; add text in HyperFrames only. | `assets/visual-references/section-01-hook/generated/hidden-future-tag-generated.png` |
| Loose screw chair-leg detail | Generated support image | Image generation, saved locally | `safe asset` | Clean failure close-up, but should be dirtied visually using real torn-chair references. | Failure beat: red circle, wobble marks, WIT betrayal. | Use with real-damage texture/color guidance. | `assets/visual-references/section-01-hook/generated/wobbly-leg-loose-screw-generated.png` |
| Blank price tag and receipt table | Generated support image | Image generation, saved locally | `safe asset` | Safe blank receipt/tag layout for fake cost overlays. | Argument beat: price tag becomes true-cost receipt. | Use if real receipt text is too risky or distracting. | `assets/visual-references/section-01-hook/generated/price-tag-receipt-generated.png` |
| Current WIT pose set | Local reusable channel asset | `.agents/_shared/assets/wit/poses/manifest.json` | `safe asset` | Adds viewer emotion over the realistic image layer. | WIT is the buyer discovering the trap. | Use current WIT poses only. | `.agents/_shared/assets/wit/poses/` |

## Image Generation Prompts

Generated images are support assets only. They should follow the real web references above, stay free of logos/people/readable text, and leave clean overlay space for HyperFrames labels.

### Prompt 1 - Chair Price Tag

```text
Photorealistic 16:9 video reference image, warm editorial product-photo style like a high-quality YouTube explainer asset. A simple generic budget chair in a modest room, no brand logos, no people. A blank bright yellow price tag is tied to one chair leg, no readable text anywhere. Clean composition, natural window light, warm wood floor, realistic shadows, high contrast, slightly humorous but tasteful, space on the left for later handwritten label overlay. No watermark, no distorted furniture, no extra chairs, no words.
```

### Prompt 2 - Hidden Future Tag

```text
Photorealistic 16:9 macro editorial reference image for a YouTube explainer. Close-up under the seat of a simple generic chair, warm wood floor, natural soft light. A small blank cream paper tag is half-hidden under the chair seat and hanging down by a string, suggesting a secret label. No readable text, no logos, no people, no watermark. Clean composition with shallow depth of field, tasteful, realistic, slightly suspicious mood, enough empty space for later handwritten overlay.
```

### Prompt 3 - Loose Screw

```text
Photorealistic 16:9 close-up reference image for a no-face explainer hook. A simple generic chair leg joint on a warm wooden floor, one metal screw is loose and slightly out of place near the chair leg, the leg is subtly tilted as if the chair is wobbling. Natural window light, realistic shadows, clean composition, no people, no text, no logos, no watermark. Looks like a real product detail photo, tasteful and useful as a video asset reference, not cartoonish.
```

### Prompt 4 - Receipt / Real Cost

```text
Photorealistic 16:9 overhead reference image for a YouTube explainer. Warm wooden table, a blank yellow price tag, a long blank receipt, a small screw, and a simple pen arranged cleanly like evidence of hidden cost. No readable text, no logos, no brand names, no people, no watermark. Natural light, high-quality editorial desk photography, enough empty space for later handwritten labels and red arrows. Looks similar in quality to a polished real-world reference board, not cartoonish.
```

Shared negative prompt:

```text
brand logos, store names, real product labels, copyrighted character styles, copied creator frames, real screenshots, private data, crowded background, unreadable generated text, weird hands, people, watermark, distorted furniture
```

## Rejected References

- Previous generated contact sheet and SVG references were rejected because they looked crude, diagram-like, and below the accepted busy-video visual quality bar.
- Real store screenshots and product listing screenshots are rejected because they add brand/UI/copyright risk and can imply a real accusation.
- Real web photos with unclear source, visible private data, or heavy logos should be `inspiration only` or `reject`, not direct production assets.
- Generated text is not production text. All labels must be added in HyperFrames.
