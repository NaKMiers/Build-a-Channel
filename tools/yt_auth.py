#!/usr/bin/env python3
"""Run the one-time OAuth flow against the local client_secrets.json.

This is the only script that opens a browser. The user signs in, grants the
scopes, and the script prints a refresh token to paste into .env.

    python3 tools/yt_auth.py
    python3 tools/yt_auth.py --secrets /path/to/client_secrets.json

Reads from `client_secrets.json` in the project root by default. That file is
gitignored. No token is written to disk here; only printed to stdout.

Exit codes:
  0  success (a refresh token was printed)
  1  user error (missing secrets file, missing client_id/secret, no browser)
  2  network / OAuth rejection (invalid_grant, scope mismatch, etc.)

Requires: google-auth-oauthlib (declared in requirements.txt).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import webbrowser
from pathlib import Path

# Same loader yt_oauth uses. Inline rather than importing to keep this script
# runnable before google-auth-oauthlib is installed.
def _load_dotenv() -> Path | None:
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

# Scopes needed by the youtube skill. upload scope is optional; if the user
# only wants stats/transcript/analytics/competitor they can omit it.
DEFAULT_SCOPES = [
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/yt-analytics.readonly",
    "https://www.googleapis.com/auth/youtube.force-ssl",
]


def find_secrets(path: Path) -> dict:
    """Return the parsed client secrets, surfacing the real errors.

    Lookup order:
      1. YOUTUBE_CLIENT_SECRETS_JSON env var (one-line blob in .env).
      2. client_secrets.json at --secrets / default path.

    Both shapes (file and inline) parse to the same dict Google's OAuth tooling
    downloads: a top-level object with an "installed" or "web" block.
    """
    raw = os.environ.get("YOUTUBE_CLIENT_SECRETS_JSON", "").strip()
    if raw:
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as e:
            sys.exit(f"error: YOUTUBE_CLIENT_SECRETS_JSON in .env is not valid JSON: {e}")
    elif path.is_file():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            sys.exit(f"error: client secrets at {path} is not valid JSON: {e}")
    else:
        sys.exit(
            f"error: client secrets not found. Either paste the JSON blob as "
            f"YOUTUBE_CLIENT_SECRETS_JSON=... in .env, or download the OAuth "
            f"client JSON from Google Cloud Console and place it at {path}."
        )

    # The Google-format file has either an "installed" or a "web" block at
    # the top level. Desktop apps land under "installed".
    payload = data.get("installed") or data.get("web")
    if not payload:
        sys.exit(
            "error: client secrets JSON has neither 'installed' nor 'web'. "
            "Are you sure this is the OAuth client JSON, not an API key?"
        )

    client_id = payload.get("client_id", "")
    client_secret = payload.get("client_secret", "")
    if not client_id or not client_secret:
        sys.exit("error: client secrets JSON is missing client_id or client_secret")

    return payload


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the one-time OAuth flow and print a refresh token."
    )
    parser.add_argument(
        "--secrets",
        default="client_secrets.json",
        help="Path to client_secrets.json (default: project root).",
    )
    parser.add_argument(
        "--scopes",
        nargs="+",
        default=DEFAULT_SCOPES,
        help="OAuth scopes to request (default: full youtube set).",
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Print the auth URL instead of opening the browser.",
    )
    args = parser.parse_args()

    _load_dotenv()

    secrets_path = Path(args.secrets).resolve()
    payload = find_secrets(secrets_path)

    # Lazy import so this script's existence does not block running other
    # tools on a machine that does not have google-auth-oauthlib installed.
    try:
        from google_auth_oauthlib.flow import InstalledAppFlow
    except ImportError:
        sys.exit(
            "error: google-auth-oauthlib is not installed. "
            "Run: pip install google-auth-oauthlib"
        )

    # Build a client_config dict InstalledAppFlow understands. We do not use
    # payload directly because InstalledAppFlow wants the entire "installed"
    # or "web" block plus "redirect_uris" already wired up.
    client_config = {
        "installed": {
            "client_id": payload["client_id"],
            "client_secret": payload["client_secret"],
            "auth_uri": payload.get(
                "auth_uri", "https://accounts.google.com/o/oauth2/auth"
            ),
            "token_uri": payload.get(
                "token_uri", "https://oauth2.googleapis.com/token"
            ),
            "auth_provider_x509_cert_url": payload.get(
                "auth_provider_x509_cert_url",
                "https://www.googleapis.com/oauth2/v1/certs",
            ),
            "redirect_uris": payload.get("redirect_uris", ["http://localhost"]),
        }
    }

    flow = InstalledAppFlow.from_client_config(client_config, scopes=args.scopes)

    if args.no_browser:
        # Print the URL and let the user paste the code themselves. Useful on
        # a remote box where the script cannot open a local browser.
        auth_url, _ = flow.authorization_url(
            access_type="offline",
            prompt="consent",
            include_granted_scopes="true",
        )
        print("Open this URL in a browser, approve, then paste the code:")
        print(auth_url)
        code = input("\ncode: ").strip()
        flow.fetch_token(code=code)
    else:
        # run_local_server spins up a temporary HTTP server on 127.0.0.1 to
        # catch the redirect. Client secrets with redirect_uris=["http://localhost"]
        # are pre-wired for this; google-auth-oauthlib picks a free port.
        flow.run_local_server(
            host="127.0.0.1",
            port=0,
            authorization_url_kwargs={
                "access_type": "offline",
                "prompt": "consent",  # forces a refresh token to come back
                "include_granted_scopes": "true",
            },
        )

    credentials = flow.credentials
    if not credentials.refresh_token:
        sys.exit(
            "error: Google returned no refresh_token. This happens when the app "
            "has already been authorized once; revoke access at "
            "https://myaccount.google.com/permissions and retry."
        )

    payload_out = {
        "client_id": payload["client_id"],
        "client_secret": payload["client_secret"],
        "refresh_token": credentials.refresh_token,
        "scopes": credentials.scopes,
    }
    print(json.dumps(payload_out, indent=2))
    print(
        "\n# paste these lines into .env:\n"
        f'YOUTUBE_CLIENT_ID="{payload["client_id"]}"\n'
        f'YOUTUBE_CLIENT_SECRET="{payload["client_secret"]}"\n'
        f'YOUTUBE_REFRESH_TOKEN="{credentials.refresh_token}"\n',
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())