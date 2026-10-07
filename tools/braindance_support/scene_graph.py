"""Read-only scene graph indexing for independent structural audits."""
from __future__ import annotations
from typing import Any
from braindance_support.scene_types import (
    _walk,
)


class SceneGraphIndex:
    def __init__(self, root: dict[str, Any]):
        scene_graph = root.get("sceneGraph", {}).get("Data", {})
        graph_nodes = (
            scene_graph.get("graph", [])
            if isinstance(scene_graph, dict)
            else []
        )
        self.nodes = {
            node_id: wrapper["Data"]
            for wrapper in graph_nodes
            if isinstance(wrapper, dict)
            and isinstance(wrapper.get("Data"), dict)
            and isinstance(
                node_id := wrapper["Data"].get("nodeId", {}).get("id"),
                int,
            )
        }


    def outgoing_edges(
        self, node_id: int,
    ) -> list[tuple[int, int, int, int]]:
        destinations: list[tuple[int, int, int, int]] = []
        for socket in self.nodes.get(node_id, {}).get(
            "outputSockets", []
        ):
            source_name = socket.get("stamp", {}).get("name")
            for destination in socket.get("destinations", []):
                target = destination.get("nodeId", {}).get("id")
                destination_stamp = destination.get("isockStamp", {})
                destination_name = destination_stamp.get("name")
                ordinal = destination_stamp.get("ordinal")
                if (
                    isinstance(target, int)
                    and isinstance(destination_name, int)
                    and isinstance(ordinal, int)
                    and isinstance(source_name, int)
                ):
                    destinations.append(
                        (
                            target,
                            destination_name,
                            ordinal,
                            source_name,
                        )
                    )
        return destinations

    def outgoing(self, node_id: int) -> list[tuple[int, int]]:
        return [
            (target, ordinal)
            for target, _destination_name, ordinal, _source_name
            in self.outgoing_edges(node_id)
        ]

    def nested_type(self, node_id: int, type_name: str) -> bool:
        return any(
            item.get("$type") == type_name
            for item in _walk(self.nodes.get(node_id, {}))
        )

    def reachable(self, starts: set[int]) -> set[int]:
        visited = set(starts)
        pending = list(starts)
        while pending:
            current = pending.pop()
            for target, _ in self.outgoing(current):
                if target in visited:
                    continue
                visited.add(target)
                pending.append(target)
        return visited

