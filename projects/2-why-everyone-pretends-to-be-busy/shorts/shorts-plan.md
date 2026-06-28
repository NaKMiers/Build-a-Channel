# Shorts Plan - `Why Everyone Pretends To Be Busy`

Status: `DONE - all 3 exported to output/shorts/ (1080x1920, h264+aac, 30fps). Picks: C1=S01, C4=S02, C7=S03.`

Exported (ffprobe-verified): `short-01-busy-is-not-an-emotion.mp4` 24.92s · `short-02-productivity-theater.mp4` 27.12s · `short-03-work-you-cant-see.mp4` 20.42s. Suggested posting order: S01 → S02 → S03.

Caption bug fixed during S03 build (opening caption with show-time 0.0 cancelled out). Patched S01+S02+S03 here. NOTE: video-2 (`why-cheap-products`) exported shorts have this bug and need re-export.

Source: main video (7 sections, approved + combined). Produced by the `shorts` skill (plan mode).

## Locked rules (from `shorts` skill / video-2 review)

- Native portrait rebuild (1080×1920), never a crop of the 16:9 master.
- Each short is a COMPLETE standalone short - **NO CTA / "watch the full video" card**. End on its own payoff.
- Platform-safe zone `x[60..880] · y[220..1490]`; WIT body may bleed off edges, FACE stays inside.
- WIT big (≈⅓–½ frame), face above the centered caption.
- Captions = distinct white-on-translucent-dark subtitle, centered VERTICALLY; punchline/payoff carried by cards (no duplication, no overlap).
- Reuse each source section's real photo bases + WIT poses + font; regenerate per-short VO in the approved voice `David23 / am_eric / 0.84 / en-us`; caption from real word timings (tail re-timed).
- Ports `1100 + short number`. Export to `output/shorts/`.

## Selected shorts

| ID | Short | Source section | Core idea | Target length |
|---|---|---|---|---|
| S01 | Busy is not an emotion | Section 3 (trimmed) | "Busy" signals importance, not effort | ~30s |
| S02 | Productivity theater | Section 5 (trimmed) | Visible motion gets rewarded over thinking | ~30s |
| S03 | The work you can't see | Section 2 (trimmed) | Real progress hides where it isn't visible | ~28s |

Suggested posting order: S01 → S02 → S03.

---

## S01 - Busy is not an emotion  (Section 3)

**Final VO (trimmed, ~30s):**
```
When someone says "I'm so busy," it doesn't only mean they have a lot to do.
It can also mean: please notice that I'm important.
That's why people say it even when nobody asked.
"How are you?" "Busy." Which is not actually an emotion.
Busy sounds responsible. Busy sounds needed.
So people fill the day - sometimes with real work, sometimes with meetings about why the last meeting didn't finish anything.
At some point the job stops being the work. The job becomes proving you're near the work.
```
**Scenes (real photo bases from S3):**
1. **Hook** - `base-busychat` (a chat saying "busy"). Caption + WIT talking-front.
2. **"Not an emotion"** - `base-emotions`; card `BUSY ≠ AN EMOTION` (the meme beat). WIT deadpan/suspicious.
3. **Filling the day** - `base-busychat`/meeting stack; label `MEETINGS ABOUT MEETINGS`. WIT awkward-celebration.
4. **Payoff** - `base-nearwork`; card `PROVING YOU'RE NEAR THE WORK`. WIT tiny-defeated. No CTA.

## S02 - Productivity theater  (Section 5)

**Final VO (trimmed, ~30s):**
```
Visible work is just easier to reward.
Reply quickly, and people see it. Join every meeting, and people see it.
But spend two hours thinking hard, and it can look like nothing happened.
You solved the real problem - but from the outside, you were a person staring at a wall. Possibly blinking.
So people perform motion. Reply fast, join the call, move a task from one column to another.
This has a name. Productivity theater.
Same as normal theater, except the tickets are paid in stress, and the star of the show is a spreadsheet.
```
**Scenes (real photo bases from S5):**
1. **Hook** - `base-desk-call` (visible busy). Labels `REPLY FAST` / `JOIN THE CALL`.
2. **Staring at a wall** - `base-wall`; deadpan `POSSIBLY BLINKING` label. WIT deadpan (big).
3. **Perform motion** - `base-desk-board` (dragging a task column to column).
4. **Payoff** - `base-stage`; card `PRODUCTIVITY THEATER` + small `★ a spreadsheet`. WIT facepalm. No CTA.

## S03 - The work you can't see  (Section 2)

**Final VO (trimmed, ~28s):**
```
Modern life rewards the look of work more than the work itself.
Because real progress is hard to see.
Thinking looks like nothing. Solving a problem in your head looks like nothing.
But busy is easy to see - meetings, fast typing, a serious face at a screen.
So we trust what we can see, and ignore what we can't.
Which is a problem - because the real work usually hides in the part you cannot see.
```
**Scenes (real photo bases from S2):**
1. **Hook** - `base-typing` (visible busy). Caption + label `THE LOOK OF WORK`.
2. **Thinking looks like nothing** - `base-idea`; label `THINKING = (looks like) NOTHING`. WIT thinking (big).
3. **We trust what we can see** - split `LOOKING BUSY` vs `REAL WORK` (`base-typing` / `base-idea`).
4. **Payoff** - card `REAL WORK HIDES WHERE YOU CAN'T SEE IT`. WIT deadpan. No CTA.

## Open decisions for owner

1. Picks confirmed: C1 (S01), C4 (S02), C7 (S03). Any swap before build?
2. S02 wording: keep "possibly blinking" deadpan aside (recommended - strong beat)?
3. Otherwise I build S01 → review → S02 → S03, then export to `output/shorts/`.

## Build steps (deferred until approval)

Per short: regenerate VO (approved voice) → word-timings (whisper, tail re-timed) → copy minimal asset set → portrait 1080×1920 comp on port `110N` (big WIT, safe zone, centered subtitles, no CTA) → lint/validate/snapshot QA → preview → review → export MP4 to `output/shorts/` (ffprobe-verified).
