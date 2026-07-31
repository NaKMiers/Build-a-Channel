#!/usr/bin/env python3
"""Extract the distinct visual states of a swipe-file video, then package them.

Three stages, run in order. Nothing here decides what a scene means: the tool finds
candidate frames and flags the suspicious ones, the agent looks at the review sheets and
says which candidates to drop.

    python3 tools/video-frames.py ensure-ffmpeg
    python3 tools/video-frames.py probe VIDEO
    python3 tools/video-frames.py candidates VIDEO --work WORKDIR
    python3 tools/video-frames.py finalize --work WORKDIR --out RESEARCHDIR --drop 10,44
    python3 tools/video-frames.py stats --out RESEARCHDIR --sections "1-30:Hook,31-46:Thesis"

Dependencies: Pillow and a working ffmpeg binary. No numpy, no ffprobe, no OpenCV.
`ensure-ffmpeg` fetches a static build if the system has none.

Output layout, matching the existing research folders:

    RESEARCHDIR/extracted-frames/frame-001_00m00.00s.jpg
    RESEARCHDIR/contact-sheets/contact-sheet-01.jpg
    RESEARCHDIR/frame-index.csv
"""

import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageStat

# ---------------------------------------------------------------------------
# constants that define the artifact shape. Changing one changes every folder.
# ---------------------------------------------------------------------------

DEFAULT_THRESHOLD = 0.02          # ffmpeg scene score. Low on purpose: catch build steps.
DIFF_SIZE = (64, 36)              # grayscale size the frame-to-frame diff is measured on
SHARP_SIZE = (480, 268)           # size the edge-energy (blur) measure is taken on
DUP_FLAG_DIFF = 12.0              # flag for human review at or below this mean abs diff
BLUR_FLAG_COUNT = 8               # how many lowest-edge-energy frames to report

CONTACT_COLS, CONTACT_ROWS = 4, 6
CONTACT_CELL = (400, 225)
CONTACT_LABEL_H = 34
CONTACT_BG = (242, 242, 240)
CONTACT_FG = (20, 20, 20)
CONTACT_QUALITY = 88

REVIEW_COLS, REVIEW_ROWS = 2, 3
REVIEW_CELL = (776, 434)
REVIEW_LABEL_H = 26
REVIEW_BG = (30, 30, 34)
REVIEW_FG = (255, 220, 120)
REVIEW_QUALITY = 88

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "/Library/Fonts/Arial.ttf",
    "C:/Windows/Fonts/arial.ttf",
]
FONT_BOLD_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "C:/Windows/Fonts/arialbd.ttf",
] + FONT_CANDIDATES

FFMPEG_WHEEL = "imageio-ffmpeg"
CACHE_DIR = os.path.expanduser("~/.cache/tossexplains-ffmpeg")


def die(msg, code=2):
    print("ERROR: " + msg, file=sys.stderr)
    sys.exit(code)


def load_font(size, bold=False):
    for path in (FONT_BOLD_CANDIDATES if bold else FONT_CANDIDATES):
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return ImageFont.load_default()


# ---------------------------------------------------------------------------
# ffmpeg discovery
# ---------------------------------------------------------------------------

def find_ffmpeg(explicit=None, required=True):
    """PATH is preferred. Falls back to a cached static build, then the wheel's copy."""
    for cand in (explicit, os.environ.get("FFMPEG")):
        if cand:
            if os.path.isfile(cand) and os.access(cand, os.X_OK):
                return cand
            die("ffmpeg not usable at %r" % cand)
    found = shutil.which("ffmpeg")
    if found:
        return found
    # Only our own cache, written by ensure-ffmpeg. Other cached builds on the machine
    # (Playwright ships one) are trimmed down and cannot decode what YouTube serves.
    cached = []
    if os.path.isdir(CACHE_DIR):
        for dirpath, _dirs, files in os.walk(CACHE_DIR):
            for f in files:
                if not f.startswith("ffmpeg") or f.endswith(".whl"):
                    continue
                p = os.path.join(dirpath, f)
                if os.access(p, os.X_OK):
                    cached.append(p)
    if cached:
        return sorted(cached)[-1]
    if required:
        die("no ffmpeg found. Run: python3 tools/video-frames.py ensure-ffmpeg")
    return None


