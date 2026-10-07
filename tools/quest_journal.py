"""Build journal entries from reviewed donors and normalized authoring bindings."""

from __future__ import annotations

import copy
from typing import Any

from quest_content import (
    journal_handles,
    journal_template_path,
    load,
    make_choice,
    make_choice_group,
    make_conversation,
    make_message,
    set_loc,
    wrappers,
)


def first(document: dict, kind: str, entry_id: str | None = None) -> dict:
    for entry in wrappers(document):
        data = entry["Data"]
        if data.get("$type") == kind and (
            entry_id is None or data.get("id") == entry_id
        ):
            return entry
    raise ValueError(f"Journal donor has no {kind} entry {entry_id!r}")


def template_names(configuration: dict) -> set[str]:
    """Donor dependencies used by composition, including explicit selections."""
    names = {
        configuration.get("journal_template", "gq001_shapes"),
        "gq001_shapes",
        "onscreen_container",
    }
    if any(
        entry.get("kind") == "file"
        for entry in configuration.get("readables", {}).values()
    ):
        names.add("file_group")

    def visit(value: Any) -> None:
        if isinstance(value, dict):
            if isinstance(value.get("template"), dict):
                names.add(value["template"]["donor"])
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    visit(configuration)
    return names


class JournalBuilder:
    """One handle allocator for every entry, including cross-donor content."""

    def __init__(self, donor: str):
        path = journal_template_path(donor)
        self.document = load(path)
        self.donors = {donor: copy.deepcopy(self.document)}
        self.default_donor = donor
        self.handles = journal_handles(self.document, path)

    def donor(self, name: str) -> dict:
        if name not in self.donors:
            self.donors[name] = load(journal_template_path(name))
        return self.donors[name]

    def template(
        self, kind: str, selection: Any = None, *, donor: str | None = None
    ) -> dict:
        name = donor or self.default_donor
        entry_id = selection
        if isinstance(selection, dict):
            if set(selection) != {"donor", "id"}:
                raise ValueError("Journal template selectors require donor and id")
            name, entry_id = selection["donor"], selection["id"]
        elif selection is not None and not isinstance(selection, str):
            raise ValueError("Journal template must be an entry ID or {donor, id}")
        return first(self.donor(name), kind, entry_id)

    def clone(
        self, kind: str, selection: Any = None, *, donor: str | None = None
    ) -> dict:
        return self.handles.clone(self.template(kind, selection, donor=donor))

    def objective(self, model: dict) -> dict:
        entry = self.clone("gameJournalQuestObjective", model.get("template"))
        data = entry["Data"]
        description = self.handles.clone(first(entry, "gameJournalQuestDescription"))
        description["Data"]["id"] = model["description_id"]
        set_loc(description["Data"], "description", model["description_key"])
        # Select pins independently: some objective donors have no pin at all.
        default_pin = next(
            (
                child
                for child in data.get("entries", [])
                if child["Data"]["$type"] == "gameJournalQuestMapPin"
            ),
            None,
        )
        data.update(id=model["id"], entries=[])
        set_loc(data, "description", model["localization_key"])
        if "optional" in model:
            data["optional"] = int(model["optional"])
        if "counter" in model:
            data["counter"] = model["counter"]
        for pin in model["mappins"].values():
            if "template" in pin or default_pin is None:
                result = self.clone("gameJournalQuestMapPin", pin.get("template"))
            else:
                result = self.handles.clone(default_pin)
            result_data = result["Data"]
            result_data["id"] = pin["id"]
            result_data["reference"]["reference"].update(
                {"$storage": "string", "$value": pin["ref"]}
            )
            result_data["mappinData"]["debugCaption"] = pin.get(
                "debug_caption", pin["localization_key"]
            )
            set_loc(
                result_data["mappinData"], "localizedCaption", pin["localization_key"]
            )
            if "gps_disabled" in pin:
                result_data["enableGPS"] = int(not pin["gps_disabled"])
            if "variant" in pin:
                result_data["mappinData"]["variant"] = pin["variant"]
            data["entries"].append(result)
        data["entries"].append(description)
        return entry

    def explicit_phone_entries(self, entries: dict) -> list[dict]:
        result = []
        for entry in entries.values():
            if entry["type"] == "message":
                node = self.clone(
                    "gameJournalPhoneMessage",
                    entry.get("template"),
                    donor="gq001_shapes",
                )
                data = node["Data"]
                data.update(
                    id=entry["id"],
                    delay=entry.get(
                        "delay", data["delay"] if "template" in entry else 1
                    ),
                )
                set_loc(data, "text", entry["localization_key"])
                if "sender" in entry:
                    data["sender"] = entry["sender"]
                if "important" in entry:
                    data["isQuestImportant"] = int(entry["important"])
                if "attachment" in entry:
                    if not isinstance(data.get("attachment"), dict):
                        raise ValueError(
                            "Phone attachment requires a donor with a journal path attachment"
                        )
                    data["attachment"]["Data"]["realPath"] = entry["attachment"]
            else:
                node = self.clone(
                    "gameJournalPhoneChoiceGroup",
                    entry.get("template"),
                    donor="gq001_shapes",
                )
                node["Data"].update(id=entry["id"], entries=[])
                for choice in entry["entries"].values():
                    child = self.clone(
                        "gameJournalPhoneChoiceEntry",
                        choice.get("template"),
                        donor="gq001_shapes",
                    )
                    child["Data"]["id"] = choice["id"]
                    set_loc(child["Data"], "text", choice["localization_key"])
                    node["Data"]["entries"].append(child)
            result.append(node)
        return result

    def shorthand_phone_entries(self, thread: dict) -> list[dict]:
        key = thread["text_prefix"]
        message = self.template("gameJournalPhoneMessage", donor="gq001_shapes")
        choice = self.template("gameJournalPhoneChoiceEntry", donor="gq001_shapes")
        entries = [
            make_message(self.handles, message, name, f"{key}_{name}")
            for name in thread["message_text"]
        ]
        choices = [
            make_choice(self.handles, choice, name, f"{key}_choice_{name}")
            for name in thread["choice_text"]
        ]
        if choices:
            entries.append(
                make_choice_group(
                    self.handles,
                    self.template("gameJournalPhoneChoiceGroup", donor="gq001_shapes"),
                    "choices",
                    choices,
                )
            )
        for name, value in thread["choice_text"].items():
            if isinstance(value, dict) and "reply" in value:
                entries.append(
                    make_message(
                        self.handles, message, f"{name}_reply", f"{key}_{name}_reply"
                    )
                )
        if "final_message" in thread:
            entries.append(make_message(self.handles, message, "final", f"{key}_final"))
        return entries

    def contacts(self, models: list[dict]) -> dict:
        contacts = self.clone(
            "gameJournalPrimaryFolderEntry", "contacts", donor="gq001_shapes"
        )
        contacts["Data"]["entries"] = []
        for contact in models:
            entry = self.clone(
                "gameJournalContact",
                contact.get("template", "morrow"),
                donor="gq001_shapes",
            )
            entry["Data"].update(id=contact["id"], entries=[])
            if entry["Data"]["name"]["value"] != contact["localization_key"]:
                set_loc(entry["Data"], "name", contact["localization_key"])
            for thread in contact["threads"].values():
                entries = (
                    self.explicit_phone_entries(thread["entries"])
                    if "entries" in thread
                    else self.shorthand_phone_entries(thread)
                )
                template = self.template(
                    "gameJournalPhoneConversation",
                    thread.get("template"),
                    donor="gq001_shapes",
                )
                entry["Data"]["entries"].append(
                    make_conversation(
                        self.handles,
                        template,
                        thread["id"],
                        thread["title_key"],
                        entries,
                    )
                )
            contacts["Data"]["entries"].append(entry)
        return contacts

    def readables(self, models: dict, namespace: str) -> dict:
        branch = self.clone(
            "gameJournalPrimaryFolderEntry", "onscreens", donor="gq001_shapes"
        )
        minor = first(branch, "gameJournalFolderEntry", "minor_quest")
        quest_folder = minor["Data"]["entries"][0]
        quest_folder["Data"].update(id=namespace, entries=[])
        minor["Data"]["entries"] = [quest_folder]
        groups = {}
        for model in models.values():
            is_file = model["kind"] == "file"
            donor = "file_group" if is_file else "gq001_shapes"
            group_kind = (
                "gameJournalFileGroup" if is_file else "gameJournalOnscreenGroup"
            )
            kind = "gameJournalFile" if is_file else "gameJournalOnscreen"
            if model["group"] not in groups:
                group = self.clone(group_kind, donor=donor)
                group["Data"].update(id=model["group"], entries=[])
                groups[model["group"]] = group
                quest_folder["Data"]["entries"].append(group)
            entry = self.clone(kind, donor=donor)
            entry["Data"]["id"] = model["id"]
            set_loc(entry["Data"], "title", model["title_key"])
            set_loc(
                entry["Data"],
                "content" if is_file else "description",
                model["text_key"],
            )
            if "tag" in model:
                if is_file:
                    raise ValueError("File entries do not support onscreen tags")
                entry["Data"]["tag"].update(
                    {"$storage": "string", "$value": model["tag"]}
                )
            groups[model["group"]]["Data"]["entries"].append(entry)
        return branch

    def build(self, bindings: dict) -> dict:
        quest = first(self.document, "gameJournalQuest")
        quest["Data"].update(id=bindings["quest"]["id"], entries=[])
        set_loc(quest["Data"], "title", bindings["quest"]["title_key"])
        if "type" in bindings["quest"]:
            quest["Data"]["type"] = bindings["quest"]["type"]
        phases = {}
        for model in bindings["objectives"].values():
            if model["phase_id"] not in phases:
                phase = self.clone("gameJournalQuestPhase")
                phase["Data"].update(id=model["phase_id"], entries=[])
                phases[model["phase_id"]] = phase
                quest["Data"]["entries"].append(phase)
            phases[model["phase_id"]]["Data"]["entries"].append(self.objective(model))
        quests = first(self.document, "gameJournalPrimaryFolderEntry", "quests")
        folder = first(quests, "gameJournalFolderEntry", "minor_quest")
        folder["Data"]["entries"] = [quest]
        quests["Data"]["entries"] = [folder]
        branches = [quests]
        if bindings["points_of_interest"]:
            points = self.clone("gameJournalPrimaryFolderEntry", "points_of_interest")
            group = first(points, "gameJournalPointOfInterestGroup")
            group["Data"]["entries"] = []
            for model in bindings["points_of_interest"].values():
                entry = self.clone("gameJournalPointOfInterestMappin")
                data = entry["Data"]
                data["id"] = model["id"]
                data["staticNodeRef"].update(
                    {"$storage": "string", "$value": model["ref"]}
                )
                data["questPath"]["Data"]["realPath"] = bindings["quest"]["path"]
                if "variant" in model:
                    data["mappinData"]["typedVariant"]["Data"]["variant"] = model[
                        "variant"
                    ]
                group["Data"]["entries"].append(entry)
            points["Data"]["entries"] = [group]
            branches.append(points)
        contacts = [
            contact for contact in bindings["contacts"].values() if contact["threads"]
        ]
        if contacts:
            branches.append(self.contacts(contacts))
        if bindings["readables"]:
            branches.append(
                self.readables(bindings["readables"], bindings["quest"]["id"])
            )
        self.document["Data"]["RootChunk"]["entry"]["Data"]["entries"] = branches
        return self.document
