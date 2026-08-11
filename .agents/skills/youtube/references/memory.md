# youtube - self-improving notes

## 2026-08-05 - initial setup

Five subcommands wired to `tools/youtube-api.py`:

- `stats <video_id>` - public video stats, API key only.
- `transcript <video_id>` - official captions in `[M:SS]` form, OAuth.
- `analytics <video_id>` - daily CSV, OAuth + `YOUTUBE_CHANNEL_ID`.
- `upload <video.mp4> <meta.json>` - dry-run validates metadata; live upload
  still requires a follow-up wiring step with `google-api-python-client`.
- `competitor <handle_or_id>` - top 20 videos + cadence, API key only.

Auth path: refresh-token in `.env` is exchanged for a short-lived access
token through `tools/yt_oauth.py`. No browser popup on every call; the
browser only opens once during `tools/yt_auth.py`.

Captions are parsed by `defusedxml.ElementTree` to defuse XXE on the
untrusted TTML blob YouTube returns.

## 2026-08-05 - one-time OAuth via yt_auth.py

`tools/yt_auth.py` opens the browser once, walks the user through the OAuth
flow, and prints a JSON payload plus a copy-paste block. The refresh token
is the only value that must land in `.env`.

Lookup order for OAuth secrets is `.env` first, `client_secrets.json` second:

1. `YOUTUBE_CLIENT_SECRETS_JSON` in `.env` (one-line JSON blob, the new
   canonical form).
2. `client_secrets.json` in the project root (legacy fallback, still works).

Both `tools/yt_auth.py` and `tools/yt_oauth.py` follow this order. The user
optionally kept the file for a while, then deleted it once the env blob
proved itself. End state: no file on disk, all secrets inside `.env`.

## 2026-08-05 - transcript subcommand needs OAuth

YouTube `captions.download` returns 401 with `API keys are not supported by
this API` even for public videos whose captions are world-readable. The
`youtube-transcript-api` Python lib dodges this by scraping the timedtext
endpoint without auth, but that is a different API and changes shape. Plan
default: OAuth for `transcript`. If a use case ever needs anonymous
caption pulls, drop in a fallback that calls timedtext directly.

## 2026-08-05 - delete client_secrets.json

The file was deleted from the project root after the user's call. All
material now lives in `.env` as `YOUTUBE_CLIENT_SECRETS_JSON`. Even though
the file was gitignored, having a sensitive file at the project root is a
footgun: a forgotten `.gitignore` on a fresh clone, a fat-finger `git add
.`, a sync to a backup that does not honour gitignore. The env-blob path
costs one extra line in `.env` and zero ambiguity.

To rotate, edit the JSON blob directly in `.env` or use `yt_auth.py` against
a new client from Google Cloud Console.

## 2026-08-05 - channel renamed to TossPsychology

User renamed the channel. The Data API still reports the channel title as
"Toss" (the brand name) but the custom URL is now `@tosspsychology`. The
channel id `UCQfgnFoty6qGUw0H0dCyYOQ` is stored in `.env` as
`YOUTUBE_CHANNEL_ID`, and the handle as `YOUTUBE_CHANNEL_HANDLE`. The
analytics subcommand reads `YOUTUBE_CHANNEL_ID`; the competitor subcommand
can take the handle directly. Note: a freshly-renamed channel may still
serve the old URL `youtube.com/@toss...` for a short time, so the
competitor report should be sanity-checked against the live YouTube page
on first use.

## Open lessons (fill in as they happen)

- First-rate 429 / quotaExceeded payload shape.
- Reproduction of captionNotFound vs generic 404 wording.
- Analytics 403 wording for non-owner videos.
- Anything weird about `forHandle` vs `forUsername` once we hit a holdout.

## 2026-08-06 - Analytics API must be enabled separately

OAuth consent screen being Published does NOT enable the YouTube Analytics
API. Project `373822054655` returned:

  403: "YouTube Analytics API has not been used in project 373822054655
        before or it is disabled. Enable it by visiting
        https://console.developers.google.com/apis/api/youtubeanalytics.googleapis.com/overview?project=373822054655"

