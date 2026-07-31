---
name: video-swipe
description: Turn one competitor YouTube video into a swipe-file study under research/videos-swipe/<slug>/, with every distinct frame extracted, contact sheets, frame-index.csv, and a Vietnamese visual-analysis.md. Requires the YouTube link plus the video file downloaded from that same link, and refuses to run if the file is not that video. Use when the user says "video-swipe", "phan tich video", "extract frame", "analyze this video", or gives a YouTube link plus a local video file.
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
  - Skill
---

# video-swipe

Research skill, not part of the episode pipeline. It answers one question about a video
that already worked: **what visual decisions made it hold attention**, frame by frame.

The output is a folder under `research/videos-swipe/<slug>/` holding every distinct visual
state of the video, an index, contact sheets, and `visual-analysis.md` written in
Vietnamese. Later skills do not read this folder. Humans do, and so does whoever writes
the next scene prompts.

Two artifacts already exist in this shape and are the reference for everything below:

- `research/videos-swipe/the-rarest-human-possible/` (181 frames, 8 sheets)
- `research/videos-swipe/what-did-ancient-humans-do-when-it-rained-all-week/` (355 frames, 15 sheets)

## Read first

- `.agents/rules/house-rules.md` - note the sanctioned exception: this skill's
  `visual-analysis.md` is Vietnamese with diacritics. Everything else stays ASCII, and the
  no-em-dash rule still applies here.
- `.agents/rules/visual-style.md` and `.agents/rules/channel-dna.md` - needed for the two
  closing sections of the analysis, which say what TossExplains can and cannot borrow.
- `.agents/skills/video-swipe/references/memory.md`
- At least the section skeleton of one existing `visual-analysis.md`.

## Inputs, both required

1. A YouTube link or a bare 11 character video id.
2. A path to the video file, downloaded from that same link by the user.

If either is missing, ask for it and stop. **Never download the video.** No yt-dlp, no
scraping the stream. The user downloads, this skill reads what is on disk.

## Step 0 - Verify the file is that video. Hard gate.

```bash
python3 tools/video-frames.py ensure-ffmpeg
export FFMPEG=<path it prints>          # skip if ffmpeg is already on PATH

python3 tools/youtube-verify.py "<link-or-id>" "<video-file>"; echo "exit=$?"
```

Branch on the exit code, never on the prose:

| Exit | Verdict | What to do |
| ---: | --- | --- |
| 0 | VERIFIED | Proceed to Step 1, and take the title, channel, and slug from `facts`. |
| 3 | MISMATCH | **Stop.** Report the reason verbatim. Do not extract a single frame. |
| 4 | INCONCLUSIVE | Escalate, see below. Nothing gets extracted until it resolves. |
| 2 | ERROR | Bad link shape, dead or private link, missing file, or no video stream. Stop. |

What the tool checks, and in what order:

1. The link resolves to a public video, via the oEmbed endpoint. A typo, a private video,
   or a deleted one is an ERROR before the file is even opened.
2. The 11 character id appears in the file name. Every downloader embeds it and ids are
   case sensitive, so this alone is VERIFIED.
3. A **different** id sits in the file name: MISMATCH.
4. The real title, fetched from oEmbed, matches the file name slug. A downloader names its
   output after the title of the video it actually fetched, so a long match is VERIFIED.
5. `--expect-duration` against the container duration. A duration that disagrees is a
   MISMATCH even when the title matches, since a title can be typed by hand.

The oEmbed lookup also hands back the exact title, the channel name, and a ready-made
`slug`, which Step 1 and the analysis header use instead of anything retyped by hand.

**The duration is not fetchable by script.** The watch page carries it, but from this
machine YouTube answers `LOGIN_REQUIRED / "Sign in to confirm you are not a bot"`, so
`lengthSeconds` never arrives, and forging another client to defeat that check is not
something this repo does. When the duration matters, read it with a real browser session.

**Escalating an INCONCLUSIVE.** Read `facts` first, it says which evidence was missing.

