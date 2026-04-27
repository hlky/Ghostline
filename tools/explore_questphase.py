#!/usr/bin/env python3
"""Explore a WolvenKit-deserialized questphase JSON file.

This tool is intentionally read-only. It builds indexes over CR2W handle
definitions and handle references, then exposes bounded views that are useful
when the full questphase is too large to paste into a prompt or editor pane.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from cr2w_helpers import (
    bounded,
    collect_type_counts,
    depot_path_value,
    first_scalar_label,
    int_or_text,
    load_json,
    nested_get,
    object_handle,
    path_to_string,
    print_json,
    print_table,
    short_type,
    typed_value,
    walk,
)


DEFAULT_QUESTPHASE = Path("source/raw/mod/gq000/phases/gq000_patch_meet.questphase.json")


@dataclass(frozen=True)
class NodeInfo:
    handle: str
    quest_id: str
    type: str
    short_type: str
    label: str
    socket_handles: list[str]


@dataclass(frozen=True)
class SocketInfo:
    handle: str
    owner_node: str
    name: str
    type: str


@dataclass(frozen=True)
class EdgeInfo:
    handle: str
    source_node: str
    source_node_label: str
    source_socket: str
    source_socket_name: str
    destination_node: str
    destination_node_label: str
    destination_socket: str
    destination_socket_name: str


@dataclass(frozen=True)
class RefInfo:
    kind: str
    value: str
    path: str
    owner_node: str
    owner_node_label: str


class QuestphaseExplorer:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.data = load_json(path)
        self.handle_map: dict[str, dict[str, Any]] = {}
        self.handle_paths: dict[str, tuple[Any, ...]] = {}
        self.parent_node_by_path: dict[tuple[Any, ...], str] = {}
        self.nodes_by_handle: dict[str, NodeInfo] = {}
        self.node_data_by_handle: dict[str, dict[str, Any]] = {}
        self.socket_info_by_handle: dict[str, SocketInfo] = {}
        self.edges_by_handle: dict[str, EdgeInfo] = {}
        self._index_handles()
        self._index_nodes()
        self._index_edges()

    def _index_handles(self) -> None:
        for path, value in walk(self.data):
            if not isinstance(value, dict) or "HandleId" not in value:
                continue
            handle = str(value["HandleId"])
            self.handle_map[handle] = value
            self.handle_paths[handle] = path

    def _index_nodes(self) -> None:
        for node in self.graph_nodes:
            if not isinstance(node, dict) or "HandleId" not in node:
                continue
            handle = str(node["HandleId"])
            node_data = self.resolve_data(node)
            if not isinstance(node_data, dict):
                continue

            socket_handles = []
            for socket_ref in node_data.get("sockets", []):
                socket_handle = object_handle(socket_ref)
                if socket_handle is None:
                    continue
                socket_handles.append(socket_handle)
                socket_data = self.resolve_data(socket_ref)
                if not isinstance(socket_data, dict):
                    continue
                self.socket_info_by_handle[socket_handle] = SocketInfo(
                    handle=socket_handle,
                    owner_node=handle,
                    name=str(typed_value(socket_data.get("name"), "")),
                    type=str(socket_data.get("type", "")),
                )

            info = NodeInfo(
                handle=handle,
                quest_id=str(node_data.get("id", "")),
                type=str(node_data.get("$type", "")),
                short_type=short_type(str(node_data.get("$type", ""))),
                label=self.describe_node_data(node_data),
                socket_handles=socket_handles,
            )
            self.nodes_by_handle[handle] = info
            self.node_data_by_handle[handle] = node_data

            node_path = self.handle_paths.get(handle)
            if node_path is not None:
                for child_path, _ in walk(node_data, node_path + ("Data",)):
                    self.parent_node_by_path[child_path] = handle

    def _index_edges(self) -> None:
        for socket_handle, socket_info in self.socket_info_by_handle.items():
            socket_wrapper = self.handle_map.get(socket_handle)
            socket_data = self.resolve_data(socket_wrapper)
            if not isinstance(socket_data, dict):
                continue
            for connection_ref in socket_data.get("connections", []):
                connection_handle = object_handle(connection_ref)
                if connection_handle is None or connection_handle in self.edges_by_handle:
                    continue
                connection_data = self.resolve_data(connection_ref)
                if not isinstance(connection_data, dict):
                    continue
                source_socket = object_handle(connection_data.get("source"))
                destination_socket = object_handle(connection_data.get("destination"))
                if source_socket is None or destination_socket is None:
                    continue

                source_info = self.socket_info_by_handle.get(source_socket)
                destination_info = self.socket_info_by_handle.get(destination_socket)
                source_node = source_info.owner_node if source_info else ""
                destination_node = destination_info.owner_node if destination_info else ""
                source_node_info = self.nodes_by_handle.get(source_node)
                destination_node_info = self.nodes_by_handle.get(destination_node)
                self.edges_by_handle[connection_handle] = EdgeInfo(
                    handle=connection_handle,
                    source_node=source_node,
                    source_node_label=node_display(source_node_info),
                    source_socket=source_socket,
                    source_socket_name=source_info.name if source_info else "",
                    destination_node=destination_node,
                    destination_node_label=node_display(destination_node_info),
                    destination_socket=destination_socket,
                    destination_socket_name=destination_info.name if destination_info else "",
                )

    @property
    def root_chunk(self) -> dict[str, Any]:
        root = self.data.get("Data", {}).get("RootChunk", {})
        return root if isinstance(root, dict) else {}

    @property
    def graph_data(self) -> dict[str, Any]:
        graph = self.root_chunk.get("graph", {})
        if isinstance(graph, dict):
            graph_data = graph.get("Data", {})
            if isinstance(graph_data, dict):
                return graph_data
        return {}

    @property
    def graph_nodes(self) -> list[Any]:
        nodes = self.graph_data.get("nodes", [])
        return nodes if isinstance(nodes, list) else []

    @property
    def archive_file_name(self) -> str:
        header = self.data.get("Header", {})
        if isinstance(header, dict):
            return str(header.get("ArchiveFileName", ""))
        return ""

    def resolve_data(self, value: Any) -> Any:
        if not isinstance(value, dict):
            return value
        if "HandleRefId" in value:
            ref = str(value["HandleRefId"])
            value = self.handle_map.get(ref, value)
        if isinstance(value, dict) and "Data" in value:
            return value["Data"]
        return value

    def describe_node_data(self, node_data: dict[str, Any]) -> str:
        node_type = str(node_data.get("$type", ""))
        if node_type == "questInputNodeDefinition":
            return str(typed_value(node_data.get("socketName"), "input"))
        if node_type == "questOutputNodeDefinition":
            return str(node_data.get("type") or typed_value(node_data.get("socketName"), "output"))
        if node_type == "questCheckpointNodeDefinition":
            return str(node_data.get("debugString", "checkpoint"))
        if node_type == "questSceneNodeDefinition":
            scene = depot_path_value(node_data.get("sceneFile"))
            marker = typed_value(nested_get(node_data, ("sceneLocation", "nodeRef")), "")
            pieces = [part for part in (scene, marker) if part]
            return " at ".join(str(part) for part in pieces) if pieces else "scene"
        if node_type == "questJournalNodeDefinition":
            journal_data = self.resolve_data(node_data.get("type"))
            path_data = self.resolve_data(journal_data.get("path")) if isinstance(journal_data, dict) else {}
            if isinstance(path_data, dict):
                return str(path_data.get("realPath") or typed_value(path_data.get("className"), "journal"))
            return "journal"
        if node_type == "questPauseConditionNodeDefinition":
            condition_data = self.resolve_data(node_data.get("condition"))
            if isinstance(condition_data, dict):
                trigger_ref = typed_value(condition_data.get("triggerAreaRef"), "")
                condition_type = condition_data.get("type") or short_type(str(condition_data.get("$type", "")))
                return f"{condition_type} {trigger_ref}".strip()
            return "condition"
        return first_scalar_label(node_data) or short_type(node_type) or "node"

    def node_by_selector(self, selector: str) -> NodeInfo:
        selector = selector.strip()
        if selector.lower().startswith(("handle:", "h:")):
            handle = selector.split(":", 1)[1]
            return self._node_by_handle(handle)
        if selector.lower().startswith(("id:", "quest_id:", "qid:")):
            quest_id = selector.split(":", 1)[1]
            return self._node_by_quest_id(quest_id)

        quest_matches = [info for info in self.nodes_by_handle.values() if info.quest_id == selector]
        if len(quest_matches) == 1:
            return quest_matches[0]
        if len(quest_matches) > 1:
            handles = ", ".join(info.handle for info in quest_matches)
            raise SystemExit(f"Selector {selector!r} matched multiple quest ids. Use handle:<id>. Matches: {handles}")
        return self._node_by_handle(selector)

    def _node_by_handle(self, handle: str) -> NodeInfo:
        info = self.nodes_by_handle.get(str(handle))
        if info is None:
            raise SystemExit(f"No graph node with handle {handle}")
        return info

    def _node_by_quest_id(self, quest_id: str) -> NodeInfo:
        matches = [info for info in self.nodes_by_handle.values() if info.quest_id == str(quest_id)]
        if not matches:
            raise SystemExit(f"No graph node with quest id {quest_id}")
        if len(matches) > 1:
            handles = ", ".join(info.handle for info in matches)
            raise SystemExit(f"Quest id {quest_id} matched multiple nodes. Use handle:<id>. Matches: {handles}")
        return matches[0]

    def refs(self) -> list[RefInfo]:
        refs: list[RefInfo] = []
        for path, value in walk(self.data):
            if not isinstance(value, dict):
                continue
            kind = ""
            ref_value: Any = None
            value_type = value.get("$type")
            if value_type == "ResourcePath":
                kind = "resource"
                ref_value = value.get("$value")
            elif value_type == "NodeRef":
                kind = "node_ref"
                ref_value = value.get("$value")
            elif "DepotPath" in value:
                depot = value.get("DepotPath")
                if isinstance(depot, dict):
                    kind = "depot_path"
                    ref_value = depot.get("$value")
            elif "realPath" in value and "className" in value:
                kind = "journal_path"
                ref_value = value.get("realPath")

            if kind and ref_value not in (None, "", "0"):
                owner = self.owner_node_for_path(path)
                owner_info = self.nodes_by_handle.get(owner)
                refs.append(
                    RefInfo(
                        kind=kind,
                        value=str(ref_value),
                        path=path_to_string(path),
                        owner_node=owner,
                        owner_node_label=node_display(owner_info),
                    )
                )
        return refs

    def owner_node_for_path(self, path: tuple[Any, ...]) -> str:
        for length in range(len(path), 0, -1):
            owner = self.parent_node_by_path.get(path[:length])
            if owner:
                return owner
        return ""

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

    def handle_json(self, handle: str) -> dict[str, Any]:
        wrapper = self.handle_map.get(str(handle))
        if wrapper is None:
            raise SystemExit(f"No object with HandleId {handle}")
        return wrapper

    def handle_kind(self, handle: str) -> str:
        wrapper = self.handle_map.get(str(handle))
        data = self.resolve_data(wrapper)
        if not isinstance(data, dict):
            return ""
        return str(data.get("$type", ""))

    def node_refs(self, node_handle: str) -> list[RefInfo]:
        return [ref for ref in self.refs() if ref.owner_node == node_handle]

    def summary(self) -> dict[str, Any]:
        node_type_counts = Counter(info.short_type for info in self.nodes_by_handle.values())
        all_type_counts = collect_type_counts(self.data)
        refs = self.refs()
        ref_counts = Counter(ref.kind for ref in refs)
        embedded = self.data.get("Data", {}).get("EmbeddedFiles", [])
        phase_prefabs = self.root_chunk.get("phasePrefabs", [])
        return {
            "file": str(self.path),
            "archive_file": self.archive_file_name,
            "root_type": self.root_chunk.get("$type", ""),
            "nodes": len(self.nodes_by_handle),
            "edges": len(self.edges_by_handle),
            "handles": len(self.handle_map),
            "embedded_files": len(embedded) if isinstance(embedded, list) else 0,
            "phase_prefabs": len(phase_prefabs) if isinstance(phase_prefabs, list) else 0,
            "node_types": dict(sorted(node_type_counts.items())),
            "reference_types": dict(sorted(ref_counts.items())),
            "all_types": dict(sorted((str(key), value) for key, value in all_type_counts.items())),
        }

def node_display(info: NodeInfo | None) -> str:
    if info is None:
        return ""
    pieces = [f"h{info.handle}"]
    if info.quest_id:
        pieces.append(f"id={info.quest_id}")
    pieces.append(info.short_type)
    if info.label:
        pieces.append(info.label)
    return " ".join(pieces)


def command_summary(explorer: QuestphaseExplorer, args: argparse.Namespace) -> None:
    summary = explorer.summary()
    if args.json:
        print_json(summary)
        return

    print(f"File: {summary['file']}")
    print(f"ArchiveFileName: {summary['archive_file']}")
    print(f"Root type: {summary['root_type']}")
    print(f"Graph nodes: {summary['nodes']}")
    print(f"Graph edges: {summary['edges']}")
    print(f"CR2W handles: {summary['handles']}")
    print(f"Embedded files: {summary['embedded_files']}")
    print(f"Phase prefabs: {summary['phase_prefabs']}")
    print()
    print("Node types:")
    for name, count in summary["node_types"].items():
        print(f"  {name}: {count}")
    print()
    print("References:")
    for name, count in summary["reference_types"].items():
        print(f"  {name}: {count}")


def command_nodes(explorer: QuestphaseExplorer, args: argparse.Namespace) -> None:
    nodes = list(explorer.nodes_by_handle.values())
    if args.type:
        type_filter = args.type.casefold()
        nodes = [
            node
            for node in nodes
            if type_filter in node.type.casefold() or type_filter in node.short_type.casefold()
        ]
    nodes, suffix = bounded(nodes, args.limit, args.offset)

    if args.json:
        print_json([asdict(node) for node in nodes])
    else:
        print_table(
            [
                {
                    "handle": f"h{node.handle}",
                    "id": node.quest_id,
                    "type": node.short_type,
                    "label": node.label,
                    "sockets": len(node.socket_handles),
                }
                for node in nodes
            ],
            [
                ("handle", "Handle"),
                ("id", "ID"),
                ("type", "Type"),
                ("sockets", "Sockets"),
                ("label", "Label"),
            ],
        )
        if args.sockets:
            print()
            for node in nodes:
                print(f"h{node.handle} id={node.quest_id} {node.short_type}")
                for socket_handle in node.socket_handles:
                    socket = explorer.socket_info_by_handle.get(socket_handle)
                    if socket:
                        print(f"  h{socket.handle} {socket.type} {socket.name}")
        if suffix:
            print()
            print(suffix)


def command_edges(explorer: QuestphaseExplorer, args: argparse.Namespace) -> None:
    edges = list(explorer.edges_by_handle.values())
    edges, suffix = bounded(edges, args.limit, args.offset)
    if args.json:
        print_json([asdict(edge) for edge in edges])
        return

    print_table(
        [
            {
                "handle": f"h{edge.handle}",
                "from": f"h{edge.source_node}:{edge.source_socket_name}",
                "to": f"h{edge.destination_node}:{edge.destination_socket_name}",
                "from_label": edge.source_node_label,
                "to_label": edge.destination_node_label,
            }
            for edge in edges
        ],
        [
            ("handle", "Conn"),
            ("from", "From"),
            ("to", "To"),
            ("from_label", "From Node"),
            ("to_label", "To Node"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_node(explorer: QuestphaseExplorer, args: argparse.Namespace) -> None:
    node = explorer.node_by_selector(args.selector)
    if args.raw:
        print_json(explorer.handle_json(node.handle))
        return

    print(node_display(node))
    print(f"Full type: {node.type}")
    print()
    print("Sockets:")
    for socket_handle in node.socket_handles:
        socket = explorer.socket_info_by_handle.get(socket_handle)
        if socket is None:
            print(f"  h{socket_handle} unresolved")
            continue
        print(f"  h{socket.handle} {socket.type} {socket.name}")
        for edge in explorer.edges_by_handle.values():
            if edge.source_socket == socket.handle:
                print(
                    f"    out h{edge.handle} -> h{edge.destination_node}:{edge.destination_socket_name} "
                    f"{edge.destination_node_label}"
                )
            if edge.destination_socket == socket.handle:
                print(
                    f"    in  h{edge.handle} <- h{edge.source_node}:{edge.source_socket_name} "
                    f"{edge.source_node_label}"
                )

    refs = explorer.node_refs(node.handle)
    if refs:
        print()
        print("References:")
        for ref in refs:
            print(f"  {ref.kind}: {ref.value}")


def command_handle(explorer: QuestphaseExplorer, args: argparse.Namespace) -> None:
    wrapper = explorer.handle_json(args.handle)
    if args.raw:
        print_json(wrapper)
        return

    handle = str(args.handle)
    kind = explorer.handle_kind(handle)
    print(f"h{handle} {kind or '(untyped handle)'}")
    path = explorer.handle_paths.get(handle)
    if path:
        print(f"Path: {path_to_string(path)}")
    node = explorer.nodes_by_handle.get(handle)
    if node:
        print(f"Graph node: {node_display(node)}")
    socket = explorer.socket_info_by_handle.get(handle)
    if socket:
        print(f"Socket owner: {node_display(explorer.nodes_by_handle.get(socket.owner_node))}")
        print(f"Socket: {socket.type} {socket.name}")
    edge = explorer.edges_by_handle.get(handle)
    if edge:
        print(
            f"Edge: h{edge.source_node}:{edge.source_socket_name} -> "
            f"h{edge.destination_node}:{edge.destination_socket_name}"
        )
    if not node and not socket and not edge:
        data = explorer.resolve_data(wrapper)
        if isinstance(data, dict):
            for key in sorted(data.keys()):
                if key == "$type":
                    continue
                value = data[key]
                if isinstance(value, (str, int, float, bool)) or value is None:
                    print(f"{key}: {value}")


def command_handles(explorer: QuestphaseExplorer, args: argparse.Namespace) -> None:
    rows: list[dict[str, Any]] = []
    for handle, wrapper in sorted(explorer.handle_map.items(), key=lambda item: int_or_text(item[0])):
        data = explorer.resolve_data(wrapper)
        type_name = str(data.get("$type", "")) if isinstance(data, dict) else ""
        if args.type:
            type_filter = args.type.casefold()
            if type_filter not in type_name.casefold() and type_filter not in short_type(type_name).casefold():
                continue

        path = explorer.handle_paths.get(handle, ("$",))
        owner = handle if handle in explorer.nodes_by_handle else explorer.owner_node_for_path(path)
        node = explorer.nodes_by_handle.get(handle)
        socket = explorer.socket_info_by_handle.get(handle)
        edge = explorer.edges_by_handle.get(handle)
        label = ""
        if node:
            label = node.label
        elif socket:
            label = f"{socket.type} {socket.name}".strip()
        elif edge:
            label = f"h{edge.source_node}:{edge.source_socket_name} -> h{edge.destination_node}:{edge.destination_socket_name}"
        elif isinstance(data, dict):
            label = first_scalar_label(data)

        rows.append(
            {
                "handle": f"h{handle}",
                "type": type_name,
                "short_type": short_type(type_name),
                "owner": node_display(explorer.nodes_by_handle.get(owner)),
                "path": path_to_string(path),
                "label": label,
            }
        )

    selected, suffix = bounded(rows, args.limit, args.offset)
    if args.json:
        print_json(selected)
        return

    print_table(
        selected,
        [
            ("handle", "Handle"),
            ("short_type", "Type"),
            ("owner", "Owner Node"),
            ("label", "Label"),
            ("path", "Path"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_refs(explorer: QuestphaseExplorer, args: argparse.Namespace) -> None:
    refs = explorer.refs()
    if args.kind:
        refs = [ref for ref in refs if ref.kind == args.kind]
    refs, suffix = bounded(refs, args.limit, args.offset)
    if args.json:
        print_json([asdict(ref) for ref in refs])
        return

    print_table(
        [
            {
                "kind": ref.kind,
                "value": ref.value,
                "owner": ref.owner_node_label,
                "path": ref.path,
            }
            for ref in refs
        ],
        [
            ("kind", "Kind"),
            ("value", "Value"),
            ("owner", "Owner Node"),
            ("path", "Path"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_search(explorer: QuestphaseExplorer, args: argparse.Namespace) -> None:
    matches = explorer.search(args.terms, args.limit)
    if args.json:
        print_json([{"path": path, "value": value} for path, value in matches])
        return
    print_table(
        [{"path": path, "value": value} for path, value in matches],
        [("path", "Path"), ("value", "Value")],
    )
    if args.limit > 0 and len(matches) >= args.limit:
        print()
        print(f"Stopped at --limit {args.limit}. Use --limit 0 for all matches.")


def command_types(explorer: QuestphaseExplorer, args: argparse.Namespace) -> None:
    counts = collect_type_counts(explorer.data)
    rows = [
        {"type": type_name, "short": short_type(type_name), "count": count}
        for type_name, count in sorted(counts.items())
    ]
    if args.json:
        print_json(rows)
    else:
        print_table(rows, [("count", "Count"), ("short", "Short"), ("type", "Type")])


def command_dot(explorer: QuestphaseExplorer, args: argparse.Namespace) -> None:
    print("digraph questphase {")
    print('  rankdir="LR";')
    print('  node [shape=box, fontname="Consolas"];')
    for node in explorer.nodes_by_handle.values():
        label = f"h{node.handle}"
        if node.quest_id:
            label += f" id={node.quest_id}"
        label += f"\\n{node.short_type}"
        if node.label:
            label += f"\\n{node.label}"
        print(f'  n{node.handle} [label="{dot_escape(label)}"];')
    for edge in explorer.edges_by_handle.values():
        edge_label = f"h{edge.handle} {edge.source_socket_name}->{edge.destination_socket_name}"
        print(f'  n{edge.source_node} -> n{edge.destination_node} [label="{dot_escape(edge_label)}"];')
    print("}")


def dot_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Explore a WolvenKit-deserialized questphase JSON without dumping the whole file."
    )
    parser.add_argument(
        "-f",
        "--file",
        dest="file",
        default=None,
        help=f"Deserialized questphase JSON. Default: {DEFAULT_QUESTPHASE}",
    )
    subparsers = parser.add_subparsers(dest="command")

    summary = subparsers.add_parser("summary", help="Show high-level graph, handle, and reference counts.")
    summary.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    summary.set_defaults(func=command_summary)

    nodes = subparsers.add_parser("nodes", help="List graph nodes.")
    nodes.add_argument("--type", help="Filter by full or short node type substring.")
    nodes.add_argument("--sockets", action="store_true", help="Also print each node's sockets.")
    nodes.add_argument("--limit", type=int, default=200, help="Maximum rows to print. Use 0 for all.")
    nodes.add_argument("--offset", type=int, default=0, help="Skip this many rows before printing.")
    nodes.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    nodes.set_defaults(func=command_nodes)

    edges = subparsers.add_parser("edges", help="List directed graph edges.")
    edges.add_argument("--limit", type=int, default=200, help="Maximum rows to print. Use 0 for all.")
    edges.add_argument("--offset", type=int, default=0, help="Skip this many rows before printing.")
    edges.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    edges.set_defaults(func=command_edges)

    node = subparsers.add_parser("node", help="Inspect one graph node by quest id or handle:<HandleId>.")
    node.add_argument("selector", help="Quest node id, HandleId, handle:<HandleId>, or id:<quest id>.")
    node.add_argument("--raw", action="store_true", help="Dump the raw handle JSON for this node.")
    node.set_defaults(func=command_node)

    handle = subparsers.add_parser("handle", help="Inspect any CR2W HandleId.")
    handle.add_argument("handle", help="HandleId to inspect.")
    handle.add_argument("--raw", action="store_true", help="Dump the raw handle JSON.")
    handle.set_defaults(func=command_handle)

    handles = subparsers.add_parser("handles", help="List CR2W handles, optionally filtered by type.")
    handles.add_argument("--type", help="Filter by full or short $type substring.")
    handles.add_argument("--limit", type=int, default=200, help="Maximum rows to print. Use 0 for all.")
    handles.add_argument("--offset", type=int, default=0, help="Skip this many rows before printing.")
    handles.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    handles.set_defaults(func=command_handles)

    refs = subparsers.add_parser("refs", help="List resource, NodeRef, depot, and journal references.")
    refs.add_argument("--kind", choices=["resource", "node_ref", "depot_path", "journal_path"])
    refs.add_argument("--limit", type=int, default=200, help="Maximum rows to print. Use 0 for all.")
    refs.add_argument("--offset", type=int, default=0, help="Skip this many rows before printing.")
    refs.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    refs.set_defaults(func=command_refs)

    search = subparsers.add_parser("search", help="Search scalar keys and values by substring.")
    search.add_argument("terms", nargs="+", help="Case-insensitive terms. All terms must match.")
    search.add_argument("--limit", type=int, default=50, help="Maximum matches to print. Use 0 for all.")
    search.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    search.set_defaults(func=command_search)

    types = subparsers.add_parser("types", help="Count every CR2W $type in the file.")
    types.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    types.set_defaults(func=command_types)

    dot = subparsers.add_parser("dot", help="Emit Graphviz DOT for the quest graph.")
    dot.set_defaults(func=command_dot)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        args.command = "summary"
        args.json = False
        args.func = command_summary

    file_path = Path(args.file) if args.file else DEFAULT_QUESTPHASE
    explorer = QuestphaseExplorer(file_path)
    args.func(explorer, args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
