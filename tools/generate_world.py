#!/usr/bin/env python3
"""Generate Ghostline streamingblock/streamingsector CR2W-JSON from coordinates.

The input spec is intentionally small: capture a world origin in game, describe
markers/triggers as absolute positions or local offsets from that origin, and
let this tool emit the raw CR2W-JSON that WolvenKit can deserialize.
"""

from __future__ import annotations

import argparse
import base64
import json
import math
import struct
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from cr2w_helpers import load_json, print_json, print_table


DEFAULT_WOLVENKIT = Path(r"H:\WolvenKit.Console-8.17.4\WolvenKit.CLI.exe")
DEFAULT_RAW_ROOT = Path("source/raw")
DEFAULT_ARCHIVE_ROOT = Path("source/archive")
DEFAULT_ARCHIVE_XL = Path("source/resources/Ghostline.archive.xl")

WORLD_FLOAT = 3.40282347e38
FNV64_OFFSET = 0xCBF29CE484222325
FNV64_PRIME = 0x100000001B3
UINT64_MASK = (1 << 64) - 1


@dataclass(frozen=True)
class Vec3:
    x: float
    y: float
    z: float

    def offset(self, dx: float, dy: float, dz: float) -> "Vec3":
        return Vec3(self.x + dx, self.y + dy, self.z + dz)


@dataclass(frozen=True)
class Anchor:
    position: Vec3
    yaw: float
    node_index: int | None = None


@dataclass(frozen=True)
class GeneratedFile:
    kind: str
    depot_path: str
    raw_path: Path
    archive_path: Path


@dataclass(frozen=True)
class MeasurePoint:
    label: str
    position: Vec3


@dataclass(frozen=True)
class CommunitySpot:
    spec: dict[str, Any]
    ref: str
    full_ref: str
    global_node_id: int
    position: Vec3
    yaw: float


@dataclass(frozen=True)
class CommunityEntry:
    spec: dict[str, Any]
    spots: tuple[CommunitySpot, ...]


@dataclass(frozen=True)
class DeviceRegistryEntry:
    node_ref: str
    node_hash: int
    controller_class: str
    position: Vec3


class HandleAllocator:
    def __init__(self) -> None:
        self.next_id = 0

    def take(self) -> str:
        value = str(self.next_id)
        self.next_id += 1
        return value


def node_ref_hash(value: str) -> int:
    """Match WolvenKit RED4 NodeRef.GetRedHash for runtime NodeRefs.

    RED4 NodeRef hashing is FNV1A64 over UTF-16 code units, but `#` alias
    markers are skipped. `#;.../` semicolon aliases are skipped through the next
    slash; this mirrors WolvenKit's HashStringWithoutAliases implementation.
    """

    if not value:
        return 0
    hash_value = FNV64_OFFSET
    index = 0
    while index < len(value):
        if value[index] == "#":
            index += 1
            if index < len(value) and value[index] == ";":
                next_slash = value.find("/", index)
                index = len(value) if next_slash == -1 else next_slash
        if index >= len(value):
            break
        hash_value ^= ord(value[index])
        hash_value = (hash_value * FNV64_PRIME) & UINT64_MASK
        index += 1
    return hash_value


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def normalize_depot_path(value: str) -> str:
    return str(value).replace("/", "\\")


def depot_to_raw_path(raw_root: Path, depot_path: str) -> Path:
    return raw_root / Path(normalize_depot_path(depot_path) + ".json")


def depot_to_archive_path(archive_root: Path, depot_path: str) -> Path:
    return archive_root / Path(normalize_depot_path(depot_path))


def local_ref_name(value: str) -> str:
    value = str(value)
    if "/" in value:
        value = value.rsplit("/", 1)[-1]
    return value[1:] if value.startswith("#") else value


def debug_name(ref: str, explicit: str | None = None) -> str:
    return explicit if explicit is not None else "{" + local_ref_name(ref) + "}"


def full_node_ref(prefab_root: str, value: str) -> str:
    value = str(value)
    if value.startswith("$/"):
        return value
    if not value.startswith("#"):
        value = "#" + value
    return f"{prefab_root.rstrip('/')}/{value}"


def register_anchor(anchors: dict[str, Anchor], ref: str, anchor: Anchor) -> None:
    names = {ref, local_ref_name(ref), "#" + local_ref_name(ref)}
    for name in names:
        anchors[name] = anchor


def vector3(value: Vec3) -> dict[str, Any]:
    return {"$type": "Vector3", "X": value.x, "Y": value.y, "Z": value.z}


def vector4(value: Vec3, w: float = 0) -> dict[str, Any]:
    return {"$type": "Vector4", "W": w, "X": value.x, "Y": value.y, "Z": value.z}


def quaternion_from_yaw(yaw: float) -> dict[str, Any]:
    radians = math.radians(yaw) / 2
    return {"$type": "Quaternion", "i": 0, "j": 0, "k": math.sin(radians), "r": math.cos(radians)}


def node_ref(value: str) -> dict[str, Any]:
    return {"$type": "NodeRef", "$storage": "string", "$value": value}


def node_ref_u64(value: int | str) -> dict[str, Any]:
    return {"$type": "NodeRef", "$storage": "uint64", "$value": str(value)}


def cname(value: str) -> dict[str, Any]:
    return {"$type": "CName", "$storage": "string", "$value": value}


def resource_path(value: str, storage: str = "string", flags: str = "Soft") -> dict[str, Any]:
    return {"DepotPath": {"$type": "ResourcePath", "$storage": storage, "$value": value}, "Flags": flags}


def tweakdbid(value: str) -> dict[str, Any]:
    return {"$type": "TweakDBID", "$storage": "string", "$value": value}


def fixed_point(value: float) -> dict[str, Any]:
    return {"$type": "FixedPoint", "Bits": int(round(value * 131072))}


def parse_measure_point(value: str) -> MeasurePoint:
    label = value
    raw = value
    if "=" in value:
        label, raw = value.split("=", 1)
        label = label.strip() or value
    parts = [part.strip() for part in raw.replace(";", ",").split(",")]
    if len(parts) != 3:
        raise argparse.ArgumentTypeError("coordinates must be x,y,z or label=x,y,z")
    try:
        return MeasurePoint(label, Vec3(float(parts[0]), float(parts[1]), float(parts[2])))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("coordinates must contain numeric x,y,z values") from exc


def coordinate_distance(a: Vec3, b: Vec3, include_z: bool) -> float:
    dx = b.x - a.x
    dy = b.y - a.y
    dz = b.z - a.z
    if include_z:
        return math.sqrt(dx * dx + dy * dy + dz * dz)
    return math.sqrt(dx * dx + dy * dy)


