#!/usr/bin/env python3
"""Decode and sample Cyberpunk 2077 human navigation tile resources.

The module intentionally depends only on the Python standard library.  It reads
the base64 ``DataBuffer`` values emitted by CR2W-JSON serializers, mirrors
WolvenKit's ``TilesReader``, joins triangles at resource boundaries, and emits
deterministic camera candidates for the world-location proof of concept.

Coordinates are kept in the component order stored in the navigation resource.
VAND serializes world positions as X/Z/Y; callers that need RED world X/Y/Z
coordinates can use :func:`vand_position_to_world`.  A caller assembling a
transformed navigation node must also apply that node's world transform before
calling :func:`reconstruct_navigation_islands`.
"""

from __future__ import annotations

import base64
import hashlib
import json
import math
import struct
from collections import defaultdict, deque
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


# WolvenKit names the first header field ``vand`` and real game buffers store
# these bytes in this order.  ``VNAV_MAGIC`` remains as a source-compatible
# name for early POC callers; it does not mean that b"VNAV" is accepted.
VAND_MAGIC = b"VAND"
VNAV_MAGIC = VAND_MAGIC
_VNAV_HEADER = struct.Struct("<15I")


class NavigationFormatError(ValueError):
    """Raised when a navigation resource or VNAV buffer is malformed."""


@dataclass(frozen=True, order=True)
class Vec3:
    x: float
    y: float
    z: float

    def distance_squared(self, other: "Vec3", *, vertical_weight: float = 1.0) -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        dz = (self.z - other.z) * vertical_weight
        return dx * dx + dy * dy + dz * dz


def vand_position_to_world(position: Vec3) -> Vec3:
    """Convert VAND's serialized X/Z/Y component order to world X/Y/Z."""

    return Vec3(position.x, position.z, position.y)


@dataclass(frozen=True)
class Bounds3:
    minimum: Vec3
    maximum: Vec3


@dataclass(frozen=True)
class VNAVHeader:
    magic: bytes
    unknown_1: int
    tile_x: int
    tile_y: int
    unknown_2: int
    unknown_3: int
    face_count: int
    vertex_count: int
    zero_pair_count: int
    index_record_count: int
    unknown_vector_count: int
    flag_count: int
    info_record_count: int
    bounds_record_count: int
    unknown_4: int


@dataclass(frozen=True)
class FaceConnection:
    """A raw WolvenKit ``TileConnectedFace`` entry.

    ``flagged`` is the high bit named ``Bit`` by WolvenKit.  ``index`` is the
    remaining 15-bit value and may be a sentinel or non-local reference, so
    island reconstruction only follows it when it indexes a face in the same
    buffer.
    """

    index: int
    flagged: bool
    raw: int


@dataclass(frozen=True)
class NavFace:
    index: int
    vertex_indices: tuple[int, int, int]
    connected_faces: tuple[FaceConnection, FaceConnection, FaceConnection]
    zero: int
    three: int
    num_indices: int
    bits: int


@dataclass(frozen=True)
class ZeroPair:
    unknown_1: int
    unknown_2: int


@dataclass(frozen=True)
class IndexRecord:
    unknown_1: int
    index: int
    unknown_2: int


@dataclass(frozen=True)
class InfoRecord:
    values: tuple[tuple[int, int], ...]
    unknown: int


@dataclass(frozen=True)
class AuxiliaryBoundsRecord:
    first: Vec3
    second: Vec3
    value: float
    unknown_4: int
    unknown_5: int
    unknown_6: int


@dataclass(frozen=True)
class NavigationSource:
    source_path: str = ""
    resource_path: str = ""
    buffer_index: int = 0
    tile_data_index: int | None = None
    agent_size: str = "Human"
    tile_x: int | None = None
    tile_y: int | None = None
    tile_index: int | None = None
    tile_ref: int | None = None
    active_variant_ids: tuple[int, ...] = ()
    all_variant_ids: tuple[int, ...] = ()


@dataclass(frozen=True)
class NavTileBuffer:
    header: VNAVHeader
    source: NavigationSource
    unknown_vector: Vec3
    bounds: Bounds3
    unknown_float: float
    vertices: tuple[Vec3, ...]
    faces: tuple[NavFace, ...]
    zero_pairs: tuple[ZeroPair, ...] = ()
    index_records: tuple[IndexRecord, ...] = ()
    unknown_vectors: tuple[Vec3, ...] = ()
    flags: tuple[int, ...] = ()
    info_records: tuple[InfoRecord, ...] = ()
    bounds_records: tuple[AuxiliaryBoundsRecord, ...] = ()

    def face_vertices(self, face: int | NavFace) -> tuple[Vec3, Vec3, Vec3]:
        item = self.faces[face] if isinstance(face, int) else face
        return tuple(self.vertices[index] for index in item.vertex_indices)  # type: ignore[return-value]


