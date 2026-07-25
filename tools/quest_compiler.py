#!/usr/bin/env python3
"""Validate and compile typed Ghostline quest manifests."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from generate_cache_phase import (  # noqa: E402
    GraphNode,
    JsonObject,
    PhaseGraphBuilder,
    cname,
    entity_reference,
    fact_node,
    input_node,
    journal_entry_node,
    journal_path,
    mappin_node,
    node_ref,
    objective_node,
    output_node,
    realtime_delay_node,
    trigger_condition_node,
    local_player_reference,
    tweakdbid,
)
from generate_delivery_phase import (  # noqa: E402
    fact_condition_node,
    inventory_condition_node,
    journal_choice_succeeded_node,
    journal_entry_visited_node,
    logical_xor_node,
    reward_node,
)


SCHEMA_VERSION = 1
SUPPORTED_STAGE_TYPES = {
    "phone_job_offer",
    "meet_contact",
    "hack_access_point",
    "deliver_drop_point",
    "phone_conversation",
    "reach_area",
    "interact_device",
    "acquire_item",
    "combat_encounter",
    "leave_area",
    "read_shard",
    "investigate_clues",
    "optional_condition",
    "choice_gate",
    "escort_npc",
    "carry_npc",
    "deliver_vehicle",
    "time_gate",
    "read_terminal_document",
    "stealth_monitor",
    "plant_item",
    "defend_target",
    "release_or_rescue_npc",
    "enter_vehicle",
    "ride_with_contact",
    "drive_to",
    "steal_vehicle",
    "vehicle_cleanup",
}
DIRECT_STAGE_TYPES = {
    "phone_job_offer",
    "phone_conversation",
    "reach_area",
    "acquire_item",
    "leave_area",
    "read_shard",
    "investigate_clues",
    "interact_device",
    "combat_encounter",
    "time_gate",
    "read_terminal_document",
}
TEMPLATE_REQUIRED_STAGE_TYPES = {
    "optional_condition",
    "choice_gate",
    "escort_npc",
    "carry_npc",
    "deliver_vehicle",
    "stealth_monitor",
    "plant_item",
    "defend_target",
    "release_or_rescue_npc",
    "enter_vehicle",
    "ride_with_contact",
    "drive_to",
    "steal_vehicle",
    "vehicle_cleanup",
}

BUILTIN_TEMPLATE_RESOURCES = {
    stage_type: rf"mod\ghostline\quest_blocks\templates\{stage_type}.questphase"
    for stage_type in TEMPLATE_REQUIRED_STAGE_TYPES
}

BUILTIN_UNSUPPORTED_FIELDS = {
    "optional_condition": {"description_entry"},
    "choice_gate": {"default_branch"},
    "escort_npc": {
        "description_entry",
        "failure_fact",
        "allow_combat_interrupt",
    },
    "carry_npc": {"description_entry", "placement_slot", "completion_fact"},
    "deliver_vehicle": {
        "description_entry",
        "mappin",
        "require_player_exit",
        "completion_fact",
    },
}

STAGE_IMPLEMENTATION_MODE = {
    **{stage_type: "generated" for stage_type in DIRECT_STAGE_TYPES},
    **{stage_type: "template" for stage_type in TEMPLATE_REQUIRED_STAGE_TYPES},
    "meet_contact": "template",
    "hack_access_point": "template",
    "deliver_drop_point": "template",
}
STAGE_REQUIRED_FIELDS = {
    "phone_job_offer": {
        "contact",
        "message",
        "choice_group",
        "accept_choice",
        "start_fact",
        "accepted_fact",
    },
    "meet_contact": {
        "contact",
        "scene",
        "community",
        "objective",
        "description_entry",
        "mappin",
    },
    "hack_access_point": {"device", "success_fact"},
    "deliver_drop_point": {"item", "drop_point", "deposit_fact"},
    "phone_conversation": {"contact", "thread", "choice_group", "final_message"},
    "reach_area": {"trigger", "objective", "description_entry", "mappin"},
    "interact_device": {
        "device", "controller_class", "action", "completion_function",
    },
    "acquire_item": {"item", "source"},
    "combat_encounter": {"community", "hostility", "completion"},
    "leave_area": {"trigger", "objective", "description_entry"},
    "read_shard": {"item", "journal_entry"},
    "investigate_clues": {"objective", "description_entry"},
    "optional_condition": {
        "objective", "success_fact", "failure_fact", "evaluation",
    },
    "choice_gate": {"gate_kind"},
    "escort_npc": {"community", "entry", "objective", "completion_fact"},
    "carry_npc": {"community", "entry", "destination", "objective"},
    "deliver_vehicle": {"vehicle", "destination", "objective"},
    "time_gate": set(),
    "read_terminal_document": {
        "computer", "completion_fact", "objective",
    },
    "stealth_monitor": {
        "objective", "failure_fact", "success_fact", "stop_fact",
    },
    "plant_item": {
        "item", "device", "controller_class", "action",
        "completion_function", "completion_fact", "objective",
    },
    "defend_target": {
        "community", "entry", "completion_fact", "failure_fact", "objective",
    },
    "release_or_rescue_npc": {
        "community", "entry", "device", "controller_class", "action",
        "completion_function", "completion_fact", "objective",
    },
    "enter_vehicle": {
        "vehicle_community", "vehicle_entry", "objective", "mappin",
    },
    "ride_with_contact": {
        "vehicle_community", "vehicle_entry", "contact_community",
        "contact_entry", "objective",
    },
    "drive_to": {
        "vehicle_community", "vehicle_entry", "destination",
        "completion_fact", "objective", "mappin",
    },
    "steal_vehicle": {
        "vehicle_community", "vehicle_entry", "objective", "mappin",
    },
    "vehicle_cleanup": {"player_vehicle_record", "completion_fact"},
}
TOP_LEVEL_FIELDS = {
    "schema_version",
    "id",
    "title",
    "description",
    "phase_prefabs",
    "debug_fact",
    "stages",
}
COMMON_STAGE_FIELDS = {
    "id",
    "type",
    "status",
    "phase_resource",
    "phase_template",
    "inherit_phase_prefabs",
    "template_bindings",
    "required_assets",
    "notes",
}
STAGE_TYPE_FIELDS = {
    "phone_job_offer": {
        "contact", "message", "choice_group", "accept_choice", "start_fact",
        "accepted_fact", "delay_seconds",
    },
    "meet_contact": {
        "contact", "scene", "community", "appearance", "objective",
        "description_entry", "mappin",
    },
    "hack_access_point": {
        "device", "success_fact", "guard_community", "grants",
    },
    "deliver_drop_point": {"item", "drop_point", "deposit_fact"},
    "phone_conversation": {
        "contact", "thread", "choice_group", "messages", "choices",
        "opening_branches", "final_message", "completion_fact", "complete_quest",
        "delay_seconds", "objective", "description_entry", "reward",
    },
    "reach_area": {
        "trigger", "objective", "description_entry", "mappin",
        "start_fact", "disable_previous_mappins",
    },
    "interact_device": {
        "device", "controller_class", "action", "completion_function",
        "objective", "description_entry", "mappin", "success_fact",
        "send_action",
    },
    "acquire_item": {
        "item", "source", "quantity", "objective", "description_entry", "mappin",
        "acquisition_fact",
    },
    "combat_encounter": {
        "community", "entries", "activate", "hostility", "completion",
        "nonlethal_allowed", "completion_fact", "cleanup_on_exit",
        "objective", "description_entry", "trigger",
    },
    "leave_area": {
        "trigger", "objective", "description_entry", "mappin",
        "completion_fact", "cleanup_community",
    },
    "read_shard": {
        "item", "journal_entry", "file_entry_index", "activate_entry",
        "objective", "description_entry", "acquisition_fact",
        "presentation_delay_seconds", "completion_fact",
    },
    "investigate_clues": {
        "clues", "required_count", "objective", "description_entry",
        "completion_fact",
    },
    "optional_condition": {
        "objective", "description_entry", "condition", "success_fact",
        "failure_fact", "evaluation",
    },
    "choice_gate": {
        "gate_kind", "branches", "default_branch", "join",
    },
    "escort_npc": {
        "community", "entry", "destinations", "objective", "description_entry",
        "failure_fact", "allow_combat_interrupt", "completion_fact",
    },
    "carry_npc": {
        "community", "entry", "destination", "objective", "description_entry",
        "placement_slot", "completion_fact",
    },
    "deliver_vehicle": {
        "vehicle", "destination", "objective", "description_entry", "mappin",
        "require_player_exit", "completion_fact",
    },
    "time_gate": {
        "days", "hours", "minutes", "seconds", "completion_fact",
    },
    "read_terminal_document": {
        "computer", "scene", "output_socket", "document_entry",
        "completion_fact", "objective", "description_entry",
    },
    "stealth_monitor": {
        "objective", "description_entry", "failure_fact", "success_fact",
        "stop_fact",
    },
    "plant_item": {
        "item", "device", "controller_class", "action",
        "completion_function", "completion_fact", "objective",
        "description_entry", "consume_item",
    },
    "defend_target": {
        "community", "entry", "completion_fact", "failure_fact", "objective",
        "description_entry",
    },
    "release_or_rescue_npc": {
        "community", "entry", "device", "controller_class", "action",
        "completion_function", "completion_fact", "objective",
        "description_entry",
    },
    "enter_vehicle": {
        "vehicle_community", "vehicle_entry", "objective", "mappin",
        "description_entry",
    },
    "ride_with_contact": {
        "vehicle_community", "vehicle_entry", "contact_community",
        "contact_entry", "objective",
        "description_entry",
    },
    "drive_to": {
        "vehicle_community", "vehicle_entry", "destination",
        "completion_fact", "objective", "mappin", "description_entry",
    },
    "steal_vehicle": {
        "vehicle_community", "vehicle_entry", "objective", "mappin",
        "description_entry",
    },
    "vehicle_cleanup": {"player_vehicle_record", "completion_fact"},
}
ID_RE = re.compile(r"^[a-z][a-z0-9_]*$")
DEPOT_RE = re.compile(r"^(?:base|ep1|mod)\\.+$")


class QuestSpecError(ValueError):
    pass


@dataclass(frozen=True)
class Diagnostic:
    level: str
    code: str
    message: str
    stage: str | None = None

    def as_dict(self) -> dict[str, Any]:
        result: dict[str, Any] = {
            "level": self.level,
            "code": self.code,
            "message": self.message,
        }
        if self.stage is not None:
            result["stage"] = self.stage
        return result


@dataclass(frozen=True)
class CompiledStage:
    index: int
    id: str
    type: str
    status: str
    phase_resource: str
    data: dict[str, Any]

    @property
    def node_id(self) -> int:
        return 10 + self.index


@dataclass(frozen=True)
class QuestSpec:
    path: Path
    id: str
    title: str
    description: str
    phase_prefabs: tuple[str, ...]
    debug_fact: str | None
    stages: tuple[CompiledStage, ...]


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise QuestSpecError(f"Cannot read quest manifest {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise QuestSpecError("Quest manifest root must be an object")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def require_string(
    value: dict[str, Any], key: str, *, context: str, diagnostics: list[Diagnostic]
) -> str:
    result = value.get(key)
    if not isinstance(result, str) or not result.strip():
        diagnostics.append(
            Diagnostic("error", "invalid_string", f"{context}.{key} must be a non-empty string")
        )
        return ""
    return result


def resource_paths(depot_path: str) -> tuple[Path, Path]:
    relative = Path(*depot_path.split("\\"))
    return ROOT / "source" / "raw" / Path(f"{relative}.json"), ROOT / "source" / "archive" / relative


def validate_depot_path(
    depot_path: Any,
    *,
    field: str,
    stage_id: str,
    diagnostics: list[Diagnostic],
) -> str:
    if not isinstance(depot_path, str) or not DEPOT_RE.fullmatch(depot_path):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_depot_path",
                f"{field} must be an explicit base\\, ep1\\, or mod\\ depot path",
                stage_id,
            )
        )
        return ""
    return depot_path


def load_spec(path: Path) -> tuple[QuestSpec | None, list[Diagnostic]]:
    diagnostics: list[Diagnostic] = []
    raw = read_json(path)

    unknown = sorted(set(raw) - TOP_LEVEL_FIELDS)
    for field in unknown:
        diagnostics.append(
            Diagnostic("error", "unknown_field", f"Unknown quest field: {field}")
        )

    if raw.get("schema_version") != SCHEMA_VERSION:
        diagnostics.append(
            Diagnostic(
                "error",
                "schema_version",
                f"schema_version must be {SCHEMA_VERSION}",
            )
        )

    quest_id = require_string(raw, "id", context="quest", diagnostics=diagnostics)
    if quest_id and not ID_RE.fullmatch(quest_id):
        diagnostics.append(
            Diagnostic("error", "invalid_id", f"Invalid quest id: {quest_id}")
        )
    title = require_string(raw, "title", context="quest", diagnostics=diagnostics)
    description = str(raw.get("description", ""))
    debug_fact_value = raw.get("debug_fact")
    debug_fact: str | None = None
    if debug_fact_value is not None:
        if not isinstance(debug_fact_value, str) or not ID_RE.fullmatch(
            debug_fact_value
        ):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_debug_fact",
                    "debug_fact must be a lowercase fact name",
                )
            )
        else:
            debug_fact = debug_fact_value

    prefabs_value = raw.get("phase_prefabs", [])
    phase_prefabs: list[str] = []
    if not isinstance(prefabs_value, list):
        diagnostics.append(
            Diagnostic("error", "invalid_phase_prefabs", "phase_prefabs must be an array")
        )
    else:
        for index, value in enumerate(prefabs_value):
            if not isinstance(value, str) or not value.startswith("#"):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "invalid_phase_prefab",
                        f"phase_prefabs[{index}] must be a shorthand NodeRef beginning with #",
                    )
                )
            elif value in phase_prefabs:
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "duplicate_phase_prefab",
                        f"Duplicate phase prefab: {value}",
                    )
                )
            else:
                phase_prefabs.append(value)

    stages_value = raw.get("stages")
    stages: list[CompiledStage] = []
    seen_ids: set[str] = set()
    if not isinstance(stages_value, list) or not stages_value:
        diagnostics.append(
            Diagnostic("error", "invalid_stages", "stages must be a non-empty array")
        )
        stages_value = []

    for index, stage in enumerate(stages_value):
        context = f"stages[{index}]"
        if not isinstance(stage, dict):
            diagnostics.append(
                Diagnostic("error", "invalid_stage", f"{context} must be an object")
            )
            continue
        stage_id = require_string(stage, "id", context=context, diagnostics=diagnostics)
        stage_type = require_string(stage, "type", context=context, diagnostics=diagnostics)
        status = stage.get("status", "ready")
        phase_resource = validate_depot_path(
            stage.get("phase_resource"),
            field=f"{context}.phase_resource",
            stage_id=stage_id,
            diagnostics=diagnostics,
        )

        allowed_fields = COMMON_STAGE_FIELDS | STAGE_TYPE_FIELDS.get(stage_type, set())
        for field in sorted(set(stage) - allowed_fields):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "unknown_stage_field",
                    f"Unknown field for {stage_id or context}: {field}",
                    stage_id or None,
                )
            )
        if stage_id:
            if not ID_RE.fullmatch(stage_id):
                diagnostics.append(
                    Diagnostic("error", "invalid_stage_id", f"Invalid stage id: {stage_id}", stage_id)
                )
            if stage_id in seen_ids:
                diagnostics.append(
                    Diagnostic("error", "duplicate_stage_id", f"Duplicate stage id: {stage_id}", stage_id)
                )
            seen_ids.add(stage_id)
        if stage_type not in SUPPORTED_STAGE_TYPES:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "unsupported_stage_type",
                    f"Unsupported stage type: {stage_type}",
                    stage_id or None,
                )
            )
        if status not in {"ready", "planned"}:
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_stage_status",
                    "status must be ready or planned",
                    stage_id or None,
                )
            )
        for field in sorted(STAGE_REQUIRED_FIELDS.get(stage_type, set())):
            require_string(stage, field, context=context, diagnostics=diagnostics)

        if (
            stage_type in TEMPLATE_REQUIRED_STAGE_TYPES
            and not isinstance(stage.get("phase_template"), str)
        ):
            unsupported = sorted(
                BUILTIN_UNSUPPORTED_FIELDS.get(stage_type, set()) & set(stage)
            )
            if unsupported:
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "unsupported_builtin_fields",
                        f"{context} fields require an explicit custom template: "
                        + ", ".join(unsupported),
                        stage_id or None,
                    )
                )

        if stage_type == "acquire_item":
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

        if stage_type == "time_gate":
            duration_fields = ("days", "hours", "minutes", "seconds")
            duration = []
            for field in duration_fields:
                value = stage.get(field, 0)
                if (
                    not isinstance(value, int)
                    or isinstance(value, bool)
                    or value < 0
                ):
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

        if stage_type == "read_shard":
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

        if stage_type == "reach_area" and not isinstance(
            stage.get("disable_previous_mappins", True), bool
        ):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_disable_previous_mappins",
                    f"{context}.disable_previous_mappins must be a boolean",
                    stage_id or None,
                )
            )

        if stage_type == "investigate_clues":
            clues = stage.get("clues")
            if (
                not isinstance(clues, list)
                or not clues
                or not all(
                    isinstance(item, dict)
                    and isinstance(item.get("id"), str)
                    and ID_RE.fullmatch(item["id"])
                    and isinstance(item.get("object_ref"), str)
                    for item in clues
                )
                or len({item["id"] for item in clues if isinstance(item, dict)}) != len(clues)
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "invalid_clues",
                        f"{context}.clues must contain unique id/object_ref objects",
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

        if stage_type == "optional_condition":
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

        if stage_type == "choice_gate":
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
            elif (
                len({item["id"] for item in choices}) != len(choices)
                or len({item["set_fact"] for item in choices}) != len(choices)
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "duplicate_gate_choice",
                        f"{context}.branches must use unique ids and outcome facts",
                        stage_id or None,
                    )
                )

        if stage_type == "combat_encounter":
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
        if stage_type == "escort_npc":
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
            elif (
                not isinstance(stage.get("phase_template"), str)
                and len(destinations) != 3
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "unsupported_destination_count",
                        f"{context}.destinations currently requires exactly three route gates",
                        stage_id or None,
                    )
                )

        if stage_type == "investigate_clues":
            clues = stage.get("clues")
            if (
                not isinstance(stage.get("phase_template"), str)
                and isinstance(clues, list)
                and stage.get("required_count", len(clues)) != len(clues)
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "unsupported_clue_threshold",
                        f"{context} generated flow currently requires all authored clues; "
                        "use a custom phase_template for a partial threshold",
                        stage_id or None,
                    )
                )

        if stage_type == "optional_condition":
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

        if stage_type == "choice_gate":
            branches = stage.get("branches")
            if (
                not isinstance(stage.get("phase_template"), str)
                and (
                    stage.get("gate_kind") != "fact"
                    or not isinstance(branches, list)
                    or len(branches) != 2
                )
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "unsupported_choice_shape",
                        f"{context} currently supports exactly two fact branches",
                        stage_id or None,
                    )
                )

        if stage_type == "phone_conversation":
            messages = stage.get("messages")
            if (
                not isinstance(messages, list)
                or not messages
                or not all(isinstance(item, str) and item.strip() for item in messages)
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "invalid_phone_messages",
                        f"{context}.messages must be a non-empty string array",
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
                        or (
                            isinstance(item["set_fact"], str)
                            and item["set_fact"].strip()
                        )
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
                    and set(item) == {"condition", "messages"}
                    and isinstance(item["condition"], str)
                    and item["condition"].strip()
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

        for field in ("scene",):
            if field in stage:
                validate_depot_path(
                    stage[field],
                    field=f"{context}.{field}",
                    stage_id=stage_id,
                    diagnostics=diagnostics,
                )
        if "phase_template" in stage:
            validate_depot_path(
                stage["phase_template"],
                field=f"{context}.phase_template",
                stage_id=stage_id,
                diagnostics=diagnostics,
            )
        if "template_bindings" in stage:
            bindings = stage["template_bindings"]
            if not isinstance(bindings, dict) or not all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in bindings.items()
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "invalid_template_bindings",
                        "template_bindings must map strings to strings",
                        stage_id or None,
                    )
                )
        required_assets = stage.get("required_assets", [])
        if not isinstance(required_assets, list):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_required_assets",
                    "required_assets must be an array",
                    stage_id or None,
                )
            )
        else:
            for asset_index, asset in enumerate(required_assets):
                validate_depot_path(
                    asset,
                    field=f"{context}.required_assets[{asset_index}]",
                    stage_id=stage_id,
                    diagnostics=diagnostics,
                )

        stages.append(
            CompiledStage(
                index=index,
                id=stage_id,
                type=stage_type,
                status=str(status),
                phase_resource=phase_resource,
                data=dict(stage),
            )
        )

    if diagnostics and any(item.level == "error" for item in diagnostics):
        return None, diagnostics
    return (
        QuestSpec(
            path=path.resolve(),
            id=quest_id,
            title=title,
            description=description,
            phase_prefabs=tuple(phase_prefabs),
            debug_fact=debug_fact,
            stages=tuple(stages),
        ),
        diagnostics,
    )


def audit_resources(spec: QuestSpec) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    for stage in spec.stages:
        resources = []
        template = stage_template_resource(stage)
        if template is not None:
            resources.append(template)
        elif stage.type not in DIRECT_STAGE_TYPES:
            resources.append(stage.phase_resource)
        if isinstance(stage.data.get("scene"), str):
            resources.append(stage.data["scene"])
        resources.extend(
            asset
            for asset in stage.data.get("required_assets", [])
            if isinstance(asset, str)
        )
        for depot_path in resources:
            raw_path, archive_path = resource_paths(depot_path)
            if not raw_path.is_file() and not archive_path.is_file():
                diagnostics.append(
                    Diagnostic(
                        "warning" if stage.status == "planned" else "error",
                        "missing_resource",
                        f"No raw or packed resource found for {depot_path}",
                        stage.id,
                    )
                )
    return diagnostics


def replace_template_scalars(
    value: Any, bindings: dict[str, str], counts: dict[str, int]
) -> Any:
    if isinstance(value, dict):
        return {
            key: replace_template_scalars(child, bindings, counts)
            for key, child in value.items()
        }
    if isinstance(value, list):
        return [replace_template_scalars(child, bindings, counts) for child in value]
    if isinstance(value, str) and value in bindings:
        counts[value] += 1
        return bindings[value]
    return value


def validate_handle_graph(value: Any, *, context: str) -> None:
    """Reject duplicate handles and dangling HandleRefId values before CR2W import."""
    handle_ids: list[str] = []
    handle_refs: list[str] = []

    def walk(child: Any) -> None:
        if isinstance(child, dict):
            if "HandleId" in child:
                handle_id = str(child["HandleId"])
                handle_ids.append(handle_id)
            if "HandleRefId" in child:
                handle_ref = str(child["HandleRefId"])
                handle_refs.append(handle_ref)
            for nested in child.values():
                walk(nested)
        elif isinstance(child, list):
            for nested in child:
                walk(nested)

    walk(value)
    duplicates = sorted(
        handle for handle in set(handle_ids) if handle_ids.count(handle) > 1
    )
    if duplicates:
        raise QuestSpecError(
            f"{context} contains duplicate HandleId values: " + ", ".join(duplicates)
        )
    unresolved = sorted(set(handle_refs) - set(handle_ids))
    if unresolved:
        raise QuestSpecError(
            f"{context} contains unresolved HandleRefId values: "
            + ", ".join(unresolved)
        )


def validate_no_forward_handle_refs(value: Any, *, context: str) -> None:
    """Reject forward refs in generated JSON; WolvenKit's importer is order-sensitive."""
    defined: set[str] = set()
    forward_refs: list[str] = []

    def walk(child: Any) -> None:
        if isinstance(child, dict):
            if "HandleRefId" in child:
                handle_ref = str(child["HandleRefId"])
                if handle_ref not in defined:
                    forward_refs.append(handle_ref)
            if "HandleId" in child:
                defined.add(str(child["HandleId"]))
            for nested in child.values():
                walk(nested)
        elif isinstance(child, list):
            for nested in child:
                walk(nested)

    walk(value)
    if forward_refs:
        raise QuestSpecError(
            f"{context} contains forward HandleRefId values that WolvenKit "
            "cannot deserialize: " + ", ".join(sorted(set(forward_refs)))
        )