def as_vec3(value: Any, label: str) -> Vec3:
    if isinstance(value, list) and len(value) >= 3:
        return Vec3(float(value[0]), float(value[1]), float(value[2]))
    if isinstance(value, dict) and all(axis in value for axis in ("x", "y", "z")):
        return Vec3(float(value["x"]), float(value["y"]), float(value["z"]))
    raise SystemExit(f"{label} must be [x, y, z] or an object with x/y/z")


def lookup_anchor(anchors: dict[str, Anchor], name: str) -> Anchor:
    if name in anchors:
        return anchors[name]
    normalized = local_ref_name(name)
    for key in (normalized, "#" + normalized):
        if key in anchors:
            return anchors[key]
    known = ", ".join(sorted(anchors))
    raise SystemExit(f"Unknown anchor '{name}'. Known anchors: {known}")


def resolve_yaw(value: Any, anchors: dict[str, Anchor], default: float) -> float:
    if value is None:
        return default
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        if value in ("origin", "anchor"):
            return default
        return lookup_anchor(anchors, value).yaw
    raise SystemExit(f"Invalid yaw value: {value!r}")


def resolve_position(value: Any, anchors: dict[str, Anchor], label: str) -> tuple[Vec3, float]:
    if value is None:
        anchor = lookup_anchor(anchors, "origin")
        return anchor.position, anchor.yaw
    if isinstance(value, list) or (isinstance(value, dict) and all(axis in value for axis in ("x", "y", "z"))):
        origin = lookup_anchor(anchors, "origin")
        return as_vec3(value, label), origin.yaw
    if not isinstance(value, dict):
        raise SystemExit(f"{label}.position must be an object, [x, y, z], or omitted")

    anchor_name = str(value.get("from", "origin"))
    anchor = lookup_anchor(anchors, anchor_name)
    yaw = resolve_yaw(value.get("yaw"), anchors, anchor.yaw)

    forward = float(value.get("forward", 0))
    right = float(value.get("right", 0))
    up = float(value.get("up", value.get("z_offset", 0)))
    if "distance" in value:
        bearing = float(value.get("bearing", 0))
        angle = math.radians(yaw + bearing)
        forward += math.cos(angle - math.radians(yaw)) * float(value["distance"])
        right += math.sin(angle - math.radians(yaw)) * float(value["distance"])

    yaw_rad = math.radians(yaw)
    right_rad = yaw_rad + math.pi / 2
    dx = math.cos(yaw_rad) * forward + math.cos(right_rad) * right
    dy = math.sin(yaw_rad) * forward + math.sin(right_rad) * right
    return anchor.position.offset(dx, dy, up), yaw


def node_data(
    node_index: int,
    ref: str | int,
    position: Vec3,
    yaw: float,
    overrides: dict[str, Any] | None = None,
) -> dict[str, Any]:
    overrides = overrides or {}
    quest_ref = node_ref(ref) if isinstance(ref, str) else node_ref_u64(ref)
    return {
        "Id": "0",
        "NodeIndex": node_index,
        "Position": vector4(position),
        "Orientation": quaternion_from_yaw(yaw),
        "Scale": {
            "$type": "Vector3",
            "X": float(overrides.get("scale_x", 1)),
            "Y": float(overrides.get("scale_y", 1)),
            "Z": float(overrides.get("scale_z", 1)),
        },
        "Pivot": vector3(position),
        "Bounds": {"$type": "Box", "Max": vector4(position), "Min": vector4(position)},
        "QuestPrefabRefHash": quest_ref,
        "UkHash1": node_ref_u64(0),
        "CookedPrefabData": resource_path("0", storage="uint64", flags="Default"),
        "MaxStreamingDistance": float(overrides.get("max_streaming_distance", 120)),
        "UkFloat1": float(overrides.get("streaming_distance", 100)),
        "Uk10": int(overrides.get("uk10", 1024)),
        "Uk11": int(overrides.get("uk11", 512)),
        "Uk12": int(overrides.get("uk12", 0)),
        "Uk13": str(overrides.get("uk13", "0")),
        "Uk14": str(overrides.get("uk14", "0")),
    }


def color() -> dict[str, Any]:
    return {"$type": "Color", "Alpha": 0, "Blue": 0, "Green": 0, "Red": 0}


def outline_points(spec: dict[str, Any]) -> tuple[list[Vec3], float]:
    height = float(spec.get("height", 2))
    if "points" in spec:
        return [as_vec3(point, "outline point") for point in spec["points"]], height

    shape = str(spec.get("type", "rectangle")).casefold()
    if shape in ("rectangle", "box", "square"):
        width = float(spec.get("width", spec.get("size", 2)))
        depth = float(spec.get("depth", spec.get("length", spec.get("size", width))))
        half_width = width / 2
        half_depth = depth / 2
        return (
            [
                Vec3(-half_width, -half_depth, 0),
                Vec3(half_width, -half_depth, 0),
                Vec3(half_width, half_depth, 0),
                Vec3(-half_width, half_depth, 0),
            ],
            height,
        )
    if shape in ("circle", "disc", "regular_polygon"):
        radius = float(spec.get("radius", 1))
        count = int(spec.get("points_count", spec.get("segments", 12)))
        if count < 3:
            raise SystemExit("circle outlines need at least 3 points")
        return (
            [
                Vec3(math.cos(2 * math.pi * index / count) * radius, math.sin(2 * math.pi * index / count) * radius, 0)
                for index in range(count)
            ],
            height,
        )
    raise SystemExit(f"Unsupported outline type: {shape}")


def outline_buffer(points: list[Vec3], height: float) -> str:
    raw = struct.pack("<I", len(points))
    for point in points:
        raw += struct.pack("<ffff", point.x, point.y, point.z, 1.0)
    raw += struct.pack("<f", height)
    return base64.b64encode(raw).decode("ascii")


def area_outline(spec: dict[str, Any], handles: HandleAllocator) -> dict[str, Any]:
    points, height = outline_points(spec)
    return {
        "HandleId": handles.take(),
        "Data": {
            "$type": "AreaShapeOutline",
            "buffer": outline_buffer(points, height),
            "height": height,
            "points": [{"$type": "Vector3", "X": point.x, "Y": point.y, "Z": point.z} for point in points],
        },
    }


def notifier(spec: Any, handles: HandleAllocator) -> dict[str, Any]:
    if isinstance(spec, dict) and "raw" in spec:
        return {"HandleId": handles.take(), "Data": spec["raw"]}
    name = spec if isinstance(spec, str) else (spec or {}).get("type", "quest")
    name = str(name).casefold()
    if name == "quest":
        data = {"$type": "questTriggerNotifier_Quest", "excludeChannels": 0, "includeChannels": "TC_Default", "isEnabled": 1}
    elif name == "interior":
        data = {
            "$type": "worldInteriorAreaNotifier",
            "excludeChannels": 0,
            "gameRestrictionIDs": [],
            "includeChannels": "TC_Player",
            "isEnabled": 1,
            "setTier2": 0,
            "treatAsInterior": 1,
        }
    elif name in ("prevention_deescalation", "prevention"):
        data = {
            "$type": "worldQuestPreventionNotifier",
            "activation": "Always",
            "excludeChannels": 0,
            "includeChannels": "TC_Player",
            "isEnabled": 1,
            "type": "Deescalation",
        }
    else:
        raise SystemExit(f"Unsupported trigger notifier: {name}")
    return {"HandleId": handles.take(), "Data": data}


