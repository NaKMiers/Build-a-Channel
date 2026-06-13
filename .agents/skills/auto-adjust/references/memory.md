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
