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
PROJECT = next(parent for parent in Path(__file__).resolve().parents if (parent / "project.json").is_file())
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))


import generate_scene as scene_builder  # noqa: E402
import generate_world as world_builder  # noqa: E402
import quest_authoring
import quest_build
from quest_content import load
import quest_compiler  # noqa: E402

NAME = "gqt007_barry_lipsync"
MANIFEST = PROJECT / "gqt007_barry_lipsync.quest.json"
SCENE_SPEC = (
    PROJECT / "implementation/scenes/barry-lipsync.scene-spec.json"
)
WORLD_SPEC = PROJECT / "implementation/world/barry-lipsync.world.json"

JOURNAL_RAW = PROJECT / "source/raw/mod/gqt007/journal/gqt007.journal.json"
JOURNAL_ARCHIVE = PROJECT / "source/archive/mod/gqt007/journal/gqt007.journal"
ONSCREEN_RAW = (
    PROJECT / "source/raw/mod/gqt007/localization/en-us/onscreens/gqt007.json.json"
)
ONSCREEN_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt007/localization/en-us/onscreens/gqt007.json"
)
LIPMAP_RAW = PROJECT / "source/raw/mod/gqt007/localization/en-us/gqt007.lipmap.json"
LIPMAP_ARCHIVE = PROJECT / "source/archive/mod/gqt007/localization/en-us/gqt007.lipmap"
SUBTITLES_RAW = (
    PROJECT / "source/raw/mod/gqt007/localization/en-us/subtitles/gqt007.json.json"
)
SUBTITLES_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt007/localization/en-us/subtitles/gqt007.json"
)
SUBTITLE_MAP_RAW = (
    PROJECT / "source/raw/mod/gqt007/localization/en-us/subtitles/"
    "gqt007_subtitles_map.json.json"
)
SUBTITLE_MAP_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt007/localization/en-us/subtitles/"
    "gqt007_subtitles_map.json"
)
VO_MAP_RAW = PROJECT / "source/raw/mod/gqt007/localization/en-us/vo/gqt007.json.json"
VO_MAP_ARCHIVE = PROJECT / "source/archive/mod/gqt007/localization/en-us/vo/gqt007.json"
ROOT_PHASE_RAW = (
    PROJECT / "source/raw/mod/gqt007/phases/gqt007_barry_lipsync.questphase.json"
)
ROOT_PHASE_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt007/phases/gqt007_barry_lipsync.questphase"
)
CUSTOM_ANIMSET = (
    ROOT / "projects/test-quests/gqt007/source/archive/base/localization/en-us/lipsync/mod/gqt007/scenes/"
    "gqt007_barry_lipsync/civ_low_m_11_enus_40_fat.anims"
)
CUSTOM_ANIMSET_DEPOT_PATH = str(
    CUSTOM_ANIMSET.relative_to(PROJECT / "source/archive")
).replace("/", "\\")


def dialogue_lines() -> list[dict[str, Any]]:
    """Use the same authored lines and ordering as the scene compiler."""
    spec = load(SCENE_SPEC)
    spoken, _ = scene_builder.load_manifest(spec)
    return [spoken[key] for key in spec["spoken_line_order"]]


def wem_archive_paths() -> set[Path]:
    return {
        PROJECT / "source/archive" / Path(path.replace("\\", "/"))
        for line in dialogue_lines()
        for path in (
            line["audio_path"],
            line.get("male_audio_path") or line["audio_path"],
        )
    }


def generate_journal() -> dict[str, Any]:
    """Compatibility accessor for the manifest-owned composition resource."""
    return quest_authoring.compose(load(MANIFEST)).documents[
        "mod\\gqt007\\journal\\gqt007.journal"
    ]


def generate_onscreens() -> dict[str, Any]:
    """Compatibility accessor for the manifest-owned composition resource."""
    return quest_authoring.compose(load(MANIFEST)).documents[
        "mod\\gqt007\\localization\\en-us\\onscreens\\gqt007.json"
    ]


def generate_lipmap() -> dict[str, Any]:
    """Map the mod scene and Barry voice tag to the localized animset."""
    spec = load(SCENE_SPEC)
    actor = next(actor for actor in spec["actors"] if actor["key"] == "barry")
    scene_depot = str(
        (ROOT / spec["archive_path"]).relative_to(PROJECT / "source/archive")
    ).replace("/", "\\")
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
                        "actorVoiceTags": [str(actor["voicetag"])],
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
                "scenePaths": [str(scene_builder.fnv1a64(scene_depot))],
            },
            "EmbeddedFiles": [],
        },
    }


