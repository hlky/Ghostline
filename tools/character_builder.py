#!/usr/bin/env python3
"""Generate, validate, compare, and build Ghostline character resources."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import shutil
import struct
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "characters/patch.character.json"
LOCAL_PATHS = ROOT / "characters/local-paths.json"
DEFAULT_WOLVENKIT = Path(r"H:\WolvenKit.Console-8.17.4\WolvenKit.CLI.exe")
DEFAULT_BLENDER = Path(r"C:\Program Files\Blender Foundation\Blender 5.1\blender.exe")
DEFAULT_GAME = Path(r"H:\Cyberpunk 2077")
BLENDER_RUNNER = Path(__file__).with_name("character_head_blender.py")
SHAPE_NAMES = ("eyes", "nose", "mouth", "jaw", "ears")
SHAPE_PART_DIGITS = {"eyes": "1", "nose": "2", "mouth": "3", "jaw": "4", "ears": "5"}
HEAD_SHAPE_MIN = 1
HEAD_SHAPE_MAX = 22
FRAME_PROFILES: dict[str, dict[str, Any]] = {
    "male_average": {
        "player_token": "pma",
        "npc_token": "ma",
        "base_entity_type": "ManAverage",
        "root_component_count": 110,
        "head_shape_max": 21,
        "preview_morphtargets": ("h0_000_pma__morphs.morphtarget",),
        "unresolved_documented_values": (22,),
    },
    "female_average": {
        "player_token": "pwa",
        "npc_token": "wa",
        "base_entity_type": "WomanAverage",
        "root_component_count": 116,
        "head_shape_max": 22,
        "preview_morphtargets": ("h0_000_pwa__morphs.morphtarget",),
        "unresolved_documented_values": (),
    },
}
INDEXED_OVERRIDE_KEYS = frozenset({"depot_path", "mesh_appearance"})
CNAME_PATTERN = re.compile(r"^[A-Za-z0-9_.:-]+$")
FRAME_TOKEN_PATTERN = re.compile(
    r"(?:^|_)(pma|pwa|mba|wba|mab|wab|ma|wa|mb|wb)(?=__|_|\.|$)", re.IGNORECASE
)


class CharacterBuildError(RuntimeError):
    """Raised when character input or generated output is unsafe or invalid."""


@dataclass
class ValidationReport:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    details: dict[str, Any] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return not self.errors

    def require_ok(self) -> None:
        if self.errors:
            raise CharacterBuildError("\n".join(self.errors))

    def as_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "errors": self.errors,
            "warnings": self.warnings,
            "details": self.details,
        }


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CharacterBuildError(f"Unable to read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise CharacterBuildError(f"Expected a JSON object in {path}")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as stream:
            stream.write(json.dumps(value, indent=2, ensure_ascii=False) + "\n")
            temporary = Path(stream.name)
        temporary.replace(path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def repo_path(value: str | Path) -> Path:
    raw = str(value)
    if raw.startswith("@"):
        alias, separator, relative = raw[1:].partition("/")
        if (
            not separator
            or not CNAME_PATTERN.fullmatch(alias)
            or not relative
            or Path(relative).is_absolute()
            or ".." in Path(relative).parts
        ):
            raise CharacterBuildError(f"Invalid local path alias: {raw}")
        if not LOCAL_PATHS.is_file():
            raise CharacterBuildError(
                f"{raw} requires {LOCAL_PATHS}; copy local-paths.example.json "
                "and configure this machine"
            )
        configured = read_json(LOCAL_PATHS).get(alias)
        if not isinstance(configured, str) or not configured.strip():
            raise CharacterBuildError(
                f"Local path alias @{alias} is not configured in {LOCAL_PATHS}"
            )
        base = Path(configured)
        if not base.is_absolute():
            base = ROOT / base
        return base / Path(relative)
    path = Path(raw)
    return path if path.is_absolute() else ROOT / path


def frame_profile(manifest: dict[str, Any]) -> dict[str, Any]:
    frame = manifest.get("frame")
    profile = FRAME_PROFILES.get(str(frame))
    if profile is None:
        raise CharacterBuildError(
            f"Unsupported character frame {frame!r}; choose one of {', '.join(FRAME_PROFILES)}"
        )
    return profile


def normalized_depot_root(value: Any, label: str) -> str:
    root = str(value or "")
    parts = root.split("\\")
    if (
        not root
        or "/" in root
        or ":" in root
        or root != root.strip()
        or root.endswith("\\")
        or any(not part or part in {".", ".."} for part in parts)
    ):
        raise CharacterBuildError(f"{label} must be a normalized depot path")
    return root


def fnv1a64_resource_path(value: str) -> str:
    result = 0xCBF29CE484222325
    for byte in value.casefold().encode("utf-8"):
        result ^= byte
        result = (result * 0x100000001B3) & 0xFFFFFFFFFFFFFFFF
    return str(result)


def template_asset_records(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    spec = manifest.get("template_assets")
    if spec is None:
        return []
    if not isinstance(spec, dict):
        raise CharacterBuildError("template_assets must be an object")
    source_root_value = spec.get("source_root")
    if (
        not isinstance(source_root_value, str)
        or not source_root_value
        or source_root_value != source_root_value.strip()
    ):
        raise CharacterBuildError("template_assets.source_root must name a directory")
    source_root = repo_path(source_root_value)
    if not source_root.is_dir():
        raise CharacterBuildError(f"Template asset source was not found: {source_root}")
    source_depot_root = normalized_depot_root(
        spec.get("source_depot_root"), "template_assets.source_depot_root"
    )
    target_depot_root = normalized_depot_root(
        manifest.get("namespace"), "character namespace"
    )
    template_identity = manifest.get("template_identity")
    if not isinstance(template_identity, dict):
        raise CharacterBuildError("template_identity must be an object")
    identity_namespace = normalized_depot_root(
        template_identity.get("namespace"), "template_identity.namespace"
    )
    if source_depot_root.casefold() != identity_namespace.casefold():
        raise CharacterBuildError(
            "template_assets.source_depot_root must match template_identity.namespace"
        )
    records: list[dict[str, Any]] = []
    hashes: set[str] = set()
    for source in sorted(source_root.rglob("*.mesh"), key=lambda path: str(path).casefold()):
        relative = source.relative_to(source_root).as_posix().replace("/", "\\")
        source_depot_path = f"{source_depot_root}\\{relative}"
        resource_hash = fnv1a64_resource_path(source_depot_path)
        if resource_hash in hashes:
            raise CharacterBuildError(
                f"Template asset ResourcePath hash collision for {source_depot_path}"
            )
        hashes.add(resource_hash)
        records.append(
            {
                "hash": resource_hash,
                "source": source,
                "source_depot_path": source_depot_path,
                "target_depot_path": f"{target_depot_root}\\{relative}",
            }
        )
    if not records:
        raise CharacterBuildError(f"Template asset source contains no .mesh files: {source_root}")
    return records


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def stat_identity(path: Path) -> dict[str, Any]:
    stat = path.stat()
    return {"path": str(path.resolve()), "size": stat.st_size, "mtime_ns": stat.st_mtime_ns}


def head_preview_cache_key(source: Path, wolvenkit: Path, game_path: Path) -> str:
    game_executable = game_path / "bin/x64/Cyberpunk2077.exe"
    value = {
        "schema": 1,
        "source": {**stat_identity(source), "sha256": sha256_file(source)},
        "wolvenkit": stat_identity(wolvenkit),
        "game": stat_identity(game_executable) if game_executable.is_file() else str(game_path.resolve()),
    }
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def load_manifest(path: Path) -> dict[str, Any]:
    manifest = read_json(path)
    manifest["_manifest_path"] = str(path.resolve())
    return manifest


def load_catalog(manifest: dict[str, Any]) -> dict[str, Any]:
    value = manifest.get("catalog")
    if not isinstance(value, str) or not value:
        raise CharacterBuildError("Manifest catalog must be a repository-relative path")
    return read_json(repo_path(value))


def typed_value(value: Any) -> Any:
    if isinstance(value, dict) and "$value" in value:
        return value["$value"]
    return value


def set_typed_value(container: dict[str, Any], key: str, value: Any) -> None:
    current = container.get(key)
    if isinstance(current, dict) and "$value" in current:
        current["$value"] = value
    else:
        container[key] = value


def is_typed_string(value: Any, expected_type: str) -> bool:
    return (
        isinstance(value, dict)
        and value.get("$type") == expected_type
        and value.get("$storage") == "string"
        and isinstance(value.get("$value"), str)
    )


def appearance_data(document: dict[str, Any]) -> list[dict[str, Any]]:
    root = document.get("Data", {}).get("RootChunk", {})
    values = root.get("appearances", []) if isinstance(root, dict) else []
    rows: list[dict[str, Any]] = []
    if not isinstance(values, list):
        return rows
    for value in values:
        data = value.get("Data", value) if isinstance(value, dict) else None
        if isinstance(data, dict):
            rows.append(data)
    return rows


def component_name(component: dict[str, Any]) -> str:
    value = component.get("name")
    return str(typed_value(value) or "")


def component_sets(appearance: dict[str, Any]) -> list[list[dict[str, Any]]]:
    rows: list[list[dict[str, Any]]] = []
    components = appearance.get("components")
    if isinstance(components, list):
        rows.append([item for item in components if isinstance(item, dict)])
    compiled = appearance.get("compiledData", {}).get("Data", {}).get("Chunks")
    if isinstance(compiled, list):
        rows.append([item for item in compiled if isinstance(item, dict)])
    return rows


def components_by_name(appearance: dict[str, Any]) -> list[dict[str, dict[str, Any]]]:
    return [{component_name(item): item for item in values if component_name(item)} for values in component_sets(appearance)]


def find_appearance(document: dict[str, Any], name: str) -> dict[str, Any]:
    for appearance in appearance_data(document):
        if str(typed_value(appearance.get("name")) or "") == name:
            return appearance
    raise CharacterBuildError(f"Appearance template {name!r} was not found")


def required_component_names(manifest: dict[str, Any], catalog: dict[str, Any]) -> set[str]:
    """Return every named component required by the selected catalog operations."""
    required: set[str] = set()
    categories = catalog.get("categories", {})
    selections = manifest.get("appearance", {}).get("selections", {})
    if not isinstance(selections, dict):
        raise CharacterBuildError("appearance.selections must be an object")

    for category_id, option_id in selections.items():
        category = categories.get(category_id)
        option = category.get("options", {}).get(option_id) if isinstance(category, dict) else None
        if not isinstance(option, dict):
            raise CharacterBuildError(f"Unknown catalog selection {category_id}={option_id}")
        for key in ("component_names", "disable_components"):
            values = option.get(key, [])
            if not isinstance(values, list) or any(
                not isinstance(value, str) or not value for value in values
            ):
                raise CharacterBuildError(
                    f"Catalog {category_id}={option_id} has invalid {key}"
                )
            required.update(values)
        for change in option.get("changes", []):
            if not isinstance(change, dict) or not isinstance(change.get("component"), str):
                raise CharacterBuildError(f"Invalid change in {category_id}={option_id}")
            required.add(change["component"])
        for binding in option.get("bindings", []):
            if not isinstance(binding, dict) or not isinstance(binding.get("component"), str):
                raise CharacterBuildError(f"Invalid binding in {category_id}={option_id}")
            required.add(binding["component"])

    overrides = manifest.get("appearance", {}).get("indexed_overrides", {})
    if not isinstance(overrides, dict):
        raise CharacterBuildError("appearance.indexed_overrides must be an object")
    for category_id, override in overrides.items():
        config, _, _ = normalized_indexed_override(
            manifest, catalog, str(category_id), override
        )
        required.add(str(config["component"]))
    return required


def load_component_library(manifest: dict[str, Any]) -> tuple[dict[str, Any], Path]:
    templates = manifest.get("templates", {})
    library_value = templates.get("component_library") if isinstance(templates, dict) else None
    if not isinstance(library_value, str):
        raise CharacterBuildError("templates.component_library must be a repository path")
    library = read_json(repo_path(library_value))
    if library.get("schema_version") != 1:
        raise CharacterBuildError("Only component-library schema_version 1 is supported")
    if library.get("frame") != manifest.get("frame"):
        raise CharacterBuildError(
            "Component library frame must match the character manifest frame"
        )
    donor_value = library.get("donor")
    if not isinstance(donor_value, str) or not repo_path(donor_value).is_file():
        raise CharacterBuildError(f"Component library donor does not exist: {donor_value}")
    return library, repo_path(donor_value)


def load_component_archives(
    library: dict[str, Any], frame: str
) -> dict[str, tuple[dict[str, Any], dict[str, Any]]]:
    """Load optional normal/compiled component pairs that extend donor prototypes."""
    archive_values = library.get("component_archives", [])
    if not isinstance(archive_values, list) or any(
        not isinstance(value, str) or not value for value in archive_values
    ):
        raise CharacterBuildError(
            "Component library component_archives must be repository paths"
        )

    archived: dict[str, tuple[dict[str, Any], dict[str, Any]]] = {}
    for archive_value in archive_values:
        archive_path = repo_path(archive_value)
        if not archive_path.is_file():
            raise CharacterBuildError(f"Component archive does not exist: {archive_value}")
        archive = read_json(archive_path)
        if archive.get("schema_version") != 1:
            raise CharacterBuildError(
                f"Component archive {archive_value} must use schema_version 1"
            )
        if archive.get("frame") != frame:
            raise CharacterBuildError(
                f"Component archive {archive_value} frame must match {frame}"
            )
        components = archive.get("components")
        if not isinstance(components, list):
            raise CharacterBuildError(
                f"Component archive {archive_value} components must be a list"
            )
        for row in components:
            if not isinstance(row, dict):
                raise CharacterBuildError(
                    f"Component archive {archive_value} entries must be objects"
                )
            name = row.get("name")
            normal = row.get("normal")
            compiled = row.get("compiled")
            if (
                not isinstance(name, str)
                or not name
                or not isinstance(normal, dict)
                or not isinstance(compiled, dict)
                or component_name(normal) != name
                or component_name(compiled) != name
            ):
                raise CharacterBuildError(
                    f"Component archive {archive_value} has an invalid normal/compiled pair"
                )
            if name in archived:
                raise CharacterBuildError(f"Archived component {name!r} is duplicated")
            archived[name] = (normal, compiled)
    return archived


def select_component_prototype(
    manifest: dict[str, Any],
    catalog: dict[str, Any],
    library: dict[str, Any],
    donor: dict[str, Any],
) -> tuple[str, dict[str, Any]]:
    required = required_component_names(manifest, catalog)
    archived = load_component_archives(library, str(manifest.get("frame", "")))
    candidates: list[tuple[int, str, dict[str, Any]]] = []
    prototypes = library.get("prototypes")
    if not isinstance(prototypes, list) or not prototypes:
        raise CharacterBuildError("Component library must define at least one prototype")

    seen_ids: set[str] = set()
    seen_appearances: set[str] = set()
    for row in prototypes:
        if not isinstance(row, dict):
            raise CharacterBuildError("Component library prototypes must be objects")
        prototype_id = row.get("id")
        appearance_name = row.get("appearance")
        if (
            not isinstance(prototype_id, str)
            or not prototype_id
            or prototype_id in seen_ids
            or not isinstance(appearance_name, str)
            or not appearance_name
            or appearance_name in seen_appearances
        ):
            raise CharacterBuildError(
                "Component library prototype ids and appearances must be unique"
            )
        seen_ids.add(prototype_id)
        seen_appearances.add(appearance_name)
        appearance = copy.deepcopy(find_appearance(donor, appearance_name))
        mappings = components_by_name(appearance)
        if len(mappings) != 2:
            raise CharacterBuildError(
                f"Component prototype {prototype_id!r} must contain normal and compiled copies"
            )
        native = set(mappings[0]) & set(mappings[1])
        available = native | set(archived)
        if required <= available:
            normal_components = appearance.get("components")
            compiled_components = (
                appearance.get("compiledData", {}).get("Data", {}).get("Chunks")
            )
            if not isinstance(normal_components, list) or not isinstance(
                compiled_components, list
            ):
                raise CharacterBuildError(
                    f"Component prototype {prototype_id!r} has malformed component copies"
                )
            for name in sorted(required - native):
                normal, compiled = archived[name]
                normal_components.append(copy.deepcopy(normal))
                compiled_components.append(copy.deepcopy(compiled))
            candidates.append((len(normal_components), prototype_id, appearance))

    if not candidates:
        missing = ", ".join(sorted(required)) or "<no named requirements>"
        raise CharacterBuildError(
            f"No component prototype covers the selected character components: {missing}"
        )
    _, prototype_id, appearance = min(candidates, key=lambda item: (item[0], item[1]))
    return prototype_id, appearance


def assemble_appearance_document(
    manifest: dict[str, Any],
    catalog: dict[str, Any],
) -> tuple[dict[str, Any], str, Path]:
    templates = manifest["templates"]
    shell_value = templates.get("appearance_shell")
    if not isinstance(shell_value, str):
        raise CharacterBuildError("templates.appearance_shell must be a repository path")
    shell = read_json(repo_path(shell_value))
    if appearance_data(shell):
        raise CharacterBuildError("Appearance shell must not contain authored appearances")
    root = shell.get("Data", {}).get("RootChunk")
    if not isinstance(root, dict) or root.get("$type") != "appearanceAppearanceResource":
        raise CharacterBuildError("Appearance shell has an invalid RootChunk")

    library, donor_path = load_component_library(manifest)
    donor = read_json(donor_path)
    shell_entity_type = typed_value(root.get("baseEntityType"))
    donor_root = donor.get("Data", {}).get("RootChunk")
    donor_entity_type = (
        typed_value(donor_root.get("baseEntityType"))
        if isinstance(donor_root, dict)
        else None
    )
    if donor_entity_type != shell_entity_type:
        raise CharacterBuildError(
            "Appearance shell and component donor baseEntityType values must match"
        )
    prototype_id, prototype = select_component_prototype(
        manifest, catalog, library, donor
    )
    root["appearances"] = [{"HandleId": "0", "Data": copy.deepcopy(prototype)}]
    return shell, prototype_id, donor_path


def appearance_shell_document(donor: dict[str, Any]) -> dict[str, Any]:
    shell = copy.deepcopy(donor)
    root = shell.get("Data", {}).get("RootChunk")
    if not isinstance(root, dict) or root.get("$type") != "appearanceAppearanceResource":
        raise CharacterBuildError("Appearance donor has an invalid RootChunk")
    root["appearances"] = []
    header = shell.get("Header")
    if isinstance(header, dict):
        header["ArchiveFileName"] = ""
    return shell


def entity_shell_document(donor: dict[str, Any], frame: str) -> dict[str, Any]:
    profile = FRAME_PROFILES.get(frame)
    if profile is None:
        raise CharacterBuildError(f"Unsupported entity-shell frame: {frame}")
    shell = copy.deepcopy(donor)
    root = shell.get("Data", {}).get("RootChunk")
    if not isinstance(root, dict) or root.get("$type") != "entEntityTemplate":
        raise CharacterBuildError("Entity donor has an invalid RootChunk")
    components = root.get("components")
    expected_count = int(profile["root_component_count"])
    if not isinstance(components, list) or len(components) != expected_count:
        actual = len(components) if isinstance(components, list) else "malformed"
        raise CharacterBuildError(
            f"Entity donor has {actual} root components; {frame} requires {expected_count}"
        )
    mappings = root.get("appearances")
    if not isinstance(mappings, list) or not mappings or not isinstance(mappings[0], dict):
        raise CharacterBuildError("Entity donor has no appearance mapping")
    root["appearances"] = [copy.deepcopy(mappings[0])]
    mapping = root["appearances"][0].get("Data", root["appearances"][0])
    if not isinstance(mapping, dict):
        raise CharacterBuildError("Entity donor appearance mapping is malformed")
    set_typed_value(mapping, "name", "template_default")
    set_typed_value(mapping, "appearanceName", "default")
    resource = mapping.get("appearanceResource", {}).get("DepotPath")
    if not isinstance(resource, dict) or "$value" not in resource:
        raise CharacterBuildError("Entity donor appearanceResource is malformed")
    resource["$value"] = r"mod\ghostline\characters\template\template.app"
    set_typed_value(root, "defaultAppearance", "template_default")
    header = shell.get("Header")
    if isinstance(header, dict):
        header["ArchiveFileName"] = ""
    return shell


def set_nested(target: dict[str, Any], dotted_path: str, value: Any) -> None:
    keys = dotted_path.split(".")
    current: Any = target
    for key in keys[:-1]:
        if not isinstance(current, dict) or key not in current:
            raise CharacterBuildError(f"Component field {dotted_path!r} does not exist")
        current = current[key]
    if not isinstance(current, dict) or keys[-1] not in current:
        raise CharacterBuildError(f"Component field {dotted_path!r} does not exist")
    current[keys[-1]] = value


def binding_data(binding_type: str, bind_name: str, slot_name: str | None = None) -> dict[str, Any]:
    allowed = {
        "entAnimationControlBinding",
        "entHardTransformBinding",
        "entSkinningBinding",
    }
    if binding_type not in allowed:
        raise CharacterBuildError(f"Unsupported component binding type {binding_type!r}")
    value: dict[str, Any] = {
        "$type": binding_type,
        "bindName": {
            "$type": "CName",
            "$storage": "string",
            "$value": bind_name,
        },
        "enabled": 1,
        "enableMask": {
            "$type": "entTagMask",
            "excludedTags": {
                "$type": "redTagList",
                "tags": [
                    {
                        "$type": "CName",
                        "$storage": "string",
                        "$value": "NoBinding",
                    }
                ],
            },
            "hardTags": {"$type": "redTagList", "tags": []},
            "softTags": {"$type": "redTagList", "tags": []},
        },
    }
    if binding_type == "entHardTransformBinding":
        value["slotName"] = {
            "$type": "CName",
            "$storage": "string",
            "$value": slot_name or "None",
        }
    elif slot_name is not None:
        raise CharacterBuildError(f"slot_name is only valid for entHardTransformBinding, not {binding_type}")
    return value


def handle_ids(value: Any) -> set[int]:
    ids: set[int] = set()
    for item in walk_values(value):
        if not isinstance(item, dict) or "HandleId" not in item:
            continue
        raw = item["HandleId"]
        if not isinstance(raw, str) or not raw.isdigit():
            raise CharacterBuildError(f"Invalid CR2W HandleId {raw!r}")
        handle_id = int(raw)
        if handle_id in ids:
            raise CharacterBuildError(f"Duplicate CR2W HandleId {handle_id}")
        ids.add(handle_id)
    return ids


def renumber_handles(value: Any) -> dict[str, str]:
    wrappers = [
        item
        for item in walk_values(value)
        if isinstance(item, dict) and "HandleId" in item
    ]
    mapping: dict[str, str] = {}
    for new_id, wrapper in enumerate(wrappers):
        old_id = wrapper["HandleId"]
        if not isinstance(old_id, str) or not old_id.isdigit():
            raise CharacterBuildError(f"Invalid CR2W HandleId {old_id!r}")
        if old_id in mapping:
            raise CharacterBuildError(f"Duplicate CR2W HandleId {old_id}")
        mapping[old_id] = str(new_id)

    for item in walk_values(value):
        if not isinstance(item, dict):
            continue
        if "HandleId" in item:
            item["HandleId"] = mapping[str(item["HandleId"])]
        if "HandleRefId" in item:
            old_ref = item["HandleRefId"]
            if not isinstance(old_ref, str) or old_ref not in mapping:
                raise CharacterBuildError(f"Unresolved CR2W HandleRefId {old_ref!r}")
            item["HandleRefId"] = mapping[old_ref]
    return mapping


def apply_catalog_bindings(
    app_document: dict[str, Any],
    component_mappings: list[dict[str, dict[str, Any]]],
    category_id: str,
    option_id: str,
    bindings: Any,
) -> list[str]:
    if not bindings:
        return []
    if not isinstance(bindings, list):
        raise CharacterBuildError(f"Catalog bindings for {category_id}={option_id} must be a list")
    if len(component_mappings) != 2:
        raise CharacterBuildError(
            f"Catalog bindings for {category_id}={option_id} require components and compiledData copies"
        )

    used_ids = handle_ids(app_document)
    next_id = max(used_ids, default=-1) + 1
    warnings: list[str] = []
    allowed_fields = {
        "controlBinding": "entAnimationControlBinding",
        "parentTransform": "entHardTransformBinding",
        "skinning": "entSkinningBinding",
    }

    for binding in bindings:
        if not isinstance(binding, dict):
            raise CharacterBuildError(f"Invalid binding in {category_id}={option_id}")
        component_name_value = str(binding.get("component", ""))
        field = str(binding.get("field", ""))
        binding_type = str(binding.get("type", ""))
        bind_name = str(binding.get("bind_name", ""))
        expected_type = allowed_fields.get(field)
        if expected_type is None or binding_type != expected_type or not bind_name:
            raise CharacterBuildError(
                f"Invalid {field or 'component'} binding in {category_id}={option_id}"
            )
        normal = component_mappings[0].get(component_name_value)
        compiled = component_mappings[1].get(component_name_value)
        if normal is None or compiled is None:
            raise CharacterBuildError(
                f"Binding targets missing component {component_name_value!r} in {category_id}={option_id}"
            )
        if field not in normal or field not in compiled:
            raise CharacterBuildError(
                f"Binding field {field!r} is absent from {component_name_value!r}"
            )

        current_compiled = compiled[field]
        current_handle = current_compiled.get("HandleId") if isinstance(current_compiled, dict) else None
        if current_handle is not None:
            if not isinstance(current_handle, str) or not current_handle.isdigit():
                raise CharacterBuildError(
                    f"Binding {component_name_value}.{field} has invalid HandleId {current_handle!r}"
                )
            handle_id = int(current_handle)
        else:
            while next_id in used_ids:
                next_id += 1
            handle_id = next_id
            used_ids.add(handle_id)
            next_id += 1

        normal[field] = {"HandleRefId": str(handle_id)}
        compiled[field] = {
            "HandleId": str(handle_id),
            "Data": binding_data(binding_type, bind_name, binding.get("slot_name")),
        }
        warnings.append(
            f"{category_id}={option_id} rewires {component_name_value}.{field}; verify its companion bundle in game"
        )
    return warnings


def walk_values(value: Any) -> Iterable[Any]:
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from walk_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_values(child)


def resource_paths(value: Any) -> list[str]:
    paths: list[str] = []
    for item in walk_values(value):
        if isinstance(item, dict) and item.get("$type") == "ResourcePath":
            path = item.get("$value")
            if path not in (None, "", "0", 0) and str(path) not in paths:
                paths.append(str(path))
    return paths


def replace_strings(value: Any, replacements: list[tuple[str, str]]) -> Any:
    if isinstance(value, str):
        for old, new in replacements:
            if old and old != new:
                value = value.replace(old, new)
        return value
    if isinstance(value, list):
        return [replace_strings(child, replacements) for child in value]
    if isinstance(value, dict):
        return {key: replace_strings(child, replacements) for key, child in value.items()}
    return value


def resolve_template_asset_paths(value: Any, records: list[dict[str, Any]]) -> int:
    """Replace serialized numeric tutorial mesh paths with explicit character paths."""
    by_hash = {record["hash"]: record["target_depot_path"] for record in records}
    by_source = {
        str(record["source_depot_path"]).casefold(): record["target_depot_path"]
        for record in records
    }
    replaced = 0

    def visit(child: Any) -> None:
        nonlocal replaced
        if isinstance(child, list):
            for item in child:
                visit(item)
            return
        if not isinstance(child, dict):
            return
        if child.get("$type") == "ResourcePath":
            raw = child.get("$value")
            target = by_hash.get(str(raw))
            if target is None and isinstance(raw, str):
                target = by_source.get(raw.casefold())
            if target is not None and raw != target:
                child["$storage"] = "string"
                child["$value"] = target
                replaced += 1
        for item in child.values():
            visit(item)

    visit(value)
    return replaced


def stage_template_assets(
    manifest: dict[str, Any],
    entity: dict[str, Any],
    appearance: dict[str, Any],
    output_root: Path,
) -> list[str]:
    spec = manifest.get("template_assets")
    if not isinstance(spec, dict):
        return []
    records = template_asset_records(manifest)
    referenced = {
        path.casefold() for path in resource_paths(entity) + resource_paths(appearance)
    }
    staged: list[str] = []
    for record in records:
        depot_path = str(record["target_depot_path"])
        if depot_path.casefold() not in referenced:
            continue
        normalized_depot_path = depot_path.replace("\\", "/")
        relative = f"source/archive/{normalized_depot_path}"
        target = output_path(output_root, relative)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(record["source"], target)
        staged.append(relative)

    source_root = repo_path(str(spec.get("source_root", "")))
    source_depot_root = normalized_depot_root(
        spec.get("source_depot_root"), "template_assets.source_depot_root"
    )
    dependency_globs = spec.get("dependency_globs", [])
    if not isinstance(dependency_globs, list):
        raise CharacterBuildError("template_assets.dependency_globs must be a list")
    for pattern in dependency_globs:
        if (
            not isinstance(pattern, str)
            or not pattern
            or "\\" in pattern
            or ":" in pattern
            or ".." in Path(pattern).parts
        ):
            raise CharacterBuildError(
                "template_assets.dependency_globs entries must be safe source-relative glob patterns"
            )
        for source in sorted(source_root.glob(pattern), key=lambda path: str(path).casefold()):
            if not source.is_file():
                continue
            child = source.relative_to(source_root).as_posix()
            normalized_source_root = source_depot_root.replace("\\", "/")
            relative = f"source/archive/{normalized_source_root}/{child}"
            target = output_path(output_root, relative)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
            staged.append(relative)
    return sorted(set(staged), key=str.casefold)


def archive_path_for_raw(raw_path: str) -> Path:
    normalized = raw_path.replace("\\", "/")
    if not normalized.startswith("source/raw/") or not normalized.endswith(".json"):
        raise CharacterBuildError(f"CR2W raw output has unexpected path: {raw_path}")
    relative = normalized.removeprefix("source/raw/").removesuffix(".json")
    return ROOT / "source/archive" / relative


def set_archive_header(document: dict[str, Any], raw_output: str) -> None:
    header = document.get("Header")
    if not isinstance(header, dict):
        raise CharacterBuildError("CR2W JSON is missing Header")
    header["ArchiveFileName"] = str(archive_path_for_raw(raw_output))


def apply_catalog_selections(
    app_document: dict[str, Any], manifest: dict[str, Any], catalog: dict[str, Any]
) -> list[str]:
    app_spec = manifest["appearance"]
    appearances = appearance_data(app_document)
    if len(appearances) != 1:
        raise CharacterBuildError(
            "Generated appearance document must contain exactly one assembled appearance"
        )
    appearance = appearances[0]
    sets = components_by_name(appearance)
    warnings: list[str] = []
    categories = catalog.get("categories", {})
    selections = app_spec.get("selections", {})

    for category_id, option_id in selections.items():
        category = categories.get(category_id)
        option = category.get("options", {}).get(option_id) if isinstance(category, dict) else None
        if not isinstance(option, dict):
            raise CharacterBuildError(f"Unknown catalog selection {category_id}={option_id}")

        expected_names = option.get("component_names", [])
        disabled_names = option.get("disable_components", [])
        for name in [*expected_names, *disabled_names]:
            missing = [index for index, mapping in enumerate(sets) if name not in mapping]
            if missing:
                raise CharacterBuildError(
                    f"Catalog component {name!r} is absent from appearance copy/copies {missing}"
                )

        for name in disabled_names:
            for mapping in sets:
                mapping[name]["isEnabled"] = 0

        warnings.extend(
            apply_catalog_bindings(
                app_document,
                sets,
                str(category_id),
                str(option_id),
                option.get("bindings", []),
            )
        )

        resource_changes = False
        for change in option.get("changes", []):
            if not isinstance(change, dict):
                raise CharacterBuildError(f"Invalid change in {category_id}={option_id}")
            name = str(change.get("component", ""))
            path = str(change.get("path", ""))
            for mapping in sets:
                if name not in mapping:
                    raise CharacterBuildError(f"Change targets missing component {name!r}")
                set_nested(mapping[name], path, copy.deepcopy(change.get("value")))
            if "ResourcePath" in path or path.endswith(".$value"):
                resource_changes = True
        if resource_changes:
            warnings.append(f"{category_id}={option_id} changes resources; recheck resolved dependencies")

    set_typed_value(appearance, "name", app_spec["name"])
    return warnings


def normalized_indexed_override(
    manifest: dict[str, Any], catalog: dict[str, Any], category_id: str, override: Any
) -> tuple[dict[str, Any], str, str]:
    categories = catalog.get("categories", {})
    category = categories.get(category_id) if isinstance(categories, dict) else None
    config = category.get("indexed_override") if isinstance(category, dict) else None
    if not isinstance(config, dict):
        raise CharacterBuildError(f"Category {category_id!r} does not support indexed mesh overrides")
    if not isinstance(override, dict):
        raise CharacterBuildError(f"Indexed override {category_id!r} must be an object")
    unknown = sorted(set(override) - INDEXED_OVERRIDE_KEYS)
    if unknown:
        raise CharacterBuildError(
            f"Indexed override {category_id!r} contains unsupported fields: {', '.join(unknown)}"
        )

    depot_path = override.get("depot_path")
    mesh_appearance = override.get("mesh_appearance")
    asset_slot = str(config.get("asset_slot", ""))
    frame_token = str(config.get("frame_token", ""))
    component = str(config.get("component", ""))
    anchor_option = str(config.get("anchor_option", ""))
    if not all((asset_slot, frame_token, component, anchor_option)):
        raise CharacterBuildError(f"Catalog indexed override metadata is incomplete for {category_id!r}")
    required_frame_token = str(frame_profile(manifest)["player_token"])
    if frame_token.casefold() != required_frame_token.casefold():
        raise CharacterBuildError(
            f"Catalog indexed override {category_id!r} uses {frame_token or 'no'} body frame, "
            f"but {manifest.get('frame')} requires {required_frame_token}"
        )
    if not isinstance(depot_path, str) or not depot_path:
        raise CharacterBuildError(f"Indexed override {category_id!r} requires a depot_path")
    depot_segments = depot_path.split("\\")
    if (
        "/" in depot_path
        or ":" in depot_path
        or depot_path != depot_path.strip()
        or any(not segment or segment in {".", ".."} for segment in depot_segments)
    ):
        raise CharacterBuildError(
            f"Indexed override {category_id!r} depot_path must be a normalized game depot path"
        )
    path_pattern = re.compile(
        rf"^(?:base|ep1)\\characters\\garment\\player_equipment\\{re.escape(asset_slot)}\\.+\.mesh$",
        re.IGNORECASE,
    )
    if not path_pattern.fullmatch(depot_path):
        raise CharacterBuildError(
            f"Indexed override {category_id!r} must reference a {asset_slot} player-equipment .mesh"
        )
    depot_file_name = depot_segments[-1]
    filename_frames = {
        match.group(1).casefold() for match in FRAME_TOKEN_PATTERN.finditer(depot_file_name)
    }
    if filename_frames != {frame_token.casefold()}:
        raise CharacterBuildError(
            f"Indexed override {category_id!r} must use the {frame_token} body frame"
        )
    if (
        not isinstance(mesh_appearance, str)
        or not mesh_appearance
        or len(mesh_appearance) > 128
        or CNAME_PATTERN.fullmatch(mesh_appearance) is None
    ):
        raise CharacterBuildError(
            f"Indexed override {category_id!r} requires a valid mesh appearance name"
        )
    selected_option = manifest.get("appearance", {}).get("selections", {}).get(category_id)
    if selected_option != anchor_option:
        raise CharacterBuildError(
            f"Indexed override {category_id!r} requires curated anchor {anchor_option!r}"
        )
    if depot_path.casefold().startswith("ep1\\") and manifest.get("requirements", {}).get(
        "phantom_liberty"
    ) is not True:
        raise CharacterBuildError(
            f"Indexed override {category_id!r} references ep1\\ without declaring Phantom Liberty"
        )
    return config, depot_path, mesh_appearance


def apply_indexed_overrides(
    app_document: dict[str, Any], manifest: dict[str, Any], catalog: dict[str, Any]
) -> list[str]:
    overrides = manifest.get("appearance", {}).get("indexed_overrides", {})
    if not overrides:
        return []
    if not isinstance(overrides, dict):
        raise CharacterBuildError("appearance.indexed_overrides must be an object")

    appearance = find_appearance(app_document, str(manifest["appearance"]["name"]))
    sets = components_by_name(appearance)
    if len(sets) != 2:
        raise CharacterBuildError(
            "Indexed overrides require both components and compiledData component copies"
        )
    warnings: list[str] = []
    for category_id, override in overrides.items():
        config, depot_path, mesh_appearance = normalized_indexed_override(
            manifest, catalog, category_id, override
        )
        component_name_value = str(config["component"])
        for index, mapping in enumerate(sets):
            component = mapping.get(component_name_value)
            if component is None:
                raise CharacterBuildError(
                    f"Indexed override target {component_name_value!r} is absent from appearance copy {index}"
                )
            allowed_types = config.get("component_types", ["entGarmentSkinnedMeshComponent"])
            if (
                not isinstance(allowed_types, list)
                or not allowed_types
                or any(not isinstance(value, str) or not value for value in allowed_types)
            ):
                raise CharacterBuildError(
                    f"Indexed override {category_id!r} has invalid component_types metadata"
                )
            if component.get("$type") not in allowed_types:
                raise CharacterBuildError(
                    f"Indexed override target {component_name_value!r} has unsupported component type "
                    f"{component.get('$type')!r}"
                )
            mesh = component.get("mesh", {}).get("DepotPath")
            mesh_appearance_value = component.get("meshAppearance")
            if not is_typed_string(mesh, "ResourcePath"):
                raise CharacterBuildError(
                    f"Indexed override target {component_name_value!r} has no typed ResourcePath DepotPath"
                )
            if not is_typed_string(mesh_appearance_value, "CName"):
                raise CharacterBuildError(
                    f"Indexed override target {component_name_value!r} has no typed CName meshAppearance"
                )
            mesh["$value"] = depot_path
            mesh_appearance_value["$value"] = mesh_appearance
            component["isEnabled"] = 1
        warnings.append(
            f"{category_id} uses indexed mesh {depot_path}; its curated cuff/shadow companion remains provisional"
        )
    return warnings


def render_tweak(manifest: dict[str, Any]) -> str:
    tweak = manifest["tweak"]
    namespace = manifest["namespace"]
    entity_file = manifest["entity"]["file_name"]
    combat = tweak.get("combat")
    lines = [
        f"{tweak['record']}:",
        f"  $base: {tweak['base']}",
        f"  entityTemplatePath: {namespace}\\{entity_file}",
        f"  displayName: {tweak['display_name']}",
        f"  fullDisplayName: {tweak['display_name']}",
        f"  affiliation: {tweak['affiliation']}",
        f"  voiceTag: {tweak['voice_tag']}",
    ]
    if not isinstance(combat, dict):
        return "\n".join(lines) + "\n"

    record = tweak["record"]
    level_modifier = f"{record}_FixedLevel"
    content_assignment = f"{record}_FixedLevelContent"
    health_modifier = f"{record}_HealthMultiplier"
    boss_stat_group = f"{record}_BossStatModifiers"
    equipment_group = f"{record}_PrimaryEquipment"
    weapon_record = f"{record}_PrimaryWeapon"

    scalar_fields = (
        ("action_map", "actionMap"),
        ("archetype_data", "archetypeData"),
        ("base_attitude_group", "baseAttitudeGroup"),
        ("rarity", "rarity"),
        ("reaction_preset", "reactionPreset"),
        ("scanner_module_preset", "scannerModulePreset"),
        ("threat_tracking_preset", "threatTrackingPreset"),
        ("ui_nameplate", "uiNameplate"),
    )
    for source_name, output_name in scalar_fields:
        value = combat.get(source_name)
        if value is not None:
            lines.append(f"  {output_name}: {value}")

    bool_fields = (
        ("disable_defeated_state", "disableDefeatedState"),
        ("drops_weapon_on_death", "dropsWeaponOnDeath"),
        ("skip_display_archetype", "skipDisplayArchetype"),
    )
    for source_name, output_name in bool_fields:
        value = combat.get(source_name)
        if value is not None:
            lines.append(f"  {output_name}: {str(value).lower()}")

    for source_name, output_name in (
        ("abilities", "abilities"),
        ("effectors", "effectors"),
        ("tags", "tags"),
        ("visual_tags", "visualTags"),
    ):
        values = combat.get(source_name)
        if values:
            lines.append(f"  {output_name}:")
            lines.extend(f"    - {value}" for value in values)

    stat_modifier_groups = list(combat.get("stat_modifier_groups", []))
    if "health_multiplier" in combat:
        stat_modifier_groups.append(boss_stat_group)
    if stat_modifier_groups:
        lines.append("  statModifierGroups:")
        lines.extend(f"    - {value}" for value in stat_modifier_groups)

    if "level" in combat:
        lines.append(f"  contentAssignment: {content_assignment}")
    weapon = combat.get("primary_weapon")
    if isinstance(weapon, dict):
        lines.append(f"  primaryEquipment: {equipment_group}")

    records: list[str] = []
    if "level" in combat:
        records.extend(
            [
                f"{level_modifier}:",
                "  $type: gamedataConstantStatModifier_Record",
                "  statType: BaseStats.PowerLevel",
                "  modifierType: Additive",
                f"  value: {combat['level']}",
                "",
                f"{content_assignment}:",
                "  $type: gamedataDeviceContentAssignment_Record",
                f"  powerLevelMod: {level_modifier}",
            ]
        )
    if "health_multiplier" in combat:
        if records:
            records.append("")
        records.extend(
            [
                f"{health_modifier}:",
                "  $type: gamedataConstantStatModifier_Record",
                "  statType: BaseStats.Health",
                "  modifierType: Multiplier",
                f"  value: {combat['health_multiplier']}",
                "",
                f"{boss_stat_group}:",
                "  $type: gamedataStatModifierGroup_Record",
                "  statModifiers:",
                f"    - {health_modifier}",
            ]
        )
    if isinstance(weapon, dict):
        if records:
            records.append("")
        records.extend(
            [
                f"{equipment_group}:",
                "  $type: gamedataNPCEquipmentGroup_Record",
                "  equipmentItems:",
                f"    - {weapon_record}",
                "",
                f"{weapon_record}:",
                "  $type: gamedataNPCEquipmentItem_Record",
                f"  item: {weapon['item']}",
                f"  equipSlot: {weapon['equip_slot']}",
                f"  onBodySlot: {weapon['on_body_slot']}",
                "  equipCondition:",
                f"    - {weapon['equip_condition']}",
                "  unequipCondition:",
                f"    - {weapon['unequip_condition']}",
            ]
        )

    if records:
        lines.extend(["", *records])
    return "\n".join(lines) + "\n"


def update_localization(document: dict[str, Any], manifest: dict[str, Any]) -> None:
    spec = manifest["localization"]
    root = document.get("Data", {}).get("RootChunk", {}).get("root", {}).get("Data", {})
    entries = root.get("entries") if isinstance(root, dict) else None
    if not isinstance(entries, list):
        raise CharacterBuildError("Localization template has no onscreen entries")
    matching = [item for item in entries if item.get("secondaryKey") == spec["secondary_key"]]
    if matching:
        entry = matching[0]
    else:
        entry = {"$type": "localizationPersistenceOnScreenEntry", "primaryKey": "0"}
        entries.append(entry)
    entry["femaleVariant"] = spec.get("female_variant", "")
    entry["maleVariant"] = spec.get("male_variant", "")
    entry["secondaryKey"] = spec["secondary_key"]


def validate_manifest(manifest: dict[str, Any], catalog: dict[str, Any] | None = None) -> ValidationReport:
    report = ValidationReport()
    if manifest.get("schema_version") != 1:
        report.errors.append("Only character schema_version 1 is supported")
    for key in ("id", "display_name", "namespace", "templates", "outputs", "entity", "appearance", "tweak"):
        if key not in manifest:
            report.errors.append(f"Manifest is missing {key}")

    namespace = str(manifest.get("namespace", ""))
    if not namespace.startswith("mod\\") or ".." in namespace or namespace.endswith("\\"):
        report.errors.append("namespace must be a normalized mod\\... depot path")

    frame = manifest.get("frame")
    profile = FRAME_PROFILES.get(str(frame))
    if profile is None:
        report.errors.append(
            f"Unsupported character frame {frame!r}; choose one of {', '.join(FRAME_PROFILES)}"
        )
    template_identity = manifest.get("template_identity")
    if not isinstance(template_identity, dict):
        report.errors.append("template_identity must be an object")
        template_identity = {}
    template_frame = template_identity.get("frame")
    if template_frame != frame:
        report.errors.append(
            "template_identity.frame must match the manifest frame so root entity templates cannot be mixed"
        )

    phantom_liberty = manifest.get("requirements", {}).get("phantom_liberty")
    if not isinstance(phantom_liberty, bool):
        report.errors.append("requirements.phantom_liberty must be a JSON boolean")

    tweak = manifest.get("tweak")
    if not isinstance(tweak, dict):
        report.errors.append("tweak must be an object")
        tweak = {}
    combat = tweak.get("combat")
    if combat is not None and not isinstance(combat, dict):
        report.errors.append("tweak.combat must be an object")
        combat = {}
    if isinstance(combat, dict) and combat:
        level = combat.get("level")
        max_level = 60 if phantom_liberty is True else 50
        if not isinstance(level, int) or isinstance(level, bool) or not 1 <= level <= max_level:
            report.errors.append(
                f"tweak.combat.level must be an integer from 1 through {max_level}"
            )
        health_multiplier = combat.get("health_multiplier")
        if (
            not isinstance(health_multiplier, (int, float))
            or isinstance(health_multiplier, bool)
            or not 1.0 <= float(health_multiplier) <= 100.0
        ):
            report.errors.append(
                "tweak.combat.health_multiplier must be a number from 1 through 100"
            )
        for key in (
            "action_map",
            "archetype_data",
            "base_attitude_group",
            "rarity",
            "reaction_preset",
            "scanner_module_preset",
            "threat_tracking_preset",
            "ui_nameplate",
        ):
            if not isinstance(combat.get(key), str) or not combat[key]:
                report.errors.append(f"tweak.combat.{key} must be a non-empty string")
        for key in ("disable_defeated_state", "drops_weapon_on_death", "skip_display_archetype"):
            if not isinstance(combat.get(key), bool):
                report.errors.append(f"tweak.combat.{key} must be a JSON boolean")
        for key in ("abilities", "effectors", "stat_modifier_groups", "tags", "visual_tags"):
            values = combat.get(key)
            if (
                not isinstance(values, list)
                or not values
                or any(not isinstance(value, str) or not value for value in values)
            ):
                report.errors.append(
                    f"tweak.combat.{key} must be a non-empty list of record names"
                )
        weapon = combat.get("primary_weapon")
        if not isinstance(weapon, dict):
            report.errors.append("tweak.combat.primary_weapon must be an object")
        else:
            for key in (
                "item",
                "equip_slot",
                "on_body_slot",
                "equip_condition",
                "unequip_condition",
            ):
                if not isinstance(weapon.get(key), str) or not weapon[key]:
                    report.errors.append(
                        f"tweak.combat.primary_weapon.{key} must be a non-empty string"
                    )

    templates = manifest.get("templates")
    if not isinstance(templates, dict):
        report.errors.append("templates must be an object")
        templates = {}
    for required_template in (
        "entity",
        "appearance_shell",
        "component_library",
        "localization",
    ):
        if required_template not in templates:
            report.errors.append(f"templates is missing {required_template}")
    for kind, value in templates.items():
        if not isinstance(value, str) or not repo_path(value).is_file():
            report.errors.append(f"Template {kind} does not exist: {value}")

    if profile is not None:
        entity_template = templates.get("entity")
        if isinstance(entity_template, str) and repo_path(entity_template).is_file():
            try:
                entity_document = read_json(repo_path(entity_template))
                root_components = entity_document.get("Data", {}).get("RootChunk", {}).get(
                    "components"
                )
                expected_count = int(profile["root_component_count"])
                if not isinstance(root_components, list) or len(root_components) != expected_count:
                    actual = len(root_components) if isinstance(root_components, list) else "malformed"
                    report.errors.append(
                        f"Entity template has {actual} root components; {frame} requires {expected_count}"
                    )
            except CharacterBuildError as exc:
                report.errors.append(str(exc))
        appearance_shell = templates.get("appearance_shell")
        if isinstance(appearance_shell, str) and repo_path(appearance_shell).is_file():
            try:
                appearance_document = read_json(repo_path(appearance_shell))
                actual_type = typed_value(
                    appearance_document.get("Data", {}).get("RootChunk", {}).get("baseEntityType")
                )
                if actual_type != profile["base_entity_type"]:
                    report.errors.append(
                        f"Appearance shell baseEntityType is {actual_type!r}; {frame} requires "
                        f"{profile['base_entity_type']!r}"
                    )
                if appearance_data(appearance_document):
                    report.errors.append(
                        "Appearance shell must not contain authored appearances"
                    )
            except CharacterBuildError as exc:
                report.errors.append(str(exc))

    outputs = manifest.get("outputs", {})
    for kind, value in outputs.items():
        normalized = str(value).replace("\\", "/")
        if not normalized.startswith("source/") or ".." in normalized.split("/"):
            report.errors.append(f"Output {kind} must stay under source/: {value}")

    if catalog is None:
        try:
            catalog = load_catalog(manifest)
        except CharacterBuildError as exc:
            report.errors.append(str(exc))
            catalog = {}
    if catalog.get("schema_version") != 1:
        report.errors.append("Only catalog schema_version 1 is supported")
    catalog_frames = catalog.get("frames")
    if (
        not isinstance(catalog_frames, list)
        or not catalog_frames
        or any(value not in FRAME_PROFILES for value in catalog_frames)
    ):
        report.errors.append("Catalog frames must list one or more supported character frames")
    elif frame not in catalog_frames:
        report.errors.append(
            f"Catalog {catalog.get('id', '')!r} does not support character frame {frame!r}"
        )
    categories = catalog.get("categories", {})
    for category_id, option_id in manifest.get("appearance", {}).get("selections", {}).items():
        category = categories.get(category_id)
        options = category.get("options", {}) if isinstance(category, dict) else {}
        if option_id not in options:
            report.errors.append(f"Unknown catalog selection {category_id}={option_id}")

    overrides = manifest.get("appearance", {}).get("indexed_overrides", {})
    if not isinstance(overrides, dict):
        report.errors.append("appearance.indexed_overrides must be an object")
        overrides = {}
    for category_id, override in overrides.items():
        try:
            normalized_indexed_override(manifest, catalog, str(category_id), override)
        except CharacterBuildError as exc:
            report.errors.append(str(exc))
        else:
            report.warnings.append(
                f"Indexed {category_id} mesh exists in the installed-game catalog only after UI/index validation"
            )

    try:
        _, component_prototype, _ = assemble_appearance_document(manifest, catalog)
    except CharacterBuildError as exc:
        report.errors.append(str(exc))
        component_prototype = ""

    try:
        template_assets = template_asset_records(manifest)
    except CharacterBuildError as exc:
        report.errors.append(str(exc))
        template_assets = []
    template_asset_spec = manifest.get("template_assets")
    dependency_globs = (
        template_asset_spec.get("dependency_globs", [])
        if isinstance(template_asset_spec, dict)
        else []
    )
    if template_asset_spec is not None and not isinstance(dependency_globs, list):
        report.errors.append("template_assets.dependency_globs must be a list")
    elif isinstance(dependency_globs, list):
        for pattern in dependency_globs:
            if (
                not isinstance(pattern, str)
                or not pattern
                or "\\" in pattern
                or ":" in pattern
                or Path(pattern).is_absolute()
                or ".." in Path(pattern).parts
            ):
                report.errors.append(
                    "template_assets.dependency_globs entries must be safe source-relative glob patterns"
                )

    shapes = manifest.get("head", {}).get("shapes", {})
    head_shape_max = int(profile["head_shape_max"]) if profile is not None else HEAD_SHAPE_MAX
    for name in SHAPE_NAMES:
        value = shapes.get(name)
        if value is None:
            report.warnings.append(f"Head shape {name} is unset; head generation is unavailable")
        elif not isinstance(value, int) or not HEAD_SHAPE_MIN <= value <= head_shape_max:
            suffix = (
                "; the current male morph resources do not contain the documented option 22 target"
                if frame == "male_average" and value == 22
                else ""
            )
            report.errors.append(
                f"Head shape {name} must be an integer from {HEAD_SHAPE_MIN} through {head_shape_max}{suffix}"
            )

    morph_names = manifest.get("head", {}).get("morphtargets", [])
    if not isinstance(morph_names, list) or not morph_names:
        report.errors.append("Manifest head.morphtargets must select at least one file")
    elif profile is not None:
        expected_token = str(profile["player_token"])
        for value in morph_names:
            filename_frames = {
                match.group(1).casefold()
                for match in FRAME_TOKEN_PATTERN.finditer(Path(str(value)).name)
            }
            if filename_frames != {expected_token}:
                report.errors.append(
                    f"Head morphtarget {value!r} must use the {expected_token} body frame"
                )

    report.details["manifest"] = manifest.get("_manifest_path", "")
    report.details["catalog"] = manifest.get("catalog", "")
    report.details["frame"] = frame
    report.details["player_frame_token"] = profile.get("player_token") if profile else ""
    report.details["template_assets"] = len(template_assets)
    report.details["selections"] = len(manifest.get("appearance", {}).get("selections", {}))
    report.details["indexed_overrides"] = len(overrides)
    report.details["component_prototype"] = component_prototype
    return report


def validate_generated(
    manifest: dict[str, Any], entity: dict[str, Any], appearance: dict[str, Any]
) -> ValidationReport:
    report = ValidationReport()
    entity_apps = appearance_data(entity)
    app_apps = appearance_data(appearance)
    entity_spec = manifest["entity"]
    namespace = manifest["namespace"]
    profile = frame_profile(manifest)

    root_components = entity.get("Data", {}).get("RootChunk", {}).get("components")
    expected_root_components = int(profile["root_component_count"])
    if not isinstance(root_components, list) or len(root_components) != expected_root_components:
        actual = len(root_components) if isinstance(root_components, list) else "malformed"
        report.errors.append(
            f"Generated entity has {actual} root components, expected {expected_root_components} "
            f"for {manifest['frame']}"
        )

    app_root = appearance.get("Data", {}).get("RootChunk", {})
    actual_base_entity_type = typed_value(app_root.get("baseEntityType"))
    if actual_base_entity_type != profile["base_entity_type"]:
        report.errors.append(
            f"Appearance baseEntityType is {actual_base_entity_type!r}, expected "
            f"{profile['base_entity_type']!r} for {manifest['frame']}"
        )

    if len(entity_apps) != 1:
        report.errors.append(f"Schema v1 expects exactly one root appearance, found {len(entity_apps)}")
    if len(app_apps) != 1:
        report.errors.append(f"Schema v1 expects exactly one app appearance, found {len(app_apps)}")

    if entity_apps:
        row = entity_apps[0]
        expected_resource = f"{namespace}\\{entity_spec['appearance_file']}"
        actual_resource = resource_paths(row.get("appearanceResource", {}))
        if str(typed_value(row.get("name")) or "") != entity_spec["root_appearance"]:
            report.errors.append("Root appearance name does not match the manifest")
        if str(typed_value(row.get("appearanceName")) or "") != entity_spec["appearance_name"]:
            report.errors.append("Root appearanceName does not match the manifest")
        if actual_resource != [expected_resource]:
            report.errors.append(f"Root appearance resource is {actual_resource}, expected {expected_resource}")

    if app_apps:
        row = app_apps[0]
        if str(typed_value(row.get("name")) or "") != entity_spec["appearance_name"]:
            report.errors.append("App appearance name does not match the root mapping")
        names = [component_name(item) for item in row.get("components", []) if isinstance(item, dict)]
        duplicates = sorted({name for name in names if name and name != "Component" and names.count(name) > 1})
        if duplicates:
            report.errors.append(f"Duplicate appearance component names: {', '.join(duplicates)}")
        mappings = components_by_name(row)
        if manifest.get("appearance", {}).get("indexed_overrides") and len(mappings) != 2:
            report.errors.append(
                "Generated indexed overrides require both components and compiledData component copies"
            )
        for category_id, override in manifest.get("appearance", {}).get(
            "indexed_overrides", {}
        ).items():
            try:
                config, depot_path, mesh_appearance = normalized_indexed_override(
                    manifest, load_catalog(manifest), category_id, override
                )
            except CharacterBuildError as exc:
                report.errors.append(str(exc))
                continue
            target_name = str(config["component"])
            for index, mapping in enumerate(mappings):
                component = mapping.get(target_name)
                if component is None:
                    report.errors.append(
                        f"Generated indexed override target {target_name!r} is missing from copy {index}"
                    )
                    continue
                mesh_value = component.get("mesh", {}).get("DepotPath")
                appearance_value = component.get("meshAppearance")
                if not is_typed_string(mesh_value, "ResourcePath"):
                    report.errors.append(
                        f"Generated indexed override {category_id!r} has a malformed ResourcePath in copy {index}"
                    )
                    continue
                if not is_typed_string(appearance_value, "CName"):
                    report.errors.append(
                        f"Generated indexed override {category_id!r} has a malformed CName in copy {index}"
                    )
                    continue
                actual_path = mesh_value["$value"]
                actual_appearance = appearance_value["$value"]
                if actual_path != depot_path or actual_appearance != mesh_appearance:
                    report.errors.append(
                        f"Generated indexed override {category_id!r} does not match its manifest in copy {index}"
                    )
                if component.get("isEnabled") != 1:
                    report.errors.append(
                        f"Generated indexed override {category_id!r} is disabled in copy {index}"
                    )

    all_resources = resource_paths(entity) + resource_paths(appearance)
    numeric = sorted({path for path in all_resources if path.isdigit()})
    template_resources: list[str] = []
    entity_template = manifest.get("templates", {}).get("entity")
    if isinstance(entity_template, str) and repo_path(entity_template).is_file():
        template_resources.extend(resource_paths(read_json(repo_path(entity_template))))
    try:
        _, donor_path = load_component_library(manifest)
    except CharacterBuildError as exc:
        report.errors.append(str(exc))
    else:
        template_resources.extend(resource_paths(read_json(donor_path)))
    template_numeric = {path for path in template_resources if path.isdigit()}
    template_asset_map = template_asset_records(manifest)
    mapped_target_numeric = {
        fnv1a64_resource_path(str(record["target_depot_path"]))
        for record in template_asset_map
    }
    resolved_mapped_numeric = sorted(set(numeric) & mapped_target_numeric)
    preserved_template_numeric = set() if template_asset_map else template_numeric
    new_numeric = sorted(set(numeric) - preserved_template_numeric - mapped_target_numeric)
    if new_numeric:
        report.errors.append(f"Generated new opaque numeric ResourcePath values: {', '.join(new_numeric)}")
    elif resolved_mapped_numeric:
        report.warnings.append(
            f"Resolved {len(resolved_mapped_numeric)} hashed template ResourcePaths through the manifest asset map"
        )
    elif numeric:
        report.warnings.append(
            f"Preserved {len(numeric)} opaque numeric ResourcePath values from the validated template"
        )
    base_override_refs = sorted({path for path in all_resources if path.startswith("base\\")})
    ep1_refs = sorted({path for path in all_resources if path.startswith("ep1\\")})
    requires_ep1 = manifest.get("requirements", {}).get("phantom_liberty") is True
    if ep1_refs and not requires_ep1:
        report.errors.append("Generated resources reference ep1\\ but Phantom Liberty is not declared")
    if requires_ep1 and not ep1_refs:
        report.warnings.append("Phantom Liberty is declared but no ep1\\ resource is referenced")

    report.details.update(
        {
            "entity_appearances": len(entity_apps),
            "app_appearances": len(app_apps),
            "app_components": len(app_apps[0].get("components", [])) if app_apps else 0,
            "resource_paths": len(set(all_resources)),
            "base_game_references": len(base_override_refs),
            "phantom_liberty_references": len(ep1_refs),
            "opaque_numeric_resources": len(numeric),
            "resolved_template_hashes": len(resolved_mapped_numeric),
            "frame": manifest["frame"],
            "base_entity_type": actual_base_entity_type,
        }
    )
    return report


def generate_documents(manifest: dict[str, Any], catalog: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str, list[str]]:
    templates = manifest["templates"]
    entity = read_json(repo_path(templates["entity"]))
    app, prototype_id, _ = assemble_appearance_document(manifest, catalog)
    localization = read_json(repo_path(templates["localization"]))

    identity = manifest.get("template_identity", {})
    replacements = [
        (str(identity.get("namespace", manifest["namespace"])), manifest["namespace"]),
        (str(identity.get("id", manifest["id"])), manifest["id"]),
    ]
    entity = replace_strings(entity, replacements)
    app = replace_strings(app, replacements)
    template_assets = template_asset_records(manifest)
    resolved_template_resources = resolve_template_asset_paths(entity, template_assets)
    resolved_template_resources += resolve_template_asset_paths(app, template_assets)
    if template_assets:
        unresolved_template_resources = sorted(
            {
                path
                for path in resource_paths(entity) + resource_paths(app)
                if path.isdigit()
            }
        )
        if unresolved_template_resources:
            raise CharacterBuildError(
                "Template asset rebasing left opaque numeric ResourcePath values: "
                + ", ".join(unresolved_template_resources)
            )

    entity_rows = appearance_data(entity)
    if not entity_rows:
        raise CharacterBuildError("Entity template has no appearance mapping")
    entity["Data"]["RootChunk"]["appearances"] = entity["Data"]["RootChunk"]["appearances"][:1]
    entity_row = appearance_data(entity)[0]
    spec = manifest["entity"]
    set_typed_value(entity_row, "name", spec["root_appearance"])
    set_typed_value(entity_row, "appearanceName", spec["appearance_name"])
    resource = entity_row.get("appearanceResource", {}).get("DepotPath")
    if not isinstance(resource, dict) or "$value" not in resource:
        raise CharacterBuildError("Entity appearanceResource is malformed")
    resource["$value"] = f"{manifest['namespace']}\\{spec['appearance_file']}"
    set_typed_value(entity["Data"]["RootChunk"], "defaultAppearance", spec["root_appearance"])

    selected_app = appearance_data(app)[0]
    set_typed_value(selected_app, "name", manifest["appearance"]["name"])
    warnings = apply_catalog_selections(app, manifest, catalog)
    warnings.extend(apply_indexed_overrides(app, manifest, catalog))
    warnings.append(f"Assembled appearance from component prototype {prototype_id}")
    if resolved_template_resources:
        warnings.append(
            f"Resolved {resolved_template_resources} template mesh ResourcePaths into {manifest['namespace']}"
        )
    renumber_handles(app)
    update_localization(localization, manifest)

    set_archive_header(entity, manifest["outputs"]["entity_raw"])
    set_archive_header(app, manifest["outputs"]["appearance_raw"])
    set_archive_header(localization, manifest["outputs"]["localization_raw"])
    return entity, app, localization, render_tweak(manifest), warnings


def output_path(output_root: Path, relative: str) -> Path:
    normalized = Path(relative.replace("\\", "/"))
    target = (output_root / normalized).resolve()
    root = output_root.resolve()
    if root != target and root not in target.parents:
        raise CharacterBuildError(f"Output escapes output root: {relative}")
    return target


def generate(manifest_path: Path, output_root: Path) -> dict[str, Any]:
    manifest = load_manifest(manifest_path)
    catalog = load_catalog(manifest)
    input_report = validate_manifest(manifest, catalog)
    input_report.require_ok()
    entity, app, localization, tweak, warnings = generate_documents(manifest, catalog)
    output_report = validate_generated(manifest, entity, app)
    output_report.warnings.extend(input_report.warnings)
    output_report.warnings.extend(warnings)
    output_report.require_ok()

    outputs = manifest["outputs"]
    write_json(output_path(output_root, outputs["entity_raw"]), entity)
    write_json(output_path(output_root, outputs["appearance_raw"]), app)
    write_json(output_path(output_root, outputs["localization_raw"]), localization)
    tweak_path = output_path(output_root, outputs["tweak"])
    tweak_path.parent.mkdir(parents=True, exist_ok=True)
    tweak_path.write_text(tweak, encoding="utf-8")

    staged_assets = stage_template_assets(manifest, entity, app, output_root)
    generated_files = [
        outputs["entity_raw"],
        outputs["appearance_raw"],
        outputs["localization_raw"],
        outputs["tweak"],
        *staged_assets,
    ]
    hashes = {
        relative: hashlib.sha256(output_path(output_root, relative).read_bytes()).hexdigest().upper()
        for relative in generated_files
    }
    build_report = {
        "schema_version": 1,
        "character": manifest["id"],
        "frame": manifest["frame"],
        "manifest": str(manifest_path.resolve()),
        "output_root": str(output_root.resolve()),
        "files": generated_files,
        "staged_template_assets": staged_assets,
        "sha256": hashes,
        "validation": output_report.as_dict(),
    }
    write_json(output_root / "character-build-report.json", build_report)
    return build_report


def semantic_value(path: Path) -> Any:
    if path.suffix.lower() in {".json"}:
        value = read_json(path)
        value.get("Header", {}).pop("ExportedDateTime", None)
        return value
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def compare_generated(manifest_path: Path, generated_root: Path) -> dict[str, Any]:
    manifest = load_manifest(manifest_path)
    pairs = {output_name: output_name for output_name in manifest["outputs"].values()}
    results: dict[str, bool] = {}
    for generated_name, baseline_name in pairs.items():
        generated = output_path(generated_root, generated_name)
        baseline = repo_path(baseline_name)
        results[generated_name] = generated.is_file() and baseline.is_file() and semantic_value(generated) == semantic_value(baseline)
    return {"equivalent": all(results.values()), "files": results}


def parse_shape_overrides(values: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for value in values:
        name, separator, raw = value.partition("=")
        if not separator or name not in SHAPE_NAMES:
            raise CharacterBuildError(f"Shape override must be one of {', '.join(SHAPE_NAMES)} as name=value")
        try:
            number = int(raw)
        except ValueError as exc:
            raise CharacterBuildError(f"Shape {name} must be an integer") from exc
        if not HEAD_SHAPE_MIN <= number <= HEAD_SHAPE_MAX:
            raise CharacterBuildError(f"Shape {name} must be from {HEAD_SHAPE_MIN} through {HEAD_SHAPE_MAX}")
        result[name] = number
    return result


def mesh_name_for_morphtarget(name: str) -> str:
    stem = name.removesuffix(".morphtarget")
    stem = stem.replace("__morphs_default", "__morphs").replace("__morphs", "_c__basehead")
    return f"{stem}.mesh"


def glb_target_names(path: Path) -> list[str]:
    """Read glTF morph target names without loading the binary geometry payload."""
    try:
        with path.open("rb") as stream:
            header = stream.read(12)
            if len(header) != 12:
                raise CharacterBuildError(f"Preview GLB has a truncated header: {path}")
            magic, version, _length = struct.unpack("<4sII", header)
            if magic != b"glTF" or version != 2:
                raise CharacterBuildError(f"Preview file is not a glTF 2 GLB: {path}")
            chunk_header = stream.read(8)
            if len(chunk_header) != 8:
                raise CharacterBuildError(f"Preview GLB has no JSON chunk: {path}")
            chunk_length, chunk_type = struct.unpack("<II", chunk_header)
            if chunk_type != 0x4E4F534A:
                raise CharacterBuildError(f"Preview GLB does not start with a JSON chunk: {path}")
            document = json.loads(stream.read(chunk_length).decode("utf-8").rstrip("\x00 \t\r\n"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, struct.error) as exc:
        raise CharacterBuildError(f"Unable to inspect preview GLB {path}: {exc}") from exc
    names: list[str] = []
    for mesh in document.get("meshes", []):
        for name in mesh.get("extras", {}).get("targetNames", []):
            if isinstance(name, str) and name not in names:
                names.append(name)
    return names


def build_preview_manifest(
    manifest: dict[str, Any], exported: list[Path], output_dir: Path
) -> dict[str, Any]:
    colors = ("#d6a08a", "#d7e8ef", "#f1e7d5", "#5f3c31", "#9b718c")
    models = []
    all_target_names: list[str] = []
    for index, path in enumerate(sorted(exported, key=lambda item: item.name.casefold())):
        target_names = glb_target_names(path)
        for target_name in target_names:
            if target_name not in all_target_names:
                all_target_names.append(target_name)
        models.append(
            {
                "id": path.name.removesuffix(".morphtarget.glb"),
                "file": path.relative_to(output_dir).as_posix(),
                "source_type": "morphtarget",
                "color": colors[index % len(colors)],
                "morph_target_count": len(target_names),
            }
        )
    shapes = manifest.get("head", {}).get("shapes", {})
    target_pattern = re.compile(r"^h(?P<variant>\d{2})(?P<part>[1-5])_")
    targets_by_part: dict[str, dict[str, str]] = {name: {} for name in SHAPE_NAMES}
    digit_to_shape = {digit: name for name, digit in SHAPE_PART_DIGITS.items()}
    for target_name in all_target_names:
        match = target_pattern.match(target_name)
        if match is None:
            continue
        shape = digit_to_shape[match.group("part")]
        creator_value = int(match.group("variant")) + 1
        targets_by_part[shape].setdefault(str(creator_value), target_name)
    profile = frame_profile(manifest)
    return {
        "schema_version": 1,
        "character_id": str(manifest.get("id", "")),
        "frame": str(manifest.get("frame", "")),
        "models": models,
        "morph_mapping": {
            name: {
                "creator_value": shapes.get(name),
                "part_digit": SHAPE_PART_DIGITS[name],
                "available_creator_values": sorted(
                    {HEAD_SHAPE_MIN, *(int(value) for value in targets_by_part[name])}
                ),
                "targets": targets_by_part[name],
                "unresolved_documented_values": [
                    value
                    for value in profile["unresolved_documented_values"]
                    if str(value) not in targets_by_part[name]
                ],
            }
            for name in SHAPE_NAMES
        },
        "camera": {"view": "head", "up": [0, 1, 0]},
    }


def prepare_head_preview(
    manifest_path: Path,
    output_dir: Path,
    wolvenkit: Path = DEFAULT_WOLVENKIT,
    game_path: Path = DEFAULT_GAME,
    include_all: bool = False,
) -> dict[str, Any]:
    """Export morph-preserving GLBs for the browser without applying shape keys."""
    manifest = load_manifest(manifest_path)
    character_id = str(manifest.get("id", ""))
    report = validate_manifest(manifest)
    report.require_ok()
    if not wolvenkit.is_file():
        raise CharacterBuildError(f"WolvenKit was not found: {wolvenkit}")
    if not game_path.is_dir():
        raise CharacterBuildError(f"Cyberpunk game directory was not found: {game_path}")

    head = manifest.get("head", {})
    source_root = repo_path(str(head.get("morphtarget_source", "")))
    if not source_root.is_dir():
        raise CharacterBuildError(f"Morphtarget source was not found: {source_root}")
    configured = [str(value) for value in head.get("morphtargets", [])]
    configured_preview = head.get("preview_morphtargets")
    if configured_preview is None:
        preview_names = tuple(frame_profile(manifest)["preview_morphtargets"])
    elif isinstance(configured_preview, list) and all(
        isinstance(value, str) and value for value in configured_preview
    ):
        preview_names = tuple(configured_preview)
    else:
        raise CharacterBuildError("head.preview_morphtargets must be a list of filenames")
    names = configured if include_all else [name for name in configured if name in preview_names]
    if not names:
        names = [name for name in preview_names if (source_root / name).is_file()]
    sources = [source_root / name for name in names]
    missing = [str(path) for path in sources if not path.is_file()]
    if missing:
        raise CharacterBuildError(f"Preview morphtargets were not found: {', '.join(missing)}")
    if not sources:
        raise CharacterBuildError("No head morphtargets were selected for preview")

    models_dir = output_dir / "models"
    models_dir.mkdir(parents=True, exist_ok=True)
    expected = [models_dir / f"{source.name}.glb" for source in sources]
    cache_path = output_dir / "preview-cache.json"
    try:
        cache = read_json(cache_path) if cache_path.is_file() else {"schema_version": 1, "models": {}}
    except CharacterBuildError:
        cache = {"schema_version": 1, "models": {}}
    cached_models = cache.get("models")
    if not isinstance(cached_models, dict):
        cached_models = {}
    cache_keys = {
        source.name: head_preview_cache_key(source, wolvenkit, game_path) for source in sources
    }
    reused = [
        output
        for source, output in zip(sources, expected)
        if output.is_file() and cached_models.get(source.name) == cache_keys[source.name]
    ]
    export_sources = [
        source
        for source, output in zip(sources, expected)
        if not output.is_file() or cached_models.get(source.name) != cache_keys[source.name]
    ]
    commands: list[list[str]] = []
    if export_sources:
        command = [
            str(wolvenkit),
            "export",
            *[str(source) for source in export_sources],
            "-o",
            str(models_dir),
            "--gamepath",
            str(game_path),
            "-v",
            "Minimal",
        ]
        commands.append(command)
        completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
        if completed.returncode != 0 and not all(path.is_file() for path in expected):
            raise CharacterBuildError(
                f"Preview export failed ({completed.returncode}): {' '.join(command)}\n"
                f"{completed.stdout}\n{completed.stderr}"
            )

    missing_outputs = [str(path) for path in expected if not path.is_file()]
    if missing_outputs:
        raise CharacterBuildError(f"Preview export did not produce: {', '.join(missing_outputs)}")
    cached_models.update(cache_keys)
    write_json(cache_path, {"schema_version": 1, "models": cached_models})
    preview = build_preview_manifest(manifest, expected, output_dir)
    preview["cache_keys"] = cache_keys
    manifest_output = output_dir / "preview-manifest.json"
    write_json(manifest_output, preview)
    return {
        "ok": True,
        "character_id": character_id,
        "manifest": str(manifest_output.resolve()),
        "models": [str(path.resolve()) for path in expected],
        "reused": [str(path.resolve()) for path in reused],
        "commands": commands,
    }


def head_build(
    manifest_path: Path,
    workspace: Path,
    shape_overrides: dict[str, int],
    wolvenkit: Path,
    blender: Path,
    game_path: Path,
    dry_run: bool,
) -> dict[str, Any]:
    manifest = load_manifest(manifest_path)
    profile_error = ""
    try:
        profile = frame_profile(manifest)
        head_shape_max = int(profile["head_shape_max"])
    except CharacterBuildError as exc:
        profile = {}
        head_shape_max = HEAD_SHAPE_MAX
        profile_error = str(exc)
    shapes = dict(manifest.get("head", {}).get("shapes", {}))
    shapes.update(shape_overrides)
    missing = [name for name in SHAPE_NAMES if shapes.get(name) is None]
    validation_manifest = copy.deepcopy(manifest)
    validation_manifest.setdefault("head", {})["shapes"] = shapes
    validation = validate_manifest(validation_manifest)
    errors: list[str] = list(validation.errors)
    validation_warnings = list(validation.warnings)
    if not profile:
        errors.append(profile_error)
    for path, label in ((wolvenkit, "WolvenKit"), (blender, "Blender"), (BLENDER_RUNNER, "Blender runner")):
        if not path.is_file():
            errors.append(f"{label} was not found: {path}")
    if not game_path.is_dir():
        errors.append(f"Cyberpunk game directory was not found: {game_path}")
    blend_template = repo_path(manifest.get("head", {}).get("blend_template", ""))
    morph_source = repo_path(manifest.get("head", {}).get("morphtarget_source", ""))
    mesh_source = repo_path(manifest.get("head", {}).get("mesh_source", ""))
    if not blend_template.is_file():
        errors.append(f"Head blend template was not found: {blend_template}")
    if not morph_source.is_dir():
        errors.append(f"Morphtarget source was not found: {morph_source}")
    if not mesh_source.is_dir():
        errors.append(f"Head mesh source was not found: {mesh_source}")
    morph_names = manifest.get("head", {}).get("morphtargets", [])
    if not isinstance(morph_names, list) or not morph_names:
        errors.append("Manifest head.morphtargets must select at least one file")
        morph_names = []
    selected_morphs = [morph_source / str(name) for name in morph_names]
    missing_morphs = [str(path) for path in selected_morphs if not path.is_file()]
    if missing_morphs:
        errors.append(f"Selected morphtargets were not found: {', '.join(missing_morphs)}")
    selected_meshes = [mesh_source / mesh_name_for_morphtarget(str(name)) for name in morph_names]
    missing_meshes = [str(path) for path in selected_meshes if not path.is_file()]
    if missing_meshes:
        errors.append(f"Matching head meshes were not found: {', '.join(missing_meshes)}")
    if missing:
        errors.append(f"Head shapes are unset: {', '.join(missing)}")
    for name in SHAPE_NAMES:
        value = shapes.get(name)
        if value is not None and (
            not isinstance(value, int) or not HEAD_SHAPE_MIN <= value <= head_shape_max
        ):
            errors.append(f"Shape {name} must be from {HEAD_SHAPE_MIN} through {head_shape_max}")
    errors = list(dict.fromkeys(errors))
    plan = {
        "ok": not errors,
        "dry_run": dry_run,
        "workspace": str(workspace.resolve()),
        "frame": str(manifest.get("frame", "")),
        "wolvenkit": str(wolvenkit),
        "blender": str(blender),
        "game_path": str(game_path),
        "blend_template": str(blend_template),
        "morphtarget_source": str(morph_source),
        "mesh_source": str(mesh_source),
        "morphtargets": [path.name for path in selected_morphs],
        "shapes": shapes,
        "errors": errors,
        "warnings": validation_warnings,
        "commands": [],
    }
    if errors or dry_run:
        return plan

    head_dir = workspace / "head"
    morph_dir = head_dir / "morphtargets"
    morph_dir.mkdir(parents=True, exist_ok=True)
    blend_file = head_dir / "head_import.blend"
    shutil.copy2(blend_template, blend_file)
    shape_file = head_dir / "head-shapes.json"
    write_json(shape_file, {name: shapes[name] for name in SHAPE_NAMES})

    export_command = [
        str(wolvenkit),
        "export",
        *[str(path) for path in selected_morphs],
        "-o",
        str(morph_dir),
        "--gamepath",
        str(game_path),
        "-v",
        "Minimal",
    ]
    blender_command = [
        str(blender),
        "--background",
        str(blend_file),
        "--python",
        str(BLENDER_RUNNER),
        "--",
        "--shapes",
        str(shape_file),
    ]
    plan["commands"] = [export_command, blender_command]
    exported_morphs = list(morph_dir.glob("*.morphtarget.glb"))
    if not exported_morphs:
        completed = subprocess.run(export_command, cwd=ROOT, text=True, capture_output=True, check=False)
        exported_morphs = list(morph_dir.glob("*.morphtarget.glb"))
        if completed.returncode != 0 and not exported_morphs:
            plan["errors"].append(
                f"Command failed ({completed.returncode}): {' '.join(export_command)}\n{completed.stdout}\n{completed.stderr}"
            )
            plan["ok"] = False
            return plan
        if completed.returncode != 0:
            plan["warnings"].append(
                f"WolvenKit returned {completed.returncode}, but exported {len(exported_morphs)} morphtarget GLBs; "
                "the source folder contains a non-CR2W readme"
            )
    else:
        plan["warnings"].append(f"Reused {len(exported_morphs)} existing morphtarget GLBs")

    completed = subprocess.run(blender_command, cwd=ROOT, text=True, capture_output=True, check=False)
    if completed.returncode != 0:
        plan["errors"].append(
            f"Command failed ({completed.returncode}): {' '.join(blender_command)}\n{completed.stdout}\n{completed.stderr}"
        )
        plan["ok"] = False
        return plan
    outputs = sorted(str(path) for path in head_dir.glob("*.glb"))
    expected_glbs = [head_dir / f"{path.stem}.glb" for path in selected_meshes]
    missing_glbs = [str(path) for path in expected_glbs if not path.is_file()]
    plan["glb_outputs"] = [str(path) for path in expected_glbs if path.is_file()]
    if missing_glbs:
        plan["errors"].append("Blender completed without producing any head GLBs")
        plan["errors"].extend(f"Missing GLB: {path}" for path in missing_glbs)
        plan["ok"] = False
        return plan

    depot_head = manifest["namespace"].replace("\\", "/") + "/head"
    archive_dir = output_path(workspace, f"source/archive/{depot_head}")
    archive_dir.mkdir(parents=True, exist_ok=True)
    for source_mesh in selected_meshes:
        shutil.copy2(source_mesh, archive_dir / source_mesh.name)
    import_command = [
        str(wolvenkit),
        "import",
        *[str(path) for path in expected_glbs],
        "-o",
        str(archive_dir),
        "--keep",
        "-v",
        "Minimal",
    ]
    plan["commands"].append(import_command)
    completed = subprocess.run(import_command, cwd=ROOT, text=True, capture_output=True, check=False)
    if completed.returncode != 0:
        plan["errors"].append(
            f"Command failed ({completed.returncode}): {' '.join(import_command)}\n{completed.stdout}\n{completed.stderr}"
        )
        plan["ok"] = False
        return plan
    if "Warning" in completed.stdout:
        plan["warnings"].append(
            "WolvenKit reported garment-support warnings while rebuilding head meshes; review the CLI log before runtime use"
        )
    rebuilt = [archive_dir / path.name for path in selected_meshes]
    bad_headers = [str(path) for path in rebuilt if not path.is_file() or path.read_bytes()[:4] != b"CR2W"]
    if bad_headers:
        plan["errors"].extend(f"Invalid rebuilt CR2W: {path}" for path in bad_headers)
        plan["ok"] = False
        return plan
    plan["cr2w_outputs"] = [str(path) for path in rebuilt]
    plan["cr2w_sha256"] = {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest().upper() for path in rebuilt
    }
    plan["ok"] = True
    write_json(workspace / "head-build-report.json", plan)
    return plan


def print_report(value: Any) -> None:
    print(json.dumps(value, indent=2, ensure_ascii=False))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("validate", help="Validate the manifest and catalog")
    generate_parser = subparsers.add_parser("generate", help="Generate isolated character source files")
    generate_parser.add_argument("--out", type=Path, required=True)
    shell_parser = subparsers.add_parser(
        "make-shell",
        help="Create a neutral appearance shell from a CR2W-JSON donor",
    )
    shell_parser.add_argument("--donor", type=Path, required=True)
    shell_parser.add_argument("--out", type=Path, required=True)
    entity_shell_parser = subparsers.add_parser(
        "make-entity-shell",
        help="Create a neutral frame-specific entity shell from CR2W-JSON",
    )
    entity_shell_parser.add_argument("--donor", type=Path, required=True)
    entity_shell_parser.add_argument("--frame", choices=tuple(FRAME_PROFILES), required=True)
    entity_shell_parser.add_argument("--out", type=Path, required=True)
    compare_parser = subparsers.add_parser("compare", help="Compare generated output with the handwritten baseline")
    compare_parser.add_argument("--generated", type=Path, required=True)
    head_parser = subparsers.add_parser("head", help="Run or inspect the headless head build")
    head_parser.add_argument("--workspace", type=Path, required=True)
    head_parser.add_argument("--shape", action="append", default=[])
    head_parser.add_argument("--wolvenkit", type=Path, default=DEFAULT_WOLVENKIT)
    head_parser.add_argument("--blender", type=Path, default=DEFAULT_BLENDER)
    head_parser.add_argument("--gamepath", type=Path, default=DEFAULT_GAME)
    head_parser.add_argument("--dry-run", action="store_true")
    preview_parser = subparsers.add_parser("preview", help="Export morph-preserving GLBs for the local UI")
    preview_parser.add_argument("--out", type=Path, required=True)
    preview_parser.add_argument("--wolvenkit", type=Path, default=DEFAULT_WOLVENKIT)
    preview_parser.add_argument("--gamepath", type=Path, default=DEFAULT_GAME)
    preview_parser.add_argument("--all-head-parts", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "validate":
            manifest = load_manifest(args.manifest)
            report = validate_manifest(manifest)
            print_report(report.as_dict())
            return 0 if report.ok else 1
        if args.command == "generate":
            print_report(generate(args.manifest, args.out))
            return 0
        if args.command == "make-shell":
            write_json(args.out, appearance_shell_document(read_json(args.donor)))
            print_report({"ok": True, "donor": str(args.donor), "output": str(args.out)})
            return 0
        if args.command == "make-entity-shell":
            write_json(
                args.out,
                entity_shell_document(read_json(args.donor), args.frame),
            )
            print_report(
                {
                    "ok": True,
                    "donor": str(args.donor),
                    "frame": args.frame,
                    "output": str(args.out),
                }
            )
            return 0
        if args.command == "compare":
            report = compare_generated(args.manifest, args.generated)
            print_report(report)
            return 0 if report["equivalent"] else 1
        if args.command == "head":
            report = head_build(
                args.manifest,
                args.workspace,
                parse_shape_overrides(args.shape),
                args.wolvenkit,
                args.blender,
                args.gamepath,
                args.dry_run,
            )
            print_report(report)
            return 0 if report["ok"] else 1
        if args.command == "preview":
            print_report(
                prepare_head_preview(
                    args.manifest,
                    args.out,
                    args.wolvenkit,
                    args.gamepath,
                    args.all_head_parts,
                )
            )
            return 0
    except CharacterBuildError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
