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
    fact_node,
    input_node,
    journal_entry_node,
    mappin_node,
    node_ref,
    output_node,
    realtime_delay_node,
)
from generate_delivery_phase import (  # noqa: E402
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
}
DIRECT_STAGE_TYPES = {"phone_job_offer", "phone_conversation"}
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
}
TOP_LEVEL_FIELDS = {
    "schema_version",
    "id",
    "title",
    "description",
    "phase_prefabs",
    "stages",
}
STAGE_FIELDS = {
    "id",
    "type",
    "status",
    "phase_resource",
    "phase_template",
    "template_bindings",
    "contact",
    "scene",
    "community",
    "appearance",
    "objective",
    "description_entry",
    "mappin",
    "device",
    "success_fact",
    "guard_community",
    "grants",
    "item",
    "drop_point",
    "deposit_fact",
    "thread",
    "messages",
    "message",
    "accept_choice",
    "start_fact",
    "accepted_fact",
    "choice_group",
    "choices",
    "final_message",
    "completion_fact",
    "delay_seconds",
    "required_assets",
    "notes",
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

        for field in sorted(set(stage) - STAGE_FIELDS):
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
        for field in STAGE_REQUIRED_FIELDS.get(stage_type, set()):
            require_string(stage, field, context=context, diagnostics=diagnostics)

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
        template = stage.data.get("phase_template")
        if isinstance(template, str):
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

    values = scalar_strings(phase)
    missing = [f"{field}={value}" for field, value in expected if value not in values]
    if missing:
        raise QuestSpecError(
            f"Stage {stage.id} child phase does not implement typed fields: "
            + ", ".join(missing)
        )


def instantiate_stage_phase(stage: CompiledStage, archive_target: Path) -> JsonObject:
    template_resource = stage.data.get("phase_template")
    if not isinstance(template_resource, str):
        raise QuestSpecError(f"Stage {stage.id} does not declare phase_template")
    raw_template, packed_template = resource_paths(template_resource)
    if not raw_template.is_file():
        raise QuestSpecError(
            f"Stage {stage.id} needs raw template {raw_template}; packed-only templates cannot be rewritten"
        )
    bindings_value = stage.data.get("template_bindings", {})
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


def build_stage_phase(stage: CompiledStage, archive_target: Path) -> JsonObject:
    if stage.type == "phone_job_offer" and not stage.data.get("phase_template"):
        result = build_phone_job_offer_phase(stage, archive_target)
    elif stage.type == "phone_conversation" and not stage.data.get("phase_template"):
        result = build_phone_phase(stage, archive_target)
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
                "phase_template": stage.data.get("phase_template"),
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
            not isinstance(stage.data.get("phase_template"), str)
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