- `title_conflict: true` means the file name was built from **some other video's title**.
  Treat it as a wrong file: do not extract, tell the user which title the link really has
  and which one the file carries, and wait. The two innocent explanations are a renamed
  file and a localized title, since YouTube serves titles per language.
- Otherwise the file name simply says nothing, for example `video.mp4`. Use the `/browse`
  skill on `https://www.youtube.com/watch?v=<ID>` to read the length off the page, then:

```bash
python3 tools/youtube-verify.py "<link-or-id>" "<video-file>" --expect-duration <seconds>
```

Never use `mcp__claude-in-chrome__*` for that; `/browse` is the sanctioned path.

If it is still inconclusive, say exactly what does not line up and ask the user to confirm
in one sentence that the file is that video. Proceed only on an explicit yes, and write one
line in the analysis header saying verification was manual.

If the verdict is MISMATCH and the user insists the pairing is right, say once why the tool
disagrees, then proceed at their direction and note in the report that the gate was
overridden.

**An unverifiable run is an error, not a weaker run.** If YouTube cannot be reached, the
tool answers ERROR and you stop there: report it and run nothing else. No probe, no
candidates, no folder created. There is no silent fallback to the file name, because a run
that never asked the one authority on what the link points at would still print VERIFIED.

`--offline` is the explicit escape hatch, and using it is the user's call, not yours. Offer
it when the network is down, say plainly that it verifies from the file name alone, and put
one line in the analysis header recording that the link was never checked live.

## Step 1 - Name the folder and park the video

**Use the `slug` that Step 0 printed in `facts`.** It is the real YouTube title, lowercased,
with every run of non-alphanumeric characters turned into a single hyphen: "What Did Ancient
Humans Do When It Rained All Week?" gives
`what-did-ancient-humans-do-when-it-rained-all-week`. Derive it by hand only when the
lookup was skipped or unreachable, using that same rule.

Take `facts.title` and `facts.channel` for the analysis header too, rather than retyping
either. The channel name in particular is easy to get subtly wrong: the first study of this
kind wrote "InkExplainer" while the channel is "Ink Explainer".

```bash
R="research/videos-swipe/<slug>"
mkdir -p "$R"
mv "<video-file>" "$R"/          # keep the video beside its analysis
```

Show the slug before creating anything. `*.mp4` is gitignored, so the video stays local
while the frames and the analysis are committed, which is what the two existing folders do.

Pick a working directory **outside the repo** for the candidates, they are scaffolding:

```bash
W=<scratch dir>/video-swipe-<slug>
```

## Step 2 - Extract candidates

```bash
python3 tools/video-frames.py probe "$R"/<video>
python3 tools/video-frames.py candidates "$R"/<video> --work "$W"
```

Scene detection at threshold 0.02, low on purpose: it has to catch a single icon being
added, not just hard cuts. Expect roughly 30 candidates per minute of video and about one
minute of runtime per twelve minutes of video. It writes `$W/cand/`,
`$W/candidates.json`, `$W/showinfo.log`, and `$W/review-sheets/`.

Raise `--threshold` only if the video has film grain or camera shake and the candidate
count is absurd. A doodle explainer that yields almost no candidates is far more likely to
be the wrong input file than a genuinely static video.

## Step 3 - Look at every review sheet. Do not skip, do not sample.

The review sheets are 6 frames each at 776 px wide, sized so on-screen text is readable
after the API downscales the image. The 24-up contact sheets are the deliverable, not a
reading aid: at 400 px a caption is unreadable, and an analysis written off them will
invent text that is not in the video.

Read the sheets in batches of four to eight. **Write your notes to a file in `$W` as you
go, after every batch.** Images fall out of context when the conversation is summarized;
notes on disk survive. The first run of this workflow lost thirty sheets that way and had
to read them twice.

