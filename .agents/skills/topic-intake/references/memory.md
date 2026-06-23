# Topic Intake Skill Memory

This file stores memory specific to the `topic-intake` skill.

Use `.agents/_shared/` for channel-wide systems and strategy.
Use this file for lessons about how this skill should suggest, score, reject, and persist topic candidates.

## Current Skill Standard

- Generate angles, not generic topics.
- Start from the shared channel brain every run because the channel can improve over time.
- Browse YouTube or the web before recommending or choosing ideas.
- Prefer the project-local vendored browse skill at `.agents/skills/browse/SKILL.md`; fall back to global gstack browse only if needed.
- Use high-view reference videos as demand and packaging evidence, not as source material to copy.
- Score candidates before recommending them.
- Show the full score breakdown for every candidate in the main table.
- Treat the first output as candidate selection, not research, script, or production.
- Do not create a project folder unless the user chooses a candidate or explicitly asks to start the project.
- When Persist Mode creates or updates `00-topic-intake.md`, treat all downstream outputs in that project as stale.
- Do not delete stale downstream outputs unless the user explicitly asks; otherwise tell the user to rerun downstream skills in order.
- Keep the channel influence-first; do not suggest topics that exist mainly to promote a product.

## Calibration From Current Best Project

Reference project:
`projects/why-everyone-pretends-to-be-busy`

Useful pattern:

- broad topic: people look busy
- sharp angle: modern life rewards visible activity over real progress
- viewer pain: people feel pressured to perform busyness
- hidden system: status, tools, visibility, and social safety reward visible activity
- recurring motif: calendar cage and fake emergency machine
- WIT role: trapped, attacked, overloaded, deadpan
- final insight: modern life confuses activity with value

Apply this pattern to future topic suggestions:

- Find the hidden system behind a familiar pain.
- Make the system happen to WIT.
- Pick one recurring object or motif before script writing.
- Protect the viewer from blame by showing the system first.
- Keep the final insight simple enough for an English learner to repeat.

## Candidate Mix

Default to a balanced batch:

- `2-3` money or spending angles
- `2-3` internet behavior angles
- `2` modern life or work-status angles
- `1-2` business or hidden pricing angles
- `1` wildcard if it still fits the channel promise

Avoid repeating active or recent production topics unless the user asks for variations.

## Feedback Log

### 2026-06-06 - Skill Created

Classification: `Core operational capability`

Created `topic-intake` as the first sequential video-production skill for `Why It Works`.

Initial memory rules:

- always read `.agents/_shared/` before suggesting topics
- keep skill-specific learning here
- promote reusable channel-wide lessons into `.agents/_shared/channel/learning-log.md`
- use the topic angle scorecard as the gate before research, packaging, hooks, scripts, or production

### 2026-06-06 - Add Reference And Score Transparency

Classification: `Topic intake lesson`

Context:
The first test run gave a ranked topic list, but the user wanted to know the exact criteria behind the score and wanted internet or YouTube references before choosing an idea.

Lesson:
Topic intake should not choose from internal judgment only. It should compare candidates against high-view reference videos and show the full score breakdown for each candidate.

Apply next time:

- browse YouTube or the web before recommending topic ideas
- list reference videos with channel, URL, visible views when available, and what to learn
- show all `8` score criteria per candidate, then sum to `/40`
- use references as demand and packaging signals, not as material to copy

Promote to shared memory:
no, this is currently a topic-intake skill behavior rather than a channel-wide strategy change.

### 2026-06-06 - Prefer Project-Local Browse

Classification: `Operational lesson`

Context:
The user noted that references to global skills may break when the project runs on another PC.

Lesson:
Topic intake should prefer project-local vendored skill dependencies when possible, then fall back to global skills only when necessary.

Apply next time:

- use `.agents/skills/browse/SKILL.md` for browsing instructions
- use `.agents/skills/browse/dist/browse.exe` on Windows when available
- if local browse is unavailable, say so clearly and then use global gstack browse if installed

