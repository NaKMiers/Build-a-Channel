# Shorts Plan - `Why Cheap Products Keep Getting Worse`

Status: `DONE - all 3 shorts approved + exported to output/shorts/ (1080x1920, h264+aac, 30fps). Previews still live: S01 :1101, S02 :1102, S03 :1103.`

Exported deliverables (verified with ffprobe):
- `output/shorts/short-01-the-9-dollar-chair.mp4` - 28.42s, 1080x1920, 4.2 MB
- `output/shorts/short-02-you-own-me.mp4` - 26.62s, 1080x1920, 5.5 MB
- `output/shorts/short-03-subscription-with-extra-steps.mp4` - 21.42s, 1080x1920, 7.0 MB
Render: `npx hyperframes render` per short (Chrome + ffmpeg-static). Suggested posting order: S01 → S02 → S03.

RE-EXPORTED 2026-06-23: applied the opening-caption fix (first caption with show-time 0.0 was cancelling out) and re-rendered all 3 to `output/shorts/`. ffprobe-verified 1080x1920 h264+aac.

Vertical safe-zone rule (apply to ALL shorts): keep readable content (labels, captions, CTA, WIT face) inside `x[60..880] · y[220..1490]`. Outside it the platform UI covers content - top title, right action rail (like/comment/share/menu), bottom caption + subscribe + progress bar. WIT body may bleed off the bottom/side edges; its face must stay inside. Captions + CTA live at `bottom:470px`.

Environment note: HyperFrames TTS requires Python 3 + kokoro-onnx. This machine had none - installed Python 3.14.6 (scoop) + kokoro-onnx 0.4.7 + soundfile. Word timings via cached transformers.js whisper-tiny.en. ffmpeg/ffprobe static binaries reused from `%TEMP%/wiw-ffmpeg-static`.

Type: `one-off shorts sub-workflow (skill-ify later once the recipe is proven)`

Source: main video (8 sections, approved) + combined voiceover + combined word-timings.

## Goal

Produce **3 first-class vertical shorts (9:16, 1080×1920)** for YouTube Shorts / TikTok / Reels.
Each short is a self-contained idea with a fast hook, a payoff, channel-identity visuals (big readable
handwritten labels + big WIT + real photo bases), burned-in voice-synced captions, and a CTA toward the
full video. Production method = **native portrait rebuild** (new portrait HyperFrames comp per short,
reusing the existing assets/WIT/photos/fonts), NOT a crop of the 16:9 master.

## Selected shorts

| ID | Short | Source section(s) | Core idea | Target length |
|---|---|---|---|---|
| S01 | The $9 chair | Section 1 (+ Section 8 button) | A bargain that loses its future | ~25s |
| S02 | You own me, but not enough to open me | Section 6 (trimmed) | Repairability, explained simply | ~31s |
| S03 | A subscription with extra steps | Section 7 (trimmed) | Replacement becomes the default | ~27s |

Suggested posting order: **S01 first** (anchor/trailer for the freshly published long video), then S02, then S03.

## Global spec (applies to all 3)

