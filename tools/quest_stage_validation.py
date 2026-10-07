"""Stage-specific semantic validation beyond the editor's structural schema."""

from __future__ import annotations

import math
import re
from pathlib import Path
from typing import Any

from quest_types import Diagnostic, ID_RE, require_string


def validate_acquire_item(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    if stage.get("source") not in {"inventory", "grant"}:
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_item_source",
                f"{context}.source must be inventory or grant",
                stage_id or None,
            )
        )
    quantity = stage.get("quantity", 1)
    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity < 1:
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_quantity",
                f"{context}.quantity must be a positive integer",
                stage_id or None,
            )
        )


def validate_phone_job_offer(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    hours = stage.get("delay_game_hours", 0)
    if (
        not isinstance(hours, int) or isinstance(hours, bool)
        or not 0 <= hours <= 2147483647
    ):
        diagnostics.append(Diagnostic(
            "error", "invalid_phone_game_delay",
            f"{context}.delay_game_hours must be an integer between 0 and 2147483647",
            stage_id or None,
        ))


def validate_time_gate(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    duration_fields = ("days", "hours", "minutes", "seconds")
    duration = []
    for field in duration_fields:
        value = stage.get(field, 0)
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_time_gate_duration",
                    f"{context}.{field} must be a non-negative integer",
                    stage_id or None,
                )
            )
        else:
            duration.append(value)
    if len(duration) == len(duration_fields) and not any(duration):
        diagnostics.append(
            Diagnostic(
                "error",
                "empty_time_gate",
                f"{context} must wait for a non-zero game-time duration",
                stage_id or None,
            )
        )


def validate_read_shard(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    file_index = stage.get("file_entry_index")
    if (
        not isinstance(file_index, int)
        or isinstance(file_index, bool)
        or file_index < 0
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_file_entry_index",
                f"{context}.file_entry_index must be a non-negative integer",
                stage_id or None,
            )
        )


def validate_reach_area(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    if not isinstance(stage.get("disable_previous_mappins", True), bool):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_disable_previous_mappins",
                f"{context}.disable_previous_mappins must be a boolean",
                stage_id or None,
            )
        )


def validate_investigate_clues(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    clues = stage.get("clues")
    clue_fields = {
        "id",
        "object_ref",
        "completion_fact",
        "grant_item",
        "grant_items",
        "journal_entry",
        "mappin",
    }
    if (
        not isinstance(clues, list)
        or not clues
        or not all(
            isinstance(item, dict)
            and set(item) <= clue_fields
            and isinstance(item.get("id"), str)
            and ID_RE.fullmatch(item["id"])
            and isinstance(item.get("object_ref"), str)
            and (
                "grant_items" not in item
                or (
                    isinstance(item["grant_items"], list)
                    and bool(item["grant_items"])
                    and all(
                        isinstance(value, str) and value.strip()
                        for value in item["grant_items"]
                    )
                    and len(set(item["grant_items"])) == len(item["grant_items"])
                )
            )
            for item in clues
        )
        or len({item["id"] for item in clues if isinstance(item, dict)}) != len(clues)
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_clues",
                f"{context}.clues must contain typed unique id/object_ref objects",
                stage_id or None,
            )
        )
    if isinstance(clues, list) and clues:
        required_count = stage.get("required_count", len(clues))
        if (
            not isinstance(required_count, int)
            or isinstance(required_count, bool)
            or not 1 <= required_count <= len(clues)
        ):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_required_count",
                    f"{context}.required_count must be between 1 and the clue count",
                    stage_id or None,
                )
            )

    if stage.get("scan_order", "ordered") not in {"ordered", "any"}:
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_scan_order",
                f"{context}.scan_order must be ordered or any",
                stage_id or None,
            )
        )
    if isinstance(clues, list):
        references = [
            item.get("object_ref") for item in clues if isinstance(item, dict)
        ]
        if all(isinstance(item, str) for item in references) and len(
            set(references)
        ) != len(references):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "duplicate_clue_object",
                    f"{context}.clues must reference distinct objects so one scan cannot satisfy multiple clues",
                    stage_id or None,
                )
            )


