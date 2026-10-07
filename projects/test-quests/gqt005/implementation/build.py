#!/usr/bin/env python3
"""Generate and package the concrete GQT005 braindance test quest."""

from __future__ import annotations

import argparse
import copy
import json
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


import generate_advanced_quest_block_templates as advanced_templates
import generate_scene as scene_builder
import generate_world as world_builder
import quest_authoring
import quest_build
from quest_content import load
import quest_compiler
from braindance_pipeline import (
    audit_scene_document,
    link_scene_document,
    package_assets,
)

NAME = "gqt005_braindance_analysis"
LAUNCH_NAME = "gqt005_patch_start"
SCENE_DEPOT = rf"mod\gqt005\scenes\{NAME}.scene"
LAUNCH_SCENE_DEPOT = rf"mod\gqt005\scenes\{LAUNCH_NAME}.scene"
RID_DEPOT = rf"mod\gqt005\braindance\{NAME}.scenerid"
SCENE_ORIGIN = "#gqt005_bd_origin"
BD_VIEW_SPAWNER = "#gqt005_bdview_spawner"
CAMERA_REF = "#gqt005_bd_camera"
COMMUNITY = "#gqt005_com_contact"
ENTRY = "patch"
SCENE_SPAWN_SET_ACTORS: list[dict[str, Any]] = []
PLAYER_ACTOR_ID = 2
PLAYER_PERFORMER_ID = 513
CAMERA_PROP_ID = 0
CAMERA_PERFORMER_ID = 2
BD_VIEW_PROP_ID = 1
BD_VIEW_PERFORMER_ID = 258
BD_FOG_PROP_ID = 2
BD_FOG_PERFORMER_ID = 514
BD_SETUP_PROP_ID = 3
BD_SETUP_PERFORMER_ID = 770
VISUAL_CLUE_PROP_ID = 4
VISUAL_CLUE_PERFORMER_ID = 1026
BD_VIEW_DYNAMIC_NAME = "p_gqt005_braindance_analysis_bdview"
BD_FOG_DYNAMIC_NAME = "p_gqt005_braindance_analysis_bdfog"
BD_SETUP_DYNAMIC_NAME = "p_gqt005_braindance_analysis_bdsetup"
VISUAL_CLUE_DYNAMIC_NAME = "p_gqt005_braindance_analysis_encrypted_shard"
CLUE_TARGETS = {
    "encrypted_shard": {
        # The focus-clue scanner must own the same entity that renders the
        # tablet.  A separate meshless proxy cannot receive the vanilla
        # outline/fill vision appearance applied by gameScanningComponent.
        "dynamic_name": VISUAL_CLUE_DYNAMIC_NAME,
        "prop_name": "gqt005_encrypted_shard",
        "record": "Props.GhostlineGQT005BDEncryptedShardClue",
        "availability_fact": "gqt005_bd_encrypted_shard_clue_on",
        "attach": {
            "performer_id": 1,
            "slot": "WeaponLeft",
            "at": "scene_start",
            "offset_mode": "useCustomOffset",
        },
        "focus": {
            "visualizer_style": "onScreen",
            "location_type": "None",
            "activation_range": 3,
            "indication_range": 20,
        },
    },
    "guard_warning": {
        "dynamic_name": "p_gqt005_braindance_analysis_clue_audio",
        "prop_name": "gqt005_bd_clue_audio",
        "record": "Props.GhostlineGQT005BDGuardWarningClue",
        "availability_fact": "gqt005_bd_guard_warning_clue_on",
        # This is a moving-performer clue, unlike Q004's stable world audio
        # emitters.  Keep the scan target on the same performer that owns the
        # spatial audio event.
        "attach": {
            "performer_id": 257,
            "slot": "(Root)",
            "at": "scene_start",
            "offset_mode": "useCustomOffset",
            "position": [0.0, 0.0, 1.55],
        },
        "audio": {
            "event": "q004_sc_04a_thug_breath_long",
            "reverse_event": "q004_sc_04a_thug_breath_long_rev",
            "performer_id": 257,
        },
        "focus": {
            "visualizer_style": "onScreen",
            "location_type": "None",
            "activation_range": 3,
            "indication_range": 20,
        },
    },
    "guard_implant_heat": {
        "dynamic_name": "p_gqt005_braindance_analysis_clue_thermal",
        "prop_name": "gqt005_bd_clue_thermal",
        "record": "Props.GhostlineGQT005BDGuardImplantHeatClue",
        "availability_fact": "gqt005_bd_guard_implant_heat_clue_on",
        "attach": {
            "performer_id": 257,
            "slot": "(Root)",
            "at": "scene_start",
            "offset_mode": "useCustomOffset",
            "position": [0.0, 0.0, 1.2],
        },
        "focus": {
            "visualizer_style": "onScreen",
            "location_type": "None",
            "activation_range": 3,
            "indication_range": 20,
        },
    },
}

WORLD_SPEC = (
    PROJECT / "implementation/world/braindance-analysis.world.json"
)
MANIFEST = PROJECT / "gqt005_braindance_analysis.quest.json"
BDVIEW_RENDER_PRESET = ROOT / "braindance/render_presets/q004_outdoor_bdview.json"
SCENE_TEMPLATE = ROOT / "braindance/templates/braindance_analysis.scene.json"

