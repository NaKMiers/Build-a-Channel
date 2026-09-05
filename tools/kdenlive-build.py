#!/usr/bin/env python3
"""Build a Kdenlive project that cuts the scene images on the transcript's own timestamps.

The scenes folder holds one image per cue, named `[M-SS].jpg`, the Windows-safe form of
the `[M:SS]` stamp in prompts/image-prompts.md. That stamp is itself `to_mss()` of the
transcript's `[MM:SS.SSS]`, so the transcript is the only place the real cut time still
exists. This tool reads it back: every image is placed at the millisecond its own line
starts, and held until the next one, so no image ever has to be dragged by hand.

    python3 tools/kdenlive-build.py projects/13-the-psychology-of-being-poor

Writes `<project>/edit/<slug>.kdenlive`. Open it in Kdenlive and the timeline is
already cut: audio on A1, scenes on V1, an optional logo on V2.

A legacy whole-second transcript (`[0:03]`) still works, it just cuts on the second.
With no transcript at all the file names themselves are the timeline.
"""

import argparse
import json
import re
import sys
import time
import uuid
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))
import tsfmt  # noqa: E402

MLT_VERSION = "7.38.0"
KDENLIVE_VERSION = "26.04.3"
DOC_VERSION = "1.1"

# Scene image file names: the `[M:SS]` prompt stamp with the colon swapped for a hyphen.
SCENE_RE = re.compile(r"^\[(\d+)-(\d{2})\]$")
IMAGE_EXTS = (".jpg", ".jpeg", ".png", ".webp")

PROFILES = {
    "qhd_1440p_30": ("2.5K QHD 1440p 30 fps", 2560, 1440, 30),
    "atsc_1080p_30": ("HD 1080p 30 fps", 1920, 1080, 30),
    "atsc_1080p_60": ("HD 1080p 60 fps", 1920, 1080, 60),
    "atsc_720p_30": ("HD 720p 30 fps", 1280, 720, 30),
    "uhd_2160p_30": ("UHD 2160p 30 fps", 3840, 2160, 30),
}


# --------------------------------------------------------------------------- timecode


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


