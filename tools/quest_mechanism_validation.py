"""Strict shape and composition checks for research-derived owned blocks."""

import json
from functools import lru_cache
from pathlib import Path

from jsonschema import Draft202012Validator

from quest_types import Diagnostic


def action_resource(action):
    kind = action["kind"]
    if kind in {"objective", "mappin", "message"}:
        return f"{kind}:{action['path']}"
    if kind == "community":
        return f"actor:{action['community']}:{action['entry']}"
    if kind == "weather_reset":
        return f"weather:{action['source']}"
    if kind == "prefab_variant":
        return f"prefab:{action['prefab']}:{action['variant']}"
    return None


def scope_claims(stage):
    """Actual bound resources, for the linker's concurrent-owner check."""
    actions = [
        *stage.data.get("setup", []),
        *stage.data.get("restore", []),
        *stage.data.get("retire", []),
    ]
    for effects in stage.data.get("effects", {}).values():
        actions.extend(effects)
    claims = {resource for action in actions if (resource := action_resource(action))}
    if stage.type == "investigate_reactions":
        claims.update(
            f"mappin:{clue['mappin']}"
            for clue in stage.data["clues"]
            if clue.get("mappin")
        )
    return claims


@lru_cache
def validator(kind):
    schema = json.loads(Path(__file__).with_name("quest-schema-v1.json").read_text())
    branch = next(
        branch
        for branch in schema["$defs"]["stage"]["oneOf"]
        if branch["allOf"][1]["properties"]["type"]["const"] == kind
    )
    return Draft202012Validator({"$defs": schema["$defs"], **branch})


def validate_mechanism(data, context, stage_id, diagnostics):
    def error(message):
        diagnostics.append(
            Diagnostic(
                "error", "invalid_owned_block", f"{context}: {message}", stage_id
            )
        )

    errors = list(validator(data["type"]).iter_errors(data))
    for problem in errors:
        error(f"{'.'.join(map(str, problem.path))}: {problem.message}")
    if errors:
        return
    kind = data["type"]
    if any(
        field in data
        for field in ("phase_template", "template_bindings", "objective_lifecycle")
    ):
        error(
            "owned blocks generate their lifecycle; templates and objective_lifecycle are not supported"
        )
    if data.get("inputs", {"start": "In1"}).keys() != {"start"}:
        error("owned blocks accept exactly one start input")
    outcomes = set(data.get("outcomes", {"success": "Out1"}))
    expected = {"success"}
    if kind == "owned_scope":
        notifications = data.get("notifications", {})
        if set(notifications) - set(data["child"]["exits"]):
            error("notification aliases must be declared child exits")
        expected = set(data["child"]["exits"]) - set(notifications)
        if not expected:
            error("a scope needs a terminal child exit")
    elif kind in {"acquire_or_use", "access_routes", "resolve_and_report"}:
        child = data["report"] if kind == "resolve_and_report" else data["application"]
        expected = set(child["exits"])
        if "success" not in expected:
            error("application/report needs a success exit")
    elif kind == "contact_fallback":
        expected = {"connected", "fallback"}
        if "connected" not in data["call"]["exits"] or len(data["call"]["exits"]) < 2:
            error("call needs connected and at least one fallback exit")
    elif kind == "entitlement_reconcile":
        expected = {"owned", "unowned"}
        if ("entitled_fact" in data) == ("vehicle_record" in data):
            error(
                "choose exactly one vehicle_record predicate or entitled_fact adapter"
            )
        if not data["retire"]:
            error("entitlement reconciliation requires an explicit offer retirement")
        if any(
            action["kind"] not in {"objective", "message", "mappin", "fact"}
            or action.get("state", "Inactive") != "Inactive"
            for action in data["retire"]
        ):
            error(
                "offer retirement permits only inactive journal/mappin states and facts"
            )
    if data.get("cancellation_fact"):
        if "cancelled" in expected:
            error("cancelled is owned by the scope, not the child")
        expected.add("cancelled")
    if outcomes != expected:
        error(f"outcomes must be exactly {sorted(expected)}")
    if set(data.get("effects", {})) - expected:
        error("effects refer to an undeclared outcome")
    if data.get("commit_fact") and "success" not in expected:
        error("commit_fact requires a success outcome")
    if kind == "access_routes":
        ids = [route["id"] for route in data["routes"]]
        if len(ids) != len(set(ids)):
            error("access route ids must be distinct")
        if any(set(route["exits"]) != {"success"} for route in data["routes"]):
            error("access attempts expose exactly one success outcome")
        if set(data.get("route_facts", {})) - set(ids):
            error("route_facts must refer to declared access routes")
    if kind in {"resolve_and_report", "observe_lethal"}:
        keys = [(target["community"], target["entry"]) for target in data["targets"]]
        if len(keys) != len(set(keys)):
            error("targets must be distinct")
        if kind == "resolve_and_report" and any(
            not any(t["resolution"].values()) for t in data["targets"]
        ):
            error("each target requires at least one explicit resolution state")
    if kind == "adaptive_timer" and bool(data.get("busy_fact")) != (
        "max_deferral_seconds" in data
    ):
        error("busy_fact and max_deferral_seconds must be supplied together")
    if kind == "investigate_reactions":
        clues = data["clues"]
        if data.get("required_count", len(clues)) > len(clues):
            error("required_count exceeds the number of clues")
        for key in ("id", "object_ref", "scan_fact", "completion_fact"):
            values = [clue[key] for clue in clues]
            if len(values) != len(set(values)):
                error(f"clue {key} bindings must be distinct")
        facts = [
            clue[key] for clue in clues for key in ("scan_fact", "completion_fact")
        ]
        if len(facts) != len(set(facts)):
            error("scan and reaction completion facts must be distinct")
        for clue in clues:
            if clue.get("reaction") and set(clue["reaction"]["exits"]) != {"success"}:
                error("each clue reaction exposes exactly one success exit")
    for field in ("child", "application", "report", "call"):
        if field in data:
            ports = list(data[field]["exits"].values())
            if len(ports) != len(set(ports)):
                error(f"{field} exit sockets must be distinct")
    # Restoration may acknowledge a child phase, but may never grant a reward.
    if any(action["kind"] == "item" for action in data.get("restore", [])):
        error(
            "restore cannot contain item grants; use success effects or reward_commit"
        )
    restored = {action_resource(action) for action in data.get("restore", [])}
    for action in data.get("setup", []):
        resource = action_resource(action)
        if resource and resource not in restored:
            error(f"setup acquires {resource} without a shared restore operation")
    if data.get("commit_fact") == data.get("cancellation_fact") and data.get(
        "commit_fact"
    ):
        error("commit_fact and cancellation_fact must be distinct")
    from quest_interfaces import bound_interfaces
    from quest_compiler import validate_depot_path
    from types import SimpleNamespace

    for resource, kind, _ in bound_interfaces(SimpleNamespace(data=data)):
        validate_depot_path(
            resource,
            field=f"{context}.{kind}",
            stage_id=stage_id,
            diagnostics=diagnostics,
        )
        if not resource.endswith(".questphase" if kind == "phase" else ".scene"):
            error(f"{kind} binding has the wrong resource extension: {resource}")
