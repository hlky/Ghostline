#!/usr/bin/env python3
"""Assemble and render world-location tiles without Blender.

The assembler consumes the selected-appearance PBR GLBs produced by the same
``ghostline-red mesh-export-batch --pbr`` path used by the item database.  It
stores an instanced tile manifest; Godot then loads those standard GLBs and
renders the requested viewpoints directly.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import shutil
import struct
import subprocess
import sys
import time
import urllib.parse
from collections import defaultdict
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "converted/world-location-database"
DEFAULT_JOBS = DEFAULT_OUTPUT / "six-tile-render-jobs.json"
DEFAULT_GODOT = (
    DEFAULT_OUTPUT
    / "renderer/godot/Godot_v4.7.1-stable_win64_console.exe"
)
GODOT_PROJECT = ROOT / "tools/world_location_renderer"
CATALOG_TEXTURE_MAX_DIMENSION = 512
CATALOG_TEXTURE_VERSION = "tex512-v2"
TERRAIN_GLTF_VERSION = "tex512-v3-terrain-uv"
VIEWPOINT_CHUNK_RADIUS = 50.0

STATIC_MESH_NODE_TYPES = {
    "worldAdvertisingNode",
    "worldAdvertisementNode",
    "worldBakedDestructionNode",
    "worldBuildingProxyMeshNode",
    "worldClothMeshNode",
    "worldDecorationMeshNode",
    "worldDestructibleProxyMeshNode",
    "worldDestructibleEntityProxyMeshNode",
    "worldDynamicMeshNode",
    "worldEntityProxyMeshNode",
    "worldGenericProxyMeshNode",
    "worldMeshNode",
    "worldPhysicalDestructionNode",
    "worldRotatingMeshNode",
    "worldRoadProxyMeshNode",
    "worldStaticMeshNode",
    "worldStaticOccluderMeshNode",
    "worldTerrainMeshNode",
    "worldTerrainProxyMeshNode",
}

COARSE_LOD_NODE_TYPES = {
    "worldBuildingProxyMeshNode",
    "worldGenericProxyMeshNode",
    "worldRoadProxyMeshNode",
    "worldTerrainMeshNode",
    "worldTerrainProxyMeshNode",
}

ALTERNATE_DESTRUCTION_NODE_TYPES: set[str] = set()


class DirectRenderError(RuntimeError):
    pass


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise DirectRenderError(f"Could not read JSON {path}: {exc}") from exc


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        temporary.write_text(
            json.dumps(value, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def current_renderer_fingerprint() -> str:
    return hashlib.sha256(
        Path(__file__).read_bytes()
        + (GODOT_PROJECT / "render.gd").read_bytes()
        + (GODOT_PROJECT / "project.godot").read_bytes()
    ).hexdigest()


def wrapped_value(value: Any, default: Any = None) -> Any:
    if isinstance(value, Mapping) and "$value" in value:
        return value["$value"]
    return default if value is None else value


def resource_path(data: Mapping[str, Any]) -> str:
    for key in ("mesh", "meshRef"):
        reference = data.get(key)
        if not isinstance(reference, Mapping):
            continue
        depot = reference.get("DepotPath")
        value = wrapped_value(depot, "")
        if value and str(value) != "0":
            return str(value).replace("/", "\\").casefold()
    return ""


def mesh_appearance(data: Mapping[str, Any]) -> str:
    value = wrapped_value(
        data.get("meshAppearance", data.get("appearanceName")), "default"
    )
    return str(value or "default")


def vector(value: Any, keys: Sequence[str], default: Sequence[float]) -> list[float]:
    if not isinstance(value, Mapping):
        return [float(item) for item in default]
    properties = value.get("Properties")
    source = properties if isinstance(properties, Mapping) else value
    return [float(wrapped_value(source.get(key), fallback)) for key, fallback in zip(keys, default)]


def position(value: Mapping[str, Any]) -> list[float]:
    for key in ("Position", "position", "translation", "Translation"):
        raw = value.get(key)
        if not isinstance(raw, Mapping):
            continue
        if raw.get("$type") == "WorldPosition":
            return [
                float(wrapped_value(raw.get(axis, {}).get("Bits"), 0.0)) / 131072.0
                if isinstance(raw.get(axis), Mapping)
                else 0.0
                for axis in ("x", "y", "z")
            ]
        return vector(raw, ("X", "Y", "Z"), (0.0, 0.0, 0.0))
    return [0.0, 0.0, 0.0]


def rotation(value: Mapping[str, Any]) -> list[float]:
    for key in ("Orientation", "orientation", "Rotation", "rotation"):
        raw = value.get(key)
        if not isinstance(raw, Mapping):
            continue
        properties = raw.get("Properties")
        source = properties if isinstance(properties, Mapping) else raw
        if "r" in source:
            return [
                float(wrapped_value(source.get("i"), 0.0)),
                float(wrapped_value(source.get("j"), 0.0)),
                float(wrapped_value(source.get("k"), 0.0)),
                float(wrapped_value(source.get("r"), 1.0)),
            ]
        if "W" in source:
            return [
                float(wrapped_value(source.get("X"), 0.0)),
                float(wrapped_value(source.get("Y"), 0.0)),
                float(wrapped_value(source.get("Z"), 0.0)),
                float(wrapped_value(source.get("W"), 1.0)),
            ]
    return [0.0, 0.0, 0.0, 1.0]


def scale(value: Mapping[str, Any]) -> list[float]:
    for key in ("Scale", "scale"):
        raw = value.get(key)
        if isinstance(raw, Mapping):
            return vector(raw, ("X", "Y", "Z"), (1.0, 1.0, 1.0))
    return [1.0, 1.0, 1.0]


def identity() -> list[list[float]]:
    return [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]


def matrix_multiply(left: Sequence[Sequence[float]], right: Sequence[Sequence[float]]) -> list[list[float]]:
    return [
        [sum(float(left[row][inner]) * float(right[inner][column]) for inner in range(4)) for column in range(4)]
        for row in range(4)
    ]


def trs_matrix(
    translation: Sequence[float],
    quaternion: Sequence[float],
    dimensions: Sequence[float],
) -> list[list[float]]:
    x, y, z, w = (float(item) for item in quaternion)
    length = math.sqrt(x * x + y * y + z * z + w * w)
    if length > 0.0:
        x, y, z, w = x / length, y / length, z / length, w / length
    sx, sy, sz = (float(item) for item in dimensions)
    result = [
        [(1.0 - 2.0 * (y * y + z * z)) * sx, (2.0 * (x * y - z * w)) * sy, (2.0 * (x * z + y * w)) * sz, float(translation[0])],
        [(2.0 * (x * y + z * w)) * sx, (1.0 - 2.0 * (x * x + z * z)) * sy, (2.0 * (y * z - x * w)) * sz, float(translation[1])],
        [(2.0 * (x * z - y * w)) * sx, (2.0 * (y * z + x * w)) * sy, (1.0 - 2.0 * (x * x + y * y)) * sz, float(translation[2])],
        [0.0, 0.0, 0.0, 1.0],
    ]
    return result


def instance_matrix(value: Mapping[str, Any]) -> list[list[float]]:
    return trs_matrix(position(value), rotation(value), scale(value))


def gltf_node_matrix(node: Mapping[str, Any]) -> list[list[float]]:
    raw_matrix = node.get("matrix")
    if isinstance(raw_matrix, Sequence) and not isinstance(raw_matrix, (str, bytes)) and len(raw_matrix) == 16:
        # glTF matrices are column-major.
        return [[float(raw_matrix[column * 4 + row]) for column in range(4)] for row in range(4)]
    return trs_matrix(
        node.get("translation", (0.0, 0.0, 0.0)),
        node.get("rotation", (0.0, 0.0, 0.0, 1.0)),
        node.get("scale", (1.0, 1.0, 1.0)),
    )


def transform_point(matrix: Sequence[Sequence[float]], point: Sequence[float]) -> list[float]:
    return [
        sum(float(matrix[row][column]) * float((*point, 1.0)[column]) for column in range(4))
        for row in range(3)
    ]


def read_glb_document(path: Path) -> Mapping[str, Any]:
    try:
        with path.open("rb") as handle:
            header = handle.read(12)
            if len(header) != 12:
                raise DirectRenderError(f"GLB header is truncated: {path}")
            magic, version, _length = struct.unpack("<4sII", header)
            if magic != b"glTF" or version != 2:
                raise DirectRenderError(f"Not a glTF 2 GLB: {path}")
            chunk_header = handle.read(8)
            chunk_length, chunk_type = struct.unpack("<II", chunk_header)
            if chunk_type != 0x4E4F534A:
                raise DirectRenderError(f"First GLB chunk is not JSON: {path}")
            payload = handle.read(chunk_length).decode("utf-8").rstrip("\x00 \t\r\n")
        document = json.loads(payload)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, struct.error) as exc:
        raise DirectRenderError(f"Could not inspect GLB {path}: {exc}") from exc
    if not isinstance(document, Mapping):
        raise DirectRenderError(f"GLB JSON root is not an object: {path}")
    return document


def glb_chunks(path: Path) -> tuple[int, list[tuple[int, bytes]]]:
    try:
        payload = path.read_bytes()
        if len(payload) < 12:
            raise DirectRenderError(f"GLB header is truncated: {path}")
        magic, version, declared_length = struct.unpack_from("<4sII", payload, 0)
        if magic != b"glTF" or version != 2 or declared_length != len(payload):
            raise DirectRenderError(f"Invalid glTF 2 GLB header: {path}")
        offset = 12
        chunks: list[tuple[int, bytes]] = []
        while offset < len(payload):
            length, kind = struct.unpack_from("<II", payload, offset)
            offset += 8
            end = offset + length
            if end > len(payload):
                raise DirectRenderError(f"GLB chunk is truncated: {path}")
            chunks.append((kind, payload[offset:end]))
            offset = end
    except (OSError, struct.error) as exc:
        raise DirectRenderError(f"Could not read GLB chunks {path}: {exc}") from exc
    return version, chunks


def texture_source(glb: Path, uri: str) -> Path:
    decoded = urllib.parse.unquote(uri).replace("\\", "/")
    if decoded.startswith("file:///"):
        decoded = decoded[8:]
    if decoded.startswith("?/"):
        decoded = decoded[2:]
    candidate = Path(decoded)
    if not candidate.is_absolute():
        candidate = glb.parent / candidate
    return candidate.resolve()


def hardlink_or_copy(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.is_file():
        return
    try:
        os.link(source, target)
    except OSError:
        shutil.copy2(source, target)


def materialize_catalog_texture(source: Path, target: Path) -> None:
    if target.is_file():
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_name(f".{target.name}.{os.getpid()}.tmp")
    try:
        with Image.open(source) as image:
            image.load()
            if image.mode not in {"1", "L", "LA", "RGB", "RGBA", "I;16"}:
                image = image.convert("RGBA")
            image.thumbnail(
                (CATALOG_TEXTURE_MAX_DIMENSION, CATALOG_TEXTURE_MAX_DIMENSION),
                Image.Resampling.LANCZOS,
            )
            image.save(temporary, format="PNG", compress_level=4)
        os.replace(temporary, target)
    except (OSError, ValueError) as exc:
        raise DirectRenderError(
            f"Could not create catalog texture {target} from {source}: {exc}"
        ) from exc
    finally:
        temporary.unlink(missing_ok=True)


def terrain_uv_transform(source: Path) -> tuple[float, float, float, float] | None:
    material_path = source.with_name(f"{source.stem}.Material.json")
    if not material_path.is_file():
        return None
    document = read_json(material_path)
    if not isinstance(document, Mapping):
        return None
    materials = document.get("Materials", [])
    if not isinstance(materials, Sequence):
        return None
    for material in materials:
        if not isinstance(material, Mapping):
            continue
        template = str(material.get("MaterialTemplate", material.get("BaseMaterial", "")))
        if template.replace("/", "\\").casefold() != "base\\materials\\multilayered_terrain.mt":
            continue
        data = material.get("Data", {})
        transform = data.get("UVGenScaleOffset", {}) if isinstance(data, Mapping) else {}
        if isinstance(transform, Mapping):
            defaults = (1.0, 1.0, 0.0, 0.0)
            return tuple(
                float(transform.get(key, fallback))
                for key, fallback in zip("XYZW", defaults)
            )
    return None


def add_planar_terrain_uvs(
    document: dict[str, Any],
    binary_payload: bytes,
    transform: tuple[float, float, float, float],
) -> bytes:
    """Generate RED terrain UV0 from local X/Z positions for standard glTF."""
    buffers = document.get("buffers", [])
    buffer_views = document.get("bufferViews", [])
    accessors = document.get("accessors", [])
    meshes = document.get("meshes", [])
    if not all(isinstance(value, list) for value in (buffers, buffer_views, accessors, meshes)):
        raise DirectRenderError("Terrain GLB has invalid buffer tables")
    if not buffers or not isinstance(buffers[0], dict):
        raise DirectRenderError("Terrain GLB has no primary buffer")
    declared_length = int(buffers[0].get("byteLength", len(binary_payload)))
    payload = bytearray(binary_payload[:declared_length])
    scale_u, scale_v, offset_u, offset_v = transform
    for mesh in meshes:
        if not isinstance(mesh, Mapping):
            continue
        for primitive in mesh.get("primitives", []):
            if not isinstance(primitive, dict):
                continue
            attributes = primitive.get("attributes", {})
            if not isinstance(attributes, dict) or "TEXCOORD_0" in attributes:
                continue
            position_index = attributes.get("POSITION")
            if not isinstance(position_index, int) or not 0 <= position_index < len(accessors):
                continue
            position_accessor = accessors[position_index]
            if not isinstance(position_accessor, Mapping):
                continue
            if position_accessor.get("componentType") != 5126 or position_accessor.get("type") != "VEC3":
                raise DirectRenderError("Terrain POSITION accessor is not float VEC3")
            view_index = position_accessor.get("bufferView")
            if not isinstance(view_index, int) or not 0 <= view_index < len(buffer_views):
                raise DirectRenderError("Terrain POSITION accessor has no buffer view")
            view = buffer_views[view_index]
            if not isinstance(view, Mapping) or int(view.get("buffer", 0)) != 0:
                raise DirectRenderError("Terrain POSITION accessor is not in the primary buffer")
            count = int(position_accessor.get("count", 0))
            stride = int(view.get("byteStride", 12))
            start = int(view.get("byteOffset", 0)) + int(position_accessor.get("byteOffset", 0))
            uv_values = bytearray()
            minimum = [math.inf, math.inf]
            maximum = [-math.inf, -math.inf]
            for vertex in range(count):
                x, _y, z = struct.unpack_from("<fff", binary_payload, start + vertex * stride)
                uv = (x * scale_u + offset_u, z * scale_v + offset_v)
                uv_values.extend(struct.pack("<ff", *uv))
                for axis in range(2):
                    minimum[axis] = min(minimum[axis], uv[axis])
                    maximum[axis] = max(maximum[axis], uv[axis])
            payload.extend(b"\x00" * ((-len(payload)) % 4))
            uv_offset = len(payload)
            payload.extend(uv_values)
            buffer_views.append(
                {
                    "buffer": 0,
                    "byteOffset": uv_offset,
                    "byteLength": len(uv_values),
                    "target": 34962,
                }
            )
            accessors.append(
                {
                    "bufferView": len(buffer_views) - 1,
                    "componentType": 5126,
                    "count": count,
                    "type": "VEC2",
                    "min": minimum,
                    "max": maximum,
                }
            )
            attributes["TEXCOORD_0"] = len(accessors) - 1
    buffers[0]["byteLength"] = len(payload)
    payload.extend(b"\x00" * ((-len(payload)) % 4))
    return bytes(payload)


def materialize_glb(source: Path, assets_root: Path, fingerprint: str) -> Path:
    """Rewrite external image URIs to persistent, shared, relative textures."""

    uv_transform = terrain_uv_transform(source)
    gltf_version = TERRAIN_GLTF_VERSION if uv_transform is not None else CATALOG_TEXTURE_VERSION
    destination = (
        assets_root
        / f"meshes-{gltf_version}"
        / fingerprint
        / "render.glb"
    )
    manifest_path = destination.with_name("render-manifest.json")
    if destination.is_file() and manifest_path.is_file():
        return destination
    version, chunks = glb_chunks(source)
    if not chunks or chunks[0][0] != 0x4E4F534A:
        raise DirectRenderError(f"GLB has no leading JSON chunk: {source}")
    try:
        document = json.loads(chunks[0][1].decode("utf-8").rstrip("\x00 \t\r\n"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise DirectRenderError(f"Could not decode GLB JSON {source}: {exc}") from exc
    if not isinstance(document, dict):
        raise DirectRenderError(f"GLB JSON root is not an object: {source}")
    installed_textures: list[dict[str, str]] = []
    images = document.get("images", [])
    if isinstance(images, list):
        for image in images:
            if not isinstance(image, dict):
                continue
            uri = image.get("uri")
            if not isinstance(uri, str) or uri.startswith("data:"):
                continue
            texture = texture_source(source, uri)
            if not texture.is_file():
                raise DirectRenderError(
                    f"Materialized GLB texture is missing: {texture} (from {source})"
                )
            digest = hashlib.sha256(texture.read_bytes()).hexdigest()
            target = (
                assets_root
                / f"textures-{CATALOG_TEXTURE_VERSION}"
                / f"{digest}.png"
            )
            materialize_catalog_texture(texture, target)
            image["uri"] = os.path.relpath(target, destination.parent).replace("\\", "/")
            installed_textures.append(
                {
                    "source": str(texture),
                    "asset": str(target.resolve()),
                    "sha256": digest,
                }
            )
    rewritten_tail = list(chunks[1:])
    if uv_transform is not None:
        for index, (kind, payload) in enumerate(rewritten_tail):
            if kind == 0x004E4942:
                rewritten_tail[index] = (
                    kind,
                    add_planar_terrain_uvs(document, payload, uv_transform),
                )
                break
        else:
            raise DirectRenderError(f"Terrain GLB has no binary chunk: {source}")
    json_payload = json.dumps(document, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    json_payload += b" " * ((-len(json_payload)) % 4)
    rewritten = [(0x4E4F534A, json_payload), *rewritten_tail]
    total_length = 12 + sum(8 + len(payload) for _, payload in rewritten)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(f".{destination.name}.{os.getpid()}.tmp")
    try:
        with temporary.open("wb") as handle:
            handle.write(struct.pack("<4sII", b"glTF", version, total_length))
            for kind, payload in rewritten:
                handle.write(struct.pack("<II", len(payload), kind))
                handle.write(payload)
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)
    write_json(
        manifest_path,
        {
            "schema_version": 1,
            "source_glb": str(source.resolve()),
            "asset_glb": str(destination.resolve()),
            "fingerprint": fingerprint,
            "textures": installed_textures,
        },
    )
    return destination


def glb_bounds(path: Path) -> tuple[list[float], list[float]] | None:
    document = read_glb_document(path)
    nodes = document.get("nodes", [])
    meshes = document.get("meshes", [])
    accessors = document.get("accessors", [])
    scenes = document.get("scenes", [])
    if not all(isinstance(value, Sequence) and not isinstance(value, (str, bytes)) for value in (nodes, meshes, accessors, scenes)):
        return None
    scene_index = int(document.get("scene", 0)) if scenes else -1
    roots = scenes[scene_index].get("nodes", []) if 0 <= scene_index < len(scenes) and isinstance(scenes[scene_index], Mapping) else range(len(nodes))
    minimum = [math.inf, math.inf, math.inf]
    maximum = [-math.inf, -math.inf, -math.inf]

    def visit(index: int, parent: Sequence[Sequence[float]]) -> None:
        if index < 0 or index >= len(nodes) or not isinstance(nodes[index], Mapping):
            return
        node = nodes[index]
        world = matrix_multiply(parent, gltf_node_matrix(node))
        mesh_index = node.get("mesh")
        if isinstance(mesh_index, int) and 0 <= mesh_index < len(meshes) and isinstance(meshes[mesh_index], Mapping):
            for primitive in meshes[mesh_index].get("primitives", []):
                if not isinstance(primitive, Mapping):
                    continue
                attributes = primitive.get("attributes", {})
                accessor_index = attributes.get("POSITION") if isinstance(attributes, Mapping) else None
                if not isinstance(accessor_index, int) or not (0 <= accessor_index < len(accessors)):
                    continue
                accessor = accessors[accessor_index]
                if not isinstance(accessor, Mapping):
                    continue
                low, high = accessor.get("min"), accessor.get("max")
                if not (isinstance(low, Sequence) and isinstance(high, Sequence) and len(low) >= 3 and len(high) >= 3):
                    continue
                for x in (float(low[0]), float(high[0])):
                    for y in (float(low[1]), float(high[1])):
                        for z in (float(low[2]), float(high[2])):
                            transformed = transform_point(world, (x, y, z))
                            for axis in range(3):
                                minimum[axis] = min(minimum[axis], transformed[axis])
                                maximum[axis] = max(maximum[axis], transformed[axis])
        for child in node.get("children", []):
            if isinstance(child, int):
                visit(child, world)

    for root in roots:
        if isinstance(root, int):
            visit(root, identity())
    if not all(math.isfinite(value) for value in (*minimum, *maximum)):
        return None
    return minimum, maximum


def transformed_bounds(
    bounds: tuple[Sequence[float], Sequence[float]],
    matrix: Sequence[Sequence[float]],
) -> tuple[list[float], list[float]]:
    low, high = bounds
    points = [
        transform_point(matrix, (x, y, z))
        for x in (low[0], high[0])
        for y in (low[1], high[1])
        for z in (low[2], high[2])
    ]
    return (
        [min(point[axis] for point in points) for axis in range(3)],
        [max(point[axis] for point in points) for axis in range(3)],
    )


def intersects(bounds: tuple[Sequence[float], Sequence[float]], tile: Sequence[float], margin: float) -> bool:
    low, high = bounds
    return all(
        high[axis] >= float(tile[axis]) - margin
        and low[axis] <= float(tile[axis + 3]) + margin
        for axis in range(3)
    )


RED_TO_GODOT = [
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
    [0.0, -1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0],
]
GODOT_TO_RED = [
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, -1.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0],
]


def rebase_and_convert(matrix: Sequence[Sequence[float]], origin: Sequence[float]) -> list[float]:
    rebased = [list(row) for row in matrix]
    for axis in range(3):
        rebased[axis][3] -= float(origin[axis])
    converted = matrix_multiply(matrix_multiply(RED_TO_GODOT, rebased), GODOT_TO_RED)
    return [converted[row][column] for row in range(4) for column in range(4)]


def convert_point(point: Sequence[float], origin: Sequence[float]) -> list[float]:
    return [
        float(point[0]) - float(origin[0]),
        float(point[2]) - float(origin[2]),
        -(float(point[1]) - float(origin[1])),
    ]


def useful_view_yaws(
    eye: Sequence[float],
    geometry: Sequence[tuple[Sequence[float], Sequence[float]]],
    count: int,
    fallback_yaw: float,
) -> list[float]:
    """Choose separated headings that put nearby, above-ground geometry in frame."""
    candidates = [float(angle) for angle in range(0, 360, 15)]
    scored: list[tuple[float, float]] = []
    for yaw in candidates:
        score = 0.0
        for center, extent in geometry:
            dx = float(center[0]) - float(eye[0])
            dy = float(center[1]) - float(eye[1])
            distance = math.hypot(dx, dy)
            if distance < 2.0 or distance > 120.0:
                continue
            relative = (math.degrees(math.atan2(dy, dx)) - yaw + 180.0) % 360.0 - 180.0
            if abs(relative) > 42.0:
                continue
            vertical_interest = max(0.25, min(8.0, float(extent[2])))
            horizontal_interest = max(0.5, min(8.0, max(float(extent[0]), float(extent[1]))))
            centered = math.cos(math.radians(relative / 42.0 * 90.0)) ** 2
            score += centered * math.sqrt(vertical_interest * horizontal_interest) / (distance + 5.0)
        scored.append((score, yaw))

    selected: list[float] = []
    for score, yaw in sorted(scored, reverse=True):
        if score <= 0.0:
            break
        if all(abs((yaw - other + 180.0) % 360.0 - 180.0) >= 55.0 for other in selected):
            selected.append(yaw)
            if len(selected) == count:
                return sorted(selected)

    for offset in range(0, 360, max(1, 360 // count)):
        yaw = (fallback_yaw + offset) % 360.0
        if all(abs((yaw - other + 180.0) % 360.0 - 180.0) >= 55.0 for other in selected):
            selected.append(yaw)
        if len(selected) == count:
            break
    return sorted(selected)


def sector_records(root: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    raw = root.get("nodeData", [])
    if isinstance(raw, Mapping):
        raw = raw.get("Data", [])
    if not isinstance(raw, Sequence) or isinstance(raw, (str, bytes)):
        return []
    return [row for row in raw if isinstance(row, Mapping)]


def transform_buffer(
    nodes: Sequence[Any], node: Mapping[str, Any], field: str
) -> list[Mapping[str, Any]]:
    descriptor = node.get(field)
    if not isinstance(descriptor, Mapping):
        return []
    shared = descriptor.get("sharedDataBuffer")
    if not isinstance(shared, Mapping):
        return []
    data = shared.get("Data")
    if not isinstance(data, Mapping):
        handle_ref = str(wrapped_value(shared.get("HandleRefId"), ""))
        try:
            owner_handle = str(int(handle_ref) - 1)
        except ValueError:
            return []
        owner = next(
            (
                candidate.get("Data")
                for candidate in nodes
                if isinstance(candidate, Mapping)
                and str(candidate.get("HandleId", "")) == owner_handle
                and isinstance(candidate.get("Data"), Mapping)
            ),
            None,
        )
        if not isinstance(owner, Mapping):
            return []
        owner_descriptor = owner.get(field)
        owner_shared = owner_descriptor.get("sharedDataBuffer") if isinstance(owner_descriptor, Mapping) else None
        data = owner_shared.get("Data") if isinstance(owner_shared, Mapping) else None
    buffer = data.get("buffer") if isinstance(data, Mapping) else None
    expanded = buffer.get("Data") if isinstance(buffer, Mapping) else None
    transforms = expanded.get("Transforms") if isinstance(expanded, Mapping) else None
    if not isinstance(transforms, Sequence) or isinstance(transforms, (str, bytes)):
        return []
    return [item for item in transforms if isinstance(item, Mapping)]


def node_matrices(
    node_type: str,
    node: Mapping[str, Any],
    records: Sequence[Mapping[str, Any]],
    nodes: Sequence[Any],
) -> list[list[list[float]]]:
    if node_type in STATIC_MESH_NODE_TYPES:
        return [instance_matrix(record) for record in records]
    if node_type == "worldInstancedMeshNode":
        descriptor = node.get("worldTransformsBuffer", {})
        transforms = transform_buffer(nodes, node, "worldTransformsBuffer")
        start = int(wrapped_value(descriptor.get("startIndex"), 0)) if isinstance(descriptor, Mapping) else 0
        count = int(wrapped_value(descriptor.get("numElements"), len(transforms))) if isinstance(descriptor, Mapping) else len(transforms)
        return [instance_matrix(value) for value in transforms[start : start + count]]
    if node_type == "worldInstancedDestructibleMeshNode":
        descriptor = node.get("cookedInstanceTransforms", {})
        transforms = transform_buffer(nodes, node, "cookedInstanceTransforms")
        start = int(wrapped_value(descriptor.get("startIndex"), 0)) if isinstance(descriptor, Mapping) else 0
        count = int(wrapped_value(descriptor.get("numElements"), len(transforms))) if isinstance(descriptor, Mapping) else len(transforms)
        children = [instance_matrix(value) for value in transforms[start : start + count]]
        return [matrix_multiply(instance_matrix(parent), child) for parent in records for child in children]
    return []


def select_job(document: Mapping[str, Any], selector: str) -> Mapping[str, Any]:
    jobs = document.get("jobs", [])
    if not isinstance(jobs, Sequence) or isinstance(jobs, (str, bytes)):
        raise DirectRenderError("Render jobs document has no jobs array")
    matches = [
        job
        for job in jobs
        if isinstance(job, Mapping)
        and (
            str(job.get("tile_id", "")) == selector
            or str(job.get("tile_id", "")).split("--", 1)[0] == selector
        )
    ]
    if len(matches) != 1:
        raise DirectRenderError(
            f"Tile selector {selector!r} matched {len(matches)} render jobs; use an exact tile-state id"
        )
    return matches[0]


def sector_kind_and_lod(path: Path) -> tuple[str, int]:
    name = path.name.removesuffix(".streamingsector.json")
    if name.startswith("exterior_"):
        kind = "exterior"
    elif name.startswith("interior_"):
        kind = "interior"
    elif name.startswith("quest_"):
        kind = "quest"
    else:
        kind = "other"
    suffix = name.rsplit("_", 1)[-1]
    lod = int(suffix) if suffix in {"0", "1", "2"} else 0
    return kind, lod


def build_scene_manifest(
    job: Mapping[str, Any], output_root: Path, *, clip_margin: float = 64.0
) -> dict[str, Any]:
    tile_id = str(job.get("tile_id", ""))
    tile_bounds = job.get("tile_bounds", [])
    if not isinstance(tile_bounds, Sequence) or len(tile_bounds) != 6:
        raise DirectRenderError(f"Render job {tile_id} has invalid tile_bounds")
    project_raw = Path(str(job.get("project", ""))) / "source/raw"
    all_sector_paths = sorted(project_raw.rglob("*.streamingsector.json"))
    sector_paths = [
        path
        for path in all_sector_paths
        if sector_kind_and_lod(path)[0] in {"exterior", "interior", "quest", "other"}
    ]
    assets = job.get("native_pbr_assets", [])
    if not isinstance(assets, Sequence) or isinstance(assets, (str, bytes)):
        raise DirectRenderError(f"Render job {tile_id} has invalid native_pbr_assets")
    if not assets:
        cached_assets: list[dict[str, Any]] = []
        for manifest_path in sorted((output_root / "cache/pbr-meshes").glob("*/manifest.json")):
            try:
                cached = read_json(manifest_path)
            except (DirectRenderError, OSError, ValueError):
                continue
            if not isinstance(cached, Mapping):
                continue
            glb = Path(str(cached.get("glb", "")))
            material_json = Path(str(cached.get("material_json", "")))
            if glb.is_file() and material_json.is_file():
                cached_assets.append(dict(cached))
        assets = cached_assets
        print(
            f"GHOSTLINE_DIRECT_ASSET_CACHE reused={len(assets)}",
            flush=True,
        )
    asset_index: dict[tuple[str, str], dict[str, Any]] = {}
    for row in assets:
        if not isinstance(row, Mapping):
            continue
        key = (
            str(row.get("depot_path", "")).replace("/", "\\").casefold(),
            str(row.get("appearance", "default")).casefold(),
        )
        glb = Path(str(row.get("glb", "")))
        if key[0] and glb.is_file():
            asset_index[key] = dict(row)

    materialization_failures: list[dict[str, str]] = []
    assets_root = output_root / "assets"

    origin = [
        (float(tile_bounds[0]) + float(tile_bounds[3])) * 0.5,
        (float(tile_bounds[1]) + float(tile_bounds[4])) * 0.5,
        (float(tile_bounds[2]) + float(tile_bounds[5])) * 0.5,
    ]
    camera_positions = [
        [
            float(viewpoint["surface_position"][0]),
            float(viewpoint["surface_position"][1]),
            float(viewpoint["surface_position"][2])
            + float(viewpoint.get("eye_height", 1.7)),
        ]
        for viewpoint in job.get("viewpoints", [])
        if isinstance(viewpoint, Mapping)
        and isinstance(viewpoint.get("surface_position"), Sequence)
        and len(viewpoint["surface_position"]) >= 3
    ]
    bounds_cache: dict[Path, tuple[list[float], list[float]] | None] = {}
    batches: dict[tuple[str, str], dict[str, Any]] = {}
    missing: dict[tuple[str, str], dict[str, Any]] = {}
    node_type_counts: defaultdict[str, int] = defaultdict(int)
    candidate_instances = 0
    retained_instances = 0
    clipped_instances = 0
    catalog_culled_instances = 0
    visible_geometry: list[tuple[list[float], list[float]]] = []

    for sector_number, sector_path in enumerate(sector_paths, 1):
        _, sector_lod = sector_kind_and_lod(sector_path)
        document = read_json(sector_path)
        root = document.get("Data", {}).get("RootChunk", {}) if isinstance(document, Mapping) else {}
        if not isinstance(root, Mapping):
            continue
        nodes = root.get("nodes", [])
        if not isinstance(nodes, Sequence) or isinstance(nodes, (str, bytes)):
            continue
        records_by_node: defaultdict[int, list[Mapping[str, Any]]] = defaultdict(list)
        for record in sector_records(root):
            try:
                index = int(wrapped_value(record.get("NodeIndex"), -1))
            except (TypeError, ValueError):
                continue
            records_by_node[index].append(record)
        for node_index, wrapper in enumerate(nodes):
            data = wrapper.get("Data") if isinstance(wrapper, Mapping) else None
            if not isinstance(data, Mapping):
                continue
            node_type = str(data.get("$type", ""))
            if node_type in ALTERNATE_DESTRUCTION_NODE_TYPES:
                continue
            depot_path = resource_path(data)
            if not depot_path:
                continue
            matrices = node_matrices(
                node_type, data, records_by_node.get(node_index, []), nodes
            )
            if not matrices:
                continue
            appearance = mesh_appearance(data)
            key = (depot_path, appearance.casefold())
            asset = asset_index.get(key)
            candidate_instances += len(matrices)
            node_type_counts[node_type] += len(matrices)
            if asset is None:
                record = missing.setdefault(
                    key,
                    {
                        "depot_path": depot_path,
                        "appearance": appearance,
                        "instance_count": 0,
                        "node_types": set(),
                    },
                )
                record["instance_count"] += len(matrices)
                record["node_types"].add(node_type)
                continue
            glb = Path(str(asset["glb"])).resolve()
            if glb not in bounds_cache:
                bounds_cache[glb] = glb_bounds(glb)
            local_bounds = bounds_cache[glb]
            batch_key = key
            batch = batches.setdefault(
                batch_key,
                {
                    "source_glb": str(glb),
                    "fingerprint": str(asset.get("fingerprint", "")),
                    "depot_path": depot_path,
                    "appearance": appearance,
                    "transforms": [],
                    "visibility": [],
                },
            )
            for matrix in matrices:
                world_bounds = transformed_bounds(local_bounds, matrix) if local_bounds is not None else None
                if world_bounds is not None:
                    if not intersects(world_bounds, tile_bounds, clip_margin):
                        clipped_instances += 1
                        continue
                    low, high = world_bounds
                    dimensions = [high[axis] - low[axis] for axis in range(3)]
                    largest_dimension = max(dimensions)
                    if largest_dimension < 0.5:
                        catalog_culled_instances += 1
                        continue
                    center = [(low[axis] + high[axis]) * 0.5 for axis in range(3)]
                    structural = (
                        node_type in COARSE_LOD_NODE_TYPES
                        or node_type == "worldGenericProxyMeshNode"
                        or largest_dimension >= 12.0
                    )
                    if camera_positions and not structural:
                        nearest_camera = min(
                            math.dist(center, camera) for camera in camera_positions
                        )
                        if nearest_camera > 90.0:
                            catalog_culled_instances += 1
                            continue
                    visible_geometry.append(
                        (
                            center,
                            dimensions,
                        )
                    )
                batch["transforms"].append(rebase_and_convert(matrix, origin))
                batch["visibility"].append(
                    {
                        "center": convert_point(center, origin),
                        "radius": 0.5 * math.sqrt(sum(value * value for value in dimensions)),
                        "dimensions": dimensions,
                        "node_type": node_type,
                    }
                    if world_bounds is not None
                    else None
                )
                retained_instances += 1
        if sector_number == 1 or sector_number % 50 == 0 or sector_number == len(sector_paths):
            print(
                f"GHOSTLINE_DIRECT_SECTORS [{sector_number}/{len(sector_paths)}] "
                f"candidates={candidate_instances} retained={retained_instances}",
                flush=True,
            )

    retained_batch_candidates = [
        batch for batch in batches.values() if batch["transforms"]
    ]
    retained_batches = []
    total_assets = len(retained_batch_candidates)
    for asset_number, batch in enumerate(retained_batch_candidates, 1):
        try:
            batch["asset"] = str(
                materialize_glb(
                    Path(str(batch.pop("source_glb"))).resolve(),
                    assets_root,
                    str(batch.get("fingerprint")),
                ).resolve()
            )
            retained_batches.append(batch)
        except DirectRenderError as exc:
            materialization_failures.append(
                {
                    "depot_path": str(batch.get("depot_path", "")),
                    "appearance": str(batch.get("appearance", "default")),
                    "error": str(exc),
                }
            )
        if asset_number == 1 or asset_number % 25 == 0 or asset_number == total_assets:
            print(
                f"GHOSTLINE_DIRECT_MATERIALIZE [{asset_number}/{total_assets}] "
                f"ready={len(retained_batches)} "
                f"failed={len(materialization_failures)}",
                flush=True,
            )
    retained_batches.sort(key=lambda row: (row["depot_path"], row["appearance"]))
    retained_instances = sum(
        len(batch["transforms"]) for batch in retained_batches
    )
    viewpoints = []
    for viewpoint_number, viewpoint in enumerate(job.get("viewpoints", []), 1):
        if not isinstance(viewpoint, Mapping):
            continue
        surface = viewpoint.get("surface_position", (0.0, 0.0, 0.0))
        eye = [float(surface[0]), float(surface[1]), float(surface[2]) + float(viewpoint.get("eye_height", 1.7))]
        direction_count = len(viewpoint.get("directions", (0.0, 90.0, 180.0, 270.0)))
        yaws = useful_view_yaws(
            eye,
            visible_geometry,
            direction_count,
            float(viewpoint.get("yaw_degrees", 0.0)),
        )
        pitch = math.radians(-8.0)
        for yaw in yaws:
            radians = math.radians(yaw)
            horizontal = math.cos(pitch)
            forward_red = [horizontal * math.cos(radians), horizontal * math.sin(radians), math.sin(pitch)]
            forward_godot = [forward_red[0], forward_red[2], -forward_red[1]]
            viewpoints.append(
                {
                    "id": str(viewpoint.get("id", "viewpoint")),
                    "folder": f"viewpoint-{viewpoint_number:02d}",
                    "direction": f"yaw_{yaw:06.2f}",
                    "yaw_degrees": yaw,
                    "pitch_degrees": -8.0,
                    "eye_height": float(viewpoint.get("eye_height", 1.7)),
                    "position": convert_point(eye, origin),
                    "forward": forward_godot,
                    "horizontal_fov_degrees": float(viewpoint.get("horizontal_fov_degrees", job.get("horizontal_fov_degrees", 80.0))),
                    "metadata": viewpoint.get("metadata", {}),
                }
            )

    scene_path = output_root / "assets/tiles" / tile_id / "scene.json"
    render_output = output_root / "renders" / tile_id
    manifest = {
        "schema_version": 1,
        "renderer": "godot-direct-gltf",
        "tile_id": tile_id,
        "run_id": str(job.get("run_id", "")),
        "content_fingerprint": str(job.get("content_fingerprint", "")),
        "renderer_fingerprint": current_renderer_fingerprint(),
        "tile_bounds_red": [float(value) for value in tile_bounds],
        "origin_red": origin,
        "clip_margin": float(clip_margin),
        "resolution": max(1024, int(job.get("resolution", 1024))),
        "image_quality": int(job.get("image_quality", 90)),
        "output": str(render_output.resolve()),
        "batches": retained_batches,
        "viewpoints": viewpoints,
        "missing_assets": [
            {
                **record,
                "node_types": sorted(record["node_types"]),
            }
            for _, record in sorted(missing.items())
        ],
        "materialization_failures": materialization_failures,
        "summary": {
            "sector_files": len(sector_paths),
            "available_assets": len(asset_index),
            "materialization_failures": len(materialization_failures),
            "retained_batches": len(retained_batches),
            "candidate_instances": candidate_instances,
            "retained_instances": retained_instances,
            "clipped_instances": clipped_instances,
            "catalog_culled_instances": catalog_culled_instances,
            "missing_asset_pairs": len(missing),
            "missing_asset_instances": sum(record["instance_count"] for record in missing.values()),
            "view_count": len(viewpoints),
            "node_type_instances": dict(sorted(node_type_counts.items())),
        },
    }
    write_json(scene_path, manifest)
    return {"scene": str(scene_path.resolve()), **manifest["summary"]}


def run_godot_scene(godot: Path, scene_path: Path, report_path: Path) -> dict[str, Any]:
    """Render one already-scoped scene manifest in a fresh Godot process."""
    command = [
        str(godot),
        "--rendering-method",
        "mobile",
        "--rendering-driver",
        "vulkan",
        "--position",
        "10000,10000",
        "--path",
        str(GODOT_PROJECT),
        "--",
        "--scene",
        str(scene_path.resolve()),
        "--report",
        str(report_path.resolve()),
    ]
    started = time.perf_counter()
    process = subprocess.Popen(
        command,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    tail: list[str] = []
    assert process.stdout is not None
    for line in process.stdout:
        tail.append(line)
        tail = tail[-200:]
        message = line.strip()
        if message.startswith("GHOSTLINE_DIRECT_"):
            print(message, flush=True)
    return_code = process.wait()
    if return_code != 0 or not report_path.is_file():
        raise DirectRenderError(
            f"Godot direct renderer exited {return_code}:\n{''.join(tail)[-8000:]}"
        )
    report = read_json(report_path)
    if not isinstance(report, dict):
        raise DirectRenderError(f"Godot wrote an invalid report: {report_path}")
    report["process_seconds"] = time.perf_counter() - started
    return report


def viewpoint_chunk(
    scene: Mapping[str, Any], viewpoint_rows: Sequence[Mapping[str, Any]]
) -> dict[str, Any]:
    """Return a scene containing geometry close enough to affect one viewpoint."""
    camera = viewpoint_rows[0].get("position", [0.0, 0.0, 0.0])
    if not isinstance(camera, Sequence) or len(camera) < 3:
        raise DirectRenderError("Viewpoint chunk has an invalid camera position")
    camera_position = [float(camera[index]) for index in range(3)]
    batches: list[dict[str, Any]] = []
    for raw_batch in scene.get("batches", []):
        if not isinstance(raw_batch, Mapping):
            continue
        transforms = raw_batch.get("transforms", [])
        visibility = raw_batch.get("visibility", [])
        if not isinstance(transforms, Sequence):
            continue
        selected_transforms: list[Any] = []
        selected_visibility: list[Any] = []
        for index, transform in enumerate(transforms):
            bounds = visibility[index] if isinstance(visibility, Sequence) and index < len(visibility) else None
            include = not isinstance(bounds, Mapping)
            if isinstance(bounds, Mapping):
                center = bounds.get("center", [])
                radius = float(bounds.get("radius", 0.0))
                if isinstance(center, Sequence) and len(center) >= 3:
                    include = math.dist(
                        camera_position,
                        [float(center[axis]) for axis in range(3)],
                    ) <= VIEWPOINT_CHUNK_RADIUS + radius
            if include:
                selected_transforms.append(transform)
                selected_visibility.append(bounds)
        if selected_transforms:
            batch = dict(raw_batch)
            batch["transforms"] = selected_transforms
            batch["visibility"] = selected_visibility
            batches.append(batch)
    chunk = dict(scene)
    chunk["batches"] = batches
    chunk["viewpoints"] = [dict(row) for row in viewpoint_rows]
    return chunk


def invalid_rendered_viewpoint_reason(view_paths: Sequence[Path]) -> str | None:
    """Detect cameras exposing missing world surfaces or enclosed black geometry."""
    bright_frames = 0
    black_frames = 0
    for path in view_paths:
        with Image.open(path) as source:
            image = source.convert("RGB")
            image.thumbnail((128, 128), Image.Resampling.LANCZOS)
            pixels = list(image.getdata())
        if not pixels:
            return "empty_framebuffer"
        luminance = [
            0.2126 * red + 0.7152 * green + 0.0722 * blue
            for red, green, blue in pixels
        ]
        bright_fraction = sum(value > 245.0 for value in luminance) / len(luminance)
        dark_fraction = sum(value < 5.0 for value in luminance) / len(luminance)
        if bright_fraction > 0.20:
            bright_frames += 1
        if dark_fraction > 0.90:
            black_frames += 1
    if bright_frames >= 2:
        return "missing_surface_visible"
    if black_frames >= 3:
        return "camera_enclosed_by_geometry"
    return None


def render_scene(godot: Path, scene_path: Path) -> dict[str, Any]:
    if not godot.is_file():
        raise DirectRenderError(
            f"Godot executable is missing: {godot}. Run the renderer install command first."
        )
    if not (GODOT_PROJECT / "project.godot").is_file():
        raise DirectRenderError(f"Godot renderer project is missing: {GODOT_PROJECT}")
    scene_document = read_json(scene_path)
    if not isinstance(scene_document, Mapping):
        raise DirectRenderError(f"Scene manifest is invalid: {scene_path}")
    scene_document = dict(scene_document)
    scene_document["renderer_fingerprint"] = current_renderer_fingerprint()
    write_json(scene_path, scene_document)
    render_output = Path(str(scene_document.get("output", ""))).resolve()
    if render_output.parent.name != "renders" or render_output.name != str(scene_document.get("tile_id", "")):
        raise DirectRenderError(f"Refusing to clear unexpected render output: {render_output}")
    views_path = render_output / "views"
    if views_path.is_dir():
        for old_file in views_path.rglob("*"):
            if old_file.is_file():
                old_file.unlink()
        for old_directory in sorted(
            (path for path in views_path.rglob("*") if path.is_dir()),
            key=lambda path: len(path.parts),
            reverse=True,
        ):
            try:
                old_directory.rmdir()
            except OSError:
                pass
    report_path = scene_path.with_name("render-report.json")
    report_path.unlink(missing_ok=True)
    grouped_viewpoints: dict[str, list[Mapping[str, Any]]] = {}
    for row in scene_document.get("viewpoints", []):
        if isinstance(row, Mapping):
            grouped_viewpoints.setdefault(str(row.get("folder", "viewpoint")), []).append(row)
    rejected_viewpoints: list[dict[str, Any]] = []
    chunk_root = scene_path.parent / "viewpoint-chunks"
    reports: list[dict[str, Any]] = []
    for chunk_number, (folder, rows) in enumerate(grouped_viewpoints.items(), 1):
        chunk = viewpoint_chunk(scene_document, rows)
        chunk_path = chunk_root / folder / "scene.json"
        chunk_report_path = chunk_path.with_name("render-report.json")
        write_json(chunk_path, chunk)
        chunk_report_path.unlink(missing_ok=True)
        instance_count = sum(len(batch.get("transforms", [])) for batch in chunk["batches"])
        print(
            f"GHOSTLINE_DIRECT_CHUNK [{chunk_number}/{len(grouped_viewpoints)}] "
            f"{folder} batches={len(chunk['batches'])} instances={instance_count}",
            flush=True,
        )
        chunk_report = run_godot_scene(godot, chunk_path, chunk_report_path)
        view_paths = [
            Path(str(view.get("output", "")))
            for view in chunk_report.get("views", [])
            if isinstance(view, Mapping)
        ]
        rejection_reason = invalid_rendered_viewpoint_reason(view_paths)
        if rejection_reason is not None:
            rejected_viewpoints.append(
                {
                    "folder": folder,
                    "viewpoint_id": str(rows[0].get("id", "")),
                    "reason": rejection_reason,
                }
            )
            for path in view_paths:
                path.unlink(missing_ok=True)
            chunk_report["views"] = []
            chunk_report["total_views"] = 0
            chunk_report["rendered_views"] = 0
            chunk_report["failed_views"] = 0
            print(
                f"GHOSTLINE_DIRECT_CAMERA_REJECT {folder} reason={rejection_reason}",
                flush=True,
            )
        reports.append(chunk_report)

    report = {
        "schema_version": 1,
        "tile_id": str(scene_document.get("tile_id", "")),
        "run_id": str(scene_document.get("run_id", "")),
        "content_fingerprint": str(scene_document.get("content_fingerprint", "")),
        "scene": str(scene_path.resolve()),
        "renderer": {
            "name": "godot-direct-gltf",
            "renderer_fingerprint": str(scene_document.get("renderer_fingerprint", "")),
            "resolution": int(scene_document.get("resolution", 0)),
        },
        "loaded_batches": sum(int(item.get("loaded_batches", 0)) for item in reports),
        "mesh_parts": sum(int(item.get("mesh_parts", 0)) for item in reports),
        "views": [view for item in reports for view in item.get("views", [])],
        "total_views": sum(int(item.get("total_views", 0)) for item in reports),
        "rendered_views": sum(int(item.get("rendered_views", 0)) for item in reports),
        "failed_views": sum(int(item.get("failed_views", 0)) for item in reports),
        "missing_assets": scene_document.get("missing_assets", []),
        "process_seconds": sum(float(item.get("process_seconds", 0.0)) for item in reports),
        "chunks": len(reports),
        "rejected_viewpoints": rejected_viewpoints,
    }
    write_json(report_path, report)
    return report


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Assemble and render materialized world tiles without Blender."
    )
    parser.add_argument("command", choices=("assemble", "render", "render-all"))
    parser.add_argument("--tile")
    parser.add_argument("--jobs", type=Path, default=DEFAULT_JOBS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--godot", type=Path, default=DEFAULT_GODOT)
    parser.add_argument("--clip-margin", type=float, default=64.0)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = create_parser().parse_args(argv)
    try:
        document = read_json(args.jobs.resolve())
        if not isinstance(document, Mapping):
            raise DirectRenderError("Render jobs document root must be an object")
        if args.command == "render-all":
            raw_jobs = document.get("jobs", [])
            if not isinstance(raw_jobs, Sequence) or isinstance(raw_jobs, (str, bytes)):
                raise DirectRenderError("Render jobs document has no jobs array")
            jobs = [job for job in raw_jobs if isinstance(job, Mapping)]
        else:
            if not args.tile:
                raise DirectRenderError("--tile is required for assemble and render")
            jobs = [select_job(document, args.tile)]

        results: list[dict[str, Any]] = []
        for job_number, job in enumerate(jobs, 1):
            tile_id = str(job.get("tile_id", ""))
            print(
                f"GHOSTLINE_DIRECT_TILE [{job_number}/{len(jobs)}] {tile_id}",
                flush=True,
            )
            assembled = build_scene_manifest(
                job, args.output.resolve(), clip_margin=max(0.0, args.clip_margin)
            )
            print(
                "GHOSTLINE_DIRECT_ASSEMBLED "
                f"batches={assembled['retained_batches']} "
                f"instances={assembled['retained_instances']} "
                f"views={assembled['view_count']} "
                f"missing_instances={assembled['missing_asset_instances']}",
                flush=True,
            )
            result: dict[str, Any] = {"assembly": assembled}
            if args.command in {"render", "render-all"}:
                render_report = render_scene(
                    args.godot.resolve(), Path(assembled["scene"])
                )
                result["render"] = {
                    "report": str(
                        Path(assembled["scene"])
                        .with_name("render-report.json")
                        .resolve()
                    ),
                    "rendered_views": int(render_report.get("rendered_views", 0)),
                    "failed_views": int(render_report.get("failed_views", 0)),
                    "chunks": int(render_report.get("chunks", 0)),
                    "rejected_viewpoints": render_report.get("rejected_viewpoints", []),
                    "process_seconds": float(render_report.get("process_seconds", 0.0)),
                }
                database = args.output.resolve() / "locations.sqlite3"
                if database.is_file():
                    from world_location_database import ingest_render_report

                    batch_report = args.output.resolve() / "direct-render-report.json"
                    write_json(
                        batch_report,
                        {
                            "tiles": [
                                {
                                    "tile_id": tile_id,
                                    "report": str(
                                        Path(assembled["scene"])
                                        .with_name("render-report.json")
                                        .resolve()
                                    ),
                                }
                            ]
                        },
                    )
                    result["ingested"] = ingest_render_report(database, batch_report)
            results.append(result)
    except (DirectRenderError, OSError, ValueError) as exc:
        print(f"world-location direct-render error: {exc}", file=sys.stderr)
        return 2
    output: Any = {"tiles": results} if args.command == "render-all" else results[0]
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
