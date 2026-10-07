"""Braindance compatibility CLI and public entry points."""
from __future__ import annotations
import argparse
import copy
import json
import math
import sys
from pathlib import Path
from typing import Any, Iterable
from braindance_support.scene_types import BraindancePipelineError as BraindancePipelineError, _actor_entity_reference as _actor_entity_reference, _cname as _cname, _fnv1a32 as _fnv1a32, _root as _root, _serial as _serial, _tag_signature as _tag_signature, _walk as _walk
from braindance_support.publication import ROOT as ROOT, RUNTIME_CASES as RUNTIME_CASES, deserialize_cr2w_json as deserialize_cr2w_json, find_wolvenkit as find_wolvenkit, init_runtime_evidence as init_runtime_evidence, load_json as load_json, package_assets as package_assets, record_runtime_case as record_runtime_case, verify_runtime_evidence as verify_runtime_evidence, write_json as write_json
from braindance_support.clues import _configure_clue_contract as _configure_clue_contract, _deterministic_scene_event_id as _deterministic_scene_event_id
from braindance_support.scene_audit import audit_scene_document as audit_scene_document
from braindance_support.clues import _BRAINDANCE_LAYER_UNLOCKS as _BRAINDANCE_LAYER_UNLOCKS, _clue_attach_event as _clue_attach_event, _clue_audio_duration_event as _clue_audio_duration_event, _clue_availability_fact as _clue_availability_fact, _clue_contract_aux_node_ids as _clue_contract_aux_node_ids, _clue_contract_node_ids as _clue_contract_node_ids, _clue_cut_control_node as _clue_cut_control_node, _clue_discovered_node as _clue_discovered_node, _clue_fact_node as _clue_fact_node, _clue_focus_state_node as _clue_focus_state_node, _clue_inspected_node as _clue_inspected_node, _clue_invalidity_node as _clue_invalidity_node, _clue_reactivate_hub_node as _clue_reactivate_hub_node, _clue_reactivation_section_node as _clue_reactivation_section_node, _clue_scan_node as _clue_scan_node, _clue_scanning_bootstrap_node as _clue_scanning_bootstrap_node, _clue_scanning_enabled_node as _clue_scanning_enabled_node, _clue_success_cut_control_node as _clue_success_cut_control_node, _clue_validity_node as _clue_validity_node, _configure_focus_clue_options as _configure_focus_clue_options, _focus_clue_choice_node as _focus_clue_choice_node, audit_clues as audit_clues
from braindance_support.publication import WOLVENKIT_CLI as WOLVENKIT_CLI, _safe_depot_path as _safe_depot_path, file_sha256 as file_sha256
from braindance_support.scene_graph import SceneGraphIndex as SceneGraphIndex
from braindance_support.scene_types import _SceneHandleAllocator as _SceneHandleAllocator, _dynamic_entity_reference as _dynamic_entity_reference, _quest_socket as _quest_socket, _scene_input_socket as _scene_input_socket, _scene_output_socket as _scene_output_socket, _scene_quest_node as _scene_quest_node


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
        default=ROOT / "projects/ghostline/source/archive",
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
