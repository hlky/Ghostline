from __future__ import annotations

import argparse
import collections
import concurrent.futures
import contextlib
import hashlib
import http.server
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
import urllib.parse
import webbrowser
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Iterator


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_GAME = Path(r"H:\Cyberpunk 2077")
DEFAULT_WOLVENKIT = Path(r"H:\WolvenKit.Console-8.17.4\WolvenKit.CLI.exe")
DEFAULT_KRAKEN = DEFAULT_WOLVENKIT.parent / "kraken.dll"
DEFAULT_GHOSTLINE_RED = ROOT / "tools/ghostline-red/target/release/ghostline-red.exe"
DEFAULT_RED_SCHEMA = ROOT / "red-schema.json"
DEFAULT_BLENDER = Path(r"C:\Program Files\Blender Foundation\Blender 5.1\blender.exe")
DEFAULT_OUTPUT = ROOT / "converted/item-database"
DEFAULT_INDEX = ROOT / "converted/character-index/assets.json"
DEFAULT_TWEAK_ROOT = (
    DEFAULT_GAME / "tools/redmod/tweaks/base/gameplay/static_data/database/items"
)
GALLERY_ROOT = ROOT / "tools/item_gallery"
BLENDER_SCRIPT = ROOT / "tools/item_render_blender.py"
SCHEMA_VERSION = 1

RECORD_HEADER = re.compile(
    r"(?m)^[ \t]*(?P<name>[A-Za-z_][A-Za-z0-9_]*)"
    r"[ \t]*:[ \t]*(?P<parent>[A-Za-z_][A-Za-z0-9_.]*)[ \t\r\n]*\{"
)
PACKAGE_LINE = re.compile(r"(?m)^[ \t]*package[ \t]+([A-Za-z_][A-Za-z0-9_.]*)")
ATTRIBUTE_BLOCK = re.compile(r"\[\s*(?P<attrs>[^\]]+)\]\s*$", re.MULTILINE)
STRING_PROPERTY = re.compile(
    r"(?m)^[ \t]*(?:[A-Za-z_][A-Za-z0-9_<>\[\], \t]*[ \t]+)?"
    r"(?P<key>displayName|localizedDescription|appearanceName|entityName|"
    r"equipArea|itemType)[ \t]*=[ \t]*\"(?P<value>[^\"]*)\"[ \t]*;"
)
TAGS_PROPERTY = re.compile(
    r"(?ms)^[ \t]*(?:CName\[\][ \t]+)?tags[ \t]*\+?=\s*\[(?P<body>.*?)\][ \t]*;"
)
QUOTED_STRING = re.compile(r"\"([^\"]+)\"")
LOC_KEY = re.compile(r"^LocKey#(.+)$", re.IGNORECASE)
FRAME_SUFFIX = re.compile(r"_(?P<frame>m|w)$", re.IGNORECASE)
FRAME_TOKEN = re.compile(r"(?:^|_)(?P<frame>pma|pwa|ma|wa)(?:_|$)", re.IGNORECASE)

EQUIPMENT_SLOTS = {
    "EquipmentArea.Feet": "feet",
    "EquipmentArea.LegArmor": "legs",
    "EquipmentArea.InnerChest": "inner_torso",
    "EquipmentArea.ChestArmor": "outer_torso",
    "EquipmentArea.HeadArmor": "head",
    "EquipmentArea.FaceArmor": "face",
    "EquipmentArea.Outfit": "outfit",
    "EquipmentArea.UnderwearTop": "underwear_top",
    "EquipmentArea.UnderwearBottom": "underwear_bottom",
}
FRAME_LABELS = {"m": "pma", "w": "pwa"}
PRIMARY_COMPONENT_TYPES = {
    "entGarmentSkinnedMeshComponent",
    "entSkinnedMeshComponent",
    "entMeshComponent",
}


class ItemDatabaseError(RuntimeError):
    pass


@dataclass
class TweakRecord:
    name: str
    parent: str
    package: str
    source: Path
    attributes: set[str] = field(default_factory=set)
    scalars: dict[str, str] = field(default_factory=dict)
    tags: list[str] = field(default_factory=list)

    @property
    def record_id(self) -> str:
        return f"{self.package}.{self.name}"


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ItemDatabaseError(f"Unable to read JSON {path}: {exc}") from exc


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(value, indent=2, ensure_ascii=False) + "\n"
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False, prefix=f".{path.name}."
    ) as handle:
        handle.write(encoded)
        temporary = Path(handle.name)
    os.replace(temporary, path)


def file_identity(path: Path) -> dict[str, Any]:
    stat = path.stat()
    return {
        "path": str(path.resolve()),
        "size": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
    }


