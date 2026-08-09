# YouTube Memory

## API contract

- `stats <video_id>` uses the public API key.
- `transcript <video_id>` uses OAuth and writes official captions as `[M:SS]` cues.
- `analytics <video_id>` uses OAuth plus `YOUTUBE_CHANNEL_ID`.
- `upload <video.mp4> <meta.json>` validates first and requires explicit live-upload
  authorization.
- `competitor <handle_or_id>` profiles public videos and cadence.

OAuth secrets live in `.env`. `YOUTUBE_CLIENT_SECRETS_JSON` is canonical and a root
`client_secrets.json` is a legacy fallback only. Never print tokens or secrets.

HumanPrice channel IDs and handles must be verified before any channel-side write. The
repository migration does not itself authorize renaming or uploading on YouTube.