@dataclass(frozen=True)
class NavigationSector:
    source_path: str
    resource_path: str
    agent_size: str
    local_bounds: Bounds3 | None
    buffers: tuple[NavTileBuffer, ...]


@dataclass(frozen=True, order=True)
class FaceRef:
    resource_path: str
    source_path: str
    buffer_index: int
    face_index: int


@dataclass(frozen=True)
class IslandFace:
    ref: FaceRef
    vertices: tuple[Vec3, Vec3, Vec3]
    neighbors: tuple[FaceRef, ...]
    source: NavigationSource


@dataclass(frozen=True)
class IslandMetrics:
    surface_area_m2: float
    z_min: float
    z_max: float
    z_range_m: float
    boundary_length_m: float
    approximate_width_m: float


@dataclass(frozen=True)
class NavigationIsland:
    island_id: str
    faces: tuple[IslandFace, ...]
    bounds: Bounds3
    metrics: IslandMetrics
    boundary_edges: tuple[tuple[Vec3, Vec3], ...]


@dataclass(frozen=True)
class SampleProvenance:
    method: str
    resource_path: str
    source_path: str
    buffer_index: int
    face_index: int
    active_variant_ids: tuple[int, ...]
    all_variant_ids: tuple[int, ...]


@dataclass(frozen=True)
class NavigationSample:
    island_id: str
    sample_index: int
    surface_position: Vec3
    camera_position: Vec3
    spacing_m: float
    camera_height_m: float
    local_width_m: float
    seed: int
    provenance: SampleProvenance


class _Cursor:
    def __init__(self, payload: bytes) -> None:
        self.payload = payload
        self.offset = 0

    def unpack(self, format_string: str) -> tuple[Any, ...]:
        parser = struct.Struct("<" + format_string)
        end = self.offset + parser.size
        if end > len(self.payload):
            raise NavigationFormatError(
                f"truncated VNAV buffer at byte {self.offset}: "
                f"need {parser.size} bytes, have {len(self.payload) - self.offset}"
            )
        result = parser.unpack_from(self.payload, self.offset)
        self.offset = end
        return result

    def vector(self) -> Vec3:
        x, y, z = self.unpack("3f")
        return Vec3(x, y, z)


