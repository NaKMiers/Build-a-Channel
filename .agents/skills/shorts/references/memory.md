# Shorts Skill Memory

Memory for the `shorts` skill - turning one finished Why It Works long video into 2-4 COMPLETE vertical shorts (1080x1920) and exporting each to MP4. Use this file for the toolchain, layout rules, and recurring fixes. Use `.agents/_shared/` only for channel-wide lessons.

## Current Skill Standard

- Side sub-workflow from `combine`; does not block caption/upload/learning.
- One project (named / smart-selected / asked); explicit short selection with `All` first.
- Modes: `plan` (menu -> `shorts/shorts-plan.md`), `build` (portrait comp on port `1100+N`), `export` (`output/shorts/*.mp4`).
- 2-4 shorts, ideally 3. One-at-a-time review like the section discipline.

## Locked layout rules (owner-confirmed 2026-06-22, first run = `why-cheap-products-keep-getting-worse`)

- Native portrait REBUILD (1080x1920), never crop/letterbox the 16:9 master.
- COMPLETE short, NOT a hook/teaser - **NO CTA / "watch the full video" / subscribe card**. End on the short's own payoff.
- Platform-safe zone `x[60..880] · y[220..1490]`. UI covers the edges: top title, right action rail, bottom caption + subscribe + progress bar. WIT body may bleed off edges; FACE stays inside. Verify with a temporary dashed `.safe-guide` overlay (+ a `.center-line` at `top:960`), then DELETE the guides before handoff.
- WIT big (≈1/3-1/2 frame), face ABOVE the centered caption; approved pose PNGs only; `transform-origin: center bottom`.
- Captions = distinct SUBTITLE style, NOT the cream label look: white text + dark text-stroke shadow on a translucent dark pill `rgba(16,12,9,0.5)`, `border-radius:22px`, centered vertically (`left:50%; top:50%; translate(-50%,-50%)`), font ~60px, max-width ~780-800, 2-4 words. Punchline/definition/payoff lines are carried by the cards/bubbles (the hero text), NOT duplicated in a caption; time captions to CLEAR before a card pops (e.g. cap end == card pop time) so nothing overlaps.
- Every scene = a real photo base (object-fit:cover) + top/bottom scrim. 16:9 -> 9:16 cover fills height fully and crops the sides to the center ~32%; center-framed subjects survive (tune `object-position` X only - vertical is a no-op under cover for a 16:9 source in a 9:16 box).
- Reuse the source section's real photos + WIT poses + font. Copy a MINIMAL working set into `assets/photos`, `assets/wit`, `assets/fonts` (Windows junctions fail on this HyperFrames setup).

## HyperFrames structure that passed lint (reuse this skeleton)

- root `#ShortNN` 1080x1920, `data-duration` = audio + ~1.0-1.5s payoff hold.
- 4 scene bases, each `class="clip scene"` on its OWN `data-track-index` (1/3/4/5) with a blur/opacity cross-fade `fromTo(..., immediateRender:false)` at its start.
- 4 cue overlays `class="clip cue"` sequential on `data-track-index="2"`; TRIM each cue duration by 0.01 so it ends before the next starts (float overlap = `overlapping_clips_same_track` hard error, e.g. `7.74+6.38=14.120000001`).
- captions in a static `.caption-layer` (inset:0, not a clip), children toggled by `tl.set(sel,{opacity},t)`.
- CAPTION GOTCHA (found `why-everyone-pretends` 2026-06-23): for the FIRST caption whose show time is `0.0`, setting `opacity:0` AND `opacity:1` at the SAME time `0` cancels out and that caption NEVER appears. Fix: clamp the show time, `const st = Math.max(s, 0.05)`, so show != hide-init. The opening caption is the hook line - verify it renders with a snapshot at ~1s, not just mid-clip frames. (Video-2 shorts shipped with this bug; re-export if you touch them.)
- one `<audio data-track-index="10">`; GSAP from jsdelivr; register `window.__timelines["ShortNN"]` synchronously.
- helpers: `show(sel,hideAt,at)` (hard-show) and `pop(sel,hideAt,at)` (scale-in for emphasis). Hide at cue start, show on the spoken word.
- Non-blocking warnings seen and accepted: `timeline_track_too_dense` (track 2), `overlapping_gsap_tweens` 0-0.2s, WCAG contrast on red labels over photos (false positives).

