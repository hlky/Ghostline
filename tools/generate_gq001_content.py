#!/usr/bin/env python3
"""Generate the gq001 journal and onscreen localization from the proven gq000 tree."""

from __future__ import annotations

import copy
import json
import subprocess
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
WOLVENKIT = Path(r"H:\WolvenKit.Console-8.17.4\WolvenKit.CLI.exe")
JOURNAL_TEMPLATE = ROOT / "source/raw/mod/gq000/journal/gq000.journal.json"
ONSCREEN_TEMPLATE = ROOT / "source/raw/mod/gq000/localization/en-us/onscreens/gq000.json.json"
JOURNAL_RAW = ROOT / "source/raw/mod/gq001/journal/gq001.journal.json"
JOURNAL_ARCHIVE = ROOT / "source/archive/mod/gq001/journal/gq001.journal"
ONSCREEN_RAW = ROOT / "source/raw/mod/gq001/localization/en-us/onscreens/gq001.json.json"
ONSCREEN_ARCHIVE = ROOT / "source/archive/mod/gq001/localization/en-us/onscreens/gq001.json"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def rewrite(value: Any, transform: Callable[[str], str]) -> Any:
    if isinstance(value, dict):
        return {key: rewrite(child, transform) for key, child in value.items()}
    if isinstance(value, list):
        return [rewrite(child, transform) for child in value]
    if isinstance(value, str):
        return transform(value)
    return value


def wrappers(value: Any):
    if isinstance(value, dict):
        if "HandleId" in value and isinstance(value.get("Data"), dict):
            yield value
        for child in value.values():
            yield from wrappers(child)
    elif isinstance(value, list):
        for child in value:
            yield from wrappers(child)


def find_entry(value: Any, type_name: str, entry_id: str) -> dict[str, Any]:
    for wrapper in wrappers(value):
        data = wrapper["Data"]
        if data.get("$type") == type_name and data.get("id") == entry_id:
            return wrapper
    raise RuntimeError(f"Missing {type_name} id={entry_id}")


def remap_clone_handles(value: Any, next_handle: int) -> tuple[Any, int]:
    clone = copy.deepcopy(value)
    mapping: dict[str, str] = {}
    for wrapper in wrappers(clone):
        old = str(wrapper["HandleId"])
        mapping[old] = str(next_handle)
        wrapper["HandleId"] = str(next_handle)
        next_handle += 1

    def remap(child: Any) -> None:
        if isinstance(child, dict):
            if "HandleRefId" in child and str(child["HandleRefId"]) in mapping:
                child["HandleRefId"] = mapping[str(child["HandleRefId"])]
            for nested in child.values():
                remap(nested)
        elif isinstance(child, list):
            for nested in child:
                remap(nested)

    remap(clone)
    return clone, next_handle


def generate_journal() -> dict[str, Any]:
    journal = rewrite(load(JOURNAL_TEMPLATE), lambda text: text.replace("gq000", "gq001"))
    quest = find_entry(journal, "gameJournalQuest", "gq001")
    phases = quest["Data"]["entries"]
    patch_phase = find_entry(journal, "gameJournalQuestPhase", "gq001_01")
    delivery_phase = find_entry(journal, "gameJournalQuestPhase", "gq001_03")

    existing_handles = [int(wrapper["HandleId"]) for wrapper in wrappers(journal)]
    iris_phase, _ = remap_clone_handles(patch_phase, max(existing_handles) + 1)
    iris_phase = rewrite(
        iris_phase,
        lambda text: (
            text.replace("gq001_01", "gq001_03")
            .replace("meet_patch", "meet_iris")
            .replace("patch_bridge", "iris")
            .replace("Patch", "Iris")
        ),
    )
    iris_phase["Data"]["id"] = "gq001_03"

    delivery_phase = rewrite(
        delivery_phase,
        lambda text: text.replace("gq001_03", "gq001_04"),
    )
    delivery_index = next(
        index for index, phase in enumerate(phases) if phase["Data"]["id"] == "gq001_03"
    )
    phases[delivery_index] = iris_phase
    phases.insert(delivery_index + 1, delivery_phase)

    journal = rewrite(
        journal,
        lambda text: (
            text.replace("gq001_04_delivery", "gq001_05_delivery")
            .replace("#gq001_01_mp_patch_bridge", "#gq000_01_mp_patch_bridge")
            .replace("#gq001_02_mp_cache", "#gq000_02_mp_cache")
            .replace("#gq001_02_ap_cache", "#gq000_02_ap_cache")
            .replace("#gq001_04_mp_drop_point", "#gq000_03_mp_drop_point")
        ),
    )
    journal["Header"]["ArchiveFileName"] = str(JOURNAL_ARCHIVE.resolve())
    journal["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return journal


IRIS_ONSCREENS = [
    {
        "$type": "localizationPersistenceOnScreenEntry",
        "femaleVariant": "Meet Iris.",
        "maleVariant": "",
        "primaryKey": "0",
        "secondaryKey": "gl_gq001_03_objective_meet_iris",
    },
    {
        "$type": "localizationPersistenceOnScreenEntry",
        "femaleVariant": "Iris can make sense of the recovered cache. Bring it to her.",
        "maleVariant": "",
        "primaryKey": "0",
        "secondaryKey": "gl_gq001_03_description_meet_iris",
    },
    {
        "$type": "localizationPersistenceOnScreenEntry",
        "femaleVariant": "Iris",
        "maleVariant": "",
        "primaryKey": "0",
        "secondaryKey": "gl_gq001_03_mappin_iris",
    },
]


def generate_onscreens() -> dict[str, Any]:
    def transform(text: str) -> str:
        result = text.replace("gq000", "gq001")
        result = result.replace("gq001_03_", "gq001_04_")
        result = result.replace("gq001_04_delivery", "gq001_05_delivery")
        return result

    onscreens = rewrite(load(ONSCREEN_TEMPLATE), transform)
    entries = onscreens["Data"]["RootChunk"]["root"]["Data"]["entries"]
    entries.extend(IRIS_ONSCREENS)
    for entry in entries:
        if entry.get("secondaryKey") == "gl_gq001_title":
            entry["femaleVariant"] = "Ghostline"
    onscreens["Header"]["ArchiveFileName"] = str(ONSCREEN_ARCHIVE.resolve())
    onscreens["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return onscreens


def deserialize(raw_path: Path, archive_path: Path) -> None:
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            str(WOLVENKIT),
            "convert",
            "deserialize",
            str(raw_path),
            "-o",
            str(archive_path.parent),
            "-v",
            "Minimal",
        ],
        check=True,
    )


def main() -> int:
    journal = generate_journal()
    onscreens = generate_onscreens()
    write(JOURNAL_RAW, journal)
    write(ONSCREEN_RAW, onscreens)
    deserialize(JOURNAL_RAW, JOURNAL_ARCHIVE)
    deserialize(ONSCREEN_RAW, ONSCREEN_ARCHIVE)
    print(JOURNAL_RAW)
    print(ONSCREEN_RAW)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
