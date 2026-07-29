"""Headless Blender renderer for prepared Ghostline world-location tiles.

Invoke through Blender so arguments after ``--`` are owned by this script::

    blender --background --factory-startup --python tools/world_location_render_blender.py -- \
        --jobs converted/world-location-database/six-tile-jobs.json \
        --batch-report converted/world-location-database/six-tile-render-report.json

The jobs file may be a list or an object with ``defaults`` and ``jobs`` keys.
See ``parse_job_payload`` for the deliberately small, versioned input schema.
The module guards Blender imports so ordinary Python can import and compile it.
"""

from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import math
import os
import re
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence, TextIO

SCRIPT_DIRECTORY = Path(__file__).resolve().parent
if str(SCRIPT_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIRECTORY))

from world_location_world import blender_node_is_visual

try:  # Blender-only modules; keep import and py_compile useful outside Blender.
    import bpy  # type: ignore[import-not-found]
    from mathutils import Vector  # type: ignore[import-not-found]
except ImportError:  # pragma: no cover - exercised by regular Python, not Blender.
    bpy = None
    Vector = None


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
IMPORT_LOG_SIGNAL_SEVERITY = {
    "mesh_not_found": "error",
    "entity_import_failed": "error",
    "mesh_import_failed": "error",
    "tracebacks": "error",
    "missing_material_json": "warning",
}
MATERIAL_CACHE: dict[str, Any] = {}
MATERIAL_CACHE_STATS = {"hits": 0, "misses": 0}
ACTIVE_MASTER_CACHE_KEY: str | None = None


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def require_blender() -> None:
    if bpy is None or Vector is None:
        raise RuntimeError(
            "This renderer must run inside Blender. Use: blender --background "
            "--python tools/world_location_render_blender.py -- --jobs <jobs.json>"
        )


def ensure_cp77_addon() -> None:
    """Enable the installed importer when Blender was started factory-clean."""

    require_blender()
    if bpy.context.preferences.addons.get("i_scene_cp77_gltf") is None:
        try:
            result = bpy.ops.preferences.addon_enable(module="i_scene_cp77_gltf")
        except Exception as exc:
            raise RuntimeError(
                "Cyberpunk 2077 Blender add-on is installed but could not be enabled"
            ) from exc
        if "FINISHED" not in result:
            raise RuntimeError("Blender did not enable the Cyberpunk 2077 add-on")
    if bpy.context.preferences.addons.get("i_scene_cp77_gltf") is None:
        raise RuntimeError("Cyberpunk 2077 Blender add-on is not installed or enabled")


def apply_cp77_addon_compatibility_shims(
    import_common: Any, addon_colors: Any
) -> list[str]:
    """Patch narrowly-scoped importer regressions in the installed add-on.

    Cyberpunk IO Suite 1.8.0 references ``bcolors`` from ``import_common``
    without importing it.  The failure occurs after a geometry-only GLB has
    loaded, while the sector importer is cloning its requested appearances,
    and otherwise discards that master asset.  Supplying the add-on's own
    colour helper restores the intended warning path without changing import
    semantics or modifying the installed add-on.
    """

    applied: list[str] = []
    if not hasattr(import_common, "bcolors"):
        import_common.bcolors = addon_colors
        applied.append("import_common.bcolors")
    return applied


def blender_arguments() -> list[str]:
    return sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render prepared Cyberpunk world-location tiles in headless Blender."
    )
    parser.add_argument("--jobs", required=True, type=Path, help="Batch jobs JSON")
    parser.add_argument("--batch-report", type=Path)
    parser.add_argument("--resolution", type=int, default=None)
    parser.add_argument(
        "--format",
        dest="image_format",
        choices=sorted(IMAGE_EXTENSIONS),
        default=None,
    )
    parser.add_argument("--quality", dest="image_quality", type=int, default=None)
    parser.add_argument(
        "--horizontal-fov",
        dest="horizontal_fov_degrees",
        type=float,
        default=None,
    )
    static_lights = parser.add_mutually_exclusive_group()
    static_lights.add_argument(
        "--with-static-lights", dest="with_static_lights", action="store_true"
    )
    static_lights.add_argument(
        "--without-static-lights", dest="with_static_lights", action="store_false"
    )
    materials = parser.add_mutually_exclusive_group()
    materials.add_argument(
        "--with-materials",
        dest="with_materials",
        action="store_true",
        help="Import Cyberpunk material sidecars (overrides jobs JSON).",
    )
    materials.add_argument(
        "--without-materials",
        dest="with_materials",
        action="store_false",
        help="Import geometry without Cyberpunk materials (overrides jobs JSON).",
    )
    parser.set_defaults(with_static_lights=None, with_materials=None)
    parser.add_argument(
        "--fail-on-invalid",
        action="store_true",
        help=(
            "Return a failing process status if a camera direction is invalid "
            "or required tile content is incomplete."
        ),
    )
    parser.add_argument(
        "--fail-fast", action="store_true", help="Stop after the first failed tile."
    )
    return parser.parse_args(blender_arguments())


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


