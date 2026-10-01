#!/usr/bin/env bash
# Serve the sitemap as static files: ./serve.sh [port]
set -euo pipefail

PORT="${1:-8900}"
cd "$(dirname "$0")"
exec python3 -m http.server "$PORT" --bind 0.0.0.0
