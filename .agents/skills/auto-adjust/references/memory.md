# Auto Adjust Skill Memory

This file stores memory specific to the `auto-adjust` skill.

Use this file for post-render QA/fix patterns, preservation habits, report expectations, and recurring misses found after `render`.
Use `.agents/_shared/` for channel-wide visual systems and production rules.
Use `visual-plan/references/memory.md` or `render/references/memory.md` only when a lesson clearly belongs to those skills.

## Current Skill Standard

- Run after `render` and before `review`.
- Require one explicit or unambiguous project and one explicit or unambiguous section.
- Do not support `All`.
- Treat `section-previews/section-XX-*/index.html` as canonical.
- Preserve manual Studio edits before any fix.
- Read `visual-plan` memory, `render` memory, shared visual-production rules, and previous sections in the same project before editing.
- Fix with targeted patches, not full rewrites, unless the user explicitly requests a remake.
- Return a table of issues, fixes, and verification.
- Do not export MP4/WebM unless explicitly requested.
- Update this memory and shared memory only with reusable lessons.

## Review Lesson Inventory

- Voice sync: every cue-critical element must appear when the voice reaches its matching phrase; never batch-show many elements at cue start when the words arrive later.
- Motion density: ordinary labels hard-show on beat; reserve smash, stamp, shake, snap, and pop for emphasized words, proof, prices, contradiction labels, and payoff text.
- Big scene rhythm: short sections should feel like a few persistent big scenes with small cue changes, not a rapid slide deck.
- WIT role: WIT is the emotional subject when present. Use large, goofy, readable WIT for emotional beats.
- WIT scale: strong WIT beats can occupy `1/3` to `1/2` of the frame, or more when it improves the joke and does not block text/evidence.
- WIT placement: avoid default tiny lower-corner full-body placement on strong emotion beats. Use giant faces, side peeks, lower-edge half-body entrances, object hiding, or looming placements when appropriate.
- WIT dominance audit: CSS width is not proof of size. Measure the visible alpha/screenshot size because transparent PNG padding can make a `650px` WIT render as a small `230px` character.
- WIT density: large WIT does not mean frequent WIT. For short sections, start around `1-2` WIT beats per persistent big scene.
- WIT crop: intentional lower-body/edge crop is fine; face, glasses, head, shoulders, mouth, key props, and expression must never look accidentally cut.
- WIT/text collision: check both directions. WIT must not hide proof/text, and payoff text/stamps/cards must not cover WIT's face or expression.
- Subtitle safety: cue-critical lower-third labels, receipts, stamps, arrows, boxes, and payoff props should be moved up above likely YouTube subtitles.
- Markup: red circles/arrows/marks must target a real object and explain the voiceover; delete decorative or obvious marks.
- Assets: real/object photos should keep texture. Avoid global white wash overlays unless needed for local readability.
- Manual preservation: if Anh Khoa edits localhost/Studio manually, the live preview becomes source of truth. Future automated fixes must diff and backup before editing.
- Verification: run HyperFrames checks and inspect direct preview screenshots/contact sheets for WIT, collision, markup, and subtitle-zone fixes.

## Feedback Log

### 2026-06-12 - Skill Created From Section 1 And Section 2 Review

Classification: `Operational lesson`

Context:
Anh Khoa asked for a new post-render skill that synthesizes Section 1 and Section 2 review lessons, reads `visual-plan` and `render` memory, references `_shared`, compares previous sections, auto-fixes current section problems, and reports the issues and solutions.

Lesson:
Auto Adjust should run after Render and before Review. It must be one-section-only, preserve manual Studio edits, apply the review-prevention checklist across voice sync, motion density, WIT scale/rhythm/crop, text collision, subtitle safety, markup, assets, and HyperFrames mechanics, then verify and document the result.

Apply next time:
- Refuse `All` and require one project plus one section.
- Read current preview before editing and create a backup.
- Keep approved structure; apply targeted fixes.
- Make WIT bigger when emotion matters, but reduce WIT frequency when the section feels dense.
- Prefer hard-show cue timing over decorative animation.
- Verify with `npm.cmd run check` and direct preview screenshots/contact sheets when layout changed.
- Update this memory and shared docs only with reusable lessons.

