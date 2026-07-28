# File formats and project layout

Canonical source for where every artifact lives and exactly how it is shaped. Read
this before writing any file into a project folder. The `check` skill validates
against this document.

## Project layout

`projects/1-why-you-feel-lonelier-in-a-crowd-than-alone-in-your-room/` is the worked
example. Every new project matches it.

```
projects/<n>-<title-slug>/
  script_<short_slug>.md      root level. Written by `script`.
  metadata.md                 root level. Written by `metadata`.
  audios/                     the recorded narration voiceover. You put files here.
  characters/                 NAME.jpeg reference sheets. You generate these.
  outputs/                    thumbnail-N.jpg and the accepted thumbnail. You generate these.
  prompts/
    character-prompts.md      Written by `cast`.
    image-prompts.md          Written by `scenes`.
    thumbnail-prompts.md      Written by `thumbnail`.
    video-prompts.md          Reserved and intentionally empty. Not missing.
  scenes/                     [M:SS].jpg scene images. You generate these.
  transcribes/
    transcript.md             Written by `transcript`.
    transcript-min5.md        Optional coarser cut, only on request.
    words.json                Forced-alignment cache. Stays .json, it is data.
```

Rules:

- **Root level holds text you read or publish.** Subfolders hold prompts and
  generated media.
- **`outputs/` is plural.** Not `output/`. So is `audios/`.
- **`audios/` holds the recorded voiceover** read from `script_<short_slug>.md`, and is the
  default place `transcript` looks for input. Multi-part recordings live here in read order,
  for example `part-1.mp3` then `part-2.mp3`. The audio itself is gitignored, so the folder
  keeps a `.gitkeep`. Never commit a recording, regenerate it from the script.
- **All prose files are `.md`.** No `.txt`. `words.json` is the one exception because
  it is data, not prose.
- **Character sheets are `.jpeg`**, matching the existing project. Not `.png`.
- `<n>` is the next integer after the highest existing project number.
- `<title-slug>` is the full title, lowercase, hyphen separated.
- `<short_slug>` is a shortened topic slug, lowercase, underscore separated, for
  example `script_why_you_feel_lonelier_in_a_crowd.md` for a much longer title.

## `script_<short_slug>.md`

1,800 to 2,500 words of pure narration and nothing else.

**The `.md` extension must not invite markdown into this file.** No headings, no
bullets, no asterisks, no brackets, no stage directions, no title heading inside the
file. Just the narration.

This is not a style preference. `tools/audio-to-timestamps.py` flattens the entire
file into one word stream for forced alignment:

```python
text = " ".join(script.read_text(encoding="utf-8").split())
```

A stray `##` or `**` becomes a spoken token and corrupts every timestamp after it.

## `transcribes/transcript.md`

One cue per line, `[M:SS] ` then the narration text.

```
[0:00] You can be surrounded by forty people and still feel like the last person on earth.
[0:04] It happened to you recently.
[0:06] A party, a train carriage,
```

A 12 minute script lands around 230 lines of roughly 3 seconds each.

## `prompts/character-prompts.md`

Header block, then the cast table, then one fenced code block per cast member, each
immediately preceded by a bold label of its file name.

```markdown
# Character reference sheets - <Video Title>

Cast derived from `../script_<short_slug>.md`.
Style rules: `.agents/rules/mascot-toss.md` and `.agents/rules/visual-style.md`
Mascot identity lock: `brand/MASCOT.jpeg`

| Token | File | Who they are | Era / setting | Where they appear |
| --- | --- | --- | --- | --- |
| @YOU | YOU.jpeg | ... | ... | ... |

---

**YOU.jpeg**

```
<full reference sheet prompt>
```
```

One code block equals one image generation. **Never merge two characters into one
block.**

## `prompts/image-prompts.md`

Header block, then one prompt per line, separated by exactly ONE blank line, no
fences, no commentary between prompts.

```markdown
# Image prompts - <Video Title>

Cast: @YOU (YOU.jpeg) · @CROWD (CROWD.jpeg) · ...
Source transcript: ../transcribes/transcript.md - <N> lines, <M> unique timestamps<duplicate note>
Attach only the reference sheets for the @ tokens that appear in a given prompt. Add to every generation: match the attached character reference exactly, no photorealism, no 3D render, no gradients, no drop shadows, no textures, no realistic faces, no anime style.

[0:00] <STYLE ANCHOR> <scene> <STYLE LOCK>

[0:04] <STYLE ANCHOR> <scene> <STYLE LOCK>
```

- Every prompt is exactly ONE unbroken line. A wrapped prompt becomes two broken
  prompts because downstream tools split this file on newlines.
- The timestamp prefix is copied character for character from the transcript. `[0:00]`
  stays `[0:00]`, `[00:00]` stays `[00:00]`. Never reformat, re-pad, or renumber:
  these strings become the scene image file names.
- If the transcript repeats a timestamp, note it in the header with the disambiguation
  the human should use, for example: `[3:24] appears twice; save the second one as
  [3:25] so it does not overwrite the first`.

## `prompts/thumbnail-prompts.md`

Header block, then exactly five unbroken lines prefixed `[thumb-a]` through
`[thumb-e]`, one blank line between, nothing after the last prompt.

The bracket name becomes that image's file name, exactly as timestamps do.

## `metadata.md`

Three sections, each holding a fenced block so the text can be copied without
markdown bleeding in.

```markdown
# Metadata - <Video Title>

## Title

```
<one viral title under 70 characters>
```

## Description

```
<hook, summary, call to action, then one hashtag line>
```

## Tags

```
<25 to 40 comma separated keywords on one line>
```
```

## `audios/` and `scenes/` and `characters/` and `outputs/`

- `audios/` holds the narration recording. One file, or `part-1`, `part-2` in read order.
  `.mp3`, `.wav`, and `.mp4` are gitignored, so only the `.gitkeep` is tracked.
- `scenes/[M:SS].jpg` where the bracket name matches the prompt's timestamp exactly.
- `characters/NAME.jpeg` where NAME matches the cast token without the `@`.
- `outputs/thumbnail-N.jpg`, and the chosen one suffixed `-accepted`.
