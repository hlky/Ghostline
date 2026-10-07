from __future__ import annotations

import argparse
import json
import math
import struct
from pathlib import Path


TARGET_CLIPS = {
    "stand__2h_on_knees__01",
    "stand__2h_on_knees__01__look_l__01",
    "stand__2h_on_knees__01__look_r__01",
    "stand__2h_on_knees__01__talk__01",
}

# The vanilla pose counter-rotates these bones until the face points upward.
# These local-Y offsets remove that counter-rotation and leave the face tilted
# slightly below the torso's forward line toward the low camera.
PITCH_OFFSETS_DEGREES = {
    "Neck": -8.0,
    "Neck1": -18.0,
    "Head": -32.0,
}


def multiply_quaternions(
    left: tuple[float, float, float, float],
    right: tuple[float, float, float, float],
) -> tuple[float, float, float, float]:
    lx, ly, lz, lw = left
    rx, ry, rz, rw = right
    return (
        lw * rx + lx * rw + ly * rz - lz * ry,
        lw * ry - lx * rz + ly * rw + lz * rx,
        lw * rz + lx * ry - ly * rx + lz * rw,
        lw * rw - lx * rx - ly * ry - lz * rz,
    )


def normalize_quaternion(
    value: tuple[float, float, float, float],
) -> tuple[float, float, float, float]:
    length = math.sqrt(sum(component * component for component in value))
    return tuple(component / length for component in value)  # type: ignore[return-value]


def adjust_glb(source: Path, destination: Path) -> int:
    output = bytearray(source.read_bytes())
    magic, version, total_length = struct.unpack_from("<4sII", output, 0)
    if magic != b"glTF" or version != 2 or total_length != len(output):
        raise ValueError(f"{source} is not a valid glTF 2 GLB")

    offset = 12
    gltf: dict | None = None
    binary_offset: int | None = None
    binary_length: int | None = None
    while offset < total_length:
        chunk_length, chunk_type = struct.unpack_from("<I4s", output, offset)
        chunk_data_offset = offset + 8
        if chunk_type == b"JSON":
            gltf = json.loads(
                bytes(output[chunk_data_offset : chunk_data_offset + chunk_length])
                .decode("utf-8")
                .rstrip()
            )
        elif chunk_type[:3] == b"BIN":
            binary_offset = chunk_data_offset
            binary_length = chunk_length
        offset = chunk_data_offset + chunk_length

    if gltf is None or binary_offset is None or binary_length is None:
        raise ValueError(f"{source} does not contain JSON and BIN chunks")

    adjusted_keys = 0
    adjusted_accessors: dict[int, list[tuple[float, float, float, float]]] = {}
    nodes = gltf["nodes"]
    for animation in gltf.get("animations", []):
        if animation.get("name") not in TARGET_CLIPS:
            continue
        samplers = animation["samplers"]
        for channel in animation["channels"]:
            target = channel["target"]
            if target.get("path") != "rotation":
                continue
            bone_name = nodes[target["node"]].get("name")
            if bone_name not in PITCH_OFFSETS_DEGREES:
                continue

            accessor_index = samplers[channel["sampler"]]["output"]
            accessor = gltf["accessors"][accessor_index]
            if accessor["componentType"] != 5126 or accessor["type"] != "VEC4":
                raise ValueError(f"Unexpected quaternion accessor for {bone_name}")
            view = gltf["bufferViews"][accessor["bufferView"]]
            first = (
                binary_offset
                + int(view.get("byteOffset", 0))
                + int(accessor.get("byteOffset", 0))
            )
            stride = int(view.get("byteStride", 16))
            half_angle = math.radians(PITCH_OFFSETS_DEGREES[bone_name]) * 0.5
            pitch = (0.0, math.sin(half_angle), 0.0, math.cos(half_angle))

            for index in range(int(accessor["count"])):
                key_offset = first + index * stride
                original = struct.unpack_from("<4f", output, key_offset)
                adjusted = normalize_quaternion(
                    multiply_quaternions(original, pitch)
                )
                struct.pack_into("<4f", output, key_offset, *adjusted)
                adjusted_accessors.setdefault(accessor_index, []).append(adjusted)
                adjusted_keys += 1

    if adjusted_keys == 0:
        raise ValueError("No matching head rotation keys were found")
    for accessor_index, values in adjusted_accessors.items():
        accessor = gltf["accessors"][accessor_index]
        accessor["min"] = [min(value[axis] for value in values) for axis in range(4)]
        accessor["max"] = [max(value[axis] for value in values) for axis in range(4)]

    json_chunk = json.dumps(gltf, separators=(",", ":")).encode("utf-8")
    json_chunk += b" " * ((-len(json_chunk)) % 4)
    binary_chunk = bytes(output[binary_offset : binary_offset + binary_length])
    binary_chunk += b"\0" * ((-len(binary_chunk)) % 4)
    rebuilt_length = 12 + 8 + len(json_chunk) + 8 + len(binary_chunk)
    rebuilt = bytearray(struct.pack("<4sII", b"glTF", 2, rebuilt_length))
    rebuilt.extend(struct.pack("<I4s", len(json_chunk), b"JSON"))
    rebuilt.extend(json_chunk)
    rebuilt.extend(struct.pack("<I4s", len(binary_chunk), b"BIN\0"))
    rebuilt.extend(binary_chunk)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(rebuilt)
    return adjusted_keys


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Tilt Goth Baddie's hands-on-knees animation toward the low camera."
    )
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    count = adjust_glb(args.source, args.destination)
    print(f"Adjusted {count} neck/head rotation keys: {args.destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