def write_json_atomic(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        temporary.write_text(
            json.dumps(payload, indent=2, sort_keys=False, allow_nan=False) + "\n",
            encoding="utf-8",
        )
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


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


def enable_material_cache() -> None:
    """Reuse identical CP77 materials without flattening imported mesh instances."""

    ensure_cp77_addon()
    try:
        from i_scene_cp77_gltf.main.setup import MaterialBuilder
    except ImportError as exc:
        raise RuntimeError("Cyberpunk 2077 Blender add-on is not enabled") from exc
    if getattr(MaterialBuilder, "_ghostline_world_cache_enabled", False):
        return
    original_create = MaterialBuilder.create

    def cached_create(builder: Any, materials: Any, material_index: int) -> Any:
        if not materials:
            return original_create(builder, materials, material_index)
        raw_material = materials[material_index]
        signature = hashlib.sha1(
            json.dumps(
                {
                    "material_repo": os.path.normcase(
                        os.path.abspath(str(builder.BasePath))
                    ),
                    "image_format": getattr(builder, "image_format", None),
                    "material": raw_material,
                },
                sort_keys=True,
                separators=(",", ":"),
                default=str,
            ).encode("utf-8")
        ).hexdigest()
        cached = MATERIAL_CACHE.get(signature)
        if cached is not None and cached.name in bpy.data.materials:
            MATERIAL_CACHE_STATS["hits"] += 1
            return cached
        material = original_create(builder, materials, material_index)
        MATERIAL_CACHE_STATS["misses"] += 1
        if material is not None:
            material.use_fake_user = True
            material["ghostline_world_material_cache"] = signature
            MATERIAL_CACHE[signature] = material
        return material

    MaterialBuilder.create = cached_create
    MaterialBuilder._ghostline_world_cache_enabled = True


def collection_tree(root: Any) -> Iterable[Any]:
    yield root
    for child in root.children:
        yield from collection_tree(child)


def master_collection() -> Any | None:
    return bpy.data.collections.get("MasterInstances") if bpy is not None else None


def clear_tile_scene(keep_master_instances: bool) -> dict[str, int]:
    """Remove tile-specific data while optionally retaining safe asset masters."""

    require_blender()
    master = master_collection() if keep_master_instances else None
    kept_collections = list(collection_tree(master)) if master is not None else []
    kept_collection_ids = {item.as_pointer() for item in kept_collections}
    kept_object_ids = {
        obj.as_pointer()
        for collection in kept_collections
        for obj in collection.objects
    }

    removed_objects = 0
    for obj in list(bpy.data.objects):
        if obj.as_pointer() not in kept_object_ids:
            bpy.data.objects.remove(obj, do_unlink=True)
            removed_objects += 1
    removed_collections = 0
    for collection in list(bpy.data.collections):
        if collection.as_pointer() not in kept_collection_ids:
            bpy.data.collections.remove(collection, do_unlink=True)
            removed_collections += 1

    for datablocks in (
        bpy.data.cameras,
        bpy.data.lights,
        bpy.data.curves,
        bpy.data.meshes,
        bpy.data.armatures,
        bpy.data.actions,
        bpy.data.images,
    ):
        for datablock in list(datablocks):
            if datablock.users == 0:
                datablocks.remove(datablock)
    for material in list(bpy.data.materials):
        if material.users == 0 and not material.get("ghostline_world_material_cache"):
            bpy.data.materials.remove(material)
    bpy.context.scene.camera = None
    bpy.context.view_layer.update()
    return {
        "removed_objects": removed_objects,
        "removed_collections": removed_collections,
        "kept_master_objects": len(kept_object_ids),
        "kept_master_collections": len(kept_collection_ids),
    }


class Tee(io.TextIOBase):
    def __init__(self, *streams: TextIO) -> None:
        self.streams = streams

    def write(self, value: str) -> int:
        for stream in self.streams:
            stream.write(value)
        return len(value)

    def flush(self) -> None:
        for stream in self.streams:
            stream.flush()


def import_log_signals(path: Path) -> dict[str, Any]:
    patterns = {
        "mesh_not_found": re.compile(
            r"Mesh(?: .*?)?(?:not found|does not exist)", re.I
        ),
        "entity_import_failed": re.compile(r"Failed during Entity import", re.I),
        "mesh_import_failed": re.compile(r"failed on\s+.*\.(?:glb|mesh)", re.I),
        "tracebacks": re.compile(r"^Traceback \(most recent call last\):", re.M),
        "missing_material_json": re.compile(r"No material json found", re.I),
    }
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return {"error": str(exc), "counts": {}}
    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "counts": {
            name: len(pattern.findall(text)) for name, pattern in patterns.items()
        },
        "tail": text.splitlines()[-40:],
    }


def _appearance_name(value: object) -> str:
    if isinstance(value, Mapping):
        value = value.get("$value", "")
    name = str(value or "").strip()
    return name or "default"


def _mesh_asset_key(mesh: object, appearance: object) -> tuple[str, str]:
    return (
        str(mesh or "").replace("/", "\\").casefold(),
        _appearance_name(appearance).casefold(),
    )


def native_pbr_asset_index(config: Mapping[str, Any]) -> dict[tuple[str, str], Path]:
    rows = config.get("native_pbr_assets", [])
    if not isinstance(rows, Sequence) or isinstance(rows, (str, bytes)):
        raise ValueError("native_pbr_assets must be an array")
    result: dict[tuple[str, str], Path] = {}
    for row in rows:
        if not isinstance(row, Mapping):
            raise ValueError("native_pbr_assets entries must be objects")
        mesh = row.get("depot_path", row.get("mesh"))
        appearance = row.get("appearance", "default")
        glb_value = row.get("glb")
        if not mesh or not glb_value:
            raise ValueError("native PBR assets require mesh/depot_path, appearance, and glb")
        glb = Path(str(glb_value)).resolve()
        if glb.is_file():
            result[_mesh_asset_key(mesh, appearance)] = glb
    return result


def import_native_pbr_master(
    glb: Path,
    mesh_path: str,
    appearance: str,
    masters: Any,
    import_common: Any,
) -> Any:
    """Import one item-style PBR GLB as a sector-instancing master."""

    existing = [
        collection
        for collection in masters.children
        if collection.get("meshpath") == mesh_path
        and collection.get("appearance") == appearance
    ]
    if existing:
        return existing[0]

    groupname = import_common.get_groupname(mesh_path, appearance)
    named = bpy.data.collections.get(groupname)
    if named is not None and not any(child == named for child in masters.children):
        named.name = f"{groupname}__source"
    collection = bpy.data.collections.new(groupname)
    masters.children.link(collection)
    collection["meshpath"] = mesh_path
    collection["appearance"] = appearance
    collection["native_pbr_glb"] = str(glb)
    before_objects = {obj.as_pointer() for obj in bpy.data.objects}
    try:
        result = bpy.ops.import_scene.gltf(filepath=str(glb))
        if "FINISHED" not in result:
            raise RuntimeError(f"Blender's native glTF importer failed for {glb}")
    except Exception:
        bpy.data.collections.remove(collection, do_unlink=True)
        raise
    imported = [
        obj for obj in bpy.data.objects if obj.as_pointer() not in before_objects
    ]
    if not any(obj.type == "MESH" for obj in imported):
        bpy.data.collections.remove(collection, do_unlink=True)
        raise RuntimeError(f"Native PBR GLB contains no meshes: {glb}")

    for obj in imported:
        for prior in list(obj.users_collection):
            prior.objects.unlink(obj)
        collection.objects.link(obj)
    return collection


def native_pbr_mesh_loader(
    assets: Mapping[tuple[str, str], Path],
    sidecar_loader: Any,
    import_common: Any,
    statistics: dict[str, Any],
) -> Any:
    """Bridge native PBR GLBs and RED sidecars into sector placement import."""

    def load(
        meshes_w_apps: Mapping[str, Any],
        path: str = "",
        from_mesh_no: int = 0,
        to_mesh_no: int = 10_000_000,
        with_mats: bool = False,
        glbs: Sequence[str] = (),
        mesh_jsons: Sequence[str] = (),
        Masters: Any | None = None,
        generate_overrides: bool = False,
    ) -> None:
        if Masters is None:
            raise RuntimeError("Sector importer did not provide MasterInstances")
        sidecar_meshes: dict[str, Any] = {}
        total = len(meshes_w_apps)
        for position, (mesh_path, descriptor) in enumerate(meshes_w_apps.items(), start=1):
            if position - 1 < from_mesh_no or position - 1 > to_mesh_no:
                continue
            raw_groups = descriptor.get("apps", [[]]) if isinstance(descriptor, Mapping) else [[]]
            raw_apps = raw_groups[0] if raw_groups else []
            requested: list[tuple[object, str]] = []
            for raw in raw_apps:
                appearance = _appearance_name(raw)
                if appearance not in {name for _, name in requested}:
                    requested.append((raw, appearance))
            if not requested:
                requested = [("default", "default")]

            missing: list[object] = []
            for raw, appearance in requested:
                glb = assets.get(_mesh_asset_key(mesh_path, appearance))
                if glb is None:
                    missing.append(raw)
                    statistics["missing"] += 1
                    statistics["sidecar_appearances"] += 1
                    continue
                try:
                    import_native_pbr_master(
                        glb, mesh_path, appearance, Masters, import_common
                    )
                    statistics["imported"] += 1
                except Exception as exc:
                    missing.append(raw)
                    statistics["failed"] += 1
                    statistics["sidecar_appearances"] += 1
                    statistics["errors"].append(
                        {
                            "mesh": mesh_path,
                            "appearance": appearance,
                            "error": str(exc),
                        }
                    )
            if missing:
                copied = dict(descriptor) if isinstance(descriptor, Mapping) else {}
                copied["apps"] = [missing]
                sidecar_meshes[mesh_path] = copied
            if position == 1 or position == total or position % 50 == 0:
                print(
                    f"GHOSTLINE_WORLD_PBR [{position}/{total}] "
                    f"imported={statistics['imported']} sidecar={statistics['sidecar_appearances']}",
                    flush=True,
                )

        if sidecar_meshes:
            statistics["sidecar_meshes"] = len(sidecar_meshes)
            sidecar_loader(
                sidecar_meshes,
                path=path,
                from_mesh_no=0,
                to_mesh_no=10_000_000,
                with_mats=True,
                glbs=glbs,
                mesh_jsons=mesh_jsons,
                Masters=Masters,
                generate_overrides=generate_overrides,
            )

    return load


