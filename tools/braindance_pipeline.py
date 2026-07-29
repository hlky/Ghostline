#!/usr/bin/env python3
"""Link, audit, package, and record runtime evidence for authored braindances."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import shutil
import subprocess
import sys
import tempfile
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
WOLVENKIT_CLI = (
    ROOT
    / "WolvenKit"
    / "WolvenKit.CLI"
    / "bin"
    / "Release"
    / "net8.0"
    / "WolvenKit.CLI.exe"
)
RUNTIME_CASES = (
    "seek_forward",
    "rewind_backward",
    "switch_visual_layer",
    "switch_audio_layer",
    "switch_thermal_layer",
    "normal_exit_cleanup",
    "interrupted_cleanup",
    "replay_after_cleanup",
)


class BraindancePipelineError(RuntimeError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise BraindancePipelineError(f"Cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise BraindancePipelineError(f"JSON root must be an object: {path}")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def find_wolvenkit(explicit: Path | None = None) -> Path:
    candidates = [explicit, WOLVENKIT_CLI]
    discovered = shutil.which("WolvenKit.CLI")
    if discovered:
        candidates.append(Path(discovered))
    for candidate in candidates:
        if candidate is not None and candidate.is_file():
            return candidate.resolve()
    raise BraindancePipelineError(
        "WolvenKit.CLI.exe was not found; pass --wolvenkit"
    )


def deserialize_cr2w_json(
    json_path: Path,
    binary_output: Path,
    *,
    wolvenkit: Path,
) -> dict[str, Any]:
    serialized_name = json_path.name.casefold()
    if (
        not serialized_name.endswith(".json")
        or "." not in serialized_name[:-5]
    ):
        raise BraindancePipelineError(
            "CR2W JSON input must retain its resource extension before .json"
        )
    with tempfile.TemporaryDirectory(prefix="ghostline-bd-cr2w-") as directory:
        staging = Path(directory)
        command = [
            str(wolvenkit),
            "cr2w",
            "--deserialize",
            "--path",
            str(json_path.resolve()),
            "--outpath",
            str(staging),
        ]
        completed = subprocess.run(
            command,
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        failed_output = (
            "[ 0: Error" in completed.stdout
            or "Could not convert" in completed.stdout
            or "Invalid output directory" in completed.stdout
        )
        if completed.returncode != 0 or failed_output:
            raise BraindancePipelineError(
                f"WolvenKit failed ({completed.returncode}): "
                f"{completed.stdout.strip()}"
            )
        expected_name = json_path.name[:-5]
        matches = list(staging.rglob(expected_name))
        if len(matches) != 1:
            raise BraindancePipelineError(
                f"WolvenKit did not produce exactly one {expected_name}"
            )
        binary_output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(matches[0], binary_output)
    if binary_output.read_bytes()[:4] != b"CR2W":
        raise BraindancePipelineError(
            f"Deserialized output is not CR2W: {binary_output}"
        )
    return {
        "binary_output": str(binary_output.resolve()),
        "bytes": binary_output.stat().st_size,
        "sha256": file_sha256(binary_output),
    }


def _root(document: dict[str, Any], expected_type: str) -> dict[str, Any]:
    data = document.get("Data")
    root = data.get("RootChunk") if isinstance(data, dict) else None
    if not isinstance(root, dict) or root.get("$type") != expected_type:
        raise BraindancePipelineError(
            f"Expected Data.RootChunk of type {expected_type}"
        )
    return root


def _serial(value: Any) -> int:
    if not isinstance(value, dict) or not isinstance(value.get("serialNumber"), int):
        raise BraindancePipelineError("RID record has no serial number")
    return int(value["serialNumber"])


def _tag_signature(record: dict[str, Any]) -> str:
    signature = record.get("tag", {}).get("signature", {}).get("$value")
    if not isinstance(signature, str):
        raise BraindancePipelineError("RID record has no tag signature")
    return signature


def _fnv1a32(text: str) -> int:
    value = 0x811C9DC5
    for byte in text.casefold().encode("utf-8"):
        value ^= byte
        value = value * 0x01000193 & 0xFFFFFFFF
    return value or 1


def _walk(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from _walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk(child)


def build_rid_catalog(document: dict[str, Any]) -> dict[str, Any]:
    root = _root(document, "scnRidResource")
    actors: dict[str, dict[str, Any]] = {}
    for actor in root.get("actors", []):
        if not isinstance(actor, dict):
            continue
        signature = _tag_signature(actor)
        row: dict[str, Any] = {"actor_serial": _serial(actor["tag"]["serialNumber"])}
        for channel, field in (
            ("body", "animations"),
            ("facial", "facialAnimations"),
            ("cyberware", "cyberwareAnimations"),
        ):
            clips = actor.get(field, [])
            if not isinstance(clips, list) or len(clips) > 1:
                raise BraindancePipelineError(
                    f"RID actor {signature!r} must have zero or one {channel} clip"
                )
            if clips:
                clip_row = {
                    "signature": _tag_signature(clips[0]),
                    "serial": _serial(clips[0]["tag"]["serialNumber"]),
                }
                if channel == "body":
                    clip_row["offset"] = copy.deepcopy(clips[0].get("offset"))
                    clip_row["motion_extracted"] = clips[0].get(
                        "motionExtracted"
                    )
                    clip_row["trajectory_joint_index"] = clips[0].get(
                        "trajectoryBoneIndex"
                    )
                row[channel] = clip_row
            else:
                row[channel] = None
        actors[signature] = row
    cameras = root.get("cameras", [])
    if not isinstance(cameras, list) or len(cameras) != 1:
        raise BraindancePipelineError("RID must contain exactly one camera")
    camera_clips = cameras[0].get("animations", [])
    if not isinstance(camera_clips, list) or len(camera_clips) != 1:
        raise BraindancePipelineError("RID camera must contain exactly one clip")
    return {
        "actors": actors,
        "camera": {
            "signature": _tag_signature(camera_clips[0]),
            "serial": _serial(camera_clips[0]["tag"]["serialNumber"]),
        },
    }


def _rid_animation_ref(serial: int, resource_id: int) -> dict[str, Any]:
    return {
        "$type": "scnRidAnimationSRRef",
        "animationSN": {
            "$type": "scnRidSerialNumber",
            "serialNumber": serial,
        },
        "resourceId": {"$type": "scnRidResourceId", "id": resource_id},
    }


def _rid_set_ref(animation_index: int) -> dict[str, Any]:
    return {
        "$type": "scnRidAnimSetSRRef",
        "animations": [{"$type": "scnSRRefId", "id": animation_index}],
    }


def _camera_ref(serial: int, resource_id: int) -> dict[str, Any]:
    return {
        "$type": "scnRidCameraAnimationSRRef",
        "animationSN": {
            "$type": "scnRidSerialNumber",
            "serialNumber": serial,
        },
        "resourceId": {"$type": "scnRidResourceId", "id": resource_id},
    }


def _set_reference_anim_name(event: dict[str, Any], set_index: int) -> None:
    anim_name = event.get("animName")
    data = anim_name.get("Data") if isinstance(anim_name, dict) else None
    if not isinstance(data, dict):
        raise BraindancePipelineError("scnPlaySkAnimEvent has no animName.Data")
    data["type"] = "reference"
    data["unk1"] = []
    data["unk2"] = [set_index, 0]


def _retarget_scene_markers(root: dict[str, Any], node_ref: str) -> None:
    for value in _walk(root):
        if value.get("$type") != "scnMarker":
            continue
        marker = value.get("nodeRef")
        if isinstance(marker, dict):
            marker["$storage"] = "string"
            marker["$value"] = node_ref


def _actor_root_motion_trajectory(
    handoff: dict[str, Any],
    actor_id: str,
) -> list[dict[str, Any]]:
    samples = handoff.get("animation_samples")
    actors = samples.get("actors") if isinstance(samples, dict) else None
    if not isinstance(actors, list):
        raise BraindancePipelineError(
            "Handoff has no sampled actor animation data"
        )
    sampled_actor = next(
        (
            actor
            for actor in actors
            if isinstance(actor, dict) and str(actor.get("id")) == actor_id
        ),
        None,
    )
    if sampled_actor is None:
        raise BraindancePipelineError(
            f"Handoff has no sampled root motion for actor {actor_id!r}"
        )
    trajectory_index = sampled_actor.get("trajectory_joint_index")
    joint = next(
        (
            value
            for value in sampled_actor.get("joints", [])
            if value.get("index") == trajectory_index
        ),
        None,
    )
    rows = joint.get("samples") if isinstance(joint, dict) else None
    if not isinstance(rows, list) or len(rows) < 2:
        raise BraindancePipelineError(
            f"Actor {actor_id!r} has no sampled trajectory joint"
        )
    frame_start = int(samples["frame_start"])
    frame_end = int(samples["frame_end"])
    sample_rate = float(samples["sample_rate"])
    duration = (frame_end - frame_start) / sample_rate
    checkpoint_count = max(2, math.ceil(duration) + 1)
    row_indices = sorted(
        {
            round(index * (len(rows) - 1) / (checkpoint_count - 1))
            for index in range(checkpoint_count)
        }
    )
    result: list[dict[str, Any]] = []
    for row_index in row_indices:
        row = rows[row_index]
        rotation = [float(value) for value in row["rotation"]]
        translation = [float(value) for value in row["translation"]]
        result.append(
            {
                "$type": "scnAnimationMotionSample",
                "time": (
                    int(row["frame"]) - frame_start
                )
                / sample_rate,
                "transform": {
                    "$type": "Transform",
                    "orientation": {
                        "$type": "Quaternion",
                        "i": rotation[0],
                        "j": rotation[1],
                        "k": rotation[2],
                        "r": rotation[3],
                    },
                    "position": {
                        "$type": "Vector4",
                        "W": 0.0,
                        "X": translation[0],
                        "Y": translation[1],
                        "Z": translation[2],
                    },
                },
            }
        )
    return result


def _synchronize_root_motion(
    event: dict[str, Any],
    *,
    actor: dict[str, Any],
    rid_body: dict[str, Any],
    handoff: dict[str, Any],
) -> None:
    if rid_body.get("motion_extracted") != 1:
        raise BraindancePipelineError(
            f"RID actor {actor['id']!r} does not expose extracted root motion"
        )
    offset = rid_body.get("offset")
    if not isinstance(offset, dict):
        raise BraindancePipelineError(
            f"RID actor {actor['id']!r} has no body offset"
        )
    root_motion = event.get("rootMotionData")
    if not isinstance(root_motion, dict):
        raise BraindancePipelineError(
            f"Body event for actor {actor['id']!r} has no rootMotionData"
        )
    root_motion["enabled"] = 1
    root_motion["originOffset"] = copy.deepcopy(offset)
    root_motion["trajectoryLOD"] = _actor_root_motion_trajectory(
        handoff,
        str(actor["id"]),
    )


class _SceneHandleAllocator:
    def __init__(self, root: dict[str, Any]) -> None:
        handle_ids = [
            int(item["HandleId"])
            for item in _walk(root)
            if isinstance(item.get("HandleId"), str)
            and item["HandleId"].isdigit()
        ]
        self._next = max(handle_ids, default=0) + 1

    def wrap(self, data: dict[str, Any]) -> dict[str, Any]:
        handle = {"HandleId": str(self._next), "Data": data}
        self._next += 1
        return handle


def _cname(value: str) -> dict[str, Any]:
    return {
        "$type": "CName",
        "$storage": "string",
        "$value": value,
    }


def _dynamic_entity_reference(dynamic_name: str) -> dict[str, Any]:
    return {
        "$type": "gameEntityReference",
        "dynamicEntityUniqueName": _cname(dynamic_name),
        "names": [],
        "reference": {
            "$type": "NodeRef",
            "$storage": "uint64",
            "$value": "0",
        },
        "sceneActorContextName": _cname("None"),
        "slotName": _cname("None"),
        "type": "EntityRef",
    }


def _actor_entity_reference(
    node_ref: str,
    entry_name: str,
) -> dict[str, Any]:
    return {
        "$type": "gameEntityReference",
        "dynamicEntityUniqueName": _cname("None"),
        "names": [_cname(entry_name)],
        "reference": {
            "$type": "NodeRef",
            "$storage": "string",
            "$value": node_ref,
        },
        "sceneActorContextName": _cname("None"),
        "slotName": _cname("None"),
        "type": "EntityRef",
    }


def _add_scene_spawn_set_actors(
    root: dict[str, Any],
    definitions: Iterable[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Add scene-only spawn-set actors without creating RID bindings."""

    requested = list(definitions)
    if not requested:
        return []

    scene_actors = root.get("actors")
    if not isinstance(scene_actors, list) or not scene_actors:
        raise BraindancePipelineError(
            "Scene spawn-set actors require an existing actor definition"
        )
    player_actors = root.get("playerActors", [])
    if not isinstance(player_actors, list):
        raise BraindancePipelineError("Scene playerActors must be an array")

    existing_definitions = [*scene_actors, *player_actors]
    actor_ids = [
        actor.get("actorId", {}).get("id")
        for actor in existing_definitions
        if isinstance(actor, dict)
    ]
    if (
        len(actor_ids) != len(existing_definitions)
        or not all(isinstance(actor_id, int) for actor_id in actor_ids)
        or sorted(actor_ids) != list(range(len(actor_ids)))
    ):
        raise BraindancePipelineError(
            "Scene spawn-set actors require dense existing actor IDs"
        )
    scene_actor_ids = [
        actor["actorId"]["id"]
        for actor in scene_actors
    ]
    player_actor_ids = [
        actor["actorId"]["id"]
        for actor in player_actors
    ]
    insertion_id = len(scene_actors)
    if (
        sorted(scene_actor_ids) != list(range(insertion_id))
        or sorted(player_actor_ids)
        != list(range(insertion_id, len(existing_definitions)))
    ):
        raise BraindancePipelineError(
            "Scene spawn-set actors require player actor IDs after "
            "non-player actor IDs"
        )

    player_id_remap = {
        actor_id: actor_id + len(requested)
        for actor_id in player_actor_ids
    }
    performer_id_remap = {
        1 + (actor_id << 8): 1 + (new_actor_id << 8)
        for actor_id, new_actor_id in player_id_remap.items()
    }
    for value in _walk(root):
        if value.get("$type") == "scnActorId":
            actor_id = value.get("id")
            if actor_id in player_id_remap:
                value["id"] = player_id_remap[actor_id]
        elif value.get("$type") == "scnPerformerId":
            performer_id = value.get("id")
            if performer_id in performer_id_remap:
                value["id"] = performer_id_remap[performer_id]

    actor_names = {
        str(actor.get("actorName", actor.get("playerName", "")))
        for actor in existing_definitions
        if isinstance(actor, dict)
    }

    base_actor = scene_actors[0]
    rewindable_sections = [
        value
        for value in _walk(root.get("sceneGraph"))
        if value.get("$type") == "scnRewindableSectionNode"
    ]
    if not rewindable_sections:
        raise BraindancePipelineError(
            "Scene spawn-set actors require a rewindable section"
        )
    debug_symbols = root.setdefault("debugSymbols", {})
    if not isinstance(debug_symbols, dict):
        raise BraindancePipelineError("Scene debugSymbols must be an object")
    performer_symbols = debug_symbols.setdefault(
        "performersDebugSymbols",
        [],
    )
    if not isinstance(performer_symbols, list):
        raise BraindancePipelineError(
            "Scene performersDebugSymbols must be an array"
        )

    reports: list[dict[str, Any]] = []
    animation_fields = (
        "animSets",
        "bodyCinematicAnimSets",
        "cyberwareAnimSets",
        "cyberwareCinematicAnimSets",
        "deformationAnimSets",
        "dynamicAnimSets",
        "facialAnimSets",
        "facialCinematicAnimSets",
    )
    for definition_index, definition in enumerate(requested):
        if not isinstance(definition, dict):
            raise BraindancePipelineError(
                "Scene spawn-set actor definition must be an object"
            )
        actor_name = definition.get("actor_name")
        entry_name = definition.get("entry_name")
        spawn_set_ref = definition.get("spawn_set_ref")
        if not all(
            isinstance(value, str) and value
            for value in (actor_name, entry_name, spawn_set_ref)
        ):
            raise BraindancePipelineError(
                "Scene spawn-set actor requires actor_name, entry_name, "
                "and spawn_set_ref"
            )
        assert isinstance(actor_name, str)
        assert isinstance(entry_name, str)
        assert isinstance(spawn_set_ref, str)
        if actor_name in actor_names:
            raise BraindancePipelineError(
                f"Scene already defines actor {actor_name!r}"
            )

        actor_id = insertion_id + definition_index
        performer_id = 1 + (actor_id << 8)
        actor = copy.deepcopy(base_actor)
        actor["acquisitionPlan"] = "spawnSet"
        actor["actorId"] = {
            "$type": "scnActorId",
            "id": actor_id,
        }
        actor["actorName"] = actor_name
        for field in animation_fields:
            actor[field] = []
        actor["communityParams"] = {
            "$type": "scnCommunityParams",
            "entryName": _cname("None"),
            "forceMaxVisibility": 0,
            "reference": {
                "$type": "NodeRef",
                "$storage": "uint64",
                "$value": "0",
            },
        }
        actor["spawnSetParams"] = {
            "$type": "scnSpawnSetParams",
            "entryName": _cname(entry_name),
            "forceMaxVisibility": 0,
            "reference": {
                "$type": "NodeRef",
                "$storage": "string",
                "$value": spawn_set_ref,
            },
        }
        lipsync = actor.get("lipsyncAnimSet")
        if isinstance(lipsync, dict):
            lipsync["id"] = 0xFFFFFFFF
        scene_actors.append(actor)

        section_ids: list[int] = []
        for section in rewindable_sections:
            behaviors = section.setdefault("actorBehaviors", [])
            if not isinstance(behaviors, list):
                raise BraindancePipelineError(
                    "Rewindable actorBehaviors must be an array"
                )
            if not any(
                behavior.get("actorId", {}).get("id") == actor_id
                for behavior in behaviors
                if isinstance(behavior, dict)
            ):
                behaviors.append(
                    {
                        "$type": "scnSectionInternalsActorBehavior",
                        "actorId": {
                            "$type": "scnActorId",
                            "id": actor_id,
                        },
                        "behaviorMode": "OnlyIfAlive",
                    }
                )
            node_id = section.get("nodeId", {}).get("id")
            if isinstance(node_id, int):
                section_ids.append(node_id)

        performer_symbols.append(
            {
                "$type": "scnPerformerSymbol",
                "editorPerformerId": _deterministic_scene_event_id(
                    "scene-spawn-set-actor",
                    actor_name,
                    actor_id,
                    entry_name,
                    spawn_set_ref,
                ),
                "entityRef": _actor_entity_reference(
                    spawn_set_ref,
                    entry_name,
                ),
                "performerId": {
                    "$type": "scnPerformerId",
                    "id": performer_id,
                },
            }
        )
        actor_names.add(actor_name)
        reports.append(
            {
                "actor_name": actor_name,
                "actor_id": actor_id,
                "performer_id": performer_id,
                "spawn_set_ref": spawn_set_ref,
                "entry_name": entry_name,
                "rewindable_section_ids": section_ids,
            }
        )
    return reports