def cmd_ensure_ffmpeg(args):
    existing = find_ffmpeg(required=False)
    if existing:
        print("ffmpeg already available: %s" % existing)
        return
    cache = args.cache or CACHE_DIR
    os.makedirs(cache, exist_ok=True)
    dl = os.path.join(cache, "wheel")
    os.makedirs(dl, exist_ok=True)
    print("no ffmpeg on PATH, fetching a static build from the %s wheel" % FFMPEG_WHEEL)
    rc = subprocess.call([sys.executable, "-m", "pip", "download", "--no-deps",
                          "-d", dl, FFMPEG_WHEEL])
    if rc != 0:
        die("pip download failed. Install ffmpeg yourself, or pass --ffmpeg <path>.")
    wheels = [os.path.join(dl, f) for f in os.listdir(dl) if f.endswith(".whl")]
    if not wheels:
        die("no wheel downloaded")
    with zipfile.ZipFile(sorted(wheels)[-1]) as z:
        z.extractall(cache)
    binaries = []
    for dirpath, _dirs, files in os.walk(cache):
        for f in files:
            if f.startswith("ffmpeg") and not f.endswith(".whl"):
                binaries.append(os.path.join(dirpath, f))
    if not binaries:
        die("the wheel held no ffmpeg binary")
    binary = sorted(binaries)[-1]
    os.chmod(binary, 0o755)
    out = subprocess.run([binary, "-version"], capture_output=True, text=True)
    print(out.stdout.splitlines()[0] if out.stdout else "(no version output)")
    print("ffmpeg ready: %s" % binary)
    print("Export it for later runs:  export FFMPEG=%s" % binary)


# ---------------------------------------------------------------------------
# probe
# ---------------------------------------------------------------------------

def probe(video, ffmpeg):
    if not os.path.isfile(video):
        die("no such video: %s" % video)
    out = subprocess.run([ffmpeg, "-hide_banner", "-i", video],
                         capture_output=True, text=True).stderr
    info = {"file": video, "size_bytes": os.path.getsize(video)}
    m = re.search(r"Duration: (\d+):(\d\d):(\d\d(?:\.\d+)?)", out)
    if m:
        info["duration"] = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    m = re.search(r"Video: (\w+).*?, (\d+)x(\d+)", out, re.S)
    if m:
        info["codec"] = m.group(1)
        info["width"], info["height"] = int(m.group(2)), int(m.group(3))
    m = re.search(r"(\d+(?:\.\d+)?) fps", out)
    if m:
        info["fps"] = float(m.group(1))
    m = re.search(r"handler_name\s*:\s*(.+)", out)
    if m:
        info["handler_name"] = m.group(1).strip()
    m = re.search(r"encoder\s*:\s*(.+)", out)
    if m:
        info["encoder"] = m.group(1).strip()
    if "duration" not in info or "width" not in info:
        die("ffmpeg could not read a video stream from %s\n%s" % (video, out[-1500:]))
    if "fps" in info:
        info["coded_frames_estimate"] = int(round(info["duration"] * info["fps"]))
    return info


def cmd_probe(args):
    info = probe(args.video, find_ffmpeg(args.ffmpeg))
    print(json.dumps(info, indent=2))


# ---------------------------------------------------------------------------
# candidates
# ---------------------------------------------------------------------------

