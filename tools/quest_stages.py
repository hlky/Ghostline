"""One registry for stage structure, semantic checks, and implementation policy.

The editor JSON Schema owns field names and structural requirements. This module
adds execution policy; builders themselves stay in the compiler/phase library.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from quest_stage_validation import VALIDATORS
from quest_types import Diagnostic

SCHEMA_PATH = Path(__file__).with_name("quest-schema-v1.json")
SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
SCHEMA_VERSION = SCHEMA["properties"]["schema_version"]["const"]
TOP_LEVEL_FIELDS = set(SCHEMA["properties"])
COMMON_STAGE_FIELDS = set(SCHEMA["$defs"]["baseStage"]["properties"])


@dataclass(frozen=True)
class StageImplementation:
    builder: str | None = None
    builtin_template: bool = True
    unsupported_fields: frozenset[str] = frozenset()


IMPLEMENTATIONS = {
    "acquire_item": StageImplementation(
        "build_acquire_item_phase", builtin_template=False
    ),
    "braindance_analysis": StageImplementation(),
    "carry_npc": StageImplementation(
        unsupported_fields=frozenset(
            {"completion_fact", "description_entry", "placement_slot"}
        )
    ),
    "choice_gate": StageImplementation(),
    "combat_encounter": StageImplementation(
        "build_combat_encounter_phase", builtin_template=False
    ),
    "cyberpsycho_encounter": StageImplementation(
        "build_cyberpsycho_encounter_phase", builtin_template=False
    ),
    "defend_target": StageImplementation(),
    "deliver_drop_point": StageImplementation(builtin_template=False),
    "deliver_vehicle": StageImplementation(
        unsupported_fields=frozenset(
            {"completion_fact", "description_entry", "mappin", "require_player_exit"}
        )
    ),
    "drive_to": StageImplementation(),
    "enter_vehicle": StageImplementation(),
    "escort_npc": StageImplementation(
        unsupported_fields=frozenset({"allow_combat_interrupt"})
    ),
    "hack_access_point": StageImplementation(builtin_template=False),
    "interact_device": StageImplementation(
        "build_interact_device_phase", builtin_template=False
    ),
    "investigate_clues": StageImplementation(
        "build_investigate_clues_phase", builtin_template=False
    ),
    "leave_area": StageImplementation("build_leave_area_phase", builtin_template=False),
    "meet_contact": StageImplementation(builtin_template=False),
    "optional_condition": StageImplementation(
        unsupported_fields=frozenset({"description_entry"})
    ),
    "phone_conversation": StageImplementation(
        "build_phone_phase", builtin_template=False
    ),
    "phone_job_offer": StageImplementation(
        "build_phone_job_offer_phase", builtin_template=False
    ),
    "plant_item": StageImplementation(),
    "reach_area": StageImplementation("build_reach_area_phase", builtin_template=False),
    "read_shard": StageImplementation("build_read_shard_phase", builtin_template=False),
    "read_terminal_document": StageImplementation(
        "build_read_terminal_document_phase", builtin_template=False
    ),
    "release_or_rescue_npc": StageImplementation(),
    "ride_with_contact": StageImplementation(),
    "steal_vehicle": StageImplementation(),
    "stealth_monitor": StageImplementation(),
    "time_gate": StageImplementation("build_time_gate_phase", builtin_template=False),
    "vehicle_cleanup": StageImplementation(),
}


def _string_property(value: dict[str, Any]) -> bool:
    if "$ref" in value:
        value = SCHEMA["$defs"][value["$ref"].rsplit("/", 1)[-1]]
    return value.get("type") == "string" or (
        bool(value.get("enum")) and all(isinstance(item, str) for item in value["enum"])
    )


@dataclass(frozen=True)
class StageDefinition:
    name: str
    structure: dict[str, Any]
    implementation: StageImplementation

    @property
    def fields(self) -> set[str]:
        return set(self.structure["properties"]) - {"type"}

    @property
    def required_strings(self) -> tuple[str, ...]:
        return tuple(
            field
            for field in self.structure.get("required", [])
            if _string_property(self.structure["properties"].get(field, {}))
        )

    def validate(
        self,
        data: dict[str, Any],
        context: str,
        stage_id: str,
        diagnostics: list[Diagnostic],
    ) -> None:
        if (
            self.name in {"escort_npc", "defend_target", "choice_gate", "investigate_clues"}
            and data.get("phase_template")
            and set(data) & {"actor_lifecycle", "objective_lifecycle"}
        ):
            diagnostics.append(Diagnostic("error", "custom_template_lifecycle", f"{context} lifecycle policies require the generated block; custom templates own their lifecycle", stage_id or None))
        validator = VALIDATORS.get(self.name)
        if validator is not None:
            validator(data, context, stage_id, diagnostics)

    def builder(self, data: dict[str, Any]) -> str | None:
        if data.get("phase_template"):
            return None
        if self.name == "interact_device" and data.get("outcome_branches"):
            return "build_outcome_interact_device_phase"
        if self.name == "hack_access_point" and data.get("completion_function"):
            return "build_interact_device_phase"
        if self.name == "deliver_drop_point" and data.get("item_branches"):
            return "build_outcome_delivery_phase"
        if self.name == "escort_npc" and (
            len(data.get("destinations", [None] * 3)) != 3
            or set(data)
            & {
                "actor_lifecycle",
                "objective_lifecycle",
                "cancellation_fact",
                "outcomes",
                "inputs",
                "description_entry",
                "failure_fact",
            }
        ):
            return "build_escort_phase"
        if self.name == "defend_target" and set(data) & {
            "duration_seconds",
            "attackers",
            "actor_lifecycle",
            "objective_lifecycle",
            "cancellation_fact",
            "outcomes",
            "inputs",
        }:
            return "build_timed_defense_phase"
        if self.name == "choice_gate" and (
            len(data.get("branches", [None] * 2)) != 2
            or set(data) & {"default_branch", "evaluation", "outcomes", "inputs"}
        ):
            return "build_choice_phase"
        if self.name == "investigate_clues" and (
            data.get("required_count", len(data.get("clues", [])))
            != len(data.get("clues", []))
            or data.get("scan_order") == "any"
            or set(data) & {"objective_lifecycle", "outcomes", "inputs"}
        ):
            return "build_investigation_phase"
        return self.implementation.builder

    def template(self, data: dict[str, Any]) -> str | None:
        explicit = data.get("phase_template")
        if isinstance(explicit, str):
            return explicit
        if self.builder(data):
            return None
        if not self.implementation.builtin_template:
            return None
        name = self.name
        if name == "defend_target" and data.get("block_on_failure", False):
            name = "defend_target_retry"
        return rf"mod\ghostline\quest_blocks\templates\{name}.questphase"

    def mode(self, data: dict[str, Any]) -> str:
        return "generated" if self.builder(data) else "template"


STAGE_REGISTRY = {}
for branch in SCHEMA["$defs"]["stage"]["oneOf"]:
    structure = branch["allOf"][1]
    name = structure["properties"]["type"]["const"]
    STAGE_REGISTRY[name] = StageDefinition(name, structure, IMPLEMENTATIONS[name])
if set(STAGE_REGISTRY) != set(IMPLEMENTATIONS):
    raise ValueError("Stage schema and implementation registry disagree")

# Compatibility exports for callers; these are derived, never independently edited.
SUPPORTED_STAGE_TYPES = set(STAGE_REGISTRY)
DIRECT_STAGE_TYPES = {
    name for name, entry in STAGE_REGISTRY.items() if entry.implementation.builder
}
TEMPLATE_REQUIRED_STAGE_TYPES = {
    name
    for name, entry in STAGE_REGISTRY.items()
    if entry.implementation.builtin_template
}
BUILTIN_TEMPLATE_RESOURCES = {
    name: STAGE_REGISTRY[name].template({}) for name in TEMPLATE_REQUIRED_STAGE_TYPES
}
BUILTIN_UNSUPPORTED_FIELDS = {
    name: entry.implementation.unsupported_fields
    for name, entry in STAGE_REGISTRY.items()
    if entry.implementation.unsupported_fields
}
STAGE_IMPLEMENTATION_MODE = {
    name: entry.mode({}) for name, entry in STAGE_REGISTRY.items()
}
STAGE_REQUIRED_FIELDS = {
    name: entry.required_strings for name, entry in STAGE_REGISTRY.items()
}
STAGE_TYPE_FIELDS = {name: entry.fields for name, entry in STAGE_REGISTRY.items()}


def reference_table() -> str:
    rows = [
        "| Type | Default implementation | Required structural fields |",
        "| --- | --- | --- |",
    ]
    for name, entry in STAGE_REGISTRY.items():
        required = (
            ", ".join(f"`{field}`" for field in entry.structure.get("required", []))
            or "See semantic constraints below."
        )
        mode = (
            "template or generated"
            if name
            in {
                "hack_access_point",
                "deliver_drop_point",
                "escort_npc",
                "defend_target",
                "choice_gate",
            }
            else entry.mode({})
        )
        rows.append(f"| `{name}` | {mode} | {required} |")
    return "\n".join(rows)
