# Script Draft Skill Memory

This file stores memory specific to the `script-draft` skill.

Use `.agents/_shared/` for channel-wide systems and strategy.
Use this file for lessons about selecting projects, shaping sectioned scripts, preserving source claims, improving WIT arcs, and making scripts easier to voice and board.

## Current Skill Standard

- Select the project before drafting.
- Smart-select a project only when context is clear or exactly one unfinished script candidate exists.
- Require both `00-topic-intake.md` and `01-research-pack.md`.
- Write only `projects/<slug>/02-script.md`.
- Use `projects/why-everyone-pretends-to-be-busy/02-script.md` as the structural reference when available.
- Copy the reference script's discipline, not its topic, jokes, or wording.
- Draft in sections with estimates, word counts, purpose, visual goal, narration, approval checks, and voice revision notes.
- Treat `01-research-pack.md` as the claim source of truth.
- Label risky ideas as inferences or avoid them.
- Keep the script learner-friendly, dry, concrete, and boardable.
- Stop before voiceover, packaging, visual plan, HyperFrames, renders, upload, or self-learning.
- After creating or updating a script, respond in chat with status, estimated duration, a `3-5` line brief, and the section summary table.
- Do not paste the full script into chat unless the user asks.

## Script Draft Output Standard

A good script draft should make the next voice revision easy.

It should include:

- one core thesis
- one recurring motif
- one WIT emotional arc
- a section summary table
- sectioned narration blocks
- visual goals, not full visual plans
- approval checks for future section review
- claim safety notes
- English learner notes
- a clear next-step boundary
- a concise chat response that helps the user review the output quickly

## Chat Response Lesson

After writing `02-script.md`, the user wants the chat response to include:

- script status
- estimated duration
- a `3-5` line brief for the entire script
- section summary

Apply every run. This is part of the skill output contract, not a reason to rerun the skill.

## Reference Script Lesson

The current best reference is `Why Everyone Pretends To Be Busy`.

Useful structure to preserve:

- section summary table before the full script
- each section has a job, visual goal, narration, and approval checks
- section names describe the hidden mechanism, not generic chapter numbers
- script can be implemented one section at a time
- humor comes from the system happening to WIT
- final payoff restates the useful insight in simple English

Do not preserve:

- exact number of sections
- workplace topic structure
- exact jokes
- exact pacing
- exact labels

## Feedback Log

### 2026-06-06 - Skill Created

Classification: `Core operational capability`

Created `script-draft` as step 3 of the sequential Why It Works video-production skill system.

Initial rules:

- require topic intake and research pack
- write only `02-script.md`
- structure scripts into sections
- keep claims tied to research
- include WIT, learner clarity, visual goals, and approval checks
- keep skill-specific learning here and promote only reusable channel-wide lessons upward

### 2026-06-06 - Chat Summary Required

Classification: `Script draft lesson`

Context:
After running the first script draft, the user clarified that the skill should respond in chat with a quick summary of the script output.

Lesson:
The written file is the main artifact, but the chat response must make the script easy to judge quickly.

Apply next time:
Include status, estimated duration, `3-5` line brief, and section summary in chat after creating or updating `02-script.md`. Do not rerun the skill only to produce this summary.

Promote to shared memory:
No. This is specific to the `script-draft` skill response contract.

## Feedback Entry Template

Use this shape when updating the skill after user review:

```markdown
### YYYY-MM-DD - <short lesson>

Classification: `Script draft lesson` / `Operational lesson` / `Experiment`

Context:

Lesson:

Apply next time:

Promote to shared memory:
yes/no, with reason
```
