# video-swipe - memory

Self-improving notes for the swipe-file frame study. Single canonical copy.

## Environment on this machine

- **There is no ffmpeg or ffprobe on PATH**, and no numpy, cv2, av, or imageio in Python.
  Pillow 10.2 is present. `python3 tools/video-frames.py ensure-ffmpeg` fetches a static
  build through `pip download imageio-ffmpeg` and unpacks it to
  `~/.cache/tossexplains-ffmpeg`. Export `FFMPEG=<path>` for the rest of the session.
- **Outbound HTTP works, but it has been intermittent.** On 2026-07-31 `curl` and `urllib`
  to youtube.com and pypi.org timed out from Bash while `pip download` succeeded; a retest
  the same day got youtube.com in 0.2s. `youtube-verify.py` therefore uses an 8 second
  timeout, and **an unreachable lookup is a hard ERROR, not a fallback**: the owner asked
  for a stop rather than a quietly weaker run. `--offline` is the opt-in for file-name-only
  verification and only the user may ask for it.
- **oEmbed answers, the watch page does not.**
  `https://www.youtube.com/oembed?url=...&format=json` returns title, `author_name`, and
  the thumbnail URL with no key and no bot check, and answers 404 or 400 for an id that is
  not a public video. The watch page still contains `ytInitialPlayerResponse`, but from
  this address its `playabilityStatus` is `LOGIN_REQUIRED / "Sign in to confirm you are
  not a bot"`, so **`lengthSeconds` and `viewCount` are not obtainable by script.** Do not
  add an Innertube or alternate-client workaround for that; the duration comes from a real
  browser session through `/browse` and reaches the tool as `--expect-duration`.
- The Playwright ffmpeg under `~/.cache/ms-playwright/` is a trimmed build. Do not use it;
  `find_ffmpeg` deliberately ignores it.

## Known-good settings

- Scene threshold **0.02** is right for flat doodle explainers. It produced 357 candidates
  for an 11:36 video (30.8 per minute) and 187 for a 6:18 video (29.7 per minute). Both
  counts survived review almost intact, which is the sign the threshold is not too low.
- **0.02 is wrong for a video with karaoke word-by-word subtitles.** See the next section.
  `how-did-ancient-humans-sleep-through-endless-rain` was run at **0.06**, but see the conflict
  note there: for **Before Civilization** the settled default is **0.02 plus hand-drops**.
- Runtime: about **1 minute of extraction per 12 minutes of video**, plus a few seconds for
  the sheets. 355 frames at 1920x1072 weigh 56 MB.
- Review sheets at **2 x 3, 776 px cells** are the smallest layout where on-screen captions
  stay readable after the API downscale. 4 x 6 was tried for reading and failed.

## Regression fixture

`research/videos-swipe/what-did-ancient-humans-do-when-it-rained-all-week/` is the fixture
for the tool. Re-running the pipeline on its video reproduces all 355 frames, all 15 contact
sheets, and `frame-index.csv` **byte for byte**:

```bash
python3 tools/video-frames.py candidates "<that mp4>" --work "$W"
python3 tools/video-frames.py finalize --work "$W" --out /tmp/check --drop 10,44
diff <(cd /tmp/check/extracted-frames && md5sum * | sort -k2) \
     <(cd research/videos-swipe/what-did-ancient-humans-do-when-it-rained-all-week/extracted-frames && md5sum * | sort -k2)
```

Any change to `DIFF_SIZE`, the contact sheet constants, the JPEG quality, or the ffmpeg
filter chain breaks that equality. If a change is intentional, say so and re-verify.

## Lessons paid for

- **Write frame notes to disk after every batch of sheets.** In the first run, thirty
  review sheets were read and then lost to context summarization, and had to be read again.
  Notes in the working directory survive; images in context do not.
- **Candidate ids are not final frame numbers.** Dropping c010 and c044 shifted everything
  after them, and two frame citations in the first draft pointed at the wrong image. The
  file name carries the timestamp, so a wrong link fails the link check instead of pointing
  at a plausible wrong frame. Map through `frame-index.csv`.
- The mean-difference shortlist at 12.0 caught both real duplicates on the ancient-humans
  video (c010 at 8.22 and c044 at 2.58) inside a list of 17. Every other flagged frame was a
  genuine progressive build and was kept.