- **Canvas:** root composition `data-width="1080" data-height="1920"` (portrait). HyperFrames renders at the declared dims.
- **Ports:** S01 → `localhost:1101`, S02 → `1102`, S03 → `1103` (kept clear of the long-form 1000–1008 range).
- **Working dirs:** `projects/<slug>/shorts/short-01-the-9-dollar-chair/`, `.../short-02-you-own-me/`, `.../short-03-subscription-with-extra-steps/` (each a self-contained HyperFrames project) + review mirrors.
- **Final exports:** `projects/<slug>/output/shorts/short-01-the-9-dollar-chair.mp4`, `short-02-you-own-me.mp4`, `short-03-subscription-with-extra-steps.mp4`.
- **Voiceover:** regenerate a clean short-specific VO per short from the trimmed/assembled script using the **approved channel voice** (`David23 / am_eric / 0.84 / en-us`, `npx hyperframes tts`). Same words, same voice - only the subset each short needs (+ any tiny CTA line). This avoids audible seams from mid-section splicing and gives clean caption timing. (Alternative if you prefer zero re-TTS: reuse original section audio and slice `combined-word-timings.json` by time window - works for S01, but S02/S03 need mid-section cuts so re-TTS is cleaner.)
- **Captions:** burned-in, handwritten font (PatrickHand), 2–4 words at a time, voice-synced. Timing from each short's freshly generated word-timings (whisper-tiny.en recipe), or sliced from `combined-word-timings.json` if we reuse original audio. Placed in a lower-mid **subtitle-safe zone**.
- **Vertical safe zones:** keep key content out of the **top ~12%** (Shorts title/UI) and **bottom ~18%** (action rail + platform caption). Keep important labels center / slightly left of the right-hand action rail.
- **WIT:** reuse approved poses; BIG and HIGH (≈1/3–1/2 of the vertical frame), head+glasses+torso in-frame. Portrait actually flatters a tall WIT. Re-arrange labels around WIT, never shrink WIT to fit.
- **Backgrounds:** reuse the section's already-vetted real photo bases (attribution already recorded). Every scene gets a real people-free photo base per channel rule.
- **Audio:** narration-first. Optional light reused SFX only (receipt printer, lock click) under narration; never over words.
- **Ending:** complete standalone short - no CTA / "watch the full video" card. End on the short's own payoff beat (loop-friendly where possible).
- **Per-short platform packaging (light):** on-screen hook text + a one-line caption/title + hashtags (reuse `#WhyItWorks` family). Folded into each short below, not a separate packaging skill.

---

## S01 - The $9 chair  (anchor / trailer)

**Why:** funniest, most visual, one dominant object, a complete mini-story; best at selling the full video.

**Final VO (regenerated, ~25s):**
```
I find a chair for nine dollars.
It has four legs, a seat, and the confidence of a much better chair.
So he buys it.
For the first week, everything is fine.
Then the chair starts making a noise that sounds like legal advice.
The screw gets loose. One leg begins exploring other career options.
And suddenly, the cheap chair was not really cheap.
It was a normal chair with one small problem: future not included.
[button] So next time, the better question isn't "how much does it cost?" - it's "how much future is included?"
```
*(Body = Section 1 verbatim; button = condensed Section 8. "The seat feels nervous" line optional-cut for pace.)*

**Vertical scenes (3 + button):**
1. **Setup (0–~6s):** real cheap-chair photo base, big `$9` sale tag, hook caption. WIT excited entering from bottom.
2. **Failure (~6–15s):** same chair, screw loosening / leg wobbling; labels hard-show on beats (`legal advice`, `other career options`). WIT suspicious (big).
3. **Reveal (~15–22s):** hidden tag drops - `FUTURE NOT INCLUDED`. WIT betrayed (giant, high).
4. **Button (~22–25s):** `HOW MUCH FUTURE?` + CTA card.

**Assets reused:** Section 1 chair photo, `FUTURE NOT INCLUDED` tag, WIT excited/suspicious/betrayed poses.
**Captions:** S1 window of combined timings (0–21.26s) re-zeroed, + new timing for the button line.
**Platform caption:** "I bought a $9 chair. It had a hidden label. 😳" · `#WhyItWorks #cheapproducts #righttorepair`

---

## S02 - You own me, but not enough to open me  (the useful insight)

**Why:** strongest punchline + a real, teachable concept (repairability). "I never thought about it like that."

**Final VO (regenerated, trimmed, ~31s):**
```
A product feels disposable when fixing it becomes harder than replacing it.
Sometimes the part is not available. Sometimes the tool is special.
Sometimes the repair costs almost as much as buying a new one.
And sometimes the product looks at you and says: "You own me, but not enough to open me."
Very healthy relationship.
This is why repairability matters.
Repairability just means how easy something is to fix.
That is basically society looking at a phone and saying: "Please have a future."
```
*(Cuts the governments/policy sentence and the "can you replace the battery / buy the part / local repair shop" list to fit short length. Section 6 has REAL word-timings already.)*

