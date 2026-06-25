---
name: packaging
description: Create or update side-branch step 3 YouTube packaging for a Why It Works video project. Use when the user asks for Packaging, title and thumbnail, YouTube description, upload metadata, tags, hashtags, thumbnail concepts, thumbnail images, A/B thumbnail testing, packaging, or step 3 of the side-branch workflow; requires completed 00-topic-intake.md and 01-research-pack.md only, does not require script or voiceover, creates thumbnail drafts using the current approved or pending WIT direction with reusable generation prompts, scores them, then writes only the project's 03-packaging.md and thumbnail assets under assets/thumbnails/.
---

# Packaging

## Purpose

Run side-branch step `3` of the `Why It Works` video workflow.

Turn a selected project's topic and research into a strong YouTube package:

- titles
- `5` thumbnail drafts in different styles for A/B testing
- generation prompt for each thumbnail
- thumbnail comparison and score table
- YouTube description
- tags, hashtags, links, chapters, and pinned comment ideas

Packaging should make the click promise clear for publishing and testing, but it does not block the main production pipeline.

## Pipeline Position

This skill branches from `research-pack`.

Pipeline rule:

Packaging is outside the main production pipeline. It only requires `00-topic-intake.md` and `01-research-pack.md`. It does not require `02-script.md` or voiceover.

Required previous outputs:

- `projects/<slug>/00-topic-intake.md`
- `projects/<slug>/01-research-pack.md`

Write or update:

- `projects/<slug>/03-packaging.md`
- `projects/<slug>/assets/thumbnails/`

If `00-topic-intake.md` or `01-research-pack.md` is missing, stop and tell the user to run the missing previous skill in order before `packaging`.

If `01-research-pack.md` is older than `00-topic-intake.md`, treat the research pack as stale and stop. Tell the user to rerun `research-pack`.

If `03-packaging.md` exists but `00-topic-intake.md` or `01-research-pack.md` has a newer modified time, treat packaging as stale and use Update Mode when the user asks for packaging.

When this skill creates, updates, or reruns `03-packaging.md` or thumbnail assets, do not mark main-pipeline outputs stale.

List only packaging-side notes in chat. Do not delete or regenerate main-pipeline files unless the user explicitly asks.

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
15. the chosen project files:
    - `projects/<slug>/00-topic-intake.md`
    - `projects/<slug>/01-research-pack.md`

Load additional shared systems only when needed:

- `.agents/_shared/systems/visual-production.md` when planning real or real-looking thumbnail assets or reference-board support
- `.agents/_shared/assets/wit/poses/` when current WIT pose assets are needed
- `projects/<slug>/02-script.md` when available, as optional context only; never require it for packaging.

## Project Selection Gate

Always resolve the target project before writing packaging.

Use this order:

1. If the user names a project slug or path, use that project.
2. If the current chat clearly selected a project and the folder exists, use that project.
3. If there is exactly one project with completed `00-topic-intake.md` and `01-research-pack.md` but no completed `03-packaging.md`, smart-select it and say so.
4. Otherwise scan `projects/`, excluding `_template`, and find unfinished packaging candidates.

A packaging candidate is usually:

- a folder with non-empty `00-topic-intake.md`
- and non-empty `01-research-pack.md`
- and no `03-packaging.md`, or an empty/stub `03-packaging.md`
- and not obviously blocked by stale upstream files

When multiple candidates exist or context is unclear, ask the user to choose before writing.

Do not create a new project folder in this skill. New projects come from `topic-intake`.

## Required Inputs Gate

Before writing packaging, verify the chosen project has:

- non-empty `00-topic-intake.md`
- non-empty `01-research-pack.md`

If any are missing, stop and name the missing skill:

- missing `00-topic-intake.md` -> run `topic-intake`
- missing `01-research-pack.md` -> run `research-pack`

Do not create placeholder upstream files.

## Request Modes

### Create Mode

Use when the chosen project has no usable `03-packaging.md`.

Write:

```text
projects/<slug>/03-packaging.md
```

### Update Mode

Use when the user asks to improve, rewrite, score, refresh, or choose a different title, thumbnail, description, tags, hashtags, or links.

Read the existing `03-packaging.md`, preserve useful approved decisions, and update only the necessary sections unless the whole package is clearly affected.

### Thumbnail A/B Mode

Use on every Create Mode and Update Mode run unless the user explicitly says not to generate thumbnails.

Create or update:

```text
projects/<slug>/assets/thumbnails/
```

Generate exactly `5` thumbnail drafts with meaningfully different styles for A/B testing.

Each thumbnail must have:

- variant name
- style direction
- image path or generation status
- reusable generation prompt
- negative prompt / avoid list
- dominant object
- thumbnail label
- WIT emotion
- visual contradiction
- score
- strength
- risk
- decision

