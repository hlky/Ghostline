#!/usr/bin/env python3
"""Build and optionally install the verified standalone Goth Baddie profile."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import uuid

ROOT = next(parent for parent in Path(__file__).resolve().parents if (parent / "AGENTS.md").is_file())
PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from package_manifest import build_manifest
from package_project import install_verified, package_profile
from toolchain import resolve_tool


def disable_combined_ghostline(game: Path) -> list[str]:
    """Keep uniquely named backups when an explicit standalone install replaces the combined mod."""
    candidates = [game / "archive/pc/mod/Ghostline.archive", game / "archive/pc/mod/Ghostline.archive.xl"]
    candidates.extend((game / "r6/tweaks/ghostline").glob("*.yaml"))
    suffix = ".disabled-" + uuid.uuid4().hex[:12]
    disabled = []
    moved = []
    try:
        for source in candidates:
            if source.is_file():
                target = source.with_name(source.name + suffix)
                source.rename(target)
                moved.append((source, target))
                disabled.append(str(source.relative_to(game)))
    except BaseException:
        for source, target in reversed(moved):
            target.rename(source)
        raise
    return disabled


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wolvenkit", type=Path)
    parser.add_argument("--game", type=Path)
    parser.add_argument("--output", type=Path, default=PROJECT / "generated/packages")
    parser.add_argument("--install", action="store_true")
    parser.add_argument("--disable-ghostline", action="store_true")
    args = parser.parse_args()
    if args.disable_ghostline and not args.install:
        parser.error("--disable-ghostline requires --install")
    receipt = package_profile(build_manifest("gqt006"), output=args.output.resolve(),
                              wolvenkit=resolve_tool("wolvenkit", args.wolvenkit))
    disabled = []
    if args.install:
        game = resolve_tool("game", args.game)
        install_verified(receipt, game)
        if args.disable_ghostline:
            disabled = disable_combined_ghostline(game)
    print(json.dumps({**receipt, "installed": args.install, "disabled_ghostline_files": disabled}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
