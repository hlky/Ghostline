#!/usr/bin/env python3
"""Explore a WolvenKit-deserialized .scene CR2W-JSON file."""

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
    typed_id,
    typed_value,
    walk,
)


DEFAULT_SCENE = Path("source/raw/mod/gq000/scenes/gq000_patch_meet.scene.json")


@dataclass(frozen=True)
class ActorInfo:
    actor_id: str
    name: str
    kind: str
    acquisition: str
    reference: str
    record: str


@dataclass(frozen=True)
class SceneNodeInfo:
    handle: str
    node_id: str
    type: str
    short_type: str
    label: str
    events: int
    duration: str
    outputs: int
    quest_node_type: str
    quest_node_id: str


@dataclass(frozen=True)
class SceneEdgeInfo:
    source_node: str
    source_node_label: str
    source_socket: str
    destination_node: str
    destination_node_label: str
    destination_socket: str


@dataclass(frozen=True)
class EventInfo:
    handle: str
    node_id: str
    event_type: str
    screenplay_line_id: str
    locstring_id: str
    speaker: str
    addressee: str
    start_time: str
    duration: str


@dataclass(frozen=True)
class RefInfo:
    kind: str
    value: str
    path: str
    owner_node: str
    owner_node_label: str


class SceneExplorer:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.data = load_json(path)
        self.handle_map: dict[str, dict[str, Any]] = {}
        self.handle_paths: dict[str, tuple[Any, ...]] = {}
        self.parent_node_by_path: dict[tuple[Any, ...], str] = {}
        self.nodes_by_id: dict[str, SceneNodeInfo] = {}
        self.nodes_by_handle: dict[str, SceneNodeInfo] = {}
        self.node_data_by_id: dict[str, dict[str, Any]] = {}
        self.screenplay_lines_by_item_id: dict[str, dict[str, Any]] = {}
        self.screenplay_options_by_item_id: dict[str, dict[str, Any]] = {}
        self.loc_payload_by_locstring: dict[str, str] = {}
        self.actor_name_by_id: dict[str, str] = {}
        self._index_handles()
        self._index_actors()
        self._index_screenplay()
        self._index_scene_nodes()

    def _index_handles(self) -> None:
        for path, value in walk(self.data):
            if isinstance(value, dict) and "HandleId" in value:
                handle = str(value["HandleId"])
                self.handle_map[handle] = value
                self.handle_paths[handle] = path

    def _index_actors(self) -> None:
        for actor in self.raw_actors:
            actor_id = str(typed_id(actor.get("actorId"), ""))
            name = actor.get("actorName") or actor.get("playerName") or actor_id
            self.actor_name_by_id[actor_id] = str(name)

    def _index_screenplay(self) -> None:
        for line in self.screenplay_store.get("lines", []):
            item_id = str(typed_id(line.get("itemId"), ""))
            if item_id:
                self.screenplay_lines_by_item_id[item_id] = line
        for option in self.screenplay_store.get("options", []):
            item_id = str(typed_id(option.get("itemId"), ""))
            if item_id:
                self.screenplay_options_by_item_id[item_id] = option

        loc_store = self.root_chunk.get("locStore", {})
        if not isinstance(loc_store, dict):
            return
        payloads = loc_store.get("vpEntries", [])
        for descriptor in loc_store.get("vdEntries", []):
            locstring = str(nested_get(descriptor, ("locstringId", "ruid"), ""))
            index = descriptor.get("vpeIndex")
            if locstring and isinstance(index, int) and 0 <= index < len(payloads):
                payload = payloads[index]
                if isinstance(payload, dict):
                    content = payload.get("content")
                    if content is not None:
                        self.loc_payload_by_locstring[locstring] = str(content)

    def _index_scene_nodes(self) -> None:
        for wrapper in self.graph_nodes:
            if not isinstance(wrapper, dict):
                continue
            handle = str(wrapper.get("HandleId", ""))
            node_data = self.resolve_data(wrapper)
            if not isinstance(node_data, dict):
                continue
            node_id = str(typed_id(node_data.get("nodeId"), ""))
            if not node_id:
                continue
            quest_node = self.resolve_data(node_data.get("questNode"))
            quest_type = ""
            quest_id = ""
            if isinstance(quest_node, dict):
                quest_type = short_type(str(quest_node.get("$type", "")))
                quest_id = str(quest_node.get("id", ""))
            info = SceneNodeInfo(
                handle=handle,
                node_id=node_id,
                type=str(node_data.get("$type", "")),
                short_type=short_type(str(node_data.get("$type", ""))),
                label=self.describe_node(node_data),
                events=len(node_data.get("events", [])) if isinstance(node_data.get("events"), list) else 0,
                duration=str(nested_get(node_data, ("sectionDuration", "stu"), "")),
                outputs=len(node_data.get("outputSockets", [])) if isinstance(node_data.get("outputSockets"), list) else 0,
                quest_node_type=quest_type,
                quest_node_id=quest_id,
            )
            self.nodes_by_id[node_id] = info
            if handle:
                self.nodes_by_handle[handle] = info

            node_path = self.handle_paths.get(handle)
            if node_path is not None:
                for child_path, _ in walk(node_data, node_path + ("Data",)):
                    self.parent_node_by_path[child_path] = node_id

    @property
    def root_chunk(self) -> dict[str, Any]:
        root = self.data.get("Data", {}).get("RootChunk", {})
        return root if isinstance(root, dict) else {}

    @property
    def raw_actors(self) -> list[dict[str, Any]]:
        actors: list[dict[str, Any]] = []
        for key in ("actors", "playerActors"):
            value = self.root_chunk.get(key, [])
            if isinstance(value, list):
                actors.extend(actor for actor in value if isinstance(actor, dict))
        return actors

    @property
    def scene_graph(self) -> dict[str, Any]:
        graph = self.root_chunk.get("sceneGraph", {})
        data = graph.get("Data", {}) if isinstance(graph, dict) else {}
        return data if isinstance(data, dict) else {}

    @property
    def graph_nodes(self) -> list[Any]:
        nodes = self.scene_graph.get("graph", [])
        return nodes if isinstance(nodes, list) else []

    @property
    def screenplay_store(self) -> dict[str, Any]:
        store = self.root_chunk.get("screenplayStore", {})
        return store if isinstance(store, dict) else {}

    @property
    def archive_file_name(self) -> str:
        header = self.data.get("Header", {})
        return str(header.get("ArchiveFileName", "")) if isinstance(header, dict) else ""

    def resolve_data(self, value: Any) -> Any:
        if not isinstance(value, dict):
            return value
        if "HandleRefId" in value:
            value = self.handle_map.get(str(value["HandleRefId"]), value)
        if isinstance(value, dict) and "Data" in value:
            return value["Data"]
        return value

    def describe_node(self, node_data: dict[str, Any]) -> str:
        node_type = node_data.get("$type", "")
        if node_type == "scnStartNode":
            return "start"
        if node_type == "scnEndNode":
            return "end"
        if node_type == "scnSectionNode":
            line_ids = [
                str(typed_id(event.get("Data", {}).get("screenplayLineId"), ""))
                for event in node_data.get("events", [])
                if isinstance(event, dict)
            ]
            speakers = []
            for line_id in line_ids:
                line = self.screenplay_lines_by_item_id.get(line_id)
                speaker = self.actor_label(typed_id(line.get("speaker"), "")) if isinstance(line, dict) else ""
                if speaker and speaker not in speakers:
                    speakers.append(speaker)
            label = ", ".join(speakers)
            return label or f"{len(line_ids)} event(s)"
        if node_type == "scnChoiceNode":
            captions = [str(typed_value(option.get("caption"), "")) for option in node_data.get("options", [])]
            return " | ".join(caption for caption in captions if caption)
        if node_type == "scnQuestNode":
            quest_data = self.resolve_data(node_data.get("questNode"))
            if isinstance(quest_data, dict):
                pieces = [short_type(str(quest_data.get("$type", "")))]
                quest_id = quest_data.get("id")
                if quest_id not in (None, ""):
                    pieces.append(f"id={quest_id}")
                condition = self.describe_condition(quest_data)
                if condition:
                    pieces.append(condition)
                return " ".join(piece for piece in pieces if piece)
            return "quest node"
        return first_scalar_label(node_data) or short_type(str(node_type))

    def describe_condition(self, value: dict[str, Any]) -> str:
        condition = self.resolve_data(value.get("condition"))
        if not isinstance(condition, dict):
            return ""
        trigger = typed_value(condition.get("triggerAreaRef"), "")
        if trigger:
            return str(trigger)
        conditions = condition.get("conditions", [])
        if isinstance(conditions, list):
            triggers = []
            for child in conditions:
                child_data = self.resolve_data(child)
                if isinstance(child_data, dict):
                    trigger = typed_value(child_data.get("triggerAreaRef"), "")
                    if trigger:
                        triggers.append(str(trigger))
            return ", ".join(triggers)
        return ""

    def actor_label(self, actor_id: Any) -> str:
        actor_id_text = str(actor_id)
        name = self.actor_name_by_id.get(actor_id_text, "")
        return f"{name}({actor_id_text})" if name else actor_id_text

    def actors(self) -> list[ActorInfo]:
        rows: list[ActorInfo] = []
        for actor in self.raw_actors:
            actor_id = str(typed_id(actor.get("actorId"), ""))
            name = str(actor.get("actorName") or actor.get("playerName") or actor_id)
            ref = str(typed_value(nested_get(actor, ("spawnDespawnParams", "spawnMarkerNodeRef"), {}), ""))
            if not ref:
                ref = str(typed_value(nested_get(actor, ("findActorInWorldParams", "actorRef", "reference"), {}), ""))
            record = str(
                typed_value(nested_get(actor, ("spawnDespawnParams", "specRecordId"), {}), "")
                or typed_value(actor.get("specCharacterRecordId"), "")
                or typed_value(nested_get(actor, ("findActorInContextParams", "specRecordId"), {}), "")
            )
            rows.append(
                ActorInfo(
                    actor_id=actor_id,
                    name=name,
                    kind=short_type(str(actor.get("$type", ""))),
                    acquisition=str(actor.get("acquisitionPlan", "")),
                    reference=ref,
                    record=record,
                )
            )
        return rows

    def edges(self) -> list[SceneEdgeInfo]:
        edges: list[SceneEdgeInfo] = []
        for node in self.graph_nodes:
            node_data = self.resolve_data(node)
            if not isinstance(node_data, dict):
                continue
            source_id = str(typed_id(node_data.get("nodeId"), ""))
            source_info = self.nodes_by_id.get(source_id)
            for output in node_data.get("outputSockets", []):
                source_socket = socket_stamp_label(output.get("stamp"))
                for destination in output.get("destinations", []):
                    destination_id = str(typed_id(destination.get("nodeId"), ""))
                    destination_info = self.nodes_by_id.get(destination_id)
                    edges.append(
                        SceneEdgeInfo(
                            source_node=source_id,
                            source_node_label=node_display(source_info),
                            source_socket=source_socket,
                            destination_node=destination_id,
                            destination_node_label=node_display(destination_info),
                            destination_socket=socket_stamp_label(destination.get("isockStamp")),
                        )
                    )
        return edges

    def events(self) -> list[EventInfo]:
        events: list[EventInfo] = []
        for node in self.graph_nodes:
            node_data = self.resolve_data(node)
            if not isinstance(node_data, dict):
                continue
            node_id = str(typed_id(node_data.get("nodeId"), ""))
            for event in node_data.get("events", []):
                if not isinstance(event, dict):
                    continue
                event_data = self.resolve_data(event)
                if not isinstance(event_data, dict):
                    continue
                line_id = str(typed_id(event_data.get("screenplayLineId"), ""))
                line = self.screenplay_lines_by_item_id.get(line_id, {})
                locstring = str(nested_get(line, ("locstringId", "ruid"), ""))
                speaker = self.actor_label(typed_id(line.get("speaker"), "")) if isinstance(line, dict) else ""
                addressee = self.actor_label(typed_id(line.get("addressee"), "")) if isinstance(line, dict) else ""
                events.append(
                    EventInfo(
                        handle=str(event.get("HandleId", "")),
                        node_id=node_id,
                        event_type=short_type(str(event_data.get("$type", ""))),
                        screenplay_line_id=line_id,
                        locstring_id=locstring,
                        speaker=speaker,
                        addressee=addressee,
                        start_time=str(event_data.get("startTime", "")),
                        duration=str(event_data.get("duration", "")),
                    )
                )
        return events

    def refs(self) -> list[RefInfo]:
        refs: list[RefInfo] = []
        for path, value in walk(self.data):
            if not isinstance(value, dict):
                continue
            kind = ""
            ref_value: Any = None
            value_type = value.get("$type")
            if value_type in ("ResourcePath", "NodeRef", "TweakDBID"):
                kind = value_type
                ref_value = value.get("$value")
            elif "DepotPath" in value and isinstance(value.get("DepotPath"), dict):
                kind = "DepotPath"
                ref_value = value["DepotPath"].get("$value")
            elif "realPath" in value and "className" in value:
                kind = "journal_path"
                ref_value = value.get("realPath")
            elif value_type == "scnlocLocstringId":
                kind = "locstring"
                ref_value = value.get("ruid")

            if kind and ref_value not in (None, "", "0", "None"):
                owner = self.owner_node_for_path(path)
                refs.append(
                    RefInfo(
                        kind=kind,
                        value=str(ref_value),
                        path=path_to_string(path),
                        owner_node=owner,
                        owner_node_label=node_display(self.nodes_by_id.get(owner)),
                    )
                )
        return refs

    def owner_node_for_path(self, path: tuple[Any, ...]) -> str:
        for length in range(len(path), 0, -1):
            owner = self.parent_node_by_path.get(path[:length])
            if owner:
                return owner
        return ""

    def node_by_selector(self, selector: str) -> SceneNodeInfo:
        selector = selector.strip()
        if selector.lower().startswith(("handle:", "h:")):
            handle = selector.split(":", 1)[1]
            node = self.nodes_by_handle.get(handle)
            if node:
                return node
            raise SystemExit(f"No scene graph node with handle {handle}")
        if selector.lower().startswith(("node:", "id:")):
            selector = selector.split(":", 1)[1]
        node = self.nodes_by_id.get(selector)
        if node is None:
            raise SystemExit(f"No scene graph node with node id {selector}")
        return node

    def handle_json(self, handle: str) -> dict[str, Any]:
        wrapper = self.handle_map.get(str(handle))
        if wrapper is None:
            raise SystemExit(f"No object with HandleId {handle}")
        return wrapper

    def handle_kind(self, handle: str) -> str:
        data = self.resolve_data(self.handle_map.get(str(handle), {}))
        return str(data.get("$type", "")) if isinstance(data, dict) else ""

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

    def summary(self) -> dict[str, Any]:
        root_arrays = {
            key: len(value)
            for key, value in sorted(self.root_chunk.items())
            if isinstance(value, list)
        }
        return {
            "file": str(self.path),
            "archive_file": self.archive_file_name,
            "root_type": self.root_chunk.get("$type", ""),
            "actors": len(self.root_chunk.get("actors", [])),
            "player_actors": len(self.root_chunk.get("playerActors", [])),
            "scene_nodes": len(self.nodes_by_id),
            "scene_edges": len(self.edges()),
            "section_events": len(self.events()),
            "screenplay_lines": len(self.screenplay_store.get("lines", [])),
            "screenplay_options": len(self.screenplay_store.get("options", [])),
            "handles": len(self.handle_map),
            "node_types": dict(sorted(Counter(node.short_type for node in self.nodes_by_id.values()).items())),
            "reference_types": dict(sorted(Counter(ref.kind for ref in self.refs()).items())),
            "root_arrays": root_arrays,
            "all_types": dict(sorted(collect_type_counts(self.data).items())),
        }


