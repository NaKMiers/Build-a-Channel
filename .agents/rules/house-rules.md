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

## Guarding the versioned verbatim strings

The V1 and V2 STYLE ANCHOR, STYLE LOCK, GENERATION LINE, and REFERENCE SHEET OPENING
LINE are **defined** in `.agents/rules/visual-style.md`. That file is the authority.

V1 is frozen for legacy Projects 1 through 5. V2 is current for new projects. Never mix V1
and V2 scene strings inside one project. Never bulk-rewrite a legacy project's prompts merely
to make it current.

One other place legitimately contains copies, and no others:

1. Generated scene artifacts and legacy thumbnail artifacts under `projects/`.

Verification skills source both versions through `.agents/bin/style-strings.sh`; they never
hard-code another copy. The historical unversioned shell variables remain V1 aliases for
backward compatibility. New pipeline work uses the explicit `V2_*` variables.

Thumbnail prompts use the separate self-contained rendering system in
`.agents/rules/thumbnail-rules.md` and never copy the scene STYLE ANCHOR or STYLE LOCK.

**The guarantee is identity, not uniqueness.** Every copy must be byte-identical to the
definition in `visual-style.md`. The `check` skill extracts the canonical string and
diffs the copies against it, because a partial edit that updates one copy and not the
others is exactly how the arced-versus-straight thumbnail contradiction survived
undetected. If you edit one of these strings, edit `visual-style.md` first, then run
`check` and fix every copy it reports.

A copy anywhere outside those three places is a bug: delete it and point at the rule
file instead.
