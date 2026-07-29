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
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import generate_advanced_quest_block_templates as advanced_templates
import generate_scene as scene_builder
import generate_world as world_builder
import ghostline_red
import quest_compiler
from braindance_pipeline import (
    audit_scene_document,
    deserialize_cr2w_json,
    find_wolvenkit,
    link_scene_document,
    package_assets,
)
from quest_content import Handles, find_entry, load, loc

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
OBJECTIVE = "quests/minor_quest/gqt005/gqt005_01/gqt005_01_obj_review_braindance"
MAPPIN = f"{OBJECTIVE}/gqt005_01_qmp_braindance"

JOURNAL_TEMPLATE = ROOT / "source/raw/mod/gqt001/journal/gqt001.journal.json"
ONSCREEN_TEMPLATE = (
    ROOT / "source/raw/mod/gqt001/localization/en-us/onscreens/gqt001.json.json"
)
WORLD_SPEC = (
    ROOT / "quests/tests/gqt005/implementation/world/braindance-analysis.world.json"
)
MANIFEST = ROOT / "quests/tests/gqt005_braindance_analysis.quest.json"
BDVIEW_RENDER_PRESET = ROOT / "braindance/render_presets/q004_outdoor_bdview.json"
SCENE_TEMPLATE = ROOT / "braindance/templates/braindance_analysis.scene.json"

JOURNAL_RAW = ROOT / "source/raw/mod/gqt005/journal/gqt005.journal.json"
JOURNAL_ARCHIVE = ROOT / "source/archive/mod/gqt005/journal/gqt005.journal"
ONSCREEN_RAW = (
    ROOT / "source/raw/mod/gqt005/localization/en-us/onscreens/gqt005.json.json"
)
ONSCREEN_ARCHIVE = (
    ROOT / "source/archive/mod/gqt005/localization/en-us/onscreens/gqt005.json"
)
SCENE_RAW = ROOT / f"source/raw/mod/gqt005/scenes/{NAME}.scene.json"
SCENE_ARCHIVE = ROOT / f"source/archive/mod/gqt005/scenes/{NAME}.scene"
LAUNCH_SCENE_RAW = ROOT / f"source/raw/mod/gqt005/scenes/{LAUNCH_NAME}.scene.json"
LAUNCH_SCENE_ARCHIVE = ROOT / f"source/archive/mod/gqt005/scenes/{LAUNCH_NAME}.scene"
CHOICE_DONOR = ROOT / "source/raw/mod/gq000/scenes/gq000_patch_meet.scene.json"
RID_ARCHIVE = ROOT / f"source/archive/mod/gqt005/braindance/{NAME}.scenerid"
ROOT_PHASE_RAW = ROOT / f"source/raw/mod/gqt005/phases/{NAME}.questphase.json"
ROOT_PHASE_ARCHIVE = ROOT / f"source/archive/mod/gqt005/phases/{NAME}.questphase"
TEMPLATE_RAW = (
    ROOT / "source/raw/mod/ghostline/quest_blocks/templates/"
    "braindance_analysis.questphase.json"
)
TEMPLATE_ARCHIVE = (
    ROOT / "source/archive/mod/ghostline/quest_blocks/templates/"
    "braindance_analysis.questphase"
)
BD_HELPER_RESOURCES = [
    (
        ROOT / "source/raw/mod/gqt005/braindance/gqt005_bdview.ent.json",
        ROOT / "source/archive/mod/gqt005/braindance/gqt005_bdview.ent",
        r"mod\gqt005\braindance\gqt005_bdview.ent",
    ),
    (
        ROOT / "source/raw/mod/gqt005/braindance/gqt005_bdfog.ent.json",
        ROOT / "source/archive/mod/gqt005/braindance/gqt005_bdfog.ent",
        r"mod\gqt005\braindance\gqt005_bdfog.ent",
    ),
    (
        ROOT / "source/raw/mod/gqt005/braindance/gqt005_bdsetup.ent.json",
        ROOT / "source/archive/mod/gqt005/braindance/gqt005_bdsetup.ent",
        r"mod\gqt005\braindance\gqt005_bdsetup.ent",
    ),
    (
        ROOT / "source/raw/mod/gqt005/braindance/gqt005_bdview.mesh.json",
        ROOT / "source/archive/mod/gqt005/braindance/gqt005_bdview.mesh",
        r"mod\gqt005\braindance\gqt005_bdview.mesh",
    ),
    (
        ROOT / "source/raw/mod/gqt005/braindance/gqt005_bdview.mi.json",
        ROOT / "source/archive/mod/gqt005/braindance/gqt005_bdview.mi",
        r"mod\gqt005\braindance\gqt005_bdview.mi",
    ),
    (
        ROOT / "source/raw/mod/gqt005/braindance/gqt005_bdfog.mesh.json",
        ROOT / "source/archive/mod/gqt005/braindance/gqt005_bdfog.mesh",
        r"mod\gqt005\braindance\gqt005_bdfog.mesh",
    ),
    (
        ROOT / "source/raw/mod/gqt005/braindance/gqt005_reveal_mask.xbm.json",
        ROOT / "source/archive/mod/gqt005/braindance/gqt005_reveal_mask.xbm",
        r"mod\gqt005\braindance\gqt005_reveal_mask.xbm",
    ),
    (
        ROOT / "source/raw/mod/gqt005/braindance/gqt005_clues_data.xbm.json",
        ROOT / "source/archive/mod/gqt005/braindance/gqt005_clues_data.xbm",
        r"mod\gqt005\braindance\gqt005_clues_data.xbm",
    ),
    (
        ROOT / "source/raw/mod/gqt005/braindance/gqt005_encrypted_shard_clue.ent.json",
        ROOT / "source/archive/mod/gqt005/braindance/gqt005_encrypted_shard_clue.ent",
        r"mod\gqt005\braindance\gqt005_encrypted_shard_clue.ent",
    ),
    (
        ROOT / "source/raw/mod/gqt005/braindance/gqt005_guard_warning_clue.ent.json",
        ROOT / "source/archive/mod/gqt005/braindance/gqt005_guard_warning_clue.ent",
        r"mod\gqt005\braindance\gqt005_guard_warning_clue.ent",
    ),
    (
        ROOT
        / "source/raw/mod/gqt005/braindance/gqt005_guard_implant_heat_clue.ent.json",
        ROOT
        / "source/archive/mod/gqt005/braindance/gqt005_guard_implant_heat_clue.ent",
        r"mod\gqt005\braindance\gqt005_guard_implant_heat_clue.ent",
    ),
]

