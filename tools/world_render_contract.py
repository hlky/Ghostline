"""Pure configuration and completeness contracts for the world tile renderer."""
from __future__ import annotations
import argparse
import json
import os
import re
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

SCHEMA_VERSION = 1

DEFAULT_YAW_OFFSETS = (0.0, 90.0, 180.0, 270.0)

DEFAULTS: dict[str, Any] = {
    "resolution": 768,
    "image_format": "WEBP",
    "image_quality": 90,
    "horizontal_fov_degrees": 80.0,
    "clip_start": 0.05,
    "clip_end": 2000.0,
    "eye_height": 1.65,
    "position_mode": "camera",
    "with_materials": True,
    "with_static_lights": False,
    "remap_depot": False,
    "reuse_mesh_cache": True,
    "yaw_offsets_degrees": list(DEFAULT_YAW_OFFSETS),
    "sun_energy": 2.5,
    "sun_angle_degrees": 4.0,
    "world_strength": 0.35,
    "transparent_background": False,
    "validation": {
        "enabled": True,
        "require_floor": False,
        "floor_max_distance": 3.0,
        "floor_clearance_min": 0.9,
        "floor_clearance_max": 2.5,
        "floor_normal_z_min": 0.25,
        "headroom_probe_distance": 8.0,
        "minimum_ceiling_height": 1.9,
        "surface_clearance": 0.12,
        "surface_probe_directions": 16,
        "forward_clearance": 0.18,
        "openness_probe_distance": 20.0,
    },
}

IMAGE_EXTENSIONS = {"WEBP": ".webp", "PNG": ".png", "JPEG": ".jpg"}

EXPECTED_CONTENT_KEYS = (
    "sector_jsons",
    "mesh_glbs",
    "imported_mesh_glbs",
    "entity_jsons",
    "appearance_jsons",
    "node_definitions",
    "node_instances",
)

def merge_dict(base: Mapping[str, Any], overlay: Mapping[str, Any]) -> dict[str, Any]:
    result = dict(base)
    for key, value in overlay.items():
        if isinstance(value, Mapping) and isinstance(result.get(key), Mapping):
            result[key] = merge_dict(result[key], value)
        else:
            result[key] = value
    return result

def normalise_option_aliases(value: Mapping[str, Any]) -> dict[str, Any]:
    """Accept authoring-manifest names without weakening the render schema."""

    result = dict(value)
    aliases = {
        "render_resolution": "resolution",
        "render_format": "image_format",
        "render_quality": "image_quality",
        "directions_degrees": "yaw_offsets_degrees",
        "eye_height_metres": "eye_height",
        "fov_degrees": "horizontal_fov_degrees",
        "static_lights": "with_static_lights",
    }
    for alias, canonical in aliases.items():
        if canonical not in result and alias in result:
            result[canonical] = result[alias]
    return result

def normalise_expected_content(value: object) -> dict[str, int]:
    """Return the strict content contract used by the tile completeness gate.

    ``expected`` was used by early proof-of-concept job files, so it remains a
    supported input alias.  The canonical job field is ``expected_content``.
    """

    if value is None:
        return {}
    if not isinstance(value, Mapping):
        raise ValueError("expected_content must be an object")
    source = dict(value)
    if "sector_jsons" not in source and "sector_count" in source:
        source["sector_jsons"] = source["sector_count"]
    result: dict[str, int] = {}
    for key in EXPECTED_CONTENT_KEYS:
        if key not in source:
            continue
        raw_count = source[key]
        if isinstance(raw_count, bool):
            raise ValueError(f"expected_content.{key} must be a non-negative integer")
        try:
            count = int(raw_count)
        except (TypeError, ValueError) as exc:
            raise ValueError(
                f"expected_content.{key} must be a non-negative integer"
            ) from exc
        if count < 0 or isinstance(raw_count, float) and not raw_count.is_integer():
            raise ValueError(f"expected_content.{key} must be a non-negative integer")
        result[key] = count
    return result

