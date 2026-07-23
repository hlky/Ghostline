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
}
DIRECT_STAGE_TYPES = {
    "phone_job_offer",
    "phone_conversation",
    "reach_area",
    "acquire_item",
    "leave_area",
    "read_shard",
}
TEMPLATE_REQUIRED_STAGE_TYPES = {
    "interact_device",
    "combat_encounter",
    "investigate_clues",
    "optional_condition",
    "choice_gate",
    "escort_npc",
    "carry_npc",
    "deliver_vehicle",
}

BUILTIN_TEMPLATE_RESOURCES = {
    stage_type: rf"mod\ghostline\quest_blocks\templates\{stage_type}.questphase"
    for stage_type in TEMPLATE_REQUIRED_STAGE_TYPES
}

BUILTIN_UNSUPPORTED_FIELDS = {
    "interact_device": {"objective", "description_entry", "mappin", "success_fact"},
    "combat_encounter": {
        "entries",
        "completion_fact",
        "cleanup_on_exit",
        "nonlethal_allowed",
    },
    "investigate_clues": {"completion_fact"},
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
    "read_shard": {"journal_entry"},
    "investigate_clues": {"objective", "description_entry"},
    "optional_condition": {
        "objective", "success_fact", "failure_fact", "evaluation",
    },
    "choice_gate": {"gate_kind"},
    "escort_npc": {"community", "entry", "objective"},
    "carry_npc": {"community", "entry", "destination", "objective"},
    "deliver_vehicle": {"vehicle", "destination", "objective"},
}
TOP_LEVEL_FIELDS = {
    "schema_version",
    "id",
    "title",
    "description",
    "phase_prefabs",
    "stages",
}
COMMON_STAGE_FIELDS = {
    "id",
    "type",
    "status",
    "phase_resource",
    "phase_template",
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
        "final_message", "completion_fact", "delay_seconds",
    },
    "reach_area": {
        "trigger", "objective", "description_entry", "mappin",
        "start_fact", "disable_previous_mappins",
    },
    "interact_device": {
        "device", "controller_class", "action", "completion_function",
        "objective", "description_entry", "mappin", "success_fact",
    },
    "acquire_item": {
        "item", "source", "quantity", "objective", "description_entry", "mappin",
        "acquisition_fact",
    },
    "combat_encounter": {
        "community", "entries", "activate", "hostility", "completion",
        "nonlethal_allowed", "completion_fact", "cleanup_on_exit",
    },
    "leave_area": {
        "trigger", "objective", "description_entry", "mappin",
        "completion_fact", "cleanup_community",
    },
    "read_shard": {
        "item", "journal_entry", "file_entry_index", "activate_entry",
        "objective", "description_entry", "completion_fact",
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
        "failure_fact", "allow_combat_interrupt",
    },
    "carry_npc": {
        "community", "entry", "destination", "objective", "description_entry",
        "placement_slot", "completion_fact",
    },
    "deliver_vehicle": {
        "vehicle", "destination", "objective", "description_entry", "mappin",
        "require_player_exit", "completion_fact",
    },
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
            if (
                not isinstance(stage.get("phase_template"), str)
                and isinstance(clues, list)
                and any(
                    isinstance(clue, dict)
                    and set(clue) - {"id", "object_ref"}
                    for clue in clues
                )
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "unsupported_clue_fields",
                        f"{context} built-in template supports clue id and object_ref only",
                        stage_id or None,
                    )
                )
            else:
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
                and len(destinations) != 2
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "unsupported_destination_count",
                        f"{context}.destinations currently requires exactly two route gates",
                        stage_id or None,
                    )
                )

        if stage_type == "investigate_clues":
            clues = stage.get("clues")
            if (
                not isinstance(stage.get("phase_template"), str)
                and isinstance(clues, list)
                and (
                len(clues) != 1 or stage.get("required_count", 1) != 1
                )
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "unsupported_clue_count",
                        f"{context} currently supports exactly one required clue",
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
                    and set(item) == {"choice", "reply"}
                    and all(
                        isinstance(item[key], str) and item[key].strip()
                        for key in ("choice", "reply")
                    )
                    for item in choices
                )
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "invalid_phone_choices",
                        f"{context}.choices must contain at least two choice/reply objects",
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
                handle_ids.append(str(child["HandleId"]))
            if "HandleRefId" in child:
                handle_refs.append(str(child["HandleRefId"]))
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
    elif stage.type == "reach_area":
        expected.extend(
            (field, stage.data[field])
            for field in ("trigger", "objective", "description_entry", "mappin")
        )
    elif stage.type == "interact_device":
        expected.extend(
            (field, stage.data[field])
            for field in ("device", "controller_class", "action", "completion_function")
        )
    elif stage.type == "acquire_item":
        expected.append(("item", stage.data["item"]))
    elif stage.type == "combat_encounter":
        expected.append(("community", stage.data["community"]))
        expected.extend(("entries", item) for item in stage.data.get("entries", []))
    elif stage.type == "leave_area":
        expected.extend(
            (field, stage.data[field]) for field in ("trigger", "objective")
        )
        if isinstance(stage.data.get("cleanup_community"), str):
            expected.append(
                ("cleanup_community", stage.data["cleanup_community"])
            )
    elif stage.type == "read_shard":
        expected.append(("journal_entry", stage.data["journal_entry"]))
        if isinstance(stage.data.get("item"), str):
            expected.append(("item", stage.data["item"]))
    elif stage.type == "investigate_clues":
        for clue in stage.data.get("clues", []):
            expected.append(("clues", clue["object_ref"]))
            for field in ("completion_fact", "journal_entry", "mappin"):
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
            for field in ("community", "entry", "objective")
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
            "{{objective}}": stage.data["objective"],
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


