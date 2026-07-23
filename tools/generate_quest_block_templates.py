#!/usr/bin/env python3
"""Generate the small, Ghostline-owned quest block template corpus.

These templates deliberately contain exact scalar placeholders.  The typed
quest compiler replaces complete scalar values only, leaving the audited CR2W
handle graph unchanged.

The templates are structural candidates, not claims of in-game validation.
Their supported variants and vanilla provenance are documented beside the
generated resources.
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
    input_node,
    journal_entry_node,
    node_ref,
    objective_node,
    output_node,
)
from generate_delivery_phase import fact_condition_node, logical_xor_node
from quest_compiler import (
    community_action_node,
    fact_node,
    phase_document,
    write_json,
)


ROOT = Path(__file__).resolve().parents[1]
DEPOT_ROOT = r"mod\ghostline\quest_blocks\templates"
RAW_ROOT = ROOT / "source/raw/mod/ghostline/quest_blocks/templates"

DEVICE = "{{device}}"
CONTROLLER = "{{controller_class}}"
ACTION = "{{action}}"
COMPLETION_FUNCTION = "{{completion_function}}"
COMMUNITY = "{{community}}"
OBJECTIVE = "{{objective}}"
DESCRIPTION = "{{description_entry}}"
CLUE_OBJECT = "{{clue_object_ref}}"
CONDITION_FACT = "{{condition_fact}}"
SUCCESS_FACT = "{{success_fact}}"
FAILURE_FACT = "{{failure_fact}}"
BRANCH_A_CONDITION = "{{branch_a_condition}}"
BRANCH_A_FACT = "{{branch_a_set_fact}}"
BRANCH_B_CONDITION = "{{branch_b_condition}}"
BRANCH_B_FACT = "{{branch_b_set_fact}}"

JsonObject = dict[str, Any]


def template_target(name: str) -> Path:
    return ROOT / "source/archive/mod/ghostline/quest_blocks/templates" / (
        f"{name}.questphase"
    )


def device_manager(
    builder: PhaseGraphBuilder,
    quest_id: int,
    *,
    device: str,
    controller: str,
    action: str,
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
    *,
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


def character_spawned(
    builder: PhaseGraphBuilder, quest_id: int, community: str
) -> GraphNode:
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
            "objectRef": entity_reference(community),
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


def community_defeated(
    builder: PhaseGraphBuilder, quest_id: int, community: str
) -> GraphNode:
    comparison = builder.handles.wrap(
        {
            "$type": "questComparisonParam",
            "comparisonType": "GreaterOrEqual",
            "count": 0,
            "entireCommunity": 1,
        }
    )
    condition_type = builder.handles.wrap(
        {
            "$type": "questCharacterKilled_ConditionType",
            "comparisonParams": comparison,
            "defeated": 1,
            "killed": 1,
            "objectRef": entity_reference(community),
            "source": None,
            "unconscious": 1,
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


def scan_started(
    builder: PhaseGraphBuilder, quest_id: int, object_ref: str
) -> GraphNode:
    condition_type = builder.handles.wrap(
        {
            "$type": "questScan_ConditionType",
            "eventType": "Started",
            "objectRef": entity_reference(object_ref),
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


def build_interact_device() -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    action = device_manager(
        builder, 10, device=DEVICE, controller=CONTROLLER, action=ACTION
    )
    completed = device_condition(
        builder,
        11,
        device=DEVICE,
        controller=CONTROLLER,
        function=COMPLETION_FUNCTION,
    )
    builder.connect(start, action)
    builder.connect(action, completed)
    builder.connect_to_earlier_output(completed, end)
    return phase_document(builder, template_target("interact_device"))


def build_combat_encounter() -> JsonObject:
    """Already-hostile, whole-community activation and defeat gate."""

    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    activate = community_action_node(builder, 10, COMMUNITY, "Activate")
    spawned = character_spawned(builder, 11, COMMUNITY)
    defeated = community_defeated(builder, 12, COMMUNITY)
    builder.connect(start, activate)
    builder.connect(activate, spawned)
    builder.connect(spawned, defeated)
    builder.connect_to_earlier_output(defeated, end)
    return phase_document(builder, template_target("combat_encounter"))


def build_investigate_clues() -> JsonObject:
    """One scan-started clue; multi-clue graphs are generated separately later."""

    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    objective = objective_node(builder, 10, OBJECTIVE)
    description = journal_entry_node(
        builder, 11, DESCRIPTION, "gameJournalQuestDescription", 2
    )
    scanned = scan_started(builder, 12, CLUE_OBJECT)
    objective_done = objective_node(builder, 13, OBJECTIVE)
    builder.connect(start, objective, destination_socket="Active")
    builder.connect(objective, description, destination_socket="Active")
    builder.connect(description, scanned)
    builder.connect(scanned, objective_done, destination_socket="Succeeded")
    builder.connect_to_earlier_output(objective_done, end)
    return phase_document(builder, template_target("investigate_clues"))


def build_optional_condition() -> JsonObject:
    """Evaluate a boolean fact immediately and converge both outcomes."""

    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    objective = objective_node(builder, 10, OBJECTIVE)
    passed = fact_condition_node(
        builder, 11, CONDITION_FACT, comparison="Greater", value=0
    )
    failed = fact_condition_node(
        builder, 12, CONDITION_FACT, comparison="Equal", value=0
    )
    success = fact_node(builder, 13, SUCCESS_FACT)
    failure = fact_node(builder, 14, FAILURE_FACT)
    join = logical_xor_node(builder, 15, input_count=2)
    objective_done = objective_node(builder, 16, OBJECTIVE)
    builder.connect(start, objective, destination_socket="Active")
    builder.connect(objective, passed)
    builder.connect(objective, failed)
    builder.connect(passed, success)
    builder.connect(failed, failure)
    builder.connect(success, join, destination_socket="In1")
    builder.connect(failure, join, destination_socket="In2")
    builder.connect(
        join,
        objective_done,
        source_socket="Out1",
        destination_socket="Succeeded",
    )
    builder.connect_to_earlier_output(objective_done, end)
    return phase_document(builder, template_target("optional_condition"))


def build_choice_gate() -> JsonObject:
    """Two fact-backed alternatives which set a branch fact and reconverge."""

    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    branch_a = fact_condition_node(
        builder, 10, BRANCH_A_CONDITION, comparison="Greater", value=0
    )
    branch_b = fact_condition_node(
        builder, 11, BRANCH_B_CONDITION, comparison="Greater", value=0
    )
    choose_a = fact_node(builder, 12, BRANCH_A_FACT)
    choose_b = fact_node(builder, 13, BRANCH_B_FACT)
    join = logical_xor_node(builder, 14, input_count=2)
    builder.connect(start, branch_a)
    builder.connect(start, branch_b)
    builder.connect(branch_a, choose_a)
    builder.connect(branch_b, choose_b)
    builder.connect(choose_a, join, destination_socket="In1")
    builder.connect(choose_b, join, destination_socket="In2")
    builder.connect_to_earlier_output(join, end, source_socket="Out1")
    return phase_document(builder, template_target("choice_gate"))


BUILDERS = {
    "interact_device": build_interact_device,
    "combat_encounter": build_combat_encounter,
    "investigate_clues": build_investigate_clues,
    "optional_condition": build_optional_condition,
    "choice_gate": build_choice_gate,
}


def main() -> int:
    for name, build in BUILDERS.items():
        write_json(RAW_ROOT / f"{name}.questphase.json", build())
    print(f"Wrote {len(BUILDERS)} quest block templates under {RAW_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
