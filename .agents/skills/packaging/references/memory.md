# Packaging Skill Memory

This file stores memory specific to the `packaging` skill.

Use `.agents/_shared/` for channel-wide packaging systems, thumbnail rules, and YouTube strategy.
Use this file for title taste, thumbnail concept behavior, description format, tag habits, and lessons about making packaging stronger for this channel.

## Current Skill Standard

- Run after `script-draft` and before `voiceover`.
- Require non-empty `00-topic-intake.md`, `01-research-pack.md`, and `02-script.md`.
- Write only `03-packaging.md` and thumbnail assets under `assets/thumbnails/`.
- Create title options, exactly `5` thumbnail drafts for A/B testing, reusable prompt for each thumbnail, thumbnail comparison scoring, and a full YouTube description package.
- The previous current channel WIT design from `original-wit-24` was removed on `2026-06-07`.
- A draft replacement pose set now exists at `.agents/_shared/assets/wit/poses/` and is awaiting user review. Thumbnail prompts should use this WIT style: simple white round-headed figure, thick black outline, oversized black glasses, expressive eyebrows, simple white body, and strong suspicious / betrayed / panicked expressions.
- Never prompt the removed old WIT details as current channel WIT: messy black hair, white shirt, receipt-like tie, dark pants, oversized dark shoes.
- In chat responses, include every thumbnail variant with its image/path and full prompt in a copyable fenced block.
- Include tags, keywords, hashtags, links or placeholders, chapters when useful, and pinned comment ideas.
- Use the channel rule: thumbnail shows the weird situation; title names the hidden logic.
- Score packages with `.agents/_shared/systems/topic-packaging-hooks.md`.
- Score all `5` thumbnail variants in a comparison table before recommending one.
- Prefer simple English and mobile-readable thumbnail labels.
- Keep the channel influence-first; do not turn descriptions into direct product promotion.
- When `03-packaging.md` is created, updated, or rerun, treat `04-09` downstream outputs as stale.
- Do not delete stale downstream outputs unless the user explicitly asks.
- Stop before voiceover, visual plan, HyperFrames, renders, upload, or self-learning.

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
The user wanted a `Packaging` skill that creates title, thumbnails, and YouTube description metadata, and wanted it placed after Research Pack and before Voiceover.

Lesson:
Packaging should run after the script exists but before voiceover, so title, thumbnail, and description can reflect the actual video promise before audio and visual production continue.

Apply next time:

- require `02-script.md`
- create `03-packaging.md`
- include title, thumbnails, YouTube description, tags, links, hashtags, chapters, and pinned comment
- treat `04-voiceover.md` and later outputs as stale after packaging changes

Promote to shared memory:
yes, this is a pipeline-level capability.

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
