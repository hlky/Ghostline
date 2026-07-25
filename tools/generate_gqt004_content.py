#!/usr/bin/env python3
"""Generate GQT004 journal/localization and its completing cleanup template."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any

from generate_advanced_quest_block_templates import (
    PhaseGraphBuilder,
    fact_node,
    finish,
    input_node,
    output_node,
    player_vehicle_node,
)
from generate_gqt001_content import Handles, find_entry, load, loc
from ghostline_red import deserialize
from quest_compiler import quest_completion_node

ROOT = Path(__file__).resolve().parents[1]
JOURNAL_TEMPLATE = ROOT / "source/raw/mod/gqt001/journal/gqt001.journal.json"
ONSCREEN_TEMPLATE = (
    ROOT / "source/raw/mod/gqt001/localization/en-us/onscreens/gqt001.json.json"
)
JOURNAL_RAW = ROOT / "source/raw/mod/gqt004/journal/gqt004.journal.json"
JOURNAL_ARCHIVE = ROOT / "source/archive/mod/gqt004/journal/gqt004.journal"
ONSCREEN_RAW = (
    ROOT / "source/raw/mod/gqt004/localization/en-us/onscreens/gqt004.json.json"
)
ONSCREEN_ARCHIVE = (
    ROOT / "source/archive/mod/gqt004/localization/en-us/onscreens/gqt004.json"
)
FINAL_TEMPLATE_RAW = (
    ROOT / "source/raw/mod/gqt004/templates/gqt004_final_cleanup.questphase.json"
)
FINAL_TEMPLATE_ARCHIVE = (
    ROOT / "source/archive/mod/gqt004/templates/gqt004_final_cleanup.questphase"
)

OBJECTIVES = (
    (1, "enter_vehicle", "Enter the contact vehicle.", "#gqt004_01_mp_ride_vehicle"),
    (2, "ride_with_patch", "Ride with Patch.", None),
    (3, "drive_contact", "Drive to the first test point.", "#gqt004_03_mp_ride_destination"),
    (4, "steal_vehicle", "Take the designated test vehicle.", "#gqt004_04_mp_theft_vehicle"),
    (5, "deliver_vehicle", "Deliver the test vehicle.", "#gqt004_05_mp_theft_destination"),
)

TEXT = {
    "gl_gqt004_title": "Vehicle Lab",
    "gl_gqt004_01_objective_enter_vehicle": "Enter the contact vehicle.",
    "gl_gqt004_02_objective_ride_with_patch": "Ride with Patch.",
    "gl_gqt004_03_objective_drive_contact": "Drive to the first test point.",
    "gl_gqt004_04_objective_steal_vehicle": "Take the designated test vehicle.",
    "gl_gqt004_05_objective_deliver_vehicle": "Deliver the test vehicle.",
    "gl_gqt004_description": "Exercise the Ghostline vehicle lifecycle fixtures.",
    "gl_gqt004_mappin": "Vehicle test",
}


def write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def generate_journal() -> dict[str, Any]:
    journal = load(JOURNAL_TEMPLATE)
    handles = Handles(journal)
    quest = find_entry(journal, "gameJournalQuest", "gqt001")
    quest["Data"]["id"] = "gqt004"
    quest["Data"]["title"] = loc("gl_gqt004_title")
    phase_template = find_entry(journal, "gameJournalQuestPhase", "gqt001_01")
    objective_template = find_entry(
        journal, "gameJournalQuestObjective", "gqt001_01_obj_reach_terminal"
    )
    map_template = next(
        item
        for item in objective_template["Data"]["entries"]
        if item["Data"]["$type"] == "gameJournalQuestMapPin"
    )
    description_template = next(
        item
        for item in objective_template["Data"]["entries"]
        if item["Data"]["$type"] == "gameJournalQuestDescription"
    )
    phases = []
    for index, suffix, _, marker in OBJECTIVES:
        phase = handles.clone(phase_template)
        phase["Data"]["id"] = f"gqt004_0{index}"
        objective = handles.clone(objective_template)
        objective["Data"]["id"] = f"gqt004_0{index}_obj_{suffix}"
        objective["Data"]["description"] = loc(
            f"gl_gqt004_0{index}_objective_{suffix}"
        )
        description = handles.clone(description_template)
        description["Data"]["id"] = f"gqt004_0{index}_desc_{suffix}"
        description["Data"]["description"] = loc("gl_gqt004_description")
        objective["Data"]["entries"] = [description]
        if marker:
            pin = handles.clone(map_template)
            pin["Data"]["id"] = f"gqt004_0{index}_qmp_{suffix}"
            pin["Data"]["reference"]["reference"]["$storage"] = "string"
            pin["Data"]["reference"]["reference"]["$value"] = marker
            pin["Data"]["mappinData"]["debugCaption"] = "gl_gqt004_mappin"
            pin["Data"]["mappinData"]["localizedCaption"] = loc(
                "gl_gqt004_mappin"
            )
            objective["Data"]["entries"].insert(0, pin)
        phase["Data"]["entries"] = [objective]
        phases.append(phase)
    quest["Data"]["entries"] = phases

    contacts = find_entry(journal, "gameJournalPrimaryFolderEntry", "contacts")
    contacts["Data"]["entries"] = []
    onscreens = find_entry(journal, "gameJournalFolderEntry", "gqt001")
    onscreens["Data"]["id"] = "gqt004"
    onscreens["Data"]["entries"] = []
    poi = find_entry(
        journal, "gameJournalPointOfInterestMappin", "gqt001_01_poi_terminal"
    )
    poi["Data"]["id"] = "gqt004_01_poi_vehicle"
    poi["Data"]["staticNodeRef"]["$storage"] = "string"
    poi["Data"]["staticNodeRef"]["$value"] = "#gqt004_01_mp_ride_vehicle"
    poi["Data"]["questPath"]["Data"]["realPath"] = "quests/minor_quest/gqt004"
    journal["Header"]["ArchiveFileName"] = str(JOURNAL_ARCHIVE.resolve())
    journal["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return journal


def generate_onscreens() -> dict[str, Any]:
    result = load(ONSCREEN_TEMPLATE)
    result["Data"]["RootChunk"]["root"]["Data"]["entries"] = [
        {
            "$type": "localizationPersistenceOnScreenEntry",
            "femaleVariant": text,
            "maleVariant": "",
            "primaryKey": "0",
            "secondaryKey": key,
        }
        for key, text in TEXT.items()
    ]
    result["Header"]["ArchiveFileName"] = str(ONSCREEN_ARCHIVE.resolve())
    result["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return result


def generate_final_cleanup() -> dict[str, Any]:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    cleanup = player_vehicle_node(
        builder, 10, "{{player_vehicle_record}}", despawn=True
    )
    completed = fact_node(builder, 11, "{{completion_fact}}")
    quest_done = quest_completion_node(
        builder, 12, "quests/minor_quest/gqt004"
    )
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--deserialize", action="store_true")
    args = parser.parse_args()
    outputs = (
        (JOURNAL_RAW, JOURNAL_ARCHIVE, generate_journal()),
        (ONSCREEN_RAW, ONSCREEN_ARCHIVE, generate_onscreens()),
        (FINAL_TEMPLATE_RAW, FINAL_TEMPLATE_ARCHIVE, generate_final_cleanup()),
    )
    for raw, archive, document in outputs:
        write(raw, document)
        if args.deserialize:
            deserialize(raw, archive)
        print(raw)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
