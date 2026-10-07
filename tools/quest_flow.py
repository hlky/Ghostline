"""Named phase ports and a small, static linker for quest composition.

Contracts describe dependencies; they do not set game facts or invent scene exits.
Legacy manifests keep their implicit linear success route.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Any, Mapping

from quest_types import Diagnostic, ID_RE, QuestSpec, QuestSpecError


def stage_inputs(stage: Any) -> dict[str, str]:
    return dict(stage.data.get("inputs", {"start": "In1"}))


def stage_outcomes(stage: Any) -> dict[str, str]:
    return dict(stage.data.get("outcomes", {"success": "Out1"}))


def stage_transitions(spec: QuestSpec) -> dict[str, dict[str, str]]:
    result = {}
    for index, stage in enumerate(spec.stages):
        following = (
            spec.stages[index + 1].id if index + 1 < len(spec.stages) else "$end"
        )
        result[stage.id] = dict(stage.data.get("on", {"success": following}))
    return result


@dataclass(frozen=True)
class StageContract:
    reads_facts: tuple[str, ...] = ()
    writes_facts: tuple[str, ...] = ()
    external_events: tuple[str, ...] = ()
    scene_exits: tuple[tuple[str, tuple[str, ...]], ...] = ()

    @classmethod
    def from_data(cls, data: Mapping[str, Any]) -> StageContract:
        contract = data.get("contract", {})
        return cls(
            tuple(contract.get("reads_facts", ())),
            tuple(contract.get("writes_facts", ())),
            tuple(contract.get("external_events", ())),
            tuple(
                (scene, tuple(exits))
                for scene, exits in contract.get("scene_exits", {}).items()
            ),
        )

    def as_dict(self) -> dict[str, Any]:
        return {
            "reads_facts": list(self.reads_facts),
            "writes_facts": list(self.writes_facts),
            "external_events": list(self.external_events),
            "scene_exits": {scene: list(exits) for scene, exits in self.scene_exits},
        }


def contract_dict(stage: Any) -> dict[str, Any]:
    return StageContract.from_data(stage.data).as_dict()


def validate_flow_fields(raw: dict[str, Any], diagnostics: list[Diagnostic]) -> None:
    """Validate shape before the linker consumes author-controlled dictionaries."""

    def error(code: str, message: str, stage: str | None = None) -> None:
        diagnostics.append(Diagnostic("error", code, message, stage))

    def names(value: Any, *, facts: bool = False) -> bool:
        return (
            isinstance(value, list)
            and all(
                isinstance(item, str)
                and bool(item.strip())
                and (not facts or ID_RE.fullmatch(item))
                for item in value
            )
            and len(value) == len(set(value))
        )

    for field in ("external_facts", "external_events"):
        if field in raw and not names(raw[field], facts=field == "external_facts"):
            error(
                "invalid_external_contract",
                f"{field} must contain unique non-empty names",
            )
    completion = raw.get("completion")
    if completion is not None:
        if (
            not isinstance(completion, dict)
            or set(completion) != {"quest_path", "outcomes"}
            or not isinstance(completion.get("quest_path"), str)
            or not completion["quest_path"].startswith("quests/")
            or not isinstance(completion.get("outcomes"), dict)
            or not completion["outcomes"]
        ):
            error(
                "invalid_completion",
                "completion requires quest_path and outcome policies",
            )
        else:
            for outcome, policy in completion["outcomes"].items():
                if (
                    not ID_RE.fullmatch(outcome)
                    or not isinstance(policy, dict)
                    or set(policy) - {"state", "fact"}
                    or not isinstance(policy.get("state"), str)
                    or policy["state"] not in {"Succeeded", "Failed", "Inactive"}
                    or (
                        "fact" in policy
                        and (
                            not isinstance(policy["fact"], str)
                            or not ID_RE.fullmatch(policy["fact"])
                        )
                    )
                ):
                    error(
                        "invalid_completion",
                        f"Invalid terminal completion policy: {outcome}",
                    )
    if "entry_stage" in raw and (
        not isinstance(raw["entry_stage"], str)
        or not ID_RE.fullmatch(raw["entry_stage"])
    ):
        error("invalid_entry_stage", "entry_stage must be a stage id")
    stages = raw.get("stages", [])
    for stage in stages if isinstance(stages, list) else []:
        if not isinstance(stage, dict):
            continue
        identifier = stage.get("id")
        for field in ("inputs", "outcomes", "on"):
            if field not in stage:
                continue
            value = stage[field]
            if (
                not isinstance(value, dict)
                or not value
                or not all(
                    isinstance(key, str)
                    and ID_RE.fullmatch(key)
                    and isinstance(socket, str)
                    and socket.strip()
                    for key, socket in value.items()
                )
            ):
                error(
                    "invalid_ports",
                    f"{field} must map names to non-empty strings",
                    identifier,
                )
            elif field != "on" and len(set(value.values())) != len(value):
                error(
                    "duplicate_port",
                    f"{field} aliases must address distinct sockets",
                    identifier,
                )
        if isinstance(stage.get("inputs"), dict) and "start" not in stage["inputs"]:
            error(
                "missing_start_input", "inputs must declare the start alias", identifier
            )
        contract = stage.get("contract", {})
        fields = {"reads_facts", "writes_facts", "external_events", "scene_exits"}
        if not isinstance(contract, dict) or set(contract) - fields:
            error(
                "invalid_stage_contract",
                f"contract supports only {sorted(fields)}",
                identifier,
            )
            continue
        for field in fields - {"scene_exits"}:
            if field in contract and not names(
                contract[field], facts=field.endswith("facts")
            ):
                error(
                    "invalid_stage_contract",
                    f"contract.{field} must contain unique names",
                    identifier,
                )
        scenes = contract.get("scene_exits", {})
        if not isinstance(scenes, dict) or not all(
            isinstance(scene, str)
            and scene.startswith(("mod\\", "base\\", "ep1\\"))
            and ".." not in scene.split("\\")
            and scene.endswith(".scene")
            and names(exits)
            and exits
            for scene, exits in scenes.items()
        ):
            error(
                "invalid_scene_contract",
                "scene_exits must map scene depot paths to exit names",
                identifier,
            )
        lifecycle = stage.get("objective_lifecycle", {})
        policy = {
            "on_enter": {"activate", "retain"},
            "on_success": {"succeed", "retain"},
            "on_failure": {"fail", "retain"},
            "on_cancelled": {"deactivate", "retain"},
        }
        if (
            not isinstance(lifecycle, dict)
            or set(lifecycle) - set(policy)
            or any(
                not isinstance(value, str) or value not in policy[key]
                for key, value in lifecycle.items()
                if key in policy
            )
        ):
            error(
                "invalid_objective_lifecycle",
                "Invalid objective lifecycle policy",
                identifier,
            )
        elif lifecycle and stage.get("type") not in {
            "meet_contact",
            "braindance_analysis",
            "escort_npc",
            "defend_target",
            "investigate_clues",
        }:
            error(
                "unsupported_objective_lifecycle",
                "This block does not implement objective lifecycle policies",
                identifier,
            )
        elif stage.get("type") in {"meet_contact", "braindance_analysis"} and set(
            lifecycle
        ) & {"on_failure", "on_cancelled"}:
            error(
                "unsupported_objective_lifecycle",
                "Meeting and braindance templates expose only entry and success retention policies",
                identifier,
            )


def validate_flow(spec: QuestSpec) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    stages = {stage.id: stage for stage in spec.stages}
    routes = stage_transitions(spec)
    entry = spec.entry_stage or spec.stages[0].id

    def error(code: str, message: str, stage: str | None = None) -> None:
        diagnostics.append(Diagnostic("error", code, message, stage))

    if entry not in stages:
        error("unknown_entry_stage", f"Unknown entry stage: {entry}")
    explicit = any(
        set(stage.data) & {"inputs", "outcomes", "on"} for stage in spec.stages
    )
    if spec.parallel_groups and (explicit or spec.entry_stage or spec.completion):
        error(
            "parallel_explicit_flow",
            "parallel_groups use implicit success flow; put named branches in child phases",
        )
    for stage in spec.stages:
        outcomes = stage_outcomes(stage)
        if (
            stage.data.get("actor_lifecycle") or stage.data.get("objective_lifecycle")
        ) and (
            "success" not in outcomes
            or set(outcomes) - {"success", "failure", "cancelled"}
        ):
            error(
                "ambiguous_lifecycle_outcome",
                "Lifecycle policies require success/failure/cancelled outcome aliases",
                stage.id,
            )
        for outcome in set(outcomes) - set(routes[stage.id]):
            error(
                "unhandled_outcome",
                f"Outcome {outcome} needs an explicit on route",
                stage.id,
            )
        for outcome, target in routes[stage.id].items():
            if outcome not in outcomes:
                error("unknown_outcome", f"No declared outcome {outcome}", stage.id)
            if target != "$end" and target not in stages:
                error(
                    "unknown_transition",
                    f"Unknown transition target: {target}",
                    stage.id,
                )
            if (
                target == "$end"
                and spec.completion
                and outcome not in spec.completion["outcomes"]
            ):
                error(
                    "missing_completion_policy",
                    f"Terminal outcome {outcome} needs a completion policy",
                    stage.id,
                )
        for event in StageContract.from_data(stage.data).external_events:
            if event not in spec.external_events:
                error(
                    "undeclared_external_event",
                    f"External event {event} is not declared by this quest",
                    stage.id,
                )
    if diagnostics:
        return diagnostics
    # Existing all-of groups have separate compiler wiring. Check concurrent
    # ownership here without pretending the flattened stage list is its graph.
    if spec.parallel_groups:
        for group in spec.parallel_groups:
            branch_resources = [
                set().union(*(_claims(stages[item]) for item in branch))
                for branch in group.branches
            ]
            for index, resources in enumerate(branch_resources):
                for other in branch_resources[index + 1 :]:
                    for resource in resources & other:
                        error(
                            "parallel_ownership_conflict",
                            f"Parallel group {group.id} has competing owners for {resource}",
                        )
        diagnostics.extend(_validate_parallel_facts(spec))
        # Disjoint branch ownership can be checked in manifest order: only one
        # branch can touch each resource, and every branch must finish at the join.
        diagnostics.extend(_validate_ownership(spec, routes, entry))
        return diagnostics

    reachable: set[str] = set()
    pending = [entry]
    while pending:
        current = pending.pop()
        if current == "$end" or current in reachable:
            continue
        reachable.add(current)
        pending.extend(routes[current].values())
    for identifier in stages.keys() - reachable:
        error(
            "unreachable_stage", "Stage cannot be reached from entry_stage", identifier
        )
    can_end = {
        identifier for identifier, edges in routes.items() if "$end" in edges.values()
    }
    while True:
        expanded = can_end | {
            identifier
            for identifier, edges in routes.items()
            if set(edges.values()) & can_end
        }
        if expanded == can_end:
            break
        can_end = expanded
    for identifier in reachable - can_end:
        error("nonterminating_flow", "No outcome route can reach $end", identifier)

    # Definite writes use intersection at merges. Start with the top set and
    # converge down so loop-only writes cannot satisfy a first-entry read.
    contracts = {stage.id: StageContract.from_data(stage.data) for stage in spec.stages}
    universe = set(spec.external_facts).union(
        *(set(value.writes_facts) for value in contracts.values())
    )
    incoming = {identifier: set(universe) for identifier in reachable}
    predecessors = {identifier: set() for identifier in reachable}
    for identifier in reachable:
        for target in routes[identifier].values():
            if target != "$end":
                predecessors[target].add(identifier)
    changed = True
    while changed:
        changed = False
        for identifier in reachable:
            paths = [
                incoming[parent] | set(contracts[parent].writes_facts)
                for parent in predecessors[identifier]
            ]
            if identifier == entry:
                paths.append(set(spec.external_facts))
            value = set.intersection(*paths) if paths else set()
            if value != incoming[identifier]:
                incoming[identifier] = value
                changed = True
    for identifier in reachable:
        for fact in set(contracts[identifier].reads_facts) - incoming[identifier]:
            error(
                "missing_fact_producer",
                f"Fact {fact} needs an upstream writer on every path or external_facts declaration",
                identifier,
            )
    diagnostics.extend(_validate_ownership(spec, routes, entry))
    return diagnostics


def _validate_parallel_facts(spec: QuestSpec) -> list[Diagnostic]:
    stages = {stage.id: stage for stage in spec.stages}
    groups = {
        min(stages[name].index for branch in group.branches for name in branch): group
        for group in spec.parallel_groups
    }
    available = set(spec.external_facts)
    diagnostics = []

    def sequence(names: tuple[str, ...], initial: set[str]) -> set[str]:
        known = set(initial)
        for name in names:
            contract = StageContract.from_data(stages[name].data)
            for fact in set(contract.reads_facts) - known:
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "missing_fact_producer",
                        f"Fact {fact} needs a prior writer in this branch or an external_facts declaration",
                        name,
                    )
                )
            known.update(contract.writes_facts)
        return known

    index = 0
    while index < len(spec.stages):
        group = groups.get(index)
        if group:
            # All-of completion guarantees every branch's unconditional writes.
            branch_writes = [sequence(branch, available) for branch in group.branches]
            available.update(*branch_writes)
            index = (
                max(stages[name].index for branch in group.branches for name in branch)
                + 1
            )
        else:
            available = sequence((spec.stages[index].id,), available)
            index += 1
    return diagnostics


def _claims(stage: Any) -> set[str]:
    result = set()
    if stage.data.get("actor_lifecycle"):
        result.add(f"actor:{stage.data.get('community')}:{stage.data.get('entry')}")
    if stage.data.get("objective_lifecycle"):
        result.add(f"objective:{stage.data.get('objective')}")
    return result


def _validate_ownership(
    spec: QuestSpec, routes: dict[str, dict[str, str]], entry: str
) -> list[Diagnostic]:
    """Track each declared resource independently, including alternative paths."""
    result = []
    stages = {stage.id: stage for stage in spec.stages}
    resources = set().union(*(_claims(stage) for stage in spec.stages))
    reported: set[tuple[str, str, str]] = set()
    for resource in resources:
        pending = deque([(entry, False)])
        seen = set()
        while pending:
            identifier, owned = pending.popleft()
            if (identifier, owned) in seen:
                continue
            seen.add((identifier, owned))
            stage = stages[identifier]
            policy = {}
            if resource in _claims(stage):
                actor = resource.startswith("actor:")
                policy = stage.data[
                    "actor_lifecycle" if actor else "objective_lifecycle"
                ]
                acquire = "assign_follower" if actor else "activate"
                default_enter = (
                    "retain" if actor and stage.type == "defend_target" else acquire
                )
                enter = policy.get("on_enter", default_enter)
                problem = (
                    "ownership_not_acquired"
                    if enter == "retain" and not owned
                    else (
                        "ownership_already_acquired"
                        if enter == acquire and owned
                        else None
                    )
                )
                if problem:
                    key = (problem, identifier, resource)
                    if key not in reported:
                        result.append(
                            Diagnostic(
                                "error",
                                problem,
                                f"Invalid {enter} handoff for {resource}",
                                identifier,
                            )
                        )
                        reported.add(key)
                owned = True
            for outcome, target in routes[identifier].items():
                retained = owned
                if policy:
                    retained = policy.get(f"on_{outcome}", "release") == "retain"
                if target == "$end":
                    if retained:
                        key = ("ownership_leak", identifier, resource)
                        if key not in reported:
                            result.append(
                                Diagnostic(
                                    "error",
                                    key[0],
                                    f"Terminal {outcome} retains {resource} without an owner",
                                    identifier,
                                )
                            )
                            reported.add(key)
                else:
                    pending.append((target, retained))
    return result


def walk(value: Any):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def validate_phase_ports(stage: Any, phase: dict[str, Any]) -> None:
    _, nodes, edges = _phase_topology(phase)
    for kind, declared in (
        ("Input", stage_inputs(stage)),
        ("Output", stage_outcomes(stage)),
    ):
        emitted = {
            node.get("socketName", {}).get("$value")
            for node in nodes.values()
            if node.get("$type") == f"quest{kind}NodeDefinition"
        }
        missing = set(declared.values()) - emitted
        if missing:
            raise QuestSpecError(
                f"Stage {stage.id} declares missing {kind.lower()} ports: {sorted(missing)}"
            )
    starts = {
        identifier
        for identifier, node in nodes.items()
        if node.get("$type") == "questInputNodeDefinition"
        and node.get("socketName", {}).get("$value") == stage_inputs(stage)["start"]
    }
    reachable = _reachable(edges, starts)
    for identifier, node in nodes.items():
        if (
            node.get("$type") == "questOutputNodeDefinition"
            and node.get("socketName", {}).get("$value")
            in stage_outcomes(stage).values()
        ):
            if identifier not in reachable:
                raise QuestSpecError(
                    f"Stage {stage.id} declares an unreachable output: {node['socketName']['$value']}"
                )


def validate_emitted_contract(stage: Any, phase: dict[str, Any]) -> None:
    """Check declarations against typed nodes, never arbitrary matching text."""
    contract = StageContract.from_data(stage.data)
    nodes = list(walk(phase))

    # RED types use either a plain string or CName depending on the field.
    def value(item: Any) -> Any:
        return item.get("$value") if isinstance(item, dict) else item

    writes = {
        value(node.get("factName"))
        for node in nodes
        if node.get("$type") == "questSetVar_NodeType"
    }
    reads = {
        value(node.get("factName"))
        for node in nodes
        if node.get("$type")
        in {"questVarComparison_ConditionType", "questFactsDBCondition"}
    }
    for category, declared, emitted in (
        ("writes", contract.writes_facts, writes),
        ("reads", contract.reads_facts, reads),
    ):
        missing = set(declared) - emitted
        if missing:
            raise QuestSpecError(
                f"Stage {stage.id} contract {category} absent from typed fact nodes: {sorted(missing)}"
            )
    if contract.writes_facts:
        _validate_unconditional_writes(stage, phase, contract.writes_facts)
    for scene, exits in contract.scene_exits:
        scene_nodes = [
            node
            for node in nodes
            if node.get("$type") == "questSceneNodeDefinition"
            and any(
                item.get("$value") == scene for item in walk(node.get("sceneFile", {}))
            )
        ]
        if not scene_nodes:
            raise QuestSpecError(f"Stage {stage.id} contract scene is absent: {scene}")
        definitions = {
            str(node["HandleId"]): node["Data"]
            for node in nodes
            if "HandleId" in node and "Data" in node
        }
        sockets = set()
        for node in scene_nodes:
            for socket in node.get("sockets", []):
                data = socket.get("Data") or definitions.get(
                    str(socket.get("HandleRefId")), {}
                )
                if data.get("type") == "Output":
                    sockets.add(value(data.get("name")))
        if set(exits) - sockets:
            raise QuestSpecError(
                f"Stage {stage.id} scene {scene} lacks required output sockets: {sorted(set(exits) - sockets)}"
            )


def _validate_unconditional_writes(
    stage: Any, phase: dict[str, Any], facts: tuple[str, ...]
) -> None:
    """A writes_facts promise must hold on every declared phase outcome path."""
    definitions, graph_nodes, adjacency = _phase_topology(phase)

    def resolve(wrapper: dict[str, Any]) -> dict[str, Any]:
        return definitions[str(wrapper.get("HandleId", wrapper.get("HandleRefId")))]

    starts = {
        identifier
        for identifier, node in graph_nodes.items()
        if node.get("$type") == "questInputNodeDefinition"
        and node.get("socketName", {}).get("$value") == stage_inputs(stage)["start"]
    }
    ends = {
        identifier
        for identifier, node in graph_nodes.items()
        if node.get("$type") == "questOutputNodeDefinition"
        and node.get("socketName", {}).get("$value") in stage_outcomes(stage).values()
    }
    for fact in facts:
        writers = set()
        for identifier, node in graph_nodes.items():
            if node.get("$type") == "questFactsDBManagerNodeDefinition":
                operation = resolve(node["type"])
                if (
                    operation.get("$type") == "questSetVar_NodeType"
                    and operation.get("factName") == fact
                ):
                    writers.add(identifier)
        seen = _reachable(adjacency, starts, stop=writers)
        if seen & ends:
            raise QuestSpecError(
                f"Stage {stage.id} contract writes fact {fact} on only some outcome paths"
            )


def _reachable(
    edges: dict[str, set[str]], starts: set[str], *, stop: set[str] | None = None
) -> set[str]:
    pending = list(starts)
    seen = set()
    while pending:
        current = pending.pop()
        if current in seen or (stop and current in stop):
            continue
        seen.add(current)
        pending.extend(edges[current])
    return seen


def _phase_topology(phase: dict[str, Any]) -> tuple[dict, dict, dict[str, set[str]]]:
    definitions = {
        str(item["HandleId"]): item["Data"]
        for item in walk(phase)
        if "HandleId" in item
    }
    graph = phase.get("Data", {}).get("RootChunk", {}).get("graph", {}).get("Data", {})
    graph_nodes = {
        str(wrapper.get("HandleId", wrapper.get("HandleRefId"))): definitions[
            str(wrapper.get("HandleId", wrapper.get("HandleRefId")))
        ]
        for wrapper in graph.get("nodes", [])
    }
    owners = {
        str(socket.get("HandleId", socket.get("HandleRefId"))): identifier
        for identifier, node in graph_nodes.items()
        for socket in node.get("sockets", [])
    }
    adjacency = {identifier: set() for identifier in graph_nodes}
    for node in definitions.values():
        if node.get("$type") != "graphGraphConnectionDefinition":
            continue
        endpoints = [
            str(node[key].get("HandleId", node[key].get("HandleRefId")))
            for key in ("source", "destination")
        ]
        if all(endpoint in owners for endpoint in endpoints):
            adjacency[owners[endpoints[0]]].add(owners[endpoints[1]])
    return definitions, graph_nodes, adjacency


def audit_scene_contracts(spec: QuestSpec, root: Any) -> list[Diagnostic]:
    """Check child phase socket promises against real authored scene exit tables."""
    import json
    from pathlib import Path
    from project_layout import source_path

    diagnostics = []
    for stage in spec.stages:
        for scene, exits in StageContract.from_data(stage.data).scene_exits:
            raw = source_path(scene, "raw", root=Path(root))
            level = "warning" if stage.status == "planned" else "error"
            try:
                scene_root = json.loads(raw.read_text(encoding="utf-8"))["Data"][
                    "RootChunk"
                ]
                points = {
                    point.get("name", {}).get("$value"): point.get("nodeId", {}).get(
                        "id"
                    )
                    for point in scene_root["exitPoints"]
                }
                ends = {
                    node.get("nodeId", {}).get("id")
                    for node in walk(scene_root.get("sceneGraph", {}))
                    if node.get("$type") == "scnEndNode"
                }
            except (OSError, ValueError, KeyError, TypeError) as exc:
                diagnostics.append(
                    Diagnostic(
                        level,
                        "missing_scene_contract_evidence",
                        f"Cannot inspect scene contract {scene}: {exc}",
                        stage.id,
                    )
                )
                continue
            for name in exits:
                if name not in points or points[name] not in ends:
                    diagnostics.append(
                        Diagnostic(
                            level,
                            "missing_scene_exit",
                            f"Scene {scene} has no emitted exit {name}",
                            stage.id,
                        )
                    )
    return diagnostics
