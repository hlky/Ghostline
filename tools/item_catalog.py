"""Tweak parsing, appearance indexing and the SQLite equipment catalog."""

from __future__ import annotations
import json
import os
import re
import sqlite3
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

from item_common import (
    ATTRIBUTE_BLOCK,
    EQUIPMENT_SLOTS,
    FRAME_LABELS,
    FRAME_SUFFIX,
    FRAME_TOKEN,
    ItemDatabaseError,
    LOC_KEY,
    PACKAGE_LINE,
    PRIMARY_COMPONENT_TYPES,
    QUOTED_STRING,
    RECORD_HEADER,
    ROOT,
    SCHEMA_VERSION,
    STRING_PROPERTY,
    TAGS_PROPERTY,
    read_json,
    sha1_text,
    write_json,
)


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
        regex = r"appearances.*player.*items.*\.app$"
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
