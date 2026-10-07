"""Braindance clue graph construction and independent clue-contract auditing."""
from __future__ import annotations
import copy
import hashlib
from typing import Any
from braindance_support.scene_types import (
    BraindancePipelineError,
    _SceneHandleAllocator,
    _cname,
    _dynamic_entity_reference,
    _fnv1a32,
    _scene_input_socket,
    _scene_output_socket,
    _scene_quest_node,
    _walk,
)
from braindance_support.scene_graph import (
    SceneGraphIndex,
)


def audit_clues(
    root: dict[str, Any], all_values: list[dict[str, Any]], graph: SceneGraphIndex,
    handoff: dict[str, Any] | None, require_functional_clues: bool, errors: list[str],
) -> dict[str, Any]:
    node_by_id = graph.nodes
    outgoing_edges = graph.outgoing_edges
    reachable = graph.reachable
    layers = {
        value.get("layer")
        for value in all_values
        if value.get("$type") == "scneventsClueEvent"
    }
    expected_layers = (
        {clue["layer"] for clue in handoff.get("clues", [])}
        if handoff is not None
        else set()
    )
    missing_layers = sorted(expected_layers - layers)
    if missing_layers:
        errors.append("Scene has no clue events for: " + ", ".join(missing_layers))
    spawned_prop_by_dynamic_name = {
        value: prop
        for prop in root.get("props", [])
        if isinstance(prop, dict)
        if isinstance(prop.get("spawnDespawnParams"), dict)
        if isinstance(
            value := prop["spawnDespawnParams"]
            .get("dynamicEntityUniqueName", {})
            .get("$value"),
            str,
        )
        and value not in {"", "0", "None"}
    }
    spawned_prop_dynamic_names = set(spawned_prop_by_dynamic_name)
    spawned_actor_dynamic_names = {
        value
        for actor in root.get("actors", [])
        if isinstance(actor, dict)
        if isinstance(actor.get("spawnDespawnParams"), dict)
        if isinstance(
            value := actor["spawnDespawnParams"]
            .get("dynamicEntityUniqueName", {})
            .get("$value"),
            str,
        )
        and value not in {"", "0", "None"}
    }
    spawned_dynamic_names = (
        spawned_prop_dynamic_names | spawned_actor_dynamic_names
    )
    clue_entities: dict[str, str] = {}
    clue_events = [
        value
        for value in all_values
        if value.get("$type") == "scneventsClueEvent"
    ]
    for event in clue_events:
        clue_name = event.get("clueName", {}).get("$value")
        clue_entity = event.get("clueEntity")
        if not isinstance(clue_entity, dict):
            errors.append(f"Clue {clue_name!r} has no entity reference")
            continue
        dynamic_name = clue_entity.get("dynamicEntityUniqueName", {}).get(
            "$value"
        )
        node_ref = clue_entity.get("reference", {}).get("$value")
        names = clue_entity.get("names", [])
        resolved = (
            isinstance(dynamic_name, str)
            and dynamic_name in spawned_dynamic_names
        ) or (
            isinstance(node_ref, str)
            and node_ref not in {"", "0"}
            and (
                not names
                or all(
                    isinstance(name, dict)
                    and isinstance(name.get("$value"), str)
                    for name in names
                )
            )
        )
        if not resolved:
            errors.append(
                f"Clue {clue_name!r} does not resolve to a scene prop "
                "or world entity"
            )
        if isinstance(clue_name, str):
            clue_entities[clue_name] = str(dynamic_name or node_ref)
    if handoff is not None and require_functional_clues:
        event_by_name = {
            event.get("clueName", {}).get("$value"): event
            for event in clue_events
        }
        for clue in handoff.get("clues", []):
            if clue.get("layer") != "Visual" or "position" not in clue:
                continue
            event = event_by_name.get(clue.get("id"))
            dynamic_name = (
                event.get("clueEntity", {})
                .get("dynamicEntityUniqueName", {})
                .get("$value")
                if isinstance(event, dict)
                else None
            )
            if (
                not isinstance(dynamic_name, str)
                or dynamic_name not in spawned_prop_dynamic_names
            ):
                errors.append(
                    f"Visual clue {clue['id']!r} has no matching spawned prop"
                )
    functional_clue_count = 0
    clue_availability_facts: dict[str, str] = {}
    if handoff is not None and require_functional_clues:
        clue_event_by_name = {
            event.get("clueName", {}).get("$value"): event
            for event in clue_events
        }
        for clue in handoff.get("clues", []):
            clue_name = clue.get("id")
            fact_name = clue.get("fact")
            event = clue_event_by_name.get(clue_name)
            availability_fact = (
                event.get("factName", {}).get("$value")
                if isinstance(event, dict)
                else None
            )
            has_distinct_availability_fact = (
                isinstance(availability_fact, str)
                and bool(availability_fact)
                and availability_fact != fact_name
            )
            if isinstance(availability_fact, str):
                clue_availability_facts[str(clue_name)] = availability_fact
            if not has_distinct_availability_fact:
                errors.append(
                    f"Clue {clue_name!r} must use a transient availability "
                    "fact distinct from its completion fact"
                )
            target = (
                event.get("clueEntity", {})
                .get("dynamicEntityUniqueName", {})
                .get("$value")
                if isinstance(event, dict)
                else None
            )
            scan_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                for item in _walk(node)
                if item.get("$type") == "questScan_ConditionType"
                and item.get("eventType") == "Finished"
                and item.get("objectRef", {})
                .get("dynamicEntityUniqueName", {})
                .get("$value")
                    == target
            }
            validity_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if any(
                    item.get("$type") == "questPauseConditionNodeDefinition"
                    for item in _walk(node)
                )
                and any(
                    item.get("$type") == "questLogicalCondition"
                    and item.get("operation") == "AND"
                    and any(
                        condition.get("$type")
                        == "questVarComparison_ConditionType"
                        and condition.get("comparisonType") == "Greater"
                        and condition.get("factName") == availability_fact
                        and condition.get("value") == 0
                        for condition in _walk(item)
                    )
                    and any(
                        condition.get("$type")
                        == "scnBraindanceLayer_ConditionType"
                        and condition.get("layer") == clue.get("layer")
                        and isinstance(
                            condition.get("sceneFile", {})
                            .get("DepotPath", {})
                            .get("$value"),
                            str,
                        )
                        and condition["sceneFile"]["DepotPath"]["$value"]
                        not in {"", "0"}
                        for condition in _walk(item)
                    )
                    for item in _walk(node)
                )
            }
            wrong_layers = {
                candidate
                for candidate in ("Visual", "Audio", "Thermal")
                if candidate != clue.get("layer")
            }
            invalidity_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if any(
                    item.get("$type") == "questPauseConditionNodeDefinition"
                    for item in _walk(node)
                )
                and any(
                    item.get("$type") == "questLogicalCondition"
                    and item.get("operation") == "OR"
                    and any(
                        condition.get("$type")
                        == "questVarComparison_ConditionType"
                        and condition.get("comparisonType") == "LessOrEqual"
                        and condition.get("factName") == availability_fact
                        and condition.get("value") == 0
                        for condition in _walk(item)
                    )
                    and wrong_layers.issubset(
                        {
                            condition.get("layer")
                            for condition in _walk(item)
                            if condition.get("$type")
                            == "scnBraindanceLayer_ConditionType"
                            and isinstance(
                                condition.get("sceneFile", {})
                                .get("DepotPath", {})
                                .get("$value"),
                                str,
                            )
                            and condition["sceneFile"]["DepotPath"]["$value"]
                            not in {"", "0"}
                        }
                    )
                    for item in _walk(node)
                )
            }
            target_prop = (
                spawned_prop_by_dynamic_name.get(target)
                if isinstance(target, str)
                else None
            )
            target_prop_id = (
                target_prop.get("propId", {}).get("id")
                if isinstance(target_prop, dict)
                else None
            )
            focus_choice_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if node.get("$type") == "scnChoiceNode"
                and node.get("choiceFlags") == "IsFocusClue"
                and node.get("mode") == "attachToProp"
                and node.get("atpParams", {})
                .get("propId", {})
                .get("id")
                == target_prop_id
                and any(
                    option.get("isSingleChoice") == 1
                    and any(
                        tag.get("$value")
                        == "ChoiceCaptionParts.Inspect"
                        for tag in option.get("iconTagIds", [])
                    )
                    for option in node.get("options", [])
                )
            }
            cut_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if node.get("$type") == "scnCutControlNode"
            }
            inspected_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if any(
                    item.get("$type") == "ToggleFocusClueEvent"
                    and item.get("investigationState") == "INSPECTED"
                    and item.get("isEnabled") == 1
                    and item.get("updatePS") == 1
                    for item in _walk(node)
                )
                and any(
                    item.get("$type") == "questEventManagerNodeDefinition"
                    and item.get("managerName") == "FocusClueManager"
                    and item.get("componentName", {}).get("$value")
                    == "scanning"
                    and item.get("PSClassName", {}).get("$value")
                    == "gameScanningComponentPS"
                    and item.get("objectRef", {})
                    .get("dynamicEntityUniqueName", {})
                    .get("$value")
                    == target
                    for item in _walk(node)
                )
            }
            discovered_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if any(
                    item.get("$type")
                    == "questDiscoverBraindanceClue_NodeType"
                    and item.get("clueName", {}).get("$value") == clue_name
                    for item in _walk(node)
                )
            }
            fact_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if any(
                    item.get("$type") == "questSetVar_NodeType"
                    and item.get("factName") == fact_name
                    and item.get("setExactValue") == 1
                    and item.get("value") == 1
                    for item in _walk(node)
                )
            }
            scanning_enable_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if any(
                    item.get("$type")
                    == "questEnableScanning_NodeType"
                    and item.get("enable") == 1
                    and item.get("objectRef", {})
                    .get("dynamicEntityUniqueName", {})
                    .get("$value")
                    == target
                    for item in _walk(node)
                )
            }
            scanning_disable_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if any(
                    item.get("$type")
                    == "questEnableScanning_NodeType"
                    and item.get("enable") == 0
                    and item.get("objectRef", {})
                    .get("dynamicEntityUniqueName", {})
                    .get("$value")
                    == target
                    for item in _walk(node)
                )
            }
            not_inspected_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if any(
                    item.get("$type") == "ToggleFocusClueEvent"
                    and item.get("investigationState")
                    == "NOT_INSPECTED"
                    and item.get("isEnabled") == 1
                    and item.get("updatePS") == 1
                    for item in _walk(node)
                )
                and any(
                    item.get("$type")
                    == "questEventManagerNodeDefinition"
                    and item.get("managerName")
                    == "FocusClueManager"
                    and item.get("componentName", {}).get("$value")
                    == "scanning"
                    and item.get("PSClassName", {}).get("$value")
                    == "gameScanningComponentPS"
                    and item.get("objectRef", {})
                    .get("dynamicEntityUniqueName", {})
                    .get("$value")
                    == target
                    for item in _walk(node)
                )
            }
            reactivation_sections = {
                node_id
                for node_id, node in node_by_id.items()
                if node.get("$type") == "scnSectionNode"
                and node.get("isFocusClue") == 1
            }
            reactivation_hubs = {
                node_id
                for node_id, node in node_by_id.items()
                if node.get("$type") == "scnHubNode"
            }
            start_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if node.get("$type") == "scnStartNode"
            }

            def has_edge(
                source: int,
                destination: int,
                *,
                destination_name: int,
                ordinal: int,
                source_name: int,
            ) -> bool:
                return (
                    destination,
                    destination_name,
                    ordinal,
                    source_name,
                ) in outgoing_edges(source)

            vanilla_focus_topology = False
            for scan_node in scan_nodes:
                bootstrap_nodes = {
                    enable_node
                    for enable_node in scanning_enable_nodes
                    if has_edge(
                        enable_node,
                        scan_node,
                        destination_name=0,
                        ordinal=1,
                        source_name=0,
                    )
                    and any(
                        has_edge(
                            start_node,
                            enable_node,
                            destination_name=0,
                            ordinal=1,
                            source_name=0,
                        )
                        for start_node in start_nodes
                    )
                    and any(
                        has_edge(
                            enable_node,
                            seed_node,
                            destination_name=0,
                            ordinal=1,
                            source_name=0,
                        )
                        for seed_node in not_inspected_nodes
                    )
                }
                if not bootstrap_nodes:
                    continue
                scan_validity_nodes = {
                    target_node
                    for (
                        target_node,
                        destination_name,
                        ordinal,
                        source_name,
                    ) in outgoing_edges(scan_node)
                    if target_node in validity_nodes
                    and destination_name == 0
                    and ordinal == 1
                    and source_name == 0
                }
                for validity_node in scan_validity_nodes:
                    reenable_nodes = {
                        target_node
                        for (
                            target_node,
                            destination_name,
                            ordinal,
                            source_name,
                        ) in outgoing_edges(validity_node)
                        if target_node in scanning_enable_nodes
                        and destination_name == 0
                        and ordinal == 1
                        and source_name == 0
                    }
                    invalid_nodes = {
                        target_node
                        for (
                            target_node,
                            destination_name,
                            ordinal,
                            source_name,
                        ) in outgoing_edges(validity_node)
                        if target_node in invalidity_nodes
                        and destination_name == 0
                        and ordinal == 1
                        and source_name == 0
                    }
                    for reenable_node in reenable_nodes:
                        choice_nodes = {
                            target_node
                            for (
                                target_node,
                                destination_name,
                                ordinal,
                                source_name,
                            ) in outgoing_edges(reenable_node)
                            if target_node in focus_choice_nodes
                            and destination_name == 0
                            and ordinal == 0
                            and source_name == 0
                        }
                        for choice_node in choice_nodes:
                            success_cut_nodes = {
                                target_node
                                for (
                                    target_node,
                                    destination_name,
                                    ordinal,
                                    source_name,
                                ) in outgoing_edges(choice_node)
                                if target_node in cut_nodes
                                and destination_name == 0
                                and ordinal == 0
                                and source_name == 0
                            }
                            for invalid_node in invalid_nodes:
                                invalidation_loop = any(
                                    has_edge(
                                        invalid_node,
                                        disable_node,
                                        destination_name=0,
                                        ordinal=1,
                                        source_name=0,
                                    )
                                    and any(
                                        has_edge(
                                            disable_node,
                                            reset_cut_node,
                                            destination_name=0,
                                            ordinal=0,
                                            source_name=0,
                                        )
                                        and has_edge(
                                            reset_cut_node,
                                            validity_node,
                                            destination_name=0,
                                            ordinal=1,
                                            source_name=0,
                                        )
                                        and has_edge(
                                            reset_cut_node,
                                            choice_node,
                                            destination_name=1,
                                            ordinal=0,
                                            source_name=1,
                                        )
                                        for reset_cut_node in cut_nodes
                                    )
                                    for disable_node
                                    in scanning_disable_nodes
                                )
                                if not invalidation_loop:
                                    continue
                                for success_cut_node in success_cut_nodes:
                                    stops_invalidity = (
                                        has_edge(
                                            success_cut_node,
                                            invalid_node,
                                            destination_name=0,
                                            ordinal=0,
                                            source_name=1,
                                        )
                                        and has_edge(
                                            success_cut_node,
                                            invalid_node,
                                            destination_name=1026,
                                            ordinal=0,
                                            source_name=1,
                                        )
                                    )
                                    if not stops_invalidity:
                                        continue
                                    success_inspected_nodes = {
                                        inspected_node
                                        for inspected_node
                                        in inspected_nodes
                                        if has_edge(
                                            success_cut_node,
                                            inspected_node,
                                            destination_name=0,
                                            ordinal=1,
                                            source_name=0,
                                        )
                                    }
                                    completion_reactivates = any(
                                        has_edge(
                                            inspected_node,
                                            discovered_node,
                                            destination_name=0,
                                            ordinal=1,
                                            source_name=0,
                                        )
                                        and any(
                                            has_edge(
                                                discovered_node,
                                                fact_node,
                                                destination_name=0,
                                                ordinal=1,
                                                source_name=0,
                                            )
                                            and any(
                                                has_edge(
                                                    fact_node,
                                                    section_node,
                                                    destination_name=0,
                                                    ordinal=0,
                                                    source_name=0,
                                                )
                                                and any(
                                                    has_edge(
                                                        section_node,
                                                        hub_node,
                                                        destination_name=0,
                                                        ordinal=0,
                                                        source_name=0,
                                                    )
                                                    and has_edge(
                                                        hub_node,
                                                        choice_node,
                                                        destination_name=2,
                                                        ordinal=0,
                                                        source_name=0,
                                                    )
                                                    for hub_node
                                                    in reactivation_hubs
                                                )
                                                for section_node
                                                in reactivation_sections
                                            )
                                            for fact_node in fact_nodes
                                        )
                                        for discovered_node
                                        in discovered_nodes
                                        for inspected_node
                                        in success_inspected_nodes
                                    )
                                    if completion_reactivates:
                                        vanilla_focus_topology = True
                                        break
                                if vanilla_focus_topology:
                                    break
                            if vanilla_focus_topology:
                                break
                        if vanilla_focus_topology:
                            break
                    if vanilla_focus_topology:
                        break
                if vanilla_focus_topology:
                    break
            contract_reachable = reachable(scan_nodes)
            functional = bool(
                isinstance(target, str)
                and target in spawned_prop_dynamic_names
                and has_distinct_availability_fact
                and scan_nodes
                and validity_nodes
                and invalidity_nodes
                and focus_choice_nodes
                and cut_nodes
                and inspected_nodes
                and discovered_nodes
                and fact_nodes
                and vanilla_focus_topology
                and contract_reachable & inspected_nodes
                and contract_reachable & discovered_nodes
                and contract_reachable & fact_nodes
            )
            if functional:
                functional_clue_count += 1
            else:
                errors.append(
                    f"Clue {clue_name!r} has no complete scan, availability/"
                    "layer focus choice, invalidation/cut loop, inspected, "
                    "discovered, and fact contract"
                )

    return {
        "clue_layers": sorted(layer for layer in layers if isinstance(layer, str)),
        "clue_entities": clue_entities,
        "functional_clue_count": functional_clue_count,
        "clue_availability_facts": clue_availability_facts,
    }


