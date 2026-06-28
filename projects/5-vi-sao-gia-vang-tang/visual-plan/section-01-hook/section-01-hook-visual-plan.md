# Section 1 Visual Plan - Hook: "the metal that does nothing"

Video: `Vì sao giá vàng tăng điên cuồng?` (Vietnamese-language experiment)
Section: `Section 1: Hook`
Status: `draft visual plan for approval`
Timing basis: `estimated` (no word-timings file; proportional to the 29.35s section audio)

> Language note: this plan is written in English per the File Language Convention. The only Vietnamese
> is the quoted narration lines and the `On-screen text` VALUES (both are in-video content).

## Video-Level Direction (keep identical to master)

- Audience: Vietnamese-native entertainment explainer (Vui Vẻ / Threads-City style); NOT English-learner.
- Renderer: HyperFrames (composited from pre-made isolated assets via `visual-implement`).
- Visual grammar: real / real-looking photo base + mascot drawn on top; **new scene ~every sentence**; vary everything.
- Mascot: WIT (white round head, thick black outline, oversized black glasses), BIG & HIGH, the soul of each scene.
- On-screen tone: deadpan + cheeky at FOMO / the viewer's own wallet; never mock people who buy gold; no investment advice.
- Recurring motif: a gold bar = a fear barometer; "gold earns you nothing".

## Section Overview

- Goal: open on a curiosity gap - gold is useless, yet everyone rushes to buy it at its most expensive.
- Duration: ~29.35s
- Scenes: 5 (per-sentence)
- Scene-type rotation: object-hero → wide-frenzy → chart+mascot → question/close-up → mascot-only focus
- Mascot arc: deadpan mockery → swept into the crowd → FOMO hugging gold → confused → deadpan "let's dissect it"

## Scenes

### Scene 1.1 - narration: "Vàng không trả lãi. Không trả cổ tức. Không nhắn tin chúc bạn ngủ ngon."

- **Local time:** `0:00–0:07` (estimated)
- **Role:** opening line = the "gold is useless" running gag; sets the deadpan tone at second 0.
- **Composition / layout:** white background, thin gray horizon line at ~88%. Left-center (10–55%): a lone gold bar on a clean surface, floating with a soft drop shadow - sitting there "doing nothing". Right (62–100%, cropped at hip): mascot turned left, palm out presenting the bar. Three struck-through "feature" labels stacked upper-middle, appearing one per beat.
- **Elements:**
  - *Left:* `gold-bar-on-table.jpg` - one real gold bar on a clean surface; no logo, no people.
  - *Right:* mascot, deadpan, palm up ("here it is").
- **Mascot:** `pose_deadpan_unimpressed_half_lidded` (half-lidded eyes, flat mouth); right side, ~1/3 frame, cropped at hip, looking toward the bar.
- **On-screen text (handwritten, red strike-through, one per beat):** `"không trả lãi"` → `"không trả cổ tức"` → `"không nhắn tin chúc ngủ ngon"`.
- **Emotion:** dry mockery - "this thing is useless".
- **Insight/joke:** listing what gold does NOT do - funny because it's true.
- **Linkage / eye path:** eye lands on the shiny bar (gold on white) → deadpan mascot on the right confirms "yeah, useless".
- **Show-as-you-say:** beat 1 → label 1 (hard-show); beat 2 → label 2; beat 3 → label 3 (slight impact pop on the last for comedy).
- **Sound:** a soft "tick" per label; a held silence after label 3 (deadpan).
- **Color / contrast:** gold + red labels on white; bright mascot balances the right.

**Assets:**