def socket_stamp_label(stamp: Any) -> str:
    if not isinstance(stamp, dict):
        return ""
    return f"{stamp.get('name', '')}:{stamp.get('ordinal', '')}"


def node_display(info: SceneNodeInfo | None) -> str:
    if info is None:
        return ""
    pieces = [f"n{info.node_id}", f"h{info.handle}", info.short_type]
    if info.label:
        pieces.append(info.label)
    return " ".join(piece for piece in pieces if piece)


def dot_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def command_summary(explorer: SceneExplorer, args: argparse.Namespace) -> None:
    summary = explorer.summary()
    if args.json:
        print_json(summary)
        return
    print(f"File: {summary['file']}")
    print(f"ArchiveFileName: {summary['archive_file']}")
    print(f"Root type: {summary['root_type']}")
    print(f"Actors: {summary['actors']} NPC, {summary['player_actors']} player")
    print(f"Scene graph: {summary['scene_nodes']} nodes, {summary['scene_edges']} edges")
    print(f"Section events: {summary['section_events']}")
    print(f"Screenplay: {summary['screenplay_lines']} lines, {summary['screenplay_options']} options")
    print(f"CR2W handles: {summary['handles']}")
    print()
    print("Node types:")
    for name, count in summary["node_types"].items():
        print(f"  {name}: {count}")
    print()
    print("References:")
    for name, count in summary["reference_types"].items():
        print(f"  {name}: {count}")