def _scene_input_socket(
    node_id: int,
    ordinal: int,
    *,
    name: int = 0,
) -> dict[str, Any]:
    return {
        "$type": "scnInputSocketId",
        "isockStamp": {
            "$type": "scnInputSocketStamp",
            "name": name,
            "ordinal": ordinal,
        },
        "nodeId": {"$type": "scnNodeId", "id": node_id},
    }


def _scene_output_socket(
    destinations: list[tuple[int, int]],
    *,
    name: int = 0,
) -> dict[str, Any]:
    return {
        "$type": "scnOutputSocket",
        "destinations": [
            _scene_input_socket(node_id, ordinal)
            for node_id, ordinal in destinations
        ],
        "stamp": {
            "$type": "scnOutputSocketStamp",
            "name": name,
            "ordinal": 0,
        },
    }


def _quest_socket(
    allocator: _SceneHandleAllocator,
    name: str,
    socket_type: str,
) -> dict[str, Any]:
    return allocator.wrap(
        {
            "$type": "questSocketDefinition",
            "connections": [],
            "name": _cname(name),
            "type": socket_type,
        }
    )


def _scene_quest_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    quest_data: dict[str, Any],
    destination: tuple[int, int] | None,
) -> dict[str, Any]:
    quest_data["id"] = node_id
    quest_data["sockets"] = [
        _quest_socket(allocator, "CutDestination", "CutDestination"),
        _quest_socket(allocator, "In", "Input"),
        _quest_socket(allocator, "Out", "Output"),
    ]
    return allocator.wrap(
        {
            "$type": "scnQuestNode",
            "ffStrategy": "automatic",
            "isockMappings": [
                _cname("CutDestination"),
                _cname("In"),
            ],
            "nodeId": {"$type": "scnNodeId", "id": node_id},
            "osockMappings": [_cname("Out")],
            "outputSockets": [
                _scene_output_socket(
                    [destination] if destination is not None else []
                )
            ],
            "questNode": allocator.wrap(quest_data),
        }
    )


def _clue_scan_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    target: str,
    destination: tuple[int, int],
) -> dict[str, Any]:
    scan_type = allocator.wrap(
        {
            "$type": "questScan_ConditionType",
            "eventType": "Finished",
            "objectRef": _dynamic_entity_reference(target),
        }
    )
    condition = allocator.wrap(
        {
            "$type": "questObjectCondition",
            "type": scan_type,
        }
    )
    return _scene_quest_node(
        allocator,
        node_id=node_id,
        quest_data={
            "$type": "questPauseConditionNodeDefinition",
            "condition": condition,
        },
        destination=destination,
    )


def _clue_inspected_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    target: str,
    destination: tuple[int, int] | None,
) -> dict[str, Any]:
    return _clue_focus_state_node(
        allocator,
        node_id=node_id,
        target=target,
        investigation_state="INSPECTED",
        destination=destination,
    )


def _clue_focus_state_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    target: str,
    investigation_state: str,
    destination: tuple[int, int] | None,
) -> dict[str, Any]:
    return _scene_quest_node(
        allocator,
        node_id=node_id,
        quest_data={
            "$type": "questEventManagerNodeDefinition",
            "componentName": _cname("scanning"),
            "event": allocator.wrap(
                {
                    "$type": "ToggleFocusClueEvent",
                    "clueIndex": 0,
                    "investigationState": investigation_state,
                    "isEnabled": 1,
                    "updatePS": 1,
                }
            ),
            "isObjectPlayer": 0,
            "isUiEvent": 0,
            "managerName": "FocusClueManager",
            "objectRef": _dynamic_entity_reference(target),
            "PSClassName": _cname("gameScanningComponentPS"),
        },
        destination=destination,
    )


def _clue_discovered_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    clue_name: str,
    destination: tuple[int, int],
) -> dict[str, Any]:
    return _scene_quest_node(
        allocator,
        node_id=node_id,
        quest_data={
            "$type": "questUIManagerNodeDefinition",
            "type": allocator.wrap(
                {
                    "$type": "questDiscoverBraindanceClue_NodeType",
                    "clueName": _cname(clue_name),
                }
            ),
        },
        destination=destination,
    )


def _clue_fact_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    fact_name: str,
    destination: tuple[int, int] | None = None,
) -> dict[str, Any]:
    return _scene_quest_node(
        allocator,
        node_id=node_id,
        quest_data={
            "$type": "questFactsDBManagerNodeDefinition",
            "type": allocator.wrap(
                {
                    "$type": "questSetVar_NodeType",
                    "factName": fact_name,
                    "setExactValue": 1,
                    "value": 1,
                }
            ),
        },
        destination=destination,
    )


def _clue_contract_node_ids(
    index: int,
) -> tuple[int, int, int, int, int, int, int, int, int]:
    base = 6000 + index * 10
    return (
        base + 1,
        base + 2,
        base + 3,
        base + 4,
        base + 5,
        base + 6,
        base + 7,
        base + 8,
        base + 9,
    )


def _clue_contract_aux_node_ids(
    index: int,
) -> tuple[int, int, int, int, int, int]:
    """IDs for the vanilla completion and scan-enable lifecycle."""

    base = 6500 + index * 10
    return (
        base + 1,
        base + 2,
        base + 3,
        base + 4,
        base + 5,
        base + 6,
    )


_BRAINDANCE_LAYER_UNLOCKS = {
    "Audio": (6091, "braindaneAudioLayerAvailable"),
    "Thermal": (6092, "braindaneThermalLayerAvailable"),
}


def _clue_availability_fact(clue: dict[str, Any]) -> str:
    completion_fact = str(clue["fact"])
    stem = (
        completion_fact[: -len("_found")]
        if completion_fact.endswith("_found")
        else completion_fact
    )
    return f"{stem}_clue_on"


def _clue_validity_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    availability_fact: str,
    layer: str,
    scene_depot_path: str,
    destinations: list[tuple[int, int]],
) -> dict[str, Any]:
    fact_condition = allocator.wrap(
        {
            "$type": "questFactsDBCondition",
            "type": allocator.wrap(
                {
                    "$type": "questVarComparison_ConditionType",
                    "comparisonType": "Greater",
                    "factName": availability_fact,
                    "value": 0,
                }
            ),
        }
    )
    layer_condition = allocator.wrap(
        {
            "$type": "questSceneCondition",
            "type": allocator.wrap(
                {
                    "$type": "scnBraindanceLayer_ConditionType",
                    "layer": layer,
                    "sceneFile": {
                        "DepotPath": {
                            "$type": "ResourcePath",
                            "$storage": "string",
                            "$value": scene_depot_path,
                        },
                        "Flags": "Soft",
                    },
                    "SceneVersion": "OlderOrEqual",
                }
            ),
        }
    )
    node = _scene_quest_node(
        allocator,
        node_id=node_id,
        quest_data={
            "$type": "questPauseConditionNodeDefinition",
            "condition": allocator.wrap(
                {
                    "$type": "questLogicalCondition",
                    "conditions": [
                        fact_condition,
                        layer_condition,
                    ],
                    "operation": "AND",
                }
            ),
        },
        destination=None,
    )
    node["Data"]["outputSockets"] = [
        _scene_output_socket(destinations)
    ]
    return node


def _deterministic_scene_event_id(*parts: object) -> str:
    digest = hashlib.sha256(
        ":".join(str(part) for part in parts).encode("utf-8")
    ).digest()
    value = int.from_bytes(digest[:8], "little")
    return str(value or 1)


def _configure_focus_clue_options(
    root: dict[str, Any],
    clue_ids: list[str],
) -> dict[str, int]:
    screenplay_store = root.get("screenplayStore")
    loc_store = root.get("locStore")
    if not isinstance(screenplay_store, dict) or not isinstance(
        screenplay_store.get("options"), list
    ):
        raise BraindancePipelineError(
            "Scene has no screenplay option store for focus clues"
        )
    if (
        not isinstance(loc_store, dict)
        or not isinstance(loc_store.get("vdEntries"), list)
        or not isinstance(loc_store.get("vpEntries"), list)
    ):
        raise BraindancePipelineError(
            "Scene has no embedded localization store for focus clues"
        )

    item_ids = {
        clue_id: 2 + index * 256
        for index, clue_id in enumerate(clue_ids)
    }
    loc_ids = {
        clue_id: _deterministic_scene_event_id(
            "ghostline",
            "focus-clue-option",
            clue_id,
        )
        for clue_id in clue_ids
    }
    owned_item_ids = set(item_ids.values())
    options = screenplay_store["options"]
    options[:] = [
        option
        for option in options
        if option.get("itemId", {}).get("id") not in owned_item_ids
    ]
    for clue_id in clue_ids:
        options.append(
            {
                "$type": "scnscreenplayChoiceOption",
                "itemId": {
                    "$type": "scnscreenplayItemId",
                    "id": item_ids[clue_id],
                },
                "locstringId": {
                    "$type": "scnlocLocstringId",
                    "ruid": loc_ids[clue_id],
                },
                "usage": {
                    "$type": "scnscreenplayOptionUsage",
                    "playerGenderMask": {
                        "$type": "scnGenderMask",
                        "mask": 3,
                    },
                },
            }
        )

    owned_loc_ids = set(loc_ids.values())
    descriptors = loc_store["vdEntries"]
    removed_variant_ids = {
        descriptor.get("variantId", {}).get("ruid")
        for descriptor in descriptors
        if descriptor.get("locstringId", {}).get("ruid")
        in owned_loc_ids
    }
    descriptors[:] = [
        descriptor
        for descriptor in descriptors
        if descriptor.get("locstringId", {}).get("ruid")
        not in owned_loc_ids
    ]
    payloads = loc_store["vpEntries"]
    payloads[:] = [
        payload
        for payload in payloads
        if payload.get("variantId", {}).get("ruid")
        not in removed_variant_ids
    ]

    localized_clue_ids = sorted(
        clue_ids,
        key=lambda clue_id: int(loc_ids[clue_id]),
    )
    for locale in ("db_db", "pl_pl", "en_us"):
        for clue_id in localized_clue_ids:
            variants = (
                (("", "blank"), ("Inspect clue", "source"))
                if locale == "db_db"
                else (("Inspect clue", "text"),)
            )
            for content, variant_kind in variants:
                variant_id = _deterministic_scene_event_id(
                    "ghostline",
                    "focus-clue-option",
                    clue_id,
                    locale,
                    variant_kind,
                )
                payload_index = len(payloads)
                payloads.append(
                    {
                        "$type":
                            "scnlocLocStoreEmbeddedVariantPayloadEntry",
                        "content": content,
                        "variantId": {
                            "$type": "scnlocVariantId",
                            "ruid": variant_id,
                        },
                    }
                )
                descriptors.append(
                    {
                        "$type":
                            "scnlocLocStoreEmbeddedVariantDescriptorEntry",
                        "localeId": locale,
                        "locstringId": {
                            "$type": "scnlocLocstringId",
                            "ruid": loc_ids[clue_id],
                        },
                        "signature": {
                            "$type": "scnlocSignature",
                            "val": "3",
                        },
                        "variantId": {
                            "$type": "scnlocVariantId",
                            "ruid": variant_id,
                        },
                        "vpeIndex": payload_index,
                    }
                )
    return item_ids