def count_coverage(expected: int | None, actual: int) -> dict[str, Any]:
    """Describe count coverage without hiding over-production or shortfalls."""

    record: dict[str, Any] = {"actual": int(actual), "expected": expected}
    if expected is None:
        record.update({"missing": None, "ratio": None, "complete": None})
        return record
    missing = max(0, int(expected) - int(actual))
    ratio = 1.0 if expected == 0 else min(1.0, float(actual) / float(expected))
    record.update(
        {
            "missing": missing,
            "ratio": round(ratio, 6),
            "complete": missing == 0,
        }
    )
    return record

def evaluate_content_coverage(
    expected: object, actual: Mapping[str, int]
) -> dict[str, Any]:
    """Evaluate staged and imported tile content against the job contract.

    The imported counters deliberately distinguish definitions from placement
    instances.  A sector can parse successfully while individual node types or
    mesh assets fail to materialise; that is the incompleteness this gate must
    expose instead of treating a valid camera render as a completed tile.
    """

    contract = normalise_expected_content(expected)
    required_actual = (
        "staged_sector_jsons",
        "imported_sector_jsons",
        "staged_mesh_glbs",
        "imported_mesh_glbs",
        "staged_entity_jsons",
        "staged_appearance_jsons",
        "staged_node_definitions",
        "imported_node_definitions",
        "expected_node_instances",
        "imported_node_instances",
        "imported_instance_records",
    )
    counters = {key: max(0, int(actual.get(key, 0))) for key in required_actual}
    coverage = {
        "sectors": {
            "staged": count_coverage(
                contract.get("sector_jsons"), counters["staged_sector_jsons"]
            ),
            "imported": count_coverage(
                contract.get("sector_jsons"), counters["imported_sector_jsons"]
            ),
        },
        "meshes": {
            "staged": count_coverage(
                contract.get("mesh_glbs"), counters["staged_mesh_glbs"]
            ),
            "imported": count_coverage(
                contract.get("imported_mesh_glbs", contract.get("mesh_glbs")),
                counters["imported_mesh_glbs"],
            ),
        },
        "entity_dependencies": {
            "entities": count_coverage(
                contract.get("entity_jsons"), counters["staged_entity_jsons"]
            ),
            "appearances": count_coverage(
                contract.get("appearance_jsons"),
                counters["staged_appearance_jsons"],
            ),
        },
        "nodes": {
            "staged_definitions": count_coverage(
                contract.get("node_definitions"),
                counters["staged_node_definitions"],
            ),
            "imported_definitions": count_coverage(
                contract.get("node_definitions"),
                counters["imported_node_definitions"],
            ),
            "imported_instances": count_coverage(
                contract.get("node_instances", counters["expected_node_instances"]),
                counters["imported_node_instances"],
            ),
            "instance_records": counters["imported_instance_records"],
        },
    }

    signals: list[dict[str, Any]] = []

    def require_coverage(code: str, record: Mapping[str, Any]) -> None:
        missing = record.get("missing")
        if isinstance(missing, int) and missing > 0:
            signals.append(
                {
                    "severity": "error",
                    "code": code,
                    "expected": record.get("expected"),
                    "actual": record.get("actual"),
                    "missing": missing,
                    "ratio": record.get("ratio"),
                }
            )

    require_coverage("staged_sector_json_shortfall", coverage["sectors"]["staged"])
    require_coverage("imported_sector_shortfall", coverage["sectors"]["imported"])
    require_coverage("staged_mesh_glb_shortfall", coverage["meshes"]["staged"])
    require_coverage("imported_mesh_shortfall", coverage["meshes"]["imported"])
    require_coverage(
        "staged_entity_json_shortfall",
        coverage["entity_dependencies"]["entities"],
    )
    require_coverage(
        "staged_appearance_json_shortfall",
        coverage["entity_dependencies"]["appearances"],
    )
    require_coverage(
        "staged_node_definition_shortfall",
        coverage["nodes"]["staged_definitions"],
    )
    require_coverage(
        "imported_node_definition_shortfall",
        coverage["nodes"]["imported_definitions"],
    )
    require_coverage(
        "imported_node_instance_shortfall",
        coverage["nodes"]["imported_instances"],
    )
    return {
        "expected": contract,
        "actual": counters,
        "coverage": coverage,
        "signals": signals,
    }