Promote to shared memory:
Yes, as production workflow discoverability and post-render QA behavior.

### 2026-06-12 - WIT CSS Box Is Not WIT Visual Size

Classification: `Auto Adjust lesson`

Context:
After Auto Adjust ran on Section 3 of `why-cheap-products-keep-getting-worse`, Anh Khoa reported that WIT still looked very small and remained in the corners. The HTML used WIT CSS widths around `610-690px`, but the PNG transparent alpha boxes only contained about `33-43%` visible character width. The contact sheet confirmed the visible WIT still read as a full-body corner sticker.

Lesson:
Auto Adjust must not treat CSS image size as proof that WIT is large. It needs a WIT Dominance Gate that checks the visible alpha/screenshot size and the actual screen role. A WIT cue fails if it is still a lower-corner full-body sticker, if the visible character is too narrow, or if the face/expression does not dominate the emotional beat.

Apply next time:
- Build a WIT audit table before and after WIT fixes.
- Measure or estimate visible alpha bounding boxes for transparent WIT PNGs.
- Fail strong emotion beats when visible WIT width is below about `25%` of frame width.
- Prefer close-up, upper-body, bottom half-body, side peek, behind-object, or looming-face placements over corner standing poses.
- Do not report WIT as fixed unless the contact sheet proves visible WIT dominance, not only a bigger CSS box.

Promote to shared memory:
No for now; keep as Auto Adjust execution memory unless the same miss repeats across more sections.

### 2026-06-12 - Section 3 WIT Dominance Needs Real Seeked Proof

Classification: `Auto Adjust lesson`

Context:
The Section 3 WIT-dominance fix initially looked valid in HTML because WIT CSS widths were increased, but several visible characters were still under one-third of the frame after transparent padding and viewport clipping. A first contact sheet was also invalid because changing the Studio `t=` hash did not actually seek the player, producing repeated `t=0` frames.

Lesson:
For WIT-size review fixes, Auto Adjust must validate the viewport-clipped visible alpha box and a real seeked screenshot/contact sheet. If the contact sheet frames repeat or the Studio time indicator does not change, the screenshot proof is invalid. Move text blocks away from WIT before shrinking WIT; strong emotional WIT should normally land near `1/3` to `1/2` of the visible frame, not merely have a large CSS box.

Apply next time:
- Compute visible WIT size from alpha bbox and viewport clipping when PNGs have transparent padding.
- Use Studio progress-bar seeking or another verified seek mechanism; confirm the time indicator changes before capturing frames.
- Reject contact sheets where multiple timestamps show the same frame.
- If WIT collides with text, first reposition text/stamps/props; do not solve collision by returning WIT to a tiny corner.
- Report WIT dominance only after both `npm.cmd run check` and runtime screenshots/contact sheets pass.

Promote to shared memory:
No; keep as Auto Adjust verification procedure unless repeated in other skills.

### 2026-06-15 - Verify Fixed-Port Preview Scripts Before Browser QA

Classification: `Operational lesson`

Context:
During Auto Adjust for Section 6 of `why-cheap-products-keep-getting-worse`, the preview server was down. Restarting with the section `package.json` script launched HyperFrames on its default Studio port instead of the required fixed section port `1006`, so direct-preview browser QA failed until the server was restarted with `hyperframes preview --port 1006`.

Lesson:
Auto Adjust should verify the selected section preview is actually running on `1000 + section number`. If restarting is needed, use an explicit `--port` flag and patch the section `dev` script when it would otherwise drift to a random/default HyperFrames port.

Apply next time:
- check the fixed direct composition URL before screenshot QA
- inspect `preview.log` when the URL is down or reports an unexpected port
- start HyperFrames with `npx.cmd --yes hyperframes@<version> preview --port <section-port>` on Windows
- update the section-local `package.json` dev script if it lacks the fixed port
- document the port fix in `IMPLEMENTATION.md` and `06-production-board.md`

