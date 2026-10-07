#!/usr/bin/env python3
"""Validate and compile typed Ghostline quest manifests."""

from __future__ import annotations


import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PureWindowsPath
from typing import Any, Callable, Iterable, Mapping
from project_layout import resource_project, owning_project, project_root as resolve_project


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from phase_graph import (
    resource_ref as resource_ref,
    add_item_node as add_item_node, scan_started_node as scan_started_node,
    combat_threat_node as combat_threat_node,
    JsonObject as JsonObject,
    device_manager_node as device_manager_node,
    device_condition_node as device_condition_node,
    character_spawned_node as character_spawned_node,
    community_defeated_node as community_defeated_node,
    community_action_node as community_action_node,
    phase_document as phase_document,
    quest_completion_node as quest_completion_node,
    GraphNode as GraphNode,
    PhaseGraphBuilder as PhaseGraphBuilder,
    cname as cname,
    entity_reference as entity_reference,
    fact_node as fact_node,
    input_node as input_node,
    journal_entry_node as journal_entry_node,
    journal_path as journal_path,
    logical_and_node as logical_and_node,
    mappin_node as mappin_node,
    node_ref as node_ref,
    objective_node as objective_node,
    output_node as output_node,
    realtime_delay_node as realtime_delay_node,
    trigger_condition_node as trigger_condition_node,
    local_player_reference as local_player_reference,
    tweakdbid as tweakdbid,
    fact_condition_node as fact_condition_node,
    inventory_condition_node as inventory_condition_node,
    journal_choice_succeeded_node as journal_choice_succeeded_node,
    journal_entry_visited_node as journal_entry_visited_node,
    logical_xor_node as logical_xor_node,
    reserve_drop_point_node as reserve_drop_point_node,
    reward_node as reward_node,
)

from quest_encounter import (
    gameplay_ai_node as gameplay_ai_node,
    character_not_in_combat_node as character_not_in_combat_node,
    clear_ai_role_node as clear_ai_role_node,
    alerted_patrol_role_node as alerted_patrol_role_node,
    combat_target_node as combat_target_node,
    named_character_spawned_node as named_character_spawned_node,
    named_character_outcome_node as named_character_outcome_node,
    cyberpsycho_reveal_node as cyberpsycho_reveal_node,
    character_mortality_node as character_mortality_node,
    character_attitude_group_node as character_attitude_group_node,
    player_health_condition_node as player_health_condition_node,
    player_modify_health_node as player_modify_health_node,
    scene_flow_node as scene_flow_node,
    build_cyberpsycho_encounter_phase as build_cyberpsycho_encounter_phase,
)

from artifact_io import atomic_write_json, publish_json_artifacts
from quest_lifecycle import apply_objective_lifecycle
from quest_block_builders import (
    build_escort_phase, build_timed_defense_phase, build_choice_phase,
    build_investigation_phase,
)
from quest_flow import (
    contract_dict, stage_inputs, stage_outcomes, stage_transitions,
    validate_flow, validate_flow_fields, validate_phase_ports, validate_emitted_contract,
    audit_scene_contracts,
)


from quest_types import (
    QuestSpecError, Diagnostic, CompiledStage, ParallelGroup, QuestSpec,
    require_string, ID_RE,
)
from quest_stages import (
    SCHEMA_VERSION, STAGE_REGISTRY, TOP_LEVEL_FIELDS, COMMON_STAGE_FIELDS,
    SUPPORTED_STAGE_TYPES, DIRECT_STAGE_TYPES as DIRECT_STAGE_TYPES, TEMPLATE_REQUIRED_STAGE_TYPES,
    BUILTIN_TEMPLATE_RESOURCES as BUILTIN_TEMPLATE_RESOURCES, BUILTIN_UNSUPPORTED_FIELDS,
    STAGE_IMPLEMENTATION_MODE as STAGE_IMPLEMENTATION_MODE, STAGE_REQUIRED_FIELDS, STAGE_TYPE_FIELDS,
)

DEPOT_RE = re.compile(r"^(?:base|ep1|mod)\\.+$")


def _depot_parts(depot_path: Any) -> tuple[str, ...] | None:
    """Accept canonical depot names without filesystem traversal or aliases."""
    if not isinstance(depot_path, str) or not DEPOT_RE.fullmatch(depot_path):
        return None
    parts = tuple(depot_path.split("\\"))
    for part in parts:
        if (
            not part or part in {".", ".."} or part.endswith((".", " "))
            or any(ord(char) < 32 or char in '/:<>"|?*' for char in part)
            or PureWindowsPath(part).is_reserved()
        ):
            return None
    return parts


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise QuestSpecError(f"Cannot read quest manifest {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise QuestSpecError("Quest manifest root must be an object")
    return value


def write_json(path: Path, value: Any) -> None:
    atomic_write_json(path, value)


def resource_paths(depot_path: str, *, project_root: Path | None = None) -> tuple[Path, Path]:
    parts = _depot_parts(depot_path)
    if parts is None:
        raise QuestSpecError(f"Invalid depot path: {depot_path!r}")
    relative = Path(*parts)
    project = (project_root or resource_project(depot_path, root=ROOT)).resolve()
    raw_root = project / "source/raw"
    archive_root = project / "source/archive"
    raw, archive = raw_root / Path(f"{relative}.json"), archive_root / relative
    if not raw.resolve().is_relative_to(raw_root) or not archive.resolve().is_relative_to(archive_root):
        raise QuestSpecError(f"Depot path escapes its source directory: {depot_path!r}")
    return raw, archive


def validate_depot_path(
    depot_path: Any,
    *,
    field: str,
    stage_id: str,
    diagnostics: list[Diagnostic],
) -> str:
    if _depot_parts(depot_path) is None:
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_depot_path",
                f"{field} must be an explicit base\\, ep1\\, or mod\\ depot path without traversal, empty components, or invalid filename characters",
                stage_id,
            )
        )
        return ""
    return depot_path


