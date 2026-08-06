#!/usr/bin/env python3
"""Trade a YouTube OAuth refresh token for a short-lived access token.

    from yt_oauth import get_access_token
    token = get_access_token()                       # cached for this process
    token = get_access_token(force=True)             # bypass cache

Reads YOUTUBE_CLIENT_ID, YOUTUBE_CLIENT_SECRET, YOUTUBE_REFRESH_TOKEN from the
nearest .env using the same loader audio-to-timestamps.py uses. No browser
popup, no token.json: the user already ran the one-time OAuth flow that
produced the refresh token, and this helper just keeps it warm.

Usage from a tool:

    import yt_oauth
    headers = {"Authorization": f"Bearer {yt_oauth.get_access_token()}"}
"""

from __future__ import annotations

import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

TOKEN_ENDPOINT = "https://oauth2.googleapis.com/token"
GRANT_TYPE = "refresh_token"

_cached_token: str | None = None


def load_dotenv() -> Path | None:
    """Read KEY=value pairs from the nearest .env, without overriding the shell."""
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


def load_client_secrets() -> dict | None:
    """Fall back to client_secrets.json when .env holds no OAuth values.

    Lookup order:
      1. YOUTUBE_CLIENT_SECRETS_JSON in .env (one-line JSON blob).
      2. client_secrets.json in the project root.

    Sets CLIENT_ID and CLIENT_SECRET on os.environ so the existing exchange
    code does not need to change. The refresh token still has to come from
    .env (or from yt_auth.py output).
    """
    if os.environ.get("YOUTUBE_CLIENT_ID") and os.environ.get("YOUTUBE_CLIENT_SECRET"):
        return None  # already configured
    import json

    blob = os.environ.get("YOUTUBE_CLIENT_SECRETS_JSON", "").strip()
    if blob:
        try:
            data = json.loads(blob)
        except json.JSONDecodeError:
            return None
    else:
        for folder in (Path.cwd(), *Path(__file__).resolve().parents):
            path = folder / "client_secrets.json"
            if not path.is_file():
                continue
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                return None
            break
        else:
            return None

    payload = data.get("installed") or data.get("web")
    if not payload:
        return None
    os.environ.setdefault("YOUTUBE_CLIENT_ID", payload.get("client_id", ""))
    os.environ.setdefault("YOUTUBE_CLIENT_SECRET", payload.get("client_secret", ""))
    return True


def _require(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        sys.exit(
            f"error: {name} is missing from .env and the environment. "
            "Run the OAuth flow once to populate it, or paste the refresh token in."
        )
    return value


def _exchange() -> str:
    # Pull client_id/secret from client_secrets.json if .env did not have them.
    if not (os.environ.get("YOUTUBE_CLIENT_ID") and os.environ.get("YOUTUBE_CLIENT_SECRET")):
        load_client_secrets()
    client_id = _require("YOUTUBE_CLIENT_ID")
    client_secret = _require("YOUTUBE_CLIENT_SECRET")
    refresh_token = _require("YOUTUBE_REFRESH_TOKEN")

    body = urllib.parse.urlencode(
        {
            "client_id": client_id,
            "client_secret": client_secret,
            "refresh_token": refresh_token,
            "grant_type": GRANT_TYPE,
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        TOKEN_ENDPOINT,
        data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            payload = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        # Google's body holds the real reason (invalid_grant, etc.). Surface it.
        detail = e.read().decode("utf-8", errors="replace")[:400]
        sys.exit(f"error: refresh-token exchange rejected: {e.code} {detail}")
    except urllib.error.URLError as e:
        sys.exit(f"error: cannot reach {TOKEN_ENDPOINT}: {e.reason}")

    import json

    parsed = json.loads(payload)
    token = parsed.get("access_token")
    if not token:
        sys.exit(f"error: token endpoint returned no access_token: {payload[:200]}")
    return token


def get_access_token(force: bool = False) -> str:
    """Return a valid access token, refreshing once if the cache is empty."""
    global _cached_token
    if force or _cached_token is None:
        _cached_token = _exchange()
    return _cached_token


def main() -> int:
    """CLI form: prints the token. Useful for `Bearer $(python3 yt_oauth.py)`."""
    load_dotenv()
    print(get_access_token(force=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())