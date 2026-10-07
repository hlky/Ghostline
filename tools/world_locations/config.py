"""Versioned configuration loading and path resolution."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Mapping


DEFAULT_CONFIG = Path(__file__).resolve().parents[1] / "world-location-capture-v1.json"
PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_config(path: Path | None = None) -> dict[str, Any]:
    selected = (path or DEFAULT_CONFIG).resolve()
    config = json.loads(selected.read_text(encoding="utf-8"))
    if config.get("schema_version") != 1:
        raise ValueError(f"unsupported config schema: {config.get('schema_version')!r}")
    validate_planning_config(config)
    config["_config_path"] = str(selected)
    return config


def validate_planning_config(config: Mapping[str, Any]) -> None:
    """Reject distances that cannot produce a finite, terminating capture plan."""
    groups = {
        "road_rules": (
            "short_road_threshold_m",
            "endpoint_inset_m",
            "interval_m",
            "minimum_arc_separation_m",
            "minimum_straight_separation_m",
        ),
        "sparse_road_rules": ("object_proximity_m", "minimum_separation_m"),
        "location_spacing_rules": ("minimum_separation_m",),
        "metadata_rules": ("runtime_area_fallback_m",),
    }
    for group, fields in groups.items():
        for field in fields:
            if field not in config.get(group, {}):
                continue
            value = config[group][field]
            try:
                number = float(value)
            except (ValueError, TypeError) as error:
                raise ValueError(
                    f"{group}.{field} must be a finite distance"
                ) from error
            if (
                isinstance(value, bool)
                or not math.isfinite(number)
                or number < 0
                or (field == "interval_m" and number == 0)
            ):
                raise ValueError(
                    f"{group}.{field} must be finite and {'positive' if field == 'interval_m' else 'nonnegative'}"
                )
    for rule in config.get("classification_rules", ()):
        for field in (
            "front_extent_m",
            "clearance_m",
            "minimum_candidate_separation_m",
        ):
            value = rule.get(field, 0)
            try:
                number = float(value)
            except (ValueError, TypeError) as error:
                raise ValueError(
                    f"classification rule {rule.get('id')}.{field} must be a finite distance"
                ) from error
            if isinstance(value, bool) or not math.isfinite(number) or number < 0:
                raise ValueError(
                    f"classification rule {rule.get('id')}.{field} must be finite and nonnegative"
                )
    for rule in config.get("scope_rules", ()):
        if not rule.get("enabled", True):
            continue
        coordinates = {
            f"{field}.{axis}": rule.get(field, {}).get(axis)
            for field in (
                "boundary_origin",
                "boundary_tangent",
                "in_scope_reference",
                "out_of_scope_reference",
            )
            if field != "out_of_scope_reference" or field in rule
            for axis in ("x", "y")
        }
        for field, value in {
            **coordinates,
            "margin_m": rule.get("margin_m", 0),
        }.items():
            try:
                valid = not isinstance(value, bool) and math.isfinite(float(value))
            except (ValueError, TypeError):
                valid = False
            if not valid:
                raise ValueError(f"scope rule {rule.get('id')}.{field} must be finite")


def resolve_project_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else (PROJECT_ROOT / path).resolve()


def output_paths(config: dict[str, Any]) -> dict[str, Path]:
    root = resolve_project_path(config["output_root"])
    return {
        "root": root,
        "database": root / config.get("database", "locations.sqlite3"),
        "runtime": root / config.get("runtime", "runtime"),
        "captures": root / config.get("captures", "captures"),
        "reports": root / config.get("reports", "reports"),
        "exports": root / config.get("exports", "exports"),
    }
