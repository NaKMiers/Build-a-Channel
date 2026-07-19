#!/usr/bin/env python3
"""
Collect YouTube Data API v3 data for a channel into JSON + CSV for analysis.

Zero third-party deps (stdlib urllib only).

Usage:
    YOUTUBE_API_KEY=xxx python3 yt_collect.py --channel-id UCxxxx --out DIR
    YOUTUBE_API_KEY=xxx python3 yt_collect.py --handle @Simplewaysoflife --out DIR

Outputs (in --out):
    channel.json          full channel resource
    videos.json           list of every video with snippet+stats+contentDetails
    videos.csv            flat table for quick analysis / spreadsheets
    summary.md            human-readable top-lines
"""
import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

API = "https://www.googleapis.com/youtube/v3"


def get(path, params, key):
    params = {**params, "key": key}
    url = f"{API}/{path}?{urllib.parse.urlencode(params)}"
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")
            if e.code in (403, 429) and attempt < 3:
                time.sleep(2 * (attempt + 1))
                continue
            print(f"HTTP {e.code} on {path}: {body}", file=sys.stderr)
            raise
    raise RuntimeError("unreachable")


def resolve_channel_id(handle, key):
    handle = handle.lstrip("@")
    # forHandle is the modern, exact resolver
    data = get("channels", {"part": "id", "forHandle": handle}, key)
    items = data.get("items", [])
    if items:
        return items[0]["id"]
    # fallback: search
    data = get("search", {"part": "snippet", "q": handle, "type": "channel", "maxResults": 1}, key)
    items = data.get("items", [])
    if items:
        return items[0]["snippet"]["channelId"]
    raise SystemExit(f"Could not resolve channel for handle @{handle}")


def iso8601_dur_to_sec(d):
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", d or "")
    if not m:
        return 0
    h, mn, s = (int(x) if x else 0 for x in m.groups())
    return h * 3600 + mn * 60 + s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel-id")
    ap.add_argument("--handle")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    key = os.environ.get("YOUTUBE_API_KEY")
    if not key:
        raise SystemExit("Set YOUTUBE_API_KEY env var")

    os.makedirs(args.out, exist_ok=True)

    cid = args.channel_id
    if not cid:
        if not args.handle:
            raise SystemExit("Provide --channel-id or --handle")
        cid = resolve_channel_id(args.handle, key)
        print(f"Resolved channel id: {cid}")

    # 1) channel
    ch = get(
        "channels",
        {"part": "snippet,statistics,contentDetails,topicDetails,brandingSettings", "id": cid},
        key,
    )
    if not ch.get("items"):
        raise SystemExit(f"No channel found for id {cid}")
    channel = ch["items"][0]
    with open(os.path.join(args.out, "channel.json"), "w") as f:
        json.dump(channel, f, ensure_ascii=False, indent=2)
    uploads = channel["contentDetails"]["relatedPlaylists"]["uploads"]
    print(f"Channel: {channel['snippet']['title']} | subs "
          f"{channel['statistics'].get('subscriberCount')} | "
          f"videos {channel['statistics'].get('videoCount')}")

    # 2) all upload video ids via playlistItems
    vids = []
    page = None
    while True:
        params = {"part": "contentDetails", "playlistId": uploads, "maxResults": 50}
        if page:
            params["pageToken"] = page
        data = get("playlistItems", params, key)
        vids += [it["contentDetails"]["videoId"] for it in data.get("items", [])]
        page = data.get("nextPageToken")
        if not page:
            break
    print(f"Found {len(vids)} uploaded video ids")

    # 3) batch video details (50 per call)
    videos = []
    for i in range(0, len(vids), 50):
        chunk = vids[i:i + 50]
        data = get(
            "videos",
            {"part": "snippet,statistics,contentDetails,status", "id": ",".join(chunk)},
            key,
        )
        videos += data.get("items", [])
    print(f"Fetched details for {len(videos)} videos")

    with open(os.path.join(args.out, "videos.json"), "w") as f:
        json.dump(videos, f, ensure_ascii=False, indent=2)

    # 4) flat CSV
    rows = []
    for v in videos:
        sn = v.get("snippet", {})
        st = v.get("statistics", {})
        cd = v.get("contentDetails", {})
        dur = iso8601_dur_to_sec(cd.get("duration"))
        views = int(st.get("viewCount", 0) or 0)
        likes = int(st.get("likeCount", 0) or 0)
        comments = int(st.get("commentCount", 0) or 0)
        rows.append({
            "video_id": v["id"],
            "published_at": sn.get("publishedAt", ""),
            "title": sn.get("title", ""),
            "duration_sec": dur,
            "is_short": 1 if dur <= 60 else 0,
            "views": views,
            "likes": likes,
            "comments": comments,
            "like_rate_pct": round(100 * likes / views, 3) if views else 0,
            "comment_rate_pct": round(100 * comments / views, 3) if views else 0,
            "tags": "|".join(sn.get("tags", []) or []),
            "url": f"https://youtu.be/{v['id']}",
        })
    rows.sort(key=lambda r: r["views"], reverse=True)
    cols = list(rows[0].keys()) if rows else []
    with open(os.path.join(args.out, "videos.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)

    # 5) summary.md
    total_views = sum(r["views"] for r in rows)
    top = rows[:10]
    with open(os.path.join(args.out, "summary.md"), "w") as f:
        f.write(f"# {channel['snippet']['title']} - data snapshot\n\n")
        f.write(f"- Channel id: `{cid}`\n")
        f.write(f"- Subscribers: {channel['statistics'].get('subscriberCount')}\n")
        f.write(f"- Total videos (API): {len(videos)}\n")
        f.write(f"- Lifetime views (channel stat): {channel['statistics'].get('viewCount')}\n")
        f.write(f"- Sum of per-video views: {total_views:,}\n\n")
        f.write("## Top 10 videos by views\n\n")
        f.write("| Views | Published | Dur(s) | Short | Title |\n")
        f.write("|---:|---|---:|:---:|---|\n")
        for r in top:
            f.write(f"| {r['views']:,} | {r['published_at'][:10]} | "
                    f"{r['duration_sec']} | {'Y' if r['is_short'] else ''} | "
                    f"{r['title'].replace('|','/')} |\n")

    print(f"Wrote channel.json, videos.json, videos.csv, summary.md to {args.out}")


if __name__ == "__main__":
    main()
