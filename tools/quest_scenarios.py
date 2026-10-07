#!/usr/bin/env python3
"""Preview and exercise a quest plan's structural signal-routing contract.

This model does not execute REDengine conditions, scene cuts, world events,
facts, parallel branches, or the game's save system.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import html
import json
from pathlib import Path
from typing import Any, Mapping

from artifact_io import atomic_write_json


class ScenarioError(ValueError):
    pass


def load_plan(path: Path, *, manifest: bool = False) -> dict:
    if not manifest:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    from quest_compiler import build_plan, load_spec

    spec, diagnostics = load_spec(path)
    errors = [item.message for item in diagnostics if item.level == "error"]
    if spec is None or errors:
        raise ScenarioError("Invalid quest manifest: " + "; ".join(errors))
    return build_plan(spec, diagnostics)


def routing_contract(plan: Mapping[str, Any]) -> dict:
    if not isinstance(plan, Mapping) or not isinstance(plan.get("stages"), list):
        raise ScenarioError("Plan requires a stages array")
    if plan.get("parallel_groups"):
        raise ScenarioError(
            "Parallel groups are not supported by the sequential scenario model"
        )
    if any(item.get("level") == "error" for item in plan.get("diagnostics", [])):
        raise ScenarioError("Plan has compiler errors")
    stages = plan["stages"]
    identifiers = [stage.get("id") for stage in stages if isinstance(stage, dict)]
    if (
        not identifiers
        or len(identifiers) != len(stages)
        or any(
            not isinstance(name, str) or not name or name == "$end"
            for name in identifiers
        )
        or len(set(identifiers)) != len(identifiers)
    ):
        raise ScenarioError("Plan stage IDs must be unique, nonempty strings")
    entry = plan.get("entry_stage", identifiers[0])
    if entry not in identifiers:
        raise ScenarioError(f"Unknown entry stage: {entry}")
    transitions = plan.get("transitions")
    if not isinstance(transitions, dict) or set(transitions) != set(identifiers):
        raise ScenarioError("Plan requires a transition map for every stage")
    for stage, routes in transitions.items():
        if not isinstance(routes, dict) or not routes:
            raise ScenarioError(f"Stage {stage} requires named outcomes")
        for outcome, target in routes.items():
            if not isinstance(outcome, str) or not outcome:
                raise ScenarioError(f"Invalid outcome in {stage}")
            if not isinstance(target, str) or target not in {*identifiers, "$end"}:
                raise ScenarioError(f"Unknown target for {stage}.{outcome}: {target}")
    ports = {}
    for stage in stages:
        declared = stage.get("outcomes", stage.get("data", {}).get("outcomes"))
        if declared is not None and (
            not isinstance(declared, dict)
            or set(declared) != set(transitions[stage["id"]])
        ):
            raise ScenarioError(
                f"Transitions disagree with declared outcomes: {stage['id']}"
            )
        ports[stage["id"]] = {"inputs": stage.get("inputs", {}), "outcomes": declared}
    return {
        "schema_version": 1,
        "entry_stage": entry,
        "stages": identifiers,
        "ports": ports,
        "transitions": deepcopy(transitions),
        "contracts": deepcopy(plan.get("contracts", {})),
    }


class ScenarioModel:
    """One active stage with explicit, model-only event deduplication policy."""

    def __init__(self, plan: Mapping[str, Any]):
        self.contract = routing_contract(plan)
        self.fingerprint = hashlib.sha256(
            json.dumps(self.contract, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        self.active_stage: str | None = self.contract["entry_stage"]
        self.terminal_outcome: str | None = None
        self.processed_events: dict[str, dict] = {}

    def state(self) -> dict:
        return {
            "active_stage": self.active_stage,
            "terminal_outcome": self.terminal_outcome,
        }

    def signal(self, event: Mapping[str, Any]) -> dict:
        if not isinstance(event, Mapping) or set(event) != {
            "event_id",
            "stage",
            "outcome",
        }:
            raise ScenarioError("Events require exactly event_id, stage, and outcome")
        if any(not isinstance(event[name], str) or not event[name] for name in event):
            raise ScenarioError("Event fields must be nonempty strings")
        event = dict(event)
        identifier = event["event_id"]
        if identifier in self.processed_events:
            if self.processed_events[identifier] != event:
                raise ScenarioError(
                    f"Event ID reused with different content: {identifier}"
                )
            return {"result": "duplicate", **self.state()}
        stage = event["stage"]
        outcome = event["outcome"]
        if stage not in self.contract["transitions"]:
            raise ScenarioError(f"Unknown event stage: {stage}")
        if outcome not in self.contract["transitions"][stage]:
            raise ScenarioError(f"Unknown outcome: {stage}.{outcome}")
        self.processed_events[identifier] = event
        if self.active_stage is None:
            result = "terminal"
        elif stage != self.active_stage:
            result = "inactive"
        else:
            target = self.contract["transitions"][stage][outcome]
            self.active_stage = None if target == "$end" else target
            if target == "$end":
                self.terminal_outcome = outcome
            result = "advanced"
        return {"result": result, **self.state()}

    def snapshot(self) -> dict:
        return {
            "schema_version": 1,
            "contract_sha256": self.fingerprint,
            **self.state(),
            "processed_events": deepcopy(list(self.processed_events.values())),
        }

    def restore(self, snapshot: dict) -> None:
        if (
            not isinstance(snapshot, dict)
            or snapshot.get("schema_version") != 1
            or snapshot.get("contract_sha256") != self.fingerprint
        ):
            raise ScenarioError("Snapshot does not match this routing contract")
        active = snapshot.get("active_stage")
        outcome = snapshot.get("terminal_outcome")
        events = snapshot.get("processed_events")
        if (
            (active is not None and active not in self.contract["stages"])
            or (active is None and (not isinstance(outcome, str) or not outcome))
            or (active is not None and outcome is not None)
            or not isinstance(events, list)
        ):
            raise ScenarioError("Invalid snapshot state")
        # Replay the journal to validate both state and receipt identity before replacing state.
        replay = ScenarioModel(
            {
                "stages": [
                    {"id": name, **self.contract["ports"][name]}
                    for name in self.contract["stages"]
                ],
                **{
                    key: self.contract[key]
                    for key in ("entry_stage", "transitions", "contracts")
                },
            }
        )
        for event in events:
            if (
                not isinstance(event, dict)
                or not isinstance(event.get("event_id"), str)
                or event["event_id"] in replay.processed_events
            ):
                raise ScenarioError("Invalid snapshot event receipt")
            replay.signal(event)
        if replay.state() != {"active_stage": active, "terminal_outcome": outcome}:
            raise ScenarioError("Snapshot state disagrees with its event journal")
        self.active_stage = active
        self.terminal_outcome = outcome
        self.processed_events = deepcopy(replay.processed_events)


def check_expectation(actual: dict, expected: Any) -> None:
    if not isinstance(expected, dict) or not expected or set(expected) - set(actual):
        raise ScenarioError("Expectation must name supported state/result fields")
    differences = {
        key: {"expected": value, "actual": actual[key]}
        for key, value in expected.items()
        if actual[key] != value
    }
    if differences:
        raise ScenarioError(
            "Expectation failed: " + json.dumps(differences, sort_keys=True)
        )


def run_scenarios(plan: dict, suite: dict) -> dict:
    model = ScenarioModel(plan)
    if (
        not isinstance(suite, dict)
        or suite.get("schema_version") != 1
        or not isinstance(suite.get("scenarios"), list)
        or not suite["scenarios"]
    ):
        raise ScenarioError(
            "Scenario suite requires schema_version 1 and nonempty scenarios"
        )
    reports = []
    identifiers: set[str] = set()
    for scenario in suite["scenarios"]:
        if (
            not isinstance(scenario, dict)
            or not isinstance(scenario.get("id"), str)
            or not scenario["id"]
            or scenario["id"] in identifiers
        ):
            raise ScenarioError("Scenario IDs must be unique, nonempty strings")
        identifiers.add(scenario["id"])
        model = ScenarioModel(plan)
        checkpoints: dict[str, dict] = {}
        trace: list[dict] = []
        error = None
        try:
            if not isinstance(scenario.get("steps"), list) or not scenario["steps"]:
                raise ScenarioError("Scenario requires nonempty steps")
            for index, step in enumerate(scenario["steps"]):
                if (
                    not isinstance(step, dict)
                    or len(set(step) & {"event", "save", "load"}) != 1
                    or set(step) - {"event", "save", "load", "expect"}
                ):
                    raise ScenarioError("Step requires one event/save/load operation")
                if "event" in step:
                    result = model.signal(step["event"])
                else:
                    operation = "save" if "save" in step else "load"
                    name = step[operation]
                    if not isinstance(name, str) or not name:
                        raise ScenarioError("Checkpoint names must be nonempty strings")
                    if operation == "save":
                        if name in checkpoints:
                            raise ScenarioError(f"Checkpoint already exists: {name}")
                        checkpoints[name] = model.snapshot()
                    else:
                        if name not in checkpoints:
                            raise ScenarioError(f"Unknown checkpoint: {name}")
                        model.restore(checkpoints[name])
                    result = {"result": operation, **model.state()}
                trace.append({"step": index, **result})
                if "expect" in step:
                    check_expectation(result, step["expect"])
            check_expectation(model.state(), scenario.get("expect"))
        except ScenarioError as exc:
            error = str(exc)
        reports.append(
            {
                "id": scenario["id"],
                "passed": error is None,
                "error": error,
                "trace": trace,
                "final_state": model.state(),
            }
        )
    return {
        "schema_version": 1,
        "scope": "Structural sequential signal-routing model; no game, condition, scene, fact, or save-system execution.",
        "runtime_verified": False,
        "contract_sha256": model.fingerprint,
        "passed": all(report["passed"] for report in reports),
        "scenarios": reports,
    }


def graph_markdown(plan: dict) -> str:
    contract = routing_contract(plan)
    names = {name: f"stage_{index}" for index, name in enumerate(contract["stages"])}
    names["$end"] = "quest_end"
    lines = [
        "# Quest routing preview",
        "",
        "Structural plan only. Conditions, scene behavior, and game save/load require runtime checks.",
        "",
        "```mermaid",
        "flowchart TD",
        '    entry(["Entry"])',
        '    quest_end(["End"])',
    ]
    for stage in plan["stages"]:
        label = html.escape(
            f"{stage['id']}: {stage.get('type', 'stage')}", quote=True
        ).replace("\n", " ")
        lines.append(f'    {names[stage["id"]]}["{label}"]')
    lines.append(f"    entry --> {names[contract['entry_stage']]}")
    for stage, outcomes in contract["transitions"].items():
        for outcome, target in outcomes.items():
            label = (
                html.escape(outcome, quote=True)
                .replace("\n", " ")
                .replace("|", "&#124;")
            )
            lines.append(f'    {names[stage]} -->|"{label}"| {names[target]}')
    return "\n".join([*lines, "```", ""])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--manifest", type=Path)
    source.add_argument("--plan", type=Path)
    parser.add_argument("--scenarios", type=Path)
    parser.add_argument("--output", type=Path, help="Write the scenario report")
    parser.add_argument(
        "--graph", type=Path, help="Write a Markdown Mermaid routing preview"
    )
    args = parser.parse_args()
    if not args.scenarios and not args.graph:
        parser.error("Provide --scenarios and/or --graph")
    try:
        plan = load_plan(args.manifest or args.plan, manifest=bool(args.manifest))
        routing_contract(plan)
        if args.graph:
            graph = graph_markdown(plan)
            args.graph.parent.mkdir(parents=True, exist_ok=True)
            args.graph.write_text(graph, encoding="utf-8")
        if args.scenarios:
            result = run_scenarios(
                plan, json.loads(args.scenarios.read_text(encoding="utf-8-sig"))
            )
            if args.output:
                atomic_write_json(args.output, result)
            print(json.dumps(result, indent=2))
            return 0 if result["passed"] else 1
        return 0
    except (OSError, ValueError) as exc:
        parser.exit(2, f"error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