def build_phone_phase(stage: CompiledStage, archive_target: Path) -> JsonObject:
    """Build a self-contained phone exchange with any number of response branches."""
    if stage.type != "phone_conversation":
        raise QuestSpecError(f"Stage {stage.id} is not a phone_conversation")

    messages = stage.data["messages"]
    choices = stage.data["choices"]
    builder = PhaseGraphBuilder()
    phase_input = input_node(builder)
    phase_output = output_node(builder)
    delay = realtime_delay_node(
        builder, 10, seconds=int(stage.data.get("delay_seconds", 1))
    )
    builder.connect(phase_input, delay)
    previous = delay
    next_id = 11
    for path in messages:
        message = journal_entry_node(
            builder, next_id, path, "gameJournalPhoneMessage", 1
        )
        builder.connect(previous, message, destination_socket="Active")
        previous = message
        next_id += 1

    choice_group = journal_entry_node(
        builder,
        next_id,
        stage.data["choice_group"],
        "gameJournalPhoneChoiceGroup",
        1,
    )
    builder.connect(previous, choice_group, destination_socket="Active")
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
        branch_nodes.append((succeeded, reply))

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
    final_visited = journal_entry_visited_node(
        builder,
        next_id,
        stage.data["final_message"],
        "gameJournalPhoneMessage",
    )
    next_id += 1
    builder.connect(join, final_message, source_socket="Out1", destination_socket="Active")
    builder.connect(final_message, final_visited)
    previous = final_visited

    completion_fact = stage.data.get("completion_fact")
    if isinstance(completion_fact, str) and completion_fact:
        completed = fact_node(builder, next_id, completion_fact)
        builder.connect(previous, completed)
        previous = completed
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
    if stage.data.get("start_fact"):
        started = fact_node(builder, 14, stage.data["start_fact"])
        builder.connect(previous, started)
        previous = started
    builder.connect(previous, entered, destination_socket="In")
    builder.connect_to_earlier_input(
        entered, objective, destination_socket="Succeeded"
    )
    builder.connect(objective, mappin, destination_socket="Inactive")
    previous = mappin
    builder.connect_to_earlier_output(previous, end)
    return phase_document(builder, archive_target)


