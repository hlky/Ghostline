"""Explicit install profiles and dependency-aware depot selection.

Packed CR2W string tables are read as binary structures; source resources are
never rewritten. Game-owned base/ep1 paths remain external unless explicitly
included. This records named dependencies, not runtime reachability or save state.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import struct
from typing import Any, Mapping

import yaml
from project_layout import project_root, project_config, project_sources

ROOT = Path(__file__).resolve().parents[1]
DEPOT = re.compile(r"^(?:mod|tutorial|base|ep1)[\\/][^\x00\r\n:*?\"<>|]+\.[a-zA-Z0-9_]+$")


class PackageError(RuntimeError):
    pass


def depot_path(value: str) -> str:
    normalized = value.replace("\\", "/").casefold()
    path = PurePosixPath(normalized)
    parts = normalized.split("/")
    reserved = {"con", "prn", "aux", "nul", *(f"com{i}" for i in range(1, 10)), *(f"lpt{i}" for i in range(1, 10))}
    if (path.is_absolute() or re.search(r'[\x00-\x1f<>:"|?*]', normalized)
        or any(part in ("", ".", "..") or part.endswith((" ", ".")) or part.split(".")[0] in reserved for part in parts)):
        raise PackageError(f"Unsafe depot path: {value}")
    return str(path)


def path_component(value: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", value):
        raise PackageError(f"Invalid package name: {value!r}")
    depot_path(value)
    return value


def sha256(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def resource_strings(value: Any) -> set[str]:
    result: set[str] = set()
    if isinstance(value, str) and DEPOT.fullmatch(value):
        result.add(depot_path(value))
    elif isinstance(value, Mapping):
        for key, child in value.items():
            result.update(resource_strings(key))
            result.update(resource_strings(child))
    elif isinstance(value, (list, tuple)):
        for child in value:
            result.update(resource_strings(child))
    return result


def cr2w_dependencies(path: Path) -> set[str]:
    """Read the bounded string table described by the CR2W header (table zero)."""
    with path.open("rb") as stream:
        header = stream.read(160)
        if header[:4] != b"CR2W":
            return set()  # WEM and other opaque payloads have no CR2W imports.
        if len(header) < 160:
            raise PackageError(f"Truncated CR2W header: {path}")
        offset, size = struct.unpack_from("<II", header, 40)
        if offset < 160 or offset + size > path.stat().st_size:
            raise PackageError(f"Invalid CR2W string table: {path}")
        stream.seek(offset)
        content = stream.read(size)
    try:
        return resource_strings(content.decode("utf-8").split("\0"))
    except UnicodeDecodeError as exc:
        raise PackageError(f"Invalid CR2W strings: {path}") from exc


def depot_hash(path: str) -> int:
    """RED resource hashes use case-insensitive backslash depot paths."""
    value = 0xCBF29CE484222325
    for byte in depot_path(path).replace("/", "\\").encode("utf-8"):
        value = ((value ^ byte) * 0x100000001B3) & 0xFFFFFFFFFFFFFFFF
    return value


def inventory_hashes(inventory: Mapping[str, Path]) -> dict[int, str]:
    result: dict[int, str] = {}
    for path in inventory:
        key = depot_hash(path)
        if key in result and result[key] != path:
            raise PackageError(f"Depot hash collision: {result[key]} and {path}")
        result[key] = path
    return result


def authored_dependencies(
    path: Path, known_hashes: Mapping[int, str] | None = None, *, unresolved: set[int] | None = None,
) -> set[str]:
    """Include declared paths hidden by hashed/embedded binary serialization.

    This is a conservative union with packed dependencies: a newer raw source
    can add dependencies, but cannot remove references discovered in the binary.
    """
    if not path.is_file():
        return set()
    document = json.loads(path.read_text(encoding="utf-8-sig"))
    dependencies = resource_strings(document)
    known_hashes = known_hashes or {}

    def visit(value: Any) -> None:
        if isinstance(value, dict):
            if value.get("$type") == "ResourcePath" and value.get("$storage") == "uint64":
                try:
                    resource_hash = int(value["$value"])
                except (KeyError, TypeError, ValueError) as exc:
                    raise PackageError(f"Invalid numeric resource path in {path}") from exc
                if resource_hash in known_hashes:
                    dependencies.add(known_hashes[resource_hash])
                elif resource_hash and unresolved is not None:
                    unresolved.add(resource_hash)
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    visit(document)
    return dependencies


def archive_inventory(root: Path) -> dict[str, Path]:
    result: dict[str, Path] = {}
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        key = depot_path(path.relative_to(root).as_posix())
        if key in result:
            raise PackageError(f"Case-insensitive depot collision: {key}")
        if key.split("/")[0] not in {"mod", "tutorial", "base", "ep1"}:
            raise PackageError(f"Support file in packed depot tree: {key}")
        result[key] = path
    return result


def filter_registration(document: dict, profile: dict, quests: set[str]) -> dict:
    def keep(path: str) -> bool:
        parts = depot_path(path).split("/")
        return len(parts) > 1 and (parts[1] in quests or parts[:3] == ["mod", "ghostline", "localization"])

    result: dict[str, Any] = {}
    phases = [entry for entry in document.get("quest", {}).get("phases", [])
              if depot_path(entry["path"]).split("/")[1] in profile["active_quests"]]
    if Counter(depot_path(entry["path"]).split("/")[1] for entry in phases) != Counter(profile["active_quests"]):
        raise PackageError("Each active quest must have one ArchiveXL phase registration")
    result["quest"] = {"phases": phases}
    result["journal"] = [path for path in document.get("journal", []) if keep(path)]
    result["localization"] = {
        category: {locale: [path for path in paths if keep(path)] for locale, paths in locales.items()}
        for category, locales in document.get("localization", {}).items()
    }
    result["streaming"] = {"blocks": [path for path in document.get("streaming", {}).get("blocks", []) if keep(path)]}
    patches = {source: targets for source, targets in document.get("resource", {}).get("patch", {}).items() if keep(source)}
    if patches:
        result["resource"] = {"patch": patches}
    return result


@dataclass(frozen=True)
class PackageManifest:
    profile: str
    archive_name: str
    payloads: Mapping[str, Path]
    loose_files: Mapping[str, Path]
    registration: dict
    audit: dict


def package_inputs(root: Path) -> tuple[dict[str, Path], dict[str, Path], dict[str, Path], dict]:
    """Merge only this project and its explicit dependencies; never scan siblings."""
    sources = project_sources(root) if (root / "project.json").is_file() else [root]
    inventory: dict[str, Path] = {}
    raw: dict[str, Path] = {}
    loose: dict[str, Path] = {}
    registration: dict = {}

    def merge(target: dict, incoming: dict) -> None:
        for key, value in incoming.items():
            if isinstance(value, dict):
                merge(target.setdefault(key, {}), value)
            elif isinstance(value, list):
                values = target.setdefault(key, [])
                values.extend(item for item in value if item not in values)
            elif key in target and target[key] != value:
                raise PackageError(f"Conflicting ArchiveXL declaration: {key}")
            else:
                target[key] = value

    for source in sources:
        for depot, path in archive_inventory(source / "source/archive").items():
            if depot in inventory:
                raise PackageError(f"Multiple owners for depot {depot}: {inventory[depot]} and {path}")
            inventory[depot] = path
            raw[depot] = source / "source/raw" / (depot + ".json")
        resources = source / "source/resources"
        for path in sorted(resources.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(resources).as_posix()
            if relative in loose:
                raise PackageError(f"Multiple owners for loose resource {relative}")
            loose[relative] = path
            if path.name.endswith(".archive.xl"):
                merge(registration, yaml.safe_load(path.read_text(encoding="utf-8")) or {})
    return inventory, raw, loose, registration


def build_manifest(profile_name: str | None = None, *, root: Path = ROOT, project: str | Path | None = None, deduplicate: bool | None = None) -> PackageManifest:
    if project is not None:
        root = project_root(project, root=root)
    elif (root / "packaging/profiles.json").is_file():
        routing = json.loads((root / "packaging/profiles.json").read_text(encoding="utf-8"))
        if routing.get("schema_version") == 2:
            if profile_name not in routing["profiles"]:
                raise PackageError(f"Unknown package profile: {profile_name}")
            root = project_root(routing["profiles"][profile_name]["project"], root=root)
    if profile_name is None:
        profile_name = project_config(root)["default_profile"]
    config = json.loads((root / "packaging/profiles.json").read_text(encoding="utf-8"))
    if config.get("schema_version") != 1 or profile_name not in config["profiles"]:
        raise PackageError(f"Unknown package profile: {profile_name}")
    profile = config["profiles"][profile_name]
    path_component(profile_name)
    path_component(profile["archive_name"])
    inventory, raw_inventory, loose_inventory, document = package_inputs(root)
    known_hashes = inventory_hashes(inventory)
    quests = set(profile.get("active_quests", [])) | set(profile.get("support_quests", []))
    prefixes = [f"mod/{quest}/" for quest in quests]
    prefixes += ["mod/ghostline/localization/"]
    prefixes += [f"base/localization/en-us/lipsync/mod/{quest}/" for quest in quests]
    excluded_prefixes = profile.get("exclude_prefixes", [])
    selected = {path for path in inventory if (profile.get("include_all") or any(path.startswith(prefix) for prefix in prefixes))
                and not any(path.startswith(prefix) for prefix in excluded_prefixes)}
    for name in profile.get("characters", []):
        entity = f"mod/ghostline/characters/{name}/{name}.ent"
        if entity not in inventory:
            raise PackageError(f"Missing character entry point: {entity}")
        selected.add(entity)
    registration = filter_registration(document, profile, quests)
    if profile.get("include_all"):
        loose = {relative: path for relative, path in loose_inventory.items()
                 if not path.name.endswith(".xl") and relative not in profile.get("exclude_loose", [])}
    else:
        loose = {f"r6/tweaks/{profile['archive_name']}/{name}.yaml": loose_inventory.get(
                    f"r6/tweaks/ghostline/{name}.yaml", root / "source/resources/r6/tweaks/ghostline" / f"{name}.yaml")
                 for name in profile["tweaks"]}
    references = resource_strings(registration)
    for path in loose.values():
        if not path.is_file():
            raise PackageError(f"Missing loose resource: {path}")
        if path.suffix in {".yaml", ".yml"}:
            references.update(resource_strings(yaml.safe_load(path.read_text(encoding="utf-8"))))
    external: set[str] = set()
    added: set[str] = set()
    inspected: set[str] = set()
    raw_sources: set[str] = set()
    unresolved_numeric: dict[str, list[str]] = {}
    character_bundles: dict[str, dict[str, Any]] = {}
    pending = set(selected)
    # Scenes retain an unlocalized soft reference; the registered language map
    # owns the concrete animset. Accept it only with matching packed map evidence.
    lipmaps = resource_strings(registration.get("localization", {}).get("lipmaps", {}))
    localized_targets = set().union(*(cr2w_dependencies(inventory[path]) for path in lipmaps if path in inventory))
    localized_references: dict[str, str] = {}

    def require(paths: set[str]) -> None:
        for path in sorted(paths):
            if any(path.startswith(prefix) for prefix in profile.get("forbidden_prefixes", [])):
                raise PackageError(f"Forbidden profile dependency: {path}")
            if any(path.startswith(prefix) for prefix in excluded_prefixes):
                raise PackageError(f"Dependency belongs to an excluded profile section: {path}")
            if path not in inventory and "/scenes/lipsync/en/" in path:
                owner, suffix = path.split("/scenes/lipsync/en/", 1)
                localized = f"base/localization/en-us/lipsync/{owner}/scenes/{suffix}"
                if localized in localized_targets and localized in inventory:
                    localized_references[path] = localized
                    path = localized
            game_owned = path.startswith(("base/", "ep1/")) and not path.startswith("base/localization/en-us/lipsync/mod/")
            if game_owned and path not in selected:
                external.add(path)
            elif path not in inventory:
                raise PackageError(f"Missing owned depot dependency: {path}")
            elif path not in selected:
                selected.add(path)
                pending.add(path)
                added.add(path)

    require(references)
    while pending:
        path = pending.pop()
        if path in inspected:
            continue
        inspected.add(path)
        dependencies = cr2w_dependencies(inventory[path])
        raw = raw_inventory[path]
        if raw.is_file():
            raw_sources.add(path)
            unresolved: set[int] = set()
            dependencies.update(authored_dependencies(raw, known_hashes, unresolved=unresolved))
            if unresolved:
                unresolved_numeric[path] = [str(value) for value in sorted(unresolved)]
        elif path.startswith("mod/ghostline/characters/") and path.endswith(".mesh"):
            owner = path.split("/")[3]
            if owner not in character_bundles:
                prefix = f"mod/ghostline/characters/{owner}/"
                bundle = {depot for depot in inventory if depot.startswith(prefix)}
                character_bundles[owner] = {
                    "reason": "Mesh material buffers have no parsed raw companion; retain the owning character bundle.",
                    "meshes_without_raw": sorted(
                        depot for depot in bundle if depot.endswith(".mesh")
                        and not raw_inventory[depot].is_file()
                    ),
                    "retained_file_count": len(bundle),
                }
                require(bundle)
        require(dependencies)
    payloads = {path: inventory[path] for path in sorted(selected)}
    groups: dict[str, list[str]] = defaultdict(list)
    for path, source in payloads.items():
        if path.startswith("mod/ghostline/characters/") and path.endswith(".mesh"):
            groups[sha256(source)].append(path)
    aliases: dict[str, list[str]] = {}
    bytes_removed = 0
    if profile.get("deduplicate_meshes") if deduplicate is None else deduplicate:
        for digest, paths in sorted(groups.items()):
            if len(paths) < 2:
                continue
            source = payloads[paths[0]]
            canonical = f"mod/ghostline/shared/{digest}.mesh"
            existing = payloads.get(canonical)
            if existing is not None and sha256(existing) != digest:
                raise PackageError(f"Shared mesh path collides with different content: {canonical}")
            aliases[canonical] = paths
            bytes_removed += source.stat().st_size * (len(paths) - (0 if existing else 1))
            for path in paths:
                del payloads[path]
            payloads[canonical] = source
        if aliases:
            registration.setdefault("resource", {})["link"] = {
                canonical.replace("/", "\\"): [path.replace("/", "\\") for path in paths]
                for canonical, paths in aliases.items()
            }
    audit = {
        "project_root": str(root.resolve()),
        "source_projects": [str(path) for path in (project_sources(root) if (root / "project.json").is_file() else [root])],
        "profile": profile_name, "active_quests": profile["active_quests"],
        "selected_paths": sorted(payloads), "loose_files": sorted(loose),
        "payload_count": len(payloads), "payload_bytes": sum(p.stat().st_size for p in payloads.values()),
        "dependency_additions": sorted(added), "external_game_dependencies": sorted(external),
        "localized_lipsync_references": localized_references,
        "authored_dependency_sources": sorted(raw_sources),
        "unresolved_numeric_resource_paths": dict(sorted(unresolved_numeric.items())),
        "character_bundle_fallbacks": dict(sorted(character_bundles.items())),
        "excluded_paths": sorted(set(inventory) - selected), "mesh_aliases": aliases,
        "deduplicated_bytes": bytes_removed,
        "dependency_scope": "Packed string-table paths plus conservative authored raw/loose paths and inventory-resolved ResourcePath hashes; unresolved hashes, embedded binary-only references and external game paths still require validation.",
        "minimum_archivexl": "1.14" if aliases else None,
    }
    return PackageManifest(profile_name, profile["archive_name"], payloads, loose, registration, audit)
