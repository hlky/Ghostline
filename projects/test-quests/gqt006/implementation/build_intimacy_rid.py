#!/usr/bin/env python3
"""Build GQT006's 20-second, female-V FPP bottom-role RID."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any


ROOT = next(
    parent
    for parent in Path(__file__).resolve().parents
    if (parent / "AGENTS.md").is_file()
)
PROJECT = next(parent for parent in Path(__file__).resolve().parents if (parent / "project.json").is_file())
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from braindance_rid import RID_KIND, compile_binary
from sex_rid_preview import decode_compressed_buffer, decode_simd_buffer


SOURCE_JSON = ROOT / ".tmp/vanilla-sex-rids-json/sex_13_2s_f.scenerid.json"
SOURCE_BINARY = (
    ROOT
    / ".tmp/vanilla-sex-rids/base/animations/quest/lore/generic_sex/intercourse"
    / "sex_13_2s_f.scenerid"
)
LAYOUT_BINARY = (
    ROOT
    / ".tmp/vanilla-sex-rids/base/animations/quest/lore/generic_sex/exclusive_intros"
    / "exclusive_intro_01_a.scenerid"
)
LAYOUT_JSON = ROOT / ".tmp/vanilla-sex-rids-json/exclusive_intro_01_a.scenerid.json"
LAYOUT_WITH_MOTION = PROJECT / ".tmp/gqt006-intimacy/sex-rid-layout.scenerid.json"
MOTION_TEMPLATE = ROOT / "projects/test-quests/gqt005/.tmp/braindance/gqt005/gqt005_braindance_analysis.scenerid.json"
WOMAN_RIG = ROOT / ".tmp/rid-binding-rigs3/woman_base.rig.json"
PLAYER_WOMAN_RIG = ROOT / ".tmp/rid-binding-rigs/player_woman_skeleton.rig.json"
PLAYER_MAN_RIG = ROOT / ".tmp/rid-binding-rigs2/player_man_skeleton.rig.json"
HANDOFF = PROJECT / ".tmp/gqt006-intimacy/gqt006_goth_doggy_20s.handoff.json"
OUTPUT = (
    PROJECT
    / "source/archive/mod/gqt006/animations/gqt006_goth_doggy_20s.scenerid"
)
RAW_OUTPUT = Path(f"{OUTPUT}.json").resolve().relative_to(
    (PROJECT / "source/archive").resolve()
)
RAW_OUTPUT = PROJECT / "source/raw" / RAW_OUTPUT
REPORT = PROJECT / ".tmp/gqt006-intimacy/gqt006_goth_doggy_20s.rid-report.json"

FPS = 30
SOURCE_FRAMES = 61
OUTPUT_FRAMES = 601
SEAM_START = 54


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def cname(value: Any) -> str | None:
    if isinstance(value, dict):
        value = value.get("$value")
    return value if isinstance(value, str) else None


def actor_by_signature(root: dict[str, Any], signature: str) -> dict[str, Any]:
    for actor in root["actors"]:
        if cname(actor.get("tag", {}).get("signature")) == signature:
            return actor
    raise ValueError(f"RID actor {signature!r} was not found")


def camera_by_signature(root: dict[str, Any], signature: str) -> dict[str, Any]:
    for camera in root["cameras"]:
        if cname(camera.get("tag", {}).get("signature")) == signature:
            return camera
    raise ValueError(f"RID camera {signature!r} was not found")


def decode_actor(actor: dict[str, Any]) -> Any:
    buffer = actor["animations"][0]["animation"]["Data"]["animBuffer"]["Data"]
    if buffer["$type"] == "animAnimationBufferSimd":
        return decode_simd_buffer(buffer)
    return decode_compressed_buffer(buffer)


def decode_camera(camera: dict[str, Any]) -> Any:
    buffer = camera["animations"][0]["animation"]["Data"]
    if buffer["$type"] == "animAnimationBufferSimd":
        return decode_simd_buffer(buffer)
    return decode_compressed_buffer(buffer)


def rig_names(path: Path) -> list[str]:
    root = load_json(path)["Data"]["RootChunk"]
    return [cname(value) or "" for value in root["boneNames"]]


def rig_contract(path: Path, name: str) -> dict[str, Any]:
    names = rig_names(path)
    return {
        "contract": str(path.relative_to(PROJECT)).replace("\\", "/"),
        "name": name,
        "contract_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "bone_count": len(names),
        "bone_order": names,
        "trajectory_joint_index": names.index("Trajectory"),
    }


def normalized_lerp(left: list[float], right: list[float], factor: float) -> list[float]:
    if sum(a * b for a, b in zip(left, right)) < 0.0:
        right = [-value for value in right]
    value = [a + (b - a) * factor for a, b in zip(left, right)]
    length = math.sqrt(sum(component * component for component in value))
    return [component / length for component in value]


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


def loop_value(rows: list[list[float]], output_frame: int, *, quaternion: bool) -> list[float]:
    local = output_frame % (SOURCE_FRAMES - 1)
    if output_frame == OUTPUT_FRAMES - 1:
        local = 0
    if local < SEAM_START:
        return list(rows[local])
    factor = (local - SEAM_START) / ((SOURCE_FRAMES - 1) - SEAM_START)
    if quaternion:
        return normalized_lerp(rows[SEAM_START], rows[0], factor)
    return [
        left + (right - left) * factor
        for left, right in zip(rows[SEAM_START], rows[0])
    ]


def retarget_samples(
    *,
    actor_id: str,
    source: Any,
    source_names: list[str],
    target_names: list[str],
    fallback: Any | None,
    fallback_names: list[str] | None,
    contract: dict[str, Any],
) -> dict[str, Any]:
    source_index = {name: index for index, name in enumerate(source_names)}
    fallback_index = {
        name: index for index, name in enumerate(fallback_names or [])
    }
    joints = []
    for target_index, name in enumerate(target_names):
        if name in source_index:
            source_animation = source
            source_joint = source_index[name]
        elif fallback is not None and name in fallback_index:
            source_animation = fallback
            source_joint = fallback_index[name]
        else:
            source_animation = None
            source_joint = -1
        translations = (
            [row[source_joint] for row in source_animation.translations]
            if source_animation is not None
            else [[0.0, 0.0, 0.0]] * SOURCE_FRAMES
        )
        rotations = (
            [row[source_joint] for row in source_animation.rotations]
            if source_animation is not None
            else [[0.0, 0.0, 0.0, 1.0]] * SOURCE_FRAMES
        )
        scales = (
            [row[source_joint] for row in source_animation.scales]
            if source_animation is not None
            else [[1.0, 1.0, 1.0]] * SOURCE_FRAMES
        )
        joints.append(
            {
                "index": target_index,
                "name": name,
                "samples": [
                    {
                        "frame": frame,
                        "translation": loop_value(
                            translations, frame, quaternion=False
                        ),
                        "rotation": loop_value(rotations, frame, quaternion=True),
                        "scale": loop_value(scales, frame, quaternion=False),
                    }
                    for frame in range(OUTPUT_FRAMES)
                ],
            }
        )
    trajectory = next(joint for joint in joints if joint["name"] == "Trajectory")
    reference = next(joint for joint in joints if joint["name"] == "reference_joint")
    reference["samples"] = copy.deepcopy(trajectory["samples"])
    return {
        "id": actor_id,
        "armature": f"ARMATURE_{actor_id}",
        "bone_order": target_names,
        "bone_count": len(target_names),
        "rig_contract_sha256": contract["contract_sha256"],
        "trajectory_joint_index": contract["trajectory_joint_index"],
        "joints": joints,
        "facial": None,
        "cyberware": None,
    }


def actor_spec(actor_id: str, signature: str, rig: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": actor_id,
        "actor_id": 0,
        "performer_id": 1,
        "display_name": actor_id,
        "rid_signature": signature,
        "root_object": f"ACTOR_{actor_id}",
        "asset": {"path": "braindance/rigs/man_base.glb"},
        "rig": rig,
        "body_animation": {"type": "retargeted_vanilla_sex_09"},
        "facial": None,
        "cyberware": None,
        "transform_keys": [
            {"frame": 0, "location": [0.0, 0.0, 0.0], "rotation_degrees": [0.0, 0.0, 0.0]},
            {"frame": OUTPUT_FRAMES - 1, "location": [0.0, 0.0, 0.0], "rotation_degrees": [0.0, 0.0, 0.0]},
        ],
        "interpolation": "LINEAR",
    }


def build_handoff() -> dict[str, Any]:
    source_document = load_json(SOURCE_JSON)
    root = source_document["Data"]["RootChunk"]
    female_average = decode_actor(actor_by_signature(root, "female_average"))
    female_player = decode_actor(actor_by_signature(root, "femalePlayerFpp"))
    player = decode_actor(actor_by_signature(root, "player"))
    camera = decode_camera(camera_by_signature(root, "Camera"))
    woman_names = rig_names(WOMAN_RIG)
    player_names = rig_names(PLAYER_WOMAN_RIG)
    if player_names != rig_names(PLAYER_MAN_RIG):
        raise ValueError("Male and female player skeleton orders differ")
    woman_contract = rig_contract(WOMAN_RIG, "woman_base")
    player_contract = rig_contract(PLAYER_WOMAN_RIG, "player")
    actors = [
        actor_spec("goth", "goth_average", woman_contract),
        actor_spec("male_v", "male_v", player_contract),
        actor_spec("female_v", "female_v", player_contract),
    ]
    inverse_camera_basis = (math.sqrt(0.5), 0.0, 0.0, math.sqrt(0.5))
    camera_translations = [row[0] for row in camera.translations]
    camera_rotations = [row[0] for row in camera.rotations]
    camera_focal_lengths = [row[1] for row in camera.tracks]
    camera_samples = [
        {
            "frame": frame,
            "translation": loop_value(
                camera_translations, frame, quaternion=False
            ),
            "rotation": list(
                multiply_quaternions(
                    loop_value(camera_rotations, frame, quaternion=True),
                    inverse_camera_basis,
                )
            ),
            "scale": [1.0, 1.0, 1.0],
            "focal_length": loop_value(
                [[value] for value in camera_focal_lengths],
                frame,
                quaternion=False,
            )[0],
        }
        for frame in range(OUTPUT_FRAMES)
    ]
    sample_actors = [
        retarget_samples(
            actor_id="goth",
            source=female_average,
            source_names=woman_names,
            target_names=woman_names,
            fallback=None,
            fallback_names=None,
            contract=woman_contract,
        ),
        retarget_samples(
            actor_id="male_v",
            source=player,
            source_names=player_names,
            target_names=player_names,
            fallback=None,
            fallback_names=None,
            contract=player_contract,
        ),
        retarget_samples(
            actor_id="female_v",
            source=female_player,
            source_names=player_names,
            target_names=player_names,
            fallback=None,
            fallback_names=None,
            contract=player_contract,
        ),
    ]
    return {
        "schema_version": 1,
        "kind": RID_KIND,
        "name": "gqt006_goth_doggy_20s",
        "source_spec": str(SOURCE_JSON.relative_to(PROJECT)).replace("\\", "/"),
        "source_sha256": hashlib.sha256(SOURCE_JSON.read_bytes()).hexdigest(),
        "fps": FPS,
        "frames": {"start": 0, "end": OUTPUT_FRAMES - 1},
        "origin": {"location": [0.0, 0.0, 0.0], "rotation_degrees": [0.0, 0.0, 0.0]},
        "actors": actors,
        "recording_camera": {
            "id": "sex_13_f_camera",
            "rid_signature": "Camera",
            "keys": [
                {
                    "frame": 0,
                    "location": camera_samples[0]["translation"],
                    "rotation_quaternion": camera_samples[0]["rotation"],
                    "focal_length": camera_samples[0]["focal_length"],
                },
                {
                    "frame": OUTPUT_FRAMES - 1,
                    "location": camera_samples[-1]["translation"],
                    "rotation_quaternion": camera_samples[-1]["rotation"],
                    "focal_length": camera_samples[-1]["focal_length"],
                },
            ],
        },
        "clues": [],
        "markers": [],
        "rid_status": "authored",
        "animation_samples": {
            "schema_version": 1,
            "coordinate_space": "blender_local_z_up_right_handed",
            "frame_start": 0,
            "frame_end": OUTPUT_FRAMES - 1,
            "sample_rate": FPS,
            "actors": sample_actors,
            "camera": {"id": "sex_13_f_camera", "samples": camera_samples},
        },
    }


def prepare_layout() -> None:
    layout = load_json(LAYOUT_JSON)
    donor = load_json(MOTION_TEMPLATE)
    donor_motion = donor["Data"]["RootChunk"]["actors"][0]["animations"][0][
        "animation"
    ]["Data"]["motionExtraction"]
    donor_camera = donor["Data"]["RootChunk"]["cameras"][0]
    for index, actor in enumerate(layout["Data"]["RootChunk"]["actors"]):
        if not actor.get("animations"):
            continue
        motion = copy.deepcopy(donor_motion)
        motion["HandleId"] = str(9000 + index)
        actor["animations"][0]["animation"]["Data"]["motionExtraction"] = motion
    layout["Data"]["RootChunk"]["cameras"] = [copy.deepcopy(donor_camera)]
    LAYOUT_WITH_MOTION.parent.mkdir(parents=True, exist_ok=True)
    LAYOUT_WITH_MOTION.write_text(
        json.dumps(layout, indent=2) + "\n", encoding="utf-8"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--wolvenkit", type=Path)
    args = parser.parse_args()
    for path in (
        SOURCE_JSON,
        SOURCE_BINARY,
        LAYOUT_BINARY,
        LAYOUT_JSON,
        MOTION_TEMPLATE,
        WOMAN_RIG,
        PLAYER_WOMAN_RIG,
        PLAYER_MAN_RIG,
    ):
        if not path.is_file():
            raise FileNotFoundError(path)
    handoff = build_handoff()
    HANDOFF.parent.mkdir(parents=True, exist_ok=True)
    HANDOFF.write_text(json.dumps(handoff, indent=2) + "\n", encoding="utf-8")
    prepare_layout()
    compile_binary(
        HANDOFF,
        LAYOUT_WITH_MOTION,
        OUTPUT,
        wolvenkit_path=args.wolvenkit,
        actor_template_signatures=[
            "female_average",
            "player",
            "player",
        ],
        json_output_path=RAW_OUTPUT,
        report_path=REPORT,
    )
    print(OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