def sha1_text(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()


def balanced_block(text: str, opening_brace: int) -> tuple[str, int]:
    depth = 0
    quote = False
    escaped = False
    line_comment = False
    block_comment = False
    index = opening_brace
    while index < len(text):
        char = text[index]
        following = text[index + 1] if index + 1 < len(text) else ""
        if line_comment:
            if char == "\n":
                line_comment = False
            index += 1
            continue
        if block_comment:
            if char == "*" and following == "/":
                block_comment = False
                index += 2
            else:
                index += 1
            continue
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                quote = False
            index += 1
            continue
        if char == "/" and following == "/":
            line_comment = True
            index += 2
            continue
        if char == "/" and following == "*":
            block_comment = True
            index += 2
            continue
        if char == '"':
            quote = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[opening_brace + 1 : index], index + 1
        index += 1
    raise ItemDatabaseError("Unterminated TweakDB record block")


def record_attributes(text: str, header_start: int) -> set[str]:
    prefix = text[max(0, header_start - 256) : header_start]
    match = ATTRIBUTE_BLOCK.search(prefix)
    if not match:
        return set()
    tail = prefix[match.end() :]
    if tail.strip():
        return set()
    return {value for value in re.split(r"[\s,]+", match.group("attrs").strip()) if value}


def parse_tweak_file(path: Path) -> list[TweakRecord]:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    package_match = PACKAGE_LINE.search(text)
    package = package_match.group(1) if package_match else "Items"
    records: list[TweakRecord] = []
    cursor = 0
    while True:
        match = RECORD_HEADER.search(text, cursor)
        if not match:
            break
        opening = match.end() - 1
        body, end = balanced_block(text, opening)
        scalars = {
            property_match.group("key"): property_match.group("value")
            for property_match in STRING_PROPERTY.finditer(body)
        }
        tags: list[str] = []
        for tags_match in TAGS_PROPERTY.finditer(body):
            for value in QUOTED_STRING.findall(tags_match.group("body")):
                if value not in tags:
                    tags.append(value)
        records.append(
            TweakRecord(
                name=match.group("name"),
                parent=match.group("parent"),
                package=package,
                source=path,
                attributes=record_attributes(text, match.start()),
                scalars=scalars,
                tags=tags,
            )
        )
        cursor = end
    return records


def load_tweak_records(root: Path) -> dict[str, TweakRecord]:
    if not root.is_dir():
        raise ItemDatabaseError(f"REDmod item tweak directory was not found: {root}")
    records: dict[str, TweakRecord] = {}
    for path in sorted(root.rglob("*.tweak")):
        for record in parse_tweak_file(path):
            records[record.record_id] = record
    return records


def resolve_record(
    record_id: str,
    records: dict[str, TweakRecord],
    cache: dict[str, dict[str, Any]],
    resolving: set[str] | None = None,
) -> dict[str, Any]:
    if record_id in cache:
        return cache[record_id]
    record = records.get(record_id)
    if record is None:
        return {}
    active = set() if resolving is None else set(resolving)
    if record_id in active:
        raise ItemDatabaseError(f"TweakDB inheritance cycle includes {record_id}")
    active.add(record_id)
    parent_id = record.parent if "." in record.parent else f"{record.package}.{record.parent}"
    inherited = resolve_record(parent_id, records, cache, active)
    resolved = {
        "scalars": dict(inherited.get("scalars", {})),
        "tags": list(inherited.get("tags", [])),
        "lineage": list(inherited.get("lineage", [])),
    }
    resolved["scalars"].update(record.scalars)
    for tag in record.tags:
        if tag not in resolved["tags"]:
            resolved["tags"].append(tag)
    resolved["lineage"].append(record_id)
    cache[record_id] = resolved
    return resolved


def localization_entries(document: dict[str, Any]) -> dict[str, str]:
    root = document.get("Data", {}).get("RootChunk", {})
    handle = root.get("root")
    payload = handle.get("Data", {}) if isinstance(handle, dict) else {}
    entries = payload.get("entries", [])
    if not isinstance(entries, list):
        raise ItemDatabaseError("Localization document has no entries array")
    result: dict[str, str] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        value = entry.get("femaleVariant") or entry.get("maleVariant") or ""
        if not isinstance(value, str) or not value:
            continue
        for key_name in ("primaryKey", "secondaryKey"):
            key = entry.get(key_name)
            if key is not None and str(key) not in {"", "0"}:
                result[str(key)] = value
    return result


def load_localizations(paths: Iterable[Path]) -> dict[str, str]:
    result: dict[str, str] = {}
    for path in paths:
        result.update(localization_entries(read_json(path)))
    return result


def localized_value(raw: str | None, localizations: dict[str, str]) -> str:
    if not raw:
        return ""
    match = LOC_KEY.match(raw)
    key = match.group(1) if match else raw
    return localizations.get(key, "")


def typed_value(value: Any) -> Any:
    if isinstance(value, dict) and "$value" in value:
        return value["$value"]
    return value


def resource_path(value: Any) -> str:
    if not isinstance(value, dict):
        return ""
    depot = value.get("DepotPath")
    result = typed_value(depot)
    return result if isinstance(result, str) else ""


def mesh_frame(path: str, definition_name: str) -> str:
    filename = Path(path.replace("\\", "/")).stem
    matches = list(FRAME_TOKEN.finditer(filename))
    if matches:
        token = matches[-1].group("frame").casefold()
        return {"ma": "pma", "wa": "pwa"}.get(token, token)
    suffix = FRAME_SUFFIX.search(definition_name)
    return FRAME_LABELS.get(suffix.group("frame").casefold(), "") if suffix else ""


def is_shadow_component(component: dict[str, Any]) -> bool:
    name = str(typed_value(component.get("name")) or "").casefold()
    mesh = resource_path(component.get("mesh")).casefold()
    return "shadow" in name or "shadow_mesh" in mesh


def app_appearance_rows(document: dict[str, Any], app_path: str) -> list[dict[str, Any]]:
    root = document.get("Data", {}).get("RootChunk", {})
    appearances = root.get("appearances", [])
    if not isinstance(appearances, list):
        raise ItemDatabaseError(f"Appearance resource has no definitions: {app_path}")
    rows: list[dict[str, Any]] = []
    app_stem = Path(app_path.replace("\\", "/")).stem
    for wrapper in appearances:
        definition = wrapper.get("Data", wrapper) if isinstance(wrapper, dict) else {}
        if not isinstance(definition, dict):
            continue
        name = typed_value(definition.get("name"))
        if not isinstance(name, str) or not name:
            continue
        components: list[dict[str, Any]] = []
        for component_wrapper in definition.get("components") or []:
            component = (
                component_wrapper.get("Data", component_wrapper)
                if isinstance(component_wrapper, dict)
                else {}
            )
            if not isinstance(component, dict):
                continue
            mesh = resource_path(component.get("mesh"))
            if not mesh:
                continue
            components.append(
                {
                    "name": str(typed_value(component.get("name")) or ""),
                    "type": str(component.get("$type") or ""),
                    "mesh": mesh,
                    "mesh_appearance": str(
                        typed_value(component.get("meshAppearance")) or "default"
                    ),
                    "chunk_mask": str(component.get("chunkMask") or ""),
                    "enabled": bool(component.get("isEnabled", 1)),
                    "shadow": is_shadow_component(component),
                }
            )
        primary_candidates = [
            component
            for component in components
            if component["enabled"]
            and not component["shadow"]
            and component["type"] in PRIMARY_COMPONENT_TYPES
        ]
        if not primary_candidates:
            primary_candidates = [
                component
                for component in components
                if component["enabled"] and not component["shadow"]
            ]
        if not primary_candidates:
            continue
        primary = primary_candidates[0]
        suffix = FRAME_SUFFIX.search(name)
        definition_base = name[: suffix.start()] if suffix else name
        lookup = f"{app_stem}_{definition_base}".casefold()
        rows.append(
            {
                "lookup": lookup,
                "app_path": app_path,
                "app_appearance": name,
                "frame": mesh_frame(primary["mesh"], name),
                "primary_mesh": primary["mesh"],
                "mesh_appearance": primary["mesh_appearance"],
                "components": components,
                "expansion": "phantom_liberty"
                if app_path.casefold().startswith("ep1\\")
                else "base_game",
            }
        )
    return rows


def infer_app_path(json_path: Path, document: dict[str, Any]) -> str:
    archive_name = document.get("Header", {}).get("ArchiveFileName")
    if isinstance(archive_name, str) and archive_name:
        normalized = archive_name.replace("/", "\\")
        for marker in ("base\\", "ep1\\"):
            index = normalized.casefold().find(marker)
            if index >= 0:
                return normalized[index:]
    name = json_path.as_posix()
    for marker in ("/base/", "/ep1/"):
        index = name.casefold().find(marker)
        if index >= 0:
            result = name[index + 1 :]
            if result.endswith(".json"):
                result = result[:-5]
            return result.replace("/", "\\")
    raise ItemDatabaseError(f"Cannot infer depot path for {json_path}")


def load_app_index(root: Path | None) -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = {}
    if root is None:
        return result
    if not root.is_dir():
        raise ItemDatabaseError(f"Serialized appearance directory was not found: {root}")
    for path in sorted(root.rglob("*.app.json")):
        document = read_json(path)
        app_path = infer_app_path(path, document)
        for row in app_appearance_rows(document, app_path):
            result.setdefault(row["lookup"], []).append(row)
    return result


def asset_sources(index: dict[str, Any]) -> dict[str, Path]:
    return {
        str(source["id"]): Path(str(source["path"]))
        for source in index.get("sources", [])
        if isinstance(source, dict) and source.get("id") and source.get("path")
    }


def app_assets(index: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        asset
        for asset in index.get("assets", [])
        if asset.get("category") == "clothing_appearance"
        and asset.get("resource_type") == "app"
    ]


def extract_app_metadata(
    index_path: Path,
    output: Path,
    wolvenkit: Path,
    game: Path,
) -> Path:
    index = read_json(index_path)
    sources = asset_sources(index)
    grouped: dict[str, list[str]] = {}
    for asset in app_assets(index):
        for source_id in asset.get("source_archives", []):
            grouped.setdefault(str(source_id), []).append(str(asset["depot_path"]))
    if not grouped:
        raise ItemDatabaseError("The character asset index contains no item .app resources")
    cache_root = output / "app-metadata"
    for source_id, paths in grouped.items():
        archive = sources.get(source_id)
        if archive is None or not archive.is_file():
            raise ItemDatabaseError(f"Archive provider is unavailable: {source_id}")
        regex = rf"appearances.*player.*items.*\.app$"
        destination = cache_root / sha1_text(source_id)[:12]
        cooked = destination / "cooked"
        serialized = destination / "serialized"
        extract_command = [
            str(wolvenkit),
            "extract",
            str(archive),
            "-o",
            str(cooked),
            "-r",
            regex,
            "-v",
            "Minimal",
        ]
        completed = subprocess.run(extract_command, cwd=ROOT, text=True, capture_output=True)
        if completed.returncode != 0:
            raise ItemDatabaseError(
                f"WolvenKit failed to extract item appearances:\n"
                f"{completed.stdout}\n{completed.stderr}"
            )
        apps = sorted(cooked.rglob("*.app"))
        if not apps:
            continue
        serialized.mkdir(parents=True, exist_ok=True)
        serialize_command = [
            str(wolvenkit),
            "convert",
            "serialize",
            *[str(path) for path in apps],
            "-o",
            str(serialized),
            "-v",
            "Minimal",
        ]
        completed = subprocess.run(serialize_command, cwd=ROOT, text=True, capture_output=True)
        if completed.returncode != 0:
            raise ItemDatabaseError(
                f"WolvenKit failed to serialize item appearances:\n"
                f"{completed.stdout}\n{completed.stderr}"
            )
    if not any(cache_root.rglob("*.app.json")):
        raise ItemDatabaseError("WolvenKit did not produce serialized item appearances")
    return cache_root


def extract_localization(
    output: Path,
    wolvenkit: Path,
    game: Path,
    include_ep1: bool = True,
) -> list[Path]:
    archives = [game / "archive/pc/content/lang_en_text.archive"]
    if include_ep1:
        archives.append(game / "archive/pc/ep1/lang_en_text.archive")
    results: list[Path] = []
    for archive in archives:
        if not archive.is_file():
            continue
        label = "ep1" if "\\ep1\\" in str(archive).casefold() else "base"
        destination = output / "localization" / label
        cooked = destination / "cooked"
        serialized = destination / "serialized"
        extract_command = [
            str(wolvenkit),
            "extract",
            str(archive),
            "-o",
            str(cooked),
            "-r",
            r"onscreens.json$",
            "-v",
            "Minimal",
        ]
        completed = subprocess.run(extract_command, cwd=ROOT, text=True, capture_output=True)
        if completed.returncode != 0:
            raise ItemDatabaseError(
                f"WolvenKit failed to extract {label} localization:\n"
                f"{completed.stdout}\n{completed.stderr}"
            )
        sources = [
            path
            for path in cooked.rglob("onscreens.json")
            if path.name == "onscreens.json"
        ]
        if not sources:
            continue
        serialized.mkdir(parents=True, exist_ok=True)
        serialize_command = [
            str(wolvenkit),
            "convert",
            "serialize",
            *[str(path) for path in sources],
            "-o",
            str(serialized),
            "-v",
            "Minimal",
        ]
        completed = subprocess.run(serialize_command, cwd=ROOT, text=True, capture_output=True)
        if completed.returncode != 0:
            raise ItemDatabaseError(
                f"WolvenKit failed to serialize {label} localization:\n"
                f"{completed.stdout}\n{completed.stderr}"
            )
        results.extend(serialized.rglob("onscreens.json.json"))
    return results


def connect(path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def create_schema(connection: sqlite3.Connection) -> None:
    connection.executescript(
        """
        PRAGMA journal_mode = WAL;
        DROP TABLE IF EXISTS renders;
        DROP TABLE IF EXISTS variants;
        DROP TABLE IF EXISTS items;
        DROP TABLE IF EXISTS metadata;
        CREATE TABLE metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
        CREATE TABLE items (
            record_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            display_key TEXT NOT NULL,
            description_key TEXT NOT NULL,
            equip_area TEXT NOT NULL,
            slot TEXT NOT NULL,
            item_type TEXT NOT NULL,
            entity_name TEXT NOT NULL,
            appearance_stem TEXT NOT NULL,
            tags_json TEXT NOT NULL,
            source_file TEXT NOT NULL,
            lineage_json TEXT NOT NULL
        );
        CREATE TABLE variants (
            variant_id TEXT PRIMARY KEY,
            item_id TEXT NOT NULL REFERENCES items(record_id) ON DELETE CASCADE,
            frame TEXT NOT NULL,
            app_path TEXT NOT NULL,
            app_appearance TEXT NOT NULL,
            expansion TEXT NOT NULL,
            primary_mesh TEXT NOT NULL,
            mesh_appearance TEXT NOT NULL,
            components_json TEXT NOT NULL,
            UNIQUE(item_id, frame, app_path, app_appearance)
        );
        CREATE TABLE renders (
            render_id TEXT PRIMARY KEY,
            variant_id TEXT NOT NULL UNIQUE REFERENCES variants(variant_id) ON DELETE CASCADE,
            hero_path TEXT NOT NULL,
            views_json TEXT NOT NULL,
            fingerprint TEXT NOT NULL,
            renderer TEXT NOT NULL,
            status TEXT NOT NULL,
            error TEXT NOT NULL
        );
        CREATE INDEX variants_item_idx ON variants(item_id);
        CREATE INDEX variants_frame_idx ON variants(frame);
        CREATE INDEX items_slot_idx ON items(slot);
        """
    )


def fallback_title(name: str) -> str:
    return re.sub(r"[_-]+", " ", name).strip().title()


def build_database(
    database: Path,
    tweak_root: Path,
    app_root: Path | None,
    localization_paths: list[Path],
    output_json: Path | None = None,
) -> dict[str, Any]:
    records = load_tweak_records(tweak_root)
    resolved_cache: dict[str, dict[str, Any]] = {}
    localizations = load_localizations(localization_paths)
    appearances = load_app_index(app_root)
    database.parent.mkdir(parents=True, exist_ok=True)
    if database.exists():
        database.unlink()
    connection = connect(database)
    create_schema(connection)
    item_count = 0
    variant_count = 0
    matched_items = 0
    flattened: list[dict[str, Any]] = []
    for record_id, record in sorted(records.items()):
        if "notQueryable" in record.attributes or record.name.endswith("_Crafting"):
            continue
        resolved = resolve_record(record_id, records, resolved_cache)
        scalars = resolved.get("scalars", {})
        appearance_stem = str(scalars.get("appearanceName", ""))
        equip_area = str(scalars.get("equipArea", ""))
        if not appearance_stem or equip_area not in EQUIPMENT_SLOTS:
            continue
        display_key = str(scalars.get("displayName", ""))
        description_key = str(scalars.get("localizedDescription", ""))
        title = localized_value(display_key, localizations) or fallback_title(record.name)
        description = localized_value(description_key, localizations)
        tags = list(resolved.get("tags", []))
        connection.execute(
            """
            INSERT INTO items VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                record_id,
                title,
                description,
                display_key,
                description_key,
                equip_area,
                EQUIPMENT_SLOTS[equip_area],
                str(scalars.get("itemType", "")),
                str(scalars.get("entityName", "")),
                appearance_stem,
                json.dumps(tags, ensure_ascii=False),
                str(record.source.resolve()),
                json.dumps(resolved.get("lineage", []), ensure_ascii=False),
            ),
        )
        item_count += 1
        lookup = appearance_stem.rstrip("_").casefold()
        rows = appearances.get(lookup, [])
        if rows:
            matched_items += 1
        seen_variants: set[str] = set()
        for row in rows:
            frame = row["frame"] or "unknown"
            unique = f"{frame}\0{row['app_path']}\0{row['app_appearance']}"
            if unique in seen_variants:
                continue
            seen_variants.add(unique)
            variant_id = (
                f"{record_id}:{frame}:{sha1_text(row['app_path'] + chr(0) + row['app_appearance'])[:12]}"
            )
            connection.execute(
                """
                INSERT INTO variants VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    variant_id,
                    record_id,
                    frame,
                    row["app_path"],
                    row["app_appearance"],
                    row["expansion"],
                    row["primary_mesh"],
                    row["mesh_appearance"],
                    json.dumps(row["components"], ensure_ascii=False),
                ),
            )
            variant_count += 1
            flattened.append(
                {
                    "variant_id": variant_id,
                    "record_id": record_id,
                    "title": title,
                    "description": description,
                    "slot": EQUIPMENT_SLOTS[equip_area],
                    "frame": frame,
                    "tags": tags,
                    "appearance_stem": appearance_stem,
                    **{key: row[key] for key in row if key != "lookup"},
                }
            )
    metadata = {
        "schema_version": SCHEMA_VERSION,
        "items": item_count,
        "variants": variant_count,
        "matched_items": matched_items,
        "unmatched_items": item_count - matched_items,
        "localization_entries": len(localizations),
        "serialized_apps": len(list(app_root.rglob("*.app.json"))) if app_root else 0,
    }
    for key, value in metadata.items():
        connection.execute(
            "INSERT INTO metadata(key, value) VALUES (?, ?)", (key, json.dumps(value))
        )
    connection.commit()
    connection.close()
    if output_json is not None:
        write_json(
            output_json,
            {
                "schema_version": SCHEMA_VERSION,
                "summary": metadata,
                "variants": flattened,
            },
        )
    return metadata


def variant_filter(
    query: str = "",
    slot: str = "",
    frame: str = "",
    tag: str = "",
    rendered: str = "",
) -> tuple[str, list[Any]]:
    clauses: list[str] = []
    parameters: list[Any] = []
    if query:
        clauses.append(
            "(lower(i.title) LIKE ? OR lower(i.description) LIKE ? "
            "OR lower(i.record_id) LIKE ? OR lower(i.tags_json) LIKE ?)"
        )
        term = f"%{query.casefold()}%"
        parameters.extend([term, term, term, term])
    if slot:
        clauses.append("i.slot = ?")
        parameters.append(slot)
    if frame:
        clauses.append("v.frame = ?")
        parameters.append(frame)
    if tag:
        clauses.append("lower(i.tags_json) LIKE ?")
        parameters.append(f'%"{tag.casefold()}"%')
    if rendered == "complete":
        clauses.append("r.variant_id IS NOT NULL")
    elif rendered == "pending":
        clauses.append("r.variant_id IS NULL")
    where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    return where, parameters


def query_variants(
    connection: sqlite3.Connection,
    query: str = "",
    slot: str = "",
    frame: str = "",
    tag: str = "",
    limit: int = 100,
    offset: int = 0,
    rendered: str = "",
) -> list[dict[str, Any]]:
    where, parameters = variant_filter(query, slot, frame, tag, rendered)
    parameters.extend([max(1, min(limit, 500)), max(0, offset)])
    rows = connection.execute(
        f"""
        SELECT i.*, v.*, r.hero_path, r.views_json, r.status AS render_status
        FROM variants v
        JOIN items i ON i.record_id = v.item_id
        LEFT JOIN renders r ON r.variant_id = v.variant_id AND r.status = 'complete'
        {where}
        ORDER BY i.title COLLATE NOCASE, v.frame, v.app_appearance
        LIMIT ? OFFSET ?
        """,
        parameters,
    ).fetchall()
    result: list[dict[str, Any]] = []
    for row in rows:
        value = dict(row)
        value["tags"] = json.loads(value.pop("tags_json"))
        value["components"] = json.loads(value.pop("components_json"))
        value["views"] = json.loads(value.pop("views_json")) if value.get("views_json") else []
        value.pop("lineage_json", None)
        result.append(value)
    return result


def count_variants(
    connection: sqlite3.Connection,
    query: str = "",
    slot: str = "",
    frame: str = "",
    tag: str = "",
    rendered: str = "",
) -> int:
    where, parameters = variant_filter(query, slot, frame, tag, rendered)
    return int(
        connection.execute(
            f"""
            SELECT count(*)
            FROM variants v
            JOIN items i ON i.record_id = v.item_id
            LEFT JOIN renders r ON r.variant_id = v.variant_id AND r.status = 'complete'
            {where}
            """,
            parameters,
        ).fetchone()[0]
    )


def database_summary(connection: sqlite3.Connection) -> dict[str, Any]:
    summary = {
        row["key"]: json.loads(row["value"])
        for row in connection.execute("SELECT key, value FROM metadata")
    }
    summary["slots"] = [
        dict(row)
        for row in connection.execute(
            "SELECT slot, count(*) AS count FROM items GROUP BY slot ORDER BY slot"
        )
    ]
    summary["frames"] = [
        dict(row)
        for row in connection.execute(
            "SELECT frame, count(*) AS count FROM variants GROUP BY frame ORDER BY frame"
        )
    ]
    summary["rendered"] = connection.execute(
        "SELECT count(*) FROM renders WHERE status = 'complete'"
    ).fetchone()[0]
    tag_counts: dict[str, int] = {}
    for row in connection.execute("SELECT tags_json FROM items"):
        for tag in json.loads(row["tags_json"]):
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
    summary["tags"] = [
        {"tag": tag, "count": count}
        for tag, count in sorted(tag_counts.items(), key=lambda pair: (-pair[1], pair[0]))[:100]
    ]
    return summary


def source_archive_for_mesh(index: dict[str, Any], depot_path: str) -> Path:
    sources = asset_sources(index)
    normalized = depot_path.replace("/", "\\").casefold()
    for asset in index.get("assets", []):
        if str(asset.get("depot_path", "")).casefold() != normalized:
            continue
        for source_id in asset.get("source_archives", []):
            archive = sources.get(str(source_id))
            if archive and archive.is_file():
                return archive
    raise ItemDatabaseError(f"Mesh is absent from the installed asset index: {depot_path}")


def material_export_fingerprint(
    mesh: str,
    appearance: str,
    archive: Path,
    ghostline_red: Path,
    red_schema: Path,
    game: Path,
) -> str:
    executable = game / "bin/x64/Cyberpunk2077.exe"
    payload = {
        "mesh": mesh.casefold(),
        "appearance": appearance,
        "archive": file_identity(archive),
        "ghostline_red": file_identity(ghostline_red),
        "red_schema": file_identity(red_schema),
        "game": file_identity(executable),
        "mode": "native-pbr-selected-appearance-v3",
    }
    return sha1_text(json.dumps(payload, sort_keys=True))


def prepare_material_export(
    index: dict[str, Any],
    depot_path: str,
    appearance: str,
    cache_root: Path,
    ghostline_red: Path,
    red_schema: Path,
    game: Path,
) -> dict[str, Any]:
    archive = source_archive_for_mesh(index, depot_path)
    fingerprint = material_export_fingerprint(
        depot_path,
        appearance,
        archive,
        ghostline_red,
        red_schema,
        game,
    )
    final = cache_root / fingerprint
    relative = Path(*depot_path.replace("/", "\\").split("\\"))
    glb = (final / "raw" / relative).with_suffix(".glb")
    material_json = glb.with_name(f"{glb.stem}.Material.json")
    manifest = final / "manifest.json"
    if glb.is_file() and material_json.is_file() and manifest.is_file():
        return read_json(manifest)
    cache_root.mkdir(parents=True, exist_ok=True)
    shared_materials = cache_root.parent / "material-repo"
    shared_materials.mkdir(parents=True, exist_ok=True)
    kraken = DEFAULT_KRAKEN
    with tempfile.TemporaryDirectory(dir=cache_root, prefix=".material-export.") as directory:
        staging = Path(directory)
        cooked = staging / "cooked"
        raw = staging / "raw"
        cooked_mesh = cooked / relative
        staged_glb = (raw / relative).with_suffix(".glb")
        extract_command = [
            str(ghostline_red),
            "--kraken",
            str(kraken),
            "extract",
            str(archive),
            "--output",
            str(cooked),
            "--path",
            depot_path,
        ]
        extracted = subprocess.run(extract_command, cwd=ROOT, text=True, capture_output=True)
        if extracted.returncode != 0 or not cooked_mesh.is_file():
            raise ItemDatabaseError(
                f"ghostline-red mesh extraction failed for {depot_path}:\n"
                f"{extracted.stdout}\n{extracted.stderr}"
            )
        staged_glb.parent.mkdir(parents=True, exist_ok=True)
        export_command = [
            str(ghostline_red),
            "--kraken",
            str(kraken),
            "mesh-export",
            str(cooked_mesh),
            "--schema",
            str(red_schema),
            "--output",
            str(staged_glb),
            "--archives-root",
            str(game / "archive/pc"),
            "--material-repo",
            str(shared_materials),
            "--appearance",
            appearance,
            "--pbr",
            "--pbr-size",
            "512",
        ]
        completed = subprocess.run(export_command, cwd=ROOT, text=True, capture_output=True)
        staged_material = staged_glb.with_name(f"{staged_glb.stem}.Material.json")
        if completed.returncode != 0 or not staged_glb.is_file() or not staged_material.is_file():
            raise ItemDatabaseError(
                f"ghostline-red material export failed for {depot_path} ({appearance}):\n"
                f"{completed.stdout}\n{completed.stderr}"
            )
        final.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(staging, final)
    result = {
        "schema_version": 1,
        "fingerprint": fingerprint,
        "source": depot_path,
        "appearance": appearance,
        "archive": str(archive.resolve()),
        "glb": str(glb.resolve()),
        "material_json": str(material_json.resolve()),
        "material_repo": str(shared_materials.resolve()),
        "exporter": "ghostline-red",
        "native_pbr": True,
    }
    write_json(manifest, result)
    return result


def prepare_material_exports_bulk(
    index: dict[str, Any],
    requests: Iterable[tuple[str, str]],
    cache_root: Path,
    ghostline_red: Path,
    red_schema: Path,
    game: Path,
    export_workers: int,
) -> tuple[dict[tuple[str, str], dict[str, Any]], dict[tuple[str, str], str]]:
    cache_root.mkdir(parents=True, exist_ok=True)
    shared_materials = cache_root.parent / "material-repo"
    shared_materials.mkdir(parents=True, exist_ok=True)
    descriptors: dict[tuple[str, str], dict[str, Any]] = {}
    errors: dict[tuple[str, str], str] = {}
    jobs: list[dict[str, str]] = []
    for depot_path, appearance in dict.fromkeys(requests):
        archive = source_archive_for_mesh(index, depot_path)
        fingerprint = material_export_fingerprint(
            depot_path,
            appearance,
            archive,
            ghostline_red,
            red_schema,
            game,
        )
        final = cache_root / fingerprint
        relative = Path(*depot_path.replace("/", "\\").split("\\"))
        glb = (final / "raw" / relative).with_suffix(".glb")
        material_json = glb.with_name(f"{glb.stem}.Material.json")
        manifest = final / "manifest.json"
        failure_manifest = final / "failure.json"
        result = {
            "schema_version": 1,
            "fingerprint": fingerprint,
            "source": depot_path,
            "appearance": appearance,
            "archive": str(archive.resolve()),
            "glb": str(glb.resolve()),
            "material_json": str(material_json.resolve()),
            "material_repo": str(shared_materials.resolve()),
            "exporter": "ghostline-red-batch",
            "native_pbr": True,
        }
        key = (depot_path, appearance)
        descriptors[key] = {
            "result": result,
            "manifest": manifest,
            "failure_manifest": failure_manifest,
            "glb": glb,
            "material_json": material_json,
        }
        if glb.is_file() and material_json.is_file() and manifest.is_file():
            continue
        if failure_manifest.is_file():
            failure = read_json(failure_manifest)
            errors[key] = str(failure.get("error") or "cached material export failure")
            continue
        glb.parent.mkdir(parents=True, exist_ok=True)
        jobs.append(
            {
                "mesh": depot_path,
                "appearance": appearance,
                "output": str(glb.resolve()),
            }
        )

    if jobs:
        with tempfile.TemporaryDirectory(dir=cache_root, prefix=".bulk-material-export.") as directory:
            temporary = Path(directory)
            job_manifest = temporary / "jobs.json"
            report_path = temporary / "report.json"
            write_json(job_manifest, {"jobs": jobs})
            command = [
                str(ghostline_red),
                "--kraken",
                str(DEFAULT_KRAKEN),
                "mesh-export-batch",
                str(job_manifest),
                "--schema",
                str(red_schema),
                "--archives-root",
                str(game / "archive/pc"),
                "--material-repo",
                str(shared_materials),
                "--report",
                str(report_path),
                "--pbr",
                "--pbr-size",
                "512",
                "--threads",
                str(max(1, export_workers)),
            ]
            completed = subprocess.run(command, cwd=ROOT, text=True)
            outcomes = read_json(report_path) if report_path.is_file() else []
            outcome_map = {
                (str(outcome["mesh"]), str(outcome["appearance"])): outcome
                for outcome in outcomes
            }
            for job in jobs:
                key = (job["mesh"], job["appearance"])
                outcome = outcome_map.get(key)
                error = str(outcome.get("error") or "") if outcome else ""
                descriptor = descriptors[key]
                if (
                    not error
                    and descriptor["glb"].is_file()
                    and descriptor["material_json"].is_file()
                ):
                    write_json(descriptor["manifest"], descriptor["result"])
                else:
                    failure = error or (
                        f"bulk exporter exited {completed.returncode} without producing "
                        f"{descriptor['glb']}"
                    )
                    errors[key] = failure
                    if error:
                        write_json(
                            descriptor["failure_manifest"],
                            {
                                "schema_version": 1,
                                "source": job["mesh"],
                                "appearance": job["appearance"],
                                "error": failure,
                            },
                        )

    exports = {
        key: descriptor["result"]
        for key, descriptor in descriptors.items()
        if key not in errors
        and descriptor["glb"].is_file()
        and descriptor["material_json"].is_file()
        and descriptor["manifest"].is_file()
    }
    return exports, errors


def render_fingerprint(
    export: dict[str, Any],
    appearance: str,
    blender: Path,
    resolution: int,
    samples: int,
    engine: str,
    views: list[str],
) -> str:
    payload = {
        "asset": export["fingerprint"],
        "appearance": appearance,
        "blender": file_identity(blender),
        "script": file_identity(BLENDER_SCRIPT),
        "resolution": resolution,
        "samples": samples,
        "engine": engine,
        "views": views,
    }
    return sha1_text(json.dumps(payload, sort_keys=True))


def compatible_render_reports(
    render_root: Path,
    resolution: int,
    samples: int,
    engine: str,
    views: list[str],
) -> dict[tuple[str, str], Path]:
    compatible: dict[tuple[str, str], Path] = {}
    for report_path in render_root.glob("*/render-report.json"):
        try:
            report = read_json(report_path)
            report_views = [Path(path).stem for path in report.get("images", [])]
            image_paths = [Path(path) for path in report.get("images", [])]
            if (
                report.get("resolution") != resolution
                or report.get("samples") != samples
                or report.get("engine") != engine
                or report_views != views
                or not image_paths
                or not all(path.is_file() for path in image_paths)
            ):
                continue
            key = (
                os.path.normcase(str(Path(report["glb"]).resolve())),
                str(report["appearance"]),
            )
            previous = compatible.get(key)
            if previous is None or report_path.stat().st_mtime_ns > previous.stat().st_mtime_ns:
                compatible[key] = report_path
        except (KeyError, OSError, ValueError, json.JSONDecodeError):
            continue
    return compatible


def render_variants(
    database: Path,
    index_path: Path,
    output: Path,
    ghostline_red: Path,
    red_schema: Path,
    blender: Path,
    game: Path,
    item: str,
    frame: str,
    slot: str,
    limit: int,
    resolution: int,
    samples: int,
    engine: str,
    views: list[str],
    batch_size: int,
    workers: int,
    export_workers: int,
    reuse_compatible: bool,
) -> dict[str, Any]:
    if not database.is_file():
        raise ItemDatabaseError(f"Item database was not found: {database}")
    if not index_path.is_file():
        raise ItemDatabaseError(f"Character asset index was not found: {index_path}")
    if not ghostline_red.is_file() or not red_schema.is_file() or not blender.is_file():
        raise ItemDatabaseError(
            "ghostline-red release binary, RED schema, and Blender 5.1 are required for rendering"
        )
    index = read_json(index_path)
    connection = connect(database)
    clauses: list[str] = []
    parameters: list[Any] = []
    if item:
        clauses.append("(i.record_id = ? OR i.record_id LIKE ?)")
        parameters.extend([item, f"%{item}%"])
    if frame:
        clauses.append("v.frame = ?")
        parameters.append(frame)
    if slot:
        clauses.append("i.slot = ?")
        parameters.append(slot)
    where = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    parameters.append(max(1, limit))
    candidates = connection.execute(
        f"""
        SELECT i.record_id, i.title, v.*
        FROM variants v JOIN items i ON i.record_id = v.item_id
        {where}
        ORDER BY i.title, v.frame LIMIT ?
        """,
        parameters,
    ).fetchall()
    export_requests = [
        (str(row["primary_mesh"]), str(row["mesh_appearance"])) for row in candidates
    ]
    print(
        f"Bulk-exporting {len(dict.fromkeys(export_requests))} unique mesh appearances",
        flush=True,
    )
    exports, export_errors = prepare_material_exports_bulk(
        index,
        export_requests,
        output / "asset-cache",
        ghostline_red,
        red_schema,
        game,
        export_workers,
    )
    rendered = 0
    reused = 0
    failures: list[dict[str, str]] = []
    prepared: list[dict[str, Any]] = []
    compatible = (
        compatible_render_reports(
            output / "renders",
            resolution,
            samples,
            engine,
            views,
        )
        if reuse_compatible
        else {}
    )
    for position, row in enumerate(candidates, start=1):
        variant = dict(row)
        started = time.monotonic()
        print(
            f"[{position}/{len(candidates)}] {variant['variant_id']} "
            f"({variant['mesh_appearance']})",
            flush=True,
        )
        try:
            export_key = (variant["primary_mesh"], variant["mesh_appearance"])
            if export_key in export_errors:
                raise ItemDatabaseError(export_errors[export_key])
            export = exports[export_key]
            fingerprint = render_fingerprint(
                export,
                variant["mesh_appearance"],
                blender,
                resolution,
                samples,
                engine,
                views,
            )
            render_root = output / "renders" / fingerprint
            report_path = render_root / "render-report.json"
            if report_path.is_file():
                reused += 1
                state = "reused"
            elif compatible_report := compatible.get(
                (
                    os.path.normcase(str(Path(export["glb"]).resolve())),
                    variant["mesh_appearance"],
                )
            ):
                report_path = compatible_report
                render_root = compatible_report.parent
                fingerprint = render_root.name
                reused += 1
                state = "reused"
            else:
                render_root.mkdir(parents=True, exist_ok=True)
                state = "pending"
            prepared.append(
                {
                    "variant": variant,
                    "export": export,
                    "fingerprint": fingerprint,
                    "render_root": render_root,
                    "report_path": report_path,
                    "state": state,
                }
            )
            print(
                f"[{position}/{len(candidates)}] prepared ({state}) in "
                f"{time.monotonic() - started:.1f}s",
                flush=True,
            )
        except Exception as exc:
            failures.append({"variant_id": variant["variant_id"], "error": str(exc)})
            print(
                f"[{position}/{len(candidates)}] failed in "
                f"{time.monotonic() - started:.1f}s: {exc}",
                flush=True,
            )

    pending_by_fingerprint: dict[str, dict[str, Any]] = {}
    for entry in prepared:
        if entry["state"] == "pending":
            pending_by_fingerprint.setdefault(entry["fingerprint"], entry)
    pending = list(pending_by_fingerprint.values())
    duplicate_count = sum(entry["state"] == "pending" for entry in prepared) - len(pending)
    if duplicate_count:
        print(
            f"Reusing {duplicate_count} duplicate variant renders within this run",
            flush=True,
        )
    batch_size = max(1, batch_size)
    workers = max(1, workers)
    render_errors: dict[str, str] = {}
    with tempfile.TemporaryDirectory(dir=output, prefix=".render-batch.") as directory:
        batch_directory = Path(directory)
        batch_count = (len(pending) + batch_size - 1) // batch_size
        batches: list[dict[str, Any]] = []
        for batch_start in range(0, len(pending), batch_size):
            batch = pending[batch_start : batch_start + batch_size]
            batch_number = batch_start // batch_size + 1
            jobs_path = batch_directory / f"jobs-{batch_number}.json"
            batch_report = batch_directory / f"report-{batch_number}.json"
            write_json(
                jobs_path,
                {
                    "jobs": [
                        {
                            "glb": entry["export"]["glb"],
                            "appearance": entry["variant"]["mesh_appearance"],
                            "output": str(entry["render_root"]),
                            "native_pbr": bool(entry["export"].get("native_pbr")),
                        }
                        for entry in batch
                    ]
                },
            )
            command = [
                str(blender),
                "--background",
                "--python",
                str(BLENDER_SCRIPT),
                "--",
                "--jobs",
                str(jobs_path),
                "--batch-report",
                str(batch_report),
                "--resolution",
                str(resolution),
                "--samples",
                str(samples),
                "--engine",
                engine,
                "--views",
                ",".join(views),
            ]
            batches.append(
                {
                    "number": batch_number,
                    "entries": batch,
                    "command": command,
                }
            )

        def run_batch(batch: dict[str, Any]) -> tuple[dict[str, Any], subprocess.CompletedProcess[str]]:
            print(
                f"[batch {batch['number']}/{batch_count}] rendering "
                f"{len(batch['entries'])} variants",
                flush=True,
            )
            process = subprocess.Popen(
                batch["command"],
                cwd=ROOT,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                bufsize=1,
            )
            diagnostic_lines: collections.deque[str] = collections.deque(maxlen=200)
            if process.stdout is None:
                raise ItemDatabaseError("Blender did not provide a progress stream")
            for line in process.stdout:
                diagnostic_lines.append(line)
                message = line.strip()
                if message.startswith(
                    ("GHOSTLINE_BATCH_DONE", "GHOSTLINE_BATCH_FAILED", "GHOSTLINE_BATCH_OK")
                ):
                    print(f"[batch {batch['number']}/{batch_count}] {message}", flush=True)
            return_code = process.wait()
            completed = subprocess.CompletedProcess(
                args=batch["command"],
                returncode=return_code,
                stdout="".join(diagnostic_lines),
                stderr="",
            )
            return batch, completed

        print(
            f"Rendering {len(pending)} unique variants with "
            f"{min(workers, max(1, len(batches)))} Blender workers",
            flush=True,
        )
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            futures = [executor.submit(run_batch, batch) for batch in batches]
            for future in concurrent.futures.as_completed(futures):
                batch, completed = future.result()
                diagnostic = f"{completed.stdout}\n{completed.stderr}"[-8000:]
                print(
                    f"[batch {batch['number']}/{batch_count}] finished "
                    f"(exit {completed.returncode})",
                    flush=True,
                )
                for entry in batch["entries"]:
                    report_path = entry["report_path"]
                    if not report_path.is_file():
                        render_errors[entry["fingerprint"]] = (
                            f"Blender batch render failed ({completed.returncode}):\n"
                            f"{diagnostic}"
                        )

    for entry in prepared:
        if entry["state"] != "pending":
            continue
        if entry["report_path"].is_file():
            entry["state"] = "rendered"
            rendered += 1
        else:
            entry["state"] = "failed"
            failures.append(
                {
                    "variant_id": entry["variant"]["variant_id"],
                    "error": render_errors.get(
                        entry["fingerprint"],
                        "Blender did not create a render report",
                    ),
                }
            )

    for entry in prepared:
        if entry["state"] == "failed":
            continue
        report = read_json(entry["report_path"])
        image_paths = [str(Path(path).resolve()) for path in report["images"]]
        hero = next(
            (path for path in image_paths if Path(path).stem == "hero"),
            image_paths[0],
        )
        connection.execute(
            """
            INSERT INTO renders VALUES (?, ?, ?, ?, ?, ?, 'complete', '')
            ON CONFLICT(variant_id) DO UPDATE SET
                render_id=excluded.render_id,
                hero_path=excluded.hero_path,
                views_json=excluded.views_json,
                fingerprint=excluded.fingerprint,
                renderer=excluded.renderer,
                status=excluded.status,
                error=excluded.error
            """,
            (
                hashlib.sha1(
                    f"{entry['fingerprint']}:{entry['variant']['variant_id']}".encode()
                ).hexdigest(),
                entry["variant"]["variant_id"],
                hero,
                json.dumps(image_paths),
                entry["fingerprint"],
                f"Blender {engine}",
            ),
        )
    connection.commit()
    connection.close()
    return {
        "selected": len(candidates),
        "rendered": rendered,
        "reused": reused,
        "failures": failures,
    }


def caption_jobs(
    database: Path,
    output: Path,
    only_rendered: bool,
    limit: int,
) -> dict[str, Any]:
    connection = connect(database)
    where = "WHERE r.status = 'complete'" if only_rendered else ""
    rows = connection.execute(
        f"""
        SELECT i.record_id, i.title, i.description, i.slot, i.tags_json,
               v.variant_id, v.frame, v.expansion, v.app_appearance,
               v.primary_mesh, v.mesh_appearance, r.hero_path, r.views_json
        FROM variants v
        JOIN items i ON i.record_id = v.item_id
        LEFT JOIN renders r ON r.variant_id = v.variant_id
        {where}
        ORDER BY i.title, v.frame
        LIMIT ?
        """,
        (max(1, limit),),
    ).fetchall()
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=output.parent, delete=False, prefix=f".{output.name}."
    ) as handle:
        for row in rows:
            value = dict(row)
            value["game_tags"] = json.loads(value.pop("tags_json"))
            value["images"] = (
                json.loads(value.pop("views_json")) if value.get("views_json") else []
            )
            value.pop("views_json", None)
            value["caption_schema"] = {
                "colors": [],
                "materials": [],
                "patterns": [],
                "silhouette": [],
                "style": [],
                "character_signals": [],
                "coverage": [],
                "condition": [],
                "confidence": 0.0,
            }
            handle.write(json.dumps(value, ensure_ascii=False) + "\n")
        temporary = Path(handle.name)
    os.replace(temporary, output)
    connection.close()
    return {"jobs": len(rows), "output": str(output.resolve())}