def scalar_strings(value: Any) -> set[str]:
    result: set[str] = set()
    if isinstance(value, dict):
        for child in value.values():
            result.update(scalar_strings(child))
    elif isinstance(value, list):
        for child in value:
            result.update(scalar_strings(child))
    elif isinstance(value, str):
        result.add(value)
    return result


def validate_stage_contract(stage: CompiledStage, phase: JsonObject) -> None:
    """Ensure typed runtime identifiers are actually represented by the child phase."""
    expected: list[tuple[str, str]] = []
    if stage.type == "meet_contact":
        expected.extend(
            (field, stage.data[field]) for field in ("contact", "scene", "community")
        )
    elif stage.type == "hack_access_point":
        expected.extend(
            (field, stage.data[field]) for field in ("device", "success_fact")
        )
        if isinstance(stage.data.get("guard_community"), str):
            expected.append(("guard_community", stage.data["guard_community"]))
        expected.extend(("grants", item) for item in stage.data.get("grants", []))
    elif stage.type == "deliver_drop_point":
        expected.extend(
            (field, stage.data[field])
            for field in ("item", "drop_point", "deposit_fact")
        )
    elif stage.type == "phone_conversation":
        expected.extend(
            ("choices.set_fact", choice["set_fact"])
            for choice in stage.data.get("choices", [])
            if isinstance(choice.get("set_fact"), str)
        )
        for opening in stage.data.get("opening_branches", []):
            expected.append(("opening_branches.condition", opening["condition"]))
            expected.extend(
                ("opening_branches.messages", message)
                for message in opening["messages"]
            )
    elif stage.type == "reach_area":
        expected.extend(
            (field, stage.data[field])
            for field in ("trigger", "objective", "description_entry", "mappin")
        )
    elif stage.type == "interact_device":
        expected.extend(
            (field, stage.data[field])
            for field in ("device", "controller_class", "completion_function")
        )
        if stage.data.get("send_action", True):
            expected.append(("action", stage.data["action"]))
    elif stage.type == "acquire_item":
        expected.append(("item", stage.data["item"]))
    elif stage.type == "combat_encounter":
        expected.append(("community", stage.data["community"]))
        expected.extend(("entries", item) for item in stage.data.get("entries", []))
        if isinstance(stage.data.get("trigger"), str):
            expected.append(("trigger", stage.data["trigger"]))
    elif stage.type == "leave_area":
        expected.extend(
            (field, stage.data[field]) for field in ("trigger", "objective")
        )
        if isinstance(stage.data.get("cleanup_community"), str):
            expected.append(
                ("cleanup_community", stage.data["cleanup_community"])
            )
    elif stage.type == "read_shard":
        if stage.data.get("acquisition_fact"):
            expected.append(("acquisition_fact", stage.data["acquisition_fact"]))
        else:
            expected.append(("item", stage.data["item"]))
        if stage.data.get("activate_entry", False):
            expected.append(("journal_entry", stage.data["journal_entry"]))
    elif stage.type == "investigate_clues":
        for clue in stage.data.get("clues", []):
            expected.append(("clues", clue["object_ref"]))
            for field in (
                "completion_fact", "grant_item", "journal_entry", "mappin"
            ):
                if isinstance(clue.get(field), str):
                    expected.append((f"clues.{field}", clue[field]))
    elif stage.type == "optional_condition":
        expected.extend(
            (field, stage.data[field])
            for field in ("success_fact", "failure_fact")
        )
        condition_value = stage.data.get("condition", {}).get("value")
        if isinstance(condition_value, str):
            expected.append(("condition.value", condition_value))
    elif stage.type == "choice_gate":
        for branch in stage.data.get("branches", []):
            expected.extend(
                (
                    ("branches.condition", branch["condition"]),
                    ("branches.set_fact", branch["set_fact"]),
                )
            )
    elif stage.type == "escort_npc":
        expected.extend(
            (field, stage.data[field])
            for field in ("community", "entry", "objective", "completion_fact")
        )
        expected.extend(("destinations", item) for item in stage.data["destinations"])
    elif stage.type == "carry_npc":
        expected.extend(
            (field, stage.data[field])
            for field in ("community", "entry", "destination", "objective")
        )
    elif stage.type == "deliver_vehicle":
        expected.extend(
            (field, stage.data[field])
            for field in ("vehicle", "destination", "objective")
        )
    elif stage.type == "time_gate":
        if isinstance(stage.data.get("completion_fact"), str):
            expected.append(("completion_fact", stage.data["completion_fact"]))
    elif stage.type == "read_terminal_document":
        expected.extend(
            (field, stage.data[field])
            for field in ("objective", "completion_fact")
        )
        if isinstance(stage.data.get("document_entry"), str):
            expected.append(("document_entry", stage.data["document_entry"]))
    elif stage.type == "stealth_monitor":
        expected.extend(
            (field, stage.data[field])
            for field in (
                "objective", "failure_fact", "success_fact", "stop_fact"
            )
        )
    elif stage.type == "plant_item":
        expected.extend(
            (field, stage.data[field])
            for field in (
                "item", "device", "controller_class", "action",
                "completion_function", "completion_fact", "objective",
            )
        )
    elif stage.type == "defend_target":
        expected.extend(
            (field, stage.data[field])
            for field in (
                "community", "entry", "completion_fact",
                "failure_fact", "objective",
            )
        )
    elif stage.type == "release_or_rescue_npc":
        expected.extend(
            (field, stage.data[field])
            for field in (
                "community", "entry", "device", "controller_class",
                "action", "completion_function", "completion_fact", "objective",
            )
        )
    elif stage.type in {"enter_vehicle", "steal_vehicle"}:
        expected.extend(
            (field, stage.data[field])
            for field in ("vehicle_community", "vehicle_entry", "objective", "mappin")
        )
    elif stage.type == "ride_with_contact":
        expected.extend(
            (field, stage.data[field])
            for field in (
                "vehicle_community", "vehicle_entry", "contact_community",
                "contact_entry", "objective",
            )
        )
    elif stage.type == "drive_to":
        expected.extend(
            (field, stage.data[field])
            for field in (
                "vehicle_community", "vehicle_entry", "destination",
                "completion_fact", "objective", "mappin",
            )
        )
    elif stage.type == "vehicle_cleanup":
        expected.append(("completion_fact", stage.data["completion_fact"]))

    if stage.type in SUPPORTED_STAGE_TYPES - {
        "phone_job_offer",
        "meet_contact",
        "hack_access_point",
        "deliver_drop_point",
        "phone_conversation",
    }:
        for field in (
            "description_entry",
            "mappin",
            "completion_fact",
            "acquisition_fact",
            "success_fact",
            "failure_fact",
        ):
            if (
                isinstance(stage.data.get(field), str)
                and (field, stage.data[field]) not in expected
            ):
                expected.append((field, stage.data[field]))

    values = scalar_strings(phase)
    missing = [f"{field}={value}" for field, value in expected if value not in values]
    if missing:
        raise QuestSpecError(
            f"Stage {stage.id} child phase does not implement typed fields: "
            + ", ".join(missing)
        )


