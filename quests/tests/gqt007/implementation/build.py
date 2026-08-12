#!/usr/bin/env python3
"""Generate the GQT007 Barry lipsync A/B runtime fixture."""

from __future__ import annotations

import argparse
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

import generate_scene as scene_builder  # noqa: E402
import generate_world as world_builder  # noqa: E402
import quest_compiler  # noqa: E402
from braindance_pipeline import deserialize_cr2w_json, find_wolvenkit  # noqa: E402
from quest_content import Handles, find_entry, load, loc  # noqa: E402

NAME = "gqt007_barry_lipsync"
MANIFEST = ROOT / "quests/tests/gqt007_barry_lipsync.quest.json"
SCENE_SPEC = (
    ROOT
    / "quests/tests/gqt007/implementation/scenes/barry-lipsync.scene-spec.json"
)
WORLD_SPEC = (
    ROOT / "quests/tests/gqt007/implementation/world/barry-lipsync.world.json"
)

JOURNAL_TEMPLATE = ROOT / "source/raw/mod/gqt001/journal/gqt001.journal.json"
ONSCREEN_TEMPLATE = (
    ROOT / "source/raw/mod/gqt001/localization/en-us/onscreens/gqt001.json.json"
)
JOURNAL_RAW = ROOT / "source/raw/mod/gqt007/journal/gqt007.journal.json"
JOURNAL_ARCHIVE = ROOT / "source/archive/mod/gqt007/journal/gqt007.journal"
ONSCREEN_RAW = (
    ROOT / "source/raw/mod/gqt007/localization/en-us/onscreens/gqt007.json.json"
)
ONSCREEN_ARCHIVE = (
    ROOT / "source/archive/mod/gqt007/localization/en-us/onscreens/gqt007.json"
)
LIPMAP_RAW = (
    ROOT / "source/raw/mod/gqt007/localization/en-us/gqt007.lipmap.json"
)
LIPMAP_ARCHIVE = (
    ROOT / "source/archive/mod/gqt007/localization/en-us/gqt007.lipmap"
)
SUBTITLES_RAW = (
    ROOT / "source/raw/mod/gqt007/localization/en-us/subtitles/gqt007.json.json"
)
SUBTITLES_ARCHIVE = (
    ROOT / "source/archive/mod/gqt007/localization/en-us/subtitles/gqt007.json"
)
SUBTITLE_MAP_RAW = (
    ROOT
    / "source/raw/mod/gqt007/localization/en-us/subtitles/"
    "gqt007_subtitles_map.json.json"
)
SUBTITLE_MAP_ARCHIVE = (
    ROOT
    / "source/archive/mod/gqt007/localization/en-us/subtitles/"
    "gqt007_subtitles_map.json"
)
VO_MAP_RAW = (
    ROOT / "source/raw/mod/gqt007/localization/en-us/vo/gqt007.json.json"
)
VO_MAP_ARCHIVE = (
    ROOT / "source/archive/mod/gqt007/localization/en-us/vo/gqt007.json"
)
ROOT_PHASE_RAW = (
    ROOT / "source/raw/mod/gqt007/phases/gqt007_barry_lipsync.questphase.json"
)
ROOT_PHASE_ARCHIVE = (
    ROOT / "source/archive/mod/gqt007/phases/gqt007_barry_lipsync.questphase"
)
CUSTOM_ANIMSET = (
    ROOT
    / "source/archive/base/localization/en-us/lipsync/mod/gqt007/scenes/"
    "gqt007_barry_lipsync/civ_low_m_11_enus_40_fat.anims"
)
SCENE_DEPOT_PATH = "mod\\gqt007\\scenes\\gqt007_barry_lipsync.scene"
BARRY_VOICE_TAG_ID = "1624173162010260376"
CUSTOM_ANIMSET_DEPOT_PATH = (
    "base\\localization\\en-us\\lipsync\\mod\\gqt007\\scenes\\"
    "gqt007_barry_lipsync\\civ_low_m_11_enus_40_fat.anims"
)
LINE_IDS = ("9041139144898214479", "14094805234786396679")
WEM_DEPOT_PATHS = (
    "mod\\gqt007\\localization\\en-us\\vo\\barry_who_is_it.wem",
    "mod\\gqt007\\localization\\en-us\\vo\\barry_who_is_it.wem",
)
WEM_ARCHIVE_PATHS = tuple({
    ROOT / "source/archive" / Path(path.replace("\\", "/"))
    for path in WEM_DEPOT_PATHS
})

OBJECTIVE = (
    "quests/minor_quest/gqt007/gqt007_01/"
    "gqt007_01_obj_compare_lipsync"
)
DESCRIPTION = f"{OBJECTIVE}/gqt007_01_desc_compare_lipsync"
MAPPIN = f"{OBJECTIVE}/gqt007_01_qmp_barry"

