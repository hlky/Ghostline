#!/usr/bin/env python3
"""Generate the compound GQT002 stealth-and-plant runtime harness."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any

from generate_advanced_quest_block_templates import (
    ACTION,
    COMPLETION_FACT,
    COMPLETION_FUNCTION,
    CONTROLLER,
    DEVICE,
    FAILURE_FACT,
    ITEM,
    OBJECTIVE,
    PhaseGraphBuilder,
    device_condition,
    device_manager,
    fact_node,
    finish,
    input_node,
    mappin_node,
    objective_node,
    output_node,
    remove_item_node,
)
from generate_cache_phase import attitude_group_node, logical_and_node
from generate_delivery_phase import fact_condition_node, logical_xor_node
from generate_gqt001_content import Handles, find_entry, load, loc
from generate_world import (
    DeviceRegistryEntry,
    Vec3,
    cname,
    device_registry,
    full_node_ref,
    node_data,
    node_ref,
    node_ref_hash,
    streaming_sector,
)
from ghostline_red import deserialize
from quest_compiler import (
    add_item_node,
    build_stage_phase,
    character_spawned_node,
    community_action_node,
    load_spec,
    phase_node,
    quest_completion_node,
    stage_template_resource,
)


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "source/quests/tests/gqt002_quiet_install.quest.json"

JOURNAL_TEMPLATE = ROOT / "source/raw/mod/gqt003/journal/gqt003.journal.json"
JOURNAL_BINARY_TEMPLATE = ROOT / "source/archive/mod/gqt003/journal/gqt003.journal"
ONSCREEN_TEMPLATE = ROOT / "source/raw/mod/gqt003/localization/en-us/onscreens/gqt003.json.json"
ONSCREEN_BINARY_TEMPLATE = ROOT / "source/archive/mod/gqt004/localization/en-us/onscreens/gqt004.json"
LAPTOP_TEMPLATE = ROOT / "source/raw/mod/gqt001/world/gqt001_laptop_instance.streamingsector.json"
COMBAT_PHASE_TEMPLATE = (
    ROOT
    / "reference/vanilla_quest_blocks/cr2w/base/open_world/street_stories"
    / "heywood/vista_del_rey/sts_hey_rey_09/phases/sts_hey_rey_09_combat.questphase"
)
ROOT_PHASE_TEMPLATE = (
    ROOT
    / "source/archive/mod/gqt002/phases"
    / "gqt002_quiet_install.questphase"
)
QUEST_SECTOR_TEMPLATE = ROOT / "source/archive/mod/gq002/world/gq002_machine_stops.streamingsector"
ALWAYS_SECTOR_TEMPLATE = ROOT / "source/archive/mod/gqt003/world/gqt003_always_loaded.streamingsector"
DEVICE_REGISTRY_TEMPLATE = ROOT / "source/archive/mod/gqt001/world/gqt001_custom_devices.devices"
SECURITY_NODE_REFERENCE = (
    ROOT
    / "reference/world/ambient-terminals/exterior_-18_28_0_0.streamingsector.json"
)
WORLD_SPEC = ROOT / "tools/gqt002_quiet_install.world.json"

JOURNAL_RAW = ROOT / "source/raw/mod/gqt002/journal/gqt002.journal.json"
JOURNAL_ARCHIVE = ROOT / "source/archive/mod/gqt002/journal/gqt002.journal"
ONSCREEN_RAW = ROOT / "source/raw/mod/gqt002/localization/en-us/onscreens/gqt002.json.json"
ONSCREEN_ARCHIVE = ROOT / "source/archive/mod/gqt002/localization/en-us/onscreens/gqt002.json"
PLANT_TEMPLATE_RAW = ROOT / "source/raw/mod/gqt002/templates/gqt002_guarded_plant.questphase.json"
PLANT_TEMPLATE_ARCHIVE = ROOT / "source/archive/mod/gqt002/templates/gqt002_guarded_plant.questphase"
DETECT_RAW = ROOT / "source/raw/mod/gqt002/phases/gqt002_detect_guards.questphase.json"
DETECT_ARCHIVE = ROOT / "source/archive/mod/gqt002/phases/gqt002_detect_guards.questphase"
ROOT_RAW = ROOT / "source/raw/mod/gqt002/phases/gqt002_quiet_install.questphase.json"
ROOT_ARCHIVE = ROOT / "source/archive/mod/gqt002/phases/gqt002_quiet_install.questphase"
LAPTOP_RAW = ROOT / "source/raw/mod/gqt002/world/gqt002_laptop_instance.streamingsector.json"
LAPTOP_ARCHIVE = ROOT / "source/archive/mod/gqt002/world/gqt002_laptop_instance.streamingsector"
BLOCK_RAW = ROOT / "source/raw/mod/gqt002/world/gqt002_quiet_install.streamingblock.json"
BLOCK_ARCHIVE = ROOT / "source/archive/mod/gqt002/world/gqt002_quiet_install.streamingblock"
DEVICE_REGISTRY_RAW = ROOT / "source/raw/mod/gqt002/world/gqt002_custom_devices.devices.json"
DEVICE_REGISTRY_ARCHIVE = ROOT / "source/archive/mod/gqt002/world/gqt002_custom_devices.devices"
QUEST_SECTOR_RAW = ROOT / "source/raw/mod/gqt002/world/gqt002_quiet_install.streamingsector.json"
QUEST_SECTOR_ARCHIVE = ROOT / "source/archive/mod/gqt002/world/gqt002_quiet_install.streamingsector"
ALWAYS_SECTOR_RAW = ROOT / "source/raw/mod/gqt002/world/gqt002_always_loaded.streamingsector.json"
ALWAYS_SECTOR_ARCHIVE = ROOT / "source/archive/mod/gqt002/world/gqt002_always_loaded.streamingsector"
SECURITY_SECTOR_RAW = ROOT / "source/raw/mod/gqt002/world/gqt002_security.streamingsector.json"
SECURITY_SECTOR_ARCHIVE = ROOT / "source/archive/mod/gqt002/world/gqt002_security.streamingsector"

PREFAB = "#gqt002_pr_quiet_install"
GUARD_COMMUNITY = "#gqt002_01_com_guards"
SECURITY_SYSTEM = "#gqt002_01_dvc_security_system"
SECURITY_AREA = "#gqt002_01_dvc_security_area"
TARGET_REF = "$/mod/gqt002/#gqt002_pr_quiet_install/#gqt002_02_computer_target_r2"
OLD_TARGET_REF = "$/mod/gqt001/#gqt001_pr_signal_delay/#gqt001_terminal_laptop_r2"
GUARD_ENTRIES = ("guard_ranged_m", "guard_ranged_f", "guard_melee")
TARGET_POSITION = {"X": -1052.1395, "Y": 1283.3362, "Z": 12.46019}
TARGET_ORIENTATION = {"i": 0.0, "j": 0.0, "k": -0.4137633, "r": 0.9103846}
PLANT_MAPPIN = (
    "quests/minor_quest/gqt002/gqt002_02/"
    "gqt002_02_obj_plant_keylogger/gqt002_02_qmp_target"
)
ITEM_RECORD = "Items.GhostlineGQT002Keylogger"

TEXT = {
    "gl_gqt002_title": "Quiet Install",
    "gl_gqt002_01_objective_remain_undetected": "Remain undetected.",
    "gl_gqt002_02_objective_plant_keylogger": "Plant the keylogger on the guarded computer.",
    "gl_gqt002_description": "Reach the elevated terminal and install the Ghostline package without alerting its guards.",
    "gl_gqt002_mappin": "Guarded computer",
    "gl_gqt002_item_keylogger_name": "Ghostline Keylogger",
    "gl_gqt002_installing_keylogger": "INSTALLING KEYLOGGER...",
    "gl_gqt002_do_not_disconnect": "DO NOT DISCONNECT",
}


def write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def phase_document(builder: PhaseGraphBuilder, archive: Path, *, prefab: bool = False) -> dict[str, Any]:
    return {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": "1970-01-01T00:00:00Z",
            "DataType": "CR2W",
            "ArchiveFileName": str(archive.resolve()),
        },
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {
                "$type": "questQuestPhaseResource",
                "cookingPlatform": "PLATFORM_PC",
                "graph": builder.graph,
                "inplacePhases": [],
                "phasePrefabs": (
                    [{"$type": "questQuestPrefabEntry", "prefabNodeRef": {"$type": "NodeRef", "$storage": "string", "$value": PREFAB}}]
                    if prefab
                    else []
                ),
            },
            "EmbeddedFiles": [],
        },
    }


def generate_journal() -> dict[str, Any]:
    journal = load(JOURNAL_TEMPLATE)
    handles = Handles(journal)
    quest = find_entry(journal, "gameJournalQuest", "gqt003")
    quest["Data"]["id"] = "gqt002"
    quest["Data"]["title"] = loc("gl_gqt002_title")
    phase_template = find_entry(journal, "gameJournalQuestPhase", "gqt003_01")
    objective_template = find_entry(
        journal, "gameJournalQuestObjective", "gqt003_01_obj_reach_relay"
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
    objectives = (
        (1, "remain_undetected", True, None),
        (2, "plant_keylogger", False, "#gqt002_02_mp_target"),
    )
    for index, suffix, optional, marker in objectives:
        phase = handles.clone(phase_template)
        phase["Data"]["id"] = f"gqt002_0{index}"
        objective = handles.clone(objective_template)
        objective["Data"]["id"] = f"gqt002_0{index}_obj_{suffix}"
        objective["Data"]["description"] = loc(
            f"gl_gqt002_0{index}_objective_{suffix}"
        )
        objective["Data"]["optional"] = int(optional)
        description = handles.clone(description_template)
        description["Data"]["id"] = f"gqt002_0{index}_desc_{suffix}"
        description["Data"]["description"] = loc("gl_gqt002_description")
        objective["Data"]["entries"] = [description]
        if marker:
            pin = handles.clone(map_template)
            pin["Data"]["id"] = "gqt002_02_qmp_target"
            pin["Data"]["reference"]["reference"]["$storage"] = "string"
            pin["Data"]["reference"]["reference"]["$value"] = marker
            pin["Data"]["mappinData"]["debugCaption"] = "gl_gqt002_mappin"
            pin["Data"]["mappinData"]["localizedCaption"] = loc("gl_gqt002_mappin")
            objective["Data"]["entries"] = [pin, description]
        phase["Data"]["entries"] = [objective]
        phases.append(phase)
    quest["Data"]["entries"] = phases

    find_entry(journal, "gameJournalPrimaryFolderEntry", "contacts")["Data"]["entries"] = []
    onscreens = find_entry(journal, "gameJournalFolderEntry", "gqt003")
    onscreens["Data"]["id"] = "gqt002"
    onscreens["Data"]["entries"] = []
    poi = find_entry(journal, "gameJournalPointOfInterestMappin", "gqt003_01_poi_relay")
    poi["Data"]["id"] = "gqt002_02_poi_target"
    poi["Data"]["staticNodeRef"]["$storage"] = "string"
    poi["Data"]["staticNodeRef"]["$value"] = "#gqt002_02_mp_target"
    poi["Data"]["questPath"]["Data"]["realPath"] = "quests/minor_quest/gqt002"
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


def progress_bar_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    *,
    duration: float,
    text: str,
    bottom_text: str,
):
    node_type = builder.handles.wrap(
        {
            "$type": "questProgressBar_NodeType",
            "bottomText": loc(bottom_text),
            "duration": duration,
            "show": 1,
            "text": loc(text),
            "type": "Undefined",
        }
    )
    return builder.node(
        quest_id,
        "questUIManagerNodeDefinition",
        input_names=("In",),
        properties={"type": node_type},
    )


def generate_guarded_plant() -> dict[str, Any]:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    active = objective_node(builder, 10, OBJECTIVE)
    pin_on = mappin_node(builder, 11, PLANT_MAPPIN)
    connected = device_condition(
        builder, 12, DEVICE, CONTROLLER, COMPLETION_FUNCTION
    )
    progress = progress_bar_node(
        builder,
        13,
        duration=5.0,
        text="gl_gqt002_installing_keylogger",
        bottom_text="gl_gqt002_do_not_disconnect",
    )
    disconnect = device_manager(
        builder,
        14,
        DEVICE,
        "ScriptableDeviceComponentPS",
        ACTION,
    )
    remove = remove_item_node(builder, 15, ITEM)
    done = objective_node(builder, 16, OBJECTIVE)
    pin_off = mappin_node(builder, 17, PLANT_MAPPIN)
    fact = fact_node(builder, 18, COMPLETION_FACT)
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, pin_on, destination_socket="Active")
    builder.connect(pin_on, connected)
    builder.connect(connected, progress)
    builder.connect(progress, disconnect)
    builder.connect(disconnect, remove)
    builder.connect(remove, done, destination_socket="Succeeded")
    builder.connect(done, pin_off, destination_socket="Inactive")
    builder.connect(pin_off, fact)
    finish(builder, fact, end)
    return phase_document(builder, PLANT_TEMPLATE_ARCHIVE)


def generate_detection_phase() -> dict[str, Any]:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    detected = device_condition(
        builder,
        10,
        SECURITY_SYSTEM,
        "SecuritySystemControllerPS",
        "IsSystemInCombat",
    )
    stopped = fact_condition_node(builder, 11, "gqt002_plant_complete")
    failed = fact_node(builder, 12, "gqt002_stealth_failed")
    join = logical_xor_node(builder, 13, input_count=2)
    builder.connect(start, detected)
    builder.connect(start, stopped)
    builder.connect(detected, failed)
    builder.connect(failed, join, destination_socket="In1")
    builder.connect(stopped, join, destination_socket="In2")
    finish(builder, join, end, source_socket="Out1")
    return phase_document(builder, DETECT_ARCHIVE)


def generate_root_phase() -> dict[str, Any]:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    activate = community_action_node(builder, 10, GUARD_COMMUNITY, "Activate")
    spawned = character_spawned_node(builder, 11, GUARD_COMMUNITY)
    guard_attitudes = tuple(
        (
            attitude_group_node(
                builder,
                12 + index * 2,
                entry,
                "neutral",
                community_ref=GUARD_COMMUNITY,
            ),
            attitude_group_node(
                builder,
                13 + index * 2,
                entry,
                "hostile",
                community_ref=GUARD_COMMUNITY,
            ),
        )
        for index, entry in enumerate(GUARD_ENTRIES)
    )
    item = add_item_node(builder, 18, ITEM_RECORD, 1)
    detector = phase_node(builder, 19, r"mod\gqt002\phases\gqt002_detect_guards.questphase")
    monitor = phase_node(builder, 20, r"mod\gqt002\phases\gqt002_remain_undetected.questphase")
    plant = phase_node(builder, 21, r"mod\gqt002\phases\gqt002_plant_keylogger.questphase")
    join = logical_and_node(builder, 22, 3)
    deactivate = community_action_node(builder, 23, GUARD_COMMUNITY, "Deactivate")
    quest_done = quest_completion_node(builder, 24, "quests/minor_quest/gqt002")
    completed = fact_node(builder, 25, "gqt002_completed")
    builder.connect(start, activate)
    builder.connect(activate, spawned)
    previous = spawned
    for neutral, hostile in guard_attitudes:
        builder.connect(previous, neutral)
        builder.connect(neutral, hostile)
        previous = hostile
    builder.connect(previous, item)
    for child in (detector, monitor, plant):
        builder.connect(item, child, destination_socket="In1")
    builder.connect(detector, join, source_socket="Out1", destination_socket="In1")
    builder.connect(monitor, join, source_socket="Out1", destination_socket="In2")
    builder.connect(plant, join, source_socket="Out1", destination_socket="In3")
    builder.connect(join, deactivate, source_socket="Out1")
    builder.connect(deactivate, quest_done, destination_socket="Succeeded")
    builder.connect(quest_done, completed)
    finish(builder, completed, end)
    return phase_document(builder, ROOT_ARCHIVE, prefab=True)


def replace_string(value: Any, old: str, new: str) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if child == old:
                value[key] = new
            else:
                replace_string(child, old, new)
    elif isinstance(value, list):
        for child in value:
            replace_string(child, old, new)


def generate_laptop() -> dict[str, Any]:
    sector = load(LAPTOP_TEMPLATE)
    replace_string(sector, OLD_TARGET_REF, TARGET_REF)
    root = sector["Data"]["RootChunk"]
    node_data = root["nodeData"]["Data"][0]
    node_data["Position"].update(TARGET_POSITION)
    node_data["Orientation"].update(TARGET_ORIENTATION)
    for bound in ("Min", "Max"):
        node_data["Bounds"][bound].update(TARGET_POSITION)
    node = root["nodes"][0]
    node["Data"]["debugName"]["$value"] = "{gqt002_keylogger_laptop}"
    package = node["Data"]["instanceData"]["Data"]["buffer"]["Data"]
    for chunk in package["Chunks"]:
        persistent = chunk.get("persistentState", {}).get("Data", {})
        if persistent.get("$type") == "ComputerControllerPS":
            persistent["hasPersonalLinkSlot"] = 0
            persistent["personalLinkCustomInteraction"] = {
                "$type": "TweakDBID",
                "$storage": "string",
                "$value": "Interactions.StealData",
            }
            persistent["markAsQuest"] = 1
            persistent["isKeyloggerInstalled"] = 0
            persistent["deviceState"] = "ON"
    sector["Header"]["ArchiveFileName"] = str(LAPTOP_ARCHIVE.resolve())
    sector["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return sector


def generate_security_sector() -> dict[str, Any]:
    world = load(WORLD_SPEC)
    security = world["security"]
    reference = load(SECURITY_NODE_REFERENCE)
    reference_nodes = reference["Data"]["RootChunk"]["nodes"]
    system = copy.deepcopy(reference_nodes[923])
    area = copy.deepcopy(reference_nodes[927])

    prefab_root = world["prefab_root"]
    system_ref = full_node_ref(prefab_root, security["system_ref"])
    area_ref = full_node_ref(prefab_root, security["area_ref"])
    community_ref = full_node_ref(prefab_root, GUARD_COMMUNITY)

    system_data = system["Data"]
    system_data["debugName"] = cname("{gqt002_security_system}")
    system_data["deviceConnections"] = [
        {
            "$type": "worldDeviceConnections",
            "deviceClassName": cname("SecurityAreaControllerPS"),
            "nodeRefs": [node_ref(area_ref)],
        },
        {
            "$type": "worldDeviceConnections",
            "deviceClassName": cname("CommunityProxyPS"),
            "nodeRefs": [node_ref(community_ref)],
        }
    ]

    area_data = area["Data"]
    area_data["debugName"] = cname("{gqt002_security_area}")
    area_data["deviceConnections"] = [
        {
            "$type": "worldDeviceConnections",
            "deviceClassName": cname("CommunityProxyPS"),
            "nodeRefs": [node_ref(community_ref)],
        }
    ]
    for chunk in area_data["instanceData"]["Data"]["buffer"]["Data"]["Chunks"]:
        if chunk.get("$type") == "gameStaticTriggerAreaComponent":
            outline = chunk["outline"]["Data"]
            outline["buffer"] = ""
            outline["height"] = float(security["outline"]["height"])
            outline["points"] = [
                {
                    "$type": "Vector3",
                    "X": float(point["x"]),
                    "Y": float(point["y"]),
                    "Z": float(point["z"]),
                }
                for point in security["outline"]["points"]
            ]
        persistent = chunk.get("persistentState", {}).get("Data", {})
        if persistent.get("$type") == "SecurityAreaControllerPS":
            persistent["securityAreaType"] = security["type"]
            persistent["deviceState"] = "ON"

    position = Vec3(
        float(security["position"]["x"]),
        float(security["position"]["y"]),
        float(security["position"]["z"]),
    )
    overrides = security.get("node_data", {})
    sector = streaming_sector(
        "Quest",
        0,
        SECURITY_SECTOR_ARCHIVE,
        [
            node_data(0, system_ref, position, 0.0, overrides),
            node_data(1, area_ref, position, 0.0, overrides),
        ],
        [system_ref, area_ref],
        [system, area],
    )
    sector["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return sector


def generate_block() -> dict[str, Any]:
    block = load(BLOCK_RAW)
    descriptors = block["Data"]["RootChunk"]["descriptors"]
    laptop_path = r"mod\gqt002\world\gqt002_laptop_instance.streamingsector"
    security_path = r"mod\gqt002\world\gqt002_security.streamingsector"
    descriptors[:] = [
        descriptor
        for descriptor in descriptors
        if descriptor["data"]["DepotPath"].get("$value")
        not in {laptop_path, security_path}
    ]
    always_template = next(
        item
        for item in descriptors
        if item["data"]["DepotPath"].get("$value")
        == r"mod\gqt002\world\gqt002_always_loaded.streamingsector"
    )
    quest_template = next(
        item
        for item in descriptors
        if item["data"]["DepotPath"].get("$value")
        == r"mod\gqt002\world\gqt002_quiet_install.streamingsector"
    )
    laptop_descriptor = copy.deepcopy(always_template)
    laptop_descriptor["data"]["DepotPath"]["$value"] = laptop_path
    laptop_descriptor["questPrefabNodeRef"] = {
        "$type": "NodeRef",
        "$storage": "uint64",
        "$value": "0",
    }
    security_descriptor = copy.deepcopy(quest_template)
    security_descriptor["data"]["DepotPath"]["$value"] = security_path
    descriptors.extend((laptop_descriptor, security_descriptor))
    block["Header"]["ArchiveFileName"] = str(BLOCK_ARCHIVE.resolve())
    block["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return block


def generate_device_registry() -> dict[str, Any]:
    world = load(WORLD_SPEC)
    security = world["security"]
    security_position = Vec3(
        float(security["position"]["x"]),
        float(security["position"]["y"]),
        float(security["position"]["z"]),
    )
    prefab_root = world["prefab_root"]
    system_ref = full_node_ref(prefab_root, security["system_ref"])
    area_ref = full_node_ref(prefab_root, security["area_ref"])
    return device_registry(
        DEVICE_REGISTRY_ARCHIVE,
        [
            DeviceRegistryEntry(
                node_ref=TARGET_REF,
                node_hash=node_ref_hash(TARGET_REF),
                controller_class="ComputerControllerPS",
                position=Vec3(TARGET_POSITION["X"], TARGET_POSITION["Y"], TARGET_POSITION["Z"]),
            ),
            DeviceRegistryEntry(
                node_ref=system_ref,
                node_hash=node_ref_hash(system_ref),
                controller_class="SecuritySystemControllerPS",
                position=security_position,
            ),
            DeviceRegistryEntry(
                node_ref=area_ref,
                node_hash=node_ref_hash(area_ref),
                controller_class="SecurityAreaControllerPS",
                position=security_position,
            ),
        ],
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--deserialize", action="store_true")
    args = parser.parse_args()
    outputs = (
        (JOURNAL_RAW, JOURNAL_ARCHIVE, JOURNAL_BINARY_TEMPLATE, generate_journal()),
        (ONSCREEN_RAW, ONSCREEN_ARCHIVE, ONSCREEN_BINARY_TEMPLATE, generate_onscreens()),
        (
            PLANT_TEMPLATE_RAW,
            PLANT_TEMPLATE_ARCHIVE,
            PLANT_TEMPLATE_ARCHIVE,
            generate_guarded_plant(),
        ),
        (DETECT_RAW, DETECT_ARCHIVE, COMBAT_PHASE_TEMPLATE, generate_detection_phase()),
        (ROOT_RAW, ROOT_ARCHIVE, ROOT_PHASE_TEMPLATE, generate_root_phase()),
        (LAPTOP_RAW, LAPTOP_ARCHIVE, LAPTOP_ARCHIVE, generate_laptop()),
        (QUEST_SECTOR_RAW, QUEST_SECTOR_ARCHIVE, QUEST_SECTOR_TEMPLATE, load(QUEST_SECTOR_RAW)),
        (ALWAYS_SECTOR_RAW, ALWAYS_SECTOR_ARCHIVE, ALWAYS_SECTOR_TEMPLATE, load(ALWAYS_SECTOR_RAW)),
        (
            SECURITY_SECTOR_RAW,
            SECURITY_SECTOR_ARCHIVE,
            SECURITY_SECTOR_ARCHIVE,
            generate_security_sector(),
        ),
        (BLOCK_RAW, BLOCK_ARCHIVE, BLOCK_ARCHIVE, generate_block()),
        (
            DEVICE_REGISTRY_RAW,
            DEVICE_REGISTRY_ARCHIVE,
            DEVICE_REGISTRY_TEMPLATE,
            generate_device_registry(),
        ),
    )
    for raw, archive, template, document in outputs:
        write(raw, document)
        if args.deserialize:
            deserialize(raw, archive, template=template)
        print(raw)
    spec, diagnostics = load_spec(MANIFEST)
    errors = [item for item in diagnostics if item.level == "error"]
    if spec is None or errors:
        raise RuntimeError(
            "GQT002 manifest cannot instantiate child phases: "
            + "; ".join(item.message for item in errors)
        )
    for stage in spec.stages:
        archive = ROOT / "source/archive" / Path(*stage.phase_resource.split("\\"))
        raw = ROOT / "source/raw" / Path(f"{stage.phase_resource}.json")
        document = build_stage_phase(stage, archive, spec.phase_prefabs)
        write(raw, document)
        if args.deserialize:
            template_resource = stage_template_resource(stage)
            template = (
                ROOT / "source/archive" / Path(*template_resource.split("\\"))
                if template_resource
                else None
            )
            deserialize(raw, archive, template=template)
        print(raw)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
