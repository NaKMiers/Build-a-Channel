#!/usr/bin/env python3
"""Pull a weekly snapshot of TossExplains analytics.

Reads YOUTUBE_API_KEY, YOUTUBE_REFRESH_TOKEN, YOUTUBE_CHANNEL_ID from .env
the same way tools/youtube-api.py does. Pulls Data API stats and Analytics
totals per video, then writes one CSV row per video.

Output: outputs/snapshot-YYYY-MM-DD.csv at the repo root.

This is intentionally read-only. It never edits project files. Run it from
the repo root once a week, then commit the snapshot if you want history.
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

# Allow this script to import yt_oauth from tools/ when invoked as a file.
TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))

import yt_oauth  # noqa: E402

DATA_API = "https://www.googleapis.com/youtube/v3"
ANALYTICS_API = "https://youtubeanalytics.googleapis.com/v2"


def load_dotenv() -> None:
    for folder in (Path.cwd(), *Path(__file__).resolve().parents):
        env = folder / ".env"
        if not env.is_file():
            continue
        for line in env.read_text(encoding="utf-8").splitlines():
            line = line.strip().removeprefix("export ").strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip("\"'")
            if key and value:
                os.environ.setdefault(key, value)
        return


def http_get_json(url: str, headers: dict | None = None) -> dict:
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode("utf-8"))


def list_channel_videos(api_key: str, channel_id: str) -> list[dict]:
    """Use search.list scoped to the channel, then videos.list for stats."""
    params = urllib.parse.urlencode(
        {
            "key": api_key,
            "channelId": channel_id,
            "part": "id",
            "maxResults": "50",
            "order": "date",
            "type": "video",
        }
    )
    search = http_get_json(f"{DATA_API}/search?{params}")
    ids = [item["id"]["videoId"] for item in search.get("items", [])]
    if not ids:
        return []
    params = urllib.parse.urlencode(
        {
            "key": api_key,
            "id": ",".join(ids),
            "part": "snippet,statistics,contentDetails,status",
        }
    )
    videos = http_get_json(f"{DATA_API}/videos?{params}")
    return videos.get("items", [])


def analytics_per_video(channel_id: str, access_token: str, video_id: str) -> dict:
    """Per-video lifetime totals. Quirk: the project API rejects the
    `impressions` metric on this GCP project, so we pull only the metrics
    that actually return, as documented in `.agents/skills/youtube/references/memory.md`.
    """
    metrics = [
        "views",
        "comments",
        "likes",
        "dislikes",
        "shares",
        "averageViewDuration",
        "averageViewPercentage",
    ]
    params = urllib.parse.urlencode(
        {
            "ids": f"channel=={channel_id}",
            "startDate": "2005-02-01",
            "endDate": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d"),
            "metrics": ",".join(metrics),
            "filters": f"video=={video_id}",
        }
    )
    url = f"{ANALYTICS_API}/reports?{params}"
    req = urllib.request.Request(
        url, headers={"Authorization": f"Bearer {access_token}"}
    )
    try:
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return {"error": body[:200]}
    rows = data.get("rows", [])
    if not rows:
        return {m: 0 for m in metrics}
    cols = [h["name"] for h in data["columnHeaders"]]
    return dict(zip(cols, rows[0]))


def traffic_source_per_video(
    channel_id: str, access_token: str, video_id: str
) -> dict:
    """Per-video views broken down by traffic source. Optional best-effort."""
    params = urllib.parse.urlencode(
        {
            "ids": f"channel=={channel_id}",
            "startDate": "2005-02-01",
            "endDate": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d"),
            "metrics": "views",
            "dimensions": "insightTrafficSourceType",
            "filters": f"video=={video_id}",
        }
    )
    url = f"{ANALYTICS_API}/reports?{params}"
    req = urllib.request.Request(
        url, headers={"Authorization": f"Bearer {access_token}"}
    )
    try:
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError:
        return {}
    out = {}
    for row in data.get("rows", []):
        source, views = row[0], row[1]
        out[source] = views
    return out


def iso8601_to_seconds(raw: str) -> int:
    if not raw or not raw.startswith("PT"):
        return 0
    secs = 0
    import re
    h = re.search(r"(\d+)H", raw)
    m = re.search(r"(\d+)M", raw)
    s = re.search(r"(\d+)S", raw)
    if h:
        secs += int(h.group(1)) * 3600
    if m:
        secs += int(m.group(1)) * 60
    if s:
        secs += int(s.group(1))
    return secs


def main() -> int:
    load_dotenv()
    api_key = os.environ.get("YOUTUBE_API_KEY")
    refresh_token = os.environ.get("YOUTUBE_REFRESH_TOKEN")
    channel_id = os.environ.get("YOUTUBE_CHANNEL_ID")
    if not api_key:
        sys.exit("error: YOUTUBE_API_KEY missing from .env")
    if not refresh_token:
        sys.exit("error: YOUTUBE_REFRESH_TOKEN missing from .env")
    if not channel_id:
        sys.exit("error: YOUTUBE_CHANNEL_ID missing from .env")

    videos = list_channel_videos(api_key, channel_id)
    access_token = yt_oauth.get_access_token()

    today = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    out_dir = Path("outputs")
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / f"snapshot-{today}.csv"

    fieldnames = [
        "date",
        "video_id",
        "title",
        "published_at",
        "age_days",
        "duration_seconds",
        "duration_raw",
        "data_views",
        "data_likes",
        "data_dislikes",
        "data_comments",
        "privacy",
        "ana_views",
        "ana_likes",
        "ana_dislikes",
        "ana_comments",
        "ana_shares",
        "ana_avg_duration",
        "ana_avg_view_pct",
        "src_subscribers",
        "src_related",
        "src_channel",
        "src_search",
        "src_other_page",
        "src_external",
        "src_unknown",
        "src_playlist",
    ]

    now = dt.datetime.now(dt.timezone.utc)
    rows = []
    for v in videos:
        vid = v["id"]
        snip = v["snippet"]
        stats = v.get("statistics", {})
        content = v.get("contentDetails", {})
        status = v.get("status", {})
        try:
            ana = analytics_per_video(channel_id, access_token, vid)
        except Exception as e:  # noqa: BLE001
            ana = {"error": str(e)[:200]}
        try:
            src = traffic_source_per_video(channel_id, access_token, vid)
        except Exception as e:  # noqa: BLE001
            src = {}

        published = snip.get("publishedAt", "")
        try:
            pub_dt = dt.datetime.fromisoformat(published.replace("Z", "+00:00"))
            age = (now - pub_dt).days
        except ValueError:
            age = -1

        rows.append(
            {
                "date": today,
                "video_id": vid,
                "title": snip.get("title", ""),
                "published_at": published,
                "age_days": age,
                "duration_seconds": iso8601_to_seconds(content.get("duration", "")),
                "duration_raw": content.get("duration", ""),
                "data_views": int(stats.get("viewCount", 0)),
                "data_likes": int(stats.get("likeCount", 0)),
                "data_dislikes": stats.get("dislikeCount", ""),
                "data_comments": int(stats.get("commentCount", 0)),
                "privacy": status.get("privacyStatus", ""),
                "ana_views": ana.get("views", 0),
                "ana_likes": ana.get("likes", 0),
                "ana_dislikes": ana.get("dislikes", 0),
                "ana_comments": ana.get("comments", 0),
                "ana_shares": ana.get("shares", 0),
                "ana_avg_duration": ana.get("averageViewDuration", 0),
                "ana_avg_view_pct": ana.get("averageViewPercentage", 0),
                "src_subscribers": src.get("SUBSCRIBER", 0),
                "src_related": src.get("RELATED_VIDEO", 0),
                "src_channel": src.get("YT_CHANNEL", 0),
                "src_search": src.get("YT_SEARCH", 0),
                "src_other_page": src.get("YT_OTHER_PAGE", 0),
                "src_external": src.get("EXT_URL", 0),
                "src_unknown": src.get("NO_LINK_OTHER", 0),
                "src_playlist": src.get("PLAYLIST", 0),
            }
        )

    with out_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"snapshot saved: {out_path}  ({len(rows)} videos)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
