#!/usr/bin/env python3
"""World-sector indexing and variant-aware staging for location renders.

The module deliberately operates on WolvenKit CR2W-JSON rather than packed
``.streamingblock``/``.streamingsector`` resources.  It provides the small,
deterministic boundary needed by the world-location proof of concept:

* normalize streaming-block descriptors and group logical world variants;
* classify sector overlap against a tile's core, near, and optional far skirt;
* select the default range plus an explicit, mutually-exclusive world state;
* spatially clip nodeData instances and compact their node definitions; and
* emit content-addressed staged JSON plus a manifest row.

It does not edit or deserialize CR2W binaries.  The staged document is an
import/render input, not an authored replacement for the source sector.
"""

from __future__ import annotations

import base64
import binascii
import copy
import hashlib
import json
import math
import struct
from bisect import bisect_right
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


JsonObject = dict[str, Any]

GEOMETRY_POLICY_DETAILED = "detailed"
GEOMETRY_POLICY_PROXY_ONLY = "proxy_only"
DISTANCE_BANDS = ("core", "near", "far")
SPATIAL_CLIP_POLICY = "point_origin_safe_only_v1"
BLENDER_WOLVENKIT_COMPAT_VERSION = "8.17-compatible (ghostline-red staged JSON)"
BLENDER_TRANSFORM_BUFFER_POLICY = "wolvenkit_transform_buffers_v1"

_WORLD_TRANSFORM_RECORD = struct.Struct("<4i4f3fi")
_COOKED_TRANSFORM_RECORD = struct.Struct("<8f")
_WORLD_TRANSLATION_UNIT = 1.0 / 131_072.0
_WORLD_TRANSFORMS_BUFFER_TYPE = (
    "WolvenKit.RED4.Archive.Buffer.WorldTransformsBuffer, WolvenKit.RED4"
)
_COOKED_TRANSFORMS_BUFFER_TYPE = (
    "WolvenKit.RED4.Archive.Buffer.CookedInstanceTransformsBuffer, WolvenKit.RED4"
)

# ``worldNodeData.Bounds`` stores streaming reference points, not the
# transformed bound of the referenced mesh/entity/instance buffer.  It often
# degenerates to a point, but neither endpoint is guaranteed to equal Position
# and Min can exceed Max.  It therefore cannot prove that a placement outside
# the clip box has no geometry inside it.  Keep this allowlist deliberately
# narrow: every unlisted or future node type is conservatively retained until
# the staging pipeline can inspect accurate transformed resource bounds.
_POINT_ORIGIN_CLIP_SAFE_NODE_TYPES = frozenset(
    {
        "worldaispotnode",
        "worldaudiotagnode",
        "worldcrowdparkingspacenode",
        "worldspawnpointmarker",
        "worldstaticgpslocationentrancemarkernode",
        "worldstaticmarkernode",
    }
)

# Node branches which Cyberpunk IO Suite 1.8.0 can materialize as visible
# Blender geometry.  Markers, triggers, audio, smart objects, collisions (the
# POC disables collision import), lights (disabled), and unknown future nodes
# remain searchable metadata but are not part of the visual import gate.
BLENDER_VISUAL_NODE_TYPES = frozenset(
    {
        "worldadvertisementnode",
        "worldadvertisingnode",
        "worldbakeddestructionnode",
        "worldbendedmeshnode",
        "worldbuildingproxymeshnode",
        "worldclothmeshnode",
        "worlddecorationmeshnode",
        "worlddestructibleentityproxymeshnode",
        "worlddevicenode",
        "worlddynamicmeshnode",
        "worldentitynode",
        "worldgenericproxymeshnode",
        "worldinstanceddestructiblemeshnode",
        "worldinstancedmeshnode",
        "worldmeshnode",
        "worldphysicaldestructionnode",
        "worldroadproxymeshnode",
        "worldrotatingmeshnode",
        "worldstaticdecalnode",
        "worldstaticmeshnode",
        "worldstaticoccludermeshnode",
        "worldterrainmeshnode",
        "worldterrainproxymeshnode",
    }
)


class WorldLocationWorldError(ValueError):
    """Raised when world CR2W-JSON cannot be staged without guessing."""


def _canonical_json(value: Any) -> bytes:
    try:
        encoded = json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            separators=(",", ":"),
            sort_keys=True,
        )
    except (TypeError, ValueError) as exc:
        raise WorldLocationWorldError(f"Value is not canonical JSON: {exc}") from exc
    return encoded.encode("utf-8")


def content_fingerprint(value: Any) -> str:
    """Return a stable SHA-256 fingerprint of JSON-compatible content."""

    return hashlib.sha256(_canonical_json(value)).hexdigest()


def _typed_value(value: Any, default: Any = None) -> Any:
    if isinstance(value, Mapping):
        if "$value" in value:
            return value["$value"]
        if "value" in value and len(value) == 1:
            return value["value"]
    return default if value is None else value


def _as_int(value: Any, field: str, *, default: int | None = None) -> int:
    raw = _typed_value(value, default)
    if raw is None:
        raise WorldLocationWorldError(f"Missing integer field {field}.")
    if isinstance(raw, bool):
        return int(raw)
    try:
        result = int(raw)
    except (TypeError, ValueError) as exc:
        raise WorldLocationWorldError(f"Invalid integer for {field}: {raw!r}") from exc
    return result


def _as_float(value: Any, field: str) -> float:
    raw = _typed_value(value)
    try:
        result = float(raw)
    except (TypeError, ValueError) as exc:
        raise WorldLocationWorldError(f"Invalid number for {field}: {raw!r}") from exc
    if math.isnan(result):
        raise WorldLocationWorldError(f"NaN is not valid for {field}.")
    return result


def _as_bool(value: Any, field: str, *, default: bool = False) -> bool:
    raw = _typed_value(value, default)
    if isinstance(raw, bool):
        return raw
    if isinstance(raw, (int, float)):
        return bool(raw)
    if isinstance(raw, str):
        normalized = raw.strip().casefold()
        if normalized in {"1", "true", "yes", "on"}:
            return True
        if normalized in {"0", "false", "no", "off", ""}:
            return False
    raise WorldLocationWorldError(f"Invalid boolean for {field}: {raw!r}")


def _as_string(value: Any, *, default: str = "") -> str:
    raw = _typed_value(value, default)
    return default if raw is None else str(raw)


def normalize_depot_path(value: Any) -> str:
    """Normalize a DepotPath for deterministic comparison and manifests."""

    if isinstance(value, Mapping) and "DepotPath" in value:
        value = value["DepotPath"]
    raw = _as_string(value).strip().replace("/", "\\")
    while "\\\\" in raw:
        raw = raw.replace("\\\\", "\\")
    while raw.startswith(".\\"):
        raw = raw[2:]
    return raw.lstrip("\\").casefold()


