#!/usr/bin/env python3
"""Generate the compound GQT002 stealth-and-plant runtime harness."""

from __future__ import annotations

import argparse
import copy
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
    ACTION,
    COMPLETION_FACT,
    COMPLETION_FUNCTION,
    CONTROLLER,
    DEVICE,
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
from phase_graph import (
    logical_and_node as logical_and_node,
)
from generate_cache_phase import (
    attitude_group_node as attitude_group_node,
)
from phase_graph import (
    fact_condition_node as fact_condition_node,
    logical_xor_node as logical_xor_node,
)
from quest_authoring import compose as compose_quest, normalize_spec, resolve_bindings
from quest_compiler import QuestArtifact, compile_manifest_artifacts
from quest_build import publish_build, relocate_artifacts
from quest_content import load, loc
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
from quest_compiler import (
    add_item_node,
    character_spawned_node,
    community_action_node,
    phase_node,
    quest_completion_node,
)


MANIFEST = PROJECT / "gqt002_quiet_install.quest.json"

JOURNAL_BINARY_TEMPLATE = ROOT / "quests/templates/source/archive/mod/ghostline/quest_blocks/donors/journal_large.journal"
ONSCREEN_BINARY_TEMPLATE = (
    ROOT / "quests/templates/source/archive/mod/ghostline/quest_blocks/donors/onscreens.json"
)
LAPTOP_TEMPLATE = (
    ROOT / "quests/templates/source/raw/mod/ghostline/quest_blocks/donors/laptop_instance.streamingsector.json"
)
COMBAT_PHASE_TEMPLATE = (
    ROOT
    / "reference/vanilla_quest_blocks/cr2w/base/open_world/street_stories"
    / "heywood/vista_del_rey/sts_hey_rey_09/phases/sts_hey_rey_09_combat.questphase"
)
ROOT_PHASE_TEMPLATE = (
    PROJECT / "source/archive/mod/gqt002/phases" / "gqt002_quiet_install.questphase"
)
QUEST_SECTOR_TEMPLATE = (
    ROOT / "quests/templates/source/archive/mod/ghostline/quest_blocks/donors/quest_sector.streamingsector"
)
ALWAYS_SECTOR_TEMPLATE = (
    ROOT / "quests/templates/source/archive/mod/ghostline/quest_blocks/donors/always_loaded.streamingsector"
)
DEVICE_REGISTRY_TEMPLATE = (
    ROOT / "quests/templates/source/archive/mod/ghostline/quest_blocks/donors/custom_devices.devices"
)
SECURITY_NODE_REFERENCE = (
    ROOT / "reference/world/ambient-terminals/exterior_-18_28_0_0.streamingsector.json"
)
WORLD_SPEC = PROJECT / "implementation/world/quiet-install.world.json"

JOURNAL_RAW = PROJECT / "source/raw/mod/gqt002/journal/gqt002.journal.json"
JOURNAL_ARCHIVE = PROJECT / "source/archive/mod/gqt002/journal/gqt002.journal"
ONSCREEN_RAW = (
    PROJECT / "source/raw/mod/gqt002/localization/en-us/onscreens/gqt002.json.json"
)
ONSCREEN_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt002/localization/en-us/onscreens/gqt002.json"
)
PLANT_TEMPLATE_RAW = (
    PROJECT / "source/raw/mod/gqt002/templates/gqt002_guarded_plant.questphase.json"
)
PLANT_TEMPLATE_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt002/templates/gqt002_guarded_plant.questphase"
)
DETECT_RAW = PROJECT / "source/raw/mod/gqt002/phases/gqt002_detect_guards.questphase.json"
DETECT_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt002/phases/gqt002_detect_guards.questphase"
)
ROOT_RAW = PROJECT / "source/raw/mod/gqt002/phases/gqt002_quiet_install.questphase.json"
ROOT_ARCHIVE = PROJECT / "source/archive/mod/gqt002/phases/gqt002_quiet_install.questphase"
LAPTOP_RAW = (
    PROJECT / "source/raw/mod/gqt002/world/gqt002_laptop_instance.streamingsector.json"
)
LAPTOP_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt002/world/gqt002_laptop_instance.streamingsector"
)
BLOCK_RAW = (
    PROJECT / "source/raw/mod/gqt002/world/gqt002_quiet_install.streamingblock.json"
)
BLOCK_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt002/world/gqt002_quiet_install.streamingblock"
)
DEVICE_REGISTRY_RAW = (
    PROJECT / "source/raw/mod/gqt002/world/gqt002_custom_devices.devices.json"
)
DEVICE_REGISTRY_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt002/world/gqt002_custom_devices.devices"
)
QUEST_SECTOR_RAW = (
    PROJECT / "source/raw/mod/gqt002/world/gqt002_quiet_install.streamingsector.json"
)
QUEST_SECTOR_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt002/world/gqt002_quiet_install.streamingsector"
)
ALWAYS_SECTOR_RAW = (
    PROJECT / "source/raw/mod/gqt002/world/gqt002_always_loaded.streamingsector.json"
)
ALWAYS_SECTOR_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt002/world/gqt002_always_loaded.streamingsector"
)
SECURITY_SECTOR_RAW = (
    PROJECT / "source/raw/mod/gqt002/world/gqt002_security.streamingsector.json"
)
SECURITY_SECTOR_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt002/world/gqt002_security.streamingsector"
)