JOURNAL_RAW = PROJECT / "source/raw/mod/gqt005/journal/gqt005.journal.json"
JOURNAL_ARCHIVE = PROJECT / "source/archive/mod/gqt005/journal/gqt005.journal"
ONSCREEN_RAW = (
    PROJECT / "source/raw/mod/gqt005/localization/en-us/onscreens/gqt005.json.json"
)
ONSCREEN_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt005/localization/en-us/onscreens/gqt005.json"
)
SCENE_RAW = PROJECT / f"source/raw/mod/gqt005/scenes/{NAME}.scene.json"
SCENE_ARCHIVE = PROJECT / f"source/archive/mod/gqt005/scenes/{NAME}.scene"
LAUNCH_SCENE_RAW = PROJECT / f"source/raw/mod/gqt005/scenes/{LAUNCH_NAME}.scene.json"
LAUNCH_SCENE_ARCHIVE = PROJECT / f"source/archive/mod/gqt005/scenes/{LAUNCH_NAME}.scene"
CHOICE_DONOR = ROOT / "projects/shared/ghostline-runtime/source/raw/mod/gq000/scenes/gq000_patch_meet.scene.json"
RID_ARCHIVE = PROJECT / f"source/archive/mod/gqt005/braindance/{NAME}.scenerid"
ROOT_PHASE_RAW = PROJECT / f"source/raw/mod/gqt005/phases/{NAME}.questphase.json"
ROOT_PHASE_ARCHIVE = PROJECT / f"source/archive/mod/gqt005/phases/{NAME}.questphase"
TEMPLATE_RAW = (
    ROOT / "quests/templates/source/raw/mod/ghostline/quest_blocks/templates/"
    "braindance_analysis.questphase.json"
)
TEMPLATE_ARCHIVE = (
    ROOT / "quests/templates/source/archive/mod/ghostline/quest_blocks/templates/"
    "braindance_analysis.questphase"
)
BD_HELPER_RESOURCES = [
    (
        PROJECT / "source/raw/mod/gqt005/braindance/gqt005_bdview.ent.json",
        PROJECT / "source/archive/mod/gqt005/braindance/gqt005_bdview.ent",
        r"mod\gqt005\braindance\gqt005_bdview.ent",
    ),
    (
        PROJECT / "source/raw/mod/gqt005/braindance/gqt005_bdfog.ent.json",
        PROJECT / "source/archive/mod/gqt005/braindance/gqt005_bdfog.ent",
        r"mod\gqt005\braindance\gqt005_bdfog.ent",
    ),
    (
        PROJECT / "source/raw/mod/gqt005/braindance/gqt005_bdsetup.ent.json",
        PROJECT / "source/archive/mod/gqt005/braindance/gqt005_bdsetup.ent",
        r"mod\gqt005\braindance\gqt005_bdsetup.ent",
    ),
    (
        PROJECT / "source/raw/mod/gqt005/braindance/gqt005_bdview.mesh.json",
        PROJECT / "source/archive/mod/gqt005/braindance/gqt005_bdview.mesh",
        r"mod\gqt005\braindance\gqt005_bdview.mesh",
    ),
    (
        PROJECT / "source/raw/mod/gqt005/braindance/gqt005_bdview.mi.json",
        PROJECT / "source/archive/mod/gqt005/braindance/gqt005_bdview.mi",
        r"mod\gqt005\braindance\gqt005_bdview.mi",
    ),
    (
        PROJECT / "source/raw/mod/gqt005/braindance/gqt005_bdfog.mesh.json",
        PROJECT / "source/archive/mod/gqt005/braindance/gqt005_bdfog.mesh",
        r"mod\gqt005\braindance\gqt005_bdfog.mesh",
    ),
    (
        PROJECT / "source/raw/mod/gqt005/braindance/gqt005_reveal_mask.xbm.json",
        PROJECT / "source/archive/mod/gqt005/braindance/gqt005_reveal_mask.xbm",
        r"mod\gqt005\braindance\gqt005_reveal_mask.xbm",
    ),
    (
        PROJECT / "source/raw/mod/gqt005/braindance/gqt005_clues_data.xbm.json",
        PROJECT / "source/archive/mod/gqt005/braindance/gqt005_clues_data.xbm",
        r"mod\gqt005\braindance\gqt005_clues_data.xbm",
    ),
    (
        PROJECT / "source/raw/mod/gqt005/braindance/gqt005_encrypted_shard_clue.ent.json",
        PROJECT / "source/archive/mod/gqt005/braindance/gqt005_encrypted_shard_clue.ent",
        r"mod\gqt005\braindance\gqt005_encrypted_shard_clue.ent",
    ),
    (
        PROJECT / "source/raw/mod/gqt005/braindance/gqt005_guard_warning_clue.ent.json",
        PROJECT / "source/archive/mod/gqt005/braindance/gqt005_guard_warning_clue.ent",
        r"mod\gqt005\braindance\gqt005_guard_warning_clue.ent",
    ),
    (
        ROOT
        / "projects/test-quests/gqt005/source/raw/mod/gqt005/braindance/gqt005_guard_implant_heat_clue.ent.json",
        ROOT
        / "projects/test-quests/gqt005/source/archive/mod/gqt005/braindance/gqt005_guard_implant_heat_clue.ent",
        r"mod\gqt005\braindance\gqt005_guard_implant_heat_clue.ent",
    ),
]

