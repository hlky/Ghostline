#!/usr/bin/env python3
"""Generate GQT003 journal, localization, and escort/defend harness templates."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from generate_advanced_quest_block_templates import (
    COMMUNITY,
    COMPLETION_FACT,
    DESTINATION_1,
    DESTINATION_2,
    DESTINATION_3,
    ENTRY,
    ESCORT_MAPPIN_1,
    ESCORT_MAPPIN_2,
    ESCORT_MAPPIN_3,
    FAILURE_FACT,
    PhaseGraphBuilder,
    assign_follower_role,
    character_killed,
    clear_ai_role,
    entity_reference,
    fact_node,
    finish,
    input_node,
    mappin_node,
    objective_node,
    output_node,
    puppet_ai_tier,
    trigger_condition,
)
from generate_cache_phase import realtime_delay_node
from generate_delivery_phase import fact_condition_node, logical_xor_node
from generate_gqt001_content import Handles, find_entry, load, loc
from ghostline_red import deserialize
from quest_compiler import (
    character_spawned_node,
    combat_threat_node,
    community_action_node,
    quest_completion_node,
)


ROOT = Path(__file__).resolve().parents[1]
JOURNAL_TEMPLATE = ROOT / "source/raw/mod/gqt004/journal/gqt004.journal.json"
JOURNAL_BINARY_TEMPLATE = ROOT / "source/archive/mod/gqt004/journal/gqt004.journal"
ONSCREEN_TEMPLATE = (
    ROOT / "source/raw/mod/gqt004/localization/en-us/onscreens/gqt004.json.json"
)
ONSCREEN_BINARY_TEMPLATE = (
    ROOT / "source/archive/mod/gqt004/localization/en-us/onscreens/gqt004.json"
)
RICH_PHASE_TEMPLATE = (
    ROOT
    / "reference/vanilla_quest_blocks/cr2w/base/open_world/street_stories"
    / "watson/kabuki/sts_wat_kab_02/phases/sts_wat_kab_02_openworld.questphase"
)
COMBAT_PHASE_TEMPLATE = (
    ROOT
    / "reference/vanilla_quest_blocks/cr2w/base/open_world/street_stories"
    / "heywood/vista_del_rey/sts_hey_rey_09/phases/sts_hey_rey_09_combat.questphase"
)

JOURNAL_RAW = ROOT / "source/raw/mod/gqt003/journal/gqt003.journal.json"
JOURNAL_ARCHIVE = ROOT / "source/archive/mod/gqt003/journal/gqt003.journal"
ONSCREEN_RAW = (
    ROOT / "source/raw/mod/gqt003/localization/en-us/onscreens/gqt003.json.json"
)
ONSCREEN_ARCHIVE = (
    ROOT / "source/archive/mod/gqt003/localization/en-us/onscreens/gqt003.json"
)
HOLD_TEMPLATE_RAW = (
    ROOT / "source/raw/mod/gqt003/templates/gqt003_timed_defend.questphase.json"
)
HOLD_TEMPLATE_ARCHIVE = (
    ROOT / "source/archive/mod/gqt003/templates/gqt003_timed_defend.questphase"
)
ESCORT_TEMPLATE_RAW = (
    ROOT / "source/raw/mod/gqt003/templates/gqt003_escort_retain.questphase.json"
)
ESCORT_TEMPLATE_ARCHIVE = (
    ROOT / "source/archive/mod/gqt003/templates/gqt003_escort_retain.questphase"
)

HOLD_SECONDS = 20
ATTACKER_COMMUNITY = "#gqt003_04_com_attackers"
ATTACKER_ENTRIES = ("attacker_ranged_m", "attacker_ranged_f", "attacker_melee")
OBJECTIVES = (
    (1, "reach_relay", "Reach the extraction relay.", "#gqt003_01_mp_relay"),
    (2, "release_patch", "Hack the relay to release Patch.", None),
    (
        3,
        "escort_patch",
        "Escort Patch through the extraction route.",
        (
            "#gqt003_03_mp_gate_01",
            "#gqt003_03_mp_gate_02",
            "#gqt003_03_mp_gate_03",
        ),
    ),
    (4, "defend_patch", f"Hold the position for {HOLD_SECONDS} seconds.", None),
)

TEXT = {
    "gl_gqt003_title": "Extract and Hold",
    "gl_gqt003_01_objective_reach_relay": "Reach the extraction relay.",
    "gl_gqt003_02_objective_release_patch": "Hack the relay to release Patch.",
    "gl_gqt003_03_objective_escort_patch": (
        "Escort Patch through the extraction route."
    ),
    "gl_gqt003_04_objective_defend_patch": (
        f"Hold the position for {HOLD_SECONDS} seconds."
    ),
    "gl_gqt003_description": (
        "Exercise the Ghostline rescue, follower escort, and defend-target fixtures."
    ),
    "gl_gqt003_mappin": "Extraction relay",
}


def write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def generate_journal() -> dict[str, Any]:
    journal = load(JOURNAL_TEMPLATE)
    handles = Handles(journal)
    quest = find_entry(journal, "gameJournalQuest", "gqt004")
    quest["Data"]["id"] = "gqt003"
    quest["Data"]["title"] = loc("gl_gqt003_title")
    phase_template = find_entry(journal, "gameJournalQuestPhase", "gqt004_01")
    objective_template = find_entry(
        journal, "gameJournalQuestObjective", "gqt004_01_obj_enter_vehicle"
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
        phase["Data"]["id"] = f"gqt003_0{index}"
        objective = handles.clone(objective_template)
        objective["Data"]["id"] = f"gqt003_0{index}_obj_{suffix}"
        objective["Data"]["description"] = loc(
            f"gl_gqt003_0{index}_objective_{suffix}"
        )
        description = handles.clone(description_template)
        description["Data"]["id"] = f"gqt003_0{index}_desc_{suffix}"
        description["Data"]["description"] = loc("gl_gqt003_description")
        objective["Data"]["entries"] = [description]
        if marker:
            markers = marker if isinstance(marker, tuple) else (marker,)
            pins = []
            for marker_index, marker_ref in enumerate(markers, start=1):
                pin = handles.clone(map_template)
                pin_suffix = (
                    f"escort_gate_0{marker_index}"
                    if len(markers) > 1
                    else suffix
                )
                pin["Data"]["id"] = f"gqt003_0{index}_qmp_{pin_suffix}"
                pin["Data"]["reference"]["reference"]["$storage"] = "string"
                pin["Data"]["reference"]["reference"]["$value"] = marker_ref
                pin["Data"]["mappinData"]["debugCaption"] = "gl_gqt003_mappin"
                pin["Data"]["mappinData"]["localizedCaption"] = loc(
                    "gl_gqt003_mappin"
                )
                pins.append(pin)
            objective["Data"]["entries"] = pins + objective["Data"]["entries"]
        phase["Data"]["entries"] = [objective]
        phases.append(phase)
    quest["Data"]["entries"] = phases

    contacts = find_entry(journal, "gameJournalPrimaryFolderEntry", "contacts")
    contacts["Data"]["entries"] = []
    onscreens = find_entry(journal, "gameJournalFolderEntry", "gqt004")
    onscreens["Data"]["id"] = "gqt003"
    onscreens["Data"]["entries"] = []
    poi = find_entry(
        journal, "gameJournalPointOfInterestMappin", "gqt004_01_poi_vehicle"
    )
    poi["Data"]["id"] = "gqt003_01_poi_relay"
    poi["Data"]["staticNodeRef"]["$storage"] = "string"
    poi["Data"]["staticNodeRef"]["$value"] = "#gqt003_01_mp_relay"
    poi["Data"]["questPath"]["Data"]["realPath"] = "quests/minor_quest/gqt003"
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


def generate_timed_defend() -> dict[str, Any]:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    active = objective_node(builder, 10, "{{objective}}")
    activate_attackers = community_action_node(
        builder, 11, ATTACKER_COMMUNITY, "Activate"
    )
    attackers_spawned = character_spawned_node(builder, 12, ATTACKER_COMMUNITY)
    threats = [
        combat_threat_node(builder, 13 + index, ATTACKER_COMMUNITY, entry)
        for index, entry in enumerate(ATTACKER_ENTRIES)
    ]
    # Two attackers pressure the protected actor; the third engages V.
    for threat in threats[:2]:
        threat.data["params"]["Data"]["targetPuppetRef"] = entity_reference(
            COMMUNITY, names=(ENTRY,)
        )
    complete = fact_condition_node(
        builder, 16, COMPLETION_FACT, comparison="Greater", value=0
    )
    killed = character_killed(builder, 17, COMMUNITY, ENTRY)
    timer = realtime_delay_node(builder, 18, seconds=HOLD_SECONDS)
    timer_complete = fact_node(builder, 19, COMPLETION_FACT)
    success = objective_node(builder, 20, "{{objective}}")
    success_cleanup = community_action_node(
        builder, 21, ATTACKER_COMMUNITY, "Deactivate"
    )
    success_clear = clear_ai_role(builder, 22, COMMUNITY, ENTRY)
    success_quest = quest_completion_node(
        builder, 23, "quests/minor_quest/gqt003"
    )
    completed = fact_node(builder, 24, "gqt003_completed")
    failure = objective_node(builder, 25, "{{objective}}")
    failure_cleanup = community_action_node(
        builder, 26, ATTACKER_COMMUNITY, "Deactivate"
    )
    failure_quest = quest_completion_node(
        builder, 27, "quests/minor_quest/gqt003"
    )
    failed_fact = fact_node(builder, 28, FAILURE_FACT)
    join = logical_xor_node(builder, 29, input_count=2)

    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, activate_attackers)
    builder.connect(activate_attackers, attackers_spawned)
    builder.connect(attackers_spawned, threats[0])
    builder.connect(threats[0], threats[1], source_socket="Success")
    builder.connect(threats[1], threats[2], source_socket="Success")
    builder.connect(threats[2], complete, source_socket="Success")
    builder.connect(threats[2], killed, source_socket="Success")
    builder.connect(threats[2], timer, source_socket="Success")
    builder.connect(timer, timer_complete)
    builder.connect(complete, success, destination_socket="Succeeded")
    builder.connect(success, success_cleanup)
    builder.connect(success_cleanup, success_clear)
    builder.connect(
        success_clear,
        success_quest,
        source_socket="Success",
        destination_socket="Succeeded",
    )
    builder.connect(success_quest, completed)
    builder.connect(completed, join, destination_socket="In1")
    builder.connect(killed, failure, destination_socket="Failed")
    builder.connect(failure, failure_cleanup)
    builder.connect(failure_cleanup, failure_quest, destination_socket="Failed")
    builder.connect(failure_quest, failed_fact)
    builder.connect(failed_fact, join, destination_socket="In2")
    finish(builder, join, end, source_socket="Out1")

    return {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": "1970-01-01T00:00:00Z",
            "DataType": "CR2W",
            "ArchiveFileName": str(HOLD_TEMPLATE_ARCHIVE.resolve()),
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


def generate_retain_follower_escort() -> dict[str, Any]:
    """Escort through three gates while leaving the follower role for the hold."""

    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    active = objective_node(builder, 10, "{{objective}}")
    pin_1_on = mappin_node(builder, 11, ESCORT_MAPPIN_1)
    ai = puppet_ai_tier(builder, 12, COMMUNITY, ENTRY)
    follow = assign_follower_role(builder, 13, COMMUNITY, ENTRY)
    actor = entity_reference(COMMUNITY, names=(ENTRY,))
    gate_1 = trigger_condition(builder, 14, DESTINATION_1, actor)
    pin_1_off = mappin_node(builder, 15, ESCORT_MAPPIN_1)
    pin_2_on = mappin_node(builder, 16, ESCORT_MAPPIN_2)
    gate_2 = trigger_condition(builder, 17, DESTINATION_2, actor)
    pin_2_off = mappin_node(builder, 18, ESCORT_MAPPIN_2)
    pin_3_on = mappin_node(builder, 19, ESCORT_MAPPIN_3)
    gate_3 = trigger_condition(builder, 20, DESTINATION_3, actor)
    done = objective_node(builder, 21, "{{objective}}")
    pin_3_off = mappin_node(builder, 22, ESCORT_MAPPIN_3)
    fact = fact_node(builder, 23, COMPLETION_FACT)

    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, pin_1_on, destination_socket="Active")
    builder.connect(pin_1_on, ai)
    builder.connect(ai, follow)
    builder.connect(follow, gate_1, source_socket="Success")
    builder.connect(gate_1, pin_1_off, destination_socket="Inactive")
    builder.connect(pin_1_off, pin_2_on, destination_socket="Active")
    builder.connect(pin_2_on, gate_2)
    builder.connect(gate_2, pin_2_off, destination_socket="Inactive")
    builder.connect(pin_2_off, pin_3_on, destination_socket="Active")
    builder.connect(pin_3_on, gate_3)
    builder.connect(gate_3, done, destination_socket="Succeeded")
    builder.connect(done, pin_3_off, destination_socket="Inactive")
    builder.connect(pin_3_off, fact)
    finish(builder, fact, end)

    return {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": "1970-01-01T00:00:00Z",
            "DataType": "CR2W",
            "ArchiveFileName": str(ESCORT_TEMPLATE_ARCHIVE.resolve()),
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--deserialize", action="store_true")
    args = parser.parse_args()
    outputs = (
        (
            JOURNAL_RAW,
            JOURNAL_ARCHIVE,
            JOURNAL_BINARY_TEMPLATE,
            generate_journal(),
        ),
        (
            ONSCREEN_RAW,
            ONSCREEN_ARCHIVE,
            ONSCREEN_BINARY_TEMPLATE,
            generate_onscreens(),
        ),
        (
            HOLD_TEMPLATE_RAW,
            HOLD_TEMPLATE_ARCHIVE,
            COMBAT_PHASE_TEMPLATE,
            generate_timed_defend(),
        ),
        (
            ESCORT_TEMPLATE_RAW,
            ESCORT_TEMPLATE_ARCHIVE,
            RICH_PHASE_TEMPLATE,
            generate_retain_follower_escort(),
        ),
    )
    for raw, archive, template, document in outputs:
        write(raw, document)
        if args.deserialize:
            deserialize(raw, archive, template=template)
        print(raw)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