def import_sector_project(
    config: Mapping[str, Any], import_log: Path
) -> dict[str, Any]:
    ensure_cp77_addon()
    project, raw_root = project_layout(Path(config["project"]))
    if not project.parent.is_dir():
        raise FileNotFoundError(
            f"Prepared WolvenKit project root does not exist: {project.parent}"
        )
    if not raw_root.is_dir():
        raise FileNotFoundError(
            f"Prepared project has no source/raw directory: {raw_root}"
        )
    if not any(raw_root.rglob("*.streamingsector.json")):
        raise FileNotFoundError(
            f"Prepared project has no streamingsector JSON: {raw_root}"
        )

    try:
        from i_scene_cp77_gltf.importers import import_common, sector_import
        from i_scene_cp77_gltf.main.setup import bcolors as addon_colors
    except ImportError as exc:
        raise RuntimeError(
            "Cyberpunk 2077 Blender sector importer is not enabled"
        ) from exc
    compatibility_shims = apply_cp77_addon_compatibility_shims(
        import_common, addon_colors
    )
    if bpy.context.preferences.addons.get("i_scene_cp77_gltf") is None:
        raise RuntimeError("Cyberpunk 2077 Blender add-on is not enabled")
    props = getattr(bpy.context.scene, "cp77_panel_props", None)
    if props is None:
        raise RuntimeError("Cyberpunk add-on scene properties are not registered")
    props.remap_depot = bool(config.get("remap_depot", False))
    sector_import.VERBOSE = bool(config.get("verbose_import", False))
    pbr_assets = (
        native_pbr_asset_index(config)
        if bool(config.get("with_materials", True))
        else {}
    )
    pbr_statistics: dict[str, Any] = {
        "available": len(pbr_assets),
        "imported": 0,
        "missing": 0,
        "failed": 0,
        "sidecar_appearances": 0,
        "sidecar_meshes": 0,
        "errors": [],
    }
    original_mesh_loader = sector_import.meshes_from_mesheswapps
    if pbr_assets:
        sector_import.meshes_from_mesheswapps = native_pbr_mesh_loader(
            pbr_assets,
            original_mesh_loader,
            import_common,
            pbr_statistics,
        )

    import_log.parent.mkdir(parents=True, exist_ok=True)
    started = time.perf_counter()
    try:
        with import_log.open("w", encoding="utf-8") as log_stream:
            stdout_tee = Tee(sys.stdout, log_stream)
            stderr_tee = Tee(sys.stderr, log_stream)
            with (
                contextlib.redirect_stdout(stdout_tee),
                contextlib.redirect_stderr(stderr_tee),
            ):
                sector_import.importSectors(
                    str(project),
                    # Item-database PBR GLBs already contain standard Blender
                    # materials.  RED sidecar rebuilding would discard those
                    # materials and is both slower and less reliable.
                    with_mats=(
                        bool(config.get("with_materials", True))
                        and not pbr_assets
                    ),
                    remap_depot=bool(config.get("remap_depot", False)),
                    want_collisions=False,
                    am_modding=False,
                    with_lights=bool(config.get("with_static_lights", False)),
                )
    except Exception:
        try:
            from i_scene_cp77_gltf.jsontool import JSONTool

            JSONTool.stop_caching()
        except Exception:
            pass
        raise
    finally:
        sector_import.meshes_from_mesheswapps = original_mesh_loader
        elapsed = time.perf_counter() - started

    master = master_collection()
    if master is not None:
        # The importer hides masters in the viewport. Explicit render hiding is
        # required in headless mode so only placed copies enter the catalogue.
        master.hide_viewport = True
        master.hide_render = True
    bpy.context.view_layer.update()
    return {
        "seconds": elapsed,
        "project": str(project),
        "raw_root": str(raw_root),
        "with_materials": bool(config.get("with_materials", True)),
        "material_mode": (
            "native_pbr"
            if pbr_assets
            else "red_sidecars"
            if bool(config.get("with_materials", True))
            else "geometry_only"
        ),
        "native_pbr": pbr_statistics,
        "with_static_lights": bool(config.get("with_static_lights", False)),
        "compatibility_shims": compatibility_shims,
        "log": import_log_signals(import_log),
    }


def sector_content_counts(document: object) -> tuple[int, int]:
    """Return node-definition and node-instance counts from CR2W JSON."""

    if not isinstance(document, Mapping):
        raise ValueError("streamingsector JSON root must be an object")
    data = document.get("Data")
    root = data.get("RootChunk") if isinstance(data, Mapping) else None
    if not isinstance(root, Mapping):
        raise ValueError("streamingsector JSON has no Data.RootChunk object")
    nodes = root.get("nodes")
    if not isinstance(nodes, Sequence) or isinstance(nodes, (str, bytes)):
        raise ValueError("streamingsector RootChunk.nodes must be an array")
    raw_node_data = root.get("nodeData")
    if isinstance(raw_node_data, Mapping):
        node_data = raw_node_data.get("Data")
    else:
        node_data = raw_node_data
    if not isinstance(node_data, Sequence) or isinstance(node_data, (str, bytes)):
        raise ValueError("streamingsector RootChunk.nodeData must contain an array")
    return len(nodes), len(node_data)


def sector_visual_content_counts(document: object) -> tuple[int, int]:
    """Return Blender-supported visual definition and placement counts."""

    if not isinstance(document, Mapping):
        raise ValueError("streamingsector JSON root must be an object")
    data = document.get("Data")
    root = data.get("RootChunk") if isinstance(data, Mapping) else None
    if not isinstance(root, Mapping):
        raise ValueError("streamingsector JSON has no Data.RootChunk object")
    nodes = root.get("nodes")
    if not isinstance(nodes, Sequence) or isinstance(nodes, (str, bytes)):
        raise ValueError("streamingsector RootChunk.nodes must be an array")
    raw_node_data = root.get("nodeData")
    node_data = (
        raw_node_data.get("Data")
        if isinstance(raw_node_data, Mapping)
        else raw_node_data
    )
    if not isinstance(node_data, Sequence) or isinstance(node_data, (str, bytes)):
        raise ValueError("streamingsector RootChunk.nodeData must contain an array")

    candidate_visual_indices = {
        index for index, node in enumerate(nodes) if blender_node_is_visual(node)
    }
    used_visual_indices: set[int] = set()
    visual_instances = 0
    for record in node_data:
        if not isinstance(record, Mapping):
            continue
        raw_index = record.get("NodeIndex")
        if isinstance(raw_index, Mapping):
            raw_index = raw_index.get("$value")
        try:
            node_index = int(raw_index)
        except (TypeError, ValueError):
            continue
        if node_index in candidate_visual_indices:
            used_visual_indices.add(node_index)
            visual_instances += 1
    return len(used_visual_indices), visual_instances


