"""Evaluate emitted graph paths independently of the block construction code.

The small interpreter models one-shot quest AND/XOR and condition signals. It
checks structural behavior, not REDengine scheduling or save-game persistence.
"""

from __future__ import annotations

from collections import defaultdict, deque
from itertools import permutations
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import quest_compiler as compiler
from quest_block_builders import (
    build_choice_phase,
    build_escort_phase,
    build_investigation_phase,
    build_timed_defense_phase,
)
from quest_stage_validation import (
    validate_choice_gate,
    validate_defend_target,
    validate_escort_npc,
    validate_investigate_clues,
)
from quest_stages import STAGE_REGISTRY
from quest_types import CompiledStage


def objects(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from objects(child)


def stage(kind, **fields):
    data = {"id": "block", "type": kind, "objective": "quests/test/objective", **fields}
    return CompiledStage(0, "block", kind, "ready", r"mod\test\block.questphase", data)


def document(builder, value):
    result = builder(value, ROOT / "generated/tests/block.questphase")
    compiler.validate_handle_graph(result, context="block")
    compiler.validate_no_forward_handle_refs(result, context="block")
    return result


class GraphRun:
    """Follow serialized edges; only explicit external events release waiters."""

    def __init__(
        self, document, *, facts=None, stall_threats=False, stall_follower=False
    ):
        self.definitions = {
            str(item["HandleId"]): item["Data"]
            for item in objects(document)
            if "HandleId" in item
        }
        self.nodes = {
            handle: item
            for handle, item in self.definitions.items()
            if "sockets" in item
        }
        self.owners = {}
        self.output_names = defaultdict(list)
        for handle, node in self.nodes.items():
            for wrapper in node["sockets"]:
                socket_id = self.handle(wrapper)
                socket = self.definitions[socket_id]
                self.owners[socket_id] = (handle, socket["name"]["$value"])
                if socket["type"] == "Output":
                    self.output_names[handle].append(socket["name"]["$value"])
        self.edges = defaultdict(list)
        for item in self.definitions.values():
            if item.get("$type") == "graphGraphConnectionDefinition":
                self.edges[self.owners[self.handle(item["source"])]].append(
                    self.owners[self.handle(item["destination"])]
                )
        self.facts = dict(facts or {})
        self.dead = False
        self.active = set()
        self.fired = set()
        self.and_inputs = defaultdict(set)
        self.outputs = []
        self.trace = []
        self.pending = deque()
        self.stall_threats = stall_threats
        self.stall_follower = stall_follower
        self.terminated = False
        start = next(
            handle
            for handle, node in self.nodes.items()
            if node["$type"] == "questInputNodeDefinition"
        )
        self.emit(start, "Out")
        self.drain()

    @staticmethod
    def handle(wrapper):
        return str(wrapper.get("HandleId", wrapper.get("HandleRefId")))

    def typed(self, node, kind):
        return next((item for item in objects(node) if item.get("$type") == kind), None)

    def condition(self, node):
        wrapper = node["condition"]
        value = self.definitions[self.handle(wrapper)]
        nested = value.get("type")
        return (
            self.definitions[self.handle(nested)] if isinstance(nested, dict) else value
        )

    def truth(self, node):
        condition = self.condition(node)
        if condition["$type"] == "questCharacterKilled_ConditionType":
            return self.dead
        if condition["$type"] == "questVarComparison_ConditionType":
            return self.facts.get(condition["factName"], 0) > condition["value"]
        return False

    def emit(self, handle, socket):
        self.pending.extend(self.edges[handle, socket])

    def drain(self):
        while self.pending and not self.terminated:
            handle, input_name = self.pending.popleft()
            node = self.nodes[handle]
            kind = node["$type"]
            self.trace.append((node, input_name))
            if kind == "questOutputNodeDefinition":
                self.outputs.append(node["socketName"]["$value"])
                self.terminated = True
                continue
            if kind == "questPhaseNodeDefinition":
                self.active.add(handle)
                continue
            if kind == "questPauseConditionNodeDefinition":
                self.active.add(handle)
                if self.truth(node):
                    self.emit(handle, "Out")
                continue
            if kind == "questConditionNodeDefinition":
                self.emit(handle, "True" if self.truth(node) else "False")
                continue
            if kind in {
                "questLogicalXorNodeDefinition",
                "questLogicalAndNodeDefinition",
            }:
                if handle in self.fired:
                    continue
                self.and_inputs[handle].add(input_name)
                if (
                    kind.endswith("AndNodeDefinition")
                    and len(self.and_inputs[handle]) < node["inputSocketCount"]
                ):
                    continue
                self.fired.add(handle)
            if kind == "questFactsDBManagerNodeDefinition":
                fact = self.definitions[self.handle(node["type"])]
                self.facts[fact["factName"]] = fact["value"]
            if self.stall_threats and kind == "questCombatNodeDefinition":
                continue
            if self.stall_follower and self.typed(node, "AIAssignRoleCommandParams"):
                continue
            names = self.output_names[handle]
            if len(names) != 1:
                raise AssertionError(
                    f"Unsupported interpreter node outputs: {kind}: {names}"
                )
            self.emit(handle, names[0])

    def events(self, *events):
        """Inject a batch before propagation to cover competing outcome signals."""
        if "defeated" in events:
            self.dead = True
        for event in events:
            if event.startswith("fact:"):
                self.facts[event[5:]] = 1
        for handle in list(self.active):
            condition = self.condition(self.nodes[handle])
            kind = condition["$type"]
            matches = (
                (kind == "questCharacterKilled_ConditionType" and "defeated" in events)
                or (
                    kind == "questVarComparison_ConditionType"
                    and f"fact:{condition['factName']}" in events
                )
                or (kind == "questRealtimeDelay_ConditionType" and "timer" in events)
                or any(
                    event
                    in {
                        item.get("$value"),
                        item.get("triggerAreaRef", {}).get("$value"),
                    }
                    for item in objects(condition)
                    for event in events
                )
            )
            if matches:
                self.emit(handle, "Out")
        self.drain()

    def actions(self, kind):
        return [(node, socket) for node, socket in self.trace if self.typed(node, kind)]

    def complete_phase(self, depot, socket="Out1"):
        handle = next(
            handle
            for handle in self.active
            if self.nodes[handle]
            .get("phaseResource", {})
            .get("DepotPath", {})
            .get("$value")
            == depot
        )
        self.active.remove(handle)
        self.emit(handle, socket)
        self.drain()


class VariableQuestBlockTests(unittest.TestCase):
    def test_k_distinct_clues_all_subsets_orders_and_repeated_events(self):
        # Every ordered subset of five clues, each scanned twice. Repeated scans
        # must not grant twice or cross the threshold early.
        for required in range(1, 6):
            clues = [
                {
                    "id": f"clue_{i}",
                    "object_ref": f"#clue_{i}",
                    "completion_fact": f"scanned_{i}",
                    "grant_item": f"Items.clue_{i}",
                }
                for i in range(5)
            ]
            phase = document(
                build_investigation_phase,
                stage(
                    "investigate_clues",
                    clues=clues,
                    required_count=required,
                    scan_order="any",
                    completion_fact="done",
                ),
            )
            for length in range(6):
                for order in permutations(range(5), length):
                    run = GraphRun(phase)
                    for count, clue in enumerate(order, 1):
                        run.events(f"#clue_{clue}")
                        run.events(f"#clue_{clue}")
                        self.assertEqual(
                            bool(run.outputs),
                            count >= required,
                            (required, order, count),
                        )
                    self.assertEqual(
                        len(run.actions("questAddRemoveItem_NodeType")),
                        min(length, required),
                    )
                    self.assertEqual(run.facts.get("done", 0), int(length >= required))

    def test_escort_arbitrary_ordered_gates_and_actor_handoff(self):
        for count in (1, 2, 5):
            gates = [f"#gate_{i}" for i in range(count)]
            phase = document(
                build_escort_phase,
                stage(
                    "escort_npc",
                    community="#patch",
                    entry="patch",
                    destinations=gates,
                    mappin="quests/test/pin",
                    completion_fact="escorted",
                    failure_fact="lost",
                    outcomes={"success": "Out1", "failure": "Failure"},
                    actor_lifecycle={"on_success": "retain"},
                ),
            )
            run = GraphRun(phase)
            if count > 1:
                run.events(gates[-1])
                self.assertEqual(run.outputs, [])
            for index, gate in enumerate(gates):
                run.events(gate)
                self.assertEqual(bool(run.outputs), index == count - 1)
            self.assertEqual(run.outputs, ["Out1"])
            self.assertEqual(len(run.actions("AIAssignRoleCommandParams")), 1)
            self.assertEqual(run.actions("AIClearRoleCommandParams"), [])
            failed = GraphRun(phase)
            failed.events("defeated", *gates)
            self.assertEqual(failed.outputs, ["Failure"])
            self.assertEqual(failed.facts.get("escorted", 0), 0)
            self.assertEqual(len(failed.actions("AIClearRoleCommandParams")), 1)
            stalled = GraphRun(phase, stall_follower=True)
            stalled.events("defeated")
            self.assertEqual(stalled.outputs, ["Failure"])

    def defense(self, **overrides):
        data = dict(
            community="#patch",
            entry="patch",
            completion_fact="held",
            failure_fact="lost",
            cancellation_fact="cancel",
            cancelled_fact="cancelled",
            duration_seconds=2.25,
            outcomes={
                "success": "Out1",
                "failure": "Failure",
                "cancelled": "Cancelled",
            },
            attackers={
                "community": "#attackers",
                "entries": [{"entry": "gunner", "target": "protected"}],
                "cleanup": True,
            },
        )
        data.update(overrides)
        return stage("defend_target", **data)

    def test_defense_winner_owns_cleanup_and_facts(self):
        phase = document(build_timed_defense_phase, self.defense())
        for event, outcome, fact in [
            ("timer", "Out1", "held"),
            ("defeated", "Failure", "lost"),
            ("fact:cancel", "Cancelled", "cancelled"),
        ]:
            run = GraphRun(phase)
            self.assertEqual(run.actions("AIClearRoleCommandParams"), [])
            run.events("#attackers")
            run.events(event)
            self.assertEqual(run.outputs, [outcome])
            run.events("timer", "defeated", "fact:cancel")
            self.assertEqual(len(run.actions("AIClearRoleCommandParams")), 1)
            self.assertEqual(
                {name for name in ("held", "lost", "cancelled") if run.facts.get(name)},
                {fact},
            )
        race = GraphRun(phase)
        race.events("#attackers")
        race.events("timer", "defeated")
        self.assertEqual(race.outputs, ["Failure"])
        self.assertNotIn("held", race.facts)
        timer = next(
            item
            for item in objects(phase)
            if item.get("$type") == "questRealtimeDelay_ConditionType"
        )
        self.assertEqual((timer["seconds"], timer["miliseconds"]), (2, 250))

    def test_actor_failure_remains_armed_if_attacker_setup_stalls(self):
        run = GraphRun(
            document(build_timed_defense_phase, self.defense()), stall_threats=True
        )
        # Spawn completion unlocks the threat command which intentionally stalls.
        run.events("#attackers")
        run.events("defeated")
        self.assertEqual(run.outputs, ["Failure"])

    def test_n_way_choices_first_matching_branch_and_fallback(self):
        branches = [
            {
                "id": f"branch_{i}",
                "condition": f"option_{i}",
                "set_fact": f"selected_{i}",
            }
            for i in range(4)
        ]
        value = stage(
            "choice_gate",
            branches=branches,
            default_branch="branch_3",
            outcomes={f"branch_{i}": f"Route{i}" for i in range(4)},
        )
        phase = document(build_choice_phase, value)
        for initial, expected in [
            ({}, 3),
            ({"option_2": 1}, 2),
            ({"option_1": 1, "option_2": 1}, 1),
            ({"option_0": 1, "option_3": 1}, 0),
        ]:
            run = GraphRun(phase, facts=initial)
            self.assertEqual(run.outputs, [f"Route{expected}"])
            self.assertEqual(
                {key for key in run.facts if key.startswith("selected_")},
                {f"selected_{expected}"},
            )
        waiting = GraphRun(
            document(build_choice_phase, stage("choice_gate", branches=branches))
        )
        self.assertEqual(waiting.outputs, [])
        waiting.events("fact:option_2")
        self.assertEqual(waiting.facts["selected_2"], 1)

    def test_retained_objective_has_no_state_changes_but_activates_description(self):
        phase = document(
            build_investigation_phase,
            stage(
                "investigate_clues",
                clues=[{"id": "clue", "object_ref": "#clue"}],
                description_entry="quests/test/description",
                objective_lifecycle={"on_enter": "retain", "on_success": "retain"},
            ),
        )
        run = GraphRun(phase)
        run.events("#clue")
        paths = [
            item["realPath"]
            for node, _ in run.trace
            for item in objects(node)
            if item.get("$type") == "gameJournalPath"
        ]
        self.assertNotIn("quests/test/objective", paths)
        self.assertIn("quests/test/description", paths)

    def test_lifecycle_opt_in_preserves_legacy_ordered_full_investigation(self):
        clues = [{"id": f"clue_{i}", "object_ref": f"#clue_{i}"} for i in range(3)]
        run = GraphRun(
            document(
                build_investigation_phase,
                stage(
                    "investigate_clues",
                    clues=clues,
                    objective_lifecycle={"on_success": "retain"},
                ),
            )
        )
        run.events("#clue_2", "#clue_1")
        self.assertEqual(run.outputs, [])
        run.events("#clue_0")
        run.events("#clue_1")
        self.assertEqual(run.outputs, [])
        run.events("#clue_2")
        self.assertEqual(run.outputs, ["Out1"])

    def test_invalid_new_field_combinations_are_rejected(self):
        cases = [
            (
                validate_investigate_clues,
                {
                    "clues": [
                        {"id": "a", "object_ref": "#same"},
                        {"id": "b", "object_ref": "#same"},
                    ],
                    "required_count": 2,
                },
                "duplicate_clue_object",
            ),
            (
                validate_choice_gate,
                {
                    "gate_kind": "fact",
                    "branches": [
                        {"id": "a", "condition": "a", "set_fact": "selected_a"},
                        {"id": "b", "condition": "b", "set_fact": "selected_b"},
                    ],
                    "evaluation": "on_entry",
                },
                "invalid_choice_fallback",
            ),
            (
                validate_escort_npc,
                {"destinations": ["#a", "#b"], "route_mappins": ["quests/a"]},
                "invalid_route_mappins",
            ),
            (
                validate_defend_target,
                {"duration_seconds": float("nan")},
                "invalid_defense_duration",
            ),
            (
                validate_defend_target,
                {
                    "retry_checkpoint": True,
                    "block_on_failure": True,
                    "outcomes": {"failure": "Failure"},
                },
                "blocked_defense_failure_port",
            ),
        ]
        for validator, data, code in cases:
            diagnostics = []
            validator(data, "stage", "test", diagnostics)
            self.assertIn(code, {item.code for item in diagnostics})

    def test_legacy_templates_remain_default_and_explicit_templates_win(self):
        for kind, fields in [
            ("escort_npc", {"destinations": ["a", "b", "c"]}),
            ("choice_gate", {"branches": [{}, {}]}),
            ("defend_target", {}),
        ]:
            definition = STAGE_REGISTRY[kind]
            self.assertIsNone(definition.builder(fields))
            self.assertIsNotNone(definition.template(fields))
            extended = {**fields, "outcomes": {"success": "Out1"}}
            self.assertIsNotNone(definition.builder(extended))
            self.assertIsNone(definition.template(extended))
            self.assertEqual(
                definition.template({**extended, "phase_template": "custom"}), "custom"
            )
            diagnostics = []
            definition.validate(
                {
                    **fields,
                    "phase_template": "custom",
                    "actor_lifecycle": {"on_success": "retain"},
                },
                "stage",
                "block",
                diagnostics,
            )
            self.assertIn(
                "custom_template_lifecycle", {item.code for item in diagnostics}
            )

    def test_gqt003_compiles_complete_set_without_custom_graph_templates(self):
        artifacts = compiler.compile_manifest_artifacts(
            ROOT / "projects/test-quests/gqt003/gqt003_extract_and_hold.quest.json",
            ROOT / "generated/tests/gqt003.questphase.json",
            ROOT / "generated/tests/gqt003.questphase",
            child_root=ROOT / "generated/tests/children",
        )
        self.assertEqual(len(artifacts), 7)
        self.assertEqual(len({artifact.raw_path for artifact in artifacts}), 7)
        self.assertNotIn(
            "gqt003_escort_retain",
            json.dumps([artifact.document for artifact in artifacts]),
        )
        children = {
            artifact.stage_id: artifact.document
            for artifact in artifacts
            if artifact.stage_id
        }
        escort = GraphRun(children["escort_patch"])
        for index in (1, 2, 3):
            escort.events(f"#gqt003_03_tr_escort_gate_0{index}")
        self.assertEqual(escort.outputs, ["Out1"])
        self.assertEqual(escort.actions("AIClearRoleCommandParams"), [])
        defense = GraphRun(children["defend_patch"])
        defense.events("#gqt003_04_com_attackers")
        defense.events("timer")
        self.assertEqual(defense.outputs, ["Out1"])
        self.assertEqual(len(defense.actions("AIClearRoleCommandParams")), 1)

    def test_retry_fixture_checkpoints_live_actor_and_never_progresses_on_failure(self):
        artifacts = compiler.compile_manifest_artifacts(
            ROOT / "quests/examples/timed-defense-retry.quest.json",
            ROOT / "generated/tests/retry.questphase.json",
            ROOT / "generated/tests/retry.questphase",
            child_root=ROOT / "generated/tests/retry-children",
        )
        checkpoint = next(
            item
            for item in objects(artifacts[0].document)
            if item.get("$type") == "questCheckpointNodeDefinition"
        )
        self.assertEqual(checkpoint["retryOnFailure"], 1)
        self.assertEqual(checkpoint["debugString"], "gqt003_live_follower_hold")
        defense = next(
            item.document for item in artifacts if item.stage_id == "defend_patch"
        )
        run = GraphRun(defense)
        run.events("defeated")
        run.events("#gqt003_04_com_attackers", "timer")
        self.assertEqual(run.outputs, [])
        self.assertEqual(run.facts["gqt003_patch_lost"], 1)
        self.assertNotIn("gqt003_hold_complete", run.facts)
        self.assertEqual(len(run.actions("AIClearRoleCommandParams")), 1)
        # A restored native checkpoint starts with a live actor and fresh gates;
        # structural model does not claim to simulate REDengine persistence.
        restored = GraphRun(defense)
        restored.events("#gqt003_04_com_attackers")
        restored.events("timer")
        self.assertEqual(restored.outputs, ["Out1"])


if __name__ == "__main__":
    unittest.main()