def decode_vnav_buffer(
    payload: bytes | bytearray | memoryview | str,
    *,
    source: NavigationSource | None = None,
) -> NavTileBuffer:
    """Decode one binary or base64-encoded ``worldNavigationTileResource`` buffer.

    The layout follows WolvenKit ``TilesBufferHeader`` and ``TilesReader``.
    Unknown records are retained so a caller can fingerprint the complete
    decoded buffer even though the proof of concept only consumes faces.
    """

    raw = _decode_payload(payload)
    if len(raw) < _VNAV_HEADER.size:
        raise NavigationFormatError(
            f"VNAV buffer is {len(raw)} bytes; header requires {_VNAV_HEADER.size}"
        )
    if raw[:4] != VAND_MAGIC:
        raise NavigationFormatError(
            f"invalid VAND magic {raw[:4]!r}; expected {VAND_MAGIC!r}"
        )

    values = _VNAV_HEADER.unpack_from(raw)
    header = VNAVHeader(
        magic=raw[:4],
        unknown_1=values[1],
        tile_x=values[2],
        tile_y=values[3],
        unknown_2=values[4],
        unknown_3=values[5],
        face_count=values[6],
        vertex_count=values[7],
        zero_pair_count=values[8],
        index_record_count=values[9],
        unknown_vector_count=values[10],
        flag_count=values[11],
        info_record_count=values[12],
        bounds_record_count=values[13],
        unknown_4=values[14],
    )

    expected_size = (
        _VNAV_HEADER.size
        + 40
        + header.vertex_count * 12
        + header.face_count * 20
        + header.zero_pair_count * 16
        + header.index_record_count * 12
        + header.unknown_vector_count * 12
        + header.flag_count * 4
        + header.info_record_count * 16
        + header.bounds_record_count * 40
    )
    if len(raw) != expected_size:
        relation = "truncated" if len(raw) < expected_size else "has trailing data"
        raise NavigationFormatError(
            f"VNAV buffer {relation}: header describes {expected_size} bytes, got {len(raw)}"
        )

    cursor = _Cursor(raw)
    cursor.offset = _VNAV_HEADER.size
    unknown_vector = cursor.vector()
    bounds = Bounds3(cursor.vector(), cursor.vector())
    (unknown_float,) = cursor.unpack("f")
    vertices = tuple(cursor.vector() for _ in range(header.vertex_count))

    faces: list[NavFace] = []
    for face_index in range(header.face_count):
        (zero,) = cursor.unpack("I")
        vertex_indices = cursor.unpack("3H")
        raw_connections = cursor.unpack("3H")
        three, num_indices, bits = cursor.unpack("HBB")
        if any(index >= len(vertices) for index in vertex_indices):
            raise NavigationFormatError(
                f"face {face_index} references vertex outside 0..{len(vertices) - 1}: "
                f"{vertex_indices}"
            )
        connections = tuple(
            FaceConnection(value & 0x7FFF, bool(value & 0x8000), value)
            for value in raw_connections
        )
        faces.append(
            NavFace(
                index=face_index,
                vertex_indices=vertex_indices,  # type: ignore[arg-type]
                connected_faces=connections,  # type: ignore[arg-type]
                zero=zero,
                three=three,
                num_indices=num_indices,
                bits=bits,
            )
        )

    zero_pairs = tuple(
        ZeroPair(*cursor.unpack("2Q")) for _ in range(header.zero_pair_count)
    )
    index_records = tuple(
        IndexRecord(*cursor.unpack("3I")) for _ in range(header.index_record_count)
    )
    unknown_vectors = tuple(cursor.vector() for _ in range(header.unknown_vector_count))
    flags = tuple(cursor.unpack("I")[0] for _ in range(header.flag_count))
    info_records = tuple(
        InfoRecord(
            values=tuple(
                (pair[0], pair[1]) for pair in (cursor.unpack("2b") for _ in range(6))
            ),
            unknown=cursor.unpack("I")[0],
        )
        for _ in range(header.info_record_count)
    )
    bounds_records = tuple(
        AuxiliaryBoundsRecord(
            first=cursor.vector(),
            second=cursor.vector(),
            value=cursor.unpack("f")[0],
            unknown_4=cursor.unpack("I")[0],
            unknown_5=cursor.unpack("I")[0],
            unknown_6=cursor.unpack("I")[0],
        )
        for _ in range(header.bounds_record_count)
    )

    source_metadata = source or NavigationSource()
    if source_metadata.tile_x is None or source_metadata.tile_y is None:
        source_metadata = replace(
            source_metadata,
            tile_x=header.tile_x
            if source_metadata.tile_x is None
            else source_metadata.tile_x,
            tile_y=header.tile_y
            if source_metadata.tile_y is None
            else source_metadata.tile_y,
        )
    return NavTileBuffer(
        header=header,
        source=source_metadata,
        unknown_vector=unknown_vector,
        bounds=bounds,
        unknown_float=unknown_float,
        vertices=vertices,
        faces=tuple(faces),
        zero_pairs=zero_pairs,
        index_records=index_records,
        unknown_vectors=unknown_vectors,
        flags=flags,
        info_records=info_records,
        bounds_records=bounds_records,
    )