def load_spec(path: Path) -> tuple[QuestSpec | None, list[Diagnostic]]:
    diagnostics: list[Diagnostic] = []
    raw = read_json(path)
    authoring_source = raw if "composition" in raw else None
    if "composition" in raw:
        from quest_authoring import normalize_spec, AuthoringError
        try:
            raw = normalize_spec(raw)
        except AuthoringError as exc:
            return None, [Diagnostic("error", "invalid_composition", str(exc))]
    validate_flow_fields(raw, diagnostics)

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
        stage_prefabs = stage.get("phase_prefabs")
        if stage_prefabs is not None:
            if (
                not isinstance(stage_prefabs, list)
                or any(
                    not isinstance(value, str) or not value.startswith("#")
                    for value in stage_prefabs
                )
                or len(set(stage_prefabs)) != len(stage_prefabs)
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "invalid_stage_phase_prefabs",
                        f"{context}.phase_prefabs must contain unique shorthand NodeRefs",
                        stage_id or None,
                    )
                )
            elif any(value not in phase_prefabs for value in stage_prefabs):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "unknown_stage_phase_prefab",
                        f"{context}.phase_prefabs must be selected from the quest phase_prefabs",
                        stage_id or None,
                    )
                )
            if "inherit_phase_prefabs" in stage:
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "conflicting_stage_phase_prefabs",
                        f"{context} cannot combine phase_prefabs with inherit_phase_prefabs",
                        stage_id or None,
                    )
                )
        checkpoint = stage.get("checkpoint")
        retry_checkpoint = stage.get("retry_checkpoint", False)
        if checkpoint is not None and (
            not isinstance(checkpoint, str) or not checkpoint.strip()
        ):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_checkpoint",
                    f"{context}.checkpoint must be a non-empty string",
                    stage_id or None,
                )
            )
        if not isinstance(retry_checkpoint, bool):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "invalid_retry_checkpoint",
                    f"{context}.retry_checkpoint must be a boolean",
                    stage_id or None,
                )
            )
        elif retry_checkpoint and not isinstance(checkpoint, str):
            diagnostics.append(
                Diagnostic(
                    "error",
                    "missing_retry_checkpoint",
                    f"{context}.retry_checkpoint requires checkpoint",
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

        stage_definition = STAGE_REGISTRY.get(stage_type)
        if stage_definition is not None:
            stage_definition.validate(stage, context, stage_id, diagnostics)

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

    parallel_groups: list[ParallelGroup] = []
    parallel_value = raw.get("parallel_groups", [])
    stage_by_id = {stage.id: stage for stage in stages}
    stage_order = {stage.id: stage.index for stage in stages}
    claimed_parallel_stages: set[str] = set()
    seen_group_ids: set[str] = set()
    if not isinstance(parallel_value, list):
        diagnostics.append(
            Diagnostic(
                "error",
                "invalid_parallel_groups",
                "parallel_groups must be an array",
            )
        )
    else:
        for group_index, group in enumerate(parallel_value):
            context = f"parallel_groups[{group_index}]"
            if (
                not isinstance(group, dict)
                or set(group) != {"id", "branches"}
                or not isinstance(group.get("id"), str)
                or not ID_RE.fullmatch(group["id"])
                or not isinstance(group.get("branches"), list)
                or len(group["branches"]) < 2
                or any(
                    not isinstance(branch, list)
                    or not branch
                    or any(
                        not isinstance(stage_id, str) or not ID_RE.fullmatch(stage_id)
                        for stage_id in branch
                    )
                    for branch in group["branches"]
                )
            ):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "invalid_parallel_group",
                        f"{context} must contain an id and at least two non-empty stage-id branches",
                    )
                )
                continue
            group_id = group["id"]
            branches = tuple(tuple(branch) for branch in group["branches"])
            members = [stage_id for branch in branches for stage_id in branch]
            if group_id in seen_group_ids:
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "duplicate_parallel_group",
                        f"Duplicate parallel group id: {group_id}",
                    )
                )
            seen_group_ids.add(group_id)
            unknown_members = sorted(set(members) - set(stage_by_id))
            if unknown_members:
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "unknown_parallel_stage",
                        f"{context} references unknown stages: {', '.join(unknown_members)}",
                    )
                )
                continue
            if len(set(members)) != len(members):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "duplicate_parallel_stage",
                        f"{context} repeats a stage across branches",
                    )
                )
                continue
            overlap = sorted(set(members) & claimed_parallel_stages)
            if overlap:
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "overlapping_parallel_group",
                        f"{context} reuses stages from another group: {', '.join(overlap)}",
                    )
                )
                continue
            indices = sorted(stage_order[stage_id] for stage_id in members)
            if indices != list(range(indices[0], indices[-1] + 1)):
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "noncontiguous_parallel_group",
                        f"{context} stages must occupy one contiguous manifest span",
                    )
                )
                continue
            unsupported = sorted(
                stage_id
                for stage_id in members
                if stage_by_id[stage_id].type == "meet_contact"
                or stage_by_id[stage_id].data.get("checkpoint")
            )
            if unsupported:
                diagnostics.append(
                    Diagnostic(
                        "error",
                        "unsupported_parallel_stage",
                        f"{context} cannot contain meeting or checkpoint stages: {', '.join(unsupported)}",
                    )
                )
                continue
            claimed_parallel_stages.update(members)
            parallel_groups.append(ParallelGroup(group_id, branches))
    if parallel_groups and debug_fact is not None:
        diagnostics.append(
            Diagnostic(
                "error",
                "parallel_debug_unsupported",
                "debug_fact is not supported with parallel_groups",
            )
        )

    if diagnostics and any(item.level == "error" for item in diagnostics):
        return None, diagnostics
    spec = QuestSpec(
            path=path.resolve(),
            id=quest_id,
            title=title,
            description=description,
            phase_prefabs=tuple(phase_prefabs),
            parallel_groups=tuple(parallel_groups),
            debug_fact=debug_fact,
            stages=tuple(stages),
            entry_stage=raw.get("entry_stage"),
            external_facts=tuple(raw.get("external_facts", [])),
            external_events=tuple(raw.get("external_events", [])),
            completion=raw.get("completion"),
            authoring_source=authoring_source,
    )
    diagnostics.extend(validate_flow(spec))
    return (None if any(item.level == "error" for item in diagnostics) else spec), diagnostics


def collect_ref_values(value: Any) -> set[str]:
    refs: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "ref" and isinstance(child, str):
                refs.add(child)
            refs.update(collect_ref_values(child))
    elif isinstance(value, list):
        for child in value:
            refs.update(collect_ref_values(child))
    return refs


