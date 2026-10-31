"""Versioned configuration loading and path resolution."""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Mapping


DEFAULT_CONFIG = Path(__file__).resolve().parents[1] / "world-location-capture-roads-v1.json"
PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_config(path: Path | None = None) -> dict[str, Any]:
    selected = (path or DEFAULT_CONFIG).resolve()
    config = json.loads(selected.read_text(encoding="utf-8"))
    if config.get("schema_version") != 1:
        raise ValueError(f"unsupported config schema: {config.get('schema_version')!r}")
    if config.get("hazard_exclusions_file") and "hazard_rules" not in config:
        hazards = json.loads((selected.parent / config["hazard_exclusions_file"]).read_text(encoding="utf-8"))
        config.update(hazards)
    validate_planning_config(config)
    config["_config_path"] = str(selected)
    return config


def validate_planning_config(config: Mapping[str, Any]) -> None:
    """Reject distances that cannot produce a finite, terminating capture plan."""
    from .hazards import validate_hazard_rules
    validate_hazard_rules(config)
    groups = {
        "road_rules": (
            "short_road_threshold_m",
            "endpoint_inset_m",
            "interval_m",
            "minimum_arc_separation_m",
            "minimum_straight_separation_m",
            "global_minimum_separation_m",
        ),
        "sparse_road_rules": ("object_proximity_m", "minimum_separation_m"),
        "location_spacing_rules": ("minimum_separation_m",),
        "metadata_rules": ("runtime_area_fallback_m",),
        "fake_door_rules": ("outward_distance_m", "building_distance_m"),
        "vending_machine_rules": ("minimum_separation_m",),
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
            positive = field in ("interval_m", "outward_distance_m", "building_distance_m")
            if (
                isinstance(value, bool)
                or not math.isfinite(number)
                or number < 0
                or (positive and number == 0)
            ):
                raise ValueError(
                    f"{group}.{field} must be finite and {'positive' if positive else 'nonnegative'}"
                )
    vending_maximum = config.get("vending_machine_rules", {}).get("maximum_locations", 2000)
    if isinstance(vending_maximum, bool) or not isinstance(vending_maximum, int) or vending_maximum <= 0:
        raise ValueError("vending_machine_rules.maximum_locations must be a positive integer")
    fake_doors = config.get("fake_door_rules", {})
    if "include_rule_ids" in fake_doors:
        included = fake_doors["include_rule_ids"]
        if not isinstance(included, list) or not included or any(
            not isinstance(rule, str) or rule not in {"fake_door_v1", "fake_garage_door_v1"} for rule in included
        ):
            raise ValueError("fake_door_rules.include_rule_ids must select fake door or garage rules")
    if float(fake_doors.get("building_distance_m", 15)) <= float(fake_doors.get("outward_distance_m", 1.5)):
        raise ValueError("fake_door_rules.building_distance_m must exceed outward_distance_m")
    for category, profile in config.get("site_survey_rules", {}).items():
        if "ground_reference_categories" in profile:
            from .site_surveys import GROUND_CATEGORIES
            categories = profile["ground_reference_categories"]
            if not isinstance(categories, list) or not categories or any(
                not isinstance(value, str) or value not in GROUND_CATEGORIES for value in categories
            ):
                raise ValueError(f"Invalid ground reference categories for {category}")
        if profile.get("mode") not in {"detail_approach", "entrance_lobby", "two_sides", "ground_context", "usable_side_pair"}:
            raise ValueError(f"Unknown site survey mode for {category}")
        labels = profile.get("view_labels", [])
        if len(labels) != 2 or any(not isinstance(label, str) or not label.strip() for label in labels) or labels[0] == labels[1]:
            raise ValueError(f"Site survey {category} needs two distinct view labels")
        for field in ("near_distance_m", "far_distance_m", "minimum_anchor_separation_m", "minimum_ground_reference_distance_m", "maximum_ground_reference_distance_m", "maximum_ground_reference_drop_m", "ground_reference_height_ratio"):
            value = profile.get(field, 0 if field == "minimum_anchor_separation_m" else 1)
            try:
                number = float(value)
            except (TypeError, ValueError) as error:
                raise ValueError(f"Invalid site survey distance: {category}.{field}") from error
            if isinstance(value, bool) or not math.isfinite(number) or number < 0 or (number == 0 and field != "minimum_anchor_separation_m"):
                raise ValueError(f"Invalid site survey distance: {category}.{field}")
        if profile["mode"] == "usable_side_pair" and profile.get("front_axis") not in {"+x", "-x", "+y", "-y"}:
            raise ValueError(f"Site survey {category} needs a valid local front_axis")
        if profile["mode"] in {"detail_approach", "usable_side_pair"} and float(profile.get("far_distance_m", 12)) <= float(profile.get("near_distance_m", 3)):
            raise ValueError(f"Site survey {category} far distance must exceed near distance")
        if profile["mode"] == "ground_context" and float(profile.get("minimum_ground_reference_distance_m", 4)) > float(profile.get("maximum_ground_reference_distance_m", 25)):
            raise ValueError(f"Site survey {category} ground-reference minimum exceeds maximum")
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
