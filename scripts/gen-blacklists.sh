#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BLACKLIST_DIR="$(cd "$SCRIPT_DIR/.." && pwd)/output"

declare -A URLS
CONFIG_FILE="$SCRIPT_DIR/blacklists.conf"

if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "ERROR: Configuration file $CONFIG_FILE not found."
    exit 1
fi

while IFS='=' read -r filename url || [ -n "$filename" ]; do
    [[ -z "$filename" || "$filename" =~ ^# ]] && continue
    filename=$(echo "$filename" | xargs)
    url=$(echo "$url" | xargs)
    URLS["$filename"]="$url"
done < "$CONFIG_FILE"

mkdir -p "$BLACKLIST_DIR"
cd "$BLACKLIST_DIR"

echo "Downloading lists..."
declare -A PIDS
for filename in "${!URLS[@]}"; do
    curl -fsSL --retry 3 --max-time 180 "${URLS[$filename]}" -o "$filename.tmp" &
    PIDS["$filename"]=$!
done
failed=0
for filename in "${!PIDS[@]}"; do
    if wait "${PIDS[$filename]}" && [[ -s "$filename.tmp" ]]; then
        mv "$filename.tmp" "$filename"
    else
        echo "ERROR: download of $filename failed or empty."
        rm -f "$filename.tmp"
        failed=1
    fi
done
if (( failed )); then
    exit 1
fi
echo "All lists were successfully downloaded."

echo "Removing private/reserved ranges..."
python3 "$SCRIPT_DIR/filter-private.py" "${!URLS[@]}"

AIO_DIR="$BLACKLIST_DIR/aio"
AIO_FILE="$AIO_DIR/aio_blacklist.list"
mkdir -p "$AIO_DIR"

BLACKLIST_FILES=("${!URLS[@]}")

LC_ALL=C cat "${BLACKLIST_FILES[@]}" \
  | LC_ALL=C grep -vE '^#|^$|^0\.' \
  | LC_ALL=C sort -u > "$AIO_FILE"
echo "Combined list created at $AIO_FILE."

# Compare against the published version (if reachable) and abort on suspicious results.
PREVIOUS_DIR=""
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
if git -C "$REPO_DIR" fetch -q --depth=1 origin release 2>/dev/null || \
   git -C "$REPO_DIR" rev-parse -q --verify origin/release >/dev/null; then
    PREVIOUS_DIR="$(mktemp -d)"
    trap 'rm -rf "$PREVIOUS_DIR"' EXIT
    git -C "$REPO_DIR" archive origin/release | tar -x -C "$PREVIOUS_DIR"
else
    echo "WARNING: previous release not available, skipping size comparison."
fi
python3 "$SCRIPT_DIR/validate-lists.py" "$BLACKLIST_DIR" ${PREVIOUS_DIR:+"$PREVIOUS_DIR"}
