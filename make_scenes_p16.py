import sys, os, re

P = "projects/16-you-never-noticed-how-one-good-choice-lets-you-make-a-bad-one"

# Read transcript cues
raw_lines = [l.strip() for l in open(f"{P}/transcribes/transcript.md") if l.strip()]
cues = []
for i, l in enumerate(raw_lines):
    m = re.match(r'^\[(\d+):(\d+)\.\d+\]\s*(.*)$', l)
    mm, ss, txt = int(m.group(1)), int(m.group(2)), m.group(3)
    # Collision bump at cue 77 (index 76)
    if i == 76:
        ts = "[2:33]"
    else:
        ts = f"[{mm}:{ss:02d}]"
    cues.append({'idx': i+1, 'ts': ts, 'txt': txt})

print(f"Loaded {len(cues)} cues.")

# Style strings
V2_ANCHOR = "Hand-drawn 2D editorial storybook doodle animation, semi-flat colors on a warm paper-based palette, expressive charcoal outlines with subtle line-weight hierarchy,"
V2_LOCK = "restrained paper grain, clear visual hierarchy, no photorealism, no 3D, no CGI, no anime, no manga, no realistic anatomy, no glossy vector finish, no busy decoration, no timestamp shown in the image, @[name] is mention syntax for reference only and must never be rendered as visible text, 16:9 aspect ratio, Warm Editorial Storybook Doodle style."
V2_LIMIT = "use the attached scene reference only as the design source for the object named beside it, matching that object's shape, proportion, colour and line treatment exactly, and take nothing else from it: not its composition, not its camera or framing, not its background or surface, and none of the other objects in it,"

print("Constants loaded.")
