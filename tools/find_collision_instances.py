"""Find repeated collision actors in a serialized streaming sector.

World Inspector often identifies a visible prop through a collision actor
inside a much larger worldCollisionNode. This tool fingerprints the selected
actor by its collision-shape hashes and lists matching actors with world-space
transforms. Actor indices are zero-based, matching the inspected Ghostline
cache candidate (`Collision Actor: 36 / 64`).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


FIXED_POINT_SCALE = 131072.0


def scalar(value: Any, default: Any = None) -> Any:
    if isinstance(value, dict):
        return value.get("$value", default)
    return value if value is not None else default


def actor_hashes(actor: dict[str, Any]) -> set[str]:
    return {
        str(shape["Hash"])
        for shape in actor.get("Shapes", [])
        if shape.get("Hash") is not None
    }


def fixed_position(actor: dict[str, Any]) -> tuple[float, float, float]:
    position = actor["Position"]
    return tuple(float(position[axis]["Bits"]) / FIXED_POINT_SCALE for axis in ("x", "y", "z"))


def collision_nodes(document: dict[str, Any]):
    nodes = document["Data"]["RootChunk"]["nodes"]
    for node_index, wrapper in enumerate(nodes):
        node = wrapper.get("Data", {})
        if node.get("$type") == "worldCollisionNode":
            yield node_index, node


def fingerprint_hashes(
    document: dict[str, Any], debug_name: str, actor_index: int, source_prefab_hash: str | None
) -> set[str]:
    matches = []
    for node_index, node in collision_nodes(document):
        if scalar(node.get("debugName"), "") != debug_name:
            continue
        if source_prefab_hash is not None and str(node.get("sourcePrefabHash")) != source_prefab_hash:
            continue
        actors = node.get("compiledData", {}).get("Data", {}).get("Actors", [])
        if actor_index >= len(actors):
            raise SystemExit(
                f"Actor {actor_index} is outside {debug_name}'s {len(actors)} actors at node {node_index}."
            )
        matches.append(actor_hashes(actors[actor_index]))
    if not matches:
        raise SystemExit(f"Collision node not found: {debug_name}")
    hashes = set.union(*matches)
    if not hashes:
        raise SystemExit(f"Actor {actor_index} in {debug_name} has no collision shape hash.")
    return hashes


def find_matches(document: dict[str, Any], hashes: set[str]) -> list[dict[str, Any]]:
    rows = []
    for node_index, node in collision_nodes(document):
        debug_name = scalar(node.get("debugName"), "")
        source_hash = str(node.get("sourcePrefabHash", "0"))
        actors = node.get("compiledData", {}).get("Data", {}).get("Actors", [])
        for actor_index, actor in enumerate(actors):
            matched = sorted(actor_hashes(actor) & hashes)
            if not matched:
                continue
            x, y, z = fixed_position(actor)
            orientation = actor.get("Orientation", {})
            scale = actor.get("Scale", {})
            rows.append(
                {
                    "node_index": node_index,
                    "debug_name": debug_name,
                    "source_prefab_hash": source_hash,
                    "actor_index": actor_index,
                    "position": {"x": x, "y": y, "z": z},
                    "orientation": {
                        "i": orientation.get("i", 0),
                        "j": orientation.get("j", 0),
                        "k": orientation.get("k", 0),
                        "r": orientation.get("r", 1),
                    },
                    "scale": {
                        "x": scale.get("X", 1),
                        "y": scale.get("Y", 1),
                        "z": scale.get("Z", 1),
                    },
                    "shape_hashes": matched,
                }
            )
    return rows


def print_table(rows: list[dict[str, Any]]) -> None:
    columns = ("Node", "Actor", "Debug name", "Source prefab", "Position", "Shape hashes")
    rendered = []
    for row in rows:
        position = row["position"]
        rendered.append(
            (
                str(row["node_index"]),
                str(row["actor_index"]),
                row["debug_name"],
                row["source_prefab_hash"],
                f'{position["x"]:.4f}, {position["y"]:.4f}, {position["z"]:.4f}',
                ",".join(row["shape_hashes"]),
            )
        )
    widths = [len(column) for column in columns]
    for row in rendered:
        widths = [max(width, len(value)) for width, value in zip(widths, row)]
    print("  ".join(column.ljust(width) for column, width in zip(columns, widths)))
    print("  ".join("-" * width for width in widths))
    for row in rendered:
        print("  ".join(value.ljust(width) for value, width in zip(row, widths)))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", required=True, type=Path, help="Serialized .streamingsector.json")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--shape-hash", action="append", help="Collision shape hash; repeat as needed")
    source.add_argument("--debug-name", help="Collision node debug name used with --actor")
    parser.add_argument("--actor", type=int, help="Zero-based actor index for --debug-name")
    parser.add_argument("--source-prefab-hash", help="Disambiguate a repeated debug name")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.debug_name is not None and args.actor is None:
        raise SystemExit("--debug-name requires --actor")
    if args.actor is not None and args.debug_name is None:
        raise SystemExit("--actor requires --debug-name")
    document = json.loads(args.file.read_text(encoding="utf-8"))
    hashes = (
        {str(value) for value in args.shape_hash}
        if args.shape_hash
        else fingerprint_hashes(document, args.debug_name, args.actor, args.source_prefab_hash)
    )
    rows = find_matches(document, hashes)
    if args.json:
        print(json.dumps({"shape_hashes": sorted(hashes), "matches": rows}, indent=2))
    else:
        print(f"Shape hashes: {', '.join(sorted(hashes))}")
        print(f"Matches: {len(rows)}")
        print_table(rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