OLD_TARGET_REF = "$/mod/gqt001/#gqt001_pr_signal_delay/#gqt001_terminal_laptop_r2"
TARGET_POSITION = {"X": -1052.1395, "Y": 1283.3362, "Z": 12.46019}
TARGET_ORIENTATION = {"i": 0.0, "j": 0.0, "k": -0.4137633, "r": 0.9103846}


def phase_document(
    builder: PhaseGraphBuilder,
    archive: Path,
    *,
    prefab: bool = False,
    bindings: dict[str, Any] | None = None,
) -> dict[str, Any]:
    bindings = resolve_bindings(load(MANIFEST)) if bindings is None else bindings
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
                    [
                        {
                            "$type": "questQuestPrefabEntry",
                            "prefabNodeRef": {
                                "$type": "NodeRef",
                                "$storage": "string",
                                "$value": bindings["locations"]["prefab"]["ref"],
                            },
                        }
                    ]
                    if prefab
                    else []
                ),
            },
            "EmbeddedFiles": [],
        },
    }


def generate_journal() -> dict[str, Any]:
    return compose_quest(load(MANIFEST)).documents[r"mod\gqt002\journal\gqt002.journal"]


def generate_onscreens() -> dict[str, Any]:
    return compose_quest(load(MANIFEST)).documents[
        r"mod\gqt002\localization\en-us\onscreens\gqt002.json"
    ]


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


def generate_guarded_plant(bindings: dict[str, Any] | None = None) -> dict[str, Any]:
    bindings = resolve_bindings(load(MANIFEST)) if bindings is None else bindings
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    active = objective_node(builder, 10, OBJECTIVE)
    pin_on = mappin_node(
        builder, 11, bindings["objectives"]["plant_keylogger"]["mappin"]
    )
    connected = device_condition(builder, 12, DEVICE, CONTROLLER, COMPLETION_FUNCTION)
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
    pin_off = mappin_node(
        builder, 17, bindings["objectives"]["plant_keylogger"]["mappin"]
    )
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
    return phase_document(builder, PLANT_TEMPLATE_ARCHIVE, bindings=bindings)


def generate_detection_phase(bindings: dict[str, Any] | None = None) -> dict[str, Any]:
    bindings = resolve_bindings(load(MANIFEST)) if bindings is None else bindings
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    detected = device_condition(
        builder,
        10,
        bindings["locations"]["security"]["ref"],
        "SecuritySystemControllerPS",
        "IsSystemInCombat",
    )
    stopped = fact_condition_node(builder, 11, bindings["facts"]["plant_complete"])
    failed = fact_node(builder, 12, bindings["facts"]["stealth_failed"])
    join = logical_xor_node(builder, 13, input_count=2)
    builder.connect(start, detected)
    builder.connect(start, stopped)
    builder.connect(detected, failed)
    builder.connect(failed, join, destination_socket="In1")
    builder.connect(stopped, join, destination_socket="In2")
    finish(builder, join, end, source_socket="Out1")
    return phase_document(builder, DETECT_ARCHIVE, bindings=bindings)


def generate_root_phase(
    bindings: dict[str, Any] | None = None,
    *,
    stage_resources: dict[str, str] | None = None,
) -> dict[str, Any]:
    bindings = resolve_bindings(load(MANIFEST)) if bindings is None else bindings
    if stage_resources is None:
        stage_resources = {
            stage["id"]: stage["phase_resource"]
            for stage in normalize_spec(load(MANIFEST))["stages"]
        }
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    activate = community_action_node(
        builder, 10, bindings["locations"]["guards"]["ref"], "Activate"
    )
    spawned = character_spawned_node(
        builder, 11, bindings["locations"]["guards"]["ref"]
    )
    guard_attitudes = tuple(
        (
            attitude_group_node(
                builder,
                12 + index * 2,
                entry,
                "neutral",
                community_ref=bindings["locations"]["guards"]["ref"],
            ),
            attitude_group_node(
                builder,
                13 + index * 2,
                entry,
                "hostile",
                community_ref=bindings["locations"]["guards"]["ref"],
            ),
        )
        for index, entry in enumerate(bindings["locations"]["guards"]["entries"])
    )
    item = add_item_node(builder, 18, bindings["locations"]["target"]["item"], 1)
    detector = phase_node(
        builder,
        19,
        DETECT_ARCHIVE.relative_to(PROJECT / "source/archive")
        .as_posix()
        .replace("/", "\\"),
    )
    monitor = phase_node(builder, 20, stage_resources["remain_undetected"])
    plant = phase_node(builder, 21, stage_resources["plant_keylogger"])
    join = logical_and_node(builder, 22, 3)
    deactivate = community_action_node(
        builder, 23, bindings["locations"]["guards"]["ref"], "Deactivate"
    )
    quest_done = quest_completion_node(builder, 24, bindings["quest"]["path"])
    completed = fact_node(builder, 25, bindings["facts"]["completed"])
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
    return phase_document(builder, ROOT_ARCHIVE, prefab=True, bindings=bindings)


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


