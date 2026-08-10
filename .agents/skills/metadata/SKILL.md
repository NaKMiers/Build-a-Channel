---
name: metadata
description: Generate the publish-ready YouTube title, description with hashtags and chapters, 25 to 40 SEO tags, and a citations block for a TossExplains video, saved to outputs/metadata.md. Use when the user says "metadata", "title", "description", "tags", "SEO", "citations", or "package the video".
allowed-tools:
  - Bash
  - Read
  - Write
---

# metadata

Stage 5a of the TossExplains pipeline. Text packaging only. Thumbnails are a separate skill
because they need the cast and iterate at a different rate.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/channel-dna.md` - the voice, the title constraints, the guardrails
- `.agents/rules/file-formats.md` - the `outputs/metadata.md` section
- `.agents/skills/metadata/references/memory.md`

## Preconditions

Two inputs are required:

```bash
ls projects/<n>-<slug>/script_*.md
ls projects/<n>-<slug>/transcribes/transcript.md
```

**Read both in full before writing.** The script drives the title, the description hook, and
the tags. The transcript drives the chapter timestamps. A summary of the script is not
enough: the description must mirror the tone of the script's actual opening, and the tags
must be pulled from the script's actual topic.

**This skill must run after `/transcript`.** The chapters in the description are derived from
the transcript's timestamp structure. Run `/transcript` first.

## Five title variants

Generate five title options, one per formula slot. The folder title slug is a hint, not
a constraint. Pick the slot that best fits the script's actual angle.

| Slot | Formula                                              | Constraint                                        |
| ---- | ---------------------------------------------------- | ------------------------------------------------- |
| A    | "Why do/can't you \_\_\_?"                           | Universal inner experience, traced to tribal life |
| B    | "Your brain still thinks you're \_\_\_"              | Modern mismatch, ancient wiring misfiring         |
| C    | "The \_\_\_ Effect"                                  | Named experiment mirrored onto daily life         |
| D    | "What every human tribe does that you stopped doing" | Lost cross-cultural practice                      |
| E    | "You never noticed that \_\_\_"                      | Hidden pattern revealed as survival instinct      |

Rules per title:

- Under 70 characters.
- Uses "you" or "your".
- Promises an inner experience the viewer has personally felt, not an era or species fact.
- Never names the takeaway outright. The curiosity gap is the point.
- **If the formula is a question, the title must end with "?".**
- **No clickbait the script does not deliver on.**

## Citations

Every named study, experiment, researcher, or scientific finding mentioned in the script
must be cited. Citations go **inside the description block**, after the call-to-action and
before the hashtags, separated by a blank line.

**Research and find the best link for each citation:**

- Wikipedia for the study or paper (e.g. Milgram experiment, Dunbar's number)
- The original paper if no good Wikipedia article exists
- A reputable science news source (NPR, Scientific American, APS, The Atlantic, etc.) if the
  finding is well-covered there and the article is accurate
- Never cite a tabloid, a pop-psychology blog, or an unknown site

**For each citation, provide:**

1. The short reference (study name, researcher name, or paper title)
2. The year
3. The URL

**Do not fabricate links.** If you cannot find a reliable source, write the reference text
but omit the link and note "(link not found)".

Example sources block inside the description:

```
Sources:
- Cacioppo, J.T. (2008): https://en.wikipedia.org/wiki/John_T._Cacioppo
- Dunbar, R.I.M. (1992): https://en.wikipedia.org/wiki/Dunbar%27s_number
```

## Description

Structure: hook paragraph, summary paragraph, chapters block, call-to-action, sources block,
hashtag line.

**Hook (2-3 sentences).** Mirror the tone of the script's actual opening. Tease the core
reframe. Do not give the answer away.

**Summary (3-4 sentences).** Written in the calm 2nd-person voice. Name the psychological
mechanism, hint at its ancestral origin, and tease the one shift they walk away with.

**Chapters.** Derive 5 to 7 chapter entries from the transcript. Scan for natural topic
shifts, major research introductions, and structural beats. Each entry is:

```
M:SS  <short chapter title, max ~8 words>
```

Match the M:SS to the nearest transcript timestamp. Chapters should feel like a useful
viewing map, not a complete outline.

**Call to action.** One line inviting likes, comments, and subscribes in the channel voice.

**Emoji.** One emoji at the start of each section label — `🗺️ Chapters:`, `💡` before the
call-to-action, `📚 Sources:`. Adjust to fit the video's tone and topic. For dark or
unsettling subjects, pick a softer or warmer set. For bright, practical topics, pick a
sharper, more energetic set. The emoji signals what the section is before the viewer reads
it. Keep it minimal — one emoji per section label.

**Hashtags.** 15 to 25 relevant hashtags on one line, each starting with `#`. Include the
broad channel hashtags (psychology, anthropology, selfhelp, etc.) plus topic-specific ones
derived from the script.

