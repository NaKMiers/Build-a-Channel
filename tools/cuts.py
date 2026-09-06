"""Where every scene image is cut, and for how long. Shared by every exporter.

The scene image on disk is named `[M-SS].jpg`, the Windows-safe form of the `[M:SS]`
stamp in prompts/image-prompts.md, which is itself `tsfmt.to_mss()` of the transcript's
`[MM:SS.SSS]`. Truncation threw the milliseconds away, so the file name can only say
which second a cut lands in and the transcript is the only place the real time survives.

Everything subtle about that recovery lives here, in one place, because it is subtle:
pairing by position rather than by stamp, prompt stamps that drifted from `to_mss`, cues
that share a whole second in a legacy transcript, and cues with no image at all. A second
exporter that re-derived any of it would drift from the first.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tsfmt  # noqa: E402

# Where the logo sits, as fractions of the frame, so both exporters place it identically.
# The numbers come from the Kdenlive transform the channel settled on: at 2560x1440 that
# is a 100px square at 2330,1200, which leaves 130px to its right and 140px below it.
LOGO_WIDTH = 100 / 2560
LOGO_RIGHT = 130 / 2560
LOGO_BOTTOM = 140 / 1440


def logo_box(width, height, size=None, right=None, bottom=None):
    """Pixel box (x, y, w, h) for the logo in a frame of this size."""
    w = round(width * (size if size is not None else LOGO_WIDTH))
    x = width - w - round(width * (right if right is not None else LOGO_RIGHT))
    y = height - w - round(height * (bottom if bottom is not None else LOGO_BOTTOM))
    return x, y, w, w


# Scene image file names: the `[M:SS]` prompt stamp with the colon swapped for a hyphen.
SCENE_RE = re.compile(r"^\[(\d+)-(\d{2})\]$")
IMAGE_EXTS = (".jpg", ".jpeg", ".png", ".webp")


def tc(frames, fps):
    """MLT's HH:MM:SS.mmm. Milliseconds are derived from the frame, never the reverse."""
    ms = round(frames * 1000 / fps)
    h, rest = divmod(ms, 3_600_000)
    m, rest = divmod(rest, 60_000)
    return f"{h:02d}:{m:02d}:{rest // 1000:02d}.{rest % 1000:03d}"


def tc_frames(frames, fps):
    """HH:MM:SS:FF, the shape kdenlive:duration takes."""
    total = int(round(frames))
    f = total % round(fps)
    total //= round(fps)
    return f"{total // 3600:02d}:{total // 60 % 60:02d}:{total % 60:02d}:{f:02d}"


# ------------------------------------------------------------------------ image sizes


def image_size(path):
    """Width and height straight out of the file header. Pillow is not a dependency here."""
    with open(path, "rb") as fh:
        head = fh.read(32)
        if head[:8] == b"\x89PNG\r\n\x1a\n":
            return int.from_bytes(head[16:20], "big"), int.from_bytes(head[20:24], "big")
        if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
            fh.seek(12)
            chunk = fh.read(30)
            if chunk[:4] == b"VP8X":
                w = int.from_bytes(chunk[8:11], "little") + 1
                h = int.from_bytes(chunk[11:14], "little") + 1
                return w, h
            if chunk[:4] == b"VP8 ":
                return (
                    int.from_bytes(chunk[14:16], "little") & 0x3FFF,
                    int.from_bytes(chunk[16:18], "little") & 0x3FFF,
                )
            if chunk[:4] == b"VP8L":
                bits = int.from_bytes(chunk[9:13], "little")
                return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
            return None
        if head[:2] != b"\xff\xd8":
            return None
        # JPEG: walk the marker segments to the frame header that carries the size.
        fh.seek(2)
        while True:
            marker = fh.read(2)
            if len(marker) < 2 or marker[0] != 0xFF:
                return None
            length = int.from_bytes(fh.read(2), "big")
            if 0xC0 <= marker[1] <= 0xCF and marker[1] not in (0xC4, 0xC8, 0xCC):
                body = fh.read(5)
                return int.from_bytes(body[3:5], "big"), int.from_bytes(body[1:3], "big")
            fh.seek(length - 2, 1)


# ----------------------------------------------------------------------- audio length


def audio_seconds(path):
    """Length of the narration, without requiring ffmpeg."""
    if path.suffix.lower() == ".mp3":
        try:
            import mp3frames

            return mp3frames.duration(str(path))
        except Exception:
            pass
    import subprocess

    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(path)],
        capture_output=True, text=True,
    )
    if out.returncode != 0 or not out.stdout.strip():
        raise SystemExit(f"cannot measure {path}: install ffprobe or supply --duration")
    return float(out.stdout.strip())


