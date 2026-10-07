#!/usr/bin/env python3
"""Build GQT003 phases, journal, and localization as one validated artifact set."""

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
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from quest_content import load
from quest_build import main as build_quest
from quest_authoring import compose as compose_quest


JOURNAL_RAW = PROJECT / "source/raw/mod/gqt003/journal/gqt003.journal.json"
JOURNAL_ARCHIVE = PROJECT / "source/archive/mod/gqt003/journal/gqt003.journal"
ONSCREEN_RAW = (
    PROJECT / "source/raw/mod/gqt003/localization/en-us/onscreens/gqt003.json.json"
)
ONSCREEN_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt003/localization/en-us/onscreens/gqt003.json"
)
MANIFEST = PROJECT / "gqt003_extract_and_hold.quest.json"
ROOT_RAW = PROJECT / "source/raw/mod/gqt003/phases/gqt003_extract_and_hold.questphase.json"
ROOT_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt003/phases/gqt003_extract_and_hold.questphase"
)


def generate_journal() -> dict[str, Any]:
    authored = compose_quest(
        load(PROJECT / "gqt003_extract_and_hold.quest.json")
    )
    return authored.documents[r"mod\gqt003\journal\gqt003.journal"]


def generate_onscreens() -> dict[str, Any]:
    authored = compose_quest(
        load(PROJECT / "gqt003_extract_and_hold.quest.json")
    )
    return authored.documents[r"mod\gqt003\localization\en-us\onscreens\gqt003.json"]


def main() -> int:
    return build_quest(
        MANIFEST, r"mod\gqt003\phases\gqt003_extract_and_hold.questphase"
    )


if __name__ == "__main__":
    raise SystemExit(main())