Before generating thumbnail images, use the research pack's real visual/reference leads when available. Real objects and real internet-image references should define the thumbnail's material, lighting, prop choice, and viewer closeness.

Use image generation when an image generation tool is available to create controlled, brand-safe thumbnail outputs. Save generated thumbnails or returned image references under `assets/thumbnails/` when the environment supports saving them.

Generated thumbnail images should be treated as controlled outputs informed by real references, not replacements for doing the real-reference thinking.

If image generation is unavailable, still create the `5` production-ready prompts and mark each image status as `prompt only / image not generated`. Do not pretend images were created.

Always write the prompts into a ready-to-paste `projects/<slug>/assets/thumbnails/PROMPTS.md` (in addition to recording them in `03-packaging.md`), optimized for the user generating images in ChatGPT / DALL·E:

- each variant is a SELF-CONTAINED block the user can paste alone (no cross-references needed to generate)
- ChatGPT/DALL·E has no separate negative-prompt field, so fold the avoid-list INTO the prompt as `Do NOT include: ...`
- assume the user attaches the WIT neutral pose (`.agents/_shared/assets/wit/poses/wit-pose-neutral-front.png`) as the reference image; open each prompt with "use the cartoon character in the attached reference image as WIT — keep his art style, only change his pose/expression"
- for the two comparison variants, tell the user to ALSO attach the approved comparison thumbnail (`projects/1-why-cheap-products-keep-getting-worse/assets/thumbnails/variant-c-generated.png`) as a layout reference
- include a short how-to (attach images, ask for 16:9 1280x720, re-roll line if WIT drifts) and the A/B generate-first order
- name each output file (`variant-a-generated.png` … `variant-e-generated.png`) and the reject rule (no hair / shirt-tie / shoes = off-model WIT)

The prompts should also be reusable in another AI image platform if the user dislikes the generated thumbnails.

Every thumbnail prompt must include the channel WIT identity block from `WIT Prompt Requirements`.
If image generation produces an off-model WIT, mark that thumbnail as failed or concept-only and write a corrected prompt.

### Improve Memory Mode

Use when the user reviews packaging and gives reusable lessons.

Update in this order:

1. the project `03-packaging.md` if the review affects this video
2. this skill's `references/memory.md`
3. shared memory only if the lesson improves packaging across the whole channel

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
3. Read required context and the chosen project files.
4. Extract:
   - core promise
   - main contradiction
   - recurring motif
   - WIT arc
   - first `10` seconds promise
   - likely section spine or hook beats from the research pack or optional script
   - risky claims to avoid in packaging
5. Generate `10-15` title options.
6. Generate `5` thumbnail A/B directions using the required variant styles.
7. For each thumbnail, choose a WIT pose/emotion from the current WIT direction.
8. Write a reusable image-generation prompt and negative prompt for each thumbnail. Each prompt must include the WIT identity block.
9. Generate `5` thumbnail drafts when image generation is available; otherwise record prompt-only status.
10. Compare and score all `5` thumbnails in a table using the thumbnail rules, packaging scorecard, and WIT consistency.
11. Pair the strongest titles and thumbnail drafts into `3-5` complete packages.
12. Score the strongest packages with `.agents/_shared/systems/topic-packaging-hooks.md`.
13. Write YouTube description options:
   - final recommended description
   - alternate first two lines when useful
   - rough chapters from the package/research promise when useful, or mark chapters as `draft until script`
   - tags, keywords, hashtags, links, and pinned comment idea
14. Write or update `projects/<slug>/03-packaging.md`.
15. Run the Side-Branch Notes Gate.
16. Respond with the Chat Response Format, including every thumbnail and its copyable prompt block.
17. Stop before script, voiceover, visual plan, render, review, upload, or learning.

## Output File Format

Use this structure for `projects/<slug>/03-packaging.md`:

````markdown
# 03 Packaging

Video: `<title>`

Status: `draft packaging`

Source skill: `packaging`

Source files:

- `00-topic-intake.md`
- `01-research-pack.md`

## Packaging Brief

- Core promise:
- Main contradiction:
- Audience question:
- Recurring motif:
- WIT emotion:
- First 10 seconds promise:
- Risk to avoid:

## Title Options

| # | Title | Promise | Curiosity | Risk | Score |
|---:|---|---|---|---|---:|

## Thumbnail Concepts

| # | Concept | Dominant object | Label | WIT emotion | Visual contradiction | Prompt / Production notes |
|---:|---|---|---|---|---|---|

## Thumbnail A/B Test

| Variant | Style | Image / Path | Prompt ref | Label | WIT pose / emotion | WIT consistency | Score | Strength | Risk | Decision |
|---|---|---|---|---|---|---|---:|---|---|---|

