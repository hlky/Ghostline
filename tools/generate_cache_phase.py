#!/usr/bin/env python3
"""Generate the deterministic gq000 post-accept cache questphase.

The phase is intentionally linear.  Keeping its authored topology here makes
the two-stage objective, access-point state changes, journal unlocks, and
delayed guard cleanup reviewable without hand-editing CR2W handle graphs.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "source/raw/mod/gq000/phases/gq000_post_accept.questphase.json"
ARCHIVE_TARGET = str(
    ROOT / "source/archive/mod/gq000/phases/gq000_post_accept.questphase"
)

REACH_OBJECTIVE = "quests/minor_quest/gq000/gq000_02/gq000_02_obj_reach_cache"
REACH_DESCRIPTION = f"{REACH_OBJECTIVE}/gq000_02_desc_reach_cache"
CACHE_MAPPIN = f"{REACH_OBJECTIVE}/gq000_02_qmp_cache"
EXTRACT_OBJECTIVE = "quests/minor_quest/gq000/gq000_02/gq000_02_obj_extract_cache"
EXTRACT_DESCRIPTION = f"{EXTRACT_OBJECTIVE}/gq000_02_desc_extract_cache"
EXTRACT_MAPPIN = f"{EXTRACT_OBJECTIVE}/gq000_02_qmp_extract_cache"
LEAVE_OBJECTIVE = "quests/minor_quest/gq000/gq000_02/gq000_02_obj_leave_area"
LEAVE_DESCRIPTION = f"{LEAVE_OBJECTIVE}/gq000_02_desc_leave_area"
SHARD_PATHS = (
    "onscreens/emails/quests/minor_quest/gq000/shards/quiet_spine_01",
    "onscreens/emails/quests/minor_quest/gq000/shards/quiet_spine_02",
)
SHARD_ITEMS = (
    "Items.GhostlineQuietSpine01",
    "Items.GhostlineQuietSpine02",
)
DATACACHE_ITEM = "Items.gq000_datacache"
GUARD_ENTRIES = (
    "guard_ranged_m",
    "guard_ranged_f",
    "guard_melee",
)

ACCESS_POINT_REF = "#gq000_02_ap_cache"
GUARD_COMMUNITY_REF = "#gq000_02_com_cache_guards"
ARRIVAL_TRIGGER_REF = "#gq000_02_tr_cache_arrive"
CLEANUP_TRIGGER_REF = "#gq000_02_tr_cache_cleanup"
PHASE_PREFAB_REF = "#gq000_pr_patch_meet"
PLAYER_REF = "#player"
EXPECTED_GRAPH_NODES = 43


JsonObject = dict[str, Any]


def cname(value: str) -> JsonObject:
    return {"$type": "CName", "$storage": "string", "$value": value}


def node_ref(value: str, *, storage: str = "string") -> JsonObject:
    return {"$type": "NodeRef", "$storage": storage, "$value": value}


def tweakdbid(value: str) -> JsonObject:
    return {"$type": "TweakDBID", "$storage": "string", "$value": value}


def entity_reference(
    reference: str | None = None, *, names: Iterable[str] = ()
) -> JsonObject:
    """Return a vanilla entity reference, optionally scoped to named entries."""

    return {
        "$type": "gameEntityReference",
        "dynamicEntityUniqueName": cname("None"),
        "names": [cname(name) for name in names],
        "reference": (
            node_ref(reference) if reference is not None else node_ref("0", storage="uint64")
        ),
        "sceneActorContextName": cname("None"),
        "slotName": cname("None"),
        "type": "EntityRef",
    }


def local_player_reference(builder: "PhaseGraphBuilder") -> JsonObject:
    """Return the vanilla questUniversalRef form for the local player."""

    return builder.handles.wrap(
        {
            "$type": "questUniversalRef",
            "entityReference": entity_reference(),
            "mainPlayerObject": 0,
            "refLocalPlayer": 1,
        }
    )


class Handles:
    """Allocate deterministic CR2W handle IDs."""

    def __init__(self) -> None:
        self._next = 0

    def reserve(self) -> str:
        handle_id = str(self._next)
        self._next += 1
        return handle_id

    @staticmethod
    def define(handle_id: str, data: JsonObject) -> JsonObject:
        return {"HandleId": handle_id, "Data": data}

    def wrap(self, data: JsonObject) -> JsonObject:
        return self.define(self.reserve(), data)

    @staticmethod
    def ref(handle: JsonObject | str) -> JsonObject:
        handle_id = handle if isinstance(handle, str) else handle["HandleId"]
        return {"HandleRefId": handle_id}


@dataclass
class GraphNode:
    wrapper: JsonObject
    inputs: dict[str, JsonObject]
    outputs: dict[str, JsonObject]

    @property
    def data(self) -> JsonObject:
        return self.wrapper["Data"]


class PhaseGraphBuilder:
    def __init__(self) -> None:
        self.handles = Handles()
        graph_handle = self.handles.reserve()
        self.graph = self.handles.define(
            graph_handle,
            {"$type": "questGraphDefinition", "nodes": []},
        )

    def socket(self, name: str, socket_type: str) -> JsonObject:
        return self.handles.wrap(
            {
                "$type": "questSocketDefinition",
                "connections": [],
                "name": cname(name),
                "type": socket_type,
            }
        )

    def node(
        self,
        quest_id: int,
        node_type: str,
        *,
        input_names: Iterable[str],
        output_names: Iterable[str] = ("Out",),
        properties: JsonObject | None = None,
    ) -> GraphNode:
        handle_id = self.handles.reserve()
        cut = self.socket("CutDestination", "CutDestination")
        inputs = {name: self.socket(name, "Input") for name in input_names}
        outputs = {name: self.socket(name, "Output") for name in output_names}
        data: JsonObject = {
            "$type": node_type,
            "id": quest_id,
            "sockets": [cut, *inputs.values(), *outputs.values()],
        }
        if properties:
            data.update(properties)
        wrapper = self.handles.define(handle_id, data)
        result = GraphNode(wrapper, inputs, outputs)
        self.graph["Data"]["nodes"].append(wrapper)
        return result

    @staticmethod
    def _replace_socket(node: GraphNode, socket: JsonObject, replacement: JsonObject) -> None:
        sockets = node.data["sockets"]
        index = next(index for index, candidate in enumerate(sockets) if candidate is socket)
        sockets[index] = replacement

    def connect(
        self,
        source: GraphNode,
        destination: GraphNode,
        *,
        source_socket: str = "Out",
        destination_socket: str = "In",
    ) -> None:
        """Connect a node to a later node using WolvenKit's forward embedding."""

        source_handle = source.outputs[source_socket]
        destination_handle = destination.inputs[destination_socket]
        connection_id = self.handles.reserve()
        destination_handle["Data"]["connections"].append(self.handles.ref(connection_id))
        connection = self.handles.define(
            connection_id,
            {
                "$type": "graphGraphConnectionDefinition",
                "destination": destination_handle,
                "source": self.handles.ref(source_handle),
            },
        )
        source_handle["Data"]["connections"].append(connection)
        self._replace_socket(
            destination,
            destination_handle,
            self.handles.ref(destination_handle),
        )

    def connect_to_earlier_output(
        self,
        source: GraphNode,
        output_node: GraphNode,
        *,
        source_socket: str = "Out",
    ) -> None:
        """Connect the final node to the conventionally second Output node."""

        source_handle = source.outputs[source_socket]
        destination_handle = output_node.inputs["In"]
        connection_id = self.handles.reserve()
        source_handle["Data"]["connections"].append(self.handles.ref(connection_id))
        connection = self.handles.define(
            connection_id,
            {
                "$type": "graphGraphConnectionDefinition",
                "destination": self.handles.ref(destination_handle),
                "source": source_handle,
            },
        )
        destination_handle["Data"]["connections"].append(connection)
        self._replace_socket(source, source_handle, self.handles.ref(source_handle))

    def connect_to_earlier_input(
        self,
        source: GraphNode,
        destination: GraphNode,
        *,
        source_socket: str = "Out",
        destination_socket: str = "In",
    ) -> None:
        """Connect a later node to an input socket owned by an earlier node."""

        source_handle = source.outputs[source_socket]
        destination_handle = destination.inputs[destination_socket]
        connection_id = self.handles.reserve()
        source_handle["Data"]["connections"].append(self.handles.ref(connection_id))
        connection = self.handles.define(
            connection_id,
            {
                "$type": "graphGraphConnectionDefinition",
                "destination": self.handles.ref(destination_handle),
                "source": source_handle,
            },
        )
        destination_handle["Data"]["connections"].append(connection)
        self._replace_socket(source, source_handle, self.handles.ref(source_handle))