def _node_ref(value: Any) -> str:
    return _as_string(value).strip()


@dataclass(frozen=True)
class AABB:
    min_x: float
    min_y: float
    min_z: float
    max_x: float
    max_y: float
    max_z: float

    def __post_init__(self) -> None:
        values = (
            self.min_x,
            self.min_y,
            self.min_z,
            self.max_x,
            self.max_y,
            self.max_z,
        )
        if any(math.isnan(value) for value in values):
            raise WorldLocationWorldError("AABB coordinates cannot be NaN.")
        if (
            self.min_x > self.max_x
            or self.min_y > self.max_y
            or self.min_z > self.max_z
        ):
            raise WorldLocationWorldError(f"AABB minimum exceeds maximum: {self!r}")

    @classmethod
    def from_wolvenkit_box(cls, value: Any) -> "AABB":
        if not isinstance(value, Mapping):
            raise WorldLocationWorldError("streamingBox must be an object.")
        minimum = value.get("Min")
        maximum = value.get("Max")
        if not isinstance(minimum, Mapping) or not isinstance(maximum, Mapping):
            raise WorldLocationWorldError(
                "streamingBox must contain Min and Max vectors."
            )
        return cls(
            min_x=_as_float(minimum.get("X"), "streamingBox.Min.X"),
            min_y=_as_float(minimum.get("Y"), "streamingBox.Min.Y"),
            min_z=_as_float(minimum.get("Z"), "streamingBox.Min.Z"),
            max_x=_as_float(maximum.get("X"), "streamingBox.Max.X"),
            max_y=_as_float(maximum.get("Y"), "streamingBox.Max.Y"),
            max_z=_as_float(maximum.get("Z"), "streamingBox.Max.Z"),
        )

    @classmethod
    def centered_square(
        cls,
        center: Sequence[float],
        size: float,
        *,
        z_min: float = -math.inf,
        z_max: float = math.inf,
    ) -> "AABB":
        if len(center) < 2:
            raise WorldLocationWorldError("Tile center needs at least X and Y.")
        size = float(size)
        if not math.isfinite(size) or size <= 0:
            raise WorldLocationWorldError("Tile size must be a positive finite number.")
        half = size / 2.0
        x = float(center[0])
        y = float(center[1])
        return cls(x - half, y - half, float(z_min), x + half, y + half, float(z_max))

    def expanded(self, margin: float) -> "AABB":
        margin = float(margin)
        if not math.isfinite(margin) or margin < 0:
            raise WorldLocationWorldError(
                "Clip margin must be a non-negative finite number."
            )
        return AABB(
            self.min_x - margin,
            self.min_y - margin,
            self.min_z - margin,
            self.max_x + margin,
            self.max_y + margin,
            self.max_z + margin,
        )

    def intersects(self, other: "AABB") -> bool:
        return not (
            self.max_x < other.min_x
            or self.min_x > other.max_x
            or self.max_y < other.min_y
            or self.min_y > other.max_y
            or self.max_z < other.min_z
            or self.min_z > other.max_z
        )

    def contains_point(self, point: Sequence[float]) -> bool:
        if len(point) < 3:
            raise WorldLocationWorldError("A point needs X, Y, and Z.")
        return (
            self.min_x <= float(point[0]) <= self.max_x
            and self.min_y <= float(point[1]) <= self.max_y
            and self.min_z <= float(point[2]) <= self.max_z
        )

    def as_dict(self) -> dict[str, dict[str, float | None]]:
        def portable(value: float) -> float | None:
            return value if math.isfinite(value) else None

        return {
            "min": {
                "x": portable(self.min_x),
                "y": portable(self.min_y),
                "z": portable(self.min_z),
            },
            "max": {
                "x": portable(self.max_x),
                "y": portable(self.max_y),
                "z": portable(self.max_z),
            },
        }


@dataclass(frozen=True, order=True)
class VariantKey:
    node_ref: str
    variant_id: int
    name: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "node_ref": self.node_ref,
            "variant_id": self.variant_id,
            "name": self.name,
        }


@dataclass(frozen=True)
class SectorVariant:
    key: VariantKey
    parent_variant_id: int
    range_index: int
    enabled_by_default: bool

    def as_dict(self) -> dict[str, Any]:
        return {
            **self.key.as_dict(),
            "parent_variant_id": self.parent_variant_id,
            "range_index": self.range_index,
            "enabled_by_default": self.enabled_by_default,
        }


@dataclass(frozen=True)
class SectorDescriptor:
    source_block: str
    block_fingerprint: str
    descriptor_index: int
    depot_path: str
    category: str
    level: int
    bounds: AABB
    quest_prefab_node_ref: str
    num_node_ranges: int
    variants: tuple[SectorVariant, ...]
    descriptor_fingerprint: str

    def sort_key(self) -> tuple[Any, ...]:
        return (
            self.depot_path.casefold(),
            self.category,
            self.level,
            self.source_block.casefold(),
            self.descriptor_index,
        )


@dataclass(frozen=True)
class VariantOccurrence:
    source_block: str
    descriptor_index: int
    depot_path: str
    range_index: int
    parent_variant_id: int
    enabled_by_default: bool


@dataclass(frozen=True)
class VariantGroup:
    key: VariantKey
    occurrences: tuple[VariantOccurrence, ...]

    @property
    def enabled_by_default(self) -> bool:
        return any(item.enabled_by_default for item in self.occurrences)


@dataclass(frozen=True)
class TileBounds:
    core: AABB
    near: AABB
    far: AABB | None

    @classmethod
    def from_center(
        cls,
        center: Sequence[float],
        *,
        core_size: float = 128.0,
        near_size: float = 256.0,
        far_size: float | None = 512.0,
        z_min: float = -math.inf,
        z_max: float = math.inf,
    ) -> "TileBounds":
        if near_size < core_size:
            raise WorldLocationWorldError("near_size must be at least core_size.")
        if far_size is not None and far_size < near_size:
            raise WorldLocationWorldError("far_size must be at least near_size.")
        core = AABB.centered_square(center, core_size, z_min=z_min, z_max=z_max)
        near = AABB.centered_square(center, near_size, z_min=z_min, z_max=z_max)
        far = (
            AABB.centered_square(center, far_size, z_min=z_min, z_max=z_max)
            if far_size is not None
            else None
        )
        return cls(core=core, near=near, far=far)


@dataclass(frozen=True)
class TileSectorOverlap:
    descriptor: SectorDescriptor
    distance_band: str
    geometry_policy: str

    def __post_init__(self) -> None:
        if self.distance_band not in DISTANCE_BANDS:
            raise WorldLocationWorldError(
                f"Invalid distance band {self.distance_band!r}."
            )
        expected = (
            GEOMETRY_POLICY_PROXY_ONLY
            if self.distance_band == "far"
            else GEOMETRY_POLICY_DETAILED
        )
        if self.geometry_policy != expected:
            raise WorldLocationWorldError(
                f"Distance band {self.distance_band!r} requires geometry policy {expected!r}."
            )