## Thumbnail Generation Prompts

### Variant A: `<style>`

Prompt:

```text
...
```

Negative prompt / avoid:

```text
...
```

Use notes:

-

Repeat this prompt block for `Variant B`, `Variant C`, `Variant D`, and `Variant E`.

## Title-Thumbnail Packages

| Rank | Title | Thumbnail concept | Why it works | Score | Decision |
|---:|---|---|---|---:|---|

## Recommended Package

- Title:
- Thumbnail concept:
- Thumbnail label:
- Dominant object:
- WIT emotion:
- Visual contradiction:
- First 10 seconds payoff:
- Packaging score:
- Decision:

## Thumbnail Comparison Notes

- Best thumbnail:
- Best prompt to reuse manually:
- Most clickable:
- Clearest for mobile:
- Biggest risk:
- Recommended A/B order:

## YouTube Description

### Final Description

```text
...
```

### Chapters

```text
draft until script
```

### Tags / Keywords

### Hashtags

### Links

### Pinned Comment

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

Next workflow step: `independent side branch`

Do not continue into script, voiceover, visual plan, render, review, upload, or learning until the user asks for that step.
````

## Side-Branch Notes Gate

After creating, updating, or rerunning `03-packaging.md` or thumbnail assets:

- do not mark `02-script.md`, `04-voiceover.md`, `05-visual-plan.md`, render, review, upload, or learning outputs as stale
- list `none` for stale main-pipeline outputs
- if upload metadata already exists and the packaging change affects upload text, mention that upload metadata may need manual review, but do not delete or regenerate it

## Chat Response Format

After creating or updating packaging, respond with a short review summary.

Do not paste every title and description option unless the user asks.
Always paste each thumbnail variant and its copyable prompt block.

Use this structure:

````markdown
Done. I created/updated:

[03-packaging.md](<absolute path>)

Status: `<status>`

Recommended title: `<title>`

Recommended thumbnail: `<one-line concept>`

Packaging score: `<score>/100`

Thumbnail A/B winner: `<variant + score>`

Description brief:
- <line 1>
- <line 2>
- <line 3>

Top options:

| Rank | Title | Thumbnail | Score | Decision |
|---:|---|---|---:|---|

Thumbnail drafts:

| Variant | Style | Image / Path | Score | Decision |
|---|---|---|---:|---|

Thumbnail prompts:

### Variant A: `<style>`

Image / path: `<path or prompt-only>`

```text
<full reusable prompt, including the channel WIT identity block>
```

Negative prompt:

```text
<negative prompt / avoid list>
```

Repeat for Variant B, Variant C, Variant D, and Variant E.

Stale main pipeline:
- <file or none>
````

## Quality Bar

A packaging pass is ready when:

- title and thumbnail do different jobs
- exactly `5` thumbnail variants are generated or recorded as prompt-only if generation is unavailable
- each thumbnail has a reusable prompt
- the five variants follow the fixed structure: variants 1-2 are split-screen comparisons, variants 3-5 are full-drama single scenes
- a ready-to-paste `assets/thumbnails/PROMPTS.md` is written (self-contained ChatGPT prompts, negatives folded in, reference-image WIT)
- thumbnail variants are meaningfully different for A/B testing
- thumbnails are compared and scored in a table
- every thumbnail prompt uses the current approved or pending WIT direction
- generated thumbnails are checked for WIT consistency before recommendation
- title names the hidden logic
- thumbnail shows the weird situation
- WIT has one clear emotion
- label is `1-3` words
- package scores at least `75/100`, preferably `85+`
- no hard-fail rule is triggered
- the YouTube description feels useful and on-brand
- tags and hashtags are relevant, not spammy
- the first `10` seconds can pay off the promise
- stale main-pipeline status is listed as `none`

## Hard Fails

Reject or revise packaging before finishing if:

- the project lacks `00-topic-intake.md` or `01-research-pack.md`
- `01-research-pack.md` is older than `00-topic-intake.md`
- the title and thumbnail repeat the same phrase
- the thumbnail is just a presentation slide
- fewer than `5` thumbnail variants are produced or prompt-recorded
- thumbnail prompts are too vague to reuse in another image platform
- thumbnail variants are basically the same idea with tiny style changes
- thumbnail prompts use removed `original-wit-24` details after the WIT replacement decision
- generated WIT is off-model and still recommended as final
- WIT is neutral or decorative
- the label is too long for mobile
- the description makes unsupported claims
- tags are stuffed with irrelevant keywords
- the package relies on rage bait, fake urgency, or copied thumbnail structure
- the skill creates script, voiceover, visual plan, render, review, upload, or learning files

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
