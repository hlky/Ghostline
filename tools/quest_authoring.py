#!/usr/bin/env python3
"""Expand quest aliases and small stage recipes into the existing compiler format."""

from __future__ import annotations

import argparse
import copy
from dataclasses import dataclass
import json
import math
from pathlib import Path
import re
from typing import Any, Mapping

from artifact_io import publish_json_artifacts
from quest_content import journal_template_path, load, make_onscreens

ROOT = Path(__file__).resolve().parents[1]
IDENTIFIER = re.compile(r"^[a-z][a-z0-9_]*$")
JOURNAL_ID = re.compile(r"^[A-Za-z0-9_]+$")
RECIPES = {
    "offer_meeting_investigation_decision_debrief": (
        ("offer", "phone_job_offer"),
        ("meeting", "meet_contact"),
        ("investigation", "investigate_clues"),
        ("decision", "choice_gate"),
        ("debrief", "phone_conversation"),
    ),
    "rescue_escort_defense_extraction": (
        ("rescue", "release_or_rescue_npc"),
        ("escort", "escort_npc"),
        ("defense", "defend_target"),
        ("extraction", "leave_area"),
    ),
    # The existing phone block grants its reward after the final report message.
    "encounter_evidence_report_reward": (
        ("encounter", "combat_encounter"),
        ("evidence", "investigate_clues"),
        ("report", "phone_conversation"),
    ),
}


class AuthoringError(ValueError):
    pass


@dataclass(frozen=True)
class AuthoringResult:
    manifest: dict[str, Any]
    bindings: dict[str, Any]
    documents: dict[str, dict[str, Any]]  # archive depot path -> editable CR2W-JSON