def build_cues(project, images, report):
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

    cues = []
    used = set()
    missing = []
    for seconds, key in lines:
        if key in used:
            # Two lines truncating into the same second share one image; it is already
            # on screen, so the second line is not a cut.
            continue
        path = images.get(key)
        if path is None:
            missing.append(key)
            continue
        used.add(key)
        cues.append((seconds, path))

    extra = [k for k in images if k not in used]
    if missing:
        report.append(
            f"{len(missing)} transcript cue(s) have no scene image, the previous image "
            f"holds through them: {', '.join(missing[:8])}"
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


def prop(name, value=None, indent=2):
    pad = " " * indent
    if value is None or value == "":
        return f'{pad}<property name="{name}"/>\n'
    return f'{pad}<property name="{name}">{escape(str(value))}</property>\n'


def image_producer(pid, kid, path, out_frames, fps):
    size = image_size(path)
    fmt = {"jpg": 1, "jpeg": 1, "png": 2}.get(path.suffix.lower().lstrip("."))
    xml = f'<producer id="{pid}" in="00:00:00.000" out="{tc(out_frames, fps)}">\n'
    xml += prop("length", tc(out_frames + 1, fps))
    xml += prop("eof", "pause")
    xml += prop("resource", path)
    xml += prop("ttl", 25)
    xml += prop("aspect_ratio", 1)
    xml += prop("meta.media.progressive", 1)
    xml += prop("seekable", 1)
    if fmt:
        xml += prop("format", fmt)
    if size:
        xml += prop("meta.media.width", size[0])
        xml += prop("meta.media.height", size[1])
    xml += prop("mlt_service", "qimage")
    xml += prop("kdenlive:duration", tc_frames(out_frames + 1, fps))
    xml += prop("xml", "was here")
    xml += prop("kdenlive:folderid", -1)
    xml += prop("kdenlive:id", kid)
    xml += prop("kdenlive:control_uuid", "{%s}" % uuid.uuid4())
    xml += prop("kdenlive:clip_type", 2)
    xml += prop("kdenlive:file_size", path.stat().st_size)
    xml += prop("kdenlive:clipname", path.name)
    xml += " </producer>\n"
    return " " + xml


def audio_chain(cid, kid, path, out_frames, fps, control, timeline):
    service = "avformat-novalidate" if timeline else "avformat"
    xml = f' <chain id="{cid}" out="{tc(out_frames, fps)}">\n'
    xml += prop("length", out_frames + 1)
    xml += prop("eof", "pause")
    xml += prop("resource", path)
    xml += prop("mlt_service", service)
    xml += prop("seekable", 1)
    xml += prop("audio_index", 0)
    xml += prop("video_index", -1)
    xml += prop("astream", 0)
    xml += prop("kdenlive:folderid", -1)
    xml += prop("kdenlive:id", kid)
    xml += prop("kdenlive:control_uuid", control)
    xml += prop("kdenlive:clip_type", 1)
    xml += prop("kdenlive:file_size", path.stat().st_size)
    xml += prop("kdenlive:clipname", path.name)
    if timeline:
        xml += prop("xml", "was here")
        xml += prop("mute_on_pause", 0)
        xml += prop("set.test_audio", 0)
        xml += prop("set.test_image", 1)
    xml += " </chain>\n"
    return xml


def track_tractor(tid, total_out, playlists, audio, fps):
    xml = f' <tractor id="{tid}" in="00:00:00.000" out="{tc(total_out, fps)}">\n'
    if audio:
        xml += prop("kdenlive:audio_track", 1)
    xml += prop("kdenlive:trackheight", 72)
    xml += prop("kdenlive:timeline_active", 1)
    xml += prop("kdenlive:collapsed", 0)
    xml += prop("kdenlive:thumbs_format")
    xml += prop("kdenlive:audio_rec")
    hide = "video" if audio else "audio"
    for pl in playlists:
        xml += f'  <track hide="{hide}" producer="{pl}"/>\n'
    if audio:
        xml += (
            '  <filter id="f_vol_%s">\n' % tid
            + prop("window", 75, 3)
            + prop("max_gain", "20dB", 3)
            + prop("level", 0, 3)
            + prop("channel_mask", -1, 3)
            + prop("mlt_service", "volume", 3)
            + prop("internal_added", 237, 3)
            + prop("disable", 0, 3)
            + "  </filter>\n"
            + '  <filter id="f_pan_%s">\n' % tid
            + prop("channel", -1, 3)
            + prop("mlt_service", "panner", 3)
            + prop("internal_added", 237, 3)
            + prop("start", 0.5, 3)
            + prop("disable", 1, 3)
            + "  </filter>\n"
        )
    xml += " </tractor>\n"
    return xml


def fit_filter(mode, width, height, fid):
    """qtblend that maps the image onto the frame. `contain` needs no filter at all."""
    if mode == "contain":
        return ""
    distort = 1 if mode == "stretch" else 0
    return (
        f'   <filter id="{fid}">\n'
        + prop("rotate_center", 1, 4)
        + prop("mlt_service", "qtblend", 4)
        + prop("kdenlive_id", "qtblend", 4)
        + prop("compositing", 0, 4)
        + prop("distort", distort, 4)
        + prop("rect", f"00:00:00.000=0 0 {width} {height} 1.000000", 4)
        + prop("rotation", "00:00:00.000=0", 4)
        + prop("kdenlive:collapsed", 0, 4)
        + "   </filter>\n"
    )


GUIDE_CATEGORIES = json.dumps(
    [
        {"color": c, "comment": f"Category {i + 1}", "index": i}
        for i, c in enumerate(
            ["#9b59b6", "#3daee9", "#1abc9c", "#1cdc9a", "#c9ce3b",
             "#fdbc4b", "#f39c1f", "#f47750", "#da4453"]
        )
    ],
    indent=4,
)


# ------------------------------------------------------------------------------ build


def build(args):
    project = Path(args.project).resolve()
    if not project.is_dir():
        raise SystemExit(f"no such project: {project}")

    scenes_dir = project / "scenes"
    if not scenes_dir.is_dir():
        raise SystemExit(f"no scenes folder in {project.name}, run /scenes first")

    audio = Path(args.audio) if args.audio else project / "audios" / "full.mp3"
    if not audio.exists():
        raise SystemExit(f"no narration at {audio}, run /transcript first")
    audio = audio.resolve()

    desc, width, height, fps = PROFILES[args.profile]
    if args.fps:
        fps = args.fps

    report = []
    images, dupes = scene_files(scenes_dir)
    for key, first, second in dupes:
        report.append(f"{key} has two images, using {first.name}, ignoring {second}")
    if not images:
        raise SystemExit(f"no `[M-SS]` scene images under {scenes_dir}")

    cues = build_cues(project, images, report)
    if not cues:
        raise SystemExit("no scene image matched any transcript cue")

    total_seconds = args.duration or audio_seconds(audio)
    total_frames = int(round(total_seconds * fps))

    # Frame boundaries. Each scene runs until the next one starts; the last runs out
    # the narration, so the video track and the audio track end together.
    starts = [int(round(seconds * fps)) for seconds, _ in cues]
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

    out_path = Path(args.out) if args.out else project / "edit" / f"{project.name}.kdenlive"
    out_path = out_path.resolve()

    # Once this file has been opened in Kdenlive it holds hand work no rebuild can
    # recover, so a rebuild has to be asked for by name.
    if out_path.exists() and not args.force and not args.dry_run:
        raise SystemExit(
            f"{out_path} already exists. Kdenlive edits are not reproducible from the\n"
            f"transcript, so rebuilding would discard them. Pass --force to overwrite, or\n"
            f"--out to write a second file beside it."
        )

    if args.dry_run:
        for (seconds, path), start, length in zip(cues, starts, lengths):
            print(f"{tc(start, fps)}  {length:5d}f  {length / fps:6.2f}s  {path.name}")
        print(f"\n{len(cues)} scenes, {tc(total_frames, fps)} total, {fps} fps")
        for line in report:
            print(f"note: {line}")
        print(f"would write {out_path}")
        return

    seq_uuid = "{%s}" % uuid.uuid4()
    audio_uuid = "{%s}" % uuid.uuid4()
    logo = Path(args.logo).resolve() if args.logo else None
    if logo and not logo.exists():
        raise SystemExit(f"no logo at {logo}")

    out = []
    out.append("<?xml version='1.0' encoding='utf-8'?>\n")
    out.append(
        f'<mlt LC_NUMERIC="C" producer="main_bin" root="{escape(str(out_path.parent))}" '
        f'version="{MLT_VERSION}">\n'
    )
    out.append(
        f' <profile colorspace="709" description="{escape(desc)}" display_aspect_den="9" '
        f'display_aspect_num="16" frame_rate_den="1" frame_rate_num="{fps}" '
        f'height="{height}" progressive="1" sample_aspect_den="1" sample_aspect_num="1" '
        f'width="{width}"/>\n'
    )

    # Black background track.
    out.append(f' <producer id="producer0" in="00:00:00.000" out="{tc(total_frames - 1, fps)}">\n')
    out.append(prop("length", 2147483647))
    out.append(prop("eof", "continue"))
    out.append(prop("resource", "black"))
    out.append(prop("aspect_ratio", 1))
    out.append(prop("mlt_service", "color"))
    out.append(prop("kdenlive:playlistid", "black_track"))
    out.append(prop("mlt_image_format", "rgba"))
    out.append(prop("set.test_audio", 0))
    out.append(" </producer>\n")

    # A1: the narration, one entry running the whole timeline.
    out.append(audio_chain("chain0", 4, audio, total_frames - 1, fps, audio_uuid, True))
    out.append(' <playlist id="playlist0">\n')
    out.append(prop("kdenlive:audio_track", 1))
    out.append(f'  <entry in="00:00:00.000" out="{tc(total_frames - 1, fps)}" producer="chain0">\n')
    out.append(prop("kdenlive:id", 4, 3))
    out.append("  </entry>\n")
    out.append(" </playlist>\n")
    out.append(' <playlist id="playlist1">\n')
    out.append(prop("kdenlive:audio_track", 1))
    out.append(" </playlist>\n")
    out.append(track_tractor("tractor0", total_frames - 1, ["playlist0", "playlist1"], True, fps))

    # V1: one producer per scene, each cut to the length its cue earns.
    for i, ((_, path), length) in enumerate(zip(cues, lengths)):
        out.append(image_producer(f"producer{i + 1}", 5 + i, path, length - 1, fps))

    out.append(' <playlist id="playlist2">\n')
    if starts[0] > 0:
        out.append(f'  <blank length="{tc(starts[0], fps)}"/>\n')
    for i, length in enumerate(lengths):
        out.append(
            f'  <entry in="00:00:00.000" out="{tc(length - 1, fps)}" producer="producer{i + 1}">\n'
        )
        out.append(prop("kdenlive:id", 5 + i, 3))
        out.append(fit_filter(args.fit, width, height, f"f_fit{i}"))
        out.append("  </entry>\n")
    out.append(" </playlist>\n")
    out.append(' <playlist id="playlist3"/>\n')
    out.append(track_tractor("tractor1", total_frames - 1, ["playlist2", "playlist3"], False, fps))

    # V2: the channel logo, held over the whole video.
    logo_kid = 5 + len(cues)
    tracks = ["producer0", "tractor0", "tractor1"]
    if logo:
        out.append(image_producer(f"producer{len(cues) + 1}", logo_kid, logo, total_frames - 1, fps))
        out.append(' <playlist id="playlist4">\n')
        out.append(
            f'  <entry in="00:00:00.000" out="{tc(total_frames - 1, fps)}" '
            f'producer="producer{len(cues) + 1}">\n'
        )
        out.append(prop("kdenlive:id", logo_kid, 3))
        w = round(width * args.logo_size)
        h = w
        x = width - w - round(width * args.logo_margin)
        y = height - h - round(width * args.logo_margin)
        out.append(f'   <filter id="f_logo">\n')
        out.append(prop("rotate_center", 1, 4))
        out.append(prop("mlt_service", "qtblend", 4))
        out.append(prop("kdenlive_id", "qtblend", 4))
        out.append(prop("compositing", 0, 4))
        out.append(prop("distort", 0, 4))
        out.append(prop("rect", f"00:00:00.000={x} {y} {w} {h} 1.000000", 4))
        out.append(prop("rotation", "00:00:00.000=0", 4))
        out.append(prop("kdenlive:collapsed", 0, 4))
        out.append("   </filter>\n")
        out.append("  </entry>\n")
        out.append(" </playlist>\n")
        out.append(' <playlist id="playlist5"/>\n')
        out.append(
            track_tractor("tractor2", total_frames - 1, ["playlist4", "playlist5"], False, fps)
        )
        tracks.append("tractor2")

    # The sequence: the timeline itself, one track per tractor above.
    out.append(f' <tractor id="{seq_uuid}" in="00:00:00.000" out="{tc(total_frames - 1, fps)}">\n')
    out.append(prop("kdenlive:uuid", seq_uuid))
    out.append(prop("kdenlive:clipname", "Sequence 1"))
    out.append(prop("kdenlive:sequenceproperties.hasAudio", 1))
    out.append(prop("kdenlive:sequenceproperties.hasVideo", 1))
    out.append(prop("kdenlive:sequenceproperties.activeTrack", 1))
    out.append(prop("kdenlive:sequenceproperties.tracksCount", len(tracks) - 1))
    out.append(prop("kdenlive:sequenceproperties.documentuuid", seq_uuid))
    out.append(prop("kdenlive:control_uuid", seq_uuid))
    out.append(prop("kdenlive:duration", tc(total_frames, fps)))
    out.append(prop("kdenlive:maxduration", total_frames))
    out.append(prop("kdenlive:producer_type", 17))
    out.append(prop("kdenlive:id", 3))
    out.append(prop("kdenlive:clip_type", 0))
    out.append(prop("kdenlive:file_size", 0))
    out.append(prop("kdenlive:folderid", 2))
    out.append(prop("kdenlive:sequenceproperties.audioTarget", 1))
    out.append(prop("kdenlive:sequenceproperties.videoTarget", 2))
    out.append(prop("kdenlive:sequenceproperties.disablepreview", 0))
    out.append(prop("kdenlive:sequenceproperties.position", 0))
    out.append(prop("kdenlive:sequenceproperties.scrollPos", 0))
    out.append(prop("kdenlive:sequenceproperties.tracks", len(tracks)))
    out.append(prop("kdenlive:sequenceproperties.verticalzoom", 1))
    out.append(prop("kdenlive:sequenceproperties.zonein", 0))
    out.append(prop("kdenlive:sequenceproperties.zoneout", total_frames))
    out.append(prop("kdenlive:sequenceproperties.zoom", 8))
    out.append(prop("kdenlive:sequenceproperties.groups", "[\n]\n"))
    out.append(prop("kdenlive:sequenceproperties.guides", "[\n]\n"))
    for name in tracks:
        out.append(f'  <track producer="{name}"/>\n')
    # Track 1 is the audio, mixed down. Every video track above it composites on black.
    out.append('  <transition id="transition0">\n')
    out.append(prop("a_track", 0, 3))
    out.append(prop("b_track", 1, 3))
    out.append(prop("mlt_service", "mix", 3))
    out.append(prop("kdenlive_id", "mix", 3))
    out.append(prop("internal_added", 237, 3))
    out.append(prop("always_active", 1, 3))
    out.append(prop("accepts_blanks", 1, 3))
    out.append(prop("sum", 1, 3))
    out.append("  </transition>\n")
    for n in range(2, len(tracks)):
        out.append(f'  <transition id="transition{n - 1}">\n')
        out.append(prop("a_track", 0, 3))
        out.append(prop("b_track", n, 3))
        out.append(prop("compositing", 0, 3))
        out.append(prop("distort", 0, 3))
        out.append(prop("rotate_center", 0, 3))
        out.append(prop("mlt_service", "qtblend", 3))
        out.append(prop("kdenlive_id", "qtblend", 3))
        out.append(prop("internal_added", 237, 3))
        out.append(prop("always_active", 1, 3))
        out.append("  </transition>\n")
    out.append('  <filter id="f_seq_vol">\n')
    out.append(prop("window", 75, 3))
    out.append(prop("max_gain", "20dB", 3))
    out.append(prop("level", 0, 3))
    out.append(prop("channel_mask", -1, 3))
    out.append(prop("mlt_service", "volume", 3))
    out.append(prop("internal_added", 237, 3))
    out.append(prop("disable", 0, 3))
    out.append("  </filter>\n")
    out.append('  <filter id="f_seq_pan">\n')
    out.append(prop("channel", -1, 3))
    out.append(prop("mlt_service", "panner", 3))
    out.append(prop("internal_added", 237, 3))
    out.append(prop("start", 0.5, 3))
    out.append(prop("disable", 1, 3))
    out.append("  </filter>\n")
    out.append(" </tractor>\n")

    # The bin. Its copy of the narration is a plain avformat chain.
    out.append(audio_chain("chain1", 4, audio, total_frames - 1, fps, audio_uuid, False))
    out.append(' <playlist id="main_bin">\n')
    out.append(prop("kdenlive:folder.-1.2", "Sequences"))
    out.append(prop("kdenlive:sequenceFolder", 2))
    out.append(prop("kdenlive:docproperties.audioChannels", 2))
    # Kdenlive keys its cache directory on this; it uses milliseconds since the epoch.
    out.append(prop("kdenlive:docproperties.documentid", int(time.time() * 1000)))
    out.append(prop("kdenlive:docproperties.enableTimelineZone", 0))
    out.append(prop("kdenlive:docproperties.enableexternalproxy", 0))
    out.append(prop("kdenlive:docproperties.enableproxy", 0))
    out.append(prop("kdenlive:docproperties.externalproxyparams"))
    out.append(prop("kdenlive:docproperties.generateimageproxy", 0))
    out.append(prop("kdenlive:docproperties.generateproxy", 0))
    out.append(prop("kdenlive:docproperties.guidesCategories", GUIDE_CATEGORIES))
    out.append(prop("kdenlive:docproperties.kdenliveversion", KDENLIVE_VERSION))
    out.append(prop("kdenlive:docproperties.previewextension"))
    out.append(prop("kdenlive:docproperties.previewparameters"))
    out.append(prop("kdenlive:docproperties.profile", args.profile))
    out.append(prop("kdenlive:docproperties.proxyextension"))
    out.append(prop("kdenlive:docproperties.proxyimageminsize", 2000))
    out.append(prop("kdenlive:docproperties.proxyimagesize", 800))
    out.append(prop("kdenlive:docproperties.proxyminsize", 1000))
    out.append(prop("kdenlive:docproperties.proxyparams"))
    out.append(prop("kdenlive:docproperties.proxyresize", 640))
    out.append(prop("kdenlive:docproperties.seekOffset", 30000))
    out.append(prop("kdenlive:docproperties.sessionid", "{%s}" % uuid.uuid4()))
    out.append(prop("kdenlive:docproperties.uuid", seq_uuid))
    out.append(prop("kdenlive:docproperties.version", DOC_VERSION))
    out.append(prop("kdenlive:docproperties.opensequences", seq_uuid))
    out.append(prop("kdenlive:docproperties.activetimeline", seq_uuid))
    out.append(f'  <entry in="00:00:00.000" out="00:00:00.000" producer="{seq_uuid}"/>\n')
    out.append(f'  <entry in="00:00:00.000" out="{tc(total_frames - 1, fps)}" producer="chain1"/>\n')
    for i, length in enumerate(lengths):
        out.append(
            f'  <entry in="00:00:00.000" out="{tc(length - 1, fps)}" producer="producer{i + 1}"/>\n'
        )
    if logo:
        out.append(
            f'  <entry in="00:00:00.000" out="{tc(total_frames - 1, fps)}" '
            f'producer="producer{len(cues) + 1}"/>\n'
        )
    out.append(" </playlist>\n")

    out.append(f' <tractor id="tractor_project" in="00:00:00.000" out="{tc(total_frames - 1, fps)}">\n')
    out.append(prop("kdenlive:projectTractor", 1))
    out.append(
        f'  <track in="00:00:00.000" out="{tc(total_frames - 1, fps)}" producer="{seq_uuid}"/>\n'
    )
    out.append(" </tractor>\n")
    out.append("</mlt>\n")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("".join(out), encoding="utf-8")

    print(f"{out_path}")
    print(
        f"  {len(cues)} scenes on V1, narration on A1"
        + (", logo on V2" if logo else "")
        + f", {tc(total_frames, fps)} at {fps} fps, {width}x{height}"
    )
    for line in report:
        print(f"  note: {line}")


def main():
    p = argparse.ArgumentParser(
        description="Cut a project's scene images onto a Kdenlive timeline at their transcript times."
    )
    p.add_argument("project", help="projects/<n>-<slug>")
    p.add_argument("--out", help="output .kdenlive path (default <project>/edit/<name>.kdenlive)")
    p.add_argument("--force", action="store_true", help="overwrite an existing project file")
    p.add_argument("--audio", help="narration file (default <project>/audios/full.mp3)")
    p.add_argument("--duration", type=float, help="override the narration length, in seconds")
    p.add_argument(
        "--profile", default="qhd_1440p_30", choices=sorted(PROFILES),
        help="kdenlive project profile (default qhd_1440p_30)",
    )
    p.add_argument("--fps", type=int, help="override the profile's frame rate")
    p.add_argument(
        "--fit", default="contain", choices=("contain", "cover", "stretch"),
        help="how a scene image maps onto the frame (default contain, letterboxed)",
    )
    p.add_argument("--logo", help="image to hold on V2 for the whole video")
    p.add_argument("--logo-size", type=float, default=0.04, help="logo width as a fraction of the frame")
    p.add_argument("--logo-margin", type=float, default=0.02, help="logo inset as a fraction of the frame")
    p.add_argument("--dry-run", action="store_true", help="print the cut list, write nothing")
    build(p.parse_args())


if __name__ == "__main__":
    main()