def load_navigation_sector(
    source: str | Path | Mapping[str, Any],
    *,
    source_id: str | None = None,
    human_only: bool = True,
) -> NavigationSector:
    """Load a CR2W-JSON navigation resource and decode selected tile buffers.

    ``tilesData.bufferIndex`` is used to associate metadata with ``tileBuffers``.
    Human records are selected by default.  When ``tilesData`` is absent, the
    root resource's ``agentSize`` applies to every buffer.
    """

    document, source_path = _load_document(source)
    root = _payload(_mapping(_mapping(document.get("Data")).get("RootChunk")))
    root_type = str(root.get("$type", ""))
    if root_type and root_type != "worldNavigationTileResource":
        raise NavigationFormatError(
            f"expected worldNavigationTileResource root, got {root_type!r}"
        )

    header = _mapping(document.get("Header"))
    archive_name = _string_value(header.get("ArchiveFileName"))
    resource_path = source_id or archive_name or source_path
    root_agent = _agent_name(root.get("agentSize"))
    raw_buffers = _as_list(root.get("tileBuffers"))
    tile_data = _as_list(root.get("tilesData"))
    decoded: list[NavTileBuffer] = []

    if tile_data:
        for tile_data_index, raw_tile in enumerate(tile_data):
            tile = _payload(_mapping(raw_tile))
            agent = _agent_name(tile.get("agentSize")) or root_agent
            if human_only and agent != "Human":
                continue
            buffer_index = _int_value(tile.get("bufferIndex"), "bufferIndex")
            if buffer_index < 0 or buffer_index >= len(raw_buffers):
                raise NavigationFormatError(
                    f"tilesData[{tile_data_index}].bufferIndex={buffer_index} "
                    f"outside tileBuffers[0:{len(raw_buffers)}]"
                )
            metadata = NavigationSource(
                source_path=source_path,
                resource_path=resource_path,
                buffer_index=buffer_index,
                tile_data_index=tile_data_index,
                agent_size=agent or "Unknown",
                tile_x=_optional_int(tile.get("tileX")),
                tile_y=_optional_int(tile.get("tileY")),
                tile_index=_optional_int(tile.get("tileIndex")),
                tile_ref=_optional_int(tile.get("tileRef")),
                active_variant_ids=_int_tuple(tile.get("activeVariantIDs")),
                all_variant_ids=_int_tuple(tile.get("allVariantIDs")),
            )
            decoded.append(
                decode_vnav_buffer(
                    _extract_buffer_bytes(raw_buffers[buffer_index]), source=metadata
                )
            )
    elif not human_only or root_agent == "Human":
        for buffer_index, raw_buffer in enumerate(raw_buffers):
            metadata = NavigationSource(
                source_path=source_path,
                resource_path=resource_path,
                buffer_index=buffer_index,
                agent_size=root_agent or "Unknown",
            )
            decoded.append(
                decode_vnav_buffer(_extract_buffer_bytes(raw_buffer), source=metadata)
            )

    local_bounds = _parse_bounds(root.get("localBoundingBox"))
    return NavigationSector(
        source_path=source_path,
        resource_path=resource_path,
        agent_size=(
            "Human"
            if human_only and decoded
            else root_agent or (decoded[0].source.agent_size if decoded else "Unknown")
        ),
        local_bounds=local_bounds,
        buffers=tuple(decoded),
    )


def reconstruct_navigation_islands(
    navigation: Iterable[NavigationSector | NavTileBuffer],
    *,
    edge_quantization_m: float = 0.05,
) -> tuple[NavigationIsland, ...]:
    """Join faces by decoded adjacency and shared quantized 3-D edges.

    Z is part of every edge key.  Coincident XY surfaces on different floors
    therefore remain separate unless an explicit VNAV face connection joins
    them (for example, through a stair mesh).
    """

    if edge_quantization_m <= 0:
        raise ValueError("edge_quantization_m must be positive")
    buffers = _flatten_buffers(navigation)
    face_records: dict[
        FaceRef, tuple[NavTileBuffer, NavFace, tuple[Vec3, Vec3, Vec3]]
    ] = {}
    by_buffer: dict[tuple[str, str, int], dict[int, FaceRef]] = defaultdict(dict)
    adjacency: dict[FaceRef, set[FaceRef]] = defaultdict(set)
    edge_faces: dict[
        tuple[tuple[int, int, int], tuple[int, int, int]], list[FaceRef]
    ] = defaultdict(list)

    for buffer in buffers:
        buffer_key = (
            buffer.source.resource_path,
            buffer.source.source_path,
            buffer.source.buffer_index,
        )
        for face in buffer.faces:
            ref = FaceRef(*buffer_key, face.index)
            vertices = buffer.face_vertices(face)
            face_records[ref] = (buffer, face, vertices)
            by_buffer[buffer_key][face.index] = ref
            for first, second in _triangle_edges(vertices):
                edge_faces[_edge_key(first, second, edge_quantization_m)].append(ref)

    for ref, (buffer, face, _vertices) in face_records.items():
        buffer_key = (
            buffer.source.resource_path,
            buffer.source.source_path,
            buffer.source.buffer_index,
        )
        local_faces = by_buffer[buffer_key]
        for connection in face.connected_faces:
            neighbor = local_faces.get(connection.index)
            if neighbor is not None and neighbor != ref:
                adjacency[ref].add(neighbor)
                adjacency[neighbor].add(ref)

    for refs in edge_faces.values():
        unique_refs = sorted(set(refs))
        for index, first in enumerate(unique_refs):
            for second in unique_refs[index + 1 :]:
                adjacency[first].add(second)
                adjacency[second].add(first)

    components: list[tuple[FaceRef, ...]] = []
    unseen = set(face_records)
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        queue = deque([start])
        component: list[FaceRef] = []
        while queue:
            current = queue.popleft()
            component.append(current)
            for neighbor in sorted(adjacency[current]):
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    queue.append(neighbor)
        components.append(tuple(sorted(component)))

    islands = [
        _make_island(component, face_records, adjacency, edge_quantization_m)
        for component in components
    ]
    return tuple(sorted(islands, key=lambda island: island.island_id))