def audit_cyberpsycho_authoring(
    stage: CompiledStage, *, root: Path
) -> list[Diagnostic]:
    authoring = stage.data.get("authoring")
    if not isinstance(authoring, dict):
        return []
    diagnostics: list[Diagnostic] = []
    level = "warning" if stage.status == "planned" else "error"

    world_relative = authoring.get("world_spec")
    if isinstance(world_relative, str):
        world_path = root / Path(world_relative)
        if not world_path.is_file():
            diagnostics.append(
                Diagnostic(
                    level,
                    "missing_cyberpsycho_world_spec",
                    f"No world authoring spec found at {world_relative}",
                    stage.id,
                )
            )
        else:
            try:
                world = read_json(world_path)
            except QuestSpecError as exc:
                diagnostics.append(
                    Diagnostic(
                        level,
                        "invalid_cyberpsycho_world_spec",
                        str(exc),
                        stage.id,
                    )
                )
            else:
                communities: list[dict[str, Any]] = []
                if isinstance(world.get("community"), dict):
                    communities.append(world["community"])
                if isinstance(world.get("communities"), list):
                    communities.extend(
                        item
                        for item in world["communities"]
                        if isinstance(item, dict)
                    )
                community = next(
                    (
                        item
                        for item in communities
                        if item.get("ref") == stage.data["community"]
                    ),
                    None,
                )
                if community is None:
                    diagnostics.append(
                        Diagnostic(
                            level,
                            "missing_cyberpsycho_community",
                            f"{world_relative} does not define community "
                            f"{stage.data['community']}",
                            stage.id,
                        )
                    )
                else:
                    entries = (
                        community.get("entries")
                        if isinstance(community.get("entries"), list)
                        else [community]
                    )
                    boss_entry = next(
                        (
                            item
                            for item in entries
                            if isinstance(item, dict)
                            and item.get("entry") == stage.data["boss_entry"]
                        ),
                        None,
                    )
                    if boss_entry is None:
                        diagnostics.append(
                            Diagnostic(
                                level,
                                "missing_cyberpsycho_entry",
                                f"{stage.data['community']} does not define entry "
                                f"{stage.data['boss_entry']}",
                                stage.id,
                            )
                        )
                    elif boss_entry.get("character") != stage.data["boss_character"]:
                        diagnostics.append(
                            Diagnostic(
                                level,
                                "cyberpsycho_character_mismatch",
                                f"{stage.data['boss_entry']} uses "
                                f"{boss_entry.get('character')!r}; expected "
                                f"{stage.data['boss_character']}",
                                stage.id,
                            )
                        )
                    if (
                        stage.data.get("activate", True)
                        and community.get("active_on_start", 1) not in (0, False)
                    ):
                        diagnostics.append(
                            Diagnostic(
                                level,
                                "cyberpsycho_community_active_on_start",
                                f"{stage.data['community']} must use active_on_start: 0 "
                                "when the encounter activates it",
                                stage.id,
                            )
                        )

                required_refs = {
                    stage.data["activation_trigger"],
                }
                if isinstance(stage.data.get("arena_trigger"), str):
                    required_refs.add(stage.data["arena_trigger"])
                reveal_trigger = stage.data["reveal"].get("trigger")
                if isinstance(reveal_trigger, str):
                    required_refs.add(reveal_trigger)
                cleanup = stage.data.get("cleanup")
                if isinstance(cleanup, dict) and isinstance(
                    cleanup.get("trigger"), str
                ):
                    required_refs.add(cleanup["trigger"])
                alerted_path = stage.data.get("alerted_path")
                if isinstance(alerted_path, str):
                    required_refs.add(alerted_path)
                required_refs.update(
                    value
                    for value in stage.data.get("alerted_spots", [])
                    if isinstance(value, str)
                )
                missing_refs = sorted(required_refs - collect_ref_values(world))
                if missing_refs:
                    diagnostics.append(
                        Diagnostic(
                            level,
                            "missing_cyberpsycho_world_ref",
                            f"{world_relative} does not define encounter refs: "
                            + ", ".join(missing_refs),
                            stage.id,
                        )
                    )

    tweak_relative = authoring.get("tweak_file")
    if isinstance(tweak_relative, str):
        tweak_path = root / Path(tweak_relative)
        if not tweak_path.is_file():
            diagnostics.append(
                Diagnostic(
                    level,
                    "missing_cyberpsycho_tweak",
                    f"No TweakXL file found at {tweak_relative}",
                    stage.id,
                )
            )
        else:
            try:
                tweak_text = tweak_path.read_text(encoding="utf-8")
            except OSError as exc:
                diagnostics.append(
                    Diagnostic(
                        level,
                        "invalid_cyberpsycho_tweak",
                        f"Cannot read {tweak_relative}: {exc}",
                        stage.id,
                    )
                )
            else:
                header = re.search(
                    rf"(?m)^{re.escape(stage.data['boss_character'])}:\s*$",
                    tweak_text,
                )
                if header is None:
                    diagnostics.append(
                        Diagnostic(
                            level,
                            "missing_cyberpsycho_tweak_record",
                            f"{tweak_relative} does not define "
                            f"{stage.data['boss_character']}",
                            stage.id,
                        )
                    )
                else:
                    next_header = re.search(
                        r"(?m)^[A-Za-z][A-Za-z0-9_.]*:\s*$",
                        tweak_text[header.end():],
                    )
                    end = (
                        header.end() + next_header.start()
                        if next_header is not None
                        else len(tweak_text)
                    )
                    record = tweak_text[header.end():end]
                    requirements = {
                        r"(?m)^\s+rarity:\s*NPCRarity\.Boss\s*$": (
                            "boss HUD rarity"
                        ),
                        (
                            r"(?m:^\s+tags:\s*\[[^\]]*\bCyberpsycho\b[^\]]*\]\s*$)"
                            r"|(?ms:^\s+tags:\s*$.*?^\s+-\s*Cyberpsycho\s*$)"
                        ): "Cyberpsycho tag",
                        r"\bCharacter\.Cyberpsycho_ModGroup\b": (
                            "cyberpsycho stat group"
                        ),
                        r"\bCharacter\.Cyberpsycho_HitReaction_Resistance\b": (
                            "cyberpsycho hit-reaction resistance"
                        ),
                        r"\bTargetTracking\.DefaultPreset\b": (
                            "target tracking preset"
                        ),
                        r"\bUINameplate\.CombatSettings\b": (
                            "combat UI nameplate"
                        ),
                        r"\bScanningNPCPresets\.ScannerPreset_NPCFull\b": (
                            "full scanner preset"
                        ),
                    }
                    missing = [
                        label
                        for pattern, label in requirements.items()
                        if re.search(pattern, record) is None
                    ]
                    for field in (
                        "entityTemplatePath:",
                        "displayName:",
                        "fullDisplayName:",
                    ):
                        if field not in record:
                            missing.append(field.removesuffix(":"))
                    if re.search(
                        r"(?m)^\s+disableDefeatedState:\s*true\s*$",
                        record,
                        re.IGNORECASE,
                    ):
                        missing.append("disableDefeatedState must not be true")
                    if missing:
                        diagnostics.append(
                            Diagnostic(
                                level,
                                "incomplete_cyberpsycho_tweak",
                                f"{stage.data['boss_character']} is missing explicit "
                                "vanilla cyberpsycho requirements: "
                                + ", ".join(missing),
                                stage.id,
                            )
                        )
    return diagnostics


