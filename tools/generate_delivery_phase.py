#!/usr/bin/env python3
"""Generate the deterministic gq000 drop-point delivery questphase.

The cache phase grants ``Items.gq000_datacache`` before this sibling phase is
entered.  This graph waits until the item is present, reserves it to Kabuki's
live ``drop_point_009``, waits for the drop-point deposit fact, completes the
delivery objective, and runs Morrow's authored two-choice phone exchange.
"""

from __future__ import annotations

from phase_graph import phase_document
from phase_graph import (
    inventory_condition_node as inventory_condition_node,
    fact_condition_node as fact_condition_node,
    _empty_action_widget_package as _empty_action_widget_package,
    _empty_interaction_choice as _empty_interaction_choice,
    reserve_drop_point_node as reserve_drop_point_node,
    journal_entry_visited_node as journal_entry_visited_node,
    journal_choice_succeeded_node as journal_choice_succeeded_node,
    logical_xor_node as logical_xor_node,
    quest_completion_node as quest_completion_node,
    reward_node as reward_node,
)

import argparse
import json
from pathlib import Path
from typing import Any, Iterable

from phase_graph import (
    GraphNode as GraphNode,
    PhaseGraphBuilder as PhaseGraphBuilder,
    cname as cname,
    entity_reference as entity_reference,
    fact_node as fact_node,
    input_node as input_node,
    journal_entry_node as journal_entry_node,
    journal_path as journal_path,
    mappin_node as mappin_node,
    node_ref as node_ref,
    objective_node as objective_node,
    output_node as output_node,
    realtime_delay_node as realtime_delay_node,
    tweakdbid as tweakdbid,
)


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "projects/shared/ghostline-runtime/source/raw/mod/gq000/phases/gq000_delivery.questphase.json"
ARCHIVE_TARGET = str(ROOT / "projects/shared/ghostline-runtime/source/archive/mod/gq000/phases/gq000_delivery.questphase")

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

    phase = phase_document(builder, Path(ARCHIVE_TARGET),
        exported_datetime="2026-07-22T00:00:00Z")
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
