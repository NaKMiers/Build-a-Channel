import re, sys, os
from pathlib import Path

P = Path("projects/18-why-your-brain-still-treats-silence-like-a-warning-signal")
transcript_path = P / "transcribes/transcript.md"

lines = [l.strip() for l in transcript_path.read_text().splitlines() if l.strip()]

cues = []
for idx, line in enumerate(lines):
    m = re.match(r'^\[(\d+):(\d+)\.(\d+)\] (.*)$', line)
    mins, secs, ms, text = int(m.group(1)), int(m.group(2)), int(m.group(3)), m.group(4)
    time_str = f"[{mins}:{secs:02d}]"
    cues.append({
        "idx": idx + 1,
        "time_str": time_str,
        "full_ts": f"[{mins:02d}:{secs:02d}.{ms:03d}]",
        "text": text
    })

print(f"Loaded {len(cues)} cues.")
