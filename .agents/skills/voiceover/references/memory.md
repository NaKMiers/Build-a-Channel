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
- Write only `03-voiceover.md` and files under `voiceover/`.
- Keep one useful MP3 preview per section by default.
- Avoid preserving duplicate MP3/WAV scratch files unless a renderer requires them or the user asks.
- Use `David23 / am_eric / 0.84 / en-us` as the default final voice direction from shared memory.
- When generating `David23`, test `am_eric` directly with HyperFrames before declaring it unavailable; `hyperframes@0.6.76` accepts `am_eric` even when the short voice list does not display it.
- If local TTS tooling cannot generate `David23`, stop and ask before using any alternate scratch voice.
- Never generate scratch audio as a substitute when the user asked for `David23` unless the user explicitly approves scratch timing audio.
- Stop before packaging, visual plan, HyperFrames build, renders, upload, or self-learning.

## Output Standard

For each selected section, create or update:

- `voiceover/section-XX-kebab-section-name/README.md`
- `voiceover/section-XX-kebab-section-name/section-XX-kebab-section-name-script.txt`
- `voiceover/section-XX-kebab-section-name/section-XX-kebab-section-name-marked-script.md`
- `voiceover/section-XX-kebab-section-name/tts-inputs/`
- `voiceover/section-XX-kebab-section-name/scratch-audio/`
- `voiceover/section-XX-kebab-section-name/scratch-results.json`
- `03-voiceover.md`

`03-voiceover.md` should act as the project-level index for generated and not-yet-generated section voiceovers.

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
