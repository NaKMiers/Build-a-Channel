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
- Write only the voiceover index file (new projects `03-voiceover.md`; legacy projects `04-voiceover.md` - resolve by suffix per `.agents/rules/video-workflow.md`) and files under `voiceover/`.
- Keep one useful MP3 preview per section by default.
- Avoid preserving duplicate MP3/WAV scratch files unless a renderer requires them or the user asks.
- Use `David23 / am_eric / 0.84 / en-us` as the default final voice direction from shared memory.
- When generating `David23`, test `am_eric` directly with HyperFrames before declaring it unavailable; `hyperframes@0.6.76` accepts `am_eric` even when the short voice list does not display it.
- If local TTS tooling cannot generate `David23`, stop and ask before using any alternate scratch voice.
- Never generate scratch audio as a substitute when the user asked for `David23` unless the user explicitly approves scratch timing audio.
- Author every section TTS input in the APPROVED Section 5 pacing style by default (spacious, heavy
  `...` holds, `. .` staccato on punchy lines). See "Canonical Pacing Template" below.
- Stop before visual plan, HyperFrames build, renders, upload, or self-learning.

## Canonical Pacing Template (follow by default)

APPROVED GOLD STANDARD: the user loves the pace, tone, and pause of `why-everything-is-a-subscription-now`
Section 5 (final heavy-pause version, `David23 / am_eric / 0.84`, ~50s for ~195 words). Generate ALL
future section TTS inputs in this style by default - do not wait to be asked, do not start sparse.

Exemplar file to imitate (read it before authoring a new tts-input):
`projects/3-why-everything-is-a-subscription-now/voiceover/section-05-free-trial-countdown/tts-inputs/section-05-free-trial-countdown-tts.txt`

The Section 5 recipe (concrete, copyable):
- SPACIOUS BY DEFAULT. Put a standalone `...` line between almost every spoken beat. Use 2-3 stacked
  `...` lines for the bigger holds (before reveals, before/after punchlines, around the thesis).
- Trailing `...` on every setup phrase so the voice lifts and hangs before the payoff lands on its
  own line ("Just pop in your card..." -> hold -> "you know, for no reason at all.").
- `. .` inline on punchy short statement-list lines so each lands separately, not blurred
  ("Strangers love holding your card. .", "For seven days. .", "A mystery charge. .",
  "Three dollars. .", "Every month. .").