def stage_template_resource(stage: CompiledStage) -> str | None:
    explicit = stage.data.get("phase_template")
    if isinstance(explicit, str):
        return explicit
    return BUILTIN_TEMPLATE_RESOURCES.get(stage.type)


def builtin_template_bindings(stage: CompiledStage) -> dict[str, str]:
    if stage.type == "interact_device":
        return {
            "{{device}}": stage.data["device"],
            "{{controller_class}}": stage.data["controller_class"],
            "{{action}}": stage.data["action"],
            "{{completion_function}}": stage.data["completion_function"],
        }
    if stage.type == "combat_encounter":
        return {"{{community}}": stage.data["community"]}
    if stage.type == "investigate_clues":
        return {
            "{{objective}}": stage.data["objective"],
            "{{description_entry}}": stage.data["description_entry"],
            "{{clue_object_ref}}": stage.data["clues"][0]["object_ref"],
        }
    if stage.type == "optional_condition":
        return {
            "{{objective}}": stage.data["objective"],
            "{{condition_fact}}": stage.data["condition"]["value"],
            "{{success_fact}}": stage.data["success_fact"],
            "{{failure_fact}}": stage.data["failure_fact"],
        }
    if stage.type == "choice_gate":
        first, second = stage.data["branches"]
        return {
            "{{branch_a_condition}}": first["condition"],
            "{{branch_a_set_fact}}": first["set_fact"],
            "{{branch_b_condition}}": second["condition"],
            "{{branch_b_set_fact}}": second["set_fact"],
        }
    if stage.type == "escort_npc":
        return {
            "{{community}}": stage.data["community"],
            "{{entry}}": stage.data["entry"],
            "{{destination_1}}": stage.data["destinations"][0],
            "{{destination_2}}": stage.data["destinations"][1],
            "{{destination_3}}": stage.data["destinations"][2],
            "{{objective}}": stage.data["objective"],
            "{{completion_fact}}": stage.data["completion_fact"],
        }
    if stage.type == "carry_npc":
        return {
            "{{community}}": stage.data["community"],
            "{{entry}}": stage.data["entry"],
            "{{destination}}": stage.data["destination"],
            "{{objective}}": stage.data["objective"],
        }
    if stage.type == "deliver_vehicle":
        return {
            "{{vehicle}}": stage.data["vehicle"],
            "{{destination}}": stage.data["destination"],
            "{{objective}}": stage.data["objective"],
        }
    if stage.type == "stealth_monitor":
        return {
            "{{objective}}": stage.data["objective"],
            "{{failure_fact}}": stage.data["failure_fact"],
            "{{success_fact}}": stage.data["success_fact"],
            "{{stop_fact}}": stage.data["stop_fact"],
        }
    if stage.type == "plant_item":
        return {
            "{{objective}}": stage.data["objective"],
            "Items.GhostlineTemplateItem": stage.data["item"],
            "{{device}}": stage.data["device"],
            "{{controller_class}}": stage.data["controller_class"],
            "{{action}}": stage.data["action"],
            "{{completion_function}}": stage.data["completion_function"],
            "{{completion_fact}}": stage.data["completion_fact"],
        }
    if stage.type == "defend_target":
        return {
            "{{objective}}": stage.data["objective"],
            "{{community}}": stage.data["community"],
            "{{entry}}": stage.data["entry"],
            "{{completion_fact}}": stage.data["completion_fact"],
            "{{failure_fact}}": stage.data["failure_fact"],
        }
    if stage.type == "release_or_rescue_npc":
        return {
            "{{objective}}": stage.data["objective"],
            "{{community}}": stage.data["community"],
            "{{entry}}": stage.data["entry"],
            "{{device}}": stage.data["device"],
            "{{controller_class}}": stage.data["controller_class"],
            "{{action}}": stage.data["action"],
            "{{completion_function}}": stage.data["completion_function"],
            "{{completion_fact}}": stage.data["completion_fact"],
        }
    if stage.type in {"enter_vehicle", "steal_vehicle"}:
        return {
            "{{objective}}": stage.data["objective"],
            "{{vehicle_community}}": stage.data["vehicle_community"],
            "{{vehicle_entry}}": stage.data["vehicle_entry"],
            "{{mappin}}": stage.data["mappin"],
        }
    if stage.type == "ride_with_contact":
        return {
            "{{objective}}": stage.data["objective"],
            "{{vehicle_community}}": stage.data["vehicle_community"],
            "{{vehicle_entry}}": stage.data["vehicle_entry"],
            "{{contact_community}}": stage.data["contact_community"],
            "{{contact_entry}}": stage.data["contact_entry"],
        }
    if stage.type == "drive_to":
        return {
            "{{objective}}": stage.data["objective"],
            "{{vehicle_community}}": stage.data["vehicle_community"],
            "{{vehicle_entry}}": stage.data["vehicle_entry"],
            "{{destination_1}}": stage.data["destination"],
            "{{completion_fact}}": stage.data["completion_fact"],
            "{{mappin}}": stage.data["mappin"],
        }
    if stage.type == "vehicle_cleanup":
        return {
            "{{completion_fact}}": stage.data["completion_fact"],
        }
    return {}