class GalleryHandler(http.server.SimpleHTTPRequestHandler):
    database: Path
    output_root: Path

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, directory=str(GALLERY_ROOT), **kwargs)

    def log_message(self, format: str, *args: Any) -> None:
        sys.stderr.write(f"[item-gallery] {format % args}\n")

    def send_json(self, value: Any, status: int = 200) -> None:
        body = json.dumps(value, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/summary":
            with contextlib.closing(connect(self.database)) as connection:
                self.send_json(database_summary(connection))
            return
        if parsed.path == "/api/items":
            query = urllib.parse.parse_qs(parsed.query)
            query_text = query.get("q", [""])[0]
            slot = query.get("slot", [""])[0]
            frame = query.get("frame", [""])[0]
            tag = query.get("tag", [""])[0]
            rendered = query.get("rendered", [""])[0]
            limit = max(1, min(int(query.get("limit", ["48"])[0]), 500))
            offset = max(0, int(query.get("offset", ["0"])[0]))
            with contextlib.closing(connect(self.database)) as connection:
                items = query_variants(
                    connection,
                    query_text,
                    slot,
                    frame,
                    tag,
                    limit,
                    offset,
                    rendered,
                )
                total = count_variants(
                    connection, query_text, slot, frame, tag, rendered
                )
            for item in items:
                view_urls: dict[str, str] = {}
                for view_path in item.get("views", []):
                    resolved_view = Path(view_path).resolve()
                    try:
                        relative_view = resolved_view.relative_to(
                            self.output_root.resolve()
                        )
                    except ValueError:
                        continue
                    view_urls[resolved_view.stem] = (
                        "/images/"
                        + urllib.parse.quote(str(relative_view).replace("\\", "/"))
                    )
                item["view_urls"] = view_urls
                if item.get("hero_path"):
                    item["image_url"] = "/images/" + urllib.parse.quote(
                        str(Path(item["hero_path"]).resolve().relative_to(self.output_root.resolve())).replace(
                            "\\", "/"
                        )
                    )
            self.send_json(
                {
                    "items": items,
                    "total": total,
                    "limit": limit,
                    "offset": offset,
                }
            )
            return
        if parsed.path.startswith("/images/"):
            relative = urllib.parse.unquote(parsed.path.removeprefix("/images/"))
            target = (self.output_root / Path(relative)).resolve()
            try:
                target.relative_to(self.output_root.resolve())
            except ValueError:
                self.send_error(403)
                return
            if not target.is_file():
                self.send_error(404)
                return
            body = target.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "image/png")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        super().do_GET()


