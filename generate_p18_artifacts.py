import re, sys, os
from pathlib import Path

P = Path("projects/18-why-your-brain-still-treats-silence-like-a-warning-signal")
transcript_path = P / "transcribes/transcript.md"

V2_STYLE_ANCHOR = "Hand-drawn 2D editorial storybook doodle animation, semi-flat colors on a warm paper-based palette, expressive charcoal outlines with subtle line-weight hierarchy,"
V2_STYLE_LOCK = "restrained paper grain, clear visual hierarchy, no photorealism, no 3D, no CGI, no anime, no manga, no realistic anatomy, no glossy vector finish, no busy decoration, no timestamp shown in the image, @[name] is mention syntax for reference only and must never be rendered as visible text, 16:9 aspect ratio, Warm Editorial Storybook Doodle style."
V2_SCENE_REF_LIMIT = "use the attached scene reference only as the design source for the object named beside it, matching that object's shape, proportion, colour and line treatment exactly, and take nothing else from it: not its composition, not its camera or framing, not its background or surface, and none of the other objects in it,"

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
        "text": text,
        "mins": mins,
        "secs": secs
    })

print(f"Total cues: {len(cues)}")
