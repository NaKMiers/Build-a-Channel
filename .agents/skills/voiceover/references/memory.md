# Voiceover Skill Memory

This file stores memory specific to the `voiceover` skill.

Use `.agents/_shared/` for channel-wide voice systems, narrator identity, pacing standards, and reusable production lessons.
Use this file for section-selection behavior, section voiceover output shape, TTS tooling notes, per-section generation habits, and lessons about keeping audio generation aligned with the script pipeline.

## Current Skill Standard

- Run after `script-draft`.
- Require non-empty `00-topic-intake.md`, `01-research-pack.md`, and `02-script.md`.
- Treat `02-script.md` as the voiceover source of truth.
- If upstream files are newer than `02-script.md`, stop and ask the user to rerun `script-draft`.
- Require the user to explicitly select `All` or a specific section before creating or editing voiceover files.
- Ask which section to generate whenever the user does not explicitly name a section target.
- Do not infer the section from the active video state, the next unfinished section, existing previews, missing outputs, or prior chat context.
- Put `All` at the top of section choices.
- Interpret `All` as separate voiceover outputs for every script section, not one stitched full-video file.
- Write only `04-voiceover.md` and files under `voiceover/`.
- Keep one useful MP3 preview per section by default.
- Avoid preserving duplicate MP3/WAV scratch files unless a renderer requires them or the user asks.
- Use `David23 / am_eric / 0.84 / en-us` as the default final voice direction from shared memory.
- When generating `David23`, test `am_eric` directly with HyperFrames before declaring it unavailable; `hyperframes@0.6.76` accepts `am_eric` even when the short voice list does not display it.
- If local TTS tooling cannot generate `David23`, stop and ask before using any alternate scratch voice.
- Never generate scratch audio as a substitute when the user asked for `David23` unless the user explicitly approves scratch timing audio.
- Stop before visual plan, HyperFrames build, renders, upload, or self-learning.

## Output Standard

For each selected section, create or update:

- `voiceover/section-XX-kebab-section-name/README.md`
- `voiceover/section-XX-kebab-section-name/section-XX-kebab-section-name-script.txt`
- `voiceover/section-XX-kebab-section-name/section-XX-kebab-section-name-marked-script.md`
- `voiceover/section-XX-kebab-section-name/tts-inputs/`
- `voiceover/section-XX-kebab-section-name/scratch-audio/`
- `voiceover/section-XX-kebab-section-name/scratch-results.json`
- `04-voiceover.md`

`04-voiceover.md` should act as the project-level index for generated and not-yet-generated section voiceovers.

## Feedback Log

### 2026-06-06 - Skill Created

Classification: `Core operational capability`

Context:
The user clarified that the post-script workflow branches into section-by-section production. Full-video voiceover should not be the default because each section is created and reviewed separately, then combined later.

Lesson:
The voiceover skill must be section-first. It should ask which script section to generate, include `All` as the first option, and create separate voiceover outputs for each section.

Apply next time:
Use the section list from `02-script.md`. Do not create a stitched full-video voiceover unless the user explicitly asks for a combined master.

Promote to shared memory:
Yes, as an operational production lesson if not already recorded elsewhere.

### 2026-06-07 - Packaging Before Voiceover

Classification: `Superseded operational lesson`

Context:
The user moved Packaging before Voiceover so title, thumbnail, and YouTube description are decided before audio generation.

Lesson:
Superseded. Packaging is now outside the main pipeline. Voiceover no longer requires `03-packaging.md`.

Apply next time:

- require non-empty `02-script.md`
- do not require `03-packaging.md`
- write or update `04-voiceover.md`, not `03-voiceover.md`

Promote to shared memory:
yes, this is a pipeline-level rule.

### 2026-06-07 - Packaging Outside Main Pipeline

Classification: `Operational lesson`

Context:
The user clarified that packaging is outside the main pipeline. It branches from Research Pack and requires only topic intake and research pack.

Lesson:
Voiceover must not require packaging. For voiceover freshness, only topic intake, research pack, and script matter.

Apply next time:

- require non-empty `02-script.md`
- treat script older than topic/research as stale
- treat voiceover older than script as stale

Promote to shared memory:
yes, this is a channel-wide pipeline rule.

### 2026-06-06 - Explicit Section Selection Required

Classification: `Voiceover lesson`

Context:
The user clarified that the skill must always ask which section to work on and must not assume the target section.

Lesson:
Voiceover generation requires explicit user section selection. The skill may use a section only if the user names that section or chooses it from the options. It must not infer from active project state, previous work, missing files, or the next likely section.

Apply next time:
Ask for `All` or a specific section whenever the target is not explicit. Stop before writing files if no explicit target exists.

Promote to shared memory:
No. This is a `voiceover` skill behavior rule rather than a channel-wide strategy change.

### 2026-06-06 - Scratch Fallback Requires Approval

Classification: `Voiceover lesson`

Context:
The user asked why the generated Section 1 voiceover used `am_adam` instead of the approved `David23 / am_eric` voice.

Lesson:
The skill must not silently fall back to scratch voices when `David23` is requested. If `am_eric` is unavailable, stop, document the missing voice/tooling, and ask before generating any scratch timing audio.

Apply next time:
Use `David23 / am_eric` when available. If unavailable, do not generate `am_adam` or another alternate voice unless the user explicitly approves scratch fallback.

Promote to shared memory:
No. This is a skill behavior rule and local tooling guardrail.

### 2026-06-06 - David23 Works Through Direct am_eric

Classification: `Voiceover lesson`

Context:
Section 1 for `Why Cheap Products Keep Getting Worse` was first generated with `am_adam` because the HyperFrames short voice list did not show `am_eric`. A direct test with `hyperframes@0.6.76` succeeded using `--voice am_eric`.

