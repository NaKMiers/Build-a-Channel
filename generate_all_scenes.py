import sys, os, re

P = "projects/16-you-never-noticed-how-one-good-choice-lets-you-make-a-bad-one"

raw_lines = [l.strip() for l in open(f"{P}/transcribes/transcript.md") if l.strip()]
cues = []
for i, l in enumerate(raw_lines):
    m = re.match(r'^\[(\d+):(\d+)\.\d+\]\s*(.*)$', l)
    mm, ss, txt = int(m.group(1)), int(m.group(2)), m.group(3)
    if i == 76:
        ts = "[2:33]"
    else:
        ts = f"[{mm}:{ss:02d}]"
    cues.append({'idx': i+1, 'ts': ts, 'txt': txt})

print(f"Total cues loaded: {len(cues)}")
