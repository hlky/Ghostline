"""Compile explicit outcome routes using the same proven phase graph nodes."""

from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

from phase_graph import (
    PhaseGraphBuilder,
    input_node,
    output_node,
    phase_document,
    journal_entry_node,
    mappin_node,
    fact_node,
    quest_completion_node,
)
from quest_flow import stage_inputs, stage_outcomes, stage_transitions, walk
from quest_types import QuestSpec


def order_handles(document: dict[str, Any]) -> dict[str, Any]:
    """Define each handle at its first use, allowing back edges and joins.

    RED graphs can be cyclic; JSON importer references cannot point forward.
    Re-embedding the same handle at its first reference changes no graph edge.
    """
    definitions = {
        str(item["HandleId"]): item for item in walk(document) if "HandleId" in item
    }
    defined: set[str] = set()

    def visit(value: Any) -> Any:
        if isinstance(value, list):
            return [visit(child) for child in value]
        if not isinstance(value, dict):
            return value
        identifier = value.get("HandleId", value.get("HandleRefId"))
        if identifier is not None:
            identifier = str(identifier)
            if identifier in defined:
                return {"HandleRefId": identifier}
            defined.add(identifier)
            definition = definitions[identifier]
            return {key: visit(child) for key, child in definition.items()}
        return {key: visit(child) for key, child in value.items()}

    return visit(deepcopy(document))


def build_explicit_orchestration(
    spec: QuestSpec, archive_target: Path
) -> dict[str, Any]:
    # These are compatibility exports for established checkpoint and resource
    # encodings. Runtime import keeps the public compiler API cycle-free.
    from quest_compiler import checkpoint_node, debug_step_node, phase_node

    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    entries = {}
    phases = {}
    next_id = max(stage.node_id for stage in spec.stages) + 1

    def allocate() -> int:
        nonlocal next_id
        result = next_id
        next_id += 1
        return result

    for stage in spec.stages:
        prefix = []
        if stage.type == "meet_contact":
            if isinstance(stage.data.get("opening_message"), str):
                prefix.append(
                    (
                        journal_entry_node(
                            builder,
                            allocate(),
                            stage.data["opening_message"],
                            "gameJournalPhoneMessage",
                            1,
                        ),
                        "Active",
                    )
                )
            if (
                stage.data.get("objective_lifecycle", {}).get("on_enter", "activate")
                != "retain"
            ):
                prefix.append(
                    (
                        journal_entry_node(
                            builder,
                            allocate(),
                            stage.data["objective"],
                            "gameJournalQuestObjective",
                            2,
                        ),
                        "Active",
                    )
                )
            prefix.extend(
                [
                    (
                        journal_entry_node(
                            builder,
                            allocate(),
                            stage.data["description_entry"],
                            "gameJournalQuestDescription",
                            2,
                        ),
                        "Active",
                    ),
                    (
                        mappin_node(
                            builder,
                            allocate(),
                            stage.data["mappin"],
                            disable_previous_mappins=True,
                        ),
                        "Active",
                    ),
                ]
            )
        if stage.data.get("checkpoint"):
            prefix.append(
                (
                    checkpoint_node(
                        builder,
                        allocate(),
                        stage.data["checkpoint"],
                        retry_on_failure=stage.data.get("retry_checkpoint", False),
                    ),
                    "In",
                )
            )
        if spec.debug_fact:
            prefix.append(
                (
                    debug_step_node(
                        builder, allocate(), spec.debug_fact, (stage.index + 1) * 10
                    ),
                    "In",
                )
            )
        phase = phase_node(
            builder,
            stage.node_id,
            stage.phase_resource,
            inputs=tuple(stage_inputs(stage).values()),
            outputs=tuple(stage_outcomes(stage).values()),
        )
        chain = [*prefix, (phase, stage_inputs(stage)["start"])]
        for (source, _), (destination, socket) in zip(chain, chain[1:]):
            builder.connect(source, destination, destination_socket=socket)
        entries[stage.id] = chain[0]
        phases[stage.id] = phase

    entry, socket = entries[spec.entry_stage or spec.stages[0].id]
    builder.connect(start, entry, destination_socket=socket)
    routes = stage_transitions(spec)
    terminal_entries = {}
    if spec.completion:
        for outcome, policy in spec.completion["outcomes"].items():
            journal = quest_completion_node(
                builder, allocate(), spec.completion["quest_path"]
            )
            terminal_entries[outcome] = (journal, policy["state"])
            tail = journal
            if policy.get("fact"):
                tail = fact_node(builder, allocate(), policy["fact"])
                builder.connect(journal, tail)
            builder.connect(tail, end)
    for stage in spec.stages:
        for outcome, target in routes[stage.id].items():
            destination, socket = (
                terminal_entries.get(outcome, (end, "In"))
                if target == "$end"
                else entries[target]
            )
            builder.connect(
                phases[stage.id],
                destination,
                source_socket=stage_outcomes(stage)[outcome],
                destination_socket=socket,
            )
    return order_handles(
        phase_document(builder, archive_target, phase_prefabs=spec.phase_prefabs)
    )