def _focus_clue_choice_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    clue_id: str,
    prop_id: int,
    screenplay_item_id: int,
    success_cut_id: int,
    visualizer_style: str = "inWorld",
    location_type: str = "Interaction",
    activation_range: float = 3,
    indication_range: float = 20,
    choice_group: str = "ghostline_bd_clues",
) -> dict[str, Any]:
    output_sockets = [_scene_output_socket([(success_cut_id, 0)])]
    output_sockets.extend(
        _scene_output_socket([], name=name)
        for name in range(1, 7)
    )
    return allocator.wrap(
        {
            "$type": "scnChoiceNode",
            "alwaysUseBrainGender": 0,
            "ataParams": {
                "$type": "scnChoiceNodeNsAttachToActorParams",
                "actorId": {
                    "$type": "scnActorId",
                    "id": 0xFFFFFFFF,
                },
                "visualizerStyle": "onScreen",
            },
            "atgoParams": {
                "$type": "scnChoiceNodeNsAttachToGameObjectParams",
                "nodeRef": {
                    "$type": "NodeRef",
                    "$storage": "uint64",
                    "$value": "0",
                },
                "visualizerStyle": "inWorld",
            },
            "atpParams": {
                "$type": "scnChoiceNodeNsAttachToPropParams",
                "propId": {
                    "$type": "scnPropId",
                    "id": prop_id,
                },
                "visualizerStyle": visualizer_style,
            },
            "atsParams": {
                "$type": "scnChoiceNodeNsAttachToScreenParams",
            },
            "atwParams": {
                "$type": "scnChoiceNodeNsAttachToWorldParams",
                "customEntityRadius": 0,
                "entityOrientation": {
                    "$type": "Quaternion",
                    "i": 0,
                    "j": 0,
                    "k": 0,
                    "r": 1,
                },
                "entityPosition": {
                    "$type": "Vector3",
                    "X": 0,
                    "Y": 0,
                    "Z": 0,
                },
                "visualizerStyle": "onScreen",
            },
            "choiceFlags": "IsFocusClue",
            "choiceGroup": _cname(choice_group),
            "choicePriority": 0,
            "cpoHoldInputActionSection": 0,
            "customPersistentLine": {
                "$type": "scnscreenplayItemId",
                "id": 4294967040,
            },
            "displayNameOverride": "",
            "doNotTurnOffPreventionSystem": 0,
            "ffStrategy": "automatic",
            "forceAttachToScreenCondition": None,
            "hubPriority": 0,
            "interruptCapability": "Interruptable",
            "interruptionSpeakerOverride": {
                "$type": "scnActorId",
                "id": 0xFFFFFFFF,
            },
            "localizedDisplayNameOverride": {
                "unk1": "0",
                "value": "",
            },
            "lookAtParams": allocator.wrap(
                {
                    "$type": "scnChoiceNodeNsBasicLookAtParams",
                    "offset": {
                        "$type": "Vector3",
                        "X": 0,
                        "Y": 0,
                        "Z": 0,
                    },
                    "slotName": _cname("(Root)"),
                }
            ),
            "mappinParams": allocator.wrap(
                {
                    "$type": "scnChoiceNodeNsMappinParams",
                    "locationType": location_type,
                    "mappinSettings": {
                        "$type": "TweakDBID",
                        "$storage": "string",
                        "$value":
                            "MappinUISettings.SceneDialogObjectSettings",
                    },
                }
            ),
            "mode": "attachToProp",
            "nodeId": {"$type": "scnNodeId", "id": node_id},
            "options": [
                {
                    "$type": "scnChoiceNodeOption",
                    "blueline": 0,
                    "bluelineCondition": None,
                    "caption": _cname(f"int_{clue_id}"),
                    "emphasisCondition": None,
                    "exDataFlags": 1,
                    "gameplayAction": {
                        "$type": "TweakDBID",
                        "$storage": "uint64",
                        "$value": "0",
                    },
                    "iconCondition": None,
                    "iconTagIds": [
                        {
                            "$type": "TweakDBID",
                            "$storage": "string",
                            "$value": "ChoiceCaptionParts.Inspect",
                        }
                    ],
                    "isFixedAsRead": 0,
                    "isSingleChoice": 1,
                    "mappinReferencePointId": {
                        "$type": "scnReferencePointId",
                        "id": 0xFFFFFFFF,
                    },
                    "questCondition": None,
                    "screenplayOptionId": {
                        "$type": "scnscreenplayItemId",
                        "id": screenplay_item_id,
                    },
                    "timedCondition": None,
                    "timedParams": None,
                    "triggerCondition": None,
                    "type": {
                        "$type":
                            "gameinteractionsChoiceTypeWrapper",
                        "properties": 0,
                    },
                }
            ],
            "outputSockets": output_sockets,
            "persistentLineEvents": [],
            "reminderCondition": None,
            "reminderParams": None,
            "shapeParams": allocator.wrap(
                {
                    "$type": "scnInteractionShapeParams",
                    "activationBaseLength": 1,
                    "activationHeight": 3,
                    "activationYawLimit": 360,
                    "customActivationRange": activation_range,
                    "customIndicationRange": indication_range,
                    "offset": {
                        "$type": "Vector3",
                        "X": 0,
                        "Y": 0,
                        "Z": 0,
                    },
                    "preset": "normal",
                    "rotation": {
                        "$type": "Quaternion",
                        "i": 0,
                        "j": 0,
                        "k": 0,
                        "r": 1,
                    },
                }
            ),
            "timedParams": None,
            "timedSectionCondition": None,
        }
    )


def _clue_reactivate_hub_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    choice_id: int,
) -> dict[str, Any]:
    output = _scene_output_socket([])
    output["destinations"] = [
        _scene_input_socket(choice_id, 0, name=2)
    ]
    return allocator.wrap(
        {
            "$type": "scnHubNode",
            "ffStrategy": "automatic",
            "nodeId": {"$type": "scnNodeId", "id": node_id},
            "outputSockets": [output],
        }
    )


def _clue_scanning_enabled_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    target: str,
    enable: bool,
    destination: tuple[int, int] | None,
) -> dict[str, Any]:
    return _scene_quest_node(
        allocator,
        node_id=node_id,
        quest_data={
            "$type": "questVisionModesManagerNodeDefinition",
            "type": allocator.wrap(
                {
                    "$type": "questEnableScanning_NodeType",
                    "enable": int(enable),
                    "objectRef": _dynamic_entity_reference(target),
                }
            ),
        },
        destination=destination,
    )


def _clue_scanning_bootstrap_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    target: str,
    scan_id: int,
    seed_id: int,
) -> dict[str, Any]:
    node = _clue_scanning_enabled_node(
        allocator,
        node_id=node_id,
        target=target,
        enable=True,
        destination=None,
    )
    node["Data"]["outputSockets"][0]["destinations"] = [
        _scene_input_socket(scan_id, 1),
        _scene_input_socket(seed_id, 1),
    ]
    return node


def _clue_success_cut_control_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    invalidity_id: int,
    inspected_id: int,
) -> dict[str, Any]:
    stop_invalidity = _scene_output_socket([], name=1)
    stop_invalidity["destinations"] = [
        _scene_input_socket(invalidity_id, 0),
        _scene_input_socket(invalidity_id, 0, name=1026),
    ]
    return allocator.wrap(
        {
            "$type": "scnCutControlNode",
            "ffStrategy": "automatic",
            "nodeId": {"$type": "scnNodeId", "id": node_id},
            "outputSockets": [
                _scene_output_socket([(inspected_id, 1)]),
                stop_invalidity,
            ],
        }
    )


def _clue_reactivation_section_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    hub_id: int,
) -> dict[str, Any]:
    output = _scene_output_socket([])
    output["destinations"] = [_scene_input_socket(hub_id, 0)]
    return allocator.wrap(
        {
            "$type": "scnSectionNode",
            "actorBehaviors": [],
            "events": [],
            "ffStrategy": "automatic",
            "isFocusClue": 1,
            "nodeId": {"$type": "scnNodeId", "id": node_id},
            "outputSockets": [
                output,
                _scene_output_socket([], name=1),
            ],
            "sectionDuration": {
                "$type": "scnSceneTime",
                "stu": 100,
            },
        }
    )


def _clue_invalidity_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    availability_fact: str,
    layer: str,
    scene_depot_path: str,
    destination: tuple[int, int],
) -> dict[str, Any]:
    conditions = [
        allocator.wrap(
            {
                "$type": "questFactsDBCondition",
                "type": allocator.wrap(
                    {
                        "$type": "questVarComparison_ConditionType",
                        "comparisonType": "LessOrEqual",
                        "factName": availability_fact,
                        "value": 0,
                    }
                ),
            }
        )
    ]
    for other_layer in (
        candidate
        for candidate in ("Visual", "Audio", "Thermal")
        if candidate != layer
    ):
        conditions.append(
            allocator.wrap(
                {
                    "$type": "questSceneCondition",
                    "type": allocator.wrap(
                        {
                            "$type":
                                "scnBraindanceLayer_ConditionType",
                            "layer": other_layer,
                            "sceneFile": {
                                "DepotPath": {
                                    "$type": "ResourcePath",
                                    "$storage": "string",
                                    "$value": scene_depot_path,
                                },
                                "Flags": "Soft",
                            },
                            "SceneVersion": "OlderOrEqual",
                        }
                    ),
                }
            )
        )
    return _scene_quest_node(
        allocator,
        node_id=node_id,
        quest_data={
            "$type": "questPauseConditionNodeDefinition",
            "condition": allocator.wrap(
                {
                    "$type": "questLogicalCondition",
                    "conditions": conditions,
                    "operation": "OR",
                }
            ),
        },
        destination=destination,
    )


def _clue_cut_control_node(
    allocator: _SceneHandleAllocator,
    *,
    node_id: int,
    validity_id: int,
    choice_id: int,
) -> dict[str, Any]:
    cut_choice = _scene_output_socket([], name=1)
    cut_choice["destinations"] = [
        _scene_input_socket(choice_id, 0, name=1)
    ]
    return allocator.wrap(
        {
            "$type": "scnCutControlNode",
            "ffStrategy": "automatic",
            "nodeId": {"$type": "scnNodeId", "id": node_id},
            "outputSockets": [
                _scene_output_socket([(validity_id, 1)]),
                cut_choice,
            ],
        }
    )


def _clue_attach_event(
    *,
    clue_id: str,
    prop_id: int,
    performer_id: int,
    slot: str,
    start_time: int,
    offset_mode: str,
    offset_position: list[float],
    offset_rotation: list[float],
) -> dict[str, Any]:
    return {
        "$type": "scneventsAttachPropToPerformer",
        "customOffsetPos": {
            "$type": "Vector3",
            "X": float(offset_position[0]),
            "Y": float(offset_position[1]),
            "Z": float(offset_position[2]),
        },
        "customOffsetRot": {
            "$type": "Quaternion",
            "i": float(offset_rotation[0]),
            "j": float(offset_rotation[1]),
            "k": float(offset_rotation[2]),
            "r": float(offset_rotation[3]),
        },
        "duration": 0,
        "executionTagFlags": 0,
        "fallbackData": [],
        "id": {
            "$type": "scnSceneEventId",
            "id": _deterministic_scene_event_id(
                "ghostline", "clue-attach", clue_id
            ),
        },
        "offsetMode": offset_mode,
        "performerId": {
            "$type": "scnPerformerId",
            "id": performer_id,
        },
        "propId": {"$type": "scnPropId", "id": prop_id},
        "scalingData": None,
        "slot": _cname(slot),
        "startTime": start_time,
        "type": "0",
    }


def _clue_audio_duration_event(
    *,
    clue_id: str,
    event_name: str,
    performer_id: int,
    start_time: int,
    duration: int,
    direction: str,
) -> dict[str, Any]:
    return {
        "$type": "scnAudioDurationEvent",
        "audioEventName": _cname(event_name),
        "duration": duration,
        "executionTagFlags": 0,
        "id": {
            "$type": "scnSceneEventId",
            "id": _deterministic_scene_event_id(
                "ghostline", "clue-audio", clue_id, direction
            ),
        },
        "performer": {
            "$type": "scnPerformerId",
            "id": performer_id,
        },
        "playbackDirectionSupport": direction,
        "scalingData": None,
        "startTime": start_time,
        "type": "0",
    }