The fix is one click in that URL; propagation took under a minute in this
run. Add this to the preconditions gate in `tools/youtube-api.py` so the
"analytics requires OAuth" error does not mask the real "Analytics API
disabled" error - they have identical wording shape otherwise.

## 2026-08-06 - impressions metric unavailable on this project

After enabling the API, `metrics=impressions` and `metrics=impression` both
return:

  400: "Unknown identifier (impressions) given in field parameters.metrics."

Why: this specific GCP project seems to scope Analytics to the channel/
engagement metric set, not the discovery set. Workaround: ask for
`views, comments, likes, dislikes, shares, averageViewDuration,
averageViewPercentage` and pull CTR / traffic share via the
`insightTrafficSourceType` dimension instead. `impressionClickThroughRate`
in the same call also rejected, so CTR is compute-from-source-counts only.

## 2026-08-11 - correction: impressions is an API-wide gap, not project scoping

The 2026-08-06 note above guessed that this GCP project scopes Analytics to the
engagement metric set. That guess was wrong. Thumbnail `impressions` and
`impressionClickThroughRate` are **YouTube Studio exclusives** and have never
existed in Analytics API v2 for any project. No console toggle fixes it. Any CTR
number has to be read out of Studio by hand.

Consequence: `cmd_analytics` in `tools/youtube-api.py` hardcodes both metrics in
its `metrics=` list, so **the `analytics` subcommand fails 400 on every single
call**. It has never worked. Fix is to drop those two names from the list. Until
then, query `youtubeanalytics.googleapis.com/v2/reports` directly.

Metrics confirmed working on this channel: `views`,
`estimatedMinutesWatched`, `averageViewDuration`, `averageViewPercentage`,
`subscribersGained`, `subscribersLost`, `likes`, `dislikes`, `comments`,
`shares`.

## 2026-08-11 - audience retention report is the high-value call

Not in the skill yet, and it is the most useful thing the API gives this channel:

```
dimensions=elapsedVideoTimeRatio
metrics=audienceWatchRatio,relativeRetentionPerformance
filters=video==<id>
```

Returns 100 buckets from 0.01 to 1.0. `audienceWatchRatio` is the share of
viewers still watching. `relativeRetentionPerformance` is a percentile against
comparable videos, 0.5 = median. This is what diagnoses whether a weak video is
a packaging problem or a hook problem, which the view/CTR pair cannot do.
Worth promoting to a documented step in SKILL.md.

## 2026-08-11 - data horizon lags 3 to 4 days

Queried on 2026-08-11, the last day with any rows was 2026-08-07. Videos
published inside that window return **zero** views from Analytics while the Data
API shows real public counts (2 videos at 3 and 14 public views both reported 0).
Any report that mixes `data_*` and `ana_*` columns must say so, and a zero from
Analytics on a fresh video is never evidence the video flopped.

## 2026-08-11 - competitor subcommand rejects channel ids

`cmd_competitor` branches on `not ID_RE.match(handle)`, but `ID_RE` is the
11-character **video** id regex. Channel ids are 24 characters starting with
`UC`, so they never match and always fall through to the `forHandle` path,
producing a misleading `error: channel handle 'UCQfgnFoty6qGUw0H0dCyYOQ' not
found`. The `else` branch that calls `channels?id=` is currently dead code.
Workaround: pass the handle. Real fix: gate on `^UC[A-Za-z0-9_-]{22}$`.

## 2026-08-06 - reject loop in yauth.py auth block

OAuth error screen reads "EnglishForOnlyMe has not completed the Google
verification process" - this happens when the OAuth client is in Testing
mode and the Google account signing in is not on the Test users list. Fix:
either add the account under APIs & Services > OAuth consent screen >
Audience > Test users, or Publish the consent screen first. `yt_auth.py`
itself is fine; the block is purely a project-config gate.

## 2026-08-06 - refresh_token lifetime on this project

The minted refresh token is 103 characters and starts with `1//0g...`,
matching the standard Google format. Token was written into `.env` by an
agent script rather than re-pasted manually - same loader parses it on the
next `load_dotenv()`. Treat the token as if printed: never echo to chat,
never log to disk except `.env`.