def _clue_scan_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    target: str,
    destination: tuple[int, int],
) -> dict[str, Any]:
    scan_type = allocator.wrap(
        {
            "$type": "questScan_ConditionType",
            "eventType": "Finished",
            "objectRef": _dynamic_entity_reference(target),
        }
    )
    condition = allocator.wrap(
        {
            "$type": "questObjectCondition",
            "type": scan_type,
        }
    )
    return _scene_quest_node(
        allocator,
        node_id=node_id,
        quest_data={
            "$type": "questPauseConditionNodeDefinition",
            "condition": condition,
        },
        destination=destination,
    )


def _clue_inspected_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    target: str,
    destination: tuple[int, int] | None,
) -> dict[str, Any]:
    return _clue_focus_state_node(
        allocator,
        node_id=node_id,
        target=target,
        investigation_state="INSPECTED",
        destination=destination,
    )


def _clue_focus_state_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    target: str,
    investigation_state: str,
    destination: tuple[int, int] | None,
) -> dict[str, Any]:
    return _scene_quest_node(
        allocator,
        node_id=node_id,
        quest_data={
            "$type": "questEventManagerNodeDefinition",
            "componentName": _cname("scanning"),
            "event": allocator.wrap(
                {
                    "$type": "ToggleFocusClueEvent",
                    "clueIndex": 0,
                    "investigationState": investigation_state,
                    "isEnabled": 1,
                    "updatePS": 1,
                }
            ),
            "isObjectPlayer": 0,
            "isUiEvent": 0,
            "managerName": "FocusClueManager",
            "objectRef": _dynamic_entity_reference(target),
            "PSClassName": _cname("gameScanningComponentPS"),
        },
        destination=destination,
    )


