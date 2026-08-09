---
name: metadata
description: Generate publish-ready HumanPrice titles, description, chapters, hashtags, and SEO tags from a finished script and research brief. Use for YouTube metadata, title options, descriptions, chapters, hashtags, tags, or SEO packaging.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# metadata

Packaging stage for HumanPrice.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/channel-dna.md`
- `.agents/rules/research-standards.md`
- `.agents/rules/file-formats.md`
- `.agents/skills/metadata/references/memory.md`

## Inputs

Read one finished `script_*.md`, its `research/research-brief.md`, and
`transcribes/transcript.md` when chapters are requested. If the transcript is absent,
write chapter labels without fabricated timestamps and clearly mark timestamps pending.

## Build the package

Produce five title candidates in the five slots defined by `channel-dna.md`:

1. canonical series title;
2. contradiction;
3. hidden price;
4. beneficiary or system reveal;
5. quantified claim.

Every title should begin with or preserve `The Economics of [Behavior]` when natural.
Keep the recommended title concise enough for mobile. Exact numbers are allowed only if
the research brief explicitly clears them for title use.

Write a two-paragraph description. The first two lines must communicate the behavior,
contradiction, and payoff without clickbait. Mention HumanPrice naturally once.

Include 4 to 6 chapters for an 8 to 12 minute episode, 12 to 20 hashtags, and 25 to 40
SEO tags. Tags should combine behavioral economics, money psychology, hidden costs,
consumer psychology, the specific behavior, and relevant institutions or mechanisms.

## Output

Write `outputs/metadata.md` using the exact structure in `file-formats.md`. Mark one title
`Recommended` and add one sentence explaining the choice. Do not include unsupported
claims, extra research, or copied competitor language.

Report the saved path. If cast is ready, say `/thumbnail` can run next.

## Self-improvement

Append durable title and packaging lessons to `references/memory.md` only after real
performance data or explicit user feedback exists.