For each candidate record, in one line: the id, the timestamp, the mode, the subject, any
on-screen text verbatim, and whether it is a build step on the previous frame. A useful
mode vocabulary, taken from the two videos studied so far:

- `FULL` - full-bleed painted or coloured scene, story work
- `WHITE` - white card: diagram, number, map, object card, big type
- `NARR` - narrator alone on white, a punctuation beat
- `SPLIT` - a comparison card, this-versus-that

Count the modes and the mode switches when you are done. That census is the spine of the
analysis: on the ancient-humans video it was 51.5 / 40.3 / 7.0 percent with 138 switches,
and that single number explained more than any individual frame did.

## Step 4 - Decide which candidates to drop. You decide, not the tool.

The candidates stage prints two shortlists: frames whose mean difference from the previous
candidate is at or below 12, and the eight lowest edge-energy frames. Both are hints.

Drop a candidate for exactly two reasons:

1. It carries **no new information** against the frame before it: a walk-cycle midpoint, a
   blink, a mouth shape.
2. It is a **blur or crossfade midpoint**, a frame that exists only between two states.

Never drop these, they are the material of the analysis:

- A progressive build step, even if only one icon changed.
- A zoom or reframe of the same composition.
- A held layout that gained a label, an arrow, or a character.
- A low edge-energy frame that is simply a flat title card. Those score low by nature.

Two of 357 candidates were dropped on the ancient-humans video. If your list is long,
suspect that you are throwing away build steps.

## Step 5 - Finalize

```bash
python3 tools/video-frames.py finalize --work "$W" --out "$R" \
  --drop 10,44 \
  --sections "1-30:Hook,31-46:Luan de,47-82:Ba cach mua giet nguoi"
```

It writes `extracted-frames/frame-NNN_MMmSS.SSs.jpg`, `frame-index.csv`, and
`contact-sheets/contact-sheet-NN.jpg`, then prints the contact-sheet table and the pacing
numbers ready to paste into the analysis. Frame numbering is continuous after the drops,
so the candidate ids in your notes are not the final frame numbers: `--drop 10,44` shifts
everything after them. Map through `frame-index.csv`, never by hand.

`--sections` takes the chapters you identified in Step 3, as final frame numbers. Re-run
the numbers any time without rebuilding:

```bash
python3 tools/video-frames.py stats --out "$R" --duration <seconds> --sections "..."
```

Two seconds-per-beat figures are printed. `mean gap between beats` ignores the tail after
the last beat, `duration / beats` counts it. Quote one and label it the same way the other
analyses do; do not mix them inside one document.

The tool prints its table headers in ASCII (`| Doan | Frame | Beat moi phut |`) because
`tools/` stays ASCII. Retype them with diacritics when you paste them in, and keep the
section names identical to the ones you pass to `--sections` so the two tables agree.

## Step 6 - Write visual-analysis.md

Language: **Vietnamese with diacritics.** Keep verbatim and untranslated: file names,
timestamps, on-screen text from the video ("THE ART.", "TRANSMISSION TIME."), craft terms
that have no settled Vietnamese equivalent (hook, beat, payoff, progressive build,
base plate, contact sheet, split card), and any quoted rule string. No em dash, ever.

Required sections, in this order:

1. `# Phân tích hình ảnh - <video title>` plus a line naming the channel, the view count
   if known, and the link.
2. `## Kết quả extract` - duration, resolution, fps, coded frame estimate, how many frames
   the study keeps, sheet count, the index file, the method, and **which candidates were
   dropped and why**, by timestamp.
3. `## Kết luận quan trọng nhất` - the one mechanism that explains the video. Not a list of
   nice frames. State it in the first two sentences, then support it.
4. `## Nhịp hình ảnh` - the pacing table from the tool, plus the per-section table.
   Interpret it: where does the video speed up, where does it slow down, and why.
5. A numbered block of mechanisms, one `###` each, in the order they first appear in the
   video. Every mechanism cites the frames that prove it.
6. `## Phân tích từng chương` - one table row per chapter: time range, frame range, what
   the images do, what it achieves.
