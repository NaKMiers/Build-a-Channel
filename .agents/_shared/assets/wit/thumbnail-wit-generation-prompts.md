# Thumbnail WIT Generation Prompts

Status: `prompt pack only`

Created: `2026-06-07`

Purpose:
generate the new WIT pose set from the WIT style in the five restored `Why Cheap Products Keep Getting Worse` thumbnail drafts.

Reference thumbnails:

```text
projects/why-cheap-products-keep-getting-worse/assets/thumbnails/variant-a-generated.png
projects/why-cheap-products-keep-getting-worse/assets/thumbnails/variant-b-generated.png
projects/why-cheap-products-keep-getting-worse/assets/thumbnails/variant-c-generated.png
projects/why-cheap-products-keep-getting-worse/assets/thumbnails/variant-d-generated.png
projects/why-cheap-products-keep-getting-worse/assets/thumbnails/variant-e-generated.png
```

## Master Identity Prompt

Use this first in ChatGPT with the five thumbnail images attached.

```text
I am creating a reusable character pose set for my no-face explainer YouTube channel, Why It Works.

Use the WIT character from the attached 5 thumbnail images as the exact identity reference.

Important: preserve the thumbnail WIT, not the old channel WIT.

WIT identity to preserve:
- simple white round-headed cartoon figure
- thick imperfect black outline
- oversized black rectangular/rounded glasses
- small black dot eyes
- expressive black eyebrows
- simple white body with no detailed clothes
- clean bold silhouette
- dry, suspicious, betrayed, panicked, confused, or defeated expressions
- hand-drawn explainer-thumbnail style
- high contrast, funny, simple, readable at small size

Do NOT add:
- black hair
- human skin tone
- white shirt
- tie or receipt tie
- pants or shoes
- detailed human clothes
- anime style
- 3D glossy mascot style
- cute baby mascot style
- brand logos
- background scenes
- readable text on the character

The goal is a reusable WIT pose library that matches the character from the thumbnails exactly.
Create transparent-background PNG-style character poses, centered, with enough margin for animation.
Each pose should show the full character or strong upper body when the pose needs close emotion.
Use simple props only when requested.
No captions, no labels, no watermark, no background.
```

## Batch Prompt 1 - Core Explainer Poses

```text
Using the attached thumbnail WIT as the exact character reference, create a clean pose sheet with 6 separate transparent-background WIT poses.

Preserve the same simple white round-headed character, thick black outline, oversized black glasses, dot eyes, expressive eyebrows, and simple white body from the thumbnails.

Do NOT use the old WIT with hair, shirt, tie, pants, or shoes.

Create these 6 poses:

1. Neutral front - calm, slightly deadpan, standing straight.
2. Talking front - one hand raised as if explaining, mouth slightly open.
3. Pointing left - pointing clearly to something on the left.
4. Pointing right - pointing clearly to something on the right.
5. Thinking - one hand on chin, skeptical eyebrows.
6. Deadpan side-eye - unimpressed expression, arms crossed or one hand on chin.

Style requirements:
- transparent background
- centered characters
- consistent WIT identity across all poses
- thick black hand-drawn outline
- simple white body
- readable expression at small size
- no text, no logo, no watermark
- no background scene
```

## Batch Prompt 2 - Confusion And Shock Poses

```text
Using the attached thumbnail WIT as the exact character reference, create a clean pose sheet with 6 separate transparent-background WIT poses.

Preserve the thumbnail WIT exactly: white round head, simple white body, oversized black glasses, dot eyes, thick imperfect black outline, expressive eyebrows.

Do NOT add hair, shirt, receipt tie, pants, shoes, skin tone, or detailed clothing.

Create these 6 poses:

1. Confused - scratching head, small question-mark feeling in the face but no text.
2. Shocked - wide eyes, open mouth, hands raised.
3. Suspicious - narrowed eyes behind glasses, leaning forward slightly.
4. Betrayed - sad eyebrows, one hand on chest, looking hurt.
5. Facepalm - one hand covering face, tired and disappointed.
6. Tiny defeated - smaller slumped pose, exhausted and beaten by the system.

Style requirements:
- transparent background
- centered characters
- consistent WIT identity across all poses
- strong readable emotion
- simple thumbnail-like linework
- no captions, no labels, no logo, no watermark
- no background scene
```

