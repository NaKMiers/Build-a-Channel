---
name: topic-intake
description: Generate and evaluate next-video topic ideas for the Why It Works YouTube channel. Use when the user asks for topic intake, next video ideas, raw topic candidates, scored video angles, or step 0 of the Why It Works video workflow; reads the shared channel brain and this skill's memory, browses YouTube or the web for high-view reference videos, shapes ideas into angle packages, scores each criterion, and optionally writes a project topic-intake file when a candidate is chosen.
---

# Topic Intake

## Purpose

Run step `0` of the `Why It Works` video workflow: turn raw topic possibilities into sharp, scored video angle candidates.

The output is not a generic idea list. It should be a small set of usable angle packages that connect topic, contradiction, visual metaphor, WIT role, thumbnail tension, first `10` seconds, English learner value, and final insight.

## Pipeline Position

This is step `0` of the video workflow.

It has no previous required output.

When Persist Mode creates, updates, or reruns `projects/<slug>/00-topic-intake.md`, every later output in the same project becomes stale:

- `01-research-pack.md`
- `02-script.md`
- `03-packaging.md`
- `04-voiceover.md`
- `05-visual-plan.md`
- `06-production-board.md`
- `07-review.md`
- `08-upload.md`
- `09-self-learning.md`

List stale downstream files in chat. Do not silently delete them. Remove stale downstream files only when the user explicitly asks; otherwise downstream skills must be rerun in order.

## Required Context

Read these before generating or persisting topic ideas:

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/_shared/channel/current-state.md`
4. `.agents/_shared/channel/channel-foundation.md`
5. `.agents/_shared/channel/channel-guardrails.md`
6. `.agents/_shared/channel/reference-channels.md`
7. `.agents/_shared/channel/learning-log.md`
8. `.agents/_shared/channel/codex-collaboration.md`
9. `.agents/_shared/channel/production-workflow.md`
10. `.agents/_shared/systems/topic-packaging-hooks.md`
11. `.agents/_shared/systems/script-learner-voice.md`
12. `references/memory.md`

For quality calibration, inspect recent project examples when available, especially:

- `projects/2-why-everyone-pretends-to-be-busy/02-script.md`
- `projects/2-why-everyone-pretends-to-be-busy/03-packaging.md`
- `projects/2-why-everyone-pretends-to-be-busy/04-visual-plan.md`

## Reference Browsing Requirement

Before recommending or choosing topic ideas, browse YouTube or the web for reference videos with strong view signals.

Use the project-local `/browse` skill at `.agents/skills/browse/SKILL.md` for all browsing when available. This skill is vendored from gstack so the project does not depend only on global skills installed on one machine.

If the project-local browse skill is missing or its binary cannot run, fall back to the global gstack `/browse` skill. Do not use other browser tools for web research in this workspace unless the user explicitly approves a fallback.

For each serious candidate, find at least `1` relevant reference video, preferably `2`, that shows audience demand, packaging patterns, or angle risk. Prioritize videos with many views, clear titles, strong topic fit, and adjacent audience overlap.

Record:

- reference title
- channel
- URL
- visible view count if available
- why it matters for this candidate
- what to learn without copying

Use reference videos as evidence of demand and packaging shape, not as permission to copy a premise, thumbnail, joke, script, or frame.

If browsing fails, say so clearly, mark `Reference confidence: low`, and do not invent view counts.

## Request Modes

Choose the narrowest useful mode.

### Suggest Mode

Use when the user asks for topic ideas, next-video ideas, or topic intake without naming a final choice.

Return candidates only. Do not create a project folder unless the user asks.

### Persist Mode

Use when the user selects a topic or asks to start the next video project.

Create or update only `projects/<slug>/00-topic-intake.md` from the chosen angle. Do not create research, script, packaging, voice, visual plan, HyperFrames, or upload files beyond the project template unless explicitly asked.

If updating an existing `00-topic-intake.md` and downstream outputs already exist, treat those downstream outputs as stale after the update. Tell the user to remove them or rerun downstream skills in order, starting with `research-pack`.

### Improve Memory Mode

Use when the user reviews topic suggestions, rejects candidates, chooses a direction, or gives a lesson that should improve future topic intake.

Update the active project first if a project exists, then this skill's `references/memory.md`, then shared memory only when the lesson is reusable across the channel.

## Workflow

1. Rebuild channel context from the required files.
2. Identify recent or active topics so candidates do not repeat the same promise.
3. Generate `8-12` raw topic ideas across the channel lanes:
   - money and spending
   - internet behavior
   - modern life problems
   - business and hidden systems
   - work, status, attention, and social behavior
4. Convert each raw idea into `1-2` sharper angles using:

```text
topic + contradiction + visual metaphor + viewer pain
```

Use the sentence test:

```text
This video is about how _____ looks like _____, but is actually _____.
```

5. Reject or revise angles that trigger hard fails:
   - generic education
   - advice or motivation without a hidden system
   - no repeated visual motif
   - no clear WIT emotional role
   - no real-life object, UI, paper, receipt, product, or phone evidence
   - obvious final insight
   - weak English learner fit
   - unsafe, copied, misleading, or rage-bait packaging
   - too close to direct product promotion
6. Browse YouTube or the web for high-view reference videos for each serious candidate.
7. Use the reference signal to revise, reject, or strengthen candidate angles.
8. Score the strongest angles with `.agents/_shared/systems/topic-packaging-hooks.md`.
9. Keep the best `5-7` candidates and recommend the top `1-3`.
10. For the best candidate, include concrete next-step readiness: what would become research, packaging, and first `10` seconds.
11. In Persist Mode, create or update only `projects/<slug>/00-topic-intake.md`.
12. After updating `00-topic-intake.md`, run the stale downstream check and list later outputs that must be removed or rerun.

## Output Format

In Suggest Mode, use this structure:

```markdown
## Best Next Pick

