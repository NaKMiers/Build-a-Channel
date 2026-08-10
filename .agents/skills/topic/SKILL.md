---
name: topic
description: Generate five high-potential HumanPrice episode ideas, wait for the user to choose, then scaffold one project per selection. Use for topic ideas, a new video, what to make next, or starting a HumanPrice episode.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# topic

Stage 1 of the HumanPrice pipeline.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/channel-dna.md`
- `.agents/rules/file-formats.md`
- `.agents/skills/topic/references/memory.md`

## Generate five ideas

Check existing project folders and memory so no made or rejected topic is repeated. Each
idea must center on a behavior the viewer has experienced and pass these silent tests:

- a clear transaction, price, or resource tradeoff exists;
- a credible behavioral mechanism exists;
- a hidden beneficiary, cost, subsidy, or incentive can be revealed;
- the story has enough evidence and escalation for 8 to 12 minutes;
- the framing is specific without shaming a demographic or diagnosing the viewer.

Spread the five ideas across different settings and mechanisms. Prefer the core title
`The Economics of [Behavior]`. Add a contradiction clause only when it earns curiosity.
Use an exact number only if it is already well-established and will still require
verification in `/research`.

Output only:

```markdown
| # | Video Title |
| --- | --- |
| 1 | [Title] |
| 2 | [Title] |
| 3 | [Title] |
| 4 | [Title] |
| 5 | [Title] |
```

Then stop with:

> **Which idea do you want to develop? Reply with a number (1-5).**

Write no files before the user selects.

## Scaffold selected ideas

For every selected number, create a separate `projects/<n>-<title-slug>/` using the next
available positive integer. Create:

```text
research/
audios/
transcribes/
prompts/
outputs/
scenes/
```

Do not invent a script or research brief during scaffolding. Report every created path
and say: `Next: run /research for the selected project.`

## Self-improvement

Append made or explicitly rejected titles to `references/memory.md` after selection.