def validate_optional_condition(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    if stage.get("success_fact") == stage.get("failure_fact"):
        diagnostics.append(
            Diagnostic(
                "error",
                "duplicate_outcome_fact",
                f"{context}.success_fact and failure_fact must differ",
                stage_id or None,
            )
        )
    condition = stage.get("condition")
    if (
        not isinstance(condition, dict)
        or set(condition) != {"kind", "value"}
        or condition.get("kind")
        not in {"fact", "trigger", "detection", "alarm", "timer"}
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_optional_condition",
                f"{context}.condition must contain a supported kind and value",
                stage_id or None,
            )
        )
    if stage.get("evaluation") not in {"continuous", "at_exit"}:
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_evaluation",
                f"{context}.evaluation must be continuous or at_exit",
                stage_id or None,
            )
        )

    if (
        not isinstance(stage.get("phase_template"), str)
        and stage.get("evaluation") != "at_exit"
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "unsupported_condition_evaluation",
                f"{context} currently supports evaluation=at_exit",
                stage_id or None,
            )
        )


def validate_choice_gate(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    if "objective_lifecycle" in stage:
        diagnostics.append(
            Diagnostic(
                "error",
                "unsupported_choice_lifecycle",
                f"{context} choices do not own an objective",
                stage_id or None,
            )
        )
    choices = stage.get("branches")
    if (
        not isinstance(choices, list)
        or len(choices) < 2
        or not all(
            isinstance(item, dict)
            and set(item) == {"id", "condition", "set_fact"}
            and isinstance(item["id"], str)
            and ID_RE.fullmatch(item["id"])
            and isinstance(item["condition"], str)
            and item["condition"].strip()
            and isinstance(item["set_fact"], str)
            and item["set_fact"].strip()
            for item in choices
        )
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_gate_choices",
                f"{context}.branches must contain at least two id/condition/set_fact objects",
                stage_id or None,
            )
        )
    elif len({item["id"] for item in choices}) != len(choices) or len(
        {item["set_fact"] for item in choices}
    ) != len(choices):
        diagnostics.append(
            Diagnostic(
                "error",
                "duplicate_gate_choice",
                f"{context}.branches must use unique ids and outcome facts",
                stage_id or None,
            )
        )

    branches = stage.get("branches")
    if not isinstance(stage.get("phase_template"), str) and (
        stage.get("gate_kind") != "fact" or not isinstance(branches, list)
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "unsupported_choice_shape",
                f"{context} generated choices require fact branches",
                stage_id or None,
            )
        )
    fallback = stage.get("default_branch")
    if fallback is not None and (
        not isinstance(choices, list)
        or fallback
        not in [item.get("id") for item in choices if isinstance(item, dict)]
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_default_branch",
                f"{context}.default_branch must name an authored branch",
                stage_id or None,
            )
        )
    evaluation = stage.get("evaluation", "on_entry" if fallback else "wait")
    if evaluation not in {"on_entry", "wait"}:
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_choice_evaluation",
                f"{context}.evaluation must be on_entry or wait",
                stage_id or None,
            )
        )
    elif (evaluation == "on_entry") != (fallback is not None):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_choice_fallback",
                f"{context} on_entry evaluation requires a fallback; wait evaluation cannot use a fallback",
                stage_id or None,
            )
        )


def validate_interact_device(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    if "outcome_branches" in stage:
        branches = stage.get("outcome_branches")
        allowed_branch_fields = {
            "id",
            "condition",
            "set_fact",
            "add_items",
            "remove_items",
        }
        if (
            not isinstance(branches, list)
            or len(branches) != 2
            or not all(
                isinstance(item, dict)
                and set(item) <= allowed_branch_fields
                and {"id", "condition", "set_fact"} <= set(item)
                and isinstance(item["id"], str)
                and ID_RE.fullmatch(item["id"])
                and isinstance(item["condition"], str)
                and item["condition"].strip()
                and isinstance(item["set_fact"], str)
                and item["set_fact"].strip()
                and all(
                    isinstance(values, list)
                    and all(
                        isinstance(value, str) and value.strip() for value in values
                    )
                    for values in (
                        item.get("add_items", []),
                        item.get("remove_items", []),
                    )
                )
                for item in branches
            )
        ):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_interact_outcomes",
                    f"{context}.outcome_branches must contain exactly two typed fact branches",
                    stage_id or None,
                )
            )
        elif (
            len({item["id"] for item in branches}) != 2
            or len({item["condition"] for item in branches}) != 2
            or len({item["set_fact"] for item in branches}) != 2
        ):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "duplicate_interact_outcome",
                    f"{context}.outcome_branches must use unique ids, conditions, and facts",
                    stage_id or None,
                )
            )