def sample_navigation_islands(
    islands: Iterable[NavigationIsland],
    *,
    spacing_m: float = 25.0,
    camera_height_m: float = 1.65,
    seed: int = 0,
    vertical_weight: float = 6.0,
) -> tuple[NavigationSample, ...]:
    """Produce deterministic farthest-point camera samples on every island.

    The candidate lattice is denser than ``spacing_m`` and farthest-point
    selection stops once every candidate lies within that radius of a selected
    point.  ``vertical_weight`` deliberately gives stacked floors distinct
    coverage even when their XY footprints overlap.
    """

    if spacing_m <= 0:
        raise ValueError("spacing_m must be positive")
    if camera_height_m < 0:
        raise ValueError("camera_height_m must not be negative")
    if vertical_weight <= 0:
        raise ValueError("vertical_weight must be positive")

    samples: list[NavigationSample] = []
    for island in sorted(islands, key=lambda item: item.island_id):
        candidates = _island_candidates(island, spacing_m)
        if not candidates:
            continue
        start_digest = hashlib.sha256(
            f"{seed}:{island.island_id}".encode("utf-8")
        ).digest()
        selected = [int.from_bytes(start_digest[:8], "little") % len(candidates)]
        minimum_distances = [
            candidate[0].distance_squared(
                candidates[selected[0]][0], vertical_weight=vertical_weight
            )
            for candidate in candidates
        ]
        threshold_squared = spacing_m * spacing_m
        while True:
            farthest = max(
                range(len(candidates)),
                key=lambda index: (minimum_distances[index], -index),
            )
            if minimum_distances[farthest] < threshold_squared - 1e-9:
                break
            selected.append(farthest)
            chosen = candidates[farthest][0]
            for index, candidate in enumerate(candidates):
                distance = candidate[0].distance_squared(
                    chosen, vertical_weight=vertical_weight
                )
                if distance < minimum_distances[index]:
                    minimum_distances[index] = distance

        selected_points = sorted(
            (candidates[index] for index in selected),
            key=lambda item: (item[0].x, item[0].y, item[0].z, item[1].ref),
        )
        for sample_index, (surface, face) in enumerate(selected_points):
            source = face.source
            samples.append(
                NavigationSample(
                    island_id=island.island_id,
                    sample_index=sample_index,
                    surface_position=surface,
                    camera_position=Vec3(
                        surface.x, surface.y, surface.z + camera_height_m
                    ),
                    spacing_m=spacing_m,
                    camera_height_m=camera_height_m,
                    local_width_m=local_width_at(surface, island),
                    seed=seed,
                    provenance=SampleProvenance(
                        method="navmesh_farthest",
                        resource_path=face.ref.resource_path,
                        source_path=face.ref.source_path,
                        buffer_index=face.ref.buffer_index,
                        face_index=face.ref.face_index,
                        active_variant_ids=source.active_variant_ids,
                        all_variant_ids=source.all_variant_ids,
                    ),
                )
            )
    return tuple(samples)


def local_width_at(point: Vec3, island: NavigationIsland) -> float:
    """Approximate local walkable width as twice the nearest XY boundary distance."""

    if not island.boundary_edges:
        return 0.0
    distance = min(
        _point_segment_distance_xy(point, edge[0], edge[1])
        for edge in island.boundary_edges
    )
    return 2.0 * distance


def _decode_payload(payload: bytes | bytearray | memoryview | str) -> bytes:
    if isinstance(payload, str):
        compact = "".join(payload.split())
        try:
            return base64.b64decode(compact, validate=True)
        except (ValueError, base64.binascii.Error) as exc:
            raise NavigationFormatError("tile buffer is not valid base64") from exc
    if isinstance(payload, (bytes, bytearray, memoryview)):
        return bytes(payload)
    raise TypeError(
        f"VNAV payload must be bytes or base64 text, got {type(payload).__name__}"
    )