def marker_node(spec: dict[str, Any], ref: str, handles: HandleAllocator) -> dict[str, Any]:
    return {
        "HandleId": handles.take(),
        "Data": {
            "$type": "worldStaticMarkerNode",
            "debugName": cname(debug_name(ref, spec.get("debug_name"))),
            "isHostOnly": 0,
            "isVisibleInGame": 1,
            "proxyScale": None,
            "sourcePrefabHash": str(spec.get("source_prefab_hash", "0")),
            "tag": spec.get("tag", "None"),
            "tagExt": spec.get("tag_ext", "None"),
        },
    }


def trigger_node(spec: dict[str, Any], ref: str, handles: HandleAllocator) -> dict[str, Any]:
    notifiers = spec.get("notifiers", ["quest"])
    if not isinstance(notifiers, list):
        notifiers = [notifiers]
    return {
        "HandleId": handles.take(),
        "Data": {
            "$type": "worldTriggerAreaNode",
            "color": color(),
            "debugName": cname(debug_name(ref, spec.get("debug_name"))),
            "isHostOnly": 0,
            "isVisibleInGame": 1,
            "notifiers": [notifier(item, handles) for item in notifiers],
            "outline": area_outline(spec.get("outline", {}), handles),
            "proxyScale": None,
            "sourcePrefabHash": str(spec.get("source_prefab_hash", "0")),
            "tag": spec.get("tag", "None"),
            "tagExt": spec.get("tag_ext", "None"),
        },
    }


def access_point_instance_data(spec: dict[str, Any], handles: HandleAllocator) -> dict[str, Any] | None:
    if not int(spec.get("instance_data", 1)):
        return None
    return {
        "HandleId": handles.take(),
        "Data": {
            "$type": "entEntityInstanceData",
            "buffer": {
                # Buffer 0 belongs to the sector's main node-data buffer.
                # Instance packages need a different file-unique buffer ID.
                "BufferId": str(spec.get("buffer_id", "1")),
                "Flags": 4063232,
                "Type": "WolvenKit.RED4.Archive.Buffer.RedPackage, WolvenKit.RED4, Version=8.17.4.0, Culture=neutral, PublicKeyToken=null",
                "Data": {
                    "Version": 4,
                    "Sections": 6,
                    "CruidIndex": 0,
                    "CruidDict": {"0": "0"},
                    "Chunks": [
                        {
                            "$type": "AccessPoint",
                            "contentScale": tweakdbid(spec.get("content_scale", "DeviceContentAssignment.Autoscaling")),
                            "controllerTypeName": cname("AccessPointController"),
                            "deviceState": spec.get("initial_state", "OFF"),
                            "displayDescription": {"unk1": "0", "value": ""},
                            "displayName": {"unk1": "0", "value": ""},
                            "networkName": spec.get("network_name", "Local Network 1"),
                            "tags": {"$type": "redTagList", "tags": []},
                        }
                    ],
                },
            },
        },
    }


def device_node(spec: dict[str, Any], ref: str, handles: HandleAllocator) -> dict[str, Any]:
    kind = str(spec.get("kind", "access_point")).lower()
    if kind != "access_point":
        raise SystemExit(f"Unsupported device kind '{kind}' for {ref}")
    return {
        "HandleId": handles.take(),
        "Data": {
            "$type": "worldDeviceNode",
            "alphaHackStreamingDistanceOverride": float(spec.get("alpha_hack_streaming_distance_override", 0)),
            "appearanceName": cname(spec.get("appearance", "access_point_access_point_socket_f_neomil")),
            "debugName": cname(debug_name(ref, spec.get("debug_name"))),
            "deviceClassName": cname(spec.get("device_class_name", "None")),
            "deviceConnections": [],
            "entityLod": int(spec.get("entity_lod", 0)),
            "entityTemplate": resource_path(
                normalize_depot_path(
                    spec.get("entity_template", r"base\gameplay\devices\masters\access_points\accesspoint.ent")
                )
            ),
            "instanceData": access_point_instance_data(spec, handles),
            "ioPriority": spec.get("io_priority", "Immediate"),
            "isHostOnly": 0,
            "isVisibleInGame": 1,
            "proxyScale": None,
            "sourcePrefabHash": str(spec.get("source_prefab_hash", "0")),
            "tag": spec.get("tag", "None"),
            "tagExt": spec.get("tag_ext", "None"),
        },
    }


def device_registry(archive_path: Path, entries: list[DeviceRegistryEntry]) -> dict[str, Any]:
    """Build the sparse device registry emitted by WolvenKit World Builder.

    ArchiveXL merges this mod-owned resource into Night City's global device
    registry. Without that merge, a worldDeviceNode can render and expose its
    interaction while quest device-manager conditions still fail to resolve
    its persistent controller reliably.
    """

    return {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": now_utc(),
            "DataType": "CR2W",
            "ArchiveFileName": str(archive_path.resolve()),
        },
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {
                "$type": "gameDeviceResource",
                "data": {
                    "Data": {
                        "$type": "gameDeviceResourceData",
                        "unk1": [
                            {
                                "$type": "gameDeviceResourceData_Cls1",
                                "children": [],
                                "className": cname(entry.controller_class),
                                "hash": str(entry.node_hash),
                                "nodePosition": vector3(entry.position),
                                "parents": [],
                            }
                            for entry in entries
                        ],
                        "version": 2,
                    }
                },
            },
            "EmbeddedFiles": [],
        },
    }


def ai_spot_node(spec: dict[str, Any], ref: str, handles: HandleAllocator) -> dict[str, Any]:
    workspot = spec.get(
        "workspot",
        r"base\workspots\common\wall\generic__stand_wall_lean_back_cigarette__smoke__01.workspot",
    )
    return {
        "HandleId": handles.take(),
        "Data": {
            "$type": "worldAISpotNode",
            "crowdBlacklist": {"$type": "redTagList", "tags": []},
            "crowdWhitelist": {"$type": "redTagList", "tags": []},
            "debugName": cname(debug_name(ref, spec.get("debug_name"))),
            "disableBumps": 0,
            "isHostOnly": 0,
            "isVisibleInGame": 1,
            "isWorkspotInfinite": int(spec.get("is_workspot_infinite", 1)),
            "isWorkspotStatic": int(spec.get("is_workspot_static", 0)),
            "lookAtTarget": node_ref_u64(0),
            "markings": [cname(marking) for marking in spec.get("markings", [])],
            "proxyScale": None,
            "sourcePrefabHash": str(spec.get("source_prefab_hash", "0")),
            "spot": {
                "HandleId": handles.take(),
                "Data": {
                    "$type": "AIActionSpot",
                    "ActorBodytypeE3": "Undefined",
                    "clippingSpaceOrientation": float(spec.get("clipping_space_orientation", 180)),
                    "clippingSpaceRange": float(spec.get("clipping_space_range", 120)),
                    "enabledWhenMasterOccupied": 0,
                    "masterNodeRef": node_ref_u64(0),
                    "resource": resource_path(workspot),
                    "snapToGround": int(spec.get("snap_to_ground", 0)),
                    "useClippingSpace": int(spec.get("use_clipping_space", 0)),
                },
            },
            "spotDef": None,
            "tag": spec.get("tag", "None"),
            "tagExt": spec.get("tag_ext", "None"),
            "useCrowdBlacklist": 1,
            "useCrowdWhitelist": 1,
        },
    }