def _clue_discovered_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    clue_name: str,
    destination: tuple[int, int],
) -> dict[str, Any]:
    return _scene_quest_node(
        allocator,
        node_id=node_id,
        quest_data={
            "$type": "questUIManagerNodeDefinition",
            "type": allocator.wrap(
                {
                    "$type": "questDiscoverBraindanceClue_NodeType",
                    "clueName": _cname(clue_name),
                }
            ),
        },
        destination=destination,
    )


def _clue_fact_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    fact_name: str,
    destination: tuple[int, int] | None = None,
) -> dict[str, Any]:
    return _scene_quest_node(
        allocator,
        node_id=node_id,
        quest_data={
            "$type": "questFactsDBManagerNodeDefinition",
            "type": allocator.wrap(
                {
                    "$type": "questSetVar_NodeType",
                    "factName": fact_name,
                    "setExactValue": 1,
                    "value": 1,
                }
            ),
        },
        destination=destination,
    )


def _clue_contract_node_ids(
    index: int,
) -> tuple[int, int, int, int, int, int, int, int, int]:
    base = 6000 + index * 10
    return (
        base + 1,
        base + 2,
        base + 3,
        base + 4,
        base + 5,
        base + 6,
        base + 7,
        base + 8,
        base + 9,
    )


def _clue_contract_aux_node_ids(
    index: int,
) -> tuple[int, int, int, int, int, int]:
    """IDs for the vanilla completion and scan-enable lifecycle."""

    base = 6500 + index * 10
    return (
        base + 1,
        base + 2,
        base + 3,
        base + 4,
        base + 5,
        base + 6,
    )


_BRAINDANCE_LAYER_UNLOCKS = {
    "Audio": (6091, "braindaneAudioLayerAvailable"),
    "Thermal": (6092, "braindaneThermalLayerAvailable"),
}