def instantiate_stage_phase(stage: CompiledStage, archive_target: Path) -> JsonObject:
    template_resource = stage_template_resource(stage)
    if template_resource is None:
        raise QuestSpecError(f"Stage {stage.id} does not declare phase_template")
    raw_template, packed_template = resource_paths(template_resource)
    if not raw_template.is_file():
        raise QuestSpecError(
            f"Stage {stage.id} needs raw template {raw_template}; packed-only templates cannot be rewritten"
        )
    bindings_value = stage.data.get("template_bindings")
    if bindings_value is None:
        bindings_value = builtin_template_bindings(stage)
    if not isinstance(bindings_value, dict) or not all(
        isinstance(key, str) and isinstance(value, str)
        for key, value in bindings_value.items()
    ):
        raise QuestSpecError(
            f"Stage {stage.id}.template_bindings must map strings to strings"
        )
    template = read_json(raw_template)
    counts = {key: 0 for key in bindings_value}
    result = replace_template_scalars(template, dict(bindings_value), counts)
    unused = sorted(key for key, count in counts.items() if count == 0)
    if unused:
        raise QuestSpecError(
            f"Stage {stage.id} has template bindings not present in {template_resource}: "
            + ", ".join(unused)
        )
    result["Header"]["ArchiveFileName"] = str(archive_target.resolve())
    return result


def quest_completion_node(
    builder: PhaseGraphBuilder, quest_id: int, path: str
) -> GraphNode:
    node_type = builder.handles.wrap(
        {
            "$type": "questJournalQuestEntry_NodeType",
            "optional": 0,
            "path": journal_path(builder, path, "gameJournalQuest", 2),
            "sendNotification": 1,
            "trackQuest": 1,
            "version": "Initial",
        }
    )
    return builder.node(
        quest_id,
        "questJournalNodeDefinition",
        input_names=("Active", "Inactive", "Succeeded", "Failed"),
        properties={"type": node_type},
    )


