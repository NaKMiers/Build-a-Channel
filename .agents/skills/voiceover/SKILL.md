---
name: voiceover
description: Create or update step 3 section voiceover for a Why It Works video project. Use when the user asks for Voiceover, section voiceover, generate audio for a script section, create narration audio, run step 3, or create all section voiceovers; requires completed project 00-topic-intake.md, 01-research-pack.md, and 02-script.md first, asks which script section to generate with All as the first option, then writes only the project's 03-voiceover.md plus section-local files under voiceover/.
---

# Voiceover

## Purpose

Run step `5` of the `Why It Works` video workflow.

Create voiceover for one selected script section at a time, or for `All` sections only when the user explicitly selects `All`.

This skill is section-first. It does not default to one full-video voiceover file.

## Pipeline Position

This is step `4` of the main video workflow.

Required previous outputs:

- `projects/<slug>/00-topic-intake.md`
- `projects/<slug>/01-research-pack.md`
- `projects/<slug>/02-script.md`

Do not create voiceover without a real, non-empty script file.

If `02-script.md` is missing or empty, stop and tell the user to run `script-draft` first.

If `00-topic-intake.md` or `01-research-pack.md` is missing, stop and tell the user to run the missing previous skill in order before `script-draft`.

If `01-research-pack.md` is older than `00-topic-intake.md`, treat the research pack as stale and stop. Tell the user to rerun `research-pack`.

If `02-script.md` is older than `00-topic-intake.md` or `01-research-pack.md`, treat the script as stale and stop. Tell the user to rerun `script-draft`.

If `02-script.md` has a newer modified time than `03-voiceover.md` or any section voiceover output, treat the existing voiceover output as stale. Do not trust it as current. Ask whether to regenerate the affected section or all sections.

When this skill creates, updates, or reruns `projects/<slug>/03-voiceover.md` or any file under `projects/<slug>/voiceover/`, every later output in the same project becomes stale.

List stale downstream files in chat. Do not silently delete them. Remove stale downstream files only when the user explicitly asks; otherwise downstream skills must be rerun in order.

## Required Context

Read these before creating or updating voiceover:

1. `README.md`
2. `.agents/rules/README.md`
3. `.agents/rules/video-workflow.md`
4. `.agents/_shared/channel/current-state.md`
5. `.agents/_shared/channel/channel-foundation.md`
6. `.agents/_shared/channel/channel-guardrails.md`
7. `.agents/_shared/channel/learning-log.md`
8. `.agents/_shared/channel/codex-collaboration.md`
9. `.agents/_shared/channel/production-workflow.md`
10. `.agents/_shared/systems/script-learner-voice.md`
11. `.agents/_shared/systems/audio-feedback-quality.md`
12. `references/memory.md`
13. the chosen project file: `projects/<slug>/02-script.md`

Load additional shared systems only when needed:

- `.agents/_shared/systems/topic-packaging-hooks.md` when generating Section 1 or checking the first `10` seconds
- `.agents/_shared/systems/visual-production.md` when the section audio needs visual cue timing notes
- `.agents/_shared/systems/audio-feedback-quality.md` when the user asks about mix, silence, or sound under narration

## Project Selection Gate

Always resolve the target project before generating audio.

Use this order:

1. If the user names a project slug or path, use that project.
2. If the current chat clearly selected a project and the folder exists, use that project.
3. If there is exactly one project with completed `00-topic-intake.md`, `01-research-pack.md`, and `02-script.md`, smart-select it and say so.
4. Otherwise scan `projects/`, excluding `_template`, and find voiceover candidates.

A voiceover candidate is usually:

- a folder with `00-topic-intake.md`
- and `01-research-pack.md`
- and `02-script.md`
- and not obviously blocked by stale upstream files

When multiple candidates exist or context is unclear, ask the user to choose before generating audio.

Do not create a new project folder in this skill. New projects come from `topic-intake`.

## Required Inputs Gate

Before section selection or audio generation, verify the chosen project has:

- non-empty `00-topic-intake.md`
- non-empty `01-research-pack.md`
- non-empty `02-script.md`

If `02-script.md` does not contain parsable sections in the form:

```text
## Section N: Section Name
```

stop and ask the user to rerun `script-draft` or fix the script structure first.

