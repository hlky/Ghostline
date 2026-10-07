"""Explicit objective handoffs for existing proven phase templates."""

from __future__ import annotations

import copy
from typing import Any

from quest_flow import walk


def apply_objective_lifecycle(stage: Any, document: dict[str, Any]) -> None:
    if stage.type not in {"meet_contact", "braindance_analysis"}:
        return  # Generated block builders implement their own policies directly.
    policy = stage.data.get("objective_lifecycle", {})
    if policy.get("on_success") == "retain":
        retain_objective_transition(document, stage.data["objective"])
    if stage.type == "braindance_analysis" and policy.get("on_enter") == "retain":
        retain_objective_transition(document, stage.data["objective"], "Active")


def retain_objective_transition(
    document: dict[str, Any],
    objective: str,
    transition: str = "Succeeded",
) -> dict[str, Any]:
    """Bypass one journal state transition while preserving its continuation."""

    graph_nodes = document["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
    journal_nodes = [
        wrapper
        for wrapper in graph_nodes
        if wrapper.get("Data", {}).get("$type") == "questJournalNodeDefinition"
        and wrapper["Data"]
        .get("type", {})
        .get("Data", {})
        .get("path", {})
        .get("Data", {})
        .get("realPath")
        == objective
    ]
    definitions = {
        str(item["HandleId"]): item
        for item in walk(document)
        if "HandleId" in item and isinstance(item.get("Data"), dict)
    }

    def connected_transition(wrapper):
        for socket in wrapper["Data"]["sockets"]:
            socket = definitions[
                str(socket.get("HandleId", socket.get("HandleRefId")))
            ]["Data"]
            if socket.get("name", {}).get("$value") == transition and socket.get(
                "connections"
            ):
                return True
        return False

    journal_nodes = [node for node in journal_nodes if connected_transition(node)]
    if len(journal_nodes) != 1:
        raise ValueError(
            "Expected one meet-stage review objective transition, found "
            f"{len(journal_nodes)}"
        )
    journal = journal_nodes[0]

    definitions = {
        str(item["HandleId"]): item
        for item in walk(document)
        if isinstance(item, dict)
        and "HandleId" in item
        and isinstance(item.get("Data"), dict)
    }

    def handle_id(wrapper: dict[str, Any]) -> str:
        value = wrapper.get("HandleId", wrapper.get("HandleRefId"))
        if value is None:
            raise ValueError("Expected a CR2W handle wrapper")
        return str(value)

    def resolve(wrapper: dict[str, Any]) -> dict[str, Any]:
        return definitions[handle_id(wrapper)]

    def socket(name: str) -> tuple[int, dict[str, Any]]:
        for index, wrapper in enumerate(journal["Data"]["sockets"]):
            definition = resolve(wrapper)
            if definition["Data"].get("name", {}).get("$value") == name:
                return index, definition
        raise ValueError(f"Meet-stage objective has no {name} socket")

    succeeded_index, succeeded_socket = socket(transition)
    _, output_socket = socket("Out")
    succeeded_id = handle_id(succeeded_socket)
    output_id = handle_id(output_socket)
    connections = [
        item
        for item in walk(document)
        if isinstance(item, dict)
        and item.get("Data", {}).get("$type") == "graphGraphConnectionDefinition"
    ]
    incoming = [
        item
        for item in connections
        if handle_id(item["Data"]["destination"]) == succeeded_id
    ]
    outgoing = [
        item for item in connections if handle_id(item["Data"]["source"]) == output_id
    ]
    if len(incoming) != 1 or len(outgoing) != 1:
        raise ValueError(
            "Meet-stage objective handoff must have exactly one incoming "
            "and one outgoing edge"
        )

    incoming_connection = incoming[0]
    outgoing_connection = outgoing[0]
    incoming_id = handle_id(incoming_connection)
    old_objective_destination = copy.deepcopy(
        incoming_connection["Data"]["destination"]
    )
    next_destination = copy.deepcopy(outgoing_connection["Data"]["destination"])
    if "HandleId" not in old_objective_destination:
        raise ValueError("Objective input socket must be defined by its incoming edge")
    if "HandleId" not in next_destination:
        raise ValueError("Mappin input socket must be defined by the objective edge")

    old_objective_destination["Data"]["connections"] = []
    journal["Data"]["sockets"][succeeded_index] = old_objective_destination
    next_destination["Data"]["connections"] = [{"HandleRefId": incoming_id}]
    incoming_connection["Data"]["destination"] = next_destination
    output_socket["Data"]["connections"] = []

    return document
