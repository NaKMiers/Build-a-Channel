---
name: packaging
description: Create or update YouTube packaging for a Why It Works video project. Use when the user asks for Packaging, title and thumbnail, YouTube description, upload metadata, tags, hashtags, thumbnail concepts, thumbnail images, A/B thumbnail testing, A/B title testing, or packaging; this is the packaging step that runs after caption and requires completed 00-topic-intake.md, 01-research-pack.md, and 02-script.md (it does not require voiceover/render to be finished, but its recommended position is after caption so it can also package shorts and use real chapters). Produces 5 LOCKED title+thumbnail A/B pairs for the main video (title N is coupled to thumbnail N — editing one rewrites the other), plus the YouTube description and tags; when built shorts are available it also creates one title, description, and thumbnail per short. Writes everything to ONE file, projects/<slug>/output/packaging.md (titles, descriptions, AND the thumbnail generation prompts folded in), and saves all thumbnail images under projects/<slug>/output/thumbnails/. It no longer creates 03-packaging.md or a separate PROMPTS.md.
---

# Packaging

## Purpose

Run the `packaging` step of the `Why It Works` video workflow. Its position is **after `caption`** (so the video is finished and any shorts already exist), and it hard-requires `00-topic-intake.md`, `01-research-pack.md`, and `02-script.md`.

Turn a finished project into a strong YouTube package, written to ONE file (`output/packaging.md`):

- `5` **locked title+thumbnail A/B pairs** for the main video — title `N` is coupled to thumbnail `N`, so A/B title testing runs alongside A/B thumbnail testing as one unit
- a reusable generation prompt for each of the `5` thumbnails, **folded into `output/packaging.md`** (no separate `PROMPTS.md`)
- a thumbnail comparison and score table
- the YouTube description, tags, hashtags, links, chapters, and pinned comment idea for the main video
- when built shorts are available: one title, one description, and one thumbnail for **each** short

Everything lands in `projects/<slug>/output/packaging.md`; thumbnail images go under `projects/<slug>/output/thumbnails/`. This skill no longer creates `03-packaging.md` or a separate `PROMPTS.md`.

## Pipeline Position

Packaging runs **after `caption`**, near the end of the workflow:

```text
... -> combine -> caption -> packaging -> upload -> learning
                     \-> shorts (side sub-workflow; if built, packaging includes them)
```

Hard-required previous outputs (the skill refuses without these three):

- `projects/<slug>/00-topic-intake.md`
- `projects/<slug>/01-research-pack.md`
- `projects/<slug>/02-script.md`

Recommended position is after `caption` so the finished video, real chapter timing, and any built shorts are available — but the only hard gate is the three files above. When the combined video / captions exist, use them for real chapters; otherwise estimate chapters from `02-script.md` and mark them `draft until aligned`.

Write or update (only these):

- `projects/<slug>/output/packaging.md` — the SINGLE deliverable: the `5` locked title+thumbnail pairs, the thumbnail generation prompts (folded in), the description/tags/hashtags/chapters/pinned comment, and one title+description+thumbnail per short when shorts exist
- `projects/<slug>/output/thumbnails/` — the thumbnail images (`main-pair-1.png` … `main-pair-5.png`, and `short-0N.png` when shorts exist)

Do **not** create `03-packaging.md` or a separate `PROMPTS.md` anymore, and do not write under `assets/thumbnails/`. If an older project already has `03-packaging.md` or `assets/thumbnails/` from before this change, leave them in place as-is unless the user explicitly asks to remove or migrate them — write all new output to `output/`.

If `00-topic-intake.md`, `01-research-pack.md`, or `02-script.md` is missing, stop and tell the user to run the missing previous skill in order before `packaging`.

If `01-research-pack.md` is older than `00-topic-intake.md`, or `02-script.md` is older than `01-research-pack.md`, treat the upstream as stale and stop. Tell the user to rerun the stale step.

If `output/packaging.md` exists but any required upstream file has a newer modified time, treat packaging as stale and use Update Mode when the user asks for packaging.

When this skill creates, updates, or reruns `output/packaging.md` or thumbnail images, the only downstream steps are `upload` and `learning`; do not mark earlier production outputs stale. Do not delete or regenerate other files unless the user explicitly asks.

## Required Context