TEXT = {
    "gl_gqt007_title": "Barry Lipsync A/B",
    "gl_gqt007_objective": "Compare Barry's vanilla and modified lipsync.",
    "gl_gqt007_description": (
        "Choose either playback repeatedly while watching Barry's mouth."
    ),
    "gl_gqt007_mappin": "Barry lipsync test",
}


def write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def generate_journal() -> dict[str, Any]:
    journal = load(JOURNAL_TEMPLATE)
    handles = Handles(journal)
    quest = find_entry(journal, "gameJournalQuest", "gqt001")
    quest["Data"]["id"] = "gqt007"
    quest["Data"]["title"] = loc("gl_gqt007_title")

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
    phase["Data"]["id"] = "gqt007_01"
    objective = handles.clone(objective_template)
    objective["Data"]["id"] = "gqt007_01_obj_compare_lipsync"
    objective["Data"]["counter"] = 0
    objective["Data"]["description"] = loc("gl_gqt007_objective")
    pin = handles.clone(map_template)
    pin["Data"]["id"] = "gqt007_01_qmp_barry"
    pin["Data"]["reference"]["reference"]["$storage"] = "string"
    pin["Data"]["reference"]["reference"]["$value"] = "#gqt007_sm_barry"
    pin["Data"]["mappinData"]["debugCaption"] = "gl_gqt007_mappin"
    pin["Data"]["mappinData"]["localizedCaption"] = loc("gl_gqt007_mappin")
    description = handles.clone(description_template)
    description["Data"]["id"] = "gqt007_01_desc_compare_lipsync"
    description["Data"]["description"] = loc("gl_gqt007_description")
    objective["Data"]["entries"] = [pin, description]
    phase["Data"]["entries"] = [objective]
    quest["Data"]["entries"] = [phase]

    find_entry(journal, "gameJournalPrimaryFolderEntry", "contacts")["Data"][
        "entries"
    ] = []
    onscreens = find_entry(journal, "gameJournalFolderEntry", "gqt001")
    onscreens["Data"]["id"] = "gqt007"
    onscreens["Data"]["entries"] = []
    poi = find_entry(
        journal,
        "gameJournalPointOfInterestMappin",
        "gqt001_01_poi_terminal",
    )
    poi["Data"]["id"] = "gqt007_01_poi_barry"
    poi["Data"]["staticNodeRef"]["$storage"] = "string"
    poi["Data"]["staticNodeRef"]["$value"] = "#gqt007_sm_barry"
    poi["Data"]["questPath"]["Data"]["realPath"] = "quests/minor_quest/gqt007"

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


def generate_lipmap() -> dict[str, Any]:
    """Map the mod scene and Barry voice tag to the localized animset."""
    return {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": "1970-01-01T00:00:00Z",
            "DataType": "CR2W",
            "ArchiveFileName": str(LIPMAP_ARCHIVE.resolve()),
        },
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {
                "$type": "animLipsyncMapping",
                "cookingPlatform": "PLATFORM_PC",
                "languageCodeName": {
                    "$type": "CName",
                    "$storage": "string",
                    "$value": "en-us",
                },
                "sceneEntries": [
                    {
                        "$type": "animLipsyncMappingSceneEntry",
                        "actorVoiceTags": [BARRY_VOICE_TAG_ID],
                        "animSets": [
                            {
                                "DepotPath": {
                                    "$type": "ResourcePath",
                                    "$storage": "string",
                                    "$value": CUSTOM_ANIMSET_DEPOT_PATH,
                                },
                                "Flags": "Soft",
                            }
                        ],
                    }
                ],
                "scenePaths": [str(scene_builder.fnv1a64(SCENE_DEPOT_PATH))],
            },
            "EmbeddedFiles": [],
        },
    }


def json_resource(archive_path: Path, root_type: str, data: dict[str, Any]) -> dict[str, Any]:
    return {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": "1970-01-01T00:00:00Z",
            "DataType": "CR2W",
            "ArchiveFileName": str(archive_path.resolve()),
        },
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {
                "$type": "JsonResource",
                "cookingPlatform": "PLATFORM_PC",
                "root": {
                    "HandleId": "0",
                    "Data": {"$type": root_type, **data},
                },
            },
            "EmbeddedFiles": [],
        },
    }


def generate_subtitles() -> dict[str, Any]:
    return json_resource(
        SUBTITLES_ARCHIVE,
        "localizationPersistenceSubtitleEntries",
        {
            "entries": [
                {
                    "$type": "localizationPersistenceSubtitleEntry",
                    "femaleVariant": "Who is it?",
                    "maleVariant": "Who is it?",
                    "stringId": string_id,
                }
                for string_id in LINE_IDS
            ]
        },
    )