def community_area_node(
    spec: dict[str, Any],
    source_object_id: str,
    entries: list[CommunityEntry],
    handles: HandleAllocator,
) -> dict[str, Any]:
    entries_data = []
    for entry in entries:
        entry_name = entry.spec.get("entry", "patch")
        phase = entry.spec.get("phase", "default")
        period = entry.spec.get("period", "Day")
        entries_data.append(
            {
                "$type": "communityCommunityEntrySpotsData",
                "entryName": cname(entry_name),
                "phasesData": [
                    {
                        "$type": "communityCommunityEntryPhaseSpotsData",
                        "entryPhaseName": cname(phase),
                        "timePeriodsData": [
                            {
                                "$type": "communityCommunityEntryPhaseTimePeriodData",
                                "isSequence": int(entry.spec.get("is_sequence", 0)),
                                "periodName": cname(period),
                                "spotNodeIds": [
                                    {"$type": "worldGlobalNodeID", "hash": str(spot.global_node_id)}
                                    for spot in entry.spots
                                ],
                            }
                        ],
                    }
                ],
            }
        )
    return {
        "HandleId": handles.take(),
        "Data": {
            "$type": "worldCompiledCommunityAreaNode_Streamable",
            "area": {
                "HandleId": handles.take(),
                "Data": {
                    "$type": "communityArea",
                    "entriesData": entries_data,
                },
            },
            "debugName": cname(debug_name(spec["ref"], spec.get("debug_name"))),
            "isHostOnly": 0,
            "isVisibleInGame": 1,
            "proxyScale": None,
            "sourceObjectId": {"$type": "entEntityID", "hash": str(source_object_id)},
            "sourcePrefabHash": str(spec.get("source_prefab_hash", "0")),
            "streamingDistance": float(spec.get("streaming_distance", 0)),
            "tag": spec.get("tag", "None"),
            "tagExt": spec.get("tag_ext", "None"),
        },
    }


def community_registry_node(
    spec: dict[str, Any],
    source_object_id: str,
    entries: list[CommunityEntry],
    handles: HandleAllocator,
) -> dict[str, Any]:
    registry_handle = handles.take()
    template_handle = handles.take()
    initial_states = []
    spawn_entries = []
    persistent_spots = []
    for entry in entries:
        entry_name = entry.spec.get("entry", "patch")
        phase = entry.spec.get("phase", "default")
        period = entry.spec.get("period", "Day")
        appearances = entry.spec.get("appearances", [entry.spec.get("appearance", "default")])
        if not isinstance(appearances, list):
            appearances = [appearances]
        initial_states.append(
            {
                "$type": "worldCommunityEntryInitialState",
                "entryActiveOnStart": int(entry.spec.get("active_on_start", 1)),
                "entryName": cname(entry_name),
                "initialPhaseName": cname(phase),
            }
        )
        spawn_entries.append(
            {
                "HandleId": handles.take(),
                "Data": {
                    "$type": "communitySpawnEntry",
                    "characterRecordId": tweakdbid(entry.spec.get("character", "Character.GhostlinePatch")),
                    "entryName": cname(entry_name),
                    "initializers": [],
                    "phases": [
                        {
                            "HandleId": handles.take(),
                            "Data": {
                                "$type": "communitySpawnPhase",
                                "alwaysSpawned": entry.spec.get("always_spawned", "default__false_"),
                                "appearances": [cname(value) for value in appearances],
                                "phaseName": cname(phase),
                                "prefetchAppearance": int(entry.spec.get("prefetch_appearance", 0)),
                                "timePeriods": [
                                    {
                                        "$type": "communityPhaseTimePeriod",
                                        "categories": [],
                                        "hour": period,
                                        "isSequence": int(entry.spec.get("is_sequence", 0)),
                                        "markings": [],
                                        "quantity": int(entry.spec.get("quantity", len(entry.spots))),
                                        "spotNodeRefs": [node_ref(spot.full_ref) for spot in entry.spots],
                                    }
                                ],
                            },
                        }
                    ],
                    "spawnInView": entry.spec.get("spawn_in_view", "default__true_"),
                },
            }
        )
        for spot in entry.spots:
            persistent_spots.append(
                {
                    "$type": "AISpotPersistentData",
                    "globalNodeId": {"$type": "worldGlobalNodeID", "hash": str(spot.global_node_id)},
                    "isEnabled": 1,
                    "worldPosition": {
                        "$type": "WorldPosition",
                        "x": fixed_point(spot.position.x),
                        "y": fixed_point(spot.position.y),
                        "z": fixed_point(spot.position.z),
                    },
                    "yaw": spot.yaw,
                }
            )
    return {
        "HandleId": registry_handle,
        "Data": {
            "$type": "worldCommunityRegistryNode",
            "communitiesData": [
                {
                    "$type": "worldCommunityRegistryItem",
                    "communityAreaType": spec.get("community_area_type", "Regular"),
                    "communityId": {"$type": "gameCommunityID", "entityId": {"$type": "entEntityID", "hash": str(source_object_id)}},
                    "entriesInitialState": initial_states,
                    "template": {
                        "HandleId": template_handle,
                        "Data": {
                            "$type": "communityCommunityTemplateData",
                            "crowdEntries": [],
                            "entries": spawn_entries,
                            "spawnSetReference": cname(spec.get("spawn_set_reference", "None")),
                        },
                    },
                }
            ],
            "crowdCreationRegistry": None,
            "debugName": cname(spec.get("registry_debug_name", "registry")),
            "isHostOnly": 0,
            "isVisibleInGame": 1,
            "proxyScale": None,
            "representsCrowd": 0,
            "sourcePrefabHash": str(spec.get("registry_source_prefab_hash", "0")),
            "spawnSetNameToCommunityID": {"$type": "gameCommunitySpawnSetNameToID", "entries": []},
            "tag": "None",
            "tagExt": "None",
            "workspotsPersistentData": persistent_spots,
        },
    }