| Filename | Type | Description (no prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `gold-bar-on-table.jpg` | browse-real-photo | one real gold bar on a clean surface, no logo/no people | left-center 10–55%, float + shadow | new |
| `pose_deadpan_unimpressed_half_lidded.png` | pose | mascot deadpan, palm out presenting | right, ~1/3 frame, cropped at hip | reuse (library) |

### Scene 1.2 - narration: "Vậy mà cứ vài tháng, cả nước lại lao đi mua nó như sắp hết hàng."

- **Local time:** `0:07–0:12` (estimated)
- **Role:** the contrast flip - useless, yet the whole country rushes to buy.
- **Composition / layout:** full-frame real-looking photo of a crowded gold shop (faces turned away, no-face). Mascot rises from the bottom-center, getting "swept" into the crowd, eyes shining.
- **Elements:**
  - *Background:* `gold-shop-crowd.png` - busy gold shop, shoppers seen from behind (no faces).
  - *Mascot:* rushing in, giddy.
- **Mascot:** `pose_excited_giddy_fists_at_face` (both fists at face, eyes squeezed happy); bottom-center, ~1/2 frame, cropped at chest.
- **On-screen text:** handwritten `"cả nước lao đi mua"` + a crowd arrow; small tag `"sắp hết hàng?!"`.
- **Emotion:** contagious frenzy, slightly absurd.
- **Insight/joke:** the thing just called useless → everyone fights to buy it.
- **Linkage:** the crowd background pushes the eye to the mascot being swept along → "wait, I'm about to join too".
- **Show-as-you-say:** "lao đi mua" → mascot pops in + arrow; "như sắp hết hàng" → `"sắp hết hàng?!"` impact.
- **Sound:** faint crowd murmur, then duck.
- **Color / contrast:** warm/busy background; bright mascot pops in the center.

**Assets:**

| Filename | Type | Description (no prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `gold-shop-crowd.png` | generate (photoreal) | busy gold shop, shoppers from behind, no faces, no brand | full-frame background | new |
| `pose_excited_giddy_fists_at_face.png` | pose | mascot giddy, rushing in | bottom-center, ~1/2 frame | reuse (library) |

### Scene 1.3 - narration: "…'nơi trú ẩn an toàn' - rồi giành nhau mua đúng lúc nó đắt nhất."

- **Local time:** `0:12–0:21` (estimated)
- **Role:** state the core paradox - "safe" yet everyone buys at the peak.
- **Composition / layout:** background is a red gold-price line chart climbing to a peak. On the chart's PEAK, the mascot hugs a gold bar with gold-bar eyes. An ironic `"an toàn?"` label points at the exact peak (most expensive).
- **Elements:**
  - *Background:* `gold-price-chart-rising.png` - red line climbing to a peak (real-looking; no brand/text).
  - *Mascot:* perched on the peak, hugging gold, full FOMO.
- **Mascot:** **NEW pose** `pose_hugging_gold_bar_eyes_gold` - hugging a gold bar to its chest, eyes turned into gold-bar shapes, greedy grin; ~1/2 frame, sitting on the chart's peak.
- **On-screen text:** `"nơi trú ẩn an toàn"` (in quotes) appears, then a red scrawl `"an toàn?"` + an arrow into the PEAK.
- **Emotion:** irony - "safe" yet buying at the top.
- **Insight/joke:** visual pun - climb all the way to the peak (most expensive) to feel "safe".
- **Linkage:** eye follows the rising line up → hits the mascot hugging gold at the peak → the "an toàn?" label mocks it.
- **Show-as-you-say:** "nơi trú ẩn an toàn" → quoted label hard-show; "đúng lúc đắt nhất" → mascot pops onto the peak + "an toàn?" impact.
- **Sound:** a metallic "ting" as the mascot grabs the gold.
- **Color / contrast:** red rising line on a light field; gold + gold eyes are the focal point at the peak.

**Assets:**

| Filename | Type | Description (no prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `gold-price-chart-rising.png` | generate | red gold-price line climbing to a peak, no brand/text | full-frame background | new |
| `pose_hugging_gold_bar_eyes_gold.png` | generate (**NEW pose** - not in the library) | mascot hugging a gold bar, gold-bar eyes, greedy grin | on the chart peak, ~1/2 frame | new |

### Scene 1.4 - narration: "Vì sao một cục kim loại chẳng làm gì cả lại tăng giá điên cuồng? Và vì sao não bạn cứ muốn mua thêm khi giá càng cao?"

- **Local time:** `0:21–0:27` (estimated)
- **Role:** pose the two core questions of the video (open the curiosity loop).
- **Composition / layout:** mascot CENTER, confused; left = the gold bar (reused) wearing a big `?`; for the second question, a small gold-glowing brain appears by the mascot's head. Two questions appear in turn on each side.
- **Elements:**
  - *Left:* `gold-bar-on-table.jpg` **(REUSED from Scene 1.1)** + a large `?`.
  - *Right:* `gold-glowing-brain.png` doodle by the head.
- **Mascot:** `pose_pondering_skeptical_hand_on_chin` (hand on chin, raised brow); center, ~1/3–1/2 frame.
- **On-screen text:** question 1 `"cục kim loại chẳng làm gì… mà tăng điên cuồng?"` (left); question 2 `"sao não cứ đòi mua khi càng đắt?"` (right).
- **Emotion:** puzzled curiosity (pull the viewer in).
- **Insight/joke:** lay out the double paradox: a dumb object + the human brain.
- **Linkage:** mascot in the center = the viewer; the two questions on each side = the two mysteries to solve.
- **Show-as-you-say:** question 1 ↔ line 1 (gold bar + "?"); question 2 ↔ line 2 (gold brain lights up).
- **Sound:** "?" bounces in; a "ping" as the brain lights up.
- **Color / contrast:** clean background; gold + gold glow from the brain.

**Assets:**

| Filename | Type | Description (no prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `gold-bar-on-table.jpg` | reuse | the gold bar (same as Scene 1.1) | left, wearing a `?` | **reuse (Scene 1.1)** |
| `gold-glowing-brain.png` | generate | small gold-glowing brain doodle (no text) | by the mascot's head, right | new |
| `pose_pondering_skeptical_hand_on_chin.png` | pose | mascot hand on chin, puzzled | center, ~1/3–1/2 frame | reuse (library) |

### Scene 1.5 - narration: "Bình tĩnh. Hôm nay mình mổ xẻ."

- **Local time:** `0:27–0:29.4` (estimated)
- **Role:** mascot-only focus beat - close the hook, invite the viewer to stay.
- **Composition / layout:** nearly empty frame, mascot CENTER (focus beat), clean background; a small title card below: `Vì sao giá vàng tăng điên cuồng?`.
- **Elements:** only the mascot + a title card; no evidence object (let the eye rest, the ear catch the line).
- **Mascot:** `pose_deadpan_unimpressed_half_lidded` (deadpan, slight smirk); center, ~1/2 frame.
- **On-screen text:** title `"Vì sao giá vàng tăng điên cuồng?"` + a small `"mổ xẻ"` tag (optional tiny scalpel doodle on a gold bar).
- **Emotion:** confident deadpan - "sit tight, I'll explain".
- **Insight/joke:** "mổ xẻ" (dissect) - turning a dry economics topic into a comic surgery.
- **Linkage:** empty space + centered mascot = "listen to this"; hands off to the explanation.
- **Show-as-you-say:** "Bình tĩnh" → mascot hard-show center; "mình mổ xẻ" → title card + scalpel doodle.
- **Sound:** brief silence, then a soft closing note.
- **Color / contrast:** clean background, mascot is the sole focal point.

**Assets:**

| Filename | Type | Description (no prompt) | Layout / position | Reuse? |
|---|---|---|---|---|
| `pose_deadpan_unimpressed_half_lidded.png` | reuse | mascot deadpan (same as Scene 1.1) | center, ~1/2 frame | **reuse (Scene 1.1)** |
| `doodle-scalpel.png` | generate | tiny surgical scalpel (no text) | on the gold bar (optional) | new |

## Section Asset Summary

| Filename | Type | First scene | Reused in | Notes |
|---|---|---|---|---|
| `gold-bar-on-table.jpg` | browse-real-photo | 1.1 | 1.4 | main gold bar; one file reused |
| `gold-shop-crowd.png` | generate (photoreal) | 1.2 | - | no-face crowd |
| `gold-price-chart-rising.png` | generate | 1.3 | - | red rising line |
| `gold-glowing-brain.png` | generate | 1.4 | - | gold brain doodle |
| `doodle-scalpel.png` | generate | 1.5 | - | scalpel doodle |
| `pose_deadpan_unimpressed_half_lidded.png` | pose | 1.1 | 1.5 | library (Vui Vẻ placeholder for this test) |
| `pose_excited_giddy_fists_at_face.png` | pose | 1.2 | - | library (Vui Vẻ placeholder) |
| `pose_hugging_gold_bar_eyes_gold.png` | generate | 1.3 | - | **NEW pose** (on-model via attached WIT neutral pose) |
| `pose_pondering_skeptical_hand_on_chin.png` | pose | 1.4 | - | library (Vui Vẻ placeholder) |

## Approval Checks

- each scene picturable from text alone: ✔ (5 per-sentence scenes, rotated scene-types)
- every scene has a real/real-looking base (no bare gradient): ✔
- mascot has a specific pose + expression per scene, big & high: ✔
- show-as-you-say timeline per scene: ✔ (timing `estimated` - no word-timings)
- every asset has type + description + filename + layout: ✔; NO prompts here (prompts live in `visual-implement`): ✔
- repeated subjects reuse the same filename (`gold-bar-on-table`, `pose_deadpan_…`): ✔
- demonstrates an invented NEW pose (`pose_hugging_gold_bar_eyes_gold`): ✔
- public figures: none (safe): ✔
- in sync with master `04-visual-plan.md`: ✔
- file written in English per convention (VN only in narration quotes + on-screen values): ✔

## Next Step

`render` Section 1: composite `gold-bar-on-table.jpg` + the generated assets + the poses per each
scene's layout. All 9 assets are present in `assets/`.
