"""Validation of generated replacements without weakening explicit templates."""

from functools import lru_cache
import json
from pathlib import Path

from jsonschema import Draft202012Validator

from quest_types import Diagnostic


@lru_cache
def validator(kind):
    schema = json.loads(Path(__file__).with_name("quest-schema-v1.json").read_text())
    branch = next(
        b
        for b in schema["$defs"]["stage"]["oneOf"]
        if b["allOf"][1]["properties"]["type"]["const"] == kind
    )
    return Draft202012Validator({"$defs": schema["$defs"], **branch})


def validate_generated(stage, context, identifier, diagnostics):
    if stage.get("phase_template") or "template_bindings" in stage:
        return

    def error(message):
        diagnostics.append(
            Diagnostic(
                "error", "invalid_generated_block", f"{context}: {message}", identifier
            )
        )

    problems = list(validator(stage["type"]).iter_errors(stage))
    for problem in problems:
        error(f"{'.'.join(map(str, problem.path))}: {problem.message}")
    if problems:
        return
    kind = stage["type"]
    if stage.get("inputs", {"start": "In1"}).keys() != {"start"}:
        error("generated replacement accepts exactly one start input")
    if set(stage.get("outcomes", {"success": "Out1"})) != {"success"}:
        error(
            "this block exposes one success port; use owned_scope for cancellation and explicit outcome composition"
        )
    if (
        kind == "optional_condition"
        and stage.get("condition", {}).get("kind") != "fact"
    ):
        error(
            "generated optional_condition requires a fact; other condition kinds need an explicit template"
        )
    policy = stage.get("objective_lifecycle", {})
    supported = {"on_enter", "on_success"} | (
        {"on_failure"} if kind == "stealth_monitor" else set()
    )
    if (
        kind not in {"escort_npc", "defend_target", "choice_gate"}
        and set(policy) - supported
    ):
        error("unsupported objective lifecycle transition for this block")
    if kind == "carry_npc" and "placement_slot" in stage:
        error(
            "placement_slot needs an explicit custom template; generated carrying observes delivery without dropping the actor"
        )
    if kind == "meet_contact":
        for key in ("setup_trigger", "scene_origin", "accepted_fact"):
            if not stage.get(key):
                diagnostics.append(
                    Diagnostic(
                        "warning" if stage.get("status") == "planned" else "error",
                        "missing_generated_binding",
                        f"{context}: generated meeting requires explicit {key}",
                        identifier,
                    )
                )
        if stage.get("defer_policy") == "rearm" and not stage.get("rearm_trigger"):
            error("rearm deferral requires rearm_trigger")
        if stage.get("accept_exit", "job_accept") == stage.get("defer_exit", "end"):
            error("accept and defer exits must differ")
    if kind == "ride_with_contact":
        passengers = stage.get("additional_passengers", [])
        if not isinstance(passengers, list) or not all(
            isinstance(p, dict) and all(k in p for k in ("community", "entry", "slot"))
            for p in passengers
        ):
            return  # Shape diagnostics already explain malformed passengers.
        actors = [
            (stage.get("contact_community"), stage.get("contact_entry")),
            *[(p["community"], p["entry"]) for p in passengers],
        ]
        slots = [
            stage.get("contact_slot", "seat_front_right"),
            *[p["slot"] for p in passengers],
        ]
        if len(actors) != len(set(actors)) or len(slots) != len(set(slots)):
            error("passengers require distinct actors and seat slots")
        if (
            stage.get("player_role", "Driver")
            == stage.get("contact_role", "Passenger")
            == "Driver"
        ):
            error("player and contact cannot both require the driver role")
