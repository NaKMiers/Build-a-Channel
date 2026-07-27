# TossExplain

Production repo for **TossExplain** — a YouTube channel of hand-drawn doodle explainers about
psychology, anthropology, and self-help.

Every video answers one question the viewer has personally felt ("why do you feel lonelier in a
crowd than alone in your room?") by hitting three pillars in order:

1. **Psychology** — the real mechanism in the mind, with named research
2. **Anthropology** — the ancestral world that installed it
3. **Self-help** — one concrete shift the viewer can make tonight

This repo holds no video editor and no rendering code. It holds the **prompts that drive the AI
pipeline**, the **tools** that turn narration audio into timestamps, and the **per-video artifacts**
(script, transcript, character sheets, scene images) each episode produces.

---

## Repository layout

```
master-prompt.md        The 5-stage video engine — the heart of the channel
character-prompt.md     Reference-sheet prompts for the current cast (TRUE STICKMAN style)
MASCOT.jpeg             Channel mascot
tools/                  Audio/subtitle → [M:SS] transcript converters
projects/               One folder per video
  <n>-<title-slug>/
    transcribes/        script_*.txt, transcript*.txt, words.json
    characters/         NAME.jpeg reference sheets (YOU, FRIEND, CROWD, …)
    prompts/            image-prompts.md, video-prompts.md
    scenes/             Generated scene images, named by timestamp
```

Generated media (`*.mp3`, `*.wav`, `*.mp4`) and `.env` are gitignored — regenerate them from the
script rather than committing them.

---

## The pipeline

[master-prompt.md](master-prompt.md) is a single prompt you paste into an AI chat. It runs five
stages and **waits for you between each one** — never skip ahead, never reorder.

| Stage                 | You say                              | It produces                                                                                                               |
| --------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| **1 — Topics**        | _(activate the prompt)_              | 5 viral topic ideas as a table; you pick a number                                                                         |
| **2 — Script**        | the number                           | `script_[topic].txt` — 1,800–2,500 words of pure 2nd-person narration, delivered as a **downloadable file**, never inline |
| **3 — Cast**          | `cast`                               | A 2–6 entry cast table + one reference-sheet prompt per character, each in its own code block, labeled with its file name |
| **4 — Image prompts** | _(paste the timestamped transcript)_ | One image prompt per timestamp, in batches of 20; reply `next` between batches                                            |
| **5 — Metadata**      | `yes`                                | Viral title, full description with hashtags, and 25–40 SEO tags — three separate code blocks                              |

Between Stage 2 and Stage 4 you record the narration and convert it to timestamps — see
[Tools](#tools) below.

### Stage 3 — why the cast exists

The channel's one hard visual failure mode is **character drift**: the same person looking slightly
different in every frame, so the video reads as if five people drew it.

The fix is a named cast. Each member gets a ONE-WORD ALL-CAPS name and a reference sheet saved as
`characters/NAME.jpeg`. From Stage 4 onward, prompts refer to a character **only** as `@NAME` and
never re-describe them — the sheet carries the design, the prompt carries only action, expression,
and framing.

Rules that matter:

- **`@YOU` is always Toss, the channel mascot.** Toss is the one permanent character on TossExplain
  and appears in every video as the viewer stand-in. His design is fixed channel-wide — oversized
  white circle head at ⅓ of his height, a tuft of 3–4 spikes breaking the head outline, wide black
  oval eyes, thick separate brows, one line mouth, thin limbs with splayed fingers. Canonical sheet:
  [MASCOT.jpeg](MASCOT.jpeg), which you attach when generating each video's `YOU` sheet.
  Only his **costume** changes per video — hoodie for a modern section, a hide wrap if the script
  puts `@YOU` in prehistory. Costume color is free; recognition comes from the head, hair, face, and
  build, never from a color. Toss plays `@YOU` and nothing else.
- **Every other cast member is derived from the script, never templated.** No house cast, no default
  ancestor. If the anthropology section is set in a monastery, the character is a monk — not a
  caveman. Never default to the Neolithic farmer, brown tunic, hoe, or wheat stalk. The figure
  carrying that section is a genuinely different person, never Toss in a costume.
- Cast size 2–6. Fewer is better. A recurring group (`CROWD`, `TRIBE`) counts as **one** entry.
- No `@` token may be used in Stage 4 unless it exists in that video's cast table.

[character-prompt.md](character-prompt.md) holds the reference-sheet template. It specifies the TRUE
STICKMAN look (circle head, single-line spine, no filled torso), the 16:9 model-sheet layout, and a
hard **absolutely-no-text** rule — image models love to label panels "FRONT / SIDE / BACK", and every
such label has to be suppressed explicitly.

### Stage 4 — image prompt anatomy

Every prompt is one line, beginning with its timestamp copied **character for character** from the
transcript (`[0:00]` stays `[0:00]`) — those strings become the scene file names.

```
[0:17] Hand-drawn 2D doodle cartoon animation, flat colors, bold black outlines, slightly
imperfect sketchy marker lines, @YOU centered with a hollow ache expression …, plain white
background, bold red ALL CAPS text "A COLD HOLLOW" at the top of the frame, no gradients, no
shadows, no textures, no photorealism, no 3D, no timestamp shown in the image, @[name] is
mention syntax for reference only and must never be rendered as visible text, 16:9 aspect
ratio, educational YouTube explainer doodle style.
```

- Opens with the **style anchor**, ends with the **style lock** — both verbatim, every time.
- The timestamp and the `@TOKEN`s are instructions for you and the file system. They must **never**
  render as visible text in the image, which is why the style lock repeats that negative.
- Hold a scene across consecutive timestamps. Three lines about the same moment = same scene, same
  background, only the expression changes. Don't invent a new scene every 5 seconds.
- Emotion lives in the eyebrows, mouth line, posture, and head color (red = embarrassed/angry,
  white = neutral, blue-tinted = sad/cold) — not in background detail.

When generating, attach **only** the reference sheets for the `@` tokens that appear in that prompt.

### Visual style DNA

Flat colors, bold black outlines, sketchy marker lines. Flat solid color backgrounds only — **zero**
gradients, shadows, or textures. Always 16:9.

Background color carries tone: white = modern everyday · tan/dark blue = ancient · orange = fire or
ritual · cobalt blue = inside the mind · solid blue = lab/science · green ground + blue sky = outdoors.

Palette: `#F5820D` orange · `#2D5FBF` cobalt · `#3A9E3A` green · `#F5C518` yellow · `#D94040` red ·
`#8B5E3C` brown · `#6EB5E8` sky · `#C4965A` tan · `#FFFFFF` white.

On-screen text is bold ALL CAPS hand-lettered marker, placed at the top of the frame, in red, black,
or yellow.

---

## Tools

Both scripts emit the `[M:SS] line of narration` format that Stage 4 consumes. They share
[tools/tsfmt.py](tools/tsfmt.py), which does the line-splitting: lines break where the narrator
actually paused and after every sentence, so a short sentence stays its own line.

### `audio-to-timestamps.py` — narration audio → transcript

```bash
# Forced alignment (recommended): you supply the audio AND the script it was read
# from, so the wording is never wrong. Needs ELEVENLABS_API_KEY. ~$0.08 / 12-min video.
python3 tools/audio-to-timestamps.py voice.mp3 \
    --script projects/1-.../transcribes/script_why_you_feel_lonelier_in_a_crowd.txt \
    -o transcript.txt

# Plain transcription, no script needed. Needs GROQ_API_KEY. Under a cent per video,
# but wording and punctuation can drift from your script.
python3 tools/audio-to-timestamps.py voice.mp3 --engine groq -o transcript.txt

# Multiple files are treated as consecutive parts of one recording
python3 tools/audio-to-timestamps.py part-1.mp3 part-2.mp3 --script s1.txt --script s2.txt
```

Useful flags: `--max-dur` (split any line holding more than N seconds; default 4.5), `--pause`
(new line wherever the narrator paused this long; default 0.30), `--min-words`, `--max-chars`,
`--save-json` / `--from-json` (cache the API result so you can re-cut the transcript for free).

A 12-minute script lands around 230 lines of ~3s each. Re-run with a larger `--max-dur` to get
fewer, longer scenes — see `transcript-min3.txt` and `transcript-min5.txt` in the example project.

### `srt-to-timestamps.py` — existing subtitles → transcript

```bash
python3 tools/srt-to-timestamps.py part-1.srt part-2.srt -o transcript.txt
python3 tools/srt-to-timestamps.py caption.vtt --min-dur 5 --max-chars 180
python3 tools/srt-to-timestamps.py part-2.srt --offset 4:12
```

Set API keys in a gitignored `.env` (or export them) before running the audio tool.

---

## Making a new video

1. Create `projects/<n>-<title-slug>/` with `transcribes/`, `characters/`, `prompts/`, `scenes/`.
2. Activate [master-prompt.md](master-prompt.md), pick a topic (Stage 1), get the script (Stage 2).
   Save it to `transcribes/script_[topic].txt`.
3. Record the narration.
4. Convert it: `audio-to-timestamps.py` with `--script` → `transcribes/transcript.txt`.
5. Reply `cast` (Stage 3). Generate each reference sheet with the prompts from
   [character-prompt.md](character-prompt.md); save them as `characters/NAME.jpeg`.
6. Paste the transcript (Stage 4). Work through the batches with `next`, saving them to
   `prompts/image-prompts.md`.
7. Generate each scene image, attaching only the sheets for the `@` tokens in that prompt. Save to
   `scenes/` named by timestamp.
8. Reply `yes` (Stage 5) for the title, description, and tags.
9. Assemble and upload.

`projects/1-why-you-feel-lonelier-in-a-crowd-than-alone-in-your-room/` is the worked example — read
its `prompts/image-prompts.md` alongside `transcribes/transcript.txt` to see the whole mapping.

---

## Editorial guardrails

- **Never shame the viewer.** The emotional promise is relief: _you are not broken, you are running
  ancient software in a world it was never written for._
- **Never diagnose, never prescribe treatment, never mention medication.** If a topic brushes
  anxiety, depression, or trauma, stay at the level of ordinary human experience.
- Every scientific term gets decoded in plain English immediately.
- Second person throughout — "you", "your brain", "your ancestors". Never "we" or "I".
- History and prehistory are supporting material, never the subject. If a script could run without
  the viewer's inner life in it, it's the wrong script.
- End on a closing line that echoes the opening, completely reframed.
- **Off-limits:** pure history with no inner-life payoff, pure advice with no science underneath,
  dated news, politics, religion as a truth claim, medical prescriptions.