- Split comma lists into one line per item, each trailing `...` ("The charge is small... / the date
  is fuzzy... / life is loud.").
- Precede the key reveal / deadpan punchline with 3 stacked `...` ("Your free trial of financial
  awareness... / ... / ... / has expired.").
- Keep speed at the default `0.84` and shape ALL the pacing with ellipses + `. .` (not speed), unless
  the user explicitly asks for a slower voice on a specific section (e.g. S3 was 0.82 by request).
- Levers reminder (measured): only `...` (~0.28s) and `.` (~0.21s) add pause; `. .` resets prosody
  without adding length; commas, line breaks, and `_` add nothing.

Density check: a finished section should have MANY more `...` lines than spoken lines - if it reads
sparse/even, it will sound "đều đều, buồn ngủ" (flat, sleepy). When unsure, add more holds, not fewer.
The user's repeated direction across S3/S4/S5 was always "more pause".

## Output Standard

For each selected section, create or update:

- `voiceover/section-XX-kebab-section-name/README.md`
- `voiceover/section-XX-kebab-section-name/section-XX-kebab-section-name-script.txt`
- `voiceover/section-XX-kebab-section-name/section-XX-kebab-section-name-marked-script.md`
- `voiceover/section-XX-kebab-section-name/tts-inputs/`
- `voiceover/section-XX-kebab-section-name/scratch-audio/`
- `voiceover/section-XX-kebab-section-name/scratch-results.json`
- the voiceover index file (`03-voiceover.md`; legacy `04-voiceover.md`)

The voiceover index file (`03-voiceover.md`; legacy `04-voiceover.md`) should act as the project-level index for generated and not-yet-generated section voiceovers.

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
- do not require packaging
- write or update the voiceover index file (SUPERSEDED 2026-06-26: new projects now use `03-voiceover.md` because packaging left the numbered set; legacy projects keep `04-voiceover.md`. Resolve by suffix.)

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
Python is absent, TTS cannot run for ANY voice, so a scratch fallback is also impossible - do not
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
- Pauses: WRONG to rely on line breaks or commas - both are ignored for timing on this build. Use
  PERIODS and ELLIPSES. See the 2026-06-23 measured correction below for the verified table.
- Pseudo-emphasis: true per-word stress is not possible in Kokoro. Comma-isolation gives at most a
  slight intonation change, not a timing pause.
- Global deliberateness: lower speed (0.80, or the learner 0.78/0.76) - but changing speed mid-video
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

### 2026-06-23 - MEASURED: Line Breaks AND Commas Do NOT Pause; Use Periods/Ellipses (Correction)

Classification: `Voiceover lesson`

Context:
For `why-everything-is-a-subscription-now` Section 2 the user added extra blank lines to the tts-input
and the regenerated audio was byte-identical (`33.003s` -> `33.003s`). The user then asked why line
breaks produce no audible pause. Rather than guess, ran a controlled experiment with
`hyperframes@0.6.76 tts ... --voice am_eric --speed 0.84` on the same 8-word phrase
("The cat sat / the dog ran / the bird flew"):

| Separator                | Duration | Pause vs no-punct |
| ------------------------ | -------- | ----------------- |
| no punctuation           | 2.581s   | baseline          |
| commas `,`               | 2.581s   | none (identical!) |
| line breaks / blank lines| 2.795s*  | none (newlines flattened; the .214 here is the periods, not the breaks) |
| em dash `-`              | 2.645s   | ~0.06s (tiny)     |
| period `.`               | 2.795s   | ~0.21s            |
| ellipsis `...`           | 2.859s   | ~0.28s (largest)  |

This DISPROVES the 2026-06-21 claims that "each sentence on its own line gives real pauses" and that
comma-isolation adds a pause. Both the per-section files used the same `0.6.76` build, so the older
"pauses" were actually the PERIODS in the text, mis-attributed to line layout.

Lesson:
This HyperFrames Kokoro build flattens ALL whitespace (newlines + blank lines) into one continuous
string before synthesis. Timing pauses come ONLY from punctuation and `--speed`. Measured pause
strength: ellipsis `...` > period `.` > em dash `-` > comma `,` ≈ nothing ≈ line break. Even the
strongest single mark adds only ~0.2-0.3s, so a long dramatic silence is NOT achievable from text
punctuation alone.

Apply next time:
- Do NOT shape pauses with line breaks or commas - they do nothing for timing on this build. The
  canonical `*-script.txt` and `tts-inputs/*.txt` line layout is for human readability only.
- For a noticeable beat, use `...`; for a normal sentence stop, a period; chain `. ...` or split into
  more sentences to stack ~0.2s holds.
- For a LONG/dramatic pause, add real silence at the HyperFrames render/assembly stage (visual holds
  while audio is quiet) - TTS text cannot produce it.
- For a uniformly slower read, use `--speed` (0.80 / learner 0.78 / 0.76), not punctuation.
- Fast confirmation that an edit changed nothing: the JSON `durationSeconds` is identical to the prior run.

Promote to shared memory:
no; voiceover/Kokoro tooling behavior, not a channel-wide strategy change.

### 2026-06-23 - User's Punctuation Rhythm Style (Anti-Monotone Delivery)

Classification: `Voiceover lesson`

Context:
On `why-everything-is-a-subscription-now`, the user repeatedly re-tuned the S1 and S2 tts-input files
by hand, then told me my own punctuation choices made David23 sound "không ấn tượng, không có nhân
nhá tone giọng gì hết, nghe cứ đều đều rất buồn ngủ" (flat, no light/shade, monotone, sleepy). They
asked me to LEARN their `... . , _` style so I produce it myself next time. Decoded from their files
+ measured tests (`am_eric`, speed 0.84):

Root cause of my flat output: I used uniform, sparse punctuation -> even rhythm -> monotone. The fix
is deliberate RHYTHM VARIATION + rising-suspense holds, exactly what the user's files do.

The user's verified style toolkit:
- Trailing `...` on an UNFINISHED phrase (e.g. `Whatever number you guessed...` then `it's higher.`)
  = the voice lifts and hangs, then drops on the payoff. THE key anti-monotone move; use it often on
  setup->payoff pairs. I under-used this.
- Stacked `...` on their own lines (2-3 in a row) = long dramatic hold after a question or before a
  punchline. Measured: stacking ellipses DOES add real time (unlike line breaks/commas).
- `. .` (a period, space, then a lone period) = hard sentence RESET between short punchy lines so each
  lands with its own fresh intonation instead of blurring into a monotone run-on. Measured: it does
  NOT add pause length (`. .` ~= `.` in duration); its value is the prosody reset / staccato landing.
- Commas = FLOW, not pause (measured ~0 added time). Long comma-runs (e.g. "your apps, your shows,
  your software, even buttons inside your car") are meant to RUSH together as one breath. The CONTRAST
  between fast comma-runs and choppy `. .` lines is what creates dynamics.
- `_word_` underscores: NO measurable effect in this Kokoro build (tested `_really_` == `really`,
  identical duration). True per-word stress is impossible; "stress" a word by isolating it with stops/
  ellipses around it. The user listed `_` but their files don't actually use it.

Measured pause strength (same 8-word phrase, speed 0.84), to combine with the rhythm rules:
ellipsis `...` (~0.28s) > period `.` (~0.21s) > em dash `-` (~0.06s) > comma `,` ~= line break ~= 0.

Apply next time (author tts-inputs in THIS style by default, don't wait to be told):
- Vary pause lengths within a section: single `.` (short), `. .` (reset/staccato), trailing `...`
  (suspense lift), stacked `...`/`...` lines (long dramatic hold). Even rhythm = sleepy; varied = alive.
- On every setup->payoff or question->answer pair, end the setup with a trailing `...` and let the
  payoff land on its own short line.
- Use `. .` between short punchy list items and thesis lines so they don't blur (e.g.
  `An app. .` / `A "free" trial that stopped being free. .` / `A show you watched once.`).
- Keep deliberate fast comma-runs for "everything everywhere" rushes, then contrast with hard stops.
- Keep the canonical `*-script.txt` as clean real wording; all this rhythm shaping lives only in
  `tts-inputs/*.txt`. Document any divergence in the section README.
- After regen, the JSON `durationSeconds` changing confirms the edit had a real timing effect (e.g.
  adding ellipses raised S2 from 33.109 -> 33.792s; line-break-only edits leave it identical).
- Speed taste signal (this project, `why-everything-is-a-subscription-now`): for a dense/heavy section
  the user wanted it slower, asking for BOTH `--speed 0.82` AND extra `...` holds together (S3 went
  44.928s@0.84 -> 48.896s@0.82). So "slower" can mean lower speed + more ellipses combined, not just
  one. When a user asks for a slower section, offer both levers and note any mismatch.
- FINAL speed for this project: after iterating (0.84 -> S3 at 0.82 -> 0.81 -> whole video at 0.79 ->
  whole video at `0.8`), the user settled on a unified `0.8` across all 7 sections on top of the S5
  spacious pacing. Takeaway: this user trends slower than the 0.84 channel default for learner clarity
  and likes to A/B nearby speeds whole-video. When starting a new video for them, expect the comfortable
  speed around `0.79-0.82` with heavy `...` pacing; offer `~0.8` early, and ALWAYS keep all sections at
  one speed (per-section mismatches always get unified later, so don't create them).

Reference exemplars to imitate (this project, user-tuned):
- `projects/3-why-everything-is-a-subscription-now/voiceover/section-01-hook/tts-inputs/section-01-hook-tts.txt`
- `projects/3-why-everything-is-a-subscription-now/voiceover/section-02-reframe/tts-inputs/section-02-reframe-tts.txt`

Promote to shared memory:
no for now; it's a Kokoro tts-input authoring technique. But it materially improves delivery on EVERY
video, so apply it on all future sections by default and revisit promoting a short "voice rhythm"
note to `script-learner-voice.md` if the user confirms the style across more videos.

### 2026-06-24 - Kokoro Spells Out Non-Word Letter Clusters (shh -> "s-h-h")

Classification: `Voiceover lesson`

Context:
On `why-buy-1-get-1-beats-50-off` Section 7, the tts-input contained "shh... relax." The owner heard
David23 read it as the three letters "s-h-h" instead of the shushing sound. Fix: change the tts-input
to the real word "shush" ("shush... relax."), which Kokoro pronounces as /ʃʌʃ/ and carries the same
intent. Canonical `*-script.txt` kept "shh" to match `02-script.md`; only the tts-input diverged, and
the divergence is documented in the section README.

Lesson:
HyperFrames Kokoro spells out short non-dictionary letter clusters letter-by-letter (interjections,
onomatopoeia, initialisms): "shh", "hmm", "pfft", "ugh", "tsk", "brb", etc. can come out as named
letters or garbled. For anything meant as a SOUND, write a real dictionary word the model knows, or a
phonetic respelling that maps to normal English phonemes.

Apply next time:
- When a script line uses an interjection/onomatopoeia/initialism, swap it in the tts-input for a
  pronounceable real word: shh -> "shush", hmm -> "hmmm" usually works but test, ugh -> "ugh" test,
  initialisms -> spell the intended delivery ("F B I" if you WANT letters, "fibbie" if not).
- Keep the canonical `*-script.txt` matching `02-script.md`; put the pronounceable form only in the
  tts-input and note the divergence in the section README.
- Quick proof the swap worked: regenerate and listen (and the JSON `durationSeconds` shifts).

Promote to shared memory:
no; Kokoro tts-input authoring guardrail, not a channel-wide strategy change. Fold into a future
"voice rhythm / tts quirks" note in `script-learner-voice.md` if more quirks accumulate.

### 2026-06-27 - $9.99 hook: owner A/B'd speed down to 0.79 and wanted a shorter, condensed hook

Classification: `Voiceover lesson`

Context:
On `why-everything-costs-9-99` Section 1, I generated the hook at the channel default 0.84 (25.7s, 99
words) and offered 0.80. The owner replied: "it should be 0.82, should make the hook script shorter and
more condense." Trimmed the script ~99 → ~63 words (cut the "most powerful penny on earth" line, moved
to contractions, kept the trap question + "your brain said nine" reveal + "still get you tomorrow"
close) and regenerated at 0.82 → 19.456s. He then auditioned downward in single-step nudges: "0.80"
(20.672s), then "0.79" (21.739s), landing on 0.79. Each regen removed the prior MP3 (one preview per
section). Speed locked at 0.79 for all later sections of this video.

Lesson:
This owner's comfortable David23 speed is the slow end of the predicted band - he A/B'd 0.84 → 0.82 →
0.80 → 0.79 and settled on 0.79 (even slower than `why-everything-is-a-subscription-now`'s 0.8). Default
to ~0.79-0.80 for him, not 0.84. He also has a clear taste for a SHORT, punchy hook - when a hook runs
long, expect "shorter / more condense," so draft hooks tight and lean on contractions for the open. He
auditions speed in fast one-step nudges (just a bare number like "0.79"), so generate one, expect a
nudge, regen cheaply, and don't over-document until it stabilizes.

Apply next time:
- For this owner, generate at ~0.79-0.80 first (offer one step faster as an A/B); keep all sections at the one chosen speed.
- Draft hooks tight from the start (~60-70 words), then expand only if asked; condensing is the common note.
- When the hook wording changes, update `02-script.md` (rev bump + summary row + header totals) AND
  regenerate the section audio at the locked speed, replacing the old MP3.

Promote to shared memory:
no; confirms the existing ~0.8 speed preference and is a per-owner hook-length taste, not a
channel-wide change.

### 2026-06-27 - "All" batch TTS exceeds the 2-min default Bash timeout; batch in 3-4s or raise it

Classification: `Voiceover lesson`

Context:
On `why-everything-costs-9-99` the user chose "all remaining section" (2-7). Running all six `npx
hyperframes@0.6.76 tts` calls in one Bash command hit the 120s default timeout after 4 sections
(2,3,4,5 done; 6,7 not). Re-ran 6-7 in a second call with `timeout: 240000` and they finished.
Each section gen is ~20-35s wall (model load + synth), so 6 sequential calls > 2 min.

Lesson:
For `All`-mode generation, don't run more than ~4 TTS calls in a single default-timeout Bash call.
Either pass an explicit longer `timeout` (e.g. 240000-480000) or split into batches of 3-4. The npx
calls are idempotent per output path, so a re-run of the unfinished ones is safe and doesn't duplicate
(one MP3 per section folder, fixed filename).

Apply next time:
- `All` mode: raise the Bash `timeout` (~60s per section budget) or chunk into 2 batches.
- After a timeout, `ls */scratch-audio/` to see which sections completed, then generate only the rest.

Promote to shared memory:
no; voiceover tooling/runtime guardrail, not a channel-wide strategy change.

### 2026-07-08 - P6 shipped best-ever: pacing-via-punctuation + one owner-locked speed is the voiceover standard

Classification: `Voiceover lesson`

Context:
`6-why-countries-fight-to-host-the-world-cup` shipped and the owner called it the best video the channel
has made (voice explicitly praised). Re-read of `03-voiceover.md` + the section `tts-inputs/` confirms the
approach that produced the loved narration; lock it in as the default.

Lesson (apply to every future video):
- ONE OWNER-LOCKED SPEED FOR THE WHOLE VIDEO, found by a bare-number A/B ladder on Section 1 only
  (P6: 0.79 -> 0.80 -> 0.81, owner nudged to 0.81), then ALL sections generated at that locked speed.
  Do the ladder on the hook, lock, and stop re-auditioning speed per section.
- PACING IS SHAPED IN THE `tts-inputs/*.txt` VIA PUNCTUATION, not via speed or SSML: standalone `...`
  hold lines, stacked `...` before a reveal/punchline, `. .` staccato resets, trailing `...` on setup
  phrases. The script's `[beat]`/`[slower]`/`[deadpan]` markup is STRIPPED for TTS and REALIZED as these
  punctuation holds. Wording in the tts-input must match `02-script.md` EXACTLY (only spacing differs).
- ISOLATE THE THESIS AND PUNCHLINE LINES with their own holds so they breathe ("It is a purchase.";
  "Full of buses."; "Two dollars fifty."; "Who keeps the tickets?"). The channel voice = a calm person
  explaining something ridiculous; the silence around the punchline is what makes it land.
- ONE MP3 PREVIEW PER SECTION at the locked speed; keep a per-section duration table (P6 total 434.24s,
  ~7:14) so combine/caption inherit accurate timings. Expect the spacious holds to run the real audio a
  bit longer than the flat-read word estimate - that is intended, not drift.
- REGEN DISCIPLINE: if a script section's wording changes, regenerate ONLY that section's MP3 at the
  locked speed and replace it; do not re-ladder speed.

Apply next time: ladder+lock speed on the hook, then shape every section's delivery through punctuation
holds in tts-inputs (markup stripped, wording exact), isolating thesis/punchline lines.

Promote to shared memory:
no; confirms + sharpens the existing ~0.8-speed and pacing-via-punctuation preferences already logged.

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
