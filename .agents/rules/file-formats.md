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
  audios/                     the recorded narration voiceover. You put files here.
    part-1.mp3, part-2.mp3    multi-part recording, in read order.
    full.mp3                  the parts combined. Written by `transcript`.
  characters/                 NAME.jpeg reference sheets. You generate these.
  outputs/                    metadata.md, thumbnail-N.jpg, and the accepted thumbnail. You generate these.
  prompts/
    character-prompts.md      Written by `cast`.
    image-prompts.md          Written by `scenes`.
    thumbnail-prompts.md      Written by `thumbnail`.
    video-prompts.md          Reserved and intentionally empty. Not missing.
  scenes/                     [M-SS].jpg scene images. You generate these.
  transcribes/
    transcript.md             Written by `transcript`.
    transcript-min5.md        Optional coarser cut, only on request.
    words.json                Forced-alignment cache. Stays .json, it is data.
    offsets.json              Part durations from `combine-audio.py`. Multi-part only.
```

Rules:

- **Root level holds the script.** Subfolders hold prompts, generated media, and published
  packaging.
- **`outputs/` is plural.** Not `output/`. So is `audios/`.
- **`audios/` holds the recorded voiceover** read from `script_<short_slug>.md`, and is the
  default place `transcript` looks for input. Multi-part recordings live here in read order,
  for example `part-1.mp3` then `part-2.mp3`. The audio itself is gitignored, so the folder
  keeps a `.gitkeep`. Never commit a recording, regenerate it from the script.
- **`audios/full.mp3` is the combined recording**, written by `transcript` via
  `tools/combine-audio.py` whenever there is more than one part. It is the single timeline
  every `[M:SS]` in `transcript.md` refers to, and the file the editor loads. It is an
  output, never an input: collect `part-*.mp3` and exclude it. Also gitignored, and
  reproducible from the parts.
- **All prose files are `.md`.** No `.txt`. `words.json` and `offsets.json` are the
  exceptions because they are data, not prose. Keep `offsets.json`: re-merging the
  per-part word caches onto the combined timeline needs those durations, and re-measuring
  is only possible while the parts still exist.
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

**PROMPTS ONLY. No header, no title, no cast line, no commentary.** The file is a machine
input: it gets imported wholesale into an image tool that expects every line to be a prompt.
The first line of the file is the first prompt. One prompt per line, separated by exactly ONE
blank line, no fences.

```markdown
[0:00] <STYLE ANCHOR> <scene> <STYLE LOCK>

[0:04] <STYLE ANCHOR> <scene> <STYLE LOCK>
```

- Every prompt is exactly ONE unbroken line. A wrapped prompt becomes two broken
  prompts because downstream tools split this file on newlines.
- **Nothing but prompts and single blank separators.** `grep -v '^\[' | grep -c .` must be 0.
  A title line or an attachment note is not harmless decoration here, it is an extra record
  the importing tool will try to render as an image.
- The timestamp prefix is copied character for character from the transcript. `[0:00]`
  stays `[0:00]`, `[00:00]` stays `[00:00]`. Never reformat, re-pad, or renumber.
  Scene image file names replace the timestamp colon with a hyphen for Windows
  compatibility: `[0:00]` becomes `[0-00].jpg`.
- **The cast list, the cue counts, the duplicate-timestamp note, and the GENERATION LINE are
  reported in chat by `scenes` instead**, because the human needs them and the tool must not
  see them. A repeated timestamp still gets remapped in the prompts themselves, for example a
  transcript with `[3:24]` twice produces prompts `[3:24]` then `[3:25]`, so the remap is
  visible in the file without any note explaining it.

Project 1 and project 4 predate this and still carry a 4 line header block. Project 1 is the
regression fixture and must not be touched. Project 4 should be stripped before its prompts are
imported: `tail -n +7 <file> > <file>.new && mv <file>.new <file>`, then confirm the prompt
count is unchanged. Project 2 already has no header.

## `prompts/thumbnail-prompts.md`

**PROMPTS ONLY. No header, title, cast line, labels, or commentary.** The file is imported
into an image tool that splits on `\n\n`, so it contains exactly five prompt records.

- Every prompt is exactly one unbroken line.
- Prompts are separated by exactly one blank line. There is no leading blank line and no
  trailing blank line after the fifth prompt.
- The first through fifth lines map in order to `thumbnail-1.jpg` through
  `thumbnail-5.jpg`.
- Reference-sheet attachment directions, output dimensions, file names, and logo badge
  instructions are reported in chat by `thumbnail`, never written into this file.

Project 1 predates this import format and remains unchanged as the regression fixture. Its
legacy header, `[thumb-*]` labels, and blank separators are informational when validating.
Apply the prompt-only format from project 2 onward.

## `outputs/metadata.md`

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

- `audios/` holds the narration recording. One file, or `part-1`, `part-2` in read order,
  plus the `full.mp3` that `transcript` combines them into.
  `.mp3`, `.wav`, and `.mp4` are gitignored, so only the `.gitkeep` is tracked.
- `scenes/[M-SS].jpg`, derived from the matching prompt timestamp by replacing its
  colon with a hyphen. For example, `[3:20]` becomes `[3-20].jpg`.
- `characters/NAME.jpeg` where NAME matches the cast token without the `@`.
- `outputs/metadata.md`, `thumbnail-N.jpg`, and the chosen one suffixed `-accepted`.