- Low edge energy does **not** mean blur in this genre. The eight lowest scores on the
  ancient-humans video were all clean flat cards: a fire icon on white, narrator cut-ins, a
  lamp-lit near-black cave.
- Two seconds-per-beat conventions exist in the older analyses. `the-rarest-human-possible`
  quotes 2.09, which is duration divided by beats; the mean gap is 2.05. The tool prints
  both, labelled. Pick one per document.

## Verification behaviour worth remembering

- The id-in-file-name gate carried every real case so far, because the downloader the owner
  uses writes names like
  `What-Did-Ancient-Humans-Do-When-It-Raine_Media_SD7XyG2wd1k_001_1080p.mp4`. Title
  matching is the fallback for files that lost the id.
- Detecting "a different id in the name" needs a position-by-position scan, not one regex.
  A regex that consumes its delimiters matched `_Media_` first and hid the real id that
  followed it. Title words also reach 11 characters (`Did-Ancient`), so an id-shaped token
  only counts when it carries a digit plus both letter cases.
- `title_conflict` is deliberately INCONCLUSIVE rather than MISMATCH. A renamed file and a
  localized YouTube title both trigger it innocently, and both paths stop and ask anyway.

## Other things worth knowing about this tool

- With **more than 99 review sheets** the file names mix widths (`sheet-01` .. `sheet-99`,
  then `sheet-100` .. `sheet-163`), so plain `ls` sorts them wrong. Use `ls | sort -V`.
- The downloader truncates long titles. `How-Did-Ancient-Humans-Sleep-Through-End_...` gave a
  folder named `...-sleep-through-end` while the real oEmbed slug is
  `...-sleep-through-endless-rain`. **Always take the slug from `facts`, even when the user has
  already created the folder**, and rename it.
- Source files can carry render defects. Frame 25 of this study has a solid black 170x160 pixel
  rectangle over the picture, straight from the downloaded file. Worth reporting, not worth
  dropping the frame over.

## Mode vocabulary is per channel, not universal

The FULL / WHITE / NARR / SPLIT vocabulary came from Ink Explainer, which puts every caption
on a white card. **Past Tense has no white frame at all**: all 272 frames of
`why-humans-eat-3-meals-a-day` sit on a warm tinted ground (cream, amber, yellow, terracotta,
tan), so `WHITE` had to be replaced by `CARD`, meaning a flat tinted card carrying type, a
number, icons, or a labelled diagram. Two extra registers were needed there too, `MAP` and
`SEQ` for the timeline pans. Decide the vocabulary from the sheets, do not inherit it.

## Burned-in karaoke subtitles break the default threshold

`how-did-ancient-humans-sleep-through-endless-rain` (Before Civilization, 26:19) burns a
**one-word-at-a-time red caption with a white glow** into the picture, synced to the narration.
At 0.02 the detector fires **once per spoken word**: 973 candidates, 37.0 per minute, 290 of 972
gaps under 0.11s, and one held shot shredded into **24 candidates inside 1.00 second**. The
resulting "beats per minute" would measure speech rate, not visual rhythm.

Diagnose it from the gap histogram before looking at a single image: a large sub-0.11s population
combined with *high* diffs means animation or captions, not a duplicate-frame problem. Then
compare thresholds on the real file and show the owner the table. Measured here:

| Threshold | Candidates | /min | sub-0.11s gaps | mean gap |
| --- | ---: | ---: | ---: | ---: |
| 0.02 | 973 | 37.0 | 290 (29.8%) | 1.62s |
| 0.06 | 433 | 16.4 | 50 (11.6%) | 3.64s |
| 0.12 | 366 | 13.9 | 24 (6.6%) | 4.31s |

**0.06 was chosen and approved by the owner** on that evidence, and the resulting 349-frame study
is internally consistent and verified. Raising the threshold is the owner's call, like `--offline`
is; show the numbers and ask.

### But read the next section before repeating this

**This decision conflicts with the sibling study of the same channel**, and the sibling method is
probably the better one. `why-ancient-humans-couldn-t-afford-to-lose-their-grandparents` kept
**0.02 and hand-dropped 524 of 1252 in five named classes**, on the explicit finding that no
threshold separates a real caption state from an animation duplicate on this channel. That run is
right that raising the threshold **discards most caption-word states**: the 0.06 study kept only
45 captioned frames out of the several hundred the film contains.