def streaming_sector(category: str, level: int, archive_path: Path, node_datas: list[dict[str, Any]], refs: list[str], nodes: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": now_utc(),
            "DataType": "CR2W",
            "ArchiveFileName": str(archive_path.resolve()),
        },
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {
                "$type": "worldStreamingSector",
                "category": category,
                "cookingPlatform": "PLATFORM_None",
                "externInplaceResource": resource_path("0", storage="uint64"),
                "level": level,
                "localInplaceResource": [],
                "nodeData": {
                    "BufferId": "0",
                    "Flags": 0,
                    "Type": "WolvenKit.RED4.Archive.Buffer.worldNodeDataBuffer, WolvenKit.RED4, Version=8.17.4.0, Culture=neutral, PublicKeyToken=null",
                    "Data": node_datas,
                },
                "nodeRefs": [node_ref(ref) for ref in refs],
                "nodes": nodes,
                "persistentNodeIndex": 0,
                "persistentNodes": [],
                "variantIndices": [0],
                "variantNodes": [],
                "version": 62,
            },
            "EmbeddedFiles": [],
        },
    }


def descriptor(
    category: str,
    depot_path: str,
    level: int,
    quest_prefab_ref: str | None,
    bounds_min: Vec3,
    bounds_max: Vec3,
) -> dict[str, Any]:
    return {
        "$type": "worldStreamingSectorDescriptor",
        "blockIndex": {"$type": "worldStreamingBlockIndex", "oup": "Base", "rldGridCell": 0},
        "category": category,
        "data": resource_path(depot_path),
        "level": level,
        "numNodeRanges": 1,
        "questPrefabNodeRef": node_ref(quest_prefab_ref) if quest_prefab_ref else node_ref_u64(0),
        "streamingBox": {"$type": "Box", "Max": vector4(bounds_max, WORLD_FLOAT), "Min": vector4(bounds_min, -WORLD_FLOAT)},
        "variants": [],
    }


def block_bounds(spec: dict[str, Any], positions: list[Vec3]) -> tuple[Vec3, Vec3]:
    box = spec.get("streaming_box", "world")
    if box == "world":
        return Vec3(-WORLD_FLOAT, -WORLD_FLOAT, -WORLD_FLOAT), Vec3(WORLD_FLOAT, WORLD_FLOAT, WORLD_FLOAT)
    if isinstance(box, dict) and "min" in box and "max" in box:
        return as_vec3(box["min"], "streaming_box.min"), as_vec3(box["max"], "streaming_box.max")
    if isinstance(box, dict):
        padding = float(box.get("padding", 300))
        return (
            Vec3(min(p.x for p in positions) - padding, min(p.y for p in positions) - padding, min(p.z for p in positions) - padding),
            Vec3(max(p.x for p in positions) + padding, max(p.y for p in positions) + padding, max(p.z for p in positions) + padding),
        )
    raise SystemExit("streaming_box must be 'world' or an object")


def streaming_block(
    archive_path: Path,
    quest_sector_path: str,
    prefab_root: str,
    quest_bounds: tuple[Vec3, Vec3],
    always_loaded_path: str | None,
) -> dict[str, Any]:
    descriptors = [
        descriptor("Quest", quest_sector_path, 0, prefab_root, quest_bounds[0], quest_bounds[1]),
    ]
    if always_loaded_path:
        descriptors.append(
            descriptor(
                "AlwaysLoaded",
                always_loaded_path,
                1,
                None,
                Vec3(-99999, -99999, -99999),
                Vec3(99999, 99999, 99999),
            )
        )
    return {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": now_utc(),
            "DataType": "CR2W",
            "ArchiveFileName": str(archive_path.resolve()),
        },
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {
                "$type": "worldStreamingBlock",
                "cookingPlatform": "PLATFORM_PC",
                "descriptors": descriptors,
                "index": {"$type": "worldStreamingBlockIndex", "oup": "Base", "rldGridCell": 0},
            },
            "EmbeddedFiles": [],
        },
    }