def validate_hack_access_point(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    if "completion_function" in stage:
        for field in ("controller_class", "action", "completion_function"):
            require_string(stage, field, context=context, diagnostics=diagnostics)
        if "send_action" in stage and not isinstance(stage["send_action"], bool):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_hack_send_action",
                    f"{context}.send_action must be a boolean",
                    stage_id or None,
                )
            )


def validate_deliver_drop_point(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    if "item_branches" in stage:
        branches = stage.get("item_branches")
        if (
            not isinstance(branches, list)
            or len(branches) != 2
            or not all(
                isinstance(item, dict)
                and set(item) == {"id", "condition", "item"}
                and isinstance(item["id"], str)
                and ID_RE.fullmatch(item["id"])
                and isinstance(item["condition"], str)
                and item["condition"].strip()
                and isinstance(item["item"], str)
                and item["item"].strip()
                for item in branches
            )
        ):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_delivery_item_branches",
                    f"{context}.item_branches must contain exactly two id/condition/item branches",
                    stage_id or None,
                )
            )
        elif (
            len({item["id"] for item in branches}) != 2
            or len({item["condition"] for item in branches}) != 2
            or len({item["item"] for item in branches}) != 2
        ):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "duplicate_delivery_item_branch",
                    f"{context}.item_branches must use unique ids, conditions, and items",
                    stage_id or None,
                )
            )

    if not stage.get("item") and not stage.get("item_branches"):
        diagnostics.append(
            Diagnostic(
                "error",
                "missing_delivery_item",
                f"{context} requires item or item_branches",
                stage_id or None,
            )
        )


def validate_defend_target(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    validate_actor_lifecycle(stage, context, stage_id, diagnostics)
    if "duration_seconds" in stage:
        duration = stage["duration_seconds"]
        if (
            not isinstance(duration, (int, float))
            or isinstance(duration, bool)
            or not math.isfinite(duration)
            or duration < 0.001
        ):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_defense_duration",
                    f"{context}.duration_seconds must be finite and at least 0.001 seconds",
                    stage_id or None,
                )
            )
    attackers = stage.get("attackers")
    if attackers is not None:
        if (
            not isinstance(attackers, dict)
            or set(attackers) - {"community", "entries", "cleanup"}
            or not isinstance(attackers.get("community"), str)
            or not attackers["community"].strip()
            or not isinstance(attackers.get("cleanup", True), bool)
        ):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_defense_attackers",
                    f"{context}.attackers requires a community, entries, and optional boolean cleanup",
                    stage_id or None,
                )
            )
        else:
            entries = attackers.get("entries")
            if (
                not isinstance(entries, list)
                or not entries
                or not all(
                    isinstance(item, dict)
                    and set(item) <= {"entry", "target"}
                    and isinstance(item.get("entry"), str)
                    and item["entry"].strip()
                    and item.get("target", "player") in {"player", "protected"}
                    for item in entries
                )
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "invalid_defense_entries",
                        f"{context}.attackers.entries requires entry names and player/protected targets",
                        stage_id or None,
                    )
                )
            elif len({item["entry"] for item in entries}) != len(entries):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "duplicate_defense_attacker",
                        f"{context}.attackers.entries must be unique",
                        stage_id or None,
                    )
                )
    block_on_failure = stage.get("block_on_failure", False)
    if not isinstance(block_on_failure, bool):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_block_on_failure",
                f"{context}.block_on_failure must be a boolean",
                stage_id or None,
            )
        )
    elif block_on_failure and not stage.get("retry_checkpoint", False):
        diagnostics.append(
            Diagnostic(
                "error",
                "blocked_defense_without_retry",
                f"{context}.block_on_failure requires retry_checkpoint",
                stage_id or None,
            )
        )
    if block_on_failure and "failure" in stage.get("outcomes", {}):
        diagnostics.append(
            Diagnostic(
                "error",
                "blocked_defense_failure_port",
                f"{context}.block_on_failure cannot declare a failure output; checkpoint recovery resumes the attempt",
                stage_id or None,
            )
        )


