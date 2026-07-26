#!/usr/bin/env python3
"""Generate reduced templates for advanced, vanilla-derived quest blocks.

The templates intentionally stop at boundaries owned by scenes, devices, or
world authoring.  For example, ``read_terminal_document`` waits for the fact
emitted by a named computer-scene output; it does not pretend that opening an
inventory shard is equivalent to reading a computer document.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from generate_cache_phase import (
    GraphNode,
    PhaseGraphBuilder,
    cname,
    entity_reference,
    fact_node,
    input_node,
    local_player_reference,
    mappin_node,
    node_ref,
    objective_node,
    output_node,
    tweakdbid,
)
from generate_delivery_phase import fact_condition_node, logical_xor_node


ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = ROOT / "source/raw/mod/ghostline/quest_blocks/templates"
ARCHIVE_ROOT = ROOT / "source/archive/mod/ghostline/quest_blocks/templates"

OBJECTIVE = "{{objective}}"
COMPLETION_FACT = "{{completion_fact}}"
FAILURE_FACT = "{{failure_fact}}"
SUCCESS_FACT = "{{success_fact}}"
STOP_FACT = "{{stop_fact}}"
DEVICE = "{{device}}"
CONTROLLER = "{{controller_class}}"
ACTION = "{{action}}"
COMPLETION_FUNCTION = "{{completion_function}}"
# TweakDBID JSON values must be parseable before template instantiation, so
# this one placeholder is a valid sentinel record rather than brace syntax.
ITEM = "Items.GhostlineTemplateItem"
COMMUNITY = "{{community}}"
ENTRY = "{{entry}}"
DESTINATION_1 = "{{destination_1}}"
DESTINATION_2 = "{{destination_2}}"
DESTINATION_3 = "{{destination_3}}"
VEHICLE = "{{vehicle}}"
VEHICLE_COMMUNITY = "{{vehicle_community}}"
VEHICLE_ENTRY = "{{vehicle_entry}}"
MAPPIN = "{{mappin}}"
ESCORT_MAPPIN_1 = "{{route_mappin_1}}"
ESCORT_MAPPIN_2 = "{{route_mappin_2}}"
ESCORT_MAPPIN_3 = "{{route_mappin_3}}"
CONTACT_COMMUNITY = "{{contact_community}}"
CONTACT_ENTRY = "{{contact_entry}}"
PLAYER_VEHICLE_RECORD = "{{player_vehicle_record}}"

JsonObject = dict[str, Any]


def phase_document(builder: PhaseGraphBuilder, name: str) -> JsonObject:
    return {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": "2026-07-24T00:00:00Z",
            "DataType": "CR2W",
            "ArchiveFileName": str((ARCHIVE_ROOT / f"{name}.questphase").resolve()),
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


def finish(
    builder: PhaseGraphBuilder,
    previous: GraphNode,
    end: GraphNode,
    *,
    source_socket: str = "Out",
) -> None:
    builder.connect_to_earlier_output(
        previous, end, source_socket=source_socket
    )


def device_manager(
    builder: PhaseGraphBuilder, quest_id: int, device: str, controller: str, action: str
) -> GraphNode:
    params = builder.handles.wrap(
        {
            "$type": "questDeviceManager_NodeTypeParams",
            "actionProperties": [],
            "deviceAction": cname(action),
            "deviceControllerClass": cname(controller),
            "entityRef": entity_reference(),
            "objectRef": node_ref(device),
            "slotName": cname("None"),
        }
    )
    node_type = builder.handles.wrap(
        {"$type": "questDeviceManager_NodeType", "params": [params]}
    )
    return builder.node(
        quest_id,
        "questInteractiveObjectManagerNodeDefinition",
        input_names=("In",),
        properties={"type": node_type},
    )


def device_condition(
    builder: PhaseGraphBuilder,
    quest_id: int,
    device: str,
    controller: str,
    function: str,
) -> GraphNode:
    condition_type = builder.handles.wrap(
        {
            "$type": "questDevice_ConditionType",
            "deviceConditionFunction": cname(function),
            "deviceControllerClass": cname(controller),
            "functionParameters": [],
            "objectRef": node_ref(device),
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questObjectCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def remove_item_node(builder: PhaseGraphBuilder, quest_id: int, item: str) -> GraphNode:
    params = builder.handles.wrap(
        {
            "$type": "questAddRemoveItem_NodeTypeParams",
            "entityRef": local_player_reference(builder),
            "flagItemAddedCallbackAsSilent": 1,
            "isPlayer": 0,
            "itemID": tweakdbid(item),
            "itemIDsToIgnoreOnRemove": [],
            "nodeType": "RemoveAll",
            "objectRef": entity_reference(),
            "quantity": 1,
            "removeAllQuantity": 0,
            "sendNotification": 0,
            "tagsToIgnoreOnRemove": [],
            "tagToRemove": cname("None"),
        }
    )
    node_type = builder.handles.wrap(
        {"$type": "questAddRemoveItem_NodeType", "params": [params]}
    )
    return builder.node(
        quest_id,
        "questItemManagerNodeDefinition",
        input_names=("In",),
        properties={"type": node_type},
    )


def character_condition(
    builder: PhaseGraphBuilder,
    quest_id: int,
    condition_type: JsonObject,
) -> GraphNode:
    wrapped_type = builder.handles.wrap(condition_type)
    condition = builder.handles.wrap(
        {"$type": "questCharacterCondition", "type": wrapped_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def character_killed(
    builder: PhaseGraphBuilder, quest_id: int, community: str, entry: str
) -> GraphNode:
    comparison = builder.handles.wrap(
        {
            "$type": "questComparisonParam",
            "comparisonType": "Greater",
            "count": 0,
            "entireCommunity": 0,
        }
    )
    return character_condition(
        builder,
        quest_id,
        {
            "$type": "questCharacterKilled_ConditionType",
            "comparisonParams": comparison,
            "defeated": 1,
            "killed": 1,
            "objectRef": entity_reference(community, names=(entry,)),
            "source": None,
            "unconscious": 1,
        },
    )


def character_spawned(
    builder: PhaseGraphBuilder, quest_id: int, community: str, entry: str
) -> GraphNode:
    comparison = builder.handles.wrap(
        {
            "$type": "questComparisonParam",
            "comparisonType": "Greater",
            "count": 0,
            "entireCommunity": 0,
        }
    )
    return character_condition(
        builder,
        quest_id,
        {
            "$type": "questCharacterSpawned_ConditionType",
            "comparisonParams": comparison,
            "objectRef": entity_reference(community, names=(entry,)),
        },
    )


def mount_condition(
    builder: PhaseGraphBuilder,
    quest_id: int,
    *,
    vehicle: str,
    vehicle_community: str | None = None,
    vehicle_entry: str | None = None,
    community: str | None = None,
    entry: str | None = None,
) -> GraphNode:
    is_player = community is None
    child_ref = (
        entity_reference()
        if is_player
        else entity_reference(community or "", names=(entry or "",))
    )
    return character_condition(
        builder,
        quest_id,
        {
            "$type": "questCharacterMount_ConditionType",
            "anyChild": 0,
            "anyParent": 0,
            "childIsPlayer": int(is_player),
            "childRef": child_ref,
            "condition": "OnMount",
            "enterAnimationFinished": 0,
            "parentIsPlayer": 0,
            "parentRef": (
                entity_reference(
                    vehicle_community,
                    names=(vehicle_entry or "",),
                )
                if vehicle_community is not None
                else entity_reference(vehicle)
            ),
            "playerVehicleName": "",
            "role": "Driver",
            "usePlayersVehicle": 0,
            "vehicleAfiliation": "Invalid",
            "vehicleOrigin": "Any",
            "vehicleType": "Any",
        },
    )


def trigger_condition(
    builder: PhaseGraphBuilder, quest_id: int, trigger: str, activator: JsonObject
) -> GraphNode:
    condition = builder.handles.wrap(
        {
            "$type": "questTriggerCondition",
            "activatorRef": activator,
            "isPlayerActivator": 0,
            "triggerAreaRef": node_ref(trigger),
            "type": "IsInside",
        }
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def puppet_ai_tier(
    builder: PhaseGraphBuilder, quest_id: int, community: str, entry: str
) -> GraphNode:
    return builder.node(
        quest_id,
        "questPuppetAIManagerNodeDefinition",
        input_names=("In",),
        properties={
            "entries": [
                {
                    "$type": "questPuppetAIManagerNodeDefinitionEntry",
                    "aiTier": "Gameplay",
                    "entityReference": entity_reference(community, names=(entry,)),
                }
            ]
        },
    )


def player_vehicle_node(
    builder: PhaseGraphBuilder, quest_id: int, record: str, *, despawn: bool
) -> GraphNode:
    node_type = builder.handles.wrap(
        {
            "$type": "questEnablePlayerVehicle_NodeType",
            "despawn": int(despawn),
            "enable": int(not despawn),
            "makePlayerActiveVehicle": int(not despawn),
            "vehicle": record,
        }
    )
    return builder.node(
        quest_id,
        "questVehicleNodeDefinition",
        input_names=("In",),
        properties={"type": node_type},
    )


def community_action_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    community_ref: str,
    action: str,
    *,
    entry: str = "None",
    phase: str = "None",
) -> GraphNode:
    action_type = builder.handles.wrap(
        {
            "$type": "questCommunityTemplate_NodeType",
            "action": action,
            "communityEntryName": cname(entry),
            "communityEntryPhaseName": cname(phase),
            "spawnerReference": node_ref(community_ref),
        }
    )
    return builder.node(
        quest_id,
        "questSpawnManagerNodeDefinition",
        input_names=("In",),
        properties={
            "actions": [
                {
                    "$type": "questSpawnManagerNodeActionEntry",
                    "type": action_type,
                }
            ]
        },
    )


def assign_follower_role(
    builder: PhaseGraphBuilder, quest_id: int, community: str, entry: str
) -> GraphNode:
    """Assign the named actor the vanilla follower role targeting V."""

    role = builder.handles.wrap(
        {
            "$type": "AIFollowerRole",
            "attitudeGroupName": cname("None"),
            "followerRef": entity_reference("#player"),
            "followTarget": None,
            "followTargetSquads": [],
            "friendlyTargetSlotListener": None,
            "isFriendMelee": 0,
            "isOwnerSniper": 0,
            "lastStealthLeaveTimeStamp": {"$type": "EngineTime"},
            "owner": None,
            "ownerTargetSlotListener": None,
            "playerCombatListener": None,
        }
    )
    params = builder.handles.wrap(
        {
            "$type": "AIAssignRoleCommandParams",
            "role": role,
        }
    )
    return builder.node(
        quest_id,
        "questMiscAICommandNode",
        input_names=("In",),
        output_names=("Success",),
        properties={
            "entityReference": entity_reference(community, names=(entry,)),
            # Vanilla follower assignments retain this reflected function name
            # while dispatching from the concrete params class above.
            "function": cname("AIClearRoleCommandParams"),
            "params": params,
        },
    )


def clear_ai_role(
    builder: PhaseGraphBuilder, quest_id: int, community: str, entry: str
) -> GraphNode:
    params = builder.handles.wrap({"$type": "AIClearRoleCommandParams"})
    return builder.node(
        quest_id,
        "questMiscAICommandNode",
        input_names=("In",),
        output_names=("Success",),
        properties={
            "entityReference": entity_reference(community, names=(entry,)),
            "function": cname("AIClearRoleCommandParams"),
            "params": params,
        },
    )


def assign_character_to_vehicle(
    builder: PhaseGraphBuilder,
    quest_id: int,
    *,
    community: str,
    entry: str,
    vehicle: str,
    vehicle_entry: str | None = None,
    slot: str = "seat_front_right",
) -> GraphNode:
    node_type = builder.handles.wrap(
        {
            "$type": "questAssignCharacter_NodeType",
            "assign": 1,
            "characterRef": entity_reference(community, names=(entry,)),
            "clearAssignedVehicleIdWhenUnmounting": 0,
            "entryAnimName": cname("None"),
            "entrySlotName": cname("default"),
            "isInstant": 1,
            "isPlayer": 0,
            "slotName": cname(slot),
            "vehicleRef": entity_reference(
                vehicle,
                names=(vehicle_entry,) if vehicle_entry is not None else (),
            ),
        }
    )
    return builder.node(
        quest_id,
        "questVehicleNodeDefinition",
        input_names=("In",),
        properties={"type": node_type},
    )


def simple_fact_gate(name: str) -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    active = objective_node(builder, 10, OBJECTIVE)
    wait = fact_condition_node(
        builder, 11, COMPLETION_FACT, comparison="Greater", value=0
    )
    done = objective_node(builder, 12, OBJECTIVE)
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, wait)
    builder.connect(wait, done, destination_socket="Succeeded")
    finish(builder, done, end)
    return phase_document(builder, name)


def build_stealth_monitor() -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    active = objective_node(builder, 10, OBJECTIVE)
    failed = fact_condition_node(
        builder, 11, FAILURE_FACT, comparison="Greater", value=0
    )
    stopped = fact_condition_node(
        builder, 12, STOP_FACT, comparison="Greater", value=0
    )
    failed_objective = objective_node(builder, 13, OBJECTIVE)
    succeeded_objective = objective_node(builder, 14, OBJECTIVE)
    success_fact = fact_node(builder, 15, SUCCESS_FACT)
    join = logical_xor_node(builder, 16, input_count=2)
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, failed)
    builder.connect(active, stopped)
    builder.connect(failed, failed_objective, destination_socket="Failed")
    builder.connect(stopped, succeeded_objective, destination_socket="Succeeded")
    builder.connect(failed_objective, join, destination_socket="In1")
    builder.connect(succeeded_objective, success_fact)
    builder.connect(success_fact, join, destination_socket="In2")
    finish(builder, join, end, source_socket="Out1")
    return phase_document(builder, "stealth_monitor")


def build_plant_item() -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    active = objective_node(builder, 10, OBJECTIVE)
    action = device_manager(builder, 11, DEVICE, CONTROLLER, ACTION)
    completed = device_condition(
        builder, 12, DEVICE, CONTROLLER, COMPLETION_FUNCTION
    )
    remove = remove_item_node(builder, 13, ITEM)
    done = objective_node(builder, 14, OBJECTIVE)
    fact = fact_node(builder, 15, COMPLETION_FACT)
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, action)
    builder.connect(action, completed)
    builder.connect(completed, remove)
    builder.connect(remove, done, destination_socket="Succeeded")
    builder.connect(done, fact)
    finish(builder, fact, end)
    return phase_document(builder, "plant_item")


def build_defend_target() -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    active = objective_node(builder, 10, OBJECTIVE)
    complete = fact_condition_node(
        builder, 11, COMPLETION_FACT, comparison="Greater", value=0
    )
    killed = character_killed(builder, 12, COMMUNITY, ENTRY)
    success = objective_node(builder, 13, OBJECTIVE)
    failure = objective_node(builder, 14, OBJECTIVE)
    failed_fact = fact_node(builder, 15, FAILURE_FACT)
    join = logical_xor_node(builder, 16, input_count=2)
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, complete)
    builder.connect(active, killed)
    builder.connect(complete, success, destination_socket="Succeeded")
    builder.connect(killed, failure, destination_socket="Failed")
    builder.connect(success, join, destination_socket="In1")
    builder.connect(failure, failed_fact)
    builder.connect(failed_fact, join, destination_socket="In2")
    finish(builder, join, end, source_socket="Out1")
    return phase_document(builder, "defend_target")


def build_release_or_rescue() -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    active = objective_node(builder, 10, OBJECTIVE)
    action = device_manager(builder, 11, DEVICE, CONTROLLER, ACTION)
    released = device_condition(
        builder, 12, DEVICE, CONTROLLER, COMPLETION_FUNCTION
    )
    ready = character_spawned(builder, 13, COMMUNITY, ENTRY)
    done = objective_node(builder, 14, OBJECTIVE)
    fact = fact_node(builder, 15, COMPLETION_FACT)
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, action)
    builder.connect(action, released)
    builder.connect(released, ready)
    builder.connect(ready, done, destination_socket="Succeeded")
    builder.connect(done, fact)
    finish(builder, fact, end)
    return phase_document(builder, "release_or_rescue_npc")


def build_escort() -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    active = objective_node(builder, 10, OBJECTIVE)
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
    clear = clear_ai_role(builder, 21, COMMUNITY, ENTRY)
    done = objective_node(builder, 22, OBJECTIVE)
    pin_3_off = mappin_node(builder, 23, ESCORT_MAPPIN_3)
    fact = fact_node(builder, 24, COMPLETION_FACT)
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
    builder.connect(gate_3, clear)
    builder.connect(clear, done, source_socket="Success", destination_socket="Succeeded")
    builder.connect(done, pin_3_off, destination_socket="Inactive")
    builder.connect(pin_3_off, fact)
    finish(builder, fact, end)
    return phase_document(builder, "escort_npc")


def build_enter_vehicle() -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    active = objective_node(builder, 10, OBJECTIVE)
    pin_on = mappin_node(builder, 11, MAPPIN)
    mounted = mount_condition(
        builder,
        12,
        vehicle=VEHICLE_COMMUNITY,
        vehicle_community=VEHICLE_COMMUNITY,
        vehicle_entry=VEHICLE_ENTRY,
    )
    mounted.data["condition"]["Data"]["type"]["Data"]["role"] = "Invalid"
    done = objective_node(builder, 13, OBJECTIVE)
    pin_off = mappin_node(builder, 14, MAPPIN)
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, pin_on, destination_socket="Active")
    builder.connect(pin_on, mounted)
    builder.connect(mounted, done, destination_socket="Succeeded")
    builder.connect(done, pin_off, destination_socket="Inactive")
    finish(builder, pin_off, end)
    return phase_document(builder, "enter_vehicle")


def build_ride_with_contact() -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    active = objective_node(builder, 10, OBJECTIVE)
    assign = assign_character_to_vehicle(
        builder,
        11,
        community=CONTACT_COMMUNITY,
        entry=CONTACT_ENTRY,
        vehicle=VEHICLE_COMMUNITY,
        vehicle_entry=VEHICLE_ENTRY,
    )
    player = mount_condition(
        builder,
        12,
        vehicle=VEHICLE,
        vehicle_community=VEHICLE_COMMUNITY,
        vehicle_entry=VEHICLE_ENTRY,
    )
    contact = mount_condition(
        builder,
        13,
        vehicle=VEHICLE,
        vehicle_community=VEHICLE_COMMUNITY,
        vehicle_entry=VEHICLE_ENTRY,
        community=CONTACT_COMMUNITY,
        entry=CONTACT_ENTRY,
    )
    contact.data["condition"]["Data"]["type"]["Data"]["role"] = "Passenger"
    join = builder.node(
        14,
        "questLogicalAndNodeDefinition",
        input_names=("In1", "In2"),
        output_names=("Out1",),
        properties={"inputSocketCount": 2, "outputSocketCount": 1},
    )
    done = objective_node(builder, 15, OBJECTIVE)
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, assign)
    builder.connect(assign, player)
    builder.connect(assign, contact)
    builder.connect(player, join, destination_socket="In1")
    builder.connect(contact, join, destination_socket="In2")
    builder.connect(join, done, source_socket="Out1", destination_socket="Succeeded")
    finish(builder, done, end)
    return phase_document(builder, "ride_with_contact")


def build_drive_to() -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    active = objective_node(builder, 10, OBJECTIVE)
    pin_on = mappin_node(builder, 11, MAPPIN)
    arrived = trigger_condition(
        builder,
        12,
        DESTINATION_1,
        entity_reference(VEHICLE_COMMUNITY, names=(VEHICLE_ENTRY,)),
    )
    done = objective_node(builder, 13, OBJECTIVE)
    pin_off = mappin_node(builder, 14, MAPPIN)
    fact = fact_node(builder, 15, COMPLETION_FACT)
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, pin_on, destination_socket="Active")
    builder.connect(pin_on, arrived)
    builder.connect(arrived, done, destination_socket="Succeeded")
    builder.connect(done, pin_off, destination_socket="Inactive")
    builder.connect(pin_off, fact)
    finish(builder, fact, end)
    return phase_document(builder, "drive_to")


def build_steal_vehicle() -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    active = objective_node(builder, 10, OBJECTIVE)
    pin_on = mappin_node(builder, 11, MAPPIN)
    mounted = mount_condition(
        builder,
        12,
        vehicle=VEHICLE_COMMUNITY,
        vehicle_community=VEHICLE_COMMUNITY,
        vehicle_entry=VEHICLE_ENTRY,
    )
    mounted.data["condition"]["Data"]["type"]["Data"]["role"] = "Invalid"
    done = objective_node(builder, 13, OBJECTIVE)
    pin_off = mappin_node(builder, 14, MAPPIN)
    builder.connect(start, active, destination_socket="Active")
    builder.connect(active, pin_on, destination_socket="Active")
    builder.connect(pin_on, mounted)
    builder.connect(mounted, done, destination_socket="Succeeded")
    builder.connect(done, pin_off, destination_socket="Inactive")
    finish(builder, pin_off, end)
    return phase_document(builder, "steal_vehicle")


def build_vehicle_cleanup() -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    # questEnablePlayerVehicle despawns every quest vehicle in this harness,
    # not just the requested record. Keep intermediate cleanup non-destructive;
    # the dedicated final-cleanup template still performs the actual despawn.
    fact = fact_node(builder, 10, COMPLETION_FACT)
    builder.connect(start, fact)
    finish(builder, fact, end)
    return phase_document(builder, "vehicle_cleanup")


BUILDERS = {
    "read_terminal_document": lambda: simple_fact_gate("read_terminal_document"),
    "stealth_monitor": build_stealth_monitor,
    "plant_item": build_plant_item,
    "defend_target": build_defend_target,
    "release_or_rescue_npc": build_release_or_rescue,
    "escort_npc": build_escort,
    "enter_vehicle": build_enter_vehicle,
    "ride_with_contact": build_ride_with_contact,
    "drive_to": build_drive_to,
    "steal_vehicle": build_steal_vehicle,
    "vehicle_cleanup": build_vehicle_cleanup,
}


def generate(*, write: bool = True) -> dict[str, JsonObject]:
    documents = {name: builder() for name, builder in BUILDERS.items()}
    if write:
        RAW_ROOT.mkdir(parents=True, exist_ok=True)
        for name, document in documents.items():
            (RAW_ROOT / f"{name}.questphase.json").write_text(
                json.dumps(document, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
    return documents


def main() -> int:
    documents = generate()
    for name, document in documents.items():
        nodes = document["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
        print(f"{name}: {len(nodes)} nodes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
