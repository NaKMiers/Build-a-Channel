---
name: metadata
description: Generate the publish-ready YouTube title, description with hashtags, and 25 to 40 SEO tags for a TossExplains video, saved to outputs/metadata.md. Use when the user says "metadata", "title", "description", "tags", "SEO", or "package the video".
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# metadata

Stage 5a of the TossExplains pipeline. Text packaging only. Thumbnails are a separate skill
because they need the cast and iterate at a different rate.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/channel-dna.md` - the voice, the title constraints, the guardrails
- `.agents/rules/file-formats.md` - the `metadata.md` section
- `.agents/skills/metadata/references/memory.md`

## Preconditions

```bash
ls projects/<n>-<slug>/script_*.md
```

The script is required and is the only input. Read it in full before writing. The
description must mirror the tone of the script's actual opening, and the tags must be
pulled from the script's actual topic, so a summary of the script is not enough.

## The rules

**Title.** One scroll-stopping, curiosity-driven title under 70 characters. Use the
channel's proven angles: provocative question, counterintuitive reframe, or hidden-truth
reveal. **No clickbait the script does not deliver on.** Uses "you" or "your". Never names
the takeaway outright.

**Description.**

- Open with a 2 to 3 sentence hook that mirrors the tone of the script's opening and
  teases the core reframe.
- Follow with a short paragraph, 3 to 4 sentences, summarizing what the viewer will
  discover, written in the calm 2nd-person voice. Name the psychological mechanism, hint
  at its ancestral origin, and tease the one shift they walk away with.
- Add a line inviting likes, comments, and subscribes in the channel's voice.
- End with a block of 15 to 25 relevant hashtags on one line, each starting with `#`.

**Tags.** 25 to 40 SEO tags in a single comma-separated line. Mix broad terms (psychology,
human behavior, anthropology, self improvement, personal growth, evolutionary psychology,
mental health awareness, human nature) with specific long-tail phrases pulled from this
video's topic. **No hashtags here.** Plain comma-separated keywords only.

## Step 1 - Write the file

Path: `projects/<n>-<slug>/outputs/metadata.md`, shaped exactly as `file-formats.md` specifies:
three sections, each holding a fenced block so the text copies out without markdown
bleeding in.

## Step 2 - Verify

```bash
F="projects/<n>-<slug>/outputs/metadata.md"
grep -n "$(printf '\u2014')" "$F" && echo "FAIL: em dash" || echo "clean"
```

Then check by eye: title under 70 characters, hashtag count between 15 and 25, tag count
between 25 and 40, tags on one line with no `#`.

## Step 3 - Report and hand off

Print the title, description, and tags in three separate copyable code blocks in chat, in
that order, so the user can paste each straight into YouTube. The file is the durable copy,
the code blocks are the convenience.

> Metadata saved to `<path>`.
>
> Paste the title into the title field, the description into the description box, and the
> tags into YouTube Studio, Details, Show More, Tags.
>
> Next: **`/thumbnail`** for the five thumbnail concepts.

## Guardrails

- Never promise something the script does not deliver. If the best title overstates the
  script, pick a weaker title or say the script needs a stronger payoff.
- Never put hashtags in the tags block or commas-as-tags in the hashtag line.
- Never shame the viewer in the description. The emotional promise is relief.
- The title may differ from the working title used for the folder slug. Do not rename the
  folder to match: the `script_<short_slug>.md` file name is derived from it and is referenced
  by `character-prompts.md`. Note that `image-prompts.md` no longer carries a header, so it is
  not one of the places that would need updating.

## Self-improvement

Read `.agents/skills/metadata/references/memory.md` at the start of every run. Append when
the user rewrites a title (record what was wrong with yours), when a tag set is corrected,
or when published performance teaches something about title shape.