The two studies therefore measure different units and **must not be compared**:

| Study | Threshold | Kept | Unit it actually measures |
| --- | --- | ---: | --- |
| `...-lose-their-grandparents` | 0.02 + 524 hand-drops | 728 | caption states, one per settled word |
| `...-sleep-through-endless-rain` | 0.06 | 349 | plates and shots, captions sampled |

Its "13.3 beats per minute" is a **plate rate**, not the caption rate, and not comparable to the
sibling's 28.5. Say which unit you measured, in the analysis, every time.

**Default for Before Civilization from now on: keep 0.02 and hand-drop by the five classes.**
Reach for `--threshold` on this channel only if the owner prefers a cheaper plate-level study and
you label it as such.

## Dimness is not emptiness. Do not drop a dark frame on a statistic.

The worst near-miss of this run. A filter of "grayscale stddev < 14" flagged **89** frames as
near-uniform. On inspection **most were complete compositions** sitting at the bottom of a
fade-in from black: fully drawn, just dark. Dropping them would have deleted 25-plus real shots.

The correct test is **structure, not brightness**: crop out the watermark, run
`ImageOps.autocontrast`, then measure stddev. On this video that split cleanly into exactly
**60 frames at 0.0** (true pure black or pure white) and everything else at **25 or above**,
median 61.6. A clean binary gap, no judgement needed. Brighten a dark frame 4x and look at it
before dropping it.

Also: a video can fade through **white** as well as black. The 24 pure-white frames here all
reported the identical `sharp` value (3.43) because the only remaining variance was the corner
watermark. An identical sharpness across many frames is a signature worth grepping for.

## Frames whose only content is the caption are keeps, not crossfade midpoints

When the illustration has fully dissolved but the caption word is opaque and legible, the
information the frame carries is complete, so it is not a "between two states" frame. Kept 6 of
these (`does`, `second`, `And`, `is`) as the exemplars of the mechanism. But a *second* frame of
the same word on the same emptying ground 0.03s later is a duplicate: keep one, drop the rest.

Conversely, **a caption leaving is a real state change** when the film then holds the clean shot.
Nearly dropped a frame at 20:58.17 as a 0.04s duplicate; it was the same shot with the caption
gone, held afterward for 6.3 seconds.

## Renumber once, and re-audit every citation after a second drop pass

This run needed a second drop pass (10 more frames) after the review sheets revealed residual
animation bursts. That shifted every frame number after the first new drop, and **two citations
in the finished draft silently pointed at the wrong frame** while still resolving as valid links,
because the note-time f-numbers came from the first numbering.

The link check alone does not catch this. Audit by mapping each cited frame number back to its
**candidate id** and diffing against the note for that candidate:

```python
new = {}; n = 0
for c in candidates:            # in order
    if c["id"] in drops: continue
    n += 1; new[n] = c["id"]    # final frame number -> candidate id
```

Better: collect the whole drop list from the review pass first and finalize exactly once.

## A one-frame gap means the detector fired twice

On the 3-meals video, candidates 08:17.37 and 08:17.40 were **0.03s apart, one frame at
30 fps**, and were the same timeline asset shifted a few pixels. That is a scene-detect
double-fire on a single cut, and it is a certain drop. Check the gap column for anything
under about 0.1s before looking at the images. That plus one title-mid-exit frame were the
only two drops out of 274, matching the 2-of-357 ratio on the earlier video.

## A title leaving the frame is not a build step

A frame where a caption has already gone and the layout has panned slightly, with nothing
added, is a between-states frame and drops under reason 2. A frame where a caption *arrives*
is always a keep. The distinction matters because both score low on the diff shortlist.

## Findings worth reusing across videos

- All three studied videos alternate a small set of visual registers rather than drawing more
  detail. The ancient-humans video changes register every 2.6 beats on average, the 3-meals
  video every 2.26.