def _load_document(source: Path | str | Mapping[str, Any]) -> tuple[JsonObject, str]:
    if isinstance(source, Mapping):
        return dict(source), "<memory>"
    path = Path(source)
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise WorldLocationWorldError(f"Could not load {path}: {exc}") from exc
    if not isinstance(document, dict):
        raise WorldLocationWorldError(f"Expected a JSON object in {path}.")
    return document, str(path)


def _root_chunk(document: Mapping[str, Any], expected_type: str) -> JsonObject:
    data = document.get("Data")
    root = data.get("RootChunk") if isinstance(data, Mapping) else None
    if not isinstance(root, dict):
        raise WorldLocationWorldError("CR2W-JSON must contain Data.RootChunk.")
    root_type = root.get("$type")
    if root_type not in {None, expected_type}:
        raise WorldLocationWorldError(
            f"Expected RootChunk type {expected_type}, found {root_type!r}."
        )
    return root


def _parse_variant(
    value: Any, descriptor_index: int, variant_index: int
) -> SectorVariant:
    if not isinstance(value, Mapping):
        raise WorldLocationWorldError(
            f"Descriptor {descriptor_index} variant {variant_index} must be an object."
        )
    key = VariantKey(
        node_ref=_node_ref(value.get("nodeRef")),
        variant_id=_as_int(
            value.get("variantId"),
            f"descriptors[{descriptor_index}].variants[{variant_index}].variantId",
            default=0,
        ),
        name=_as_string(value.get("name")).strip(),
    )
    range_index = _as_int(
        value.get("rangeIndex"),
        f"descriptors[{descriptor_index}].variants[{variant_index}].rangeIndex",
    )
    if range_index < 0:
        raise WorldLocationWorldError(
            f"Variant rangeIndex cannot be negative; got {range_index}."
        )
    return SectorVariant(
        key=key,
        parent_variant_id=_as_int(
            value.get("parentVariantID"),
            f"descriptors[{descriptor_index}].variants[{variant_index}].parentVariantID",
            default=0,
        ),
        range_index=range_index,
        enabled_by_default=_as_bool(
            value.get("enabledByDefault"),
            f"descriptors[{descriptor_index}].variants[{variant_index}].enabledByDefault",
            default=False,
        ),
    )


def parse_streaming_block(
    source: Path | str | Mapping[str, Any],
    *,
    source_block: str | None = None,
) -> tuple[SectorDescriptor, ...]:
    """Parse and normalize the descriptors in a WolvenKit streaming block."""

    document, inferred_source = _load_document(source)
    root = _root_chunk(document, "worldStreamingBlock")
    source_name = inferred_source if source_block is None else str(source_block)
    block_fingerprint = content_fingerprint(document)
    raw_descriptors = root.get("descriptors", [])
    if not isinstance(raw_descriptors, list):
        raise WorldLocationWorldError("RootChunk.descriptors must be an array.")

    descriptors: list[SectorDescriptor] = []
    for index, raw in enumerate(raw_descriptors):
        if not isinstance(raw, Mapping):
            raise WorldLocationWorldError(f"Descriptor {index} must be an object.")
        data_ref = raw.get("data")
        depot_path = normalize_depot_path(data_ref)
        if not depot_path:
            raise WorldLocationWorldError(
                f"Descriptor {index} has no string DepotPath."
            )
        num_ranges = _as_int(
            raw.get("numNodeRanges"), f"descriptors[{index}].numNodeRanges"
        )
        if num_ranges < 1:
            raise WorldLocationWorldError(
                f"Descriptor {index} must contain a default node range."
            )
        raw_variants = raw.get("variants", [])
        if not isinstance(raw_variants, list):
            raise WorldLocationWorldError(
                f"Descriptor {index} variants must be an array."
            )
        variants = tuple(
            _parse_variant(item, index, item_index)
            for item_index, item in enumerate(raw_variants)
        )
        invalid_ranges = sorted(
            {item.range_index for item in variants if item.range_index >= num_ranges}
        )
        if invalid_ranges:
            raise WorldLocationWorldError(
                f"Descriptor {index} variant range indices exceed numNodeRanges {num_ranges}: "
                f"{invalid_ranges}"
            )
        descriptors.append(
            SectorDescriptor(
                source_block=source_name,
                block_fingerprint=block_fingerprint,
                descriptor_index=index,
                depot_path=depot_path,
                category=_as_string(raw.get("category"), default="unknown")
                .strip()
                .casefold(),
                level=_as_int(
                    raw.get("level"), f"descriptors[{index}].level", default=0
                ),
                bounds=AABB.from_wolvenkit_box(raw.get("streamingBox")),
                quest_prefab_node_ref=_node_ref(raw.get("questPrefabNodeRef")),
                num_node_ranges=num_ranges,
                variants=variants,
                descriptor_fingerprint=content_fingerprint(raw),
            )
        )
    return tuple(descriptors)


class WorldSectorIndex:
    """Deterministic in-memory spatial and variant index for streaming sectors."""

    def __init__(self, descriptors: Iterable[SectorDescriptor]) -> None:
        self.descriptors = tuple(sorted(descriptors, key=SectorDescriptor.sort_key))
        grouped: dict[VariantKey, list[VariantOccurrence]] = {}
        for descriptor in self.descriptors:
            for variant in descriptor.variants:
                grouped.setdefault(variant.key, []).append(
                    VariantOccurrence(
                        source_block=descriptor.source_block,
                        descriptor_index=descriptor.descriptor_index,
                        depot_path=descriptor.depot_path,
                        range_index=variant.range_index,
                        parent_variant_id=variant.parent_variant_id,
                        enabled_by_default=variant.enabled_by_default,
                    )
                )
        self.variant_groups = tuple(
            VariantGroup(
                key=key,
                occurrences=tuple(
                    sorted(
                        occurrences,
                        key=lambda item: (
                            item.depot_path.casefold(),
                            item.source_block.casefold(),
                            item.descriptor_index,
                            item.range_index,
                            item.parent_variant_id,
                            item.enabled_by_default,
                        ),
                    )
                ),
            )
            for key, occurrences in sorted(grouped.items())
        )

    @classmethod
    def from_streaming_blocks(
        cls, sources: Iterable[Path | str | Mapping[str, Any]]
    ) -> "WorldSectorIndex":
        descriptors: list[SectorDescriptor] = []
        for source_index, source in enumerate(sources):
            source_name = None
            if isinstance(source, Mapping):
                source_name = f"<memory:{source_index}>"
            descriptors.extend(parse_streaming_block(source, source_block=source_name))
        return cls(descriptors)

    def query(self, bounds: AABB) -> tuple[SectorDescriptor, ...]:
        return tuple(
            item for item in self.descriptors if item.bounds.intersects(bounds)
        )

    def query_tile(
        self,
        center: Sequence[float],
        *,
        core_size: float = 128.0,
        near_size: float = 256.0,
        far_size: float | None = 512.0,
        z_min: float = -math.inf,
        z_max: float = math.inf,
    ) -> tuple[TileBounds, tuple[TileSectorOverlap, ...]]:
        tile = TileBounds.from_center(
            center,
            core_size=core_size,
            near_size=near_size,
            far_size=far_size,
            z_min=z_min,
            z_max=z_max,
        )
        outer = tile.far or tile.near
        overlaps: list[TileSectorOverlap] = []
        for descriptor in self.query(outer):
            if descriptor.bounds.intersects(tile.core):
                band = "core"
            elif descriptor.bounds.intersects(tile.near):
                band = "near"
            else:
                band = "far"
            overlaps.append(
                TileSectorOverlap(
                    descriptor=descriptor,
                    distance_band=band,
                    geometry_policy=(
                        GEOMETRY_POLICY_PROXY_ONLY
                        if band == "far"
                        else GEOMETRY_POLICY_DETAILED
                    ),
                )
            )
        band_order = {name: index for index, name in enumerate(DISTANCE_BANDS)}
        overlaps.sort(
            key=lambda item: (
                band_order[item.distance_band],
                item.descriptor.sort_key(),
            )
        )
        return tile, tuple(overlaps)