PLAY_BRAINDANCE_CHOICE = "gqt005_play_braindance"
PLAY_BRAINDANCE_TEXT = "Play braindance"
PLAY_BRAINDANCE_ICON = "ChoiceCaptionParts.BraindanceIcon"
PATCH_VOICETAG = "1624173162010260376"
PATCH_LIPSYNC_ANIMSET = (
    "base\\localization\\en-us\\lipsync\\mod\\gq000\\scenes\\gq000_patch_meet\\"
    "civ_low_m_11_enus_40_fat.anims"
)
PATCH_LIPSYNC_LINES = (
    {
        "choice_key": "gqt005_replay_lipsync_intro",
        "caption": "Replay: You made it",
        "locstring": "3552541838326363267",
        "screenplay_item_id": 1,
        "node_id": 11,
    },
    {
        "choice_key": "gqt005_replay_lipsync_location",
        "caption": "Replay: Knew you would",
        "locstring": "1728179479238269697",
        "donor_screenplay_item_id": 2817,
        "screenplay_item_id": 257,
        "node_id": 12,
    },
    {
        "choice_key": "gqt005_replay_lipsync_cache",
        "caption": "Replay: Pull the cache",
        "locstring": "1563333104533324901",
        "donor_screenplay_item_id": 3073,
        "screenplay_item_id": 513,
        "node_id": 13,
    },
    {
        "choice_key": "gqt005_replay_lipsync_network",
        "caption": "Replay: That's the point",
        "locstring": "1855362652331361983",
        "donor_screenplay_item_id": 513,
        "screenplay_item_id": 769,
        "node_id": 14,
    },
)
PATCH_REPLAY_LOOKAT_DONOR = (
    ROOT / "reference/vanilla_extract_json/mq010/mq010_02_barry_talk.scene.json"
)


def write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def review_clue_facts() -> tuple[str, ...]:
    manifest = quest_authoring.normalize_spec(load(MANIFEST))
    stages = [
        stage
        for stage in manifest.get("stages", [])
        if stage.get("id") == "review_braindance"
    ]
    if len(stages) != 1:
        raise ValueError("GQT005 manifest must contain one review_braindance stage")
    facts = stages[0].get("clue_facts")
    if (
        not isinstance(facts, list)
        or not facts
        or not all(isinstance(fact, str) and fact for fact in facts)
        or len(set(facts)) != len(facts)
    ):
        raise ValueError("GQT005 review_braindance clue_facts must be unique names")
    return tuple(facts)


def generate_journal() -> dict[str, Any]:
    """Compatibility accessor for the manifest-owned composition resource."""
    return quest_authoring.compose(load(MANIFEST)).documents[
        "mod\\gqt005\\journal\\gqt005.journal"
    ]


def generate_onscreens() -> dict[str, Any]:
    """Compatibility accessor for the manifest-owned composition resource."""
    return quest_authoring.compose(load(MANIFEST)).documents[
        "mod\\gqt005\\localization\\en-us\\onscreens\\gqt005.json"
    ]


def _quaternion_multiply(
    left: dict[str, Any],
    right: dict[str, Any],
) -> dict[str, float | str]:
    lx, ly, lz, lw = (float(left[axis]) for axis in ("i", "j", "k", "r"))
    rx, ry, rz, rw = (float(right[axis]) for axis in ("i", "j", "k", "r"))
    return {
        "$type": "Quaternion",
        "i": lw * rx + lx * rw + ly * rz - lz * ry,
        "j": lw * ry - lx * rz + ly * rw + lz * rx,
        "k": lw * rz + lx * ry - ly * rx + lz * rw,
        "r": lw * rw - lx * rx - ly * ry - lz * rz,
    }


def _rotate_vector(
    rotation: dict[str, Any],
    vector: tuple[float, float, float],
) -> tuple[float, float, float]:
    x, y, z, w = (float(rotation[axis]) for axis in ("i", "j", "k", "r"))
    vx, vy, vz = vector
    tx = 2.0 * (y * vz - z * vy)
    ty = 2.0 * (z * vx - x * vz)
    tz = 2.0 * (x * vy - y * vx)
    return (
        vx + w * tx + y * tz - z * ty,
        vy + w * ty + z * tx - x * tz,
        vz + w * tz + x * ty - y * tx,
    )


def _vector3(values: tuple[float, float, float]) -> dict[str, Any]:
    return {
        "$type": "Vector3",
        "X": values[0],
        "Y": values[1],
        "Z": values[2],
    }


