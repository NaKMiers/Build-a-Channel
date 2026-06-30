# Learning Log

Reusable lessons for `Why It Works`.

Keep this short. Current rules belong in `current-state.md`, `production-workflow.md`, `brand-system.md`, or the compact `systems/` docs. One-video details belong in `projects/<slug>/`.

## Core Decisions

- English learners are the main audience lens, but the channel is still an explainer channel, not an English class.
- Working rule: `Teach the topic first. Make the English learner-friendly by design.`
- Handwritten-looking labels, captions, arrows, red corrections, and punchline text are part of the default visual language.
- Animated interactive UI mockups (a screen that performs the action: SVG cursor clicks, buttons boing + flip state, counters tick, confetti/toasts pop, all word-timed) are a confirmed go-to device for CTAs and any "tap/click/toggle/subscribe" beat (owner-confirmed 2026-06-30, after the S8 subscribe-popup outro). Parody UI + our own branding, no fake metrics, CSS/SVG not emoji. See `systems/visual-production.md` (Animated Interactive UI Mockup). Pairs with the Real-UI Illustration preference.
- Topic selection should use angle thinking: `topic + contradiction + visual metaphor + viewer pain`.
- Publishing learning rule: `Measure the upload. Learn one useful thing. Change the next video.`

## Current Operational Decisions

- `.agents/_shared/` is now intentionally compact: use `channel/production-workflow.md`, `channel/brand-system.md`, and the four docs in `systems/` as the shared production brain.
- Main pipeline order is `topic-intake -> research-pack -> script-draft -> voiceover -> visual-plan -> visual-implement -> render -> review -> combine -> caption -> packaging -> upload -> learning`.
- Packaging (as of 2026-06-26) runs after `caption`, requires `00-topic-intake.md` + `01-research-pack.md` + `02-script.md`, and writes `output/packaging.md` (+ `output/thumbnails/`); it is no longer the numbered `03-packaging.md`.
- New-project file numbering shifted up by one (voiceover `03` … self-learning `08`); existing projects keep old numbers and skills resolve step files by name suffix (`.agents/rules/video-workflow.md`).
- After voiceover, production branches by section. `visual-plan` requires the selected section voiceover and creates section-level plans before render.
- `render` uses one HyperFrames preview project and one localhost per section. Unified/final preview is reserved for `localhost:1000`; section `N` uses `localhost:1000 + N`.
- Current WIT source is the pose-transferred set in `.agents/_shared/assets/wit/poses/` (catalog `pose.md`; `_origin_.png` = neutral identity). As of 2026-06-28 the `67` poses are TRANSPARENT RGBA cutouts (chroma-keyed in place + committed) - use directly, no keying step, no `poses-keyed` folder (green originals in git history). Replaced the old `wit-pose-*` 24-set on 2026-06-28.
- Do not use the removed older WIT directions as current channel WIT.
- Default final narrator is `David23 / am_eric / 0.84 / en-us`; test `am_eric` directly before declaring it unavailable.
- `Experiment` tooling (2026-06-28): Kokoro (HyperFrames `tts`) has NO Vietnamese voice. For Vietnamese-language experiment videos (e.g. `5-vi-sao-gia-vang-tang`), use **edge-tts** (Microsoft Edge TTS, free, no key, needs internet): `python -m edge_tts --voice vi-VN-NamMinhNeural` (young male, the VN equivalent of David23) or `vi-VN-HoaiMyNeural` (female); `--rate=-8%` to slow for clarity. This does NOT change the default English `David23 / am_eric` voice; it is the VN-experiment path only.

## Experiments

- `Experiment` (owner-requested 2026-06-23, `why-everything-is-a-subscription-now`): denser, trend-aware
  humor. Owner said "I love joking in the video" and asked for dad jokes, currently-trending internet
  joke/meme formats, and harmless dark jokes (self-aimed/absurd, never targeting a person or group).
  Hypothesis: higher joke density (~every 15-25s) + a recognized meme format adapted as a running gag
  (e.g. "your free trial of ___ has expired") raises retention/shares without hurting learner clarity.
  Guardrails: every trending/slang line needs an on-screen visual + a one-line learner gloss (the
  channel bans native-only-knowledge jokes); jokes must still support clarity. Concrete device/object
  motifs (phone, laptop, monitor, car screen) preferred over abstract symbols. NOT a voice/tone
  foundation change - validate against real retention before promoting to `channel-foundation.md`.