class WorldStateSelector:
    """Resolve one explicit logical variant per NodeRef, plus default variants.

    A logical variant is the full ``(nodeRef, variantId, name)`` key.  The same
    key may occur in multiple sector descriptors or map to repeated ranges in
    one descriptor; all of those occurrences activate together.  Selecting a
    key suppresses enabled-by-default alternatives for that NodeRef while
    enabled defaults for untouched NodeRefs remain active.
    """

    def __init__(
        self,
        index: WorldSectorIndex,
        selected: Iterable[VariantKey] = (),
        *,
        include_enabled_defaults: bool = True,
    ) -> None:
        groups = {group.key: group for group in index.variant_groups}
        selected_keys = tuple(sorted(set(selected)))
        unknown = [key for key in selected_keys if key not in groups]
        if unknown:
            raise WorldLocationWorldError(
                "Unknown world-state variant(s): "
                + ", ".join(
                    json.dumps(item.as_dict(), sort_keys=True) for item in unknown
                )
            )
        by_node_ref: dict[str, VariantKey] = {}
        for key in selected_keys:
            existing = by_node_ref.get(key.node_ref)
            if existing is not None and existing != key:
                raise WorldLocationWorldError(
                    f"Mutually exclusive variants selected for NodeRef {key.node_ref!r}: "
                    f"{existing.name!r} and {key.name!r}."
                )
            by_node_ref[key.node_ref] = key

        active = set(selected_keys)
        if include_enabled_defaults:
            explicit_refs = set(by_node_ref)
            active.update(
                group.key
                for group in index.variant_groups
                if group.enabled_by_default and group.key.node_ref not in explicit_refs
            )
        self.index = index
        self.selected_keys = selected_keys
        self.active_keys = frozenset(active)
        self.include_enabled_defaults = bool(include_enabled_defaults)

    @classmethod
    def defaults(cls, index: WorldSectorIndex) -> "WorldStateSelector":
        return cls(index)

    def selected_ranges(self, descriptor: SectorDescriptor) -> tuple[int, ...]:
        ranges = {0}
        ranges.update(
            item.range_index
            for item in descriptor.variants
            if item.key in self.active_keys
        )
        return tuple(sorted(ranges))

    def active_variants(self, descriptor: SectorDescriptor) -> tuple[VariantKey, ...]:
        return tuple(
            sorted(
                {
                    item.key
                    for item in descriptor.variants
                    if item.key in self.active_keys
                }
            )
        )


def _node_data_records(root: Mapping[str, Any]) -> tuple[list[Any], str]:
    node_data = root.get("nodeData")
    if isinstance(node_data, Mapping):
        records = node_data.get("Data")
        if not isinstance(records, list):
            raise WorldLocationWorldError("RootChunk.nodeData.Data must be an array.")
        return records, "buffer"
    if isinstance(node_data, list):
        return node_data, "array"
    raise WorldLocationWorldError(
        "RootChunk.nodeData must be a DataBuffer object or array."
    )


def _range_for_instance(instance_index: int, starts: Sequence[int]) -> int:
    return bisect_right(starts, instance_index) - 1


def _instance_position(record: Any) -> tuple[float, float, float] | None:
    if not isinstance(record, Mapping):
        return None
    value = record.get("Position")
    if not isinstance(value, Mapping):
        return None
    try:
        return (
            _as_float(value.get("X"), "nodeData.Position.X"),
            _as_float(value.get("Y"), "nodeData.Position.Y"),
            _as_float(value.get("Z"), "nodeData.Position.Z"),
        )
    except WorldLocationWorldError:
        return None


def _node_definition_type(node: Any) -> str:
    """Return a node handle's RED type, or an empty string when unknown."""

    if not isinstance(node, Mapping):
        return ""
    data = node.get("Data")
    definition = data if isinstance(data, Mapping) else node
    return _as_string(definition.get("$type")).strip()


def _point_origin_clip_is_safe(node: Any) -> bool:
    """Whether a node can be rejected solely from its placement origin."""

    return _node_definition_type(node).casefold() in _POINT_ORIGIN_CLIP_SAFE_NODE_TYPES


def blender_node_is_visual(node: Any) -> bool:
    """Whether a node has a resource-backed visual dependency.

    Known node types remain catalogued in ``BLENDER_VISUAL_NODE_TYPES``, but
    staging must conservatively retain resource-bearing future types until
    transformed resource bounds and importer support are known.
    """

    return bool(_resource_paths(node))


def _set_node_index(record: JsonObject, new_index: int) -> None:
    current = record.get("NodeIndex")
    if isinstance(current, dict) and "$value" in current:
        current["$value"] = new_index
    else:
        record["NodeIndex"] = new_index


def _resource_paths(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, Mapping):
        depot = value.get("DepotPath")
        if depot is not None:
            path = normalize_depot_path(depot)
            if path and path != "0":
                found.add(path)
        for nested in value.values():
            found.update(_resource_paths(nested))
    elif isinstance(value, list):
        for nested in value:
            found.update(_resource_paths(nested))
    return found


def _embedded_file_name(value: Any) -> str:
    if not isinstance(value, Mapping):
        return ""
    return normalize_depot_path(value.get("FileName"))


