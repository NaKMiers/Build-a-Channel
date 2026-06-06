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
