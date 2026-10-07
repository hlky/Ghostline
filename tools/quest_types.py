"""Typed quest authoring model and diagnostics, independent of emitters."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ID_RE = re.compile(r"^[a-z][a-z0-9_]*$")


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
class ParallelGroup:
    id: str
    branches: tuple[tuple[str, ...], ...]


@dataclass(frozen=True)
class QuestSpec:
    path: Path
    id: str
    title: str
    description: str
    phase_prefabs: tuple[str, ...]
    parallel_groups: tuple[ParallelGroup, ...]
    debug_fact: str | None
    stages: tuple[CompiledStage, ...]
    entry_stage: str | None = None
    external_facts: tuple[str, ...] = ()
    external_events: tuple[str, ...] = ()
    completion: dict[str, Any] | None = None
    authoring_source: dict[str, Any] | None = None


def require_string(
    value: dict[str, Any], key: str, *, context: str, diagnostics: list[Diagnostic]
) -> str:
    result = value.get(key)
    if not isinstance(result, str) or not result.strip():
        diagnostics.append(
            Diagnostic(
                "error", "invalid_string", f"{context}.{key} must be a non-empty string"
            )
        )
        return ""
    return result
