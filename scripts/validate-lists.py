#!/usr/bin/env python3
"""Sanity-check generated lists before they are published.

Usage: validate-lists.py NEW_DIR [PREVIOUS_DIR]

Fails (exit 1) if a list is missing, nearly empty, contains unparsable lines, or
differs in size from the previously published version by more than MAX_CHANGE
(MAX_CHANGE_AIO for the combined list).
Without PREVIOUS_DIR only the absolute checks run.
"""
import ipaddress
import sys
from pathlib import Path

MIN_ENTRIES = 100
MAX_CHANGE = 0.50
MAX_CHANGE_AIO = 0.20


def entries(path):
    out = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        token = line.split("#", 1)[0].strip()
        if token:
            out.append(token)
    return out


def main():
    new_dir = Path(sys.argv[1])
    prev_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    errors = []
    files = sorted(new_dir.glob("*.list")) + sorted(new_dir.glob("aio/*.list"))
    if not files:
        errors.append("no lists found")
    for path in files:
        rel = path.relative_to(new_dir)
        items = entries(path)
        if len(items) < MIN_ENTRIES:
            errors.append(f"{rel}: only {len(items)} entries")
            continue
        bad = 0
        for token in items:
            try:
                ipaddress.ip_network(token, strict=False)
            except ValueError:
                bad += 1
        if bad:
            errors.append(f"{rel}: {bad} unparsable entries")
        prev = prev_dir / rel if prev_dir else None
        if prev and prev.is_file():
            old = len(entries(prev))
            limit = MAX_CHANGE_AIO if rel.parts[0] == "aio" else MAX_CHANGE
            if old and abs(len(items) - old) / old > limit:
                errors.append(f"{rel}: size changed {old} -> {len(items)} (> {limit:.0%})")
        print(f"{rel}: {len(items)} entries")
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    print("Validation passed.")


if __name__ == "__main__":
    main()
