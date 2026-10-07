"""Compare generated quest CR2W data after resolving serializer representations.

This checks requested typed values, quest graph edges, and ordered sockets.
It deliberately excludes CR2W headers and allocator identities. Unsupported
handle shapes fail closed. It does not establish in-game behavior.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import base64
import hashlib
import json
from pathlib import Path
import struct
from typing import Any, Mapping
import zlib


def _source_evidence_current(record: Mapping[str, Any]) -> bool:
    root = Path(__file__).resolve().parents[1]
    for name, expected in record["source_sha256"].items():
        path = root / name
        if (
            not path.is_file()
            or hashlib.sha256(path.read_bytes()).hexdigest() != expected
        ):
            return False
    return True


def _default_evidence() -> dict[str, Any]:
    return json.loads(
        Path(__file__).with_name("cr2w_scene_defaults.json").read_text(encoding="utf-8")
    )


def _scene_defaults() -> dict[str, Any]:
    record = _default_evidence()
    if not _source_evidence_current(record):
        return {}
    return record["classes"]


def _outline_geometry(value: Mapping[str, Any]) -> None:
    """AreaShapeOutline.CustomWrite writes its buffer, not Points/Height.

    WolvenKit's CustomRead keeps the buffer and leaves the convenience fields
    at the constructor's square/height2 defaults. Accept those or a matching
    decoded outline; reject other contradictory authoring geometry.
    """
    buffer = base64.b64decode(value["buffer"], validate=True)
    if len(buffer) < 8:
        raise ValueError("Truncated AreaShapeOutline buffer")
    count = struct.unpack_from("<I", buffer)[0]
    if len(buffer) != 8 + 16 * count:
        raise ValueError("AreaShapeOutline buffer size disagrees with point count")
    points = [
        struct.unpack_from("<4f", buffer, 4 + 16 * index)[:3] for index in range(count)
    ]
    height = struct.unpack_from("<f", buffer, 4 + 16 * count)[0]
    defaults = [(-1, -1, 0), (1, -1, 0), (1, 1, 0), (-1, 1, 0)]
    if "points" in value:
        explicit = []
        for point in value["points"]:
            if set(point) - {"$type", "X", "Y", "Z"} or point.get("$type") != "Vector3":
                raise ValueError("Unsupported AreaShapeOutline point metadata")
            explicit.append(
                tuple(
                    struct.unpack("<f", struct.pack("<f", point.get(axis, 0)))[0]
                    for axis in ("X", "Y", "Z")
                )
            )
        if explicit != points and explicit != defaults:
            raise ValueError("AreaShapeOutline points contradict its packed buffer")
    if "height" in value and struct.pack("<f", value["height"]) not in {
        struct.pack("<f", height),
        struct.pack("<f", 2),
    }:
        raise ValueError("AreaShapeOutline height contradicts its packed buffer")


def _objects(value: Any):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from _objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from _objects(child)


def canonical_document(document: Mapping[str, Any]) -> dict[str, Any]:
    """Resolve handles and represent quest graph wiring independently of IDs."""
    definitions = {}
    for value in _objects(document):
        if "HandleId" in value:
            identifier = str(value["HandleId"])
            if identifier in definitions:
                raise ValueError(f"Duplicate CR2W handle definition: {identifier}")
            definitions[identifier] = value["Data"]

    def resolve(value, active=()):
        if isinstance(value, list):
            return [resolve(child, active) for child in value]
        if not isinstance(value, dict):
            return value
        identifier = value.get("HandleId", value.get("HandleRefId"))
        if identifier is not None:
            identifier = str(identifier)
            if identifier in ("-1", "0") and identifier not in definitions:
                return None
            if identifier in active:
                raise ValueError(f"Unsupported cyclic CR2W value handle: {identifier}")
            if identifier not in definitions:
                raise ValueError(f"Unresolved CR2W handle: {identifier}")
            resolved = resolve(definitions[identifier], (*active, identifier))
            metadata = {
                key: resolve(child, active)
                for key, child in value.items()
                if key not in {"HandleId", "HandleRefId", "Data"}
            }
            return {"value": resolved, "wrapper": metadata} if metadata else resolved
        return {key: resolve(child, active) for key, child in value.items()}

    def data(wrapper):
        return definitions[str(wrapper.get("HandleId", wrapper.get("HandleRefId")))]

    root = document["Data"]["RootChunk"]
    graph_references = set()
    if root.get("$type") == "questQuestPhaseResource":
        for wrapper in data(root["graph"])["nodes"]:
            for socket in data(wrapper).get("sockets", []):
                graph_references.add(
                    str(socket.get("HandleId", socket.get("HandleRefId")))
                )
                for connection in data(socket).get("connections", []):
                    graph_references.add(
                        str(connection.get("HandleId", connection.get("HandleRefId")))
                    )
    for value in _objects(document):
        if "HandleRefId" in value:
            identifier = str(value["HandleRefId"])
            if identifier in ("-1", "0") and identifier not in definitions:
                continue
            if identifier not in definitions:
                raise ValueError(f"Unresolved CR2W handle: {identifier}")
            if identifier not in graph_references:
                raise ValueError(f"Unsupported shared CR2W value handle: {identifier}")
    envelope = resolve(
        {key: value for key, value in document["Data"].items() if key != "RootChunk"}
    )
    if root.get("$type") != "questQuestPhaseResource":
        return {"root": resolve(root), "data": envelope}
    graph = data(root["graph"])
    owners, nodes = {}, {}
    for wrapper in graph["nodes"]:
        node = data(wrapper)
        identifier = str(node["id"])
        if identifier in nodes:
            raise ValueError(f"Duplicate quest node ID: {identifier}")
        ports = []
        socket_properties = []
        for ordinal, socket in enumerate(node.get("sockets", [])):
            socket_id = str(socket.get("HandleId", socket.get("HandleRefId")))
            port = data(socket)
            ports.append([port["type"], port["name"]["$value"]])
            owners[socket_id] = [identifier, ordinal, *ports[-1]]
            socket_properties.append(
                resolve(
                    {key: value for key, value in port.items() if key != "connections"}
                )
            )
        nodes[identifier] = {
            "semantics": resolve(
                {key: value for key, value in node.items() if key != "sockets"}
            ),
            "ports": ports,
            "socket_properties": socket_properties,
        }
    edges = []
    connection_properties = []

    def endpoints(connection):
        edge = []
        for endpoint in ("source", "destination"):
            wrapper = connection[endpoint]
            edge.extend(
                owners[str(wrapper.get("HandleId", wrapper.get("HandleRefId")))]
            )
        return edge

    for connection in definitions.values():
        if (
            isinstance(connection, dict)
            and connection.get("$type") == "graphGraphConnectionDefinition"
        ):
            edge = endpoints(connection)
            edges.append(edge)
            connection_properties.append(
                [
                    edge,
                    resolve(
                        {
                            key: value
                            for key, value in connection.items()
                            if key not in {"source", "destination"}
                        }
                    ),
                ]
            )
    for wrapper in graph["nodes"]:
        node = data(wrapper)
        nodes[str(node["id"])]["socket_connections"] = [
            [
                endpoints(data(connection))
                for connection in data(socket).get("connections", [])
            ]
            for socket in node.get("sockets", [])
        ]
    return {
        "root": resolve({key: value for key, value in root.items() if key != "graph"}),
        "graph": resolve(
            {key: value for key, value in graph.items() if key != "nodes"}
        ),
        "nodes": nodes,
        "edges": sorted(edges),
        "connection_properties": sorted(
            connection_properties, key=lambda item: json.dumps(item, sort_keys=True)
        ),
        "data": envelope,
    }


@dataclass
class Comparison:
    errors: list[dict[str, Any]] = field(default_factory=list)
    normalizations: list[dict[str, Any]] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def compare_documents(
    expected: Mapping[str, Any],
    actual: Mapping[str, Any],
    *,
    schema: Mapping[str, Any],
    fresh_wolvenkit_defaults: Mapping[str, Any] | None = None,
) -> Comparison:
    """Compare requested values with bounded, evidenced RED representations.

    CFloat rounding requires identical float32 bits and a reflected CFloat
    field. TweakDBID strings use WolvenKit's CRC32 + UTF-16 length encoding.
    Additional properties require the pinned render-default allowlist plus a
    freshly written/read WolvenKit oracle. Arbitrary reflected additions and
    template-retained values are not accepted as defaults.
    Missing requested fields and populated arrays are never defaulted away.
    AreaShapeOutline keeps its packed geometry authoritative; convenience
    fields must match that geometry or source-bound reader defaults. Shared
    value handles outside explicit quest graph wiring are unsupported.
    """
    outlines = [
        value
        for document in (expected, actual, fresh_wolvenkit_defaults)
        for value in _objects(document)
        if value.get("$type") == "AreaShapeOutline"
    ]
    if outlines:
        evidence = _default_evidence()["custom_data"]["AreaShapeOutline"]
        if not _source_evidence_current(evidence):
            raise ValueError("AreaShapeOutline custom-data source evidence is stale")
        for outline in outlines:
            _outline_geometry(outline)
    left, right = canonical_document(expected), canonical_document(actual)
    defaults = (
        canonical_document(fresh_wolvenkit_defaults)
        if fresh_wolvenkit_defaults is not None
        else None
    )
    result = Comparison()
    known_defaults = _scene_defaults()

    def property_type(class_name, name):
        seen = set()
        while class_name and class_name not in seen:
            seen.add(class_name)
            definition = schema.get(class_name, {})
            prop = definition.get("properties", {}).get(name)
            if prop:
                return prop.get("cs_type")
            class_name = definition.get("base")
        return None

    def tweak_id(value):
        if value.get("$storage") == "uint64":
            return int(value["$value"])
        text = value["$value"]
        return zlib.crc32(text.encode("utf-8")) + (
            (len(text.encode("utf-16-le")) // 2) << 32
        )

    def visit(a, b, oracle, path, red_type=None):
        if a == b:
            return
        evidence = {"path": path, "expected": a, "actual": b}
        if isinstance(a, dict) and isinstance(b, dict):
            kind = a.get("$type", b.get("$type", red_type))
            if kind == "AreaShapeOutline" and a.get("$type") == b.get("$type"):
                _outline_geometry(a)
                _outline_geometry(b)
                for key in ("points", "height"):
                    if a.get(key) != b.get(key):
                        result.normalizations.append(
                            {
                                "path": f"{path}.{key}",
                                "expected": a.get(key, "<missing>"),
                                "actual": b.get(key, "<missing>"),
                                "reason": "AreaShapeOutline buffer is authoritative; convenience fields match buffer or documented reader defaults",
                            }
                        )
                a = {
                    key: value
                    for key, value in a.items()
                    if key not in {"points", "height"}
                }
                b = {
                    key: value
                    for key, value in b.items()
                    if key not in {"points", "height"}
                }
            if (
                kind == "TweakDBID"
                and a.get("$type") == b.get("$type")
                and a.keys() == b.keys() == {"$type", "$storage", "$value"}
                and a["$storage"] in {"string", "uint64"}
                and b["$storage"] in {"string", "uint64"}
                and tweak_id(a) == tweak_id(b)
            ):
                result.normalizations.append(
                    {**evidence, "reason": "same TweakDBID CRC32/length identity"}
                )
                return
            for key in a.keys() | b.keys():
                item_path = f"{path}.{key}"
                reflected = property_type(kind, key)
                if key not in a:
                    extra = {
                        "path": item_path,
                        "expected": "<missing>",
                        "actual": b[key],
                    }
                    if (
                        kind == "questQuestPhaseResource"
                        and key == "inplacePhases"
                        and b[key] == []
                    ):
                        result.normalizations.append(
                            {**extra, "reason": "empty inplace phase array"}
                        )
                    elif (
                        reflected
                        and key in known_defaults.get(kind, {})
                        and b[key] == known_defaults[kind][key]
                        and isinstance(oracle, dict)
                        and key in oracle
                        and oracle[key] == b[key]
                    ):
                        result.normalizations.append(
                            {
                                **extra,
                                "reason": "pinned render default matches fresh WolvenKit writer",
                            }
                        )
                    else:
                        result.errors.append(extra)
                elif key not in b:
                    result.errors.append(
                        {"path": item_path, "expected": a[key], "actual": "<missing>"}
                    )
                else:
                    visit(
                        a[key],
                        b[key],
                        oracle.get(key) if isinstance(oracle, dict) else None,
                        item_path,
                        reflected,
                    )
            return
        if isinstance(a, list) and isinstance(b, list):
            if len(a) != len(b):
                result.errors.append(
                    {"path": path, "expected_length": len(a), "actual_length": len(b)}
                )
            element_type = (
                red_type[7:-1] if red_type and red_type.startswith("CArray<") else None
            )
            for index, (one, two) in enumerate(zip(a, b)):
                visit(
                    one,
                    two,
                    oracle[index]
                    if isinstance(oracle, list) and index < len(oracle)
                    else None,
                    f"{path}[{index}]",
                    element_type,
                )
            return
        if red_type == "CFloat" and type(a) in (int, float) and type(b) in (int, float):
            if struct.pack("<f", a) == struct.pack("<f", b):
                result.normalizations.append(
                    {**evidence, "reason": "identical reflected CFloat bits"}
                )
                return
        result.errors.append(evidence)

    visit(left, right, defaults, "$")
    return result
