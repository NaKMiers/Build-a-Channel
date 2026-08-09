#!/usr/bin/env python3
"""Decide whether a local video file really is the YouTube video that was named.

    python3 tools/youtube-verify.py <link-or-id> <video-file>
    python3 tools/youtube-verify.py <link-or-id> <video-file> --expect-duration 696
    python3 tools/youtube-verify.py <link-or-id> <video-file> --offline

Exit codes, meant to be branched on:

    0  VERIFIED      safe to proceed
    3  MISMATCH      the file is a different video, stop
    4  INCONCLUSIVE  cannot tell from what was given, ask the human
    2  ERROR         bad link, dead link, missing file, not a video

The evidence, strongest first:

  1. The 11 character video id appears verbatim in the file name. Every YouTube
     downloader embeds it, and ids are case sensitive, so this is close to proof.
  2. A different id-shaped token appears in the file name instead. That is a mismatch,
     not an unknown.
  3. The real title, fetched from the oEmbed endpoint, matches the file name slug. A
     downloader names its output after the title of the video it actually fetched.
  4. --expect-duration matches the container duration within the tolerance.
  5. Duration agrees but nothing identifies the video. Inconclusive on its own: many
     videos share a length.

## What the network gives, and what it does not

`https://www.youtube.com/oembed` answers without authentication and yields the title, the
channel name, and the thumbnail URL. It also answers 404 or 400 for an id that is not a
public video, which catches a typo or a private link before any frame is extracted.

The duration is **not** available to a script. The watch page carries
`ytInitialPlayerResponse`, but from a datacenter address its `playabilityStatus` comes back
`LOGIN_REQUIRED / "Sign in to confirm you are not a bot"`, so `lengthSeconds` is absent.
Forging a different client to get around that check is not something this tool does. When
the duration is needed, a real browser session reads it, which is the `/browse` skill's job,
and the number arrives here through `--expect-duration`.

## An unverifiable run is an error, not a weaker run

If the lookup cannot be reached, the answer is ERROR and nothing else happens. There is no
silent fallback to the file name, because a run that quietly skipped the one authority on
what the link points at would still print VERIFIED. Verifying without the network has to be
asked for explicitly, with `--offline`, which is also the flag to use when a run must be
reproducible.
"""

import argparse
import json
import os
import re
import subprocess
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request

ID_RE = r"[A-Za-z0-9_-]{11}"
DURATION_TOLERANCE = 2.0   # seconds. Container duration vs the reported length.
CACHE_DIR = os.path.expanduser("~/.cache/humanprice-ffmpeg")
OEMBED = "https://www.youtube.com/oembed"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36")
NET_TIMEOUT = 8.0
# Slug characters a file name must share with the real title before the match alone is
# treated as proof. Lower when a second fact (the duration) agrees.
TITLE_MATCH_ALONE = 20
TITLE_MATCH_WITH_DURATION = 12

VERIFIED, MISMATCH, INCONCLUSIVE, ERROR = 0, 3, 4, 2


def out(verdict, code, reasons, facts):
    print(json.dumps({"verdict": verdict, "reasons": reasons, "facts": facts}, indent=2))
    sys.exit(code)


def parse_video_id(raw):
    """Accepts a bare id or any of the URL shapes YouTube hands out."""
    raw = raw.strip().strip('"').strip("'")
    if re.fullmatch(ID_RE, raw):
        return raw, "bare id"
    patterns = [
        (r"[?&]v=(" + ID_RE + r")", "watch?v="),
        (r"youtu\.be/(" + ID_RE + r")", "youtu.be/"),
        (r"/shorts/(" + ID_RE + r")", "/shorts/"),
        (r"/embed/(" + ID_RE + r")", "/embed/"),
        (r"/live/(" + ID_RE + r")", "/live/"),
        (r"/v/(" + ID_RE + r")", "/v/"),
    ]
    for pat, label in patterns:
        m = re.search(pat, raw)
        if m:
            return m.group(1), label
    return None, None


def find_ffmpeg(explicit=None):
    for cand in (explicit, os.environ.get("FFMPEG")):
        if cand and os.path.isfile(cand) and os.access(cand, os.X_OK):
            return cand
    found = shutil.which("ffmpeg")
    if found:
        return found
    if os.path.isdir(CACHE_DIR):
        hits = []
        for dirpath, _dirs, files in os.walk(CACHE_DIR):
            for f in files:
                if f.startswith("ffmpeg") and not f.endswith(".whl"):
                    p = os.path.join(dirpath, f)
                    if os.access(p, os.X_OK):
                        hits.append(p)
        if hits:
            return sorted(hits)[-1]
    return None


