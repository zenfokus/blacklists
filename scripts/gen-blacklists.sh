#!/bin/bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BLACKLIST_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

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
for filename in "${!URLS[@]}"; do
    url="${URLS[$filename]}"
    curl -fsSL "$url" -o "$filename" &
done
wait
echo "All lists were successfully downloaded."

AIO_DIR="$BLACKLIST_DIR/aio"
AIO_FILE="$AIO_DIR/aio_blacklist.list"
mkdir -p "$AIO_DIR"

BLACKLIST_FILES=("${!URLS[@]}")

LC_ALL=C cat "${BLACKLIST_FILES[@]}" \
  | LC_ALL=C grep -vE '^#|^$|^0\.' \
  | LC_ALL=C sort -u > "$AIO_FILE"
echo "Combined list created at $AIO_FILE."