- The first two keep text off the story frames and push it onto separate cards. **Past Tense
  does the opposite and still works**, by restricting caption colour instead of caption
  location: black for neutral labels, outlined red for every verdict and negation, outlined
  white only over a deliberately defocused plate. TossExplains already has this colour rule,
  so the transferable habit is the colour discipline, not the white card.
- The strongest single mechanism found so far is **base plate plus progressive build, then a
  large red word laid over the finished image**. The 3-meals video runs eight build chains and
  seven text-over-image payoffs in 8:25, and its hook spends four of its twelve beats on one
  such chain.
- Pacing shape differs by channel and both shapes work. Ink Explainer accelerates into
  emotional payoffs. Past Tense front-loads instead: 65.8 beats per minute in the hook,
  falling monotonically to 24.9 in its slowest chapter. Its densest-text frames sit inside its
  slowest chapter, which yields a usable rule: hold longer on frames that carry reading.
- Reuse is cheaper than anyone assumes. About 15 of 272 frames in the 3-meals video are
  verbatim repeats, including a five-shot recap before the ending and a closing pair that
  restates the two opening frames exactly.
- One dark frame in a whole video is worth more than a dark palette. The 3-meals video goes
  near-black exactly once, for its `BREAK the FAST` etymology reveal, and that produced the
  largest frame-to-frame difference in the entire film (123.8).

## An animated channel breaks the threshold assumption, and raising it is the wrong fix

`why-ancient-humans-couldn-t-afford-to-lose-their-grandparents` (Before Civilization, 25:31)
produced **1252 candidates, 49 per minute** against the 30 per minute that flat-cut doodle
channels give. The cause is that the video animates continuously: 446 of 1251 gaps are under
0.10s, and 747 candidates sit inside 273 bursts of near-adjacent frames.

**Do not reach for `--threshold` here.** The real caption words `DO` and `LIVE` at 05:11 score
diff 4.05 and 5.55, the same band as the icon-rotation duplicates at 1.79 to 6.46. No
threshold separates them, so raising it deletes the channel's defining mechanism. Keep 0.02
and drop by hand. 524 of 1252 dropped, in five named classes:

| Class | n | What it is |
| --- | ---: | --- |
| D3 | 232 | camera-drift duplicate, same caption and same content as the kept frame before it |
| D5 | 131 | caption scale animation: the word enters small, overshoots large, then settles |
| D1 | 119 | the pure-black frame of a fade plus its fade-up midpoint, about 40 fades in 25 min |
| D2 | 25 | the midpoints of one 1.2s dust wipe at 04:10.13 to 04:11.30 |
| D4 | 17 | a rotating pixel-hourglass overlay, nothing else changed |

**Name the drop classes in the analysis and give each a count.** 524 drops needs an audit
trail; "two of 357" did not.

### The caption pulse is a three-state animation

Each word enters small, overshoots larger than final, then settles. Keep the settled state.
This alone is why one word yields 5 to 8 candidates, and it is the single biggest source of
duplicates on any channel that animates its captions. Check for the small-large-settle triple
before assuming a burst is a progressive build.

### Skill text to reconcile

`SKILL.md` Step 4 says never drop "a zoom or reframe of the same composition". That rule was
written for discrete zoom cuts. On a continuously animated video every candidate inside a held
shot is a zoom step, so the rule as written would keep hundreds of animation frames. The
governing test is still reason 1, no new information: a drift step carrying the same caption
and the same content is a drop. A deliberate reframe still reads as a large diff and is kept.
State the rule you applied in the analysis, as this run did.

### Expect the mode vocabulary to be wrong again

Third channel, third vocabulary. Before Civilization has **no white or tinted card at all**,
every frame is a painted environment, so `WHITE` and Past Tense's `CARD` both fail. What
worked: STORY 57.1, CLOSE 8.5, CAVE 8.0, MODERN 6.6, FIRE 6.5, OBJ 5.2, LAND 4.4, GROUP 2.1,
ANIMAL 1.6 percent.

When tagging modes in the notes file, **put the mode in its own column and never write a
caption-scale word there**. The first census came back with `LARGE` and `LARGEST` as modes
because the note format let a scale word land in the mode position.

## The register-switch rate is the same on all three channels

Ink Explainer changes register every 2.6 beats, Past Tense every 2.26, Before Civilization
every 2.23 (326 switches over 728 frames). Three completely different art styles, one
frequency. This is the most transferable number the three studies have produced: **change
register every 2 to 2.5 beats regardless of render style.**