def _configure_clue_contract(
    root: dict[str, Any],
    *,
    clues: list[dict[str, Any]],
    clue_events: list[dict[str, Any]],
    clue_targets: dict[str, dict[str, Any]] | None,
    scene_depot_path: str,
) -> None:
    if not clues:
        return
    graph_data = root.get("sceneGraph", {}).get("Data")
    graph = graph_data.get("graph") if isinstance(graph_data, dict) else None
    if not isinstance(graph, list):
        raise BraindancePipelineError("Scene has no graph for clue wiring")
    starts = [
        wrapper["Data"]
        for wrapper in graph
        if isinstance(wrapper, dict)
        and isinstance(wrapper.get("Data"), dict)
        and wrapper["Data"].get("$type") == "scnStartNode"
    ]
    if len(starts) != 1:
        raise BraindancePipelineError(
            f"Scene clue wiring requires one Start node; found {len(starts)}"
        )
    start = starts[0]
    output_sockets = start.get("outputSockets")
    if not isinstance(output_sockets, list) or not output_sockets:
        raise BraindancePipelineError("Scene Start node has no output socket")

    configured: list[
        tuple[dict[str, Any], dict[str, Any], str, str, str]
    ] = []
    attachments: list[
        tuple[str, dict[str, Any], dict[str, Any], dict[str, Any]]
    ] = []
    props = root.get("props")
    if not isinstance(props, list) or not props:
        raise BraindancePipelineError("Scene has no prop prototype for clues")
    prop_by_dynamic_name = {
        prop.get("spawnDespawnParams", {})
        .get("dynamicEntityUniqueName", {})
        .get("$value"): prop
        for prop in props
        if isinstance(prop, dict)
    }
    prototype = copy.deepcopy(props[-1])
    for clue, event in zip(clues, clue_events, strict=False):
        clue_id = str(clue["id"])
        target = (
            clue_targets.get(clue_id)
            if isinstance(clue_targets, dict)
            else None
        )
        dynamic_name = (
            target.get("dynamic_name")
            if isinstance(target, dict)
            else clue.get("target_dynamic_name")
        )
        record = (
            target.get("record")
            if isinstance(target, dict)
            else clue.get("target_record")
        )
        prop_name = (
            target.get("prop_name")
            if isinstance(target, dict)
            else clue.get("target_prop_name")
        )
        if not isinstance(dynamic_name, str) or not dynamic_name:
            existing = event.get("clueEntity", {})
            dynamic_name = (
                existing.get("dynamicEntityUniqueName", {}).get("$value")
                if isinstance(existing, dict)
                else None
            )
        prop = prop_by_dynamic_name.get(dynamic_name)
        if prop is None:
            if (
                not isinstance(dynamic_name, str)
                or not dynamic_name
                or not isinstance(record, str)
                or not record
            ):
                raise BraindancePipelineError(
                    f"Clue {clue_id!r} needs a spawned target record and "
                    "dynamic name"
                )
            prop = copy.deepcopy(prototype)
            prop_id = len(props)
            prop["propId"] = {"$type": "scnPropId", "id": prop_id}
            prop["propName"] = (
                prop_name
                if isinstance(prop_name, str) and prop_name
                else f"ghostline_bd_clue_{clue_id}"
            )
            prop["entityAcquisitionPlan"] = "spawnDespawn"
            spawn = prop["spawnDespawnParams"]
            spawn["appearance"] = _cname("default")
            spawn["dynamicEntityUniqueName"] = _cname(dynamic_name)
            spawn["isEnabled"] = 1
            spawn["spawnOnStart"] = 1
            spawn["validateSpawnPostion"] = 0
            spawn["specRecordId"] = {
                "$type": "TweakDBID",
                "$storage": "string",
                "$value": record,
            }
            prop["specPropRecordId"] = {
                "$type": "TweakDBID",
                "$storage": "string",
                "$value": record,
            }
            props.append(prop)
            prop_by_dynamic_name[dynamic_name] = prop
        elif isinstance(record, str) and record:
            prop["spawnDespawnParams"]["specRecordId"] = {
                "$type": "TweakDBID",
                "$storage": "string",
                "$value": record,
            }
            prop["specPropRecordId"] = {
                "$type": "TweakDBID",
                "$storage": "string",
                "$value": record,
            }
        position = clue.get("position")
        if isinstance(position, list) and len(position) == 3:
            prop["spawnDespawnParams"]["spawnOffset"]["position"] = {
                "$type": "Vector4",
                "W": 0,
                "X": float(position[0]),
                "Y": float(position[1]),
                "Z": float(position[2]),
            }
        availability_fact = (
            target.get("availability_fact")
            if isinstance(target, dict)
            else None
        )
        if not isinstance(availability_fact, str) or not availability_fact:
            availability_fact = _clue_availability_fact(clue)
        event["factName"] = _cname(availability_fact)
        event["overrideFact"] = 1
        event["clueEntity"] = _dynamic_entity_reference(dynamic_name)
        configured.append(
            (clue, event, dynamic_name, clue_id, availability_fact)
        )
        attach = target.get("attach") if isinstance(target, dict) else None
        if isinstance(attach, dict):
            attachments.append((clue_id, clue, event, prop))

    contract_ids = {
        node_id
        for index in range(len(configured))
        for node_id in (
            *_clue_contract_node_ids(index),
            *_clue_contract_aux_node_ids(index),
        )
    }
    layer_unlocks = [
        _BRAINDANCE_LAYER_UNLOCKS[layer]
        for layer in dict.fromkeys(
            str(clue["layer"]) for clue, *_rest in configured
        )
        if layer in _BRAINDANCE_LAYER_UNLOCKS
    ]
    contract_ids.update(node_id for node_id, _fact_name in layer_unlocks)
    retained: list[dict[str, Any]] = []
    for wrapper in graph:
        data = wrapper.get("Data") if isinstance(wrapper, dict) else None
        node_id = (
            data.get("nodeId", {}).get("id")
            if isinstance(data, dict)
            else None
        )
        if node_id not in contract_ids:
            retained.append(wrapper)
            continue
        generated_types = {
            "questScan_ConditionType",
            "ToggleFocusClueEvent",
            "questDiscoverBraindanceClue_NodeType",
            "questSetVar_NodeType",
            "questEnableScanning_NodeType",
            "questLogicalCondition",
            "scnBraindanceLayer_ConditionType",
            "scnChoiceNode",
            "scnCutControlNode",
            "scnHubNode",
            "scnSectionNode",
        }
        if not any(
            item.get("$type") in generated_types for item in _walk(data)
        ):
            raise BraindancePipelineError(
                f"Clue contract node ID {node_id} collides with scene content"
            )
    graph[:] = retained
    notable_points = root.get("notablePoints")
    if notable_points is None:
        root["notablePoints"] = []
    elif not isinstance(notable_points, list):
        raise BraindancePipelineError("Scene notablePoints must be an array")
    else:
        notable_points[:] = [
            point
            for point in notable_points
            if point.get("nodeId", {}).get("id") not in contract_ids
        ]
    destinations = output_sockets[0].get("destinations")
    if not isinstance(destinations, list):
        raise BraindancePipelineError(
            "Scene Start output has no destinations array"
        )
    destinations[:] = [
        destination
        for destination in destinations
        if destination.get("nodeId", {}).get("id") not in contract_ids
    ]

    allocator = _SceneHandleAllocator(root)
    focus_option_ids = _configure_focus_clue_options(
        root,
        [clue_id for _, _, _, clue_id, _ in configured],
    )
    # Vanilla Q004 explicitly unlocks the nonvisual controls before their
    # clues can become scannable.  These typo-preserved engine facts are
    # persistent tutorial unlocks and deliberately are not reset on exit.
    for node_id, fact_name in layer_unlocks:
        destinations.append(_scene_input_socket(node_id, 1))
        graph.append(
            _clue_fact_node(
                allocator,
                node_id=node_id,
                fact_name=fact_name,
            )
        )
    for index, (
        clue,
        _event,
        dynamic_name,
        clue_id,
        availability_fact,
    ) in enumerate(configured):
        (
            scan_id,
            validity_id,
            choice_id,
            invalidity_id,
            cut_id,
            inspected_id,
            discovered_id,
            fact_id,
            reactivate_id,
        ) = _clue_contract_node_ids(index)
        (
            success_cut_id,
            reactivation_section_id,
            enable_scanning_id,
            disable_scanning_id,
            bootstrap_scanning_id,
            seed_focus_id,
        ) = _clue_contract_aux_node_ids(index)
        prop = prop_by_dynamic_name[dynamic_name]
        prop_id = int(prop["propId"]["id"])
        target = (
            clue_targets.get(clue_id)
            if isinstance(clue_targets, dict)
            else None
        )
        focus = target.get("focus") if isinstance(target, dict) else None
        if not isinstance(focus, dict):
            focus = {}
        destinations.append(
            _scene_input_socket(bootstrap_scanning_id, 1)
        )
        graph.extend(
            [
                _clue_scanning_bootstrap_node(
                    allocator,
                    node_id=bootstrap_scanning_id,
                    target=dynamic_name,
                    scan_id=scan_id,
                    seed_id=seed_focus_id,
                ),
                _clue_focus_state_node(
                    allocator,
                    node_id=seed_focus_id,
                    target=dynamic_name,
                    investigation_state="NOT_INSPECTED",
                    destination=None,
                ),
                _clue_scan_node(
                    allocator,
                    node_id=scan_id,
                    target=dynamic_name,
                    destination=(validity_id, 1),
                ),
                _clue_validity_node(
                    allocator,
                    node_id=validity_id,
                    availability_fact=availability_fact,
                    layer=str(clue["layer"]),
                    scene_depot_path=scene_depot_path,
                    destinations=[
                        (enable_scanning_id, 1),
                        (invalidity_id, 1),
                    ],
                ),
                _clue_scanning_enabled_node(
                    allocator,
                    node_id=enable_scanning_id,
                    target=dynamic_name,
                    enable=True,
                    destination=(choice_id, 0),
                ),
                _focus_clue_choice_node(
                    allocator,
                    node_id=choice_id,
                    clue_id=clue_id,
                    prop_id=prop_id,
                    screenplay_item_id=focus_option_ids[clue_id],
                    success_cut_id=success_cut_id,
                    visualizer_style=str(
                        focus.get("visualizer_style", "inWorld")
                    ),
                    location_type=str(
                        focus.get("location_type", "Interaction")
                    ),
                    activation_range=float(
                        focus.get("activation_range", 3)
                    ),
                    indication_range=float(
                        focus.get("indication_range", 20)
                    ),
                    choice_group=str(
                        focus.get("choice_group", "ghostline_bd_clues")
                    ),
                ),
                _clue_invalidity_node(
                    allocator,
                    node_id=invalidity_id,
                    availability_fact=availability_fact,
                    layer=str(clue["layer"]),
                    scene_depot_path=scene_depot_path,
                    destination=(disable_scanning_id, 1),
                ),
                _clue_scanning_enabled_node(
                    allocator,
                    node_id=disable_scanning_id,
                    target=dynamic_name,
                    enable=False,
                    destination=(cut_id, 0),
                ),
                _clue_cut_control_node(
                    allocator,
                    node_id=cut_id,
                    validity_id=validity_id,
                    choice_id=choice_id,
                ),
                _clue_success_cut_control_node(
                    allocator,
                    node_id=success_cut_id,
                    invalidity_id=invalidity_id,
                    inspected_id=inspected_id,
                ),
                _clue_inspected_node(
                    allocator,
                    node_id=inspected_id,
                    target=dynamic_name,
                    destination=(discovered_id, 1),
                ),
                _clue_discovered_node(
                    allocator,
                    node_id=discovered_id,
                    clue_name=clue_id,
                    destination=(fact_id, 1),
                ),
                _clue_fact_node(
                    allocator,
                    node_id=fact_id,
                    fact_name=str(clue["fact"]),
                    destination=(reactivation_section_id, 0),
                ),
                _clue_reactivation_section_node(
                    allocator,
                    node_id=reactivation_section_id,
                    hub_id=reactivate_id,
                ),
                _clue_reactivate_hub_node(
                    allocator,
                    node_id=reactivate_id,
                    choice_id=choice_id,
                ),
            ]
        )
        notable_points = root.setdefault("notablePoints", [])
        if not isinstance(notable_points, list):
            raise BraindancePipelineError(
                "Scene notablePoints must be an array"
            )
        notable_points.append(
            {
                "$type": "scnNotablePoint",
                "name": _cname(f"ghostline_bd_clue_{clue_id}"),
                "nodeId": {"$type": "scnNodeId", "id": choice_id},
            }
        )

    rewindable = [
        wrapper["Data"]
        for wrapper in graph
        if isinstance(wrapper, dict)
        and isinstance(wrapper.get("Data"), dict)
        and wrapper["Data"].get("$type") == "scnRewindableSectionNode"
    ]
    if configured and len(rewindable) != 1:
        raise BraindancePipelineError(
            "Functional clues require exactly one rewindable section"
        )
    if configured:
        rewindable_node = rewindable[0]
        events = rewindable_node.get("events")
        if not isinstance(events, list):
            raise BraindancePipelineError(
                "Rewindable section has no event array for functional clues"
            )
        clue_prop_ids = {
            int(prop_by_dynamic_name[dynamic_name]["propId"]["id"])
            for _, _, dynamic_name, _, _ in configured
        }
        authored_audio_event_ids = {
            _deterministic_scene_event_id(
                "ghostline", "clue-audio", clue_id, direction
            )
            for _, _, _, clue_id, _ in configured
            for direction in ("Forward", "Backward")
        }
        events[:] = [
            wrapper
            for wrapper in events
            if not (
                isinstance(wrapper, dict)
                and isinstance(wrapper.get("Data"), dict)
                and (
                    (
                        wrapper["Data"].get("$type")
                        == "scneventsAttachPropToPerformer"
                        and wrapper["Data"].get("propId", {}).get("id")
                        in clue_prop_ids
                    )
                    or (
                        wrapper["Data"].get("$type")
                        == "scnAudioDurationEvent"
                        and wrapper["Data"].get("id", {}).get("id")
                        in authored_audio_event_ids
                    )
                )
            )
        ]
        debug_symbols = root.get("debugSymbols")
        debug_event_symbols = (
            debug_symbols.get("sceneEventsDebugSymbols")
            if isinstance(debug_symbols, dict)
            else None
        )
        existing_event_ids = {
            event_id.get("id")
            for symbol in debug_event_symbols or []
            if isinstance(symbol, dict)
            for event_id in symbol.get("sceneEventIds", [])
            if isinstance(event_id, dict)
        }
        origin_node_id = int(rewindable_node["nodeId"]["id"])
        for clue_id, _clue, event, prop in attachments:
            target = clue_targets.get(clue_id) if clue_targets else None
            attach = target.get("attach") if isinstance(target, dict) else None
            if not isinstance(attach, dict):
                continue
            at = str(attach.get("at", "scene_start"))
            start_time = (
                int(event.get("startTime", 0))
                if at == "clue_start"
                else int(attach.get("start_ms", 0))
            )
            offset_position = attach.get("position", [0.0, 0.0, 0.0])
            offset_rotation = attach.get(
                "rotation",
                [0.0, 0.0, 0.0, 1.0],
            )
            if (
                not isinstance(offset_position, list)
                or len(offset_position) != 3
                or not all(
                    isinstance(value, (int, float))
                    for value in offset_position
                )
            ):
                raise BraindancePipelineError(
                    f"Clue {clue_id!r} attach.position must be XYZ"
                )
            if (
                not isinstance(offset_rotation, list)
                or len(offset_rotation) != 4
                or not all(
                    isinstance(value, (int, float))
                    for value in offset_rotation
                )
            ):
                raise BraindancePipelineError(
                    f"Clue {clue_id!r} attach.rotation must be XYZW"
                )
            attach_event = _clue_attach_event(
                clue_id=clue_id,
                prop_id=int(prop["propId"]["id"]),
                performer_id=int(attach["performer_id"]),
                slot=str(attach["slot"]),
                start_time=start_time,
                offset_mode=str(
                    attach.get("offset_mode", "useCustomOffset")
                ),
                offset_position=offset_position,
                offset_rotation=offset_rotation,
            )
            attach_wrapper = allocator.wrap(attach_event)
            clue_event_id = event.get("id", {}).get("id")
            clue_event_index = next(
                (
                    event_index
                    for event_index, wrapper in enumerate(events)
                    if wrapper.get("Data", {}).get("id", {}).get("id")
                    == clue_event_id
                ),
                len(events),
            )
            events.insert(clue_event_index, attach_wrapper)
            event_id = attach_event["id"]["id"]
            if (
                isinstance(debug_event_symbols, list)
                and event_id not in existing_event_ids
            ):
                editor_event_id = (
                    0x10000000
                    | (
                        _fnv1a32(f"clue-attach:{clue_id}")
                        & 0x0FFFFFFF
                    )
                )
                debug_event_symbols.append(
                    {
                        "$type": "scnSceneEventSymbol",
                        "editorEventId": str(editor_event_id),
                        "originNodeId": {
                            "$type": "scnNodeId",
                            "id": origin_node_id,
                        },
                        "sceneEventIds": [
                            {
                                "$type": "scnSceneEventId",
                                "id": event_id,
                            }
                        ],
                    }
                )
                existing_event_ids.add(event_id)
        for clue, event, _dynamic_name, clue_id, _availability in configured:
            target = clue_targets.get(clue_id) if clue_targets else None
            audio = target.get("audio") if isinstance(target, dict) else None
            if not isinstance(audio, dict):
                continue
            performer_id = int(audio["performer_id"])
            start_time = int(event.get("startTime", 0))
            duration = int(event.get("duration", 0))
            names = [
                ("Forward", str(audio["event"])),
                ("Backward", str(audio["reverse_event"])),
            ]
            clue_event_id = event.get("id", {}).get("id")
            clue_event_index = next(
                (
                    event_index
                    for event_index, wrapper in enumerate(events)
                    if wrapper.get("Data", {}).get("id", {}).get("id")
                    == clue_event_id
                ),
                len(events),
            )
            for direction, event_name in names:
                audio_event = _clue_audio_duration_event(
                    clue_id=clue_id,
                    event_name=event_name,
                    performer_id=performer_id,
                    start_time=start_time,
                    duration=duration,
                    direction=direction,
                )
                events.insert(
                    clue_event_index,
                    allocator.wrap(audio_event),
                )
                clue_event_index += 1