def audit_resources(spec: QuestSpec, *, root: Path = ROOT) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = audit_scene_contracts(spec, root)
    for stage in spec.stages:
        resources = []
        template = stage_template_resource(stage)
        if template is not None:
            resources.append(template)
        elif not emits_stage_phase(stage):
            resources.append(stage.phase_resource)
        if isinstance(stage.data.get("scene"), str):
            resources.append(stage.data["scene"])
        if isinstance(stage.data.get("launch_scene"), str):
            resources.append(stage.data["launch_scene"])
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
        if stage.type == "cyberpsycho_encounter":
            diagnostics.extend(
                audit_cyberpsycho_authoring(stage, root=root)
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


def validate_meeting_journal_bindings(stage: CompiledStage, phase: JsonObject) -> None:
    """Match child-owned objective/mappin changes to the root's typed paths.

    Descriptions are root-owned. Some custom meeting templates intentionally
    leave the objective active; check a child field only when that resource
    actually contains an operation on its journal class.
    """
    paths: dict[str, set[str]] = {}
    def visit(value: Any) -> None:
        if isinstance(value, dict):
            if value.get("$type") == "gameJournalPath":
                name = value.get("className", {}).get("$value")
                paths.setdefault(name, set()).add(value.get("realPath", ""))
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)
    visit(phase)
    for field, class_name in (("objective", "gameJournalQuestObjective"), ("mappin", "gameJournalQuestMapPin")):
        owned_paths = paths.get(class_name, set())
        if owned_paths and stage.data[field] not in owned_paths:
            raise QuestSpecError(
                f"Stage {stage.id} child {field} paths {sorted(owned_paths)} "
                f"do not match root binding {stage.data[field]}"
            )