## Toolchain (this Windows box)

### Voiceover (regenerate per short)
- `hyperframes tts` needs **Python 3 + kokoro-onnx** - NOT preinstalled here. One-time setup (done 2026-06-22):
  - `scoop install python` (installed 3.14.6). `python` is shadowed by the Microsoft Store alias, so prepend the real dir to PATH: `export PATH="$HOME/scoop/apps/python/current:$HOME/scoop/apps/python/current/Scripts:$PATH"` (then `python` resolves correctly).
  - `python -m pip install kokoro-onnx soundfile` (kokoro-onnx 0.4.7 works on py3.14).
- Generate: `npx --yes hyperframes@0.6.76 tts <input.txt> --output <out.mp3> --voice am_eric --speed 0.84 --lang en-us --json` (run with the python-first PATH so HyperFrames finds real Python).

### Word timings
- whisper-tiny.en via `@xenova/transformers` over the short's own audio. Decode first: `<ffmpeg> -y -i short.mp3 -ar 16000 -ac 1 -f f32le out.raw`, then run `references/gen-word-timings.mjs <raw> <out.json>` from a folder that HAS `@xenova/transformers` installed (Node ESM resolves it from the SCRIPT folder, not cwd). The cached setup `%TEMP%/wiw-whisper/` already has the package + cached model; reuse it.
- TAIL GLITCH: whisper-tiny.en stamps the last few words non-monotonically / backwards at end-of-audio. Re-time the final caption line monotonically across the remaining window up to the audio duration. Always sanity-check the last 1-2 caption chunks.

### ffmpeg / Chrome (export)
- Static binaries: `%TEMP%/wiw-ffmpeg-static/node_modules/ffmpeg-static/ffmpeg.exe` and `.../ffprobe-static/bin/win32/x64/ffprobe.exe`. Install if missing: `npm.cmd install --prefix %TEMP%/wiw-ffmpeg-static --no-save ffmpeg-static ffprobe-static`. Put both dirs on PATH for the render.
- Export: from the short folder, `npx --yes hyperframes@0.6.76 render --output <abs .mp4>`. Chrome was already provisioned (HyperFrames manages it; use `hyperframes doctor`/`browser` if not). Renders ~30fps; frames = duration*30.
- Verify: `ffprobe -select_streams v:0 -show_entries stream=width,height,codec_name,r_frame_rate,duration` -> expect 1080x1920, h264, 30/1; audio aac.

## Server start (Windows, persistent)
`Start-Process -WindowStyle Hidden powershell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -Command \"Set-Location '<short dir>'; npx --yes hyperframes@0.6.76 preview --port 110N *> preview.log\""`, then verify HTTP 200 on `localhost:110N`.

## Verified Result (first run)

`why-cheap-products-keep-getting-worse` -> 3 shorts, all 1080x1920 / h264 / aac / 30fps, exported to `output/shorts/`:
- S01 The $9 chair (Section 1 + condensed Section 8) - 28.42s, 4.2 MB.
- S02 You own me, but not enough to open me (Section 6 trimmed) - 26.62s, 5.5 MB.
- S03 A subscription with extra steps (Section 7 re-ordered) - 21.42s, 7.0 MB.

## Beat-sync the short to the SOURCE section's signature device (owner-confirmed 2026-06-24)

