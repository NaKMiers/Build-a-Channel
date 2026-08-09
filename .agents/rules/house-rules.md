# House rules - output hygiene, always active

Applies to every skill, every file written, and every chat reply in this repository.
Both Codex and Claude read this file.

## Writing

- **Never use the em dash character.** Not in scripts, titles, descriptions, tags,
  prompts, rule files, or chat replies. Use a plain hyphen, a comma, or a period.
  This applies to files you write and to what you say.
- ASCII only, unless the artifact genuinely needs otherwise. Two sanctioned exceptions,
  and no others:
  1. The middle dot `·` used as a separator in prompt-file cast lines, matching the
     existing project.
  2. `research/videos-swipe/*/visual-analysis.md` is written in Vietnamese with
     diacritics, as are the section names that `.agents/skills/video-swipe/SKILL.md`
     quotes to specify them. These are notes the owner reads, not anything an image model
     or a downstream tool parses, and unaccented Vietnamese was ambiguous enough to have
     already produced two unreadable sentences. The em dash ban still applies, and every
     file name, timestamp, on-screen string, and quoted rule inside them stays verbatim.
- Never say "sure", "great", "absolutely", or any filler. Go straight into output.
- Keep progress updates concise and concrete.

## Stage discipline

- The pipeline order is topic -> research -> script -> transcript, cast, and metadata ->
  scenes and thumbnail, with `check` runnable at any point. Never generate image
  prompts before the cast exists.
- Every skill validates its preconditions first and stops with a clear message if an
  input is missing. Do not improvise around a missing input.
- Every skill ends by naming the next command to run.
- If the user asks to redo a stage, redo only that stage.

## Never ask the user about the channel

The channel style, palette, voice, pillars, and cast identity are all in `.agents/rules/`.
Never ask the user to describe them. Read the rule file.

## File writing

- Read `.agents/rules/file-formats.md` before writing any project artifact, and match
  the shape exactly. Downstream image tools split prompt files on newlines, so a
  wrapped line is a broken prompt, not a cosmetic issue.
- Never create a file the user did not ask for and the format spec does not name.

## Guarding the verbatim style strings

The style string and generation string are defined once in
`.agents/rules/visual-style.md`. That file is authoritative. Project prompt artifacts may
copy them verbatim. Skills and validators must source them through
`.agents/bin/style-strings.sh`, never maintain another hard-coded copy.

If either string changes, edit `visual-style.md` first, then run `/check` on every active
project. A partial copy is a validation failure.
