#!/usr/bin/env python3
"""Reject material that crosses the public repository boundary."""

from __future__ import annotations

import ipaddress
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_NAMES = {
    ".env",
    "id_rsa",
    "id_ed25519",
    "known_hosts",
}
FORBIDDEN_SUFFIXES = {
    ".key",
    ".pem",
    ".p12",
    ".pfx",
    ".kdbx",
}
FORBIDDEN_PATH_PARTS = {
    "inventory",
    "runtime-inventory",
    "evidence",
}
PRIVATE_KEY = re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----")
IPV4 = re.compile(r"(?<![0-9.])(?:\d{1,3}\.){3}\d{1,3}(?![0-9.])")

DOCUMENTATION_NETWORKS = tuple(
    ipaddress.ip_network(net)
    for net in ("192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24")
)


def tracked_files() -> list[Path]:
    output = subprocess.check_output(
        ["git", "-C", str(ROOT), "ls-files", "-z"],
        stderr=subprocess.DEVNULL,
    )
    return [ROOT / item.decode() for item in output.split(b"\0") if item]


def allowed_address(address: ipaddress.IPv4Address) -> bool:
    if address.is_loopback:
        return True
    return any(address in network for network in DOCUMENTATION_NETWORKS)


def main() -> int:
    failures: list[str] = []

    for path in tracked_files():
        relative = path.relative_to(ROOT)
        rel = relative.as_posix()

        if path.name in FORBIDDEN_NAMES or path.suffix.lower() in FORBIDDEN_SUFFIXES:
            failures.append(f"sensitive file name/type: {rel}")

        if any(part.lower() in FORBIDDEN_PATH_PARTS for part in relative.parts):
            failures.append(f"private operational path is not allowed: {rel}")

        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        lower = text.lower()
        if ".home.arpa" in lower:
            failures.append(f"private DNS name found: {rel}")
        if PRIVATE_KEY.search(text):
            failures.append(f"private-key material found: {rel}")

        for candidate in IPV4.findall(text):
            try:
                address = ipaddress.ip_address(candidate)
            except ValueError:
                continue
            if isinstance(address, ipaddress.IPv4Address) and address.is_private and not allowed_address(address):
                failures.append(f"private IPv4 address {candidate} found: {rel}")

    if failures:
        for failure in sorted(set(failures)):
            print(f"ERROR: {failure}", file=sys.stderr)
        return 1

    print("Public boundary validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