def _clue_availability_fact(clue: dict[str, Any]) -> str:
    completion_fact = str(clue["fact"])
    stem = (
        completion_fact[: -len("_found")]
        if completion_fact.endswith("_found")
        else completion_fact
    )
    return f"{stem}_clue_on"


def _clue_validity_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    availability_fact: str,
    layer: str,
    scene_depot_path: str,
    destinations: list[tuple[int, int]],
) -> dict[str, Any]:
    fact_condition = allocator.wrap(
        {
            "$type": "questFactsDBCondition",
            "type": allocator.wrap(
                {
                    "$type": "questVarComparison_ConditionType",
                    "comparisonType": "Greater",
                    "factName": availability_fact,
                    "value": 0,
                }
            ),
        }
    )
    layer_condition = allocator.wrap(
        {
            "$type": "questSceneCondition",
            "type": allocator.wrap(
                {
                    "$type": "scnBraindanceLayer_ConditionType",
                    "layer": layer,
                    "sceneFile": {
                        "DepotPath": {
                            "$type": "ResourcePath",
                            "$storage": "string",
                            "$value": scene_depot_path,
                        },
                        "Flags": "Soft",
                    },
                    "SceneVersion": "OlderOrEqual",
                }
            ),
        }
    )
    node = _scene_quest_node(
        allocator,
        node_id=node_id,
        quest_data={
            "$type": "questPauseConditionNodeDefinition",
            "condition": allocator.wrap(
                {
                    "$type": "questLogicalCondition",
                    "conditions": [
                        fact_condition,
                        layer_condition,
                    ],
                    "operation": "AND",
                }
            ),
        },
        destination=None,
    )
    node["Data"]["outputSockets"] = [
        _scene_output_socket(destinations)
    ]
    return node


def _deterministic_scene_event_id(*parts: object) -> str:
    digest = hashlib.sha256(
        ":".join(str(part) for part in parts).encode("utf-8")
    ).digest()
    value = int.from_bytes(digest[:8], "little")
    return str(value or 1)


def _configure_focus_clue_options(
    root: dict[str, Any],
    clue_ids: list[str],
) -> dict[str, int]:
    screenplay_store = root.get("screenplayStore")
    loc_store = root.get("locStore")
    if not isinstance(screenplay_store, dict) or not isinstance(
        screenplay_store.get("options"), list
    ):
        raise BraindancePipelineError(
            "Scene has no screenplay option store for focus clues"
        )
    if (
        not isinstance(loc_store, dict)
        or not isinstance(loc_store.get("vdEntries"), list)
        or not isinstance(loc_store.get("vpEntries"), list)
    ):
        raise BraindancePipelineError(
            "Scene has no embedded localization store for focus clues"
        )

    item_ids = {
        clue_id: 2 + index * 256
        for index, clue_id in enumerate(clue_ids)
    }
    loc_ids = {
        clue_id: _deterministic_scene_event_id(
            "ghostline",
            "focus-clue-option",
            clue_id,
        )
        for clue_id in clue_ids
    }
    owned_item_ids = set(item_ids.values())
    options = screenplay_store["options"]
    options[:] = [
        option
        for option in options
        if option.get("itemId", {}).get("id") not in owned_item_ids
    ]
    for clue_id in clue_ids:
        options.append(
            {
                "$type": "scnscreenplayChoiceOption",
                "itemId": {
                    "$type": "scnscreenplayItemId",
                    "id": item_ids[clue_id],
                },
                "locstringId": {
                    "$type": "scnlocLocstringId",
                    "ruid": loc_ids[clue_id],
                },
                "usage": {
                    "$type": "scnscreenplayOptionUsage",
                    "playerGenderMask": {
                        "$type": "scnGenderMask",
                        "mask": 3,
                    },
                },
            }
        )

    owned_loc_ids = set(loc_ids.values())
    descriptors = loc_store["vdEntries"]
    removed_variant_ids = {
        descriptor.get("variantId", {}).get("ruid")
        for descriptor in descriptors
        if descriptor.get("locstringId", {}).get("ruid")
        in owned_loc_ids
    }
    descriptors[:] = [
        descriptor
        for descriptor in descriptors
        if descriptor.get("locstringId", {}).get("ruid")
        not in owned_loc_ids
    ]
    payloads = loc_store["vpEntries"]
    payloads[:] = [
        payload
        for payload in payloads
        if payload.get("variantId", {}).get("ruid")
        not in removed_variant_ids
    ]

    localized_clue_ids = sorted(
        clue_ids,
        key=lambda clue_id: int(loc_ids[clue_id]),
    )
    for locale in ("db_db", "pl_pl", "en_us"):
        for clue_id in localized_clue_ids:
            variants = (
                (("", "blank"), ("Inspect clue", "source"))
                if locale == "db_db"
                else (("Inspect clue", "text"),)
            )
            for content, variant_kind in variants:
                variant_id = _deterministic_scene_event_id(
                    "ghostline",
                    "focus-clue-option",
                    clue_id,
                    locale,
                    variant_kind,
                )
                payload_index = len(payloads)
                payloads.append(
                    {
                        "$type":
                            "scnlocLocStoreEmbeddedVariantPayloadEntry",
                        "content": content,
                        "variantId": {
                            "$type": "scnlocVariantId",
                            "ruid": variant_id,
                        },
                    }
                )
                descriptors.append(
                    {
                        "$type":
                            "scnlocLocStoreEmbeddedVariantDescriptorEntry",
                        "localeId": locale,
                        "locstringId": {
                            "$type": "scnlocLocstringId",
                            "ruid": loc_ids[clue_id],
                        },
                        "signature": {
                            "$type": "scnlocSignature",
                            "val": "3",
                        },
                        "variantId": {
                            "$type": "scnlocVariantId",
                            "ruid": variant_id,
                        },
                        "vpeIndex": payload_index,
                    }
                )
    return item_ids