def build_scene_marker_entries(
    scene_document: dict[str, Any],
) -> list[dict[str, Any]]:
    root = _scene_root(scene_document)
    event_symbol_ids: dict[str, str] = {}
    for symbol in root["debugSymbols"]["sceneEventsDebugSymbols"]:
        editor_event_id = symbol.get("editorEventId")
        if editor_event_id is None:
            continue
        for scene_event_id in symbol.get("sceneEventIds", []):
            value = scene_event_id.get("id")
            if value is not None:
                event_symbol_ids[str(value)] = str(editor_event_id)

    entries: list[tuple[int, dict[str, Any]]] = []
    for node in root["sceneGraph"]["Data"]["graph"]:
        for wrapper in node["Data"].get("events", []):
            event = wrapper.get("Data", {})
            if event.get("$type") != "scnPlaySkAnimEvent":
                continue
            root_motion = event.get("rootMotionData")
            if not isinstance(root_motion, dict) or root_motion.get("enabled") != 1:
                continue
            event_id = str(event.get("id", {}).get("id", ""))
            editor_event_id = event_symbol_ids.get(event_id)
            if editor_event_id is None:
                raise ValueError(
                    f"Body event {event_id or '<missing>'} has no editor "
                    "event ID for scene-marker generation"
                )
            trajectory = root_motion.get("trajectoryLOD")
            if not isinstance(trajectory, list) or not trajectory:
                raise ValueError(f"Body event {event_id} has no root-motion trajectory")
            origin = root_motion["originOffset"]
            origin_position = origin["position"]
            origin_rotation = origin["orientation"]
            end_transform = trajectory[-1]["transform"]
            end_position_local = end_transform["position"]
            rotated_end_position = _rotate_vector(
                origin_rotation,
                (
                    float(end_position_local["X"]),
                    float(end_position_local["Y"]),
                    float(end_position_local["Z"]),
                ),
            )
            start_position = (
                float(origin_position["X"]),
                float(origin_position["Y"]),
                float(origin_position["Z"]),
            )
            end_position = tuple(
                start + delta
                for start, delta in zip(
                    start_position,
                    rotated_end_position,
                    strict=True,
                )
            )
            end_rotation = _quaternion_multiply(
                origin_rotation,
                end_transform["orientation"],
            )
            entries.append(
                (
                    int(editor_event_id),
                    {
                        "$type": "scnSceneMarkerInternalsAnimEventEntry",
                        "endDir": _vector3(
                            _rotate_vector(end_rotation, (0.0, 1.0, 0.0))
                        ),
                        "endName": {
                            "$type": "CName",
                            "$storage": "string",
                            "$value": f"{editor_event_id}_end",
                        },
                        "endPos": _vector3(end_position),
                        "flags": 0,
                        "startDir": _vector3(
                            _rotate_vector(
                                origin_rotation,
                                (0.0, 1.0, 0.0),
                            )
                        ),
                        "startName": {
                            "$type": "CName",
                            "$storage": "string",
                            "$value": f"{editor_event_id}_start",
                        },
                        "startPos": _vector3(start_position),
                    },
                )
            )
    entries.sort(key=lambda item: item[0])
    return [entry for _, entry in entries]


def _scene_root(document: dict[str, Any]) -> dict[str, Any]:
    root = document["Data"]["RootChunk"]
    if root.get("$type") != "scnSceneResource":
        raise ValueError("Scene donor is not an scnSceneResource")
    return root


def _destination(
    node_id: int,
    *,
    ordinal: int = 1,
) -> dict[str, Any]:
    return {
        "$type": "scnInputSocketId",
        "isockStamp": {
            "$type": "scnInputSocketStamp",
            "name": 0,
            "ordinal": ordinal,
        },
        "nodeId": {"$type": "scnNodeId", "id": node_id},
    }


def _actor_reference(
    *,
    community: str | None = None,
    entry: str | None = None,
    dynamic_name: str | None = None,
) -> dict[str, Any]:
    return {
        "$type": "gameEntityReference",
        "dynamicEntityUniqueName": {
            "$type": "CName",
            "$storage": "string" if dynamic_name else "uint64",
            "$value": dynamic_name or "0",
        },
        "names": (
            [
                {
                    "$type": "CName",
                    "$storage": "string",
                    "$value": entry,
                }
            ]
            if entry
            else []
        ),
        "reference": {
            "$type": "NodeRef",
            "$storage": "string" if community else "uint64",
            "$value": community or "0",
        },
        "sceneActorContextName": {
            "$type": "CName",
            "$storage": "string",
            "$value": "None",
        },
        "slotName": {
            "$type": "CName",
            "$storage": "string",
            "$value": "None",
        },
        "type": "EntityRef",
    }


def _retarget_spawned_prop(
    prop: dict[str, Any],
    *,
    prop_id: int,
    name: str,
    dynamic_name: str,
    record_id: str | None = None,
    spawn_marker: str = SCENE_ORIGIN,
    position: tuple[float, float, float] = (0.0, 0.0, 0.0),
) -> dict[str, Any]:
    result = copy.deepcopy(prop)
    result["propId"]["id"] = prop_id
    result["propName"] = name
    spawn = result["spawnDespawnParams"]
    spawn["dynamicEntityUniqueName"]["$storage"] = "string"
    spawn["dynamicEntityUniqueName"]["$value"] = dynamic_name
    spawn["spawnMarkerNodeRef"]["$storage"] = "string"
    spawn["spawnMarkerNodeRef"]["$value"] = spawn_marker
    spawn["spawnMarkerType"] = "Global"
    spawn["spawnOnStart"] = 1
    if record_id is not None:
        result["specPropRecordId"]["$storage"] = "string"
        result["specPropRecordId"]["$value"] = record_id
        spawn["specRecordId"]["$storage"] = "string"
        spawn["specRecordId"]["$value"] = record_id
    spawn["spawnOffset"]["position"].update(
        {
            "W": 0,
            "X": position[0],
            "Y": position[1],
            "Z": position[2],
        }
    )
    return result


def _next_handle_id(value: Any) -> int:
    handles: list[int] = []

    def collect(item: Any) -> None:
        if isinstance(item, dict):
            handle = item.get("HandleId")
            if handle is not None:
                handles.append(int(handle))
            for child in item.values():
                collect(child)
        elif isinstance(item, list):
            for child in item:
                collect(child)

    collect(value)
    return max(handles, default=2) + 1