Promote to shared memory:
No; this is an Auto Adjust/browser QA operational fix, not channel strategy.

### 2026-06-18 - Use `hyperframes snapshot --at` For WIT/Collision Verification

Classification: `Auto Adjust lesson`

Context:
Auto Adjust on the restored Section 6 of `why-cheap-products-keep-getting-worse`. Earlier WIT-verification attempts (2026-06-12 Section 3) struggled with manual Studio seeking and invalid contact sheets (repeated `t=0` frames). This run needed reliable visible-WIT and text-collision proof for cues 5 and 8.

Lesson:
`npx --yes hyperframes@<ver> snapshot --at <t1,t2,...>` captures real composited PNG frames plus a `contact-sheet.jpg` into `snapshots/`, seeking the paused GSAP timeline correctly. It is the reliable WIT Dominance Gate and collision-verification tool — no custom Puppeteer/seek hacks, no invalid repeated-frame contact sheets. Read the contact sheet for the overview, then read the critical full-res frames for the WIT/collision beats and judge visible WIT size from the frame, not the CSS box.

Apply next time:
- from the section preview dir, run `npx --yes hyperframes@<ver> snapshot --at <one timestamp per cue, including each WIT beat after its reveal>`
- Read `snapshots/contact-sheet.jpg`, then the full-res frames for WIT/collision cues
- when auto-adjusting an already-approved or restored build, confirm flagged risks on snapshots before editing — they may already be fine (the cue 5 trapped-WIT-behind-glass and cue 8 WIT-vs-payoff-tag collisions were both non-issues here because text sat in a separate zone from the face)
- still patch the section `dev` script to `preview --port <1000+N>` (recurring port-drift fix)
- treat validate contrast warnings on dark labels over light photo bases as likely false positives; confirm readability on the snapshot rather than redesigning the approved build

Promote to shared memory:
No; this is Auto Adjust verification tooling, not channel strategy.

### 2026-06-21 - Word-Timings JSON Is The Source Of Truth For Voice-Sync Re-Timing

Classification: `Auto Adjust lesson`

Context:
Anh Khoa reviewed Section 6 of `why-cheap-products-keep-getting-worse` and reported that the `cue-ownership-lock` beat ("And sometimes the product looks at you and says, 'You own me...' Very healthy relationship") was spoken at ~13s but the cue was pinned at `16.8s`, which pushed every downstream cue late. He also asked to remove the gray photo overlay (and clarified: keep backgrounds as-is, only remove the gray wash).

Lesson:
The section voiceover folder contains `section-XX-word-timings.json` (faster-whisper word + segment timestamps). This is the authoritative source for voice-sync fixes — re-pin every cue `data-start`, scene cut, and GSAP reveal to the actual word start, not to estimates or the prior build's values. When one cue is misaligned, fix the whole downstream chain, not just that cue. For "remove the gray overlay," confirm scope: the gray wash = the `.photo-grade` overlay div + desaturating `filter` on the photo; the user may want backgrounds (scene gradients) kept — ask before touching backgrounds.

Apply next time:
- Read `voiceover/section-XX-*/section-XX-word-timings.json` first for any voice-sync complaint; build the cue map from `words[]`/`segments[]`.
- Re-pin cues, scene clips, nested clips, and GSAP reveal times together so the whole chain matches the voice.
- Accumulating elements that must stay visible together (e.g., the 3 barrier trays) cannot overlap on one track — put each on its own `data-track-index` (3/4/5), give them `clip` class + stable ids; overlapping same-track clips is a blocking lint error.
- Watch floating-point cue boundaries: `5.3 + 4.56 = 9.860000000000001` overlaps a clip starting at `9.86`. Trim the duration (e.g., to `4.55`) to leave a clean boundary.
- After re-timing, update the section `package.json` `inspect --at` timestamps to the new cue mid-points, and regenerate snapshots at the new times.
- Disambiguate "remove gray overlay / linear-gradient" with the user before stripping background gradients or prop shading; flattening prop gradients destroys 3D objects.

Promote to shared memory:
No; this is Auto Adjust execution practice. Note for visual-plan/render: section word-timings JSON should be used at render time so cues are voice-synced before Auto Adjust ever sees them.