def _filter_embedded_files(
    data: JsonObject,
    root: JsonObject,
    retained_nodes: Sequence[Any],
    retained_records: Sequence[Any],
    *,
    retain_all: bool,
) -> tuple[int, int, str]:
    embedded = data.get("EmbeddedFiles", [])
    if not isinstance(embedded, list):
        raise WorldLocationWorldError("Data.EmbeddedFiles must be an array.")
    source_count = len(embedded)
    if retain_all or not embedded:
        return source_count, source_count, "all" if retain_all else "referenced"

    needed = _resource_paths(retained_nodes) | _resource_paths(retained_records)
    by_name: dict[str, Any] = {}
    unnamed: list[Any] = []
    for item in embedded:
        name = _embedded_file_name(item)
        if name:
            by_name[name] = item
        else:
            unnamed.append(item)

    retained_names: set[str] = set()
    changed = True
    while changed:
        changed = False
        for name, item in by_name.items():
            if name not in needed or name in retained_names:
                continue
            retained_names.add(name)
            needed.update(
                _resource_paths(
                    item.get("Content") if isinstance(item, Mapping) else item
                )
            )
            changed = True

    filtered = [
        item
        for item in embedded
        if not _embedded_file_name(item) or _embedded_file_name(item) in retained_names
    ]
    data["EmbeddedFiles"] = filtered

    local = root.get("localInplaceResource")
    if isinstance(local, list):
        root["localInplaceResource"] = [
            item
            for item in local
            if not normalize_depot_path(item)
            or normalize_depot_path(item) in retained_names
        ]
    return source_count, len(filtered), "referenced"


def _decode_buffer_bytes(buffer: Mapping[str, Any], field: str) -> bytes:
    encoded = buffer.get("Bytes")
    if not isinstance(encoded, str):
        raise WorldLocationWorldError(
            f"{field} must contain base64 Bytes or expanded Data.Transforms."
        )
    try:
        return base64.b64decode(encoded.strip(), validate=True)
    except (binascii.Error, ValueError) as exc:
        raise WorldLocationWorldError(f"{field}.Bytes is not valid base64.") from exc


def _finite_transform(values: Sequence[float], field: str) -> None:
    if not all(math.isfinite(value) for value in values):
        raise WorldLocationWorldError(f"{field} contains a non-finite transform.")


def _decode_world_transforms(raw: bytes, field: str) -> list[JsonObject]:
    """Decode WolvenKit ``WorldTransformsBuffer`` records.

    RED stores each record as three 17.17 fixed-point translations plus one
    unused int32, a quaternion, a Vector3 scale, and one unused int32.  This is
    the layout used by WolvenKit's ``WorldTransformsReader`` and consumed by
    Cyberpunk IO Suite's sector importer after JSON expansion.
    """

    if len(raw) % _WORLD_TRANSFORM_RECORD.size:
        raise WorldLocationWorldError(
            f"{field}.Bytes has {len(raw)} bytes; world transform buffers must "
            f"be a multiple of {_WORLD_TRANSFORM_RECORD.size}."
        )
    result: list[JsonObject] = []
    for index, record in enumerate(_WORLD_TRANSFORM_RECORD.iter_unpack(raw)):
        (
            translation_x,
            translation_y,
            translation_z,
            _translation_w,
            rotation_i,
            rotation_j,
            rotation_k,
            rotation_r,
            scale_x,
            scale_y,
            scale_z,
            _scale_w,
        ) = record
        translation = (
            translation_x * _WORLD_TRANSLATION_UNIT,
            translation_y * _WORLD_TRANSLATION_UNIT,
            translation_z * _WORLD_TRANSLATION_UNIT,
        )
        values = (
            *translation,
            rotation_i,
            rotation_j,
            rotation_k,
            rotation_r,
            scale_x,
            scale_y,
            scale_z,
        )
        _finite_transform(values, f"{field}.Transforms[{index}]")
        result.append(
            {
                "$type": "worldNodeTransform",
                "rotation": {
                    "$type": "Quaternion",
                    "i": rotation_i,
                    "j": rotation_j,
                    "k": rotation_k,
                    "r": rotation_r,
                },
                "scale": {
                    "$type": "Vector3",
                    "X": scale_x,
                    "Y": scale_y,
                    "Z": scale_z,
                },
                "translation": {
                    "$type": "Vector3",
                    "X": translation[0],
                    "Y": translation[1],
                    "Z": translation[2],
                },
            }
        )
    return result


def _decode_cooked_transforms(raw: bytes, field: str) -> list[JsonObject]:
    """Decode WolvenKit ``CookedInstanceTransformsBuffer`` records."""

    if len(raw) % _COOKED_TRANSFORM_RECORD.size:
        raise WorldLocationWorldError(
            f"{field}.Bytes has {len(raw)} bytes; cooked transform buffers must "
            f"be a multiple of {_COOKED_TRANSFORM_RECORD.size}."
        )
    result: list[JsonObject] = []
    for index, record in enumerate(_COOKED_TRANSFORM_RECORD.iter_unpack(raw)):
        (
            position_x,
            position_y,
            position_z,
            position_w,
            orientation_i,
            orientation_j,
            orientation_k,
            orientation_r,
        ) = record
        _finite_transform(record, f"{field}.Transforms[{index}]")
        result.append(
            {
                "$type": "Transform",
                "orientation": {
                    "$type": "Quaternion",
                    "i": orientation_i,
                    "j": orientation_j,
                    "k": orientation_k,
                    "r": orientation_r,
                },
                "position": {
                    "$type": "Vector4",
                    "W": position_w,
                    "X": position_x,
                    "Y": position_y,
                    "Z": position_z,
                },
            }
        )
    return result


_TRANSFORM_BUFFER_FIELDS = {
    "worldInstancedMeshNode": ("worldTransformsBuffer", "world"),
    "worldInstancedDestructibleMeshNode": (
        "cookedInstanceTransforms",
        "cooked",
    ),
}


def _node_transform_buffer(
    node: Any,
) -> tuple[str, str, JsonObject] | None:
    if not isinstance(node, Mapping):
        return None
    raw_data = node.get("Data")
    if not isinstance(raw_data, Mapping):
        return None
    node_type = _as_string(raw_data.get("$type"))
    specification = _TRANSFORM_BUFFER_FIELDS.get(node_type)
    if specification is None:
        return None
    buffer_field, buffer_kind = specification
    transform_buffer = raw_data.get(buffer_field)
    if not isinstance(transform_buffer, Mapping):
        return None
    shared = transform_buffer.get("sharedDataBuffer")
    if not isinstance(shared, dict):
        return None
    return buffer_field, buffer_kind, shared


def _transform_buffer_sources(
    nodes: Sequence[Any],
) -> dict[str, tuple[int, str, JsonObject]]:
    sources: dict[str, tuple[int, str, JsonObject]] = {}
    for node_index, node in enumerate(nodes):
        match = _node_transform_buffer(node)
        if match is None:
            continue
        _buffer_field, buffer_kind, shared = match
        handle_id = _as_string(shared.get("HandleId")).strip()
        data = shared.get("Data")
        if not handle_id or not isinstance(data, dict):
            continue
        previous = sources.get(handle_id)
        if previous is not None and previous[0] != node_index:
            raise WorldLocationWorldError(
                f"Duplicate shared transform buffer HandleId {handle_id}."
            )
        sources[handle_id] = (node_index, buffer_kind, data)
    return sources