def build_leave_area_phase(stage: CompiledStage, archive_target: Path) -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    objective: GraphNode | None = None
    previous: GraphNode = start
    if stage.data.get("objective"):
        objective = objective_node(builder, 10, stage.data["objective"])
        builder.connect(start, objective, destination_socket="Active")
        previous = objective
    if stage.data.get("description_entry"):
        description = journal_entry_node(
            builder, 11, stage.data["description_entry"], "gameJournalQuestDescription", 2
        )
        builder.connect(previous, description, destination_socket="Active")
        previous = description
    mappin: GraphNode | None = None
    if stage.data.get("mappin"):
        mappin = mappin_node(builder, 12, stage.data["mappin"])
        builder.connect(previous, mappin, destination_socket="Active")
        previous = mappin
    exited = trigger_condition_node(builder, 13, stage.data["trigger"], "Exited")
    builder.connect(previous, exited, destination_socket="In")
    builder.connect_to_earlier_input(
        exited, objective, destination_socket="Succeeded"
    )
    previous = objective
    if mappin is not None:
        builder.connect(previous, mappin, destination_socket="Inactive")
        previous = mappin
    if stage.data.get("completion_fact"):
        completed = fact_node(builder, 14, stage.data["completion_fact"])
        builder.connect(previous, completed)
        previous = completed
    if stage.data.get("cleanup_community"):
        cleanup = community_action_node(
            builder, 15, stage.data["cleanup_community"], "Deactivate"
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
    if stage.data.get("objective"):
        objective = objective_node(builder, 10, stage.data["objective"])
        builder.connect(start, objective, destination_socket="Active")
        previous = objective
    if stage.data.get("description_entry"):
        description = journal_entry_node(
            builder, 11, stage.data["description_entry"], "gameJournalQuestDescription", 2
        )
        builder.connect(previous, description, destination_socket="Active")
        previous = description
    mappin: GraphNode | None = None
    if stage.data.get("mappin"):
        mappin = mappin_node(builder, 12, stage.data["mappin"])
        builder.connect(previous, mappin, destination_socket="Active")
        previous = mappin
    if stage.data["source"] == "grant":
        grant = add_item_node(
            builder, 13, stage.data["item"], stage.data.get("quantity", 1)
        )
        builder.connect(previous, grant)
        previous = grant
    acquired = inventory_condition_node(
        builder, 14, stage.data["item"], quantity=stage.data.get("quantity", 1)
    )
    builder.connect(previous, acquired, destination_socket="In")
    previous = acquired
    if objective is not None:
        builder.connect_to_earlier_input(
            previous, objective, destination_socket="Succeeded"
        )
        previous = objective
    if mappin is not None:
        builder.connect(previous, mappin, destination_socket="Inactive")
        previous = mappin
    if stage.data.get("acquisition_fact"):
        completed = fact_node(builder, 15, stage.data["acquisition_fact"])
        builder.connect(previous, completed)
        previous = completed
    builder.connect_to_earlier_output(previous, end)
    return phase_document(builder, archive_target)


def build_read_shard_phase(stage: CompiledStage, archive_target: Path) -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    previous: GraphNode = start
    objective: GraphNode | None = None
    if stage.data.get("objective"):
        objective = objective_node(builder, 10, stage.data["objective"])
        builder.connect(previous, objective, destination_socket="Active")
        previous = objective
    if stage.data.get("description_entry"):
        description = journal_entry_node(
            builder, 11, stage.data["description_entry"], "gameJournalQuestDescription", 2
        )
        builder.connect(previous, description, destination_socket="Active")
        previous = description
    if stage.data.get("activate_entry", False):
        activate = journal_entry_node(
            builder,
            12,
            stage.data["journal_entry"],
            "gameJournalOnscreen",
            stage.data["file_entry_index"],
        )
        builder.connect(previous, activate, destination_socket="Active")
        previous = activate
    if stage.data.get("item"):
        acquired = inventory_condition_node(builder, 13, stage.data["item"])
        builder.connect(previous, acquired, destination_socket="In")
        previous = acquired
    visited = journal_entry_visited_node(
        builder,
        14,
        stage.data["journal_entry"],
        stage.data.get("journal_class", "gameJournalOnscreen"),
        file_index=stage.data.get("file_entry_index", 1),
    )
    builder.connect(previous, visited, destination_socket="In")
    previous = visited
    if objective is not None:
        builder.connect_to_earlier_input(
            previous, objective, destination_socket="Succeeded"
        )
        previous = objective
    if stage.data.get("completion_fact"):
        completed = fact_node(builder, 15, stage.data["completion_fact"])
        builder.connect(previous, completed)
        previous = completed
    builder.connect_to_earlier_output(previous, end)
    return phase_document(builder, archive_target)


def build_stage_phase(stage: CompiledStage, archive_target: Path) -> JsonObject:
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
    else:
        result = instantiate_stage_phase(stage, archive_target)
    validate_handle_graph(result, context=f"Stage {stage.id}")
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
        write_json(child_output, build_stage_phase(stage, child_archive))
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
