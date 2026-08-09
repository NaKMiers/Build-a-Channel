---
name: research
description: Research a HumanPrice topic and write the sourced evidence brief that gates scriptwriting, titles, thumbnails, and metadata. Use after a topic is selected, or when the user asks to research, fact-check, source, validate claims, or build an evidence brief for an episode.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - WebSearch
  - WebFetch
---

# research

Stage 2 of the HumanPrice pipeline. It turns a selected topic into a claim ledger that
the rest of the episode is allowed to use.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/channel-dna.md`
- `.agents/rules/research-standards.md`
- `.agents/rules/file-formats.md`
- `.agents/skills/research/references/memory.md`

## Inputs

Resolve one project under `projects/<n>-<slug>/`. The project must already contain the
selected title in its folder name or a user-provided topic statement.

If multiple projects could match, ask for the project number. Do not research several
episodes into one brief.

## Workflow

1. State the episode's familiar behavior, economic mechanism, behavioral engine, and
   likely human price as working hypotheses.
2. Browse the web. Research current or potentially changed facts from primary sources
   first, then add high-quality synthesis where it improves interpretation.
3. Collect 6 to 10 sources, including at least 3 primary or official sources.
4. Build the claim ledger. Label every entry `FACT`, `ESTIMATE`, `INFERENCE`, or
   `ILLUSTRATION`.
5. For every exact number, record geography, time period, unit, population, and the
   arithmetic used to derive it. Never silently combine unlike denominators.
6. Separate association from causation. Record uncertainty and meaningful contrary
   evidence.
7. Identify which claims may be used in the title or thumbnail. A number is not cleared
   unless the source directly supports it and the context remains honest when compressed.
8. Convert the evidence into a 14-step reveal map matching `channel-dna.md`.
9. Write `research/research-brief.md` in the project folder using the exact contract in
   `file-formats.md`.

## Quality gate

Do not hand off to `/script` unless all are true:

- 6 to 10 credible sources are present and at least 3 are primary or official.
- Every load-bearing claim maps to a source or is explicitly labeled as inference.
- Every title or thumbnail number is explicitly cleared or rejected.
- The unit economics can be explained from the participant's point of view.
- The behavioral engine is supported without diagnosing or shaming the viewer.
- The final human price includes more than money when the evidence supports it.

## Completion

Report the saved path, source count, primary-source count, and title-number clearance.
Then say: `Next: run /script for this project.`

## Self-improvement

After a successful run, append only durable sourcing lessons to
`references/memory.md`. Never store episode claims there.