def _object(value: Any, context: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise AuthoringError(f"{context} must be an object")
    return value


def _identifier(value: Any, context: str) -> str:
    if not isinstance(value, str) or not IDENTIFIER.fullmatch(value):
        raise AuthoringError(f"{context} must be a lowercase identifier")
    return value


def _journal_id(value: Any, context: str) -> str:
    if not isinstance(value, str) or not JOURNAL_ID.fullmatch(value):
        raise AuthoringError(f"Invalid {context}: {value!r}")
    return value


def _phone_entries(raw: Any, path: str, key: str, add_text: Any) -> dict:
    """Resolve explicitly ordered legacy phone entries without changing IDs."""
    entries = {}
    ids = set()
    for alias, value in _object(raw, "phone entries").items():
        _identifier(alias, "phone entry alias")
        entry = dict(_object(value, "phone entry"))
        _fields(
            entry,
            {
                "type",
                "id",
                "text",
                "localization_key",
                "delay",
                "template",
                "entries",
                "sender",
                "important",
                "attachment",
            },
            "phone entry",
        )
        kind = entry.get("type")
        if kind not in {"message", "choice_group"}:
            raise AuthoringError(f"Unsupported phone entry type: {kind}")
        entry_id = _journal_id(entry.get("id", alias), "phone entry id")
        if entry_id in ids:
            raise AuthoringError(f"Duplicate conversation entry: {entry_id}")
        ids.add(entry_id)
        entry.update(id=entry_id, path=f"{path}/{entry_id}")
        if kind == "message":
            if "entries" in entry:
                raise AuthoringError("Phone messages cannot contain entries")
            entry.setdefault("localization_key", f"{key}_{alias}")
            add_text(entry["localization_key"], entry.get("text"))
            if "delay" in entry:
                delay = entry["delay"]
                if (
                    isinstance(delay, bool)
                    or not isinstance(delay, (int, float))
                    or not math.isfinite(delay)
                    or delay < 0
                ):
                    raise AuthoringError(
                        "Phone message delay must be finite and nonnegative"
                    )
            if "sender" in entry and entry["sender"] not in {"NPC", "Player"}:
                raise AuthoringError("Phone sender must be NPC or Player")
            if "important" in entry and not isinstance(entry["important"], bool):
                raise AuthoringError("Phone important must be a Boolean")
            if "attachment" in entry and not isinstance(entry["attachment"], str):
                raise AuthoringError("Phone attachment must be a journal path")
        else:
            if set(entry) & {
                "text",
                "localization_key",
                "delay",
                "sender",
                "important",
                "attachment",
            }:
                raise AuthoringError(
                    "Phone choice groups contain choices, not message fields"
                )
            choices = {}
            choice_ids = set()
            for choice_alias, choice_value in _object(
                entry.get("entries"), "phone choices"
            ).items():
                _identifier(choice_alias, "phone choice alias")
                choice = dict(_object(choice_value, "phone choice"))
                _fields(
                    choice,
                    {"id", "text", "localization_key", "template"},
                    "phone choice",
                )
                choice_id = _journal_id(
                    choice.get("id", choice_alias), "phone choice id"
                )
                if choice_id in choice_ids:
                    raise AuthoringError(f"Duplicate phone choice: {choice_id}")
                choice_ids.add(choice_id)
                choice.update(id=choice_id, path=f"{entry['path']}/{choice_id}")
                choice.setdefault("localization_key", f"{key}_choice_{choice_alias}")
                add_text(choice["localization_key"], choice.get("text"))
                choices[choice_alias] = choice
            if not choices:
                raise AuthoringError("Phone choice groups must contain choices")
            entry["entries"] = choices
        entries[alias] = entry
    return entries


def _fields(value: dict, allowed: set[str], context: str) -> None:
    unknown = set(value) - allowed
    if unknown:
        raise AuthoringError(f"Unknown {context} fields: {', '.join(sorted(unknown))}")


def _resolve(value: Any, bindings: dict, trail: tuple[str, ...] = ()) -> Any:
    """Resolve whole-value references only; detect missing names and cycles."""
    if isinstance(value, str) and value.startswith("@@"):
        return value[1:]
    if isinstance(value, str) and value.startswith("@"):
        reference = value[1:]
        if reference in trail:
            raise AuthoringError("Alias cycle: " + " -> ".join((*trail, reference)))
        target: Any = bindings
        for name in reference.split("."):
            if not isinstance(target, dict) or name not in target:
                raise AuthoringError(f"Unknown alias: {value}")
            target = target[name]
        return _resolve(copy.deepcopy(target), bindings, (*trail, reference))
    if isinstance(value, dict):
        return {key: _resolve(child, bindings, trail) for key, child in value.items()}
    if isinstance(value, list):
        return [_resolve(child, bindings, trail) for child in value]
    return value


def expand_recipe(
    name: str, steps: Mapping[str, Any], *, prefix: str = "", reward: str | None = None
) -> list[dict]:
    """Parameterize a reviewed ordering with ordinary stage fields and overrides."""
    if not isinstance(name, str) or name not in RECIPES:
        raise AuthoringError(f"Unknown quest recipe: {name}")
    steps = _object(steps, f"{name}.steps")
    expected = {slot for slot, _ in RECIPES[name]}
    if set(steps) != expected:
        raise AuthoringError(
            f"{name}.steps must contain exactly {', '.join(sorted(expected))}"
        )
    if prefix:
        _identifier(prefix, "recipe prefix")
    if name == "encounter_evidence_report_reward" and not reward:
        raise AuthoringError(f"{name} requires an explicit reward record")
    if name != "encounter_evidence_report_reward" and reward is not None:
        raise AuthoringError(f"{name} does not accept reward")
    result = []
    for slot, stage_type in RECIPES[name]:
        stage = {"id": f"{prefix}_{slot}" if prefix else slot, "type": stage_type}
        stage.update(copy.deepcopy(_object(steps[slot], f"{name}.{slot}")))
        if slot == "report" and reward:
            stage.setdefault("reward", reward)
        result.append(stage)
    return result


def _prepare(raw: Mapping[str, Any]) -> tuple[dict, dict, dict | None]:
    manifest = copy.deepcopy(_object(raw, "quest"))
    composition = manifest.pop("composition", None)
    if composition is None:
        return manifest, {}, None
    composition = _object(composition, "composition")
    _fields(
        composition,
        {
            "namespace",
            "quest",
            "journal_template",
            "objectives",
            "contacts",
            "locations",
            "clues",
            "facts",
            "text",
            "recipes",
            "points_of_interest",
            "readables",
        },
        "composition",
    )
    namespace = _identifier(
        composition.get("namespace", manifest.get("id")), "composition.namespace"
    )
    bindings: dict[str, Any] = {
        "quest": {
            "id": namespace,
            "path": f"quests/minor_quest/{namespace}",
            "title_key": f"gl_{namespace}_title",
        },
        "resources": {
            "journal": f"mod\\{namespace}\\journal\\{namespace}.journal",
            "onscreens": f"mod\\{namespace}\\localization\\en-us\\onscreens\\{namespace}.json",
        },
        "objectives": {},
        "contacts": {},
        "locations": {},
        "clues": {},
        "facts": {},
        "points_of_interest": {},
        "readables": {},
    }
    text_entries: list[tuple[str, str]] = []

    def add_text(key: str, value: Any) -> None:
        if not isinstance(key, str) or not key or not isinstance(value, str):
            raise AuthoringError("Localization keys and text must be strings")
        text_entries.append((key, value))

    quest = _object(composition.get("quest", {}), "composition.quest")
    _fields(quest, {"title", "localization_key", "type"}, "composition.quest")
    bindings["quest"]["title_key"] = quest.get(
        "localization_key", bindings["quest"]["title_key"]
    )
    add_text(bindings["quest"]["title_key"], quest.get("title", manifest.get("title")))
    if "type" in quest:
        bindings["quest"]["type"] = quest["type"]
    for category in ("locations", "facts", "clues", "objectives", "contacts"):
        definitions = _object(composition.get(category, {}), f"composition.{category}")
        for alias, value in definitions.items():
            _identifier(alias, f"{category} alias")
            if category == "facts":
                bindings[category][alias] = (
                    value if value is not None else f"{namespace}_{alias}"
                )
            elif category == "locations":
                record = (
                    {"ref": value}
                    if isinstance(value, str)
                    else dict(_object(value, f"locations.{alias}"))
                )
                record.setdefault("ref", f"#{namespace}_{alias}")
                bindings[category][alias] = record
            elif category == "clues":
                record = (
                    {"object_ref": value}
                    if isinstance(value, str)
                    else dict(_object(value, f"clues.{alias}"))
                )
                _fields(
                    record,
                    {
                        "id",
                        "object_ref",
                        "completion_fact",
                        "grant_item",
                        "grant_items",
                        "journal_entry",
                        "mappin",
                    },
                    f"clues.{alias}",
                )
                record.setdefault("id", alias)
                record.setdefault("object_ref", f"#{namespace}_clue_{alias}")
                record.setdefault(
                    "completion_fact", f"{namespace}_clue_{alias}_scanned"
                )
                bindings[category][alias] = record
            elif category == "objectives":
                record = (
                    {"text": value}
                    if isinstance(value, str)
                    else dict(_object(value, f"objectives.{alias}"))
                )
                _fields(
                    record,
                    {
                        "text",
                        "description",
                        "phase_id",
                        "id",
                        "localization_key",
                        "description_id",
                        "description_key",
                        "mappins",
                        "completion_fact",
                        "optional",
                        "template",
                        "counter",
                    },
                    f"objectives.{alias}",
                )
                phase_id = _journal_id(
                    record.get("phase_id", f"{namespace}_{alias}"), "objective phase_id"
                )
                objective_id = _journal_id(
                    record.get("id", f"{phase_id}_obj_{alias}"), "objective id"
                )
                description_id = _journal_id(
                    record.get("description_id", f"{phase_id}_desc_{alias}"),
                    "description id",
                )
                path = f"{bindings['quest']['path']}/{phase_id}/{objective_id}"
                record.update(
                    phase_id=phase_id,
                    id=objective_id,
                    description_id=description_id,
                    path=path,
                    description_entry=f"{path}/{description_id}",
                )
                record.setdefault(
                    "localization_key", f"gl_{namespace}_objective_{alias}"
                )
                record.setdefault(
                    "description_key", f"gl_{namespace}_description_{alias}"
                )
                record.setdefault("description", manifest.get("description", ""))
                record.setdefault("completion_fact", f"{namespace}_{alias}_complete")
                if "optional" in record and not isinstance(record["optional"], bool):
                    raise AuthoringError("Objective optional must be a Boolean")
                if "counter" in record and (
                    isinstance(record["counter"], bool)
                    or not isinstance(record["counter"], int)
                    or record["counter"] < 0
                ):
                    raise AuthoringError(
                        "Objective counter must be a nonnegative integer"
                    )
                add_text(record["localization_key"], record.get("text"))
                add_text(record["description_key"], record["description"])
                pins = {}
                for pin_alias, pin_value in _object(
                    record.get("mappins", {}), "objective mappins"
                ).items():
                    _identifier(pin_alias, "mappin alias")
                    pin = (
                        {"ref": pin_value}
                        if isinstance(pin_value, str)
                        else dict(_object(pin_value, "mappin"))
                    )
                    _fields(
                        pin,
                        {
                            "ref",
                            "id",
                            "text",
                            "localization_key",
                            "gps_disabled",
                            "debug_caption",
                            "template",
                            "variant",
                        },
                        "mappin",
                    )
                    pin.setdefault("id", f"{phase_id}_qmp_{pin_alias}")
                    _journal_id(pin["id"], "mappin id")
                    pin.setdefault(
                        "localization_key", f"gl_{namespace}_mappin_{alias}_{pin_alias}"
                    )
                    pin.setdefault("text", record["text"])
                    pin["path"] = f"{path}/{pin['id']}"
                    add_text(pin["localization_key"], pin["text"])
                    pins[pin_alias] = pin
                record["mappins"] = pins
                record["mappin"] = next(iter(pins.values()))["path"] if pins else ""
                record["route_mappins"] = [pin["path"] for pin in pins.values()]
                bindings[category][alias] = record
            else:
                record = dict(_object(value, f"contacts.{alias}"))
                _fields(
                    record,
                    {
                        "id",
                        "name",
                        "template",
                        "localization_key",
                        "threads",
                        "community",
                        "entry",
                        "appearance",
                        "scene",
                    },
                    f"contacts.{alias}",
                )
                record.setdefault("id", f"{namespace}_{alias}")
                record["contact"] = _identifier(record["id"], "contact id")
                record.setdefault("localization_key", f"gl_{namespace}_contact_{alias}")
                if "name" in record or "localization_key" not in value:
                    add_text(record["localization_key"], record.get("name", alias))
                threads = {}
                for thread_alias, thread_value in _object(
                    record.get("threads", {}), "contact threads"
                ).items():
                    _identifier(thread_alias, "thread alias")
                    thread = dict(_object(thread_value, "thread"))
                    _fields(
                        thread,
                        {
                            "id",
                            "title",
                            "title_key",
                            "messages",
                            "choices",
                            "final_message",
                            "entries",
                            "template",
                        },
                        "thread",
                    )
                    thread.setdefault("id", f"{namespace}_{thread_alias}")
                    _journal_id(thread["id"], "thread id")
                    path = f"contacts/{record['id']}/{thread['id']}"
                    key = f"gl_{namespace}_{alias}_{thread_alias}"
                    thread.update(
                        path=path,
                        title_key=thread.get("title_key", f"{key}_title"),
                        choice_group=f"{path}/choices",
                    )
                    add_text(
                        thread["title_key"], thread.get("title", manifest.get("title"))
                    )
                    if "entries" in thread:
                        if set(thread) & {"messages", "choices", "final_message"}:
                            raise AuthoringError(
                                "Explicit phone entries cannot be combined with shorthand messages/choices"
                            )
                        thread["entries"] = _phone_entries(
                            thread["entries"], path, key, add_text
                        )
                        thread["messages"] = [
                            entry["path"]
                            for entry in thread["entries"].values()
                            if entry["type"] == "message"
                        ]
                        thread["message"] = next(iter(thread["messages"]), "")
                        groups = [
                            entry
                            for entry in thread["entries"].values()
                            if entry["type"] == "choice_group"
                        ]
                        thread["choice_group"] = groups[0]["path"] if groups else ""
                        thread["accept_choice"] = (
                            next(iter(groups[0]["entries"].values()))["path"]
                            if groups
                            else ""
                        )
                        threads[thread_alias] = thread
                        continue
                    messages = _object(thread.get("messages", {}), "thread messages")
                    choices = _object(thread.get("choices", {}), "thread choices")
                    for message_id, message in messages.items():
                        _identifier(message_id, "message id")
                        add_text(f"{key}_{message_id}", message)
                    thread["message_text"] = messages
                    thread["messages"] = [f"{path}/{name}" for name in messages]
                    thread["message"] = next(iter(thread["messages"]), "")
                    thread["choice_text"] = choices
                    thread["choices"] = []
                    entry_ids = set(messages) | {"choices", "final"}
                    if set(messages) & {"choices", "final"}:
                        raise AuthoringError(
                            "Message IDs choices and final are reserved"
                        )
                    for choice_id, choice_value in choices.items():
                        _identifier(choice_id, "choice id")
                        choice = (
                            {"text": choice_value}
                            if isinstance(choice_value, str)
                            else _object(choice_value, "phone choice")
                        )
                        _fields(choice, {"text", "reply"}, "phone choice")
                        add_text(f"{key}_choice_{choice_id}", choice.get("text"))
                        paths = {"choice": f"{path}/choices/{choice_id}"}
                        if "reply" in choice:
                            reply_id = f"{choice_id}_reply"
                            if reply_id in entry_ids:
                                raise AuthoringError(
                                    f"Duplicate conversation entry: {reply_id}"
                                )
                            entry_ids.add(reply_id)
                            add_text(f"{key}_{reply_id}", choice["reply"])
                            paths["reply"] = f"{path}/{reply_id}"
                        thread["choices"].append(paths)
                    thread["accept_choice"] = (
                        thread["choices"][0]["choice"] if thread["choices"] else ""
                    )
                    if "final_message" in thread:
                        add_text(f"{key}_final", thread["final_message"])
                        thread["final_message"] = f"{path}/final"
                    thread["text_prefix"] = key
                    threads[thread_alias] = thread
                record["threads"] = threads
                bindings[category][alias] = record
    for alias, value in _object(
        composition.get("readables", {}), "composition.readables"
    ).items():
        _identifier(alias, "readable alias")
        readable = dict(_object(value, "readable"))
        _fields(
            readable,
            {"kind", "group", "id", "title", "text", "title_key", "text_key", "tag"},
            "readable",
        )
        if readable.get("kind") not in {"file", "onscreen"}:
            raise AuthoringError("Readable kind must be file or onscreen")
        readable.setdefault(
            "group", "files" if readable["kind"] == "file" else "shards"
        )
        readable.setdefault("id", alias)
        _journal_id(readable["group"], "readable group")
        _journal_id(readable["id"], "readable id")
        readable.setdefault("title_key", f"gl_{namespace}_{alias}_title")
        readable.setdefault("text_key", f"gl_{namespace}_{alias}_body")
        readable["path"] = (
            f"onscreens/emails/quests/minor_quest/{namespace}/{readable['group']}/{readable['id']}"
        )
        add_text(readable["title_key"], readable.get("title"))
        add_text(readable["text_key"], readable.get("text"))
        bindings["readables"][alias] = readable
    for key, value in _object(composition.get("text", {}), "composition.text").items():
        add_text(key, value)
    for alias, value in _object(
        composition.get("points_of_interest", {}), "composition.points_of_interest"
    ).items():
        _identifier(alias, "point-of-interest alias")
        point = dict(_object(value, "point of interest"))
        _fields(point, {"id", "ref", "variant"}, "point of interest")
        point.setdefault("id", f"{namespace}_poi_{alias}")
        _identifier(point["id"], "point-of-interest id")
        bindings["points_of_interest"][alias] = point
    stages = manifest.get("stages", [])
    if not isinstance(stages, list):
        raise AuthoringError("stages must be an array")
    recipes = composition.get("recipes", [])
    if not isinstance(recipes, list):
        raise AuthoringError("composition.recipes must be an array")
    for recipe in recipes:
        recipe = _object(recipe, "recipe")
        _fields(recipe, {"name", "steps", "prefix", "reward"}, "recipe")
        stages.extend(
            expand_recipe(
                recipe.get("name"),
                recipe.get("steps"),
                prefix=recipe.get("prefix", ""),
                reward=recipe.get("reward"),
            )
        )
    seen = set()
    for stage in stages:
        stage = _object(stage, "stage")
        stage_id = _identifier(stage.get("id"), "stage id")
        if stage_id in seen:
            raise AuthoringError(f"Duplicate expanded stage id: {stage_id}")
        seen.add(stage_id)
        stage.setdefault(
            "phase_resource",
            f"mod\\{namespace}\\phases\\{namespace}_{stage_id}.questphase",
        )
    manifest["stages"] = stages
    resolved = _resolve(bindings, bindings)
    for name, fact in resolved["facts"].items():
        _identifier(fact, f"facts.{name}")
    objective_paths = [value["path"] for value in resolved["objectives"].values()]
    if len(set(objective_paths)) != len(objective_paths):
        raise AuthoringError("Duplicate objective path")
    readable_paths = [value["path"] for value in resolved["readables"].values()]
    if len(set(readable_paths)) != len(readable_paths):
        raise AuthoringError("Duplicate readable path")
    readable_groups: dict[str, str] = {}
    for readable in resolved["readables"].values():
        previous = readable_groups.setdefault(readable["group"], readable["kind"])
        if previous != readable["kind"]:
            raise AuthoringError("Readable groups cannot mix file and onscreen entries")
    contact_ids = [value["id"] for value in resolved["contacts"].values()]
    if len(set(contact_ids)) != len(contact_ids):
        raise AuthoringError("Duplicate contact id")
    for contact in resolved["contacts"].values():
        thread_ids = [thread["id"] for thread in contact["threads"].values()]
        if len(set(thread_ids)) != len(thread_ids):
            raise AuthoringError(f"Duplicate thread id for {contact['id']}")
    for objective in resolved["objectives"].values():
        ids = [
            objective["description_id"],
            *(pin["id"] for pin in objective["mappins"].values()),
        ]
        if len(set(ids)) != len(ids):
            raise AuthoringError(
                f"Duplicate journal child id under {objective['path']}"
            )
    points = list(resolved["points_of_interest"].values())
    point_ids = [point["id"] for point in points]
    if len(set(point_ids)) != len(point_ids):
        raise AuthoringError("Duplicate point-of-interest id")
    points += [
        pin
        for objective in resolved["objectives"].values()
        for pin in objective["mappins"].values()
    ]
    for point in points:
        ref = point.get("ref")
        if not isinstance(ref, str) or len(ref) < 2 or not ref.startswith(("#", "$")):
            raise AuthoringError(
                f"Map marker {point['id']} requires an explicit NodeRef"
            )
    text: dict[str, str] = {}
    for key, value in text_entries:
        key, value = _resolve(key, bindings), _resolve(value, bindings)
        if not isinstance(key, str) or not key or not isinstance(value, str):
            raise AuthoringError("Resolved localization keys and text must be strings")
        if key in text and text[key] != value:
            raise AuthoringError(f"Conflicting localization text for {key}")
        text[key] = value
    return (
        _resolve(manifest, bindings),
        resolved,
        {"configuration": composition, "text": text},
    )


def normalize_spec(raw: Mapping[str, Any]) -> dict[str, Any]:
    """Return ordinary compiler input without donor reads or output writes."""
    return _prepare(raw)[0]


def resolve_bindings(raw: Mapping[str, Any]) -> dict[str, Any]:
    """Resolve shared authoring declarations without loading CR2W donors."""
    return _prepare(raw)[1]


def compose(raw: Mapping[str, Any], *, root: Path = ROOT) -> AuthoringResult:
    """Build normalized stages and donor-based journal/onscreen documents in memory."""
    manifest, bindings, model = _prepare(raw)
    if model is None:
        return AuthoringResult(manifest, bindings, {})
    from quest_journal import JournalBuilder

    config = model["configuration"]
    try:
        journal = JournalBuilder(config.get("journal_template", "gq001_shapes")).build(
            bindings
        )
    except (KeyError, ValueError) as exc:
        raise AuthoringError(f"Cannot compose journal: {exc}") from exc
    journal_depot = bindings["resources"]["journal"]
    onscreen_depot = bindings["resources"]["onscreens"]
    from project_layout import source_path
    journal["Header"]["ArchiveFileName"] = str(
        source_path(journal_depot, "archive", root=root).resolve()
    )
    journal["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    onscreens = make_onscreens(
        journal_template_path("onscreen_container"),
        model["text"],
        source_path(onscreen_depot, "archive", root=root),
    )
    return AuthoringResult(
        manifest, bindings, {journal_depot: journal, onscreen_depot: onscreens}
    )


def artifact_documents(result: AuthoringResult, output_root: Path) -> dict[Path, dict]:
    """Map archive depot identities to editable artifacts under an output root."""
    return {
        output_root / "source/raw" / (depot.replace("\\", "/") + ".json"): document
        for depot, document in result.documents.items()
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument(
        "--output",
        type=Path,
        help="Publish normalized input and raw artifacts to an isolated output directory",
    )
    args = parser.parse_args(argv)
    result = compose(load(args.manifest))
    if args.output:
        documents = artifact_documents(result, args.output)
        documents[args.output / "quest.json"] = result.manifest
        documents[args.output / "bindings.json"] = result.bindings
        publish_json_artifacts(documents)
    else:
        print(json.dumps(result.manifest, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