7. `## Vì sao phần kết hiệu quả` - the ending deserves its own section, it is where
   shareability is won.
8. `## Những điểm không nên sao chép` - at least one item must be a fact you checked
   yourself, not a style opinion. Both existing analyses caught a real arithmetic or
   sourcing problem here. Also state plainly which parts of the render cannot be copied
   because `.agents/rules/visual-style.md` forbids them.
9. `## Cách áp dụng cho TossExplains` - concrete and inside the style lock: mode
   definitions, beat targets per section, and the techniques that survive flat colour.
10. `## Checklist review cho mỗi video TossExplains tiếp theo` - one line per checkable item.
11. `## Thứ tự xem bộ frame` - the contact-sheet table the tool printed.

Rules for the body:

- **Every claim about a frame links to that frame**, as
  `[frame 254](extracted-frames/frame-254_07m52.53s.jpg)`. A claim with no link is an
  opinion, and a link that does not resolve is worse.
- Quote on-screen text exactly as it appears, including capitals.
- Numbers come from the tool. Never round differently in two places.
- Name mechanisms in a way that transfers to a TossExplains scene prompt. "Chữ luôn nằm
  trên thẻ trắng" is usable; "bố cục đẹp" is not.
- Say what the video does badly too, with evidence.

## Step 7 - Self-check before reporting

```bash
cd "$R"
# every frame and sheet link resolves
grep -o '(\(extracted-frames\|contact-sheets\)/[^)]*)' visual-analysis.md | tr -d '()' \
  | sort -u | while read -r p; do [ -f "$p" ] || echo "MISSING $p"; done
grep -c "$(printf '\u2014')" visual-analysis.md   # em dash count, must be 0
ls extracted-frames | wc -l                          # must equal frame-index.csv rows - 1
wc -l frame-index.csv
ls contact-sheets | wc -l                            # must match the table in the doc
head -3 frame-index.csv; tail -1 frame-index.csv
```

A missing link is always a real error: the file name carries the timestamp, so a wrong
link means the frame number and the timestamp disagree and the citation points at nothing.

## Step 8 - Report and hand off

Give the verification verdict, the candidate count and how many were dropped with the
reason, the frame and sheet counts, the three or four findings that matter most for the
next TossExplains video, and anything the video gets wrong. Then:

> Swipe study saved to `research/videos-swipe/<slug>/`.
>
> Next: apply the findings when you run **`/scenes`**, and keep the render rules from
> `.agents/rules/visual-style.md` intact.

## Guardrails

- **Never download the video.** The user supplies the file.
- **Never extract before Step 0 passes.** An unverified pairing produces a study of the
  wrong video, and every frame citation in it is then a lie.
- **Never treat an unreachable YouTube as an offline run.** Exit 2 is a full stop: report it
  and run nothing else. Only the user may authorise `--offline`.
- **Never write the analysis from the 24-up contact sheets.** Read the review sheets.
- **Never let the tool choose the drops.** It flags, you decide, and you say why in the doc.
- **Never renumber or rename frames by hand.** `finalize` owns the numbering; hand edits
  break the timestamp encoded in every file name.
- Never put the working directory inside the repo. Candidates are scaffolding.
- Never commit the video file. `*.mp4` is gitignored on purpose. Frames are committed:
  around 150 KB each, so a 12 minute video adds roughly 50 MB. Say that number in the
  report so the user can object before it lands in git.
- Never copy the competitor's rendering into a TossExplains prompt. The four verbatim
  strings in `.agents/rules/visual-style.md` win over anything admired in a swipe video.
- Never claim a study is complete while any candidate went unviewed.

## Self-improvement

Read `.agents/skills/video-swipe/references/memory.md` at the start of every run. Append
when a channel needs a different scene threshold, when a downloader's file naming defeats
or helps verification, when a new mode vocabulary is needed for a different visual style,
or when a pacing target proves itself on a published TossExplains video.