def scan_prepared_project(project: Path) -> dict[str, Any]:
    project, raw_root = project_layout(project)
    counts = {
        "streamingsector_json": 0,
        "glb": 0,
        "mesh_json": 0,
        "entity_json": 0,
        "appearance_json": 0,
        "material_json": 0,
        "images": 0,
        "node_definitions": 0,
        "node_instances": 0,
        "visual_node_definitions": 0,
        "visual_node_instances": 0,
        "other": 0,
    }
    total_bytes = 0
    sector_paths: list[str] = []
    sector_scan_errors: list[dict[str, str]] = []
    if not raw_root.is_dir():
        return {
            "project": str(project),
            "raw_root": str(raw_root),
            "counts": counts,
            "bytes": 0,
            "sectors": [],
            "sector_scan_errors": [],
        }
    for root, _, filenames in os.walk(raw_root):
        root_path = Path(root)
        for filename in filenames:
            path = root_path / filename
            try:
                total_bytes += path.stat().st_size
            except OSError:
                pass
            folded = filename.casefold()
            if folded.endswith(".streamingsector.json"):
                counts["streamingsector_json"] += 1
                sector_paths.append(path.relative_to(raw_root).as_posix())
                try:
                    sector_document = read_json(path)
                    definitions, instances = sector_content_counts(sector_document)
                    counts["node_definitions"] += definitions
                    counts["node_instances"] += instances
                    visual_definitions, visual_instances = sector_visual_content_counts(
                        sector_document
                    )
                    counts["visual_node_definitions"] += visual_definitions
                    counts["visual_node_instances"] += visual_instances
                except (RuntimeError, ValueError) as exc:
                    sector_scan_errors.append(
                        {
                            "path": path.relative_to(raw_root).as_posix(),
                            "error": str(exc),
                        }
                    )
            elif folded.endswith(".glb"):
                counts["glb"] += 1
            elif folded.endswith(".mesh.json"):
                counts["mesh_json"] += 1
            elif folded.endswith(".ent.json"):
                counts["entity_json"] += 1
            elif folded.endswith(".app.json"):
                counts["appearance_json"] += 1
            elif folded.endswith(".material.json"):
                counts["material_json"] += 1
            elif folded.endswith((".png", ".jpg", ".jpeg", ".webp", ".dds", ".tga")):
                counts["images"] += 1
            else:
                counts["other"] += 1
    return {
        "project": str(project),
        "raw_root": str(raw_root),
        "counts": counts,
        "bytes": total_bytes,
        "sectors": sorted(sector_paths),
        "sector_scan_errors": sector_scan_errors,
    }


def master_object_ids() -> set[int]:
    master = master_collection()
    if master is None:
        return set()
    return {obj.as_pointer() for obj in master.all_objects}


def renderable_objects() -> list[Any]:
    excluded = master_object_ids()
    return [
        obj
        for obj in bpy.context.scene.objects
        if obj.as_pointer() not in excluded
        and obj.type in {"MESH", "CURVE", "SURFACE", "FONT"}
        and not obj.hide_render
    ]


def world_bounds(objects: Sequence[Any]) -> tuple[Any, Any]:
    minimum = Vector((math.inf, math.inf, math.inf))
    maximum = Vector((-math.inf, -math.inf, -math.inf))
    found = False
    for obj in objects:
        for corner in obj.bound_box:
            point = obj.matrix_world @ Vector(corner)
            minimum.x = min(minimum.x, point.x)
            minimum.y = min(minimum.y, point.y)
            minimum.z = min(minimum.z, point.z)
            maximum.x = max(maximum.x, point.x)
            maximum.y = max(maximum.y, point.y)
            maximum.z = max(maximum.z, point.z)
            found = True
    if not found:
        raise RuntimeError("Sector import produced no renderable geometry bounds")
    return minimum, maximum


def bounds_record(minimum: Any, maximum: Any) -> dict[str, list[float]]:
    center = (minimum + maximum) * 0.5
    return {
        "minimum": [float(value) for value in minimum],
        "maximum": [float(value) for value in maximum],
        "center": [float(value) for value in center],
        "size": [float(value) for value in maximum - minimum],
    }


def imported_content_statistics() -> dict[str, Any]:
    """Collect the coverage metadata written by the CP77 sector importer."""

    sector_collections = [
        collection
        for collection in bpy.data.collections
        if "expectedNodes" in collection
    ]
    expected_node_instances = sum(
        int(collection.get("expectedNodes", 0)) for collection in sector_collections
    )
    imported_node_definitions: set[tuple[str, int]] = set()
    imported_node_instances: set[tuple[str, int]] = set()
    imported_instance_records = 0
    tagged_items = [*bpy.data.collections, *bpy.data.objects]
    for item in tagged_items:
        sector_name = str(item.get("sectorName", ""))
        if "nodeIndex" in item:
            imported_node_definitions.add((sector_name, int(item["nodeIndex"])))
        if "nodeDataIndex" in item:
            imported_node_instances.add((sector_name, int(item["nodeDataIndex"])))
            imported_instance_records += 1

    imported_mesh_paths: set[str] = set()
    master = master_collection()
    if master is not None:
        for collection in collection_tree(master):
            for property_name in ("meshpath", "depotPath", "glb_file"):
                raw_path = str(collection.get(property_name, "")).strip()
                folded = raw_path.replace("\\", "/").casefold()
                if folded.endswith((".mesh", ".w2mesh", ".physicalscene")):
                    imported_mesh_paths.add(folded)

    return {
        "sector_collections": len(sector_collections),
        "expected_node_instances": expected_node_instances,
        "imported_node_definitions": len(imported_node_definitions),
        "imported_node_instances": len(imported_node_instances),
        "imported_instance_records": imported_instance_records,
        "imported_mesh_paths": sorted(imported_mesh_paths),
        "imported_mesh_glbs": len(imported_mesh_paths),
        "master_asset_groups": len(master.children) if master is not None else 0,
    }


