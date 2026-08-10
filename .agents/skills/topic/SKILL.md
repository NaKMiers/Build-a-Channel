---
name: topic
description: Generate 5 viral TossExplains video topic ideas as a table, wait for the user to pick one, then scaffold the project folder for it. Use when the user says "topic", "topics", "new video", "video ideas", "what should I make next", or asks to start a new episode.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# topic

Stage 1 of the TossExplains pipeline. Produces 5 candidate titles in chat, nothing on
disk, then scaffolds a project folder once the user picks.

## Read first

- `.agents/rules/house-rules.md`
- `.agents/rules/channel-dna.md` - the pillars, the five proven angles, the recurring
  themes, the off-limits list, and the title constraints
- `.agents/skills/topic/references/memory.md` - which topics are already made or
  already rejected

## Step 1 - See what already exists

```bash
ls -d projects/*/ 2>/dev/null
cat .agents/skills/topic/references/memory.md 2>/dev/null
```

Never propose a topic that an existing project already covers, and never repeat a title
recorded as rejected in memory.

## Step 2 - Choose the 5

Internal constraints. **Do not print these.**

- Each title must promise an inner experience the viewer has personally felt, not an
  era, a civilization, or a species-level fact.
- Each idea must have a real psychological mechanism behind it, a plausible ancestral
  origin, and something the viewer can do differently afterwards. If you cannot name all
  three silently, the idea is not eligible.
- The 5 must be spread across different themes. Do not give five variations of the same
  drive. They must draw on at least 3 different angles from the five in
  `channel-dna.md`.
- Titles stay under 70 characters, use "you" or "your", and never name the takeaway
  outright. The curiosity gap is the point.

## Step 3 - Output

Print this table and nothing before it.

```markdown
| # | Video Title |
| --- | --- |
| 1 | [Title] |
| 2 | [Title] |
| 3 | [Title] |
| 4 | [Title] |
| 5 | [Title] |
```

Then end with exactly this line and stop:

> **Which idea do you want to develop? Reply with a number (1-5).**

**Write no files in this step.** Wait for the user.

## Step 4 - On selection, scaffold ONE project PER selected topic

**The user may select more than one number**, for example `1 and 4`. That is normal.
**Scaffold one project folder for each number they gave**, numbered in the order given, so
two picks produce two folders.

For each selected title, in the order the user listed them:

1. Compute `<n>` as the next integer after the highest existing `projects/<n>-*` folder,
   incrementing as you go so each new project gets its own number. If none exist, `<n>`
   is 0.
2. Compute `<title-slug>`: that title, lowercased, non-alphanumerics collapsed to single
   hyphens, no leading or trailing hyphen.
3. Create the folder tree from `.agents/rules/file-formats.md`:

```bash
P="projects/<n>-<title-slug>"
mkdir -p "$P"/{audios,characters,outputs,prompts,scenes,transcribes}
touch "$P"/prompts/video-prompts.md
for d in audios characters outputs scenes transcribes; do touch "$P/$d/.gitkeep"; done
find "$P" | sort
```

A quick loop handles several picks at once:

```bash
slugify() { echo "$1" | tr '[:upper:]' '[:lower:]' | sed -E "s/[^a-z0-9]+/-/g; s/^-+//; s/-+$//"; }
N=$(ls -d projects/*/ 2>/dev/null | sed -E 's#projects/([0-9]+)-.*#\1#' | sort -n | tail -1)
N=$((N+1))
for t in "<selected title 1>" "<selected title 2>"; do
  P="projects/$N-$(slugify "$t")"
  mkdir -p "$P"/{audios,characters,outputs,prompts,scenes,transcribes}
  touch "$P"/prompts/video-prompts.md
  for d in audios characters outputs scenes transcribes; do touch "$P/$d/.gitkeep"; done
  echo "$N  $P"; N=$((N+1))
done
```

`prompts/video-prompts.md` is created empty on purpose. It is a reserved slot, and
`check` will not flag it.

4. Append every title the user did NOT select to
   `.agents/skills/topic/references/memory.md` under a "Proposed but not picked" heading,
   with today's date. They are next month's backlog.

## Step 5 - Report and hand off

State every created path with its title, then:

> Projects scaffolded. Next: **`/script`** to write the narration.

If more than one project was scaffolded, say that `/script` handles one project at a time
and ask which to write first. Never start writing a script inside this skill.

## Guardrails

- Never write the 5 titles to a file before the user picks. Chat only.
- Never scaffold before the user picks.
- Never propose a topic that fails a pillar. A topic with no ancestral origin is
  off-channel however good the title sounds.
- Never reuse a rejected title from memory without saying it was rejected before and why
  you are re-proposing it.

## Self-improvement

Read `.agents/skills/topic/references/memory.md` at the start of every run. Append to it
when the user rejects a whole batch (record why), when they steer toward a theme, or when
a published video's performance teaches something about which angles land.
