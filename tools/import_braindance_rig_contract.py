#!/usr/bin/env python3
"""Extract the animation-facing skeleton contract from a serialized RED rig.

This is a maintenance importer, not part of normal braindance generation.
Normal generation consumes the checked ``*.skeleton.json`` contract and does
not need WolvenKit or a vanilla game file.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def _cname(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, dict) and isinstance(value.get("$value"), str):
        return value["$value"]
    raise ValueError(f"Invalid rig bone name: {value!r}")


def _vector(value: dict[str, Any]) -> list[float]:
    return [
        float(value["X"]),
        float(value["Y"]),
        float(value["Z"]),
    ]


def _quaternion(value: dict[str, Any]) -> list[float]:
    return [
        float(value["i"]),
        float(value["j"]),
        float(value["k"]),
        float(value["r"]),
    ]


def _transform(value: dict[str, Any]) -> dict[str, list[float]]:
    return {
        "translation": _vector(value["Translation"]),
        "rotation": _quaternion(value["Rotation"]),
        "scale": _vector(value["Scale"]),
    }


def build_contract(document: dict[str, Any], source_sha256: str) -> dict[str, Any]:
    root = document["Data"]["RootChunk"]
    if root.get("$type") != "animRig":
        raise ValueError("Data.RootChunk must be an animRig")
    names = [_cname(value) for value in root["boneNames"]]
    parents = [int(value) for value in root["boneParentIndexes"]]
    local_rest = root["aPoseLS"]
    model_rest = root["aPoseMS"]
    count = len(names)
    if not (
        len(parents) == count
        and len(local_rest) == count
        and len(model_rest) == count
    ):
        raise ValueError("Rig bone arrays have inconsistent lengths")
    if len(set(names)) != count:
        raise ValueError("Rig bone names must be unique")
    bones: list[dict[str, Any]] = []
    for index, name in enumerate(names):
        parent = parents[index]
        if parent >= index or parent < -1:
            raise ValueError(
                f"Bone {index} {name!r} has invalid parent index {parent}"
            )
        model = _transform(model_rest[index])
        red_position = model["translation"]
        bones.append(
            {
                "index": index,
                "name": name,
                "parent": parent,
                "local_rest": _transform(local_rest[index]),
                "model_rest": model,
                # RED and Blender are both right-handed and Z-up, but the
                # character export convention maps RED (X,Y,Z) to
                # Blender (X,Z,-Y).
                "blender_model_position": [
                    red_position[0],
                    red_position[2],
                    -red_position[1],
                ],
            }
        )
    return {
        "schema_version": 1,
        "kind": "ghostline_braindance_skeleton",
        "name": Path(document.get("_source_name", "rig")).stem,
        "source_sha256": source_sha256,
        "bone_count": count,
        "trajectory_joint_index": (
            names.index("Trajectory") if "Trajectory" in names else None
        ),
        "bones": bones,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="WolvenKit serialized .rig.json")
    parser.add_argument("output", type=Path, help="Checked skeleton contract")
    parser.add_argument("--name", help="Override the contract name")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    raw = args.input.read_bytes()
    document = json.loads(raw)
    if not isinstance(document, dict):
        raise ValueError("Rig JSON root must be an object")
    document["_source_name"] = args.input.name.removesuffix(".json")
    contract = build_contract(document, hashlib.sha256(raw).hexdigest())
    if args.name:
        contract["name"] = args.name
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(contract, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output": str(args.output),
                "name": contract["name"],
                "bone_count": contract["bone_count"],
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