def missing_content_diagnostics(
    objects: Sequence[Any], prepared: Mapping[str, Any], expected: object
) -> dict[str, Any]:
    meshes = [obj for obj in objects if obj.type == "MESH"]
    unique_meshes = {obj.data.as_pointer() for obj in meshes if obj.data is not None}
    missing_images: list[str] = []
    unloaded_images: list[str] = []
    for image in bpy.data.images:
        if image.source != "FILE" or image.packed_file is not None:
            continue
        filepath = Path(bpy.path.abspath(image.filepath)) if image.filepath else None
        if filepath is None or not filepath.is_file():
            missing_images.append(image.name if filepath is None else str(filepath))
        if not image.has_data:
            unloaded_images.append(image.name)

    importer = imported_content_statistics()
    prepared_counts = prepared.get("counts", {})
    if not isinstance(prepared_counts, Mapping):
        prepared_counts = {}
    staged_sector_count = int(prepared_counts.get("streamingsector_json", 0))
    staged_mesh_count = int(prepared_counts.get("glb", 0))
    staged_node_definitions = int(prepared_counts.get("node_definitions", 0))
    staged_node_instances = int(prepared_counts.get("node_instances", 0))
    evaluated = evaluate_content_coverage(
        expected,
        {
            "staged_sector_jsons": staged_sector_count,
            "imported_sector_jsons": importer["sector_collections"],
            "staged_mesh_glbs": staged_mesh_count,
            "imported_mesh_glbs": importer["imported_mesh_glbs"],
            "staged_entity_jsons": int(prepared_counts.get("entity_json", 0)),
            "staged_appearance_jsons": int(prepared_counts.get("appearance_json", 0)),
            "staged_node_definitions": staged_node_definitions,
            "imported_node_definitions": importer["imported_node_definitions"],
            "expected_node_instances": int(
                prepared_counts.get("visual_node_instances", staged_node_instances)
            ),
            "imported_node_instances": importer["imported_node_instances"],
            "imported_instance_records": importer["imported_instance_records"],
        },
    )
    signals: list[dict[str, Any]] = list(evaluated["signals"])
    if staged_sector_count == 0:
        signals.append({"severity": "error", "code": "no_staged_sectors"})
    if importer["sector_collections"] == 0:
        signals.append({"severity": "error", "code": "no_imported_sectors"})
    if not meshes:
        signals.append({"severity": "error", "code": "no_imported_meshes"})
    if missing_images:
        signals.append(
            {
                "severity": "warning",
                "code": "missing_texture_files",
                "count": len(missing_images),
            }
        )
    empty_meshes = [obj.name for obj in meshes if len(obj.data.polygons) == 0]
    if empty_meshes:
        signals.append(
            {
                "severity": "warning",
                "code": "empty_mesh_objects",
                "count": len(empty_meshes),
            }
        )
    without_materials = [obj.name for obj in meshes if len(obj.material_slots) == 0]
    if meshes and len(without_materials) == len(meshes):
        signals.append({"severity": "warning", "code": "no_material_assignments"})
    sector_scan_errors = prepared.get("sector_scan_errors", [])
    if sector_scan_errors:
        signals.append(
            {
                "severity": "error",
                "code": "sector_json_scan_errors",
                "count": len(sector_scan_errors),
            }
        )

    master = master_collection()
    return {
        "signals": signals,
        "expected": evaluated["expected"],
        "actual": evaluated["actual"],
        "coverage": evaluated["coverage"],
        "renderable_objects": len(objects),
        "mesh_objects": len(meshes),
        "unique_mesh_datablocks": len(unique_meshes),
        "shared_mesh_instance_ratio": (
            round(len(meshes) / len(unique_meshes), 4) if unique_meshes else None
        ),
        "empty_mesh_objects": empty_meshes[:100],
        "objects_without_material_slots": without_materials[:100],
        "missing_image_files": missing_images[:100],
        "unloaded_images": unloaded_images[:100],
        "materials": len(bpy.data.materials),
        "images": len(bpy.data.images),
        "sector_collections": importer["sector_collections"],
        "expected_sector_nodes": importer["expected_node_instances"],
        "expected_visual_node_definitions": int(
            prepared_counts.get("visual_node_definitions", 0)
        ),
        "expected_visual_node_instances": int(
            prepared_counts.get("visual_node_instances", 0)
        ),
        "instantiated_node_data": importer["imported_node_instances"],
        "imported_node_definitions": importer["imported_node_definitions"],
        "imported_instance_records": importer["imported_instance_records"],
        "imported_mesh_glbs": importer["imported_mesh_glbs"],
        "imported_mesh_paths": importer["imported_mesh_paths"][:100],
        "master_asset_groups": len(master.children) if master is not None else 0,
        "sector_scan_errors": list(sector_scan_errors)[:100],
    }


def _set_enum_safely(owner: Any, name: str, candidates: Sequence[str]) -> str | None:
    for candidate in candidates:
        try:
            setattr(owner, name, candidate)
            return candidate
        except (AttributeError, TypeError, ValueError):
            continue
    return None