If the script has `Status` such as `draft`, `remade draft`, or `sectioned working script`, voiceover is allowed. The skill creates section timing audio for production, not final locked broadcast audio unless the user says the section is final.

## Section Selection Gate

Voiceover must get an explicit target section before writing audio files.

The target must be selected by the user as `All` or as a specific section number/name in the current request or in the section-choice response.

Do not infer the target section from:

- the active video state
- the latest reviewed section
- the next unfinished section
- an existing section preview
- the only missing voiceover output
- the previous section generated in chat
- the section most likely to be next

If no explicit section target is present, ask and stop before creating or editing files.

Parse `02-script.md` for:

- section number
- section name
- estimated time
- word count
- narration block
- voice revision notes

If the user explicitly names a section number or section name, use it.

If the user explicitly says `all`, `whole script`, or `all sections`, use `All`.

If the user does not explicitly specify a section target, ask them to choose.

Preferred option order:

1. `All`
2. `Section 1: <name>`
3. `Section 2: <name>`
4. Continue through the section list

Important:

- `All` means generate each section as its own section voiceover output.
- `All` does not mean create one stitched full-video audio file unless the user explicitly asks for a combined master.
- If option UI is available, show `All` first, then section choices.
- If option UI is unavailable, list numbered choices in chat and stop. Do not guess.
- Never auto-select a section just because it is probably the next section.

Fallback selection text:

```markdown
Choose voiceover target:

0. All sections
1. Section 1: <name>
2. Section 2: <name>
   ...
```

## Request Modes

### Section Create Mode

Use when the chosen section has no existing section voiceover output.

Create:

```text
projects/<slug>/voiceover/section-XX-kebab-section-name/
projects/<slug>/voiceover/section-XX-kebab-section-name/README.md
projects/<slug>/voiceover/section-XX-kebab-section-name/section-XX-script.txt
projects/<slug>/voiceover/section-XX-kebab-section-name/section-XX-marked-script.md
projects/<slug>/voiceover/section-XX-kebab-section-name/tts-inputs/
projects/<slug>/voiceover/section-XX-kebab-section-name/scratch-audio/
projects/<slug>/voiceover/section-XX-kebab-section-name/scratch-results.json
projects/<slug>/03-voiceover.md
```

If audio generation succeeds, place the selected audio file in:

```text
projects/<slug>/voiceover/section-XX-kebab-section-name/scratch-audio/
```

If the project has a HyperFrames asset folder ready, also copy the selected MP3 into the active section or video asset folder only when needed for preview. Document that copy in `scratch-results.json`.

### Section Update Mode

Use when the user asks to regenerate, revise, slow down, speed up, change voice, fix pronunciation, improve markup, or replace an existing section voiceover.

Read the existing section folder first. Preserve approved outputs unless the user explicitly asks to replace them.

When replacing audio, keep old files only if they are approved, needed for comparison, or explicitly requested. Otherwise keep one useful MP3 preview per section.

### All Sections Mode

Use when the user chooses `All`.

Generate each script section as a separate section output using the same Section Create or Section Update rules.

Do not stitch sections together. Assembly belongs to a later production or final-combine step.

If one section fails, continue only when the failure does not invalidate the remaining sections. Record the failure in `03-voiceover.md` and chat.

### Improve Memory Mode

Use when the user reviews voiceover and gives reusable lessons.

Update in this order:

1. the project `03-voiceover.md` or section README if the review affects this video
2. this skill's `references/memory.md`
3. shared memory only if the lesson improves the whole channel

Promote shared lessons with a clear classification such as `Operational lesson` or `Core operational capability`.

## Voice Direction Defaults

Use `.agents/_shared/systems/script-learner-voice.md` as the source of truth.

Default final channel voice (owner-locked 2026-07-18): **`Alan`** - a custom ElevenLabs Voice-Design voice, the channel's official voice going forward.

```text
Name: Alan
Engine: ElevenLabs (commercial license - owner on Starter+)
voice_id: f8k6yACqa8sb7OSDGsSp
model_id: eleven_multilingual_v2
Settings: stability 0.4, similarity_boost 0.8, style 0.35, use_speaker_boost true
Language: English (en)
Direction: young American man, mid-20s, warm + clear, dry deadpan with a slightly cheeky edge,
           expressive comedic timing, easy to follow for learners
Key: read from ELEVENLABS_API_KEY env var - NEVER hardcode or commit the key
```

