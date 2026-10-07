"""Shared helpers for quest-owned journal and localization build scripts."""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any, Iterator


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def wrappers(value: Any) -> Iterator[dict[str, Any]]:
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


class Handles:
    """Allocate an isolated handle namespace while cloning RedPackage chunks."""

    def __init__(self, document: dict[str, Any], *, minimum_next: int = 0):
        self.next = max(minimum_next, max(int(item["HandleId"]) for item in wrappers(document)) + 1)

    def clone(self, value: dict[str, Any]) -> dict[str, Any]:
        result = copy.deepcopy(value)
        mapping: dict[str, str] = {}
        for wrapper in wrappers(result):
            old = str(wrapper["HandleId"])
            mapping[old] = str(self.next)
            wrapper["HandleId"] = str(self.next)
            self.next += 1

        def remap(child: Any) -> None:
            if isinstance(child, dict):
                ref = child.get("HandleRefId")
                if ref is not None and str(ref) in mapping:
                    child["HandleRefId"] = mapping[str(ref)]
                for nested in child.values():
                    remap(nested)
            elif isinstance(child, list):
                for nested in child:
                    remap(nested)

        remap(result)
        return result


def loc(value: str) -> dict[str, str]:
    return {"unk1": "0", "value": value}


def set_loc(data: dict[str, Any], field: str, value: str) -> None:
    data[field] = loc(value)


def make_phase(
    handles: Handles,
    phase_template: dict[str, Any],
    objective_template: dict[str, Any],
    *,
    phase_id: str,
    objective_id: str,
    objective_loc: str,
    description_id: str,
    description_loc: str,
    mappins: list[tuple[str, str, str]],
    gps_disabled_mappins: frozenset[str] = frozenset(),
    mappin_captions: dict[str, str] | None = None,
) -> dict[str, Any]:
    phase = handles.clone(phase_template)
    phase["Data"]["id"] = phase_id
    phase["Data"]["entries"] = []

    objective = handles.clone(objective_template)
    objective_data = objective["Data"]
    objective_data["id"] = objective_id
    set_loc(objective_data, "description", objective_loc)
    objective_data["entries"] = []

    map_template = next(
        child
        for child in objective_template["Data"]["entries"]
        if child["Data"]["$type"] == "gameJournalQuestMapPin"
    )
    description_template = next(
        child
        for child in objective_template["Data"]["entries"]
        if child["Data"]["$type"] == "gameJournalQuestDescription"
    )
    for mappin_id, mappin_loc, node_ref in mappins:
        pin = handles.clone(map_template)
        pin_data = pin["Data"]
        pin_data["id"] = mappin_id
        pin_data["mappinData"]["debugCaption"] = (mappin_captions or {}).get(mappin_id, mappin_loc)
        set_loc(pin_data["mappinData"], "localizedCaption", mappin_loc)
        pin_data["reference"]["reference"]["$storage"] = "string"
        pin_data["reference"]["reference"]["$value"] = node_ref
        if mappin_id in gps_disabled_mappins:
            pin_data["enableGPS"] = 0
        objective_data["entries"].append(pin)

    description = handles.clone(description_template)
    description["Data"]["id"] = description_id
    set_loc(description["Data"], "description", description_loc)
    objective_data["entries"].append(description)
    phase["Data"]["entries"].append(objective)
    return phase


def make_message(
    handles: Handles,
    template: dict[str, Any],
    entry_id: str,
    text_key: str,
) -> dict[str, Any]:
    result = handles.clone(template)
    result["Data"]["id"] = entry_id
    set_loc(result["Data"], "text", text_key)
    return result


def make_choice(
    handles: Handles,
    template: dict[str, Any],
    entry_id: str,
    text_key: str,
) -> dict[str, Any]:
    result = handles.clone(template)
    result["Data"]["id"] = entry_id
    set_loc(result["Data"], "text", text_key)
    return result


def make_choice_group(
    handles: Handles,
    template: dict[str, Any],
    entry_id: str,
    choices: list[dict[str, Any]],
) -> dict[str, Any]:
    result = handles.clone(template)
    result["Data"]["id"] = entry_id
    result["Data"]["entries"] = choices
    return result


def make_conversation(
    handles: Handles,
    template: dict[str, Any],
    conversation_id: str,
    title_key: str,
    entries: list[dict[str, Any]],
) -> dict[str, Any]:
    result = handles.clone(template)
    result["Data"]["id"] = conversation_id
    set_loc(result["Data"], "title", title_key)
    result["Data"]["entries"] = entries
    return result


_TEMPLATE_ROOT = Path(__file__).resolve().parents[1]
_TEMPLATE_CATALOG = load(_TEMPLATE_ROOT / "quests/templates/journal/catalog.json")["templates"]


def journal_template_path(name: str) -> Path:
    """Resolve a reviewed donor shape independently of generated quest resources."""
    return _TEMPLATE_ROOT / _TEMPLATE_CATALOG[name]["path"]


def journal_handles(document: dict[str, Any], template: Path) -> Handles:
    """Keep allocation stable when unused donor branches have been removed."""
    relative = template.resolve().relative_to(_TEMPLATE_ROOT).as_posix()
    entry = next(value for value in _TEMPLATE_CATALOG.values() if value["path"] == relative)
    return Handles(document, minimum_next=entry.get("minimum_next_handle", 0))


def make_onscreens(template: Path, text: dict[str, str], archive: Path) -> dict[str, Any]:
    result = load(template)
    result["Data"]["RootChunk"]["root"]["Data"]["entries"] = [
        {
            "$type": "localizationPersistenceOnScreenEntry",
            "femaleVariant": value,
            "maleVariant": "",
            "primaryKey": "0",
            "secondaryKey": key,
        }
        for key, value in text.items()
    ]
    result["Header"]["ArchiveFileName"] = str(archive.resolve())
    result["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return result
