# captions - memory

Durable translation lessons for the captions skill. Keep this file source-independent.

## Standing rules

- Always parse from `transcribes/transcript.md`, never from the script.
- English SRT is a direct copy, no LLM call needed.
- Translate all other languages in parallel in the same turn.
- Merge consecutive cues with no more than 2 seconds gap into one subtitle block.
- UTF-8 encoding for every file, including CJK languages.
- Output directory is `outputs/captions/`, created if absent.

## Future entries

After a reported quality issue, append:

```markdown
### YYYY-MM-DD, project N, <language>

Issue: <observable problem>

Fix: <durable lesson>
```

### 2026-08-22, project 9, vi

Issue: vi.srt had drifted out of sync with en.srt for roughly the first half of
the file (blocks 4-82): each block's text was offset from the block before it,
compounding until block 82's timestamp carried the video's final line instead
of its own. Blocks 83-164 were correct. Root cause unknown (likely a bad
merge during an earlier generation run), but the file had never been checked
against en.srt after writing.

Fix: after writing all language SRTs, always run a structural sync check
before reporting done: same block count as en.srt, and every block's sequence
number + timestamp pair identical across all language files (only the text
should differ). A silent per-block content drift will not show up as a count
mismatch, so diff block-by-block, not just count totals.
