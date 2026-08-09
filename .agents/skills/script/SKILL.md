---
name: script
description: Write a sourced 8 to 12 minute HumanPrice narration from an approved research brief and save it at the project root. Use when the user asks for a script, narration, outline-to-script conversion, or the next writing stage.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# script

Stage 3 of the HumanPrice pipeline. The research brief is a hard input, not optional
background.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/channel-dna.md`
- `.agents/rules/research-standards.md`
- `.agents/rules/file-formats.md`
- `.agents/skills/script/references/memory.md`

## Inputs and gate

Resolve one project and read `research/research-brief.md`. Stop and direct the user to
`/research` if it is missing, lacks the required source count, or leaves a load-bearing
claim unsupported.

## Write the narration

Write 1,250 to 1,750 words, with hard bounds of 1,150 to 1,850. Aim for 8 to 12 minutes
at a natural explanatory pace. Use second person where it makes the behavior immediate,
but vary sentence openings so the voice remains natural.

Follow the 14-step reveal ladder in `channel-dna.md`:

1. familiar moment;
2. visible price or obvious explanation;
3. contradiction before 0:25;
4. one-sentence reframe before 1:00;
5. unit economics based on one person or transaction;
6. incentive map;
7. behavioral engine;
8. hidden money machine or hidden cost;
9. mid-video reveal that changes the category;
10. scale from one person to the system;
11. one strong case study;
12. one counterargument or boundary case;
13. realistic stress test;
14. human price and a category-reframe ending that echoes the opening.

Use only claims and numbers in the brief. You may simplify wording but not strengthen
causality, erase context, or turn an estimate into a fact. Use concrete arithmetic when
it clarifies the mechanism. Do not put citations, stage directions, headings, timestamps,
or source notes in the spoken narration.

## Voice

- Curious, financially literate, and humane.
- Clear enough for a general viewer without talking down to them.
- Tension comes from contradiction and incentives, not alarmism.
- Explain why rational people participate before showing the cost.
- No moral panic, diagnosis, mockery, or fake insider authority.
- No em dash character.

## Output

Save only the finished narration as `script_<short_slug>.md` at the project root. Count
words and revise until the file passes the target range. Report the path and word count.

Then say: `Next: /transcript, /cast, and /metadata can run from this script.`

## Self-improvement

Append only durable writing lessons to `references/memory.md` after the user accepts the
script.
