# TossExplains - Agent Project Instructions

Production repo for **TossExplains**, a YouTube channel of hand-drawn doodle explainers
about psychology, anthropology, and self-help. This repo holds no video editor and no
rendering code. It holds the agent pipeline that produces each episode's script, cast,
prompts, and packaging, plus the tools that turn narration audio into timestamps.

## Source of truth

`.agents/` is the single source of truth for how agents operate here. Both **Codex**
and **Claude** read from it. `.claude/skills/` holds only thin discovery wrappers that
delegate back. See `.agents/README.md` and `.claude/README.md`.

`AGENTS.md` is this file, Codex's auto-loaded entry point. `CLAUDE.md` is just
`@AGENTS.md`, a Claude import, so the two never drift.

## Project rules - read the matching file before acting

| File                               | Read before                                                                                                   |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `.agents/rules/house-rules.md`     | anything. Always active. Output hygiene, no em dash, stage discipline.                                        |
| `.agents/rules/channel-dna.md`     | generating a topic, a script, or metadata. Pillars, angles, voice, editorial guardrails.                      |
| `.agents/rules/visual-style.md`    | writing any image, sheet, or thumbnail prompt. Palette, tone map, frame types, and the four verbatim strings. |
| `.agents/rules/mascot-toss.md`     | building the cast. Toss identity lock and the reference sheet template.                                       |
| `.agents/rules/thumbnail-rules.md` | writing thumbnail concepts. Rules A to F, evidence-backed.                                                    |
| `.agents/rules/file-formats.md`    | writing any project artifact. Layout and exact file shapes.                                                   |

## The pipeline

Nine pipeline skills and one scene-image management skill are canonical under
`.agents/skills/` and discovered by Claude through `.claude/skills/` wrappers. Each
pipeline skill validates its inputs, writes its artifact, and names the next command.

```
/topic       chat only, 5 titles, you pick one -> scaffolds projects/<n>-<slug>/
/script      script_<short_slug>.md
/transcript  transcribes/transcript.md              (needs the recorded voiceover)
/cast        prompts/character-prompts.md
/scenes      prompts/image-prompts.md               (needs transcript + cast)
/metadata    outputs/metadata.md
/thumbnail   prompts/thumbnail-prompts.md           (needs cast)
/check       validation report, runnable any time
```

Scene-image file management is separate from the content pipeline:

```
/scene-images   check, rename, move, and verify scene image files
```

After `/script` the branches run in parallel: `/transcript`, `/cast`, and `/metadata`
depend only on the script. `/scenes` needs transcript plus cast. `/thumbnail` needs the
script plus cast, not the transcript.

## Skill routing

When the user's request matches a skill, invoke that skill instead of answering ad hoc.

- Video ideas, "what should I make next", topic brainstorm -> `/topic`
- Write the narration, "write the script" -> `/script`
- Audio to timestamps, "make the transcript" -> `/transcript`
- Characters, cast, reference sheets, "lock the cast" -> `/cast`
- Image prompts, scene prompts, "prompts for every timestamp" -> `/scenes`
- Title, description, tags, SEO -> `/metadata`
- Thumbnail concepts -> `/thumbnail`
- "Is this project correct", validate, "what is missing" -> `/check`
- Manage scene image timestamps, renaming, moves, or verification -> `/scene-images`
- Added or renamed a skill -> `/skill-sync`

For web browsing use the `/browse` skill from gstack. Do not use
`mcp__claude-in-chrome__*` tools.

## Quality bar

The nine skills replace a single 533 line mega-prompt (`prompts/master-prompt.md`,
retired to `prompts/retired/`). That prompt encoded 256 hard-won rules, several of them
recovered from specific generation failures. **This is a reorganization, not a
compression.** If a skill or rule file looks suspiciously short, something was lost.
Restore it from `prompts/retired/`.

The regression fixture is
`projects/1-why-you-feel-lonelier-in-a-crowd-than-alone-in-your-room/`, a completed and
accepted video. Any change to the pipeline must still reproduce it: run `/check` on it
and it must pass clean.

## Tools

`tools/audio-to-timestamps.py` (forced alignment via ElevenLabs, or plain transcription
via Groq) and `tools/srt-to-timestamps.py` both emit the `[M:SS] narration` format. They
share `tools/tsfmt.py` for line splitting. `tools/combine-audio.py` merges a multi-part
recording into `audios/full.mp3` and reports each part's true start, which is the timeline
the transcript is built against. It also rewrites the combined file's Xing header, because
parts exported at different bitrates otherwise make players report a badly wrong duration.
It shares `tools/mp3frames.py` with `audio-to-timestamps.py`, which needs the same
durations to offset per-part word timings.
No ffmpeg required anywhere. The `transcript` skill drives all of them. API keys live in a
gitignored `.env`.
