#!/usr/bin/env python3
"""Generate subtitle, subtitle-map, and VO-map CR2W-JSON from a dialogue manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from ghostline_red import deserialize as deserialize_cr2w

ROOT = Path(__file__).resolve().parents[1]


def header(archive_path: Path) -> dict[str, Any]:
    return {
        "WolvenKitVersion": "8.17.4",
        "WKitJsonVersion": "0.0.9",
        "GameVersion": 2310,
        "ExportedDateTime": "1970-01-01T00:00:00Z",
        "DataType": "CR2W",
        "ArchiveFileName": str(archive_path.resolve()),
    }


def json_resource(archive_path: Path, root_type: str, entries: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "Header": header(archive_path),
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {
                "$type": "JsonResource",
                "cookingPlatform": "PLATFORM_PC",
                "root": {
                    "HandleId": "0",
                    "Data": {"$type": root_type, "entries": entries},
                },
            },
            "EmbeddedFiles": [],
        },
    }


def resource_ref(path: str) -> dict[str, Any]:
    return {
        "DepotPath": {
            "$type": "ResourcePath",
            "$storage": "string",
            "$value": path,
        },
        "Flags": "Soft",
    }


def write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def deserialize(raw_path: Path, archive_dir: Path) -> None:
    deserialize_cr2w(raw_path, archive_dir / raw_path.name.removesuffix(".json"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--quest", required=True)
    parser.add_argument("--dialogue", required=True)
    parser.add_argument("--deserialize", action="store_true")
    args = parser.parse_args()

    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    lines = manifest.get("spoken_lines", [])
    if not lines:
        parser.error("manifest has no spoken_lines")

    depot_root = f"mod\\{args.quest}\\localization\\en-us"
    raw_root = ROOT / "source" / "raw" / "mod" / args.quest / "localization" / "en-us"
    archive_root = ROOT / "source" / "archive" / "mod" / args.quest / "localization" / "en-us"
    subtitle_name = f"{args.dialogue}.json"
    subtitle_map_name = f"{args.dialogue}_subtitles_map.json"

    subtitle_raw = raw_root / "subtitles" / f"{subtitle_name}.json"
    subtitle_archive = archive_root / "subtitles" / subtitle_name
    subtitle_entries = [
        {
            "$type": "localizationPersistenceSubtitleEntry",
            "femaleVariant": str(line["text"]),
            "maleVariant": str(line["text"]),
            "stringId": str(line["string_id"]),
        }
        for line in lines
    ]
    write(
        subtitle_raw,
        json_resource(
            subtitle_archive,
            "localizationPersistenceSubtitleEntries",
            subtitle_entries,
        ),
    )

    vo_raw = raw_root / "vo" / f"{subtitle_name}.json"
    vo_archive = archive_root / "vo" / subtitle_name
    vo_entries = [
        {
            "$type": "locVoLineEntry",
            "femaleResPath": resource_ref(str(line["audio_path"])),
            "maleResPath": resource_ref(str(line["audio_path"])),
            "stringId": str(line["string_id"]),
        }
        for line in lines
    ]
    write(vo_raw, json_resource(vo_archive, "locVoiceoverMap", vo_entries))

    map_raw = raw_root / "subtitles" / f"{subtitle_map_name}.json"
    map_archive = archive_root / "subtitles" / subtitle_map_name
    map_entry = {
        "$type": "localizationPersistenceSubtitleMapEntry",
        "subtitleFile": resource_ref(
            f"{depot_root}\\subtitles\\{subtitle_name}"
        ),
        "subtitleGroup": {
            "$type": "CName",
            "$storage": "string",
            "$value": "quest",
        },
    }
    write(
        map_raw,
        json_resource(
            map_archive,
            "localizationPersistenceSubtitleMap",
            [map_entry],
        ),
    )

    if args.deserialize:
        for raw_path, archive_path in (
            (subtitle_raw, subtitle_archive),
            (vo_raw, vo_archive),
            (map_raw, map_archive),
        ):
            deserialize(raw_path, archive_path.parent)

    print(
        json.dumps(
            {
                "subtitles": str(subtitle_raw),
                "voiceover_map": str(vo_raw),
                "subtitle_map": str(map_raw),
                "lines": len(lines),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