def probe(video, ffmpeg):
    text = subprocess.run([ffmpeg, "-hide_banner", "-i", video],
                          capture_output=True, text=True).stderr
    facts = {}
    m = re.search(r"Duration: (\d+):(\d\d):(\d\d(?:\.\d+)?)", text)
    if m:
        facts["duration"] = round(int(m.group(1)) * 3600 + int(m.group(2)) * 60
                                 + float(m.group(3)), 2)
    m = re.search(r"Video: (\w+).*?, (\d+)x(\d+)", text, re.S)
    if m:
        facts["codec"], facts["width"], facts["height"] = m.group(1), int(m.group(2)), int(m.group(3))
    m = re.search(r"handler_name\s*:\s*(.+)", text)
    if m:
        facts["handler_name"] = m.group(1).strip()
    m = re.search(r"encoder\s*:\s*(.+)", text)
    if m:
        facts["encoder"] = m.group(1).strip()
    return facts


ID_DELIMS = set("_-.[](){} ")


def id_like_tokens(name):
    """Every delimited 11 character run that has the character mix a real id has.

    Scanned position by position rather than with one regex, because a regex that eats
    its delimiters hides the second match: in `..._Media_SD7XyG2wd1k_001...` a match on
    `_Media_` consumes the underscore the real id needs.

    A digit plus both letter cases is the filter. Title words reach 11 characters often
    ("Did-Ancient") but rarely carry a digit. An id with no digit is missed, which lands
    on INCONCLUSIVE and asks a human, and that is the safe way to be wrong.
    """
    stem = os.path.splitext(name)[0]
    out = []
    for i in range(len(stem) - 10):
        before = stem[i - 1] if i > 0 else None
        after = stem[i + 11] if i + 11 < len(stem) else None
        if before is not None and before not in ID_DELIMS:
            continue
        if after is not None and after not in ID_DELIMS:
            continue
        token = stem[i:i + 11]
        if not re.fullmatch(ID_RE, token):
            continue
        if (re.search(r"[0-9]", token) and re.search(r"[A-Z]", token)
                and re.search(r"[a-z]", token)):
            out.append(token)
    return out


def slugify(text):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", text.lower())).strip("-")


def title_matches_filename(title, filename, min_chars):
    """YouTube downloaders truncate the title, so compare on a shared prefix."""
    a = slugify(title)
    b = slugify(os.path.splitext(os.path.basename(filename))[0])
    if not a or not b:
        return False, 0
    # Longest common prefix measured in slug characters.
    n = 0
    while n < min(len(a), len(b)) and a[n] == b[n]:
        n += 1
    trimmed_a = a[:n].rstrip("-")
    return (len(trimmed_a) >= min_chars or trimmed_a == a), len(trimmed_a)


def looks_title_derived(filename):
    """Three or more word-ish runs means a downloader named this after some title."""
    stem = os.path.splitext(os.path.basename(filename))[0]
    words = [w for w in re.split(r"[^A-Za-z]+", stem) if len(w) >= 3]
    return len(words) >= 3