def build_phone_phase(stage: CompiledStage, archive_target: Path) -> JsonObject:
    """Build a self-contained phone exchange with any number of response branches."""
    if stage.type != "phone_conversation":
        raise QuestSpecError(f"Stage {stage.id} is not a phone_conversation")

    messages = stage.data["messages"]
    choices = stage.data["choices"]
    builder = PhaseGraphBuilder()
    phase_input = input_node(builder)
    phase_output = output_node(builder)
    previous: GraphNode = phase_input
    next_id = 10
    objective: GraphNode | None = None
    if stage.data.get("objective"):
        objective = objective_node(builder, next_id, stage.data["objective"])
        next_id += 1
        builder.connect(previous, objective, destination_socket="Active")
        previous = objective
    if stage.data.get("description_entry"):
        description = journal_entry_node(
            builder,
            next_id,
            stage.data["description_entry"],
            "gameJournalQuestDescription",
            2,
        )
        next_id += 1
        builder.connect(previous, description, destination_socket="Active")
        previous = description
    delay = realtime_delay_node(
        builder, next_id, seconds=int(stage.data.get("delay_seconds", 1))
    )
    next_id += 1
    builder.connect(previous, delay)
    previous = delay
    for path in messages:
        message = journal_entry_node(
            builder, next_id, path, "gameJournalPhoneMessage", 1
        )
        builder.connect(previous, message, destination_socket="Active")
        previous = message
        next_id += 1

    opening_branches = stage.data.get("opening_branches", [])
    if opening_branches:
        branch_tails: list[GraphNode] = []
        for opening in opening_branches:
            condition = fact_condition_node(
                builder, next_id, opening["condition"]
            )
            next_id += 1
            builder.connect(previous, condition)
            branch_previous = condition
            for path in opening["messages"]:
                message = journal_entry_node(
                    builder, next_id, path, "gameJournalPhoneMessage", 1
                )
                next_id += 1
                builder.connect(branch_previous, message, destination_socket="Active")
                branch_previous = message
            branch_tails.append(branch_previous)
        opening_join = logical_xor_node(builder, next_id, len(branch_tails))
        next_id += 1
        for index, tail in enumerate(branch_tails, start=1):
            builder.connect(tail, opening_join, destination_socket=f"In{index}")
        previous = opening_join
        previous_socket = "Out1"
    else:
        previous_socket = "Out"

    choice_group = journal_entry_node(
        builder,
        next_id,
        stage.data["choice_group"],
        "gameJournalPhoneChoiceGroup",
        1,
    )
    builder.connect(
        previous,
        choice_group,
        source_socket=previous_socket,
        destination_socket="Active",
    )
    next_id += 1

    branch_nodes: list[tuple[GraphNode, GraphNode]] = []
    for choice in choices:
        succeeded = journal_choice_succeeded_node(
            builder, next_id, choice["choice"]
        )
        next_id += 1
        reply = journal_entry_node(
            builder, next_id, choice["reply"], "gameJournalPhoneMessage", 1
        )
        next_id += 1
        builder.connect(choice_group, succeeded)
        builder.connect(succeeded, reply, destination_socket="Active")
        branch_tail = reply
        if isinstance(choice.get("set_fact"), str):
            branch_fact = fact_node(builder, next_id, choice["set_fact"])
            next_id += 1
            builder.connect(branch_tail, branch_fact)
            branch_tail = branch_fact
        branch_nodes.append((succeeded, branch_tail))

    join = logical_xor_node(builder, next_id, len(branch_nodes))
    next_id += 1
    for index, (_, reply) in enumerate(branch_nodes, start=1):
        builder.connect(reply, join, destination_socket=f"In{index}")

    final_message = journal_entry_node(
        builder,
        next_id,
        stage.data["final_message"],
        "gameJournalPhoneMessage",
        1,
    )
    next_id += 1
    final_delay = realtime_delay_node(builder, next_id, seconds=1)
    next_id += 1
    builder.connect(join, final_message, source_socket="Out1", destination_socket="Active")
    builder.connect(final_message, final_delay)
    previous = final_delay

    if objective is not None:
        objective_done = objective_node(builder, next_id, stage.data["objective"])
        next_id += 1
        builder.connect(previous, objective_done, destination_socket="Succeeded")
        previous = objective_done
    reward = stage.data.get("reward")
    if isinstance(reward, str) and reward:
        granted = reward_node(builder, next_id, reward)
        next_id += 1
        builder.connect(previous, granted)
        previous = granted
    completion_fact = stage.data.get("completion_fact")
    if isinstance(completion_fact, str) and completion_fact:
        completed = fact_node(builder, next_id, completion_fact)
        builder.connect(previous, completed)
        previous = completed
        next_id += 1
    complete_quest = stage.data.get("complete_quest")
    if isinstance(complete_quest, str) and complete_quest:
        quest_done = quest_completion_node(builder, next_id, complete_quest)
        builder.connect(previous, quest_done, destination_socket="Succeeded")
        previous = quest_done
    builder.connect_to_earlier_output(previous, phase_output)

    return {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": "1970-01-01T00:00:00Z",
            "DataType": "CR2W",
            "ArchiveFileName": str(archive_target.resolve()),
        },
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {
                "$type": "questQuestPhaseResource",
                "cookingPlatform": "PLATFORM_PC",
                "graph": builder.graph,
                "inplacePhases": [],
                "phasePrefabs": [],
            },
            "EmbeddedFiles": [],
        },
    }


def build_phone_job_offer_phase(
    stage: CompiledStage, archive_target: Path
) -> JsonObject:
    """Build the one-choice phone offer used to start a meeting quest."""
    if stage.type != "phone_job_offer":
        raise QuestSpecError(f"Stage {stage.id} is not a phone_job_offer")

    builder = PhaseGraphBuilder()
    phase_input = input_node(builder)
    phase_output = output_node(builder)
    message = journal_entry_node(
        builder,
        10,
        stage.data["message"],
        "gameJournalPhoneMessage",
        1,
    )
    choice_group = journal_entry_node(
        builder,
        11,
        stage.data["choice_group"],
        "gameJournalPhoneChoiceGroup",
        1,
    )
    started = fact_node(builder, 12, stage.data["start_fact"])
    accepted = journal_entry_visited_node(
        builder,
        13,
        stage.data["accept_choice"],
        "gameJournalPhoneChoiceEntry",
    )
    accepted_fact = fact_node(builder, 14, stage.data["accepted_fact"])

    builder.connect(phase_input, message, destination_socket="Active")
    builder.connect(message, choice_group, destination_socket="Active")
    builder.connect(choice_group, started)
    builder.connect(started, accepted)
    builder.connect(accepted, accepted_fact)
    builder.connect_to_earlier_output(accepted_fact, phase_output)

    return {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": "1970-01-01T00:00:00Z",
            "DataType": "CR2W",
            "ArchiveFileName": str(archive_target.resolve()),
        },
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {
                "$type": "questQuestPhaseResource",
                "cookingPlatform": "PLATFORM_PC",
                "graph": builder.graph,
                "inplacePhases": [],
                "phasePrefabs": [],
            },
            "EmbeddedFiles": [],
        },
    }


def phase_document(builder: PhaseGraphBuilder, archive_target: Path) -> JsonObject:
    return {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": "1970-01-01T00:00:00Z",
            "DataType": "CR2W",
            "ArchiveFileName": str(archive_target.resolve()),
        },
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {
                "$type": "questQuestPhaseResource",
                "cookingPlatform": "PLATFORM_PC",
                "graph": builder.graph,
                "inplacePhases": [],
                "phasePrefabs": [],
            },
            "EmbeddedFiles": [],
        },
    }


def add_item_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    item_id: str,
    quantity: int,
) -> GraphNode:
    params = builder.handles.wrap(
        {
            "$type": "questAddRemoveItem_NodeTypeParams",
            "entityRef": local_player_reference(builder),
            "flagItemAddedCallbackAsSilent": 0,
            "isPlayer": 0,
            "itemID": tweakdbid(item_id),
            "itemIDsToIgnoreOnRemove": [],
            "nodeType": "AddItem",
            "objectRef": entity_reference(),
            "quantity": quantity,
            "removeAllQuantity": 0,
            "sendNotification": 1,
            "tagsToIgnoreOnRemove": [],
            "tagToRemove": cname("None"),
        }
    )
    node_type = builder.handles.wrap(
        {"$type": "questAddRemoveItem_NodeType", "params": [params]}
    )
    return builder.node(
        quest_id,
        "questItemManagerNodeDefinition",
        input_names=("In",),
        properties={"type": node_type},
    )


def community_action_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    community_ref: str,
    action: str,
) -> GraphNode:
    action_type = builder.handles.wrap(
        {
            "$type": "questCommunityTemplate_NodeType",
            "action": action,
            "communityEntryName": cname("None"),
            "communityEntryPhaseName": cname("None"),
            "spawnerReference": node_ref(community_ref),
        }
    )
    return builder.node(
        quest_id,
        "questSpawnManagerNodeDefinition",
        input_names=("In",),
        properties={
            "actions": [
                {
                    "$type": "questSpawnManagerNodeActionEntry",
                    "type": action_type,
                }
            ]
        },
    )


def build_reach_area_phase(stage: CompiledStage, archive_target: Path) -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    objective = objective_node(builder, 10, stage.data["objective"])
    description = journal_entry_node(
        builder, 11, stage.data["description_entry"], "gameJournalQuestDescription", 2
    )
    mappin = mappin_node(
        builder,
        12,
        stage.data["mappin"],
        disable_previous_mappins=stage.data.get("disable_previous_mappins", True),
    )
    entered = trigger_condition_node(builder, 13, stage.data["trigger"], "Entered")
    builder.connect(start, objective, destination_socket="Active")
    builder.connect(objective, description, destination_socket="Active")
    builder.connect(description, mappin, destination_socket="Active")
    previous: GraphNode = mappin
    next_id = 14
    if stage.data.get("start_fact"):
        started = fact_node(builder, next_id, stage.data["start_fact"])
        next_id += 1
        builder.connect(previous, started)
        previous = started
    builder.connect(previous, entered, destination_socket="In")
    objective_done = objective_node(
        builder, next_id, stage.data["objective"]
    )
    next_id += 1
    mappin_done = mappin_node(
        builder,
        next_id,
        stage.data["mappin"],
        disable_previous_mappins=False,
    )
    builder.connect(entered, objective_done, destination_socket="Succeeded")
    builder.connect(objective_done, mappin_done, destination_socket="Inactive")
    builder.connect_to_earlier_output(mappin_done, end)
    return phase_document(builder, archive_target)