def input_node(builder: PhaseGraphBuilder) -> GraphNode:
    return builder.node(
        0,
        "questInputNodeDefinition",
        input_names=(),
        properties={"socketName": cname("In1")},
    )


def output_node(builder: PhaseGraphBuilder) -> GraphNode:
    return builder.node(
        1,
        "questOutputNodeDefinition",
        input_names=("In",),
        output_names=(),
        properties={"socketName": cname("Out1"), "type": "Terminating"},
    )


def journal_path(builder: PhaseGraphBuilder, real_path: str, class_name: str, index: int) -> JsonObject:
    return builder.handles.wrap(
        {
            "$type": "gameJournalPath",
            "className": cname(class_name),
            "editorPath": "",
            "fileEntryIndex": index,
            "realPath": real_path,
        }
    )


def objective_node(builder: PhaseGraphBuilder, quest_id: int, path: str) -> GraphNode:
    node_type = builder.handles.wrap(
        {
            "$type": "questJournalQuestEntry_NodeType",
            "optional": 0,
            "path": journal_path(builder, path, "gameJournalQuestObjective", 2),
            "sendNotification": 1,
            "trackQuest": 1,
            "version": "Initial",
        }
    )
    return builder.node(
        quest_id,
        "questJournalNodeDefinition",
        input_names=("Active", "Inactive", "Succeeded", "Failed"),
        properties={"type": node_type},
    )