def ts_label(t):
    return "%02d:%05.2f" % (int(t // 60), t % 60)


def frame_name(n, t):
    return "frame-%03d_%02dm%05.2fs.jpg" % (n, int(t // 60), t % 60)


def measure(path, prev_small):
    """Returns (mean abs diff vs previous frame, edge energy, downsized gray image)."""
    im = Image.open(path).convert("L")
    small = im.resize(DIFF_SIZE, Image.BILINEAR)
    if prev_small is None:
        diff = None
    else:
        diff = ImageStat.Stat(ImageChops.difference(small, prev_small)).mean[0]
    mid = im.resize(SHARP_SIZE, Image.BILINEAR)
    # Edge energy stands in for sharpness. Flat title cards score low too, so this is a
    # hint for the reviewer, never an automatic drop.
    sharp = ImageStat.Stat(mid.filter(ImageFilter.FIND_EDGES)).mean[0]
    return diff, sharp, small


def build_sheets(records, src_dir, out_dir, cols, rows, cell, label_h, bg, fg,
                 quality, label_fn, font, prefix):
    os.makedirs(out_dir, exist_ok=True)
    per = cols * rows
    written = []
    for s in range((len(records) + per - 1) // per):
        chunk = records[s * per:(s + 1) * per]
        n_rows = (len(chunk) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * cell[0], n_rows * (cell[1] + label_h)), bg)
        draw = ImageDraw.Draw(sheet)
        for k, rec in enumerate(chunk):
            cx, cy = k % cols, k // cols
            x, y = cx * cell[0], cy * (cell[1] + label_h)
            pad = 2 if prefix == "sheet" else 0
            im = Image.open(os.path.join(src_dir, rec["file"])).convert("RGB")
            im = im.resize((cell[0] - pad * 2, cell[1] - pad * 2), Image.LANCZOS)
            sheet.paste(im, (x + pad, y + pad))
            draw.text((x + 6 + pad, y + cell[1] + (3 if prefix == "sheet" else 9)),
                      label_fn(rec), fill=fg, font=font)
        path = os.path.join(out_dir, "%s-%02d.jpg" % (prefix, s + 1))
        sheet.save(path, quality=quality)
        written.append((path, chunk[0], chunk[-1]))
    return written


def cmd_candidates(args):
    ffmpeg = find_ffmpeg(args.ffmpeg)
    info = probe(args.video, ffmpeg)
    work = args.work
    cand_dir = os.path.join(work, "cand")
    if os.path.isdir(cand_dir) and os.listdir(cand_dir) and not args.force:
        die("%s already holds candidates. Pass --force to redo the extraction." % cand_dir, 3)
    shutil.rmtree(cand_dir, ignore_errors=True)
    os.makedirs(cand_dir, exist_ok=True)
    log_path = os.path.join(work, "showinfo.log")

    vf = ("select='eq(n\\,0)+gt(scene\\,%s)',showinfo" % args.threshold)
    cmd = [ffmpeg, "-hide_banner", "-nostdin", "-i", args.video,
           "-vf", vf, "-fps_mode", "vfr", "-q:v", "2",
           os.path.join(cand_dir, "cand-%05d.jpg")]
    print("extracting candidates at scene threshold %s ..." % args.threshold)
    with open(log_path, "w") as log:
        rc = subprocess.call(cmd, stdout=subprocess.DEVNULL, stderr=log)
    if rc != 0:
        die("ffmpeg failed, see %s" % log_path)

    times = [float(x) for x in re.findall(r"pts_time:([0-9.]+)",
                                          open(log_path, errors="replace").read())]
    files = sorted(os.listdir(cand_dir))
    if len(times) != len(files):
        die("showinfo listed %d frames but %d files were written" % (len(times), len(files)))
    if not files:
        die("no candidates found. Raise --threshold only if the video is noisy; a still "
            "video is more likely the wrong input file.")

    print("measuring %d candidates ..." % len(files))
    frames, prev = [], None
    for i, (t, f) in enumerate(zip(times, files), start=1):
        diff, sharp, prev = measure(os.path.join(cand_dir, f), prev)
        frames.append({"id": i, "t": round(t, 3), "file": f,
                       "diff": None if diff is None else round(diff, 2),
                       "sharp": round(sharp, 2)})

    font = load_font(18, bold=True)
    sheets = build_sheets(
        frames, cand_dir, os.path.join(work, "review-sheets"),
        REVIEW_COLS, REVIEW_ROWS, REVIEW_CELL, REVIEW_LABEL_H, REVIEW_BG, REVIEW_FG,
        REVIEW_QUALITY,
        lambda r: "c%03d  %s  diff %s  sharp %s" % (r["id"], ts_label(r["t"]),
                                                    r["diff"], r["sharp"]),
        font, "sheet")

    dup_flags = [r for r in frames[1:] if r["diff"] is not None and r["diff"] <= DUP_FLAG_DIFF]
    blur_flags = sorted(frames, key=lambda r: r["sharp"])[:BLUR_FLAG_COUNT]
    state = {"video": os.path.abspath(args.video), "probe": info,
             "threshold": args.threshold, "frames": frames}
    with open(os.path.join(work, "candidates.json"), "w") as fh:
        json.dump(state, fh, indent=1)

    gaps = [b["t"] - a["t"] for a, b in zip(frames, frames[1:])]
    print("")
    print("candidates      : %d" % len(frames))
    print("review sheets   : %d in %s" % (len(sheets), os.path.join(work, "review-sheets")))
    print("state           : %s" % os.path.join(work, "candidates.json"))
    if gaps:
        print("gap mean/median : %.2fs / %.2fs" % (sum(gaps) / len(gaps),
                                                   sorted(gaps)[len(gaps) // 2]))
    print("")
    print("REVIEW THESE BEFORE finalize (low change vs the previous candidate, "
          "diff <= %s):" % DUP_FLAG_DIFF)
    if dup_flags:
        for r in dup_flags:
            print("  c%03d  %s  diff %s" % (r["id"], ts_label(r["t"]), r["diff"]))
    else:
        print("  none")
    print("Lowest edge energy (blur or crossfade suspects; flat title cards score low "
          "too, so look before dropping):")
    for r in blur_flags:
        print("  c%03d  %s  sharp %s" % (r["id"], ts_label(r["t"]), r["sharp"]))
    print("")
    print("Next: read every review sheet, then")
    print("  python3 tools/video-frames.py finalize --work %s --out <researchdir> "
          "--drop <ids>" % work)


# ---------------------------------------------------------------------------
# finalize
# ---------------------------------------------------------------------------

def parse_drop(spec):
    if not spec:
        return set()
    out = set()
    for part in re.split(r"[,\s]+", spec.strip()):
        if not part:
            continue
        m = re.fullmatch(r"c?(\d+)(?:-c?(\d+))?", part)
        if not m:
            die("cannot read --drop item %r. Use ids like 10,44 or a range 10-12." % part)
        lo = int(m.group(1))
        hi = int(m.group(2) or lo)
        out.update(range(lo, hi + 1))
    return out


def cmd_finalize(args):
    state_path = os.path.join(args.work, "candidates.json")
    if not os.path.isfile(state_path):
        die("no candidates.json in %s. Run the candidates stage first." % args.work)
    state = json.load(open(state_path))
    frames = state["frames"]
    cand_dir = os.path.join(args.work, "cand")

    drop = parse_drop(args.drop)
    unknown = sorted(i for i in drop if not any(r["id"] == i for r in frames))
    if unknown:
        die("--drop names candidates that do not exist: %s" % unknown)
    keep = [r for r in frames if r["id"] not in drop]
    if not keep:
        die("--drop would remove every candidate")

    out = args.out
    frames_dir = os.path.join(out, "extracted-frames")
    sheets_dir = os.path.join(out, "contact-sheets")
    for d in (frames_dir, sheets_dir):
        if os.path.isdir(d) and os.listdir(d) and not args.force:
            die("%s is not empty. Pass --force to rebuild it." % d, 3)
    for d in (frames_dir, sheets_dir):
        shutil.rmtree(d, ignore_errors=True)
        os.makedirs(d, exist_ok=True)

    fps = state["probe"].get("fps") or 30.0
    rows = []
    for n, rec in enumerate(keep, start=1):
        name = frame_name(n, rec["t"])
        shutil.copyfile(os.path.join(cand_dir, rec["file"]), os.path.join(frames_dir, name))
        rows.append({"frame": n, "timestamp": ts_label(rec["t"]),
                     "seconds": "%.2f" % rec["t"],
                     "source_video_frame": int(round(rec["t"] * fps)),
                     "file": name, "_t": rec["t"], "_cand": rec["id"]})

    index_path = os.path.join(out, "frame-index.csv")
    with open(index_path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["frame", "timestamp", "seconds",
                                           "source_video_frame", "file"],
                           extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    font = load_font(14)
    sheets = build_sheets(
        rows, frames_dir, sheets_dir,
        CONTACT_COLS, CONTACT_ROWS, CONTACT_CELL, CONTACT_LABEL_H, CONTACT_BG, CONTACT_FG,
        CONTACT_QUALITY,
        lambda r: "FRAME %03d   %s" % (r["frame"], r["timestamp"]),
        font, "contact-sheet")

    print("frames kept     : %d of %d candidates" % (len(keep), len(frames)))
    if drop:
        dropped = [r for r in frames if r["id"] in drop]
        print("dropped         : %s" % ", ".join(
            "c%03d @ %s (diff %s)" % (r["id"], ts_label(r["t"]), r["diff"]) for r in dropped))
    print("extracted-frames: %s" % frames_dir)
    print("contact-sheets  : %d sheets" % len(sheets))
    print("frame-index.csv : %s" % index_path)
    print("")
    print("Contact sheet table for visual-analysis.md:")
    print("")
    print("| Contact sheet | Frame | Timeline |")
    print("| --- | --- | --- |")
    for i, (_path, first, last) in enumerate(sheets, start=1):
        print("| [%02d](contact-sheets/contact-sheet-%02d.jpg) | %03d-%03d | %s-%s |"
              % (i, i, first["frame"], last["frame"], first["timestamp"], last["timestamp"]))
    print("")
    report_stats(rows, state["probe"].get("duration"), args.sections)


# ---------------------------------------------------------------------------
# stats
# ---------------------------------------------------------------------------

def parse_sections(spec):
    if not spec:
        return []
    out = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        m = re.fullmatch(r"(\d+)-(\d+):(.+)", part)
        if not m:
            die("cannot read --sections item %r. Use 1-30:Hook,31-46:Thesis." % part)
        out.append((int(m.group(1)), int(m.group(2)), m.group(3).strip()))
    return out


def report_stats(rows, duration, sections_spec):
    ts = [r["_t"] for r in rows]
    gaps = [b - a for a, b in zip(ts, ts[1:])]
    if not gaps:
        print("only one frame, no pacing to report")
        return
    span = duration or (ts[-1] - ts[0])
    ordered = sorted(gaps)
    print("Pacing:")
    print("  beats                 : %d" % len(ts))
    print("  beats per minute      : %.1f" % (len(ts) / (span / 60.0)))
    print("  mean gap between beats: %.2f" % (sum(gaps) / len(gaps)))
    # Two ways to say seconds per beat. The mean gap ignores the tail after the last
    # beat; duration/beats counts it. Quote one of them in the doc, not both.
    print("  duration / beats      : %.2f" % (span / len(ts)))
    print("  median gap            : %.2f" % ordered[len(ordered) // 2])
    print("  gaps <= 1s            : %d" % sum(1 for g in gaps if g <= 1.0))
    print("  gaps <= 2s            : %d of %d" % (sum(1 for g in gaps if g <= 2.0), len(gaps)))
    print("  gaps >= 4s            : %d" % sum(1 for g in gaps if g >= 4.0))
    print("  beats in first 15s    : %d" % sum(1 for t in ts if t < 15))
    hook = [g for t, g in zip(ts, gaps) if t < 45]
    if hook:
        print("  hook (0-45s)          : %d beats, %.2fs per beat, %.1f per minute"
              % (sum(1 for t in ts if t < 45), sum(hook) / len(hook), 60 * len(hook) / 45.0))
    longest = sorted(zip(gaps, range(1, len(rows))), reverse=True)[:5]
    print("  longest holds         : %s" % ", ".join(
        "%.2fs on frame %03d" % (g, rows[i - 1]["frame"]) for g, i in longest))

    sections = parse_sections(sections_spec)
    if not sections:
        return
    by_frame = {r["frame"]: r for r in rows}
    print("")
    print("| Doan | Frame | Beat moi phut | Giay moi beat |")
    print("| --- | --- | ---: | ---: |")
    for lo, hi, name in sections:
        seg = [by_frame[f]["_t"] for f in range(lo, hi + 1) if f in by_frame]
        if len(seg) < 2:
            print("| %s | %03d-%03d | n/a | n/a |" % (name, lo, hi))
            continue
        sgaps = [b - a for a, b in zip(seg, seg[1:])]
        sspan = seg[-1] - seg[0]
        print("| %s | %03d-%03d | %.1f | %.2f |"
              % (name, lo, hi, 60 * len(sgaps) / sspan if sspan else 0,
                 sum(sgaps) / len(sgaps)))


def cmd_stats(args):
    index_path = os.path.join(args.out, "frame-index.csv")
    if not os.path.isfile(index_path):
        die("no frame-index.csv in %s" % args.out)
    rows = []
    for r in csv.DictReader(open(index_path)):
        r["frame"] = int(r["frame"])
        r["_t"] = float(r["seconds"])
        rows.append(r)
    report_stats(rows, args.duration, args.sections)


# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("ensure-ffmpeg", help="find or fetch a usable ffmpeg binary")
    a.add_argument("--cache", help="where to unpack a fetched build (default %s)" % CACHE_DIR)
    a.set_defaults(func=cmd_ensure_ffmpeg)

    a = sub.add_parser("probe", help="print duration, resolution, fps, container metadata")
    a.add_argument("video")
    a.add_argument("--ffmpeg")
    a.set_defaults(func=cmd_probe)

    a = sub.add_parser("candidates", help="extract candidate frames and review sheets")
    a.add_argument("video")
    a.add_argument("--work", required=True, help="scratch directory, not the repo")
    a.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD)
    a.add_argument("--ffmpeg")
    a.add_argument("--force", action="store_true", help="redo an existing extraction")
    a.set_defaults(func=cmd_candidates)

    a = sub.add_parser("finalize", help="write extracted-frames, frame-index.csv, sheets")
    a.add_argument("--work", required=True)
    a.add_argument("--out", required=True, help="research/videos-swipe/<slug>")
    a.add_argument("--drop", help="candidate ids to discard, e.g. 10,44 or 10-12")
    a.add_argument("--sections", help='pacing table, e.g. "1-30:Hook,31-46:Luan de"')
    a.add_argument("--force", action="store_true", help="rebuild a non-empty output")
    a.set_defaults(func=cmd_finalize)

    a = sub.add_parser("stats", help="recompute pacing from an existing frame-index.csv")
    a.add_argument("--out", required=True)
    a.add_argument("--sections")
    a.add_argument("--duration", type=float, help="video duration in seconds")
    a.set_defaults(func=cmd_stats)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