- The owner wants each short to follow the long-form section's visual LOGIC, not just reuse its photos. If the source section pins a scene/device to a spoken word, the short must do the same: e.g. `why-buy-1-get-1` S1 shows the **magic-hat scene on the word "magic"** and **sprouts CSS bunny ears on the word "rabbit"** - the short must replicate both, synced to the short's own word timings.
- Port the source section's signature device verbatim (here the `.ear.left/.right` CSS bunny ears + `.witwrap`), don't invent a flatter substitute (a plain "YOU'RE THE RABBIT" card alone was rejected).
- Don't burn the payoff prop on the wrong beat: v1 opened on the magic hat for "sounds impossible," leaving nothing for "magic." Reserve each signature visual for the word it illustrates; pick a neutral context base (store/shelf) for the hook.
- "WIT emerges from the magic hat" came free from the standard portrait WIT geometry (centered, `bottom:360px`, width ~980) landing the figure right at a centered top-hat photo - a happy reuse; worth aiming for when the source has a hat/frame/doorway base.

## Gotcha: WIT face height is POSE-dependent - re-check caption-over-WIT per pose (2026-06-24)

Same `.wit` geometry (`bottom:360px`, `width:940px`) lands the head at very different heights depending on the pose PNG: `talking-front`, `confused`, `awkward-celebration` sit HIGH (face ~upper third), but `thinking` and `shocked` sit LOW (face ~mid-frame), so the centered caption (`top:50%`) clipped their chin/jaw - a face-coverage violation. Fix is a per-pose `bottom` override to lift the low poses (e.g. `#witThinking{bottom:540px} #witShocked{bottom:520px}`); body just bleeds further off the bottom edge, which is allowed. ALWAYS snapshot one caption-over-WIT beat for EACH pose used, not just one pose - don't assume a pose that worked elsewhere lands the same. (`why-buy-1-get-1` S03.)

## Per-pose WIT `bottom` reference + two card-overflow bugs (2026-06-24, `why-everything-is-a-subscription-now`, 4 shorts)

Measured per-pose face heights at `width:940px` (which need a raised `bottom` so the centered caption at `top:50%` clears the face). Poses that sit HIGH (face upper third, leave at default `bottom:360px`): `running-away`, `suspicious`, `hidden-fee-panic` (~430 still safer). Poses that sit LOW (raise `bottom`): `thinking` ~450, `confused` ~440, `shocked` ~420, `deadpan-side-eye` ~430, `tiny-defeated` ~430, `holding-receipt-evidence` ~400. Always snapshot a caption-over-WIT beat per pose to confirm.

Two recurring CARD bugs caught this run (both push a hero card past the right safe edge `x880` because cards center on the FRAME center 540, not the safe-zone center 470):
- Long stamp text (`NEGATIVE OPTION BILLING`, `FINANCIAL AWARENESS`) overflows - **stack to two lines** (`<br>`) or drop the font; verify with the safe guide.
- An inline-block badge inside a `white-space:nowrap` card (`.lock` "now: a monthly fee") renders BESIDE the line and blows the width out - set the badge `display:block; width:max-content; margin:.. auto` so it stacks centered. Same for statement rows: add `white-space:nowrap` so a long label ("The one you love") doesn't wrap ugly.

Result: 4 shorts all 1080x1920, 0 lint errors, built on ports 1101-1104. S01 Free-Trial-Countdown 32.6s · S02 Cancelling-Vision-Quest 28.7s · S03 Warm-Bottom 21.05s · S04 Product-Is-You 21.2s. `✓` (U+2713) DID render in snapshot Chromium (unlike emoji); barcode via `repeating-linear-gradient` works well for a "PRODUCT: YOU" tag.

## Verified Result (`why-the-internet-is-full-of-ai-slop`, 3 shorts, 2026-07-01)

3 shorts, all `1080x1920` / h264 / aac / 30fps, exported to `output/shorts/`:
- S01 Is-Any-Of-This-Real (Shrimp Jesus, source S1 hook) - 21.89s, 4.6 MB. Feed-of-fakes device: 3 absurd posts (shrimp / fake-news card / fake-band card) pinned to their spoken words, then grey-sludge GARBAGE payoff + "NOBODY TOLD IT TO." card.
- S02 Six-Fingers-Coca-Coola (source S3) - 19.52s, 4.2 MB. SLOP MACHINE intro + 3 tells (six-finger hand / gibberish sign / Coca-Coola ad) each with circle+redtag, CERTIFIED SLOP stamp payoff.
- S03 Arrest-An-Incentive (source S6) - 20.32s, 4.1 MB. Conspiracy corkboard named (DEAD INTERNET THEORY + tinfoil) -> punctured (big red X) -> empty villain throne -> glowing $ -> uncuffable-incentive coin payoff "YOU CANNOT ARREST AN INCENTIVE."