def signal_severity_counts(signals: Iterable[Mapping[str, Any]]) -> dict[str, int]:
    counts = {"error": 0, "warning": 0, "info": 0}
    for signal in signals:
        severity = str(signal.get("severity", "warning")).casefold()
        counts[severity] = counts.get(severity, 0) + 1
    return counts

def classify_render_status(
    valid_views: int, invalid_views: int, content_errors: int
) -> tuple[str, str | None]:
    """Combine camera validity and content completeness into a tile status."""

    if valid_views <= 0:
        return "failed", "No camera directions passed validation"
    if invalid_views > 0 or content_errors > 0:
        return "partial", None
    return "completed", None

def resolve_path(value: str | os.PathLike[str], base: Path) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = base / path
    return path.resolve()

def project_layout(value: Path) -> tuple[Path, Path]:
    """Return the nominal cpmodproj path and staged source/raw directory.

    The sector importer only uses the project path's parent and basename. A
    staging-only tree therefore does not need a fabricated project file.
    """

    value = value.resolve()
    if value.is_dir():
        if value.name.casefold() == "raw" and value.parent.name.casefold() == "source":
            project_root = value.parent.parent
            raw_root = value
        else:
            project_root = value
            raw_root = project_root / "source" / "raw"
        candidates = sorted(project_root.glob("*.cpmodproj"))
        project = (
            candidates[0]
            if candidates
            else project_root / f"{project_root.name}.cpmodproj"
        )
        return project, raw_root
    return value, value.parent / "source" / "raw"

def safe_name(value: object, fallback: str) -> str:
    name = re.sub(r"[^A-Za-z0-9._-]+", "_", str(value)).strip("._-")
    return name[:96] or fallback

def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Could not read JSON {path}: {exc}") from exc

def _xyz(value: object, label: str) -> list[float]:
    if isinstance(value, Mapping):
        lowered = {str(key).casefold(): item for key, item in value.items()}
        try:
            return [float(lowered[axis]) for axis in ("x", "y", "z")]
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"{label} must contain numeric X/Y/Z fields") from exc
    if (
        isinstance(value, Sequence)
        and not isinstance(value, (str, bytes))
        and len(value) == 3
    ):
        try:
            return [float(item) for item in value]
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{label} must contain three numeric values") from exc
    raise ValueError(f"{label} must be [x, y, z] or an X/Y/Z object")

def _normalise_directions(value: object) -> list[dict[str, Any]]:
    if value is None:
        value = DEFAULT_YAW_OFFSETS
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        raise ValueError("directions/yaw_offsets_degrees must be a list")
    directions: list[dict[str, Any]] = []
    names: set[str] = set()
    for index, entry in enumerate(value):
        if isinstance(entry, Mapping):
            offset = entry.get("offset_degrees", entry.get("yaw_offset_degrees"))
            if offset is None:
                offset = entry.get("yaw_degrees", 0.0)
            name = safe_name(
                entry.get("name", f"yaw_{float(offset) % 360:06.2f}"), f"view_{index}"
            )
        else:
            offset = entry
            name = safe_name(f"yaw_{float(offset) % 360:06.2f}", f"view_{index}")
        try:
            offset_number = float(offset)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Direction {index} has a non-numeric yaw offset") from exc
        if name in names:
            name = f"{name}_{index}"
        names.add(name)
        directions.append({"name": name, "offset_degrees": offset_number})
    if not directions:
        raise ValueError("At least one yaw direction is required")
    return directions