def validate_combat_encounter(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    threat_settings = {"threat_function", "threat_duration_seconds"} & stage.keys()
    if threat_settings and (stage.get("phase_template") or not stage.get("entries")):
        diagnostics.append(
            Diagnostic(
                "error",
                "unsupported_combat_threat_settings",
                f"{context} threat settings require generated combat with explicit entries",
                stage_id or None,
            )
        )
    if (
        "threat_function" in stage
        and stage["threat_function"] != "questCombatNodeParams_ShootAt"
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_combat_threat_function",
                f"{context}.threat_function must be questCombatNodeParams_ShootAt",
                stage_id or None,
            )
        )
    if "threat_duration_seconds" in stage:
        duration = stage["threat_duration_seconds"]
        if (
            isinstance(duration, bool)
            or not isinstance(duration, (int, float))
            or not math.isfinite(duration)
            or duration < 0
        ):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_combat_threat_duration",
                    f"{context}.threat_duration_seconds must be finite and nonnegative",
                    stage_id or None,
                )
            )
    if stage.get("hostility") not in {"neutral_to_hostile", "already_hostile"}:
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_hostility",
                f"{context}.hostility is not supported",
                stage_id or None,
            )
        )
    completion = stage.get("completion")
    if completion not in {"all_defeated", "named_defeated", "fact"}:
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_combat_completion",
                f"{context}.completion is not supported",
                stage_id or None,
            )
        )
    using_builtin = not isinstance(stage.get("phase_template"), str)
    if using_builtin and completion != "all_defeated":
        diagnostics.append(
            Diagnostic(
                "error",
                "unsupported_combat_completion",
                f"{context} built-in template supports completion=all_defeated",
                stage_id or None,
            )
        )
    if using_builtin and stage.get("hostility") != "already_hostile":
        diagnostics.append(
            Diagnostic(
                "error",
                "unsupported_combat_variant",
                f"{context} currently supports hostility=already_hostile",
                stage_id or None,
            )
        )


