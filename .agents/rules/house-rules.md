# House rules - output hygiene, always active

Applies to every skill, every file written, and every chat reply in this repository.
Both Codex and Claude read this file.

## Writing

- **Never use the em dash character.** Not in scripts, titles, descriptions, tags,
  prompts, rule files, or chat replies. Use a plain hyphen, a comma, or a period.
  This applies to files you write and to what you say.
- ASCII only, unless the artifact genuinely needs otherwise. The one sanctioned
  non-ASCII character is the middle dot `·` used as a separator in prompt-file cast
  lines, matching the existing project.
- Never say "sure", "great", "absolutely", or any filler. Go straight into output.
- Never explain what you are about to do. Just do it.

## Stage discipline

- The pipeline order is topic -> script -> transcript -> cast -> scenes ->
  metadata -> thumbnail, with `check` runnable at any point. Never generate image
  prompts before the cast exists.
- Every skill validates its preconditions first and stops with a clear message if an
  input is missing. Do not improvise around a missing input.
- Every skill ends by naming the next command to run.
- If the user asks to redo a stage, redo only that stage.

## Never ask the user about the channel

The channel style, palette, voice, pillars, and mascot are all in `.agents/rules/`.
Never ask the user to describe them. Read the rule file.

## File writing

- Read `.agents/rules/file-formats.md` before writing any project artifact, and match
  the shape exactly. Downstream image tools split prompt files on newlines, so a
  wrapped line is a broken prompt, not a cosmetic issue.
- Never create a file the user did not ask for and the format spec does not name.

## Guarding the verbatim strings

The STYLE ANCHOR, STYLE LOCK, GENERATION LINE, and REFERENCE SHEET OPENING LINE are
**defined** in `.agents/rules/visual-style.md`. That file is the authority.

Three other places legitimately contain a copy, and no others:

1. `.agents/rules/thumbnail-rules.md`, inside the two layout templates, because a
   template has to be copy-pasteable to be useful.
2. The verification grep patterns in `.agents/skills/scenes/SKILL.md` and
   `.agents/skills/check/SKILL.md`.
3. Generated project artifacts under `projects/`, where every prompt line carries them.

**The guarantee is identity, not uniqueness.** Every copy must be byte-identical to the
definition in `visual-style.md`. The `check` skill extracts the canonical string and
diffs the copies against it, because a partial edit that updates one copy and not the
others is exactly how the arced-versus-straight thumbnail contradiction survived
undetected. If you edit one of these strings, edit `visual-style.md` first, then run
`check` and fix every copy it reports.

A copy anywhere outside those three places is a bug: delete it and point at the rule
file instead.