def _normalise_viewpoints(
    job: Mapping[str, Any], defaults: Mapping[str, Any], jobs_base: Path
) -> list[dict[str, Any]]:
    source: object = job.get("viewpoints")
    viewpoints_file = job.get("viewpoints_file", job.get("viewpoints_path"))
    if source is None and viewpoints_file:
        viewpoint_path = resolve_path(viewpoints_file, jobs_base)
        loaded = read_json(viewpoint_path)
        source = (
            loaded.get("viewpoints", loaded) if isinstance(loaded, Mapping) else loaded
        )
    if not isinstance(source, Sequence) or isinstance(source, (str, bytes)):
        raise ValueError("Each tile job requires a viewpoints list or viewpoints_file")

    result: list[dict[str, Any]] = []
    identifiers: set[str] = set()
    for index, raw in enumerate(source):
        if not isinstance(raw, Mapping):
            raise ValueError(f"Viewpoint {index} must be an object")
        identifier = safe_name(
            raw.get("id", raw.get("sample_id", f"viewpoint_{index:04d}")),
            f"viewpoint_{index:04d}",
        )
        if identifier in identifiers:
            raise ValueError(f"Duplicate viewpoint id after sanitising: {identifier}")
        identifiers.add(identifier)

        mode = str(
            raw.get("position_mode", defaults.get("position_mode", "camera"))
        ).casefold()
        position_value = raw.get("position")
        if raw.get("camera_position") is not None:
            position_value = raw["camera_position"]
            mode = "camera"
        elif raw.get("surface_position") is not None:
            position_value = raw["surface_position"]
            mode = "surface"
        if mode not in {"camera", "surface"}:
            raise ValueError(
                f"Viewpoint {identifier} position_mode must be camera or surface"
            )
        position = _xyz(position_value, f"viewpoint {identifier} position")
        eye_height = float(
            raw.get(
                "eye_height",
                raw.get(
                    "eye_height_metres",
                    defaults.get("eye_height", defaults.get("eye_height_metres", 1.65)),
                ),
            )
        )
        if mode == "surface":
            position[2] += eye_height

        orientation = raw.get("orientation", {})
        if not isinstance(orientation, Mapping):
            orientation = {}
        yaw = float(
            raw.get(
                "yaw_degrees",
                raw.get(
                    "heading_degrees",
                    orientation.get("yaw_degrees", orientation.get("yaw", 0.0)),
                ),
            )
        )
        pitch = float(
            raw.get(
                "pitch_degrees",
                orientation.get("pitch_degrees", orientation.get("pitch", 0.0)),
            )
        )
        directions = _normalise_directions(
            raw.get("directions", defaults.get("yaw_offsets_degrees"))
        )
        validation = merge_dict(
            defaults.get("validation", {}),
            raw.get("validation", {})
            if isinstance(raw.get("validation", {}), Mapping)
            else {},
        )
        result.append(
            {
                "id": identifier,
                "position": position,
                "source_position_mode": mode,
                "eye_height": eye_height,
                "yaw_degrees": yaw,
                "pitch_degrees": pitch,
                "directions": directions,
                "horizontal_fov_degrees": float(
                    raw.get(
                        "horizontal_fov_degrees",
                        defaults.get("horizontal_fov_degrees", 80.0),
                    )
                ),
                "validation": validation,
                "metadata": raw.get("metadata", {}),
            }
        )
    if not result:
        raise ValueError("Each tile job requires at least one viewpoint")
    return result