def _load_document(
    source: str | Path | Mapping[str, Any],
) -> tuple[Mapping[str, Any], str]:
    if isinstance(source, Mapping):
        return source, ""
    path = Path(source)
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise NavigationFormatError(
            f"could not load navigation JSON {path}: {exc}"
        ) from exc
    if not isinstance(value, Mapping):
        raise NavigationFormatError(f"navigation JSON root in {path} must be an object")
    return value, str(path)


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _payload(value: Mapping[str, Any]) -> Mapping[str, Any]:
    data = value.get("Data")
    if isinstance(data, Mapping):
        return data
    return value


def _as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if isinstance(value, Mapping):
        for key in ("Data", "data", "Items", "items", "$value"):
            nested = value.get(key)
            if isinstance(nested, list):
                return nested
    return []


def _string_value(value: Any) -> str:
    if isinstance(value, Mapping):
        for key in ("$value", "value", "Value"):
            if key in value:
                return _string_value(value[key])
        return ""
    return "" if value is None else str(value)


def _agent_name(value: Any) -> str:
    raw = _string_value(value).strip()
    if not raw:
        return ""
    if raw == "0" or raw.casefold().split(".")[-1] == "human":
        return "Human"
    if raw == "1" or raw.casefold().split(".")[-1] == "vehicle":
        return "Vehicle"
    if raw == "2" or raw.casefold().split(".")[-1] == "agentsize_count":
        return "AgentSize_Count"
    return raw


def _optional_int(value: Any) -> int | None:
    raw = _string_value(value).strip()
    if not raw:
        return None
    try:
        return int(raw, 0)
    except ValueError as exc:
        raise NavigationFormatError(f"expected integer, got {raw!r}") from exc


def _int_value(value: Any, field_name: str) -> int:
    result = _optional_int(value)
    if result is None:
        raise NavigationFormatError(f"missing {field_name}")
    return result


def _int_tuple(value: Any) -> tuple[int, ...]:
    return tuple(_int_value(item, "variant ID") for item in _as_list(value))


def _extract_buffer_bytes(value: Any) -> str | bytes:
    if isinstance(value, (str, bytes, bytearray, memoryview)):
        return value  # type: ignore[return-value]
    if isinstance(value, Mapping):
        for key in ("Bytes", "bytes", "$value"):
            candidate = value.get(key)
            if isinstance(candidate, (str, bytes, bytearray, memoryview)):
                return candidate  # type: ignore[return-value]
        for key in ("Data", "data", "Buffer", "buffer"):
            if key in value:
                try:
                    return _extract_buffer_bytes(value[key])
                except NavigationFormatError:
                    pass
    raise NavigationFormatError("tileBuffers entry does not contain embedded Bytes")


def _parse_vector(value: Any) -> Vec3 | None:
    mapping = _mapping(value)
    try:
        return Vec3(float(mapping["X"]), float(mapping["Y"]), float(mapping["Z"]))
    except (KeyError, TypeError, ValueError):
        return None


def _parse_bounds(value: Any) -> Bounds3 | None:
    mapping = _mapping(value)
    minimum = _parse_vector(mapping.get("Min"))
    maximum = _parse_vector(mapping.get("Max"))
    if minimum is None or maximum is None:
        return None
    return Bounds3(minimum, maximum)


def _flatten_buffers(
    navigation: Iterable[NavigationSector | NavTileBuffer],
) -> tuple[NavTileBuffer, ...]:
    result: list[NavTileBuffer] = []
    for value in navigation:
        if isinstance(value, NavigationSector):
            result.extend(value.buffers)
        elif isinstance(value, NavTileBuffer):
            result.append(value)
        else:
            raise TypeError(
                f"expected NavigationSector or NavTileBuffer, got {type(value).__name__}"
            )
    return tuple(
        sorted(
            result,
            key=lambda item: (
                item.source.resource_path,
                item.source.source_path,
                item.source.buffer_index,
                item.source.tile_data_index
                if item.source.tile_data_index is not None
                else -1,
            ),
        )
    )


def _quantize(value: float, quantum: float) -> int:
    scaled = value / quantum
    return math.floor(scaled + 0.5) if scaled >= 0 else math.ceil(scaled - 0.5)


