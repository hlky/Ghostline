"""Independent checks for scene reference tables, shared by scene authoring tools."""

from __future__ import annotations

from typing import Any


def validate_reference_tables(root: dict[str, Any]) -> list[str]:
    """Check references in emitted data, without consulting generator inputs."""
    errors: list[str] = []
    references = root.get("resouresReferences", {})
    for actor in [*root.get("actors", []), *root.get("playerActors", [])]:
        actor_name = actor.get("actorName", actor.get("playerName", "?"))
        for field, table in (
            ("animSets", "ridAnimSets"),
            ("facialAnimSets", "ridFacialAnimSets"),
        ):
            for reference in actor.get(field, []):
                index = reference.get("id")
                if type(index) is not int or not 0 <= index < len(
                    references.get(table, [])
                ):
                    errors.append(
                        f"Actor {actor_name} has invalid {field} reference {index}"
                    )
    nodes = {
        wrapper.get("Data", {}).get("nodeId", {}).get("id"): wrapper.get("Data", {})
        for wrapper in root.get("sceneGraph", {}).get("Data", {}).get("graph", [])
    }
    for points_key, label, node_type in (
        ("entryPoints", "Entry", "scnStartNode"),
        ("exitPoints", "Exit", "scnEndNode"),
    ):
        points = root.get(points_key, [])
        if not isinstance(points, list):
            continue  # The outer scene validator reports the invalid container.
        names: set[str] = set()
        for point in points:
            name = point.get("name", {}).get("$value")
            node_id = point.get("nodeId", {}).get("id")
            if name in names:
                errors.append(f"Duplicate {label.lower()} point name: {name}")
            names.add(name)
            node = nodes.get(node_id)
            if node is None:
                errors.append(f"{label} point {name} points to missing node {node_id}")
            elif node.get("$type") != node_type:
                errors.append(
                    f"{label} point {name} must target a {node_type}; "
                    f"node {node_id} is {node.get('$type')}"
                )

    store = root.get("locStore", {})
    payloads = store.get("vpEntries", [])
    for index, descriptor in enumerate(store.get("vdEntries", [])):
        payload_index = descriptor.get("vpeIndex")
        if type(payload_index) is not int or not 0 <= payload_index < len(payloads):
            errors.append(
                f"locStore descriptor {index} has invalid vpeIndex {payload_index}"
            )
            continue
        variant = descriptor.get("variantId", {}).get("ruid")
        payload_variant = payloads[payload_index].get("variantId", {}).get("ruid")
        if variant is None or variant != payload_variant:
            errors.append(
                f"locStore descriptor {index} variantId {variant} does not match "
                f"payload {payload_index} variantId {payload_variant}"
            )
    return errors