def _focus_clue_choice_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    clue_id: str,
    prop_id: int,
    screenplay_item_id: int,
    success_cut_id: int,
    visualizer_style: str = "inWorld",
    location_type: str = "Interaction",
    activation_range: float = 3,
    indication_range: float = 20,
    choice_group: str = "ghostline_bd_clues",
) -> dict[str, Any]:
    output_sockets = [_scene_output_socket([(success_cut_id, 0)])]
    output_sockets.extend(
        _scene_output_socket([], name=name)
        for name in range(1, 7)
    )
    return allocator.wrap(
        {
            "$type": "scnChoiceNode",
            "alwaysUseBrainGender": 0,
            "ataParams": {
                "$type": "scnChoiceNodeNsAttachToActorParams",
                "actorId": {
                    "$type": "scnActorId",
                    "id": 0xFFFFFFFF,
                },
                "visualizerStyle": "onScreen",
            },
            "atgoParams": {
                "$type": "scnChoiceNodeNsAttachToGameObjectParams",
                "nodeRef": {
                    "$type": "NodeRef",
                    "$storage": "uint64",
                    "$value": "0",
                },
                "visualizerStyle": "inWorld",
            },
            "atpParams": {
                "$type": "scnChoiceNodeNsAttachToPropParams",
                "propId": {
                    "$type": "scnPropId",
                    "id": prop_id,
                },
                "visualizerStyle": visualizer_style,
            },
            "atsParams": {
                "$type": "scnChoiceNodeNsAttachToScreenParams",
            },
            "atwParams": {
                "$type": "scnChoiceNodeNsAttachToWorldParams",
                "customEntityRadius": 0,
                "entityOrientation": {
                    "$type": "Quaternion",
                    "i": 0,
                    "j": 0,
                    "k": 0,
                    "r": 1,
                },
                "entityPosition": {
                    "$type": "Vector3",
                    "X": 0,
                    "Y": 0,
                    "Z": 0,
                },
                "visualizerStyle": "onScreen",
            },
            "choiceFlags": "IsFocusClue",
            "choiceGroup": _cname(choice_group),
            "choicePriority": 0,
            "cpoHoldInputActionSection": 0,
            "customPersistentLine": {
                "$type": "scnscreenplayItemId",
                "id": 4294967040,
            },
            "displayNameOverride": "",
            "doNotTurnOffPreventionSystem": 0,
            "ffStrategy": "automatic",
            "forceAttachToScreenCondition": None,
            "hubPriority": 0,
            "interruptCapability": "Interruptable",
            "interruptionSpeakerOverride": {
                "$type": "scnActorId",
                "id": 0xFFFFFFFF,
            },
            "localizedDisplayNameOverride": {
                "unk1": "0",
                "value": "",
            },
            "lookAtParams": allocator.wrap(
                {
                    "$type": "scnChoiceNodeNsBasicLookAtParams",
                    "offset": {
                        "$type": "Vector3",
                        "X": 0,
                        "Y": 0,
                        "Z": 0,
                    },
                    "slotName": _cname("(Root)"),
                }
            ),
            "mappinParams": allocator.wrap(
                {
                    "$type": "scnChoiceNodeNsMappinParams",
                    "locationType": location_type,
                    "mappinSettings": {
                        "$type": "TweakDBID",
                        "$storage": "string",
                        "$value":
                            "MappinUISettings.SceneDialogObjectSettings",
                    },
                }
            ),
            "mode": "attachToProp",
            "nodeId": {"$type": "scnNodeId", "id": node_id},
            "options": [
                {
                    "$type": "scnChoiceNodeOption",
                    "blueline": 0,
                    "bluelineCondition": None,
                    "caption": _cname(f"int_{clue_id}"),
                    "emphasisCondition": None,
                    "exDataFlags": 1,
                    "gameplayAction": {
                        "$type": "TweakDBID",
                        "$storage": "uint64",
                        "$value": "0",
                    },
                    "iconCondition": None,
                    "iconTagIds": [
                        {
                            "$type": "TweakDBID",
                            "$storage": "string",
                            "$value": "ChoiceCaptionParts.Inspect",
                        }
                    ],
                    "isFixedAsRead": 0,
                    "isSingleChoice": 1,
                    "mappinReferencePointId": {
                        "$type": "scnReferencePointId",
                        "id": 0xFFFFFFFF,
                    },
                    "questCondition": None,
                    "screenplayOptionId": {
                        "$type": "scnscreenplayItemId",
                        "id": screenplay_item_id,
                    },
                    "timedCondition": None,
                    "timedParams": None,
                    "triggerCondition": None,
                    "type": {
                        "$type":
                            "gameinteractionsChoiceTypeWrapper",
                        "properties": 0,
                    },
                }
            ],
            "outputSockets": output_sockets,
            "persistentLineEvents": [],
            "reminderCondition": None,
            "reminderParams": None,
            "shapeParams": allocator.wrap(
                {
                    "$type": "scnInteractionShapeParams",
                    "activationBaseLength": 1,
                    "activationHeight": 3,
                    "activationYawLimit": 360,
                    "customActivationRange": activation_range,
                    "customIndicationRange": indication_range,
                    "offset": {
                        "$type": "Vector3",
                        "X": 0,
                        "Y": 0,
                        "Z": 0,
                    },
                    "preset": "normal",
                    "rotation": {
                        "$type": "Quaternion",
                        "i": 0,
                        "j": 0,
                        "k": 0,
                        "r": 1,
                    },
                }
            ),
            "timedParams": None,
            "timedSectionCondition": None,
        }
    )


def _clue_reactivate_hub_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    choice_id: int,
) -> dict[str, Any]:
    output = _scene_output_socket([])
    output["destinations"] = [
        _scene_input_socket(choice_id, 0, name=2)
    ]
    return allocator.wrap(
        {
            "$type": "scnHubNode",
            "ffStrategy": "automatic",
            "nodeId": {"$type": "scnNodeId", "id": node_id},
            "outputSockets": [output],
        }
    )


def _clue_scanning_enabled_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    target: str,
    enable: bool,
    destination: tuple[int, int] | None,
) -> dict[str, Any]:
    return _scene_quest_node(
        allocator,
        node_id=node_id,
        quest_data={
            "$type": "questVisionModesManagerNodeDefinition",
            "type": allocator.wrap(
                {
                    "$type": "questEnableScanning_NodeType",
                    "enable": int(enable),
                    "objectRef": _dynamic_entity_reference(target),
                }
            ),
        },
        destination=destination,
    )


def _clue_scanning_bootstrap_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    target: str,
    scan_id: int,
    seed_id: int,
) -> dict[str, Any]:
    node = _clue_scanning_enabled_node(
        allocator,
        node_id=node_id,
        target=target,
        enable=True,
        destination=None,
    )
    node["Data"]["outputSockets"][0]["destinations"] = [
        _scene_input_socket(scan_id, 1),
        _scene_input_socket(seed_id, 1),
    ]
    return node


def _clue_success_cut_control_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    invalidity_id: int,
    inspected_id: int,
) -> dict[str, Any]:
    stop_invalidity = _scene_output_socket([], name=1)
    stop_invalidity["destinations"] = [
        _scene_input_socket(invalidity_id, 0),
        _scene_input_socket(invalidity_id, 0, name=1026),
    ]
    return allocator.wrap(
        {
            "$type": "scnCutControlNode",
            "ffStrategy": "automatic",
            "nodeId": {"$type": "scnNodeId", "id": node_id},
            "outputSockets": [
                _scene_output_socket([(inspected_id, 1)]),
                stop_invalidity,
            ],
        }
    )


def _clue_reactivation_section_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    hub_id: int,
) -> dict[str, Any]:
    output = _scene_output_socket([])
    output["destinations"] = [_scene_input_socket(hub_id, 0)]
    return allocator.wrap(
        {
            "$type": "scnSectionNode",
            "actorBehaviors": [],
            "events": [],
            "ffStrategy": "automatic",
            "isFocusClue": 1,
            "nodeId": {"$type": "scnNodeId", "id": node_id},
            "outputSockets": [
                output,
                _scene_output_socket([], name=1),
            ],
            "sectionDuration": {
                "$type": "scnSceneTime",
                "stu": 100,
            },
        }
    )