def write_json(path: Path, data: dict[str, Any], dry_run: bool) -> None:
    if dry_run:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def build_world(spec: dict[str, Any], raw_root: Path, archive_root: Path, dry_run: bool = False) -> list[GeneratedFile]:
    prefab_root = str(spec["prefab_root"])
    quest_sector_path = normalize_depot_path(spec.get("quest_sector_path", rf"mod\{spec.get('name', 'ghostline')}\world\quest.streamingsector"))
    block_path = normalize_depot_path(spec.get("block_path", rf"mod\{spec.get('name', 'ghostline')}\world\all.streamingblock"))
    community_specs: list[dict[str, Any]] = []
    if spec.get("community"):
        community_specs.append(spec["community"])
    extra_communities = spec.get("communities", [])
    if not isinstance(extra_communities, list):
        raise SystemExit("communities must be a list")
    community_specs.extend(extra_communities)
    marker_specs = spec.get("markers", [])
    device_specs = spec.get("devices", [])
    if not isinstance(device_specs, list):
        raise SystemExit("devices must be a list")
    device_registry_path = None
    if device_specs:
        device_registry_path = normalize_depot_path(
            spec.get(
                "device_registry_path",
                rf"mod\{spec.get('name', 'ghostline')}\world\custom_devices.devices",
            )
        )
    device_buffer_ids: set[int] = set()
    for device_index, device_spec in enumerate(device_specs):
        if not isinstance(device_spec, dict):
            raise SystemExit(f"devices[{device_index}] must be an object")
        if not int(device_spec.get("instance_data", 1)):
            continue
        try:
            buffer_id = int(device_spec.get("buffer_id", 1))
        except (TypeError, ValueError) as exc:
            raise SystemExit(f"devices[{device_index}].buffer_id must be a positive integer") from exc
        if buffer_id <= 0:
            raise SystemExit(f"devices[{device_index}].buffer_id must not reuse sector buffer 0")
        if buffer_id in device_buffer_ids:
            raise SystemExit(f"devices[{device_index}].buffer_id must be unique within the sector")
        device_buffer_ids.add(buffer_id)
    always_loaded_ref_specs = spec.get("always_loaded_node_refs", [])
    if always_loaded_ref_specs and not isinstance(always_loaded_ref_specs, list):
        raise SystemExit("always_loaded_node_refs must be a list")
    always_loaded_marker_specs = [item for item in marker_specs if item.get("sector") == "always_loaded"]
    always_loaded_path = None
    if community_specs or always_loaded_ref_specs or always_loaded_marker_specs:
        always_loaded_path = normalize_depot_path(
            spec.get("always_loaded_sector_path", rf"mod\{spec.get('name', 'ghostline')}\world\always_loaded.streamingsector")
        )

    origin_data = spec.get("origin")
    if not origin_data:
        raise SystemExit("Spec requires an origin with x/y/z and optional yaw")
    origin = as_vec3(origin_data, "origin")
    origin_yaw = float(origin_data.get("yaw", spec.get("yaw", 0))) if isinstance(origin_data, dict) else float(spec.get("yaw", 0))
    anchors: dict[str, Anchor] = {"origin": Anchor(origin, origin_yaw)}

    handles = HandleAllocator()
    always_handles = HandleAllocator()
    nodes: list[dict[str, Any]] = []
    node_datas: list[dict[str, Any]] = []
    refs: list[str] = []
    positions: list[Vec3] = [origin]
    always_loaded_nodes: list[dict[str, Any]] = []
    always_loaded_node_datas: list[dict[str, Any]] = []
    always_loaded_refs: list[str] = []
    always_loaded_sector: dict[str, Any] | None = None
    registry_node_ids: list[int] = []
    device_registry_entries: list[DeviceRegistryEntry] = []

    def add_node(ref_value: str, node: dict[str, Any], pos: Vec3, yaw: float, overrides: dict[str, Any] | None = None) -> None:
        full_ref = full_node_ref(prefab_root, ref_value)
        index = len(nodes)
        nodes.append(node)
        node_datas.append(node_data(index, full_ref, pos, yaw, overrides))
        refs.append(full_ref)
        positions.append(pos)
        register_anchor(anchors, ref_value, Anchor(pos, yaw, index))
        register_anchor(anchors, full_ref, Anchor(pos, yaw, index))

    def add_always_loaded_node(
        ref_value: str,
        node: dict[str, Any],
        pos: Vec3,
        yaw: float,
        overrides: dict[str, Any] | None = None,
    ) -> None:
        full_ref = full_node_ref(prefab_root, ref_value)
        index = len(always_loaded_nodes)
        always_loaded_nodes.append(node)
        always_loaded_node_datas.append(node_data(index, full_ref, pos, yaw, overrides))
        always_loaded_refs.append(full_ref)
        positions.append(pos)
        register_anchor(anchors, ref_value, Anchor(pos, yaw, index))
        register_anchor(anchors, full_ref, Anchor(pos, yaw, index))

    for item in marker_specs:
        ref_value = item["ref"]
        pos, anchor_yaw = resolve_position(item.get("position"), anchors, f"marker {ref_value}")
        yaw = resolve_yaw(item.get("yaw"), anchors, anchor_yaw)
        if item.get("sector") == "always_loaded":
            add_always_loaded_node(ref_value, marker_node(item, ref_value, always_handles), pos, yaw, item.get("node_data"))
        else:
            add_node(ref_value, marker_node(item, ref_value, handles), pos, yaw, item.get("node_data"))

    for item in spec.get("triggers", []):
        ref_value = item["ref"]
        pos, anchor_yaw = resolve_position(item.get("position"), anchors, f"trigger {ref_value}")
        yaw = resolve_yaw(item.get("yaw"), anchors, anchor_yaw)
        add_node(ref_value, trigger_node(item, ref_value, handles), pos, yaw, item.get("node_data"))

    for item in device_specs:
        ref_value = item["ref"]
        pos, anchor_yaw = resolve_position(item.get("position"), anchors, f"device {ref_value}")
        yaw = resolve_yaw(item.get("yaw"), anchors, anchor_yaw)
        add_node(ref_value, device_node(item, ref_value, handles), pos, yaw, item.get("node_data"))
        full_ref = full_node_ref(prefab_root, ref_value)
        device_registry_entries.append(
            DeviceRegistryEntry(
                node_ref=full_ref,
                node_hash=node_ref_hash(full_ref),
                controller_class=str(item.get("controller_class", "AccessPointControllerPS")),
                position=pos,
            )
        )

    for community_index, community_spec in enumerate(community_specs):
        if not isinstance(community_spec, dict):
            raise SystemExit(f"communities[{community_index}] must be an object")
        area_ref = community_spec["ref"]
        source_object_id = str(community_spec.get("source_object_id", "auto"))
        if source_object_id == "auto":
            source_object_id = str(node_ref_hash(full_node_ref(prefab_root, area_ref)))

        raw_entries = community_spec.get("entries")
        if raw_entries is None:
            raw_entries = [community_spec]
        if not isinstance(raw_entries, list) or not raw_entries:
            raise SystemExit(f"community {area_ref} entries must be a non-empty list")

        resolved_entries: list[CommunityEntry] = []
        for entry_index, raw_entry in enumerate(raw_entries):
            if not isinstance(raw_entry, dict):
                raise SystemExit(f"community {area_ref} entries[{entry_index}] must be an object")
            entry_spec = dict(community_spec)
            entry_spec.pop("entries", None)
            entry_spec.update(raw_entry)
            entry_name = str(entry_spec.get("entry", f"entry_{entry_index + 1}"))

            raw_spots = raw_entry.get("spots")
            if raw_spots is None:
                raw_spots = entry_spec.get("spots")
            if raw_spots is None:
                raw_spots = [raw_entry.get("spot", community_spec.get("spot", {}))]
            if not isinstance(raw_spots, list) or not raw_spots:
                raise SystemExit(f"community {area_ref} entry {entry_name} spots must be a non-empty list")

            resolved_spots: list[CommunitySpot] = []
            inherited_spot = community_spec.get("spot", {})
            for spot_index, raw_spot in enumerate(raw_spots):
                if not isinstance(raw_spot, dict):
                    raise SystemExit(f"community {area_ref} entry {entry_name} spot {spot_index} must be an object")
                spot_spec = dict(inherited_spot)
                spot_spec.update(raw_spot)
                default_spot_ref = (
                    "#gq000_01_spot_patch_bridge"
                    if len(community_specs) == 1 and len(raw_entries) == 1 and len(raw_spots) == 1
                    else f"#{local_ref_name(area_ref)}_{entry_name}_spot_{spot_index + 1}"
                )
                spot_ref_value = str(spot_spec.get("ref", default_spot_ref))
                spot_ref = full_node_ref(prefab_root, spot_ref_value)
                spot_position, spot_anchor_yaw = resolve_position(
                    spot_spec.get("position"), anchors, f"community spot {spot_ref_value}"
                )
                spot_yaw = resolve_yaw(spot_spec.get("yaw"), anchors, spot_anchor_yaw)
                spot_hash = int(spot_spec.get("global_node_id", node_ref_hash(spot_ref)))
                if not 0 < spot_hash <= UINT64_MASK:
                    raise SystemExit(f"community spot {spot_ref_value} global_node_id must be an unsigned 64-bit integer")
                add_node(
                    spot_ref_value,
                    ai_spot_node(spot_spec, spot_ref_value, handles),
                    spot_position,
                    spot_yaw,
                    spot_spec.get("node_data"),
                )
                resolved_spots.append(
                    CommunitySpot(spot_spec, spot_ref_value, spot_ref, spot_hash, spot_position, spot_yaw)
                )
            resolved_entries.append(CommunityEntry(entry_spec, tuple(resolved_spots)))

        registry_node_id_value = community_spec.get("registry_node_id", "auto")
        if registry_node_id_value == "auto":
            registry_seed_ref = full_node_ref(prefab_root, area_ref) + "_registry"
            registry_node_id = node_ref_hash(registry_seed_ref)
        else:
            try:
                registry_node_id = int(registry_node_id_value)
            except (TypeError, ValueError) as exc:
                raise SystemExit("community.registry_node_id must be 'auto' or an unsigned 64-bit integer") from exc
        if not 0 < registry_node_id <= UINT64_MASK:
            raise SystemExit("community.registry_node_id must be between 1 and 18446744073709551615")
        if registry_node_id == int(source_object_id):
            raise SystemExit("community.registry_node_id must differ from community.source_object_id")
        if any(registry_node_id == spot.global_node_id for entry in resolved_entries for spot in entry.spots):
            raise SystemExit("community.registry_node_id must differ from community.spot.global_node_id")
        if registry_node_id in registry_node_ids:
            raise SystemExit("community.registry_node_id values must be unique")
        registry_node_ids.append(registry_node_id)

        area_position, area_anchor_yaw = resolve_position(community_spec.get("position"), anchors, f"community {area_ref}")
        area_yaw = resolve_yaw(community_spec.get("yaw"), anchors, area_anchor_yaw)
        add_node(
            area_ref,
            community_area_node(community_spec, source_object_id, resolved_entries, handles),
            area_position,
            area_yaw,
            community_spec.get("node_data"),
        )

        registry_node = community_registry_node(
            community_spec,
            source_object_id,
            resolved_entries,
            always_handles,
        )
        registry_index = len(always_loaded_nodes)
        always_loaded_nodes.append(registry_node)
        always_loaded_node_datas.append(
            node_data(registry_index, registry_node_id, Vec3(0, 0, 0), 0, {"max_streaming_distance": 17.320507, "streaming_distance": 100000000, "uk10": 32})
        )

    for ref_spec in always_loaded_ref_specs:
        if isinstance(ref_spec, str):
            ref_value = ref_spec
            ref_data: dict[str, Any] = {}
        elif isinstance(ref_spec, dict):
            ref_value = str(ref_spec["ref"])
            ref_data = ref_spec
        else:
            raise SystemExit("always_loaded_node_refs entries must be strings or objects")

        full_ref = full_node_ref(prefab_root, ref_value)
        position_spec = ref_data.get("position")
        if position_spec is None:
            anchor = lookup_anchor(anchors, full_ref)
            pos = anchor.position
            yaw = resolve_yaw(ref_data.get("yaw"), anchors, anchor.yaw)
            source_node_index = anchor.node_index
        else:
            pos, anchor_yaw = resolve_position(position_spec, anchors, f"always-loaded ref {ref_value}")
            yaw = resolve_yaw(ref_data.get("yaw"), anchors, anchor_yaw)
            source_node_index = None

        overrides = {
            "max_streaming_distance": 9513.75586,
            "streaming_distance": 512,
            "uk10": 32,
        }
        overrides.update(ref_data.get("node_data", {}))
        node_index = int(ref_data.get("node_index", source_node_index if source_node_index is not None else len(always_loaded_node_datas)))
        always_loaded_node_datas.append(node_data(node_index, full_ref, pos, yaw, overrides))
        always_loaded_refs.append(full_ref)

    if registry_node_ids:
        emitted_ref_hashes = {node_ref_hash(ref): ref for ref in [*refs, *always_loaded_refs]}
        for registry_node_id in registry_node_ids:
            colliding_ref = emitted_ref_hashes.get(registry_node_id)
            if colliding_ref is not None:
                raise SystemExit(
                    "community.registry_node_id must differ from emitted world node refs; "
                    f"it collides with {colliding_ref}"
                )

    if always_loaded_path and (always_loaded_node_datas or always_loaded_nodes):
        registry_archive = depot_to_archive_path(archive_root, always_loaded_path)
        always_loaded_sector = streaming_sector(
            "AlwaysLoaded",
            int(spec.get("always_loaded_level", 1)),
            registry_archive,
            always_loaded_node_datas,
            always_loaded_refs,
            always_loaded_nodes,
        )

    quest_archive = depot_to_archive_path(archive_root, quest_sector_path)
    quest_sector = streaming_sector(
        "Quest",
        int(spec.get("quest_sector_level", 255)),
        quest_archive,
        node_datas,
        refs,
        nodes,
    )

    block_archive = depot_to_archive_path(archive_root, block_path)
    block = streaming_block(
        block_archive,
        quest_sector_path,
        prefab_root,
        block_bounds(spec, positions),
        always_loaded_path,
    )

    generated: list[GeneratedFile] = []
    quest_raw = depot_to_raw_path(raw_root, quest_sector_path)
    block_raw = depot_to_raw_path(raw_root, block_path)
    write_json(quest_raw, quest_sector, dry_run)
    generated.append(GeneratedFile("quest_sector", quest_sector_path, quest_raw, quest_archive))
    if always_loaded_sector and always_loaded_path:
        always_raw = depot_to_raw_path(raw_root, always_loaded_path)
        always_archive = depot_to_archive_path(archive_root, always_loaded_path)
        write_json(always_raw, always_loaded_sector, dry_run)
        generated.append(GeneratedFile("always_loaded_sector", always_loaded_path, always_raw, always_archive))
    if device_registry_path:
        device_registry_raw = depot_to_raw_path(raw_root, device_registry_path)
        device_registry_archive = depot_to_archive_path(archive_root, device_registry_path)
        write_json(
            device_registry_raw,
            device_registry(device_registry_archive, device_registry_entries),
            dry_run,
        )
        generated.append(
            GeneratedFile(
                "device_registry",
                device_registry_path,
                device_registry_raw,
                device_registry_archive,
            )
        )
    write_json(block_raw, block, dry_run)
    generated.append(GeneratedFile("streaming_block", block_path, block_raw, block_archive))
    return generated