- `Core` positioning (owner-stated 2026-06-28): the channel's competitive advantage vs other English-learning channels is that it is **entertaining first** - viewers come for a genuinely funny, slightly-rude "Why does X work?" explainer, and the English learning rides along. Entertainment creates the motivation to keep watching/learning. Audience is A2–C1 English learners. Working frame: an interesting, lightly-savage explainer that happens to teach English, NOT an English lesson that tries to be fun. Protect this advantage in every script, visual, and packaging decision.
- `Core` tone (owner-confirmed 2026-06-28, overrides the earlier "learner-clean / not slang-heavy" caution): edginess is APPROVED and wanted - profanity (shit, damn, dumb, stupid, etc.), savage takes, and comedic mockery of public figures are allowed because viewers find it real and engaging. "Mấp mé vạch nguy hiểm" is the deliberate style. Execution guardrails (so edge ≠ self-sabotage):
  - **Monetization-safe profanity placement:** moderate words (dumb/stupid/damn/hell/shit) fine in the body; keep the STRONGEST words (f-word, anything harsher) OUT of the first 7 seconds, the title, and the thumbnail; never use slurs (race/gender/etc.) - that's the only true red line.
  - **Edge as a learning feature:** occasionally gloss spicy register on screen ("'this is BS' = casual/rude - don't say it to your boss"). Teaching the real spoken/rude register textbooks avoid is a competitive advantage, not a risk.
  - **Public-figure mockery is OK, but:** (1) use transformative memes / a mascot caricature, NOT the raw copyrighted photo/clip (avoids copyright claims); (2) keep it OBVIOUS parody, never "false-as-fact" (avoids defamation); (3) punch UP (powerful people/companies), not down.
  - **Audience-fit:** any recognizable figure must be GLOBAL (Trump, Musk, MrBeast, big brands). VN figures (MCK, Độ Mixi) are off-limits as references - global English learners don't know them.
  - Risk classes: creative edge (taboo topics, savage system-takes, absurd exaggeration) = encouraged; legal/platform own-goals (slurs, raw copyrighted media, false-as-fact, f-word in first 7s/title/thumbnail) = avoid. Maximum attitude, minimum own-goal.

## Production Lessons

- For `20-30s` hooks, start with `6-8` simple static boards before adding motion.
- One board should usually carry one thought, one readable label, and one clear joke or evidence job.
- Use hard cuts by default; add motion only when it improves clarity, timing, or the joke.
- Sequential cue timing does not require animating every block. Ordinary labels should hard-show on the spoken beat; reserve smash/pop/stamp motion for emphasized words, proof marks, and payoff phrases.
- WIT is the emotional subject when it appears. Use large, goofy, readable poses for emotional beats and verify face/head/shoulder crop with runtime screenshots or contact sheets.
- Text/WIT collision must be checked both ways. WIT should not cover labels or proof, and payoff text/stamps/cards should not cover WIT's face or expression when WIT is carrying the emotion.
- Do not overuse WIT. For short sections, start with about `1-2` WIT beats per persistent big scene and let labels, props, and markup carry explanatory cues between WIT moments.
- During section-by-section HyperFrames production, preview one section per project/port and assemble only after approval.
- If the user manually edits a HyperFrames Studio/localhost preview, preserve the current section `index.html` as canonical. Future updates must read and diff that file first, never overwrite it from an older review mirror or visual plan, and remove only targeted accidental artifacts.
- Voice sync comes first: board changes, labels, underlines, and emphasis should land on the spoken cue.
- Cue-critical visuals must be readable on the cue frame, not merely beginning animation there.
- Visual references should start from real internet, self-shot, or local images when the topic has real-world objects. Generated images are support, cleanup, or controlled mockups after real texture is understood.
- Keep only one useful audio preview per voice test unless the user asks for variants.
- Prototype `45-60s` before building a full rough cut when testing a new visual language.
- `Core` (owner-confirmed 2026-06-22, `why-everyone-pretends-to-be-busy` S5–S7): EVERY scene needs a real, people-free photo background - including real-UI scenes (chat/Meet/Trello/spreadsheet/calendar) and stylized CSS constructs (shield/stage). Float the UI as a drop-shadowed `.screen` on a real desk; back a CSS construct with a real photo. All-CSS-on-flat-gradient reads as "not lively / no background" and gets rejected. Prefer a base that echoes the line; hands-at-keyboard photos are fine (no-face allows hands).
- `Core` (owner-confirmed 2026-06-22): WIT default is BIG and HIGH - roughly `1/3`–`1/2` of the frame, anchored so head+glasses+torso+arms are inside the frame (only legs cropped), not a low bottom-edge peek showing just the head. When a big WIT would cover a label/board/UI, RE-ARRANGE the other items (opposite side / top / bottom); never shrink or lower WIT to fit. Design label/UI positions around a big, high WIT from the start.
- Operational: generate the section `section-XX-word-timings.json` from the audio (whisper) before timing cues; inspect the tail for both duplication AND backward-jump (chunk-boundary) glitches and re-time monotonically before pinning cues.
- `Core` (owner-confirmed 2026-06-28, from Threads-City reference teardown in `analysis/`): illustrate **per SENTENCE / per spoken beat, NOT per section.** The current Why It Works videos hold one composition per section (slideshow fatigue, scored 3/10 for variety). The reference changes the visual on almost every sentence - a new screenshot, a new mascot pose, or a clean focus frame - so the eye never habituates. Target cadence: a visual change every few seconds, synced to the spoken line ("show-as-you-say": the illustration lands exactly on the words). This RAISES asset count per video, so make it sustainable via a reusable mascot-pose library + scene-type templates rather than bespoke art each time.
- `Core` (owner-confirmed 2026-06-28): the mascot must be a **real character with color + personality**, not a featureless blob. Reference host = pink hair, outfit, expressive face, cheeky/"láo cá" attitude. WIT as a plain white blob is a primary reason the watch experience scores low. Give WIT color, an outfit, a wide expression range, and an attitude that fits "smart, dry, slightly rude."
- `Core` (owner-confirmed 2026-06-28): use deliberate **mascot-only focus beats** - empty frame, mascot centered, no other illustration - to signal "listen to this line." Casually Explained does this constantly. It is a rhythm tool: dense illustrated beats, then a clean mascot beat to let a point or punchline land.
- `Core` (owner-confirmed 2026-06-28): a single real screenshot / clean UI mockup can be a complete comedy beat on its own (the reference uses one real Threads post per joke). For Why It Works this = real-looking app/notification/chat/receipt mockups (see brand-system "Real-UI Illustration"), each carrying one joke or one piece of evidence.

