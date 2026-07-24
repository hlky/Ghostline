#!/usr/bin/env python3
"""Build and query reusable world-placement indexes from serialized sectors.

This complements ``explore_world.py``: the explorer answers one-off questions,
while this tool records every placed instance of one or more exact depot paths
so quest authors can choose terrain or clone a visual/device family later.
Binary pre-filtering and WolvenKit serialization remain separate, deliberate
steps because a full Night City serialization is unnecessarily expensive.
"""

from __future__ import annotations

import argparse
import json
import math
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
# Legacy exact-resource indexes have a different schema from the normalized
# multi-family catalog produced by world_asset_catalog.py. Keep their defaults
# separate so this helper cannot overwrite the canonical catalog.
DEFAULT_MANIFEST = ROOT / "reference" / "world" / "world-assets-exact.json"
WORLD_SECTOR_PREFIX = r"base\worlds\03_night_city\_compiled\default"


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


def node_resource(data: dict[str, Any]) -> str:
    template = data.get("entityTemplate")
    if isinstance(template, dict):
        path = scalar(template.get("DepotPath"))
        if isinstance(path, str) and path:
            return path
    for key in ("mesh", "resource", "cookedInstanceData"):
        candidate = data.get(key)
        if isinstance(candidate, dict):
            path = scalar(candidate.get("DepotPath"))
            if isinstance(path, str) and path:
                return path
    return ""


def sector_resource(path: Path) -> str:
    return f"{WORLD_SECTOR_PREFIX}\\{path.name.removesuffix('.json')}"


def asset_rows(sector_root: Path, resources: set[str]) -> tuple[list[dict[str, Any]], list[str]]:
    wanted = {item.casefold() for item in resources}
    rows: list[dict[str, Any]] = []
    warnings: list[str] = []
    for path in sorted(sector_root.rglob("*.streamingsector.json")):
        if path.stat().st_size == 0:
            warnings.append(f"empty serialized sector: {path.name}")
            continue
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
            resource = node_resource(data)
            if resource.casefold() not in wanted:
                continue
            placements = records_by_index.get(index, [{}])
            for placement_index, placement in enumerate(placements):
                rows.append(
                    {
                        "resource": resource,
                        "sector": sector_resource(path),
                        "source_json": path.name,
                        "node_index": index,
                        "placement_index": placement_index,
                        "node_type": str(data.get("$type") or ""),
                        "debug_name": str(scalar(data.get("debugName")) or ""),
                        "node_ref": str(scalar(placement.get("QuestPrefabRefHash")) or ""),
                        "position": vector(placement.get("Position"), ("X", "Y", "Z")),
                        "orientation": vector(placement.get("Orientation"), ("i", "j", "k", "r")),
                        "scale": vector(placement.get("Scale"), ("X", "Y", "Z")),
                    }
                )
    return rows, warnings


def build_index(sector_root: Path, resources: set[str]) -> dict[str, Any]:
    rows, warnings = asset_rows(sector_root, resources)
    rows.sort(
        key=lambda row: (
            row["resource"].casefold(),
            row["sector"].casefold(),
            row["node_index"],
            row["placement_index"],
        )
    )
    return {
        "schema_version": 1,
        "resources": sorted(resources, key=str.casefold),
        "summary": {
            "instances": len(rows),
            "sectors": len({row["sector"] for row in rows}),
            "resources": len({row["resource"] for row in rows}),
            "missing_positions": sum(row["position"] is None for row in rows),
        },
        "instances": rows,
        "warnings": warnings,
    }


def filtered_rows(
    manifest: dict[str, Any],
    *,
    resource: str | None,
    near: tuple[float, float, float] | None,
    radius: float | None,
) -> list[dict[str, Any]]:
    rows = list(manifest.get("instances", []))
    if resource:
        token = resource.casefold()
        rows = [row for row in rows if token in str(row.get("resource", "")).casefold()]
    if near is not None:
        def distance(row: dict[str, Any]) -> float:
            position = row.get("position")
            if not isinstance(position, dict):
                return math.inf
            return math.dist(near, tuple(float(position[key]) for key in ("x", "y", "z")))

        for row in rows:
            row["distance"] = round(distance(row), 3)
        rows = [row for row in rows if radius is None or row["distance"] <= radius]
        rows.sort(key=lambda row: row["distance"])
    return rows


def parse_near(value: str) -> tuple[float, float, float]:
    parts = value.split(",")
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("--near must be X,Y,Z")
    try:
        return tuple(float(part) for part in parts)  # type: ignore[return-value]
    except ValueError as error:
        raise argparse.ArgumentTypeError("--near must contain three numbers") from error


def command_build(args: argparse.Namespace) -> None:
    manifest = build_index(args.sectors, set(args.resource))
    write_json(args.output, manifest)
    print(json.dumps({"output": str(args.output), **manifest["summary"]}, indent=2))


def command_list(args: argparse.Namespace) -> None:
    rows = filtered_rows(
        read_json(args.manifest),
        resource=args.resource,
        near=args.near,
        radius=args.radius,
    )
    print(json.dumps(rows, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    build = subparsers.add_parser("build", help="Index exact resources in serialized vanilla sectors.")
    build.add_argument("--sectors", type=Path, required=True)
    build.add_argument("--resource", action="append", required=True, help="Exact depot path; repeat as needed.")
    build.add_argument("--output", type=Path, default=DEFAULT_MANIFEST)
    build.set_defaults(func=command_build)

    listing = subparsers.add_parser("list", help="Query an existing world-asset index.")
    listing.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    listing.add_argument("--resource", help="Case-insensitive depot-path substring.")
    listing.add_argument("--near", type=parse_near, help="Sort/filter by distance from X,Y,Z.")
    listing.add_argument("--radius", type=float)
    listing.set_defaults(func=command_list)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
