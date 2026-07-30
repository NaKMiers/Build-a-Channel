---
name: check
description: Validate a TossExplains project against the rule files and report what is missing or malformed, then name the next pipeline step. Checks the verbatim style strings, timestamp alignment, cast token integrity, file formats, and banned patterns. Use when the user says "check", "validate", "is this correct", "what is missing", or "audit the project".
allowed-tools:
  - Bash
  - Read
  - Glob
  - Grep
---

# check

The quality guardian. A prompt cannot verify its own output, but a skill can. This runs the
mechanical checks that the retired mega-prompt had no way to perform, then reports state
and the next step.

Read-only by default. It reports and never edits, unless the user explicitly asks it to fix
something.

## Read first

- `.agents/rules/file-formats.md` - the spec everything is validated against
- `.agents/rules/visual-style.md` - the four verbatim strings
- `.agents/rules/thumbnail-rules.md` - the thumbnail-only rendering and packaging rules
- `.agents/skills/thumbnail/references/style-spec.json` - the self-contained thumbnail style
- `.agents/skills/check/references/memory.md`

## Step 0 - Pick the project

```bash
ls -d projects/*/ 2>/dev/null
```

If the user named one, use it. If exactly one exists, use it. Otherwise use the
highest-numbered one and say which you picked.

## Step 1 - Inventory

```bash
P="projects/<n>-<slug>"
for f in script_*.md outputs/metadata.md prompts/character-prompts.md prompts/image-prompts.md \
         prompts/thumbnail-prompts.md transcribes/transcript.md; do
  ls "$P"/$f >/dev/null 2>&1 && echo "present  $f" || echo "MISSING  $f"
done
for d in audios characters outputs prompts scenes transcribes; do
  ls -d "$P/$d" >/dev/null 2>&1 && echo "present  $d/" || echo "MISSING  $d/"
done
echo "audios:     $(ls "$P"/audios/* 2>/dev/null | grep -v '\.gitkeep$' | grep -c . )"
echo "characters: $(ls "$P"/characters/*.jpeg 2>/dev/null | wc -l)"
echo "scenes:     $(ls "$P"/scenes/* 2>/dev/null | grep -v '\.gitkeep$' | grep -c . )"
echo "outputs:    $(ls "$P"/outputs/* 2>/dev/null | grep -v '\.gitkeep$' | grep -c . )"
```

The six directories are `audios/ characters/ outputs/ prompts/ scenes/ transcribes/`. A
**missing directory is a FAIL**, because the scaffold is wrong and later skills will write to
a path that does not exist.

An **empty** `audios/`, `characters/`, `scenes/`, or `outputs/` is INFO, not FAIL. Those hold
files the user generates outside this repo, so emptiness just means that step has not happened
yet. `audios/` in particular will look empty in a fresh clone even on a finished video, because
`*.mp3`, `*.wav`, and `*.mp4` are gitignored and only the `.gitkeep` is tracked.

`prompts/video-prompts.md` being empty is correct. Never report it as a problem.

## Step 2 - Repo-wide hygiene

```bash
# em dash anywhere in tracked prose
grep -rn "$(printf '\u2014')" --include='*.md' . | grep -v '^./prompts/retired/' | head -20

# .txt prose files that should be .md
find projects -name '*.txt' | head

# the verbatim strings: extract from the one definition, then find stray copies
source .agents/bin/style-strings.sh
echo "anchor ${#STYLE_ANCHOR}  lock ${#STYLE_LOCK}  gen ${#GENERATION_LINE}  sheet ${#SHEET_OPENING_LINE}"

# no other copy anywhere under .agents/ or in the root docs
grep -rlF "$STYLE_ANCHOR" .agents/ AGENTS.md 2>/dev/null | grep -v 'visual-style'
```

Any empty string means the headings in `visual-style.md` were renamed and the extractor no
longer finds them. That is a FAIL and it silently disables the anchor and lock checks
everywhere, so fix it first.

Exactly one file under `.agents/` holds the full strings: the definition in
`visual-style.md`. Scene skills source `.agents/bin/style-strings.sh` instead of hard-coding
them. Thumbnail prompts intentionally use the separate cinematic style and must not copy the
scene strings. Any file printed by the last command is a FAIL.

Project 1's `transcribes/*.txt` files are grandfathered. Report them as informational, not
as a failure.

## Step 3 - Script checks

```bash
S=$(ls "$P"/script_*.md 2>/dev/null | head -1)
wc -w "$S"                                              # 1800 to 2500
grep -nE '^#|\*\*|^- |^[0-9]+\. ' "$S" | head            # must be empty
```

- Word count outside 1,800 to 2,500 is a FAIL.
- **Any markdown syntax in the script is a hard FAIL**, not a style nit. The forced aligner
  flattens the file into a word stream, so `##` or `**` becomes a spoken token and corrupts
  every timestamp after it.