def json_resource(
    archive_path: Path, root_type: str, data: dict[str, Any]
) -> dict[str, Any]:
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
                    "femaleVariant": line["text"],
                    "maleVariant": line["text"],
                    "stringId": str(line["string_id"]),
                }
                for line in dialogue_lines()
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
                            "$value": str(
                                SUBTITLES_ARCHIVE.relative_to(PROJECT / "source/archive")
                            ).replace("/", "\\"),
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
                            "$value": line["audio_path"],
                        },
                        "Flags": "Soft",
                    },
                    "maleResPath": {
                        "DepotPath": {
                            "$type": "ResourcePath",
                            "$storage": "string",
                            "$value": line.get("male_audio_path") or line["audio_path"],
                        },
                        "Flags": "Soft",
                    },
                    "stringId": str(line["string_id"]),
                }
                for line in dialogue_lines()
            ]
        },
    )


def generate_scene() -> tuple[dict[str, Any], Path, Path]:
    spec = load(SCENE_SPEC)
    scene = scene_builder.build_scene(spec)
    errors = scene_builder.validate_scene(scene, spec)
    if errors:
        raise ValueError(
            "Generated GQT007 scene failed validation: " + "; ".join(errors)
        )
    raw = ROOT / spec["raw_path"]
    archive = ROOT / spec["archive_path"]
    return scene, raw, archive


def quest_artifacts() -> list[quest_compiler.QuestArtifact]:
    return quest_compiler.compile_manifest_artifacts(
        MANIFEST,
        ROOT_PHASE_RAW,
        ROOT_PHASE_ARCHIVE,
    )


def build_artifacts(
    output_root: Path | None = None,
) -> list[quest_compiler.QuestArtifact]:
    """Build quest composition, dialogue maps, scene, and world in memory."""
    scene, scene_raw, scene_archive = generate_scene()
    world_outputs, world_documents = world_builder.build_world_documents(
        load(WORLD_SPEC),
        PROJECT / "source/raw",
        PROJECT / "source/archive",
    )
    artifacts = [
        quest_compiler.QuestArtifact(raw, archive, document)
        for raw, archive, document in (
            (LIPMAP_RAW, LIPMAP_ARCHIVE, generate_lipmap()),
            (SUBTITLES_RAW, SUBTITLES_ARCHIVE, generate_subtitles()),
            (SUBTITLE_MAP_RAW, SUBTITLE_MAP_ARCHIVE, generate_subtitle_map()),
            (VO_MAP_RAW, VO_MAP_ARCHIVE, generate_vomap()),
            (scene_raw, scene_archive, scene),
        )
    ]
    artifacts.extend(
        quest_compiler.QuestArtifact(
            item.raw_path, item.archive_path, world_documents[item.raw_path]
        )
        for item in world_outputs
    )
    artifacts.extend(quest_artifacts())
    return quest_build.relocate_artifacts(artifacts, output_root)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--deserialize", action="store_true")
    parser.add_argument("--wolvenkit", type=Path)
    parser.add_argument(
        "--out-root", type=Path, help="Build all resources in an isolated output tree"
    )
    args = parser.parse_args()
    output_root = (args.out_root or PROJECT).resolve()

    artifacts = build_artifacts(args.out_root)
    raw_outputs = quest_build.publish_build(
        artifacts,
        namespace="gqt007",
        output_root=args.out_root,
        deserialize=args.deserialize,
        wolvenkit=args.wolvenkit,
    )
    scene_raw = next(raw for raw, _ in raw_outputs if raw.name.endswith(".scene.json"))

    print(
        json.dumps(
            {
                "ok": True,
                "scene": str(scene_raw),
                "quest": str(output_root / ROOT_PHASE_RAW.relative_to(PROJECT)),
                "journal": str(output_root / JOURNAL_RAW.relative_to(PROJECT)),
                "world": [
                    str(raw)
                    for raw, _ in raw_outputs
                    if raw.name.endswith(
                        (
                            ".streamingblock.json",
                            ".streamingsector.json",
                            ".community.json",
                        )
                    )
                ],
                "custom_animset": str(CUSTOM_ANIMSET),
                "custom_animset_exists": CUSTOM_ANIMSET.is_file(),
                "wem_files_exist": all(path.is_file() for path in wem_archive_paths()),
                "deserialized": args.deserialize,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