def _walk(value: Any):
    yield value
    if isinstance(value, dict):
        for child in value.values():
            yield from _walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from _walk(child)


def _vanilla_bdview_render_settings(
    preset: dict[str, Any],
) -> dict[str, Any]:
    """Keep only fields authored by the vanilla Q004 BD visibility event.

    Expanded CR2W defaults are not equivalent to omitted REDengine defaults.
    In particular, writing every render-area ``enable`` flag as true produces
    an almost black editor camera while playback remains visible.
    """
    authored_fields = {
        "BloomAreaSettings": {
            "luminanceThresholdMax",
            "sceneColorScale",
            "bloomColorScale",
        },
        "ChromaticAberrationAreaSettings": {
            "chromaticAberrationEnabled",
            "chromaticAberrationSize",
            "chromaticAberrationExp",
        },
        "ColorGradingAreaSettings": {
            "saturation",
            "gammaValue",
            "gain",
            "ldrLut",
            "hdrLut",
            "forceHdrLut",
        },
        "ImageBasedFlareAreaSettings": {"scale"},
        "VolumetricFogAreaSettings": {
            "albedo",
            "range",
            "fogHeight",
            "density",
            "absorption",
            "ambientScale",
            "globalLightScale",
            "globalLightAnisotropy",
            "localLightRange",
        },
    }
    result = {"override": 1}
    for perspective in ("renderSettingsFPP", "renderSettingsTPP"):
        settings = copy.deepcopy(preset[perspective])
        for wrapper in settings["areaParameters"]:
            data = wrapper["Data"]
            keep = authored_fields[data["$type"]]
            wrapper["Data"] = {
                key: value
                for key, value in data.items()
                if key == "$type" or key in keep
            }
        result[perspective] = settings
    return result


def _remap_owned_handle_ids(value: Any, *, first_id: int) -> None:
    """Give a self-contained donor payload collision-free local handles."""

    if any(isinstance(item, dict) and "HandleRefId" in item for item in _walk(value)):
        raise ValueError(
            "Render preset unexpectedly contains external HandleRefId values"
        )
    next_id = first_id
    for item in _walk(value):
        if not isinstance(item, dict) or "HandleId" not in item:
            continue
        item["HandleId"] = str(next_id)
        next_id += 1


def _launch_choice(
    root: dict[str, Any],
    *,
    braindance_node_id: int,
    allocator: scene_builder.HandleAllocator,
) -> dict[str, Any]:
    donor_root = _scene_root(load(CHOICE_DONOR))
    choice_shell = next(
        wrapper
        for wrapper in donor_root["sceneGraph"]["Data"]["graph"]
        if wrapper["Data"].get("$type") == "scnChoiceNode"
    )
    choice_spec = {
        "node_id": 10,
        "actor_id": 0,
        "options": [
            *(
                {
                    "choice_key": line["choice_key"],
                    "caption": line["caption"],
                    "single_choice": False,
                    "choice_type": 1,
                    "target_node_id": line["node_id"],
                }
                for line in PATCH_LIPSYNC_LINES
            ),
            {
                "choice_key": PLAY_BRAINDANCE_CHOICE,
                "caption": PLAY_BRAINDANCE_TEXT,
                "single_choice": True,
                "choice_type": 1,
                "icon_tags": [PLAY_BRAINDANCE_ICON],
                "target_node_id": braindance_node_id,
            },
        ],
    }
    return scene_builder.build_choice_node(
        choice_shell,
        choice_spec,
        {
            **{
                line["choice_key"]: 2 + (index * 256)
                for index, line in enumerate(PATCH_LIPSYNC_LINES)
            },
            PLAY_BRAINDANCE_CHOICE: 2 + (len(PATCH_LIPSYNC_LINES) * 256),
        },
        allocator,
    )


def _patch_player_lookat_event(
    allocator: scene_builder.HandleAllocator,
    *,
    node_id: int,
    duration: int,
) -> dict[str, Any]:
    donor_root = _scene_root(load(PATCH_REPLAY_LOOKAT_DONOR))
    event = copy.deepcopy(
        next(
            event
            for wrapper in donor_root["sceneGraph"]["Data"]["graph"]
            for event in wrapper["Data"].get("events", [])
            if event["Data"].get("$type") == "scnLookAtEvent"
            and event["Data"]["basicData"]["basic"]["isStart"] == 1
            and event["Data"]["basicData"]["basic"]["performerId"]["id"] == 1
            and event["Data"]["basicData"]["basic"]["targetPerformerId"]["id"] == 257
        )
    )
    scene_builder.reassign_handle_ids(event, allocator)
    event["Data"]["id"]["id"] = scene_builder.deterministic_event_id(
        LAUNCH_NAME, "patch_player_lookat", node_id
    )
    event["Data"]["startTime"] = 0
    event["Data"]["duration"] = duration
    return event