**Vertical scenes (3 + button):**
1. **Lock-out (0–~9s):** real repair-bench / opened-phone photo; locks appear - `PART`, `TOOL`, `COST`. Hook caption. WIT trying to get in.
2. **Punchline (~9–18s):** real padlocked-product photo; speech bubble `"YOU OWN ME, BUT NOT ENOUGH TO OPEN ME"`; deadpan `Very healthy relationship.` WIT trapped/betrayed (giant, high).
3. **Definition (~18–27s):** card `REPAIRABILITY = how easy it is to fix` (learner phrase highlighted). Real phone photo.
4. **Button (~27–31s):** `PLEASE HAVE A FUTURE` (warm/deadpan) + CTA card.

**Assets reused:** Section 6 repair/padlock/opened-phone photos, repairability definition, WIT trapped/deadpan poses.
**Captions:** Section 6 window (149.74–192.6s) - trimmed segments re-zeroed, or fresh timings if re-TTS.
**Platform caption:** "Some products literally lock you out of fixing them. 🔒" · `#WhyItWorks #righttorepair #repairability`

---

## S03 - A subscription with extra steps  (replacement becomes normal)

**Why:** the landfill line + the receipt-loop motif; meme-able button. Different emotion (resigned/tired).

**Final VO (regenerated, re-ordered for a faster hook, ~27s):**
```
Most people don't wake up and say: "Today I'd like to create a small landfill with my headphones."
They replace things because the system makes replacement feel easier.
The repair quote is high. The spare part is missing. The new one arrives tomorrow.
So you buy the product again.
The price tag smiles again. The receipt prints again.
And the cheap product quietly becomes a subscription with extra steps.
```
*(Hook moved to the landfill joke. "When repair gets slow, confusing, or expensive…" intro dropped. "So WIT buys" → "So you buy" for direct short address - flag if you'd rather keep WIT third-person.)*

**Vertical scenes (3 + button):**
1. **Hook (0–~7s):** real e-waste / pile-of-old-devices photo; hook caption (landfill line). WIT reluctant.
2. **The system (~7–17s):** real delivery-box photo; staggered labels on beats - `REPAIR QUOTE: HIGH`, `SPARE PART: MISSING`, `NEW ONE: ARRIVES TOMORROW`.
3. **Receipt loop (~17–24s):** real checkout/receipt photo; `price tag smiles again`, receipt printing. WIT tired/deadpan (big).
4. **Button (~24–27s):** `A SUBSCRIPTION WITH EXTRA STEPS` + CTA card.

**Assets reused:** Section 7 e-waste / fulfillment-box / checkout photos, receipt prop, WIT tired/deadpan poses.
**Captions:** Section 7 window (192.6–221.98s) re-zeroed (combined timings are real), or fresh if re-TTS.
**Platform caption:** "Cheap stuff is basically a subscription you didn't sign up for. 🧾" · `#WhyItWorks #consumerbehavior #modernlife`

---

## Decisions (owner-approved 2026-06-22)

1. **Voiceover:** REGENERATE clean per-short VO with the approved voice (`David23 / am_eric / 0.84 / en-us`). No splicing.
2. **Captions:** distinct SUBTITLE style - white text on a translucent dark pill (NOT the cream handwritten label look), centered VERTICALLY, 2–4 words, voice-synced. Keep WIT face below the caption, in-scene labels above it, and time captions to clear before any big reveal/question card so the caption never covers WIT, labels, or cards. (Owner-revised at S01 review 2026-06-22.)
3. **Ending:** NO CTA / "watch the full video" card. Each short is a COMPLETE standalone short, not a hook/teaser - it ends on its own payoff beat (e.g. S01 ends on `HOW MUCH FUTURE?`). (Owner-revised at S01 review 2026-06-22.)
4. **S03 wording:** default to direct address "So you buy it again" unless owner objects at review.
5. **Build order:** S01 first → owner review/edit → then S02 → then S03 (one-at-a-time review, matching the section discipline).

## Build steps (deferred until plan approval)

1. Per short: finalize VO script → generate VO (approved voice) → generate word-timings.
2. Build portrait HyperFrames project (1080×1920) reusing section assets; static-first, voice-synced, big WIT, real photo bases, burned captions; preview on 1101/1102/1103.
3. `lint` / `validate` / `inspect` + snapshot QA per short.
4. Owner review → edit loop per short.
5. Export each to `output/shorts/*.mp4`; verify with ffprobe.
6. (Later) capture the proven recipe as a reusable shorts sub-workflow / skills.
</content>
</invoke>
