#!/usr/bin/env python3
"""Explore deserialized streamingblock and streamingsector CR2W-JSON files.

World files are large and noisy. This read-only helper prints bounded summaries
of streaming block descriptors, sector nodes, NodeRefs, and community wiring so
reference sets can be compared without dumping the full CR2W-JSON.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from cr2w_helpers import (
    bounded,
    collect_type_counts,
    depot_path_value,
    load_json,
    path_to_string,
    print_json,
    print_table,
    short_type,
    typed_value,
    walk,
)


DEFAULT_REFERENCE_ROOT = Path("reference/world")


@dataclass(frozen=True)
class FileSummary:
    file: str
    archive_file: str
    root_type: str
    category: str
    level: str
    descriptors: int
    nodes: int
    node_data: int
    node_refs: int
    variant_indices: int
    variant_nodes: int
    node_types: str


@dataclass(frozen=True)
class DescriptorInfo:
    file: str
    index: int
    category: str
    level: str
    ranges: str
    path: str
    quest_prefab_ref: str
    variants: int
    bounds_min: str
    bounds_max: str


@dataclass(frozen=True)
class NodeInfo:
    file: str
    index: int
    handle: str
    type: str
    debug_name: str
    position: str
    pivot: str
    quest_prefab_ref: str
    streaming_distance: str
    resource: str
    outline: str
    source_object_id: str


@dataclass(frozen=True)
class RefInfo:
    file: str
    source: str
    index: str
    owner: str
    value: str


@dataclass(frozen=True)
class CommunityInfo:
    file: str
    node: str
    kind: str
    entry: str
    phase: str
    character: str
    source_object_id: str
    spot_refs: str
    spot_ids: str


class WorldExplorer:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.data = load_json(path)
        root = self.data.get("Data", {}).get("RootChunk", {})
        self.root = root if isinstance(root, dict) else {}

    @property
    def archive_file_name(self) -> str:
        header = self.data.get("Header", {})
        return str(header.get("ArchiveFileName", "")) if isinstance(header, dict) else ""

    @property
    def root_type(self) -> str:
        return str(self.root.get("$type", ""))

    @property
    def is_block(self) -> bool:
        return self.root_type == "worldStreamingBlock"

    @property
    def is_sector(self) -> bool:
        return self.root_type == "worldStreamingSector"

    @property
    def descriptors(self) -> list[dict[str, Any]]:
        descriptors = self.root.get("descriptors", [])
        return descriptors if isinstance(descriptors, list) else []

    @property
    def nodes(self) -> list[dict[str, Any]]:
        nodes = self.root.get("nodes", [])
        return nodes if isinstance(nodes, list) else []

    @property
    def node_refs(self) -> list[Any]:
        refs = self.root.get("nodeRefs", [])
        return refs if isinstance(refs, list) else []

    @property
    def node_data(self) -> list[dict[str, Any]]:
        node_data = self.root.get("nodeData", [])
        if isinstance(node_data, dict):
            data = node_data.get("Data", [])
            return data if isinstance(data, list) else []
        return node_data if isinstance(node_data, list) else []

    @property
    def variant_indices(self) -> list[Any]:
        values = self.root.get("variantIndices", [])
        return values if isinstance(values, list) else []

    @property
    def variant_nodes(self) -> list[Any]:
        values = self.root.get("variantNodes", [])
        return values if isinstance(values, list) else []

    def summary(self) -> FileSummary:
        node_types = Counter(node_type(node) for node in self.nodes)
        node_type_text = ", ".join(f"{name}:{count}" for name, count in sorted(node_types.items()) if name)
        return FileSummary(
            file=str(self.path),
            archive_file=self.archive_file_name,
            root_type=self.root_type,
            category=str(self.root.get("category", "")),
            level=str(self.root.get("level", "")),
            descriptors=len(self.descriptors),
            nodes=len(self.nodes),
            node_data=len(self.node_data),
            node_refs=len(self.node_refs),
            variant_indices=len(self.variant_indices),
            variant_nodes=len(self.variant_nodes),
            node_types=node_type_text,
        )

    def descriptor_infos(self) -> list[DescriptorInfo]:
        rows: list[DescriptorInfo] = []
        for index, descriptor in enumerate(self.descriptors):
            bounds = descriptor.get("streamingBox", {})
            rows.append(
                DescriptorInfo(
                    file=str(self.path),
                    index=index,
                    category=str(descriptor.get("category", "")),
                    level=str(descriptor.get("level", "")),
                    ranges=str(descriptor.get("numNodeRanges", "")),
                    path=resource_value(descriptor.get("data")),
                    quest_prefab_ref=string_value(descriptor.get("questPrefabNodeRef")),
                    variants=len(descriptor.get("variants", []) or []),
                    bounds_min=vector_string(nested_dict(bounds, "Min")),
                    bounds_max=vector_string(nested_dict(bounds, "Max")),
                )
            )
        return rows

    def node_infos(self) -> list[NodeInfo]:
        node_data_by_index: dict[int, list[dict[str, Any]]] = defaultdict(list)
        for item in self.node_data:
            if isinstance(item, dict) and isinstance(item.get("NodeIndex"), int):
                node_data_by_index[item["NodeIndex"]].append(item)

        rows: list[NodeInfo] = []
        for index, node in enumerate(self.nodes):
            data = node_payload(node)
            primary_data = node_data_by_index.get(index, [{}])[0]
            rows.append(
                NodeInfo(
                    file=str(self.path),
                    index=index,
                    handle=str(node.get("HandleId", "")) if isinstance(node, dict) else "",
                    type=node_type(node),
                    debug_name=string_value(data.get("debugName")),
                    position=vector_string(primary_data.get("Position")),
                    pivot=vector_string(primary_data.get("Pivot")),
                    quest_prefab_ref=string_value(primary_data.get("QuestPrefabRefHash")),
                    streaming_distance=str(primary_data.get("MaxStreamingDistance", "")),
                    resource=node_resource(data),
                    outline=outline_summary(data),
                    source_object_id=source_object_id(data),
                )
            )
        return rows

    def ref_infos(self) -> list[RefInfo]:
        rows: list[RefInfo] = []
        for index, value in enumerate(self.node_refs):
            rows.append(
                RefInfo(
                    file=str(self.path),
                    source="nodeRefs",
                    index=str(index),
                    owner="",
                    value=string_value(value),
                )
            )

        node_infos = {node.index: node for node in self.node_infos()}
        for index, item in enumerate(self.node_data):
            if not isinstance(item, dict):
                continue
            value = string_value(item.get("QuestPrefabRefHash"))
            if not value or value == "0":
                continue
            node_index = item.get("NodeIndex")
            node = node_infos.get(node_index)
            owner = ""
            if node:
                owner = f"node {node.index} {node.type} {node.debug_name}".strip()
            rows.append(
                RefInfo(
                    file=str(self.path),
                    source="nodeData.QuestPrefabRefHash",
                    index=str(index),
                    owner=owner,
                    value=value,
                )
            )

        for descriptor in self.descriptor_infos():
            if descriptor.quest_prefab_ref and descriptor.quest_prefab_ref != "0":
                rows.append(
                    RefInfo(
                        file=str(self.path),
                        source="descriptor.questPrefabNodeRef",
                        index=str(descriptor.index),
                        owner=descriptor.path,
                        value=descriptor.quest_prefab_ref,
                    )
                )
        return rows

    def community_infos(self) -> list[CommunityInfo]:
        rows: list[CommunityInfo] = []
        for node in self.node_infos():
            data = node_payload(self.nodes[node.index])
            node_label = f"node {node.index} {node.debug_name}".strip()
            node_kind = data.get("$type", "")
            if node_kind == "worldCommunityRegistryNode":
                rows.extend(registry_rows(str(self.path), node_label, data))
            elif str(node_kind).startswith("worldCompiledCommunityAreaNode"):
                rows.extend(area_rows(str(self.path), node_label, data))
        return rows

    def search(self, terms: list[str], limit: int) -> list[tuple[str, str]]:
        normalized_terms = [term.casefold() for term in terms if term]
        matches: list[tuple[str, str]] = []
        for path, value in walk(self.data):
            if isinstance(value, (dict, list)):
                continue
            path_text = path_to_string(path)
            value_text = str(value)
            haystack = f"{path_text} {value_text}".casefold()
            if all(term in haystack for term in normalized_terms):
                matches.append((path_text, value_text))
                if limit > 0 and len(matches) >= limit:
                    break
        return matches


def nested_dict(value: Any, key: str) -> dict[str, Any]:
    if isinstance(value, dict) and isinstance(value.get(key), dict):
        return value[key]
    return {}


def node_payload(node: Any) -> dict[str, Any]:
    if isinstance(node, dict) and isinstance(node.get("Data"), dict):
        return node["Data"]
    return node if isinstance(node, dict) else {}


def node_type(node: Any) -> str:
    return str(node_payload(node).get("$type", ""))


def string_value(value: Any) -> str:
    if isinstance(value, dict):
        if "$value" in value:
            return str(value.get("$value", ""))
        if "hash" in value:
            return str(value.get("hash", ""))
    if value is None:
        return ""
    return str(value)


def resource_value(value: Any) -> str:
    if isinstance(value, dict):
        depot = depot_path_value(value)
        if depot:
            return depot
        return string_value(value)
    return string_value(value)


def vector_string(value: Any) -> str:
    if not isinstance(value, dict):
        return ""
    if not all(axis in value for axis in ("X", "Y", "Z")):
        return ""
    return f"{value.get('X')},{value.get('Y')},{value.get('Z')}"


def node_resource(data: dict[str, Any]) -> str:
    for key in ("mesh", "resource", "entityTemplate", "workspotResource"):
        value = data.get(key)
        resource = resource_value(value)
        if resource and resource != "0":
            return resource

    spot = node_payload(data.get("spot"))
    resource = resource_value(spot.get("resource"))
    if resource and resource != "0":
        return resource
    return ""


def source_object_id(data: dict[str, Any]) -> str:
    value = data.get("sourceObjectId")
    if isinstance(value, dict):
        return str(value.get("hash", ""))
    return "" if value is None else str(value)


def outline_summary(data: dict[str, Any]) -> str:
    outline = node_payload(data.get("outline"))
    if not outline:
        return ""
    points = outline.get("points", [])
    point_count = len(points) if isinstance(points, list) else 0
    height = outline.get("height", "")
    return f"height={height} points={point_count}".strip()


def cname(value: Any) -> str:
    return string_value(value)


def node_ref_list(values: Any) -> list[str]:
    if not isinstance(values, list):
        return []
    return [string_value(value) for value in values if string_value(value)]


def registry_rows(file_path: str, node_label: str, data: dict[str, Any]) -> list[CommunityInfo]:
    rows: list[CommunityInfo] = []
    for item in data.get("communitiesData", []) or []:
        if not isinstance(item, dict):
            continue
        community_id = ""
        community_id_value = item.get("communityId")
        if isinstance(community_id_value, dict):
            community_id = string_value(community_id_value.get("entityId"))
        initial_states = item.get("entriesInitialState", []) or []
        template = node_payload(item.get("template"))
        entries = template.get("entries", []) if isinstance(template, dict) else []
        for entry in entries:
            entry_data = node_payload(entry)
            character = string_value(entry_data.get("characterRecordId"))
            entry_name = cname(entry_data.get("entryName"))
            phases = entry_data.get("phases", []) or []
            if not phases:
                rows.append(
                    CommunityInfo(file_path, node_label, "registry", entry_name, "", character, community_id, "", "")
                )
            for phase in phases:
                phase_data = node_payload(phase)
                phase_name = cname(phase_data.get("phaseName"))
                spot_refs: list[str] = []
                for period in phase_data.get("timePeriods", []) or []:
                    if isinstance(period, dict):
                        spot_refs.extend(node_ref_list(period.get("spotNodeRefs")))
                rows.append(
                    CommunityInfo(
                        file=file_path,
                        node=node_label,
                        kind="registry",
                        entry=entry_name,
                        phase=phase_name,
                        character=character,
                        source_object_id=community_id,
                        spot_refs=", ".join(spot_refs),
                        spot_ids="",
                    )
                )

        if not entries and initial_states:
            for state in initial_states:
                rows.append(
                    CommunityInfo(
                        file=file_path,
                        node=node_label,
                        kind="registry_initial_state",
                        entry=cname(state.get("entryName")),
                        phase=cname(state.get("initialPhaseName")),
                        character="",
                        source_object_id=community_id,
                        spot_refs="",
                        spot_ids="",
                    )
                )
    return rows


def area_rows(file_path: str, node_label: str, data: dict[str, Any]) -> list[CommunityInfo]:
    rows: list[CommunityInfo] = []
    area = node_payload(data.get("area"))
    source_id = source_object_id(data)
    for entry in area.get("entriesData", []) or []:
        if not isinstance(entry, dict):
            continue
        entry_name = cname(entry.get("entryName"))
        for phase in entry.get("phasesData", []) or []:
            if not isinstance(phase, dict):
                continue
            phase_name = cname(phase.get("entryPhaseName"))
            spot_ids: list[str] = []
            for period in phase.get("timePeriodsData", []) or []:
                if isinstance(period, dict):
                    spot_ids.extend(string_value(value) for value in period.get("spotNodeIds", []) or [])
            rows.append(
                CommunityInfo(
                    file=file_path,
                    node=node_label,
                    kind="area",
                    entry=entry_name,
                    phase=phase_name,
                    character="",
                    source_object_id=source_id,
                    spot_refs="",
                    spot_ids=", ".join(spot_ids),
                )
            )
    return rows


def discover_files(root: Path) -> list[Path]:
    if root.is_file():
        return [root]
    patterns = ("*.streamingblock.json", "*.streamingsector.json")
    files: list[Path] = []
    for pattern in patterns:
        files.extend(root.rglob(pattern))
    return sorted(set(files))


def load_explorers(args: argparse.Namespace) -> list[WorldExplorer]:
    paths: list[Path] = []
    for file_path in args.file or []:
        paths.extend(discover_files(Path(file_path)))
    if not paths:
        paths = discover_files(Path(args.root))
    if not paths:
        raise SystemExit("No *.streamingblock.json or *.streamingsector.json files found.")
    return [WorldExplorer(path) for path in sorted(set(paths))]


def command_summary(args: argparse.Namespace) -> None:
    rows = [explorer.summary() for explorer in load_explorers(args)]
    if args.json:
        print_json([asdict(row) for row in rows])
        return
    print_table(
        [asdict(row) for row in rows],
        [
            ("file", "File"),
            ("root_type", "Root Type"),
            ("category", "Category"),
            ("level", "Level"),
            ("descriptors", "Descriptors"),
            ("nodes", "Nodes"),
            ("node_data", "NodeData"),
            ("node_refs", "NodeRefs"),
            ("node_types", "Node Types"),
        ],
    )


def command_blocks(args: argparse.Namespace) -> None:
    rows = [row for explorer in load_explorers(args) for row in explorer.descriptor_infos()]
    if args.json:
        print_json([asdict(row) for row in rows])
        return
    print_table(
        [asdict(row) for row in rows],
        [
            ("file", "File"),
            ("index", "Index"),
            ("category", "Category"),
            ("level", "Level"),
            ("ranges", "Ranges"),
            ("path", "Sector Path"),
            ("quest_prefab_ref", "Quest Prefab Ref"),
            ("bounds_min", "Bounds Min"),
            ("bounds_max", "Bounds Max"),
        ],
    )


def command_nodes(args: argparse.Namespace) -> None:
    rows = [row for explorer in load_explorers(args) for row in explorer.node_infos()]
    if args.type:
        term = args.type.casefold()
        rows = [row for row in rows if term in row.type.casefold() or term in short_type(row.type).casefold()]
    if args.ref:
        term = args.ref.casefold()
        rows = [row for row in rows if term in row.quest_prefab_ref.casefold()]
    rows, suffix = bounded(rows, args.limit, args.offset)
    if args.json:
        print_json([asdict(row) for row in rows])
        return
    print_table(
        [asdict(row) for row in rows],
        [
            ("file", "File"),
            ("index", "Index"),
            ("type", "Type"),
            ("debug_name", "Debug Name"),
            ("position", "Position"),
            ("quest_prefab_ref", "Quest Prefab Ref"),
            ("resource", "Resource"),
            ("outline", "Outline"),
            ("source_object_id", "Source Object ID"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_noderefs(args: argparse.Namespace) -> None:
    rows = [row for explorer in load_explorers(args) for row in explorer.ref_infos()]
    if args.contains:
        term = args.contains.casefold()
        rows = [row for row in rows if term in row.value.casefold() or term in row.owner.casefold()]
    rows, suffix = bounded(rows, args.limit, args.offset)
    if args.json:
        print_json([asdict(row) for row in rows])
        return
    print_table(
        [asdict(row) for row in rows],
        [
            ("file", "File"),
            ("source", "Source"),
            ("index", "Index"),
            ("owner", "Owner"),
            ("value", "Value"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_communities(args: argparse.Namespace) -> None:
    rows = [row for explorer in load_explorers(args) for row in explorer.community_infos()]
    if args.json:
        print_json([asdict(row) for row in rows])
        return
    print_table(
        [asdict(row) for row in rows],
        [
            ("file", "File"),
            ("node", "Node"),
            ("kind", "Kind"),
            ("entry", "Entry"),
            ("phase", "Phase"),
            ("character", "Character"),
            ("source_object_id", "Source Object ID"),
            ("spot_refs", "Spot NodeRefs"),
            ("spot_ids", "Spot IDs"),
        ],
    )


def command_types(args: argparse.Namespace) -> None:
    counts: Counter[str] = Counter()
    for explorer in load_explorers(args):
        counts.update(collect_type_counts(explorer.data))
    rows = [
        {"type": type_name, "short": short_type(type_name), "count": count}
        for type_name, count in sorted(counts.items())
    ]
    if args.json:
        print_json(rows)
        return
    print_table(rows, [("count", "Count"), ("short", "Short"), ("type", "Type")])


def command_search(args: argparse.Namespace) -> None:
    matches: list[dict[str, str]] = []
    for explorer in load_explorers(args):
        for path, value in explorer.search(args.terms, args.limit):
            matches.append({"file": str(explorer.path), "path": path, "value": value})
            if args.limit > 0 and len(matches) >= args.limit:
                break
        if args.limit > 0 and len(matches) >= args.limit:
            break
    if args.json:
        print_json(matches)
        return
    print_table(matches, [("file", "File"), ("path", "Path"), ("value", "Value")])
    if args.limit > 0 and len(matches) >= args.limit:
        print()
        print(f"Stopped at --limit {args.limit}. Use --limit 0 for all matches.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Explore deserialized .streamingblock and .streamingsector CR2W-JSON files."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_REFERENCE_ROOT,
        help=f"Reference root to scan when --file is omitted. Default: {DEFAULT_REFERENCE_ROOT}",
    )
    parser.add_argument(
        "-f",
        "--file",
        action="append",
        help="Specific file or directory to inspect. May be repeated.",
    )
    subparsers = parser.add_subparsers(dest="command")

    summary = subparsers.add_parser("summary", help="Summarize all selected world reference JSON files.")
    summary.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    summary.set_defaults(func=command_summary)

    blocks = subparsers.add_parser("blocks", help="List streamingblock sector descriptors.")
    blocks.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    blocks.set_defaults(func=command_blocks)

    nodes = subparsers.add_parser("nodes", help="List sector nodes with nodeData placement and QuestPrefabRefHash.")
    nodes.add_argument("--type", help="Filter by full or short node type substring.")
    nodes.add_argument("--ref", help="Filter by QuestPrefabRefHash substring.")
    nodes.add_argument("--limit", type=int, default=200, help="Maximum rows to print. Use 0 for all.")
    nodes.add_argument("--offset", type=int, default=0, help="Skip this many rows before printing.")
    nodes.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    nodes.set_defaults(func=command_nodes)

    noderefs = subparsers.add_parser("noderefs", help="List sector nodeRefs and QuestPrefabRefHash values.")
    noderefs.add_argument("--contains", help="Filter refs and owners by substring.")
    noderefs.add_argument("--limit", type=int, default=200, help="Maximum rows to print. Use 0 for all.")
    noderefs.add_argument("--offset", type=int, default=0, help="Skip this many rows before printing.")
    noderefs.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    noderefs.set_defaults(func=command_noderefs)

    communities = subparsers.add_parser("communities", help="Summarize community registry and area node wiring.")
    communities.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    communities.set_defaults(func=command_communities)

    types = subparsers.add_parser("types", help="Count every CR2W $type across selected files.")
    types.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    types.set_defaults(func=command_types)

    search = subparsers.add_parser("search", help="Search scalar keys and values by substring.")
    search.add_argument("terms", nargs="+", help="Case-insensitive terms. All terms must match.")
    search.add_argument("--limit", type=int, default=50, help="Maximum matches to print. Use 0 for all.")
    search.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    search.set_defaults(func=command_search)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        args.command = "summary"
        args.json = False
        args.func = command_summary
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