def _clue_invalidity_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    availability_fact: str,
    layer: str,
    scene_depot_path: str,
    destination: tuple[int, int],
) -> dict[str, Any]:
    conditions = [
        allocator.wrap(
            {
                "$type": "questFactsDBCondition",
                "type": allocator.wrap(
                    {
                        "$type": "questVarComparison_ConditionType",
                        "comparisonType": "LessOrEqual",
                        "factName": availability_fact,
                        "value": 0,
                    }
                ),
            }
        )
    ]
    for other_layer in (
        candidate
        for candidate in ("Visual", "Audio", "Thermal")
        if candidate != layer
    ):
        conditions.append(
            allocator.wrap(
                {
                    "$type": "questSceneCondition",
                    "type": allocator.wrap(
                        {
                            "$type":
                                "scnBraindanceLayer_ConditionType",
                            "layer": other_layer,
                            "sceneFile": {
                                "DepotPath": {
                                    "$type": "ResourcePath",
                                    "$storage": "string",
                                    "$value": scene_depot_path,
                                },
                                "Flags": "Soft",
                            },
                            "SceneVersion": "OlderOrEqual",
                        }
                    ),
                }
            )
        )
    return _scene_quest_node(
        allocator,
        node_id=node_id,
        quest_data={
            "$type": "questPauseConditionNodeDefinition",
            "condition": allocator.wrap(
                {
                    "$type": "questLogicalCondition",
                    "conditions": conditions,
                    "operation": "OR",
                }
            ),
        },
        destination=destination,
    )


def _clue_cut_control_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    validity_id: int,
    choice_id: int,
) -> dict[str, Any]:
    cut_choice = _scene_output_socket([], name=1)
    cut_choice["destinations"] = [
        _scene_input_socket(choice_id, 0, name=1)
    ]
    return allocator.wrap(
        {
            "$type": "scnCutControlNode",
            "ffStrategy": "automatic",
            "nodeId": {"$type": "scnNodeId", "id": node_id},
            "outputSockets": [
                _scene_output_socket([(validity_id, 1)]),
                cut_choice,
            ],
        }
    )


def _clue_attach_event(
    *,
    clue_id: str,
    prop_id: int,
    performer_id: int,
    slot: str,
    start_time: int,
    offset_mode: str,
    offset_position: list[float],
    offset_rotation: list[float],
) -> dict[str, Any]:
    return {
        "$type": "scneventsAttachPropToPerformer",
        "customOffsetPos": {
            "$type": "Vector3",
            "X": float(offset_position[0]),
            "Y": float(offset_position[1]),
            "Z": float(offset_position[2]),
        },
        "customOffsetRot": {
            "$type": "Quaternion",
            "i": float(offset_rotation[0]),
            "j": float(offset_rotation[1]),
            "k": float(offset_rotation[2]),
            "r": float(offset_rotation[3]),
        },
        "duration": 0,
        "executionTagFlags": 0,
        "fallbackData": [],
        "id": {
            "$type": "scnSceneEventId",
            "id": _deterministic_scene_event_id(
                "ghostline", "clue-attach", clue_id
            ),
        },
        "offsetMode": offset_mode,
        "performerId": {
            "$type": "scnPerformerId",
            "id": performer_id,
        },
        "propId": {"$type": "scnPropId", "id": prop_id},
        "scalingData": None,
        "slot": _cname(slot),
        "startTime": start_time,
        "type": "0",
    }


def _clue_audio_duration_event(
    *,
    clue_id: str,
    event_name: str,
    performer_id: int,
    start_time: int,
    duration: int,
    direction: str,
) -> dict[str, Any]:
    return {
        "$type": "scnAudioDurationEvent",
        "audioEventName": _cname(event_name),
        "duration": duration,
        "executionTagFlags": 0,
        "id": {
            "$type": "scnSceneEventId",
            "id": _deterministic_scene_event_id(
                "ghostline", "clue-audio", clue_id, direction
            ),
        },
        "performer": {
            "$type": "scnPerformerId",
            "id": performer_id,
        },
        "playbackDirectionSupport": direction,
        "scalingData": None,
        "startTime": start_time,
        "type": "0",
    }