def validate_stage_contract(stage: CompiledStage, phase: JsonObject) -> None:
    """Ensure typed runtime identifiers are actually represented by the child phase."""
    expected: list[tuple[str, str]] = []
    if stage.type == "meet_contact":
        validate_meeting_journal_bindings(stage, phase)
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
        if stage.data.get("completion_function"):
            expected.extend(
                (field, stage.data[field])
                for field in ("controller_class", "completion_function")
            )
            if stage.data.get("send_action", True):
                expected.append(("action", stage.data["action"]))
    elif stage.type == "deliver_drop_point":
        expected.extend(
            (field, stage.data[field]) for field in ("drop_point", "deposit_fact")
        )
        if stage.data.get("item_branches"):
            expected.extend(
                ("item_branches.condition", branch["condition"])
                for branch in stage.data["item_branches"]
            )
            expected.extend(
                ("item_branches.item", branch["item"])
                for branch in stage.data["item_branches"]
            )
        else:
            expected.append(("item", stage.data["item"]))
    elif stage.type == "phone_conversation":
        expected.extend(
            ("choices.set_fact", choice["set_fact"])
            for choice in stage.data.get("choices", [])
            if isinstance(choice.get("set_fact"), str)
        )
        for opening in stage.data.get("opening_branches", []):
            expected.append(("opening_branches.condition", opening["condition"]))
            if isinstance(opening.get("unless"), str):
                expected.append(("opening_branches.unless", opening["unless"]))
            expected.extend(
                ("opening_branches.messages", message)
                for message in opening["messages"]
            )
        for group in stage.data.get("conditional_message_groups", []):
            for branch in group["branches"]:
                expected.append(
                    ("conditional_message_groups.condition", branch["condition"])
                )
                expected.extend(
                    ("conditional_message_groups.messages", message)
                    for message in branch["messages"]
                )
        expected.extend(
            ("postscript_messages", message)
            for message in stage.data.get("postscript_messages", [])
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
        for branch in stage.data.get("outcome_branches", []):
            expected.extend(
                (
                    ("outcome_branches.condition", branch["condition"]),
                    ("outcome_branches.set_fact", branch["set_fact"]),
                )
            )
            expected.extend(
                ("outcome_branches.add_items", item)
                for item in branch.get("add_items", [])
            )
            expected.extend(
                ("outcome_branches.remove_items", item)
                for item in branch.get("remove_items", [])
            )
    elif stage.type == "acquire_item":
        expected.append(("item", stage.data["item"]))
    elif stage.type == "combat_encounter":
        expected.append(("community", stage.data["community"]))
        expected.extend(("entries", item) for item in stage.data.get("entries", []))
        if isinstance(stage.data.get("trigger"), str):
            expected.append(("trigger", stage.data["trigger"]))
    elif stage.type == "cyberpsycho_encounter":
        expected.extend(
            (
                ("community", stage.data["community"]),
                ("boss_entry", stage.data["boss_entry"]),
                ("activation_trigger", stage.data["activation_trigger"]),
                (
                    "resolution.spared_fact",
                    stage.data["resolution"]["spared_fact"],
                ),
                (
                    "resolution.killed_fact",
                    stage.data["resolution"]["killed_fact"],
                ),
            )
        )
        reveal_trigger = stage.data["reveal"].get("trigger")
        if isinstance(reveal_trigger, str):
            expected.append(("reveal.trigger", reveal_trigger))
        if isinstance(stage.data.get("arena_trigger"), str):
            expected.append(("arena_trigger", stage.data["arena_trigger"]))
        if isinstance(stage.data.get("alerted_path"), str):
            expected.append(("alerted_path", stage.data["alerted_path"]))
        player_defeat_scene = stage.data.get("player_defeat_scene")
        if isinstance(player_defeat_scene, dict):
            expected.extend(
                (
                    "player_defeat_scene.completion_branches.set_fact",
                    branch["set_fact"],
                )
                for branch in player_defeat_scene.get(
                    "completion_branches", []
                )
            )
        expected.extend(
            ("alerted_spots", value)
            for value in stage.data.get("alerted_spots", [])
        )
        cleanup = stage.data.get("cleanup")
        if isinstance(cleanup, dict) and isinstance(cleanup.get("trigger"), str):
            expected.append(("cleanup.trigger", cleanup["trigger"]))
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
            expected.extend(
                ("clues.grant_items", item)
                for item in clue.get("grant_items", [])
            )
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
        expected.extend(
            ("route_mappins", item)
            for item in stage.data.get("route_mappins", [])
        )
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
        if stage.type == "steal_vehicle":
            expected.append(("completion_fact", stage.data["completion_fact"]))
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
    elif stage.type == "braindance_analysis":
        expected.extend(
            (field, stage.data[field])
            for field in (
                "scene",
                "scene_origin",
                "player_anchor",
                "player_return",
                "completion_fact",
                "objective",
            )
        )
        expected.extend(
            ("clue_facts", fact)
            for fact in stage.data["clue_facts"]
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
    policy = stage.data.get("objective_lifecycle", {})
    if policy.get("on_enter") == "retain" and all(
        policy.get(f"on_{outcome}") == "retain" for outcome in stage_outcomes(stage)
    ):
        # The linker checks the prior and next owners; retaining an objective
        # deliberately emits no journal operation for it inside this phase.
        expected = [(field, value) for field, value in expected if field != "objective"]
    missing = [f"{field}={value}" for field, value in expected if value not in values]
    if missing:
        raise QuestSpecError(
            f"Stage {stage.id} child phase does not implement typed fields: "
            + ", ".join(missing)
        )


def stage_template_resource(stage: CompiledStage) -> str | None:
    return STAGE_REGISTRY[stage.type].template(stage.data)


def stage_builder_name(stage: CompiledStage) -> str | None:
    return STAGE_REGISTRY[stage.type].builder(stage.data)


def emits_stage_phase(stage: CompiledStage) -> bool:
    return stage_builder_name(stage) is not None or stage_template_resource(stage) is not None

def builtin_template_bindings(
    stage: CompiledStage,
    *,
    template_tokens: set[str] | None = None,
) -> dict[str, str]:
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
        route_mappins = stage.data.get("route_mappins")
        if route_mappins is None:
            route_mappins = [stage.data["mappin"]] * 3
        return {
            "{{community}}": stage.data["community"],
            "{{entry}}": stage.data["entry"],
            "{{destination_1}}": stage.data["destinations"][0],
            "{{destination_2}}": stage.data["destinations"][1],
            "{{destination_3}}": stage.data["destinations"][2],
            "{{objective}}": stage.data["objective"],
            "{{route_mappin_1}}": route_mappins[0],
            "{{route_mappin_2}}": route_mappins[1],
            "{{route_mappin_3}}": route_mappins[2],
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
        bindings = {
            "{{objective}}": stage.data["objective"],
            "{{vehicle_community}}": stage.data["vehicle_community"],
            "{{vehicle_entry}}": stage.data["vehicle_entry"],
            "{{mappin}}": stage.data["mappin"],
        }
        if stage.type == "steal_vehicle":
            bindings["{{completion_fact}}"] = stage.data["completion_fact"]
        return bindings
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
        bindings = {
            "{{completion_fact}}": stage.data["completion_fact"],
        }
        if (
            "{{player_vehicle_record}}" in (template_tokens or ())
            and "player_vehicle_record" in stage.data
        ):
            bindings["{{player_vehicle_record}}"] = stage.data["player_vehicle_record"]
        return bindings
    if stage.type == "braindance_analysis":
        return {
            "{{scene}}": stage.data["scene"],
            "{{scene_origin}}": stage.data["scene_origin"],
            "{{player_anchor}}": stage.data["player_anchor"],
            "{{player_return}}": stage.data["player_return"],
            "{{clue_fact_1}}": stage.data["clue_facts"][0],
            "{{clue_fact_2}}": stage.data["clue_facts"][1],
            "{{clue_fact_3}}": stage.data["clue_facts"][2],
            "{{completion_fact}}": stage.data["completion_fact"],
            "{{objective}}": stage.data["objective"],
        }
    return {}


def instantiate_stage_phase(stage: CompiledStage, archive_target: Path, *, template_document: JsonObject | None = None) -> JsonObject:
    template_resource = stage_template_resource(stage)
    if template_resource is None:
        raise QuestSpecError(f"Stage {stage.id} does not declare phase_template")
    raw_template, _ = resource_paths(template_resource)
    if template_document is None and not raw_template.is_file():
        raise QuestSpecError(
            f"Stage {stage.id} needs raw template {raw_template}; packed-only templates cannot be rewritten"
        )
    template = read_json(raw_template) if template_document is None else template_document
    bindings_value = stage.data.get("template_bindings")
    if bindings_value is None:
        tokens = set(re.findall(r"\{\{.*?\}\}", json.dumps(template.get("Data", {}))))
        bindings_value = builtin_template_bindings(stage, template_tokens=tokens)
    if not isinstance(bindings_value, dict) or not all(
        isinstance(key, str) and isinstance(value, str)
        for key, value in bindings_value.items()
    ):
        raise QuestSpecError(
            f"Stage {stage.id}.template_bindings must map strings to strings"
        )
    counts = {key: 0 for key in bindings_value}
    result = replace_template_scalars(template, dict(bindings_value), counts)
    unused = sorted(key for key, count in counts.items() if count == 0)
    if unused:
        raise QuestSpecError(
            f"Stage {stage.id} has template bindings not present in {template_resource}: "
            + ", ".join(unused)
        )
    unresolved = sorted(set(re.findall(r"\{\{.*?\}\}", json.dumps(result.get("Data", {})))))
    if unresolved:
        raise QuestSpecError(
            f"Stage {stage.id} has unresolved template tokens in instantiated phase Data: "
            + ", ".join(unresolved)
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

    conditional_groups: list[list[dict[str, Any]]] = []
    opening_branches = stage.data.get("opening_branches", [])
    if opening_branches:
        conditional_groups.append(opening_branches)
    conditional_groups.extend(
        group["branches"]
        for group in stage.data.get("conditional_message_groups", [])
    )
    previous_socket = "Out"
    for branches in conditional_groups:
        branch_tails: list[GraphNode] = []
        for opening in branches:
            condition = fact_condition_node(
                builder, next_id, opening["condition"]
            )
            next_id += 1
            builder.connect(previous, condition, source_socket=previous_socket)
            branch_previous = condition
            branch_previous_socket = "Out"
            unless_fact = opening.get("unless")
            if isinstance(unless_fact, str):
                unless_condition = fact_condition_node(
                    builder,
                    next_id,
                    unless_fact,
                    comparison="LessOrEqual",
                    value=0,
                )
                next_id += 1
                builder.connect(
                    previous,
                    unless_condition,
                    source_socket=previous_socket,
                )
                condition_join = logical_and_node(builder, next_id, 2)
                next_id += 1
                builder.connect(
                    condition,
                    condition_join,
                    destination_socket="In1",
                )
                builder.connect(
                    unless_condition,
                    condition_join,
                    destination_socket="In2",
                )
                branch_previous = condition_join
                branch_previous_socket = "Out1"
            for path in opening["messages"]:
                message = journal_entry_node(
                    builder, next_id, path, "gameJournalPhoneMessage", 1
                )
                next_id += 1
                builder.connect(
                    branch_previous,
                    message,
                    source_socket=branch_previous_socket,
                    destination_socket="Active",
                )
                branch_previous = message
                branch_previous_socket = "Out"
            branch_tails.append(branch_previous)
        opening_join = logical_xor_node(builder, next_id, len(branch_tails))
        next_id += 1
        for index, tail in enumerate(branch_tails, start=1):
            builder.connect(tail, opening_join, destination_socket=f"In{index}")
        previous = opening_join
        previous_socket = "Out1"

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

    for path in stage.data.get("postscript_messages", []):
        message = journal_entry_node(
            builder, next_id, path, "gameJournalPhoneMessage", 1
        )
        next_id += 1
        builder.connect(previous, message, destination_socket="Active")
        previous = message

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
    previous = phase_input
    if prerequisite := stage.data.get("prerequisite_fact"):
        previous = fact_condition_node(builder, 15, prerequisite)
        builder.connect(phase_input, previous)
    if delay_hours := stage.data.get("delay_game_hours", 0):
        days, hours = divmod(delay_hours, 24)
        delay = game_time_delay_node(
            builder, 16, days=days, hours=hours, minutes=0, seconds=0
        )
        builder.connect(previous, delay, destination_socket="In")
        previous = delay
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

    builder.connect(previous, message, destination_socket="Active")
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


def remove_item_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    item_id: str,
) -> GraphNode:
    params = builder.handles.wrap(
        {
            "$type": "questAddRemoveItem_NodeTypeParams",
            "entityRef": local_player_reference(builder),
            "flagItemAddedCallbackAsSilent": 1,
            "isPlayer": 0,
            "itemID": tweakdbid(item_id),
            "itemIDsToIgnoreOnRemove": [],
            "nodeType": "RemoveAll",
            "objectRef": entity_reference(),
            "quantity": 1,
            "removeAllQuantity": 0,
            "sendNotification": 0,
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


def checkpoint_node(
    builder: PhaseGraphBuilder,
    quest_id: int,
    name: str,
    *,
    retry_on_failure: bool = False,
) -> GraphNode:
    return builder.node(
        quest_id,
        "questCheckpointNodeDefinition",
        input_names=("In",),
        properties={
            "additionalEndGameRewardsTweak": [],
            "debugString": name,
            "endGameSave": 0,
            "ignoreSaveLocks": 0,
            "pointOfNoReturn": 0,
            "retryOnFailure": int(retry_on_failure),
            "saveLock": 0,
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
    if stage.data.get("start_fact"):
        builder.connect_to_earlier_input(previous, entered, destination_socket="In")
    else:
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


def build_outcome_interact_device_phase(
    stage: CompiledStage, archive_target: Path
) -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    previous: GraphNode = start
    objective: GraphNode | None = None
    mappin: GraphNode | None = None
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

    branch_tails: list[GraphNode] = []
    for branch in stage.data["outcome_branches"]:
        condition = fact_condition_node(builder, next_id, branch["condition"])
        next_id += 1
        builder.connect(completed, condition)
        branch_previous: GraphNode = condition
        for item in branch.get("remove_items", []):
            removed = remove_item_node(builder, next_id, item)
            next_id += 1
            builder.connect(branch_previous, removed)
            branch_previous = removed
        for item in branch.get("add_items", []):
            added = add_item_node(builder, next_id, item, 1)
            next_id += 1
            builder.connect(branch_previous, added)
            branch_previous = added
        outcome = fact_node(builder, next_id, branch["set_fact"])
        next_id += 1
        builder.connect(branch_previous, outcome)
        branch_tails.append(outcome)

    join = logical_xor_node(builder, next_id, len(branch_tails))
    next_id += 1
    for index, tail in enumerate(branch_tails, start=1):
        builder.connect(tail, join, destination_socket=f"In{index}")
    previous = join
    previous_socket = "Out1"
    if objective is not None:
        objective_done = objective_node(builder, next_id, stage.data["objective"])
        next_id += 1
        builder.connect(
            previous,
            objective_done,
            source_socket=previous_socket,
            destination_socket="Succeeded",
        )
        previous = objective_done
        previous_socket = "Out"
    if mappin is not None:
        mappin_done = mappin_node(builder, next_id, stage.data["mappin"])
        next_id += 1
        builder.connect(
            previous,
            mappin_done,
            source_socket=previous_socket,
            destination_socket="Inactive",
        )
        previous = mappin_done
        previous_socket = "Out"
    if stage.data.get("success_fact"):
        succeeded = fact_node(builder, next_id, stage.data["success_fact"])
        builder.connect(previous, succeeded, source_socket=previous_socket)
        previous = succeeded
    builder.connect_to_earlier_output(previous, end)
    return phase_document(builder, archive_target)


def build_outcome_delivery_phase(
    stage: CompiledStage, archive_target: Path
) -> JsonObject:
    builder = PhaseGraphBuilder()
    start, end = input_node(builder), output_node(builder)
    previous: GraphNode = start
    objective: GraphNode | None = None
    mappin: GraphNode | None = None
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
    if stage.data.get("mappin"):
        mappin = mappin_node(
            builder,
            next_id,
            stage.data["mappin"],
            disable_previous_mappins=True,
        )
        next_id += 1
        builder.connect(previous, mappin, destination_socket="Active")
        previous = mappin

    branch_tails: list[GraphNode] = []
    for branch in stage.data["item_branches"]:
        condition = fact_condition_node(builder, next_id, branch["condition"])
        next_id += 1
        inventory = inventory_condition_node(builder, next_id, branch["item"])
        next_id += 1
        reserve = reserve_drop_point_node(
            builder,
            next_id,
            branch["item"],
            stage.data["drop_point"],
        )
        next_id += 1
        deposited = fact_condition_node(builder, next_id, stage.data["deposit_fact"])
        next_id += 1
        builder.connect(previous, condition)
        builder.connect(condition, inventory)
        builder.connect(inventory, reserve)
        builder.connect(inventory, deposited)
        branch_tails.append(deposited)

    join = logical_xor_node(builder, next_id, len(branch_tails))
    next_id += 1
    for index, tail in enumerate(branch_tails, start=1):
        builder.connect(tail, join, destination_socket=f"In{index}")
    previous = join
    previous_socket = "Out1"
    if objective is not None:
        objective_done = objective_node(builder, next_id, stage.data["objective"])
        next_id += 1
        builder.connect(
            previous,
            objective_done,
            source_socket=previous_socket,
            destination_socket="Succeeded",
        )
        previous = objective_done
        previous_socket = "Out"
    if mappin is not None:
        mappin_done = mappin_node(builder, next_id, stage.data["mappin"])
        builder.connect(
            previous,
            mappin_done,
            source_socket=previous_socket,
            destination_socket="Inactive",
        )
        previous = mappin_done
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
        # Preserve reviewed per-quest combat metadata without changing the
        # primitive defaults used by other encounter and defense builders.
        if "threat_function" in stage.data:
            attack.data["function"] = cname(stage.data["threat_function"])
        if "threat_duration_seconds" in stage.data:
            attack.data["params"]["Data"]["duration"] = stage.data[
                "threat_duration_seconds"
            ]
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
        for item in clue.get("grant_items", []):
            granted = add_item_node(builder, next_id, item, 1)
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


STAGE_BUILDERS = {builder.__name__: builder for builder in (
    build_escort_phase,
    build_timed_defense_phase,
    build_choice_phase,
    build_investigation_phase,
    build_phone_job_offer_phase,
    build_phone_phase,
    build_reach_area_phase,
    build_leave_area_phase,
    build_acquire_item_phase,
    build_read_shard_phase,
    build_investigate_clues_phase,
    build_interact_device_phase,
    build_outcome_interact_device_phase,
    build_outcome_delivery_phase,
    build_combat_encounter_phase,
    build_cyberpsycho_encounter_phase,
    build_time_gate_phase,
    build_read_terminal_document_phase,
)}


def build_stage_phase(
    stage: CompiledStage,
    archive_target: Path,
    phase_prefabs: tuple[str, ...] = (),
    *, template_document: JsonObject | None = None,
) -> JsonObject:
    builder_name = stage_builder_name(stage)
    if builder_name is None:
        result = instantiate_stage_phase(stage, archive_target, template_document=template_document)
    else:
        result = STAGE_BUILDERS[builder_name](stage, archive_target)
    scoped_prefabs = stage.data.get("phase_prefabs")
    if isinstance(scoped_prefabs, list):
        inherited_prefabs = tuple(scoped_prefabs)
    else:
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
    apply_objective_lifecycle(stage, result)
    validate_handle_graph(result, context=f"Stage {stage.id}")
    validate_no_forward_handle_refs(result, context=f"Stage {stage.id}")
    validate_stage_contract(stage, result)
    validate_phase_ports(stage, result)
    validate_emitted_contract(stage, result)
    return result


def phase_node(builder: PhaseGraphBuilder, node_id: int, path: str, *,
               inputs: tuple[str, ...] = ("In1",), outputs: tuple[str, ...] = ("Out1",)) -> GraphNode:
    return builder.node(
        node_id,
        "questPhaseNodeDefinition",
        input_names=inputs,
        output_names=outputs,
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
    node_type["setExactValue"] = 1
    node_type["value"] = value
    return node


def build_orchestration_phase(spec: QuestSpec, archive_target: Path) -> JsonObject:
    if spec.entry_stage or spec.completion or any(
        set(stage.data) & {"inputs", "outcomes", "on"}
        or (stage.type == "meet_contact" and stage.data.get("objective_lifecycle"))
        for stage in spec.stages
    ):
        from quest_orchestration import build_explicit_orchestration
        result = build_explicit_orchestration(spec, archive_target)
        validate_handle_graph(result, context=f"Quest {spec.id} orchestration")
        validate_no_forward_handle_refs(result, context=f"Quest {spec.id} orchestration")
        return result
    builder = PhaseGraphBuilder()
    start = input_node(builder)
    end = output_node(builder)
    previous = start
    stage_by_id = {stage.id: stage for stage in spec.stages}
    group_by_first_index = {
        min(stage_by_id[stage_id].index for branch in group.branches for stage_id in branch): group
        for group in spec.parallel_groups
    }
    grouped_indices = {
        stage_by_id[stage_id].index
        for group in spec.parallel_groups
        for branch in group.branches
        for stage_id in branch
    }
    stage_index = 0
    while stage_index < len(spec.stages):
        group = group_by_first_index.get(stage_index)
        if group is not None:
            source_socket = "Out" if previous is start else "Out1"
            branch_tails: list[GraphNode] = []
            for branch in group.branches:
                branch_previous: GraphNode | None = None
                for stage_id in branch:
                    stage = stage_by_id[stage_id]
                    current = phase_node(builder, stage.node_id, stage.phase_resource)
                    if branch_previous is None:
                        builder.connect(
                            previous,
                            current,
                            source_socket=source_socket,
                            destination_socket="In1",
                        )
                    else:
                        builder.connect(
                            branch_previous,
                            current,
                            source_socket="Out1",
                            destination_socket="In1",
                        )
                    branch_previous = current
                if branch_previous is None:
                    raise QuestSpecError(f"Parallel group {group.id} has an empty branch")
                branch_tails.append(branch_previous)
            join = logical_and_node(builder, 800 + len(branch_tails) + stage_index, len(branch_tails))
            for branch_index, tail in enumerate(branch_tails, start=1):
                builder.connect(
                    tail,
                    join,
                    source_socket="Out1",
                    destination_socket=f"In{branch_index}",
                )
            previous = join
            stage_index = max(
                stage_by_id[stage_id].index
                for branch in group.branches
                for stage_id in branch
            ) + 1
            continue

        if stage_index in grouped_indices:
            stage_index += 1
            continue
        stage = spec.stages[stage_index]
        source_socket = "Out" if previous is start else "Out1"
        if stage.type == "meet_contact":
            journal_base = 100 + stage.index * 3
            opening_message_path = stage.data.get("opening_message")
            if isinstance(opening_message_path, str):
                opening_message = journal_entry_node(
                    builder,
                    600 + stage.index,
                    opening_message_path,
                    "gameJournalPhoneMessage",
                    1,
                )
                builder.connect(
                    previous,
                    opening_message,
                    source_socket=source_socket,
                    destination_socket="Active",
                )
                previous = opening_message
                source_socket = "Out"
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
        if isinstance(stage.data.get("checkpoint"), str):
            checkpoint = checkpoint_node(
                builder,
                700 + stage.index,
                stage.data["checkpoint"],
                retry_on_failure=stage.data.get("retry_checkpoint", False),
            )
            builder.connect(
                previous,
                checkpoint,
                source_socket=source_socket,
                destination_socket="In",
            )
            previous = checkpoint
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
        stage_index += 1
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
    diagnostics = tuple(diagnostics)
    buildable = all(stage.status == "ready" for stage in spec.stages) and not any(item.level == "error" for item in diagnostics)
    transitions = stage_transitions(spec)
    return {
        "schema_version": SCHEMA_VERSION,
        "quest": {
            "id": spec.id,
            "title": spec.title,
            "manifest": str(spec.path),
        },
        "linear_flow": [stage.id for stage in spec.stages],
        "contract_version": 1,
        "entry_stage": spec.entry_stage or spec.stages[0].id,
        "routing_mode": "parallel_groups" if spec.parallel_groups else "named_outcomes",
        "transitions": None if spec.parallel_groups else transitions,
        "contracts": {stage.id: contract_dict(stage) for stage in spec.stages},
        "buildable": buildable,
        "runtime_verified": False,
        "completion": spec.completion,
        "parallel_groups": [
            {
                "id": group.id,
                "branches": [list(branch) for branch in group.branches],
            }
            for group in spec.parallel_groups
        ],
        "stages": [
            {
                "index": stage.index,
                "node_id": stage.node_id,
                "id": stage.id,
                "type": stage.type,
                "status": stage.status,
                "phase_resource": stage.phase_resource,
                "phase_template": stage_template_resource(stage),
                "implementation": STAGE_REGISTRY[stage.type].mode(stage.data),
                "data": stage.data,
                "inputs": stage_inputs(stage),
                "outcomes": stage_outcomes(stage),
                "transitions": None if spec.parallel_groups else transitions[stage.id],
            }
            for stage in spec.stages
        ],
        "diagnostics": [item.as_dict() for item in diagnostics],
        "shipping_ready": buildable,  # Compatibility alias; not runtime evidence.
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


@dataclass(frozen=True)
class QuestArtifact:
    raw_path: Path
    archive_path: Path
    document: JsonObject
    stage_id: str | None = None


StageOverride = Callable[[CompiledStage, Path], JsonObject]
StageTransform = Callable[[CompiledStage, JsonObject], None]


def compile_artifacts(
    spec: QuestSpec, root_output: Path, root_archive: Path, *,
    child_root: Path | None = None,
    stage_overrides: Mapping[str, StageOverride] | None = None,
    stage_transforms: Mapping[str, StageTransform] | None = None,
    template_documents: Mapping[str, JsonObject] | None = None,
    root_override: Callable[[QuestSpec, Path], JsonObject] | None = None,
    project_root: Path | None = None,
) -> list[QuestArtifact]:
    """Construct and validate every phase before publishing any destination."""
    root_document = (root_override or build_orchestration_phase)(spec, root_archive)
    validate_handle_graph(root_document, context=f"Quest {spec.id}")
    validate_no_forward_handle_refs(root_document, context=f"Quest {spec.id}")
    artifacts = [QuestArtifact(root_output, root_archive, root_document)]
    overrides = stage_overrides or {}
    transforms = stage_transforms or {}
    unknown_hooks = (set(overrides) | set(transforms)) - {stage.id for stage in spec.stages}
    if unknown_hooks:
        raise QuestSpecError(f"Unknown stage hooks: {sorted(unknown_hooks)}")
    for stage in spec.stages:
        if stage.id not in overrides and not emits_stage_phase(stage):
            if set(stage.data) & {"inputs", "outcomes", "contract"}:
                raw, _ = resource_paths(stage.phase_resource)
                document = read_json(raw)
                validate_phase_ports(stage, document)
                validate_emitted_contract(stage, document)
            continue
        raw, archive = resource_paths(stage.phase_resource, project_root=project_root)
        if child_root is not None:
            raw = child_root / Path(*f"{stage.phase_resource}.json".split("\\"))
        if stage.id in overrides:
            document = overrides[stage.id](stage, archive)
            validate_stage_contract(stage, document)
            apply_objective_lifecycle(stage, document)
        else:
            document = build_stage_phase(stage, archive, spec.phase_prefabs,
                template_document=(template_documents or {}).get(stage_template_resource(stage)))
        if stage.id in transforms:
            # An explicit quest-owned hook can change lifecycle ownership (for
            # example GQT005 keeps its review objective active across handoff).
            transforms[stage.id](stage, document)
        validate_handle_graph(document, context=f"Stage {stage.id}")
        validate_no_forward_handle_refs(document, context=f"Stage {stage.id}")
        validate_phase_ports(stage, document)
        validate_emitted_contract(stage, document)
        artifacts.append(QuestArtifact(raw, archive, document, stage.id))
    if spec.authoring_source is not None:
        from quest_authoring import compose
        for depot, document in compose(spec.authoring_source).documents.items():
            raw, archive = resource_paths(depot, project_root=project_root)
            if child_root is not None:
                raw = child_root / Path(*f"{depot}.json".split("\\"))
            document["Header"]["ArchiveFileName"] = str(archive.resolve())
            artifacts.append(QuestArtifact(raw, archive, document))
    paths = [artifact.raw_path.resolve() for artifact in artifacts]
    if len(set(paths)) != len(paths):
        raise QuestSpecError("Quest artifacts contain duplicate destination paths")
    return artifacts


def compile_manifest_artifacts(
    manifest: Path, root_output: Path, root_archive: Path, *,
    allow_planned: bool = False, **options: Any,
) -> list[QuestArtifact]:
    spec, diagnostics = load_spec(manifest)
    if spec is not None:
        diagnostics.extend(audit_resources(spec))
    errors = [item.message for item in diagnostics if item.level == "error"]
    if spec is None or errors:
        raise QuestSpecError("Quest build failed: " + "; ".join(errors))
    if not allow_planned and any(stage.status == "planned" for stage in spec.stages):
        raise QuestSpecError("Quest build contains planned stages")
    return compile_artifacts(spec, root_output, root_archive, **options)


def publish_quest_artifacts(artifacts: list[QuestArtifact], *, ownership_path: Path) -> list[tuple[Path, Path]]:
    publication = publish_json_artifacts(
        artifact_documents(artifacts),
        ownership_path=ownership_path,
    )
    if publication.obsolete_paths:
        print("Obsolete generated outputs (retained for review): " + ", ".join(map(str, publication.obsolete_paths)), file=sys.stderr)
    return [(artifact.raw_path, artifact.archive_path) for artifact in artifacts]


def artifact_documents(artifacts: list[QuestArtifact]) -> dict[Path, JsonObject]:
    documents: dict[Path, JsonObject] = {}
    for artifact in artifacts:
        path = artifact.raw_path.resolve()
        if path in documents:
            raise QuestSpecError(f"Duplicate quest artifact destination: {path}")
        documents[path] = artifact.document
    return documents


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
    project = resolve_project(args.project) if getattr(args, "project", None) else owning_project(
        args.manifest, fallback=resource_project(f"mod/{spec.id}/", root=ROOT),
    )
    archive_target = project / "source/archive/mod" / spec.id / "phases" / f"{spec.id}.questphase"
    artifacts = compile_artifacts(spec, output, archive_target, child_root=output.parent / "children", project_root=project)
    children = [
        {"stage": artifact.stage_id, "resource": next(stage.phase_resource for stage in spec.stages if stage.id == artifact.stage_id), "output": str(artifact.raw_path)}
        for artifact in artifacts if artifact.stage_id is not None
    ]
    output_key = hashlib.sha256(str(output).encode("utf-8")).hexdigest()[:12]
    metadata_root = project / "generated" / "quest-builds" / spec.id / output_key
    plan_path = args.plan.resolve() if args.plan else metadata_root / "plan.json"
    documents = artifact_documents(artifacts)
    if plan_path in documents:
        raise QuestSpecError(f"Build plan collides with quest artifact: {plan_path}")
    documents[plan_path] = build_plan(spec, diagnostics)
    ownership_path = metadata_root / "outputs.json"
    publication = publish_json_artifacts(documents, ownership_path=ownership_path)
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
                "ownership": str(ownership_path),
                "obsolete_outputs": [str(path) for path in publication.obsolete_paths],
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
    compile_parser.add_argument("--project", help="Target project ID or directory; defaults to the manifest's owner")
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
