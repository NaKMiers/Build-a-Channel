#!/usr/bin/env python3
"""Build a Kdenlive project that cuts the scene images on the transcript's own timestamps.

The scenes folder holds one image per cue, named `[M-SS].jpg`, the Windows-safe form of
the `[M:SS]` stamp in prompts/image-prompts.md. That stamp is itself `to_mss()` of the
transcript's `[MM:SS.SSS]`, so the transcript is the only place the real cut time still
exists. This tool reads it back: every image is placed at the millisecond its own line
starts, and held until the next one, so no image ever has to be dragged by hand.

    python3 tools/kdenlive-build.py projects/13-the-psychology-of-being-poor

Writes `<project>/edit/kdenlive/<slug>.kdenlive`. Open it in Kdenlive and the timeline is
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
import cuts  # noqa: E402
from cuts import tc, tc_frames, image_size  # noqa: E402

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
    # Always "avformat", never "avformat-novalidate". Kdenlive writes novalidate only
    # because it also writes the whole meta.media.* stream description alongside it;
    # novalidate means "do not probe this file, trust those properties". Without them
    # the producer is built blind and the audio track never constructs.
    service = "avformat"
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


class Ids:
    """Sequential `filterN` ids, allocated in document order.

    Kdenlive takes the number off the end of every id it reads, so a descriptive name
    like `f_logo` is not a cosmetic difference, it is a document it refuses to open.
    """

    def __init__(self):
        self.n = 0

    def filter(self):
        self.n += 1
        return f"filter{self.n - 1}"


def track_tractor(tid, total_out, playlists, audio, fps, ids):
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
            '  <filter id="%s">\n' % ids.filter()
            + prop("window", 75, 3)
            + prop("max_gain", "20dB", 3)
            + prop("level", 0, 3)
            + prop("channel_mask", -1, 3)
            + prop("mlt_service", "volume", 3)
            + prop("internal_added", 237, 3)
            + prop("disable", 0, 3)
            + "  </filter>\n"
            + '  <filter id="%s">\n' % ids.filter()
            + prop("channel", -1, 3)
            + prop("mlt_service", "panner", 3)
            + prop("internal_added", 237, 3)
            + prop("start", 0.5, 3)
            + prop("disable", 1, 3)
            + "  </filter>\n"
        )
    xml += " </tractor>\n"
    return xml


def fit_filter(mode, width, height, ids):
    """qtblend that maps the image onto the frame. `contain` needs no filter at all."""
    if mode == "contain":
        return ""
    distort = 1 if mode == "stretch" else 0
    return (
        f'   <filter id="{ids.filter()}">\n'
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
    desc, width, height, fps = PROFILES[args.profile]
    if args.fps:
        fps = args.fps

    cut = cuts.plan(project, fps, args.allow_gaps, args.audio, args.duration)
    report, total_frames, audio = cut.report, cut.total_frames, cut.audio
    starts = [c[0] for c in cut.cuts]
    lengths = [c[1] for c in cut.cuts]
    cues = [(c[0] / fps, c[2]) for c in cut.cuts]

    out_path = Path(args.out) if args.out else project / "edit" / "kdenlive" / f"{project.name}.kdenlive"
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

    ids = Ids()
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
    out.append(track_tractor("tractor0", total_frames - 1, ["playlist0", "playlist1"], True, fps, ids))

    # V1: one producer per scene, each cut to the length its cue earns.
    for i, ((_, path), length) in enumerate(zip(cues, lengths)):
        out.append(image_producer(f"producer{i + 1}", 5 + i, path, length - 1, fps))

    out.append(' <playlist id="playlist2">\n')
    for i, length in enumerate(lengths):
        out.append(
            f'  <entry in="00:00:00.000" out="{tc(length - 1, fps)}" producer="producer{i + 1}">\n'
        )
        out.append(prop("kdenlive:id", 5 + i, 3))
        out.append(fit_filter(args.fit, width, height, ids))
        out.append("  </entry>\n")
    out.append(" </playlist>\n")
    out.append(' <playlist id="playlist3"/>\n')
    out.append(track_tractor("tractor1", total_frames - 1, ["playlist2", "playlist3"], False, fps, ids))

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
        if args.logo_rect:
            x, y, w, h = (int(v) for v in args.logo_rect.split())
        else:
            x, y, w, h = cuts.logo_box(width, height, args.logo_size,
                                       args.logo_right, args.logo_bottom)
        out.append(f'   <filter id="{ids.filter()}">\n')
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
            track_tractor("tractor2", total_frames - 1, ["playlist4", "playlist5"], False, fps, ids)
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
    out.append(f'  <filter id="{ids.filter()}">\n')
    out.append(prop("window", 75, 3))
    out.append(prop("max_gain", "20dB", 3))
    out.append(prop("level", 0, 3))
    out.append(prop("channel_mask", -1, 3))
    out.append(prop("mlt_service", "volume", 3))
    out.append(prop("internal_added", 237, 3))
    out.append(prop("disable", 0, 3))
    out.append("  </filter>\n")
    out.append(f'  <filter id="{ids.filter()}">\n')
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
    out.append(prop("kdenlive:docproperties.binsort", 0))
    out.append(prop("kdenlive:documentnotes"))
    out.append(prop("kdenlive:documentnotesversion", 2))
    out.append(prop("kdenlive:expandedFolders"))
    out.append(prop("kdenlive:extraBins", "project_bin:-1"))
    out.append(prop("kdenlive:binZoom", 4))
    # Without this MLT drops main_bin as an unreferenced producer, and Kdenlive then
    # loads a document with no bin and reports it as a corrupted file it cannot recover.
    out.append(prop("kdenlive:docproperties.rendercategory", ""))
    out.append(prop("kdenlive:docproperties.rendercustomquality", -1))
    out.append(prop("kdenlive:docproperties.renderendguide", -1))
    out.append(prop("kdenlive:docproperties.renderexportaudio", 0))
    out.append(prop("kdenlive:docproperties.renderfullcolorrange", 0))
    out.append(prop("kdenlive:docproperties.rendermode", 0))
    out.append(prop("kdenlive:docproperties.renderplay", 0))
    out.append(prop("kdenlive:docproperties.renderpreview", 0))
    out.append(prop("kdenlive:docproperties.renderprofile", ""))
    out.append(prop("kdenlive:docproperties.renderrescale", 0))
    out.append(prop("kdenlive:docproperties.renderrescaleheight", 720))
    out.append(prop("kdenlive:docproperties.renderrescalewidth", 1280))
    out.append(prop("kdenlive:docproperties.renderspeed", 0))
    out.append(prop("kdenlive:docproperties.renderstartguide", -1))
    out.append(prop("kdenlive:docproperties.renderstemaudio", 0))
    out.append(prop("kdenlive:docproperties.rendertcoverlay", 0))
    out.append(prop("kdenlive:docproperties.rendertctype", -1))
    out.append(prop("kdenlive:docproperties.rendertwopass", 0))
    out.append(prop("kdenlive:docproperties.renderurl", out_path.with_suffix(".mp4").name))
    out.append(prop("xml_retain", 1))
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

    project_tractor = f"tractor{len(tracks) - 1}"
    out.append(
        f' <tractor id="{project_tractor}" in="00:00:00.000" '
        f'out="{tc(total_frames - 1, fps)}">\n'
    )
    out.append(prop("kdenlive:projectTractor", 1))
    out.append(
        f'  <track in="00:00:00.000" out="{tc(total_frames - 1, fps)}" producer="{seq_uuid}"/>\n'
    )
    out.append(" </tractor>\n")
    out.append("</mlt>\n")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("".join(out), encoding="utf-8")

    # A launcher beside the project, so opening the edit is one click rather than a
    # path typed out by hand.
    opener = out_path.parent / "open.sh"
    opener.write_text(
        "#!/usr/bin/env bash\n"
        "# Opens this project in Kdenlive. Generated by tools/kdenlive-build.py.\n"
        "cd \"$(dirname \"$0\")\" || exit 1\n"
        f"project=\"{out_path.name}\"\n"
        "if [ ! -f \"$project\" ]; then\n"
        "  echo \"$project is missing. Rebuild it with /edit.\" >&2; exit 1\n"
        "fi\n"
        "if ! command -v kdenlive >/dev/null 2>&1; then\n"
        "  echo \"Kdenlive is not installed, or not on PATH.\" >&2; exit 1\n"
        "fi\n"
        "# An XML formatter moves a <property> value onto its own line, and MLT then\n"
        "# reads the scene path with the indentation attached, so every clip goes\n"
        "# missing. Catch that here rather than in a dialog listing 290 missing clips.\n"
        "if grep -q 'name=\"resource\">$' \"$project\"; then\n"
        "  echo \"$project has been reformatted and its clip paths are broken.\" >&2\n"
        "  echo \"Something saved it through an XML formatter, VS Code format-on-save\" >&2\n"
        "  echo \"being the usual one. Rebuild it:\" >&2\n"
        "  echo \"  python3 tools/kdenlive-build.py <project> --logo brand/logo.png --force\" >&2\n"
        "  exit 1\n"
        "fi\n"
        "# Detach, so closing the terminal does not close the editor.\n"
        "(setsid kdenlive \"$project\" >/dev/null 2>&1 &) 2>/dev/null \\\n"
        "  || (nohup kdenlive \"$project\" >/dev/null 2>&1 &)\n",
        encoding="utf-8",
    )
    opener.chmod(0o755)

    print(f"{out_path}")
    print(f"  {opener.name} opens it in Kdenlive")
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
    p.add_argument("--out", help="output .kdenlive path (default <project>/edit/kdenlive/<name>.kdenlive)")
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
    p.add_argument("--logo-size", type=float,
                   help="logo width as a fraction of the frame width")
    p.add_argument("--logo-right", type=float,
                   help="gap to the right of the logo, as a fraction of the frame width")
    p.add_argument("--logo-bottom", type=float,
                   help="gap below the logo, as a fraction of the frame height")
    p.add_argument("--logo-rect", help='exact transform, "X Y W H" in project pixels')
    p.add_argument(
        "--allow-gaps", action="store_true",
        help="build even though some cues have no scene image yet",
    )
    p.add_argument("--dry-run", action="store_true", help="print the cut list, write nothing")
    build(p.parse_args())


if __name__ == "__main__":
    main()