def journal_entry_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    path: str,
    class_name: str,
    file_index: int,
) -> GraphNode:
    node_type = builder.handles.wrap(
        {
            "$type": "questJournalEntry_NodeType",
            "path": journal_path(builder, path, class_name, file_index),
            "sendNotification": 1,
        }
    )
    return builder.node(
        quest_id,
        "questJournalNodeDefinition",
        input_names=("Active", "Inactive"),
        properties={"type": node_type},
    )


def mappin_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    path: str,
    *,
    disable_previous_mappins: bool = False,
) -> GraphNode:
    return builder.node(
        quest_id,
        "questMappinManagerNodeDefinition",
        input_names=("Active", "Inactive"),
        properties={
            "disablePreviousMappins": int(disable_previous_mappins),
            "path": journal_path(builder, path, "gameJournalQuestMapPin", 2),
        },
    )


def fact_node(builder: PhaseGraphBuilder, quest_id: int, fact_name: str) -> GraphNode:
    fact_type = builder.handles.wrap(
        {
            "$type": "questSetVar_NodeType",
            "factName": fact_name,
            "setExactValue": 1,
            "value": 1,
        }
    )
    return builder.node(
        quest_id,
        "questFactsDBManagerNodeDefinition",
        input_names=("In",),
        properties={"type": fact_type},
    )


def device_manager_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    action: str,
) -> GraphNode:
    params = builder.handles.wrap(
        {
            "$type": "questDeviceManager_NodeTypeParams",
            "actionProperties": [],
            "deviceAction": cname(action),
            "deviceControllerClass": cname("AccessPointControllerPS"),
            "entityRef": entity_reference(),
            "objectRef": node_ref(ACCESS_POINT_REF),
            "slotName": cname("None"),
        }
    )
    manager_type = builder.handles.wrap(
        {"$type": "questDeviceManager_NodeType", "params": [params]}
    )
    return builder.node(
        quest_id,
        "questInteractiveObjectManagerNodeDefinition",
        input_names=("In",),
        properties={"type": manager_type},
    )