def link_scene_document(
    scene_document: dict[str, Any],
    rid_document: dict[str, Any],
    handoff: dict[str, Any],
    *,
    rid_depot_path: str,
    scene_origin: str,
    camera_ref: str,
    clue_targets: dict[str, dict[str, Any]] | None = None,
    scene_depot_path: str | None = None,
    scene_spawn_set_actors: Iterable[dict[str, Any]] = (),
) -> tuple[dict[str, Any], dict[str, Any]]:
    result = copy.deepcopy(scene_document)
    root = _root(result, "scnSceneResource")
    spawn_set_actor_report = _add_scene_spawn_set_actors(
        root,
        scene_spawn_set_actors,
    )
    catalog = build_rid_catalog(rid_document)
    actors = handoff.get("actors")
    if not isinstance(actors, list) or not actors:
        raise BraindancePipelineError("Handoff has no actors")
    duration_ms = round(
        (int(handoff["frames"]["end"]) - int(handoff["frames"]["start"]))
        / float(handoff["fps"])
        * 1000.0
    )
    resource_id = _fnv1a32(rid_depot_path)
    actor_by_performer: dict[int, dict[str, Any]] = {}
    actor_links: dict[str, dict[str, int | None]] = {}
    animation_refs: list[dict[str, Any]] = []
    body_sets: list[dict[str, Any]] = []
    facial_sets: list[dict[str, Any]] = []
    cyberware_sets: list[dict[str, Any]] = []
    for actor in actors:
        signature = str(actor.get("rid_signature", actor["id"]))
        rid_actor = catalog["actors"].get(signature)
        if not isinstance(rid_actor, dict):
            raise BraindancePipelineError(
                f"RID does not contain handoff actor {signature!r}"
            )
        link: dict[str, int | None] = {
            "body_set": None,
            "body_ref": None,
            "facial_set": None,
            "facial_ref": None,
            "cyberware_set": None,
            "cyberware_ref": None,
        }
        for channel in ("body", "facial", "cyberware"):
            clip = rid_actor[channel]
            if clip is None:
                continue
            reference_index = len(animation_refs)
            animation_refs.append(
                _rid_animation_ref(int(clip["serial"]), resource_id)
            )
            if channel == "body":
                link["body_ref"] = reference_index
                link["body_set"] = len(body_sets)
                body_sets.append(_rid_set_ref(reference_index))
            elif channel == "facial":
                link["facial_ref"] = reference_index
                link["facial_set"] = len(facial_sets)
                facial_sets.append(_rid_set_ref(reference_index))
            else:
                link["cyberware_ref"] = reference_index
                link["cyberware_set"] = len(cyberware_sets)
                cyberware_sets.append(_rid_set_ref(reference_index))
        performer_id = int(actor["performer_id"])
        actor_by_performer[performer_id] = actor
        actor_links[signature] = link

    scene_actors = root.get("actors")
    if not isinstance(scene_actors, list):
        raise BraindancePipelineError("Scene has no actor definitions")
    scene_actor_by_id = {
        int(scene_actor.get("actorId", {}).get("id")): scene_actor
        for scene_actor in scene_actors
        if isinstance(scene_actor, dict)
        and isinstance(scene_actor.get("actorId"), dict)
        and scene_actor["actorId"].get("id") is not None
    }
    for actor in actors:
        actor_id = int(actor["actor_id"])
        scene_actor = scene_actor_by_id.get(actor_id)
        if scene_actor is None:
            raise BraindancePipelineError(
                f"Scene has no actor definition for handoff actor {actor_id}"
            )
        signature = str(actor.get("rid_signature", actor["id"]))
        link = actor_links[signature]
        scene_actor["animSets"] = (
            [{"$type": "scnSRRefId", "id": int(link["body_set"])}]
            if link["body_set"] is not None
            else []
        )
        scene_actor["facialAnimSets"] = (
            [
                {
                    "$type": "scnRidFacialAnimSetSRRefId",
                    "id": int(link["facial_set"]),
                }
            ]
            if link["facial_set"] is not None
            else []
        )
        scene_actor["cyberwareAnimSets"] = (
            [
                {
                    "$type": "scnRidCyberwareAnimSetSRRefId",
                    "id": int(link["cyberware_set"]),
                }
            ]
            if link["cyberware_set"] is not None
            else []
        )

    references = root.get("resouresReferences")
    if not isinstance(references, dict):
        raise BraindancePipelineError("Scene has no resouresReferences object")
    references["ridAnimations"] = animation_refs
    references["ridAnimSets"] = body_sets
    references["ridFacialAnimSets"] = facial_sets
    references["ridCyberwareAnimSets"] = cyberware_sets
    references["ridCameraAnimations"] = [
        _camera_ref(int(catalog["camera"]["serial"]), resource_id)
    ]
    references["ridAnimationContainers"] = []
    references["ridDeformationAnimSets"] = []
    if not references.get("lipsyncAnimSets"):
        for scene_actor in [
            *root.get("actors", []),
            *root.get("playerActors", []),
        ]:
            lipsync = scene_actor.get("lipsyncAnimSet")
            if isinstance(lipsync, dict):
                lipsync["id"] = 0xFFFFFFFF
    root["ridResources"] = [
        {
            "$type": "scnRidResourceHandler",
            "id": {"$type": "scnRidResourceId", "id": resource_id},
            "ridResource": {
                "DepotPath": {
                    "$type": "ResourcePath",
                    "$storage": "string",
                    "$value": rid_depot_path,
                },
                "Flags": "Default",
            },
        }
    ]

    event_counts = {"body": 0, "facial": 0, "cyberware": 0, "camera": 0}
    binding_counts = {
        signature: {"body": 0, "facial": 0, "cyberware": 0}
        for signature in actor_links
    }
    for value in _walk(root.get("sceneGraph")):
        event_type = value.get("$type")
        if event_type == "scnPlaySkAnimEvent":
            performer = value.get("performer", {}).get("id")
            actor = actor_by_performer.get(performer)
            if actor is None:
                raise BraindancePipelineError(
                    f"Body RID event uses unmapped performer {performer}"
                )
            signature = str(actor.get("rid_signature", actor["id"]))
            reference_index = actor_links[signature]["body_ref"]
            if reference_index is None:
                raise BraindancePipelineError(
                    f"Actor {signature!r} has no body RID clip"
                )
            _set_reference_anim_name(value, int(reference_index))
            value["duration"] = duration_ms
            rid_body = catalog["actors"][signature]["body"]
            if not isinstance(rid_body, dict):
                raise BraindancePipelineError(
                    f"Actor {signature!r} has no RID body metadata"
                )
            _synchronize_root_motion(
                value,
                actor=actor,
                rid_body=rid_body,
                handoff=handoff,
            )
            event_counts["body"] += 1
            binding_counts[signature]["body"] += 1
        elif event_type == "scnPlayRidAnimEvent":
            performer = value.get("performer", {}).get("id")
            actor = actor_by_performer.get(performer)
            if actor is None:
                raise BraindancePipelineError(
                    f"Auxiliary RID event uses unmapped performer {performer}"
                )
            component = value.get("actorComponent", {}).get("$value")
            channel = "cyberware" if component == "cyberware" else "facial"
            signature = str(actor.get("rid_signature", actor["id"]))
            reference_index = actor_links[signature][f"{channel}_ref"]
            if reference_index is None:
                raise BraindancePipelineError(
                    f"Actor {signature!r} has no {channel} RID clip"
                )
            value["animResRefId"] = {
                "$type": "scnRidAnimationSRRefId",
                "id": int(reference_index),
            }
            value["duration"] = duration_ms
            event_counts[channel] += 1
            binding_counts[signature][channel] += 1
        elif event_type == "scneventsPlayRidCameraAnimEvent":
            value["animSRRefId"] = {
                "$type": "scnRidCameraAnimationSRRefId",
                "id": 0,
            }
            value["cameraRef"] = {
                "$type": "NodeRef",
                "$storage": "string",
                "$value": camera_ref,
            }
            value["duration"] = duration_ms
            event_counts["camera"] += 1

    missing_bindings: list[str] = []
    for signature, links in actor_links.items():
        for channel in ("body", "facial", "cyberware"):
            required = (
                links["body_set"] is not None
                if channel == "body"
                else links[f"{channel}_ref"] is not None
            )
            if required and binding_counts[signature][channel] == 0:
                missing_bindings.append(f"{signature}.{channel}")
    if event_counts["camera"] == 0:
        missing_bindings.append("camera")
    if missing_bindings:
        raise BraindancePipelineError(
            "Scene has no playback events for: " + ", ".join(missing_bindings)
        )

    clue_events = [
        value
        for value in _walk(root.get("sceneGraph"))
        if value.get("$type") == "scneventsClueEvent"
    ]
    clues = handoff.get("clues", [])
    if len(clue_events) < len(clues):
        raise BraindancePipelineError(
            f"Scene supplies {len(clue_events)} clue events; "
            f"handoff requires {len(clues)}"
        )
    for event, clue in zip(clue_events, clues, strict=False):
        event["clueName"] = {
            "$type": "CName",
            "$storage": "string",
            "$value": clue["id"],
        }
        event["layer"] = clue["layer"]
        if clue["layer"] == "Thermal":
            event["executionTagFlags"] = 16
        event["factName"] = {
            "$type": "CName",
            "$storage": "string",
            "$value": clue["fact"],
        }
        event["overrideFact"] = 1
        event["startTime"] = round(
            (int(clue["frames"][0]) - int(handoff["frames"]["start"]))
            / float(handoff["fps"])
            * 1000.0
        )
        event["duration"] = round(
            (int(clue["frames"][1]) - int(clue["frames"][0]))
            / float(handoff["fps"])
            * 1000.0
        )
    has_authored_clue_targets = bool(clue_targets) or any(
        isinstance(clue.get("target_record"), str)
        and isinstance(clue.get("target_dynamic_name"), str)
        for clue in clues
    )
    if has_authored_clue_targets:
        if not isinstance(scene_depot_path, str) or not scene_depot_path:
            raise BraindancePipelineError(
                "Functional clue wiring requires the scene depot path"
            )
        _configure_clue_contract(
            root,
            clues=clues,
            clue_events=clue_events,
            clue_targets=clue_targets,
            scene_depot_path=scene_depot_path,
        )
    _retarget_scene_markers(root, scene_origin)

    report = audit_scene_document(
        result,
        handoff=handoff,
        require_functional_exit=False,
        require_functional_clues=has_authored_clue_targets,
    )
    if not report["ok"]:
        raise BraindancePipelineError("; ".join(report["errors"]))
    report.update(
        {
            "rid_depot_path": rid_depot_path,
            "rid_resource_id": resource_id,
            "event_counts": event_counts,
            "binding_counts": binding_counts,
            "actor_links": actor_links,
            "scene_spawn_set_actors": spawn_set_actor_report,
        }
    )
    return result, report