def fetch_oembed(video_id, timeout):
    """Returns (status, data). status is ok, not_found, bad_request, or unreachable.

    oEmbed needs no key and is not behind the bot check that hides the watch page's
    player response. 404 and 400 mean the id is not a public video.
    """
    url = "%s?%s" % (OEMBED, urllib.parse.urlencode({
        "url": "https://www.youtube.com/watch?v=" + video_id, "format": "json"}))
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept-Language": "en-US,en;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return "ok", json.loads(resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return "not_found", None
        if e.code == 400:
            return "bad_request", None
        return "unreachable", {"error": "HTTP %d" % e.code}
    except Exception as e:                       # DNS, TLS, timeout, proxy, anything
        return "unreachable", {"error": "%s: %s" % (type(e).__name__, e)}


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("link", help="YouTube URL or 11 character video id")
    p.add_argument("video", help="local video file said to be that video")
    p.add_argument("--expect-title", help="override the fetched title, or supply one offline")
    p.add_argument("--expect-duration", type=float,
                   help="length in seconds, read off the watch page by /browse")
    p.add_argument("--tolerance", type=float, default=DURATION_TOLERANCE)
    p.add_argument("--offline", action="store_true", help="skip the oEmbed lookup")
    p.add_argument("--timeout", type=float, default=NET_TIMEOUT)
    p.add_argument("--ffmpeg")
    args = p.parse_args()

    video_id, shape = parse_video_id(args.link)
    if not video_id:
        out("ERROR", ERROR, ["%r is not a YouTube link or an 11 character video id" % args.link], {})

    facts = {"video_id": video_id, "link_shape": shape,
             "watch_url": "https://www.youtube.com/watch?v=" + video_id,
             "file": os.path.abspath(args.video),
             "basename": os.path.basename(args.video)}

    # The link is checked before the file, so a typo costs nothing.
    fetched_title = None
    if args.offline:
        facts["oembed_status"] = "skipped"
    else:
        status, data = fetch_oembed(video_id, args.timeout)
        facts["oembed_status"] = status
        if status in ("not_found", "bad_request"):
            out("ERROR", ERROR,
                ["YouTube has no public video at id %s (oEmbed said %s). Check the link, "
                 "or the video is private, deleted, or region blocked."
                 % (video_id, "404" if status == "not_found" else "400")], facts)
        if status == "unreachable":
            # Deliberately fatal. Falling back to the file name would let a run look
            # verified when the one authority on what the link points at was never asked.
            # An offline run has to be asked for.
            out("ERROR", ERROR,
                ["could not reach YouTube to verify the link (%s). Nothing was extracted. "
                 "Re-run when the network is back, or pass --offline to accept file-name "
                 "evidence alone." % (data or {}).get("error")], facts)
        if status == "ok":
            fetched_title = data.get("title")
            facts["title"] = fetched_title
            facts["channel"] = data.get("author_name")
            facts["channel_url"] = data.get("author_url")
            facts["thumbnail_url"] = data.get("thumbnail_url")
            if fetched_title:
                facts["slug"] = slugify(fetched_title)
        else:
            facts["oembed_error"] = (data or {}).get("error")

    if not os.path.isfile(args.video):
        out("ERROR", ERROR, ["no such file: %s" % args.video], facts)

    ffmpeg = find_ffmpeg(args.ffmpeg)
    if not ffmpeg:
        out("ERROR", ERROR, ["no ffmpeg. Run: python3 tools/video-frames.py ensure-ffmpeg"],
            facts)

    facts.update(probe(args.video, ffmpeg))
    if "duration" not in facts or "codec" not in facts:
        out("ERROR", ERROR, ["ffmpeg found no video stream in this file"], facts)

    base = os.path.basename(args.video)
    reasons = []
    if facts.get("oembed_status") == "skipped":
        reasons.append("--offline was passed, so the link was never checked against "
                       "YouTube and only the file name is evidence")

    # 1. the id itself, case sensitive
    if video_id in base:
        reasons.append("file name contains the video id %s" % video_id)
        facts["id_in_filename"] = True
        # A downloader that embeds one id does not embed a second one.
        out("VERIFIED", VERIFIED, reasons, facts)
    facts["id_in_filename"] = False

    if video_id.lower() in base.lower():
        reasons.append("file name contains %s but with different capitalisation; YouTube "
                       "ids are case sensitive, so confirm this is not a different video"
                       % video_id)
        out("INCONCLUSIVE", INCONCLUSIVE, reasons, facts)

    # 2. a different id-shaped token
    others = sorted(set(t for t in id_like_tokens(base) if t != video_id))
    if others:
        facts["other_ids_in_filename"] = others
        reasons.append("file name carries a different video id: %s. This looks like "
                       "another video, not %s." % (", ".join(sorted(set(others))), video_id))
        out("MISMATCH", MISMATCH, reasons, facts)

    # 3. duration and title supplied by the caller
    dur_state = None
    if args.expect_duration is not None:
        delta = abs(facts["duration"] - args.expect_duration)
        facts["duration_delta"] = round(delta, 2)
        facts["expect_duration"] = args.expect_duration
        if delta <= args.tolerance:
            dur_state = True
            reasons.append("duration %.2fs matches the reported %.0fs within %.1fs"
                           % (facts["duration"], args.expect_duration, args.tolerance))
        else:
            dur_state = False
            reasons.append("duration %.2fs is %.2fs away from the reported %.0fs"
                           % (facts["duration"], delta, args.expect_duration))

    # 4. the title. Fetched from oEmbed when the network answered, otherwise supplied.
    title = args.expect_title or fetched_title
    title_source = ("--expect-title" if args.expect_title
                    else "oEmbed" if fetched_title else None)
    title_state = None
    if title:
        need = TITLE_MATCH_WITH_DURATION if dur_state else TITLE_MATCH_ALONE
        ok, shared = title_matches_filename(title, base, need)
        facts["checked_title"] = title
        facts["title_source"] = title_source
        facts["title_slug_prefix_chars"] = shared
        facts["title_slug_chars_needed"] = need
        title_state = ok
        if ok:
            reasons.append("file name matches the real title on its first %d slug "
                           "characters (%s)" % (shared, title_source))
        else:
            reasons.append("file name does not match the real title %r, they share only "
                           "%d slug characters and %d were needed" % (title, shared, need))

    if dur_state is False:
        out("MISMATCH", MISMATCH, reasons, facts)
    if title_state and (dur_state or dur_state is None):
        out("VERIFIED", VERIFIED, reasons, facts)

    if "Google" in facts.get("handler_name", ""):
        reasons.append("container says %r, so the file did come from YouTube, but that "
                       "does not say which video" % facts["handler_name"])
    if title_state is False and looks_title_derived(base):
        facts["title_conflict"] = True
        reasons.append("the file name looks like it was named after some video's title, "
                       "and that title is not this one. Treat this as a probable wrong "
                       "file: do not extract, confirm with the user first. The two "
                       "innocent explanations are a renamed file and a localized title, "
                       "since YouTube serves titles per language and this lookup asked "
                       "for English.")
    if dur_state and title_state is None:
        reasons.append("duration agrees but nothing identifies the video; many videos "
                       "share a length, so confirm the title too")
    if title is None and args.expect_duration is None:
        reasons.append("no id in the file name and no title available; re-run with "
                       "--expect-title and --expect-duration read off the watch page")
    out("INCONCLUSIVE", INCONCLUSIVE, reasons, facts)


if __name__ == "__main__":
    main()