TEXT = {
    "gl_gqt005_title": "Braindance Analysis",
    "gl_gqt005_01_objective_review_braindance": (
        "Review the recording and scan all three clue layers."
    ),
    "gl_gqt005_description": (
        "Exercise authored braindance animation, rewind, analysis layers, and cleanup."
    ),
    "gl_gqt005_mappin": "Braindance test",
    "gl_gqt005_bd_clue_encrypted_shard_name": "Encrypted Shard",
    "gl_gqt005_bd_clue_encrypted_shard_description_01": (
        "An encrypted shard used during the recorded exchange."
    ),
    "gl_gqt005_bd_clue_encrypted_shard_description_02": (
        "Its protection obscures the data and its intended recipient."
    ),
    "gl_gqt005_bd_clue_guard_warning_name": "Guard's Warning",
    "gl_gqt005_bd_clue_guard_warning_description_01": (
        "A warning concealed beneath the surrounding street noise."
    ),
    "gl_gqt005_bd_clue_guard_warning_description_02": (
        "The speaker is alerting Patch to danger around the exchange."
    ),
    "gl_gqt005_bd_clue_guard_implant_heat_name": "Overheated Implant",
    "gl_gqt005_bd_clue_guard_implant_heat_description_01": (
        "An abnormal heat signature is coming from the guard's implant."
    ),
    "gl_gqt005_bd_clue_guard_implant_heat_description_02": (
        "The thermal spike suggests the implant was under heavy load."
    ),
}
PLAY_BRAINDANCE_CHOICE = "gqt005_play_braindance"
PLAY_BRAINDANCE_TEXT = "Play braindance"
PLAY_BRAINDANCE_ICON = "ChoiceCaptionParts.BraindanceIcon"


