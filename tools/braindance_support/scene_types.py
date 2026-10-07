"""Small RED scene value constructors and handle allocation."""
from __future__ import annotations
from typing import Any, Iterable


class BraindancePipelineError(RuntimeError):
    pass


def _root(document: dict[str, Any], expected_type: str) -> dict[str, Any]:
    data = document.get("Data")
    root = data.get("RootChunk") if isinstance(data, dict) else None
    if not isinstance(root, dict) or root.get("$type") != expected_type:
        raise BraindancePipelineError(
            f"Expected Data.RootChunk of type {expected_type}"
        )
    return root


def _serial(value: Any) -> int:
    if not isinstance(value, dict) or not isinstance(value.get("serialNumber"), int):
        raise BraindancePipelineError("RID record has no serial number")
    return int(value["serialNumber"])


def _tag_signature(record: dict[str, Any]) -> str:
    signature = record.get("tag", {}).get("signature", {}).get("$value")
    if not isinstance(signature, str):
        raise BraindancePipelineError("RID record has no tag signature")
    return signature


def _fnv1a32(text: str) -> int:
    value = 0x811C9DC5
    for byte in text.casefold().encode("utf-8"):
        value ^= byte
        value = value * 0x01000193 & 0xFFFFFFFF
    return value or 1


def _walk(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from _walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk(child)


class _SceneHandleAllocator:
    def __init__(self, root: dict[str, Any]) -> None:
        handle_ids = [
            int(item["HandleId"])
            for item in _walk(root)
            if isinstance(item.get("HandleId"), str)
            and item["HandleId"].isdigit()
        ]
        self._next = max(handle_ids, default=0) + 1

    def wrap(self, data: dict[str, Any]) -> dict[str, Any]:
        handle = {"HandleId": str(self._next), "Data": data}
        self._next += 1
        return handle


def _cname(value: str) -> dict[str, Any]:
    return {
        "$type": "CName",
        "$storage": "string",
        "$value": value,
    }


def _dynamic_entity_reference(dynamic_name: str) -> dict[str, Any]:
    return {
        "$type": "gameEntityReference",
        "dynamicEntityUniqueName": _cname(dynamic_name),
        "names": [],
        "reference": {
            "$type": "NodeRef",
            "$storage": "uint64",
            "$value": "0",
        },
        "sceneActorContextName": _cname("None"),
        "slotName": _cname("None"),
        "type": "EntityRef",
    }


def _actor_entity_reference(
    node_ref: str,
    entry_name: str,
) -> dict[str, Any]:
    return {
        "$type": "gameEntityReference",
        "dynamicEntityUniqueName": _cname("None"),
        "names": [_cname(entry_name)],
        "reference": {
            "$type": "NodeRef",
            "$storage": "string",
            "$value": node_ref,
        },
        "sceneActorContextName": _cname("None"),
        "slotName": _cname("None"),
        "type": "EntityRef",
    }


def _scene_input_socket(
    node_id: int,
    ordinal: int,
    *,
    name: int = 0,
) -> dict[str, Any]:
    return {
        "$type": "scnInputSocketId",
        "isockStamp": {
            "$type": "scnInputSocketStamp",
            "name": name,
            "ordinal": ordinal,
        },
        "nodeId": {"$type": "scnNodeId", "id": node_id},
    }


def _scene_output_socket(
    destinations: list[tuple[int, int]],
    *,
    name: int = 0,
) -> dict[str, Any]:
    return {
        "$type": "scnOutputSocket",
        "destinations": [
            _scene_input_socket(node_id, ordinal)
            for node_id, ordinal in destinations
        ],
        "stamp": {
            "$type": "scnOutputSocketStamp",
            "name": name,
            "ordinal": 0,
        },
    }


def _quest_socket(
    allocator: _SceneHandleAllocator,
    name: str,
    socket_type: str,
) -> dict[str, Any]:
    return allocator.wrap(
        {
            "$type": "questSocketDefinition",
            "connections": [],
            "name": _cname(name),
            "type": socket_type,
        }
    )


def _scene_quest_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    quest_data: dict[str, Any],
    destination: tuple[int, int] | None,
) -> dict[str, Any]:
    quest_data["id"] = node_id
    quest_data["sockets"] = [
        _quest_socket(allocator, "CutDestination", "CutDestination"),
        _quest_socket(allocator, "In", "Input"),
        _quest_socket(allocator, "Out", "Output"),
    ]
    return allocator.wrap(
        {
            "$type": "scnQuestNode",
            "ffStrategy": "automatic",
            "isockMappings": [
                _cname("CutDestination"),
                _cname("In"),
            ],
            "nodeId": {"$type": "scnNodeId", "id": node_id},
            "osockMappings": [_cname("Out")],
            "outputSockets": [
                _scene_output_socket(
                    [destination] if destination is not None else []
                )
            ],
            "questNode": allocator.wrap(quest_data),
        }
    )
