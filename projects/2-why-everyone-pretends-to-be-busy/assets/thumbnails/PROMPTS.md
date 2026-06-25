# Thumbnail Prompts — Why Everyone Pretends To Be Busy

Status: `prompt only / image not generated` (Claude can't make images — generate these in ChatGPT/DALL·E)

Canonical scored packaging file: `../../03-packaging.md`

## How to use (read once)

1. **Attach the WIT reference image** to every prompt:
   `.agents/_shared/assets/wit/poses/wit-pose-neutral-front.png`
   The prompts tell ChatGPT to reuse that exact character and only change his pose/expression.
2. **For the two comparison variants (A and B)**, ALSO attach this approved comparison layout as a
   second reference image:
   `projects/1-why-cheap-products-keep-getting-worse/assets/thumbnails/variant-c-generated.png`
3. Ask for **16:9, 1280x720**.
4. Each block below is **self-contained** — paste ONE block per image. Negatives are folded in as
   "Do NOT include."
5. **Generate in this A/B order:** D → C → A → B → E. (D is the recommended winner; C is the
   motif anchor.)
6. Save outputs here as `variant-a-generated.png` … `variant-e-generated.png` (1280x720).
7. **Reject rule (off-model WIT):** if the character has hair, a shirt/tie, shoes, or any clothing
   detail, it's off-model — re-roll. Re-roll line to paste if WIT drifts:
   *"Keep the character EXACTLY like the attached reference image — white round head, thick black
   outline, oversized black glasses, no hair, no clothes, no shoes. Only change his pose and
   expression."*
8. Honesty line: the `99+` and packed calendars are illustrative, hooks are `?!` questions — do
   not turn them into a stated statistic or fake "ONLY TODAY" urgency, and use no real app logos.

---

## Variant D — Shock Face-Zoom (recommended winner) → `variant-d-generated.png`

```text
Use the cartoon character in the attached reference image as WIT — keep his exact art style and proportions (simple white round head, thick imperfect black outline, oversized black glasses, expressive eyebrows, small black dot eyes, simple white body, no hair, no clothes, no shoes); only change his pose and expression. Make a YouTube thumbnail, 16:9, 1280x720, bold flat 2D illustration, MAXIMUM drama, extreme close-up, very high contrast for mobile. WIT's head and shoulders fill most of the frame in a total meltdown: eyes bulging huge, jaw ripped wide open mid-scream, sweat spraying off his head, trembling, comic shock-burst lines radiating out, a hot red rage glow behind him. Right next to his face, ONE giant glowing red notification badge erupting with the number "99+", oversized, little red dots bursting off it, a thick red circle slammed around it. One big handwritten-style hook reading "99+?!" placed clear of his face, with a rough red double-underline. Bold flat colors, clean background. Do NOT include: any real app logo or recognizable real app UI, iOS/Android brand-styled badges, photorealism, tiny cluttered text, paragraphs, extra characters, hair/shirt/tie/shoes on WIT, any label covering his face or glasses, watermarks, or anything important in the bottom subtitle zone.
```

---

## Variant C — Calendar Cage Trap (motif anchor) → `variant-c-generated.png`

```text
Use the cartoon character in the attached reference image as WIT — keep his exact art style and proportions (simple white round head, thick imperfect black outline, oversized black glasses, expressive eyebrows, small black dot eyes, simple white body, no hair, no clothes, no shoes); only change his pose and expression. Make a YouTube thumbnail, 16:9, 1280x720, bold flat 2D illustration, MAXIMUM drama, high contrast for mobile, tight crop. WIT is trapped inside a cage whose bars are made of calendar day-columns and bent clock hands; both hands grip the bars and shake them. Red notification dots and small "URGENT" tags swarm his head like angry bees, with thick red circles and fat red arrows pointing at him. Behind the cage, faint and out of reach, one grey glowing folder labeled "REAL WORK". Crank WIT all the way up: bulging eyes, jaw ripped wide open mid-scream, sweat spraying, trembling, comic shock-burst lines, hot red rage glow behind him. WIT fills about one third to one half of the frame. One big handwritten-style hook reading "TRAPPED?!" placed clear of his face, rough red double-underline. Bold flat colors, clean background, strong silhouette. Do NOT include: real app logos or brand UI, photorealism, tiny cluttered text, paragraphs, extra characters, hair/shirt/tie/shoes on WIT, any label covering his face or glasses, watermarks, more than 1-2 words of text, or anything important in the bottom subtitle zone.
```

---

## Variant A — Comparison: Looking Busy vs Real Work → `variant-a-generated.png`

*(Also attach the comparison layout reference: `why-cheap-products-keep-getting-worse/assets/thumbnails/variant-c-generated.png`.)*

```text
Use the cartoon character in the attached WIT reference image as WIT — keep his exact art style and proportions (simple white round head, thick imperfect black outline, oversized black glasses, expressive eyebrows, small black dot eyes, simple white body, no hair, no clothes, no shoes); only change his pose and expression. Use the second attached image only as a LAYOUT reference for the split-screen comparison style. Make a YouTube thumbnail, 16:9, 1280x720, bold flat 2D illustration, MAXIMUM contrast for mobile, split into two halves by a rough hand-drawn vertical divider with a jagged red lightning crack down it. LEFT half, cool blue, small black angled corner tag "REAL WORK": one calm glowing lightbulb or single clean document with lots of empty space, quiet and ignored. RIGHT half, hot orange/red, small black angled corner tag "LOOK BUSY": a chaotic avalanche of overlapping red "URGENT" meeting blocks, red notification dots flying everywhere, frantic motion lines. A small WIT stands on the divider, jaw dropped in shock, little comic shock strokes around his head, looking at the busy side. One big red-and-white handwritten center hook reading "FAKE?!" with a rough red underline. Bold flat colors, clean halves, strong silhouettes. Do NOT include: real app logos, Gmail/Slack/Outlook/Teams branding, real screenshots, photorealism, tiny cluttered text, paragraphs, more than the two corner tags plus the one center hook, extra characters, hair/shirt/tie/shoes on WIT, watermarks, or anything important in the bottom subtitle zone.
```

---

## Variant B — Comparison: Full Day vs Nothing Done → `variant-b-generated.png`

*(Also attach the comparison layout reference: `why-cheap-products-keep-getting-worse/assets/thumbnails/variant-c-generated.png`.)*

```text
Use the cartoon character in the attached WIT reference image as WIT — keep his exact art style and proportions (simple white round head, thick imperfect black outline, oversized black glasses, expressive eyebrows, small black dot eyes, simple white body, no hair, no clothes, no shoes); only change his pose and expression. Use the second attached image only as a LAYOUT reference for the split-screen comparison style. Make a YouTube thumbnail, 16:9, 1280x720, bold flat 2D illustration, MAXIMUM contrast for mobile, split into two halves by a rough hand-drawn vertical divider. LEFT half, hot orange/red, small black angled corner tag "ALL DAY": a fully packed calendar wall, every slot a red back-to-back meeting block, stuffed and overwhelming. RIGHT half, cool blue/grey, small black angled corner tag "0 DONE": a nearly empty task board with a single column header "DONE" and nothing under it, plus one tiny wilting plant in the corner. A small WIT stands on the divider, eyes bulging, hands on his head in disbelief, little comic shock strokes. One big red-and-white handwritten center hook reading "HUH?!" with a rough red underline. Bold flat colors. Do NOT include: real logos or brand UI, photorealism, tiny text, paragraphs, extra characters, hair/shirt/tie/shoes on WIT, more than the two corner tags plus one center hook, watermarks, or anything important in the bottom subtitle zone.
```

---

## Variant E — Treadmill Metaphor → `variant-e-generated.png`

```text
Use the cartoon character in the attached reference image as WIT — keep his exact art style and proportions (simple white round head, thick imperfect black outline, oversized black glasses, expressive eyebrows, small black dot eyes, simple white body, no hair, no clothes, no shoes); only change his pose and expression. Make a YouTube thumbnail, 16:9, 1280x720, bold flat 2D illustration, MAXIMUM drama, high contrast for mobile. WIT sprints flat-out on a treadmill whose rolling belt is made of tearing calendar pages and day-blocks, going absolutely nowhere. Big motion lines, sweat spraying off him, eyes bulging, mouth open mid-gasp, hot red rage glow. Red "URGENT" tags and notification dots fly off the spinning belt. Just off the front edge of the treadmill, standing still and glowing, one clean golden trophy or folder labeled "REAL WORK" that he can never reach, with a fat red arrow pointing at how close-yet-unreachable it is. One big handwritten-style hook reading "NOWHERE?!" with a rough red underline. Bold flat colors, clean background. Do NOT include: real logos or brand UI, photorealism, tiny text, paragraphs, extra characters, hair/shirt/tie/shoes on WIT, words cluttering the belt, watermarks, or anything important in the bottom subtitle zone.
```
