# Packaging Skill Memory

This file stores memory specific to the `packaging` skill.

Use `.agents/_shared/` for channel-wide packaging systems, thumbnail rules, and YouTube strategy.
Use this file for title taste, thumbnail concept behavior, description format, tag habits, and lessons about making packaging stronger for this channel.

## Current Skill Standard

- Runs **after `caption`** in the workflow (`... -> combine -> caption -> packaging -> upload -> learning`); it is no longer a research-pack side branch.
- Require non-empty `00-topic-intake.md`, `01-research-pack.md`, AND `02-script.md` (hard gate). Recommended position is after caption so the finished video, real chapters, and built shorts are available, but only those three files are hard-required.
- Write everything to ONE file: `output/packaging.md` (the 5 locked pairs, the description package, the thumbnail prompts folded into a `## Thumbnail Prompts` section, and per-short blocks when shorts exist). Thumbnail images go to `output/thumbnails/`. Do NOT create `03-packaging.md` or a separate `PROMPTS.md` anymore, and do NOT write under `assets/thumbnails/`. Leave legacy `03-packaging.md`/`assets/thumbnails/` in older projects as-is unless the user asks to migrate.
- Main video = exactly `5` **locked title+thumbnail A/B pairs**: title `N` is coupled to thumbnail `N`. Editing thumbnail prompt `N` also rewrites title `N`, and editing title `N` also rewrites thumbnail prompt `N`; never leave one side of a pair stale. Keep pair numbers stable; pairs are independent of each other. Files named `main-pair-1.png` … `main-pair-5.png`.
- Shorts-aware: detect built shorts via `shorts/shorts-plan.md` or `output/shorts/*.mp4`. If none, package the main video only. If present, also create ONE title + description + thumbnail per short (portrait `1080x1920` cover reusing the short's source-section assets, `short-0N.png`), standalone with NO long-video CTA.
- Provide a reusable prompt for each thumbnail, score the `5` pairs as units, and write the full YouTube description package (description, chapters, tags, max-3 hashtags, links, pinned comment).
- Export every title + description for the main video AND all shorts into the one `output/packaging.md` file.
- The previous current channel WIT design from `original-wit-24` was removed on `2026-06-07`.
- A draft replacement pose set now exists at `.agents/_shared/assets/wit/poses/` and is awaiting user review. Thumbnail prompts should use this WIT style: simple white round-headed figure, thick black outline, oversized black glasses, expressive eyebrows, simple white body, and strong suspicious / betrayed / panicked expressions.
- Never prompt the removed old WIT details as current channel WIT: messy black hair, white shirt, receipt-like tie, dark pants, oversized dark shoes.
- In chat responses, include every thumbnail variant with its image/path and full prompt in a copyable fenced block.
- Include tags, keywords, hashtags, links or placeholders, chapters when useful, and pinned comment ideas.
- Use the channel rule: thumbnail shows the weird situation; title names the hidden logic.
- Default thumbnail intensity is MAX: SHOCK / CLICKBAIT / RAGE-BAIT ENERGY / INSANE / CURIOSITY. Crank WIT expression all the way up (bulging eyes, jaw ripped open, mid-scream, sweat, shock-burst lines, red rage glow), use ONE oversized shocking element, aggressive red markup (circles, fat arrows, double-underlines, jagged divider), and short `?!` outrage-curiosity hooks (`A TRICK?!`, `ROBBED?!`, `$10?!`). Hold the honesty line (real numbers, question hooks, NO fake urgency/fabricated stat/hateful brand targeting) so it is rage-bait ENERGY, not a lie. Baked into `SKILL.md` → "Drama bar (ALL variants)".
- Use real visual/reference leads from the research pack to ground thumbnail material, lighting, props, and viewer closeness before generating controlled thumbnail outputs.
- Score packages with `.agents/_shared/systems/topic-packaging-hooks.md`.
- Score all `5` thumbnail variants in a comparison table before recommending one.
- Prefer simple English and mobile-readable thumbnail labels.
- Keep the channel influence-first; do not turn descriptions into direct product promotion.
- When `output/packaging.md` is created, updated, or rerun, the only downstream steps are `upload` and `learning`; do not mark earlier production outputs stale.
- Stop before `upload` or `learning`.

## Output Standard

A useful packaging file should include:

- packaging brief
- `10-15` title options
- exactly `5` thumbnail A/B variants with different styles
- reusable generation prompt and negative prompt for each thumbnail
- WIT consistency note for each thumbnail against the current approved or pending WIT direction
- thumbnail comparison and assessment table
- `3-5` scored title-thumbnail packages
- one recommended package
- thumbnail draft paths or generation prompts
- final YouTube description
- chapters when section timing is available or can be estimated
- tags, keywords, hashtags, links, and pinned comment
- scorecard notes
- next-step boundary

## Feedback Log

### 2026-06-07 - Skill Created

Classification: `Core operational capability`

Context:
The user wanted a `Packaging` skill that creates title, thumbnails, and YouTube description metadata.

Lesson:
Packaging creates `03-packaging.md` and is a side-branch artifact, not a main-pipeline gate.

Apply next time:

- create `03-packaging.md`
- include title, thumbnails, YouTube description, tags, links, hashtags, chapters, and pinned comment
- do not mark `02-script.md`, `04-voiceover.md`, visual plan, render, review, upload, or learning stale after packaging changes

Promote to shared memory:
yes, this is a pipeline-level capability.

### 2026-06-07 - Packaging Requires Only Topic And Research

Classification: `Core operational update`

Context:
The user clarified that packaging should not require a script or voiceover. It should be based on topic intake and research pack only.

Lesson:
Packaging is outside the main pipeline. It branches from Research Pack and can be created from topic intake and research pack alone.

Apply next time:

- require only non-empty `00-topic-intake.md` and `01-research-pack.md`
- do not block packaging when `02-script.md` or `04-voiceover.md` is missing
- do not mark main-pipeline outputs stale after packaging changes
- use research and the angle package to create the first `10` seconds promise

Promote to shared memory:
yes, this is a channel-wide pipeline rule.

### 2026-06-07 - Five Thumbnail A/B Drafts Required

Classification: `Packaging lesson`

Context:
The user clarified that every Packaging run should automatically generate `5` thumbnails in different styles for A/B testing.

Lesson:
Thumbnail generation is not optional in the normal packaging output. The skill must produce thumbnails or, if generation tooling is unavailable, production-ready prompts marked as prompt-only.

Apply next time:

- create exactly `5` thumbnail variants with different click hypotheses
- include a reusable generation prompt and negative prompt for each variant
- save or reference thumbnails under `assets/thumbnails/` when possible
- compare and score all variants in a table
- recommend one winner and an A/B testing order

Promote to shared memory:
No. This is currently a `packaging` skill output contract.

### 2026-06-07 - Thumbnail WIT Must Match Channel WIT

Classification: `Superseded packaging lesson`

Context:
The generated packaging thumbnails used a generic white stick-figure / mascot-like WIT that did not match the channel's approved WIT design.

Lesson:
This lesson is superseded by the later decision to remove `original-wit-24`.
The useful part remains: packaging prompts must explicitly preserve whatever WIT direction is current or approved.

Apply next time:

- read `.agents/_shared/channel/brand-system.md` before thumbnail generation
- include the current WIT identity block in every thumbnail prompt
- score WIT consistency in the thumbnail comparison table
- mark off-model generated WIT as failed or concept-only
- in the chat response, show each thumbnail variant with its image/path and a full copyable prompt block

Promote to shared memory:
No. Superseded by `Original-WIT Removed; Thumbnail WIT Pending`.

### 2026-06-07 - Original-WIT Removed; Thumbnail WIT Pending

Classification: `Core operational update`

Context:
After comparing the approved channel WIT against the five generated cheap-products thumbnails, the user decided the thumbnail WIT is the better direction and asked to remove the current channel WIT completely. The user will request regeneration of the full WIT pose set later.

Lesson:
Do not use `original-wit-24` as the current WIT anymore. For the cheap-products packaging, restore and preserve the five thumbnail drafts with the white round-headed glasses WIT. Future WIT generation should derive from those thumbnails only when the user asks for the next step.

Apply next time:

- do not reference `original-wit-24` as current WIT
- do not generate the old messy-hair shirt-and-tie WIT unless explicitly asked as historical reference
- keep restored thumbnail PNGs as the current visual direction for this video's WIT
- use `.agents/_shared/assets/wit/poses/` as draft WIT reference only after user review; do not mark it final without approval

Promote to shared memory:
Yes. This changes the channel-wide character direction.

### 2026-06-07 - Thumbnail Generation Should Be Real-Reference-Informed

Classification: `Packaging lesson`

Context:
The user clarified that real internet images make video visuals feel closer to viewers than generated images alone.

Lesson:
Packaging can still generate controlled thumbnail outputs, but concepts should first use real reference leads from the research pack for material, object choice, and lived-in texture. Generated thumbnails should be brand-safe outputs informed by real references, not blind synthetic scenes.

Apply next time:

- read visual/reference leads in `01-research-pack.md`
- use real object/material references to shape the thumbnail prompt
- avoid copying real photos directly when source/copyright/logo risk is unclear
- keep generated outputs clean, branded, and mobile-readable

Promote to shared memory:
no; shared visual-production rules already contain the channel-wide standard.

### 2026-06-23 - Fixed 5-variant structure: A+B comparison, C-D-E drama; always write PROMPTS.md

Classification: `Packaging lesson`

Context:
On `why-everything-is-a-subscription-now` the first calm prompts produced tidy, "normal, not interesting" thumbnails. The owner wanted shock / clickbait / curiosity, liked the `why-cheap-products` `TODAY vs LATER` split-screen comparison (`variant-c-generated.png`), and asked to bake this into the skill: variants A and B should be comparison prompts, C/D/E stay full-drama single scenes.

Lesson:
The 5 thumbnail variants now use a FIXED structure, not the old five free-form styles:
1-2 = split-screen COMPARISONS (vertical divider; cool-blue good/before half vs warm-orange bad/after half; black angled corner tags; one big red+white handwritten center hook with red underline; small shocked WIT on the divider — mirrors the approved cheap-products comparison).
3 = trap/dramatic scene; 4 = shock face-zoom with one giant shocking element (big red number); 5 = dramatic metaphor (puppet/chained/clean-thing-out-of-reach).
Push the DRAMA bar on all five (extreme WIT expression, tight crop, one shocking element, red/motion danger cues) but keep the CLAIM honest (illustrative numbers, no fake promises) so it reads dramatic, not deceptive.

Apply next time:
- generate variants by this fixed structure (A/B comparison, C/D/E drama), not random styles
- comparison subjects come from the thesis: OWN vs RENT, REAL vs FAKE, THEN vs NOW, DAY 1 vs DAY 8, promise vs reality
- always write a ready-to-paste `assets/thumbnails/PROMPTS.md` (self-contained ChatGPT prompts, negatives folded inline, reference-image WIT; for A/B also attach the cheap-products comparison as the layout reference)
- crank emotion + curiosity hard; never cross into fake claims or hateful rage bait (channel guardrail)

Promote to shared memory:
No; packaging-skill execution practice (the WIT/brand direction itself is unchanged).

### 2026-06-23 - When the user attaches a WIT reference image, prompts should point AT the image

Classification: `Packaging lesson`

Context:
On `why-everything-is-a-subscription-now`, the user generates thumbnails in ChatGPT (Claude can't make images) and said they will attach the WIT neutral pose (`.agents/_shared/assets/wit/poses/wit-pose-neutral-front.png`) as the reference image. They asked the prompts to reference the attached WIT rather than describe him from scratch.

Lesson:
For ChatGPT/DALL·E thumbnail prompts: (1) there is no separate negative-prompt field, so fold the avoid-list into the prompt as "Do NOT include: ..."; (2) make each prompt self-contained (one paste = one thumbnail); (3) when the user attaches a WIT reference image, open every prompt with "Use the cartoon character in the attached reference image as WIT — keep his exact art style and proportions; only change his pose and expression," and keep a short style reminder as a drift fallback. Write these copy-paste prompts into `assets/thumbnails/PROMPTS.md` (self-contained), with `03-packaging.md` remaining the scored source of record. Name the exact reference file to attach in the how-to.

Apply next time:
- if no image tool, write `PROMPTS.md` as ready-to-paste ChatGPT prompts, not just a pointer to `03-packaging.md`
- fold negatives inline; one self-contained block per variant; vary only pose + emotion per variant
- when a WIT reference image is attached, reference the attached image as the character and name the exact pose file

Promote to shared memory:
No; packaging-skill execution practice.

### 2026-06-24 - Owner wants thumbnails pushed to MAX shock/clickbait/rage/curiosity (honesty line held)

Classification: `Packaging lesson`

Context:
On `why-buy-1-get-1-beats-50-off`, the first thumbnail prompts (suspicious-squint WIT, calm `SAME?`
hook) were too tame. The owner asked to remake them: "it must be SHOCK, CLICK BAIT, RAGE BAIT,
CURIOSITY." This is the same direction as the 2026-06-23 drama-bar lesson but pushed harder, with
"rage bait" stated explicitly.

Lesson:
By default crank the drama bar to MAX, not medium. Turn WIT's expression all the way up (bulging
eyes, jaw ripped open, mid-scream, sweat spraying, comic shock-burst lines, hot red rage glow), make
the ONE shocking element huge (giant red number, exploding profit meter, avalanche, erupting wallet),
add aggressive red marks (circles, fat arrows, double-underlines, jagged lightning divider), and use
outrage+curiosity hooks phrased as QUESTIONS: `A TRICK?!`, `ROBBED?!`, `$10?!`, `FREE?!`.

Honesty line that keeps it rage-bait ENERGY without a hard-fail: keep numbers real (the research's
$5/$10/$1/$2), keep hooks as curiosity questions (not asserted lies), and never add fake urgency
("ONLY TODAY"), fabricated stats, or hateful targeting of a real brand/person. "Feels like rage-bait,
isn't a lie."

Apply next time:
- default thumbnail intensity = MAX (extreme WIT expression + one huge shocking element + red danger cues)
- prefer short `?!` curiosity-rage hooks over calm labels
- still hold the channel honesty guardrail: real numbers, question hooks, no fake urgency/stat, no hateful brand targeting
- a loud single-face shock-zoom that does NOT repeat the title text often makes the best recommended thumbnail (best title-thumbnail contrast)

Promote to shared memory:
No; packaging-skill execution practice. The honesty guardrail itself is unchanged in `channel-guardrails.md`.

Update 2026-06-24 (follow-up): owner asked to make this the SKILL default permanently and added "INSANE"
to the intensity list. Promoted from a per-video note into `SKILL.md` → "Drama bar (ALL variants)" so
every future run starts at MAX intensity by default (still holding the honesty line).

### 2026-06-26 - Locked title+thumbnail A/B pairs, shorts packaging, outputs moved to output/

Classification: `Core operational update`

Context:
The owner redefined the packaging output. (1) Titles and thumbnails are now A/B-tested TOGETHER as
`5` locked pairs: title `N` ships with thumbnail `N`. Updating thumbnail prompt `N` must also update
title `N`, and updating title `N` must rewrite thumbnail prompt `N`. (2) The skill is shorts-aware:
if no built shorts exist, package only the main video; if built shorts exist, also create one title +
description + thumbnail per short. (3) Relocate outputs: thumbnail images + prompts move from
`assets/thumbnails/` to `output/thumbnails/`; titles + descriptions for the main video AND every short
are exported into a single `output/packaging.md` file. `03-packaging.md` stays as the scored working doc.

Lesson:
Packaging's unit is now the locked title+thumbnail pair, not loose titles scored against loose
thumbnails. The coupling is bidirectional and pair-numbered so a single edit never desyncs a pair.
Shorts packaging is conditional on built shorts being present. `output/` is the single home for all
deliverables, so packaging writes there (thumbnails, prompts, and the consolidated copy file).

Apply next time:
- main video: 5 locked pairs (`main-pair-1..5.png`), fixed structure (pairs 1-2 comparison, 3-5 drama),
  scored as units; edit both sides of a pair together; keep pair numbers stable.
- detect shorts (`shorts/shorts-plan.md` or `output/shorts/*.mp4`); when present, one title+desc+thumbnail
  per short (portrait `short-0N.png`, standalone, no long-video CTA), pulled from the shorts plan + script.
- write `output/thumbnails/` (images), `output/packaging.md` (single consolidated file). Never `assets/thumbnails/`.

Promote to shared memory:
No; this is packaging-skill output contract. The channel WIT/honesty/drama direction is unchanged.

### 2026-06-26 (follow-up) - Single file, prompts folded in, retire 03-packaging.md/PROMPTS.md, run after caption

Classification: `Core operational update`

Context:
Same day, the owner simplified further: (1) `PROMPTS.md` is redundant — fold the thumbnail prompts
into a `## Thumbnail Prompts` section inside `output/packaging.md`. (2) Stop creating `03-packaging.md`
for new projects; write `output/packaging.md` directly (existing projects keep their `03-packaging.md`
as-is, untouched). (3) Packaging moves OUT of the "03 side-branch" slot to a step AFTER `caption`, and
now hard-requires `00-topic-intake.md` + `01-research-pack.md` + `02-script.md`.

Lesson:
ONE deliverable file per project: `output/packaging.md` holds the 5 locked pairs, the description
package, the folded thumbnail prompts, and the per-short blocks. Images only under `output/thumbnails/`.
No `03-packaging.md`, no `PROMPTS.md`. Pipeline order is now
`... -> combine -> caption -> packaging -> upload -> learning`. Recommended to run after caption so the
finished video / real chapters / built shorts are available, but the hard gate is just the three files.

Apply next time:
- create only `output/packaging.md` (+ images in `output/thumbnails/`); never `03-packaging.md` or `PROMPTS.md`.
- require topic-intake + research-pack + script; refuse otherwise.
- on legacy projects, leave old `03-packaging.md`/`assets/thumbnails/` alone unless asked to migrate
  (project 1 was migrated to the new layout on 2026-06-26 as the first test).

Promote to shared memory:
Partly — the pipeline-order change (packaging after caption, requires script) is a channel-wide
pipeline rule and should be reflected in `current-state.md`/`production-workflow.md` and the
`CLAUDE.md`/`AGENTS.md` pipeline gates. The single-file output detail stays packaging-local.

## Feedback Entry Template

```markdown
### YYYY-MM-DD - <short lesson>

Classification: `Packaging lesson` / `Operational lesson` / `Experiment`

Context:

Lesson:

Apply next time:

Promote to shared memory:
yes/no, with reason
```