## Step 4 - Transcript checks

```bash
T="$P/transcribes/transcript.md"
grep -c . "$T"
grep -cvE '^\[[0-9]+:[0-9]{2}\] .' "$T"    # must be 0
awk '{print $1}' "$T" | sort | uniq -d      # duplicates, informational
```

- Malformed cue lines are a FAIL.
- Under 20 lines is a FAIL, the transcript is incomplete.
- Duplicate timestamps are not a failure, but they must be noted in the
  `image-prompts.md` header with the file-naming workaround. Verify that note exists.

## Step 5 - Cast checks

````bash
C="$P/prompts/character-prompts.md"
grep -oE '@[A-Z]+' "$C" | sort -u                 # tokens
grep -c '^```' "$C"                                # even, 2 per character
grep -c 'brand/MASCOT.jpeg' "$C"                   # at least 1, the YOU sheet

# 'mitten' as a POSITIVE instruction, must be 0
grep -oiE '(no|never|not) +mittens?|mittens?' "$C" | grep -civE '^(no|never|not) '
````

- Cast size outside 2 to 6 is a FAIL.
- A token that is not one ALL CAPS word of letters A to Z is a FAIL.
- Odd number of code fences means a malformed or merged sheet block. FAIL.
- `mitten` as a **positive instruction** is a FAIL. `.agents/rules/mascot-toss.md` resolved this:
  the correct hand is small splayed line fingers, and `no mitten hands` belongs in every NEGATIVE
  block. So a bare `grep -c mitten` counts the fix as the fault: it reads 11 on project 2, which is
  correct, and 8 on project 1's cast file, also correct. Use the grep above, which strips
  occurrences preceded by no, never, or not. Only project 1's `image-prompts.md` genuinely fails,
  at 30, and that is the grandfathered INFO.
- The `YOU` sheet must instruct attaching `brand/MASCOT.jpeg`.
- Every `NAME` in the cast table should have a matching `characters/NAME.jpeg`. Missing
  files are informational, the user may not have generated them yet.

## Step 6 - Image prompt checks, the big one

```bash
source .agents/bin/style-strings.sh
F="$P/prompts/image-prompts.md"
CUES=$(grep -c . "$T"); PR=$(grep -c '^\[' "$F")
echo "cues $CUES  prompts $PR"

# timestamps identical, same order, except documented duplicate remaps
diff <(awk '{print $1}' "$T") <(grep -o '^\[[0-9:]*\]' "$F")
DUPS=$(awk '{print $1}' "$T" | sort | uniq -d | wc -l)
echo "declared duplicates: $DUPS"

# anchor and lock on every prompt, compared against the one definition
echo "anchor $(grep -cF "$STYLE_ANCHOR" "$F")  lock $(grep -cF "$STYLE_LOCK" "$F")  of $PR"

# tokens used but not in the cast table
comm -13 <(grep -oE '@[A-Z]+' "$C" | sort -u) <(grep -oE '@[A-Z]+' "$F" | sort -u)

# blank-line separation: no two prompt lines adjacent
awk '/^\[/{if(prev)print NR": adjacent prompts"; prev=1; next}{prev=0}' "$F"

# PROMPTS ONLY: no header, no title, no commentary. Must be 0 from project 3 onward.
grep -v '^\[' "$F" | grep -c .
```

FAIL conditions:

- prompt count not equal to cue count
- anchor count or lock count not equal to prompt count
- any `@TOKEN` not in the cast table. `@[name]` is expected, it is part of the style lock.
- two prompt lines adjacent with no blank line between them
- any non-prompt non-blank line, **from project 3 onward**. This file is imported wholesale
  into an image tool that treats every line as a prompt, so a header becomes a junk
  generation. Projects 1 and 4 still carry a 4 line header block: report those as INFO, not
  FAIL, and say project 4 should be stripped before import. Projects 2 and 3 are already clean.

**Reading the timestamp diff.** A clean diff is a PASS. A non-empty diff is only a PASS if
every differing line is a documented duplicate remap, and there are no more of them than
`declared duplicates`. Project 1 is the canonical example: `[3:24]` appears twice in the
transcript, so the second prompt is `[3:25]` to stop the second scene image overwriting the
first, and the diff is exactly one line:

```
79c79
< [3:24]
---
> [3:25]
```

That is correct and must be reported as INFO, not FAIL. **Any differing line that is not an
accounted-for remap is a FAIL**, because a drifted timestamp means a scene image will be named
wrong.

"Accounted for" is now judged arithmetically, not by reading a note. `image-prompts.md` carries
no header from project 3 onward, so there is nowhere to declare a remap. A differing line is
accounted for when the transcript stamp is one of the `declared duplicates` and the prompt
stamp is that duplicate advanced by one second. Check that the count of differing lines does
not exceed `declared duplicates`, and that each differing pair fits that shape:

```bash
# project 3: transcript has [8:26] twice, prompts are [8:26] then [8:27]
diff <(awk '{print $1}' "$T") <(grep -o '^\[[0-9:]*\]' "$F") | grep -c '^[<>]'   # 2 lines = 1 remap
```

## Step 7 - Thumbnail checks

```bash
H="$P/prompts/thumbnail-prompts.md"
wc -l < "$H"                                                  # exactly 9
grep -cve '^$' "$H"                                          # exactly 5
grep -c '^$' "$H"                                             # exactly 4
grep -c '^Create a beautiful, high-impact YouTube thumbnail' "$H"  # exactly 5

# required clauses, each must be 5
for s in 'Reserve the top 22 percent' \
         'very thick smooth black outline' \
         'richly painted cinematic 2D' \
         'bottom-right corner visually quiet' \
         'render no other text' \
         'Integrate the headline directly into the illustrated environment' \
         'do not create a separate text band'; do
  printf '%-52s %s\n' "$s" "$(grep -c "$s" "$H")"
done

# banned patterns, must be 0
grep -ciE 'competitor thumbnail|research thumbnail|style reference image' "$H"
grep -ciE 'no gradients, no shadows, no textures|educational YouTube explainer doodle style' "$H"
grep -cE '^#|^\[thumb-|^Cast:|^Five candidate|^Attach only|^Add the channel logo' "$H"

# headline text: 1 to 4 uppercase words, question or short statement
grep -oE 'exact headline "[^"]*"' "$H"

# tokens used but not in the cast table, must be empty
comm -13 <(grep -oE '@[A-Z]+' "$C" | sort -u) <(grep -oE '@[A-Z]+' "$H" | sort -u)
```

FAIL conditions: not exactly 5 nonempty prompt lines separated by exactly 4 blank lines,
any header, label, instruction, leading blank line, trailing blank line, or consecutive
blank lines, any required clause count below 5, any banned pattern present, any headline
longer than 4 words, any headline that is not uppercase, or any cast token not in the cast
table. The two headline-integration clauses prevent a detached text banner from returning.

Project 1 is the accepted regression fixture and predates both the thumbnail import format
and the thumbnail-only cinematic style. Report its legacy header, `[thumb-*]` labels, scene
STYLE ANCHOR and STYLE LOCK, and blank separators as INFO, not FAIL. Do not enforce the new
thumbnail commands above on project 1. Enforce the five-line cinematic prompt-only format
from project 2 onward.

Single cinematic stories are the default. Report more than one split comparison as INFO and
verify the script genuinely justifies each one. It is a FAIL only when the split does not
represent a real numeric, era, temperature, or state contrast.

## Step 8 - Metadata checks

````bash
M="$P/outputs/metadata.md"
grep -c '^#' "$M"
awk '/^## Title/{t=1} t&&/^```/{c++} c==2{exit}' "$M"
grep -oE '#[A-Za-z0-9_]+' "$M" | wc -l      # 15 to 25 hashtags
````

Title over 70 characters is a FAIL. Hashtag count outside 15 to 25, or tag count outside 25
to 40, is a FAIL. A `#` inside the tags block is a FAIL.

## Step 9 - Report

Print one table, most severe first:

```markdown
| Check                 | Result | Detail             |
| --------------------- | ------ | ------------------ |
| image prompts vs cues | PASS   | 254 / 254          |
| style lock coverage   | FAIL   | 251 of 254 prompts |
```

Use PASS, FAIL, or INFO. Then state the pipeline position and the next command:

> Next: **`/scenes`** to write the image prompts.

If everything passes and every artifact exists, say the project is fully packaged and ready
to publish.

## The regression fixture

`projects/1-why-you-feel-lonelier-in-a-crowd-than-alone-in-your-room/` is a completed and
accepted video. **Any change to a rule file or a skill must keep it passing.** Run `check`
on it after editing the pipeline. Known grandfathered INFO results there: `transcribes/*.txt`
extensions, and `image-prompts.md` containing `mitten hands` from before the hand-shape
conflict was resolved.

## Guardrails

- Read-only unless the user explicitly asks for a fix.
- Never report empty `prompts/video-prompts.md` as missing. It is a reserved slot.
- Never report missing `characters/*.jpeg`, `scenes/*`, `outputs/*`, or `audios/*` as FAIL.
  Those are generated by the user outside this repo, so they are INFO. A missing _directory_
  is still a FAIL.
- Never guess at a count. Run the command and report the number.

## Self-improvement

Read `.agents/skills/check/references/memory.md` at the start of every run. Append a new
check whenever a defect reaches a generated image that this skill could have caught
mechanically. That is the whole point of this skill: every failure becomes a permanent
check.
