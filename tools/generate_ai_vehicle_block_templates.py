#!/usr/bin/env python3
"""Generate reduced questphase templates for AI and vehicle quest blocks.

These templates deliberately retain the condition shapes used by the audited
vanilla references while removing quest-specific scenes, facts, and cleanup.
They are orchestration templates:

* ``escort_npc`` waits for a named community entry to cross two route gates.
  The companion's follow/patrol behaviour remains world/community authored.
* ``carry_npc`` waits for the named entry to be mounted to the player and then
  carried inside the destination trigger.
* ``deliver_vehicle`` waits for the referenced vehicle to enter the delivery
  trigger and come to a complete stop.

All authored values are complete scalar placeholders because
``quest_compiler.py`` intentionally performs exact scalar replacement only.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from generate_cache_phase import (
    GraphNode,
    PhaseGraphBuilder,
    cname,
    entity_reference,
    input_node,
    node_ref,
    objective_node,
    output_node,
)


ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = ROOT / "source/raw/mod/ghostline/quest_blocks/templates"
ARCHIVE_ROOT = ROOT / "source/archive/mod/ghostline/quest_blocks/templates"

COMMUNITY = "{{community}}"
ENTRY = "{{entry}}"
DESTINATION_1 = "{{destination_1}}"
DESTINATION_2 = "{{destination_2}}"
DESTINATION = "{{destination}}"
OBJECTIVE = "{{objective}}"
VEHICLE = "{{vehicle}}"

JsonObject = dict[str, Any]


def trigger_condition_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    trigger_ref: str,
    *,
    activator: JsonObject,
    is_player: bool = False,
) -> GraphNode:
    """Use the vanilla ``questTriggerCondition`` serialized shape."""

    condition = builder.handles.wrap(
        {
            "$type": "questTriggerCondition",
            "activatorRef": activator,
            "isPlayerActivator": int(is_player),
            "triggerAreaRef": node_ref(trigger_ref),
            "type": "IsInside",
        }
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def character_mount_condition(
    builder: PhaseGraphBuilder,
    quest_id: int,
    *,
    community: str,
    entry: str,
) -> GraphNode:
    """Wait for a named NPC to be carried by the local player.

    This matches the ``questCharacterMount_ConditionType`` used by
    ``sts_hey_rey_09`` for the carried target.
    """

    condition_type = builder.handles.wrap(
        {
            "$type": "questCharacterMount_ConditionType",
            "anyChild": 0,
            "anyParent": 0,
            "childIsPlayer": 0,
            "childRef": entity_reference(community, names=(entry,)),
            "condition": "OnMount",
            "enterAnimationFinished": 0,
            "parentIsPlayer": 1,
            "parentRef": entity_reference(),
            "playerVehicleName": "",
            "role": "Invalid",
            "usePlayersVehicle": 0,
            "vehicleAfiliation": "Invalid",
            "vehicleOrigin": "Any",
            "vehicleType": "Any",
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questCharacterCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def carried_inside_condition(
    builder: PhaseGraphBuilder,
    quest_id: int,
    *,
    community: str,
    entry: str,
    destination: str,
) -> GraphNode:
    """Wait until the player is carrying the NPC inside a destination gate."""

    mount_type = builder.handles.wrap(
        {
            "$type": "questCharacterMount_ConditionType",
            "anyChild": 0,
            "anyParent": 0,
            "childIsPlayer": 0,
            "childRef": entity_reference(community, names=(entry,)),
            "condition": "OnMount",
            "enterAnimationFinished": 0,
            "parentIsPlayer": 1,
            "parentRef": entity_reference(),
            "playerVehicleName": "",
            "role": "Invalid",
            "usePlayersVehicle": 0,
            "vehicleAfiliation": "Invalid",
            "vehicleOrigin": "Any",
            "vehicleType": "Any",
        }
    )
    mount_condition = builder.handles.wrap(
        {"$type": "questCharacterCondition", "type": mount_type}
    )
    destination_condition = builder.handles.wrap(
        {
            "$type": "questTriggerCondition",
            "activatorRef": entity_reference(),
            "isPlayerActivator": 1,
            "triggerAreaRef": node_ref(destination),
            "type": "IsInside",
        }
    )
    condition = builder.handles.wrap(
        {
            "$type": "questLogicalCondition",
            "conditions": [mount_condition, destination_condition],
            "operation": "AND",
        }
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def vehicle_stopped_condition(
    builder: PhaseGraphBuilder, quest_id: int, vehicle: str
) -> GraphNode:
    """Wait for a specific vehicle to reach zero speed."""

    condition_type = builder.handles.wrap(
        {
            "$type": "questVehicleSpeed_ConditionType",
            "comparisonType": "CT_EQUAL",
            "speed": 0,
            "vehicleRef": entity_reference(vehicle),
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questVehicleCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def phase_document(builder: PhaseGraphBuilder, archive_target: Path) -> JsonObject:
    return {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": "2026-07-23T00:00:00Z",
            "DataType": "CR2W",
            "ArchiveFileName": str(archive_target.resolve()),
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


def finish_linear(
    builder: PhaseGraphBuilder, nodes: list[tuple[GraphNode, str, str]]
) -> None:
    """Connect ``(node, source socket, destination socket)`` tuples linearly."""

    for (source, source_socket, _), (destination, _, destination_socket) in zip(
        nodes, nodes[1:]
    ):
        builder.connect(
            source,
            destination,
            source_socket=source_socket,
            destination_socket=destination_socket,
        )


def build_escort() -> JsonObject:
    builder = PhaseGraphBuilder()
    start = input_node(builder)
    finish = output_node(builder)
    objective_active = objective_node(builder, 10, OBJECTIVE)
    actor = entity_reference(COMMUNITY, names=(ENTRY,))
    gate_1 = trigger_condition_node(
        builder, 11, DESTINATION_1, activator=actor
    )
    gate_2 = trigger_condition_node(
        builder,
        12,
        DESTINATION_2,
        activator=entity_reference(COMMUNITY, names=(ENTRY,)),
    )
    objective_success = objective_node(builder, 13, OBJECTIVE)
    finish_linear(
        builder,
        [
            (start, "Out", "In"),
            (objective_active, "Out", "Active"),
            (gate_1, "Out", "In"),
            (gate_2, "Out", "In"),
            (objective_success, "Out", "Succeeded"),
        ],
    )
    builder.connect_to_earlier_output(objective_success, finish)
    return phase_document(builder, ARCHIVE_ROOT / "escort_npc.questphase")


def build_carry() -> JsonObject:
    builder = PhaseGraphBuilder()
    start = input_node(builder)
    finish = output_node(builder)
    objective_active = objective_node(builder, 10, OBJECTIVE)
    mounted = character_mount_condition(
        builder, 11, community=COMMUNITY, entry=ENTRY
    )
    delivered = carried_inside_condition(
        builder,
        12,
        community=COMMUNITY,
        entry=ENTRY,
        destination=DESTINATION,
    )
    objective_success = objective_node(builder, 13, OBJECTIVE)
    finish_linear(
        builder,
        [
            (start, "Out", "In"),
            (objective_active, "Out", "Active"),
            (mounted, "Out", "In"),
            (delivered, "Out", "In"),
            (objective_success, "Out", "Succeeded"),
        ],
    )
    builder.connect_to_earlier_output(objective_success, finish)
    return phase_document(builder, ARCHIVE_ROOT / "carry_npc.questphase")


def build_deliver_vehicle() -> JsonObject:
    builder = PhaseGraphBuilder()
    start = input_node(builder)
    finish = output_node(builder)
    objective_active = objective_node(builder, 10, OBJECTIVE)
    arrived = trigger_condition_node(
        builder,
        11,
        DESTINATION,
        activator=entity_reference(VEHICLE),
    )
    stopped = vehicle_stopped_condition(builder, 12, VEHICLE)
    objective_success = objective_node(builder, 13, OBJECTIVE)
    finish_linear(
        builder,
        [
            (start, "Out", "In"),
            (objective_active, "Out", "Active"),
            (arrived, "Out", "In"),
            (stopped, "Out", "In"),
            (objective_success, "Out", "Succeeded"),
        ],
    )
    builder.connect_to_earlier_output(objective_success, finish)
    return phase_document(builder, ARCHIVE_ROOT / "deliver_vehicle.questphase")


BUILDERS = {
    "escort_npc": build_escort,
    "carry_npc": build_carry,
    "deliver_vehicle": build_deliver_vehicle,
}


def generate(*, write: bool) -> dict[str, JsonObject]:
    documents = {name: builder() for name, builder in BUILDERS.items()}
    if write:
        RAW_ROOT.mkdir(parents=True, exist_ok=True)
        for name, document in documents.items():
            path = RAW_ROOT / f"{name}.questphase.json"
            path.write_text(
                json.dumps(document, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
    return documents


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Build and report templates without replacing checked-in raw JSON.",
    )
    args = parser.parse_args()
    documents = generate(write=not args.dry_run)
    for name, document in documents.items():
        nodes = document["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
        print(f"{name}: {len(nodes)} nodes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