## Batch Prompt 3 - Money And Receipt Poses

```text
Using the attached thumbnail WIT as the exact character reference, create a clean pose sheet with 6 separate transparent-background WIT poses for money, hidden-cost, and receipt jokes.

Preserve the thumbnail WIT exactly: simple white round-headed character, thick black outline, oversized black glasses, dot eyes, expressive eyebrows, simple white body.

Do NOT use the old WIT design with hair, shirt, tie, pants, shoes, or human skin.

Create these 6 poses:

1. Money panic - holding a bill or card in each hand, panicked expression.
2. Receipt attacked - tangled in a long receipt, trapped and nervous.
3. Holding receipt evidence - holding up a long receipt like proof, suspicious expression.
4. Empty wallet - holding an empty wallet, defeated face.
5. Price tag suspicion - holding or staring at a price tag, skeptical eyebrows.
6. Hidden fee panic - small papers or receipts flying around, mouth open, worried eyes.

Prop rules:
- props must be generic
- no real brand logos
- no readable company names
- no dense tiny text

Style requirements:
- transparent background
- centered characters
- consistent WIT identity across all poses
- no captions, no labels, no watermark
- no background scene
```

## Batch Prompt 4 - Internet And Modern-Life Poses

```text
Using the attached thumbnail WIT as the exact character reference, create a clean pose sheet with 6 separate transparent-background WIT poses for internet, app, business, and modern-life explainer videos.

Preserve the thumbnail WIT exactly: simple white round head, thick imperfect black outline, oversized black glasses, dot eyes, expressive eyebrows, simple white body.

Do NOT add hair, shirt, tie, pants, shoes, human skin, or any old channel WIT details.

Create these 6 poses:

1. Holding phone panic - holding a generic phone, worried and overwhelmed.
2. Typing on laptop - focused but suspicious, simple generic laptop.
3. Running away - panicked run pose, glasses and body still readable.
4. Trapped by app screen - simple frame or popup shape around WIT, nervous expression.
5. Awkward celebration - small false victory, slightly nervous smile.
6. Sleeping burned out - slumped on desk or simple surface, tired and defeated.

Prop rules:
- generic devices only
- no app logos
- no readable brand names
- no complex UI text

Style requirements:
- transparent background
- centered characters
- consistent WIT identity across all poses
- strong silhouette
- no captions, no labels, no watermark
- no background scene
```

## Single-Pose Prompt Template

Use this when one pose needs to be regenerated.

```text
Using the attached thumbnail WIT as the exact character reference, create one transparent-background pose asset.

Pose requested:
[WRITE ONE POSE HERE]

Preserve the thumbnail WIT exactly:
- simple white round-headed cartoon figure
- thick imperfect black outline
- oversized black glasses
- small black dot eyes
- expressive black eyebrows
- simple white body
- dry funny explainer-thumbnail style

Do NOT add:
- hair
- skin tone
- shirt
- tie
- pants
- shoes
- detailed clothing
- anime style
- glossy 3D style
- background scene
- labels or captions
- logo or watermark

The pose must be centered, clean, readable at small size, and consistent with the WIT from the attached thumbnails.
```

## Recommended First Approved Set

After generation, approve only poses that clearly match the thumbnail WIT.

Suggested first reusable set:

```text
wit-pose-neutral-front.png
wit-pose-talking-front.png
wit-pose-pointing-left.png
wit-pose-pointing-right.png
wit-pose-thinking.png
wit-pose-deadpan-side-eye.png
wit-pose-confused.png
wit-pose-shocked.png
wit-pose-suspicious.png
wit-pose-betrayed.png
wit-pose-facepalm.png
wit-pose-tiny-defeated.png
wit-pose-money-panic.png
wit-pose-receipt-attacked.png
wit-pose-holding-receipt-evidence.png
wit-pose-empty-wallet.png
wit-pose-price-tag-suspicion.png
wit-pose-hidden-fee-panic.png
wit-pose-holding-phone-panic.png
wit-pose-typing-on-laptop.png
wit-pose-running-away.png
wit-pose-trapped-by-app-screen.png
wit-pose-awkward-celebration.png
wit-pose-sleeping-burned-out.png
```
