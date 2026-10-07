"""WolvenKit GLB container and rig-track I/O."""

from __future__ import annotations
import json
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