Lessons confirmed this run:
- Centered + GSAP-animated elements: `left:50%;transform:translateX(-50%)` survives `pop`/`smash` because GSAP parses the inline `translateX(-50%)` into `xPercent:-50` and animates `scale`/`y`/`rotation` separately - centering is preserved. Verified across all 3 shorts (posts, cards, bigwords, consp title). No need to switch to `left:0;right:0` for centered animated items.
- nowrap bigwords MUST be size-checked against the safe width (820px): "NOBODY IS IN CHARGE" / "it's dumber than that." overflowed at 92px; dropped to 66-74px. Rule of thumb in portrait: a full-width nowrap line caps ~14-16 chars at 100px, ~20 chars at 66px.
- AVOID a hand-label that repeats the caption verbatim (S03 scene-1 had both "not a secret plot..." label AND caption "This is not a secret plot." - dropped the label). Captions carry the spoken line; labels/cards carry DIFFERENT emphasis or the punch.
- Whisper tail glitch on the LAST word's END recurred on S02 ("slop." end 19.92 > audio 18.325) and S03 ("incentive." end 21.54 > audio 19.051); both START times were correct, so pin the final beat to the correct start and clamp root `data-duration` to audio + ~1.2s hold. S01 had clean monotonic timings (no glitch).
- Export PATH: add BOTH `%TEMP%/wiw-ffmpeg-static/node_modules/ffmpeg-static` and `.../ffprobe-static/bin/win32/x64` to PATH; `npx hyperframes render --output <abs.mp4>` renders ~30fps (frames = round(duration*30)), Chrome already provisioned. ffprobe duration ran ~+0.04s over root (trailing frame) - acceptable.
- `snapshot` CLI takes `[DIR]` positional (run from the short folder with `.`), NOT `--out`; it writes to `snapshots/` + a `contact-sheet.jpg` automatically.

## Verified Result (`why-countries-fight-to-host-the-world-cup`, 3 shorts, 2026-07-16) + Linux toolchain adaptation

Run done fully autonomously (owner "just do it yourself"). 3 shorts, all `1080x1920` / h264 / aac / 30fps, exported to `output/shorts/`:
- S01 It's-Not-An-Investment-It's-A-Ferrari (source S2) - 22.30s. INVESTMENT crossed out -> PURCHASE; red-supercar + PRESTIGE tag + boss WIT ("to be SEEN"); TAXPAYER gold card + BILLIONS; payoff `WHO PAYS?` card.
- S02 The-Only-Auction-Where-The-Winner-Pays (source S4) - 27.10s. gold-safe "FIFA KEEPS IT"; host-pays red chips over a construction crane; `$4,000,000,000` on a chessboard; payoff auctioneer + WIT-paddle + `WINNER PAYS / the auctioneer keeps it` card.
- S03 The-Stadium-Was-Full-Of-Buses (source S6) - 30.10s. dawn empty seats; white-elephant-stadium hero + MAINTENANCE bowl; `$550,000,000` + NO BIG CLUB; payoff bus-row + `FULL OF BUSES.` card.