Generate with `POST https://api.elevenlabs.io/v1/text-to-speech/f8k6yACqa8sb7OSDGsSp`. Tune `stability`
lower for more comedic variation on a given line if a read is too flat; audition before locking a change.

Legacy fallback voice: `David23 / am_eric` (Kokoro, free, speed 0.84, en-us) - use ONLY when ElevenLabs
is unavailable or for a no-cost scratch timing pass, never as the final published voice without the
owner's say-so. Do not silently substitute it for `Alan`.

If neither `Alan` (ElevenLabs) nor the fallback tooling is available, stop and ask before using any other voice.

Do not automatically fall back to `am_adam`, `am_michael`, `bm_george`, or any other voice when the user asked for `David23`.

Scratch voice generation is allowed only when the user explicitly approves scratch timing audio after being told that approved `David23 / am_eric` is unavailable.

Current practical scratch precedent:

```text
Voice: am_adam
Speed: 1.05
Language: en-us
Use: timing reference only, not final brand approval
```

Do not silently pretend scratch audio is the final approved channel voice.
Do not generate scratch audio as a substitute for `David23` without explicit user approval.

## Expressive Voice Upgrade (owner-directed 2026-07-18)

Why It Works is a COMEDY / dry-humor channel, so the voice must carry the jokes - delivery matters MORE
here than for an earnest explainer. A flat read kills a punchline. This raises the voice bar; treat the
voiceover as a place to invest, not to cut.

- **Engine target: an expressive, top-tier TTS (ElevenLabs-class).** The owner has an ElevenLabs account
  and wants to test it against the current free engine (Kokoro `am_eric`). Kokoro / edge-tts remain the
  free fallback. Do NOT swap the locked default channel voice without owner sign-off from a real A/B.
  - **ElevenLabs usage:** read the key from the `ELEVENLABS_API_KEY` env var - NEVER hardcode or commit
    an API key into any repo file. Endpoint: `POST https://api.elevenlabs.io/v1/text-to-speech/<voice_id>`.
  - **Voice pick (match the `David23` persona: young, male, American, clear + lightly dry):** candidates
    on this account are `Liam` (`TX3LPaxmHKxFdv7VOQHJ`, young creator, confident) and `Will`
    (`bIHbv24MWmeRgasZH58o`, young, chill - good for deadpan). Confirm the final voice with the owner via
    an A/B demo before locking.
  - **Settings for comedy:** lower `stability` (~0.3-0.45) gives more emotional variation for jokes;
    keep `similarity_boost` high (~0.8); add `style` for delivery; `use_speaker_boost: true`. Too-low
    stability = inconsistent, so audition.
- **Write FOR the voice (biggest free lever).** Even great TTS reads flat on prose written for the eye:
  short sentences, fragments, contractions, one idea per line, and put the PUNCHLINE WORD at the END of
  the sentence. Use the existing `[pause] [beat] [deadpan] [slower] [emphasis]` markers deliberately -
  especially a micro-pause right BEFORE a punchline lands (comedic timing).
- **Direct it like takes.** Generate per line/short segment, keep the best take, and regenerate any weak
  line rather than accepting one flat full-length read. This is how you get "soul" out of TTS.
- **Light post-processing** makes any voice sound produced: gentle compression + a presence EQ bump
  (~3-5 kHz) + de-ess + a touch of warmth. Keep it subtle.

## Markup Rules

Use `.agents/_shared/systems/script-learner-voice.md`.

For each section:

1. Extract only the narration block from `02-script.md`.
2. Keep the script wording unless voice generation exposes a clear issue or the user asked for voice revision.
3. Add light markup only where it protects rhythm, clarity, or visual timing:
   - `[pause]`
   - `[beat]`
   - `[deadpan]`
   - `[slower]`
   - `[emphasis]`
   - `[emphasis: word]`
4. Strip markup before sending text to TTS unless the chosen TTS tool explicitly supports markup tags.
5. Save both the clean script and marked script.

Do not create tag soup. If a line needs many tags to work, rewrite the line only after noting the change in the section README.

## ElevenLabs Pause Handling

