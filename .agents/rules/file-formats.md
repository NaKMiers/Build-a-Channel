# HumanPrice file formats and project layout

Canonical source for every project artifact. Read this before writing inside `projects/`.
The `check` skill validates this contract.

## Project layout

```text
projects/<n>-<title-slug>/
  script_<short_slug>.md
  research/
    research-brief.md
  audios/
    part-1.mp3
    part-2.mp3
    full.mp3
  characters/
    NAME.jpeg
  outputs/
    metadata.md
    captions/
      english.srt
      spanish.srt
      japanese.srt
      chinese.srt
      hindi.srt
    thumbnail-N.jpg
  prompts/
    character-prompts.md
    visual-plan.md
    image-prompts.md
    thumbnail-prompts.md
    video-prompts.md
  scenes/
    [M-SS].jpg
  transcribes/
    transcript.md
    transcript-min5.md
    words.json
    offsets.json
```

Rules:

- Root holds narration only. Research, prompts, media, and packaging stay in subfolders.
- `outputs/` and `audios/` are plural.
- Audio is gitignored. Keep `.gitkeep` in generated-media directories.
- Prose uses `.md`. Machine data uses `.json` or `.csv`.
- Character sheets use `.jpeg`.
- `<n>` is one greater than the highest current project number. Start at 1 when none exist.
- `<title-slug>` is lowercase hyphen-separated title text.
- `<short_slug>` is a concise lowercase underscore-separated subject.

## `research/research-brief.md`

```markdown
# Research brief - <Working Title>

## Central question

<one question>

## Familiar moment

<concrete viewer moment>

## Common belief

<what people normally assume>

## Contradiction

<what breaks that assumption>

## One-sentence reframe

<category-changing thesis>

## Unit economics

<one person or transaction>

## Incentive map

| Actor | Pays | Receives | Controls | Incentive |
| ----- | ---- | -------- | -------- | --------- |

## Behavioral engine

<mechanism and evidence>

## Hidden system and mid-video reveal

<the second major reveal>

## Case study

<one strong case>

## Counterargument and boundary conditions

<where the thesis weakens or changes>

## Human price

<money, time, attention, autonomy, opportunity, or emotion>

## Claim ledger

| ID  | Claim | Type | Source | Year | Geography | Definition | Script use     |
| --- | ----- | ---- | ------ | ---- | --------- | ---------- | -------------- |
| C01 | ...   | FACT | S01    | 2025 | US        | ...        | unit economics |

## Sources

- S01: [Source title](https://example.com)
```

The file uses 6 to 10 sources and at least 3 primary or official sources. Every material claim
has a source ID. `ILLUSTRATION` rows may use `N/A` for Source but must show their inputs.

## `script_<short_slug>.md`

Pure English narration, 1,250 to 1,750 words. Hard limits are 1,150 and 1,850.

No title, headings, bullets, Markdown markers, citations, URLs, stage directions, or visual cues.
The forced aligner flattens every token, so formatting becomes spoken garbage and corrupts
alignment.

The research brief carries citations. The narration carries the explanation.

## `transcribes/transcript.md`

One cue per line:

```text
[0:00] You look down at the payment screen.
[0:03] Eighteen percent. Twenty percent. Twenty-five.
```

An 8 to 12 minute episode normally produces 180 to 320 cues depending on pause profile. The
real recording controls the count.

## `prompts/character-prompts.md`

```markdown
# Character reference sheets - <Video Title>

Cast derived from `../script_<short_slug>.md`.
Visual style: HumanPrice current
Master brand: Toss blue #2E77C4
Chapter palette: Olive #6F7D3C, Terracotta #C86B3C, <one extension color>
Style rules: `.agents/rules/cast-identity.md` and `.agents/rules/visual-style.md`
Protagonist identity lock: `brand/PROTAGONIST.jpeg` when present

| Token | File     | Who they are    | Setting | Where they appear        |
| ----- | -------- | --------------- | ------- | ------------------------ |
| @YOU  | YOU.jpeg | viewer stand-in | modern  | hook, mechanisms, ending |

---

**YOU.jpeg**
```

<one reference-sheet prompt>
```
```

Use one fenced block per cast entry. Tokens are one ALL-CAPS ASCII word. Cast size is 2 to 6.

## `prompts/visual-plan.md`

```markdown
# Visual plan - <Video Title>

Visual style: HumanPrice current
Master brand: Toss blue #2E77C4
Chapter colors: <olive, terracotta, one extension>
Recurring motif: <one concrete economic object>

| Beat | Time   | Meaning                   | Register | Shot | Tier        | Asset | Plate | Source | Delta | Motif   | Text |
| ---- | ------ | ------------------------- | -------- | ---- | ----------- | ----- | ----- | ------ | ----- | ------- | ---- |
| B001 | [0:00] | viewer faces a tip screen | STORY    | pov  | ATMOSPHERIC | PLATE | P001  | -      | -     | receipt | -    |
```

Enums:

- Register: `STORY`, `CARD`, `DIAGRAM`, `TRANSACTION`, `PORTRAIT`, `HYBRID`, `SPLIT_OR_SCALE`.
- Shot: `wide`, `medium`, `close`, `macro`, `overhead`, `pov`, `card`, `diagram`, `scale`.
- Tier: `CLEAN`, `LAYERED`, `ATMOSPHERIC`.
- Asset: `PLATE`, `VARIANT`, `CALLBACK`, `CAPCUT`.

Every non-plate points backward and names one information-changing delta. One row stays on one
physical line.

## `prompts/image-prompts.md`

Prompts only. The first byte is `[`. One unbroken prompt line per generated timestamp, one blank
line between records. A lone `---` line cuts the Google Flow inheritance chain and creates no
image.

```text
[0:00] <STYLE STRING> <scene> <GENERATION STRING>

---

[0:03] <STYLE STRING> <scene> <GENERATION STRING>
```

Copy timestamps exactly from the transcript. A duplicate timestamp may advance the second file by
one second to prevent overwrite. Scene filenames replace `:` with `-`.

## `prompts/thumbnail-prompts.md`

Exactly five complete prompt lines separated by exactly one blank line. No header, labels,
separate attachment-instruction lines, or commentary. Every prompt line includes the
canonical Image 1 asset-binding sentence required by `.agents/skills/thumbnail/SKILL.md`.
The lines map to `thumbnail-1.jpg` through `thumbnail-5.jpg`.

## `outputs/metadata.md`

```markdown
# Metadata - <Video Title>

## Title
```

<primary title>
```

### All five title variants

| Slot | Formula                                          | Title      |
| ---- | ------------------------------------------------ | ---------- |
| A    | The Economics of [Behavior]                      | ...        |
| B    | The Economics of [Behavior]: Why [Contradiction] | ...        |
| C    | The Hidden Cost of [Behavior]                    | ...        |
| D    | Who Really Profits When You [Behavior]?          | ...        |
| E    | Verified exact-number variant                    | ... or N/A |

## Description

```
<hook and summary>

Chapters:
M:SS  <chapter>
...

<call to action>

#hashtag ...
```

## Tags

```
<25 to 40 comma-separated tags>
```

```

Use 4 to 6 chapters and 12 to 20 hashtags. Exact-number title slot E may be `N/A` when the
research brief does not support one.
```