# ------------------------------------------------------------------------------- cues


def scene_files(scenes_dir):
    """Every scene image on disk, keyed by its `[M:SS]` stamp. Range subfolders included."""
    found = {}
    dupes = []
    for path in sorted(scenes_dir.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in IMAGE_EXTS:
            continue
        m = SCENE_RE.match(path.stem)
        if not m:
            continue
        key = f"[{int(m.group(1))}:{m.group(2)}]"
        if key in found:
            dupes.append((key, found[key], path))
            continue
        found[key] = path
    return found, dupes


PROMPT_STAMP_RE = re.compile(r"^\[(\d+):(\d{2})\]", re.M)


def prompt_keys(path):
    """The `[M:SS]` stamps of prompts/image-prompts.md, in order.

    This is the file the scene image names were derived from, so it, not the transcript,
    is the authority on what a given image is called.
    """
    return [
        f"[{int(m.group(1))}:{m.group(2)}]"
        for m in PROMPT_STAMP_RE.finditer(path.read_text(encoding="utf-8"))
    ]


def transcript_cues(path):
    """[(seconds, `[M:SS]` key)] for every stamped transcript line, in file order."""
    cues = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("["):
            continue
        m = tsfmt.STAMP_RE.match(line)
        if not m:
            continue
        seconds = tsfmt.parse_timecode(m.group(0)[1:-1])
        cues.append((seconds, tsfmt.to_mss(m.group(0))))
    return cues


def build_cues(project, images, report, allow_gaps):
    """Pair each scene image with the real time its own transcript line starts.

    A truncated `[M:SS]` name can only say which second a cut lands in. The transcript
    still holds the millisecond, so it is the source of the cut and the file name is
    only the join key.
    """
    transcript = project / "transcribes" / "transcript.md"
    if not transcript.exists():
        report.append(f"no {transcript.relative_to(project)}, cutting on file names")
        cues = []
        for key, path in images.items():
            minutes, seconds = key[1:-1].split(":")
            cues.append((int(minutes) * 60 + int(seconds), path))
        return sorted(cues)

    lines = transcript_cues(transcript)
    if not lines:
        raise SystemExit(f"{transcript} has no timestamped lines")

    # Prefer pairing by position against image-prompts.md. Both files hold one entry per
    # cue in the same order, and that file is where the image names came from, so index
    # pairing survives a prompt stamp that drifted from `to_mss` (a `[10:10.980]` line
    # written as `[10:11]` instead of truncated to `[10:10]`). Falling back to matching
    # on the stamp alone would strand that image and silently drop its cut.
    prompts = project / "prompts" / "image-prompts.md"
    keys = prompt_keys(prompts) if prompts.exists() else []
    if keys and len(keys) == len(lines):
        drift = [
            (i, keys[i], tsfmt.stamp(lines[i][0], ms=True))
            for i in range(len(keys))
            if keys[i] != lines[i][1]
        ]
        if drift:
            shown = ", ".join(f"{k} is really {t}" for _, k, t in drift[:4])
            report.append(
                f"{len(drift)} prompt stamp(s) disagree with the transcript, pairing by "
                f"position instead: {shown}" + (" ..." if len(drift) > 4 else "")
            )
        pairs = [(lines[i][0], keys[i]) for i in range(len(keys))]
    else:
        if keys:
            report.append(
                f"{prompts.name} has {len(keys)} stamps but the transcript has "
                f"{len(lines)} lines, pairing on the stamp instead of by position"
            )
        pairs = lines

    cues = []
    used = set()
    missing = []
    for seconds, key in pairs:
        if key in used:
            # Two cues sharing one image: it is already on screen, so this is not a cut.
            continue
        path = images.get(key)
        if path is None:
            missing.append(key)
            continue
        used.add(key)
        cues.append((seconds, path))

    extra = [k for k in images if k not in used]
    if missing and not allow_gaps:
        # An unrendered cue is a hole in the video, and the image before it stretches to
        # cover the hole. That is not something to discover in the edit, so the build
        # stops here rather than producing a timeline that looks finished.
        shown = ", ".join(missing[:12]) + (" ..." if len(missing) > 12 else "")
        raise SystemExit(
            f"{len(missing)} cue(s) have no scene image, so the scenes are not fully "
            f"generated yet:\n  {shown}\n"
            f"Render them, or run /scene-polish verify to see the full list. Pass "
            f"--allow-gaps to build anyway and let the previous image hold through them."
        )
    if missing:
        report.append(
            f"{len(missing)} cue(s) have no scene image, the previous image holds "
            f"through them: {', '.join(missing[:8])}"
            + (" ..." if len(missing) > 8 else "")
        )
    if extra:
        report.append(
            f"{len(extra)} scene image(s) match no transcript cue and are left out: "
            + ", ".join(sorted(extra)[:8])
            + (" ..." if len(extra) > 8 else "")
        )
    return cues


# -------------------------------------------------------------------------- xml parts


class Plan:
    """One scene image per entry, already placed on the timeline.

    cuts[i] is (start_frame, length_frames, image_path). Exporters only translate this
    into their own file format; none of them recompute a time.
    """

    def __init__(self, cuts, total_frames, fps, audio, report):
        self.cuts = cuts
        self.total_frames = total_frames
        self.fps = fps
        self.audio = audio
        self.report = report

    def __len__(self):
        return len(self.cuts)


def plan(project, fps, allow_gaps=False, audio=None, duration=None):
    """Read a project and decide when every scene image appears and for how long."""
    project = Path(project).resolve()
    if not project.is_dir():
        raise SystemExit(f"no such project: {project}")

    scenes_dir = project / "scenes"
    if not scenes_dir.is_dir():
        raise SystemExit(f"no scenes folder in {project.name}, run /scenes first")

    audio = Path(audio) if audio else project / "audios" / "full.mp3"
    if not audio.exists():
        raise SystemExit(f"no narration at {audio}, run /transcript first")
    audio = audio.resolve()

    report = []
    images, dupes = scene_files(scenes_dir)
    for key, first, second in dupes:
        report.append(f"{key} has two images, using {first.name}, ignoring {second}")
    if not images:
        raise SystemExit(f"no `[M-SS]` scene images under {scenes_dir}")

    cues = build_cues(project, images, report, allow_gaps)
    if not cues:
        raise SystemExit("no scene image matched any transcript cue")

    total_seconds = duration or audio_seconds(audio)
    total_frames = int(round(total_seconds * fps))

    # A whole-second transcript can put several cues in one second, and image-prompts.md
    # broke those ties by bumping the stamp, so the real onsets were never written down.
    # Spread such a run evenly over the second it shares: the eye expects even spacing,
    # and every alternative either stacks the cues on one frame or drops one of them.
    times = [seconds for seconds, _ in cues]
    spread = 0
    i = 0
    while i < len(times):
        j = i
        while j + 1 < len(times) and times[j + 1] == times[i]:
            j += 1
        run = j - i + 1
        if run > 1:
            nxt = times[j + 1] if j + 1 < len(times) else total_seconds
            step = (nxt - times[i]) / run
            for k in range(1, run):
                times[i + k] = times[i] + step * k
            spread += run - 1
        i = j + 1
    if spread:
        report.append(
            f"{spread} cue(s) shared a whole second with the one before them and were "
            f"spread evenly across it; the transcript has no finer timing to use"
        )

    starts = [int(round(t * fps)) for t in times]
    # Hold the first image from frame zero rather than opening on a blank. The narration
    # can start a fraction late, and that fraction would otherwise be a black flash.
    if starts and starts[0] > 0:
        report.append(
            f"first cue is at {tc(starts[0], fps)}, holding {cues[0][1].name} from the "
            f"start instead of opening on black"
        )
        starts[0] = 0
    if starts[0] < 0:
        raise SystemExit("first cue is before zero")
    if starts[-1] >= total_frames:
        raise SystemExit(
            f"last cue at {tc(starts[-1], fps)} is past the end of the narration "
            f"({tc(total_frames, fps)}); is this the right audio file?"
        )
    for i in range(1, len(starts)):
        if starts[i] <= starts[i - 1]:
            # Two cues in the same frame: nudge, so no clip is zero frames long.
            starts[i] = starts[i - 1] + 1
    bounds = starts + [total_frames]
    lengths = [bounds[i + 1] - bounds[i] for i in range(len(starts))]

    shortest = min(lengths)
    if shortest < round(fps * 0.5):
        i = lengths.index(shortest)
        report.append(
            f"shortest clip is {shortest} frame(s) at {tc(starts[i], fps)} "
            f"({cues[i][1].name})"
        )

    return Plan(
        [(starts[i], lengths[i], cues[i][1]) for i in range(len(starts))],
        total_frames, fps, audio, report,
    )