def _retain_transform_buffer_owners(
    nodes: Sequence[Any], retained_indices: set[int]
) -> tuple[set[int], int]:
    """Retain definitions which own buffers referenced by selected nodes."""

    sources = _transform_buffer_sources(nodes)
    expanded = set(retained_indices)
    dependency_indices: set[int] = set()
    for node_index in sorted(retained_indices):
        match = _node_transform_buffer(nodes[node_index])
        if match is None:
            continue
        buffer_field, buffer_kind, shared = match
        if isinstance(shared.get("Data"), Mapping):
            continue
        handle_ref = _as_string(shared.get("HandleRefId")).strip()
        if not handle_ref:
            raise WorldLocationWorldError(
                f"nodes[{node_index}].Data.{buffer_field}.sharedDataBuffer has "
                "neither inline Data nor HandleRefId."
            )
        source = sources.get(handle_ref)
        if source is None:
            raise WorldLocationWorldError(
                f"nodes[{node_index}].Data.{buffer_field}.sharedDataBuffer "
                f"references missing HandleId {handle_ref}."
            )
        owner_index, owner_kind, _owner_data = source
        if owner_kind != buffer_kind:
            raise WorldLocationWorldError(
                f"Shared transform buffer HandleId {handle_ref} is used as both "
                f"{owner_kind} and {buffer_kind}."
            )
        if owner_index not in expanded:
            expanded.add(owner_index)
            dependency_indices.add(owner_index)
    return expanded, len(dependency_indices)


def expand_blender_transform_buffers(nodes: Sequence[Any]) -> dict[str, int]:
    """Expand native transform bytes into the JSON shape used by Blender.

    ``ghostline-red`` deliberately preserves unknown ``DataBuffer`` payloads as
    base64.  The installed Cyberpunk IO Suite sector importer instead expects
    WolvenKit's semantic ``buffer.Data.Transforms`` representation.  Only the
    two transform formats with authoritative WolvenKit readers are expanded.
    Original ``Bytes`` remain in place so the staged document remains auditable.
    """

    inserted: dict[str, int] = {}

    def increment(key: str, amount: int = 1) -> None:
        inserted[key] = inserted.get(key, 0) + amount

    sources = _transform_buffer_sources(nodes)
    for node_index, node in enumerate(nodes):
        match = _node_transform_buffer(node)
        if match is None:
            continue
        buffer_field, buffer_kind, shared = match
        shared_data = shared.get("Data")
        if not isinstance(shared_data, dict):
            handle_ref = _as_string(shared.get("HandleRefId")).strip()
            source = sources.get(handle_ref)
            if source is None:
                raise WorldLocationWorldError(
                    f"nodes[{node_index}].Data.{buffer_field}.sharedDataBuffer "
                    f"references missing HandleId {handle_ref or '<empty>'}."
                )
            owner_index, owner_kind, owner_data = source
            if owner_kind != buffer_kind:
                raise WorldLocationWorldError(
                    f"Shared transform buffer HandleId {handle_ref} is used as "
                    f"both {owner_kind} and {buffer_kind}."
                )
            owner_handle = _as_string(
                nodes[owner_index].get("HandleId")
                if isinstance(nodes[owner_index], Mapping)
                else ""
            ).strip()
            try:
                addon_owner_handle = str(int(handle_ref) - 1)
            except ValueError:
                addon_owner_handle = ""
            if owner_handle != addon_owner_handle:
                shared_data = copy.deepcopy(owner_data)
                shared["Data"] = shared_data
                increment("inlined_shared_buffer_references")
            else:
                # Cyberpunk IO Suite resolves HandleRefId to the parent node
                # whose HandleId is one less, so expanding the owner is enough.
                continue

        buffer = shared_data.get("buffer")
        if not isinstance(buffer, dict):
            raise WorldLocationWorldError(
                f"nodes[{node_index}].Data.{buffer_field}.sharedDataBuffer.Data.buffer "
                "must be an object."
            )
        expanded_data = buffer.get("Data")
        if isinstance(expanded_data, Mapping):
            transforms = expanded_data.get("Transforms")
            if not isinstance(transforms, list):
                raise WorldLocationWorldError(
                    f"nodes[{node_index}].Data.{buffer_field} expanded buffer "
                    "must contain Data.Transforms."
                )
            increment("preexpanded_buffers")
            increment("preexpanded_transforms", len(transforms))
            continue

        field = f"nodes[{node_index}].Data.{buffer_field}.sharedDataBuffer.Data.buffer"
        raw = _decode_buffer_bytes(buffer, field)
        if buffer_kind == "world":
            transforms = _decode_world_transforms(raw, field)
            buffer["Type"] = _WORLD_TRANSFORMS_BUFFER_TYPE
            increment("decoded_world_buffers")
            increment("decoded_world_transforms", len(transforms))
        else:
            transforms = _decode_cooked_transforms(raw, field)
            buffer["Type"] = _COOKED_TRANSFORMS_BUFFER_TYPE
            increment("decoded_cooked_buffers")
            increment("decoded_cooked_transforms", len(transforms))
        buffer["Data"] = {"Transforms": transforms}
    return dict(sorted(inserted.items()))


