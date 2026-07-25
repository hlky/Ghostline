#!/usr/bin/env python3
"""Discover, normalize, curate, and select reusable Night City world assets.

Binary discovery is deliberately separate from detailed CR2W-JSON indexing.
The former cheaply identifies every sector that contains a category token; the
latter records concrete node placements after selected sectors are serialized
with ghostline-red. Only reviewed, quest-safe records are eligible for default
selection.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import shutil
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

from ghostline_red import DEFAULT_RED_CLI, DEFAULT_RED_SCHEMA, serialize as serialize_cr2w


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DISCOVERY = ROOT / "reference" / "world" / "world-sector-candidates.json"
DEFAULT_CATALOG = ROOT / "reference" / "world" / "world-assets.json"
DEFAULT_CURATION = ROOT / "reference" / "world" / "world-assets-curation.json"
WORLD_SECTOR_PREFIX = r"base\worlds\03_night_city\_compiled\default"


# Tokens must be ASCII strings present in cooked CR2W name/path tables.
# Detailed classification below is stricter and operates on concrete nodes.
DISCOVERY_TOKENS: dict[str, tuple[bytes, ...]] = {
    "terminal": (b"computer", b"terminal", b"dataterm", b"laptop"),
    "access_point": (b"access_point", b"accesspoint", b"antenna_access"),
    "antenna": (b"antenna", b"satellite", b"sat_dish", b"satdish"),
    "door_lock": (b"door", b"gate", b"shutter", b"restraint", b"cage"),
    "plant_target": (b"junction", b"router", b"fuse", b"electrical", b"switch"),
    "drop_point": (b"drop_point", b"droppoint"),
    "loot_anchor": (b"loot", b"weapon_case", b"container"),
    "vehicle": (b"vehicle", b"parking", b"garage"),
}

FUNCTIONAL_NODE_TYPES = {
    "worldDeviceNode",
    "worldEntityNode",
    "worldDynamicEntityNode",
    "worldVehicleNode",
}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


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


def scalar(value: Any) -> Any:
    if isinstance(value, dict) and "$value" in value:
        return value["$value"]
    return value


def vector(value: Any, keys: tuple[str, ...]) -> dict[str, float] | None:
    if not isinstance(value, dict) or not all(isinstance(value.get(key), (int, float)) for key in keys):
        return None
    labels = ("x", "y", "z") if keys == ("X", "Y", "Z") else ("i", "j", "k", "r")
    return {label: float(value[key]) for label, key in zip(labels, keys)}


def yaw_degrees(orientation: dict[str, float] | None) -> float | None:
    if orientation is None:
        return None
    i, j, k, r = (orientation[key] for key in ("i", "j", "k", "r"))
    yaw = math.degrees(math.atan2(2.0 * (r * k + i * j), 1.0 - 2.0 * (j * j + k * k)))
    return round(yaw % 360.0, 6)


def node_resource(data: dict[str, Any]) -> str:
    for key in ("entityTemplate", "mesh", "resource", "cookedInstanceData"):
        candidate = data.get(key)
        if isinstance(candidate, dict):
            path = scalar(candidate.get("DepotPath"))
            if isinstance(path, str) and path:
                return path
    return ""


def sector_resource(path: Path) -> str:
    return f"{WORLD_SECTOR_PREFIX}\\{path.name.removesuffix('.json')}"


def area_from_ref(node_ref: str) -> tuple[str, str]:
    parts = node_ref.removeprefix("$/03_night_city/").split("/")
    region = "unknown"
    area = "unknown"
    if parts:
        token = parts[0].lstrip("#")
        region = token[2:] if token.startswith("c_") else token
    if len(parts) > 1:
        candidate = parts[1].lstrip("#")
        if candidate and not candidate.startswith(("loc_", "base_", "$")):
            area = candidate
    for token in parts[1:]:
        if area != "unknown":
            break
        cleaned = token.lstrip("#")
        if cleaned.startswith("loc_"):
            bits = cleaned.split("_")
            if len(bits) >= 3:
                area = "_".join(bits[1:3])
                break
    return region or "unknown", area or "unknown"


def discover_categories(blob: bytes) -> list[str]:
    lowered = blob.lower()
    return [
        category
        for category, tokens in DISCOVERY_TOKENS.items()
        if any(token in lowered for token in tokens)
    ]


def relative_sector_path(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.name


def discover_binary_sectors(binary_root: Path) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    counts: Counter[str] = Counter()
    for path in sorted(binary_root.rglob("*.streamingsector")):
        categories = discover_categories(path.read_bytes())
        if not categories:
            continue
        counts.update(categories)
        rows.append(
            {
                "path": relative_sector_path(path, binary_root),
                "categories": categories,
                "size": path.stat().st_size,
            }
        )
    return {
        "schema_version": 1,
        "generated_by": "tools/world_asset_catalog.py discover",
        "binary_root_hint": str(binary_root),
        "tokens": {
            category: [token.decode("ascii") for token in tokens]
            for category, tokens in DISCOVERY_TOKENS.items()
        },
        "summary": {
            "candidate_sectors": len(rows),
            "category_sector_counts": dict(sorted(counts.items())),
        },
        "sectors": rows,
    }


def selected_discovery_rows(
    discovery: dict[str, Any],
    categories: set[str],
    *,
    limit_per_category: int | None,
    seed: str,
) -> list[dict[str, Any]]:
    rows = list(discovery.get("sectors", []))
    if not categories:
        categories = set(DISCOVERY_TOKENS)
    selected: dict[str, dict[str, Any]] = {}
    rng = random.Random(seed)
    for category in sorted(categories):
        candidates = [row for row in rows if category in row.get("categories", [])]
        candidates.sort(key=lambda row: row["path"])
        if limit_per_category is not None and len(candidates) > limit_per_category:
            candidates = rng.sample(candidates, limit_per_category)
        for row in candidates:
            selected[row["path"]] = row
    return [selected[key] for key in sorted(selected)]


def stage_discovered_sectors(
    discovery_path: Path,
    binary_root: Path,
    staging: Path,
    categories: set[str],
    limit_per_category: int | None,
    seed: str,
) -> list[Path]:
    rows = selected_discovery_rows(
        read_json(discovery_path),
        categories,
        limit_per_category=limit_per_category,
        seed=seed,
    )
    staged: list[Path] = []
    for row in rows:
        source = binary_root / Path(row["path"])
        if not source.is_file():
            raise FileNotFoundError(f"discovered sector no longer exists: {source}")
        target = staging / Path(row["path"])
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        staged.append(target)
    return staged


def serialize_staging(
    staging: Path,
    output: Path,
    red_cli: Path,
    schema: Path,
) -> None:
    for resource in staging.rglob("*.streamingsector"):
        relative = resource.relative_to(staging)
        serialize_cr2w(
            resource,
            output / Path(f"{relative}.json"),
            red_cli=red_cli,
            schema=schema,
        )


def classification_text(data: dict[str, Any], node_ref: str, resource: str) -> str:
    values = [
        resource,
        str(scalar(data.get("debugName")) or ""),
        node_ref,
        str(scalar(data.get("appearanceName")) or ""),
        str(scalar(data.get("recordID")) or ""),
    ]
    return " ".join(values).casefold()


def classify_node(node_type: str, text: str) -> tuple[list[str], list[str]]:
    categories: set[str] = set()
    tags: set[str] = set()
    functional = node_type in FUNCTIONAL_NODE_TYPES

    if functional and any(token in text for token in ("computer", "terminal", "dataterm", "laptop")):
        categories.add("terminal")
        tags.add("terminal_candidate")
        if (
            any(token in text for token in ("computer", "terminal", "dataterm"))
            and r"fast_travel" not in text
            and "data_term_1.ent" not in text
        ):
            tags.add("document_host_candidate")

    if functional and any(token in text for token in ("access_point", "accesspoint", "antenna_access")):
        categories.add("access_point")
        tags.update(("hackable_candidate", "plant_target_candidate"))

    if any(token in text for token in ("antenna", "satellite", "sat_dish", "satdish")):
        categories.add("antenna")
        tags.add("antenna_anchor_candidate")
        if not functional:
            tags.add("visual_anchor_only")

    if functional and any(token in text for token in ("door", "gate", "shutter", "cage", "restraint")):
        categories.add("door_lock")
        tags.add("release_target_candidate")

    if functional and any(
        token in text
        for token in ("junction", "router", "fuse", "electrical", "switch", "antenna", "access_point")
    ):
        categories.add("plant_target")
        tags.add("plant_target_candidate")

    if functional and any(token in text for token in ("drop_point", "droppoint")):
        categories.add("drop_point")
        tags.update(("delivery_target_candidate", "walkable_anchor_candidate"))

    if functional and any(
        token in text
        for token in (r"gameplay\loot", "loot_container", "weapon_case", "lootcontainer")
    ):
        categories.add("loot_anchor")
        tags.update(
            (
                "loot_container",
                "walkable_anchor_candidate",
                "npc_staging_candidate",
                "defend_staging_candidate",
            )
        )

    if (
        node_type == "worldVehicleNode"
        or (functional and any(token in text for token in (r"base\vehicles", "vehicle_", r"\vehicles\\")))
    ):
        categories.add("vehicle")
        tags.update(("vehicle_candidate", "parking_anchor_candidate"))

    return sorted(categories), sorted(tags)


def iter_sector_assets(path: Path) -> Iterable[dict[str, Any]]:
    document = read_json(path)
    root = document.get("Data", {}).get("RootChunk", {})
    nodes = root.get("nodes", [])
    raw_records = root.get("nodeData", {})
    records = raw_records.get("Data", []) if isinstance(raw_records, dict) else raw_records
    records_by_index: dict[int, list[dict[str, Any]]] = {}
    for record in records if isinstance(records, list) else []:
        if isinstance(record, dict) and isinstance(record.get("NodeIndex"), int):
            records_by_index.setdefault(record["NodeIndex"], []).append(record)
    for index, handle in enumerate(nodes if isinstance(nodes, list) else []):
        data = handle.get("Data", {}) if isinstance(handle, dict) else {}
        node_type = str(data.get("$type") or "")
        resource = node_resource(data)
        for placement_index, placement in enumerate(records_by_index.get(index, [{}])):
            node_ref = str(scalar(placement.get("QuestPrefabRefHash")) or "")
            if node_ref == "0":
                node_ref = ""
            categories, tags = classify_node(node_type, classification_text(data, node_ref, resource))
            if not categories:
                continue
            position = vector(placement.get("Position"), ("X", "Y", "Z"))
            orientation = vector(placement.get("Orientation"), ("i", "j", "k", "r"))
            region, area = area_from_ref(node_ref)
            identity = (
                f"{node_ref}|{sector_resource(path)}:{index}:{placement_index}"
            )
            stable_id = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:16]
            yield {
                "id": stable_id,
                "categories": categories,
                "tags": tags,
                "resource": resource,
                "sector": sector_resource(path),
                "source_json": path.name,
                "node_index": index,
                "placement_index": placement_index,
                "node_type": node_type,
                "debug_name": str(scalar(data.get("debugName")) or ""),
                "node_ref": node_ref,
                "position": position,
                "orientation": orientation,
                "yaw_degrees": yaw_degrees(orientation),
                "scale": vector(placement.get("Scale"), ("X", "Y", "Z")),
                "region": region,
                "area": area,
            }


def apply_curation(row: dict[str, Any], curation: dict[str, Any]) -> None:
    annotations = curation.get("annotations", {})
    annotation = annotations.get(row["id"]) or annotations.get(row["node_ref"]) or {}
    row["review"] = {
        "accessibility": annotation.get("accessibility", "unvetted"),
        "quest_safety": annotation.get("quest_safety", "unvetted"),
        "interior": annotation.get("interior", "unvetted"),
    }
    if annotation.get("add_tags"):
        row["tags"] = sorted(set(row["tags"]) | set(annotation["add_tags"]))
    if annotation.get("remove_tags"):
        row["tags"] = sorted(set(row["tags"]) - set(annotation["remove_tags"]))
    if annotation.get("notes"):
        row["review"]["notes"] = annotation["notes"]
    row["selection_eligible"] = (
        row["review"]["accessibility"] == "verified"
        and row["review"]["quest_safety"] == "verified"
    )


def build_catalog(sector_root: Path, curation_path: Path) -> dict[str, Any]:
    curation = read_json(curation_path)
    by_identity: dict[tuple[str, str], dict[str, Any]] = {}
    warnings: list[str] = []
    scanned = 0
    for path in sorted(sector_root.rglob("*.streamingsector.json")):
        if path.stat().st_size == 0:
            warnings.append(f"empty serialized sector: {path.name}")
            continue
        scanned += 1
        for row in iter_sector_assets(path):
            key = (row["sector"], row["id"])
            by_identity[key] = row
    rows = list(by_identity.values())
    for row in rows:
        apply_curation(row, curation)
    validate_catalog_rows(rows)
    rows.sort(key=lambda row: (row["region"], row["area"], row["sector"], row["node_index"], row["placement_index"]))
    category_counts = Counter(category for row in rows for category in row["categories"])
    tag_counts = Counter(tag for row in rows for tag in row["tags"])
    return {
        "schema_version": 1,
        "generated_by": "tools/world_asset_catalog.py build",
        "summary": {
            "serialized_sectors_scanned": scanned,
            "assets": len(rows),
            "selection_eligible": sum(bool(row["selection_eligible"]) for row in rows),
            "category_counts": dict(sorted(category_counts.items())),
            "tag_counts": dict(sorted(tag_counts.items())),
            "missing_positions": sum(row["position"] is None for row in rows),
        },
        "curation": str(curation_path),
        "warnings": sorted(set(warnings + list(curation.get("warnings", [])))),
        "assets": rows,
    }


def validate_catalog_rows(rows: list[dict[str, Any]]) -> None:
    ids: set[str] = set()
    allowed_review = {"unvetted", "verified", "rejected"}
    for row in rows:
        if row["id"] in ids:
            raise ValueError(f"duplicate world asset id: {row['id']}")
        ids.add(row["id"])
        if not row["categories"]:
            raise ValueError(f"world asset has no category: {row['id']}")
        if row["review"]["accessibility"] not in allowed_review:
            raise ValueError(f"invalid accessibility review for {row['id']}")
        if row["review"]["quest_safety"] not in allowed_review:
            raise ValueError(f"invalid quest-safety review for {row['id']}")
        if row["selection_eligible"] and row["position"] is None:
            raise ValueError(f"selection-eligible asset has no position: {row['id']}")


def distance_from(row: dict[str, Any], near: tuple[float, float, float]) -> float:
    position = row.get("position")
    if not isinstance(position, dict):
        return math.inf
    return math.dist(near, tuple(float(position[key]) for key in ("x", "y", "z")))


def filter_assets(
    catalog: dict[str, Any],
    *,
    categories: set[str],
    tags: set[str],
    region: str | None,
    area: str | None,
    near: tuple[float, float, float] | None,
    radius: float | None,
    include_unvetted: bool,
) -> list[dict[str, Any]]:
    rows = list(catalog.get("assets", []))
    if not include_unvetted:
        rows = [row for row in rows if row.get("selection_eligible")]
    if categories:
        rows = [row for row in rows if categories.issubset(set(row.get("categories", [])))]
    if tags:
        rows = [row for row in rows if tags.issubset(set(row.get("tags", [])))]
    if region:
        rows = [row for row in rows if str(row.get("region", "")).casefold() == region.casefold()]
    if area:
        rows = [row for row in rows if str(row.get("area", "")).casefold() == area.casefold()]
    if near is not None:
        for row in rows:
            row["distance"] = round(distance_from(row, near), 3)
        rows = [row for row in rows if radius is None or row["distance"] <= radius]
        rows.sort(key=lambda row: (row["distance"], row["id"]))
    return rows


def parse_near(value: str) -> tuple[float, float, float]:
    parts = value.split(",")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("--near must be X,Y,Z")
    try:
        return tuple(float(part) for part in parts)  # type: ignore[return-value]
    except ValueError as error:
        raise argparse.ArgumentTypeError("--near must contain three numbers") from error


def add_filters(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--category", action="append", default=[])
    parser.add_argument("--tag", action="append", default=[])
    parser.add_argument("--region")
    parser.add_argument("--area")
    parser.add_argument("--near", type=parse_near)
    parser.add_argument("--radius", type=float)
    parser.add_argument("--include-unvetted", action="store_true")


def filtered_from_args(args: argparse.Namespace) -> list[dict[str, Any]]:
    return filter_assets(
        read_json(args.catalog),
        categories=set(args.category),
        tags=set(args.tag),
        region=args.region,
        area=args.area,
        near=args.near,
        radius=args.radius,
        include_unvetted=args.include_unvetted,
    )


def command_discover(args: argparse.Namespace) -> None:
    manifest = discover_binary_sectors(args.binaries)
    write_json(args.output, manifest)
    print(json.dumps({"output": str(args.output), **manifest["summary"]}, indent=2))


def command_serialize(args: argparse.Namespace) -> None:
    with tempfile.TemporaryDirectory(prefix="ghostline-world-assets-") as temporary:
        staging = Path(temporary)
        staged = stage_discovered_sectors(
            args.discovery,
            args.binaries,
            staging,
            set(args.category),
            args.limit_per_category,
            args.seed,
        )
        serialize_staging(staging, args.output, args.red_cli, args.schema)
    print(json.dumps({"staged": len(staged), "output": str(args.output)}, indent=2))


def command_build(args: argparse.Namespace) -> None:
    catalog = build_catalog(args.sectors, args.curation)
    write_json(args.output, catalog)
    print(json.dumps({"output": str(args.output), **catalog["summary"]}, indent=2))


def command_list(args: argparse.Namespace) -> None:
    print(json.dumps(filtered_from_args(args), indent=2))


def command_choose(args: argparse.Namespace) -> None:
    rows = filtered_from_args(args)
    if not rows:
        raise SystemExit("no world assets match the requested selection policy")
    selected = random.Random(args.seed).choice(rows)
    if args.format == "placement":
        selected = {
            "asset_id": selected["id"],
            "categories": selected["categories"],
            "tags": selected["tags"],
            "origin": selected["position"],
            "yaw": selected["yaw_degrees"],
            "native_node_ref": selected["node_ref"],
            "source_sector": selected["sector"],
            "resource": selected["resource"],
        }
    print(json.dumps(selected, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    discover = subparsers.add_parser("discover", help="Scan cooked binary sectors for category tokens.")
    discover.add_argument("--binaries", type=Path, required=True)
    discover.add_argument("--output", type=Path, default=DEFAULT_DISCOVERY)
    discover.set_defaults(func=command_discover)

    serialize = subparsers.add_parser("serialize", help="Serialize discovered candidate sectors with ghostline-red.")
    serialize.add_argument("--discovery", type=Path, default=DEFAULT_DISCOVERY)
    serialize.add_argument("--binaries", type=Path, required=True)
    serialize.add_argument("--output", type=Path, required=True)
    serialize.add_argument("--category", action="append", choices=sorted(DISCOVERY_TOKENS), default=[])
    serialize.add_argument("--limit-per-category", type=int)
    serialize.add_argument("--seed", default="ghostline")
    serialize.add_argument("--red-cli", type=Path, default=DEFAULT_RED_CLI)
    serialize.add_argument("--schema", type=Path, default=DEFAULT_RED_SCHEMA)
    serialize.set_defaults(func=command_serialize)

    build = subparsers.add_parser("build", help="Build the normalized catalog from serialized sectors.")
    build.add_argument("--sectors", type=Path, required=True)
    build.add_argument("--curation", type=Path, default=DEFAULT_CURATION)
    build.add_argument("--output", type=Path, default=DEFAULT_CATALOG)
    build.set_defaults(func=command_build)

    listing = subparsers.add_parser("list", help="List matching catalog records.")
    listing.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    add_filters(listing)
    listing.set_defaults(func=command_list)

    choose = subparsers.add_parser("choose", help="Choose one deterministic matching record.")
    choose.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    choose.add_argument("--seed", default="ghostline")
    choose.add_argument("--format", choices=("record", "placement"), default="record")
    add_filters(choose)
    choose.set_defaults(func=command_choose)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
