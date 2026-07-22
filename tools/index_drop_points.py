#!/usr/bin/env python3
"""Build and query a checked index of vanilla DropPoint devices.

The world scan is authoritative for physical entities.  Cooked mappin data is
separate evidence that a position participates in a vanilla map marker; it is
not proof that the kiosk is reachable on foot.  Runtime accessibility is kept
in a small reviewed curation file and is the only source for the default
random-selection pool.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import sys
import tempfile
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "reference" / "world" / "drop-points.json"
DEFAULT_CURATION = ROOT / "reference" / "world" / "drop-points-curation.json"
DROP_POINT_TEMPLATE = r"base\gameplay\devices\drop_points\drop_point.ent"
WORLD_SECTOR_PREFIX = r"base\worlds\03_night_city\_compiled\default"
POSITION_PRECISION = 3


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


def walk(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def vector(value: dict[str, Any] | None, *, quaternion: bool = False) -> dict[str, float] | None:
    if not isinstance(value, dict):
        return None
    keys = ("i", "j", "k", "r") if quaternion else ("X", "Y", "Z")
    if not all(isinstance(value.get(key), (int, float)) for key in keys):
        return None
    labels = ("i", "j", "k", "r") if quaternion else ("x", "y", "z")
    return {label: float(value[key]) for label, key in zip(labels, keys)}


def position_key(value: dict[str, float] | None) -> tuple[float, float, float] | None:
    if value is None:
        return None
    return tuple(round(value[key], POSITION_PRECISION) for key in ("x", "y", "z"))


def yaw_degrees(orientation: dict[str, float] | None) -> float | None:
    if orientation is None:
        return None
    i, j, k, r = (orientation[key] for key in ("i", "j", "k", "r"))
    yaw = math.degrees(math.atan2(2.0 * (r * k + i * j), 1.0 - 2.0 * (j * j + k * k)))
    return round(yaw % 360.0, 6)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def sector_resource(path: Path) -> str:
    name = path.name.removesuffix(".json")
    return f"{WORLD_SECTOR_PREFIX}\\{name}"


def area_from_ref(node_ref: str) -> tuple[str, str]:
    parts = node_ref.removeprefix("$/03_night_city/").split("/")
    region = "unknown"
    area = "unknown"
    if parts:
        token = parts[0].lstrip("#")
        if token.startswith("c_"):
            region = token[2:]
        elif token == "se1":
            region = "badlands"
        else:
            region = token
    for index, token in enumerate(parts):
        if "drop_points_prefab" in token and index > 0:
            area = parts[index - 1].lstrip("#")
            break
    if "loc_megabuilding_a" in node_ref:
        area = "little_china_megabuilding"
    return region, area


def load_mappin_evidence(path: Path) -> tuple[dict[tuple[float, float, float], list[int]], dict[tuple[float, float, float], list[int]], int]:
    document = read_json(path)
    root = document.get("Data", {}).get("RootChunk", {})
    individual: dict[tuple[float, float, float], list[int]] = {}
    for entry in root.get("cookedData", []):
        key = position_key(vector(entry.get("position")))
        if key is not None:
            individual.setdefault(key, []).append(int(entry.get("journalPathHash", 0)))
    multi: dict[tuple[float, float, float], list[int]] = {}
    for entry in root.get("cookedMultiData", []):
        journal_hash = int(entry.get("journalPathHash", 0))
        for item in entry.get("positions", []):
            key = position_key(vector(item))
            if key is not None:
                multi.setdefault(key, []).append(journal_hash)
    return individual, multi, int(document.get("Data", {}).get("Version", 0))


def load_journal_refs(root: Path) -> dict[str, list[str]]:
    references: dict[str, set[str]] = {}
    for path in sorted(root.glob("*.json")):
        document = read_json(path)
        for item in walk(document):
            value = scalar(item)
            if not isinstance(value, str) or not value.startswith(("$/", "#")):
                continue
            lowered = value.casefold()
            if "drop_point" not in lowered and "droppoint" not in lowered:
                continue
            references.setdefault(value, set()).add(path.name)
    return {key: sorted(value) for key, value in sorted(references.items())}


def matching_journal_refs(node_ref: str, references: dict[str, list[str]]) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []
    for reference, files in references.items():
        exact = reference == node_ref
        alias = reference.startswith("#") and (node_ref.endswith("/" + reference) or node_ref.endswith(";" + reference))
        if exact or alias:
            matches.append({"reference": reference, "files": files})
    return matches


def drop_point_rows(sector_root: Path) -> tuple[list[dict[str, Any]], list[str]]:
    rows: list[dict[str, Any]] = []
    warnings: list[str] = []
    for path in sorted(sector_root.rglob("*.streamingsector.json")):
        if path.stat().st_size == 0:
            warnings.append(f"empty serialized sector: {path.name}")
            continue
        document = read_json(path)
        root = document.get("Data", {}).get("RootChunk", {})
        nodes = root.get("nodes", [])
        node_data = root.get("nodeData", {})
        records = node_data.get("Data", []) if isinstance(node_data, dict) else node_data
        records_by_index = {
            item.get("NodeIndex"): item for item in records if isinstance(item, dict) and isinstance(item.get("NodeIndex"), int)
        }
        for index, handle in enumerate(nodes):
            data = handle.get("Data", {}) if isinstance(handle, dict) else {}
            template = scalar((data.get("entityTemplate") or {}).get("DepotPath"))
            if template != DROP_POINT_TEMPLATE:
                continue
            placement = records_by_index.get(index, {})
            node_ref = scalar(placement.get("QuestPrefabRefHash"))
            if not isinstance(node_ref, str) or not node_ref:
                warnings.append(f"DropPoint without a string NodeRef: {path.name} node {index}")
                continue
            position = vector(placement.get("Position"))
            orientation = vector(placement.get("Orientation"), quaternion=True)
            region, area = area_from_ref(node_ref)
            rows.append(
                {
                    "node_ref": node_ref,
                    "debug_name": str(scalar(data.get("debugName")) or ""),
                    "sector": sector_resource(path),
                    "node_index": index,
                    "position": position,
                    "orientation": orientation,
                    "yaw_degrees": yaw_degrees(orientation),
                    "entity_template": template,
                    "appearance": str(scalar(data.get("appearanceName")) or ""),
                    "region": region,
                    "area": area,
                }
            )
    return rows, warnings


def build_index(
    sector_root: Path,
    mappins_path: Path,
    journal_root: Path,
    curation_path: Path,
) -> dict[str, Any]:
    curation = read_json(curation_path)
    rows, warnings = drop_point_rows(sector_root)
    rows.extend(curation.get("fallback_nodes", []))
    annotations = curation.get("annotations", {})
    individual, multi, mappin_version = load_mappin_evidence(mappins_path)
    journal_refs = load_journal_refs(journal_root)

    seen: set[str] = set()
    for row in rows:
        node_ref = row["node_ref"]
        if node_ref in seen:
            raise ValueError(f"duplicate DropPoint NodeRef: {node_ref}")
        seen.add(node_ref)
        key = position_key(row.get("position"))
        individual_hashes = sorted(set(individual.get(key, []))) if key is not None else []
        multi_hashes = sorted(set(multi.get(key, []))) if key is not None else []
        annotation = annotations.get(node_ref, {})
        accessibility = annotation.get("accessibility", "unvetted")
        runtime_map_label = annotation.get("runtime_map_label", "unvetted")
        mappin_backed = bool(individual_hashes or multi_hashes)
        if runtime_map_label == "verified":
            map_label_status = "verified"
        elif mappin_backed:
            map_label_status = "cooked_mappin"
        else:
            map_label_status = "unverified"
        row["mappin_evidence"] = {
            "backed": mappin_backed,
            "individual_journal_hashes": individual_hashes,
            "multi_journal_hashes": multi_hashes,
            "status": map_label_status,
        }
        row["journal_references"] = matching_journal_refs(node_ref, journal_refs)
        row["accessibility"] = accessibility
        row["selection_eligible"] = accessibility == "verified" and map_label_status in {
            "verified",
            "cooked_mappin",
        }
        if annotation.get("notes"):
            row["curation_notes"] = annotation["notes"]

    rows.sort(key=lambda item: item["node_ref"])
    total = len(rows)
    backed = sum(bool(item["mappin_evidence"]["backed"]) for item in rows)
    multi_backed = sum(bool(item["mappin_evidence"]["multi_journal_hashes"]) for item in rows)
    verified = sum(item["accessibility"] == "verified" for item in rows)
    rejected = sum(item["accessibility"] == "rejected" for item in rows)
    eligible = sum(bool(item["selection_eligible"]) for item in rows)
    missing_orientation = sum(item.get("orientation") is None for item in rows)
    return {
        "schema_version": 1,
        "generated_by": "tools/index_drop_points.py",
        "summary": {
            "physical_entities": total,
            "sectors": len({item["sector"] for item in rows}),
            "mappin_backed_entities": backed,
            "canonical_multi_mappin_entities": multi_backed,
            "runtime_verified_accessible": verified,
            "rejected": rejected,
            "selection_eligible": eligible,
            "missing_orientation": missing_orientation,
        },
        "provenance": {
            "world_source_archive": r"archive\pc\content\basegame_3_nightcity.archive",
            "world_scan": f"all .streamingsector files filtered by entity template {DROP_POINT_TEMPLATE}",
            "mappins_resource": r"base\worlds\03_night_city\_compiled\default\03_night_city.mappins",
            "mappins_cr2w_version": mappin_version,
            "mappins_json_sha256": sha256(mappins_path),
            "journal_reference_root": str(journal_root.relative_to(ROOT)) if journal_root.is_relative_to(ROOT) else str(journal_root),
            "curation": str(curation_path.relative_to(ROOT)) if curation_path.is_relative_to(ROOT) else str(curation_path),
        },
        "warnings": sorted(set(warnings + curation.get("warnings", []))),
        "drop_points": rows,
    }


def filtered_rows(manifest: dict[str, Any], *, include_unvetted: bool, region: str | None, area: str | None) -> list[dict[str, Any]]:
    rows = manifest.get("drop_points", [])
    if not include_unvetted:
        rows = [row for row in rows if row.get("selection_eligible")]
    if region:
        rows = [row for row in rows if row.get("region", "").casefold() == region.casefold()]
    if area:
        rows = [row for row in rows if row.get("area", "").casefold() == area.casefold()]
    return rows


def command_build(args: argparse.Namespace) -> None:
    manifest = build_index(args.sectors, args.mappins, args.journals, args.curation)
    write_json(args.output, manifest)
    print(json.dumps(manifest["summary"], indent=2))
    print(f"Wrote {args.output}")


def command_list(args: argparse.Namespace) -> None:
    manifest = read_json(args.manifest)
    rows = filtered_rows(manifest, include_unvetted=args.include_unvetted, region=args.region, area=args.area)
    if args.json:
        print(json.dumps(rows, indent=2))
        return
    for row in rows:
        position = row.get("position") or {}
        print(
            f"{row['node_ref']} | {row['accessibility']} | {row['mappin_evidence']['status']} | "
            f"({position.get('x')}, {position.get('y')}, {position.get('z')})"
        )


def command_choose(args: argparse.Namespace) -> None:
    manifest = read_json(args.manifest)
    rows = filtered_rows(manifest, include_unvetted=args.include_unvetted, region=args.region, area=args.area)
    if not rows:
        raise SystemExit("no drop points match the requested selection policy")
    selected = random.Random(args.seed).choice(rows)
    print(json.dumps(selected, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    build = subparsers.add_parser("build", help="Build the manifest from serialized vanilla sectors.")
    build.add_argument("--sectors", type=Path, required=True, help="Directory containing serialized vanilla sector JSON.")
    build.add_argument("--mappins", type=Path, required=True, help="Serialized 03_night_city.mappins JSON.")
    build.add_argument("--journals", type=Path, default=ROOT / "reference" / "journal")
    build.add_argument("--curation", type=Path, default=DEFAULT_CURATION)
    build.add_argument("--output", type=Path, default=DEFAULT_MANIFEST)
    build.set_defaults(func=command_build)

    listing = subparsers.add_parser("list", help="List vetted candidates, or the full physical index.")
    listing.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    listing.add_argument("--include-unvetted", action="store_true", help="Include unvetted and rejected physical entities.")
    listing.add_argument("--region")
    listing.add_argument("--area")
    listing.add_argument("--json", action="store_true")
    listing.set_defaults(func=command_list)

    choose = subparsers.add_parser("choose", help="Choose one deterministic random candidate.")
    choose.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    choose.add_argument("--seed", default="ghostline")
    choose.add_argument("--include-unvetted", action="store_true", help="Allow unsafe/unreviewed physical entities.")
    choose.add_argument("--region")
    choose.add_argument("--area")
    choose.set_defaults(func=command_choose)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