def complete_blender_sector_defaults(document: JsonObject) -> dict[str, int]:
    """Fill defaults assumed unconditionally by Cyberpunk IO Suite 1.8.0.

    CR2W only serializes values which differ from RED class defaults, whereas
    WolvenKit's JSON converter expands a handful of those defaults.  The
    installed Blender sector importer indexes those expanded properties
    directly.  This adapter is intentionally narrow and only supplies values
    whose class defaults are needed by importer branches exercised by staged
    world sectors; authored non-default values always win.
    """

    header = document.setdefault("Header", {})
    if not isinstance(header, dict):
        raise WorldLocationWorldError("CR2W-JSON Header must be an object.")
    original_version = str(header.get("WolvenKitVersion", ""))
    if "8.17" not in original_version:
        if original_version:
            header.setdefault("GhostlineOriginalExporterVersion", original_version)
        header["WolvenKitVersion"] = BLENDER_WOLVENKIT_COMPAT_VERSION

    root = _root_chunk(document, "worldStreamingSector")
    nodes = root.get("nodes")
    if not isinstance(nodes, list):
        raise WorldLocationWorldError("RootChunk.nodes must be an array.")

    inserted: dict[str, int] = {}

    def add(target: JsonObject, key: str, value: Any, node_type: str) -> None:
        if key not in target:
            target[key] = copy.deepcopy(value)
            label = f"{node_type}.{key}"
            inserted[label] = inserted.get(label, 0) + 1

    default_name = {"$type": "CName", "$storage": "string", "$value": "default"}
    for node in nodes:
        if not isinstance(node, Mapping):
            continue
        raw_data = node.get("Data")
        if not isinstance(raw_data, dict):
            continue
        node_type = _as_string(raw_data.get("$type"))
        if node_type == "worldStaticDecalNode":
            add(raw_data, "horizontalFlip", 0, node_type)
            add(raw_data, "verticalFlip", 0, node_type)
            add(raw_data, "alpha", 1.0, node_type)
        elif node_type in {"worldEntityNode", "worldDeviceNode"}:
            add(raw_data, "appearanceName", default_name, node_type)
        elif node_type == "worldAISpotNode":
            add(raw_data, "markings", [], node_type)
        elif node_type == "worldPopulationSpawnerNode":
            add(raw_data, "appearanceName", default_name, node_type)
            add(raw_data, "spawnOnStart", 0, node_type)
        elif node_type == "worldRotatingMeshNode":
            add(raw_data, "reverseDirection", 0, node_type)

        buffer_fields: tuple[str, ...] = ()
        buffer_key = ""
        if node_type == "worldInstancedMeshNode":
            buffer_key = "worldTransformsBuffer"
            buffer_fields = ("startIndex",)
        elif node_type == "worldInstancedDestructibleMeshNode":
            buffer_key = "cookedInstanceTransforms"
            buffer_fields = ("startIndex",)
        elif node_type == "worldFoliageNode":
            buffer_key = "populationSpanInfo"
            buffer_fields = ("cketBegin", "stancesBegin")
        if buffer_key:
            buffer = raw_data.get(buffer_key)
            if isinstance(buffer, dict):
                for field in buffer_fields:
                    add(buffer, field, 0, f"{node_type}.{buffer_key}")
    return dict(sorted(inserted.items()))


@dataclass
class StagedSector:
    document: JsonObject
    manifest_row: JsonObject

    def write(self, output_path: Path | str) -> JsonObject:
        """Write deterministic staged JSON and return the updated manifest row."""

        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(self.document, ensure_ascii=False, indent=2, sort_keys=True)
            + "\n",
            encoding="utf-8",
        )
        self.manifest_row["staged_path"] = str(path)
        return dict(self.manifest_row)


