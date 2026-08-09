#!/usr/bin/env python3
"""Discover likely quest-unused indoor locations from serialized world sectors.

This is an offline catalog builder. It does not import, invoke, or modify the
world-location capture pipeline. The generated JSON can be reviewed directly
or used as an input to a future capture-planning adapter.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from typing import Any, Iterable, Mapping


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SECTORS = ROOT / "converted/world-location-database/full-world/serialized-sectors"
DEFAULT_OUTPUT = ROOT / "generated/world-locations/indoor-candidates.json"
DEFAULT_CET_OUTPUT = ROOT / "generated/world-locations/indoor-candidates-cet.json"
CET_SOURCE = ROOT / "tools/indoor_location_browser_cet"
CET_MOD_NAME = "ghostline_indoor_locations"
SECTOR_SUFFIX = ".streamingsector.json"
INTERIOR_NODE_TYPE = "worldInteriorAreaNode"

QUEST_PATTERNS = (
    re.compile(r"(?<![a-z0-9])((?:sq|mq|q)\d{3})(?![a-z0-9])", re.IGNORECASE),
    re.compile(r"(?<![a-z0-9])(sts_[a-z]{3}_[a-z]{3}_\d{2}[a-z]?)(?![a-z0-9])", re.IGNORECASE),
    re.compile(r"(?<![a-z0-9])(ncpd_[a-z0-9_]+)", re.IGNORECASE),
    re.compile(
        r"(?<![a-z0-9])((?:ma|ce)_[a-z]{3}_[a-z]{3}_\d{2})(?![a-z0-9])",
        re.IGNORECASE,
    ),
)

SIGNAL_RULES: dict[str, frozenset[str]] = {
    "doors": frozenset(("door", "doors", "gate", "shutter", "entrance")),
    "elevators": frozenset(("elevator", "elevators", "lift")),
    "workspots": frozenset(("worldaispotnode", "workspot")),
    "terminals": frozenset(("computer", "terminal", "laptop", "dataterm")),
    "access_points": frozenset(("accesspoint", "router")),
    "seating": frozenset(("chair", "stool", "couch", "sofa", "bench", "sit")),
    "beds": frozenset(("bed", "mattress", "ripperdoc", "medical")),
    "bar_features": frozenset(("bar", "bartender", "counter", "booth")),
    "populations": frozenset(("community", "population", "spawner")),
    "vehicles": frozenset(("garage", "parking", "vehicle", "carlift")),
}

SITE_TYPE_RULES: tuple[tuple[str, tuple[str, ...], bool, bool], ...] = (
    ("story_landmark", ("arasaka_tower", "peralez", "lizzies", "kashuu_hanten", "tygerclaw_garage"), False, True),
    ("clothing_shop", ("_cloth_", "clothing", "sex_shop"), True, False),
    ("weapon_shop", ("_guns_", "gunsmith", "_melee_", "weapon_shop"), True, False),
    ("ripperdoc", ("ripdoc", "ripperdoc", "_medic_"), True, False),
    ("netrunner_shop", ("_netrun_", "netrunner"), True, False),
    ("food_shop", ("_food_", "restaurant", "eatery"), True, False),
    ("tech_shop", ("_tech_", "tech_shop"), True, False),
    ("lodging", ("motel", "hotel"), False, False),
    ("apartment", ("apart", "apartment"), False, False),
    ("industrial", ("factory", "warehouse", "garage", "workshop", "junk"), False, False),
    ("club_or_bar", ("club", "bar", "casino"), False, False),
)


def scalar(value: Any) -> Any:
    if isinstance(value, Mapping) and "$value" in value:
        return value["$value"]
    return value


def vector(value: Any) -> dict[str, float] | None:
    if not isinstance(value, Mapping):
        return None
    if not all(isinstance(value.get(key), (int, float)) for key in ("X", "Y", "Z")):
        return None
    return {"x": float(value["X"]), "y": float(value["Y"]), "z": float(value["Z"])}


def payload(handle: Any) -> dict[str, Any]:
    if not isinstance(handle, Mapping):
        return {}
    data = handle.get("Data")
    return dict(data) if isinstance(data, Mapping) else {}


def depot_path(value: Any) -> str:
    if not isinstance(value, Mapping):
        return ""
    path = scalar(value.get("DepotPath"))
    return str(path) if path else ""


def node_resource(data: Mapping[str, Any]) -> str:
    for key in ("entityTemplate", "mesh", "resource", "cookedInstanceData"):
        path = depot_path(data.get(key))
        if path:
            return path
    return ""


def node_text(data: Mapping[str, Any], quest_ref: str) -> str:
    values = (
        data.get("$type"),
        scalar(data.get("debugName")),
        node_resource(data),
        quest_ref,
    )
    return " ".join(str(value) for value in values if value).casefold()


def quest_ids(text: str) -> list[str]:
    found: set[str] = set()
    for pattern in QUEST_PATTERNS:
        found.update(match.group(1).casefold() for match in pattern.finditer(text))
    return sorted(found)


def records_by_node(root: Mapping[str, Any]) -> dict[int, list[dict[str, Any]]]:
    raw = root.get("nodeData", [])
    records = raw.get("Data", []) if isinstance(raw, Mapping) else raw
    grouped: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for record in records if isinstance(records, list) else []:
        if isinstance(record, dict) and isinstance(record.get("NodeIndex"), int):
            grouped[record["NodeIndex"]].append(record)
    return grouped


def distance(left: Mapping[str, float], right: Mapping[str, float]) -> float:
    return math.dist(
        (left["x"], left["y"], left["z"]),
        (right["x"], right["y"], right["z"]),
    )


def outline_info(data: Mapping[str, Any], placement: Mapping[str, Any]) -> dict[str, Any]:
    outline = payload(data.get("outline"))
    points = outline.get("points", [])
    scale = vector(placement.get("Scale")) or {"x": 1.0, "y": 1.0, "z": 1.0}
    xs: list[float] = []
    ys: list[float] = []
    for point in points if isinstance(points, list) else []:
        parsed = vector(point)
        if parsed:
            xs.append(parsed["x"] * scale["x"])
            ys.append(parsed["y"] * scale["y"])
    width = max(xs) - min(xs) if xs else None
    depth = max(ys) - min(ys) if ys else None
    height = outline.get("height")
    scaled_height = float(height) * scale["z"] if isinstance(height, (int, float)) else None
    return {
        "points": len(xs),
        "width": round(width, 3) if width is not None else None,
        "depth": round(depth, 3) if depth is not None else None,
        "height": round(scaled_height, 3) if scaled_height is not None else None,
    }


def semantic_signals(text: str) -> list[str]:
    words = frozenset(re.findall(r"[a-z0-9]+", text.casefold()))
    return [name for name, tokens in SIGNAL_RULES.items() if words.intersection(tokens)]


def classify_site(name: str) -> tuple[str, bool, bool]:
    folded = name.casefold()
    if quest_ids(folded):
        return "named_vanilla_content", False, True
    for site_type, tokens, retail, known_content in SITE_TYPE_RULES:
        if any(token in folded for token in tokens):
            return site_type, retail, known_content
    return "unclassified", False, False


def candidate_id(relative_sector: str, node_index: int, placement_index: int) -> str:
    source = f"{relative_sector}:{node_index}:{placement_index}".encode()
    return f"indoor_{hashlib.sha1(source).hexdigest()[:12]}"


def inspect_sector(
    path: Path,
    source_root: Path,
    *,
    support_radius: float,
    quest_radius: float,
) -> list[dict[str, Any]]:
    document = json.loads(path.read_text(encoding="utf-8"))
    root = document.get("Data", {}).get("RootChunk", {})
    if not isinstance(root, Mapping):
        return []
    nodes = root.get("nodes", [])
    if not isinstance(nodes, list):
        return []
    grouped = records_by_node(root)
    relative_sector = path.relative_to(source_root).as_posix()

    placed_nodes: list[dict[str, Any]] = []
    interiors: list[dict[str, Any]] = []
    for node_index, handle in enumerate(nodes):
        data = payload(handle)
        node_type = str(data.get("$type") or "")
        placements = grouped.get(node_index, [{}])
        for placement_index, placement in enumerate(placements):
            position = vector(placement.get("Position"))
            quest_ref = str(scalar(placement.get("QuestPrefabRefHash")) or "")
            text = node_text(data, quest_ref)
            entry = {
                "node_index": node_index,
                "placement_index": placement_index,
                "node_type": node_type,
                "debug_name": str(scalar(data.get("debugName")) or ""),
                "resource": node_resource(data),
                "quest_ref": quest_ref,
                "quest_ids": quest_ids(text),
                "position": position,
                "text": text,
                "signals": semantic_signals(text),
            }
            placed_nodes.append(entry)
            if node_type == INTERIOR_NODE_TYPE and position is not None:
                entry["outline"] = outline_info(data, placement)
                interiors.append(entry)

    results: list[dict[str, Any]] = []
    sector_quest_owned = path.name.casefold().startswith("quest_")
    for interior in interiors:
        nearby_counts: Counter[str] = Counter()
        nearby_examples: dict[str, list[str]] = defaultdict(list)
        nearby_quest_ids: set[str] = set(interior["quest_ids"])
        nearest_quest_distance: float | None = None
        for other in placed_nodes:
            if other["position"] is None:
                continue
            separation = distance(interior["position"], other["position"])
            if separation <= support_radius:
                for signal in other["signals"]:
                    nearby_counts[signal] += 1
                    label = other["debug_name"] or other["resource"] or other["node_type"]
                    if label and label not in nearby_examples[signal] and len(nearby_examples[signal]) < 3:
                        nearby_examples[signal].append(label)
            if other["quest_ids"] and separation <= quest_radius:
                nearby_quest_ids.update(other["quest_ids"])
                if nearest_quest_distance is None or separation < nearest_quest_distance:
                    nearest_quest_distance = separation

        site_type, retail, known_content = classify_site(interior["debug_name"])
        direct_quest = bool(interior["quest_ids"]) or sector_quest_owned or known_content
        quest_linked = direct_quest or bool(nearby_quest_ids)
        ownership = "quest_linked" if quest_linked else "likely_unowned"
        score = 50
        score += min(15, nearby_counts["doors"] * 3)
        score += min(10, nearby_counts["workspots"])
        score += min(8, nearby_counts["terminals"] * 2)
        score += min(5, nearby_counts["seating"])
        score += min(5, nearby_counts["beds"] * 2)
        score += min(4, nearby_counts["elevators"] * 2)
        score -= min(12, nearby_counts["populations"] * 2)
        if quest_linked:
            score -= 30 if direct_quest else 15
        if retail:
            score -= 20
        score = max(0, min(100, score))

        evidence: list[str] = []
        if sector_quest_owned:
            evidence.append("quest_* source sector")
        if interior["quest_ids"]:
            evidence.append("quest id on interior node")
        if known_content:
            evidence.append("named vanilla story location")
        if nearby_quest_ids and not interior["quest_ids"]:
            evidence.append(f"quest id within {quest_radius:g}m")
        if not evidence:
            evidence.append("no quest identifier found on or near interior area")

        results.append(
            {
                "candidate_id": candidate_id(relative_sector, interior["node_index"], interior["placement_index"]),
                "ownership": ownership,
                "ownership_confidence": "high" if direct_quest else ("medium" if quest_linked else "provisional"),
                "review_score": score,
                "site_type": site_type,
                "retail": retail,
                "position": interior["position"],
                "outline": interior["outline"],
                "debug_name": interior["debug_name"],
                "source": {
                    "sector": relative_sector,
                    "node_index": interior["node_index"],
                    "placement_index": interior["placement_index"],
                    "quest_prefab_ref": interior["quest_ref"],
                },
                "quest_evidence": {
                    "quest_ids": sorted(nearby_quest_ids),
                    "nearest_distance": round(nearest_quest_distance, 3) if nearest_quest_distance is not None else None,
                    "reasons": evidence,
                },
                "nearby_signals": dict(sorted(nearby_counts.items())),
                "signal_examples": dict(sorted(nearby_examples.items())),
            }
        )
    return results


def discover_sector_paths(source_root: Path) -> list[Path]:
    if not source_root.is_dir():
        raise FileNotFoundError(f"serialized sector root does not exist: {source_root}")
    rg = shutil.which("rg")
    if rg:
        result = subprocess.run(
            [rg, "-l", "-F", INTERIOR_NODE_TYPE, str(source_root), "-g", f"*{SECTOR_SUFFIX}"],
            check=False,
            text=True,
            capture_output=True,
        )
        if result.returncode not in (0, 1):
            raise RuntimeError(result.stderr.strip() or "rg sector discovery failed")
        return sorted(Path(line) for line in result.stdout.splitlines() if line.strip())

    matches: list[Path] = []
    needle = INTERIOR_NODE_TYPE.encode()
    for path in source_root.rglob(f"*{SECTOR_SUFFIX}"):
        with path.open("rb") as stream:
            if needle in stream.read():
                matches.append(path)
    return sorted(matches)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", newline="\n", dir=path.parent,
            prefix=f".{path.name}.", suffix=".tmp", delete=False,
        ) as stream:
            json.dump(value, stream, indent=2, ensure_ascii=False)
            stream.write("\n")
            temporary = Path(stream.name)
        temporary.replace(path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def build_manifest(
    source_root: Path,
    *,
    support_radius: float,
    quest_radius: float,
    limit_sectors: int | None = None,
) -> dict[str, Any]:
    paths = discover_sector_paths(source_root)
    if limit_sectors is not None:
        paths = paths[:limit_sectors]
    candidates: list[dict[str, Any]] = []
    errors: list[dict[str, str]] = []
    for ordinal, path in enumerate(paths, 1):
        try:
            candidates.extend(
                inspect_sector(path, source_root, support_radius=support_radius, quest_radius=quest_radius)
            )
        except Exception as error:
            errors.append({"sector": path.relative_to(source_root).as_posix(), "error": f"{type(error).__name__}: {error}"})
        if ordinal % 25 == 0 or ordinal == len(paths):
            print(f"[{ordinal}/{len(paths)}] {len(candidates)} candidates, {len(errors)} errors")
    candidates.sort(key=lambda row: (row["ownership"] != "likely_unowned", -row["review_score"], row["candidate_id"]))
    ownership_counts = Counter(row["ownership"] for row in candidates)
    return {
        "schema_version": 1,
        "generated_by": "tools/indoor_location_candidates.py",
        "source_root": str(source_root.resolve()),
        "method": {
            "seed_node_type": INTERIOR_NODE_TYPE,
            "support_radius": support_radius,
            "quest_radius": quest_radius,
            "ownership_warning": "likely_unowned means no serialized quest identifier was found on or near the area; runtime validation is still required",
        },
        "summary": {
            "matched_sectors": len(paths),
            "candidates": len(candidates),
            "ownership": dict(sorted(ownership_counts.items())),
            "errors": len(errors),
        },
        "candidates": candidates,
        "errors": errors,
    }


def command_build(args: argparse.Namespace) -> None:
    manifest = build_manifest(
        args.sectors,
        support_radius=args.support_radius,
        quest_radius=args.quest_radius,
        limit_sectors=args.limit_sectors,
    )
    write_json(args.output, manifest)
    print(json.dumps({"output": str(args.output), **manifest["summary"]}, indent=2))


def command_list(args: argparse.Namespace) -> None:
    document = json.loads(args.manifest.read_text(encoding="utf-8"))
    rows: Iterable[dict[str, Any]] = document.get("candidates", [])
    if args.ownership:
        rows = (row for row in rows if row.get("ownership") == args.ownership)
    rows = list(rows)
    rows.sort(key=lambda row: (-int(row.get("review_score", 0)), str(row.get("candidate_id", ""))))
    if args.limit is not None:
        rows = rows[: args.limit]
    print(json.dumps(rows, indent=2))


def cet_manifest(
    manifest: Mapping[str, Any],
    *,
    ownership: str | None = None,
    minimum_score: int = 0,
) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for candidate in manifest.get("candidates", []):
        if not isinstance(candidate, Mapping):
            continue
        if ownership and candidate.get("ownership") != ownership:
            continue
        score = int(candidate.get("review_score", 0))
        if score < minimum_score:
            continue
        position = candidate.get("position")
        if not isinstance(position, Mapping):
            continue
        source = candidate.get("source", {})
        evidence = candidate.get("quest_evidence", {})
        signals = candidate.get("nearby_signals", {})
        rows.append(
            {
                "id": str(candidate.get("candidate_id", "")),
                "name": str(candidate.get("debug_name") or candidate.get("candidate_id") or "indoor location"),
                "ownership": str(candidate.get("ownership", "unknown")),
                "score": score,
                "x": float(position["x"]),
                "y": float(position["y"]),
                "z": float(position["z"]),
                "sector": str(source.get("sector", "")) if isinstance(source, Mapping) else "",
                "quest_ids": list(evidence.get("quest_ids", [])) if isinstance(evidence, Mapping) else [],
                "signals": dict(signals) if isinstance(signals, Mapping) else {},
                "site_type": str(candidate.get("site_type") or classify_site(str(candidate.get("debug_name", "")))[0]),
                "retail": bool(candidate.get("retail", classify_site(str(candidate.get("debug_name", "")))[1])),
            }
        )
    rows.sort(key=lambda row: (row["ownership"] != "likely_unowned", -row["score"], row["id"]))
    return {
        "schema_version": 1,
        "generated_by": "tools/indoor_location_candidates.py export-cet",
        "source_schema_version": manifest.get("schema_version"),
        "filters": {"ownership": ownership, "minimum_score": minimum_score},
        "count": len(rows),
        "locations": rows,
    }


def command_export_cet(args: argparse.Namespace) -> None:
    source = json.loads(args.manifest.read_text(encoding="utf-8"))
    result = cet_manifest(source, ownership=args.ownership, minimum_score=args.minimum_score)
    write_json(args.output, result)
    print(json.dumps({"output": str(args.output), "locations": result["count"]}, indent=2))


def command_install_cet(args: argparse.Namespace) -> None:
    game_root = args.game_root.resolve()
    cet_root = game_root / "bin/x64/plugins/cyber_engine_tweaks"
    if not cet_root.is_dir():
        raise SystemExit(f"Cyber Engine Tweaks directory not found: {cet_root}")
    source_init = CET_SOURCE / "init.lua"
    if not source_init.is_file():
        raise SystemExit(f"CET source missing: {source_init}")
    source = json.loads(args.manifest.read_text(encoding="utf-8"))
    locations = cet_manifest(source, ownership=args.ownership, minimum_score=args.minimum_score)
    destination = cet_root / "mods" / CET_MOD_NAME
    destination.mkdir(parents=True, exist_ok=True)
    target_init = destination / "init.lua"
    if target_init.exists() and not args.force and target_init.read_bytes() != source_init.read_bytes():
        raise SystemExit(f"refusing to overwrite modified CET file without --force: {target_init}")
    shutil.copyfile(source_init, target_init)
    write_json(destination / "locations.json", locations)
    print(json.dumps({"cet_mod": str(destination), "locations": locations["count"]}, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    build = subparsers.add_parser("build", help="Build an offline indoor candidate manifest.")
    build.add_argument("--sectors", type=Path, default=DEFAULT_SECTORS)
    build.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    build.add_argument("--support-radius", type=float, default=35.0)
    build.add_argument("--quest-radius", type=float, default=75.0)
    build.add_argument("--limit-sectors", type=int, help="Development/testing limit after prefiltering.")
    build.set_defaults(func=command_build)
    listing = subparsers.add_parser("list", help="Print ranked candidates from a manifest.")
    listing.add_argument("--manifest", type=Path, default=DEFAULT_OUTPUT)
    listing.add_argument("--ownership", choices=("likely_unowned", "quest_linked"))
    listing.add_argument("--limit", type=int, default=25)
    listing.set_defaults(func=command_list)
    export_cet = subparsers.add_parser("export-cet", help="Write a compact JSON catalog for the CET browser.")
    export_cet.add_argument("--manifest", type=Path, default=DEFAULT_OUTPUT)
    export_cet.add_argument("--output", type=Path, default=DEFAULT_CET_OUTPUT)
    export_cet.add_argument("--ownership", choices=("likely_unowned", "quest_linked"))
    export_cet.add_argument("--minimum-score", type=int, default=0)
    export_cet.set_defaults(func=command_export_cet)
    install = subparsers.add_parser("install-cet", help="Install the standalone browser and current catalog into CET.")
    install.add_argument("--game-root", type=Path, required=True)
    install.add_argument("--manifest", type=Path, default=DEFAULT_OUTPUT)
    install.add_argument("--ownership", choices=("likely_unowned", "quest_linked"))
    install.add_argument("--minimum-score", type=int, default=0)
    install.add_argument("--force", action="store_true")
    install.set_defaults(func=command_install_cet)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