def validate_cyberpsycho_encounter(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    for field in (
        "community",
        "activation_trigger",
        "arena_trigger",
        "alerted_path",
    ):
        value = stage.get(field)
        if value is not None and (
            not isinstance(value, str) or not value.startswith(("#", "$/"))
        ):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_cyberpsycho_node_ref",
                    f"{context}.{field} must be a NodeRef",
                    stage_id or None,
                )
            )
    alerted_spots = stage.get("alerted_spots", [])
    if not isinstance(alerted_spots, list) or any(
        not isinstance(value, str) or not value.startswith(("#", "$/"))
        for value in alerted_spots
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_cyberpsycho_alerted_spots",
                f"{context}.alerted_spots must be a list of NodeRefs",
                stage_id or None,
            )
        )
    boss_character = stage.get("boss_character")
    if (
        isinstance(boss_character, str)
        and re.fullmatch(
            r"[A-Za-z][A-Za-z0-9_]*\.[A-Za-z0-9_.]+",
            boss_character,
        )
        is None
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_cyberpsycho_character",
                f"{context}.boss_character must be a TweakDBID",
                stage_id or None,
            )
        )
    for field in ("activate",):
        if field in stage and not isinstance(stage[field], bool):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_cyberpsycho_boolean",
                    f"{context}.{field} must be a boolean",
                    stage_id or None,
                )
            )

    for field in ("activation_mode", "arena_mode"):
        value = stage.get(field)
        if value is not None and value not in {"Entered", "IsInside"}:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_cyberpsycho_trigger_mode",
                    f"{context}.{field} must be Entered or IsInside",
                    stage_id or None,
                )
            )

    for field in ("postfight_scene", "player_defeat_scene"):
        scene_flow = stage.get(field)
        if scene_flow is None:
            continue
        allowed_scene_fields = {"scene", "origin", "entry", "exit"}
        if field == "player_defeat_scene":
            allowed_scene_fields.update(
                {
                    "debug_fact",
                    "defeat_fact",
                    "health_percent",
                    "continuation_scene",
                    "aftermath_scene",
                    "completion_exits",
                    "completion_branches",
                }
            )
        if not isinstance(scene_flow, dict):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_cyberpsycho_scene_flow",
                    f"{context}.{field} must be an object",
                    stage_id or None,
                )
            )
            continue
        unknown_scene_fields = sorted(set(scene_flow) - allowed_scene_fields)
        if unknown_scene_fields:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "unknown_cyberpsycho_scene_flow_field",
                    f"{context}.{field} has unknown fields: "
                    + ", ".join(unknown_scene_fields),
                    stage_id or None,
                )
            )
        for scene_field in ("scene", "origin", "entry", "exit"):
            value = scene_flow.get(scene_field)
            if not isinstance(value, str) or not value:
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "invalid_cyberpsycho_scene_flow_field",
                        f"{context}.{field}.{scene_field} must be a non-empty string",
                        stage_id or None,
                    )
                )
        origin = scene_flow.get("origin")
        if isinstance(origin, str) and not origin.startswith(("#", "$/")):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_cyberpsycho_scene_origin",
                    f"{context}.{field}.origin must be a NodeRef",
                    stage_id or None,
                )
            )
        if field == "player_defeat_scene":
            for nested_field in ("continuation_scene", "aftermath_scene"):
                nested_flow = scene_flow.get(nested_field)
                if nested_flow is None:
                    continue
                if not isinstance(nested_flow, dict):
                    diagnostics.append(
                        Diagnostic(
                            "error",
                            "invalid_cyberpsycho_scene_flow",
                            f"{context}.{field}.{nested_field} must be an object",
                            stage_id or None,
                        )
                    )
                    continue
                unknown_nested_fields = sorted(
                    set(nested_flow) - {"scene", "origin", "entry", "exit"}
                )
                if unknown_nested_fields:
                    diagnostics.append(
                        Diagnostic(
                            "error",
                            "unknown_cyberpsycho_scene_flow_field",
                            f"{context}.{field}.{nested_field} has unknown fields: "
                            + ", ".join(unknown_nested_fields),
                            stage_id or None,
                        )
                    )
                for nested_scene_field in ("scene", "origin", "entry", "exit"):
                    nested_value = nested_flow.get(nested_scene_field)
                    if not isinstance(nested_value, str) or not nested_value:
                        diagnostics.append(
                            Diagnostic(
                                "error",
                                "invalid_cyberpsycho_scene_flow_field",
                                f"{context}.{field}.{nested_field}.{nested_scene_field} must be a non-empty string",
                                stage_id or None,
                            )
                        )
                nested_origin = nested_flow.get("origin")
                if isinstance(nested_origin, str) and not nested_origin.startswith(
                    ("#", "$/")
                ):
                    diagnostics.append(
                        Diagnostic(
                            "error",
                            "invalid_cyberpsycho_scene_origin",
                            f"{context}.{field}.{nested_field}.origin must be a NodeRef",
                            stage_id or None,
                        )
                    )
            for fact_field in ("debug_fact", "defeat_fact"):
                fact = scene_flow.get(fact_field)
                if isinstance(fact, str) and ID_RE.fullmatch(fact):
                    continue
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "invalid_cyberpsycho_player_defeat_fact",
                        f"{context}.{field}.{fact_field} must be a lowercase fact name",
                        stage_id or None,
                    )
                )
            health_percent = scene_flow.get("health_percent", 5)
            if (
                isinstance(health_percent, bool)
                or not isinstance(health_percent, (int, float))
                or not 1 <= health_percent <= 50
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "invalid_cyberpsycho_player_defeat_health_percent",
                        f"{context}.{field}.health_percent must be between 1 and 50",
                        stage_id or None,
                    )
                )
            completion_exits = scene_flow.get("completion_exits", [])
            if not isinstance(completion_exits, list) or not all(
                isinstance(exit_name, str) and exit_name
                for exit_name in completion_exits
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "invalid_cyberpsycho_completion_exits",
                        f"{context}.{field}.completion_exits must be a string array",
                        stage_id or None,
                    )
                )
            completion_branches = scene_flow.get("completion_branches", [])
            if not isinstance(completion_branches, list) or not all(
                isinstance(branch, dict)
                and set(branch) == {"exit", "set_fact"}
                and isinstance(branch["exit"], str)
                and branch["exit"]
                and isinstance(branch["set_fact"], str)
                and ID_RE.fullmatch(branch["set_fact"])
                for branch in completion_branches
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "invalid_cyberpsycho_completion_branches",
                        f"{context}.{field}.completion_branches must contain exit/set_fact objects",
                        stage_id or None,
                    )
                )

    reveal = stage.get("reveal")
    reveal_fields = {
        "trigger",
        "scan",
        "attacked_by_boss",
        "boss_hit_by_player",
        "boss_sees_player",
    }
    if not isinstance(reveal, dict):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_cyberpsycho_reveal",
                f"{context}.reveal must be an object",
                stage_id or None,
            )
        )
    else:
        unknown_reveal = sorted(set(reveal) - reveal_fields)
        if unknown_reveal:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "unknown_cyberpsycho_reveal_field",
                    f"{context}.reveal has unknown fields: "
                    + ", ".join(unknown_reveal),
                    stage_id or None,
                )
            )
        trigger = reveal.get("trigger")
        if trigger is not None and (
            not isinstance(trigger, str) or not trigger.startswith(("#", "$/"))
        ):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_cyberpsycho_reveal_trigger",
                    f"{context}.reveal.trigger must be a NodeRef",
                    stage_id or None,
                )
            )
        for field in reveal_fields - {"trigger"}:
            if field in reveal and not isinstance(reveal[field], bool):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "invalid_cyberpsycho_reveal_flag",
                        f"{context}.reveal.{field} must be a boolean",
                        stage_id or None,
                    )
                )
        if not (
            isinstance(trigger, str)
            or any(reveal.get(field) is True for field in reveal_fields - {"trigger"})
        ):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "empty_cyberpsycho_reveal",
                    f"{context}.reveal must enable at least one reveal route",
                    stage_id or None,
                )
            )

    resolution = stage.get("resolution")
    resolution_fields = {
        "allow_nonlethal",
        "spared_fact",
        "killed_fact",
    }
    if not isinstance(resolution, dict):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_cyberpsycho_resolution",
                f"{context}.resolution must be an object",
                stage_id or None,
            )
        )
    else:
        unknown_resolution = sorted(set(resolution) - resolution_fields)
        if unknown_resolution:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "unknown_cyberpsycho_resolution_field",
                    f"{context}.resolution has unknown fields: "
                    + ", ".join(unknown_resolution),
                    stage_id or None,
                )
            )
        if resolution.get("allow_nonlethal", True) is not True:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "cyberpsycho_nonlethal_required",
                    f"{context}.resolution.allow_nonlethal must be true",
                    stage_id or None,
                )
            )
        for field in ("spared_fact", "killed_fact"):
            value = resolution.get(field)
            if not isinstance(value, str) or not ID_RE.fullmatch(value):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "invalid_cyberpsycho_outcome_fact",
                        f"{context}.resolution.{field} must be a lowercase fact name",
                        stage_id or None,
                    )
                )
        if isinstance(resolution.get("spared_fact"), str) and resolution.get(
            "spared_fact"
        ) == resolution.get("killed_fact"):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "duplicate_cyberpsycho_outcome_fact",
                    f"{context}.resolution outcome facts must differ",
                    stage_id or None,
                )
            )

    cleanup = stage.get("cleanup")
    if cleanup is not None:
        cleanup_fields = {"trigger", "deactivate_community"}
        if not isinstance(cleanup, dict):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_cyberpsycho_cleanup",
                    f"{context}.cleanup must be an object",
                    stage_id or None,
                )
            )
        else:
            unknown_cleanup = sorted(set(cleanup) - cleanup_fields)
            if unknown_cleanup:
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "unknown_cyberpsycho_cleanup_field",
                        f"{context}.cleanup has unknown fields: "
                        + ", ".join(unknown_cleanup),
                        stage_id or None,
                    )
                )
            cleanup_trigger = cleanup.get("trigger")
            if cleanup_trigger is not None and (
                not isinstance(cleanup_trigger, str)
                or not cleanup_trigger.startswith(("#", "$/"))
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "invalid_cyberpsycho_cleanup_trigger",
                        f"{context}.cleanup.trigger must be a NodeRef",
                        stage_id or None,
                    )
                )
            if "deactivate_community" in cleanup and not isinstance(
                cleanup["deactivate_community"], bool
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "invalid_cyberpsycho_cleanup_flag",
                        f"{context}.cleanup.deactivate_community must be a boolean",
                        stage_id or None,
                    )
                )

    authoring = stage.get("authoring")
    if authoring is not None:
        authoring_fields = {"world_spec", "tweak_file"}
        if not isinstance(authoring, dict):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_cyberpsycho_authoring",
                    f"{context}.authoring must be an object",
                    stage_id or None,
                )
            )
        else:
            unknown_authoring = sorted(set(authoring) - authoring_fields)
            if unknown_authoring:
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "unknown_cyberpsycho_authoring_field",
                        f"{context}.authoring has unknown fields: "
                        + ", ".join(unknown_authoring),
                        stage_id or None,
                    )
                )
            if not authoring:
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "empty_cyberpsycho_authoring",
                        f"{context}.authoring must name at least one file",
                        stage_id or None,
                    )
                )
            for field in authoring_fields:
                value = authoring.get(field)
                if value is not None and (
                    not isinstance(value, str)
                    or not value.strip()
                    or Path(value).is_absolute()
                    or ".." in Path(value).parts
                ):
                    diagnostics.append(
                        Diagnostic(
                            "error",
                            "invalid_cyberpsycho_authoring_path",
                            f"{context}.authoring.{field} must be a "
                            "workspace-relative path",
                            stage_id or None,
                        )
                    )