## Tags

25 to 40 SEO keywords in a single comma-separated line. Mix:

- Broad terms: psychology, human behavior, anthropology, self improvement, personal growth,
  evolutionary psychology, mental health awareness, human nature
- Specific long-tail phrases pulled from this video's topic

**No hashtags.** Plain comma-separated keywords only.

## Step 1 - Write the file

Path: `projects/<n>-<slug>/outputs/metadata.md`.

Shape it like this:

```markdown
# Metadata - <Video Title>

## Title
```

<one viral title under 70 characters>

```

### All five title variants

|     | Formula                        | Title                                               |
| --- | ------------------------------ | --------------------------------------------------- |
| A   | Why do/can't you \_\_\_?       | <title A>                                           |
| B   | Your brain still thinks \_\_\_ | <title B>                                           |
| C   | The \_\_\_ Effect              | <title C>                                           |
| D   | What every human tribe does... | <title D>                                           |
| E   | You never noticed that \_\_\_  | <title E>                                           |

## Description

```

<hook paragraph>

🗺️ Chapters:
<timestamp> <chapter title>
<timestamp> <chapter title>
...

💡 If this helped you see something new about yourself, a like and a comment genuinely help,
and subscribing brings you the next mechanism your mind is quietly running.

📚 Sources:

- <short reference> (<year>): <URL>
- <short reference> (<year>): <URL>
  ...

#hashtag #hashtag #hashtag ...

```

Emoji are not fixed — pick icons that match the video's emotional register.

## Tags

```

<25 to 40 comma-separated keywords on one line>

```

```

Two fenced blocks so the text copies out without markdown bleeding in.

## Step 2 - Verify

```bash
F="projects/<n>-<slug>/outputs/metadata.md"
grep -n "$(printf '\u2014')" "$F" && echo "FAIL: em dash" || echo "clean"
```

Then check by eye:

- Each of the 5 titles is under 70 characters
- Hashtag count between 15 and 25
- Tag count between 25 and 40
- Tags on one line with no `#`
- Chapters have valid M:SS timestamps matching the transcript
- No more than 7 chapter entries
- Every named study or researcher in the script has a citation with a working URL
- No fabricated links — verify each URL is real and relevant

## Step 3 - Report and hand off

Print the primary title, description, and tags in three separate copyable code blocks in
chat, in that order, so the user can paste each straight into YouTube. The description block
already contains the sources inside it — paste the whole block at once. Also print the five
title variants table. The file is the durable copy, the code blocks are the convenience.

> Metadata saved to `<path>`.
>
> Paste the **title** into the title field, the **description** into the description box,
> and the **tags** into YouTube Studio, Details, Show More, Tags.
>
> **Pick a title** from the five variants, or request a rewrite.
>
> Next: **`/thumbnail`** for the five thumbnail concepts.

## Guardrails

- Never promise something the script does not deliver. If the best title overstates the
  script, pick a weaker title or say the script needs a stronger payoff.
- Never put hashtags in the tags block or commas-as-tags in the hashtag line.
- Never shame the viewer in the description. The emotional promise is relief.
- Never write fewer than 5 or more than 7 chapters. Too few is not a useful map; too many
  kills the "just one more minute" retention effect.
- The title may differ from the working title used for the folder slug. Do not rename the
  folder to match: the `script_<short_slug>.md` file name is derived from it and is referenced
  by `character-prompts.md`. Note that `image-prompts.md` no longer carries a header, so it is
  not one of the places that would need updating.

## Self-improvement

Read `.agents/skills/metadata/references/memory.md` at the start of every run. Append when
the user rewrites a title (record what was wrong with yours), when a tag set is corrected,
or when published performance teaches something about title shape.