Promote to shared memory:
yes, this is a portability rule for project-local skills.

### 2026-06-06 - Pipeline Stale Cascade

Classification: `Operational lesson`

Context:
The user clarified that every skill should behave as part of a sequential production pipeline.

Lesson:
`topic-intake` is the first step. It does not require previous outputs, but changing its output makes research, script, packaging, and later production files stale.

Apply next time:

- when creating or updating `00-topic-intake.md`, check for `01-research-pack.md`, `02-script.md`, `03-packaging.md`, and later downstream files
- list downstream files that are now stale
- tell the user to remove stale files or rerun downstream skills in order, starting with `research-pack`
- do not remove downstream files unless the user explicitly asks

Promote to shared memory:
yes, this is a channel-wide pipeline rule.

### 2026-06-21 - Pre-Chosen Topic + External Script Is Persist Mode

Classification: `Topic intake lesson`

Context:
The user brought the `Why Everyone Pretends To Be Busy` topic with a complete external
script (`why-people-pretend-to-be-busy.md`) and asked to "run the full workflow, starting
with topic-intake." This topic was the channel's quality benchmark in skill memory but had
never been made into a real project folder.

Lesson:
When the user arrives with an already-chosen topic (and possibly a finished script) and asks
to start the pipeline at step 0, this is Persist Mode, not Suggest Mode. Still browse for
reference demand evidence and run the full scorecard, then persist `00-topic-intake.md`.

Apply next time:

- Treat a named topic + "run the workflow" as Persist Mode; create only `00-topic-intake.md`.
- Reconcile the slug to the established canonical name from the channel brain when one exists
  (used `why-everyone-pretends-to-be-busy`, not the download filename `why-people-pretend-to-be-busy`).
- Do NOT copy an externally-provided script into `02-script.md` at step 0. The script enters via
  `script-draft` after `research-pack`, so research can ground it; note its existence in the intake file.
- Still satisfy the browsing + full scorecard requirements even when the topic is pre-chosen.

Promote to shared memory:
no, this is topic-intake intake-mode behavior, not a channel-wide strategy change.

### 2026-06-24 - User-Brought Pricing Claim: Verify Math Before Persisting

Classification: `Topic intake lesson`

Context:
The user floated their own angle ("Buy 1 Get 1 Free makes more profit than 50% off, isn't
it? but it looks the same"). It scored highest in the batch (`39/40`) and had the strongest
proven demand found all session (Vox "Why 'Buy one, get one free' isn't a great deal" ~3.7M).
Persisted as `projects/why-buy-1-get-1-beats-50-off/00-topic-intake.md`.

Lesson:
When the user brings a topic built on a math/economics/pricing claim, verify the actual
mechanism with a worked numeric example BEFORE scoring or persisting, and bake an honesty
guardrail into the intake file. For BOGO vs 50% off: BOGO ~2x the store's gross profit ONLY
when margin > 50% (item costs under half its price) AND the shopper takes both units; and the
two deals are not equal for the buyer either (50% off keeps cash if you only need one). The
channel angle is the contradiction ("same deal, double profit / free cuts your judgment"), not
a blanket "BOGO is always more profit."

Apply next time:
- For any "X is more profitable / cheaper / a trick" idea, build the small worked example first.
- Write a "must stay honest" section into `00-topic-intake.md` stating the conditions under which
  the claim holds, so research and script inherit the guardrail.
- A user's own idea is still Suggest Mode until they say "start"/"I choose that"; only then Persist.
- Confirming the user's instinct (with the precise condition) builds trust; don't just validate blindly.

Promote to shared memory:
no, this is topic-intake verification behavior, not a channel-wide strategy change.

## Feedback Entry Template

Use this shape when updating the skill after user review:

```markdown
### YYYY-MM-DD - <short lesson>

Classification: `Topic intake lesson` / `Operational lesson` / `Experiment`

Context:

Lesson:

Apply next time:

Promote to shared memory:
yes/no, with reason
```
