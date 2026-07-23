#!/usr/bin/env python3
"""Generate the deterministic gq000 drop-point delivery questphase.

The cache phase grants ``Items.gq000_datacache`` before this sibling phase is
entered.  This graph waits until the item is present, reserves it to Kabuki's
live ``drop_point_009``, waits for the drop-point deposit fact, completes the
delivery objective, and runs Morrow's authored two-choice phone exchange.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable

from generate_cache_phase import (
    GraphNode,
    PhaseGraphBuilder,
    cname,
    entity_reference,
    fact_node,
    input_node,
    journal_entry_node,
    journal_path,
    mappin_node,
    node_ref,
    objective_node,
    output_node,
    realtime_delay_node,
    tweakdbid,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "source/raw/mod/gq000/phases/gq000_delivery.questphase.json"
ARCHIVE_TARGET = str(ROOT / "source/archive/mod/gq000/phases/gq000_delivery.questphase")

DELIVERY_OBJECTIVE = "quests/minor_quest/gq000/gq000_03/gq000_03_obj_deliver_cache"
DELIVERY_DESCRIPTION = f"{DELIVERY_OBJECTIVE}/gq000_03_desc_deliver_cache"
DELIVERY_MAPPIN = f"{DELIVERY_OBJECTIVE}/gq000_03_qmp_drop_point"
QUEST_PATH = "quests/minor_quest/gq000"

MORROW_CONVERSATION = "contacts/morrow/gq000_04_delivery"
MORROW_CACHE_AUTHENTICATED = f"{MORROW_CONVERSATION}/01_msg_cache_authenticated"
MORROW_ROUTE_FOUND = f"{MORROW_CONVERSATION}/02_msg_route_found"
MORROW_RESPONSE_GROUP = f"{MORROW_CONVERSATION}/03_ch_delivery_response"
MORROW_PAY_CHOICE = f"{MORROW_RESPONSE_GROUP}/03a_ch_pay_me"
MORROW_ROUTE_CHOICE = f"{MORROW_RESPONSE_GROUP}/03b_ch_what_route"
MORROW_PAY_REPLY = f"{MORROW_CONVERSATION}/04a_msg_pay_adjusted"
MORROW_ROUTE_REPLY = f"{MORROW_CONVERSATION}/04b_msg_route_explained"
MORROW_MORE_WORK = f"{MORROW_CONVERSATION}/05_msg_more_work"

DATACACHE_ITEM = "Items.gq000_datacache"
DATACACHE_DEPOSIT_FACT = "gq000_datacache"
COMPLETION_REWARD = "QuestRewards.gq000_completion"
DROP_POINT_REF = (
    "$/03_night_city/c_watson/kabuki/"
    "kabuki_drop_points_prefabAR4NTYY/drop_point_009_prefabBIYNP3Y"
)

EXPECTED_GRAPH_NODES = 25
EXPECTED_GRAPH_EDGES = 25


JsonObject = dict[str, Any]


def inventory_condition_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    item_id: str,
    *,
    quantity: int = 1,
) -> GraphNode:
    """Wait until the local player owns at least ``quantity`` of an item."""

    condition_type = builder.handles.wrap(
        {
            "$type": "questInventory_ConditionType",
            "comparisonType": "GreaterOrEqual",
            "isPlayer": 1,
            "itemID": tweakdbid(item_id),
            "itemTag": cname("None"),
            "objectRef": entity_reference(),
            "quantity": quantity,
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


def fact_condition_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    fact_name: str,
    *,
    comparison: str = "Greater",
    value: int = 0,
) -> GraphNode:
    condition_type = builder.handles.wrap(
        {
            "$type": "questVarComparison_ConditionType",
            "comparisonType": comparison,
            "factName": fact_name,
            "value": value,
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questFactsDBCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def _empty_action_widget_package() -> JsonObject:
    """Return the inherited action defaults serialized by vanilla drop points."""

    return {
        "$type": "SActionWidgetPackage",
        "action": None,
        "bckgroundTextureID": {
            "$type": "TweakDBID",
            "$storage": "uint64",
            "$value": "0",
        },
        "customData": None,
        "dependendActions": [],
        "displayName": "",
        "iconID": cname("None"),
        "iconTextureID": {
            "$type": "TweakDBID",
            "$storage": "uint64",
            "$value": "0",
        },
        "isValid": 1,
        "isWidgetInactive": 0,
        "libraryID": cname("None"),
        "libraryPath": {
            "$type": "redResourceReferenceScriptToken",
            "resource": {
                "DepotPath": {
                    "$type": "ResourcePath",
                    "$storage": "uint64",
                    "$value": "0",
                },
                "Flags": "Soft",
            },
        },
        "orientation": "Horizontal",
        "ownerID": {
            "$type": "gamePersistentID",
            "componentName": cname("None"),
            "entityHash": "0",
        },
        "ownerIDClassName": cname("None"),
        "placement": "DOCKED",
        "textData": None,
        "wasInitalized": 0,
        "widget": None,
        "widgetName": "",
        "widgetState": "DEFAULT",
        "widgetTweakDBID": {
            "$type": "TweakDBID",
            "$storage": "uint64",
            "$value": "0",
        },
    }


def _empty_interaction_choice() -> JsonObject:
    return {
        "$type": "gameinteractionsChoice",
        "caption": "",
        "captionParts": {
            "$type": "gameinteractionsChoiceCaption",
            "parts": [],
        },
        "choiceMetaData": {
            "$type": "gameinteractionsChoiceMetaData",
            "tweakDBID": {
                "$type": "TweakDBID",
                "$storage": "uint64",
                "$value": "0",
            },
            "tweakDBName": "",
            "type": {
                "$type": "gameinteractionsChoiceTypeWrapper",
                "properties": 0,
            },
        },
        "data": [],
        "doNotTurnOffPreventionSystem": 0,
        "lookAtDescriptor": {
            "$type": "gameinteractionsChoiceLookAtDescriptor",
            "offset": {"$type": "Vector3", "X": 0, "Y": 0, "Z": 0},
            "orbId": {"$type": "gameinteractionsOrbID", "id": 0},
            "slotName": cname("None"),
            "type": "Root",
        },
    }


def reserve_drop_point_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    item_id: str,
    drop_point_ref: str,
) -> GraphNode:
    """Reserve one quest item to a live vanilla drop-point controller."""

    event = builder.handles.wrap(
        {
            "$type": "ReserveItemToThisDropPoint",
            "actionName": cname("None"),
            "actionWidgetPackage": _empty_action_widget_package(),
            "activationTimeReduction": 0,
            "activeStatusEffect": {
                "$type": "TweakDBID",
                "$storage": "uint64",
                "$value": "0",
            },
            "attachedProgram": {
                "$type": "TweakDBID",
                "$storage": "uint64",
                "$value": "0",
            },
            "calculatedBaseCost": 0,
            "canSkipPayCost": 0,
            "canTriggerStim": 1,
            "clearanceLevel": 0,
            "costComponents": [],
            "deviceActionQueue": None,
            "disableSpread": 0,
            "duration": 0,
            "executor": None,
            "hasInteraction": 0,
            "inactiveReason": "",
            "inkWidgetID": {
                "$type": "TweakDBID",
                "$storage": "uint64",
                "$value": "0",
            },
            "interactionChoice": _empty_interaction_choice(),
            "interactionIconType": {
                "$type": "TweakDBID",
                "$storage": "uint64",
                "$value": "0",
            },
            "interactionLayer": cname("None"),
            "isActionQueueingUsed": 0,
            "isActionRPGCheckDissabled": 0,
            "IsAppliedByMonowire": 0,
            "isInactive": 0,
            "isQueuedAction": 0,
            "isQuickHack": 0,
            "isSpiderbotAction": 0,
            "isTargetDead": 0,
            "item": tweakdbid(item_id),
            "localizedObjectName": "",
            "objectActionID": {
                "$type": "TweakDBID",
                "$storage": "uint64",
                "$value": "0",
            },
            "objectActionRecord": None,
            "paymentQuantity": 0,
            "prop": None,
            "proxyExecutor": None,
            "requesterID": {"$type": "entEntityID", "hash": "0"},
            "shouldActivateDevice": 0,
            "spiderbotActionLocationOverride": node_ref("0", storage="uint64"),
            "wasPerformedOnOwner": 0,
            "widgetStyle": "DarkBlue",
        }
    )
    return builder.node(
        quest_id,
        "questEventManagerNodeDefinition",
        input_names=("In",),
        properties={
            "componentName": cname("controller"),
            "event": event,
            "isObjectPlayer": 0,
            "isUiEvent": 0,
            "managerName": "DropPointManager",
            "objectRef": entity_reference(drop_point_ref),
            "PSClassName": cname("DropPointControllerPS"),
        },
    )


def journal_entry_visited_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    path: str,
    class_name: str,
    *,
    file_index: int = 1,
) -> GraphNode:
    condition_type = builder.handles.wrap(
        {
            "$type": "questJournalEntryVisited_ConditionType",
            "path": journal_path(
                builder,
                path,
                class_name,
                file_index,
            ),
            "visited": 1,
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questJournalCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def journal_choice_succeeded_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    path: str,
) -> GraphNode:
    condition_type = builder.handles.wrap(
        {
            "$type": "questJournalEntryState_ConditionType",
            "inverted": 0,
            "path": journal_path(
                builder,
                path,
                "gameJournalPhoneChoiceEntry",
                1,
            ),
            "state": "Succeeded",
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questJournalCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def logical_xor_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    input_count: int,
) -> GraphNode:
    return builder.node(
        quest_id,
        "questLogicalXorNodeDefinition",
        input_names=tuple(f"In{index}" for index in range(1, input_count + 1)),
        output_names=("Out1",),
        properties={
            "inputSocketCount": input_count,
            "outputSocketCount": 1,
        },
    )


def quest_completion_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    path: str,
) -> GraphNode:
    node_type = builder.handles.wrap(
        {
            "$type": "questJournalQuestEntry_NodeType",
            "optional": 0,
            "path": journal_path(builder, path, "gameJournalQuest", 2),
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


def reward_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    reward_id: str,
) -> GraphNode:
    node_type = builder.handles.wrap(
        {
            "$type": "questGiveReward_NodeType",
            "rewards": [tweakdbid(reward_id)],
        }
    )
    return builder.node(
        quest_id,
        "questRewardManagerNodeDefinition",
        input_names=("In",),
        properties={"type": node_type},
    )


def build_phase() -> JsonObject:
    builder = PhaseGraphBuilder()
    phase_input = input_node(builder)
    phase_output = output_node(builder)

    delivery_active = objective_node(builder, 10, DELIVERY_OBJECTIVE)
    delivery_description = journal_entry_node(
        builder,
        11,
        DELIVERY_DESCRIPTION,
        "gameJournalQuestDescription",
        2,
    )
    delivery_mappin_active = mappin_node(
        builder,
        12,
        DELIVERY_MAPPIN,
        disable_previous_mappins=True,
    )
    datacache_present = inventory_condition_node(builder, 13, DATACACHE_ITEM)
    reserve_datacache = reserve_drop_point_node(
        builder,
        14,
        DATACACHE_ITEM,
        DROP_POINT_REF,
    )
    datacache_deposited = fact_condition_node(
        builder,
        15,
        DATACACHE_DEPOSIT_FACT,
    )
    cache_delivered = fact_node(builder, 16, "gq000_cache_delivered")
    delivery_succeeded = objective_node(builder, 17, DELIVERY_OBJECTIVE)
    delivery_mappin_inactive = mappin_node(builder, 18, DELIVERY_MAPPIN)
    message_delay = realtime_delay_node(builder, 19, seconds=1)
    cache_authenticated = journal_entry_node(
        builder,
        20,
        MORROW_CACHE_AUTHENTICATED,
        "gameJournalPhoneMessage",
        1,
    )
    route_found = journal_entry_node(
        builder,
        21,
        MORROW_ROUTE_FOUND,
        "gameJournalPhoneMessage",
        1,
    )
    response_group = journal_entry_node(
        builder,
        22,
        MORROW_RESPONSE_GROUP,
        "gameJournalPhoneChoiceGroup",
        1,
    )
    pay_choice_succeeded = journal_choice_succeeded_node(
        builder,
        23,
        MORROW_PAY_CHOICE,
    )
    route_choice_succeeded = journal_choice_succeeded_node(
        builder,
        24,
        MORROW_ROUTE_CHOICE,
    )
    pay_reply = journal_entry_node(
        builder,
        25,
        MORROW_PAY_REPLY,
        "gameJournalPhoneMessage",
        1,
    )
    route_reply = journal_entry_node(
        builder,
        26,
        MORROW_ROUTE_REPLY,
        "gameJournalPhoneMessage",
        1,
    )
    response_join = logical_xor_node(builder, 27, 2)
    more_work = journal_entry_node(
        builder,
        28,
        MORROW_MORE_WORK,
        "gameJournalPhoneMessage",
        1,
    )
    more_work_visited = journal_entry_visited_node(
        builder,
        29,
        MORROW_MORE_WORK,
        "gameJournalPhoneMessage",
    )
    completion_reward = reward_node(builder, 30, COMPLETION_REWARD)
    quest_completed = fact_node(builder, 31, "gq000_completed")
    quest_succeeded = quest_completion_node(builder, 32, QUEST_PATH)

    main_chain = (
        (delivery_active, "Active"),
        (delivery_description, "Active"),
        (delivery_mappin_active, "Active"),
        (datacache_present, "In"),
        (datacache_deposited, "In"),
        (cache_delivered, "In"),
        (delivery_succeeded, "Succeeded"),
        (delivery_mappin_inactive, "Inactive"),
        (message_delay, "In"),
        (cache_authenticated, "Active"),
        (route_found, "Active"),
        (response_group, "Active"),
    )
    previous = phase_input
    for destination, destination_socket in main_chain:
        builder.connect(previous, destination, destination_socket=destination_socket)
        previous = destination

    # The event node is a fire-and-forget side effect in vanilla delivery
    # phases. The deposit fact wait starts from the same inventory gate instead
    # of depending on an EventManager output that vanilla never consumes.
    builder.connect(datacache_present, reserve_datacache)

    builder.connect(response_group, pay_choice_succeeded)
    builder.connect(response_group, route_choice_succeeded)
    builder.connect(pay_choice_succeeded, pay_reply, destination_socket="Active")
    builder.connect(route_choice_succeeded, route_reply, destination_socket="Active")
    builder.connect(pay_reply, response_join, destination_socket="In1")
    builder.connect(route_reply, response_join, destination_socket="In2")
    builder.connect(response_join, more_work, source_socket="Out1", destination_socket="Active")
    builder.connect(more_work, more_work_visited)
    builder.connect(more_work_visited, completion_reward)
    builder.connect(completion_reward, quest_completed)
    builder.connect(quest_completed, quest_succeeded, destination_socket="Succeeded")
    builder.connect_to_earlier_output(quest_succeeded, phase_output)

    phase = {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": "2026-07-22T00:00:00Z",
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
                "phasePrefabs": [],
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
    if root.get("phasePrefabs") != []:
        raise ValueError("delivery phase uses only absolute world refs")

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
        print(f"Validated {len(nodes)} delivery quest nodes")
        return 0

    write_phase(args.output.resolve())
    print(f"Wrote {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