def _configure_clue_contract(
    root: dict[str, Any],
    *,
    clues: list[dict[str, Any]],
    clue_events: list[dict[str, Any]],
    clue_targets: dict[str, dict[str, Any]] | None,
    scene_depot_path: str,
) -> None:
    if not clues:
        return
    graph_data = root.get("sceneGraph", {}).get("Data")
    graph = graph_data.get("graph") if isinstance(graph_data, dict) else None
    if not isinstance(graph, list):
        raise BraindancePipelineError("Scene has no graph for clue wiring")
    starts = [
        wrapper["Data"]
        for wrapper in graph
        if isinstance(wrapper, dict)
        and isinstance(wrapper.get("Data"), dict)
        and wrapper["Data"].get("$type") == "scnStartNode"
    ]
    if len(starts) != 1:
        raise BraindancePipelineError(
            f"Scene clue wiring requires one Start node; found {len(starts)}"
        )
    start = starts[0]
    output_sockets = start.get("outputSockets")
    if not isinstance(output_sockets, list) or not output_sockets:
        raise BraindancePipelineError("Scene Start node has no output socket")

    configured: list[
        tuple[dict[str, Any], dict[str, Any], str, str, str]
    ] = []
    attachments: list[
        tuple[str, dict[str, Any], dict[str, Any], dict[str, Any]]
    ] = []
    props = root.get("props")
    if not isinstance(props, list) or not props:
        raise BraindancePipelineError("Scene has no prop prototype for clues")
    prop_by_dynamic_name = {
        prop.get("spawnDespawnParams", {})
        .get("dynamicEntityUniqueName", {})
        .get("$value"): prop
        for prop in props
        if isinstance(prop, dict)
    }
    prototype = copy.deepcopy(props[-1])
    for clue, event in zip(clues, clue_events, strict=False):
        clue_id = str(clue["id"])
        target = (
            clue_targets.get(clue_id)
            if isinstance(clue_targets, dict)
            else None
        )
        dynamic_name = (
            target.get("dynamic_name")
            if isinstance(target, dict)
            else clue.get("target_dynamic_name")
        )
        record = (
            target.get("record")
            if isinstance(target, dict)
            else clue.get("target_record")
        )
        prop_name = (
            target.get("prop_name")
            if isinstance(target, dict)
            else clue.get("target_prop_name")
        )
        if not isinstance(dynamic_name, str) or not dynamic_name:
            existing = event.get("clueEntity", {})
            dynamic_name = (
                existing.get("dynamicEntityUniqueName", {}).get("$value")
                if isinstance(existing, dict)
                else None
            )
        prop = prop_by_dynamic_name.get(dynamic_name)
        if prop is None:
            if (
                not isinstance(dynamic_name, str)
                or not dynamic_name
                or not isinstance(record, str)
                or not record
            ):
                raise BraindancePipelineError(
                    f"Clue {clue_id!r} needs a spawned target record and "
                    "dynamic name"
                )
            prop = copy.deepcopy(prototype)
            prop_id = len(props)
            prop["propId"] = {"$type": "scnPropId", "id": prop_id}
            prop["propName"] = (
                prop_name
                if isinstance(prop_name, str) and prop_name
                else f"ghostline_bd_clue_{clue_id}"
            )
            prop["entityAcquisitionPlan"] = "spawnDespawn"
            spawn = prop["spawnDespawnParams"]
            spawn["appearance"] = _cname("default")
            spawn["dynamicEntityUniqueName"] = _cname(dynamic_name)
            spawn["isEnabled"] = 1
            spawn["spawnOnStart"] = 1
            spawn["validateSpawnPostion"] = 0
            spawn["specRecordId"] = {
                "$type": "TweakDBID",
                "$storage": "string",
                "$value": record,
            }
            prop["specPropRecordId"] = {
                "$type": "TweakDBID",
                "$storage": "string",
                "$value": record,
            }
            props.append(prop)
            prop_by_dynamic_name[dynamic_name] = prop
        elif isinstance(record, str) and record:
            prop["spawnDespawnParams"]["specRecordId"] = {
                "$type": "TweakDBID",
                "$storage": "string",
                "$value": record,
            }
            prop["specPropRecordId"] = {
                "$type": "TweakDBID",
                "$storage": "string",
                "$value": record,
            }
        position = clue.get("position")
        if isinstance(position, list) and len(position) == 3:
            prop["spawnDespawnParams"]["spawnOffset"]["position"] = {
                "$type": "Vector4",
                "W": 0,
                "X": float(position[0]),
                "Y": float(position[1]),
                "Z": float(position[2]),
            }
        availability_fact = (
            target.get("availability_fact")
            if isinstance(target, dict)
            else None
        )
        if not isinstance(availability_fact, str) or not availability_fact:
            availability_fact = _clue_availability_fact(clue)
        event["factName"] = _cname(availability_fact)
        event["overrideFact"] = 1
        event["clueEntity"] = _dynamic_entity_reference(dynamic_name)
        configured.append(
            (clue, event, dynamic_name, clue_id, availability_fact)
        )
        attach = target.get("attach") if isinstance(target, dict) else None
        if isinstance(attach, dict):
            attachments.append((clue_id, clue, event, prop))

    contract_ids = {
        node_id
        for index in range(len(configured))
        for node_id in (
            *_clue_contract_node_ids(index),
            *_clue_contract_aux_node_ids(index),
        )
    }
    layer_unlocks = [
        _BRAINDANCE_LAYER_UNLOCKS[layer]
        for layer in dict.fromkeys(
            str(clue["layer"]) for clue, *_rest in configured
        )
        if layer in _BRAINDANCE_LAYER_UNLOCKS
    ]
    contract_ids.update(node_id for node_id, _fact_name in layer_unlocks)
    retained: list[dict[str, Any]] = []
    for wrapper in graph:
        data = wrapper.get("Data") if isinstance(wrapper, dict) else None
        node_id = (
            data.get("nodeId", {}).get("id")
            if isinstance(data, dict)
            else None
        )
        if node_id not in contract_ids:
            retained.append(wrapper)
            continue
        generated_types = {
            "questScan_ConditionType",
            "ToggleFocusClueEvent",
            "questDiscoverBraindanceClue_NodeType",
            "questSetVar_NodeType",
            "questEnableScanning_NodeType",
            "questLogicalCondition",
            "scnBraindanceLayer_ConditionType",
            "scnChoiceNode",
            "scnCutControlNode",
            "scnHubNode",
            "scnSectionNode",
        }
        if not any(
            item.get("$type") in generated_types for item in _walk(data)
        ):
            raise BraindancePipelineError(
                f"Clue contract node ID {node_id} collides with scene content"
            )
    graph[:] = retained
    notable_points = root.get("notablePoints")
    if notable_points is None:
        root["notablePoints"] = []
    elif not isinstance(notable_points, list):
        raise BraindancePipelineError("Scene notablePoints must be an array")
    else:
        notable_points[:] = [
            point
            for point in notable_points
            if point.get("nodeId", {}).get("id") not in contract_ids
        ]
    destinations = output_sockets[0].get("destinations")
    if not isinstance(destinations, list):
        raise BraindancePipelineError(
            "Scene Start output has no destinations array"
        )
    destinations[:] = [
        destination
        for destination in destinations
        if destination.get("nodeId", {}).get("id") not in contract_ids
    ]

    allocator = _SceneHandleAllocator(root)
    focus_option_ids = _configure_focus_clue_options(
        root,
        [clue_id for _, _, _, clue_id, _ in configured],
    )
    # Vanilla Q004 explicitly unlocks the nonvisual controls before their
    # clues can become scannable.  These typo-preserved engine facts are
    # persistent tutorial unlocks and deliberately are not reset on exit.
    for node_id, fact_name in layer_unlocks:
        destinations.append(_scene_input_socket(node_id, 1))
        graph.append(
            _clue_fact_node(
                allocator,
                node_id=node_id,
                fact_name=fact_name,
            )
        )
    for index, (
        clue,
        _event,
        dynamic_name,
        clue_id,
        availability_fact,
    ) in enumerate(configured):
        (
            scan_id,
            validity_id,
            choice_id,
            invalidity_id,
            cut_id,
            inspected_id,
            discovered_id,
            fact_id,
            reactivate_id,
        ) = _clue_contract_node_ids(index)
        (
            success_cut_id,
            reactivation_section_id,
            enable_scanning_id,
            disable_scanning_id,
            bootstrap_scanning_id,
            seed_focus_id,
        ) = _clue_contract_aux_node_ids(index)
        prop = prop_by_dynamic_name[dynamic_name]
        prop_id = int(prop["propId"]["id"])
        target = (
            clue_targets.get(clue_id)
            if isinstance(clue_targets, dict)
            else None
        )
        focus = target.get("focus") if isinstance(target, dict) else None
        if not isinstance(focus, dict):
            focus = {}
        destinations.append(
            _scene_input_socket(bootstrap_scanning_id, 1)
        )
        graph.extend(
            [
                _clue_scanning_bootstrap_node(
                    allocator,
                    node_id=bootstrap_scanning_id,
                    target=dynamic_name,
                    scan_id=scan_id,
                    seed_id=seed_focus_id,
                ),
                _clue_focus_state_node(
                    allocator,
                    node_id=seed_focus_id,
                    target=dynamic_name,
                    investigation_state="NOT_INSPECTED",
                    destination=None,
                ),
                _clue_scan_node(
                    allocator,
                    node_id=scan_id,
                    target=dynamic_name,
                    destination=(validity_id, 1),
                ),
                _clue_validity_node(
                    allocator,
                    node_id=validity_id,
                    availability_fact=availability_fact,
                    layer=str(clue["layer"]),
                    scene_depot_path=scene_depot_path,
                    destinations=[
                        (enable_scanning_id, 1),
                        (invalidity_id, 1),
                    ],
                ),
                _clue_scanning_enabled_node(
                    allocator,
                    node_id=enable_scanning_id,
                    target=dynamic_name,
                    enable=True,
                    destination=(choice_id, 0),
                ),
                _focus_clue_choice_node(
                    allocator,
                    node_id=choice_id,
                    clue_id=clue_id,
                    prop_id=prop_id,
                    screenplay_item_id=focus_option_ids[clue_id],
                    success_cut_id=success_cut_id,
                    visualizer_style=str(
                        focus.get("visualizer_style", "inWorld")
                    ),
                    location_type=str(
                        focus.get("location_type", "Interaction")
                    ),
                    activation_range=float(
                        focus.get("activation_range", 3)
                    ),
                    indication_range=float(
                        focus.get("indication_range", 20)
                    ),
                    choice_group=str(
                        focus.get("choice_group", "ghostline_bd_clues")
                    ),
                ),
                _clue_invalidity_node(
                    allocator,
                    node_id=invalidity_id,
                    availability_fact=availability_fact,
                    layer=str(clue["layer"]),
                    scene_depot_path=scene_depot_path,
                    destination=(disable_scanning_id, 1),
                ),
                _clue_scanning_enabled_node(
                    allocator,
                    node_id=disable_scanning_id,
                    target=dynamic_name,
                    enable=False,
                    destination=(cut_id, 0),
                ),
                _clue_cut_control_node(
                    allocator,
                    node_id=cut_id,
                    validity_id=validity_id,
                    choice_id=choice_id,
                ),
                _clue_success_cut_control_node(
                    allocator,
                    node_id=success_cut_id,
                    invalidity_id=invalidity_id,
                    inspected_id=inspected_id,
                ),
                _clue_inspected_node(
                    allocator,
                    node_id=inspected_id,
                    target=dynamic_name,
                    destination=(discovered_id, 1),
                ),
                _clue_discovered_node(
                    allocator,
                    node_id=discovered_id,
                    clue_name=clue_id,
                    destination=(fact_id, 1),
                ),
                _clue_fact_node(
                    allocator,
                    node_id=fact_id,
                    fact_name=str(clue["fact"]),
                    destination=(reactivation_section_id, 0),
                ),
                _clue_reactivation_section_node(
                    allocator,
                    node_id=reactivation_section_id,
                    hub_id=reactivate_id,
                ),
                _clue_reactivate_hub_node(
                    allocator,
                    node_id=reactivate_id,
                    choice_id=choice_id,
                ),
            ]
        )
        notable_points = root.setdefault("notablePoints", [])
        if not isinstance(notable_points, list):
            raise BraindancePipelineError(
                "Scene notablePoints must be an array"
            )
        notable_points.append(
            {
                "$type": "scnNotablePoint",
                "name": _cname(f"ghostline_bd_clue_{clue_id}"),
                "nodeId": {"$type": "scnNodeId", "id": choice_id},
            }
        )

    rewindable = [
        wrapper["Data"]
        for wrapper in graph
        if isinstance(wrapper, dict)
        and isinstance(wrapper.get("Data"), dict)
        and wrapper["Data"].get("$type") == "scnRewindableSectionNode"
    ]
    if configured and len(rewindable) != 1:
        raise BraindancePipelineError(
            "Functional clues require exactly one rewindable section"
        )
    if configured:
        rewindable_node = rewindable[0]
        events = rewindable_node.get("events")
        if not isinstance(events, list):
            raise BraindancePipelineError(
                "Rewindable section has no event array for functional clues"
            )
        clue_prop_ids = {
            int(prop_by_dynamic_name[dynamic_name]["propId"]["id"])
            for _, _, dynamic_name, _, _ in configured
        }
        authored_audio_event_ids = {
            _deterministic_scene_event_id(
                "ghostline", "clue-audio", clue_id, direction
            )
            for _, _, _, clue_id, _ in configured
            for direction in ("Forward", "Backward")
        }
        events[:] = [
            wrapper
            for wrapper in events
            if not (
                isinstance(wrapper, dict)
                and isinstance(wrapper.get("Data"), dict)
                and (
                    (
                        wrapper["Data"].get("$type")
                        == "scneventsAttachPropToPerformer"
                        and wrapper["Data"].get("propId", {}).get("id")
                        in clue_prop_ids
                    )
                    or (
                        wrapper["Data"].get("$type")
                        == "scnAudioDurationEvent"
                        and wrapper["Data"].get("id", {}).get("id")
                        in authored_audio_event_ids
                    )
                )
            )
        ]
        debug_symbols = root.get("debugSymbols")
        debug_event_symbols = (
            debug_symbols.get("sceneEventsDebugSymbols")
            if isinstance(debug_symbols, dict)
            else None
        )
        existing_event_ids = {
            event_id.get("id")
            for symbol in debug_event_symbols or []
            if isinstance(symbol, dict)
            for event_id in symbol.get("sceneEventIds", [])
            if isinstance(event_id, dict)
        }
        origin_node_id = int(rewindable_node["nodeId"]["id"])
        for clue_id, _clue, event, prop in attachments:
            target = clue_targets.get(clue_id) if clue_targets else None
            attach = target.get("attach") if isinstance(target, dict) else None
            if not isinstance(attach, dict):
                continue
            at = str(attach.get("at", "scene_start"))
            start_time = (
                int(event.get("startTime", 0))
                if at == "clue_start"
                else int(attach.get("start_ms", 0))
            )
            offset_position = attach.get("position", [0.0, 0.0, 0.0])
            offset_rotation = attach.get(
                "rotation",
                [0.0, 0.0, 0.0, 1.0],
            )
            if (
                not isinstance(offset_position, list)
                or len(offset_position) != 3
                or not all(
                    isinstance(value, (int, float))
                    for value in offset_position
                )
            ):
                raise BraindancePipelineError(
                    f"Clue {clue_id!r} attach.position must be XYZ"
                )
            if (
                not isinstance(offset_rotation, list)
                or len(offset_rotation) != 4
                or not all(
                    isinstance(value, (int, float))
                    for value in offset_rotation
                )
            ):
                raise BraindancePipelineError(
                    f"Clue {clue_id!r} attach.rotation must be XYZW"
                )
            attach_event = _clue_attach_event(
                clue_id=clue_id,
                prop_id=int(prop["propId"]["id"]),
                performer_id=int(attach["performer_id"]),
                slot=str(attach["slot"]),
                start_time=start_time,
                offset_mode=str(
                    attach.get("offset_mode", "useCustomOffset")
                ),
                offset_position=offset_position,
                offset_rotation=offset_rotation,
            )
            attach_wrapper = allocator.wrap(attach_event)
            clue_event_id = event.get("id", {}).get("id")
            clue_event_index = next(
                (
                    event_index
                    for event_index, wrapper in enumerate(events)
                    if wrapper.get("Data", {}).get("id", {}).get("id")
                    == clue_event_id
                ),
                len(events),
            )
            events.insert(clue_event_index, attach_wrapper)
            event_id = attach_event["id"]["id"]
            if (
                isinstance(debug_event_symbols, list)
                and event_id not in existing_event_ids
            ):
                editor_event_id = (
                    0x10000000
                    | (
                        _fnv1a32(f"clue-attach:{clue_id}")
                        & 0x0FFFFFFF
                    )
                )
                debug_event_symbols.append(
                    {
                        "$type": "scnSceneEventSymbol",
                        "editorEventId": str(editor_event_id),
                        "originNodeId": {
                            "$type": "scnNodeId",
                            "id": origin_node_id,
                        },
                        "sceneEventIds": [
                            {
                                "$type": "scnSceneEventId",
                                "id": event_id,
                            }
                        ],
                    }
                )
                existing_event_ids.add(event_id)
        for clue, event, _dynamic_name, clue_id, _availability in configured:
            target = clue_targets.get(clue_id) if clue_targets else None
            audio = target.get("audio") if isinstance(target, dict) else None
            if not isinstance(audio, dict):
                continue
            performer_id = int(audio["performer_id"])
            start_time = int(event.get("startTime", 0))
            duration = int(event.get("duration", 0))
            names = [
                ("Forward", str(audio["event"])),
                ("Backward", str(audio["reverse_event"])),
            ]
            clue_event_id = event.get("id", {}).get("id")
            clue_event_index = next(
                (
                    event_index
                    for event_index, wrapper in enumerate(events)
                    if wrapper.get("Data", {}).get("id", {}).get("id")
                    == clue_event_id
                ),
                len(events),
            )
            for direction, event_name in names:
                audio_event = _clue_audio_duration_event(
                    clue_id=clue_id,
                    event_name=event_name,
                    performer_id=performer_id,
                    start_time=start_time,
                    duration=duration,
                    direction=direction,
                )
                events.insert(
                    clue_event_index,
                    allocator.wrap(audio_event),
                )
                clue_event_index += 1
