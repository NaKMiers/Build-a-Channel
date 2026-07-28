---
name: script
description: Write the full 1,800 to 2,500 word 2nd-person narration script for a TossExplains video and save it as script_<short_slug>.md at the project root. Use when the user says "script", "write the script", "write the narration", or picks a topic to develop.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# script

Stage 2 of the TossExplains pipeline. Turns a chosen title into the narration file that
every later stage depends on.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/channel-dna.md` - the whole file. The pillar split, the researcher
  requirement, the rhythm, the arc, and the editorial guardrails all live there.
- `.agents/rules/file-formats.md` - the `script_<short_slug>.md` section
- `.agents/skills/script/references/memory.md`

## Preconditions

You need a title. Either the user just picked one from `/topic`, or they typed one.

```bash
ls -d projects/*/ 2>/dev/null
```

- If a scaffolded project folder exists but has no `script_*.md`, that is the target.
- If the user gave a title with no project folder, scaffold one first exactly as
  `/topic` Step 4 does, then continue.
- If the target project already has a `script_*.md`, stop and ask whether to overwrite.
  Never silently replace a script: the transcript, cast, and 250 image prompts
  downstream are all derived from it.

## Step 1 - Plan the three pillars before writing a word

Silently decide, and do not print:

- The **psychological mechanism**, named, and the one vivid experiment you will describe
  in plain language.
- The **ancestral condition** that installed it, and what the life-or-death stakes were.
- The **one shift** the viewer can make tonight, which must fall out of the science
  rather than being bolted on.
- The **3 or more named researchers**: at least 2 psychologists, neuroscientists, or
  behavioral scientists, and at least 1 anthropologist, ethnographer, or cross-cultural
  researcher. Name real people and real findings. If you are not confident a study says
  what you want it to say, choose a different study rather than bending it.
- The **first line** and the **closing line that echoes it, completely reframed**. Write
  both before writing the body, because the echo is the hardest thing to retrofit.

If you cannot fill all five slots, the topic is not ready. Say so instead of writing a
weak script.

## Step 2 - Write the script

Follow `channel-dna.md` exactly:

- 1,800 to 2,500 words.
- Calm, intelligent, 2nd-person throughout. Never "we" or "I".
- Rhythm: Short sentence. Short sentence. One longer sentence that adds depth. Short
  sentence. Question every 4 to 6 sentences.
- Body proportions: psychology roughly 35 percent, anthropology roughly 30 percent,
  modern mismatch plus the shift roughly 35 percent, in that order.
- Every scientific term decoded in plain English immediately.
- The shift is ONE core action, delivered as a reframe, never a numbered list, never
  commands.
- Never shame the viewer, never diagnose, never prescribe, never mention medication.

## Step 3 - Write the file

Path: `projects/<n>-<title-slug>/script_<short_slug>.md`

`<short_slug>` is a shortened topic slug, lowercase, underscore separated. It does not
have to match the full folder slug. The existing example is
`script_why_you_feel_lonelier_in_a_crowd.md` inside
`projects/1-why-you-feel-lonelier-in-a-crowd-than-alone-in-your-room/`.

**The file contains the narration and nothing else.** No heading, no title line, no
markdown syntax of any kind, despite the `.md` extension. This is a hard requirement, not
a style preference: `tools/audio-to-timestamps.py` flattens the whole file into one word
stream for forced alignment, so a stray `##` or `**` becomes a spoken token and corrupts
every timestamp after it.

Verify after writing:

```bash
F="projects/<n>-<slug>/script_<short_slug>.md"
wc -w "$F"
grep -nE '^#|\*\*|^- |^[0-9]+\.|\[|\]' "$F" && echo "FAIL: markdown in script" || echo "clean"
grep -n "$(printf '\u2014')" "$F" && echo "FAIL: em dash" || echo "clean"
```

Both checks must pass: word count in range, and the grep finding nothing.

## Step 4 - Report and hand off

Print the full video title as a plain bold heading, the word count, and the researchers
you cited. Then:

> Script saved to `<path>`.
>
> Record the narration from this file, then run **`/transcript`** to get the timestamps.
>
> `/cast` and `/metadata` only need the script, so you can run either of those now
> without waiting for the voiceover.

## Guardrails

- Never output the script inline or in a code block. It goes in the file.
- Never invent a researcher, a study, or a finding. If the anthropology is thin, pick a
  different ancestral angle rather than fabricating an ethnography.
- Never let the anthropology become the subject. If the script would still work with the
  viewer's inner life removed, it is the wrong script. Rewrite it.
- Never end without the echo of the opening line.

## Self-improvement

Read `.agents/skills/script/references/memory.md` at the start of every run. Append when
the user rewrites a section (record what was wrong), when a researcher or study turns out
to be misattributed, or when a hook shape works especially well.