def parse_job_payload(path: Path, cli: argparse.Namespace) -> list[dict[str, Any]]:
    """Validate and resolve the version-1 batch schema.

    Top-level shape::

        {
          "schema_version": 1,
          "defaults": {"resolution": 768, "image_format": "WEBP", ...},
          "jobs": [{
            "tile_id": "kabuki-alley",
            "project": "staging/kabuki/kabuki.cpmodproj",
            "output": "renders/kabuki-alley",
            "expected_content": {
              "sector_jsons": 12,
              "mesh_glbs": 240,
              "node_definitions": 1800
            },
            "viewpoints": [{
              "id": "kabuki-0001",
              "position": [-1234.0, 456.0, 18.5],
              "position_mode": "camera",
              "yaw_degrees": 35.0
            }]
          }]
        }

    A viewpoint can instead use ``surface_position`` (eye height is added), and
    can override ``directions``, FOV, pitch, metadata, and validation settings.
    Tile jobs may carry arbitrary provenance fields; selected ones are copied to
    the report.
    """

    path = path.resolve()
    payload = read_json(path)
    if isinstance(payload, Mapping):
        version = int(payload.get("schema_version", SCHEMA_VERSION))
        if version != SCHEMA_VERSION:
            raise ValueError(f"Unsupported jobs schema_version {version}")
        raw_defaults = payload.get("defaults", {})
        raw_jobs = payload.get("jobs", payload.get("tiles"))
    else:
        raw_defaults = {}
        raw_jobs = payload
    if not isinstance(raw_defaults, Mapping):
        raise ValueError("jobs defaults must be an object")
    if not isinstance(raw_jobs, Sequence) or isinstance(raw_jobs, (str, bytes)):
        raise ValueError("jobs JSON must contain a jobs list")

    base = path.parent
    defaults = merge_dict(DEFAULTS, normalise_option_aliases(raw_defaults))
    cli_overrides: dict[str, Any] = {}
    for name in (
        "resolution",
        "image_format",
        "image_quality",
        "horizontal_fov_degrees",
        "with_materials",
        "with_static_lights",
    ):
        value = getattr(cli, name, None)
        if value is not None:
            cli_overrides[name] = value

    jobs: list[dict[str, Any]] = []
    tile_ids: set[str] = set()
    for index, raw_job in enumerate(raw_jobs):
        if not isinstance(raw_job, Mapping):
            raise ValueError(f"Job {index} must be an object")
        config = merge_dict(defaults, normalise_option_aliases(raw_job))
        config.update(cli_overrides)
        tile_id = safe_name(
            raw_job.get("tile_id", raw_job.get("id", f"tile_{index:03d}")),
            f"tile_{index:03d}",
        )
        if tile_id in tile_ids:
            raise ValueError(f"Duplicate tile_id after sanitising: {tile_id}")
        tile_ids.add(tile_id)

        project_value = raw_job.get(
            "project",
            raw_job.get(
                "project_file",
                raw_job.get(
                    "prepared_project",
                    raw_job.get(
                        "wolvenkit_project",
                        raw_job.get("raw_root", raw_job.get("staged_raw")),
                    ),
                ),
            ),
        )
        output_value = raw_job.get(
            "output",
            raw_job.get("output_directory", raw_job.get("render_output")),
        )
        if not project_value or not output_value:
            raise ValueError(f"Job {tile_id} requires project and output paths")
        config["tile_id"] = tile_id
        config["project"] = resolve_path(project_value, base)
        config["output"] = resolve_path(output_value, base)
        config["viewpoints"] = _normalise_viewpoints(raw_job, config, base)
        config["resolution"] = int(config["resolution"])
        if config["resolution"] < 64:
            raise ValueError(f"Job {tile_id} resolution must be at least 64")
        config["image_format"] = str(config["image_format"]).upper()
        if config["image_format"] not in IMAGE_EXTENSIONS:
            raise ValueError(f"Job {tile_id} has unsupported image_format")
        config["image_quality"] = max(0, min(100, int(config["image_quality"])))
        config["expected_content"] = normalise_expected_content(
            config.get("expected_content", config.get("expected"))
        )
        jobs.append(config)
    if not jobs:
        raise ValueError("jobs list is empty")
    return jobs