def stage_streaming_sector(
    source: Path | str | Mapping[str, Any],
    descriptor: SectorDescriptor,
    selector: WorldStateSelector | None = None,
    *,
    tile_id: str = "",
    overlap: TileSectorOverlap | None = None,
    clip_bounds: AABB | None = None,
    clip_margin: float = 0.0,
    retain_all_embedded: bool = False,
) -> StagedSector:
    """Filter and compact one serialized streaming sector for Blender import.

    Variant membership is determined by the *position in nodeData*, using the
    half-open ranges in ``RootChunk.variantIndices``.  Spatial clipping is then
    applied per retained instance.  Point origins are only authoritative for a
    narrow set of explicitly point-like node types.  Meshes, terrain, roads,
    bended meshes, instanced groups, entities, and unknown node types are kept
    when their origin is outside because transformed resource bounds are not
    available here.  Every referenced node definition is copied exactly once,
    in original order, and NodeIndex values are remapped to the compact array.
    """

    clip_margin = float(clip_margin)
    if not math.isfinite(clip_margin) or clip_margin < 0:
        raise WorldLocationWorldError(
            "Clip margin must be a non-negative finite number."
        )
    document, source_name = _load_document(source)
    staged = copy.deepcopy(document)
    root = _root_chunk(staged, "worldStreamingSector")
    source_root = _root_chunk(document, "worldStreamingSector")
    source_records, _ = _node_data_records(source_root)
    staged_records, node_data_shape = _node_data_records(root)
    nodes = root.get("nodes")
    if not isinstance(nodes, list):
        raise WorldLocationWorldError("RootChunk.nodes must be an array.")
    # Validate every native transform buffer before filtering. A malformed
    # buffer must not escape detection merely because its node has no currently
    # previewable resource dependency.
    expand_blender_transform_buffers(copy.deepcopy(nodes))

    raw_starts = root.get("variantIndices")
    if not isinstance(raw_starts, list) or not raw_starts:
        raise WorldLocationWorldError(
            "RootChunk.variantIndices must contain the default range."
        )
    starts = [
        _as_int(value, f"RootChunk.variantIndices[{index}]")
        for index, value in enumerate(raw_starts)
    ]
    if starts[0] != 0:
        raise WorldLocationWorldError(
            "RootChunk.variantIndices[0] must start the default range at 0."
        )
    if any(left > right for left, right in zip(starts, starts[1:])):
        raise WorldLocationWorldError(
            "RootChunk.variantIndices must be non-decreasing."
        )
    if starts[-1] > len(staged_records):
        raise WorldLocationWorldError(
            "RootChunk.variantIndices starts beyond nodeData length."
        )
    if descriptor.num_node_ranges != len(starts):
        raise WorldLocationWorldError(
            f"Descriptor declares {descriptor.num_node_ranges} ranges but sector contains {len(starts)}."
        )

    if selector is None:
        selector = WorldStateSelector(WorldSectorIndex([descriptor]))
    selected_ranges = selector.selected_ranges(descriptor)
    invalid_selected = [value for value in selected_ranges if value >= len(starts)]
    if invalid_selected:
        raise WorldLocationWorldError(
            f"Selected range indices do not exist: {invalid_selected}"
        )
    selected_range_set = set(selected_ranges)

    after_variant: list[tuple[int, Any]] = [
        (index, record)
        for index, record in enumerate(staged_records)
        if _range_for_instance(index, starts) in selected_range_set
    ]
    dropped_variant = len(staged_records) - len(after_variant)

    effective_clip = (
        clip_bounds.expanded(clip_margin) if clip_bounds is not None else None
    )
    after_spatial: list[tuple[int, Any, int]] = []
    dropped_spatial = 0
    unlocated_retained = 0
    conservative_spatial_retained = 0
    conservative_spatial_node_types: set[str] = set()
    for instance_index, record in after_variant:
        if not isinstance(record, Mapping):
            raise WorldLocationWorldError(
                f"nodeData[{instance_index}] must be an object."
            )
        old_index = _as_int(
            record.get("NodeIndex"), f"nodeData[{instance_index}].NodeIndex"
        )
        if old_index < 0 or old_index >= len(nodes):
            raise WorldLocationWorldError(
                f"nodeData[{instance_index}].NodeIndex {old_index} is outside nodes[0:{len(nodes)}]."
            )
        node_type = _node_definition_type(nodes[old_index]).casefold()
        if not blender_node_is_visual(nodes[old_index]) or node_type in {
            "worlddevicenode",
            "worldentitynode",
        }:
            dropped_spatial += 1
            continue
        position = _instance_position(record)
        if (
            effective_clip is not None
            and position is not None
            and not effective_clip.contains_point(position)
        ):
            node = nodes[old_index]
            if _point_origin_clip_is_safe(node):
                dropped_spatial += 1
                continue
            conservative_spatial_retained += 1
            conservative_spatial_node_types.add(
                _node_definition_type(node) or "<unknown>"
            )
        if effective_clip is not None and position is None:
            unlocated_retained += 1
        after_spatial.append((instance_index, record, old_index))

    instance_node_indices = {old_index for _, _, old_index in after_spatial}
    retained_old_node_indices, dependency_retained_node_count = (
        _retain_transform_buffer_owners(nodes, instance_node_indices)
    )

    ordered_old_indices = sorted(retained_old_node_indices)
    remap = {
        old_index: new_index for new_index, old_index in enumerate(ordered_old_indices)
    }
    retained_nodes = [
        copy.deepcopy(nodes[old_index]) for old_index in ordered_old_indices
    ]
    transform_buffer_expansion = expand_blender_transform_buffers(retained_nodes)
    retained_records: list[Any] = []
    for instance_index, record, old_index in after_spatial:
        copied = copy.deepcopy(record)
        if not isinstance(copied, dict):
            raise WorldLocationWorldError(
                f"nodeData[{instance_index}] must be an object."
            )
        _set_node_index(copied, remap[old_index])
        retained_records.append(copied)

    root["nodes"] = retained_nodes
    if node_data_shape == "buffer":
        node_data = root["nodeData"]
        assert isinstance(node_data, dict)
        node_data["Data"] = retained_records
    else:
        root["nodeData"] = retained_records
    root["variantIndices"] = [0]
    root["persistentNodeIndex"] = 0
    if "persistentNodes" in root:
        root["persistentNodes"] = []
    if "variantNodes" in root:
        root["variantNodes"] = []

    data = staged.get("Data")
    if not isinstance(data, dict):
        raise WorldLocationWorldError("CR2W-JSON Data must be an object.")
    source_embedded, retained_embedded, embedded_policy = _filter_embedded_files(
        data,
        root,
        retained_nodes,
        retained_records,
        retain_all=retain_all_embedded,
    )
    blender_compatibility_defaults = complete_blender_sector_defaults(staged)

    source_fingerprint = content_fingerprint(document)
    staged_fingerprint = content_fingerprint(staged)
    active_variants = selector.active_variants(descriptor)
    selection_payload = {
        "active_variants": [item.as_dict() for item in active_variants],
        "selected_ranges": list(selected_ranges),
        "clip_bounds": clip_bounds.as_dict() if clip_bounds is not None else None,
        "effective_clip_bounds": (
            effective_clip.as_dict() if effective_clip is not None else None
        ),
        "clip_margin": clip_margin,
        "spatial_clip_policy": SPATIAL_CLIP_POLICY,
        "blender_transform_buffer_policy": BLENDER_TRANSFORM_BUFFER_POLICY,
    }
    distance_band = overlap.distance_band if overlap is not None else "core"
    geometry_policy = (
        overlap.geometry_policy if overlap is not None else GEOMETRY_POLICY_DETAILED
    )
    if overlap is not None and overlap.descriptor != descriptor:
        raise WorldLocationWorldError(
            "Tile overlap descriptor does not match staged descriptor."
        )

    manifest: JsonObject = {
        "tile_id": str(tile_id),
        "depot_path": descriptor.depot_path,
        "source_block": descriptor.source_block,
        "source_sector_path": source_name,
        "descriptor_index": descriptor.descriptor_index,
        "category": descriptor.category,
        "level": descriptor.level,
        "bounds": descriptor.bounds.as_dict(),
        "quest_prefab_node_ref": descriptor.quest_prefab_node_ref,
        "distance_band": distance_band,
        "geometry_policy": geometry_policy,
        "selected_range_indices": list(selected_ranges),
        "active_variants": [item.as_dict() for item in active_variants],
        "clip_bounds": clip_bounds.as_dict() if clip_bounds is not None else None,
        "effective_clip_bounds": (
            effective_clip.as_dict() if effective_clip is not None else None
        ),
        "clip_margin": clip_margin,
        "spatial_clip_policy": SPATIAL_CLIP_POLICY,
        "blender_transform_buffer_policy": BLENDER_TRANSFORM_BUFFER_POLICY,
        "source_instance_count": len(source_records),
        "variant_retained_instance_count": len(after_variant),
        "dropped_variant_instance_count": dropped_variant,
        "dropped_spatial_instance_count": dropped_spatial,
        "unlocated_retained_instance_count": unlocated_retained,
        "conservative_spatial_retained_instance_count": conservative_spatial_retained,
        "conservative_spatial_retained_node_types": sorted(
            conservative_spatial_node_types
        ),
        "retained_instance_count": len(retained_records),
        "source_node_count": len(nodes),
        "retained_node_count": len(retained_nodes),
        "dependency_retained_node_count": dependency_retained_node_count,
        "dropped_node_count": len(nodes) - len(retained_nodes),
        "source_embedded_file_count": source_embedded,
        "retained_embedded_file_count": retained_embedded,
        "dropped_embedded_file_count": source_embedded - retained_embedded,
        "embedded_file_policy": embedded_policy,
        "blender_transform_buffer_expansion": transform_buffer_expansion,
        "blender_compatibility_defaults": blender_compatibility_defaults,
        "block_fingerprint": descriptor.block_fingerprint,
        "descriptor_fingerprint": descriptor.descriptor_fingerprint,
        "source_sector_fingerprint": source_fingerprint,
        "world_state_fingerprint": content_fingerprint(selection_payload),
        "staged_sector_fingerprint": staged_fingerprint,
        "node_index_remap": {str(old): new for old, new in remap.items()},
    }
    return StagedSector(document=staged, manifest_row=manifest)


__all__ = [
    "AABB",
    "BLENDER_VISUAL_NODE_TYPES",
    "BLENDER_TRANSFORM_BUFFER_POLICY",
    "BLENDER_WOLVENKIT_COMPAT_VERSION",
    "DISTANCE_BANDS",
    "GEOMETRY_POLICY_DETAILED",
    "GEOMETRY_POLICY_PROXY_ONLY",
    "SectorDescriptor",
    "SectorVariant",
    "StagedSector",
    "TileBounds",
    "TileSectorOverlap",
    "VariantGroup",
    "VariantKey",
    "VariantOccurrence",
    "WorldLocationWorldError",
    "WorldSectorIndex",
    "WorldStateSelector",
    "content_fingerprint",
    "complete_blender_sector_defaults",
    "blender_node_is_visual",
    "expand_blender_transform_buffers",
    "normalize_depot_path",
    "parse_streaming_block",
    "stage_streaming_sector",
]