def build_renderer_identity(
    config: Mapping[str, Any],
    *,
    engine: str,
    image_format: str,
    blender_version: str,
    addon_version: object,
) -> dict[str, Any]:
    """Return the render-affecting identity and its stable fingerprint."""

    identity = {
        "script_sha256": hash_file(Path(__file__).resolve()),
        "blender_version": blender_version,
        "cp77_addon_version": addon_version,
        "engine": engine,
        "resolution": int(config["resolution"]),
        "image_format": image_format,
        "image_quality": int(config["image_quality"]),
        "world_strength": float(config.get("world_strength", 0.35)),
        "sun_energy": float(config.get("sun_energy", 2.5)),
        "sun_angle_degrees": float(config.get("sun_angle_degrees", 4.0)),
        "transparent_background": bool(config.get("transparent_background", False)),
        "with_materials": bool(config.get("with_materials", True)),
        "with_static_lights": bool(config.get("with_static_lights", False)),
    }
    return {
        **identity,
        "renderer_fingerprint": hashlib.sha256(
            json.dumps(identity, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest(),
    }


def configure_scene(config: Mapping[str, Any]) -> tuple[Any, dict[str, Any]]:
    require_blender()
    scene = bpy.context.scene
    engine = _set_enum_safely(
        scene.render, "engine", ("BLENDER_EEVEE_NEXT", "BLENDER_EEVEE")
    )
    if engine is None:
        raise RuntimeError("This Blender build does not expose the Eevee render engine")
    scene.frame_set(1)
    scene.render.resolution_x = int(config["resolution"])
    scene.render.resolution_y = int(config["resolution"])
    scene.render.resolution_percentage = 100
    scene.render.pixel_aspect_x = 1.0
    scene.render.pixel_aspect_y = 1.0
    scene.render.film_transparent = bool(config.get("transparent_background", False))
    scene.render.use_file_extension = True
    scene.render.use_persistent_data = True
    scene.render.dither_intensity = 0.0
    image_format = str(config["image_format"]).upper()
    scene.render.image_settings.file_format = image_format
    scene.render.image_settings.color_mode = (
        "RGBA" if scene.render.film_transparent else "RGB"
    )
    scene.render.image_settings.color_depth = "8"
    scene.render.image_settings.quality = int(config["image_quality"])
    if image_format == "PNG":
        scene.render.image_settings.compression = 35
    try:
        scene.view_settings.look = "AgX - Medium High Contrast"
    except (TypeError, ValueError):
        pass

    samples = int(config.get("samples", 64))
    eevee = getattr(scene, "eevee", None)
    if eevee is not None:
        for attribute in ("taa_render_samples", "taa_samples"):
            if hasattr(eevee, attribute):
                setattr(eevee, attribute, samples)

    world = scene.world or bpy.data.worlds.new("Ghostline Neutral Daylight")
    world.name = "Ghostline Neutral Daylight"
    scene.world = world
    world.use_nodes = True
    background = world.node_tree.nodes.get("Background") if world.node_tree else None
    if background is not None:
        background.inputs["Color"].default_value = (0.72, 0.78, 0.88, 1.0)
        background.inputs["Strength"].default_value = float(
            config.get("world_strength", 0.35)
        )

    sun_data = bpy.data.lights.new("Ghostline Neutral Sun", "SUN")
    sun_data.energy = float(config.get("sun_energy", 2.5))
    sun_data.color = (1.0, 0.965, 0.9)
    sun_data.angle = math.radians(float(config.get("sun_angle_degrees", 4.0)))
    sun = bpy.data.objects.new("Ghostline Neutral Sun", sun_data)
    sun["ghostline_renderer_light"] = True
    scene.collection.objects.link(sun)
    sun.rotation_euler = (
        math.radians(38.0),
        math.radians(-18.0),
        math.radians(-42.0),
    )

    camera_data = bpy.data.cameras.new("Ghostline Location Camera")
    camera_data.type = "PERSP"
    camera_data.sensor_fit = "HORIZONTAL"
    camera_data.sensor_width = 36.0
    camera_data.clip_start = float(config.get("clip_start", 0.05))
    camera_data.clip_end = float(config.get("clip_end", 2000.0))
    camera = bpy.data.objects.new("Ghostline Location Camera", camera_data)
    camera["ghostline_renderer_camera"] = True
    scene.collection.objects.link(camera)
    scene.camera = camera
    bpy.context.view_layer.update()
    try:
        import i_scene_cp77_gltf

        addon_version: object = list(i_scene_cp77_gltf.bl_info.get("version", ()))
    except (AttributeError, ImportError):
        addon_version = None
    identity = build_renderer_identity(
        config,
        engine=engine,
        image_format=image_format,
        blender_version=bpy.app.version_string,
        addon_version=addon_version,
    )
    return camera, {
        **identity,
        "static_lights": sum(
            1
            for obj in scene.objects
            if obj.type == "LIGHT" and not obj.get("ghostline_renderer_light")
        ),
    }


class SceneRaycaster:
    """Thin wrapper over Blender's evaluated dependency-graph BVH ray casts."""

    def __init__(self) -> None:
        require_blender()
        bpy.context.view_layer.update()
        self.scene = bpy.context.scene
        self.depsgraph = bpy.context.evaluated_depsgraph_get()
        self.calls = 0

    def cast(self, origin: Any, direction: Any, distance: float) -> dict[str, Any]:
        self.calls += 1
        direction = Vector(direction).normalized()
        result, location, normal, face_index, obj, _matrix = self.scene.ray_cast(
            self.depsgraph, Vector(origin), direction, distance=float(distance)
        )
        if not result:
            return {"hit": False, "distance": None}
        hit_distance = (location - Vector(origin)).length
        return {
            "hit": True,
            "distance": float(hit_distance),
            "location": [float(value) for value in location],
            "normal": [float(value) for value in normal],
            "face_index": int(face_index),
            "object": obj.name if obj is not None else None,
        }


def validate_camera_position(
    raycaster: SceneRaycaster, position: Any, validation: Mapping[str, Any]
) -> dict[str, Any]:
    if not bool(validation.get("enabled", True)):
        return {"valid": True, "reasons": [], "disabled": True}

    reasons: list[str] = []
    floor_max = float(validation.get("floor_max_distance", 3.0))
    floor = raycaster.cast(position, (0.0, 0.0, -1.0), floor_max)
    if not floor["hit"]:
        if bool(validation.get("require_floor", True)):
            reasons.append("no_floor_within_probe_distance")
    else:
        floor_distance = float(floor["distance"])
        if floor_distance < float(validation.get("floor_clearance_min", 0.9)):
            reasons.append("camera_too_close_to_floor")
        if floor_distance > float(validation.get("floor_clearance_max", 2.5)):
            reasons.append("camera_too_high_above_floor")
        normal = floor.get("normal") or [0.0, 0.0, 0.0]
        if float(normal[2]) < float(validation.get("floor_normal_z_min", 0.25)):
            reasons.append("floor_hit_is_too_steep")

    headroom_probe = float(validation.get("headroom_probe_distance", 8.0))
    ceiling = raycaster.cast(position, (0.0, 0.0, 1.0), headroom_probe)
    ceiling_height = None
    if ceiling["hit"] and floor["hit"]:
        ceiling_height = float(ceiling["distance"]) + float(floor["distance"])
        if ceiling_height < float(validation.get("minimum_ceiling_height", 1.9)):
            reasons.append("insufficient_headroom")

    clearance = float(validation.get("surface_clearance", 0.12))
    count = max(4, int(validation.get("surface_probe_directions", 16)))
    proximity_hits: list[dict[str, Any]] = []
    for index in range(count):
        angle = 2.0 * math.pi * index / count
        hit = raycaster.cast(
            position, (math.cos(angle), math.sin(angle), 0.0), clearance
        )
        if hit["hit"]:
            proximity_hits.append(hit)
    upward_near = raycaster.cast(position, (0.0, 0.0, 1.0), clearance)
    if upward_near["hit"]:
        proximity_hits.append(upward_near)
    if proximity_hits:
        reasons.append("camera_intersects_or_nearly_touches_geometry")

    openness_distance = float(validation.get("openness_probe_distance", 20.0))
    openness_samples: list[float] = []
    for index in range(8):
        angle = 2.0 * math.pi * index / 8
        hit = raycaster.cast(
            position, (math.cos(angle), math.sin(angle), 0.0), openness_distance
        )
        openness_samples.append(
            float(hit["distance"]) if hit["hit"] else openness_distance
        )

    return {
        "valid": not reasons,
        "reasons": reasons,
        "floor": floor,
        "ceiling": ceiling,
        "estimated_ceiling_height": ceiling_height,
        "near_surface_hits": proximity_hits,
        "horizontal_openness": {
            "probe_distance": openness_distance,
            "samples": openness_samples,
            "mean": sum(openness_samples) / len(openness_samples),
            "minimum": min(openness_samples),
            "maximum": max(openness_samples),
        },
        "backend": "bpy.types.Scene.ray_cast/evaluated dependency-graph BVH",
    }


def forward_vector(yaw_degrees: float, pitch_degrees: float) -> Any:
    yaw = math.radians(yaw_degrees)
    pitch = math.radians(pitch_degrees)
    horizontal = math.cos(pitch)
    return Vector(
        (
            horizontal * math.cos(yaw),
            horizontal * math.sin(yaw),
            math.sin(pitch),
        )
    ).normalized()


def aim_camera(
    camera: Any, position: Any, yaw_degrees: float, pitch_degrees: float
) -> Any:
    location = Vector(position)
    direction = forward_vector(yaw_degrees, pitch_degrees)
    camera.location = location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()
    return direction


def set_horizontal_fov(camera: Any, fov_degrees: float) -> None:
    if not 20.0 <= fov_degrees <= 140.0:
        raise ValueError(
            f"Horizontal FOV must be between 20 and 140 degrees: {fov_degrees}"
        )
    camera.data.sensor_fit = "HORIZONTAL"
    camera.data.lens = camera.data.sensor_width / (
        2.0 * math.tan(math.radians(fov_degrees) * 0.5)
    )


def render_result_statistics(
    saved_path: Path | None = None, max_samples: int = 8192
) -> dict[str, Any]:
    image = bpy.data.images.get("Render Result")
    loaded_image = None
    source = "render_result"
    if image is None or not image.has_data or not all(image.size):
        if saved_path is None:
            return {"available": False}
        try:
            loaded_image = bpy.data.images.load(str(saved_path), check_existing=False)
            image = loaded_image
            source = "saved_file"
        except RuntimeError as exc:
            return {"available": False, "error": str(exc)}
    pixels = image.pixels
    pixel_count = max(1, len(pixels) // 4)
    stride = max(1, pixel_count // max_samples)
    luminances: list[float] = []
    alpha_values: list[float] = []
    for pixel_index in range(0, pixel_count, stride):
        base = pixel_index * 4
        red, green, blue, alpha = (
            float(pixels[base]),
            float(pixels[base + 1]),
            float(pixels[base + 2]),
            float(pixels[base + 3]),
        )
        luminances.append(0.2126 * red + 0.7152 * green + 0.0722 * blue)
        alpha_values.append(alpha)
    mean = sum(luminances) / len(luminances)
    variance = sum((value - mean) ** 2 for value in luminances) / len(luminances)
    result = {
        "available": True,
        "source": source,
        "sample_count": len(luminances),
        "mean_luminance_linear": mean,
        "luminance_standard_deviation": math.sqrt(variance),
        "minimum_luminance_linear": min(luminances),
        "maximum_luminance_linear": max(luminances),
        "dark_fraction": sum(value < 0.02 for value in luminances) / len(luminances),
        "bright_fraction": sum(value > 0.9 for value in luminances) / len(luminances),
        "mean_alpha": sum(alpha_values) / len(alpha_values),
    }
    if loaded_image is not None:
        bpy.data.images.remove(loaded_image)
    return result


def hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()


def render_image_atomic(scene: Any, output: Path) -> dict[str, Any]:
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(f".{output.stem}.{os.getpid()}.tmp{output.suffix}")
    started = time.perf_counter()
    try:
        scene.render.filepath = str(temporary)
        result = bpy.ops.render.render(write_still=True)
        if "FINISHED" not in result:
            raise RuntimeError(f"Blender render operator did not finish for {output}")
        if not temporary.is_file():
            raise RuntimeError(f"Blender did not produce {temporary}")
        statistics = render_result_statistics(temporary)
        os.replace(temporary, output)
    finally:
        if temporary.exists():
            temporary.unlink()
    return {
        "path": str(output),
        "bytes": output.stat().st_size,
        "sha256": hash_file(output),
        "seconds": time.perf_counter() - started,
        "image_statistics": statistics,
    }


def render_viewpoints(
    config: Mapping[str, Any], camera: Any, raycaster: SceneRaycaster
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    output_root = Path(config["output"])
    extension = IMAGE_EXTENSIONS[str(config["image_format"]).upper()]
    reports: list[dict[str, Any]] = []
    valid_count = 0
    invalid_count = 0
    started = time.perf_counter()
    scene = bpy.context.scene

    for viewpoint in config["viewpoints"]:
        position = Vector(viewpoint["position"])
        position_validation = validate_camera_position(
            raycaster, position, viewpoint["validation"]
        )
        for direction_spec in viewpoint["directions"]:
            yaw = (
                float(viewpoint["yaw_degrees"])
                + float(direction_spec["offset_degrees"])
            ) % 360.0
            pitch = float(viewpoint["pitch_degrees"])
            direction = forward_vector(yaw, pitch)
            forward_clearance = float(
                viewpoint["validation"].get("forward_clearance", 0.18)
            )
            forward_hit = raycaster.cast(position, direction, forward_clearance)
            reasons = list(position_validation["reasons"])
            if (
                bool(viewpoint["validation"].get("enabled", True))
                and forward_hit["hit"]
            ):
                reasons.append("view_direction_starts_inside_or_too_near_geometry")

            direction_name = safe_name(direction_spec["name"], "direction")
            final_path = (
                output_root / "views" / viewpoint["id"] / f"{direction_name}{extension}"
            )
            record: dict[str, Any] = {
                "viewpoint_id": viewpoint["id"],
                "direction": direction_name,
                "position": [float(value) for value in position],
                "source_position_mode": viewpoint["source_position_mode"],
                "yaw_degrees": yaw,
                "pitch_degrees": pitch,
                "horizontal_fov_degrees": float(viewpoint["horizontal_fov_degrees"]),
                "output": str(final_path),
                "valid": not reasons,
                "invalid_reasons": reasons,
                "position_validation": position_validation,
                "forward_clearance": forward_hit,
                "metadata": viewpoint.get("metadata", {}),
            }
            if reasons:
                record["stale_output_present"] = final_path.is_file()
                invalid_count += 1
            else:
                set_horizontal_fov(camera, float(viewpoint["horizontal_fov_degrees"]))
                aim_camera(camera, position, yaw, pitch)
                bpy.context.view_layer.update()
                record["image"] = render_image_atomic(scene, final_path)
                valid_count += 1
            reports.append(record)

    return reports, {
        "seconds": time.perf_counter() - started,
        "valid_views": valid_count,
        "invalid_views": invalid_count,
        "total_views": len(reports),
        "raycast_calls": raycaster.calls,
    }


def cache_key_for_job(config: Mapping[str, Any]) -> str | None:
    if not bool(config.get("reuse_mesh_cache", True)):
        return None
    explicit = config.get("asset_cache_key")
    if explicit:
        base = f"explicit:{explicit}"
    else:
        _project, raw_root = project_layout(Path(config["project"]))
        base = f"raw-root:{os.path.normcase(str(raw_root.resolve()))}"
    import_mode = {
        "with_materials": bool(config.get("with_materials", True)),
        "with_static_lights": bool(config.get("with_static_lights", False)),
        "remap_depot": bool(config.get("remap_depot", False)),
    }
    return f"{base}|import:{hashlib.sha256(json.dumps(import_mode, sort_keys=True).encode('utf-8')).hexdigest()[:12]}"


def render_tile(config: Mapping[str, Any]) -> dict[str, Any]:
    global ACTIVE_MASTER_CACHE_KEY

    config = dict(config)
    if (
        not bool(config.get("with_materials", True))
        or bool(config.get("native_pbr_assets"))
    ):
        config["resolution"] = min(int(config.get("resolution", 768)), 384)
        config["samples"] = min(int(config.get("samples", 64)), 16)
    tile_id = str(config["tile_id"])
    output = Path(config["output"])
    output.mkdir(parents=True, exist_ok=True)
    report_path = output / "render-report.json"
    started = time.perf_counter()
    material_before = dict(MATERIAL_CACHE_STATS)
    requested_cache_key = cache_key_for_job(config)
    keep_master = (
        requested_cache_key is not None
        and requested_cache_key == ACTIVE_MASTER_CACHE_KEY
    )
    report: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "kind": "ghostline-world-location-tile-render",
        "tile_id": tile_id,
        "run_id": config.get("run_id"),
        "status": "running",
        "started_at": utc_now(),
        "project": str(Path(config["project"])),
        "output": str(output),
        "state_id": config.get("state_id", config.get("quest_variant")),
        "content_fingerprint": config.get("content_fingerprint"),
        "tile_bounds": config.get("tile_bounds"),
        "contributing_sectors": config.get(
            "contributing_sectors", config.get("sectors", [])
        ),
        "render_options": {
            "with_materials": bool(config.get("with_materials", True)),
            "with_static_lights": bool(config.get("with_static_lights", False)),
        },
        "cache": {
            "requested_key": requested_cache_key,
            "reused_master_instances": keep_master,
        },
        "timings": {},
    }
    print(f"GHOSTLINE_WORLD_TILE_START {tile_id}", flush=True)
    try:
        clear_started = time.perf_counter()
        report["clear"] = clear_tile_scene(keep_master)
        report["timings"]["clear_seconds"] = time.perf_counter() - clear_started

        prepared_started = time.perf_counter()
        prepared = scan_prepared_project(Path(config["project"]))
        report["prepared_project"] = prepared
        report["timings"]["scan_prepared_seconds"] = (
            time.perf_counter() - prepared_started
        )

        report["import"] = import_sector_project(config, output / "sector-import.log")
        report["timings"]["import_seconds"] = report["import"]["seconds"]
        ACTIVE_MASTER_CACHE_KEY = requested_cache_key

        objects = renderable_objects()
        minimum, maximum = world_bounds(objects)
        report["geometry_bounds"] = bounds_record(minimum, maximum)
        report["content"] = missing_content_diagnostics(
            objects,
            prepared,
            config.get("expected_content", config.get("expected", {})),
        )
        log_counts = report["import"]["log"].get("counts", {})
        for signal, count in log_counts.items():
            if count:
                report["content"]["signals"].append(
                    {
                        "severity": IMPORT_LOG_SIGNAL_SEVERITY.get(signal, "warning"),
                        "code": f"import_log_{signal}",
                        "count": int(count),
                    }
                )
        severity_counts = signal_severity_counts(report["content"]["signals"])
        report["content"]["severity_counts"] = severity_counts
        report["content"]["complete"] = severity_counts.get("error", 0) == 0

        setup_started = time.perf_counter()
        camera, scene_record = configure_scene(config)
        report["renderer"] = scene_record
        report["timings"]["scene_setup_seconds"] = time.perf_counter() - setup_started

        validation_started = time.perf_counter()
        raycaster = SceneRaycaster()
        report["views"], view_summary = render_viewpoints(config, camera, raycaster)
        report["view_summary"] = view_summary
        report["timings"]["validate_and_render_seconds"] = (
            time.perf_counter() - validation_started
        )
        report["status"], status_error = classify_render_status(
            int(view_summary["valid_views"]),
            int(view_summary["invalid_views"]),
            int(severity_counts.get("error", 0)),
        )
        if status_error:
            report["error"] = status_error
    except Exception as exc:
        ACTIVE_MASTER_CACHE_KEY = None
        report["status"] = "failed"
        report["error"] = str(exc)
        report["traceback"] = traceback.format_exc()
        traceback.print_exc()
    finally:
        report["material_cache"] = {
            "hits": MATERIAL_CACHE_STATS["hits"] - material_before["hits"],
            "misses": MATERIAL_CACHE_STATS["misses"] - material_before["misses"],
            "total_hits": MATERIAL_CACHE_STATS["hits"],
            "total_misses": MATERIAL_CACHE_STATS["misses"],
            "cached_materials": len(MATERIAL_CACHE),
        }
        report["timings"]["total_seconds"] = time.perf_counter() - started
        report["finished_at"] = utc_now()
        write_json_atomic(report_path, report)
        report["report_path"] = str(report_path)
    print(f"GHOSTLINE_WORLD_TILE_DONE {tile_id} status={report['status']}", flush=True)
    return report


def compact_batch_entry(report: Mapping[str, Any]) -> dict[str, Any]:
    summary = report.get("view_summary", {})
    content = report.get("content", {})
    severity_counts = (
        content.get("severity_counts", {}) if isinstance(content, Mapping) else {}
    )
    return {
        "tile_id": report.get("tile_id"),
        "status": report.get("status"),
        "report": report.get("report_path"),
        "output": report.get("output"),
        "valid_views": summary.get("valid_views", 0),
        "invalid_views": summary.get("invalid_views", 0),
        "total_views": summary.get("total_views", 0),
        "content_errors": severity_counts.get("error", 0),
        "content_warnings": severity_counts.get("warning", 0),
        "with_materials": report.get("render_options", {}).get("with_materials"),
        "seconds": report.get("timings", {}).get("total_seconds"),
        "error": report.get("error"),
    }


def run_batch(args: argparse.Namespace) -> tuple[dict[str, Any], bool]:
    jobs_path = args.jobs.resolve()
    report_path = (
        args.batch_report.resolve()
        if args.batch_report is not None
        else jobs_path.with_suffix(".report.json")
    )
    jobs: list[dict[str, Any]] = []
    started = time.perf_counter()
    batch: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "kind": "ghostline-world-location-render-batch",
        "jobs_file": str(jobs_path),
        "started_at": utc_now(),
        "tiles": [],
    }
    failed = False
    invalid = False
    try:
        jobs = parse_job_payload(jobs_path, args)
        for index, config in enumerate(jobs, start=1):
            print(
                f"GHOSTLINE_WORLD_BATCH [{index}/{len(jobs)}] {config['tile_id']}",
                flush=True,
            )
            tile_report = render_tile(config)
            entry = compact_batch_entry(tile_report)
            batch["tiles"].append(entry)
            failed = failed or tile_report["status"] == "failed"
            invalid = (
                invalid or bool(entry["invalid_views"]) or bool(entry["content_errors"])
            )
            if args.fail_fast and tile_report["status"] == "failed":
                break
    except Exception as exc:
        failed = True
        batch["batch_error"] = str(exc)
        batch["traceback"] = traceback.format_exc()
        traceback.print_exc()
    finally:
        tiles = batch["tiles"]
        batch["summary"] = {
            "requested_tiles": len(jobs),
            "attempted_tiles": len(tiles),
            "completed_tiles": sum(item["status"] == "completed" for item in tiles),
            "partial_tiles": sum(item["status"] == "partial" for item in tiles),
            "failed_tiles": sum(item["status"] == "failed" for item in tiles),
            "valid_views": sum(int(item["valid_views"]) for item in tiles),
            "invalid_views": sum(int(item["invalid_views"]) for item in tiles),
            "total_views": sum(int(item["total_views"]) for item in tiles),
            "content_errors": sum(int(item["content_errors"]) for item in tiles),
            "content_warnings": sum(int(item["content_warnings"]) for item in tiles),
            "seconds": time.perf_counter() - started,
        }
        batch["finished_at"] = utc_now()
        write_json_atomic(report_path, batch)
        batch["report_path"] = str(report_path)
    should_fail = failed or (args.fail_on_invalid and invalid)
    return batch, should_fail


def main() -> None:
    args = parse_args()
    require_blender()
    enable_material_cache()
    batch, should_fail = run_batch(args)
    summary = batch["summary"]
    print(
        "GHOSTLINE_WORLD_BATCH_DONE "
        f"completed={summary['completed_tiles']} partial={summary['partial_tiles']} "
        f"failed={summary['failed_tiles']} valid_views={summary['valid_views']} "
        f"invalid_views={summary['invalid_views']} "
        f"content_errors={summary['content_errors']} "
        f"report={batch['report_path']}",
        flush=True,
    )
    if should_fail:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