def _point_key(point: Vec3, quantum: float) -> tuple[int, int, int]:
    return (
        _quantize(point.x, quantum),
        _quantize(point.y, quantum),
        _quantize(point.z, quantum),
    )


def _edge_key(
    first: Vec3, second: Vec3, quantum: float
) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    endpoints = sorted((_point_key(first, quantum), _point_key(second, quantum)))
    return endpoints[0], endpoints[1]


def _triangle_edges(
    vertices: tuple[Vec3, Vec3, Vec3],
) -> tuple[tuple[Vec3, Vec3], tuple[Vec3, Vec3], tuple[Vec3, Vec3]]:
    return (
        (vertices[0], vertices[1]),
        (vertices[1], vertices[2]),
        (vertices[2], vertices[0]),
    )


def _triangle_area(vertices: tuple[Vec3, Vec3, Vec3]) -> float:
    first, second, third = vertices
    ab = (second.x - first.x, second.y - first.y, second.z - first.z)
    ac = (third.x - first.x, third.y - first.y, third.z - first.z)
    cross = (
        ab[1] * ac[2] - ab[2] * ac[1],
        ab[2] * ac[0] - ab[0] * ac[2],
        ab[0] * ac[1] - ab[1] * ac[0],
    )
    return 0.5 * math.sqrt(sum(value * value for value in cross))


def _make_island(
    component: tuple[FaceRef, ...],
    face_records: Mapping[
        FaceRef, tuple[NavTileBuffer, NavFace, tuple[Vec3, Vec3, Vec3]]
    ],
    adjacency: Mapping[FaceRef, set[FaceRef]],
    edge_quantization_m: float,
) -> NavigationIsland:
    island_faces: list[IslandFace] = []
    vertices: list[Vec3] = []
    edge_occurrences: dict[
        tuple[tuple[int, int, int], tuple[int, int, int]], list[tuple[Vec3, Vec3]]
    ] = defaultdict(list)
    area = 0.0
    for ref in component:
        buffer, _face, face_vertices = face_records[ref]
        vertices.extend(face_vertices)
        area += _triangle_area(face_vertices)
        for edge in _triangle_edges(face_vertices):
            edge_occurrences[_edge_key(edge[0], edge[1], edge_quantization_m)].append(
                edge
            )
        island_faces.append(
            IslandFace(
                ref=ref,
                vertices=face_vertices,
                neighbors=tuple(sorted(adjacency[ref])),
                source=buffer.source,
            )
        )

    boundary_edges = tuple(
        occurrences[0]
        for _key, occurrences in sorted(edge_occurrences.items())
        if len(occurrences) == 1
    )
    minimum = Vec3(
        min(vertex.x for vertex in vertices),
        min(vertex.y for vertex in vertices),
        min(vertex.z for vertex in vertices),
    )
    maximum = Vec3(
        max(vertex.x for vertex in vertices),
        max(vertex.y for vertex in vertices),
        max(vertex.z for vertex in vertices),
    )
    boundary_length = sum(
        _distance_xy(first, second) for first, second in boundary_edges
    )
    width = _oriented_minor_extent(vertices)
    identity = "|".join(
        f"{ref.resource_path}:{ref.source_path}:{ref.buffer_index}:{ref.face_index}"
        for ref in component
    )
    island_id = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:20]
    return NavigationIsland(
        island_id=island_id,
        faces=tuple(island_faces),
        bounds=Bounds3(minimum, maximum),
        metrics=IslandMetrics(
            surface_area_m2=area,
            z_min=minimum.z,
            z_max=maximum.z,
            z_range_m=maximum.z - minimum.z,
            boundary_length_m=boundary_length,
            approximate_width_m=width,
        ),
        boundary_edges=boundary_edges,
    )


def _oriented_minor_extent(vertices: Sequence[Vec3]) -> float:
    unique = sorted({(point.x, point.y) for point in vertices})
    if len(unique) < 2:
        return 0.0
    hull = _convex_hull(unique)
    if len(hull) < 3:
        return 0.0
    best_score: tuple[float, float] | None = None
    best_minor_extent = 0.0
    for index, first in enumerate(hull):
        second = hull[(index + 1) % len(hull)]
        angle = math.atan2(second[1] - first[1], second[0] - first[0])
        cosine = math.cos(angle)
        sine = math.sin(angle)
        first_axis = [point[0] * cosine + point[1] * sine for point in hull]
        second_axis = [-point[0] * sine + point[1] * cosine for point in hull]
        first_extent = max(first_axis) - min(first_axis)
        second_extent = max(second_axis) - min(second_axis)
        score = (first_extent * second_extent, first_extent + second_extent)
        if best_score is None or score < best_score:
            best_score = score
            best_minor_extent = min(first_extent, second_extent)
    return best_minor_extent