def spawn_manager_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    action: str,
) -> GraphNode:
    action_type = builder.handles.wrap(
        {
            "$type": "questCommunityTemplate_NodeType",
            "action": action,
            "communityEntryName": cname("None"),
            "communityEntryPhaseName": cname("None"),
            "spawnerReference": node_ref(GUARD_COMMUNITY_REF),
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


def character_spawned_node(builder: PhaseGraphBuilder, quest_id: int) -> GraphNode:
    comparison = builder.handles.wrap(
        {
            "$type": "questComparisonParam",
            "comparisonType": "Greater",
            "count": 0,
            "entireCommunity": 1,
        }
    )
    condition_type = builder.handles.wrap(
        {
            "$type": "questCharacterSpawned_ConditionType",
            "comparisonParams": comparison,
            "objectRef": entity_reference(GUARD_COMMUNITY_REF),
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


def attitude_group_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    entry_name: str,
    group_name: str,
) -> GraphNode:
    """Force one named community puppet through a vanilla attitude transition."""

    subtype = builder.handles.wrap(
        {
            "$type": "questCharacterManagerParameters_SetAttitudeGroupForPuppet",
            "groupName": cname(group_name),
            "isPlayer": 0,
            "puppetRef": entity_reference(
                GUARD_COMMUNITY_REF, names=(entry_name,)
            ),
        }
    )
    node_type = builder.handles.wrap(
        {
            "$type": "questCharacterManagerParameters_NodeType",
            "subtype": subtype,
        }
    )
    return builder.node(
        quest_id,
        "questCharacterManagerNodeDefinition",
        input_names=("In",),
        properties={"type": node_type},
    )


def logical_and_node(
    builder: PhaseGraphBuilder, quest_id: int, input_count: int
) -> GraphNode:
    input_names = tuple(f"In{index}" for index in range(1, input_count + 1))
    return builder.node(
        quest_id,
        "questLogicalAndNodeDefinition",
        input_names=input_names,
        output_names=("Out1",),
        properties={
            "inputSocketCount": input_count,
            "outputSocketCount": 1,
        },
    )


def combat_target_node(
    builder: PhaseGraphBuilder, quest_id: int, entry_name: str
) -> GraphNode:
    """Immediately make V the combat target for one named guard."""

    params = builder.handles.wrap(
        {
            "$type": "questCombatNodeParams_CombatTarget",
            "duration": 0,
            "immediately": 1,
            "targetNode": node_ref("0", storage="uint64"),
            "targetPuppet": entity_reference(PLAYER_REF),
        }
    )
    return builder.node(
        quest_id,
        "questCombatNodeDefinition",
        input_names=("In",),
        output_names=("Success",),
        properties={
            "entityReference": entity_reference(
                GUARD_COMMUNITY_REF, names=(entry_name,)
            ),
            "function": cname("questCombatNodeParams_ShootAt"),
            "params": params,
        },
    )


def inject_combat_threat_node(
    builder: PhaseGraphBuilder, quest_id: int, entry_name: str
) -> GraphNode:
    """Inject V as the explicit combat threat for one named guard."""

    params = builder.handles.wrap(
        {
            "$type": "AIInjectCombatThreatCommandParams",
            "dontForceHostileAttitude": 0,
            "duration": 0,
            "isPersistent": 0,
            "targetNodeRef": node_ref("0", storage="uint64"),
            "targetPuppetRef": entity_reference(PLAYER_REF),
        }
    )
    return builder.node(
        quest_id,
        "questCombatNodeDefinition",
        input_names=("In",),
        output_names=("Success",),
        properties={
            "entityReference": entity_reference(
                GUARD_COMMUNITY_REF, names=(entry_name,)
            ),
            "function": cname("questCombatNodeParams_ShootAt"),
            "params": params,
        },
    )


def trigger_condition_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    trigger_ref: str,
    condition_type: str,
) -> GraphNode:
    condition = builder.handles.wrap(
        {
            "$type": "questTriggerCondition",
            "activatorRef": entity_reference(),
            "isPlayerActivator": 1,
            "triggerAreaRef": node_ref(trigger_ref),
            "type": condition_type,
        }
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def hacking_succeeded_node(builder: PhaseGraphBuilder, quest_id: int) -> GraphNode:
    condition_type = builder.handles.wrap(
        {
            "$type": "questDevice_ConditionType",
            "deviceConditionFunction": cname("WasHackingMinigameSucceeded"),
            "deviceControllerClass": cname("AccessPointControllerPS"),
            "functionParameters": [],
            "objectRef": node_ref(ACCESS_POINT_REF),
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


def realtime_delay_node(
    builder: PhaseGraphBuilder, quest_id: int, *, seconds: int = 1
) -> GraphNode:
    condition_type = builder.handles.wrap(
        {
            "$type": "questRealtimeDelay_ConditionType",
            "hours": 0,
            "miliseconds": 0,
            "minutes": 0,
            "seconds": seconds,
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questTimeCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def add_recovered_items_node(builder: PhaseGraphBuilder, quest_id: int) -> GraphNode:
    params = []
    for item_id in (*SHARD_ITEMS, DATACACHE_ITEM):
        params.append(
            builder.handles.wrap(
                {
                    "$type": "questAddRemoveItem_NodeTypeParams",
                    "entityRef": local_player_reference(builder),
                    "flagItemAddedCallbackAsSilent": 0,
                    "isPlayer": 0,
                    "itemID": tweakdbid(item_id),
                    "itemIDsToIgnoreOnRemove": [],
                    "nodeType": "AddItem",
                    "objectRef": entity_reference(),
                    "quantity": 1,
                    "removeAllQuantity": 0,
                    "sendNotification": 1,
                    "tagsToIgnoreOnRemove": [],
                    "tagToRemove": cname("None"),
                }
            )
        )
    node_type = builder.handles.wrap(
        {"$type": "questAddRemoveItem_NodeType", "params": params}
    )
    return builder.node(
        quest_id,
        "questItemManagerNodeDefinition",
        input_names=("In",),
        properties={"type": node_type},
    )


def build_phase() -> JsonObject:
    builder = PhaseGraphBuilder()
    phase_input = input_node(builder)
    phase_output = output_node(builder)

    reach_active = objective_node(builder, 10, REACH_OBJECTIVE)
    reach_description = journal_entry_node(
        builder, 11, REACH_DESCRIPTION, "gameJournalQuestDescription", 2
    )
    mappin_active = mappin_node(builder, 12, CACHE_MAPPIN)
    stage_started = fact_node(builder, 13, "gq000_02_started")
    access_point_disabled = device_manager_node(builder, 14, "ForceDisabled")
    guards_active = spawn_manager_node(builder, 15, "Activate")
    guards_ready = character_spawned_node(builder, 16)
    player_arrived = trigger_condition_node(
        builder, 17, ARRIVAL_TRIGGER_REF, "IsInside"
    )
    reach_succeeded = objective_node(builder, 19, REACH_OBJECTIVE)
    mappin_inactive = mappin_node(builder, 20, CACHE_MAPPIN)
    extract_active = objective_node(builder, 21, EXTRACT_OBJECTIVE)
    extract_description = journal_entry_node(
        builder, 22, EXTRACT_DESCRIPTION, "gameJournalQuestDescription", 2
    )
    extract_mappin = mappin_node(builder, 23, EXTRACT_MAPPIN)
    access_point_enabled = device_manager_node(builder, 24, "ForceEnabled")
    hacking_succeeded = hacking_succeeded_node(builder, 25)
    cache_acquired = fact_node(builder, 26, "gq000_cache_acquired")
    post_hack_delay = realtime_delay_node(builder, 27)
    access_point_disabled_final = device_manager_node(builder, 28, "ForceDisabled")
    extract_succeeded = objective_node(builder, 29, EXTRACT_OBJECTIVE)
    extract_mappin_inactive = mappin_node(builder, 30, EXTRACT_MAPPIN)
    shard_one = journal_entry_node(
        builder, 31, SHARD_PATHS[0], "gameJournalOnscreen", 5
    )
    shard_two = journal_entry_node(
        builder, 32, SHARD_PATHS[1], "gameJournalOnscreen", 5
    )
    recovered_items = add_recovered_items_node(builder, 33)
    leave_active = objective_node(builder, 34, LEAVE_OBJECTIVE)
    leave_description = journal_entry_node(
        builder, 35, LEAVE_DESCRIPTION, "gameJournalQuestDescription", 2
    )
    player_left = trigger_condition_node(
        builder, 36, CLEANUP_TRIGGER_REF, "IsOutside"
    )
    leave_succeeded = objective_node(builder, 37, LEAVE_OBJECTIVE)
    guards_inactive = spawn_manager_node(builder, 38, "Deactivate")

    guard_attitude_neutral = tuple(
        attitude_group_node(builder, 40 + index, entry_name, "neutral")
        for index, entry_name in enumerate(GUARD_ENTRIES)
    )
    guard_attitude_hostile = tuple(
        attitude_group_node(builder, 43 + index, entry_name, "hostile")
        for index, entry_name in enumerate(GUARD_ENTRIES)
    )
    guard_attitude_ready = logical_and_node(builder, 46, len(GUARD_ENTRIES))
    guard_combat_targets = tuple(
        combat_target_node(builder, 47 + index, entry_name)
        for index, entry_name in enumerate(GUARD_ENTRIES)
    )
    guard_combat_threats = tuple(
        inject_combat_threat_node(builder, 50 + index, entry_name)
        for index, entry_name in enumerate(GUARD_ENTRIES)
    )

    chain: tuple[tuple[GraphNode, str], ...] = (
        (reach_active, "Active"),
        (reach_description, "Active"),
        (mappin_active, "Active"),
        (stage_started, "In"),
        (access_point_disabled, "In"),
        (guards_active, "In"),
        (guards_ready, "In"),
        (player_arrived, "In"),
        (reach_succeeded, "Succeeded"),
        (mappin_inactive, "Inactive"),
        (extract_active, "Active"),
        (extract_description, "Active"),
        (extract_mappin, "Active"),
        (access_point_enabled, "In"),
        (hacking_succeeded, "In"),
        (cache_acquired, "In"),
        (post_hack_delay, "In"),
        (access_point_disabled_final, "In"),
        (extract_succeeded, "Succeeded"),
        (extract_mappin_inactive, "Inactive"),
        (shard_one, "Active"),
        (shard_two, "Active"),
        (recovered_items, "In"),
        (leave_active, "Active"),
        (leave_description, "Active"),
        (player_left, "In"),
        (leave_succeeded, "Succeeded"),
        (guards_inactive, "In"),
    )

    previous = phase_input
    for destination, destination_socket in chain:
        source_socket = "Out"
        builder.connect(
            previous,
            destination,
            source_socket=source_socket,
            destination_socket=destination_socket,
        )
        previous = destination

    for index in range(len(GUARD_ENTRIES)):
        builder.connect(player_arrived, guard_attitude_neutral[index])
        builder.connect(
            guard_attitude_neutral[index], guard_attitude_hostile[index]
        )
        builder.connect(
            guard_attitude_hostile[index],
            guard_attitude_ready,
            destination_socket=f"In{index + 1}",
        )
        builder.connect(
            guard_attitude_ready,
            guard_combat_targets[index],
            source_socket="Out1",
        )
        builder.connect(
            guard_combat_targets[index],
            guard_combat_threats[index],
            source_socket="Success",
        )
    builder.connect_to_earlier_output(previous, phase_output)

    phase = {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": "2026-05-08T15:41:13.0794458Z",
            "DataType": "CR2W",
            "ArchiveFileName": ARCHIVE_TARGET,
        },
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {
                "$type": "questQuestPhaseResource",
                "cookingPlatform": "PLATFORM_PC",
                "graph": builder.graph,
                "inplacePhases": [],
                "phasePrefabs": [
                    {
                        "$type": "questQuestPrefabEntry",
                        "prefabNodeRef": node_ref(PHASE_PREFAB_REF),
                    }
                ],
            },
            "EmbeddedFiles": [],
        },
    }
    validate_phase(phase)
    return phase


def walk_json(value: Any) -> Iterable[Any]:
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from walk_json(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_json(child)


def validate_phase(phase: JsonObject) -> None:
    root = phase.get("Data", {}).get("RootChunk", {})
    if root.get("$type") != "questQuestPhaseResource":
        raise ValueError("root must be questQuestPhaseResource")
    prefab = root.get("phasePrefabs", [{}])[0].get("prefabNodeRef", {}).get("$value")
    if prefab != PHASE_PREFAB_REF:
        raise ValueError(f"phase prefab must remain {PHASE_PREFAB_REF}")

    definitions: dict[str, JsonObject] = {}
    references: set[str] = set()
    for value in walk_json(phase):
        if not isinstance(value, dict):
            continue
        if "HandleId" in value:
            handle_id = value["HandleId"]
            if handle_id in definitions:
                raise ValueError(f"duplicate HandleId {handle_id}")
            definitions[handle_id] = value
        if "HandleRefId" in value:
            references.add(value["HandleRefId"])
    missing = sorted(references.difference(definitions), key=int)
    if missing:
        raise ValueError(f"unresolved HandleRefIds: {', '.join(missing)}")

    nodes = root["graph"]["Data"]["nodes"]
    quest_ids = [node["Data"]["id"] for node in nodes]
    if len(quest_ids) != len(set(quest_ids)):
        raise ValueError("quest node IDs must be unique")
    if len(nodes) != EXPECTED_GRAPH_NODES:
        raise ValueError(
            f"expected {EXPECTED_GRAPH_NODES} graph nodes, found {len(nodes)}"
        )


def write_phase(path: Path) -> None:
    phase = build_phase()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(phase, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="build and validate without writing the CR2W-JSON",
    )
    args = parser.parse_args()

    phase = build_phase()
    if args.dry_run:
        nodes = phase["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
        print(f"Validated {len(nodes)} post-accept quest nodes")
        return 0

    write_phase(args.output.resolve())
    print(f"Wrote {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