- Working title:
- Sharp angle:
- Why this one:
- Score:
- Main risk:

## Candidate Table

| Rank | Working title | Ref signal | Curiosity | Relatability | Visual motif | Humor | English fit | Depth | Packaging | Feasible | Total | Decision |
| ---: | ------------- | ---------- | --------: | ----------: | -----------: | ----: | ----------: | ----: | --------: | -------: | ----: | -------- |

## Reference Evidence

| Candidate | Reference video | Channel | Views | URL | What to learn |
| --------- | --------------- | ------- | -----: | --- | ------------- |

## Top Candidate Details

### 1. <working title>

- Topic:
- Viewer pain:
- Hidden system:
- Main contradiction:
- Recurring visual metaphor:
- Thumbnail tension:
- First 10 seconds:
- WIT role:
- Real-life objects:
- English learner value:
- Final insight:
- Score breakdown:
  - Curiosity: __ / 5
  - Relatability: __ / 5
  - Visual motif: __ / 5
  - Humor potential: __ / 5
  - English learner fit: __ / 5
  - Explanation depth: __ / 5
  - Packaging strength: __ / 5
  - Production feasibility: __ / 5
  - Total: __ / 40
- Reference confidence:
- Score notes:
- Required fixes before research:

## Parked Or Rejected

- <idea>: <reason>

## Next Step

Pick one candidate, ask for revisions, or ask me to start `projects/<slug>/00-topic-intake.md`.
```

In Persist Mode, write the chosen candidate into:

```text
projects/<slug>/00-topic-intake.md
```

Use the template fields from `projects/_template/00-topic-intake.md`, plus the full topic angle package and scorecard.

## Quality Bar

Use `Why Everyone Pretends To Be Busy` as the current quality reference:

- It is not just a workplace productivity topic; it is a social mechanism about visible busyness becoming status, safety, and fake urgency.
- It avoids accusing the viewer; the system pressures WIT before WIT performs the behavior.
- It has a recurring visual motif: calendar cage and fake emergency machine.
- It has a clear WIT role: trapped, attacked, overloaded, deadpan.
- It creates boardable scenes before script polish.
- It ends with a useful insight in simple English: modern life confuses activity with value.

Topic candidates should aim for that level of specific contradiction and visual carry.

## Self-Improvement

Read `references/memory.md` every run.

Update skill memory when:

- the user chooses a candidate and explains why
- the user rejects candidates and gives taste feedback
- a topic later fails research, packaging, hook, or production
- a repeated pattern appears in good or weak topic suggestions

Promote lessons into `.agents/_shared/channel/learning-log.md` only when they can improve the whole channel. Classify each promoted lesson as `Core`, `Experiment`, `Operational lesson`, or `Reject` according to `.agents/_shared/channel/channel-guardrails.md`.

Do not rewrite channel foundation, audience, tone, or content pillars from one topic-intake run without explicit user confirmation.
