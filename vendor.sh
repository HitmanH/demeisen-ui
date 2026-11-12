#!/usr/bin/env bash
# Copy a fixed version of Demeisen UI into an app, e.g.:
#   ./vendor.sh v1.0.0 ../demeisen-intranet/static/ui
# Apps keep their own copy, so they never depend on this repo (or any Demeisen server) at runtime.
set -euo pipefail
ver="$1"; dest="$2"
here="$(cd "$(dirname "$0")" && pwd)"
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
git -C "$here" archive "$ver" dist | tar -x -C "$tmp"
mkdir -p "$dest"; cp -R "$tmp/dist/." "$dest/"
echo "$ver" > "$dest/VERSION"
echo "Demeisen UI $ver copied to $dest"
