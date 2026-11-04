#!/usr/bin/env python3
"""Remove private and reserved addresses/networks from IP lists (in place).

A line is dropped if its IP/network overlaps a private or reserved range (even
partially). Entries from allowlist.conf are carved out of listed networks, the
rest stays listed. Comments and blank lines are kept, unparsable lines are dropped.
Output: number of removed or split lines per file. Exit code 1 if more than
MAX_INVALID_RATIO of a file's entries are unparsable (broken download).
"""
import ipaddress
import os
import sys
from pathlib import Path

MAX_INVALID_RATIO = 0.01

EXTRA = [ipaddress.ip_network(n) for n in (
    "0.0.0.0/8", "10.0.0.0/8", "100.64.0.0/10", "127.0.0.0/8", "169.254.0.0/16",
    "172.16.0.0/12", "192.0.0.0/24", "192.0.2.0/24", "192.168.0.0/16",
    "198.18.0.0/15", "198.51.100.0/24", "203.0.113.0/24", "224.0.0.0/4",
    "240.0.0.0/4", "::/128", "::1/128", "fc00::/7", "fe80::/10", "ff00::/8",
    "2001:db8::/32",
)]


def load_allowlist():
    path = Path(__file__).with_name("allowlist.conf")
    nets = []
    for line in path.read_text(encoding="utf-8").splitlines():
        token = line.split("#", 1)[0].strip()
        if token:
            nets.append(ipaddress.ip_network(token, strict=False))
    return nets


ALLOW = load_allowlist()


def apply_allowlist(net):
    """Return the networks left of net after subtracting the allowlist."""
    parts = [net]
    for a in ALLOW:
        nxt = []
        for p in parts:
            if p.version != a.version or not p.overlaps(a):
                nxt.append(p)
            elif a.prefixlen <= p.prefixlen:
                continue  # p lies completely inside a
            else:
                nxt.extend(p.address_exclude(a))
        parts = nxt
    return parts


def is_special(addr):
    return (addr.is_private or addr.is_loopback or addr.is_link_local
            or addr.is_reserved or addr.is_multicast or addr.is_unspecified)


def is_private_line(token):
    try:
        net = ipaddress.ip_network(token, strict=False)
    except ValueError:
        return False
    if is_special(net.network_address) or is_special(net.broadcast_address):
        return True
    return any(net.version == r.version and net.overlaps(r) for r in EXTRA)


def fmt(net):
    if net.prefixlen < net.max_prefixlen:
        return f"{net.network_address}/{net.prefixlen}\n"
    return f"{net.network_address}\n"


def filter_file(path):
    kept, changed, invalid, entries = [], 0, 0, 0
    verbose = os.environ.get("VERBOSE")
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            token = line.split("#", 1)[0].strip()
            if not token:
                kept.append(line)
                continue
            entries += 1
            if is_private_line(token):
                changed += 1
                if verbose:
                    print(f"  removed: {token}")
                continue
            try:
                net = ipaddress.ip_network(token, strict=False)
            except ValueError:
                invalid += 1
                changed += 1
                if verbose:
                    print(f"  invalid: {token}")
                continue
            parts = apply_allowlist(net)
            if parts == [net]:
                kept.append(line)
                continue
            changed += 1
            if verbose:
                print(f"  allowlist: {token} -> {len(parts)} networks")
            kept.extend(fmt(p) for p in parts)
    if changed:
        with open(path, "w", encoding="utf-8") as fh:
            fh.writelines(kept)
    return changed, invalid, entries


if __name__ == "__main__":
    total, broken = 0, []
    for p in sys.argv[1:]:
        n, invalid, entries = filter_file(p)
        total += n
        print(f"{p}: {n} lines removed/split, {invalid} invalid")
        if entries and invalid / entries > MAX_INVALID_RATIO:
            broken.append(p)
    print(f"Total: {total} lines removed")
    if broken:
        print(f"ERROR: too many invalid entries in: {' '.join(broken)}", file=sys.stderr)
        sys.exit(1)
