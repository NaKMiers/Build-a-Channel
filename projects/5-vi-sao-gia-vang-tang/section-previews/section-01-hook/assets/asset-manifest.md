# Asset Manifest - `5-vi-sao-gia-vang-tang`

Source: `visual-implement` · Section: `Section 1: Hook` · Date: `2026-06-28`

Image generation is done by the OWNER in **ChatGPT** (which has NO project context), so every prompt
below is written to be **fully self-contained**: art style, subject, composition, background,
transparency, and explicit "do NOT include" rules. Each generate prompt also lists exactly **which
reference image(s) to attach**. On-screen Vietnamese text is NOT baked into assets - it is added later
in `render`; assets are text-free isolated elements.

Mascot reference convention: for ANY mascot/pose asset, attach the **mascot neutral pose** as the
character reference so identity/proportions/line-weight stay consistent.

## Status summary (9/9 present)

| Filename | Type | Used in | Status |
|---|---|---|---|
| `gold-bar-on-table.jpg` | browse-real-photo | 1.1, 1.4 | ✅ done (CC0 Wikimedia) |
| `gold-shop-crowd.png` | generate (photoreal) | 1.2 | ✅ done (generated; faces away = no-face ✓) |
| `gold-price-chart-rising.png` | generate | 1.3 | ✅ done |
| `gold-glowing-brain.png` | generate | 1.4 | ✅ done |
| `doodle-scalpel.png` | generate | 1.5 | ✅ done |
| `pose_hugging_gold_bar_eyes_gold.png` | generate (NEW pose) | 1.3 | ✅ done (neutral-pose attached; WIT identity kept) |
| `pose_deadpan_unimpressed_half_lidded.png` | pose | 1.1, 1.5 | ✅ placeholder (copied from `analysis/vuive poses/` - TEST ONLY, redo with channel WIT before publish) |
| `pose_excited_giddy_fists_at_face.png` | pose | 1.2 | ✅ placeholder (Vui Vẻ - test only) |
| `pose_pondering_skeptical_hand_on_chin.png` | pose | 1.4 | ✅ placeholder (Vui Vẻ - test only) |

> Vui Vẻ poses are another creator's mascot - used here ONLY because this video is a skill test, not for
> YouTube. Re-create all 3 with the channel WIT (attach the WIT neutral pose) before any real publish.

## Generation prompts (self-contained for ChatGPT - record + regeneration recipe)

### `gold-shop-crowd.png`
**Attach:** none.
**Prompt:**
> A photorealistic image of the interior of a busy gold jewellery shop, shot from behind the customers
> so NO faces are visible (only backs of heads and shoulders). A crowd of shoppers leans over brightly
> lit glass display counters packed with gold necklaces and bracelets; warm golden lighting; a sense of
> a busy rush. Do NOT include any readable brand names, shop logos, or text of any kind. Do NOT show any
> recognizable face. Wide 16:9 horizontal composition suitable as a video background.

### `gold-price-chart-rising.png`
**Attach:** none.
**Prompt:**
> A clean, minimal finance line chart on a near-white background. A single bold RED line (with a thin
> gold highlight) jitters slightly as it climbs steeply from the bottom-left to a sharp PEAK on the
> upper-right, with a soft red gradient fill under the line. Faint light-gray grid. Do NOT include any
> text, numbers, axis labels, currency symbols, or logos. 16:9; leave clear space around the peak so a
> character can later be composited sitting on top of it.

### `gold-glowing-brain.png`
**Attach:** none (or attach a channel doodle for style if you have one).
**Prompt:**
> A single isolated element on a fully TRANSPARENT background. Flat 2D cartoon style with a thick,
> uniform black outline and flat color fills. A cartoon human brain colored glowing gold, with a few
> small gold sparkle/twinkle marks around it. No text, no background scene, just the one object.

### `doodle-scalpel.png`
**Attach:** none.
**Prompt:**
> A single isolated element on a fully TRANSPARENT background. Flat 2D cartoon style, thick black
> outline, simple flat fills. One small surgical scalpel (silver blade, handle). No text, no background.

### `pose_hugging_gold_bar_eyes_gold.png` (NEW pose)
**Attach:** the **mascot neutral pose** reference image (the white round-headed WIT with thick black
outline and oversized black glasses).
**Prompt:**
> Using the attached character as the EXACT reference for identity, proportions, line weight, and color,
> draw the SAME mascot in a new pose on a fully TRANSPARENT background, flat 2D cartoon, thick black
> outline. The mascot hugs a shiny gold bar tightly against its chest with both arms; its eyes (behind
> the glasses) are replaced with little glowing GOLD BAR shapes; a greedy, delighted open-mouth grin;
> small gold sparkles around the bar. Full upper body, no background scene, no text. Keep the glasses,
> head shape, and outline identical to the reference.

## Library pose placeholders (this test only)

Copied verbatim from `analysis/vuive poses/`:
`deadpan_unimpressed_half_lidded.png`, `excited_giddy_fists_at_face.png`,
`pondering_skeptical_hand_on_chin.png` → `assets/pose_*`. Before publishing any real video, regenerate
each with the channel WIT (attach the WIT neutral pose; prompt = "draw the attached mascot in a
<pose description> pose, transparent bg, flat 2D, thick black outline, full upper body, no text").

## Next Step

`render` Section 1: composite `gold-bar-on-table.jpg` + the generated assets + the poses into each
scene's layout from `04-visual-plan.md`. All 9 assets are present.
