# Short 02 — Productivity Theater (vertical)

Composition: `Short02Theater` · 1080×1920 (9:16) · duration `27.1s` (audio `25.877s` + ~1.2s payoff hold)
Port: `localhost:1102`
Source: `why-everyone-pretends-to-be-busy` Section 5 (trimmed).

## Voiceover
- `voiceover/short-02.mp3` — regenerated clean per-short VO, approved voice `David23 / am_eric / 0.84 / en-us`.
- `voiceover/short-02-word-timings.json` — whisper-tiny.en; tail re-timed monotonically.

## Structure (4 scenes, real photo bases, NO CTA)
1. **Hook** `0–5.78` — busy desk (phone/coffee). `REPLY FAST` / `JOIN THE CALL`. WIT typing.
2. **Staring at a wall** `5.78–13.46` — plain wall + window. Deadpan `POSSIBLY BLINKING`. WIT deadpan-side-eye (big).
3. **Perform motion** `13.46–18.08` — to-do-list desk. `MOVE A TASK COLUMN → COLUMN`. WIT thinking.
4. **Payoff** `18.08–27.1` — red theater curtain. `PRODUCTIVITY THEATER / starring: a spreadsheet` card + `TICKETS: PAID IN STRESS`. WIT facepalm. Complete ending, no CTA.

## Checks
- `lint`: 0 errors (2 non-blocking warnings).
- snapshot QA at `3.5 / 12.8 / 16.5 / 21 / 24s`: real bases, WIT scale/crop OK, captions centered & clear, deadpan wall + red-curtain theater land, payoff complete.
- Rules: safe zone, big WIT (face above caption), centered distinct subtitles, card carries the "productivity theater" payoff, no CTA.
- No MP4 export yet.
