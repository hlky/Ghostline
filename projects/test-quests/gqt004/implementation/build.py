#!/usr/bin/env python3
"""Generate GQT004 journal/localization and its completing cleanup template."""

from __future__ import annotations

import argparse
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

from generate_advanced_quest_block_templates import (
    PhaseGraphBuilder,
    fact_node,
    finish,
    input_node,
    output_node,
    player_vehicle_node,
)
from quest_authoring import compose as compose_quest, resolve_bindings
from quest_compiler import QuestArtifact, compile_manifest_artifacts
from quest_build import publish_build, relocate_artifacts
from quest_content import load
from quest_compiler import quest_completion_node

MANIFEST = PROJECT / "gqt004_vehicle_lab.quest.json"
ROOT_RAW = PROJECT / "source/raw/mod/gqt004/phases/gqt004_vehicle_lab.questphase.json"
ROOT_ARCHIVE = PROJECT / "source/archive/mod/gqt004/phases/gqt004_vehicle_lab.questphase"

JOURNAL_RAW = PROJECT / "source/raw/mod/gqt004/journal/gqt004.journal.json"
JOURNAL_ARCHIVE = PROJECT / "source/archive/mod/gqt004/journal/gqt004.journal"
ONSCREEN_RAW = (
    PROJECT / "source/raw/mod/gqt004/localization/en-us/onscreens/gqt004.json.json"
)
ONSCREEN_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt004/localization/en-us/onscreens/gqt004.json"
)
FINAL_TEMPLATE_RAW = (
    PROJECT / "source/raw/mod/gqt004/templates/gqt004_final_cleanup.questphase.json"
)
FINAL_TEMPLATE_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt004/templates/gqt004_final_cleanup.questphase"
)


def generate_journal() -> dict[str, Any]:
    return compose_quest(load(MANIFEST)).documents[r"mod\gqt004\journal\gqt004.journal"]


def generate_onscreens() -> dict[str, Any]:
    return compose_quest(load(MANIFEST)).documents[
        r"mod\gqt004\localization\en-us\onscreens\gqt004.json"
    ]


def generate_final_cleanup(bindings: dict[str, Any] | None = None) -> dict[str, Any]:
    bindings = resolve_bindings(load(MANIFEST)) if bindings is None else bindings
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    cleanup = player_vehicle_node(
        builder, 10, "{{player_vehicle_record}}", despawn=True
    )
    completed = fact_node(builder, 11, "{{completion_fact}}")
    quest_done = quest_completion_node(builder, 12, bindings["quest"]["path"])
    builder.connect(start, cleanup)
    builder.connect(cleanup, completed)
    builder.connect(completed, quest_done, destination_socket="Succeeded")
    finish(builder, quest_done, end)
    result = {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": "1970-01-01T00:00:00Z",
            "DataType": "CR2W",
            "ArchiveFileName": str(FINAL_TEMPLATE_ARCHIVE.resolve()),
        },
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {
                "$type": "questQuestPhaseResource",
                "cookingPlatform": "PLATFORM_PC",
                "graph": builder.graph,
                "phasePrefabs": [],
            },
            "EmbeddedFiles": [],
        },
    }
    return result


def build_artifacts(output_root: Path | None = None) -> list[QuestArtifact]:
    bindings = resolve_bindings(load(MANIFEST))
    template = generate_final_cleanup(bindings)
    artifacts = compile_manifest_artifacts(
        MANIFEST,
        ROOT_RAW,
        ROOT_ARCHIVE,
        template_documents={
            r"mod\gqt004\templates\gqt004_final_cleanup.questphase": template
        },
    )
    artifacts.append(
        QuestArtifact(FINAL_TEMPLATE_RAW, FINAL_TEMPLATE_ARCHIVE, template)
    )
    return relocate_artifacts(artifacts, output_root)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-root",
        "--out-root",
        type=Path,
        help="Stage a complete candidate under this root",
    )
    parser.add_argument("--deserialize", action="store_true")
    args = parser.parse_args(argv)
    outputs = publish_build(
        build_artifacts(),
        namespace="gqt004",
        output_root=args.output_root,
        deserialize=args.deserialize,
    )
    for raw, _archive in outputs:
        print(raw)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