def command_actors(explorer: SceneExplorer, args: argparse.Namespace) -> None:
    actors = explorer.actors()
    if args.json:
        print_json([asdict(actor) for actor in actors])
        return
    print_table(
        [asdict(actor) for actor in actors],
        [
            ("actor_id", "ID"),
            ("name", "Name"),
            ("kind", "Kind"),
            ("acquisition", "Acquisition"),
            ("reference", "Reference"),
            ("record", "Record"),
        ],
    )


def command_nodes(explorer: SceneExplorer, args: argparse.Namespace) -> None:
    nodes = list(explorer.nodes_by_id.values())
    if args.type:
        type_filter = args.type.casefold()
        nodes = [
            node
            for node in nodes
            if type_filter in node.type.casefold() or type_filter in node.short_type.casefold()
        ]
    selected, suffix = bounded(nodes, args.limit, args.offset)
    if args.json:
        print_json([asdict(node) for node in selected])
        return
    print_table(
        [
            {
                "node": f"n{node.node_id}",
                "handle": f"h{node.handle}",
                "type": node.short_type,
                "events": node.events,
                "duration": node.duration,
                "outputs": node.outputs,
                "quest": f"{node.quest_node_type} {node.quest_node_id}".strip(),
                "label": node.label,
            }
            for node in selected
        ],
        [
            ("node", "Node"),
            ("handle", "Handle"),
            ("type", "Type"),
            ("events", "Events"),
            ("duration", "Duration"),
            ("outputs", "Out"),
            ("quest", "Quest"),
            ("label", "Label"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_edges(explorer: SceneExplorer, args: argparse.Namespace) -> None:
    edges, suffix = bounded(explorer.edges(), args.limit, args.offset)
    if args.json:
        print_json([asdict(edge) for edge in edges])
        return
    print_table(
        [
            {
                "from": f"n{edge.source_node}:{edge.source_socket}",
                "to": f"n{edge.destination_node}:{edge.destination_socket}",
                "from_label": edge.source_node_label,
                "to_label": edge.destination_node_label,
            }
            for edge in edges
        ],
        [("from", "From"), ("to", "To"), ("from_label", "From Node"), ("to_label", "To Node")],
    )
    if suffix:
        print()
        print(suffix)


def command_node(explorer: SceneExplorer, args: argparse.Namespace) -> None:
    node = explorer.node_by_selector(args.selector)
    wrapper = explorer.handle_json(node.handle)
    node_data = explorer.resolve_data(wrapper)
    if args.raw:
        print_json(wrapper)
        return
    print(node_display(node))
    print(f"Full type: {node.type}")
    if node.quest_node_type:
        print(f"Embedded quest node: {node.quest_node_type} {node.quest_node_id}".strip())
    print()
    print("Outgoing:")
    outgoing = [edge for edge in explorer.edges() if edge.source_node == node.node_id]
    if outgoing:
        for edge in outgoing:
            print(f"  {edge.source_socket} -> n{edge.destination_node}:{edge.destination_socket} {edge.destination_node_label}")
    else:
        print("  (none)")
    print()
    print("Incoming:")
    incoming = [edge for edge in explorer.edges() if edge.destination_node == node.node_id]
    if incoming:
        for edge in incoming:
            print(f"  n{edge.source_node}:{edge.source_socket} -> {edge.destination_socket} {edge.source_node_label}")
    else:
        print("  (none)")

    if isinstance(node_data, dict) and node_data.get("events"):
        print()
        print("Events:")
        for event in [event for event in explorer.events() if event.node_id == node.node_id]:
            print(
                f"  h{event.handle} {event.event_type} line={event.screenplay_line_id} "
                f"speaker={event.speaker} start={event.start_time} duration={event.duration}"
            )

    node_refs = [ref for ref in explorer.refs() if ref.owner_node == node.node_id]
    if node_refs:
        print()
        print("References:")
        for ref in node_refs:
            print(f"  {ref.kind}: {ref.value}")


def command_events(explorer: SceneExplorer, args: argparse.Namespace) -> None:
    events = explorer.events()
    if args.node:
        node_id = args.node.split(":", 1)[-1]
        events = [event for event in events if event.node_id == node_id]
    selected, suffix = bounded(events, args.limit, args.offset)
    if args.json:
        print_json([asdict(event) for event in selected])
        return
    print_table(
        [
            {
                "handle": f"h{event.handle}",
                "node": f"n{event.node_id}",
                "type": event.event_type,
                "line": event.screenplay_line_id,
                "locstring": event.locstring_id,
                "speaker": event.speaker,
                "addressee": event.addressee,
                "start": event.start_time,
                "duration": event.duration,
            }
            for event in selected
        ],
        [
            ("handle", "Handle"),
            ("node", "Node"),
            ("type", "Type"),
            ("line", "Line"),
            ("locstring", "Locstring"),
            ("speaker", "Speaker"),
            ("addressee", "To"),
            ("start", "Start"),
            ("duration", "Duration"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_lines(explorer: SceneExplorer, args: argparse.Namespace) -> None:
    rows = []
    event_by_line = {event.screenplay_line_id: event for event in explorer.events()}
    for item_id, line in sorted(explorer.screenplay_lines_by_item_id.items(), key=lambda item: int_or_text(item[0])):
        rows.append(
            {
                "item_id": item_id,
                "locstring": nested_get(line, ("locstringId", "ruid"), ""),
                "speaker": explorer.actor_label(typed_id(line.get("speaker"), "")),
                "addressee": explorer.actor_label(typed_id(line.get("addressee"), "")),
                "event": f"n{event_by_line[item_id].node_id}/h{event_by_line[item_id].handle}" if item_id in event_by_line else "",
            }
        )
    selected, suffix = bounded(rows, args.limit, args.offset)
    if args.json:
        print_json(selected)
        return
    print_table(
        selected,
        [
            ("item_id", "Item"),
            ("locstring", "Locstring"),
            ("speaker", "Speaker"),
            ("addressee", "To"),
            ("event", "Event"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_choices(explorer: SceneExplorer, args: argparse.Namespace) -> None:
    rows = []
    for node in explorer.graph_nodes:
        node_data = explorer.resolve_data(node)
        if not isinstance(node_data, dict) or node_data.get("$type") != "scnChoiceNode":
            continue
        node_id = str(typed_id(node_data.get("nodeId"), ""))
        for index, option in enumerate(node_data.get("options", [])):
            item_id = str(typed_id(option.get("screenplayOptionId"), ""))
            screenplay_option = explorer.screenplay_options_by_item_id.get(item_id, {})
            locstring = str(nested_get(screenplay_option, ("locstringId", "ruid"), ""))
            rows.append(
                {
                    "node": f"n{node_id}",
                    "index": index,
                    "item_id": item_id,
                    "caption": typed_value(option.get("caption"), ""),
                    "locstring": locstring,
                    "text": explorer.loc_payload_by_locstring.get(locstring, ""),
                    "single": option.get("isSingleChoice", ""),
                }
            )
    selected, suffix = bounded(rows, args.limit, args.offset)
    if args.json:
        print_json(selected)
        return
    print_table(
        selected,
        [
            ("node", "Node"),
            ("index", "#"),
            ("item_id", "Item"),
            ("caption", "Caption"),
            ("locstring", "Locstring"),
            ("text", "Text"),
            ("single", "Single"),
        ],
    )
    if suffix:
        print()
        print(suffix)


def command_refs(explorer: SceneExplorer, args: argparse.Namespace) -> None:
    refs = explorer.refs()
    if args.kind:
        refs = [ref for ref in refs if ref.kind == args.kind]
    selected, suffix = bounded(refs, args.limit, args.offset)
    if args.json:
        print_json([asdict(ref) for ref in selected])
        return
    print_table(
        [
            {
                "kind": ref.kind,
                "value": ref.value,
                "owner": ref.owner_node_label,
                "path": ref.path,
            }
            for ref in selected
        ],
        [("kind", "Kind"), ("value", "Value"), ("owner", "Owner Node"), ("path", "Path")],
    )
    if suffix:
        print()
        print(suffix)


def command_handles(explorer: SceneExplorer, args: argparse.Namespace) -> None:
    rows = []
    for handle, wrapper in sorted(explorer.handle_map.items(), key=lambda item: int_or_text(item[0])):
        data = explorer.resolve_data(wrapper)
        type_name = str(data.get("$type", "")) if isinstance(data, dict) else ""
        if args.type:
            type_filter = args.type.casefold()
            if type_filter not in type_name.casefold() and type_filter not in short_type(type_name).casefold():
                continue
        path = explorer.handle_paths.get(handle, ("$",))
        owner = handle if handle in explorer.nodes_by_handle else explorer.owner_node_for_path(path)
        label = first_scalar_label(data) if isinstance(data, dict) else ""
        node = explorer.nodes_by_handle.get(handle)
        if node:
            label = node.label
        rows.append(
            {
                "handle": f"h{handle}",
                "type": short_type(type_name),
                "owner": node_display(explorer.nodes_by_id.get(owner)),
                "label": label,
                "path": path_to_string(path),
            }
        )
    selected, suffix = bounded(rows, args.limit, args.offset)
    if args.json:
        print_json(selected)
        return
    print_table(
        selected,
        [("handle", "Handle"), ("type", "Type"), ("owner", "Owner Node"), ("label", "Label"), ("path", "Path")],
    )
    if suffix:
        print()
        print(suffix)


def command_handle(explorer: SceneExplorer, args: argparse.Namespace) -> None:
    wrapper = explorer.handle_json(args.handle)
    if args.raw:
        print_json(wrapper)
        return
    handle = str(args.handle)
    kind = explorer.handle_kind(handle)
    path = explorer.handle_paths.get(handle)
    print(f"h{handle} {kind or '(untyped handle)'}")
    if path:
        print(f"Path: {path_to_string(path)}")
        owner = explorer.owner_node_for_path(path)
        if owner:
            print(f"Owner scene node: {node_display(explorer.nodes_by_id.get(owner))}")
    node = explorer.nodes_by_handle.get(handle)
    if node:
        print(f"Scene node: {node_display(node)}")


def command_search(explorer: SceneExplorer, args: argparse.Namespace) -> None:
    matches = explorer.search(args.terms, args.limit)
    if args.json:
        print_json([{"path": path, "value": value} for path, value in matches])
        return
    print_table([{"path": path, "value": value} for path, value in matches], [("path", "Path"), ("value", "Value")])
    if args.limit > 0 and len(matches) >= args.limit:
        print()
        print(f"Stopped at --limit {args.limit}. Use --limit 0 for all matches.")


def command_types(explorer: SceneExplorer, args: argparse.Namespace) -> None:
    rows = [
        {"count": count, "short": short_type(type_name), "type": type_name}
        for type_name, count in sorted(collect_type_counts(explorer.data).items())
    ]
    if args.json:
        print_json(rows)
    else:
        print_table(rows, [("count", "Count"), ("short", "Short"), ("type", "Type")])


def command_dot(explorer: SceneExplorer, args: argparse.Namespace) -> None:
    print("digraph scene {")
    print('  rankdir="LR";')
    print('  node [shape=box, fontname="Consolas"];')
    for node in explorer.nodes_by_id.values():
        label = f"n{node.node_id} h{node.handle}\\n{node.short_type}"
        if node.label:
            label += f"\\n{node.label}"
        print(f'  n{node.node_id} [label="{dot_escape(label)}"];')
    for edge in explorer.edges():
        label = f"{edge.source_socket}->{edge.destination_socket}"
        print(f'  n{edge.source_node} -> n{edge.destination_node} [label="{dot_escape(label)}"];')
    print("}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Explore a WolvenKit-deserialized .scene CR2W-JSON file.")
    parser.add_argument("-f", "--file", default=str(DEFAULT_SCENE), help=f"Scene JSON. Default: {DEFAULT_SCENE}")
    subparsers = parser.add_subparsers(dest="command")

    summary = subparsers.add_parser("summary", help="Show high-level scene counts.")
    summary.add_argument("--json", action="store_true")
    summary.set_defaults(func=command_summary)

    actors = subparsers.add_parser("actors", help="List scene actors and player actors.")
    actors.add_argument("--json", action="store_true")
    actors.set_defaults(func=command_actors)

    nodes = subparsers.add_parser("nodes", help="List scene graph nodes.")
    nodes.add_argument("--type", help="Filter by full or short node type substring.")
    nodes.add_argument("--limit", type=int, default=200)
    nodes.add_argument("--offset", type=int, default=0)
    nodes.add_argument("--json", action="store_true")
    nodes.set_defaults(func=command_nodes)

    edges = subparsers.add_parser("edges", help="List scene graph edges.")
    edges.add_argument("--limit", type=int, default=200)
    edges.add_argument("--offset", type=int, default=0)
    edges.add_argument("--json", action="store_true")
    edges.set_defaults(func=command_edges)

    node = subparsers.add_parser("node", help="Inspect one scene graph node by node id or handle:<HandleId>.")
    node.add_argument("selector")
    node.add_argument("--raw", action="store_true")
    node.set_defaults(func=command_node)

    events = subparsers.add_parser("events", help="List section events.")
    events.add_argument("--node", help="Only events for this scene node id.")
    events.add_argument("--limit", type=int, default=200)
    events.add_argument("--offset", type=int, default=0)
    events.add_argument("--json", action="store_true")
    events.set_defaults(func=command_events)

    lines = subparsers.add_parser("lines", help="List screenplay dialog lines.")
    lines.add_argument("--limit", type=int, default=200)
    lines.add_argument("--offset", type=int, default=0)
    lines.add_argument("--json", action="store_true")
    lines.set_defaults(func=command_lines)

    choices = subparsers.add_parser("choices", help="List choice options and embedded option text.")
    choices.add_argument("--limit", type=int, default=200)
    choices.add_argument("--offset", type=int, default=0)
    choices.add_argument("--json", action="store_true")
    choices.set_defaults(func=command_choices)

    refs = subparsers.add_parser("refs", help="List resource, NodeRef, TweakDBID, locstring, and journal refs.")
    refs.add_argument("--kind", choices=["ResourcePath", "NodeRef", "TweakDBID", "DepotPath", "journal_path", "locstring"])
    refs.add_argument("--limit", type=int, default=200)
    refs.add_argument("--offset", type=int, default=0)
    refs.add_argument("--json", action="store_true")
    refs.set_defaults(func=command_refs)

    handles = subparsers.add_parser("handles", help="List CR2W handles.")
    handles.add_argument("--type", help="Filter by full or short $type substring.")
    handles.add_argument("--limit", type=int, default=200)
    handles.add_argument("--offset", type=int, default=0)
    handles.add_argument("--json", action="store_true")
    handles.set_defaults(func=command_handles)

    handle = subparsers.add_parser("handle", help="Inspect any CR2W HandleId.")
    handle.add_argument("handle")
    handle.add_argument("--raw", action="store_true")
    handle.set_defaults(func=command_handle)

    search = subparsers.add_parser("search", help="Search scalar keys and values by substring.")
    search.add_argument("terms", nargs="+")
    search.add_argument("--limit", type=int, default=50)
    search.add_argument("--json", action="store_true")
    search.set_defaults(func=command_search)

    types = subparsers.add_parser("types", help="Count every CR2W $type in the file.")
    types.add_argument("--json", action="store_true")
    types.set_defaults(func=command_types)

    dot = subparsers.add_parser("dot", help="Emit Graphviz DOT for the scene graph.")
    dot.set_defaults(func=command_dot)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        args.command = "summary"
        args.json = False
        args.func = command_summary
    explorer = SceneExplorer(Path(args.file))
    args.func(explorer, args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