def register_archive_xl(
    archive_xl: Path,
    block_path: str,
    dry_run: bool,
    device_registry_path: str | None = None,
) -> None:
    try:
        import yaml
    except ImportError as exc:
        raise SystemExit("PyYAML is required for --register") from exc

    data: dict[str, Any]
    if archive_xl.exists():
        data = yaml.safe_load(archive_xl.read_text(encoding="utf-8")) or {}
    else:
        data = {}
    if not isinstance(data, dict):
        raise SystemExit(f"ArchiveXL file is not a YAML object: {archive_xl}")
    streaming = data.setdefault("streaming", {})
    if not isinstance(streaming, dict):
        raise SystemExit("ArchiveXL 'streaming' entry exists but is not a mapping")
    blocks = streaming.setdefault("blocks", [])
    if not isinstance(blocks, list):
        raise SystemExit("ArchiveXL 'streaming.blocks' entry exists but is not a list")
    if block_path not in blocks:
        blocks.append(block_path)
    if device_registry_path:
        resource = data.setdefault("resource", {})
        if not isinstance(resource, dict):
            raise SystemExit("ArchiveXL 'resource' entry exists but is not a mapping")
        patches = resource.setdefault("patch", {})
        if not isinstance(patches, dict):
            raise SystemExit("ArchiveXL 'resource.patch' entry exists but is not a mapping")
        targets = patches.setdefault(device_registry_path, [])
        if not isinstance(targets, list):
            raise SystemExit(f"ArchiveXL resource patch entry for {device_registry_path} is not a list")
        global_devices = r"base\worlds\03_night_city\_compiled\default\03_night_city.devices"
        if global_devices not in targets:
            targets.append(global_devices)
    if dry_run:
        return
    archive_xl.parent.mkdir(parents=True, exist_ok=True)
    archive_xl.write_text(yaml.safe_dump(data, sort_keys=False, width=120), encoding="utf-8")


