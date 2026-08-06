---
name: youtube
description: Read and write YouTube data for the TossExplains channel through the official YouTube Data API v3 and YouTube Analytics API. Subcommands pull video stats, fetch official captions as [M:SS], read day-by-day analytics, upload a finished video, and profile a competitor channel. Use when the user says "/youtube", "pull video stats", "upload to YouTube", "fetch transcript from YouTube", "channel analytics", or "competitor research".
allowed-tools:
  - Bash
  - Read
  - Write
  - Glob
---

# youtube

Research and publishing skill, like `/video-swipe`. It does not feed the
eight-step content pipeline. It answers questions about a channel that is
already public, or ships a finished episode to YouTube.

The tool behind it is `tools/youtube-api.py`. It splits into two auth halves:

- `stats` and `competitor` use a server-side API key. They never touch OAuth
  and never need to ask for permission to read public data.
- `transcript`, `analytics`, and `upload` use OAuth. The user has already run
  the one-time browser flow that produced `YOUTUBE_REFRESH_TOKEN` in `.env`,
  so the tool just trades it for a fresh access token on every call.
  `transcript` needs OAuth even for public videos: YouTube's
  `captions.download` endpoint rejects API keys with a 401.

## Read first

- `.agents/rules/house-rules.md` - ASCII only, no em dash, no fluff.
- `.agents/skills/youtube/references/memory.md`

## Preconditions

Check the keys are present before spending a call. Missing keys are the most
common cause of silent failure:

```bash
P="/home/nakmiers/ME/Things/Build-a-Channel"
grep -q '^YOUTUBE_API_KEY=' "$P/.env"        && echo "api key ok"        || echo "missing YOUTUBE_API_KEY"
grep -q '^YOUTUBE_CLIENT_ID=' "$P/.env"     && echo "oauth id ok"       || echo "missing YOUTUBE_CLIENT_ID"
grep -q '^YOUTUBE_CLIENT_SECRET=' "$P/.env" && echo "oauth secret ok"   || echo "missing YOUTUBE_CLIENT_SECRET"
grep -q '^YOUTUBE_REFRESH_TOKEN=' "$P/.env" && echo "refresh token ok"  || echo "missing YOUTUBE_REFRESH_TOKEN"
grep -q '^YOUTUBE_CHANNEL_ID=' "$P/.env"    && echo "channel id ok"     || echo "missing YOUTUBE_CHANNEL_ID"
```

`analytics`, `transcript`, and `upload` need OAuth. `stats` and `competitor` only
need the API key.

Install deps once:

```bash
pip install -r requirements.txt
```

`defusedxml` is required to safely parse the TTML captions YouTube sends.
`google-auth-oauthlib` is required by `tools/yt_auth.py` for the one-time
OAuth flow. The tool exits with a clear message if either is missing.

### One-time OAuth flow

All OAuth material lives in `.env`. The client secrets JSON is stored as
`YOUTUBE_CLIENT_SECRETS_JSON` (one line, valid JSON) so it sits behind the
gitignore boundary with the rest of the secrets. `client_secrets.json` is
no longer shipped or kept in the repo; tools read `.env` first, the file
second.

The only value the user has to paste into `.env` after the flow is the
refresh token:

```bash
python3 tools/yt_auth.py
```

It opens a browser, the user signs in and grants the scopes, the script
prints a JSON payload plus a copy-paste block:

```
YOUTUBE_CLIENT_ID="..."
YOUTUBE_CLIENT_SECRET="..."
YOUTUBE_REFRESH_TOKEN="..."
```

Paste the `YOUTUBE_REFRESH_TOKEN` line into `.env`. Every subcommand picks
the secrets up from there.

If the browser cannot open (remote box, headless), run with `--no-browser`
to print the URL and accept the code manually.

## Step 1 - stats

Pull a single video's view count, like count, duration, and privacy. The
output is the same shape whether the video is yours or someone else's.

```bash
python3 tools/youtube-api.py stats <video_id>
```

`<video_id>` is the 11-character id from the URL, not the full link. The
tool prints a one-line summary to stdout and the full JSON to stderr.

## Step 2 - transcript

