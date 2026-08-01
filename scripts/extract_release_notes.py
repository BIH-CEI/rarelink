#!/usr/bin/env python3
"""Extract one version's section from docs/6_changelog.rst as Markdown."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

UNDERLINE = re.compile(r"^[-=~\"'^*+#]{3,}\s*$")


def extract(text: str, version: str) -> str:
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.startswith(f"v{version}") and i + 1 < len(lines) and UNDERLINE.match(lines[i + 1]):
            start = i + 2
            break
    if start is None:
        raise SystemExit(f"no section for v{version} in the changelog")

    end = len(lines)
    for i in range(start, len(lines)):
        if re.match(r"^v\d+\.\d+", lines[i]) and i + 1 < len(lines) and UNDERLINE.match(lines[i + 1]):
            end = i
            break

    out, block = [], lines[start:end]
    for i, line in enumerate(block):
        if i + 1 < len(block) and UNDERLINE.match(block[i + 1]) and line.strip():
            out.append(f"### {line.strip().rstrip(':')}")
        elif UNDERLINE.match(line):
            continue
        else:
            out.append(line)

    md = "\n".join(out)
    md = re.sub(r"``([^`]+)``", r"`\1`", md)
    md = re.sub(r"`([^`<]+?)\s*<([^>]+)>`_", r"[\1](\2)", md)
    md = md.replace("\\ ", "")
    return md.strip() + "\n"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("version")
    ap.add_argument("--changelog", default="docs/6_changelog.rst", type=Path)
    a = ap.parse_args()
    sys.stdout.write(extract(a.changelog.read_text(), a.version))