For the official `Alan` voice on ElevenLabs, create deliberate silence with inline break tags in the
`tts-inputs/*.txt` file. This is the approved, repeatable method for comedy timing and learner clarity.

```text
Now look down.<break time="1s"/>
The first rung is missing.<break time="0.8s"/>
So what removed it?
```

Rules:

- Use `<break time="..."/>` inline, immediately after the sentence that earns a pause. Start with
  `0.5s-0.7s` for a normal beat, `0.8s-1s` for a reveal, thesis, deadpan punchline, or cliffhanger.
- Keep the clean script and marked script free of these implementation tags. They belong only in the
  ElevenLabs input file.
- Never send a standalone `...` line to ElevenLabs. In testing, it created audible non-lexical artifacts
  after lines such as `Now look down.` even though a transcript did not show an extra word.
- Never use Kokoro's `. .` reset syntax with ElevenLabs. It is not an ElevenLabs pacing control.
- Do not assume blank lines create reliable silence. Use an inline break when the timing must be heard.
- After a pause-sensitive Alan generation, transcribe the MP3 with ElevenLabs Scribe using word timestamps
  and verify the target gaps and absence of unexpected words before locking the preview.
- Keep break tags sparse and purposeful. A pause must serve a reveal, joke, thesis, emotional turn, or
  cliffhanger, not appear after every sentence.

Kokoro punctuation pacing (`...`, `. .`) is a legacy fallback technique only. Do not transfer that
template to Alan.

## Audio Generation Workflow

1. Run the Project Selection Gate.
2. Run the Required Inputs Gate.
3. Parse `02-script.md` sections.
4. Run the Section Selection Gate.
5. Read required voice and clarity systems.
6. For each selected section:
   - create the section voiceover folder
   - extract the narration block
   - apply light voice markup
   - write `section-XX-script.txt`
   - write `section-XX-marked-script.md`
   - write a TTS input file under `tts-inputs/`
   - generate one MP3 voiceover preview when the requested voice is available
   - if the requested voice is unavailable, stop unless the user explicitly approved a scratch fallback
   - record exact voice, speed, language, tool, output path, duration, and status
   - write or update the section `README.md`
   - write or update `scratch-results.json`
7. Write or update `projects/<slug>/03-voiceover.md` as the section voiceover index.
8. Run the Downstream Stale Gate.
9. Respond with the Chat Response Format.
10. Stop before visual plan, render, review, upload, or learning unless explicitly asked.

## TTS Tooling Rules

Prefer existing project-local or HyperFrames tooling when available.

Before running TTS:

- inspect existing project voiceover folders for tool precedent
- inspect `hyperframes/` or project tools for available TTS commands
- run a help/version command when needed before assuming syntax
- if `David23 / am_eric` is requested, test `am_eric` directly before declaring it unavailable because HyperFrames may accept Kokoro voice IDs that are not shown in the short voice table

Known precedent:

```text
npx hyperframes@0.6.69 tts
npx hyperframes@0.6.76 tts
```

Known `David23` command pattern:

```text
npx hyperframes@0.6.76 tts <input.txt> --output <output.mp3> --voice am_eric --speed 0.84 --lang en-us --json
```

Use the exact command syntax supported by the local environment. If command help is unclear, the tool is unavailable, or the requested voice is unavailable, do not invent successful audio. Instead:

- write the TTS input files
- write `scratch-results.json` with status `tts not generated`
- document the command/tooling failure
- tell the user what is needed to generate audio
- ask before using a scratch fallback voice

Audio output rule:

```text
Keep one useful MP3 preview file per section. Do not preserve duplicate MP3/WAV versions unless a renderer requires them or the user asks.
```

## Output Folder Standard

Section folder naming:

```text
voiceover/section-XX-kebab-section-name/
```

Examples:

```text
voiceover/section-01-hook/
voiceover/section-02-cheap-is-not-the-villain/
voiceover/section-06-repair-gets-a-security-system/
```

File naming:

```text
section-XX-kebab-section-name-script.txt
section-XX-kebab-section-name-marked-script.md
section-XX-kebab-section-name-david23-am_eric-0.84.mp3
section-XX-kebab-section-name-scratch-am_adam-1.05.mp3
```

Use lowercase kebab-case.

## 04 Voiceover Format

Write or update:

