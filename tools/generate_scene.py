#!/usr/bin/env python3
"""Generate Ghostline .scene CR2W-JSON from a compact scene spec.

The generator emits raw CR2W-JSON under the owning project's source/raw.
Packed writes require read-back parity, with a WolvenKit fallback for layouts
that the template-backed native writer cannot preserve.
"""

from __future__ import annotations

import argparse
import copy
import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator

from cr2w_helpers import load_json, print_json
from scene_validation import validate_reference_tables
from ghostline_red import DEFAULT_RED_CLI, DEFAULT_RED_SCHEMA


DEFAULT_SPEC = Path(
    "projects/ghostline/quests/gq000/implementation/scenes/"
    "patch-meet.scene-spec.json"
)
DEFAULT_EXPORTED_DATETIME = "1970-01-01T00:00:00Z"
UINT32_NONE = 4294967295
PERFORMER_NONE = 4294967040
MAX_INT64 = "9223372036854775807"
FNV64_OFFSET = 0xCBF29CE484222325
FNV64_PRIME = 0x100000001B3
UINT64_MASK = (1 << 64) - 1


@dataclass(frozen=True)
class ActorRef:
    id: int
    key: str
    display: str


class HandleAllocator:
    def __init__(self, start: int = 3) -> None:
        self.next_id = start

    def take(self) -> str:
        value = str(self.next_id)
        self.next_id += 1
        return value

    def wrap(self, data: dict[str, Any]) -> dict[str, Any]:
        return {"HandleId": self.take(), "Data": data}


class SceneBuildError(SystemExit):
    pass


def fnv1a64(value: str) -> int:
    result = FNV64_OFFSET
    for byte in value.encode("utf-8"):
        result ^= byte
        result = (result * FNV64_PRIME) & UINT64_MASK
    return result


def deterministic_event_id(*parts: object) -> str:
    value = fnv1a64(":".join(str(part) for part in parts)) & UINT64_MASK
    if str(value) == MAX_INT64:
        value = (value + 1) & UINT64_MASK
    return str(value)


def deterministic_reserved_ruid(parts: tuple[object, ...], reserved: set[str]) -> str:
    value = fnv1a64(":".join(str(part) for part in parts)) & UINT64_MASK
    for _ in range(1024):
        candidate = str(value)
        if candidate != MAX_INT64 and candidate not in reserved:
            reserved.add(candidate)
            return candidate
        value = (value + 1) & UINT64_MASK
    raise SceneBuildError(f"Could not allocate unique ruid for {':'.join(str(part) for part in parts)}")


def cname(value: str) -> dict[str, Any]:
    return {"$type": "CName", "$storage": "string", "$value": value}


def node_ref(value: str | int, storage: str = "string") -> dict[str, Any]:
    return {"$type": "NodeRef", "$storage": storage, "$value": str(value)}


def resource_path(value: str | int, storage: str = "string", flags: str = "Soft") -> dict[str, Any]:
    return {"DepotPath": {"$type": "ResourcePath", "$storage": storage, "$value": str(value)}, "Flags": flags}


def tweakdbid(value: str | int, storage: str = "string") -> dict[str, Any]:
    return {"$type": "TweakDBID", "$storage": storage, "$value": str(value)}


def actor_id(value: int) -> dict[str, Any]:
    return {"$type": "scnActorId", "id": value}


def performer_id(value: int) -> dict[str, Any]:
    return {"$type": "scnPerformerId", "id": value}


def screenplay_item_id(value: int) -> dict[str, Any]:
    return {"$type": "scnscreenplayItemId", "id": value}


def locstring_id(value: str | int) -> dict[str, Any]:
    return {"$type": "scnlocLocstringId", "ruid": str(value)}


def variant_id(value: str | int) -> dict[str, Any]:
    return {"$type": "scnlocVariantId", "ruid": str(value)}


def scene_node_id(value: int) -> dict[str, Any]:
    return {"$type": "scnNodeId", "id": value}


def scene_time(value: int) -> dict[str, Any]:
    return {"$type": "scnSceneTime", "stu": value}


def empty_entity_ref(ref: str | int = 0, storage: str = "uint64", names: list[str] | None = None) -> dict[str, Any]:
    return {
        "$type": "gameEntityReference",
        "dynamicEntityUniqueName": cname("None"),
        "names": [cname(name) for name in (names or [])],
        "reference": node_ref(ref, storage=storage),
        "sceneActorContextName": cname("None"),
        "slotName": cname("None"),
        "type": "EntityRef",
    }


def input_socket_id(node_id: int, name: int = 0, ordinal: int = 0) -> dict[str, Any]:
    return {
        "$type": "scnInputSocketId",
        "isockStamp": {"$type": "scnInputSocketStamp", "name": name, "ordinal": ordinal},
        "nodeId": scene_node_id(node_id),
    }


def output_socket(
    name: int = 0,
    ordinal: int = 0,
    destinations: list[tuple[int, int, int]] | None = None,
) -> dict[str, Any]:
    return {
        "$type": "scnOutputSocket",
        "destinations": [input_socket_id(node, in_name, in_ordinal) for node, in_name, in_ordinal in destinations or []],
        "stamp": {"$type": "scnOutputSocketStamp", "name": name, "ordinal": ordinal},
    }


def socket_mapping(value: str) -> dict[str, Any]:
    return {"$type": "CName", "$storage": "string", "$value": value}


def quest_socket(alloc: HandleAllocator, name: str, socket_type: str) -> dict[str, Any]:
    return alloc.wrap(
        {
            "$type": "questSocketDefinition",
            "connections": [],
            "name": cname(name),
            "type": socket_type,
        }
    )


def reassign_handle_ids(value: Any, alloc: HandleAllocator) -> None:
    if isinstance(value, dict):
        if "HandleId" in value:
            value["HandleId"] = alloc.take()
        for child in value.values():
            reassign_handle_ids(child, alloc)
    elif isinstance(value, list):
        for child in value:
            reassign_handle_ids(child, alloc)


def path_from_spec(spec: dict[str, Any], key: str) -> Path:
    if key not in spec:
        raise SceneBuildError(f"Spec missing required path field: {key}")
    return Path(str(spec[key]))


def spec_declares_choices(spec: dict[str, Any]) -> bool:
    return bool(spec.get("choice_line_order")) or any(choice.get("options") for choice in spec.get("choices", []))


def expected_file_entry_index(path: str) -> int | None:
    parts = [part for part in path.replace("\\", "/").split("/") if part]
    if len(parts) >= 3 and parts[:2] == ["quests", "minor_quest"]:
        return 2
    if len(parts) >= 3 and parts[:2] == ["quests", "vehicle_metaquest"]:
        return 2
    if len(parts) >= 5 and parts[:2] == ["quests", "street_stories"]:
        return 4
    if len(parts) >= 2 and parts[0] in {"briefings", "codex", "contacts", "internet_sites", "onscreens", "points_of_interest", "tarots"}:
        return 1
    return None


def resolve_file_entry_index(node_spec: dict[str, Any]) -> int:
    if "file_entry_index" in node_spec:
        return int(node_spec["file_entry_index"])
    expected = expected_file_entry_index(str(node_spec["path"]))
    return expected if expected is not None else 1


def actor_lookup(spec: dict[str, Any]) -> dict[str, ActorRef]:
    refs: dict[str, ActorRef] = {}
    for raw_actor in spec.get("actors", []):
        actor = ActorRef(
            id=int(raw_actor["id"]),
            key=str(raw_actor["key"]).casefold(),
            display=str(raw_actor.get("name", raw_actor["key"])),
        )
        refs[actor.key] = actor
        refs[actor.display.casefold()] = actor
    return refs


