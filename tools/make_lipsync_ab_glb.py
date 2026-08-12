#!/usr/bin/env python3
"""Duplicate one lipsync animation in a WolvenKit GLB and alter track curves."""

from __future__ import annotations

import argparse
import copy
import json
import re
import struct
from pathlib import Path
from typing import Any

GLB_MAGIC = b"glTF"
JSON_CHUNK = 0x4E4F534A


def read_glb(path: Path) -> tuple[dict[str, Any], list[tuple[int, bytes]]]:
    payload = path.read_bytes()
    magic, version, declared_length = struct.unpack_from("<4sII", payload, 0)
    if magic != GLB_MAGIC or version != 2 or declared_length != len(payload):
        raise ValueError(f"{path} is not a valid glTF 2.0 binary")

    chunks: list[tuple[int, bytes]] = []
    offset = 12
    document: dict[str, Any] | None = None
    while offset < len(payload):
        length, chunk_type = struct.unpack_from("<II", payload, offset)
        offset += 8
        chunk = payload[offset : offset + length]
        offset += length
        if chunk_type == JSON_CHUNK:
            document = json.loads(chunk.decode("utf-8").rstrip(" \t\r\n\0"))
        else:
            chunks.append((chunk_type, chunk))
    if document is None:
        raise ValueError(f"{path} has no JSON chunk")
    return document, chunks


def write_glb(
    path: Path,
    document: dict[str, Any],
    chunks: list[tuple[int, bytes]],
) -> None:
    json_payload = json.dumps(
        document,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    json_payload += b" " * ((-len(json_payload)) % 4)
    encoded = [struct.pack("<II", len(json_payload), JSON_CHUNK) + json_payload]
    for chunk_type, payload in chunks:
        padding = b"\0" * ((-len(payload)) % 4)
        encoded.append(
            struct.pack("<II", len(payload) + len(padding), chunk_type)
            + payload
            + padding
        )
    body = b"".join(encoded)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(struct.pack("<4sII", GLB_MAGIC, 2, 12 + len(body)) + body)


def track_names(document: dict[str, Any]) -> list[str]:
    skins = document.get("skins", [])
    if not skins:
        raise ValueError("GLB has no skin carrying WolvenKit rig extras")
    names = skins[0].get("extras", {}).get("trackNames")
    if not isinstance(names, list) or not all(isinstance(name, str) for name in names):
        raise ValueError("GLB skin extras have no trackNames array")
    return names


def duplicate_animation(
    document: dict[str, Any],
    source_name: str,
    output_name: str,
    track_pattern: str | None,
    value: float,
) -> tuple[int, int]:
    animations = document.get("animations", [])
    if any(animation.get("name") == output_name for animation in animations):
        raise ValueError(f"Animation already exists: {output_name}")
    source = next(
        (animation for animation in animations if animation.get("name") == source_name),
        None,
    )
    if source is None:
        raise ValueError(f"Source animation not found: {source_name}")

    selected: set[int] = set()
    if track_pattern is not None:
        matcher = re.compile(track_pattern, re.IGNORECASE)
        selected = {
            index
            for index, name in enumerate(track_names(document))
            if matcher.search(name)
        }
        if not selected:
            raise ValueError(f"Track pattern matched no rig tracks: {track_pattern}")

    duplicate = copy.deepcopy(source)
    duplicate["name"] = output_name
    extras = duplicate.get("extras", {})
    changed = 0
    for field in ("trackKeys", "constTrackKeys"):
        for key in extras.get(field, []):
            if int(key.get("trackIndex", -1)) in selected:
                key["value"] = value
                changed += 1
    if track_pattern is not None and changed == 0:
        raise ValueError(
            f"Matched rig tracks {sorted(selected)} have no keys in {source_name}"
        )
    animations.append(duplicate)
    return len(selected), changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--source", required=True, help="Animation to duplicate")
    parser.add_argument("--name", required=True, help="Name of the duplicate")
    parser.add_argument(
        "--track",
        default=r"^jaliJaw$",
        help="Case-insensitive regular expression selecting rig track names",
    )
    parser.add_argument(
        "--copy-only",
        action="store_true",
        help="Duplicate and rename the animation without changing track keys",
    )
    parser.add_argument("--value", type=float, default=1.0)
    args = parser.parse_args()

    document, chunks = read_glb(args.input)
    selected, changed = duplicate_animation(
        document,
        args.source,
        args.name,
        None if args.copy_only else args.track,
        args.value,
    )
    write_glb(args.output, document, chunks)
    print(
        json.dumps(
            {
                "output": str(args.output),
                "animation": args.name,
                "selected_tracks": selected,
                "changed_keys": changed,
                "value": args.value,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