### 2026-06-21 - Sourcing A Real CC Image To Replace A CSS Prop / Empty Background

Classification: `Auto Adjust lesson`

Context:
Second Section 6 review. Anh Khoa flagged that the ownership-lock beat had no real background (just a flat gradient) and that the CSS `lock-icon` did not read as a lock, asked to reveal Scene-2 text with the voice instead of all at once, and asked to delete the empty decorative `mystery-machine`. No image-generation tool is available in this environment.

Lesson:
When a beat needs a real image and there is no image-gen tool, source a CC-licensed photo from Wikimedia Commons via its API (same provenance as the channel's existing photo bases) and grade it in. A single well-chosen photo (a padlock close-up) can serve as both the scene background and the object depiction, letting you delete the weak CSS prop entirely. Stagger within-cue text to the word timings with GSAP `opacity` sets (same pattern as the relationship-note reveal) rather than nested clips, which avoids same-track overlap lint errors. Remove decorative "empty rhetoric" elements the user names, but flag (don't silently delete) similar ones they did not name.

Apply next time:
- Wikimedia Commons API for sourcing: `curl -G https://commons.wikimedia.org/w/api.php` with `action=query&generator=search&gsrsearch=filetype:bitmap <terms>&gsrnamespace=6&prop=imageinfo&iiprop=url|size|extmetadata&iiurlwidth=1920`. Parse JSON with `node -e` (no Python on this Windows box; no `jq`). Prefer landscape ≥1600px wide; capture `Artist` + `LicenseShortName` + `descriptionurl` for attribution; CC0/CC BY/CC BY-SA are all in-policy (channel already uses CC BY-SA).
- Download the `iiurlwidth` thumb (e.g. 1920px) straight into `assets/section-06/`, view it with Read before committing, then copy it to the review mirror's `assets/section-06/` too.
- Use `object-position` (e.g. `42% center`) to keep the photo's subject clear of the WIT zone instead of re-cropping the file.
- Respect the user's standing "keep backgrounds, only remove the gray wash" rule from the prior pass — do not add heavy grade filters to the new photo; keep it clean and check readability on a snapshot.
- Add the new asset to the canonical `assets/ATTRIBUTION.md` (video-level, not the stale review-mirror copy).
- Always take a pre-edit backup at the start of the pass; if the file was hand-modified mid-session, note that the intentional user edit is being incorporated and create a fresh restore point.

Promote to shared memory:
No; this is Auto Adjust execution practice. The Wikimedia-API + node-parse sourcing recipe could move to `_shared/systems/visual-production.md` if render/visual-plan start sourcing images the same way.

Pass-3 addenda (same day, third Section 6 review):
- Brand safety beats palette: a CC0 desk photo had a recognizable laptop (MacBook). In a video criticizing products, any recognizable branded device is a risk — reject it for a logo-free image even if it means a less-perfect license (CC BY-SA). Verify on the actual snapshot, not just the thumbnail.
- A 1920-wide `object-fit: cover` source the same width as the frame is only croppable vertically — `object-position`'s horizontal value does nothing, so you cannot hide a subject on the left/right edge by repositioning. Pick a different image instead.
- Intentional off-canvas WIT (e.g. `right:-420px`) trips three inspect rules (`clipped_text`, `text_box_overflow`, `canvas_overflow`). Putting `data-layout-allow-overflow` on the *image* is not enough — the wrapping cue clips it. Add `data-layout-allow-overflow=""` AND `style="overflow: visible;"` to the cue `div`; the composition root still clips at the canvas edge, so the visual is unchanged but inspect goes clean.
- Stagger list items (policy rows, checklist questions) to each spoken word with GSAP `opacity` sets keyed to the word-timings JSON, same pattern as single-label reveals — this is the standard answer to "show each item when the voice says it."
- Section 6 now has real photo backgrounds on all four non-checkpoint beats (repair / euro-money / padlock / phone). If a future section's CSS-only beat draws a "no background / no image" review note, default to sourcing a real CC photo rather than improving the CSS.