def serve(database: Path, output: Path, host: str, port: int, open_browser: bool) -> None:
    if host not in {"127.0.0.1", "localhost", "::1"}:
        raise ItemDatabaseError("The item gallery only binds to a loopback host")
    if not database.is_file():
        raise ItemDatabaseError(f"Item database was not found: {database}")
    handler = type(
        "ConfiguredGalleryHandler",
        (GalleryHandler,),
        {"database": database.resolve(), "output_root": output.resolve()},
    )
    server = http.server.ThreadingHTTPServer((host, port), handler)
    address = f"http://{host}:{server.server_address[1]}"
    print(f"Item gallery: {address}")
    if open_browser:
        webbrowser.open(address)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build and render the Ghostline equipment database")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--gamepath", type=Path, default=DEFAULT_GAME)
    parser.add_argument("--wolvenkit", type=Path, default=DEFAULT_WOLVENKIT)
    parser.add_argument("--ghostline-red", type=Path, default=DEFAULT_GHOSTLINE_RED)
    parser.add_argument("--red-schema", type=Path, default=DEFAULT_RED_SCHEMA)
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    subparsers = parser.add_subparsers(dest="command", required=True)

    build = subparsers.add_parser("build", help="Build SQLite and JSON equipment catalogs")
    build.add_argument("--tweaks", type=Path, default=DEFAULT_TWEAK_ROOT)
    build.add_argument("--apps", type=Path)
    build.add_argument("--localization", type=Path, action="append", default=[])
    build.add_argument("--extract-apps", action="store_true")
    build.add_argument("--extract-localization", action="store_true")

    render = subparsers.add_parser("render", help="Render material-aware item previews")
    render.add_argument("--database", type=Path)
    render.add_argument("--blender", type=Path, default=DEFAULT_BLENDER)
    render.add_argument("--item", default="")
    render.add_argument("--frame", choices=["", "pma", "pwa", "unknown"], default="")
    render.add_argument("--slot", default="")
    render.add_argument("--limit", type=int, default=1)
    render.add_argument("--resolution", type=int, default=1024)
    render.add_argument("--samples", type=int, default=128)
    render.add_argument("--engine", choices=["BLENDER_EEVEE", "CYCLES"], default="CYCLES")
    render.add_argument("--views", default="hero,back")
    render.add_argument(
        "--batch-size",
        type=int,
        default=25,
        help="Variants rendered per persistent Blender process",
    )
    render.add_argument(
        "--workers",
        type=int,
        default=2,
        help="Persistent Blender processes run concurrently",
    )
    render.add_argument(
        "--export-workers",
        type=int,
        default=min(12, os.cpu_count() or 1),
        help="Concurrent ghostline-red mesh/material preparation jobs",
    )
    render.add_argument(
        "--reuse-compatible",
        action="store_true",
        help="Reuse matching reports after renderer performance-only changes",
    )

    captions = subparsers.add_parser("caption-export", help="Write caption-model JSONL jobs")
    captions.add_argument("--database", type=Path)
    captions.add_argument("--file", type=Path)
    captions.add_argument("--include-unrendered", action="store_true")
    captions.add_argument("--limit", type=int, default=100000)

    gallery = subparsers.add_parser("serve", help="Serve the local searchable item gallery")
    gallery.add_argument("--database", type=Path)
    gallery.add_argument("--host", default="127.0.0.1")
    gallery.add_argument("--port", type=int, default=8766)
    gallery.add_argument("--open", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    output = args.output.resolve()
    database = (getattr(args, "database", None) or output / "items.sqlite3").resolve()
    try:
        if args.command == "build":
            app_root = args.apps
            localization_paths = list(args.localization)
            if args.extract_apps:
                app_root = extract_app_metadata(
                    args.index.resolve(), output / "cache", args.wolvenkit.resolve(), args.gamepath.resolve()
                )
            if args.extract_localization:
                localization_paths.extend(
                    extract_localization(output / "cache", args.wolvenkit.resolve(), args.gamepath.resolve())
                )
            summary = build_database(
                database,
                args.tweaks.resolve(),
                app_root.resolve() if app_root else None,
                [path.resolve() for path in localization_paths],
                output / "catalog.json",
            )
            print(json.dumps(summary, indent=2))
        elif args.command == "render":
            result = render_variants(
                database,
                args.index.resolve(),
                output,
                args.ghostline_red.resolve(),
                args.red_schema.resolve(),
                args.blender.resolve(),
                args.gamepath.resolve(),
                args.item,
                args.frame,
                args.slot,
                args.limit,
                args.resolution,
                args.samples,
                args.engine,
                [value for value in args.views.split(",") if value],
                args.batch_size,
                args.workers,
                args.export_workers,
                args.reuse_compatible,
            )
            print(json.dumps(result, indent=2))
            return 1 if result["failures"] else 0
        elif args.command == "caption-export":
            result = caption_jobs(
                database,
                (args.file or output / "caption-jobs.jsonl").resolve(),
                not args.include_unrendered,
                args.limit,
            )
            print(json.dumps(result, indent=2))
        elif args.command == "serve":
            serve(database, output, args.host, args.port, args.open)
        return 0
    except ItemDatabaseError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