def audit_scene_document(
    document: dict[str, Any],
    *,
    handoff: dict[str, Any] | None = None,
    require_functional_exit: bool = True,
    require_functional_clues: bool = True,
) -> dict[str, Any]:
    errors: list[str] = []
    root = _root(document, "scnSceneResource")
    all_values = list(_walk(root))
    type_counts: dict[str, int] = {}
    for value in all_values:
        type_name = value.get("$type")
        if isinstance(type_name, str):
            type_counts[type_name] = type_counts.get(type_name, 0) + 1
    if type_counts.get("scnRewindableSectionNode", 0) < 1:
        errors.append("Scene has no scnRewindableSectionNode")
    if type_counts.get("scneventsPlayRidCameraAnimEvent", 0) < 1:
        errors.append("Scene has no RID camera event")
    camera_events = [
        value
        for value in all_values
        if value.get("$type") == "scneventsPlayRidCameraAnimEvent"
    ]
    camera_refs = [
        event.get("cameraRef", {}).get("$value")
        for event in camera_events
        if isinstance(event.get("cameraRef"), dict)
    ]
    if camera_events and not any(
        isinstance(camera_ref, str) and camera_ref not in {"", "0"}
        for camera_ref in camera_refs
    ):
        errors.append("Scene RID camera events have no bound camera NodeRef")
    if type_counts.get("scneventsBraindanceVisibilityEvent", 0) < 1:
        errors.append("Scene has no braindance visibility event")
    actor_definitions = [
        *root.get("actors", []),
        *root.get("playerActors", []),
    ]
    actor_ids = sorted(
        actor.get("actorId", {}).get("id")
        for actor in actor_definitions
        if isinstance(actor.get("actorId", {}).get("id"), int)
    )
    if actor_ids != list(range(len(actor_ids))):
        errors.append(
            "Scene actor IDs must be dense from zero; found "
            + ", ".join(str(actor_id) for actor_id in actor_ids)
        )
    prop_ids = sorted(
        prop.get("propId", {}).get("id")
        for prop in root.get("props", [])
        if isinstance(prop.get("propId", {}).get("id"), int)
    )
    if prop_ids != list(range(len(prop_ids))):
        errors.append(
            "Scene prop IDs must be dense from zero; found "
            + ", ".join(str(prop_id) for prop_id in prop_ids)
        )
    prop_by_performer = {
        2 + (int(prop["propId"]["id"]) << 8): prop
        for prop in root.get("props", [])
        if isinstance(prop, dict)
        and isinstance(prop.get("propId", {}).get("id"), int)
    }
    visibility_targets: list[str] = []
    for event in all_values:
        if event.get("$type") != "scneventsBraindanceVisibilityEvent":
            continue
        performer_id = event.get("performerId", {}).get("id")
        prop = prop_by_performer.get(performer_id)
        if prop is None:
            errors.append(
                "Braindance visibility event targets non-prop performer "
                f"{performer_id}"
            )
            continue
        prop_name = str(prop.get("propName", ""))
        visibility_targets.append(prop_name)
    visibility_target_names = {
        "bdview"
        if "bdview" in name.casefold()
        else "bdfog"
        if "bdfog" in name.casefold()
        else name.casefold()
        for name in visibility_targets
    }
    missing_visibility_targets = {"bdview", "bdfog"} - visibility_target_names
    if missing_visibility_targets:
        errors.append(
            "Braindance visibility events do not target: "
            + ", ".join(sorted(missing_visibility_targets))
        )
    references = root.get("resouresReferences", {})
    if not isinstance(references, dict):
        references = {}
    actor_reference_fields = {
        "animSets": "ridAnimSets",
        "facialAnimSets": "ridFacialAnimSets",
        "cyberwareAnimSets": "ridCyberwareAnimSets",
    }
    body_performers = {
        value.get("performer", {}).get("id")
        for value in all_values
        if value.get("$type") == "scnPlaySkAnimEvent"
    }
    root_motion_samples: dict[int, int] = {}
    for event in all_values:
        if event.get("$type") != "scnPlaySkAnimEvent":
            continue
        performer_id = event.get("performer", {}).get("id")
        root_motion = event.get("rootMotionData")
        if not isinstance(root_motion, dict) or root_motion.get("enabled") != 1:
            errors.append(
                f"Body performer {performer_id} has no enabled root motion"
            )
            continue
        trajectory = root_motion.get("trajectoryLOD")
        if not isinstance(trajectory, list) or len(trajectory) < 2:
            errors.append(
                f"Body performer {performer_id} has no root-motion trajectory"
            )
            continue
        times = [float(sample.get("time", -1.0)) for sample in trajectory]
        event_duration = float(event.get("duration", 0)) / 1000.0
        if times != sorted(times):
            errors.append(
                f"Body performer {performer_id} root-motion times decrease"
            )
        if times[0] < 0.0 or not math.isclose(
            times[-1],
            event_duration,
            abs_tol=1e-4,
        ):
            errors.append(
                f"Body performer {performer_id} root motion ends at "
                f"{times[-1]:g}s, event ends at {event_duration:g}s"
            )
        root_motion_samples[int(performer_id)] = len(trajectory)
    auxiliary_performers: dict[str, set[int | None]] = {
        "facialAnimSets": set(),
        "cyberwareAnimSets": set(),
    }
    for value in all_values:
        if value.get("$type") != "scnPlayRidAnimEvent":
            continue
        actor_field = (
            "cyberwareAnimSets"
            if value.get("actorComponent", {}).get("$value") == "cyberware"
            else "facialAnimSets"
        )
        auxiliary_performers[actor_field].add(
            value.get("performer", {}).get("id")
        )
    for actor in actor_definitions:
        actor_name = actor.get("actorName", actor.get("playerName", "<actor>"))
        actor_id = actor.get("actorId", {}).get("id")
        performer_id = (
            1 + (int(actor_id) << 8)
            if isinstance(actor_id, int)
            else None
        )
        if performer_id in body_performers and not actor.get("animSets"):
            errors.append(f"Actor {actor_name} has no bound RID body set")
        for actor_field, label in (
            ("facialAnimSets", "facial"),
            ("cyberwareAnimSets", "cyberware"),
        ):
            if (
                performer_id in auxiliary_performers[actor_field]
                and not actor.get(actor_field)
            ):
                errors.append(
                    f"Actor {actor_name} has no bound RID {label} set"
                )
        for actor_field, reference_field in actor_reference_fields.items():
            reference_count = len(references.get(reference_field, []))
            for reference in actor.get(actor_field, []):
                reference_id = reference.get("id")
                if (
                    not isinstance(reference_id, int)
                    or reference_id < 0
                    or reference_id >= reference_count
                ):
                    errors.append(
                        f"Actor {actor_name} has invalid {actor_field} "
                        f"reference {reference_id}"
                    )
        lipsync = actor.get("lipsyncAnimSet")
        if isinstance(lipsync, dict):
            lipsync_id = lipsync.get("id")
            lipsync_count = len(references.get("lipsyncAnimSets", []))
            if (
                lipsync_id != 0xFFFFFFFF
                and (
                    not isinstance(lipsync_id, int)
                    or lipsync_id < 0
                    or lipsync_id >= lipsync_count
                )
            ):
                errors.append(
                    f"Actor {actor_name} has invalid lipsyncAnimSet "
                    f"reference {lipsync_id}"
                )
    rid_animation_count = len(references.get("ridAnimations", []))
    for index, animation_set in enumerate(references.get("ridAnimSets", [])):
        for animation in animation_set.get("animations", []):
            animation_id = animation.get("id")
            if (
                not isinstance(animation_id, int)
                or animation_id < 0
                or animation_id >= rid_animation_count
            ):
                errors.append(
                    f"RID animation set {index} has invalid animation "
                    f"reference {animation_id}"
                )
    layers = {
        value.get("layer")
        for value in all_values
        if value.get("$type") == "scneventsClueEvent"
    }
    expected_layers = (
        {clue["layer"] for clue in handoff.get("clues", [])}
        if handoff is not None
        else set()
    )
    missing_layers = sorted(expected_layers - layers)
    if missing_layers:
        errors.append("Scene has no clue events for: " + ", ".join(missing_layers))
    spawned_prop_by_dynamic_name = {
        value: prop
        for prop in root.get("props", [])
        if isinstance(prop, dict)
        if isinstance(prop.get("spawnDespawnParams"), dict)
        if isinstance(
            value := prop["spawnDespawnParams"]
            .get("dynamicEntityUniqueName", {})
            .get("$value"),
            str,
        )
        and value not in {"", "0", "None"}
    }
    spawned_prop_dynamic_names = set(spawned_prop_by_dynamic_name)
    spawned_actor_dynamic_names = {
        value
        for actor in root.get("actors", [])
        if isinstance(actor, dict)
        if isinstance(actor.get("spawnDespawnParams"), dict)
        if isinstance(
            value := actor["spawnDespawnParams"]
            .get("dynamicEntityUniqueName", {})
            .get("$value"),
            str,
        )
        and value not in {"", "0", "None"}
    }
    spawned_dynamic_names = (
        spawned_prop_dynamic_names | spawned_actor_dynamic_names
    )
    clue_entities: dict[str, str] = {}
    clue_events = [
        value
        for value in all_values
        if value.get("$type") == "scneventsClueEvent"
    ]
    for event in clue_events:
        clue_name = event.get("clueName", {}).get("$value")
        clue_entity = event.get("clueEntity")
        if not isinstance(clue_entity, dict):
            errors.append(f"Clue {clue_name!r} has no entity reference")
            continue
        dynamic_name = clue_entity.get("dynamicEntityUniqueName", {}).get(
            "$value"
        )
        node_ref = clue_entity.get("reference", {}).get("$value")
        names = clue_entity.get("names", [])
        resolved = (
            isinstance(dynamic_name, str)
            and dynamic_name in spawned_dynamic_names
        ) or (
            isinstance(node_ref, str)
            and node_ref not in {"", "0"}
            and (
                not names
                or all(
                    isinstance(name, dict)
                    and isinstance(name.get("$value"), str)
                    for name in names
                )
            )
        )
        if not resolved:
            errors.append(
                f"Clue {clue_name!r} does not resolve to a scene prop "
                "or world entity"
            )
        if isinstance(clue_name, str):
            clue_entities[clue_name] = str(dynamic_name or node_ref)
    if handoff is not None and require_functional_clues:
        event_by_name = {
            event.get("clueName", {}).get("$value"): event
            for event in clue_events
        }
        for clue in handoff.get("clues", []):
            if clue.get("layer") != "Visual" or "position" not in clue:
                continue
            event = event_by_name.get(clue.get("id"))
            dynamic_name = (
                event.get("clueEntity", {})
                .get("dynamicEntityUniqueName", {})
                .get("$value")
                if isinstance(event, dict)
                else None
            )
            if (
                not isinstance(dynamic_name, str)
                or dynamic_name not in spawned_prop_dynamic_names
            ):
                errors.append(
                    f"Visual clue {clue['id']!r} has no matching spawned prop"
                )
    scene_graph = root.get("sceneGraph", {}).get("Data", {})
    graph_nodes = (
        scene_graph.get("graph", [])
        if isinstance(scene_graph, dict)
        else []
    )
    node_by_id = {
        node_id: wrapper["Data"]
        for wrapper in graph_nodes
        if isinstance(wrapper, dict)
        and isinstance(wrapper.get("Data"), dict)
        and isinstance(
            node_id := wrapper["Data"].get("nodeId", {}).get("id"),
            int,
        )
    }

    def outgoing_edges(
        node_id: int,
    ) -> list[tuple[int, int, int, int]]:
        destinations: list[tuple[int, int, int, int]] = []
        for socket in node_by_id.get(node_id, {}).get(
            "outputSockets", []
        ):
            source_name = socket.get("stamp", {}).get("name")
            for destination in socket.get("destinations", []):
                target = destination.get("nodeId", {}).get("id")
                destination_stamp = destination.get("isockStamp", {})
                destination_name = destination_stamp.get("name")
                ordinal = destination_stamp.get("ordinal")
                if (
                    isinstance(target, int)
                    and isinstance(destination_name, int)
                    and isinstance(ordinal, int)
                    and isinstance(source_name, int)
                ):
                    destinations.append(
                        (
                            target,
                            destination_name,
                            ordinal,
                            source_name,
                        )
                    )
        return destinations

    def outgoing(node_id: int) -> list[tuple[int, int]]:
        return [
            (target, ordinal)
            for target, _destination_name, ordinal, _source_name
            in outgoing_edges(node_id)
        ]

    def nested_type(node_id: int, type_name: str) -> bool:
        return any(
            item.get("$type") == type_name
            for item in _walk(node_by_id.get(node_id, {}))
        )

    def reachable(starts: set[int]) -> set[int]:
        visited = set(starts)
        pending = list(starts)
        while pending:
            current = pending.pop()
            for target, _ in outgoing(current):
                if target in visited:
                    continue
                visited.add(target)
                pending.append(target)
        return visited

    functional_clue_count = 0
    clue_availability_facts: dict[str, str] = {}
    if handoff is not None and require_functional_clues:
        clue_event_by_name = {
            event.get("clueName", {}).get("$value"): event
            for event in clue_events
        }
        for clue in handoff.get("clues", []):
            clue_name = clue.get("id")
            fact_name = clue.get("fact")
            event = clue_event_by_name.get(clue_name)
            availability_fact = (
                event.get("factName", {}).get("$value")
                if isinstance(event, dict)
                else None
            )
            has_distinct_availability_fact = (
                isinstance(availability_fact, str)
                and bool(availability_fact)
                and availability_fact != fact_name
            )
            if isinstance(availability_fact, str):
                clue_availability_facts[str(clue_name)] = availability_fact
            if not has_distinct_availability_fact:
                errors.append(
                    f"Clue {clue_name!r} must use a transient availability "
                    "fact distinct from its completion fact"
                )
            target = (
                event.get("clueEntity", {})
                .get("dynamicEntityUniqueName", {})
                .get("$value")
                if isinstance(event, dict)
                else None
            )
            scan_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                for item in _walk(node)
                if item.get("$type") == "questScan_ConditionType"
                and item.get("eventType") == "Finished"
                and item.get("objectRef", {})
                .get("dynamicEntityUniqueName", {})
                .get("$value")
                    == target
            }
            validity_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if any(
                    item.get("$type") == "questPauseConditionNodeDefinition"
                    for item in _walk(node)
                )
                and any(
                    item.get("$type") == "questLogicalCondition"
                    and item.get("operation") == "AND"
                    and any(
                        condition.get("$type")
                        == "questVarComparison_ConditionType"
                        and condition.get("comparisonType") == "Greater"
                        and condition.get("factName") == availability_fact
                        and condition.get("value") == 0
                        for condition in _walk(item)
                    )
                    and any(
                        condition.get("$type")
                        == "scnBraindanceLayer_ConditionType"
                        and condition.get("layer") == clue.get("layer")
                        and isinstance(
                            condition.get("sceneFile", {})
                            .get("DepotPath", {})
                            .get("$value"),
                            str,
                        )
                        and condition["sceneFile"]["DepotPath"]["$value"]
                        not in {"", "0"}
                        for condition in _walk(item)
                    )
                    for item in _walk(node)
                )
            }
            wrong_layers = {
                candidate
                for candidate in ("Visual", "Audio", "Thermal")
                if candidate != clue.get("layer")
            }
            invalidity_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if any(
                    item.get("$type") == "questPauseConditionNodeDefinition"
                    for item in _walk(node)
                )
                and any(
                    item.get("$type") == "questLogicalCondition"
                    and item.get("operation") == "OR"
                    and any(
                        condition.get("$type")
                        == "questVarComparison_ConditionType"
                        and condition.get("comparisonType") == "LessOrEqual"
                        and condition.get("factName") == availability_fact
                        and condition.get("value") == 0
                        for condition in _walk(item)
                    )
                    and wrong_layers.issubset(
                        {
                            condition.get("layer")
                            for condition in _walk(item)
                            if condition.get("$type")
                            == "scnBraindanceLayer_ConditionType"
                            and isinstance(
                                condition.get("sceneFile", {})
                                .get("DepotPath", {})
                                .get("$value"),
                                str,
                            )
                            and condition["sceneFile"]["DepotPath"]["$value"]
                            not in {"", "0"}
                        }
                    )
                    for item in _walk(node)
                )
            }
            target_prop = (
                spawned_prop_by_dynamic_name.get(target)
                if isinstance(target, str)
                else None
            )
            target_prop_id = (
                target_prop.get("propId", {}).get("id")
                if isinstance(target_prop, dict)
                else None
            )
            focus_choice_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if node.get("$type") == "scnChoiceNode"
                and node.get("choiceFlags") == "IsFocusClue"
                and node.get("mode") == "attachToProp"
                and node.get("atpParams", {})
                .get("propId", {})
                .get("id")
                == target_prop_id
                and any(
                    option.get("isSingleChoice") == 1
                    and any(
                        tag.get("$value")
                        == "ChoiceCaptionParts.Inspect"
                        for tag in option.get("iconTagIds", [])
                    )
                    for option in node.get("options", [])
                )
            }
            cut_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if node.get("$type") == "scnCutControlNode"
            }
            inspected_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if any(
                    item.get("$type") == "ToggleFocusClueEvent"
                    and item.get("investigationState") == "INSPECTED"
                    and item.get("isEnabled") == 1
                    and item.get("updatePS") == 1
                    for item in _walk(node)
                )
                and any(
                    item.get("$type") == "questEventManagerNodeDefinition"
                    and item.get("managerName") == "FocusClueManager"
                    and item.get("componentName", {}).get("$value")
                    == "scanning"
                    and item.get("PSClassName", {}).get("$value")
                    == "gameScanningComponentPS"
                    and item.get("objectRef", {})
                    .get("dynamicEntityUniqueName", {})
                    .get("$value")
                    == target
                    for item in _walk(node)
                )
            }
            discovered_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if any(
                    item.get("$type")
                    == "questDiscoverBraindanceClue_NodeType"
                    and item.get("clueName", {}).get("$value") == clue_name
                    for item in _walk(node)
                )
            }
            fact_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if any(
                    item.get("$type") == "questSetVar_NodeType"
                    and item.get("factName") == fact_name
                    and item.get("setExactValue") == 1
                    and item.get("value") == 1
                    for item in _walk(node)
                )
            }
            scanning_enable_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if any(
                    item.get("$type")
                    == "questEnableScanning_NodeType"
                    and item.get("enable") == 1
                    and item.get("objectRef", {})
                    .get("dynamicEntityUniqueName", {})
                    .get("$value")
                    == target
                    for item in _walk(node)
                )
            }
            scanning_disable_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if any(
                    item.get("$type")
                    == "questEnableScanning_NodeType"
                    and item.get("enable") == 0
                    and item.get("objectRef", {})
                    .get("dynamicEntityUniqueName", {})
                    .get("$value")
                    == target
                    for item in _walk(node)
                )
            }
            not_inspected_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if any(
                    item.get("$type") == "ToggleFocusClueEvent"
                    and item.get("investigationState")
                    == "NOT_INSPECTED"
                    and item.get("isEnabled") == 1
                    and item.get("updatePS") == 1
                    for item in _walk(node)
                )
                and any(
                    item.get("$type")
                    == "questEventManagerNodeDefinition"
                    and item.get("managerName")
                    == "FocusClueManager"
                    and item.get("componentName", {}).get("$value")
                    == "scanning"
                    and item.get("PSClassName", {}).get("$value")
                    == "gameScanningComponentPS"
                    and item.get("objectRef", {})
                    .get("dynamicEntityUniqueName", {})
                    .get("$value")
                    == target
                    for item in _walk(node)
                )
            }
            reactivation_sections = {
                node_id
                for node_id, node in node_by_id.items()
                if node.get("$type") == "scnSectionNode"
                and node.get("isFocusClue") == 1
            }
            reactivation_hubs = {
                node_id
                for node_id, node in node_by_id.items()
                if node.get("$type") == "scnHubNode"
            }
            start_nodes = {
                node_id
                for node_id, node in node_by_id.items()
                if node.get("$type") == "scnStartNode"
            }

            def has_edge(
                source: int,
                destination: int,
                *,
                destination_name: int,
                ordinal: int,
                source_name: int,
            ) -> bool:
                return (
                    destination,
                    destination_name,
                    ordinal,
                    source_name,
                ) in outgoing_edges(source)

            vanilla_focus_topology = False
            for scan_node in scan_nodes:
                bootstrap_nodes = {
                    enable_node
                    for enable_node in scanning_enable_nodes
                    if has_edge(
                        enable_node,
                        scan_node,
                        destination_name=0,
                        ordinal=1,
                        source_name=0,
                    )
                    and any(
                        has_edge(
                            start_node,
                            enable_node,
                            destination_name=0,
                            ordinal=1,
                            source_name=0,
                        )
                        for start_node in start_nodes
                    )
                    and any(
                        has_edge(
                            enable_node,
                            seed_node,
                            destination_name=0,
                            ordinal=1,
                            source_name=0,
                        )
                        for seed_node in not_inspected_nodes
                    )
                }
                if not bootstrap_nodes:
                    continue
                scan_validity_nodes = {
                    target_node
                    for (
                        target_node,
                        destination_name,
                        ordinal,
                        source_name,
                    ) in outgoing_edges(scan_node)
                    if target_node in validity_nodes
                    and destination_name == 0
                    and ordinal == 1
                    and source_name == 0
                }
                for validity_node in scan_validity_nodes:
                    reenable_nodes = {
                        target_node
                        for (
                            target_node,
                            destination_name,
                            ordinal,
                            source_name,
                        ) in outgoing_edges(validity_node)
                        if target_node in scanning_enable_nodes
                        and destination_name == 0
                        and ordinal == 1
                        and source_name == 0
                    }
                    invalid_nodes = {
                        target_node
                        for (
                            target_node,
                            destination_name,
                            ordinal,
                            source_name,
                        ) in outgoing_edges(validity_node)
                        if target_node in invalidity_nodes
                        and destination_name == 0
                        and ordinal == 1
                        and source_name == 0
                    }
                    for reenable_node in reenable_nodes:
                        choice_nodes = {
                            target_node
                            for (
                                target_node,
                                destination_name,
                                ordinal,
                                source_name,
                            ) in outgoing_edges(reenable_node)
                            if target_node in focus_choice_nodes
                            and destination_name == 0
                            and ordinal == 0
                            and source_name == 0
                        }
                        for choice_node in choice_nodes:
                            success_cut_nodes = {
                                target_node
                                for (
                                    target_node,
                                    destination_name,
                                    ordinal,
                                    source_name,
                                ) in outgoing_edges(choice_node)
                                if target_node in cut_nodes
                                and destination_name == 0
                                and ordinal == 0
                                and source_name == 0
                            }
                            for invalid_node in invalid_nodes:
                                invalidation_loop = any(
                                    has_edge(
                                        invalid_node,
                                        disable_node,
                                        destination_name=0,
                                        ordinal=1,
                                        source_name=0,
                                    )
                                    and any(
                                        has_edge(
                                            disable_node,
                                            reset_cut_node,
                                            destination_name=0,
                                            ordinal=0,
                                            source_name=0,
                                        )
                                        and has_edge(
                                            reset_cut_node,
                                            validity_node,
                                            destination_name=0,
                                            ordinal=1,
                                            source_name=0,
                                        )
                                        and has_edge(
                                            reset_cut_node,
                                            choice_node,
                                            destination_name=1,
                                            ordinal=0,
                                            source_name=1,
                                        )
                                        for reset_cut_node in cut_nodes
                                    )
                                    for disable_node
                                    in scanning_disable_nodes
                                )
                                if not invalidation_loop:
                                    continue
                                for success_cut_node in success_cut_nodes:
                                    stops_invalidity = (
                                        has_edge(
                                            success_cut_node,
                                            invalid_node,
                                            destination_name=0,
                                            ordinal=0,
                                            source_name=1,
                                        )
                                        and has_edge(
                                            success_cut_node,
                                            invalid_node,
                                            destination_name=1026,
                                            ordinal=0,
                                            source_name=1,
                                        )
                                    )
                                    if not stops_invalidity:
                                        continue
                                    success_inspected_nodes = {
                                        inspected_node
                                        for inspected_node
                                        in inspected_nodes
                                        if has_edge(
                                            success_cut_node,
                                            inspected_node,
                                            destination_name=0,
                                            ordinal=1,
                                            source_name=0,
                                        )
                                    }
                                    completion_reactivates = any(
                                        has_edge(
                                            inspected_node,
                                            discovered_node,
                                            destination_name=0,
                                            ordinal=1,
                                            source_name=0,
                                        )
                                        and any(
                                            has_edge(
                                                discovered_node,
                                                fact_node,
                                                destination_name=0,
                                                ordinal=1,
                                                source_name=0,
                                            )
                                            and any(
                                                has_edge(
                                                    fact_node,
                                                    section_node,
                                                    destination_name=0,
                                                    ordinal=0,
                                                    source_name=0,
                                                )
                                                and any(
                                                    has_edge(
                                                        section_node,
                                                        hub_node,
                                                        destination_name=0,
                                                        ordinal=0,
                                                        source_name=0,
                                                    )
                                                    and has_edge(
                                                        hub_node,
                                                        choice_node,
                                                        destination_name=2,
                                                        ordinal=0,
                                                        source_name=0,
                                                    )
                                                    for hub_node
                                                    in reactivation_hubs
                                                )
                                                for section_node
                                                in reactivation_sections
                                            )
                                            for fact_node in fact_nodes
                                        )
                                        for discovered_node
                                        in discovered_nodes
                                        for inspected_node
                                        in success_inspected_nodes
                                    )
                                    if completion_reactivates:
                                        vanilla_focus_topology = True
                                        break
                                if vanilla_focus_topology:
                                    break
                            if vanilla_focus_topology:
                                break
                        if vanilla_focus_topology:
                            break
                    if vanilla_focus_topology:
                        break
                if vanilla_focus_topology:
                    break
            contract_reachable = reachable(scan_nodes)
            functional = bool(
                isinstance(target, str)
                and target in spawned_prop_dynamic_names
                and has_distinct_availability_fact
                and scan_nodes
                and validity_nodes
                and invalidity_nodes
                and focus_choice_nodes
                and cut_nodes
                and inspected_nodes
                and discovered_nodes
                and fact_nodes
                and vanilla_focus_topology
                and contract_reachable & inspected_nodes
                and contract_reachable & discovered_nodes
                and contract_reachable & fact_nodes
            )
            if functional:
                functional_clue_count += 1
            else:
                errors.append(
                    f"Clue {clue_name!r} has no complete scan, availability/"
                    "layer focus choice, invalidation/cut loop, inspected, "
                    "discovered, and fact contract"
                )

    exit_points = root.get("exitPoints", [])
    exit_node_ids = {
        point.get("nodeId", {}).get("id")
        for point in exit_points
        if isinstance(point, dict)
        and isinstance(point.get("nodeId", {}).get("id"), int)
    }
    has_declared_exit = isinstance(exit_points, list) and bool(exit_points)
    if not has_declared_exit:
        errors.append("Scene has no exit point")
    elif require_functional_exit and not exit_node_ids:
        errors.append("Scene exit point has no target node")
    elif require_functional_exit and any(
        node_by_id.get(node_id, {}).get("$type") != "scnEndNode"
        for node_id in exit_node_ids
    ):
        errors.append("Scene exit points do not target End nodes")

    finish_node_ids = {
        node_id
        for node_id in node_by_id
        if nested_type(node_id, "questEnableBraindanceFinish_NodeType")
    }
    if require_functional_exit and not finish_node_ids:
        errors.append("Scene never enables the braindance Finish action")

    exit_action_node_ids = {
        node_id
        for node_id in node_by_id
        if any(
            item.get("$type") == "questInputAction_ConditionType"
            and item.get("inputAction", {}).get("$value")
            == "ExitBraindance"
            for item in _walk(node_by_id[node_id])
        )
    }
    if require_functional_exit and not exit_action_node_ids:
        errors.append("Scene does not consume the ExitBraindance action")

    finish_reachable = reachable(finish_node_ids)
    if (
        require_functional_exit
        and finish_node_ids
        and exit_action_node_ids
        and not (finish_reachable & exit_action_node_ids)
    ):
        errors.append(
            "Braindance Finish UI cannot reach the ExitBraindance condition"
        )

    exit_reachable = reachable(exit_action_node_ids)
    correct_end_edge = any(
        target in exit_node_ids
        and ordinal == 0
        and source in exit_reachable
        for source in exit_reachable
        for target, ordinal in outgoing(source)
    )
    if (
        require_functional_exit
        and exit_action_node_ids
        and exit_node_ids
        and not correct_end_edge
    ):
        errors.append(
            "ExitBraindance cannot reach a registered End at input ordinal 0"
        )

    rewind_node_ids = {
        node_id
        for node_id, node in node_by_id.items()
        if node.get("$type") == "scnRewindableSectionNode"
    }
    delay_node_ids = {
        node_id
        for node_id in node_by_id
        if nested_type(node_id, "questRealtimeDelay_ConditionType")
    }
    rewind_loop = any(
        delay in delay_node_ids
        and delay_ordinal == 1
        and any(
            target == rewind and ordinal == 0
            for target, ordinal in outgoing(delay)
        )
        for rewind in rewind_node_ids
        for delay, delay_ordinal in outgoing(rewind)
    )
    if require_functional_exit and rewind_node_ids and not rewind_loop:
        errors.append(
            "Rewindable section has no delayed loop back to input ordinal 0"
        )

    exit_audio = any(
        item.get("$type") == "questAudioMixNodeType"
        and item.get("mixSignpost", {}).get("$value")
        == "exit_braindance"
        for node_id in exit_reachable
        for item in _walk(node_by_id.get(node_id, {}))
    )
    if (
        require_functional_exit
        and exit_action_node_ids
        and not exit_audio
    ):
        errors.append("ExitBraindance path has no exit_braindance audio mix")

    normal_exit_present = (
        bool(
            exit_node_ids
            and finish_node_ids
            and exit_action_node_ids
            and (finish_reachable & exit_action_node_ids)
            and correct_end_edge
        )
        if require_functional_exit
        else has_declared_exit
    )
    interruption_scenarios = root.get("interruptionScenarios", [])
    enabled_interruptions = [
        scenario
        for scenario in interruption_scenarios
        if isinstance(scenario, dict) and scenario.get("enabled") == 1
    ]
    rid_resources = root.get("ridResources")
    if not isinstance(rid_resources, list) or len(rid_resources) != 1:
        errors.append("Scene must link exactly one authored RID resource")
    return {
        "schema_version": 1,
        "kind": "ghostline_braindance_scene_audit",
        "ok": not errors,
        "errors": errors,
        "type_counts": type_counts,
        "camera_refs": camera_refs,
        "visibility_targets": visibility_targets,
        "clue_layers": sorted(layer for layer in layers if isinstance(layer, str)),
        "clue_entities": clue_entities,
        "functional_clue_count": functional_clue_count,
        "clue_availability_facts": clue_availability_facts,
        "root_motion_samples": root_motion_samples,
        "rewindable": type_counts.get("scnRewindableSectionNode", 0) > 0,
        "layer_switching": type_counts.get(
            "scneventsBraindanceVisibilityEvent", 0
        )
        > 0,
        "normal_exit_present": normal_exit_present,
        "finish_action_enabled": bool(finish_node_ids),
        "exit_action_consumed": bool(exit_action_node_ids),
        "rewind_loop_present": rewind_loop,
        "interruption_scenario_present": bool(interruption_scenarios),
        "enabled_interruption_scenarios": len(enabled_interruptions),
        "normal_exit_cleanup": normal_exit_present and exit_audio,
        "interrupted_cleanup": False,
    }