def generate_launch_scene() -> dict[str, Any]:
    result = copy.deepcopy(load(CHOICE_DONOR))
    root = _scene_root(result)
    root["actors"] = [copy.deepcopy(root["actors"][0])]
    patch = root["actors"][0]
    patch["actorName"] = "patch"
    patch["acquisitionPlan"] = "community"
    patch["communityParams"]["entryName"]["$storage"] = "string"
    patch["communityParams"]["entryName"]["$value"] = ENTRY
    patch["communityParams"]["reference"]["$storage"] = "string"
    patch["communityParams"]["reference"]["$value"] = COMMUNITY
    patch["communityParams"]["forceMaxVisibility"] = 0
    patch["voicetagId"]["id"] = PATCH_VOICETAG

    graph = root["sceneGraph"]["Data"]
    selected_nodes = {
        item["Data"]["nodeId"]["id"]: copy.deepcopy(item)
        for item in graph["graph"]
        if item["Data"].get("nodeId", {}).get("id") in {1, 2, 19}
    }
    start = selected_nodes[1]
    section = selected_nodes[2]
    end = selected_nodes[19]
    start["Data"]["outputSockets"] = [scene_builder.output_socket(0, 0, [(2, 0, 0)])]
    section["Data"]["events"] = []
    section["Data"]["actorBehaviors"] = [
        behavior
        for behavior in section["Data"]["actorBehaviors"]
        if behavior["actorId"]["id"] == 0
    ]
    section["Data"]["sectionDuration"]["stu"] = 100
    section["Data"]["outputSockets"] = [
        scene_builder.output_socket(0, 0, [(10, 0, 0)]),
        scene_builder.output_socket(1, 0, [(19, 0, 0)]),
    ]
    allocator = scene_builder.HandleAllocator(_next_handle_id(root))
    donor_root = _scene_root(load(CHOICE_DONOR))
    replay_shell = next(
        wrapper
        for wrapper in donor_root["sceneGraph"]["Data"]["graph"]
        if wrapper["Data"].get("nodeId", {}).get("id") == 2
    )
    donor_events = {
        event["Data"]["screenplayLineId"]["id"]: event
        for wrapper in donor_root["sceneGraph"]["Data"]["graph"]
        if wrapper["Data"].get("$type") == "scnSectionNode"
        for event in wrapper["Data"].get("events", [])
        if event["Data"].get("$type") == "scnDialogLineEvent"
    }
    replays = []
    for line in PATCH_LIPSYNC_LINES:
        replay = copy.deepcopy(replay_shell)
        replay["Data"]["events"] = [
            copy.deepcopy(
                donor_events.get(
                    line.get("donor_screenplay_item_id", line["screenplay_item_id"])
                )
            )
        ]
        replay["Data"]["events"][0]["Data"]["screenplayLineId"] = (
            scene_builder.screenplay_item_id(line["screenplay_item_id"])
        )
        replay["Data"]["events"][0]["Data"]["startTime"] = 0
        line_duration = replay["Data"]["events"][0]["Data"]["duration"]
        replay["Data"]["events"].append(
            _patch_player_lookat_event(
                allocator,
                node_id=line["node_id"],
                duration=line_duration,
            )
        )
        replay["Data"]["sectionDuration"]["stu"] = line_duration + 400
        scene_builder.reassign_handle_ids(replay, allocator)
        replay["Data"]["nodeId"] = scene_builder.scene_node_id(line["node_id"])
        replay["Data"]["outputSockets"] = [
            scene_builder.output_socket(0, 0, [(10, 0, 0)]),
            scene_builder.output_socket(1, 0, [(10, 0, 0)]),
        ]
        replays.append(replay)
    choice = _launch_choice(
        root,
        braindance_node_id=19,
        allocator=allocator,
    )
    graph["graph"] = [start, section, choice, *replays, end]
    graph["startNodes"] = [{"$type": "scnNodeId", "id": 1}]
    graph["endNodes"] = [{"$type": "scnNodeId", "id": 19}]

    root["entryPoints"] = [
        {
            "$type": "scnEntryPoint",
            "name": scene_builder.cname("start"),
            "nodeId": {"$type": "scnNodeId", "id": 1},
        }
    ]
    root["exitPoints"] = [
        {
            "$type": "scnExitPoint",
            "name": scene_builder.cname("play_braindance"),
            "nodeId": {"$type": "scnNodeId", "id": 19},
        }
    ]

    choice_string_id = scene_builder.fnv1a64(f"{LAUNCH_NAME}:{PLAY_BRAINDANCE_CHOICE}")
    choice_manifest = {
        **{
            line["choice_key"]: {
                "string_id": scene_builder.fnv1a64(
                    f"{LAUNCH_NAME}:{line['choice_key']}"
                ),
                "text": line["caption"],
            }
            for line in PATCH_LIPSYNC_LINES
        },
        PLAY_BRAINDANCE_CHOICE: {
            "string_id": choice_string_id,
            "text": PLAY_BRAINDANCE_TEXT,
        },
    }
    root["locStore"] = scene_builder.build_loc_store(
        {
            "name": LAUNCH_NAME,
            "choice_line_order": [
                *(line["choice_key"] for line in PATCH_LIPSYNC_LINES),
                PLAY_BRAINDANCE_CHOICE,
            ],
            "choice_locales": ["db_db", "pl_pl", "en_us"],
        },
        choice_manifest,
    )
    donor_lines = {
        line["locstringId"]["ruid"]: line
        for line in donor_root["screenplayStore"]["lines"]
    }
    root["screenplayStore"]["lines"] = []
    for spec in PATCH_LIPSYNC_LINES:
        line = copy.deepcopy(donor_lines[spec["locstring"]])
        line["itemId"] = scene_builder.screenplay_item_id(spec["screenplay_item_id"])
        animation_name = f"f_{int(spec['locstring']):016X}"
        line["femaleLipsyncAnimationName"] = scene_builder.cname(animation_name)
        line["maleLipsyncAnimationName"] = scene_builder.cname(animation_name)
        root["screenplayStore"]["lines"].append(line)
    root["screenplayStore"]["options"] = [
        *(
            {
                "$type": "scnscreenplayChoiceOption",
                "itemId": scene_builder.screenplay_item_id(2 + (index * 256)),
                "locstringId": scene_builder.locstring_id(
                    choice_manifest[line["choice_key"]]["string_id"]
                ),
                "usage": {
                    "$type": "scnscreenplayOptionUsage",
                    "playerGenderMask": {
                        "$type": "scnGenderMask",
                        "mask": 3,
                    },
                },
            }
            for index, line in enumerate(PATCH_LIPSYNC_LINES)
        ),
        {
            "$type": "scnscreenplayChoiceOption",
            "itemId": scene_builder.screenplay_item_id(
                2 + (len(PATCH_LIPSYNC_LINES) * 256)
            ),
            "locstringId": scene_builder.locstring_id(choice_string_id),
            "usage": {
                "$type": "scnscreenplayOptionUsage",
                "playerGenderMask": {
                    "$type": "scnGenderMask",
                    "mask": 3,
                },
            },
        },
    ]
    for field in (
        "props",
        "workspotInstances",
        "workspots",
        "localMarkers",
        "notablePoints",
        "effectDefinitions",
        "effectInstances",
        "executionTagEntries",
        "executionTags",
    ):
        root[field] = []
    debug_symbols = root["debugSymbols"]
    debug_symbols["performersDebugSymbols"] = copy.deepcopy(
        _scene_root(load(CHOICE_DONOR))["debugSymbols"]["performersDebugSymbols"]
    )
    patch_symbol = next(
        symbol
        for symbol in debug_symbols["performersDebugSymbols"]
        if symbol["performerId"]["id"] == 1
    )
    patch_symbol["entityRef"]["reference"]["$storage"] = "string"
    patch_symbol["entityRef"]["reference"]["$value"] = COMMUNITY
    debug_symbols["sceneEventsDebugSymbols"] = []
    debug_symbols["sceneNodesDebugSymbols"] = []
    debug_symbols["workspotsDebugSymbols"] = []
    references = root["resouresReferences"]
    for field, value in references.items():
        if field != "$type" and isinstance(value, list):
            references[field] = []
    references["lipsyncAnimSets"] = [
        {
            "$type": "scnLipsyncAnimSetSRRef",
            "asyncRefLipsyncAnimSet": scene_builder.resource_path(
                PATCH_LIPSYNC_ANIMSET
            ),
            "lipsyncAnimSet": scene_builder.resource_path(
                0,
                storage="uint64",
                flags="Default",
            ),
        }
    ]
    for scenario in root["interruptionScenarios"]:
        scenario["enabled"] = 0
    result["Header"]["ArchiveFileName"] = str(LAUNCH_SCENE_ARCHIVE.resolve())
    result["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return result


def generate_scene(
    template_path: Path,
    rid_json: Path,
    handoff: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Inspect the linked scene and audit before complete-build publication."""
    template = load(template_path)
    linked, report = link_scene_document(
        template,
        load(rid_json),
        load(handoff),
        rid_depot_path=RID_DEPOT,
        scene_origin=SCENE_ORIGIN,
        camera_ref=CAMERA_REF,
        clue_targets=CLUE_TARGETS,
        scene_depot_path=SCENE_DEPOT,
        scene_spawn_set_actors=SCENE_SPAWN_SET_ACTORS,
    )
    return linked, report


def quest_artifacts(
    *, template_document: dict[str, Any] | None = None
) -> list[quest_compiler.QuestArtifact]:
    return quest_compiler.compile_manifest_artifacts(
        MANIFEST,
        ROOT_PHASE_RAW,
        ROOT_PHASE_ARCHIVE,
        template_documents={
            r"mod\ghostline\quest_blocks\templates\braindance_analysis.questphase": template_document
        }
        if template_document is not None
        else None,
    )


def _collect_artifacts(
    *,
    output_root: Path | None = None,
    scene_template: Path = SCENE_TEMPLATE,
    rid_json: Path = PROJECT / f".tmp/braindance/gqt005/{NAME}.scenerid.json",
    handoff: Path = PROJECT / f".tmp/braindance/gqt005/{NAME}.handoff.json",
) -> tuple[
    list[quest_compiler.QuestArtifact],
    dict[str, Any],
    list[world_builder.GeneratedFile],
]:
    """Keep authored RID/scene linking and marker generation in one build pass."""
    template_document = advanced_templates.build_braindance_analysis()
    scene_document, report = generate_scene(scene_template, rid_json, handoff)
    if not report["ok"]:
        raise ValueError("Generated scene failed structural audit")
    world_spec = load(WORLD_SPEC)
    origin_marker = next(
        marker for marker in world_spec["markers"] if marker["ref"] == SCENE_ORIGIN
    )
    origin_marker["scene_marker"] = True
    origin_marker["scene_marker_entries"] = build_scene_marker_entries(scene_document)
    world_outputs, world_documents = world_builder.build_world_documents(
        world_spec,
        PROJECT / "source/raw",
        PROJECT / "source/archive",
    )
    artifacts = [
        quest_compiler.QuestArtifact(
            LAUNCH_SCENE_RAW, LAUNCH_SCENE_ARCHIVE, generate_launch_scene()
        ),
        quest_compiler.QuestArtifact(SCENE_RAW, SCENE_ARCHIVE, scene_document),
        *[
            quest_compiler.QuestArtifact(
                item.raw_path, item.archive_path, world_documents[item.raw_path]
            )
            for item in world_outputs
        ],
        *(
            quest_compiler.QuestArtifact(raw, archive, load(raw))
            for raw, archive, _ in BD_HELPER_RESOURCES
        ),
        *quest_artifacts(template_document=template_document),
    ]
    return quest_build.relocate_artifacts(artifacts, output_root), report, world_outputs


def build_artifacts(
    output_root: Path | None = None,
    *,
    scene_template: Path = SCENE_TEMPLATE,
    rid_json: Path = PROJECT / f".tmp/braindance/gqt005/{NAME}.scenerid.json",
    handoff: Path = PROJECT / f".tmp/braindance/gqt005/{NAME}.handoff.json",
) -> list[quest_compiler.QuestArtifact]:
    """Build composition and the custom braindance resources without publishing."""
    artifacts, _, _ = _collect_artifacts(
        output_root=output_root,
        scene_template=scene_template,
        rid_json=rid_json,
        handoff=handoff,
    )
    return artifacts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--scene-template",
        type=Path,
        default=SCENE_TEMPLATE,
        help=(
            "Owned Ghostline scene template. Normal generation never reads "
            "a vanilla scene donor."
        ),
    )
    parser.add_argument(
        "--rid-json",
        type=Path,
        default=PROJECT / f".tmp/braindance/gqt005/{NAME}.scenerid.json",
    )
    parser.add_argument(
        "--handoff",
        type=Path,
        default=PROJECT / f".tmp/braindance/gqt005/{NAME}.handoff.json",
    )
    parser.add_argument(
        "--rid-binary",
        type=Path,
        default=PROJECT / f".tmp/braindance/gqt005/{NAME}.scenerid",
    )
    parser.add_argument("--wolvenkit", type=Path)
    parser.add_argument(
        "--serializer",
        choices=("wolvenkit", "native"),
        default="wolvenkit",
        help=(
            "CR2W writer for generated resources. WolvenKit is the runtime-safe "
            "default; native remains available for differential validation."
        ),
    )
    parser.add_argument("--deserialize", action="store_true")
    parser.add_argument(
        "--out-root", type=Path, help="Build all resources in an isolated output tree"
    )
    args = parser.parse_args()
    output_root = (args.out_root or PROJECT).resolve()

    artifacts, report, world_outputs = _collect_artifacts(
        output_root=args.out_root,
        scene_template=args.scene_template,
        rid_json=args.rid_json,
        handoff=args.handoff,
    )
    raw_outputs = quest_build.publish_build(
        artifacts,
        namespace="gqt005",
        output_root=args.out_root,
        deserialize=args.deserialize,
        serializer=args.serializer,
        wolvenkit=args.wolvenkit,
        binary_assets={
            PROJECT / "source/archive" / RID_DEPOT.replace("\\", "/"): args.rid_binary
        },
    )
    write(
        (args.out_root or PROJECT) / f".tmp/braindance/gqt005/{NAME}.scene-report.json",
        report,
    )
    quest_spec, _ = quest_compiler.load_spec(MANIFEST)
    if quest_spec is None:
        raise ValueError("GQT005 manifest became invalid after generation")
    if args.deserialize:
        archive_root = output_root / "source/archive"
        mappings = [
            (archive_root / RID_DEPOT.replace("\\", "/"), RID_DEPOT),
            *[
                (archive, archive.relative_to(archive_root).as_posix())
                for _, archive in raw_outputs
                if archive.name != TEMPLATE_ARCHIVE.name
            ],
        ]
        package = package_assets(
            mappings,
            depot_root=(args.out_root or PROJECT).resolve() / "source/archive",
        )
        write(
            (args.out_root or PROJECT) / ".tmp/braindance/gqt005/package.json",
            package,
        )

    scene_audit = audit_scene_document(
        next(
            artifact.document
            for artifact in artifacts
            if artifact.archive_path.name == SCENE_ARCHIVE.name
        ),
        handoff=load(args.handoff),
    )
    print(
        json.dumps(
            {
                "ok": scene_audit["ok"],
                "scene": str(output_root / SCENE_RAW.relative_to(PROJECT)),
                "launch_scene": str(output_root / LAUNCH_SCENE_RAW.relative_to(PROJECT)),
                "quest": str(output_root / ROOT_PHASE_RAW.relative_to(PROJECT)),
                "children": [
                    str(
                        output_root
                        / quest_compiler.resource_paths(stage.phase_resource)[
                            0
                        ].relative_to(PROJECT)
                    )
                    for stage in quest_spec.stages
                ],
                "journal": str(output_root / JOURNAL_RAW.relative_to(PROJECT)),
                "world": [
                    str(output_root / item.raw_path.relative_to(PROJECT))
                    for item in world_outputs
                ],
                "packed": bool(args.deserialize),
                "clue_layers": scene_audit["clue_layers"],
            },
            indent=2,
        )
    )
    return 0 if scene_audit["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