def deserialize(generated: list[GeneratedFile], wolvenkit: Path) -> None:
    if not wolvenkit.exists():
        raise SystemExit(f"WolvenKit CLI not found: {wolvenkit}")
    for item in generated:
        item.archive_path.parent.mkdir(parents=True, exist_ok=True)
        command = [
            str(wolvenkit),
            "convert",
            "deserialize",
            str(item.raw_path),
            "-o",
            str(item.archive_path.parent),
            "-v",
            "Minimal",
        ]
        result = subprocess.run(command, text=True)
        if result.returncode != 0:
            raise SystemExit(f"WolvenKit deserialize failed for {item.raw_path}")


def command_generate(args: argparse.Namespace) -> None:
    spec = load_json(args.spec)
    generated = build_world(spec, args.raw_root, args.archive_root, dry_run=args.dry_run)
    if args.register:
        block = next(item for item in generated if item.kind == "streaming_block")
        registry = next((item for item in generated if item.kind == "device_registry"), None)
        register_archive_xl(
            args.archive_xl,
            block.depot_path,
            args.dry_run,
            registry.depot_path if registry else None,
        )
    if args.deserialize and not args.dry_run:
        deserialize(generated, args.wolvenkit)
    rows = [
        {
            "kind": item.kind,
            "depot_path": item.depot_path,
            "raw_path": str(item.raw_path),
            "archive_path": str(item.archive_path),
        }
        for item in generated
    ]
    if args.json:
        print_json(rows)
    else:
        print_table(rows, [("kind", "Kind"), ("depot_path", "Depot Path"), ("raw_path", "Raw JSON"), ("archive_path", "Archive Target")])
        if args.dry_run:
            print()
            print("Dry run only; no files were written.")


def command_hash(args: argparse.Namespace) -> None:
    rows = [{"node_ref": value, "red_hash": str(node_ref_hash(value))} for value in args.node_refs]
    if args.json:
        print_json(rows)
    else:
        print_table(rows, [("node_ref", "NodeRef"), ("red_hash", "RED Hash")])


def command_measure(args: argparse.Namespace) -> None:
    if len(args.points) < 2:
        raise SystemExit("measure needs at least two coordinate points")
    origin = args.points[0]
    rows = []
    for target in args.points[1:]:
        dx = target.position.x - origin.position.x
        dy = target.position.y - origin.position.y
        dz = target.position.z - origin.position.z
        rows.append(
            {
                "from": origin.label,
                "to": target.label,
                "dx": dx,
                "dy": dy,
                "dz": dz,
                "xy_distance": coordinate_distance(origin.position, target.position, False),
                "xyz_distance": coordinate_distance(origin.position, target.position, True),
            }
        )
    if args.json:
        print_json(rows)
    else:
        display_rows = []
        for row in rows:
            display_rows.append(
                {
                    **row,
                    "dx": f"{row['dx']:.3f}",
                    "dy": f"{row['dy']:.3f}",
                    "dz": f"{row['dz']:.3f}",
                    "xy_distance": f"{row['xy_distance']:.3f}",
                    "xyz_distance": f"{row['xyz_distance']:.3f}",
                }
            )
        print_table(
            display_rows,
            [
                ("from", "From"),
                ("to", "To"),
                ("dx", "dX"),
                ("dy", "dY"),
                ("dz", "dZ"),
                ("xy_distance", "XY Distance"),
                ("xyz_distance", "XYZ Distance"),
            ],
        )


def command_example(args: argparse.Namespace) -> None:
    path = Path("tools/gq000_world_spec.example.json")
    print(path.read_text(encoding="utf-8"))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate Ghostline world streaming CR2W-JSON from coordinate specs.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate = subparsers.add_parser("generate", help="Generate raw .streamingsector.json and .streamingblock.json files.")
    generate.add_argument("--spec", type=Path, required=True, help="World generation spec JSON.")
    generate.add_argument("--raw-root", type=Path, default=DEFAULT_RAW_ROOT, help=f"Raw output root. Default: {DEFAULT_RAW_ROOT}")
    generate.add_argument("--archive-root", type=Path, default=DEFAULT_ARCHIVE_ROOT, help=f"Archive target root. Default: {DEFAULT_ARCHIVE_ROOT}")
    generate.add_argument("--register", action="store_true", help="Add the generated streaming block to Ghostline.archive.xl.")
    generate.add_argument("--archive-xl", type=Path, default=DEFAULT_ARCHIVE_XL, help=f"ArchiveXL YAML path. Default: {DEFAULT_ARCHIVE_XL}")
    generate.add_argument("--deserialize", action="store_true", help="Run WolvenKit CLI to convert generated raw JSON into CR2W binaries.")
    generate.add_argument("--wolvenkit", type=Path, default=DEFAULT_WOLVENKIT, help=f"WolvenKit CLI path. Default: {DEFAULT_WOLVENKIT}")
    generate.add_argument("--dry-run", action="store_true", help="Print planned outputs without writing files.")
    generate.add_argument("--json", action="store_true", help="Emit machine-readable JSON summary.")
    generate.set_defaults(func=command_generate)

    hash_parser = subparsers.add_parser("hash", help="Compute RED4 NodeRef.GetRedHash-compatible values.")
    hash_parser.add_argument("node_refs", nargs="+", help="Absolute NodeRefs to hash.")
    hash_parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON summary.")
    hash_parser.set_defaults(func=command_hash)

    measure = subparsers.add_parser(
        "measure",
        help="Measure horizontal and 3D distances between captured x,y,z coordinates.",
    )
    measure.add_argument(
        "points",
        nargs="+",
        type=parse_measure_point,
        help="Coordinates as x,y,z or label=x,y,z. Use -- before negative values.",
    )
    measure.add_argument("--json", action="store_true", help="Emit machine-readable JSON summary.")
    measure.set_defaults(func=command_measure)

    example = subparsers.add_parser("example", help="Print the checked-in gq000 world spec example.")
    example.set_defaults(func=command_example)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