Pull the official captions as a `[M:SS] narration` transcript. This is an
alternative to `tools/audio-to-timestamps.py` for cases where the official
captions are already good enough.

```bash
python3 tools/youtube-api.py transcript <video_id> -o <transcript.md>
```

It picks the best available track: human-uploaded captions beat auto-generated
ones, English first. The output file matches the format documented in
`.agents/rules/file-formats.md` under `transcribes/transcript.md`, so a
future `/scenes` could consume it without rewriting. Last cue must sit within
a few seconds of the video's duration.

Validation, same regex the `transcript` skill uses:

```bash
T=<transcript.md>
wc -l "$T"
grep -cvE '^\[[0-9]+:[0-9]{2}\] .' "$T"   # must be 0
awk '{print $1}' "$T" | sort | uniq -d     # duplicate timestamps
```

## Step 3 - analytics

Day-by-day analytics for a video the channel owns. Returns impressions, CTR,
views, average view duration, and average view percentage in CSV form.

```bash
python3 tools/youtube-api.py analytics <video_id> -o analytics.csv
```

This needs the OAuth token, and it needs `YOUTUBE_CHANNEL_ID` in `.env`.
A non-owner video returns 403 with a clear "not authorized" message, not a
crash.

## Step 4 - upload

Upload a finished `.mp4` plus a metadata JSON. Always run with `--dry-run`
first to confirm the metadata shape:

```bash
python3 tools/youtube-api.py upload videos/<slug>.mp4 outputs/<slug>.meta.json --dry-run
```

The `meta.json` shape:

```json
{
  "title": "Why you feel lonelier in a crowd than alone in your room",
  "description": "...",
  "tags": ["loneliness", "psychology"],
  "categoryId": "22",
  "privacyStatus": "private"
}
```

Live upload (not `--dry-run`) currently requires a follow-up wiring step
with `google-api-python-client`. The skill stops there on purpose: a wrong
upload is the worst case here, so the user must opt in explicitly when they
are ready to add the resumable-upload dependency.

**Before any live upload, run `tools/youtube-verify.py` on the file.** It
checks the local video against its YouTube link, which catches the case
where the wrong file got exported. Same tool the `video-swipe` skill uses.

## Step 5 - competitor

Profile a public channel. Accepts either a handle (`@veritasium`) or a
channel id (`UC...`). Returns subscriber count, total views, top 20 videos
ranked by view count, and the median days between consecutive uploads.

```bash
python3 tools/youtube-api.py competitor @veritasium -o research/competitors/veritasium.json
```

This is the read-only entry point for the `video-swipe` workflow: pick a
channel here, then run `/video-swipe` on a single video from it.

## Report and hand off

Always print a one-line summary in chat so the user can scan results without
opening the JSON:

```
Title | 12,345 views | 690s | privacy=public
42 cues, last at [11:30], language=en, kind=standard -> /tmp/test.md
30 days of analytics for dQw4w9WgXcQ, 2025-01-01 -> 2025-01-30 -> analytics.csv
@veritasium: 4,200,000 subs, 320 videos, top 20 pulled, median cadence 7.5d
```

Then suggest the next move:

- After `competitor`, **`/video-swipe`** on one of the top videos.
- After `transcript`, drop the file under `projects/<n>-<slug>/transcribes/`
  and run **`/scenes`** if the user wants visuals from it.
- After `upload` with `--dry-run`, ask the user to confirm before any live
  upload.

## Guardrails

- Never commit `client_secrets.json` or `token.json`. They are gitignored.
- Never re-run a live upload without `--dry-run` first on a new video.
- Never call `analytics` on a video the channel does not own. The token is
  the user's; surface the 403 cleanly rather than retrying.
- Never fall back to a different auth method if the requested one fails.
  The user picked the path; report the failure verbatim and stop.
- Never log a refresh token or client secret to a file. Stderr gets JSON
  payloads only; the secrets stay in `.env`.

## Self-improvement

Read `.agents/skills/youtube/references/memory.md` at the start of every run.
Append when an API quirk bites (rate-limit shape, `captionNotFound` payload,
analytics 403 wording) or when a flag combination produces a better cut for
this channel's pacing.