def _convex_hull(points: Sequence[tuple[float, float]]) -> list[tuple[float, float]]:
    def cross(
        origin: tuple[float, float],
        first: tuple[float, float],
        second: tuple[float, float],
    ) -> float:
        return (first[0] - origin[0]) * (second[1] - origin[1]) - (
            first[1] - origin[1]
        ) * (second[0] - origin[0])

    ordered = sorted(set(points))
    if len(ordered) <= 1:
        return ordered
    lower: list[tuple[float, float]] = []
    for point in ordered:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper: list[tuple[float, float]] = []
    for point in reversed(ordered):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def _island_candidates(
    island: NavigationIsland, spacing_m: float
) -> tuple[tuple[Vec3, IslandFace], ...]:
    candidate_spacing = spacing_m / 3.0
    raw: list[tuple[Vec3, IslandFace]] = []
    for face in island.faces:
        lengths = [
            _distance_3d(first, second)
            for first, second in _triangle_edges(face.vertices)
        ]
        subdivisions = max(1, math.ceil(max(lengths) / candidate_spacing))
        first, second, third = face.vertices
        for row in range(subdivisions):
            for column in range(subdivisions - row):
                a = _barycentric_point(
                    first,
                    second,
                    third,
                    (row + 1.0 / 3.0) / subdivisions,
                    (column + 1.0 / 3.0) / subdivisions,
                )
                raw.append((a, face))
                if row + column <= subdivisions - 2:
                    b = _barycentric_point(
                        first,
                        second,
                        third,
                        (row + 2.0 / 3.0) / subdivisions,
                        (column + 2.0 / 3.0) / subdivisions,
                    )
                    raw.append((b, face))

    raw.sort(key=lambda item: (item[0].x, item[0].y, item[0].z, item[1].ref))
    deduplicated: list[tuple[Vec3, IslandFace]] = []
    seen: set[tuple[int, int, int]] = set()
    for candidate in raw:
        key = _point_key(candidate[0], 0.001)
        if key not in seen:
            seen.add(key)
            deduplicated.append(candidate)
    return tuple(deduplicated)


def _barycentric_point(
    first: Vec3, second: Vec3, third: Vec3, second_weight: float, third_weight: float
) -> Vec3:
    first_weight = 1.0 - second_weight - third_weight
    return Vec3(
        first.x * first_weight + second.x * second_weight + third.x * third_weight,
        first.y * first_weight + second.y * second_weight + third.y * third_weight,
        first.z * first_weight + second.z * second_weight + third.z * third_weight,
    )


def _distance_xy(first: Vec3, second: Vec3) -> float:
    return math.hypot(first.x - second.x, first.y - second.y)


def _distance_3d(first: Vec3, second: Vec3) -> float:
    return math.sqrt(first.distance_squared(second))


def _point_segment_distance_xy(point: Vec3, first: Vec3, second: Vec3) -> float:
    dx = second.x - first.x
    dy = second.y - first.y
    length_squared = dx * dx + dy * dy
    if length_squared == 0:
        return math.hypot(point.x - first.x, point.y - first.y)
    interpolation = (
        (point.x - first.x) * dx + (point.y - first.y) * dy
    ) / length_squared
    interpolation = max(0.0, min(1.0, interpolation))
    nearest_x = first.x + interpolation * dx
    nearest_y = first.y + interpolation * dy
    return math.hypot(point.x - nearest_x, point.y - nearest_y)


__all__ = [
    "AuxiliaryBoundsRecord",
    "Bounds3",
    "FaceConnection",
    "FaceRef",
    "IndexRecord",
    "InfoRecord",
    "IslandFace",
    "IslandMetrics",
    "NavFace",
    "NavTileBuffer",
    "NavigationFormatError",
    "NavigationIsland",
    "NavigationSample",
    "NavigationSector",
    "NavigationSource",
    "SampleProvenance",
    "VNAVHeader",
    "VAND_MAGIC",
    "VNAV_MAGIC",
    "Vec3",
    "ZeroPair",
    "decode_vnav_buffer",
    "load_navigation_sector",
    "local_width_at",
    "reconstruct_navigation_islands",
    "sample_navigation_islands",
    "vand_position_to_world",
]