def build_leave_area_phase(stage: CompiledStage, archive_target: Path) -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    objective: GraphNode | None = None
    previous: GraphNode = start
    next_id = 10
    if stage.data.get("objective"):
        objective = objective_node(builder, next_id, stage.data["objective"])
        next_id += 1
        builder.connect(start, objective, destination_socket="Active")
        previous = objective
    if stage.data.get("description_entry"):
        description = journal_entry_node(
            builder, next_id, stage.data["description_entry"], "gameJournalQuestDescription", 2
        )
        next_id += 1
        builder.connect(previous, description, destination_socket="Active")
        previous = description
    mappin: GraphNode | None = None
    if stage.data.get("mappin"):
        mappin = mappin_node(builder, next_id, stage.data["mappin"])
        next_id += 1
        builder.connect(previous, mappin, destination_socket="Active")
        previous = mappin
    exited = trigger_condition_node(builder, next_id, stage.data["trigger"], "Exited")
    next_id += 1
    builder.connect(previous, exited, destination_socket="In")
    previous = exited
    if objective is not None:
        objective_done = objective_node(
            builder, next_id, stage.data["objective"]
        )
        next_id += 1
        builder.connect(previous, objective_done, destination_socket="Succeeded")
        previous = objective_done
    if mappin is not None:
        mappin_done = mappin_node(
            builder, next_id, stage.data["mappin"]
        )
        next_id += 1
        builder.connect(previous, mappin_done, destination_socket="Inactive")
        previous = mappin_done
    if stage.data.get("completion_fact"):
        completed = fact_node(builder, next_id, stage.data["completion_fact"])
        next_id += 1
        builder.connect(previous, completed)
        previous = completed
    if stage.data.get("cleanup_community"):
        cleanup = community_action_node(
            builder, next_id, stage.data["cleanup_community"], "Deactivate"
        )
        builder.connect(previous, cleanup)
        previous = cleanup
    builder.connect_to_earlier_output(previous, end)
    return phase_document(builder, archive_target)


def build_acquire_item_phase(stage: CompiledStage, archive_target: Path) -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    objective: GraphNode | None = None
    previous: GraphNode = start
    next_id = 10
    if stage.data.get("objective"):
        objective = objective_node(builder, next_id, stage.data["objective"])
        next_id += 1
        builder.connect(start, objective, destination_socket="Active")
        previous = objective
    if stage.data.get("description_entry"):
        description = journal_entry_node(
            builder, next_id, stage.data["description_entry"], "gameJournalQuestDescription", 2
        )
        next_id += 1
        builder.connect(previous, description, destination_socket="Active")
        previous = description
    mappin: GraphNode | None = None
    if stage.data.get("mappin"):
        mappin = mappin_node(builder, next_id, stage.data["mappin"])
        next_id += 1
        builder.connect(previous, mappin, destination_socket="Active")
        previous = mappin
    if stage.data["source"] == "grant":
        grant = add_item_node(
            builder, next_id, stage.data["item"], stage.data.get("quantity", 1)
        )
        next_id += 1
        builder.connect(previous, grant)
        previous = grant
    acquired = inventory_condition_node(
        builder, next_id, stage.data["item"], quantity=stage.data.get("quantity", 1)
    )
    next_id += 1
    builder.connect(previous, acquired, destination_socket="In")
    previous = acquired
    if objective is not None:
        objective_done = objective_node(
            builder, next_id, stage.data["objective"]
        )
        next_id += 1
        builder.connect(previous, objective_done, destination_socket="Succeeded")
        previous = objective_done
    if mappin is not None:
        mappin_done = mappin_node(
            builder, next_id, stage.data["mappin"]
        )
        next_id += 1
        builder.connect(previous, mappin_done, destination_socket="Inactive")
        previous = mappin_done
    if stage.data.get("acquisition_fact"):
        completed = fact_node(builder, next_id, stage.data["acquisition_fact"])
        builder.connect(previous, completed)
        previous = completed
    builder.connect_to_earlier_output(previous, end)
    return phase_document(builder, archive_target)


def build_read_shard_phase(stage: CompiledStage, archive_target: Path) -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    previous: GraphNode = start
    objective: GraphNode | None = None
    next_id = 10
    if stage.data.get("objective"):
        objective = objective_node(builder, next_id, stage.data["objective"])
        next_id += 1
        builder.connect(previous, objective, destination_socket="Active")
        previous = objective
    if stage.data.get("description_entry"):
        description = journal_entry_node(
            builder, next_id, stage.data["description_entry"], "gameJournalQuestDescription", 2
        )
        next_id += 1
        builder.connect(previous, description, destination_socket="Active")
        previous = description
    if stage.data.get("activate_entry", False):
        activate = journal_entry_node(
            builder,
            next_id,
            stage.data["journal_entry"],
            "gameJournalOnscreen",
            stage.data["file_entry_index"],
        )
        next_id += 1
        builder.connect(previous, activate, destination_socket="Active")
        previous = activate
    acquisition_fact = stage.data.get("acquisition_fact")
    if isinstance(acquisition_fact, str) and acquisition_fact:
        acquired = fact_condition_node(builder, next_id, acquisition_fact)
    else:
        acquired = inventory_condition_node(builder, next_id, stage.data["item"])
    next_id += 1
    builder.connect(previous, acquired, destination_socket="In")
    previous = acquired
    presentation_delay = stage.data.get("presentation_delay_seconds", 0)
    if presentation_delay:
        delay = realtime_delay_node(
            builder, next_id, seconds=presentation_delay
        )
        next_id += 1
        builder.connect(previous, delay, destination_socket="In")
        previous = delay
    if objective is not None:
        objective_done = objective_node(
            builder, next_id, stage.data["objective"]
        )
        next_id += 1
        builder.connect(previous, objective_done, destination_socket="Succeeded")
        previous = objective_done
    if stage.data.get("completion_fact"):
        completed = fact_node(builder, next_id, stage.data["completion_fact"])
        builder.connect(previous, completed)
        previous = completed
    builder.connect_to_earlier_output(previous, end)
    return phase_document(builder, archive_target)


