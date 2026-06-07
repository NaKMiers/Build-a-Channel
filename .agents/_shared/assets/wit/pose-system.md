# WIT Pose System

Status: `draft replacement generated - awaiting user review`

Purpose:
define the intended reusable pose system after the new WIT direction is generated.

## Current State

There is currently a draft WIT pose set:

```text
.agents/_shared/assets/wit/poses/thumbnail-wit-24/
```

Contact sheet:

```text
.agents/_shared/assets/wit/poses/thumbnail-wit-24/thumbnail-wit-24-contact-sheet.png
```

The previous current pose set `original-wit-24` was removed on `2026-06-07`.

Do not use the removed old character as the default WIT.

## Replacement Source

The next WIT pose set should be based on the WIT character visible in the restored `Why Cheap Products Keep Getting Worse` thumbnail drafts:

```text
projects/why-cheap-products-keep-getting-worse/assets/thumbnails/
```

Target visual identity:

- simple white round-headed cartoon figure
- thick imperfect black outline
- oversized black glasses
- expressive eyebrows
- small dot eyes
- simple white body
- strong suspicious, betrayed, panicked, trapped, confused, and defeated expressions

## Future Pose Batch

Draft pose set generated:

1. `wit-pose-neutral-front.png`
2. `wit-pose-talking-front.png`
3. `wit-pose-pointing-left.png`
4. `wit-pose-pointing-right.png`
5. `wit-pose-confused.png`
6. `wit-pose-shocked.png`
7. `wit-pose-deadpan.png`
8. `wit-pose-thinking.png`
9. `wit-pose-holding-phone.png`
10. `wit-pose-holding-receipt.png`
11. `wit-pose-money-panic.png`
12. `wit-pose-tiny-defeated.png`

Do not generate this set until the user asks for step `3`.

## Asset Requirements

Each future pose should have:

- transparent background
- consistent character proportions
- consistent glasses, outline, head shape, body style, and expression language
- clean silhouette readable at small size
- no readable text baked into the character
- no logo, watermark, or background scene
- enough empty margin to avoid clipping during bounce/shake animation

Preferred export:

- `2048x2048 PNG`
- transparent background
- character centered