def validate_braindance_analysis(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    for field in (
        "scene_origin",
        "player_anchor",
        "player_return",
    ):
        value = stage.get(field)
        if not isinstance(value, str) or not value.startswith(("#", "$/")):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_braindance_node_ref",
                    f"{context}.{field} must be a NodeRef",
                    stage_id or None,
                )
            )
    clue_facts = stage.get("clue_facts")
    if (
        not isinstance(clue_facts, list)
        or len(clue_facts) != 3
        or not all(
            isinstance(item, str) and ID_RE.fullmatch(item) for item in clue_facts
        )
        or len(set(clue_facts)) != 3
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_braindance_clue_facts",
                f"{context}.clue_facts must contain exactly three unique fact names",
                stage_id or None,
            )
        )


def validate_actor_lifecycle(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    policy = stage.get("actor_lifecycle", {})
    actions = {
        "on_enter": {"assign_follower", "retain"},
        "on_success": {"release", "retain"},
        "on_failure": {"release", "retain"},
        "on_cancelled": {"release", "retain"},
    }
    if not isinstance(policy, dict) or any(
        key not in actions or not isinstance(value, str) or value not in actions[key]
        for key, value in policy.items()
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_actor_lifecycle",
                f"{context}.actor_lifecycle must use assign_follower/retain on entry and release/retain on outcomes",
                stage_id or None,
            )
        )
    for field in ("cancellation_fact", "cancelled_fact"):
        if field in stage and (
            not isinstance(stage[field], str) or not ID_RE.fullmatch(stage[field])
        ):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_cancellation_fact",
                    f"{context}.{field} must be a fact name",
                    stage_id or None,
                )
            )