## Pacing shape, a third pattern

Ink Explainer accelerates into payoffs. Past Tense front-loads and falls monotonically.
Before Civilization is a **U**: hook 62.5 beats per minute, trough 21.0 in the metaphor
chapter, ending back up at 55.6. The slow trough is the chapter that asks the viewer to
connect an analogy themselves.

Also: on a channel that holds a still plate and swaps words over it, **beats per minute
measures caption speed, not drawing speed.** Its fastest mid-video chapter (38.4) is fast
because 30 candidates sit on one unchanging ice plate.

## The base plate carries whole sentences, so the art bill is far below the beat count

The strongest mechanism found across all studies so far. One still plate holds a 7 to 11 word
sentence while the words change: 25 candidates and 9 caption states on one beach plate whose
storyteller's raised arms never move; a whole sentence on a single macro of a healed femur.
728 beats came from roughly 320 plates. This is how one person ships a dense 25 minute video.

Two builds can also run at once on one plate: at 19:35 a red X draws on stroke by stroke
while the caption advances word by word, and the X completes on the negation.

## Verify a hand-typed timestamp in every citation

Three of 89 frame citations in the first draft pointed at a correct frame number with a
hand-typed wrong timestamp, and one had the wrong number entirely. The file-name link check
catches all of them, so **run it and fix before reporting**, and prefer generating citations
from `frame-index.csv` over typing them. Worth adding to the self-check: parse every
`[frame N](extracted-frames/...)` and assert the file matches row N of the index.

## Reporting scale before spending the run

At 728 kept frames this study is 170 MB, three times the largest previous one, and reading
209 review sheets is a long run. Both were put to the owner before extraction, with the
threshold analysis that ruled out the cheap fix, and the owner chose the full study. Do that
rather than silently narrowing: the guardrail's "say the number so the user can object" is
worth raising *before* the sheets are read, not only in the final report.

## Findings from this video worth reusing

- **Frames with no human subject are punctuation.** 82 of 728, 11.3 percent, and they land on
  every transition: a cold fire ring, a faded painted wall, an empty salt pan, a field of
  wrecked boat frames. The ending's central negation sits on one of them.
- **The ending goes from the widest frame to the tightest**, empty ice field to two hands
  passing a bone, in 7 seconds, and the largest word in the film lands there.
- **Close the loop by changing exactly one variable.** Opens on one person alone with a phone
  in a dark room, closes on the same composition with a child added.
- **Time periods can be separated by one mark.** Modern figures are bald; ancient figures have
  hair. 48 modern frames against 680 ancient, and the video jumps eras with no transition.
- **A macro insert is always hands or an object, never a face.** That is how it adds a beat
  without adding a character.

## What this video gets wrong, all checkable in the frames

Useful as a template for the "khong nen sao chep" section, which must contain at least one
fact checked in the frames rather than a style opinion. Five were found here:

1. **A number the art contradicts.** Frame 599 captions `1.8 MILLION` over a figure holding a
   **hafted** stone axe with **woolly mammoths** on an acacia savanna, and dresses him exactly
   like the 30,000-years-ago characters. Hafting and woolly mammoths are both far too recent.
   The lesson for us: if a number goes on a frame, the frame has to survive the number.
2. **No researcher, site, or date on screen in 25 minutes**, despite 14 scientist frames with
   clipboards and a flagged excavation trench. It also splices a 30,000-year Upper Palaeolithic
   finding and a 1.8 Ma cranium into one continuous argument with nothing on screen marking
   them as different claims.
3. **Three lowercase thought bubbles** in a plain UI font (`Muscle vs map`, `Fact`,
   `Running out of time`) against an otherwise uniform bold ALL CAPS outlined caption system.
   They read as editing notes left in the final cut.
4. **Systematic faceless heads.** Background figures render as blank cream ovals with no eyes
   or mouth, worst in the crowd frames the video most wants for "the whole community": about
   14 of 18 figures in one closing fire circle.
5. **A flat pink vector map-pin** dropped onto a painted Milky Way scene, held 8.30 seconds,
   the second-longest hold in the film.