def generate_laptop(bindings: dict[str, Any] | None = None) -> dict[str, Any]:
    bindings = resolve_bindings(load(MANIFEST)) if bindings is None else bindings
    sector = load(LAPTOP_TEMPLATE)
    replace_string(sector, OLD_TARGET_REF, bindings["locations"]["target"]["full_ref"])
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


def generate_security_sector(bindings: dict[str, Any] | None = None) -> dict[str, Any]:
    bindings = resolve_bindings(load(MANIFEST)) if bindings is None else bindings
    world = load(WORLD_SPEC)
    security = world["security"]
    reference = load(SECURITY_NODE_REFERENCE)
    reference_nodes = reference["Data"]["RootChunk"]["nodes"]
    system = copy.deepcopy(reference_nodes[923])
    area = copy.deepcopy(reference_nodes[927])

    prefab_root = world["prefab_root"]
    system_ref = full_node_ref(prefab_root, security["system_ref"])
    area_ref = full_node_ref(prefab_root, security["area_ref"])
    community_ref = full_node_ref(prefab_root, bindings["locations"]["guards"]["ref"])

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
        },
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


def generate_device_registry(bindings: dict[str, Any] | None = None) -> dict[str, Any]:
    bindings = resolve_bindings(load(MANIFEST)) if bindings is None else bindings
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
                node_ref=bindings["locations"]["target"]["full_ref"],
                node_hash=node_ref_hash(bindings["locations"]["target"]["full_ref"]),
                controller_class="ComputerControllerPS",
                position=Vec3(
                    TARGET_POSITION["X"], TARGET_POSITION["Y"], TARGET_POSITION["Z"]
                ),
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


def build_artifacts(output_root: Path | None = None) -> list[QuestArtifact]:
    bindings = resolve_bindings(load(MANIFEST))
    plant_template = generate_guarded_plant(bindings)
    artifacts = compile_manifest_artifacts(
        MANIFEST,
        ROOT_RAW,
        ROOT_ARCHIVE,
        root_override=lambda spec, _archive: generate_root_phase(
            bindings,
            stage_resources={stage.id: stage.phase_resource for stage in spec.stages},
        ),
        template_documents={
            r"mod\gqt002\templates\gqt002_guarded_plant.questphase": plant_template
        },
    )
    artifacts.extend(
        QuestArtifact(raw, archive, document)
        for raw, archive, document in (
            (PLANT_TEMPLATE_RAW, PLANT_TEMPLATE_ARCHIVE, plant_template),
            (DETECT_RAW, DETECT_ARCHIVE, generate_detection_phase(bindings)),
            (LAPTOP_RAW, LAPTOP_ARCHIVE, generate_laptop(bindings)),
            (QUEST_SECTOR_RAW, QUEST_SECTOR_ARCHIVE, load(QUEST_SECTOR_RAW)),
            (ALWAYS_SECTOR_RAW, ALWAYS_SECTOR_ARCHIVE, load(ALWAYS_SECTOR_RAW)),
            (
                SECURITY_SECTOR_RAW,
                SECURITY_SECTOR_ARCHIVE,
                generate_security_sector(bindings),
            ),
            (BLOCK_RAW, BLOCK_ARCHIVE, generate_block()),
            (
                DEVICE_REGISTRY_RAW,
                DEVICE_REGISTRY_ARCHIVE,
                generate_device_registry(bindings),
            ),
        )
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
        namespace="gqt002",
        output_root=args.output_root,
        deserialize=args.deserialize,
        binary_templates={
            JOURNAL_ARCHIVE: JOURNAL_BINARY_TEMPLATE,
            ONSCREEN_ARCHIVE: ONSCREEN_BINARY_TEMPLATE,
            DETECT_ARCHIVE: COMBAT_PHASE_TEMPLATE,
            ROOT_ARCHIVE: ROOT_PHASE_TEMPLATE,
            QUEST_SECTOR_ARCHIVE: QUEST_SECTOR_TEMPLATE,
            ALWAYS_SECTOR_ARCHIVE: ALWAYS_SECTOR_TEMPLATE,
            DEVICE_REGISTRY_ARCHIVE: DEVICE_REGISTRY_TEMPLATE,
        },
    )
    for raw, _archive in outputs:
        print(raw)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