Read these before creating or updating packaging:

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/rules/video-workflow.md`
4. `.agents/_shared/channel/current-state.md`
5. `.agents/_shared/channel/channel-foundation.md`
6. `.agents/_shared/channel/channel-guardrails.md`
7. `.agents/_shared/channel/reference-channels.md`
8. `.agents/_shared/channel/learning-log.md`
9. `.agents/_shared/channel/codex-collaboration.md`
10. `.agents/_shared/channel/production-workflow.md`
11. `.agents/_shared/channel/brand-system.md`
12. `.agents/_shared/systems/topic-packaging-hooks.md`
13. `.agents/_shared/systems/script-learner-voice.md`
14. `references/memory.md`
15. the chosen project files (all three required):
    - `projects/<slug>/00-topic-intake.md`
    - `projects/<slug>/01-research-pack.md`
    - `projects/<slug>/02-script.md`

Load additional shared systems only when needed:

- `.agents/_shared/systems/visual-production.md` when planning real or real-looking thumbnail assets or reference-board support
- `.agents/_shared/systems/youtube-publishing-growth.md` when shaping titles, descriptions, hashtag count, or A/B-testing guidance
- `.agents/_shared/assets/wit/poses/` when current WIT pose assets are needed
- the finished video and `output/captions/` when present, to align real chapter timestamps.

### Detect shorts availability

Before writing, check whether the project has **built shorts**:

- shorts are available if `projects/<slug>/shorts/shorts-plan.md` exists OR `projects/<slug>/output/shorts/*.mp4` exists
- if shorts are available, read `projects/<slug>/shorts/shorts-plan.md` (and `02-script.md` for the source-section wording) so each short's title, description, and thumbnail match its real content and source section
- if no built shorts exist, package the main video only — do not invent shorts

This is the switch for the Shorts Packaging section below.

## Project Selection Gate

Always resolve the target project before writing packaging.

Use this order:

1. If the user names a project slug or path, use that project.
2. If the current chat clearly selected a project and the folder exists, use that project.
3. If there is exactly one project with completed `00-topic-intake.md`, `01-research-pack.md`, and `02-script.md` but no completed `output/packaging.md`, smart-select it and say so.
4. Otherwise scan `projects/`, excluding `_template`, and find unfinished packaging candidates.

A packaging candidate is usually:

- a folder with non-empty `00-topic-intake.md`, `01-research-pack.md`, and `02-script.md`
- and no `output/packaging.md`, or an empty/stub `output/packaging.md`
- and not obviously blocked by stale upstream files

(A legacy `03-packaging.md` from before the relocation does not count as a completed package; the current deliverable is `output/packaging.md`.)

When multiple candidates exist or context is unclear, ask the user to choose before writing.

Do not create a new project folder in this skill. New projects come from `topic-intake`.

## Required Inputs Gate

Before writing packaging, verify the chosen project has:

- non-empty `00-topic-intake.md`
- non-empty `01-research-pack.md`
- non-empty `02-script.md`

If any are missing, stop and name the missing skill:

- missing `00-topic-intake.md` -> run `topic-intake`
- missing `01-research-pack.md` -> run `research-pack`
- missing `02-script.md` -> run `script-draft`

Do not create placeholder upstream files.

## Request Modes

### Create Mode

Use when the chosen project has no usable `output/packaging.md`.

Write:

```text
projects/<slug>/output/packaging.md
```

### Update Mode

Use when the user asks to improve, rewrite, score, refresh, or choose a different title, thumbnail, description, tags, hashtags, or links.

Read the existing `output/packaging.md`, preserve useful approved decisions, and update only the necessary sections unless the whole package is clearly affected.

### Paired Title + Thumbnail A/B Mode

Use on every Create Mode and Update Mode run unless the user explicitly says not to generate thumbnails.

Create or update:

```text
projects/<slug>/output/thumbnails/
```

Generate exactly `5` **locked title+thumbnail A/B pairs** for the main video. Each pair is one A/B test unit: thumbnail variant `N` always ships with title `N`. A/B title testing and A/B thumbnail testing run together — you never test a title against a thumbnail it was not paired with.

Each of the `5` pairs must have:

- pair number (`1`-`5`) — this is the stable key that binds the title and the thumbnail
- the paired **title** (the click promise in words; names the hidden logic)
- variant name + style direction (the thumbnail)
- image path under `output/thumbnails/` or generation status
- reusable generation prompt
- negative prompt / avoid list
- dominant object
- thumbnail label (`1-3` words; should NOT repeat the paired title's words)
- WIT emotion
- visual contradiction
- score (score the pair as a whole: does this title earn the click that this thumbnail promises?)
- strength
- risk
- decision (`Winner` / `A/B #2` / etc.)

Name the `5` thumbnail image files by pair number so the binding is obvious on disk: `main-pair-1.png` … `main-pair-5.png` (a `variant-a … variant-e` alias is fine in the table, but the pair number is canonical).

Before generating thumbnail images, use the research pack's real visual/reference leads when available. Real objects and real internet-image references should define the thumbnail's material, lighting, prop choice, and viewer closeness.

Use image generation when an image generation tool is available to create controlled, brand-safe thumbnail outputs. Save generated thumbnails or returned image references under `output/thumbnails/` when the environment supports saving them.

Generated thumbnail images should be treated as controlled outputs informed by real references, not replacements for doing the real-reference thinking.

If image generation is unavailable, still create the `5` production-ready prompts and mark each image status as `prompt only / image not generated`. Do not pretend images were created.

Write the prompts as a `## Thumbnail Prompts` section INSIDE `projects/<slug>/output/packaging.md` (there is no separate `PROMPTS.md`). Optimize them for the user generating images in ChatGPT / DALL·E. Label each prompt block by its pair number (`Pair 1` … `Pair 5`) and include the paired title at the top of the block, so the user always generates a thumbnail next to the title it ships with:

- each variant is a SELF-CONTAINED block the user can paste alone (no cross-references needed to generate)
- ChatGPT/DALL·E has no separate negative-prompt field, so fold the avoid-list INTO the prompt as `Do NOT include: ...`
- assume the user attaches the WIT neutral pose (`.agents/_shared/assets/wit/poses/wit-pose-neutral-front.png`) as the reference image; open each prompt with "use the cartoon character in the attached reference image as WIT — keep his art style, only change his pose/expression"
- for the two comparison variants, tell the user to ALSO attach an approved comparison thumbnail (e.g. `projects/1-why-cheap-products-keep-getting-worse/output/thumbnails/main-pair-2.png`) as a layout reference
- include a short how-to (attach images, ask for 16:9 1280x720, re-roll line if WIT drifts) and the A/B generate-first order
- name each output file by pair number (`main-pair-1.png` … `main-pair-5.png`) and the reject rule (no hair / shirt-tie / shoes = off-model WIT)

The prompts should also be reusable in another AI image platform if the user dislikes the generated thumbnails.

Every thumbnail prompt must include the channel WIT identity block from `WIT Prompt Requirements`.
If image generation produces an off-model WIT, mark that thumbnail as failed or concept-only and write a corrected prompt.

### Improve Memory Mode

Use when the user reviews packaging and gives reusable lessons.

Update in this order:

1. the project `output/packaging.md` if the review affects this video
2. this skill's `references/memory.md`
3. shared memory only if the lesson improves packaging across the whole channel

## Title-Thumbnail Coupling (locked pairs)

The `5` main-video A/B units are **locked pairs**. The title and the thumbnail in a pair are one test, identified by the pair number.

Coupling rule, both directions:

- When the user asks to update **thumbnail prompt N**, also rewrite **title N** so the pair still tells one coherent click story (the thumbnail shows the weird situation, the title names the hidden logic, and they do not repeat each other's words).
- When the user asks to update **title N**, also rewrite **thumbnail prompt N** (and regenerate that image when image generation is available) so the thumbnail still pays off the new title.
- Never edit one side of a pair and leave the other stale. If only one side truly needs to change, restate the other side and confirm it still fits in the chat response.
- Keep the pair number stable across edits; do not renumber pairs when updating one of them.
- Pairs are independent of each other: editing pair `2` must not touch pairs `1`, `3`, `4`, or `5`.

In every place the package is recorded (`output/packaging.md` and the chat response), keep the title and thumbnail of a pair physically together under their shared pair number so the binding is never ambiguous.

## Shorts Packaging (conditional)

Only run this when **built shorts are available** (see Detect shorts availability). If no built shorts exist, package the main video only and skip this section.

When shorts are available, also create, for **each** short:

- one **title** (short, punchy, learner-clean; a complete standalone short, never a "watch the full video" tease)
- one **description** (1-3 lines reinforcing the short's single idea + up to `3` meaningful hashtags; no CTA to the long video, matching the channel's standalone-short rule)
- one **thumbnail** for the short's grid/cover: a `1080x1920` portrait prompt that reuses the short's source-section real photos + WIT pose + the short's own payoff/hook beat, saved (or prompt-only) under `output/thumbnails/` as `short-0N.png`, with its prompt added to the `## Thumbnail Prompts` section of `output/packaging.md`

Shorts use **one** title + description + thumbnail each — not the `5`-way locked A/B pairs (that test is for the main video only). Pull each short's wording and source section from `shorts/shorts-plan.md` and `02-script.md` so the packaging matches what was actually built. Never edit the shorts themselves from this skill.

## Packaging Rules

Use the channel rule:

```text
The thumbnail shows the weird situation. The title names the hidden logic.
```

Create a package that feels like `Why It Works`:

- simple English
- dry funny framing
- one clear contradiction
- one dominant object
- one WIT emotion
- one short thumbnail label
- no direct product promotion
- no copied creator thumbnail
- no fake claim or rage bait

Titles should be clear enough for intermediate English learners and specific enough to feel like a system explanation.

Thumbnail concepts should use:

- `1280 x 720`
- one dominant object
- real object/material texture from research references when available
- one visual contradiction
- WIT as viewer emotion, not presenter
- the current approved or pending channel WIT direction, not an accidental unrelated character
- `1-3` words of thumbnail text
- readable mobile composition

## WIT Prompt Requirements

Use the current channel WIT direction from `.agents/_shared/channel/brand-system.md`.

As of `2026-06-07`, the old `original-wit-24` pose set has been removed and the current draft WIT pose set lives in `.agents/_shared/assets/wit/poses/`.
Until the user approves it as final, thumbnail prompts should follow the draft thumbnail-WIT style from the restored `Why Cheap Products Keep Getting Worse` thumbnail direction.

Every thumbnail image prompt must include a WIT block like this, adapted only for pose and emotion:

```text
Use the channel character WIT in the approved thumbnail style: a simple white round-headed cartoon figure with thick imperfect black outline, oversized black glasses, expressive eyebrows, small black dot eyes, simple white body, clean bold silhouette, and dry suspicious / betrayed / panicked expression. WIT should match the character style from the five restored `Why Cheap Products Keep Getting Worse` thumbnails.
```

For thumbnail prompts, add one clear WIT emotion:

```text
WIT emotion: suspicious / betrayed / trapped / panicked / confused / defeated.
```

Do not use removed `original-wit-24` details such as messy black hair, white shirt, receipt tie, dark pants, or oversized shoes as the current channel WIT.

Generated thumbnails should be scored down or rejected if WIT does not match the approved thumbnail-WIT style for the current video.

The `5` generated thumbnail variants use a FIXED structure — two comparison thumbnails plus three full-drama single scenes — while staying inside the channel identity:

1. `Comparison A` (split-screen): the core before/after of the video's thesis (e.g. `OWN` vs `RENT`, `REAL` vs `FAKE`, `THEN` vs `NOW`). Same object two ways.
2. `Comparison B` (split-screen): a second contrast on a different beat (e.g. time-based `DAY 1` vs `DAY 8`, promise vs reality, cheap vs true cost).
3. `Trap / Dramatic Scene`: a single dramatic scene where the system traps or overwhelms WIT (maze, bars, flood, snapping trap).
4. `Shock Face-Zoom`: WIT's face big in frame with a maximum reaction, next to ONE shocking element (a giant number, a draining card, an impossible total).
5. `Dramatic Metaphor`: the payoff/insight as one bold dramatic image (puppet on strings, chained, the one clean thing out of reach).

Comparison style (variants 1-2): a vertical divider down the middle; cool-blue "good/before" half vs warm-orange "bad/after" half; a small black angled tag in each top corner naming each side; one big red-and-white handwritten center hook with a rough red underline; a small shocked WIT standing on the divider with little shock strokes. This mirrors the approved `why-cheap-products-keep-getting-worse` `TODAY vs LATER` comparison thumbnail.

Drama bar (ALL variants) — default to MAX, not medium. Every variant should aim for SHOCK, CLICKBAIT, RAGE-BAIT ENERGY, INSANE, and CURIOSITY:

- WIT expression cranked all the way up: bulging eyes, jaw ripped wide open, mid-scream, sweat spraying, trembling, comic shock-burst lines, hot red rage glow. Push past "surprised" into screaming meltdown / furious-betrayed / hypnotized-maniac.
- ONE huge shocking element, oversized: a giant red number, an exploding/overflowing meter, an avalanche of objects, an erupting wallet, an impossible total.
- Aggressive red markup: thick red circles, fat red arrows, violent double-underlines, jagged "lightning-crack" dividers, glowing danger edges.
- Tight crop so WIT/emotion/number reads instantly at tiny mobile size.
- Hooks phrased as short outrage+curiosity QUESTIONS (`A TRICK?!`, `ROBBED?!`, `$10?!`, `FREE?!`, `SCAM?!`) — `1-3` words, big and rough.

Honesty line that keeps it rage-bait ENERGY without tripping a hard-fail (do NOT cross these — they are hard-fails): keep numbers real (illustrative figures from the research), keep hooks as curiosity QUESTIONS rather than asserted lies, and never add fake urgency (`ONLY TODAY`), fabricated stats, or hateful targeting of a real brand/person. The goal: "feels like rage-bait, isn't a lie."

Do not make the five variants random. They should test different click hypotheses for the same video promise. A loud single-face shock-zoom that does NOT repeat the title text often makes the strongest recommended thumbnail (best title-thumbnail contrast).

YouTube descriptions should be useful, not keyword spam.

Include:

- first two lines that sell the promise
- short summary in channel voice
- optional chapters based on script sections
- useful links or placeholders
- creator/channel link placeholder when appropriate
- tags and keywords
- `2-3` hashtags max
- pinned comment idea

Do not include product promotion unless the project explicitly requires it and the channel guardrails allow it.

## Workflow

1. Run the Project Selection Gate.
2. Run the Required Inputs Gate.
3. Read required context and the chosen project files, and run Detect shorts availability.
4. Extract:
   - core promise
   - main contradiction
   - recurring motif
   - WIT arc
   - first `10` seconds promise
   - likely section spine or hook beats from the research pack or optional script
   - risky claims to avoid in packaging
5. Design `5` distinct click hypotheses for the main video (use the fixed variant structure: 2 comparisons + 3 drama scenes).
6. For each of the `5`, write the **paired title and thumbnail together** as one locked unit (pair `N` = title `N` + thumbnail `N`); choose a WIT pose/emotion per thumbnail.
7. Write a reusable image-generation prompt and negative prompt for each thumbnail. Each prompt must include the WIT identity block and the paired title.
8. Generate `5` thumbnail drafts when image generation is available; otherwise record prompt-only status. Save images under `output/thumbnails/` as `main-pair-1.png` … `main-pair-5.png`.
9. Score all `5` pairs in a table (score the pair as a unit) using the thumbnail rules, packaging scorecard, and WIT consistency; mark a Winner and an A/B order.
10. Write the main-video YouTube description package:
   - final recommended description
   - alternate first two lines when useful
   - chapters from the real video timing when available, else from the research/script promise, else mark `draft until script`
   - tags, keywords, hashtags (max `3`), links, and pinned comment idea
11. If shorts are available, run Shorts Packaging: one title + description + thumbnail per short (save short thumbnails as `output/thumbnails/short-0N.png`).
12. Write or update the single `projects/<slug>/output/packaging.md` — the A/B pairs, the description package, the `## Thumbnail Prompts` section (main pairs + per-short prompts folded in), the scorecard, and the shorts blocks when shorts exist.
13. Run the Post-Packaging Notes Gate.
14. Respond with the Chat Response Format, including every main pair with its copyable prompt block and any per-short packaging.
15. Stop before `upload` or `learning`.

## Output File Format

Everything goes into the single `projects/<slug>/output/packaging.md`. Thumbnail images live beside it under `output/thumbnails/`. There is no `03-packaging.md` and no `PROMPTS.md`.

````markdown
# Packaging — `<video title>`

Source skill: `packaging`
Generated from: `00-topic-intake.md`, `01-research-pack.md`, `02-script.md`
Shorts included: `<yes — N shorts / no>`

## Packaging Brief

- Core promise:
- Main contradiction:
- Audience question:
- Recurring motif:
- WIT emotion:
- First 10 seconds promise:
- Risk to avoid:

## Main Video

### A/B Pairs (locked — title N ships with thumbnail N)

| Pair | Title | Thumbnail style | Label | WIT emotion | Visual contradiction | Image / Path | WIT consistency | Score | Decision |
|---:|---|---|---|---|---|---|---|---:|---|
| 1 |  | Comparison A |  |  |  | `output/thumbnails/main-pair-1.png` |  |  |  |
| 2 |  | Comparison B |  |  |  | `output/thumbnails/main-pair-2.png` |  |  |  |
| 3 |  | Trap / Dramatic Scene |  |  |  | `output/thumbnails/main-pair-3.png` |  |  |  |
| 4 |  | Shock Face-Zoom |  |  |  | `output/thumbnails/main-pair-4.png` |  |  |  |
| 5 |  | Dramatic Metaphor |  |  |  | `output/thumbnails/main-pair-5.png` |  |  |  |

Recommended A/B order: `<e.g. 4 -> 3 -> 1 -> 2 -> 5>`

### Description

```text
...
```

### Chapters

```text
00:00 ...
```
(Use real timestamps from the finished video/captions when available, else mark `draft until aligned`.)

### Tags / Keywords

...

### Hashtags

`#WhyItWorks ...` (max 3)

### Links

- Channel: `<placeholder>`

### Pinned Comment

```text
...
```

## Shorts

(Only when built shorts exist; one block per short. Omit this whole section if no shorts.)

### Short 01 — `<short name>` (source: Section `<n>`)

- Thumbnail: `output/thumbnails/short-01.png`
- Title: `<title>`

Description:

```text
...

#WhyItWorks ...
```

Repeat per short (`Short 02`, `Short 03`, ...).

## Thumbnail Prompts

Self-contained, ready-to-paste generation prompts. Keep each main prompt under its pair number with the paired title, so a title and its thumbnail are never separated.

### Pair 1 — Title: `<title 1>` · `main-pair-1.png`

```text
<full reusable prompt, WIT identity block, avoid-list folded in as "Do NOT include: ..."> 
```

Repeat for `Pair 2` … `Pair 5`, then one block per short (`Short 01` … `short-0N.png`).

## Scorecard Notes

- 1-second clarity:
- Curiosity gap:
- Visual contradiction:
- WIT emotion:
- Title strength:
- Title-thumbnail contrast:
- First 10 seconds promise:
- Learner-friendly clarity:
- Hard fails:

## Next Step Boundary

Next workflow step: `upload`

Do not continue into upload or learning until the user asks for that step.
````

## Post-Packaging Notes Gate

After creating, updating, or rerunning `output/packaging.md` or thumbnail images:

- the only downstream steps are `upload` and `learning`; do not mark `02-script.md`, `03-voiceover.md`, `04-visual-plan.md`, render, review, combine, caption, or shorts outputs as stale
- list `none` for stale main-pipeline outputs
- if upload metadata already exists and the packaging change affects upload text, mention that upload metadata may need manual review, but do not delete or regenerate it

## Chat Response Format

After creating or updating packaging, respond with a short review summary.

Do not paste every description option unless the user asks.
Always paste each main-video pair (title + thumbnail) and its copyable prompt block.

Use this structure:

````markdown
Done. I created/updated:

[output/packaging.md](<absolute path>) · thumbnails in `output/thumbnails/`

Status: `<status>`

Shorts packaged: `<yes — N shorts / no>`

Recommended pair: `Pair <n>` — title `<title>` + thumbnail `<one-line concept>`

Packaging score: `<score>/100`

A/B order: `<e.g. 4 -> 3 -> 1 -> 2 -> 5>`

Description brief:
- <line 1>
- <line 2>
- <line 3>

Main video — A/B pairs:

| Pair | Title | Thumbnail | Label | Score | Decision |
|---:|---|---|---|---:|---|

Pair prompts:

### Pair 1 — Title: `<title 1>` · Thumbnail: `<style>`

Image / path: `output/thumbnails/main-pair-1.png` (or prompt-only)

```text
<full reusable prompt, including the channel WIT identity block>
```

Negative prompt:

```text
<negative prompt / avoid list>
```

Repeat for Pair 2, Pair 3, Pair 4, and Pair 5.

Shorts (only when built shorts exist):

| Short | Title | Thumbnail | Hashtags |
|---|---|---|---|

Stale main pipeline:
- <file or none>
````

## Quality Bar

A packaging pass is ready when:

- the main video has exactly `5` **locked title+thumbnail pairs**, each with a paired title and a thumbnail (image or prompt-only)
- title and thumbnail within a pair do different jobs and do not repeat each other's words
- each thumbnail has a reusable prompt that names its paired title
- the five thumbnails follow the fixed structure: pairs 1-2 are split-screen comparisons, pairs 3-5 are full-drama single scenes
- the thumbnail prompts are folded into the `## Thumbnail Prompts` section of `output/packaging.md` (self-contained ChatGPT prompts, negatives folded in, reference-image WIT, labelled by pair number) — there is no separate `PROMPTS.md`
- thumbnail images are saved under `output/thumbnails/`, not `assets/thumbnails/`, and there is no `03-packaging.md`
- the `5` pairs are meaningfully different for A/B testing and are scored as units in a table
- every thumbnail prompt uses the current approved or pending WIT direction and is checked for WIT consistency before recommendation
- title names the hidden logic; thumbnail shows the weird situation; WIT has one clear emotion; label is `1-3` words
- the recommended pair scores at least `75/100`, preferably `85+`
- no hard-fail rule is triggered
- the YouTube description feels useful and on-brand; tags and hashtags (max `3`) are relevant, not spammy
- the first `10` seconds can pay off the promise
- when built shorts exist, every short has its own title, description, and thumbnail; when none exist, only the main video is packaged
- a single consolidated `output/packaging.md` holds every title and description for the main video and all shorts, with the thumbnail prompts folded in
- the Post-Packaging Notes Gate is honored (earlier production outputs are not marked stale)

## Hard Fails

Reject or revise packaging before finishing if:

- the project lacks `00-topic-intake.md`, `01-research-pack.md`, or `02-script.md`
- `01-research-pack.md` is older than `00-topic-intake.md`, or `02-script.md` is older than `01-research-pack.md`
- it creates `03-packaging.md` or a separate `PROMPTS.md` (both are retired; everything goes in `output/packaging.md`)
- a pair's title and thumbnail repeat the same phrase
- one side of a pair is edited while the other is left stale (the coupling rule was not applied)
- the thumbnail is just a presentation slide
- fewer than `5` title+thumbnail pairs are produced or prompt-recorded for the main video
- thumbnails or prompts are written under `assets/thumbnails/` instead of `output/thumbnails/`
- titles and descriptions are not exported to the single `output/packaging.md` deliverable
- built shorts exist but were not packaged (missing per-short title, description, or thumbnail)
- thumbnail prompts are too vague to reuse in another image platform
- the pairs are basically the same idea with tiny style changes
- thumbnail prompts use removed `original-wit-24` details after the WIT replacement decision
- generated WIT is off-model and still recommended as final
- WIT is neutral or decorative
- the label is too long for mobile
- the description makes unsupported claims
- tags are stuffed with irrelevant keywords
- the package relies on rage bait, fake urgency, or copied thumbnail structure
- the skill creates script, voiceover, visual plan, render, review, combine, caption, upload, or learning files

## Self-Improvement

Read `references/memory.md` every run.

Update skill memory when:

- the user rejects a title style, thumbnail concept, description style, tags, or link format
- the user chooses a package and explains why
- a later hook, voiceover, visual plan, or upload review exposes weak packaging
- generated thumbnail images fail mobile clarity or WIT emotion
- a package performs well or badly after upload

Promote lessons into `.agents/_shared/channel/learning-log.md` only when they improve the whole channel. Classify promoted lessons as `Core`, `Experiment`, `Operational lesson`, or `Reject`.

Do not rewrite channel foundation, audience, tone, or product-promotion boundary from one packaging run without explicit user confirmation.