Linux-box adaptations (this box is Linux, not the Windows box the rest of this memory assumes):
- **No pip/kokoro TTS and no whisper needed.** Slice each short's VO from the project's real recorded `hyperframes/full-video/combined-voiceover.mp3` at sentence boundaries using `voiceover/combined-segments.json` (absolute per-sentence start/end already aligned to the audio). Same approved voice, same words, EXACT caption timings for free (no tail-glitch re-timing). A node script slices contiguous ranges with `ffmpeg -ss/-to`, concats assembled shorts via the concat demuxer, and emits `voiceover/short-0N.mp3` + `short-0N-cues.json` (local caption times). Reuse `scratchpad/build-short-audio.mjs` pattern (ranges = combined-segment index spans).
- **ffmpeg install on a flaky network:** `ffmpeg-static` fails here (its binary is a GitHub postinstall download that times out; a failed npm install also ROLLS BACK the whole node_modules, wiping siblings). Use `@ffmpeg-installer/ffmpeg` (binary ships INSIDE the npm tarball) + `ffprobe-static`, `npm install --save` them into one dir so `--no-save` prunes can't remove them, and symlink both into a `bin/` on PATH. Chrome = system `/usr/bin/google-chrome` (auto-detected; screenshot capture path, ~1min/short).
- **Render audio mux fails in this env -> mux post-render.** `hyperframes render` produced VIDEO-ONLY MP4s (the render-time comp server does not proxy the `voiceover/` path, so `<audio src="./voiceover/..">` 404s during capture, even though it serves 200 in plain preview). Fix: after render, `ffmpeg -i video.mp4 -i short-0N.mp3 -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -b:a 192k out.mp4` (NO `-shortest`, so the payoff-hold tail past the VO stays). Verify with ffprobe (2 streams: h264 + aac) and `volumedetect` (non-silent). Consider first trying the mp3 under `assets/` (a configured path) with `src="./assets/short-0N.mp3"` for a native mux next time.
- Preview-local `assets` symlink works on this box, but for RENDER copy a minimal real working set into `assets/` (photos + used poses + `fonts/`) - proven safest for render bundling.
- Short covers for packaging: snapshot each payoff beat and copy the frame to `output/thumbnails/short-0N.png` (real 1080x1920, reuses the exact built payoff).

Layout lessons reconfirmed: dark-on-tag/sign text and gold `.bigword` with a 4px black stroke trip WCAG contrast warnings that are FALSE POSITIVES (validator ignores stroke/shadow). Reusing one base photo in two scenes (bookend) trips a benign `duplicate_media_discovery_risk` lint warn. Watch label-vs-caption VERBATIM duplication (caught + fixed "one side gets the bills" and "legally? a chess club." repeating their captions) - let the caption carry the spoken line and the card/label carry a DIFFERENT beat.

## Gotcha: don't zero a `.wit` that lives inside an opacity-controlled wrap (2026-06-24)

`gsap.set('.wit', {opacity:0})` as a blanket initial-hide ALSO hides the `<img class="wit">` nested inside a `.witwrap` whose visibility you control via the WRAP's opacity. Result: the wrap shows but the figure stays invisible (only ears/cards render). Fix: hide the standalone WITs by id and the wrap by id (`#witSuspicion,#witShocked,#witBetrayedWrap,.ears`), and let `.witwrap .wit{opacity:1}` stay. Always snapshot a scene that uses the wrap to confirm the body renders, not just the ears.

## Feedback Log

### 2026-06-22 - Skill created from the first verified shorts run

Classification: `Operational lesson`

Context:
Anh Khoa asked to split the main video into 3 vertical shorts as a sub-workflow, build natively in HyperFrames, review per short, then export. During the run he corrected four things that are now LOCKED rules: (1) WIT must be much bigger; (2) keep content out of the platform-UI edge zones (added the safe zone); (3) captions must sit at the vertical center AND look distinct from the in-video labels (white-on-dark subtitle), never covering WIT/labels/cards; (4) each short must be a COMPLETE short, not a hook - remove the "full video" CTA. He chose native portrait rebuild + regenerated VO + one-off-then-skillify.

Lesson:
Shorts are first-class. Rebuild vertically (don't crop), reuse the section's real assets + voice, regenerate clean per-short VO, caption from real timings, keep everything in the safe zone with a big WIT and centered distinct subtitles, and end on the payoff with NO CTA.

Promote to shared memory:
The safe-zone + "no CTA / complete short" + "WIT big & high" + "real photo base every scene" rules are already channel-wide visual rules; this skill's memory holds the shorts-specific execution recipe.