def validate_escort_npc(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    validate_actor_lifecycle(stage, context, stage_id, diagnostics)
    destinations = stage.get("destinations")
    if (
        not isinstance(destinations, list)
        or not destinations
        or not all(isinstance(item, str) and item.strip() for item in destinations)
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_destinations",
                f"{context}.destinations must be a non-empty string array",
                stage_id or None,
            )
        )
    route_mappins = stage.get("route_mappins")
    if route_mappins is not None and (
        not isinstance(route_mappins, list)
        or not all(isinstance(item, str) and item.strip() for item in route_mappins)
        or not isinstance(destinations, list)
        or len(route_mappins) != len(destinations)
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_route_mappins",
                f"{context}.route_mappins must supply one journal mappin per destination",
                stage_id or None,
            )
        )


def validate_phone_conversation(
    stage: dict[str, Any], context: str, stage_id: str, diagnostics: list[Diagnostic]
) -> None:
    messages = stage.get("messages")
    if (
        not isinstance(messages, list)
        or not all(isinstance(item, str) and item.strip() for item in messages)
        or (
            not messages
            and not stage.get("opening_branches")
            and not stage.get("conditional_message_groups")
        )
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_phone_messages",
                f"{context}.messages must be a string array and may be empty only when conditional messages exist",
                stage_id or None,
            )
        )
    choices = stage.get("choices")
    if (
        not isinstance(choices, list)
        or len(choices) < 2
        or not all(
            isinstance(item, dict)
            and {"choice", "reply"} <= set(item)
            and set(item) <= {"choice", "reply", "set_fact"}
            and all(
                isinstance(item[key], str) and item[key].strip()
                for key in ("choice", "reply")
            )
            and (
                "set_fact" not in item
                or (isinstance(item["set_fact"], str) and item["set_fact"].strip())
            )
            for item in choices
        )
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_phone_choices",
                f"{context}.choices must contain at least two choice/reply "
                "objects with an optional set_fact",
                stage_id or None,
            )
        )
    opening_branches = stage.get("opening_branches")
    if opening_branches is not None and (
        not isinstance(opening_branches, list)
        or len(opening_branches) < 2
        or not all(
            isinstance(item, dict)
            and set(item)
            in (
                {"condition", "messages"},
                {"condition", "unless", "messages"},
            )
            and isinstance(item["condition"], str)
            and item["condition"].strip()
            and (
                "unless" not in item
                or (isinstance(item["unless"], str) and item["unless"].strip())
            )
            and isinstance(item["messages"], list)
            and item["messages"]
            and all(
                isinstance(message, str) and message.strip()
                for message in item["messages"]
            )
            for item in opening_branches
        )
        or len({item["condition"] for item in opening_branches})
        != len(opening_branches)
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_phone_opening_branches",
                f"{context}.opening_branches must contain at least two "
                "unique fact conditions with non-empty message arrays",
                stage_id or None,
            )
        )
    conditional_groups = stage.get("conditional_message_groups", [])
    if (
        not isinstance(conditional_groups, list)
        or any(
            not isinstance(group, dict)
            or set(group) != {"id", "branches"}
            or not isinstance(group["id"], str)
            or not ID_RE.fullmatch(group["id"])
            or not isinstance(group["branches"], list)
            or len(group["branches"]) < 2
            or any(
                not isinstance(branch, dict)
                or set(branch) != {"condition", "messages"}
                or not isinstance(branch["condition"], str)
                or not branch["condition"].strip()
                or not isinstance(branch["messages"], list)
                or not branch["messages"]
                or any(
                    not isinstance(message, str) or not message.strip()
                    for message in branch["messages"]
                )
                for branch in group["branches"]
            )
            or len({branch["condition"] for branch in group["branches"]})
            != len(group["branches"])
            for group in conditional_groups
        )
        or len(
            {
                group["id"]
                for group in conditional_groups
                if isinstance(group, dict) and isinstance(group.get("id"), str)
            }
        )
        != len(conditional_groups)
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_phone_conditional_groups",
                f"{context}.conditional_message_groups must contain uniquely named branch groups",
                stage_id or None,
            )
        )
    postscripts = stage.get("postscript_messages", [])
    if not isinstance(postscripts, list) or any(
        not isinstance(message, str) or not message.strip() for message in postscripts
    ):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_phone_postscripts",
                f"{context}.postscript_messages must be a string array",
                stage_id or None,
            )
        )
    delay = stage.get("delay_seconds", 1)
    if not isinstance(delay, int) or isinstance(delay, bool) or delay < 0:
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_phone_delay",
                f"{context}.delay_seconds must be a non-negative integer",
                stage_id or None,
            )
        )


VALIDATORS = {
    "phone_job_offer": validate_phone_job_offer,
    "acquire_item": validate_acquire_item,
    "time_gate": validate_time_gate,
    "read_shard": validate_read_shard,
    "reach_area": validate_reach_area,
    "investigate_clues": validate_investigate_clues,
    "optional_condition": validate_optional_condition,
    "choice_gate": validate_choice_gate,
    "interact_device": validate_interact_device,
    "hack_access_point": validate_hack_access_point,
    "deliver_drop_point": validate_deliver_drop_point,
    "defend_target": validate_defend_target,
    "combat_encounter": validate_combat_encounter,
    "cyberpsycho_encounter": validate_cyberpsycho_encounter,
    "braindance_analysis": validate_braindance_analysis,
    "escort_npc": validate_escort_npc,
    "phone_conversation": validate_phone_conversation,
}
