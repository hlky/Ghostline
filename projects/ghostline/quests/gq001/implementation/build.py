#!/usr/bin/env python3
"""Build gq001's phases, journal, and localization from one authoring manifest."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

ROOT = next(
    parent
    for parent in Path(__file__).resolve().parents
    if (parent / "AGENTS.md").is_file()
)
PROJECT = next(parent for parent in Path(__file__).resolve().parents if (parent / "project.json").is_file())
if str(ROOT / "tools") not in sys.path:
    sys.path.insert(0, str(ROOT / "tools"))

from quest_authoring import compose
from quest_build import main as build_quest
from quest_content import load

MANIFEST = Path(__file__).with_name("quest.json")
ROOT_RESOURCE = r"mod\gq001\phases\gq001.questphase"
JOURNAL_RESOURCE = r"mod\gq001\journal\gq001.journal"
ONSCREEN_RESOURCE = r"mod\gq001\localization\en-us\onscreens\gq001.json"
JOURNAL_RAW = PROJECT / "source/raw/mod/gq001/journal/gq001.journal.json"
JOURNAL_ARCHIVE = PROJECT / "source/archive/mod/gq001/journal/gq001.journal"
ONSCREEN_RAW = (
    PROJECT / "source/raw/mod/gq001/localization/en-us/onscreens/gq001.json.json"
)
ONSCREEN_ARCHIVE = (
    PROJECT / "source/archive/mod/gq001/localization/en-us/onscreens/gq001.json"
)


def generate_journal() -> dict[str, Any]:
    """Compatibility entry point for content inspections and regression tests."""
    return compose(load(MANIFEST)).documents[JOURNAL_RESOURCE]


def generate_onscreens() -> dict[str, Any]:
    """Compatibility entry point for content inspections and regression tests."""
    return compose(load(MANIFEST)).documents[ONSCREEN_RESOURCE]


def main(argv: list[str] | None = None) -> int:
    return build_quest(MANIFEST, ROOT_RESOURCE, argv)


if __name__ == "__main__":
    raise SystemExit(main())