```text
projects/<slug>/03-voiceover.md
```

Use this structure:

```markdown
# 04 Voiceover

Video: `<title>`

Status: `section voiceover in progress`

Source skill: `voiceover`

Source file:

- `02-script.md`

## Voice Direction

- Default final voice:
- Current generation voice:
- Speed:
- Language:
- Tone:
- Voice status:

## Section Voiceover Index

|   # | Section | Status | Voice | Speed | Duration | Audio file | Notes |
| --: | ------- | ------ | ----- | ----: | -------: | ---------- | ----- |

## Section Details

### Section X: <name>

- Status:
- Section folder:
- Clean script:
- Marked script:
- TTS input:
- Audio file:
- Duration:
- Voice:
- Speed:
- Language:
- Tool:
- Use:
- Notes:

## Stale / Regeneration Notes

## Next Step Boundary

Next workflow step: `Visual plan`

Do not continue into visual plan, render, review, upload, or learning until the user asks for the next skill or explicitly requests that step.
```

If only one section has been generated, include the remaining sections in the index as `not generated`.

## Section README Format

Each section folder should include `README.md`:

```markdown
# Section X Voiceover

Video:
`<title>`

Section:
`Section X: <name>`

Status:
`scratch voice generated` / `final section voice generated` / `tts not generated`

## Direction

- voice:
- speed:
- language:
- tone:
- learner clarity notes:

## Output Rule

Keep one useful MP3 preview file only unless a renderer requires another format.

## Result

- File:
- Duration:
- Use:
- Tool:
- Caveat:
```

## Downstream Stale Gate

After creating, updating, or rerunning `03-voiceover.md` or section audio, check the same project for downstream files:

- `04-visual-plan.md`
- `05-production-board.md`
- `06-review.md`
- `07-upload.md`
- `08-self-learning.md`

If any exist, list them as stale in chat and tell the user they should be removed or regenerated by rerunning downstream skills in order.

Do not delete downstream files unless the user explicitly asks.

## Chat Response Format

After creating or updating section voiceover, respond with a short summary.

Do not paste the full script unless the user asks.

Use this structure:

```markdown
Done. I created/updated:

[03-voiceover.md](<absolute path>)

Section target: `<All or Section X: name>`

Status: `<status>`

Generated:

| Section | Status | Voice | Speed | Duration | File |
| ------- | ------ | ----- | ----: | -------: | ---- |

Notes:

- <line 1>
- <line 2>
- <line 3>

Stale downstream:

- <file or none>
```

## Quality Bar

A section voiceover pass is ready when:

- the selected section is extracted from the latest `02-script.md`
- the section has clean script and marked script files
- the voice direction matches the channel voice system or is clearly labeled as scratch
- the audio output path, voice, speed, language, and duration are documented
- the section output keeps one useful MP3 preview by default
- learner clarity issues are noted before production
- any TTS failure is recorded honestly
- stale downstream files are listed
- no visual plan, render, review, upload, or learning files are created

## Hard Fails

Reject or stop before finishing if:

- the project lacks `02-script.md`
- the script lacks parsable sections
- upstream files are missing, or script is older than topic/research
- the user has not explicitly selected `All` or a specific section
- the section target is inferred instead of selected by the user
- `All` is interpreted as one stitched full-video file without explicit user approval
- scratch audio is described as final channel voice without caveat
- scratch audio is generated after the user asked for `David23` and did not approve a fallback
- duplicate MP3/WAV scratch files are left without a reason
- the skill rewrites major script content without user approval
- the skill creates visual plan, render, review, upload, or learning files

## Self-Improvement

Read `references/memory.md` every run.

Update skill memory when:

- the user approves or rejects a section voice style
- the user asks for a different section-selection behavior
- TTS tooling succeeds or fails in a repeatable way
- a voiceover later causes timing, clarity, or visual sync problems
- the user clarifies how `All` should behave
- the audio output format rule changes

Promote lessons into `.agents/_shared/channel/learning-log.md` only when they improve the whole channel. Classify each promoted lesson as `Core`, `Experiment`, `Operational lesson`, or `Reject` according to `.agents/_shared/channel/channel-guardrails.md`.

Do not rewrite channel foundation, audience, tone, or default voice direction from one voiceover run without explicit user confirmation.
