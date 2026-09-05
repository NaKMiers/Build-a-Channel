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

| File                                | Read before                                                                                                  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `.agents/rules/house-rules.md`      | anything. Always active. Output hygiene, no em dash, stage discipline.                                       |
| `.agents/rules/channel-dna.md`      | generating a topic, a script, or metadata. Pillars, angles, voice, editorial guardrails.                     |
| `.agents/rules/visual-style.md`     | writing any image, sheet, or thumbnail prompt. V1/V2 strings, palettes, tiers, registers, and frame grammar. |
| `.agents/rules/mascot-toss.md`      | building the cast. Toss identity lock and the reference sheet template.                                      |
| `.agents/rules/thumbnail-rules.md`  | writing thumbnail concepts. Rules A to F, evidence-backed.                                                   |
| `.agents/rules/file-formats.md`     | writing any project artifact. Layout and exact file shapes.                                                  |
| `.agents/rules/image-generation.md` | writing or editing `image-prompts.md`. The chain workflow that renders it, and the `---` chain break.        |

## The pipeline

Eight pipeline skills, plus `scene-polish`, `video-swipe`, `youtube`, and `skill-sync`, are
canonical under `.agents/skills/` and discovered by Claude through `.claude/skills/` wrappers.
Each pipeline skill validates its inputs, writes its artifact, and names the next command.

```
/topic       chat only, 5 titles, you pick one -> scaffolds projects/<n>-<slug>/
/script      script_<short_slug>.md
/transcript  transcribes/transcript.md              (needs the recorded voiceover)
/cast        prompts/character-prompts.md
/scenes      prompts/visual-plan.md + image-prompts.md for V2
             prompts/image-prompts.md only for V1   (needs transcript + cast)
/metadata    outputs/metadata.md
/thumbnail   prompts/thumbnail-prompts.md           (needs cast)
/captions    outputs/captions/*.srt                 (needs transcript, 25 languages)
/check       validation report, runnable any time
```

Scene-image file management is separate from the content pipeline:

```
/scene-polish   check, rename, move, and verify scene image files
```

Competitor research is also separate from the content pipeline:

```
/video-swipe    research/videos-swipe/<slug>/   frames, contact sheets, visual-analysis.md
                (needs a YouTube link plus the video file downloaded from that link)
```

Channel-side read/write lives outside the content pipeline too:

```
/youtube        stats, transcript, analytics, upload, competitor
                (needs YOUTUBE_API_KEY in .env; analytics + upload also need OAuth)
```

After `/script` the branches run in parallel: `/transcript`, `/cast`, and `/metadata`
depend only on the script. `/scenes` needs transcript plus cast. `/thumbnail` needs the
script plus cast, not the transcript. `/captions` needs `/transcript` and nothing else,
because it is built on the word-level `transcribes/words.json`, not on the script.

## Skill routing

When the user's request matches a skill, invoke that skill instead of answering ad hoc.

- Video ideas, "what should I make next", topic brainstorm -> `/topic`
- Write the narration, "write the script" -> `/script`
- Audio to timestamps, "make the transcript" -> `/transcript`
- Characters, cast, reference sheets, "lock the cast" -> `/cast`
- Image prompts, scene prompts, "prompts for every timestamp" -> `/scenes`
- Title, description, tags, SEO -> `/metadata`
- Thumbnail concepts -> `/thumbnail`
- Captions, subtitles, SRT files, "translate the transcript" -> `/captions`
- "Is this project correct", validate, "what is missing" -> `/check`
- Manage scene image timestamps, renaming, moves, or verification -> `/scene-polish`
- Analyze a competitor video, extract its frames, "phan tich video" -> `/video-swipe`
- Pull from YouTube, upload to YouTube, channel analytics, competitor research -> `/youtube`
- Added or renamed a skill -> `/skill-sync`

For web browsing use the `/browse` skill from gstack. Do not use
`mcp__claude-in-chrome__*` tools.

## Quality bar

The pipeline skills replace a single 533 line mega-prompt (`prompts/master-prompt.md`,
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
via Groq) and `tools/srt-to-timestamps.py` both emit the `[MM:SS.SSS] narration` format,
the transcript's own resolution. `prompts/image-prompts.md` stays on `[M:SS]`, truncated by
`/scenes`, because the scene image file names come from it. `.agents/bin/cue-times.sh` is the
one definition of that derivation for shell, `tsfmt.to_mss()` for Python. They
share `tools/tsfmt.py` for line splitting and timestamp formatting. `tools/combine-audio.py` merges a multi-part
recording into `audios/full.mp3` and reports each part's true start, which is the timeline
the transcript is built against. It also rewrites the combined file's Xing header, because
parts exported at different bitrates otherwise make players report a badly wrong duration.
It shares `tools/mp3frames.py` with `audio-to-timestamps.py`, which needs the same
durations to offset per-part word timings.
No ffmpeg required for any of the audio tools. The `transcript` skill drives all of them.
API keys live in a gitignored `.env`.

`tools/captions-srt.py` serves the `captions` skill and reads the same
`transcribes/words.json` that `audio-to-timestamps.py` saves, so subtitles land on each
word's true onset rather than on the start of whichever transcript line contains it. It runs in three
stages: `build` cuts `en.srt` plus a `blocks.json` timing spine from the word timings and
refuses a `words.json` that does not match the transcript; `assemble` pours one language's
translation into that spine, so every file is frame-identical by construction; `check`
diffs all 25 files against `en.srt` block by block and scans for empty blocks, repeats,
overlaps, em dashes, and untranslated Latin runs inside non-Latin scripts. It shares
`tools/tsfmt.py` with the audio tools for the sentence-boundary test. No dependencies.

`tools/video-frames.py` and `tools/youtube-verify.py` serve the `video-swipe` research
skill and are the only tools here that do need ffmpeg. `video-frames.py` runs in three
stages, `candidates` then `finalize` with the agent's review in between, plus a `stats`
stage that recomputes pacing from an existing `frame-index.csv`; its `ensure-ffmpeg` stage
fetches a static ffmpeg build when the machine has none. `youtube-verify.py` decides whether
a local file really is the YouTube video that was named: it checks the link against the
oEmbed endpoint, which also hands back the real title, channel, and folder slug, then weighs
the video id in the file name, the title, and an optional duration. A lookup it cannot reach
is a hard error rather than a weaker verdict, and `--offline` is the explicit opt-out. The
duration is not fetchable by script, YouTube's bot check hides it, so it arrives from
`/browse` as `--expect-duration`. Neither tool needs numpy or ffprobe, only Pillow.

`tools/youtube-api.py` serves the `youtube` skill. It has five subcommands:
`stats`, `transcript`, `analytics`, `upload`, `competitor`. `stats` and
`competitor` use `YOUTUBE_API_KEY`; `transcript`, `analytics`, and `upload`
use an OAuth refresh token in `.env` exchanged through `tools/yt_oauth.py`.
The token is minted once via `tools/yt_auth.py`, which reads the OAuth
client blob from `YOUTUBE_CLIENT_SECRETS_JSON` in `.env` (or a legacy
`client_secrets.json` at the project root) and walks the user through the
browser flow. Every secret lives in `.env`; no JSON file is shipped.
Dependencies (`defusedxml`, `google-auth-oauthlib`) are declared in
`requirements.txt`.