def write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def review_clue_facts() -> tuple[str, ...]:
    manifest = load(MANIFEST)
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
    journal = load(JOURNAL_TEMPLATE)
    handles = Handles(journal)
    quest = find_entry(journal, "gameJournalQuest", "gqt001")
    quest["Data"]["id"] = "gqt005"
    quest["Data"]["title"] = loc("gl_gqt005_title")

    phase_template = find_entry(journal, "gameJournalQuestPhase", "gqt001_01")
    objective_template = find_entry(
        journal,
        "gameJournalQuestObjective",
        "gqt001_01_obj_reach_terminal",
    )
    map_template = next(
        item
        for item in objective_template["Data"]["entries"]
        if item["Data"]["$type"] == "gameJournalQuestMapPin"
    )
    description_template = next(
        item
        for item in objective_template["Data"]["entries"]
        if item["Data"]["$type"] == "gameJournalQuestDescription"
    )

    phase = handles.clone(phase_template)
    phase["Data"]["id"] = "gqt005_01"
    objective = handles.clone(objective_template)
    objective["Data"]["id"] = "gqt005_01_obj_review_braindance"
    objective["Data"]["counter"] = len(review_clue_facts())
    objective["Data"]["description"] = loc("gl_gqt005_01_objective_review_braindance")
    pin = handles.clone(map_template)
    pin["Data"]["id"] = "gqt005_01_qmp_braindance"
    pin["Data"]["reference"]["reference"]["$storage"] = "string"
    pin["Data"]["reference"]["reference"]["$value"] = SCENE_ORIGIN
    pin["Data"]["mappinData"]["debugCaption"] = "gl_gqt005_mappin"
    pin["Data"]["mappinData"]["localizedCaption"] = loc("gl_gqt005_mappin")
    description = handles.clone(description_template)
    description["Data"]["id"] = "gqt005_01_desc_review_braindance"
    description["Data"]["description"] = loc("gl_gqt005_description")
    objective["Data"]["entries"] = [pin, description]
    phase["Data"]["entries"] = [objective]
    quest["Data"]["entries"] = [phase]

    contacts = find_entry(journal, "gameJournalPrimaryFolderEntry", "contacts")
    contacts["Data"]["entries"] = []
    onscreens = find_entry(journal, "gameJournalFolderEntry", "gqt001")
    onscreens["Data"]["id"] = "gqt005"
    onscreens["Data"]["entries"] = []
    poi = find_entry(
        journal,
        "gameJournalPointOfInterestMappin",
        "gqt001_01_poi_terminal",
    )
    poi["Data"]["id"] = "gqt005_01_poi_braindance"
    poi["Data"]["staticNodeRef"]["$storage"] = "string"
    poi["Data"]["staticNodeRef"]["$value"] = SCENE_ORIGIN
    poi["Data"]["questPath"]["Data"]["realPath"] = "quests/minor_quest/gqt005"
    journal["Header"]["ArchiveFileName"] = str(JOURNAL_ARCHIVE.resolve())
    journal["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return journal


def generate_onscreens() -> dict[str, Any]:
    result = load(ONSCREEN_TEMPLATE)
    result["Data"]["RootChunk"]["root"]["Data"]["entries"] = [
        {
            "$type": "localizationPersistenceOnScreenEntry",
            "femaleVariant": text,
            "maleVariant": "",
            "primaryKey": "0",
            "secondaryKey": key,
        }
        for key, text in TEXT.items()
    ]
    result["Header"]["ArchiveFileName"] = str(ONSCREEN_ARCHIVE.resolve())
    result["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return result


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


def generate_world() -> list[world_builder.GeneratedFile]:
    spec = load(WORLD_SPEC)
    origin_marker = next(
        marker for marker in spec["markers"] if marker["ref"] == SCENE_ORIGIN
    )
    origin_marker["scene_marker"] = True
    origin_marker["scene_marker_entries"] = build_scene_marker_entries(load(SCENE_RAW))
    return world_builder.build_world(
        spec,
        ROOT / "source/raw",
        ROOT / "source/archive",
    )


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


def _play_braindance_choice(
    root: dict[str, Any],
    *,
    target_node_id: int,
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
            {
                "choice_key": PLAY_BRAINDANCE_CHOICE,
                "caption": PLAY_BRAINDANCE_TEXT,
                "single_choice": True,
                "choice_type": 1,
                "icon_tags": [PLAY_BRAINDANCE_ICON],
                "target_node_id": target_node_id,
            }
        ],
    }
    return scene_builder.build_choice_node(
        choice_shell,
        choice_spec,
        {PLAY_BRAINDANCE_CHOICE: 2},
        scene_builder.HandleAllocator(_next_handle_id(root)),
    )


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
    choice = _play_braindance_choice(root, target_node_id=19)
    graph["graph"] = [start, section, choice, end]
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
        PLAY_BRAINDANCE_CHOICE: {
            "string_id": choice_string_id,
            "text": PLAY_BRAINDANCE_TEXT,
        }
    }
    root["locStore"] = scene_builder.build_loc_store(
        {
            "name": LAUNCH_NAME,
            "choice_line_order": [PLAY_BRAINDANCE_CHOICE],
            "choice_locales": ["db_db", "pl_pl", "en_us"],
        },
        choice_manifest,
    )
    root["screenplayStore"]["lines"] = []
    root["screenplayStore"]["options"] = [
        {
            "$type": "scnscreenplayChoiceOption",
            "itemId": scene_builder.screenplay_item_id(2),
            "locstringId": scene_builder.locstring_id(choice_string_id),
            "usage": {
                "$type": "scnscreenplayOptionUsage",
                "playerGenderMask": {
                    "$type": "scnGenderMask",
                    "mask": 3,
                },
            },
        }
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
    for scenario in root["interruptionScenarios"]:
        scenario["enabled"] = 0
    result["Header"]["ArchiveFileName"] = str(LAUNCH_SCENE_ARCHIVE.resolve())
    result["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    write(LAUNCH_SCENE_RAW, result)
    return result


def generate_scene(
    template_path: Path,
    rid_json: Path,
    handoff: Path,
    *,
    wolvenkit: Path | None,
    deserialize_scene: bool,
) -> dict[str, Any]:
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
    write(SCENE_RAW, linked)
    if deserialize_scene:
        report["binary"] = deserialize_cr2w_json(
            SCENE_RAW,
            SCENE_ARCHIVE,
            wolvenkit=find_wolvenkit(wolvenkit),
        )
    report_path = ROOT / f".tmp/braindance/gqt005/{NAME}.scene-report.json"
    write(report_path, report)
    return report


def preserve_review_objective_across_handoff(
    document: dict[str, Any],
    objective: str,
) -> dict[str, Any]:
    """Keep the review objective active across the Patch scene handoff."""

    graph_nodes = document["Data"]["RootChunk"]["graph"]["Data"]["nodes"]
    journal_nodes = [
        wrapper
        for wrapper in graph_nodes
        if wrapper.get("Data", {}).get("$type") == "questJournalNodeDefinition"
        and wrapper["Data"]
        .get("type", {})
        .get("Data", {})
        .get("path", {})
        .get("Data", {})
        .get("realPath")
        == objective
    ]
    if len(journal_nodes) != 1:
        raise ValueError(
            "Expected one meet-stage review objective transition, found "
            f"{len(journal_nodes)}"
        )
    journal = journal_nodes[0]

    definitions = {
        str(item["HandleId"]): item
        for item in _walk(document)
        if isinstance(item, dict)
        and "HandleId" in item
        and isinstance(item.get("Data"), dict)
    }

    def handle_id(wrapper: dict[str, Any]) -> str:
        value = wrapper.get("HandleId", wrapper.get("HandleRefId"))
        if value is None:
            raise ValueError("Expected a CR2W handle wrapper")
        return str(value)

    def resolve(wrapper: dict[str, Any]) -> dict[str, Any]:
        return definitions[handle_id(wrapper)]

    def socket(name: str) -> tuple[int, dict[str, Any]]:
        for index, wrapper in enumerate(journal["Data"]["sockets"]):
            definition = resolve(wrapper)
            if definition["Data"].get("name", {}).get("$value") == name:
                return index, definition
        raise ValueError(f"Meet-stage objective has no {name} socket")

    succeeded_index, succeeded_socket = socket("Succeeded")
    _, output_socket = socket("Out")
    succeeded_id = handle_id(succeeded_socket)
    output_id = handle_id(output_socket)
    connections = [
        item
        for item in _walk(document)
        if isinstance(item, dict)
        and item.get("Data", {}).get("$type") == "graphGraphConnectionDefinition"
    ]
    incoming = [
        item
        for item in connections
        if handle_id(item["Data"]["destination"]) == succeeded_id
    ]
    outgoing = [
        item for item in connections if handle_id(item["Data"]["source"]) == output_id
    ]
    if len(incoming) != 1 or len(outgoing) != 1:
        raise ValueError(
            "Meet-stage objective handoff must have exactly one incoming "
            "and one outgoing edge"
        )

    incoming_connection = incoming[0]
    outgoing_connection = outgoing[0]
    incoming_id = handle_id(incoming_connection)
    old_objective_destination = copy.deepcopy(
        incoming_connection["Data"]["destination"]
    )
    next_destination = copy.deepcopy(outgoing_connection["Data"]["destination"])
    if "HandleId" not in old_objective_destination:
        raise ValueError("Objective input socket must be defined by its incoming edge")
    if "HandleId" not in next_destination:
        raise ValueError("Mappin input socket must be defined by the objective edge")

    old_objective_destination["Data"]["connections"] = []
    journal["Data"]["sockets"][succeeded_index] = old_objective_destination
    next_destination["Data"]["connections"] = [{"HandleRefId": incoming_id}]
    incoming_connection["Data"]["destination"] = next_destination
    output_socket["Data"]["connections"] = []

    quest_compiler.validate_handle_graph(
        document,
        context="gqt005 meet objective handoff",
    )
    quest_compiler.validate_no_forward_handle_refs(
        document,
        context="gqt005 meet objective handoff",
    )
    return document


def compile_quest() -> list[tuple[Path, Path]]:
    spec, diagnostics = quest_compiler.load_spec(MANIFEST)
    if spec is None:
        raise ValueError(
            "Invalid GQT005 manifest: "
            + "; ".join(item.message for item in diagnostics)
        )
    diagnostics.extend(quest_compiler.audit_resources(spec))
    errors = [item for item in diagnostics if item.level == "error"]
    if errors:
        raise ValueError(
            "GQT005 resource audit failed: "
            + "; ".join(item.message for item in errors)
        )
    root_phase = quest_compiler.build_orchestration_phase(
        spec,
        ROOT_PHASE_ARCHIVE,
    )
    write(ROOT_PHASE_RAW, root_phase)
    outputs = [(ROOT_PHASE_RAW, ROOT_PHASE_ARCHIVE)]
    for stage in spec.stages:
        raw, archive = quest_compiler.resource_paths(stage.phase_resource)
        child = quest_compiler.build_stage_phase(
            stage,
            archive,
            spec.phase_prefabs,
        )
        if stage.id == "meet_patch":
            preserve_review_objective_across_handoff(
                child,
                stage.data["objective"],
            )
        write(raw, child)
        outputs.append((raw, archive))
    return outputs


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
        default=ROOT / f".tmp/braindance/gqt005/{NAME}.scenerid.json",
    )
    parser.add_argument(
        "--handoff",
        type=Path,
        default=ROOT / f".tmp/braindance/gqt005/{NAME}.handoff.json",
    )
    parser.add_argument(
        "--rid-binary",
        type=Path,
        default=ROOT / f".tmp/braindance/gqt005/{NAME}.scenerid",
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
    args = parser.parse_args()

    write(
        TEMPLATE_RAW,
        advanced_templates.build_braindance_analysis(),
    )
    raw_outputs: list[tuple[Path, Path]] = []
    write(JOURNAL_RAW, generate_journal())
    write(ONSCREEN_RAW, generate_onscreens())
    raw_outputs.extend(
        [
            (JOURNAL_RAW, JOURNAL_ARCHIVE),
            (ONSCREEN_RAW, ONSCREEN_ARCHIVE),
            (TEMPLATE_RAW, TEMPLATE_ARCHIVE),
            *[(raw, archive) for raw, archive, _ in BD_HELPER_RESOURCES],
        ]
    )
    generate_launch_scene()
    raw_outputs.append((LAUNCH_SCENE_RAW, LAUNCH_SCENE_ARCHIVE))

    report = generate_scene(
        args.scene_template,
        args.rid_json,
        args.handoff,
        wolvenkit=args.wolvenkit,
        deserialize_scene=args.deserialize,
    )
    if not report["ok"]:
        raise ValueError("Generated scene failed structural audit")

    world_outputs = generate_world()
    raw_outputs.extend((item.raw_path, item.archive_path) for item in world_outputs)

    quest_outputs = compile_quest()
    raw_outputs.extend(quest_outputs)
    quest_spec, _ = quest_compiler.load_spec(MANIFEST)
    if quest_spec is None:
        raise ValueError("GQT005 manifest became invalid after generation")
    if args.deserialize:
        if args.serializer == "wolvenkit":
            wolvenkit = find_wolvenkit(args.wolvenkit)
            for raw, archive in raw_outputs:
                deserialize_cr2w_json(
                    raw,
                    archive,
                    wolvenkit=wolvenkit,
                )
        else:
            for raw, archive in raw_outputs:
                if raw == ONSCREEN_RAW:
                    ghostline_red.deserialize_localization(raw, archive)
                else:
                    ghostline_red.deserialize(raw, archive)
        mappings = [
            (args.rid_binary, RID_DEPOT),
            (LAUNCH_SCENE_ARCHIVE, LAUNCH_SCENE_DEPOT),
            (SCENE_ARCHIVE, SCENE_DEPOT),
            (
                ROOT_PHASE_ARCHIVE,
                rf"mod\gqt005\phases\{NAME}.questphase",
            ),
            *[
                (
                    quest_compiler.resource_paths(stage.phase_resource)[1],
                    stage.phase_resource,
                )
                for stage in quest_spec.stages
            ],
            (JOURNAL_ARCHIVE, r"mod\gqt005\journal\gqt005.journal"),
            (
                ONSCREEN_ARCHIVE,
                r"mod\gqt005\localization\en-us\onscreens\gqt005.json",
            ),
            *[(archive, depot_path) for _, archive, depot_path in BD_HELPER_RESOURCES],
            *[(item.archive_path, item.depot_path) for item in world_outputs],
        ]
        package = package_assets(
            mappings,
            depot_root=ROOT / "source/archive",
        )
        write(
            ROOT / ".tmp/braindance/gqt005/package.json",
            package,
        )

    scene_audit = audit_scene_document(
        load(SCENE_RAW),
        handoff=load(args.handoff),
    )
    print(
        json.dumps(
            {
                "ok": scene_audit["ok"],
                "scene": str(SCENE_RAW),
                "launch_scene": str(LAUNCH_SCENE_RAW),
                "quest": str(ROOT_PHASE_RAW),
                "children": [
                    str(quest_compiler.resource_paths(stage.phase_resource)[0])
                    for stage in quest_spec.stages
                ],
                "journal": str(JOURNAL_RAW),
                "world": [str(item.raw_path) for item in world_outputs],
                "packed": bool(args.deserialize),
                "clue_layers": scene_audit["clue_layers"],
            },
            indent=2,
        )
    )
    return 0 if scene_audit["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