def game_time_delay_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    *,
    days: int,
    hours: int,
    minutes: int,
    seconds: int,
) -> GraphNode:
    condition_type = builder.handles.wrap(
        {
            "$type": "questGameTimeDelay_ConditionType",
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questTimeCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def build_time_gate_phase(stage: CompiledStage, archive_target: Path) -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    delay = game_time_delay_node(
        builder,
        10,
        days=stage.data.get("days", 0),
        hours=stage.data.get("hours", 0),
        minutes=stage.data.get("minutes", 0),
        seconds=stage.data.get("seconds", 0),
    )
    builder.connect(start, delay, destination_socket="In")
    previous: GraphNode = delay
    if stage.data.get("completion_fact"):
        completed = fact_node(builder, 11, stage.data["completion_fact"])
        builder.connect(previous, completed)
        previous = completed
    builder.connect_to_earlier_output(previous, end)
    return phase_document(builder, archive_target)


def build_read_terminal_document_phase(
    stage: CompiledStage, archive_target: Path
) -> JsonObject:
    """Activate an optional computer file, then wait for its vanilla read fact."""
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    previous: GraphNode = start
    next_id = 10

    document_entry = stage.data.get("document_entry")
    if isinstance(document_entry, str):
        document = journal_entry_node(
            builder,
            next_id,
            document_entry,
            "gameJournalFile",
            5,
        )
        builder.connect(previous, document, destination_socket="Active")
        previous = document
        next_id += 1

    objective = objective_node(builder, next_id, stage.data["objective"])
    builder.connect(previous, objective, destination_socket="Active")
    next_id += 1

    completed = fact_condition_node(
        builder, next_id, stage.data["completion_fact"]
    )
    builder.connect(objective, completed)
    next_id += 1

    objective_done = objective_node(
        builder, next_id, stage.data["objective"]
    )
    builder.connect(completed, objective_done, destination_socket="Succeeded")
    builder.connect_to_earlier_output(objective_done, end)
    return phase_document(builder, archive_target)


def scan_started_node(
    builder: PhaseGraphBuilder, quest_id: int, object_ref: str
) -> GraphNode:
    condition_type = builder.handles.wrap(
        {
            "$type": "questScan_ConditionType",
            "eventType": "Finished",
            "objectRef": entity_reference(object_ref),
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questObjectCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def quest_highlight_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    object_ref: str,
    *,
    revealed: bool = True,
) -> GraphNode:
    highlight_data = builder.handles.wrap(
        {
            "$type": "HighlightEditableData",
            "highlightType": "QUEST",
            "inTransitionTime": 0.5,
            "isRevealed": int(revealed),
            "outlineType": "QUEST",
            "outTransitionTime": 0.5,
            "patternType": "Default",
            "priority": "VeryLow",
        }
    )
    event = builder.handles.wrap(
        {
            "$type": "SetDefaultHighlightEvent",
            "highlightData": highlight_data,
        }
    )
    return builder.node(
        quest_id,
        "questEventManagerNodeDefinition",
        input_names=("In",),
        properties={
            "componentName": cname("None"),
            "event": event,
            "isObjectPlayer": 0,
            "isUiEvent": 0,
            "managerName": "PlayerGuidance",
            "objectRef": entity_reference(object_ref),
            "PSClassName": cname("None"),
        },
    )


def device_manager_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    *,
    device: str,
    controller: str,
    action: str,
) -> GraphNode:
    params = builder.handles.wrap(
        {
            "$type": "questDeviceManager_NodeTypeParams",
            "actionProperties": [],
            "deviceAction": cname(action),
            "deviceControllerClass": cname(controller),
            "entityRef": entity_reference(),
            "objectRef": node_ref(device),
            "slotName": cname("None"),
        }
    )
    node_type = builder.handles.wrap(
        {"$type": "questDeviceManager_NodeType", "params": [params]}
    )
    return builder.node(
        quest_id,
        "questInteractiveObjectManagerNodeDefinition",
        input_names=("In",),
        properties={"type": node_type},
    )


def device_condition_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    *,
    device: str,
    controller: str,
    function: str,
) -> GraphNode:
    condition_type = builder.handles.wrap(
        {
            "$type": "questDevice_ConditionType",
            "deviceConditionFunction": cname(function),
            "deviceControllerClass": cname(controller),
            "functionParameters": [],
            "objectRef": node_ref(device),
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questObjectCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def character_spawned_node(
    builder: PhaseGraphBuilder, quest_id: int, community: str
) -> GraphNode:
    comparison = builder.handles.wrap(
        {
            "$type": "questComparisonParam",
            "comparisonType": "Greater",
            "count": 0,
            "entireCommunity": 1,
        }
    )
    condition_type = builder.handles.wrap(
        {
            "$type": "questCharacterSpawned_ConditionType",
            "comparisonParams": comparison,
            "objectRef": entity_reference(community),
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questCharacterCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def community_defeated_node(
    builder: PhaseGraphBuilder, quest_id: int, community: str
) -> GraphNode:
    comparison = builder.handles.wrap(
        {
            "$type": "questComparisonParam",
            "comparisonType": "GreaterOrEqual",
            "count": 0,
            "entireCommunity": 1,
        }
    )
    condition_type = builder.handles.wrap(
        {
            "$type": "questCharacterKilled_ConditionType",
            "comparisonParams": comparison,
            "defeated": 1,
            "killed": 1,
            "objectRef": entity_reference(community),
            "source": None,
            "unconscious": 1,
        }
    )
    condition = builder.handles.wrap(
        {"$type": "questCharacterCondition", "type": condition_type}
    )
    return builder.node(
        quest_id,
        "questPauseConditionNodeDefinition",
        input_names=("In",),
        properties={"condition": condition},
    )


def combat_threat_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    community: str,
    entry: str,
) -> GraphNode:
    params = builder.handles.wrap(
        {
            "$type": "AIInjectCombatThreatCommandParams",
            "dontForceHostileAttitude": 0,
            "duration": 0,
            "isPersistent": 0,
            "targetNodeRef": node_ref("0", storage="uint64"),
            "targetPuppetRef": entity_reference("#player"),
        }
    )
    return builder.node(
        quest_id,
        "questCombatNodeDefinition",
        input_names=("In",),
        output_names=("Success",),
        properties={
            "entityReference": entity_reference(
                community, names=[entry]
            ),
            "function": cname("questCombatNodeParams_ShootAt"),
            "params": params,
        },
    )


def build_interact_device_phase(
    stage: CompiledStage, archive_target: Path
) -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    previous: GraphNode = start
    objective: GraphNode | None = None
    next_id = 10
    if stage.data.get("objective"):
        objective = objective_node(builder, next_id, stage.data["objective"])
        next_id += 1
        builder.connect(previous, objective, destination_socket="Active")
        previous = objective
    if stage.data.get("description_entry"):
        description = journal_entry_node(
            builder,
            next_id,
            stage.data["description_entry"],
            "gameJournalQuestDescription",
            2,
        )
        next_id += 1
        builder.connect(previous, description, destination_socket="Active")
        previous = description
    mappin: GraphNode | None = None
    if stage.data.get("mappin"):
        mappin = mappin_node(builder, next_id, stage.data["mappin"])
        next_id += 1
        builder.connect(previous, mappin, destination_socket="Active")
        previous = mappin
    action: GraphNode | None = None
    if stage.data.get("send_action", True):
        action = device_manager_node(
            builder,
            next_id,
            device=stage.data["device"],
            controller=stage.data["controller_class"],
            action=stage.data["action"],
        )
        next_id += 1
    completed = device_condition_node(
        builder,
        next_id,
        device=stage.data["device"],
        controller=stage.data["controller_class"],
        function=stage.data["completion_function"],
    )
    next_id += 1
    if action is not None:
        builder.connect(previous, action)
        builder.connect(action, completed)
    else:
        builder.connect(previous, completed)
    previous = completed
    if objective is not None:
        objective_done = objective_node(
            builder, next_id, stage.data["objective"]
        )
        next_id += 1
        builder.connect(previous, objective_done, destination_socket="Succeeded")
        previous = objective_done
    if mappin is not None:
        mappin_done = mappin_node(
            builder, next_id, stage.data["mappin"]
        )
        next_id += 1
        builder.connect(previous, mappin_done, destination_socket="Inactive")
        previous = mappin_done
    if stage.data.get("success_fact"):
        succeeded = fact_node(builder, next_id, stage.data["success_fact"])
        builder.connect(previous, succeeded)
        previous = succeeded
    builder.connect_to_earlier_output(previous, end)
    return phase_document(builder, archive_target)


def build_combat_encounter_phase(
    stage: CompiledStage, archive_target: Path
) -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    previous: GraphNode = start
    objective: GraphNode | None = None
    next_id = 10
    if stage.data.get("trigger"):
        proximity = trigger_condition_node(
            builder, next_id, stage.data["trigger"], "Entered"
        )
        next_id += 1
        builder.connect(previous, proximity, destination_socket="In")
        previous = proximity
    if stage.data.get("objective"):
        objective = objective_node(builder, next_id, stage.data["objective"])
        next_id += 1
        builder.connect(previous, objective, destination_socket="Active")
        previous = objective
    if stage.data.get("description_entry"):
        description = journal_entry_node(
            builder,
            next_id,
            stage.data["description_entry"],
            "gameJournalQuestDescription",
            2,
        )
        next_id += 1
        builder.connect(previous, description, destination_socket="Active")
        previous = description
    activate = community_action_node(
        builder, next_id, stage.data["community"], "Activate"
    )
    next_id += 1
    spawned = character_spawned_node(
        builder, next_id, stage.data["community"]
    )
    next_id += 1
    defeated = community_defeated_node(
        builder, next_id, stage.data["community"]
    )
    next_id += 1
    builder.connect(previous, activate)
    builder.connect(activate, spawned)
    previous = spawned
    previous_socket = "Out"
    for entry in stage.data.get("entries", []):
        attack = combat_threat_node(
            builder, next_id, stage.data["community"], entry
        )
        next_id += 1
        builder.connect(previous, attack, source_socket=previous_socket)
        previous = attack
        previous_socket = "Success"
    if stage.data.get("entries"):
        builder.connect_to_earlier_input(
            previous,
            defeated,
            source_socket=previous_socket,
            destination_socket="In",
        )
    else:
        builder.connect(
            previous,
            defeated,
            source_socket=previous_socket,
            destination_socket="In",
        )
    previous = defeated
    if objective is not None:
        objective_done = objective_node(
            builder, next_id, stage.data["objective"]
        )
        next_id += 1
        builder.connect(previous, objective_done, destination_socket="Succeeded")
        previous = objective_done
    if stage.data.get("completion_fact"):
        completed = fact_node(builder, next_id, stage.data["completion_fact"])
        next_id += 1
        builder.connect(previous, completed)
        previous = completed
    if stage.data.get("cleanup_on_exit"):
        cleanup = community_action_node(
            builder, next_id, stage.data["community"], "Deactivate"
        )
        builder.connect(previous, cleanup)
        previous = cleanup
    builder.connect_to_earlier_output(previous, end)
    return phase_document(builder, archive_target)


def build_investigate_clues_phase(
    stage: CompiledStage, archive_target: Path
) -> JsonObject:
    """Generate an ordered scan flow for any positive number of clues."""
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    objective = objective_node(builder, 10, stage.data["objective"])
    description = journal_entry_node(
        builder, 11, stage.data["description_entry"], "gameJournalQuestDescription", 2
    )
    builder.connect(start, objective, destination_socket="Active")
    builder.connect(objective, description, destination_socket="Active")
    previous: GraphNode = description
    next_id = 20

    for clue in stage.data["clues"]:
        if clue.get("mappin"):
            clue_mappin = mappin_node(builder, next_id, clue["mappin"])
            next_id += 1
            builder.connect(
                previous, clue_mappin, destination_socket="Active"
            )
            previous = clue_mappin

        scanned = scan_started_node(builder, next_id, clue["object_ref"])
        next_id += 1
        builder.connect(previous, scanned, destination_socket="In")
        previous = scanned

        if clue.get("mappin"):
            clue_mappin_done = mappin_node(
                builder, next_id, clue["mappin"]
            )
            next_id += 1
            builder.connect(
                previous, clue_mappin_done, destination_socket="Inactive"
            )
            previous = clue_mappin_done
        if clue.get("journal_entry"):
            journal = journal_entry_node(
                builder,
                next_id,
                clue["journal_entry"],
                "gameJournalOnscreen",
                5,
            )
            next_id += 1
            builder.connect(
                previous, journal, destination_socket="Active"
            )
            previous = journal
        if clue.get("completion_fact"):
            clue_fact = fact_node(builder, next_id, clue["completion_fact"])
            next_id += 1
            builder.connect(previous, clue_fact)
            previous = clue_fact
        if clue.get("grant_item"):
            granted = add_item_node(
                builder, next_id, clue["grant_item"], 1
            )
            next_id += 1
            builder.connect(previous, granted)
            previous = granted

    objective_done = objective_node(
        builder, next_id, stage.data["objective"]
    )
    next_id += 1
    builder.connect(previous, objective_done, destination_socket="Succeeded")
    previous = objective_done
    if stage.data.get("completion_fact"):
        completed = fact_node(builder, next_id, stage.data["completion_fact"])
        builder.connect(previous, completed)
        previous = completed
    builder.connect_to_earlier_output(previous, end)
    return phase_document(builder, archive_target)


def build_stage_phase(
    stage: CompiledStage,
    archive_target: Path,
    phase_prefabs: tuple[str, ...] = (),
) -> JsonObject:
    if stage.type == "phone_job_offer" and not stage.data.get("phase_template"):
        result = build_phone_job_offer_phase(stage, archive_target)
    elif stage.type == "phone_conversation" and not stage.data.get("phase_template"):
        result = build_phone_phase(stage, archive_target)
    elif stage.type == "reach_area" and not stage.data.get("phase_template"):
        result = build_reach_area_phase(stage, archive_target)
    elif stage.type == "leave_area" and not stage.data.get("phase_template"):
        result = build_leave_area_phase(stage, archive_target)
    elif stage.type == "acquire_item" and not stage.data.get("phase_template"):
        result = build_acquire_item_phase(stage, archive_target)
    elif stage.type == "read_shard" and not stage.data.get("phase_template"):
        result = build_read_shard_phase(stage, archive_target)
    elif stage.type == "investigate_clues" and not stage.data.get("phase_template"):
        result = build_investigate_clues_phase(stage, archive_target)
    elif stage.type == "interact_device" and not stage.data.get("phase_template"):
        result = build_interact_device_phase(stage, archive_target)
    elif stage.type == "combat_encounter" and not stage.data.get("phase_template"):
        result = build_combat_encounter_phase(stage, archive_target)
    elif stage.type == "time_gate" and not stage.data.get("phase_template"):
        result = build_time_gate_phase(stage, archive_target)
    elif (
        stage.type == "read_terminal_document"
        and not stage.data.get("phase_template")
    ):
        result = build_read_terminal_document_phase(stage, archive_target)
    else:
        result = instantiate_stage_phase(stage, archive_target)
    inherited_prefabs = (
        phase_prefabs if stage.data.get("inherit_phase_prefabs", True) else ()
    )
    result["Data"]["RootChunk"]["phasePrefabs"] = [
        {
            "$type": "questQuestPrefabEntry",
            "prefabNodeRef": node_ref(prefab),
        }
        for prefab in inherited_prefabs
    ]
    validate_handle_graph(result, context=f"Stage {stage.id}")
    if stage.type in DIRECT_STAGE_TYPES and not stage.data.get("phase_template"):
        validate_no_forward_handle_refs(result, context=f"Stage {stage.id}")
    validate_stage_contract(stage, result)
    return result


def resource_ref(path: str) -> JsonObject:
    return {
        "DepotPath": {
            "$type": "ResourcePath",
            "$storage": "string",
            "$value": path,
        },
        "Flags": "Soft",
    }


def phase_node(builder: PhaseGraphBuilder, node_id: int, path: str) -> GraphNode:
    return builder.node(
        node_id,
        "questPhaseNodeDefinition",
        input_names=("In1",),
        output_names=("Out1",),
        properties={
            "phaseGraph": None,
            "phaseInstancePrefabs": [],
            "phaseResource": resource_ref(path),
            "saveLock": 0,
            "unfreezingTriggerNodeRef": node_ref("0", storage="uint64"),
        },
    )


def debug_step_node(
    builder: PhaseGraphBuilder,
    node_id: int,
    fact_name: str,
    value: int,
) -> GraphNode:
    node = fact_node(builder, node_id, fact_name)
    node_type = node.data["type"]["Data"]
    node_type["setExactValue"] = value
    node_type["value"] = value
    return node


def build_orchestration_phase(spec: QuestSpec, archive_target: Path) -> JsonObject:
    builder = PhaseGraphBuilder()
    start = input_node(builder)
    end = output_node(builder)
    previous = start
    for stage in spec.stages:
        source_socket = "Out" if previous is start else "Out1"
        if stage.type == "meet_contact":
            journal_base = 100 + stage.index * 3
            objective = journal_entry_node(
                builder,
                journal_base,
                stage.data["objective"],
                "gameJournalQuestObjective",
                2,
            )
            description = journal_entry_node(
                builder,
                journal_base + 1,
                stage.data["description_entry"],
                "gameJournalQuestDescription",
                2,
            )
            mappin = mappin_node(
                builder,
                journal_base + 2,
                stage.data["mappin"],
                disable_previous_mappins=True,
            )
            builder.connect(
                previous,
                objective,
                source_socket=source_socket,
                destination_socket="Active",
            )
            builder.connect(objective, description, destination_socket="Active")
            builder.connect(description, mappin, destination_socket="Active")
            previous = mappin
            source_socket = "Out"
        if spec.debug_fact is not None:
            debug = debug_step_node(
                builder,
                500 + stage.index,
                spec.debug_fact,
                (stage.index + 1) * 10,
            )
            builder.connect(
                previous,
                debug,
                source_socket=source_socket,
                destination_socket="In",
            )
            previous = debug
            source_socket = "Out"
        current = phase_node(builder, stage.node_id, stage.phase_resource)
        builder.connect(
            previous,
            current,
            source_socket=source_socket,
            destination_socket="In1",
        )
        previous = current
    builder.connect_to_earlier_output(previous, end, source_socket="Out1")

    result = {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": "1970-01-01T00:00:00Z",
            "DataType": "CR2W",
            "ArchiveFileName": str(archive_target.resolve()),
        },
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {
                "$type": "questQuestPhaseResource",
                "cookingPlatform": "PLATFORM_PC",
                "graph": builder.graph,
                "inplacePhases": [],
                "phasePrefabs": [
                    {
                        "$type": "questQuestPrefabEntry",
                        "prefabNodeRef": node_ref(value),
                    }
                    for value in spec.phase_prefabs
                ],
            },
            "EmbeddedFiles": [],
        },
    }
    validate_handle_graph(result, context=f"Quest {spec.id} orchestration")
    return result


def build_plan(spec: QuestSpec, diagnostics: Iterable[Diagnostic]) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "quest": {
            "id": spec.id,
            "title": spec.title,
            "manifest": str(spec.path),
        },
        "linear_flow": [stage.id for stage in spec.stages],
        "stages": [
            {
                "index": stage.index,
                "node_id": stage.node_id,
                "id": stage.id,
                "type": stage.type,
                "status": stage.status,
                "phase_resource": stage.phase_resource,
                "phase_template": stage_template_resource(stage),
                "implementation": STAGE_IMPLEMENTATION_MODE[stage.type],
                "data": stage.data,
            }
            for stage in spec.stages
        ],
        "diagnostics": [item.as_dict() for item in diagnostics],
        "shipping_ready": all(stage.status == "ready" for stage in spec.stages)
        and not any(item.level == "error" for item in diagnostics),
    }


def report(spec: QuestSpec | None, diagnostics: list[Diagnostic]) -> dict[str, Any]:
    return {
        "ok": spec is not None and not any(item.level == "error" for item in diagnostics),
        "diagnostics": [item.as_dict() for item in diagnostics],
        "quest": spec.id if spec else None,
        "stages": len(spec.stages) if spec else 0,
        "planned_stages": (
            [stage.id for stage in spec.stages if stage.status == "planned"]
            if spec
            else []
        ),
    }


def command_validate(args: argparse.Namespace) -> int:
    spec, diagnostics = load_spec(args.manifest)
    if spec is not None:
        diagnostics.extend(audit_resources(spec))
    result = report(spec, diagnostics)
    print(json.dumps(result, indent=2))
    return 0 if result["ok"] else 1


def command_compile(args: argparse.Namespace) -> int:
    spec, diagnostics = load_spec(args.manifest)
    if spec is None:
        print(json.dumps(report(spec, diagnostics), indent=2))
        return 1
    diagnostics.extend(audit_resources(spec))
    errors = [item for item in diagnostics if item.level == "error"]
    planned = [stage.id for stage in spec.stages if stage.status == "planned"]
    if planned and not args.allow_planned:
        planned_diagnostic = Diagnostic(
            "error",
            "planned_stages",
            "Compilation contains planned stages; pass --allow-planned for a non-shipping prototype",
        )
        diagnostics.append(planned_diagnostic)
        errors.append(
            planned_diagnostic
        )
    if errors:
        print(json.dumps(report(spec, diagnostics), indent=2))
        return 1

    output = args.out.resolve()
    archive_target = (
        ROOT / "source" / "archive" / "mod" / spec.id / "phases" / f"{spec.id}.questphase"
    )
    phase = build_orchestration_phase(spec, archive_target)
    write_json(output, phase)
    children: list[dict[str, str]] = []
    child_root = output.parent / "children"
    for stage in spec.stages:
        if (
            stage_template_resource(stage) is None
            and stage.type not in DIRECT_STAGE_TYPES
        ):
            continue
        relative = Path(*stage.phase_resource.split("\\"))
        child_output = child_root / Path(f"{relative}.json")
        child_archive = ROOT / "source" / "archive" / relative
        write_json(
            child_output,
            build_stage_phase(stage, child_archive, spec.phase_prefabs),
        )
        children.append(
            {
                "stage": stage.id,
                "resource": stage.phase_resource,
                "output": str(child_output),
            }
        )
    plan_path = args.plan.resolve() if args.plan else output.with_suffix(".plan.json")
    write_json(plan_path, build_plan(spec, diagnostics))
    print(
        json.dumps(
            {
                "ok": True,
                "quest": spec.id,
                "output": str(output),
                "plan": str(plan_path),
                "stages": len(spec.stages),
                "shipping_ready": not planned,
                "planned_stages": planned,
                "children": children,
            },
            indent=2,
        )
    )
    return 0


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    subparsers = result.add_subparsers(dest="command", required=True)
    validate = subparsers.add_parser("validate")
    validate.add_argument("manifest", type=Path)
    validate.set_defaults(func=command_validate)
    compile_parser = subparsers.add_parser("compile")
    compile_parser.add_argument("manifest", type=Path)
    compile_parser.add_argument("--out", type=Path, required=True)
    compile_parser.add_argument("--plan", type=Path)
    compile_parser.add_argument("--allow-planned", action="store_true")
    compile_parser.set_defaults(func=command_compile)
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        return int(args.func(args))
    except QuestSpecError as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, indent=2))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