def generate_subtitle_map() -> dict[str, Any]:
    return json_resource(
        SUBTITLE_MAP_ARCHIVE,
        "localizationPersistenceSubtitleMap",
        {
            "entries": [
                {
                    "$type": "localizationPersistenceSubtitleMapEntry",
                    "subtitleFile": {
                        "DepotPath": {
                            "$type": "ResourcePath",
                            "$storage": "string",
                            "$value": (
                                "mod\\gqt007\\localization\\en-us\\subtitles\\"
                                "gqt007.json"
                            ),
                        },
                        "Flags": "Soft",
                    },
                    "subtitleGroup": {
                        "$type": "CName",
                        "$storage": "string",
                        "$value": "quest",
                    },
                }
            ]
        },
    )


def generate_vomap() -> dict[str, Any]:
    return json_resource(
        VO_MAP_ARCHIVE,
        "locVoiceoverMap",
        {
            "entries": [
                {
                    "$type": "locVoLineEntry",
                    "femaleResPath": {
                        "DepotPath": {
                            "$type": "ResourcePath",
                            "$storage": "string",
                            "$value": wem_path,
                        },
                        "Flags": "Soft",
                    },
                    "maleResPath": {
                        "DepotPath": {
                            "$type": "ResourcePath",
                            "$storage": "string",
                            "$value": wem_path,
                        },
                        "Flags": "Soft",
                    },
                    "stringId": string_id,
                }
                for string_id, wem_path in zip(LINE_IDS, WEM_DEPOT_PATHS, strict=True)
            ]
        },
    )


def generate_scene() -> tuple[dict[str, Any], Path, Path]:
    spec = load(SCENE_SPEC)
    scene = scene_builder.build_scene(spec)
    errors = scene_builder.validate_scene(scene, spec)
    if errors:
        raise ValueError("Generated GQT007 scene failed validation: " + "; ".join(errors))
    raw = ROOT / spec["raw_path"]
    archive = ROOT / spec["archive_path"]
    write(raw, scene)
    return scene, raw, archive


def generate_world() -> list[world_builder.GeneratedFile]:
    return world_builder.build_world(
        load(WORLD_SPEC),
        ROOT / "source/raw",
        ROOT / "source/archive",
    )


def compile_quest() -> list[tuple[Path, Path]]:
    spec, diagnostics = quest_compiler.load_spec(MANIFEST)
    if spec is None:
        raise ValueError(
            "Invalid GQT007 manifest: "
            + "; ".join(item.message for item in diagnostics)
        )
    diagnostics.extend(quest_compiler.audit_resources(spec))
    errors = [item for item in diagnostics if item.level == "error"]
    if errors:
        raise ValueError(
            "GQT007 resource audit failed: "
            + "; ".join(item.message for item in errors)
        )

    write(
        ROOT_PHASE_RAW,
        quest_compiler.build_orchestration_phase(spec, ROOT_PHASE_ARCHIVE),
    )
    outputs = [(ROOT_PHASE_RAW, ROOT_PHASE_ARCHIVE)]
    for stage in spec.stages:
        raw, archive = quest_compiler.resource_paths(stage.phase_resource)
        write(
            raw,
            quest_compiler.build_stage_phase(
                stage,
                archive,
                spec.phase_prefabs,
            ),
        )
        outputs.append((raw, archive))
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--deserialize", action="store_true")
    parser.add_argument("--wolvenkit", type=Path)
    args = parser.parse_args()

    write(JOURNAL_RAW, generate_journal())
    write(ONSCREEN_RAW, generate_onscreens())
    write(LIPMAP_RAW, generate_lipmap())
    write(SUBTITLES_RAW, generate_subtitles())
    write(SUBTITLE_MAP_RAW, generate_subtitle_map())
    write(VO_MAP_RAW, generate_vomap())
    _, scene_raw, scene_archive = generate_scene()
    world_outputs = generate_world()
    quest_outputs = compile_quest()

    raw_outputs = [
        (JOURNAL_RAW, JOURNAL_ARCHIVE),
        (ONSCREEN_RAW, ONSCREEN_ARCHIVE),
        (LIPMAP_RAW, LIPMAP_ARCHIVE),
        (SUBTITLES_RAW, SUBTITLES_ARCHIVE),
        (SUBTITLE_MAP_RAW, SUBTITLE_MAP_ARCHIVE),
        (VO_MAP_RAW, VO_MAP_ARCHIVE),
        (scene_raw, scene_archive),
        *((item.raw_path, item.archive_path) for item in world_outputs),
        *quest_outputs,
    ]
    if args.deserialize:
        wolvenkit = find_wolvenkit(args.wolvenkit)
        for raw, archive in raw_outputs:
            deserialize_cr2w_json(raw, archive, wolvenkit=wolvenkit)

    print(
        json.dumps(
            {
                "ok": True,
                "scene": str(scene_raw),
                "quest": str(ROOT_PHASE_RAW),
                "journal": str(JOURNAL_RAW),
                "world": [str(item.raw_path) for item in world_outputs],
                "custom_animset": str(CUSTOM_ANIMSET),
                "custom_animset_exists": CUSTOM_ANIMSET.is_file(),
                "wem_files_exist": all(path.is_file() for path in WEM_ARCHIVE_PATHS),
                "deserialized": args.deserialize,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