Lesson:
Do not rely only on the short HyperFrames voice list. For `David23`, test the direct Kokoro voice ID `am_eric`.

Apply next time:
Use:

```text
npx hyperframes@0.6.76 tts <input.txt> --output <output.mp3> --voice am_eric --speed 0.84 --lang en-us --json
```

Promote to shared memory:
Yes. This affects how the approved channel voice is generated.

### 2026-06-21 - TTS Blocked When Python Is Missing

Classification: `Voiceover lesson`

Context:
For `why-everyone-pretends-to-be-busy` Section 1, the proven command
`npx hyperframes@0.6.76 tts ... --voice am_eric --speed 0.84 --lang en-us --json` failed with
`{"ok":false,"error":"Python 3 is required for text-to-speech. Install Python 3.8+ and run: pip install kokoro-onnx soundfile"}`.
Probing showed no `python3`, `python`, `py`, or `pip` on this Windows machine.

Lesson:
HyperFrames Kokoro TTS depends on a system Python 3.8+ with `kokoro-onnx` + `soundfile`. When
Python is absent, TTS cannot run for ANY voice, so a scratch fallback is also impossible — do not
offer scratch as a workaround in that case. This is an environment/tooling block, not an am_eric
voice-availability issue.

Apply next time:
- If `npx hyperframes tts` returns the "Python 3 is required" error, do not retry voices and do not
  fake audio. Still write the clean script, marked script, tts-input, README, and
  `scratch-results.json` with status `tts not generated`, and document the env probe.
- Tell the user to install Python 3.8+ then `pip install kokoro-onnx soundfile`, and that the
  documented command will then generate the MP3 unchanged.
- A quick `python --version` / `pip --version` probe distinguishes "no Python" (scratch won't help)
  from "voice unavailable" (scratch might help with approval).

Promote to shared memory:
no; this is a voiceover tooling/environment guardrail, not a channel-wide strategy change.

### 2026-06-21 - Resolved: Install Python + Bypass Store Stub

Classification: `Voiceover lesson`

Context:
After the Python-missing block (above), the user authorized installing it. `winget install --id
Python.Python.3.12 -e --scope user` installed Python 3.12.10 to
`C:\Users\Anpha Right Choice\AppData\Local\Programs\Python\Python312\`. But the Microsoft Store
`python.exe` alias in `WindowsApps\` still hijacked the `python` command on PATH, so running
`python` directly still printed "Python was not found."

Lesson:
The fix is to prepend the real Python dir to PATH for the TTS command so HyperFrames' `python`
lookup hits the real interpreter, not the Store stub. With that, the standard David23 command
succeeded: `{"ok":true,...,"durationSeconds":21.056}`.

Apply next time (this machine):
- Real Python: `C:\Users\Anpha Right Choice\AppData\Local\Programs\Python\Python312\python.exe` (3.12.10), deps `kokoro-onnx` + `soundfile` already installed.
- In the Bash tool, prepend before npx:
  `export PATH="/c/Users/Anpha Right Choice/AppData/Local/Programs/Python/Python312:$PATH"`
- Then run the normal `npx hyperframes@0.6.76 tts ... --voice am_eric --speed 0.84 --lang en-us --json`.
- A fresh terminal alone may NOT fix it because the Store alias can still shadow `python`; prepending the dir is the reliable fix (or disable the alias in Settings > App execution aliases).

Promote to shared memory:
no; machine-specific environment fix for the voiceover skill.

### 2026-06-21 - Emphasis And Pauses In Kokoro = Shape The Text, Not Tags

Classification: `Voiceover lesson`

Context:
For Section 4 of `why-everyone-pretends-to-be-busy`, the user asked to "emphasize important words"
and "speak with pauses between commas and periods." HyperFrames Kokoro TTS strips markup tags and
has no SSML, so `[emphasis]`/`[pause]` in the marked script do not change the audio.

Lesson:
To actually affect Kokoro delivery, shape the TTS INPUT TEXT:
- Pauses: put each beat/sentence on its own line (hyperframes synthesizes per line and concatenates,
  giving real pauses), add blank lines for longer pauses, and use an ellipsis "..." before a punchline.
- Pseudo-emphasis: isolate a key word with commas (e.g., `Everything says, urgent.`) for a slight lift.
  True per-word stress is not possible in Kokoro.
- Global deliberateness: lower speed (0.80, or the learner 0.78/0.76) — but changing speed mid-video
  breaks consistency, so prefer text-shaping at the kept 0.84 unless the user wants the whole video slower.
Keep the canonical `*-script.txt` as the real script wording (matching 02-script.md); only the
`tts-inputs/*.txt` carries the pause/comma phrasing tweaks. Document the divergence in the section README.

Apply next time:
- When a user asks for emphasis/pauses, edit the tts-input text (line breaks + commas + ellipsis), do
  not rely on markup tags, and tell the user Kokoro can't do real word-emphasis.
- Note whether the delivery applies to one section or should be back-applied to earlier sections for consistency.
- Speed taste signal: after hearing 0.84 pause-tuned, the user wanted "a little faster, just a bit",
  tried 0.88 (too fast), and settled on 0.86 (still keeping the pauses). Treat 0.86 as the user's
  "slightly faster than default" preference for David23/am_eric; flag any cross-section speed mismatch.

Promote to shared memory:
no; this is a voiceover/Kokoro tooling technique, not a channel-wide strategy change.

## Feedback Entry Template

```markdown
### YYYY-MM-DD - <short lesson>

Classification: `Voiceover lesson` / `Operational lesson` / `Experiment`

Context:

Lesson:

Apply next time:

Promote to shared memory:
yes/no, with reason
```
