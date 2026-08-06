#!/usr/bin/env python3
"""Read and write YouTube channel data through the official Data API v3.

Five subcommands. Each prints a one-line summary to stdout and a JSON payload
to stderr so the calling skill can pipe either form.

    python3 tools/youtube-api.py stats       <video_id>
    python3 tools/youtube-api.py transcript  <video_id> [-o transcript.md]
    python3 tools/youtube-api.py analytics   <video_id> [-o analytics.csv]
    python3 tools/youtube-api.py upload      <video.mp4> <meta.json> [--dry-run]
    python3 tools/youtube-api.py competitor  <channel_id_or_handle> [-o report.json]

Auth split:
  stats, transcript, competitor -> YOUTUBE_API_KEY from .env
  analytics, upload             -> OAuth refresh token via tools/yt_oauth.py

Exit codes:
  0  success
  1  user error (bad input, missing key)
  2  network or API error (HTTP non-2xx, quota, parse failure)

No third-party deps. Only stdlib + yt_oauth. The Data API v3 base URL is
documented at https://developers.google.com/youtube/v3.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

# Use defusedxml to parse untrusted TTML from YouTube. stdlib's ElementTree is
# vulnerable to XXE and billion-laughs attacks when fed external XML.
try:
    from defusedxml import ElementTree as ET
except ImportError:  # pragma: no cover
    sys.exit(
        "error: defusedxml is required to safely parse caption XML. "
        "Install it with: pip install defusedxml"
    )
from pathlib import Path

# Local import: yt_oauth lives next to this file in tools/.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import yt_oauth  # noqa: E402

DATA_API = "https://www.googleapis.com/youtube/v3"
ANALYTICS_API = "https://youtubeanalytics.googleapis.com/v2"
UPLOAD_API = "https://www.googleapis.com/upload/youtube/v3"
ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
NS = {"atom": "http://www.w3.org/2005/Atom"}


# ---------- shared helpers -------------------------------------------------- #


def load_dotenv() -> Path | None:
    """Same loader as yt_oauth.load_dotenv, duplicated so this tool runs standalone."""
    for folder in (Path.cwd(), *Path(__file__).resolve().parents):
        path = folder / ".env"
        if not path.is_file():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip().removeprefix("export ").strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip("\"'")
            if key and value:
                os.environ.setdefault(key, value)
        return path
    return None


def require_key(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        sys.exit(
            f"error: {name} missing from .env and the environment. "
            "See .agents/skills/youtube/SKILL.md for setup."
        )
    return value


def iso8601_duration_to_seconds(raw: str) -> int:
    """PT11M30S -> 690. YouTube durations always start with PT and use whole units."""
    if not raw or not raw.startswith("PT"):
        return 0
    m = re.search(r"(\d+)H", raw)
    h = int(m.group(1)) if m else 0
    m = re.search(r"(\d+)M", raw)
    mins = int(m.group(1)) if m else 0
    m = re.search(r"(\d+)S", raw)
    secs = int(m.group(1)) if m else 0
    return h * 3600 + mins * 60 + secs


def format_m_ss(seconds: int) -> str:
    seconds = max(0, int(seconds))
    return f"[{seconds // 60}:{seconds % 60:02d}]"


def http_get_json(url: str, headers: dict | None = None) -> dict:
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:600]
        sys.exit(f"error: GET {url} -> {e.code}: {body}")
    except urllib.error.URLError as e:
        sys.exit(f"error: cannot reach {url}: {e.reason}")


def emit(summary: str, payload: dict) -> None:
    print(summary)
    print(json.dumps(payload, indent=2, ensure_ascii=False), file=sys.stderr)


# ---------- stats ----------------------------------------------------------- #


def cmd_stats(args: argparse.Namespace) -> int:
    if not ID_RE.match(args.video_id):
        sys.exit(f"error: '{args.video_id}' is not an 11-character video id")
    api_key = require_key("YOUTUBE_API_KEY")

    url = (
        f"{DATA_API}/videos?part=snippet,statistics,contentDetails,status"
        f"&id={urllib.parse.quote(args.video_id)}&key={api_key}"
    )
    data = http_get_json(url)
    items = data.get("items") or []
    if not items:
        sys.exit(f"error: no video found for id {args.video_id}")

    item = items[0]
    snippet = item.get("snippet", {})
    stats = item.get("statistics", {})
    content = item.get("contentDetails", {})
    status = item.get("status", {})

    payload = {
        "video_id": args.video_id,
        "title": snippet.get("title", ""),
        "channel_id": snippet.get("channelId", ""),
        "channel_title": snippet.get("channelTitle", ""),
        "published_at": snippet.get("publishedAt", ""),
        "duration_seconds": iso8601_duration_to_seconds(content.get("duration", "")),
        "duration_raw": content.get("duration", ""),
        "view_count": int(stats.get("viewCount", 0)),
        "like_count": int(stats.get("likeCount", 0)),
        "comment_count": int(stats.get("commentCount", 0)),
        "privacy": status.get("privacyStatus", ""),
        "tags": snippet.get("tags", []),
        "category_id": snippet.get("categoryId", ""),
        "default_audio_language": snippet.get("defaultAudioLanguage", ""),
    }

    emit(
        f"{payload['title']} | {payload['view_count']:,} views | "
        f"{payload['duration_seconds']}s | privacy={payload['privacy']}",
        payload,
    )
    return 0


# ---------- transcript ------------------------------------------------------ #


def cmd_transcript(args: argparse.Namespace) -> int:
    if not ID_RE.match(args.video_id):
        sys.exit(f"error: '{args.video_id}' is not an 11-character video id")
    if not os.environ.get("YOUTUBE_REFRESH_TOKEN"):
        sys.exit(
            "error: transcript requires OAuth. "
            "The captions.download endpoint rejects API keys even for public "
            "videos; set YOUTUBE_REFRESH_TOKEN in .env."
        )
    access_token = yt_oauth.get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}

    # Step 1: captions.list. OAuth works for both the user's own videos and
    # any video whose captions have been published as public.
    url = (
        f"{DATA_API}/captions?part=snippet"
        f"&videoId={urllib.parse.quote(args.video_id)}"
    )
    listing = http_get_json(url, headers=headers)
    tracks = listing.get("items") or []
    if not tracks:
        sys.exit(
            f"error: no caption tracks for {args.video_id}. "
            "Either the owner has not published captions, or this video is "
            "private and the OAuth token does not own it."
        )

    # Prefer human-uploaded captions over auto-generated, English first.
    def track_score(t: dict) -> tuple[int, int]:
        sn = t.get("snippet", {})
        is_auto = 1 if sn.get("trackKind") == "asr" else 0
        is_en = 0 if sn.get("language", "").lower().startswith("en") else 1
        return (is_auto, is_en)

    chosen = sorted(tracks, key=track_score)[0]
    caption_id = chosen["id"]

    # Step 2: captions.download. Always needs OAuth; never accepts an API key.
    download_url = (
        f"{DATA_API}/captions/{urllib.parse.quote(caption_id)}?tfmt=ttml"
    )
    req = urllib.request.Request(download_url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            xml_bytes = resp.read()
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")[:400]
        sys.exit(f"error: caption download failed: {e.code} {body}")

    cues = parse_ttml(xml_bytes)
    if not cues:
        sys.exit("error: caption track downloaded but contained no cues")

    out_path = Path(args.output) if args.output else None
    lines = [
        f"{format_m_ss(start)} {text.strip()}" for start, text in cues
    ]
    text_blob = "\n".join(lines) + "\n"
    if out_path:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(text_blob, encoding="utf-8")

    payload = {
        "video_id": args.video_id,
        "caption_id": caption_id,
        "language": chosen.get("snippet", {}).get("language", ""),
        "track_kind": chosen.get("snippet", {}).get("trackKind", ""),
        "cue_count": len(cues),
        "last_timestamp_seconds": cues[-1][0],
        "written_to": str(out_path) if out_path else None,
    }
    emit(
        f"{payload['cue_count']} cues, last at "
        f"{format_m_ss(payload['last_timestamp_seconds'])}, "
        f"language={payload['language']}, kind={payload['track_kind']}"
        + (f" -> {out_path}" if out_path else ""),
        payload,
    )
    return 0


def parse_ttml(xml_bytes: bytes) -> list[tuple[int, str]]:
    """Return [(start_seconds, text)] from a TTML caption blob."""
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError as e:
        sys.exit(f"error: caption XML could not be parsed: {e}")
    cues: list[tuple[int, str]] = []
    for p in root.iter("{http://www.w3.org/ns/ttml}paragraph"):
        begin = p.attrib.get("begin", "")
        text = "".join(p.itertext()).strip()
        if not text or not begin:
            continue
        start = ttml_time_to_seconds(begin)
        if start is None:
            continue
        cues.append((start, text))
    return sorted(cues, key=lambda c: c[0])


def ttml_time_to_seconds(raw: str) -> int | None:
    """Accept '12.5s', '1m2.5s', '00:01:02.500', '1h2m3s'. Return whole seconds."""
    raw = raw.strip()
    if not raw:
        return None
    # Clock form: HH:MM:SS(.fff)
    if ":" in raw:
        parts = raw.split(":")
        try:
            parts_f = [float(p) for p in parts]
        except ValueError:
            return None
        while len(parts_f) < 3:
            parts_f.insert(0, 0.0)
        h, m, s = parts_f
        return int(h * 3600 + m * 60 + s)
    # Offset form
    h = m = s = 0.0
    for num, unit in re.findall(r"([0-9]+(?:\.[0-9]+)?)(h|m|s)", raw):
        v = float(num)
        if unit == "h":
            h = v
        elif unit == "m":
            m = v
        elif unit == "s":
            s = v
    return int(h * 3600 + m * 60 + s)


# ---------- analytics ------------------------------------------------------- #


def cmd_analytics(args: argparse.Namespace) -> int:
    if not ID_RE.match(args.video_id):
        sys.exit(f"error: '{args.video_id}' is not an 11-character video id")
    if not os.environ.get("YOUTUBE_REFRESH_TOKEN"):
        sys.exit(
            "error: analytics requires OAuth. "
            "Set YOUTUBE_REFRESH_TOKEN in .env (see SKILL.md)."
        )
    if not os.environ.get("YOUTUBE_CHANNEL_ID"):
        sys.exit(
            "error: YOUTUBE_CHANNEL_ID missing from .env. "
            "Add it before running analytics."
        )

    access_token = yt_oauth.get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    # YouTube Analytics expects startDate/endDate and filters as query params.
    # day-level granularity is the most useful default.
    end = args.end_date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    start = args.start_date or "2005-02-01"  # earliest possible YouTube launch day
    params = urllib.parse.urlencode(
        {
            "ids": f"channel=={os.environ['YOUTUBE_CHANNEL_ID']}",
            "startDate": start,
            "endDate": end,
            "metrics": ",".join(
                [
                    "views",
                    "impressions",
                    "impressionClickThroughRate",
                    "averageViewDuration",
                    "averageViewPercentage",
                ]
            ),
            "dimensions": "day",
            "filters": f"video=={args.video_id}",
            "sort": "day",
        }
    )
    url = f"{ANALYTICS_API}/reports?{params}"
    data = http_get_json(url, headers=headers)

    column_headers = data.get("columnHeaders", [])
    rows = data.get("rows", [])
    out_path = Path(args.output) if args.output else None
    if out_path:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with out_path.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.writer(fh)
            writer.writerow([h["name"] for h in column_headers])
            writer.writerows(rows)

    payload = {
        "video_id": args.video_id,
        "start_date": start,
        "end_date": end,
        "row_count": len(rows),
        "columns": [h["name"] for h in column_headers],
        "written_to": str(out_path) if out_path else None,
    }
    emit(
        f"{payload['row_count']} days of analytics for {args.video_id}, "
        f"{start} -> {end}"
        + (f" -> {out_path}" if out_path else ""),
        payload,
    )
    return 0


# ---------- upload --------------------------------------------------------- #


def cmd_upload(args: argparse.Namespace) -> int:
    if not os.environ.get("YOUTUBE_REFRESH_TOKEN"):
        sys.exit("error: upload requires OAuth. Set YOUTUBE_REFRESH_TOKEN in .env.")

    video_path = Path(args.video_file)
    if not video_path.is_file():
        sys.exit(f"error: video file not found: {video_path}")
    meta_path = Path(args.meta)
    if not meta_path.is_file():
        sys.exit(f"error: metadata file not found: {meta_path}")
    meta = json.loads(meta_path.read_text(encoding="utf-8"))

    summary = {
        "title": meta.get("title", ""),
        "description": (meta.get("description") or "")[:120],
        "privacy": meta.get("privacyStatus", "private"),
        "tags": meta.get("tags", []),
        "category_id": meta.get("categoryId", "22"),
        "size_bytes": video_path.stat().st_size,
    }

    if args.dry_run:
        emit(
            f"DRY RUN: would upload {video_path} ({summary['size_bytes']:,} bytes) "
            f"as '{summary['title']}' privacy={summary['privacy']}",
            {"dry_run": True, **summary},
        )
        return 0

    # Real upload uses the resumable upload protocol. For simplicity we only
    # print the request and exit 0; a follow-up can wire in google-api-python-client
    # when the user wants the full binary upload pipeline.
    sys.exit(
        "error: live upload not yet wired. Use --dry-run to confirm metadata, "
        "or install google-api-python-client and extend tools/yt_oauth.py to a "
        "google-auth Credentials object."
    )


# ---------- competitor ------------------------------------------------------ #


def cmd_competitor(args: argparse.Namespace) -> int:
    api_key = require_key("YOUTUBE_API_KEY")
    handle = args.channel.lstrip("@")
    channel_id = handle

    # If the user gave a handle, resolve it via channels.list?forHandle.
    if handle.startswith("@") or not ID_RE.match(handle):
        url = (
            f"{DATA_API}/channels?part=id,snippet,statistics"
            f"&forHandle={urllib.parse.quote(handle)}&key={api_key}"
        )
        data = http_get_json(url)
        items = data.get("items") or []
        if not items:
            sys.exit(f"error: channel handle '{handle}' not found")
        channel = items[0]
        channel_id = channel["id"]
        channel_meta = {
            "channel_id": channel_id,
            "title": channel["snippet"]["title"],
            "custom_url": channel["snippet"].get("customUrl", ""),
            "subscriber_count": int(channel["statistics"].get("subscriberCount", 0)),
            "video_count": int(channel["statistics"].get("videoCount", 0)),
            "view_count": int(channel["statistics"].get("viewCount", 0)),
            "published_at": channel["snippet"].get("publishedAt", ""),
        }
    else:
        url = (
            f"{DATA_API}/channels?part=id,snippet,statistics"
            f"&id={urllib.parse.quote(handle)}&key={api_key}"
        )
        data = http_get_json(url)
        items = data.get("items") or []
        if not items:
            sys.exit(f"error: channel id '{handle}' not found")
        channel = items[0]
        channel_meta = {
            "channel_id": channel["id"],
            "title": channel["snippet"]["title"],
            "subscriber_count": int(channel["statistics"].get("subscriberCount", 0)),
            "video_count": int(channel["statistics"].get("videoCount", 0)),
            "view_count": int(channel["statistics"].get("viewCount", 0)),
            "published_at": channel["snippet"].get("publishedAt", ""),
        }

    # Pull the top videos via search.list, ordered by viewCount.
    search_url = (
        f"{DATA_API}/search?part=id&channelId={urllib.parse.quote(channel_id)}"
        f"&order=viewCount&type=video&maxResults=20&key={api_key}"
    )
    search = http_get_json(search_url)
    video_ids = [item["id"]["videoId"] for item in search.get("items", [])]
    if not video_ids:
        sys.exit(f"error: no videos found for channel {channel_id}")

    details_url = (
        f"{DATA_API}/videos?part=snippet,statistics,contentDetails"
        f"&id={','.join(video_ids)}&key={api_key}"
    )
    details = http_get_json(details_url)

    videos = []
    for item in details.get("items", []):
        snippet = item.get("snippet", {})
        stats = item.get("statistics", {})
        videos.append(
            {
                "video_id": item["id"],
                "title": snippet.get("title", ""),
                "published_at": snippet.get("publishedAt", ""),
                "duration_seconds": iso8601_duration_to_seconds(
                    item.get("contentDetails", {}).get("duration", "")
                ),
                "view_count": int(stats.get("viewCount", 0)),
                "like_count": int(stats.get("likeCount", 0)),
            }
        )
    videos.sort(key=lambda v: v["view_count"], reverse=True)

    # Cadence: median days between consecutive uploads.
    cadence_days = None
    timestamps = sorted(
        datetime.fromisoformat(v["published_at"].replace("Z", "+00:00"))
        for v in videos
        if v["published_at"]
    )
    if len(timestamps) >= 2:
        gaps = [
            (timestamps[i] - timestamps[i - 1]).total_seconds() / 86400
            for i in range(1, len(timestamps))
        ]
        gaps.sort()
        cadence_days = round(gaps[len(gaps) // 2], 2)

    payload = {
        "channel": channel_meta,
        "top_videos": videos,
        "median_posting_cadence_days": cadence_days,
        "sampled_window": {
            "first": timestamps[0].isoformat() if timestamps else None,
            "last": timestamps[-1].isoformat() if timestamps else None,
        },
    }

    out_path = Path(args.output) if args.output else None
    if out_path:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    emit(
        f"{channel_meta['title']}: {channel_meta['subscriber_count']:,} subs, "
        f"{channel_meta['video_count']} videos, "
        f"top {len(videos)} pulled, median cadence {cadence_days}d"
        + (f" -> {out_path}" if out_path else ""),
        payload,
    )
    return 0


# ---------- argparse -------------------------------------------------------- #


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Read and write YouTube channel data via the Data API v3.",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_stats = sub.add_parser("stats", help="Video stats: views, likes, duration.")
    p_stats.add_argument("video_id")
    p_stats.set_defaults(func=cmd_stats)

    p_tx = sub.add_parser("transcript", help="Pull official captions as [M:SS].")
    p_tx.add_argument("video_id")
    p_tx.add_argument("-o", "--output", help="Write the transcript to this path.")
    p_tx.set_defaults(func=cmd_transcript)

    p_an = sub.add_parser("analytics", help="Daily analytics CSV (OAuth).")
    p_an.add_argument("video_id")
    p_an.add_argument("-o", "--output", help="Write the analytics CSV here.")
    p_an.add_argument("--start-date", help="YYYY-MM-DD, default 2005-02-01.")
    p_an.add_argument("--end-date", help="YYYY-MM-DD, default today UTC.")
    p_an.set_defaults(func=cmd_analytics)

    p_up = sub.add_parser("upload", help="Upload a finished video (OAuth).")
    p_up.add_argument("video_file", help="Path to the .mp4 file.")
    p_up.add_argument(
        "meta", help="JSON file with title, description, tags, privacy."
    )
    p_up.add_argument(
        "--dry-run", action="store_true", help="Validate metadata, skip upload."
    )
    p_up.set_defaults(func=cmd_upload)

    p_co = sub.add_parser(
        "competitor", help="Pull top videos + cadence for a channel."
    )
    p_co.add_argument(
        "channel", help="Channel id (UC...) or handle (@name)."
    )
    p_co.add_argument("-o", "--output", help="Write the report JSON here.")
    p_co.set_defaults(func=cmd_competitor)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    load_dotenv()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())