def load_manifest(spec: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    manifest = load_json(path_from_spec(spec, "manifest"))
    spoken = {str(line["key"]): line for line in manifest.get("spoken_lines", [])}
    choices = {str(line["key"]): line for line in manifest.get("choice_lines", [])}
    if not spoken:
        raise SceneBuildError("Manifest has no spoken_lines")
    if spec_declares_choices(spec) and not choices:
        raise SceneBuildError("Manifest has no choice_lines")
    return spoken, choices


def actor_performer_id(actor_index: int) -> int:
    return actor_index * 256 + 1


def prop_performer_id(prop_index: int) -> int:
    return prop_index * 256 + 2


def euler_angles(value: dict[str, Any]) -> dict[str, Any]:
    return {
        "$type": "EulerAngles",
        "Pitch": float(value.get("pitch", 0)),
        "Roll": float(value.get("roll", 0)),
        "Yaw": float(value.get("yaw", 0)),
    }


def dynamic_entity_ref(dynamic_name: str) -> dict[str, Any]:
    """Build the vanilla EntityRef shape used for scene-spawned performers."""
    value = empty_entity_ref()
    value["dynamicEntityUniqueName"] = cname(dynamic_name)
    return value


def build_fpp_gender_params(event_spec: dict[str, Any]) -> list[dict[str, Any]]:
    params = event_spec.get("fpp_gender_params")
    if not isinstance(params, dict):
        return []
    blend_angles = [
        euler_angles(value)
        for value in params.get("transition_blend_in_trajectory_space_angles", [])
    ]
    end_angles = [
        euler_angles(value)
        for value in params.get("transition_end_input_angles", [])
    ]
    return [
        {
            "$type": "scnfppGenderSpecificParams",
            "genderMask": {"$type": "scnGenderMask", "mask": int(mask)},
            "idleCameraLs": euler_angles({}),
            "idleControlCameraMs": euler_angles({}),
            "transitionBlendInCameraSpace": [],
            "transitionBlendInTrajectorySpaceAngles": copy.deepcopy(blend_angles),
            "transitionEndInputAngles": copy.deepcopy(end_angles),
        }
        for mask in params.get("gender_masks", [2, 1])
    ]


def build_props(
    spec: dict[str, Any], debug_symbols: dict[str, Any]
) -> list[dict[str, Any]]:
    props: list[dict[str, Any]] = []
    for raw_prop in spec.get("props", []):
        prop_index = int(raw_prop["id"])
        node_reference = str(raw_prop["node_ref"])
        props.append(
            {
                "$type": "scnPropDef",
                "animSets": [],
                "cinematicAnimSets": [],
                "communityParams": {
                    "$type": "scnCommunityParams",
                    "entryName": cname("None"),
                    "forceMaxVisibility": 0,
                    "reference": node_ref(0, storage="uint64"),
                },
                "dynamicAnimSets": [],
                "entityAcquisitionPlan": "findInNode",
                "findEntityInEntityParams": {
                    "$type": "scnFindEntityInEntityParams",
                    "actorId": actor_id(UINT32_NONE),
                    "forceMaxVisibility": 0,
                    "itemID": tweakdbid(0, storage="uint64"),
                    "ownershipTransferOptions": {
                        "$type": "scnPropOwnershipTransferOptions",
                        "dettachFromSlot": 1,
                        "removeFromInventory": 1,
                        "type": "TransferToWorkspotSystem_Automatic",
                    },
                    "performerId": performer_id(PERFORMER_NONE),
                    "slotID": tweakdbid(0, storage="uint64"),
                },
                "findEntityInNodeParams": {
                    "$type": "scnFindEntityInNodeParams",
                    "forceMaxVisibility": 0,
                    "nodeRef": node_ref(node_reference),
                },
                "findEntityInWorldParams": {
                    "$type": "scnFindEntityInWorldParams",
                    "actorRef": empty_entity_ref(),
                    "forceMaxVisibility": 0,
                },
                "propId": {"$type": "scnPropId", "id": prop_index},
                "propName": str(raw_prop["name"]),
                "spawnDespawnParams": {
                    "$type": "scnSpawnDespawnEntityParams",
                    "alwaysSpawned": 0,
                    "appearance": cname("None"),
                    "dynamicEntityUniqueName": cname("None"),
                    "findInWorld": 0,
                    "forceMaxVisibility": 0,
                    "isEnabled": 1,
                    "itemOwnerId": performer_id(PERFORMER_NONE),
                    "keepAlive": 0,
                    "prefetchAppearance": 0,
                    "spawnMarker": cname("None"),
                    "spawnMarkerNodeRef": node_ref(0, storage="uint64"),
                    "spawnMarkerType": "Local",
                    "spawnOffset": {
                        "$type": "Transform",
                        "orientation": {
                            "$type": "Quaternion",
                            "i": 0,
                            "j": 0,
                            "k": 0,
                            "r": 1,
                        },
                        "position": {
                            "$type": "Vector4",
                            "W": 0,
                            "X": 0,
                            "Y": 0,
                            "Z": 0,
                        },
                    },
                    "spawnOnStart": 1,
                    "specRecordId": tweakdbid(0, storage="uint64"),
                    "validateSpawnPostion": 1,
                },
                "spawnerParams": {
                    "$type": "scnSpawnerParams",
                    "forceMaxVisibility": 0,
                    "reference": node_ref(0, storage="uint64"),
                },
                "spawnSetParams": {
                    "$type": "scnSpawnSetParams",
                    "entryName": cname("None"),
                    "forceMaxVisibility": 0,
                    "reference": node_ref(0, storage="uint64"),
                },
                "specPropRecordId": tweakdbid(0, storage="uint64"),
            }
        )
        debug_symbols["performersDebugSymbols"].append(
            {
                "$type": "scnPerformerSymbol",
                "editorPerformerId": "0",
                "entityRef": empty_entity_ref(node_reference, storage="string"),
                "performerId": performer_id(prop_performer_id(prop_index)),
            }
        )
    return props


def build_actors(spec: dict[str, Any], base_root: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    if not base_root.get("actors") or not base_root.get("playerActors"):
        raise SceneBuildError("Base scene must contain at least one NPC actor and one player actor shell")

    actors: list[dict[str, Any]] = []
    player_actors: list[dict[str, Any]] = []
    debug_symbols = {
        "$type": "scnDebugSymbols",
        "performersDebugSymbols": [],
        "sceneEventsDebugSymbols": [],
        "sceneNodesDebugSymbols": [],
        "workspotsDebugSymbols": [],
    }

    npc_shell = base_root["actors"][0]
    player_shell = base_root["playerActors"][0]
    for raw_actor in spec.get("actors", []):
        actor_kind = raw_actor.get("kind")
        actor_index = int(raw_actor["id"])
        performer = actor_performer_id(actor_index)
        actor_name = str(raw_actor.get("name", raw_actor["key"]))
        if actor_kind == "community":
            actor = copy.deepcopy(npc_shell)
            actor["actorId"] = actor_id(actor_index)
            actor["actorName"] = actor_name
            actor["acquisitionPlan"] = "community"
            actor["animSets"] = [
                {"$type": "scnSRRefId", "id": int(value)}
                for value in raw_actor.get("rid_anim_sets", [])
            ]
            actor["bodyCinematicAnimSets"] = []
            actor["cyberwareAnimSets"] = []
            actor["cyberwareCinematicAnimSets"] = []
            actor["deformationAnimSets"] = []
            actor["dynamicAnimSets"] = []
            actor["facialAnimSets"] = [
                {"$type": "scnRidFacialAnimSetSRRefId", "id": int(value)}
                for value in raw_actor.get("rid_facial_anim_sets", [])
            ]
            actor["facialCinematicAnimSets"] = []
            actor["communityParams"]["entryName"] = cname(str(raw_actor["entry"]))
            actor["communityParams"]["reference"] = node_ref(str(raw_actor["community_ref"]))
            actor["lipsyncAnimSet"] = {"$type": "scnLipsyncAnimSetSRRefId", "id": int(raw_actor.get("lipsync", actor_index))}
            actor["specAppearance"] = cname(str(raw_actor.get("appearance", "default")))
            actor["specCharacterRecordId"] = tweakdbid(0, storage="uint64")
            actor["voicetagId"] = {"$type": "scnVoicetagId", "id": str(raw_actor.get("voicetag", "0"))}
            actors.append(actor)
            debug_ref = empty_entity_ref(str(raw_actor["community_ref"]), storage="string", names=[str(raw_actor["entry"])])
        elif actor_kind == "player":
            actor = copy.deepcopy(player_shell)
            actor["actorId"] = actor_id(actor_index)
            actor["playerName"] = actor_name
            actor["acquisitionPlan"] = "findInContext"
            actor["animSets"] = [
                {"$type": "scnSRRefId", "id": int(value)}
                for value in raw_actor.get("rid_anim_sets", [])
            ]
            actor["bodyCinematicAnimSets"] = []
            actor["cyberwareAnimSets"] = []
            actor["cyberwareCinematicAnimSets"] = []
            actor["deformationAnimSets"] = []
            actor["dynamicAnimSets"] = []
            actor["facialAnimSets"] = [
                {"$type": "scnRidFacialAnimSetSRRefId", "id": int(value)}
                for value in raw_actor.get("rid_facial_anim_sets", [])
            ]
            actor["facialCinematicAnimSets"] = []
            record = str(raw_actor.get("record", "Character.Player_Puppet_Base"))
            actor["findActorInContextParams"]["contextualName"] = str(raw_actor.get("contextual_name", "Player"))
            actor["findActorInContextParams"]["specRecordId"] = tweakdbid(record)
            actor["lipsyncAnimSet"] = {"$type": "scnLipsyncAnimSetSRRefId", "id": int(raw_actor.get("lipsync", actor_index))}
            actor["specAppearance"] = cname(str(raw_actor.get("appearance", "default")))
            actor["specCharacterRecordId"] = tweakdbid(record)
            actor["specTemplate"] = cname("(None)")
            actor["voicetagId"] = {"$type": "scnVoicetagId", "id": str(raw_actor.get("voicetag", "1103967280742240864"))}
            player_actors.append(actor)
            debug_ref = empty_entity_ref("#player", storage="string")
        elif actor_kind == "spawn":
            actor = copy.deepcopy(npc_shell)
            dynamic_name = str(raw_actor["dynamic_name"])
            actor["actorId"] = actor_id(actor_index)
            actor["actorName"] = actor_name
            actor["acquisitionPlan"] = "spawnDespawn"
            actor["animSets"] = [
                {"$type": "scnSRRefId", "id": int(value)}
                for value in raw_actor.get("rid_anim_sets", [])
            ]
            actor["bodyCinematicAnimSets"] = []
            actor["cyberwareAnimSets"] = []
            actor["cyberwareCinematicAnimSets"] = []
            actor["deformationAnimSets"] = []
            actor["dynamicAnimSets"] = []
            actor["facialAnimSets"] = [
                {"$type": "scnRidFacialAnimSetSRRefId", "id": int(value)}
                for value in raw_actor.get("rid_facial_anim_sets", [])
            ]
            actor["facialCinematicAnimSets"] = []
            # The NPC shell is sourced from a community-acquired actor.  A
            # spawn/despawn actor must not retain that shell's community key:
            # the scene owns it exclusively through its dynamic name/record.
            actor["communityParams"] = {
                "$type": "scnCommunityParams",
                "entryName": cname("None"),
                "forceMaxVisibility": 0,
                "reference": node_ref(0, storage="uint64"),
            }
            actor["lipsyncAnimSet"] = {
                "$type": "scnLipsyncAnimSetSRRefId",
                "id": int(raw_actor.get("lipsync", UINT32_NONE)),
            }
            actor["spawnDespawnParams"] = {
                "$type": "scnSpawnDespawnEntityParams",
                "alwaysSpawned": 1 if raw_actor.get("always_spawned", False) else 0,
                "appearance": cname(str(raw_actor.get("appearance", "default"))),
                "dynamicEntityUniqueName": cname(dynamic_name),
                "findInWorld": 0,
                "forceMaxVisibility": 1
                if raw_actor.get("force_max_visibility", False)
                else 0,
                "isEnabled": 1,
                "itemOwnerId": performer_id(PERFORMER_NONE),
                "keepAlive": 1 if raw_actor.get("keep_alive", False) else 0,
                "prefetchAppearance": 1
                if raw_actor.get("prefetch_appearance", False)
                else 0,
                "spawnMarker": cname("None"),
                "spawnMarkerNodeRef": node_ref(str(raw_actor["spawn_marker"])),
                "spawnMarkerType": str(raw_actor.get("spawn_marker_type", "Global")),
                "spawnOffset": {
                    "$type": "Transform",
                    "orientation": {
                        "$type": "Quaternion",
                        "i": 0,
                        "j": 0,
                        "k": 0,
                        "r": 1,
                    },
                    "position": {
                        "$type": "Vector4",
                        "W": 0,
                        "X": 0,
                        "Y": 0,
                        "Z": 0,
                    },
                },
                "spawnOnStart": 1 if raw_actor.get("spawn_on_start", True) else 0,
                "specRecordId": tweakdbid(str(raw_actor["record"])),
                "validateSpawnPostion": 1
                if raw_actor.get("validate_spawn_position", True)
                else 0,
            }
            actor["specAppearance"] = cname(
                str(raw_actor.get("appearance", "default"))
            )
            actor["specCharacterRecordId"] = tweakdbid(0, storage="uint64")
            actor["voicetagId"] = {
                "$type": "scnVoicetagId",
                "id": str(raw_actor.get("voicetag", "0")),
            }
            actors.append(actor)
            debug_ref = dynamic_entity_ref(dynamic_name)
        else:
            raise SceneBuildError(f"Unsupported actor kind: {actor_kind}")

        debug_symbols["performersDebugSymbols"].append(
            {
                "$type": "scnPerformerSymbol",
                "editorPerformerId": "0",
                "entityRef": debug_ref,
                "performerId": performer_id(performer),
            }
        )

    return actors, player_actors, debug_symbols


def build_resource_refs(spec: dict[str, Any]) -> dict[str, Any]:
    lipsync_path = str(
        spec.get(
            "lipsync_animset",
            r"base\animations\facial\generic\interactive_scene\generic_facial_lipsync_gestures.anims",
        )
    )
    lipsync_ids = []
    for actor in spec.get("actors", []):
        value = actor.get("lipsync")
        if value is None:
            if actor.get("kind") == "spawn":
                continue
            value = actor.get("id", 0)
        if int(value) != UINT32_NONE:
            lipsync_ids.append(int(value))
    count = max(lipsync_ids, default=-1) + 1
    lipsync_refs = [
        {
            "$type": "scnLipsyncAnimSetSRRef",
            "asyncRefLipsyncAnimSet": resource_path(lipsync_path),
            "lipsyncAnimSet": resource_path(0, storage="uint64", flags="Default"),
        }
        for _ in range(count)
    ]
    return {
        "$type": "scnSRRefCollection",
        "cinematicAnimNames": [],
        "cinematicAnimSets": [],
        "dynamicAnimNames": [],
        "dynamicAnimSets": [],
        "gameplayAnimNames": [],
        "gameplayAnimSets": [],
        "lipsyncAnimSets": lipsync_refs,
        "ridAnimationContainers": [],
        "ridAnimations": [
            {
                "$type": "scnRidAnimationSRRef",
                "animationSN": {"$type": "scnRidSerialNumber", "serialNumber": int(ref["serial_number"])},
                "resourceId": {"$type": "scnRidResourceId", "id": int(ref["resource_id"])},
            }
            for ref in spec.get("rid_animations", [])
        ],
        "ridAnimSets": [
            {
                "$type": "scnRidAnimSetSRRef",
                "animations": [
                    {"$type": "scnSRRefId", "id": int(animation_id)}
                    for animation_id in value.get("animations", [])
                ],
            }
            for value in spec.get("rid_anim_sets", [])
        ],
        "ridCameraAnimations": [
            {
                "$type": "scnRidCameraAnimationSRRef",
                "animationSN": {"$type": "scnRidSerialNumber", "serialNumber": int(ref["serial_number"])},
                "resourceId": {"$type": "scnRidResourceId", "id": int(ref["resource_id"])},
            }
            for ref in spec.get("rid_camera_animations", [])
        ],
        "ridCyberwareAnimSets": [],
        "ridDeformationAnimSets": [],
        "ridFacialAnimSets": [
            {
                "$type": "scnRidAnimSetSRRef",
                "animations": [
                    {"$type": "scnSRRefId", "id": int(animation_id)}
                    for animation_id in value.get("animations", [])
                ],
            }
            for value in spec.get("rid_facial_anim_sets", [])
        ],
    }


def rid_marker(node_ref_value: str) -> dict[str, Any]:
    return {
        "$type": "scnMarker",
        "entityRef": empty_entity_ref(),
        "isMounted": 1,
        "localMarkerId": cname("None"),
        "nodeRef": node_ref(node_ref_value),
        "slotName": cname("None"),
        "type": "Global",
    }


def rid_anim_event(
    scene_name: str,
    section_key: str,
    event_index: int,
    event_spec: dict[str, Any],
    actors: dict[str, dict[str, Any]],
    alloc: HandleAllocator,
) -> dict[str, Any]:
    actor = actors[str(event_spec["actor"]).casefold()]
    is_player = bool(event_spec.get("fpp", False))
    event = {
        "$type": "scnPlayRidAnimEvent",
        "actorComponent": cname(str(event_spec.get("component", "body"))),
        "actorHasCollision": 1,
        "actorPlacement": "SceneOrigin",
        "animData": {
            "$type": "scneventsPlayAnimEventExData",
            "basic": {"$type": "scneventsPlayAnimEventData", "blendIn": 0, "blendInCurve": "SinusoidalEaseInOut", "blendOut": 0, "blendOutCurve": "SinusoidalEaseInOut", "clipEnd": 0, "clipFront": 0, "stretch": 1},
            "bodyPartMask": cname("None"),
            "weight": 1,
        },
        "animOriginMarker": rid_marker(str(event_spec["origin"])),
        "animResRefId": {"$type": "scnRidAnimationSRRefId", "id": int(event_spec["anim_ref_id"])},
        "blendInTrajectoryBone": 0,
        "blendOverride": "CopyPitch_CopyYaw",
        "cameraBlendInDuration": 0.5,
        "cameraBlendOutDuration": 0.5,
        "cameraParallaxSpace": "Camera" if is_player else "Trajectory",
        "cameraParallaxWeight": 0,
        "cameraUseTrajectorySpace": 1,
        "convertToAdditive": 0,
        "duration": int(event_spec["duration_ms"]),
        "enableWorldSpaceSmoothing": 1,
        "executionTagFlags": 0,
        "eyesBlendAdditive": 1,
        "FPPControlActive": 1 if is_player else 0,
        "gameplayAnimName": alloc.wrap({"$type": "scnAnimName", "type": "direct", "unk1": [cname("None")], "unk2": []}),
        "genderSpecificParams": build_fpp_gender_params(event_spec),
        "id": {"$type": "scnSceneEventId", "id": deterministic_event_id(scene_name, section_key, f"rid_{event_index}", int(event_spec["anim_ref_id"]))},
        "idleIsMountedWorkspot": 0,
        "isSceneCarrying": 0,
        "lowerFaceBlendAdditive": 1,
        "muteAnimEvents": "0",
        "neckWeight": 1,
        "performer": performer_id(actor_performer_id(actor.id)),
        "pitchLimitBottom": 0,
        "pitchLimitTop": 0,
        "ridVersinon": 5,
        "scalingData": None,
        "startTime": int(event_spec.get("start_time_ms", 0)),
        "stayInScene": 0,
        "type": "0",
        "upperFaceBlendAdditive": 1,
        "vehicleProceduralCameraWeight": 0,
        "yawLimitLeft": 0,
        "yawLimitRight": 0,
    }
    return alloc.wrap(event)


def rid_camera_event(scene_name: str, section_key: str, event_spec: dict[str, Any], alloc: HandleAllocator) -> dict[str, Any]:
    return alloc.wrap({
        "$type": "scneventsPlayRidCameraAnimEvent",
        "activateAsGameCamera": 1,
        "animData": {"$type": "scneventsPlayAnimEventData", "blendIn": 0, "blendInCurve": "Linear", "blendOut": 0, "blendOutCurve": "Linear", "clipEnd": 0, "clipFront": 0, "stretch": 1},
        "animOriginMarker": rid_marker(str(event_spec["origin"])),
        "animSRRefId": {"$type": "scnRidCameraAnimationSRRefId", "id": int(event_spec["camera_ref_id"])},
        "cameraPlacement": "SceneOrigin",
        "cameraRef": node_ref(str(event_spec["camera_ref"])),
        "controlRenderToTextureState": 0,
        "duration": int(event_spec["duration_ms"]),
        "executionTagFlags": 0,
        "id": {"$type": "scnSceneEventId", "id": deterministic_event_id(scene_name, section_key, "rid_camera", int(event_spec["camera_ref_id"]))},
        "markCamerCut": 1,
        "scalingData": None,
        "startTime": int(event_spec.get("start_time_ms", 0)),
        "type": "0",
    })


def camera_event(
    scene_name: str,
    section_key: str,
    event_spec: dict[str, Any],
    alloc: HandleAllocator,
) -> dict[str, Any]:
    """Activate a world camera for a section without playing a RID camera."""
    blend_time = float(event_spec.get("blend_time_seconds", 0))
    if blend_time < 0:
        raise SceneBuildError("camera_event blend_time_seconds cannot be negative")
    duration = int(event_spec["duration_ms"])
    if duration <= 0:
        raise SceneBuildError("camera_event duration_ms must be positive")
    return alloc.wrap(
        {
            "$type": "scneventsCameraEvent",
            "blendTime": blend_time,
            "cameraRef": node_ref(str(event_spec["camera_ref"])),
            "duration": duration,
            "executionTagFlags": 0,
            "id": {
                "$type": "scnSceneEventId",
                "id": deterministic_event_id(
                    scene_name,
                    section_key,
                    "camera",
                    str(event_spec["camera_ref"]),
                ),
            },
            # isBlendIn selects whether this event acquires or releases the
            # referenced world camera. Blend time controls the transition in
            # either direction; zero is a hard cut.
            "isBlendIn": int(bool(event_spec.get("blend_in", True))),
            "scalingData": None,
            "startTime": int(event_spec.get("start_time_ms", 0)),
            "type": "0",
        }
    )


def build_screenplay_store(
    spec: dict[str, Any],
    spoken_manifest: dict[str, dict[str, Any]],
    choice_manifest: dict[str, dict[str, Any]],
    actors: dict[str, ActorRef],
) -> tuple[dict[str, Any], dict[str, int], dict[str, int]]:
    line_ids: dict[str, int] = {}
    option_ids: dict[str, int] = {}
    lines: list[dict[str, Any]] = []
    options: list[dict[str, Any]] = []

    for index, line_key in enumerate(spec["spoken_line_order"]):
        if line_key not in spoken_manifest:
            raise SceneBuildError(f"Spoken line {line_key} not found in manifest")
        line = spoken_manifest[line_key]
        speaker = actors[str(line["speaker"]).casefold()]
        addressee = actors[str(line["addressee"]).casefold()]
        item_id = 1 + index * 256
        line_ids[line_key] = item_id
        female_lipsync = str(line.get("female_lipsync_animation", "None"))
        male_lipsync = str(line.get("male_lipsync_animation", "None"))
        lines.append(
            {
                "$type": "scnscreenplayDialogLine",
                "addressee": actor_id(addressee.id),
                "femaleLipsyncAnimationName": cname(female_lipsync),
                "itemId": screenplay_item_id(item_id),
                "locstringId": locstring_id(line["string_id"]),
                "maleLipsyncAnimationName": cname(male_lipsync),
                "speaker": actor_id(speaker.id),
                "usage": {"$type": "scnscreenplayLineUsage", "playerGenderMask": {"$type": "scnGenderMask", "mask": 3}},
            }
        )

    for index, choice_key in enumerate(spec["choice_line_order"]):
        if choice_key not in choice_manifest:
            raise SceneBuildError(f"Choice line {choice_key} not found in manifest")
        choice = choice_manifest[choice_key]
        item_id = 2 + index * 256
        option_ids[choice_key] = item_id
        options.append(
            {
                "$type": "scnscreenplayChoiceOption",
                "itemId": screenplay_item_id(item_id),
                "locstringId": locstring_id(choice["string_id"]),
                "usage": {"$type": "scnscreenplayOptionUsage", "playerGenderMask": {"$type": "scnGenderMask", "mask": 3}},
            }
        )

    return {"$type": "scnscreenplayStore", "lines": lines, "options": options}, line_ids, option_ids


def build_loc_store(
    spec: dict[str, Any],
    choice_manifest: dict[str, dict[str, Any]],
    spoken_manifest: dict[str, dict[str, Any]] | None = None,
) -> dict[str, Any]:
    loc_store = {"$type": "scnlocLocStoreEmbedded", "vdEntries": [], "vpEntries": []}
    locales = spec.get("choice_locales", ["db_db", "pl_pl", "en_us"])
    reserved_ruids = {
        str(line["string_id"])
        for manifest in (spoken_manifest or {}, choice_manifest)
        for line in manifest.values()
        if "string_id" in line
    }

    def add_loc_variant(choice_key: str, locale: str, loc_id: int, content: str, variant_kind: str) -> None:
        variant = deterministic_reserved_ruid(
            (spec["name"], "choice-loc", choice_key, locale, loc_id, variant_kind),
            reserved_ruids,
        )
        vpe_index = len(loc_store["vpEntries"])
        loc_store["vpEntries"].append(
            {
                "$type": "scnlocLocStoreEmbeddedVariantPayloadEntry",
                "content": content,
                "variantId": variant_id(variant),
            }
        )
        loc_store["vdEntries"].append(
            {
                "$type": "scnlocLocStoreEmbeddedVariantDescriptorEntry",
                "localeId": str(locale),
                "locstringId": locstring_id(loc_id),
                "signature": {"$type": "scnlocSignature", "val": "3"},
                "variantId": variant_id(variant),
                "vpeIndex": vpe_index,
            }
        )

    # Vanilla choice locStores are grouped by locale, not by option, and each
    # locale block is sorted numerically by locstringId. The engine performs an
    # ordered lookup over vdEntries, so dialogue/spec order is not safe here.
    # Vanilla scenes also carry two db_db descriptors per choice: one blank
    # fallback and one source text payload.
    ordered_choice_keys = sorted(
        spec["choice_line_order"],
        key=lambda choice_key: (int(choice_manifest[choice_key]["string_id"]), str(choice_key)),
    )
    for locale in locales:
        for choice_key in ordered_choice_keys:
            choice = choice_manifest[choice_key]
            loc_id = int(choice["string_id"])
            text = str(choice["text"])
            if locale == "db_db":
                add_loc_variant(choice_key, locale, loc_id, "", "blank")
                add_loc_variant(choice_key, locale, loc_id, text, "source")
            else:
                add_loc_variant(choice_key, locale, loc_id, text, "text")
    return loc_store


def dialog_event(scene_name: str, section_key: str, line_key: str, line_id: int, start_time: int, duration: int, alloc: HandleAllocator) -> dict[str, Any]:
    return alloc.wrap(
        {
            "$type": "scnDialogLineEvent",
            "additionalSpeakers": {"$type": "scnAdditionalSpeakers", "executionTag": 0, "role": "Full", "speakers": []},
            "duration": duration,
            "executionTagFlags": 0,
            "id": {"$type": "scnSceneEventId", "id": deterministic_event_id(scene_name, section_key, line_key, line_id)},
            "scalingData": None,
            "screenplayLineId": screenplay_item_id(line_id),
            "startTime": start_time,
            "type": "0",
            "visualStyle": "regular",
            "voParams": {
                "$type": "scnDialogLineVoParams",
                "alwaysUseBrainGender": 0,
                "customVoEvent": cname("None"),
                "disableHeadMovement": 0,
                "ignoreSpeakerIncapacitation": 0,
                "isHolocallSpeaker": 0,
                "voContext": "Vo_Context_Quest",
                "voExpression": "Vo_Expression_Spoken",
            },
        }
    )


def actor_look_at_event(
    scene_name: str,
    section_key: str,
    event_index: int,
    event_spec: dict[str, Any],
    actors: dict[str, dict[str, Any]],
    duration: int,
    alloc: HandleAllocator,
) -> dict[str, Any]:
    performer = actors[str(event_spec["actor"])]
    target = actors[str(event_spec["target"])]
    return alloc.wrap(
        {
            "$type": "scnLookAtEvent",
            "basicData": {
                "$type": "scnLookAtBasicEventData",
                "basic": {
                    "$type": "scnAnimTargetBasicData",
                    "isStart": 1,
                    "performerId": performer_id(actor_performer_id(performer.id)),
                    "staticTarget": {"$type": "Vector4", "W": 1, "X": 0, "Y": 0, "Z": 0},
                    "targetActorId": actor_id(4294967295),
                    "targetOffsetEntitySpace": {"$type": "Vector4", "W": 0, "X": 0, "Y": 0, "Z": 0},
                    "targetPerformerId": performer_id(actor_performer_id(target.id)),
                    "targetPropId": {"$type": "scnPropId", "id": 4294967295},
                    "targetSlot": cname(str(event_spec.get("target_slot", "pla_default_tgt"))),
                    "targetType": "Actor",
                },
                "removePreviousAdvancedLookAts": 1,
                "requests": [
                    {
                        "$type": "animLookAtRequestForPart",
                        "attachLeftHandToRightHand": -1,
                        "attachRightHandToLeftHand": -1,
                        "bodyPart": cname("Eyes"),
                        "request": {
                            "$type": "animLookAtRequest",
                            "additionalParts": {
                                "Elements": [
                                    {"$type": "animLookAtPartRequest", "mode": 0, "partName": cname("Head"), "suppress": 0, "weight": 1},
                                    {"$type": "animLookAtPartRequest", "mode": 0, "partName": cname("Chest"), "suppress": 0, "weight": 1},
                                ]
                            },
                            "calculatePositionInParentSpace": 0,
                            "debugInfo": f"Ghostline: {event_spec['actor']} looks at {event_spec['target']}",
                            "followingSpeedFactorOverride": -1,
                            "hasOutTransition": 0,
                            "invalid": 0,
                            "limits": {"$type": "animLookAtLimits", "backLimitDegrees": 210, "hardLimitDegrees": 270, "hardLimitDistance": 1000000, "softLimitDegrees": 140},
                            "mode": 0,
                            "outTransitionSpeed": 60,
                            "priority": -1,
                            "suppress": 0,
                            "transitionSpeed": 140,
                        },
                    }
                ],
            },
            "duration": int(event_spec.get("duration_ms", duration)),
            "executionTagFlags": 0,
            "id": {"$type": "scnSceneEventId", "id": deterministic_event_id(scene_name, section_key, "actor_look_at", event_index)},
            "scalingData": None,
            "startTime": int(event_spec.get("start_ms", 0)),
            "type": "0",
        }
    )


def build_section_node(
    spec: dict[str, Any],
    section_spec: dict[str, Any],
    spoken_manifest: dict[str, dict[str, Any]],
    line_ids: dict[str, int],
    alloc: HandleAllocator,
) -> dict[str, Any]:
    if "rid_camera" in section_spec and "camera_event" in section_spec:
        raise SceneBuildError(
            f"Section {section_spec['key']} cannot declare both rid_camera and "
            "camera_event"
        )

    line_events = []
    start = 0
    gap = int(section_spec.get("line_gap_ms", spec.get("line_gap_ms", 250)))
    for line_key in section_spec["lines"]:
        line = spoken_manifest[line_key]
        duration = int(line.get("duration_ms") or spec.get("default_line_duration_ms", 2500))
        line_events.append(dialog_event(str(spec["name"]), str(section_spec["key"]), line_key, line_ids[line_key], start, duration, alloc))
        start += duration + gap

    actors = actor_lookup(spec)
    for event_index, event_spec in enumerate(section_spec.get("rid_events", [])):
        line_events.append(rid_anim_event(str(spec["name"]), str(section_spec["key"]), event_index, event_spec, actors, alloc))
    if "rid_camera" in section_spec:
        line_events.append(rid_camera_event(str(spec["name"]), str(section_spec["key"]), section_spec["rid_camera"], alloc))
    if "camera_event" in section_spec:
        line_events.append(
            camera_event(
                str(spec["name"]),
                str(section_spec["key"]),
                section_spec["camera_event"],
                alloc,
            )
        )

    if section_spec.get("rid_duration_ms") is not None:
        section_duration = int(section_spec["rid_duration_ms"])
    elif line_events:
        section_duration = start - gap + int(section_spec.get("tail_padding_ms", spec.get("section_tail_padding_ms", 400)))
    else:
        section_duration = int(section_spec.get("section_duration_ms", 1000))

    for event_index, event_spec in enumerate(section_spec.get("look_at_events", [])):
        line_events.append(actor_look_at_event(str(spec["name"]), str(section_spec["key"]), event_index, event_spec, actors, section_duration, alloc))

    actor_behaviors = [
        {"$type": "scnSectionInternalsActorBehavior", "actorId": actor_id(int(actor["id"])), "behaviorMode": "OnlyIfAlive"}
        for actor in spec.get("actors", [])
    ]
    data = {
        "$type": "scnSectionNode",
        "actorBehaviors": actor_behaviors,
        "events": line_events,
        "ffStrategy": "automatic",
        "isFocusClue": 0,
        "nodeId": scene_node_id(int(section_spec["node_id"])),
        "outputSockets": [
            output_socket(0, 0, [(int(dest["node_id"]), int(dest.get("input_name", 0)), int(dest.get("input_ordinal", 0))) for dest in section_spec.get("on_end", [])]),
            output_socket(1, 0, [(int(dest["node_id"]), int(dest.get("input_name", 0)), int(dest.get("input_ordinal", 0))) for dest in section_spec.get("on_cancel", [])]),
        ],
        "sectionDuration": scene_time(section_duration),
    }
    return alloc.wrap(data)


def build_choice_option(option_spec: dict[str, Any], option_id: int) -> dict[str, Any]:
    icon_tags = option_spec.get("icon_tags", [])
    if not isinstance(icon_tags, list) or not all(
        isinstance(tag, str) and tag for tag in icon_tags
    ):
        raise SceneBuildError("choice option icon_tags must be a list of non-empty strings")
    return {
        "$type": "scnChoiceNodeOption",
        "blueline": 0,
        "bluelineCondition": None,
        "caption": cname(str(option_spec.get("caption", "None"))),
        "emphasisCondition": None,
        "exDataFlags": 0,
        "gameplayAction": tweakdbid(0, storage="uint64"),
        "iconCondition": None,
        "iconTagIds": [tweakdbid(tag, storage="string") for tag in icon_tags],
        "isFixedAsRead": 0,
        "isSingleChoice": 1 if option_spec.get("single_choice", False) else 0,
        "mappinReferencePointId": {"$type": "scnReferencePointId", "id": UINT32_NONE},
        "questCondition": None,
        "screenplayOptionId": screenplay_item_id(option_id),
        "timedCondition": None,
        "timedParams": None,
        "triggerCondition": None,
        "type": {"$type": "gameinteractionsChoiceTypeWrapper", "properties": int(option_spec.get("choice_type", 1))},
    }


def build_choice_node(
    choice_shell: dict[str, Any],
    choice_spec: dict[str, Any],
    option_ids: dict[str, int],
    alloc: HandleAllocator,
) -> dict[str, Any]:
    node = copy.deepcopy(choice_shell)
    reassign_handle_ids(node, alloc)
    node["Data"]["nodeId"] = scene_node_id(int(choice_spec["node_id"]))
    node["Data"]["ataParams"]["actorId"] = actor_id(int(choice_spec.get("actor_id", 0)))
    node["Data"]["reminderParams"]["Data"]["reminderActor"] = actor_id(int(choice_spec.get("actor_id", 0)))
    node["Data"]["persistentLineEvents"] = []
    node["Data"]["customPersistentLine"] = screenplay_item_id(PERFORMER_NONE)
    node["Data"]["options"] = []
    node["Data"]["outputSockets"] = []

    for ordinal, option_spec in enumerate(choice_spec["options"]):
        item_id = option_ids[str(option_spec["choice_key"])]
        node["Data"]["options"].append(build_choice_option(option_spec, item_id))
        node["Data"]["outputSockets"].append(output_socket(0, ordinal, [(int(option_spec["target_node_id"]), 0, 0)]))
    for dummy_name in range(1, 7):
        node["Data"]["outputSockets"].append(output_socket(dummy_name, 0, []))
    return node


def build_start_node(node_id: int, destinations: list[dict[str, int]], alloc: HandleAllocator) -> dict[str, Any]:
    return alloc.wrap(
        {
            "$type": "scnStartNode",
            "ffStrategy": "automatic",
            "nodeId": scene_node_id(node_id),
            "outputSockets": [
                output_socket(0, 0, [(int(dest["node_id"]), int(dest.get("input_name", 0)), int(dest.get("input_ordinal", 0))) for dest in destinations])
            ],
        }
    )


def build_end_node(node_id: int, alloc: HandleAllocator) -> dict[str, Any]:
    return alloc.wrap({"$type": "scnEndNode", "ffStrategy": "automatic", "nodeId": scene_node_id(node_id), "outputSockets": []})


def build_xor_node(node_id: int, destinations: list[dict[str, int]], alloc: HandleAllocator) -> dict[str, Any]:
    return alloc.wrap(
        {
            "$type": "scnXorNode",
            "ffStrategy": "automatic",
            "nodeId": scene_node_id(node_id),
            "outputSockets": [
                output_socket(0, 0, [(int(dest["node_id"]), int(dest.get("input_name", 0)), int(dest.get("input_ordinal", 0))) for dest in destinations])
            ],
        }
    )


def build_quest_node_base(
    node_id: int,
    quest_type: str,
    inputs: list[str],
    outputs: list[str],
    destinations: list[dict[str, int]],
    alloc: HandleAllocator,
) -> tuple[dict[str, Any], dict[str, Any]]:
    data = {
        "$type": "scnQuestNode",
        "ffStrategy": "automatic",
        "isockMappings": [socket_mapping(name) for name in inputs],
        "nodeId": scene_node_id(node_id),
        "osockMappings": [socket_mapping(name) for name in outputs],
        "outputSockets": [
            output_socket(0, 0, [(int(dest["node_id"]), int(dest.get("input_name", 0)), int(dest.get("input_ordinal", 0))) for dest in destinations])
        ],
        "questNode": alloc.wrap({"$type": quest_type, "id": node_id, "sockets": []}),
    }
    return data, data["questNode"]["Data"]


def add_quest_sockets(quest_data: dict[str, Any], inputs: list[str], outputs: list[str], alloc: HandleAllocator) -> None:
    sockets = [quest_socket(alloc, "CutDestination", "CutDestination")]
    for name in inputs:
        if name != "CutDestination":
            sockets.append(quest_socket(alloc, name, "Input"))
    for name in outputs:
        sockets.append(quest_socket(alloc, name, "Output"))
    quest_data["sockets"] = sockets


def build_puppet_ai_node(node_spec: dict[str, Any], alloc: HandleAllocator) -> dict[str, Any]:
    inputs = ["CutDestination", "In"]
    outputs = ["Out"]
    data, quest = build_quest_node_base(int(node_spec["node_id"]), "questPuppetAIManagerNodeDefinition", inputs, outputs, node_spec.get("on_out", []), alloc)
    quest["entries"] = [
        {
            "$type": "questPuppetAIManagerNodeDefinitionEntry",
            "aiTier": str(node_spec.get("ai_tier", "Cinematic")),
            "entityReference": empty_entity_ref(str(node_spec["entity_ref"]), storage="string", names=[str(node_spec["entry"])]),
        }
    ]
    add_quest_sockets(quest, inputs, outputs, alloc)
    return alloc.wrap(data)


def build_use_workspot_node(
    node_spec: dict[str, Any], alloc: HandleAllocator
) -> dict[str, Any]:
    node_id = int(node_spec["node_id"])
    function = str(node_spec.get("function", "UseWorkspot"))
    stopping = function == "StopWorkspot"
    inputs = ["CutDestination", "In"]
    outputs = ["Success"] if stopping else ["Success", "Work Started"]
    data, quest = build_quest_node_base(
        node_id,
        "questUseWorkspotNodeDefinition",
        inputs,
        outputs,
        [],
        alloc,
    )
    data["outputSockets"] = [
        output_socket(
            0,
            0,
            [
                (
                    int(dest["node_id"]),
                    int(dest.get("input_name", 0)),
                    int(dest.get("input_ordinal", 0)),
                )
                for dest in node_spec.get("on_success", [])
            ],
        )
    ]
    if not stopping:
        data["outputSockets"].append(
            output_socket(
                0,
                1,
                [
                    (
                        int(dest["node_id"]),
                        int(dest.get("input_name", 0)),
                        int(dest.get("input_ordinal", 0)),
                    )
                    for dest in node_spec.get("on_work_started", [])
                ],
            )
        )
    quest["entityReference"] = empty_entity_ref(
        str(node_spec["entity_ref"]),
        storage="string",
        names=[str(node_spec["entry"])],
    )
    quest["paramsV1"] = alloc.wrap(
        {
            "$type": "questUseWorkspotParamsV1",
            "changeWorkspot": 1,
            "continueInCombat": 0,
            "dangleResetSimulation": 0,
            "enableIdleMode": 0,
            "entryId": {
                "$type": "workWorkEntryId",
                "id": int(node_spec.get("entry_id", UINT32_NONE)),
            },
            "entryTag": cname(str(node_spec.get("entry_tag", "None"))),
            "exitAnimName": cname("None"),
            "exitEntryId": {"$type": "workWorkEntryId", "id": UINT32_NONE},
            "finishAnimation": int(bool(node_spec.get("finish_animation", True))),
            "forceEntryAnimName": cname(
                str(node_spec.get("force_entry_animation", "None"))
            ),
            "function": function,
            "instant": int(bool(node_spec.get("instant", False))),
            "isPlayer": 0,
            "isWorkspotInfinite": int(
                bool(node_spec.get("is_workspot_infinite", True))
            ),
            "jumpToEntry": int(bool(node_spec.get("jump_to_entry", False))),
            "maxAnimTimeLimit": float(node_spec.get("max_anim_time_limit", 0)),
            "meshDissolvingEnabled": 1,
            "movementType": str(node_spec.get("movement_type", "Walk")),
            "playerParams": {
                "$type": "questUseWorkspotPlayerParams",
                "applyCameraParams": 0,
                "cameraSettings": {
                    "$type": "gameTier3CameraSettings",
                    "pitchBottomLimit": 45,
                    "pitchSpeedMultiplier": 1,
                    "pitchTopLimit": 60,
                    "yawLeftLimit": 60,
                    "yawRightLimit": 60,
                    "yawSpeedMultiplier": 1,
                },
                "cameraUseTrajectorySpace": 1,
                "emptyHands": 0,
                "parallaxSpace": "Trajectory",
                "parallaxWeight": 1,
                "tier": "Tier3",
                "vehicleProceduralCameraWeight": 1,
            },
            "repeatCommandOnInterrupt": int(
                bool(node_spec.get("repeat_on_interrupt", True))
            ),
            "teleport": int(bool(node_spec.get("teleport", not stopping))),
            "workExcludedGestures": [],
            "workspotNode": node_ref(str(node_spec["workspot_ref"])),
        }
    )
    add_quest_sockets(quest, inputs, outputs, alloc)
    return alloc.wrap(data)


def build_stop_workspot_node(
    node_spec: dict[str, Any], alloc: HandleAllocator
) -> dict[str, Any]:
    return build_use_workspot_node(
        {**node_spec, "function": "StopWorkspot", "teleport": False}, alloc
    )


def build_appearance_node(node_spec: dict[str, Any], alloc: HandleAllocator) -> dict[str, Any]:
    inputs = ["CutDestination", "In"]
    outputs = ["Out"]
    data, quest = build_quest_node_base(
        int(node_spec["node_id"]),
        "questCharacterManagerNodeDefinition",
        inputs,
        outputs,
        node_spec.get("on_out", []),
        alloc,
    )
    appearance_entry = {
        "$type": "questCharacterManagerVisuals_EntityAppearanceOperationBaseEntityAppearanceEntry",
        "appearanceName": cname(str(node_spec["appearance"])),
        "isPlayer": 0,
        "puppetRef": empty_entity_ref(
            str(node_spec["entity_ref"]),
            storage="string",
            names=[str(node_spec["entry"])],
        ),
    }
    quest["type"] = alloc.wrap(
        {
            "$type": "questCharacterManagerVisuals_NodeType",
            "subtype": alloc.wrap(
                {
                    "$type": "questCharacterManagerVisuals_ChangeEntityAppearance",
                    "appearanceEntries": [appearance_entry],
                }
            ),
        }
    )
    add_quest_sockets(quest, inputs, outputs, alloc)
    return alloc.wrap(data)


def build_scene_tier_node(
    node_spec: dict[str, Any], alloc: HandleAllocator
) -> dict[str, Any]:
    inputs = ["CutDestination", "In"]
    outputs = ["Out"]
    data, quest = build_quest_node_base(
        int(node_spec["node_id"]),
        "questSceneManagerNodeDefinition",
        inputs,
        outputs,
        node_spec.get("on_out", []),
        alloc,
    )
    quest["type"] = alloc.wrap(
        {
            "$type": "questSetTier_NodeType",
            "forceEmptyHands": 1 if node_spec.get("force_empty_hands", False) else 0,
            "motionConstrainedTierDataParams": {
                "$type": "gameMotionConstrainedTierDataParams",
                "adjustingDuration": 0,
                "adjustingSpeed": 0,
                "notificationBackwardIndex": 0,
                "splineRef": node_ref(0, storage="uint64"),
                "travellingDuration": 0,
                "travellingSpeed": 0,
            },
            "tier": str(node_spec["tier"]),
            "useEnterAnim": 0,
            "useExitAnim": 0,
            "usePlayerWorkspot": 0,
        }
    )
    add_quest_sockets(quest, inputs, outputs, alloc)
    return alloc.wrap(data)


def build_unequip_node(
    node_spec: dict[str, Any], alloc: HandleAllocator, *, is_player: bool
) -> dict[str, Any]:
    inputs = ["CutDestination", "In"]
    outputs = ["Out"]
    data, quest = build_quest_node_base(
        int(node_spec["node_id"]),
        "questEquipItemNodeDefinition",
        inputs,
        outputs,
        node_spec.get("on_out", []),
        alloc,
    )
    if is_player:
        entity_reference = empty_entity_ref()
    else:
        entity_reference = empty_entity_ref(
            str(node_spec["entity_ref"]),
            storage="string",
            names=[str(node_spec["entry"])],
        )
    quest["entityReference"] = alloc.wrap(
        {
            "$type": "questObservableUniversalRef",
            "entityReference": entity_reference,
            "mainPlayerObject": 0,
            "refLocalPlayer": 1 if is_player else 0,
        }
    )
    item_id = node_spec.get("item_id", 0)
    item_storage = "string" if isinstance(item_id, str) else "uint64"
    slot_id = node_spec.get("slot_id", 0)
    slot_storage = "string" if isinstance(slot_id, str) else "uint64"
    quest["params"] = alloc.wrap(
        {
            "$type": "questEquipItemParams",
            "byItem": 1 if node_spec.get("by_item", False) else 0,
            "equipDurationOverride": node_spec.get("equip_duration_override", -1),
            "equipLastWeapon": 0,
            "equipTypes": "LastWeaponEquipped",
            "failIfItemNotFound": 0,
            "forceFirstEquip": 0,
            "ignoreStateMachine": 0,
            "instant": 1 if node_spec.get("instant", False) else 0,
            "isPlayer": 1 if is_player else 0,
            "itemId": tweakdbid(item_id, storage=item_storage),
            "slotId": tweakdbid(slot_id, storage=slot_storage),
            "type": str(node_spec.get("operation", "Unequip")),
            "unequipDurationOverride": node_spec.get(
                "unequip_duration_override", -1
            ),
            "unequipTypes": str(node_spec.get("unequip_types", "AllWeapons")),
        }
    )
    add_quest_sockets(quest, inputs, outputs, alloc)
    return alloc.wrap(data)


def build_unequip_player_node(
    node_spec: dict[str, Any], alloc: HandleAllocator
) -> dict[str, Any]:
    return build_unequip_node(node_spec, alloc, is_player=True)


def build_unequip_actor_node(
    node_spec: dict[str, Any], alloc: HandleAllocator
) -> dict[str, Any]:
    return build_unequip_node(node_spec, alloc, is_player=False)


def build_equip_player_node(
    node_spec: dict[str, Any], alloc: HandleAllocator
) -> dict[str, Any]:
    equip_spec = dict(node_spec)
    equip_spec["operation"] = "Equip"
    return build_unequip_node(equip_spec, alloc, is_player=True)


def build_equip_actor_node(
    node_spec: dict[str, Any], alloc: HandleAllocator
) -> dict[str, Any]:
    equip_spec = dict(node_spec)
    equip_spec["operation"] = "Equip"
    return build_unequip_node(equip_spec, alloc, is_player=False)


def build_teleport_node(
    node_spec: dict[str, Any], alloc: HandleAllocator, *, is_player: bool
) -> dict[str, Any]:
    inputs = ["CutDestination", "In"]
    outputs = ["Out"]
    data, quest = build_quest_node_base(
        int(node_spec["node_id"]),
        "questTeleportPuppetNodeDefinition",
        inputs,
        outputs,
        node_spec.get("on_out", []),
        alloc,
    )
    if is_player:
        target_ref = empty_entity_ref()
    else:
        target_ref = empty_entity_ref(
            str(node_spec["entity_ref"]),
            storage="string",
            names=[str(node_spec["entry"])],
        )
    quest["entityReference"] = alloc.wrap(
        {
            "$type": "questUniversalRef",
            "entityReference": target_ref,
            "mainPlayerObject": 0,
            "refLocalPlayer": 1 if is_player else 0,
        }
    )
    look_at_ref = node_spec.get("look_at_ref")
    quest["lookAtAction"] = "Set" if look_at_ref else "Reset"
    quest["params"] = alloc.wrap(
        {
            "$type": "questTeleportPuppetParamsV1",
            "destinationOffset": {
                "$type": "Vector3",
                "X": 0,
                "Y": 0,
                "Z": 0,
            },
            "destinationRef": alloc.wrap(
                {
                    "$type": "questUniversalRef",
                    "entityReference": empty_entity_ref(
                        str(node_spec["destination_ref"]), storage="string"
                    ),
                    "mainPlayerObject": 0,
                    "refLocalPlayer": 0,
                }
            ),
            "doNavTest": 0,
            "healAtTeleport": 1 if node_spec.get("heal", False) else 0,
            "useFastTravelMechanism": 0,
        }
    )
    quest["playerLookAt"] = alloc.wrap(
        {
            "$type": "questPlayerLookAtParams",
            "adjustPitch": 1,
            "adjustYaw": 1,
            "cameraInputMagToBreak": 0.2,
            "duration": 0.25,
            "easeIn": 1,
            "easeOut": 1,
            "endOnCameraInputApplied": 1,
            "endOnTargetReached": 1,
            "endOnTimeExceeded": 1,
            "lookAtTarget": empty_entity_ref(
                str(look_at_ref),
                storage="string",
                names=(
                    [str(node_spec["look_at_entry"])]
                    if node_spec.get("look_at_entry")
                    else None
                ),
            ) if look_at_ref else empty_entity_ref(),
            "maxDuration": 2,
            "offset": {"$type": "Vector3", "X": 0, "Y": 0, "Z": 0},
            "precision": 0.1,
            "slotName": cname("None"),
            "useOffsetToPlayer": 0 if look_at_ref else 1,
        }
    )
    add_quest_sockets(quest, inputs, outputs, alloc)
    return alloc.wrap(data)


def build_teleport_player_node(
    node_spec: dict[str, Any], alloc: HandleAllocator
) -> dict[str, Any]:
    return build_teleport_node(node_spec, alloc, is_player=True)


def build_teleport_actor_node(
    node_spec: dict[str, Any], alloc: HandleAllocator
) -> dict[str, Any]:
    return build_teleport_node(node_spec, alloc, is_player=False)


def build_realtime_delay_node(
    node_spec: dict[str, Any], alloc: HandleAllocator
) -> dict[str, Any]:
    inputs = ["CutDestination", "In"]
    outputs = ["Out"]
    data, quest = build_quest_node_base(
        int(node_spec["node_id"]),
        "questPauseConditionNodeDefinition",
        inputs,
        outputs,
        node_spec.get("on_out", []),
        alloc,
    )
    quest["condition"] = alloc.wrap(
        {
            "$type": "questTimeCondition",
            "type": alloc.wrap(
                {
                    "$type": "questRealtimeDelay_ConditionType",
                    "hours": int(node_spec.get("hours", 0)),
                    "miliseconds": int(node_spec.get("milliseconds", 0)),
                    "minutes": int(node_spec.get("minutes", 0)),
                    "seconds": int(node_spec.get("seconds", 0)),
                }
            ),
        }
    )
    add_quest_sockets(quest, inputs, outputs, alloc)
    return alloc.wrap(data)


def build_render_fade_node(
    node_spec: dict[str, Any], alloc: HandleAllocator
) -> dict[str, Any]:
    """Fade to or from black using the vanilla scene handoff node."""
    inputs = ["CutDestination", "In"]
    outputs = ["Out"]
    duration = float(node_spec.get("duration_seconds", 0))
    if duration < 0:
        raise SceneBuildError("render_fade duration_seconds cannot be negative")
    data, quest = build_quest_node_base(
        int(node_spec["node_id"]),
        "questRenderFxManagerNodeDefinition",
        inputs,
        outputs,
        node_spec.get("on_out", []),
        alloc,
    )
    quest["type"] = alloc.wrap(
        {
            "$type": "questSetFadeInOut_NodeType",
            "duration": duration,
            "fadeColor": {
                "$type": "Color",
                "Alpha": 0,
                "Blue": 0,
                "Green": 0,
                "Red": 0,
            },
            "fadeIn": 1 if node_spec.get("fade_in", True) else 0,
        }
    )
    add_quest_sockets(quest, inputs, outputs, alloc)
    return alloc.wrap(data)


def build_player_look_at_node(
    node_spec: dict[str, Any], alloc: HandleAllocator
) -> dict[str, Any]:
    """Aim the player camera at an entity slot or an entity-relative offset."""
    inputs = ["CutDestination", "In"]
    outputs = ["Out"]
    duration = float(node_spec.get("duration_seconds", 2.5))
    max_duration = float(node_spec.get("max_duration_seconds", duration))
    if duration < 0 or max_duration < 0:
        raise SceneBuildError("player_look_at durations cannot be negative")
    target_ref = str(node_spec["target_ref"])
    target_entry = node_spec.get("target_entry")
    offset = node_spec.get("offset", {})
    data, quest = build_quest_node_base(
        int(node_spec["node_id"]),
        "questSceneManagerNodeDefinition",
        inputs,
        outputs,
        node_spec.get("on_out", []),
        alloc,
    )
    quest["type"] = alloc.wrap(
        {
            "$type": "questPlayerLookAt_NodeType",
            "adjustPitch": 1 if node_spec.get("adjust_pitch", True) else 0,
            "adjustYaw": 1 if node_spec.get("adjust_yaw", True) else 0,
            "cameraInputMagToBreak": float(
                node_spec.get("camera_input_magnitude_to_break", 2.0)
            ),
            "duration": duration,
            "easeIn": 1 if node_spec.get("ease_in", True) else 0,
            "easeOut": 1 if node_spec.get("ease_out", True) else 0,
            "endOnCameraInputApplied": 1
            if node_spec.get("end_on_camera_input", False)
            else 0,
            "endOnTargetReached": 1
            if node_spec.get("end_on_target_reached", True)
            else 0,
            "endOnTimeExceeded": 1
            if node_spec.get("end_on_time_exceeded", True)
            else 0,
            "maxDuration": max_duration,
            "objectRef": empty_entity_ref(
                target_ref,
                storage="string",
                names=[str(target_entry)] if target_entry else None,
            ),
            "offsetPos": {
                "$type": "Vector3",
                "X": float(offset.get("x", 0)),
                "Y": float(offset.get("y", 0)),
                "Z": float(offset.get("z", 0)),
            },
            "precision": float(node_spec.get("precision", 0.1)),
            "slotName": cname(str(node_spec.get("slot", "Head"))),
            "useOffsetToPlayer": 0,
        }
    )
    add_quest_sockets(quest, inputs, outputs, alloc)
    return alloc.wrap(data)


def build_player_status_effect_node(
    node_spec: dict[str, Any], alloc: HandleAllocator
) -> dict[str, Any]:
    inputs = ["CutDestination", "In"]
    outputs = ["Out"]
    data, quest = build_quest_node_base(
        int(node_spec["node_id"]),
        "questCharacterManagerNodeDefinition",
        inputs,
        outputs,
        node_spec.get("on_out", []),
        alloc,
    )
    selector = alloc.wrap(
        {
            "$type": "questRecordSelector",
            "characterRecordID": tweakdbid(0, storage="uint64"),
            "deviceRecordID": tweakdbid(0, storage="uint64"),
            "isCharacter": 1,
            "isDevice": 0,
            "isItem": 0,
            "itemRecordID": tweakdbid(0, storage="uint64"),
        }
    )
    subtype = alloc.wrap(
        {
            "$type": "questCharacterManagerParameters_SetStatusEffect",
            "isPlayer": 1,
            "isPlayerStatusEffectSource": 1,
            "puppetRef": empty_entity_ref(),
            "recordSelector": selector,
            "set": 1 if node_spec.get("set", True) else 0,
            "statusEffectID": tweakdbid(str(node_spec["status_effect"])),
            "statusEffectSourceObject": empty_entity_ref(),
        }
    )
    quest["type"] = alloc.wrap(
        {
            "$type": "questCharacterManagerParameters_NodeType",
            "subtype": subtype,
        }
    )
    add_quest_sockets(quest, inputs, outputs, alloc)
    return alloc.wrap(data)


def build_trigger_condition(trigger_ref: str) -> dict[str, Any]:
    return {
        "$type": "questTriggerCondition",
        "activatorRef": empty_entity_ref(),
        "isPlayerActivator": 1,
        "triggerAreaRef": node_ref(trigger_ref),
        "type": "IsInside",
    }


def build_pause_condition_node(node_spec: dict[str, Any], alloc: HandleAllocator) -> dict[str, Any]:
    inputs = ["CutDestination", "In"]
    outputs = ["Out"]
    data, quest = build_quest_node_base(int(node_spec["node_id"]), "questPauseConditionNodeDefinition", inputs, outputs, node_spec.get("on_out", []), alloc)
    trigger_condition = alloc.wrap(build_trigger_condition(str(node_spec["trigger_ref"])))
    if node_spec.get("require_player_not_in_combat", False):
        combat = alloc.wrap(
            {
                "$type": "questCharacterCondition",
                "type": alloc.wrap(
                    {
                        "$type": "questCharacterCombat_ConditionType",
                        "inverted": 1,
                        "isPlayer": 1,
                        "objectRef": empty_entity_ref(),
                    }
                ),
            }
        )
        quest["condition"] = alloc.wrap(
            {
                "$type": "questLogicalCondition",
                "conditions": [trigger_condition, combat],
                "operation": "AND",
            }
        )
    else:
        quest["condition"] = trigger_condition
    add_quest_sockets(quest, inputs, outputs, alloc)
    return alloc.wrap(data)


def build_character_gender_node(
    node_spec: dict[str, Any], alloc: HandleAllocator
) -> dict[str, Any]:
    """Branch on Player gender using the vanilla quest condition shape."""
    node_id = int(node_spec["node_id"])
    inputs = ["CutDestination", "In"]
    outputs = ["True", "False"]
    data = {
        "$type": "scnQuestNode",
        "ffStrategy": "automatic",
        "isockMappings": [socket_mapping(name) for name in inputs],
        "nodeId": scene_node_id(node_id),
        "osockMappings": [socket_mapping(name) for name in outputs],
        "outputSockets": [
            output_socket(
                0,
                0,
                [
                    (
                        int(dest["node_id"]),
                        int(dest.get("input_name", 0)),
                        int(dest.get("input_ordinal", 0)),
                    )
                    for dest in node_spec.get("on_true", [])
                ],
            ),
            output_socket(
                0,
                1,
                [
                    (
                        int(dest["node_id"]),
                        int(dest.get("input_name", 0)),
                        int(dest.get("input_ordinal", 0)),
                    )
                    for dest in node_spec.get("on_false", [])
                ],
            ),
        ],
        "questNode": alloc.wrap(
            {
                "$type": "questConditionNodeDefinition",
                "condition": alloc.wrap(
                    {
                        "$type": "questCharacterCondition",
                        "type": alloc.wrap(
                            {
                                "$type": "questCharacterGender_CondtionType",
                                "gender": cname(str(node_spec.get("gender", "Male"))),
                                "isPlayer": 1
                                if node_spec.get("is_player", True)
                                else 0,
                                "objectRef": empty_entity_ref(
                                    str(node_spec.get("object_ref", 0)),
                                    storage=(
                                        "string"
                                        if "object_ref" in node_spec
                                        else "uint64"
                                    ),
                                ),
                            }
                        ),
                    }
                ),
                "id": node_id,
                "sockets": [],
            }
        ),
    }
    add_quest_sockets(data["questNode"]["Data"], inputs, outputs, alloc)
    return alloc.wrap(data)


def build_spawn_actor_node(
    node_spec: dict[str, Any], alloc: HandleAllocator
) -> dict[str, Any]:
    """Activate or deactivate a scene-owned spawnDespawn performer."""
    inputs = ["CutDestination", "In"]
    outputs = ["Out"]
    data, quest = build_quest_node_base(
        int(node_spec["node_id"]),
        "questSpawnManagerNodeDefinition",
        inputs,
        outputs,
        node_spec.get("on_out", []),
        alloc,
    )
    action = str(node_spec.get("action", "Activate"))
    if action not in {"Activate", "Deactivate"}:
        raise SceneBuildError("spawn_actor action must be Activate or Deactivate")
    quest["actions"] = [
        {
            "$type": "questSpawnManagerNodeActionEntry",
            "type": alloc.wrap(
                {
                    "$type": "questScene_NodeType",
                    "action": action,
                    "entityReference": dynamic_entity_ref(
                        str(node_spec["dynamic_name"])
                    ),
                }
            ),
        }
    ]
    add_quest_sockets(quest, inputs, outputs, alloc)
    return alloc.wrap(data)


def build_wait_actor_spawned_node(
    node_spec: dict[str, Any], alloc: HandleAllocator
) -> dict[str, Any]:
    """Wait until a dynamic scene performer has materialized in the world."""
    inputs = ["CutDestination", "In"]
    outputs = ["Out"]
    data, quest = build_quest_node_base(
        int(node_spec["node_id"]),
        "questPauseConditionNodeDefinition",
        inputs,
        outputs,
        node_spec.get("on_out", []),
        alloc,
    )
    quest["condition"] = alloc.wrap(
        {
            "$type": "questCharacterCondition",
            "type": alloc.wrap(
                {
                    "$type": "questCharacterSpawned_ConditionType",
                    "comparisonParams": alloc.wrap(
                        {
                            "$type": "questComparisonParam",
                            "comparisonType": "Greater",
                            "count": 0,
                            "entireCommunity": 1,
                        }
                    ),
                    "objectRef": dynamic_entity_ref(str(node_spec["dynamic_name"])),
                }
            ),
        }
    )
    add_quest_sockets(quest, inputs, outputs, alloc)
    return alloc.wrap(data)


def build_show_player_node(
    node_spec: dict[str, Any], alloc: HandleAllocator
) -> dict[str, Any]:
    """Hide/show the real Player while a TPP cutscene replica is on camera."""
    inputs = ["CutDestination", "In"]
    outputs = ["Out"]
    data, quest = build_quest_node_base(
        int(node_spec["node_id"]),
        "questWorldDataManagerNodeDefinition",
        inputs,
        outputs,
        node_spec.get("on_out", []),
        alloc,
    )
    quest["type"] = alloc.wrap(
        {
            "$type": "questShowWorldNode_NodeType",
            "componentName": cname("None"),
            "isPlayer": 1,
            "objectRef": node_ref(0, storage="uint64"),
            "show": 1 if node_spec.get("show", True) else 0,
        }
    )
    add_quest_sockets(quest, inputs, outputs, alloc)
    return alloc.wrap(data)


def journal_path_handle(path: str, class_name: str, file_entry_index: int, alloc: HandleAllocator) -> dict[str, Any]:
    return alloc.wrap(
        {
            "$type": "gameJournalPath",
            "className": cname(class_name),
            "editorPath": "",
            "fileEntryIndex": file_entry_index,
            "realPath": path,
        }
    )


def build_journal_node(node_spec: dict[str, Any], alloc: HandleAllocator) -> dict[str, Any]:
    inputs = ["CutDestination"] + list(node_spec.get("inputs", ["Active", "Inactive"]))
    outputs = ["Out"]
    data, quest = build_quest_node_base(int(node_spec["node_id"]), "questJournalNodeDefinition", inputs, outputs, node_spec.get("on_out", []), alloc)
    node_type = str(node_spec.get("journal_type", "entry"))
    path_handle = journal_path_handle(str(node_spec["path"]), str(node_spec["class_name"]), resolve_file_entry_index(node_spec), alloc)
    if node_type == "quest_entry":
        quest["type"] = alloc.wrap(
            {
                "$type": "questJournalQuestEntry_NodeType",
                "optional": int(node_spec.get("optional", 0)),
                "path": path_handle,
                "sendNotification": int(node_spec.get("send_notification", 1)),
                "trackQuest": int(node_spec.get("track_quest", 0)),
                "version": str(node_spec.get("version", "Initial")),
            }
        )
    else:
        quest["type"] = alloc.wrap(
            {
                "$type": "questJournalEntry_NodeType",
                "path": path_handle,
                "sendNotification": int(node_spec.get("send_notification", 1)),
            }
        )
    add_quest_sockets(quest, inputs, outputs, alloc)
    return alloc.wrap(data)


def build_mappin_node(node_spec: dict[str, Any], alloc: HandleAllocator) -> dict[str, Any]:
    inputs = ["CutDestination", "Active", "Inactive"]
    outputs = ["Out"]
    data, quest = build_quest_node_base(int(node_spec["node_id"]), "questMappinManagerNodeDefinition", inputs, outputs, node_spec.get("on_out", []), alloc)
    quest["disablePreviousMappins"] = int(node_spec.get("disable_previous_mappins", 0))
    quest["path"] = journal_path_handle(str(node_spec["path"]), str(node_spec["class_name"]), resolve_file_entry_index(node_spec), alloc)
    add_quest_sockets(quest, inputs, outputs, alloc)
    return alloc.wrap(data)


def build_quest_node(node_spec: dict[str, Any], alloc: HandleAllocator) -> dict[str, Any]:
    kind = node_spec.get("kind")
    if kind == "puppet_ai":
        return build_puppet_ai_node(node_spec, alloc)
    if kind == "use_workspot":
        return build_use_workspot_node(node_spec, alloc)
    if kind == "stop_workspot":
        return build_stop_workspot_node(node_spec, alloc)
    if kind == "appearance":
        return build_appearance_node(node_spec, alloc)
    if kind == "scene_tier":
        return build_scene_tier_node(node_spec, alloc)
    if kind == "unequip_player":
        return build_unequip_player_node(node_spec, alloc)
    if kind == "unequip_actor":
        return build_unequip_actor_node(node_spec, alloc)
    if kind == "equip_player":
        return build_equip_player_node(node_spec, alloc)
    if kind == "equip_actor":
        return build_equip_actor_node(node_spec, alloc)
    if kind == "teleport_player":
        return build_teleport_player_node(node_spec, alloc)
    if kind == "teleport_actor":
        return build_teleport_actor_node(node_spec, alloc)
    if kind == "realtime_delay":
        return build_realtime_delay_node(node_spec, alloc)
    if kind == "render_fade":
        return build_render_fade_node(node_spec, alloc)
    if kind == "player_look_at":
        return build_player_look_at_node(node_spec, alloc)
    if kind == "player_status_effect":
        return build_player_status_effect_node(node_spec, alloc)
    if kind == "pause_condition":
        return build_pause_condition_node(node_spec, alloc)
    if kind == "character_gender":
        return build_character_gender_node(node_spec, alloc)
    if kind == "spawn_actor":
        return build_spawn_actor_node(node_spec, alloc)
    if kind == "wait_actor_spawned":
        return build_wait_actor_spawned_node(node_spec, alloc)
    if kind == "show_player":
        return build_show_player_node(node_spec, alloc)
    if kind == "journal":
        return build_journal_node(node_spec, alloc)
    if kind == "mappin":
        return build_mappin_node(node_spec, alloc)
    raise SceneBuildError(f"Unsupported quest node kind: {kind}")


def load_choice_shell(base_root: dict[str, Any], node_id: int | None = None) -> dict[str, Any]:
    for wrapper in base_root["sceneGraph"]["Data"]["graph"]:
        data = wrapper.get("Data", {})
        if data.get("$type") == "scnChoiceNode" and (node_id is None or int(data["nodeId"]["id"]) == node_id):
            return wrapper
    raise SceneBuildError("Base scene does not contain a scnChoiceNode shell")


def graph_node_id(wrapper: dict[str, Any]) -> int | None:
    node_id = wrapper.get("Data", {}).get("nodeId", {}).get("id")
    return int(node_id) if node_id is not None else None


def graph_destinations(wrapper: dict[str, Any]) -> list[int]:
    destinations: list[int] = []
    for socket in wrapper.get("Data", {}).get("outputSockets", []):
        for destination in socket.get("destinations", []):
            node_id = destination.get("nodeId", {}).get("id")
            if node_id is not None:
                destinations.append(int(node_id))
    return destinations


def order_graph_by_connections(graph: list[dict[str, Any]], start_node_id: int) -> list[dict[str, Any]]:
    by_id = {node_id: wrapper for wrapper in graph if (node_id := graph_node_id(wrapper)) is not None}
    ordered: list[dict[str, Any]] = []
    seen: set[int] = set()
    queue = [start_node_id]
    while queue:
        node_id = queue.pop(0)
        wrapper = by_id.get(node_id)
        if wrapper is None or node_id in seen:
            continue
        seen.add(node_id)
        ordered.append(wrapper)
        for destination in graph_destinations(wrapper):
            if destination not in seen:
                queue.append(destination)
    ordered.extend(wrapper for wrapper in graph if (node_id := graph_node_id(wrapper)) is None or node_id not in seen)
    return ordered


def order_graph_by_spec(graph: list[dict[str, Any]], graph_order: list[int]) -> list[dict[str, Any]]:
    by_id = {node_id: wrapper for wrapper in graph if (node_id := graph_node_id(wrapper)) is not None}
    actual_ids = set(by_id)
    requested_ids = set(graph_order)
    missing = sorted(actual_ids - requested_ids)
    extra = sorted(requested_ids - actual_ids)
    if missing or extra or len(graph_order) != len(actual_ids):
        raise SceneBuildError(f"graph_order must include every node exactly once; missing={missing}, extra={extra}")
    return [by_id[node_id] for node_id in graph_order]


def scene_start_specs(spec: dict[str, Any]) -> list[dict[str, Any]]:
    """Return every authored scene start while preserving legacy specs."""

    return spec.get("start_nodes") or [spec["start_node"]]


def build_graph(
    spec: dict[str, Any],
    base_root: dict[str, Any],
    spoken_manifest: dict[str, dict[str, Any]],
    line_ids: dict[str, int],
    option_ids: dict[str, int],
    alloc: HandleAllocator,
) -> dict[str, Any]:
    choice_shell = load_choice_shell(base_root, spec.get("choice_shell_node_id")) if spec_declares_choices(spec) else None
    graph: list[dict[str, Any]] = []
    for start_spec in scene_start_specs(spec):
        graph.append(
            build_start_node(
                int(start_spec["node_id"]),
                start_spec.get("on_start", []),
                alloc,
            )
        )
    for section_spec in spec.get("sections", []):
        graph.append(build_section_node(spec, section_spec, spoken_manifest, line_ids, alloc))
    for choice_spec in spec.get("choices", []):
        if choice_shell is None:
            raise SceneBuildError("Spec declares choice nodes but no choice shell was loaded")
        graph.append(build_choice_node(choice_shell, choice_spec, option_ids, alloc))
    for quest_spec in spec.get("quest_nodes", []):
        graph.append(build_quest_node(quest_spec, alloc))
    for xor_spec in spec.get("xor_nodes", []):
        graph.append(build_xor_node(int(xor_spec["node_id"]), xor_spec.get("on_out", []), alloc))
    end_specs = spec.get("end_nodes") or [spec["end_node"]]
    for end_spec in end_specs:
        graph.append(build_end_node(int(end_spec["node_id"]), alloc))
    if "graph_order" in spec:
        graph = order_graph_by_spec(graph, [int(node_id) for node_id in spec["graph_order"]])
    else:
        graph = order_graph_by_connections(
            graph,
            int(scene_start_specs(spec)[0]["node_id"]),
        )
    return {"HandleId": "2", "Data": {"$type": "scnSceneGraph", "endNodes": [], "graph": graph}}


def build_entry_points(spec: dict[str, Any]) -> list[dict[str, Any]]:
    values = spec.get("entry_points") or [spec["entry_point"]]
    return [{"$type": "scnEntryPoint", "name": cname(str(value["name"])), "nodeId": scene_node_id(int(value["node_id"]))} for value in values]


def build_exit_points(spec: dict[str, Any]) -> list[dict[str, Any]]:
    return [{"$type": "scnExitPoint", "name": cname(str(exit_spec["name"])), "nodeId": scene_node_id(int(exit_spec["node_id"]))} for exit_spec in spec["exit_points"]]


def build_scene(spec: dict[str, Any]) -> dict[str, Any]:
    base = load_json(path_from_spec(spec, "base_scene"))
    base_root = base["Data"]["RootChunk"]
    spoken_manifest, choice_manifest = load_manifest(spec)
    actors = actor_lookup(spec)
    scene = copy.deepcopy(base)
    root = scene["Data"]["RootChunk"]
    alloc = HandleAllocator(start=3)

    npc_actors, player_actors, debug_symbols = build_actors(spec, base_root)
    screenplay_store, line_ids, option_ids = build_screenplay_store(spec, spoken_manifest, choice_manifest, actors)

    scene["Header"]["ExportedDateTime"] = str(spec.get("exported_datetime", DEFAULT_EXPORTED_DATETIME))
    scene["Header"]["ArchiveFileName"] = str(Path(spec["archive_path"]).resolve())
    root["version"] = 5
    root["cookingPlatform"] = "PLATFORM_PC"
    root["sceneCategoryTag"] = "minorQuests"
    root["actors"] = npc_actors
    root["playerActors"] = player_actors
    root["debugSymbols"] = debug_symbols
    root["entryPoints"] = build_entry_points(spec)
    root["exitPoints"] = build_exit_points(spec)
    root["screenplayStore"] = screenplay_store
    root["locStore"] = build_loc_store(spec, choice_manifest, spoken_manifest)
    root["sceneGraph"] = build_graph(spec, base_root, spoken_manifest, line_ids, option_ids, alloc)
    root["effectDefinitions"] = []
    root["effectInstances"] = []
    root["executionTagEntries"] = []
    root["executionTags"] = []
    root["localMarkers"] = []
    root["notablePoints"] = [{"$type": "scnNotablePoint", "nodeId": scene_node_id(int(choice["node_id"]))} for choice in spec.get("choices", [])]
    root["props"] = build_props(spec, debug_symbols)
    root["referencePoints"] = []
    root["resouresReferences"] = build_resource_refs(spec)
    root["ridResources"] = [
        {
            "$type": "scnRidResourceHandler",
            "id": {"$type": "scnRidResourceId", "id": int(value["resource_id"])},
            # scnRidResourceHandler owns a synchronous CResourceReference.
            # A Soft import can activate the world camera before its RID
            # animation is available, leaving the camera at its entity anchor.
            "ridResource": resource_path(str(value["path"]), flags="Default"),
        }
        for value in spec.get("rid_resources", [])
    ]
    root["voInfo"] = []
    root["workspotInstances"] = []
    root["workspots"] = []
    root["sceneSolutionHash"] = {
        "$type": "scnSceneSolutionHash",
        "sceneSolutionHash": {
            "$type": "scnSceneSolutionHashHash",
            "sceneSolutionHashDate": str(fnv1a64(str(spec["name"]))),
        },
    }
    return scene


def graph_nodes(scene: dict[str, Any]) -> list[dict[str, Any]]:
    return scene["Data"]["RootChunk"]["sceneGraph"]["Data"]["graph"]


def iter_journal_paths(value: Any) -> Iterator[dict[str, Any]]:
    if isinstance(value, dict):
        if value.get("$type") == "gameJournalPath":
            yield value
        for child in value.values():
            yield from iter_journal_paths(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_journal_paths(child)


def validate_scene(scene: dict[str, Any], spec: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    root = scene.get("Data", {}).get("RootChunk", {})
    errors.extend(validate_reference_tables(root))
    if root.get("version") != 5:
        errors.append("Root version must be 5")
    if root.get("cookingPlatform") != "PLATFORM_PC":
        errors.append("cookingPlatform must be PLATFORM_PC")
    if root.get("sceneCategoryTag") != "minorQuests":
        errors.append("sceneCategoryTag must be minorQuests")
    if scene.get("Header", {}).get("ArchiveFileName") != str(Path(spec["archive_path"]).resolve()):
        errors.append("Header.ArchiveFileName does not match spec archive_path")
    expected_exported_datetime = str(spec.get("exported_datetime", DEFAULT_EXPORTED_DATETIME))
    if scene.get("Header", {}).get("ExportedDateTime") != expected_exported_datetime:
        errors.append("Header.ExportedDateTime does not match spec exported_datetime")

    if not isinstance(root.get("entryPoints"), list):
        errors.append("entryPoints must be a vanilla-style array")
    else:
        actual_entry_names = {ep.get("name", {}).get("$value") for ep in root["entryPoints"]}
        for entry_spec in spec.get("entry_points") or [spec["entry_point"]]:
            if entry_spec["name"] not in actual_entry_names:
                errors.append(f"Missing configured entry point: {entry_spec['name']}")

    if not isinstance(root.get("exitPoints"), list):
        errors.append("exitPoints must be a vanilla-style array")
    else:
        actual_exit_names = {
            ep.get("name", {}).get("$value") for ep in root["exitPoints"]
        }
        for exit_spec in spec.get("exit_points", []):
            expected_exit = str(exit_spec["name"])
            if expected_exit not in actual_exit_names:
                errors.append(f"Missing configured exit point: {expected_exit}")

    actor_count = len(root.get("actors", [])) + len(root.get("playerActors", []))
    if actor_count != len(spec.get("actors", [])):
        errors.append(f"Actor count mismatch: {actor_count}")
    actor_ids = [int(actor["id"]) for actor in spec.get("actors", [])]
    if len(actor_ids) != len(set(actor_ids)):
        errors.append("Scene actor ids must be unique")
    actual_actors = {
        actor.get("actorId", {}).get("id"): actor
        for actor in [*root.get("actors", []), *root.get("playerActors", [])]
    }
    for actor_spec in spec.get("actors", []):
        actor = actual_actors.get(int(actor_spec["id"]), {})
        default_tag = "1103967280742240864" if actor_spec.get("kind") == "player" else "0"
        expected_tag = str(actor_spec.get("voicetag", default_tag))
        if str(actor.get("voicetagId", {}).get("id")) != expected_tag:
            errors.append(f"Actor {actor_spec.get('key', actor_spec['id'])} voicetag mismatch")
    player_specs = [
        actor for actor in spec.get("actors", []) if actor.get("kind") == "player"
    ]
    if player_specs and any(int(actor["id"]) != 1 for actor in player_specs):
        errors.append("The real player actor must use actor id 1 / performer 257")
    if any(
        actor.get("kind") != "player" and int(actor["id"]) == 1
        for actor in spec.get("actors", [])
    ):
        errors.append("Actor id 1 / performer 257 is reserved for the real player")
    rid_anim_set_count = len(
        root.get("resouresReferences", {}).get("ridAnimSets", [])
    )
    rid_facial_anim_set_count = len(
        root.get("resouresReferences", {}).get("ridFacialAnimSets", [])
    )
    for actor_spec in spec.get("actors", []):
        actor_key = str(actor_spec.get("key", actor_spec.get("name", "?")))
        for set_id in actor_spec.get("rid_anim_sets", []):
            if not isinstance(set_id, int) or not 0 <= set_id < rid_anim_set_count:
                errors.append(
                    f"Actor {actor_key} references missing RID anim set {set_id}; "
                    f"scene has {rid_anim_set_count} sets"
                )
        for set_id in actor_spec.get("rid_facial_anim_sets", []):
            if (
                not isinstance(set_id, int)
                or not 0 <= set_id < rid_facial_anim_set_count
            ):
                errors.append(
                    f"Actor {actor_key} references missing RID facial anim set {set_id}; "
                    f"scene has {rid_facial_anim_set_count} sets"
                )
    performers = root.get("debugSymbols", {}).get("performersDebugSymbols", [])
    performer_ids = [entry.get("performerId", {}).get("id") for entry in performers]
    expected_performers = [actor_performer_id(int(actor["id"])) for actor in spec.get("actors", [])]
    expected_performers.extend(
        prop_performer_id(int(prop["id"])) for prop in spec.get("props", [])
    )
    if performer_ids != expected_performers:
        errors.append(f"Performer debug symbols mismatch: {performer_ids} != {expected_performers}")

    props = root.get("props", [])
    if len(props) != len(spec.get("props", [])):
        errors.append(f"Prop count mismatch: {len(props)}")
    for index, prop_spec in enumerate(spec.get("props", [])):
        if index >= len(props):
            break
        prop = props[index]
        actual_ref = (
            prop.get("findEntityInNodeParams", {})
            .get("nodeRef", {})
            .get("$value")
        )
        if prop.get("entityAcquisitionPlan") != "findInNode":
            errors.append(f"Prop {index} must use findInNode acquisition")
        if actual_ref != str(prop_spec["node_ref"]):
            errors.append(
                f"Prop {index} nodeRef mismatch: {actual_ref} != {prop_spec['node_ref']}"
            )

    for index, handler in enumerate(root.get("ridResources", [])):
        rid_resource = handler.get("ridResource", {})
        if rid_resource.get("Flags") != "Default":
            errors.append(
                f"RID resource {index} must use a synchronous Default reference"
            )

    screenplay = root.get("screenplayStore", {})
    line_ids = [line.get("itemId", {}).get("id") for line in screenplay.get("lines", [])]
    expected_line_ids = [1 + i * 256 for i in range(len(spec.get("spoken_line_order", [])))]
    if line_ids != expected_line_ids:
        errors.append(f"Spoken screenplay ids mismatch: {line_ids} != {expected_line_ids}")
    option_ids = [option.get("itemId", {}).get("id") for option in screenplay.get("options", [])]
    expected_option_ids = [2 + i * 256 for i in range(len(spec.get("choice_line_order", [])))]
    if option_ids != expected_option_ids:
        errors.append(f"Choice screenplay ids mismatch: {option_ids} != {expected_option_ids}")

    graph_wrappers = list(graph_nodes(scene))
    actual_graph_order = [wrapper.get("Data", {}).get("nodeId", {}).get("id") for wrapper in graph_wrappers]
    if "graph_order" in spec:
        expected_graph_order = [int(node_id) for node_id in spec["graph_order"]]
        if actual_graph_order != expected_graph_order:
            errors.append(f"Scene graph order mismatch: {actual_graph_order} != {expected_graph_order}")

    graph_by_id = {
        int(wrapper["Data"]["nodeId"]["id"]): wrapper["Data"]
        for wrapper in graph_wrappers
        if wrapper.get("Data", {}).get("nodeId", {}).get("id") is not None
    }

    all_node_ids = set(actual_graph_order)
    node_ids = set()
    event_ids: list[str] = []
    for wrapper in graph_wrappers:
        data = wrapper.get("Data", {})
        node_id = data.get("nodeId", {}).get("id")
        if node_id in node_ids:
            errors.append(f"Duplicate scene node id: {node_id}")
        node_ids.add(node_id)
        if data.get("$type") == "scnChoiceNode":
            option_count = len(data.get("options", []))
            sockets = data.get("outputSockets", [])
            choice_sockets = [sock for sock in sockets if sock.get("stamp", {}).get("name") == 0]
            dummy_names = [sock.get("stamp", {}).get("name") for sock in sockets[option_count:]]
            if len(choice_sockets) != option_count:
                errors.append(f"Choice node {node_id} option socket count mismatch")
            if dummy_names != [1, 2, 3, 4, 5, 6]:
                errors.append(f"Choice node {node_id} missing dummy sockets")
        for event in data.get("events", []):
            event_id = str(event.get("Data", {}).get("id", {}).get("id", ""))
            event_ids.append(event_id)
            if event_id == MAX_INT64:
                errors.append(f"Event on node {node_id} still uses max-int placeholder id")
        for socket in data.get("outputSockets", []):
            for dest in socket.get("destinations", []):
                dest_id = dest.get("nodeId", {}).get("id")
                if dest_id not in all_node_ids:
                    errors.append(f"Node {node_id} points to missing node {dest_id}")
                    continue
                target = graph_by_id.get(dest_id, {})
                stamp = dest.get("isockStamp", {})
                if target.get("$type") == "scnSectionNode":
                    if stamp.get("name") != 0 or stamp.get("ordinal") != 0:
                        errors.append(
                            f"Node {node_id} targets a non-executable socket on "
                            f"section node {dest_id}; section flow must use socket 0:0"
                        )
                    continue
                if target.get("$type") != "scnQuestNode":
                    continue
                ordinal = stamp.get("ordinal")
                mappings = [
                    mapping.get("$value")
                    for mapping in target.get("isockMappings", [])
                ]
                mapped_input = (
                    mappings[ordinal]
                    if isinstance(ordinal, int) and 0 <= ordinal < len(mappings)
                    else None
                )
                if mapped_input == "CutDestination" and data.get("$type") != "scnCutControlNode":
                    errors.append(
                        f"Node {node_id} targets CutDestination on quest node {dest_id}; "
                        "ordinary scene flow must use the executable In socket"
                    )
    if len(event_ids) != len(set(event_ids)):
        errors.append("Scene event ids must be unique")

    choice_locstrings = {str(option["locstringId"]["ruid"]) for option in screenplay.get("options", [])}
    screenplay_locstrings = choice_locstrings | {str(line.get("locstringId", {}).get("ruid", "")) for line in screenplay.get("lines", [])}
    variant_ids = [str(entry.get("variantId", {}).get("ruid", "")) for entry in root.get("locStore", {}).get("vpEntries", [])]
    if len(variant_ids) != len(set(variant_ids)):
        errors.append("locStore variant ids must be unique")
    variant_locstring_collisions = sorted(set(variant_ids) & screenplay_locstrings)
    if variant_locstring_collisions:
        errors.append(f"locStore variant ids collide with screenplay locstrings: {variant_locstring_collisions}")
    loc_entries: dict[str, set[str]] = {loc: set() for loc in choice_locstrings}
    db_db_payloads: dict[str, list[str]] = {loc: [] for loc in choice_locstrings}
    vp_entries = root.get("locStore", {}).get("vpEntries", [])
    vd_entries = root.get("locStore", {}).get("vdEntries", [])
    choice_descriptors = [
        entry
        for entry in vd_entries
        if str(entry.get("locstringId", {}).get("ruid", "")) in choice_locstrings
    ]
    locale_blocks: list[str] = []
    for entry in choice_descriptors:
        locale = str(entry.get("localeId", ""))
        if not locale_blocks or locale_blocks[-1] != locale:
            locale_blocks.append(locale)
    if choice_locstrings:
        expected_locale_blocks = [str(locale) for locale in spec.get("choice_locales", ["db_db", "pl_pl", "en_us"])]
        if locale_blocks != expected_locale_blocks:
            errors.append(f"Choice locStore locale blocks mismatch: {locale_blocks} != {expected_locale_blocks}")
        for locale in expected_locale_blocks:
            locale_locstring_ids = [
                int(entry.get("locstringId", {}).get("ruid", 0))
                for entry in choice_descriptors
                if str(entry.get("localeId", "")) == locale
            ]
            if locale_locstring_ids != sorted(locale_locstring_ids):
                errors.append(f"{locale} choice locStore descriptors must be sorted by locstringId")

    for entry in vd_entries:
        loc = str(entry.get("locstringId", {}).get("ruid", ""))
        if loc in loc_entries:
            locale_id = str(entry.get("localeId", ""))
            loc_entries[loc].add(locale_id)
            if locale_id == "db_db":
                vpe_index = entry.get("vpeIndex")
                if isinstance(vpe_index, int) and 0 <= vpe_index < len(vp_entries):
                    db_db_payloads[loc].append(str(vp_entries[vpe_index].get("content", "")))
    required_locales = set(spec.get("choice_locales", ["db_db", "pl_pl", "en_us"]))
    for loc, locales in loc_entries.items():
        if not required_locales.issubset(locales):
            errors.append(f"Choice locstring {loc} missing locales: {sorted(required_locales - locales)}")
        if "db_db" in required_locales and (len(db_db_payloads[loc]) < 2 or "" not in db_db_payloads[loc]):
            errors.append(f"Choice locstring {loc} must include blank and source db_db variants")
        elif "db_db" in required_locales and db_db_payloads[loc][0] != "":
            errors.append(f"Choice locstring {loc} must put the blank db_db variant before the source variant")

    for node_spec in spec.get("quest_nodes", []):
        if node_spec.get("kind") not in {"journal", "mappin"}:
            continue
        expected_index = expected_file_entry_index(str(node_spec["path"]))
        if expected_index is None:
            continue
        actual_index = resolve_file_entry_index(node_spec)
        if actual_index != expected_index:
            errors.append(
                f"Quest node {node_spec['node_id']} path {node_spec['path']} has file_entry_index {actual_index}; expected {expected_index}"
            )

    for journal_path in iter_journal_paths(root):
        real_path = str(journal_path.get("realPath", ""))
        expected_index = expected_file_entry_index(real_path)
        if expected_index is None:
            continue
        actual_index = int(journal_path.get("fileEntryIndex", -1))
        if actual_index != expected_index:
            errors.append(f"Journal path {real_path} has fileEntryIndex {actual_index}; expected {expected_index}")

    return errors


def run_audit(spec: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in ("base_scene", "manifest"):
        path = path_from_spec(spec, key)
        if not path.exists():
            errors.append(f"Missing {key}: {path}")
    source_checks = [
        (Path("WolvenKit/WolvenKit.RED4/Types/ClassesExt/scnSceneResource.cs"), "CalculatePerformerId"),
        (Path("WolvenKit/WolvenKit.RED4/Types/ClassesExt/scnSceneResource.cs"), "1 + actorIndex * 256"),
        (Path("WolvenKit/WolvenKit.RED4/Types/ClassesExt/scnSceneResource.cs"), "2 + propIndex * 256"),
        (Path("WolvenKit/WolvenKit.App/ViewModels/GraphEditor/RedGraph.Scene.cs"), "new scnOutputSocket { Stamp = new scnOutputSocketStamp { Name = 6, Ordinal = 0 } }"),
    ]
    for path, needle in source_checks:
        if not path.exists():
            errors.append(f"Missing WolvenKit source file: {path}")
            continue
        if needle not in path.read_text(encoding="utf-8-sig"):
            errors.append(f"WolvenKit source assumption not found in {path}: {needle}")
    try:
        base = load_json(path_from_spec(spec, "base_scene"))
        if spec_declares_choices(spec):
            load_choice_shell(base["Data"]["RootChunk"], spec.get("choice_shell_node_id"))
    except SystemExit as exc:
        errors.append(str(exc))
    return errors


def write_scene(path: Path, scene: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(scene, indent=2, ensure_ascii=False), encoding="utf-8")


def deserialize(spec: dict[str, Any], red_cli: Path, schema: Path) -> None:
    from artifact_io import publish_json_artifacts
    from project_layout import owning_project
    from quest_build import convert_resource

    raw_path = path_from_spec(spec, "raw_path")
    archive_path = Path(spec["archive_path"])
    staging = owning_project(raw_path) / "generated/scene-builds"
    staging.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f"{archive_path.stem}-", dir=staging) as directory:
        candidate = Path(directory) / archive_path.name
        try:
            convert_resource(
                raw_path, candidate, archive_path if archive_path.is_file() else None,
                serializer="native", wolvenkit=None, red_cli=red_cli, schema_path=schema,
            )
        except RuntimeError as exc:
            raise SceneBuildError(str(exc)) from exc
        publish_json_artifacts({}, binary_artifacts={archive_path: candidate.read_bytes()})


def command_example(_: argparse.Namespace) -> None:
    example = {
        "name": "gq000_patch_meet",
        "base_scene": "reference/vanilla_extract_json/mq003/mq003_03_orbital_pod.scene.json",
        "manifest": "projects/ghostline/quests/gq000/script/gq000_01_manifest.json",
        "raw_path": "projects/shared/ghostline-runtime/source/raw/mod/gq000/scenes/gq000_patch_meet.scene.json",
        "archive_path": "projects/shared/ghostline-runtime/source/archive/mod/gq000/scenes/gq000_patch_meet.scene",
        "actors": [
            {"key": "patch", "name": "patch", "kind": "community", "id": 0, "entry": "patch", "community_ref": "#gq000_01_com_patch_bridge"},
            {"key": "v", "name": "V", "kind": "player", "id": 1, "record": "Character.Player_Puppet_Base"},
        ],
        "spoken_line_order": ["gq000_01_patch_intro_01"],
        "choice_line_order": [],
        "entry_point": {"name": "start", "node_id": 1},
        "exit_points": [{"name": "job_accept", "node_id": 18}],
        "start_node": {"node_id": 1, "on_start": [{"node_id": 2}]},
        "sections": [{"key": "opening_line", "node_id": 2, "lines": ["gq000_01_patch_intro_01"], "on_end": [{"node_id": 18}]}],
        "choices": [],
        "quest_nodes": [],
        "xor_nodes": [],
        "end_node": {"node_id": 18},
    }
    print_json(example)


def load_spec(args: argparse.Namespace) -> dict[str, Any]:
    return load_json(Path(args.spec))


def command_audit(args: argparse.Namespace) -> None:
    spec = load_spec(args)
    errors = run_audit(spec)
    if errors:
        raise SceneBuildError("Audit failed:\n" + "\n".join(f"- {error}" for error in errors))
    print("Scene generator audit passed.")


def command_generate(args: argparse.Namespace) -> None:
    spec = load_spec(args)
    errors = run_audit(spec)
    if errors:
        raise SceneBuildError("Audit failed:\n" + "\n".join(f"- {error}" for error in errors))
    scene = build_scene(spec)
    validation_errors = validate_scene(scene, spec)
    if validation_errors:
        raise SceneBuildError("Generated scene failed validation:\n" + "\n".join(f"- {error}" for error in validation_errors))
    if args.dry_run:
        summary = {
            "raw_path": spec["raw_path"],
            "archive_path": spec["archive_path"],
            "actors": len(scene["Data"]["RootChunk"]["actors"]) + len(scene["Data"]["RootChunk"]["playerActors"]),
            "nodes": len(graph_nodes(scene)),
            "spoken_lines": len(scene["Data"]["RootChunk"]["screenplayStore"]["lines"]),
            "choices": len(scene["Data"]["RootChunk"]["screenplayStore"]["options"]),
        }
        print_json(summary)
        return
    write_scene(path_from_spec(spec, "raw_path"), scene)
    print(f"Wrote {spec['raw_path']}")
    if args.deserialize:
        deserialize(spec, args.red_cli, args.schema)


def command_validate(args: argparse.Namespace) -> None:
    spec = load_spec(args)
    scene = load_json(Path(args.file))
    errors = validate_scene(scene, spec)
    if errors:
        raise SceneBuildError("Scene validation failed:\n" + "\n".join(f"- {error}" for error in errors))
    print("Scene validation passed.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    example_parser = subparsers.add_parser("example", help="Print a minimal scene spec")
    example_parser.set_defaults(func=command_example)

    audit_parser = subparsers.add_parser("audit", help="Verify reference files and encoded WolvenKit assumptions")
    audit_parser.add_argument("--spec", default=str(DEFAULT_SPEC))
    audit_parser.set_defaults(func=command_audit)

    generate_parser = subparsers.add_parser("generate", help="Generate raw .scene CR2W-JSON")
    generate_parser.add_argument("--spec", default=str(DEFAULT_SPEC))
    generate_parser.add_argument("--dry-run", action="store_true")
    generate_parser.add_argument("--deserialize", action="store_true")
    generate_parser.add_argument("--red-cli", type=Path, default=DEFAULT_RED_CLI)
    generate_parser.add_argument("--schema", type=Path, default=DEFAULT_RED_SCHEMA)
    generate_parser.set_defaults(func=command_generate)

    validate_parser = subparsers.add_parser("validate", help="Validate a generated raw .scene JSON file")
    validate_parser.add_argument("--spec", default=str(DEFAULT_SPEC))
    validate_parser.add_argument("--file", required=True)
    validate_parser.set_defaults(func=command_validate)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        args.func(args)
    except SceneBuildError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except subprocess.CalledProcessError as exc:
        print(f"ghostline-red command failed with exit code {exc.returncode}", file=sys.stderr)
        return exc.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
