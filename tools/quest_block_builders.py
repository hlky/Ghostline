"""Variable quest recipes built from the existing RED graph primitives.

Legacy templates remain the default for their original shapes. Extended fields
select these generators through quest_stages; an explicit phase_template wins.

Escort gates are ordered and count is unrestricted. Actor policy assigns or
retains a follower on entry, then releases or retains it on each outcome.
Timed defense accepts milliseconds, optional attackers, and explicit failure
and cancellation ports. At resolution, actor defeat takes priority over
cancellation, which takes priority over success. Objective and actor cleanup
happens after one shared resolution gate. block_on_failure keeps the phase
active for native checkpoint recovery; it cannot also emit a failure port.

Choice branches are evaluated in declaration order. A fallback makes evaluation
an immediate snapshot; without fallback, a listener waits for a positive fact
before the snapshot. Those condition facts must remain set until resolution.
Investigation defaults to ordered scanning when all clues are required and
any order for partial thresholds; scan_order can override that. Each distinct
object scan and its side effects are latched once. The O(N*K) threshold graph
counts distinct signals without mutable counters or duplicate-event inflation.

These are graph construction guarantees. Native conversion and structural
tests do not prove REDengine scheduling, checkpoint restoration, or persistence
of a partially completed investigation; those still need in-game evidence.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable

from generate_advanced_quest_block_templates import (
    assign_follower_role,
    character_killed,
    clear_ai_role,
    puppet_ai_tier,
    trigger_condition,
)
from phase_graph import (
    GraphNode,
    JsonObject,
    PhaseGraphBuilder,
    add_item_node,
    character_spawned_node,
    cname,
    combat_threat_node,
    community_action_node,
    entity_reference,
    fact_condition_node,
    fact_node,
    input_node,
    journal_entry_node,
    logical_and_node,
    logical_xor_node,
    mappin_node,
    objective_node,
    phase_document,
    scan_started_node,
    realtime_delay_node,
)
from quest_types import CompiledStage, QuestSpecError
from quest_orchestration import order_handles


@dataclass(frozen=True)
class Signal:
    node: GraphNode
    socket: str = "Out"


class BlockBuilder:
    """Allocate block nodes and keep lifecycle policy separate from wiring."""

    def __init__(self, stage: CompiledStage):
        self.stage = stage
        self.graph = PhaseGraphBuilder()
        self.next_id = 10
        self.start = Signal(input_node(self.graph))
        inputs = stage.data.get("inputs", {"start": "In1"})
        if len(inputs) != 1:
            raise QuestSpecError(f"Block {stage.id} requires exactly one start input")
        self.start.node.data["socketName"] = cname(next(iter(inputs.values())))
        self.outputs = {}
        for index, (outcome, socket) in enumerate(
            stage.data.get("outcomes", {"success": "Out1"}).items(), 1
        ):
            self.outputs[outcome] = self.graph.node(
                index,
                "questOutputNodeDefinition",
                input_names=("In",),
                output_names=(),
                properties={"socketName": cname(socket), "type": "Terminating"},
            )
        self.next_id = max(10, len(self.outputs) + 1)

    def node(self, factory: Callable, *args, socket: str = "Out", **kwargs) -> Signal:
        node = factory(self.graph, self.next_id, *args, **kwargs)
        self.next_id += 1
        return Signal(node, socket)

    def connect(self, source: Signal, target: Signal, input_socket: str = "In") -> None:
        self.graph.connect(
            source.node,
            target.node,
            source_socket=source.socket,
            destination_socket=input_socket,
        )

    def append(
        self, source: Signal, target: Signal, input_socket: str = "In"
    ) -> Signal:
        self.connect(source, target, input_socket)
        return target

    def fact(self, source: Signal, name: str | None, value: int = 1) -> Signal:
        if name is None:
            return source
        target = self.node(fact_node, name)
        target.node.data["type"]["Data"]["value"] = value
        return self.append(source, target)

    def objective(self, source: Signal, phase: str) -> Signal:
        path = self.stage.data.get("objective")
        if not path:
            return source
        defaults = {
            "enter": "activate",
            "success": "succeed",
            "failure": "fail",
            "cancelled": "deactivate",
        }
        action = self.stage.data.get("objective_lifecycle", {}).get(
            "on_" + phase, defaults[phase]
        )
        if action == "retain":
            return source
        sockets = {
            "activate": "Active",
            "succeed": "Succeeded",
            "fail": "Failed",
            "deactivate": "Inactive",
        }
        return self.append(source, self.node(objective_node, path), sockets[action])

    def enter(self) -> Signal:
        source = self.objective(self.start, "enter")
        description = self.stage.data.get("description_entry")
        if description:
            source = self.append(
                source,
                self.node(
                    journal_entry_node, description, "gameJournalQuestDescription", 2
                ),
                "Active",
            )
        return source

    def actor(self, source: Signal, outcome: str, *, default: str) -> Signal:
        data = self.stage.data
        action = data.get("actor_lifecycle", {}).get("on_" + outcome, default)
        if action == "retain":
            return source
        if action == "assign_follower":
            source = self.append(
                source, self.node(puppet_ai_tier, data["community"], data["entry"])
            )
            return self.append(
                source,
                self.node(
                    assign_follower_role,
                    data["community"],
                    data["entry"],
                    socket="Success",
                ),
            )
        return self.append(
            source,
            self.node(
                clear_ai_role, data["community"], data["entry"], socket="Success"
            ),
        )

    def finish(self, source: Signal, outcome: str) -> None:
        output = self.outputs.get(outcome)
        if output is not None:
            self.graph.connect_to_earlier_output(
                source.node, output, source_socket=source.socket
            )

    def document(self, archive: Path) -> JsonObject:
        return order_handles(phase_document(self.graph, archive))


def _instant(condition: Signal, block: BlockBuilder) -> tuple[Signal, Signal]:
    """Use vanilla questConditionNodeDefinition for an immediate state snapshot."""
    condition.node.data["$type"] = "questConditionNodeDefinition"
    condition.node.data["sockets"] = [
        socket
        for socket in condition.node.data["sockets"]
        if socket not in condition.node.outputs.values()
    ]
    condition.node.outputs.clear()
    for name in ("True", "False"):
        socket = block.graph.socket(name, "Output")
        condition.node.outputs[name] = socket
        condition.node.data["sockets"].append(socket)
    return Signal(condition.node, "True"), Signal(condition.node, "False")


def _resolve_outcomes(
    block: BlockBuilder, running: Signal, success: Signal, *, watch_failure: bool
) -> dict[str, Signal]:
    """Latch one resolution; a defeated actor takes priority at the boundary."""
    signals = [success]
    data = block.stage.data
    if watch_failure:
        failed = block.node(character_killed, data["community"], data["entry"])
        block.connect(running, failed)
        signals.append(failed)
    cancellation = data.get("cancellation_fact")
    if cancellation:
        cancelled = block.node(fact_condition_node, cancellation)
        block.connect(running, cancelled)
        signals.append(cancelled)
    gate = block.node(logical_xor_node, len(signals), socket="Out1")
    for index, signal in enumerate(signals, 1):
        block.connect(signal, gate, f"In{index}")
    unresolved = gate
    results = {}
    if watch_failure:
        failed, healthy = _instant(
            block.node(character_killed, data["community"], data["entry"]), block
        )
        block.connect(unresolved, failed)
        results["failure"] = failed
        unresolved = healthy
    if cancellation:
        cancelled, continuing = _instant(
            block.node(fact_condition_node, cancellation), block
        )
        block.connect(unresolved, cancelled)
        results["cancelled"] = cancelled
        unresolved = continuing
    results["success"] = unresolved
    return results


def _cleanup_actor_outcome(
    block: BlockBuilder,
    signal: Signal,
    outcome: str,
    *,
    mappins: list[str],
    attackers: str | None = None,
) -> None:
    for path in dict.fromkeys(mappins):
        signal = block.append(signal, block.node(mappin_node, path), "Inactive")
    if attackers:
        signal = block.append(
            signal, block.node(community_action_node, attackers, "Deactivate")
        )
    signal = block.actor(signal, outcome, default="release")
    signal = block.objective(signal, outcome)
    fact_field = {
        "success": "completion_fact",
        "failure": "failure_fact",
        "cancelled": "cancelled_fact",
    }[outcome]
    signal = block.fact(signal, block.stage.data.get(fact_field))
    if outcome == "failure" and block.stage.data.get("block_on_failure", False):
        return  # A parent retry checkpoint owns recovery; normal progress is blocked.
    block.finish(signal, outcome)


def build_escort_phase(stage: CompiledStage, archive: Path) -> JsonObject:
    """Escort through arbitrary ordered gates with explicit actor handoff."""
    block = BlockBuilder(stage)
    active = block.enter()
    running = block.actor(active, "enter", default="assign_follower")
    previous = running
    gates = stage.data["destinations"]
    pins = stage.data.get("route_mappins") or [stage.data["mappin"]] * len(gates)
    if len(pins) != len(gates):
        raise QuestSpecError("route_mappins must match the escort destinations")
    for destination, pin in zip(gates, pins, strict=True):
        previous = block.append(previous, block.node(mappin_node, pin), "Active")
        previous = block.append(
            previous,
            block.node(
                trigger_condition,
                destination,
                entity_reference(stage.data["community"], names=(stage.data["entry"],)),
            ),
        )
        previous = block.append(previous, block.node(mappin_node, pin), "Inactive")
    outcomes = _resolve_outcomes(block, active, previous, watch_failure=True)
    for outcome, signal in outcomes.items():
        _cleanup_actor_outcome(block, signal, outcome, mappins=pins)
    return block.document(archive)


def build_timed_defense_phase(stage: CompiledStage, archive: Path) -> JsonObject:
    """Defend a named actor until a timer or external completion fact resolves."""
    block = BlockBuilder(stage)
    protected_ready = block.enter()
    running = block.actor(protected_ready, "enter", default="retain")
    data = stage.data
    attackers = data.get("attackers")
    if attackers:
        community = attackers["community"]
        running = block.append(
            running, block.node(community_action_node, community, "Activate")
        )
        running = block.append(running, block.node(character_spawned_node, community))
        for attacker in attackers["entries"]:
            threat = block.node(
                combat_threat_node, community, attacker["entry"], socket="Success"
            )
            # Preserve the timed-hold fixture's combat command duration.
            threat.node.data["params"]["Data"]["duration"] = 0
            threat.node.data["function"] = cname("questCombatNodeParams_ShootAt")
            if attacker.get("target", "player") == "protected":
                threat.node.data["params"]["Data"]["targetPuppetRef"] = (
                    entity_reference(data["community"], names=(data["entry"],))
                )
            running = block.append(running, threat)
    if "duration_seconds" in data:
        # Preserve sub-second durations without silently truncating them.
        duration_ms = round(data["duration_seconds"] * 1000)
        success = block.node(
            realtime_delay_node,
            seconds=duration_ms // 1000,
            milliseconds=duration_ms % 1000,
        )
    else:
        success = block.node(fact_condition_node, data["completion_fact"])
    block.connect(running, success)
    outcomes = _resolve_outcomes(block, protected_ready, success, watch_failure=True)
    cleanup = (
        attackers["community"] if attackers and attackers.get("cleanup", True) else None
    )
    for outcome, signal in outcomes.items():
        _cleanup_actor_outcome(block, signal, outcome, mappins=[], attackers=cleanup)
    return block.document(archive)


def build_choice_phase(stage: CompiledStage, archive: Path) -> JsonObject:
    """Choose an ordered fact branch; fallback is an explicit entry-time choice."""
    block = BlockBuilder(stage)
    data = stage.data
    branches = data["branches"]
    fallback = data.get("default_branch")
    evaluation = data.get("evaluation", "on_entry" if fallback else "wait")
    tails: list[tuple[str, Signal]] = []
    if evaluation == "on_entry":
        previous = block.start
        for branch in branches:
            yes, no = _instant(
                block.node(fact_condition_node, branch["condition"]), block
            )
            block.connect(previous, yes)
            tails.append((branch["id"], block.fact(yes, branch["set_fact"])))
            previous = no
        if fallback:
            branch = next(branch for branch in branches if branch["id"] == fallback)
            tails.append((branch["id"], block.fact(previous, branch["set_fact"])))
    else:
        # Wait until any branch is true, then snapshot in declaration order.
        probes = [
            block.node(fact_condition_node, branch["condition"]) for branch in branches
        ]
        join = block.node(logical_xor_node, len(probes), socket="Out1")
        for index, probe in enumerate(probes, 1):
            block.connect(block.start, probe)
            block.connect(probe, join, f"In{index}")
        previous = join
        for branch in branches:
            yes, no = _instant(
                block.node(fact_condition_node, branch["condition"]), block
            )
            block.connect(previous, yes)
            tails.append((branch["id"], block.fact(yes, branch["set_fact"])))
            previous = no
    for branch_id, signal in tails:
        block.finish(signal, branch_id if branch_id in block.outputs else "success")
    return block.document(archive)


def distinct_threshold(
    block: BlockBuilder, signals: list[Signal], required: int
) -> Signal:
    """At least K distinct signals in O(N*K) gates; each clue contributes once."""
    levels: dict[int, Signal] = {}
    for index, signal in enumerate(signals, 1):
        next_levels = {}
        for count in range(1, min(required, index) + 1):
            if count == 1:
                acquired = signal
            else:
                both = block.node(logical_and_node, 2, socket="Out1")
                block.connect(levels[count - 1], both, "In1")
                block.connect(signal, both, "In2")
                acquired = both
            if count in levels:
                either = block.node(logical_xor_node, 2, socket="Out1")
                block.connect(levels[count], either, "In1")
                block.connect(acquired, either, "In2")
                acquired = either
            next_levels[count] = acquired
        levels = next_levels
    return levels[required]


def build_investigation_phase(stage: CompiledStage, archive: Path) -> JsonObject:
    """Scan any K distinct clues, preserving each clue's one-time side effects."""
    block = BlockBuilder(stage)
    running = block.enter()
    signals = []
    pins = []
    clues = stage.data["clues"]
    required = stage.data.get("required_count", len(clues))
    any_order = (
        stage.data.get("scan_order", "any" if required < len(clues) else "ordered")
        == "any"
    )
    previous_clue = running
    for clue in clues:
        previous = running if any_order else previous_clue
        if clue.get("mappin"):
            pins.append(clue["mappin"])
            previous = block.append(
                previous, block.node(mappin_node, clue["mappin"]), "Active"
            )
        scanned = block.node(scan_started_node, clue["object_ref"])
        block.connect(previous, scanned)
        once = block.node(logical_xor_node, 1, socket="Out1")
        previous = block.append(scanned, once, "In1")
        if clue.get("mappin"):
            previous = block.append(
                previous, block.node(mappin_node, clue["mappin"]), "Inactive"
            )
        if clue.get("journal_entry"):
            previous = block.append(
                previous,
                block.node(
                    journal_entry_node, clue["journal_entry"], "gameJournalOnscreen", 5
                ),
                "Active",
            )
        previous = block.fact(previous, clue.get("completion_fact"))
        items = ([clue["grant_item"]] if clue.get("grant_item") else []) + clue.get(
            "grant_items", []
        )
        for item in items:
            previous = block.append(previous, block.node(add_item_node, item, 1))
        signals.append(previous)
        previous_clue = previous
    resolved = distinct_threshold(block, signals, required)
    for path in dict.fromkeys(pins):
        resolved = block.append(resolved, block.node(mappin_node, path), "Inactive")
    resolved = block.objective(resolved, "success")
    resolved = block.fact(resolved, stage.data.get("completion_fact"))
    block.finish(resolved, "success")
    return block.document(archive)