- `Core` creative direction (owner-confirmed 2026-06-28, `why-the-internet-is-full-of-ai-slop` S3): visual-plan
  must be UNLIMITED in imagination and GENERATE-FORWARD. If an idea is good it must be realized by all means -
  write generate prompts and produce bespoke surreal heroes (e.g. a content-grinder "slop machine", a melting
  AI influencer, a firehose of grey clones, a robot in a human mask) rather than downgrading to a safe browsed
  photo. Do NOT reuse one background across many sections as a crutch (the `grey-sludge-flood` overuse was
  rejected: "every section uses it but the purpose isn't clear"); each section earns its own distinct imagery,
  a motif recurs only with clear in-section meaning. Browsed real photos are grounding bases/textures, not a
  substitute for bold generated heroes. Only real bound: copyright/law/YouTube community standards (parody not
  real logos; non-existent people). A section may legitimately need ~8-12 generate assets.

### New visual pipeline architecture (owner-directed 2026-06-28, in design - replaces the current section-by-section visual-plan style)

- **One master visual plan per video.** Sections are EXACT copies of their slice of the master, kept always in sync, so each section "sees" the whole video, not just itself. Write the whole, then split.
- **Scene granularity = per sentence (or a few sentences per scene)**, never per-section. Each scene described in EXTREME detail - enough that reading it alone lets you imagine ~99% of the frame with no image: composition/layout (positions in %, crop, z-order, left/right/center), every element, which mascot pose, emotion, insight/joke, the LINKAGE between elements (why they sit together, eye path), show-as-you-say timing per beat, on-screen handwritten text, sound, color/contrast.
- For each scene, list **ASSETS**, each with: `type` (generate | browse-real-photo | screenshot/web-capture | reuse), exact description, **filename** (so it can be referenced AND reused), layout/position. If an asset already exists from an earlier scene, reference the SAME filename and reuse - do NOT recreate (this is what keeps a character identical across scenes).
- **visual-plan does NOT write image-generation prompts.** It only describes scenes in detail. Writing prompts is `implement-visual-plan`'s job.
- **visual-plan has NO imagination limit** (only bounded by copyright, law, and YouTube community standards). Anything it writes, if it's good, MUST be executed by all means. It may invent brand-new poses or whole new scene ideas from imagination - it is NOT restricted to the existing pose library. The library is a starting palette, not a cage.
- **`implement-visual-plan`** (new step) reads each scene and produces the assets: for `generate` assets IT writes the detailed image-gen prompt (isolated element on transparent/plain background, channel flat-cartoon style - NEVER a full pre-composed scene, because full-scene generation breaks cross-scene character consistency) and generates; for `browse-real` assets it browses for a license-safe real photo; it can generate a brand-new pose the plan invented; it reuses existing files by filename (no regen). All assets saved into the project `assets/` folder under the filenames the plan specified.
- **render** composites mascot + assets pulled from `assets/` into each scene's layout. Same person → same file across scenes → identical look.
- Net flow: `visual-plan` (describe only, name files, unlimited imagination) → `implement-visual-plan` (write prompts / browse / reuse → save isolated assets to assets/) → `render` (composite per layout).
