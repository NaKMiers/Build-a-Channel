# HumanPrice - Agent Project Instructions

Production repository for **HumanPrice**, a YouTube channel about the economics of social
phenomena and human behavior. Episodes explain the visible transaction, hidden economic
mechanism, behavioral engine, and full human price in 8 to 12 minutes.

The repository contains the agent pipeline for research, narration, timestamps, cast,
visual prompts, thumbnails, and publishing metadata. It does not contain a video editor or
renderer.

## Source of truth

`.agents/` is canonical for Codex and Claude. `.claude/skills/` contains thin discovery
wrappers only. `CLAUDE.md` imports this file as `@AGENTS.md`.

## Rules to read before acting

| File | Read before |
| --- | --- |
| `.agents/rules/house-rules.md` | Anything. Output hygiene and stage discipline. |
| `.agents/rules/channel-dna.md` | Topics, research, scripts, titles, and metadata. |
| `.agents/rules/research-standards.md` | Claims, sources, exact numbers, and fact-checking. |
| `.agents/rules/visual-style.md` | Character, scene, and thumbnail prompts. |
| `.agents/rules/cast-identity.md` | Cast selection and the recurring protagonist. |
| `.agents/rules/thumbnail-rules.md` | Thumbnail concepts and evidence limits. |
| `.agents/rules/file-formats.md` | Any project artifact. |
| `.agents/rules/image-generation.md` | `image-prompts.md` and chain breaks. |

## Pipeline

```text
/topic       five ideas, user selects, project is scaffolded
/research    research/research-brief.md
/script      script_<short_slug>.md, 1,250 to 1,750 words
/transcript  transcribes/transcript.md from recorded narration
/cast        prompts/character-prompts.md
/metadata    outputs/metadata.md
/scenes      prompts/visual-plan.md + prompts/image-prompts.md
/thumbnail   prompts/thumbnail-prompts.md
/check       read-only validation, runnable at any point
```

After `/script`, `/transcript`, `/cast`, and `/metadata` can proceed independently.
`/scenes` needs transcript plus cast. `/thumbnail` needs the script, research brief, and
cast.

Supporting skills:

```text
/scene-polish  verify and organize generated scene images
/video-swipe   analyze one competitor video's visual system
/youtube       channel stats, captions, analytics, uploads, competitors
/skill-sync    regenerate Claude wrappers and Codex metadata after skill changes
```

## Skill routing

- Video ideas or what to make next -> `/topic`
- Sources, evidence brief, fact-checking, claim validation -> `/research`
- Narration or episode script -> `/script`
- Audio timestamps or subtitles -> `/transcript`
- Characters, cast, or reference sheets -> `/cast`
- Scene prompts or prompts for every timestamp -> `/scenes`
- Titles, description, chapters, hashtags, tags, SEO -> `/metadata`
- Thumbnail concepts -> `/thumbnail`
- Project validation or missing artifacts -> `/check`
- Scene-image filenames, timestamps, moves, or ranges -> `/scene-polish`
- Competitor frame extraction or video analysis -> `/video-swipe`
- YouTube data, upload, analytics, or competitor profile -> `/youtube`
- Added, renamed, removed, or re-described a skill -> `/skill-sync`

For web browsing use the gstack `/browse` skill when it is available. Do not use
`mcp__claude-in-chrome__*` tools.

## Quality bar

- Research is mandatory before scriptwriting.
- Material claims come from the research brief. Exact title and thumbnail numbers need
  explicit clearance.
- Narration is 8 to 12 minutes, normally 1,250 to 1,750 words, with hard bounds of 1,150
  to 1,850.
- The participant remains the point of view. Explain why reasonable people participate
  before exposing the cost.
- Current projects use the HumanPrice style and cast identity only.
- The first accepted HumanPrice episode will become the regression fixture. Until then,
  structural validation and skill synchronization are required after system changes.

## Tools

`tools/audio-to-timestamps.py`, `tools/srt-to-timestamps.py`, and
`tools/combine-audio.py` implement the transcript stage. They use `tools/tsfmt.py` and
`tools/mp3frames.py`. Forced alignment uses ElevenLabs; plain transcription uses Groq.
No ffmpeg is required for audio processing.

`tools/video-frames.py` and `tools/youtube-verify.py` support `/video-swipe` and require
ffmpeg. The verifier uses YouTube oEmbed, title, file name, and optional duration. An
unreachable verification request is a hard error unless the user explicitly chooses
offline mode.

`tools/youtube-api.py` supports `stats`, `transcript`, `analytics`, `upload`, and
`competitor`. API and OAuth secrets live only in the gitignored `.env`.