def link_quest_document(
    quest_document: dict[str, Any],
    *,
    scene_depot_path: str,
    scene_origin: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    result = copy.deepcopy(quest_document)
    root = _root(result, "questQuestPhaseResource")
    scene_nodes = [
        value
        for value in _walk(root)
        if value.get("$type") == "questSceneNodeDefinition"
    ]
    if len(scene_nodes) != 1:
        raise BraindancePipelineError(
            f"Quest template must contain exactly one scene node; found "
            f"{len(scene_nodes)}"
        )
    node = scene_nodes[0]
    scene_file = node.get("sceneFile")
    if not isinstance(scene_file, dict):
        raise BraindancePipelineError("Quest scene node has no sceneFile")
    scene_file["DepotPath"] = {
        "$type": "ResourcePath",
        "$storage": "string",
        "$value": scene_depot_path,
    }
    scene_file["Flags"] = "Default"
    location = node.get("sceneLocation")
    if not isinstance(location, dict):
        raise BraindancePipelineError("Quest scene node has no sceneLocation")
    if location.get("$type") == "scnWorldMarker":
        node_ref = location.get("nodeRef")
        if not isinstance(node_ref, dict):
            raise BraindancePipelineError(
                "Quest scene node world marker has no nodeRef"
            )
        node_ref["$type"] = "NodeRef"
        node_ref["$storage"] = "string"
        node_ref["$value"] = scene_origin
    else:
        location["$type"] = "NodeRef"
        location["$storage"] = "string"
        location["$value"] = scene_origin
    pause_count = sum(
        1
        for value in _walk(root)
        if value.get("$type") == "questPauseConditionNodeDefinition"
    )
    if pause_count < 1:
        raise BraindancePipelineError(
            "Quest braindance template needs at least one pause/cleanup gate"
        )
    return result, {
        "schema_version": 1,
        "kind": "ghostline_braindance_quest_link_report",
        "scene_depot_path": scene_depot_path,
        "scene_origin": scene_origin,
        "scene_nodes": 1,
        "pause_condition_nodes": pause_count,
    }


def _safe_depot_path(value: str) -> Path:
    normalized = value.replace("\\", "/")
    path = Path(normalized)
    if (
        path.is_absolute()
        or ".." in path.parts
        or not path.parts
        or path.parts[0] not in {"mod", "base"}
    ):
        raise BraindancePipelineError(f"Unsafe depot path: {value}")
    return path


def package_assets(
    mappings: list[tuple[Path, str]],
    *,
    depot_root: Path,
) -> dict[str, Any]:
    root = depot_root.resolve()
    entries: list[dict[str, Any]] = []
    seen: set[str] = set()
    for source, depot_path in mappings:
        if not source.is_file():
            raise BraindancePipelineError(f"Package source does not exist: {source}")
        relative = _safe_depot_path(depot_path)
        key = relative.as_posix().casefold()
        if key in seen:
            raise BraindancePipelineError(f"Duplicate package depot path: {depot_path}")
        seen.add(key)
        target = (root / relative).resolve()
        try:
            target.relative_to(root)
        except ValueError as exc:
            raise BraindancePipelineError(
                f"Package target escapes depot root: {depot_path}"
            ) from exc
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.resolve() != target:
            shutil.copy2(source, target)
        source_hash = file_sha256(source)
        target_hash = file_sha256(target)
        if source_hash != target_hash:
            raise BraindancePipelineError(
                f"Packaged file hash mismatch: {depot_path}"
            )
        entries.append(
            {
                "source": str(source.resolve()),
                "depot_path": relative.as_posix(),
                "target": str(target),
                "bytes": target.stat().st_size,
                "sha256": target_hash,
            }
        )
    return {
        "schema_version": 1,
        "kind": "ghostline_braindance_package_manifest",
        "depot_root": str(root),
        "entries": entries,
    }


def init_runtime_evidence(
    *,
    name: str,
    package_manifest: dict[str, Any],
) -> dict[str, Any]:
    hashes = {
        entry["depot_path"]: entry["sha256"]
        for entry in package_manifest.get("entries", [])
    }
    return {
        "schema_version": 1,
        "kind": "ghostline_braindance_runtime_evidence",
        "name": name,
        "package_hashes": hashes,
        "cases": {
            case: {"status": "pending", "notes": None, "recorded_at": None}
            for case in RUNTIME_CASES
        },
    }


def record_runtime_case(
    evidence: dict[str, Any],
    *,
    case: str,
    passed: bool,
    notes: str,
) -> dict[str, Any]:
    if case not in RUNTIME_CASES:
        raise BraindancePipelineError(f"Unknown runtime case: {case}")
    result = copy.deepcopy(evidence)
    cases = result.get("cases")
    if not isinstance(cases, dict) or case not in cases:
        raise BraindancePipelineError("Runtime evidence has an invalid case table")
    cases[case] = {
        "status": "passed" if passed else "failed",
        "notes": notes,
        "recorded_at": datetime.now(UTC).isoformat(),
    }
    return result


def verify_runtime_evidence(
    evidence: dict[str, Any],
    *,
    depot_root: Path,
) -> dict[str, Any]:
    errors: list[str] = []
    hashes = evidence.get("package_hashes")
    if not isinstance(hashes, dict) or not hashes:
        errors.append("Runtime evidence has no package hashes")
        hashes = {}
    for depot_path, expected_hash in hashes.items():
        target = depot_root / _safe_depot_path(depot_path)
        if not target.is_file():
            errors.append(f"Runtime package file is missing: {depot_path}")
        elif file_sha256(target) != expected_hash:
            errors.append(f"Runtime package hash changed: {depot_path}")
    cases = evidence.get("cases")
    if not isinstance(cases, dict):
        errors.append("Runtime evidence has no cases")
        cases = {}
    for case in RUNTIME_CASES:
        status = cases.get(case, {}).get("status")
        if status != "passed":
            errors.append(f"Runtime case is not passed: {case} ({status})")
    return {
        "schema_version": 1,
        "kind": "ghostline_braindance_runtime_verification",
        "ok": not errors,
        "errors": errors,
        "package_hash_count": len(hashes),
        "passed_cases": sum(
            1
            for case in RUNTIME_CASES
            if cases.get(case, {}).get("status") == "passed"
        ),
        "required_cases": len(RUNTIME_CASES),
    }


def _mapping(value: str) -> tuple[Path, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("mapping must be SOURCE=DEPOT_PATH")
    source, depot = value.split("=", 1)
    return Path(source), depot


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    scene = commands.add_parser("link-scene")
    scene.add_argument("--scene-template", type=Path, required=True)
    scene.add_argument("--rid-json", type=Path, required=True)
    scene.add_argument("--handoff", type=Path, required=True)
    scene.add_argument("--rid-depot-path", required=True)
    scene.add_argument("--scene-origin", required=True)
    scene.add_argument("--camera-ref", required=True)
    scene.add_argument("--scene-depot-path")
    scene.add_argument("--output", type=Path, required=True)
    scene.add_argument("--binary-output", type=Path)
    scene.add_argument("--wolvenkit", type=Path)
    scene.add_argument("--report", type=Path)
    quest = commands.add_parser("link-quest")
    quest.add_argument("--quest-template", type=Path, required=True)
    quest.add_argument("--scene-depot-path", required=True)
    quest.add_argument("--scene-origin", required=True)
    quest.add_argument("--output", type=Path, required=True)
    quest.add_argument("--binary-output", type=Path)
    quest.add_argument("--wolvenkit", type=Path)
    quest.add_argument("--report", type=Path)
    audit = commands.add_parser("audit-scene")
    audit.add_argument("--scene", type=Path, required=True)
    audit.add_argument("--handoff", type=Path)
    package = commands.add_parser("package")
    package.add_argument("--asset", type=_mapping, action="append", required=True)
    package.add_argument(
        "--depot-root",
        type=Path,
        default=ROOT / "source" / "archive",
    )
    package.add_argument("--manifest", type=Path, required=True)
    runtime_init = commands.add_parser("runtime-init")
    runtime_init.add_argument("--name", required=True)
    runtime_init.add_argument("--package-manifest", type=Path, required=True)
    runtime_init.add_argument("--output", type=Path, required=True)
    runtime_record = commands.add_parser("runtime-record")
    runtime_record.add_argument("--evidence", type=Path, required=True)
    runtime_record.add_argument("--case", choices=RUNTIME_CASES, required=True)
    outcome = runtime_record.add_mutually_exclusive_group(required=True)
    outcome.add_argument("--passed", action="store_true")
    outcome.add_argument("--failed", action="store_true")
    runtime_record.add_argument("--notes", required=True)
    runtime_verify = commands.add_parser("runtime-verify")
    runtime_verify.add_argument("--evidence", type=Path, required=True)
    runtime_verify.add_argument("--depot-root", type=Path, required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "link-scene":
        document, report = link_scene_document(
            load_json(args.scene_template),
            load_json(args.rid_json),
            load_json(args.handoff),
            rid_depot_path=args.rid_depot_path,
            scene_origin=args.scene_origin,
            camera_ref=args.camera_ref,
            scene_depot_path=args.scene_depot_path,
        )
        write_json(args.output, document)
        if args.binary_output:
            report["binary"] = deserialize_cr2w_json(
                args.output,
                args.binary_output,
                wolvenkit=find_wolvenkit(args.wolvenkit),
            )
        if args.report:
            write_json(args.report, report)
        print(json.dumps(report, indent=2))
        return 0
    if args.command == "link-quest":
        document, report = link_quest_document(
            load_json(args.quest_template),
            scene_depot_path=args.scene_depot_path,
            scene_origin=args.scene_origin,
        )
        write_json(args.output, document)
        if args.binary_output:
            report["binary"] = deserialize_cr2w_json(
                args.output,
                args.binary_output,
                wolvenkit=find_wolvenkit(args.wolvenkit),
            )
        if args.report:
            write_json(args.report, report)
        print(json.dumps(report, indent=2))
        return 0
    if args.command == "audit-scene":
        report = audit_scene_document(
            load_json(args.scene),
            handoff=load_json(args.handoff) if args.handoff else None,
        )
        print(json.dumps(report, indent=2))
        return 0 if report["ok"] else 1
    if args.command == "package":
        report = package_assets(args.asset, depot_root=args.depot_root)
        write_json(args.manifest, report)
        print(json.dumps(report, indent=2))
        return 0
    if args.command == "runtime-init":
        evidence = init_runtime_evidence(
            name=args.name,
            package_manifest=load_json(args.package_manifest),
        )
        write_json(args.output, evidence)
        print(json.dumps(evidence, indent=2))
        return 0
    if args.command == "runtime-record":
        evidence = record_runtime_case(
            load_json(args.evidence),
            case=args.case,
            passed=args.passed,
            notes=args.notes,
        )
        write_json(args.evidence, evidence)
        print(json.dumps(evidence["cases"][args.case], indent=2))
        return 0
    if args.command == "runtime-verify":
        report = verify_runtime_evidence(
            load_json(args.evidence),
            depot_root=args.depot_root,
        )
        print(json.dumps(report, indent=2))
        return 0 if report["ok"] else 1
    raise BraindancePipelineError(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BraindancePipelineError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
