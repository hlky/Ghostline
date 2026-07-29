#!/usr/bin/env python3
"""Generate GQ002 journal and onscreen localization authoring resources.

The generator deliberately clones the already game-tested GQ001 journal entry
shapes.  That keeps the CR2W object layout conservative while allowing GQ002
to own a substantially different phase tree, two Cinder phone threads, and a
quest shard.
"""

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

from ghostline_red import deserialize as deserialize_cr2w

JOURNAL_TEMPLATE = ROOT / "source/raw/mod/gq001/journal/gq001.journal.json"
ONSCREEN_TEMPLATE = (
    ROOT / "source/raw/mod/gq001/localization/en-us/onscreens/gq001.json.json"
)
JOURNAL_RAW = ROOT / "source/raw/mod/gq002/journal/gq002.journal.json"
JOURNAL_ARCHIVE = ROOT / "source/archive/mod/gq002/journal/gq002.journal"
ONSCREEN_RAW = (
    ROOT / "source/raw/mod/gq002/localization/en-us/onscreens/gq002.json.json"
)
ONSCREEN_ARCHIVE = (
    ROOT / "source/archive/mod/gq002/localization/en-us/onscreens/gq002.json"
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


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


class Handles:
    def __init__(self, document: dict[str, Any]):
        self.next = max(int(item["HandleId"]) for item in wrappers(document)) + 1

    def clone(self, value: dict[str, Any]) -> dict[str, Any]:
        clone = copy.deepcopy(value)
        mapping: dict[str, str] = {}
        for wrapper in wrappers(clone):
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

        remap(clone)
        return clone


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
        pin_data["mappinData"]["debugCaption"] = mappin_loc
        set_loc(pin_data["mappinData"], "localizedCaption", mappin_loc)
        pin_data["reference"]["reference"]["$storage"] = "string"
        pin_data["reference"]["reference"]["$value"] = node_ref
        if mappin_id == "gq002_03_qmp_medical":
            # This native device projects GPS to a remote gameplay proxy.
            # Preserve its world/map icon without drawing a misleading route.
            pin_data["enableGPS"] = 0
        objective_data["entries"].append(pin)

    description = handles.clone(description_template)
    description["Data"]["id"] = description_id
    set_loc(description["Data"], "description", description_loc)
    objective_data["entries"].append(description)
    phase["Data"]["entries"].append(objective)
    return phase


def make_message(
    handles: Handles, template: dict[str, Any], entry_id: str, text_key: str
) -> dict[str, Any]:
    result = handles.clone(template)
    result["Data"]["id"] = entry_id
    set_loc(result["Data"], "text", text_key)
    return result


def make_choice(
    handles: Handles, template: dict[str, Any], entry_id: str, text_key: str
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


def generate_journal() -> dict[str, Any]:
    journal = load(JOURNAL_TEMPLATE)
    handles = Handles(journal)
    quest = find_entry(journal, "gameJournalQuest", "gq001")
    phase_template = find_entry(journal, "gameJournalQuestPhase", "gq001_01")
    objective_template = find_entry(
        journal, "gameJournalQuestObjective", "gq001_01_obj_meet_patch"
    )

    quest["Data"]["id"] = "gq002"
    set_loc(quest["Data"], "title", "gl_gq002_title")
    phase_specs = [
        (
            "gq002_01",
            "gq002_01_obj_meet_cinder",
            "meet_cinder",
            [("gq002_01_qmp_cinder", "cinder", "#gq002_01_mp_cinder")],
        ),
        (
            "gq002_02",
            "gq002_02_obj_reach_relay",
            "reach_relay",
            [("gq002_02_qmp_relay", "relay", "#gq002_02_mp_relay")],
        ),
        (
            "gq002_03",
            "gq002_03_obj_investigate",
            "investigate",
            [
                ("gq002_03_qmp_tenant", "tenant", "#gq002_03_mp_tenant"),
                (
                    "gq002_03_qmp_medical",
                    "medical",
                    "$/03_night_city/c_watson/kabuki/loc_ma_wat_kab_15_prefab7XOZ7NY/loc_ma_wat_kab_15_gameplay_prefabLA72KZQ/loc_ma_wat_kab_15_devices_prefabLCOBNEQ/ma_wat_kab_15_access_point_001",
                ),
                ("gq002_03_qmp_invoice", "invoice", "#gq002_03_mp_invoice"),
            ],
        ),
        ("gq002_04", "gq002_04_obj_read_shard", "read_shard", []),
        (
            "gq002_04b",
            "gq002_04b_obj_return_relay",
            "return_relay",
            [("gq002_04b_qmp_relay", "return_relay", "#gq002_02_mp_relay")],
        ),
        (
            "gq002_05",
            "gq002_05_obj_clear_security",
            "clear_security",
            [("gq002_05_qmp_security", "security", "#gq002_02_mp_relay")],
        ),
        (
            "gq002_06",
            "gq002_06_obj_operate_relay",
            "operate_relay",
            [("gq002_06_qmp_relay", "operate", "#gq002_02_mp_relay")],
        ),
        ("gq002_07", "gq002_07_obj_leave_relay", "leave_relay", []),
        ("gq002_08", "gq002_08_obj_respond_cinder", "respond_cinder", []),
    ]
    quest["Data"]["entries"] = [
        make_phase(
            handles,
            phase_template,
            objective_template,
            phase_id=phase_id,
            objective_id=objective_id,
            objective_loc=f"gl_gq002_{phase_id[-2:]}_objective_{suffix}",
            description_id=f"{objective_id.replace('_obj_', '_desc_')}",
            description_loc=f"gl_gq002_{phase_id[-2:]}_description_{suffix}",
            mappins=[
                (pin_id, f"gl_gq002_{phase_id[-2:]}_mappin_{pin_suffix}", node_ref)
                for pin_id, pin_suffix, node_ref in pins
            ],
        )
        for phase_id, objective_id, suffix, pins in phase_specs
    ]

    contacts_folder = find_entry(journal, "gameJournalPrimaryFolderEntry", "contacts")
    patch_template = find_entry(journal, "gameJournalContact", "patch")
    morrow_template = find_entry(journal, "gameJournalContact", "morrow")
    conversation_template = find_entry(
        journal, "gameJournalPhoneConversation", "gq001_05_delivery"
    )
    message_template = find_entry(
        journal, "gameJournalPhoneMessage", "01_msg_cache_authenticated"
    )
    choice_group_template = find_entry(
        journal, "gameJournalPhoneChoiceGroup", "03_ch_delivery_response"
    )
    choice_template = find_entry(
        journal, "gameJournalPhoneChoiceEntry", "03a_ch_pay_me"
    )

    patch = handles.clone(patch_template)
    patch["Data"]["entries"] = [
        make_conversation(
            handles,
            conversation_template,
            "gq002_01_start",
            "gl_gq002_phone_start_title",
            [
                make_message(
                    handles,
                    message_template,
                    "01_msg_cinder",
                    "gl_gq002_phone_msg_cinder",
                ),
                make_choice_group(
                    handles,
                    choice_group_template,
                    "02_ch_meet_cinder",
                    [
                        make_choice(
                            handles,
                            choice_template,
                            "02a_ch_on_my_way",
                            "gl_gq002_phone_choice_on_my_way",
                        )
                    ],
                ),
            ],
        )
    ]

    cinder = handles.clone(morrow_template)
    cinder["Data"]["id"] = "cinder"
    set_loc(cinder["Data"], "name", "gq_npc_cinder")
    relay_entries = [
        make_message(
            handles,
            message_template,
            "01_msg_hostage_circuit",
            "gl_gq002_phone_relay_hostage",
        ),
        make_message(
            handles, message_template, "02_msg_choose", "gl_gq002_phone_relay_choose"
        ),
        make_choice_group(
            handles,
            choice_group_template,
            "03_ch_response",
            [
                make_choice(
                    handles,
                    choice_template,
                    "03a_ch_destroy",
                    "gl_gq002_phone_choice_destroy",
                ),
                make_choice(
                    handles,
                    choice_template,
                    "03b_ch_spoof",
                    "gl_gq002_phone_choice_spoof",
                ),
            ],
        ),
        make_message(
            handles,
            message_template,
            "04a_msg_destroy",
            "gl_gq002_phone_relay_destroy_reply",
        ),
        make_message(
            handles,
            message_template,
            "04b_msg_spoof",
            "gl_gq002_phone_relay_spoof_reply",
        ),
        make_message(
            handles, message_template, "05_msg_proceed", "gl_gq002_phone_relay_proceed"
        ),
    ]
    debrief_entries = [
        make_message(
            handles,
            message_template,
            "01_msg_outcome",
            "gl_gq002_phone_debrief_outcome",
        ),
        make_message(
            handles,
            message_template,
            "02_msg_context",
            "gl_gq002_phone_debrief_context",
        ),
        make_message(
            handles,
            message_template,
            "02a_msg_destroy_confirm",
            "gl_gq002_phone_debrief_destroy_confirm",
        ),
        make_message(
            handles,
            message_template,
            "02b_msg_spoof_confirm",
            "gl_gq002_phone_debrief_spoof_confirm",
        ),
        make_choice_group(
            handles,
            choice_group_template,
            "03_ch_response",
            [
                make_choice(
                    handles,
                    choice_template,
                    "03a_ch_hard",
                    "gl_gq002_phone_choice_hard",
                ),
                make_choice(
                    handles,
                    choice_template,
                    "03b_ch_careful",
                    "gl_gq002_phone_choice_careful",
                ),
            ],
        ),
        make_message(
            handles,
            message_template,
            "04a_msg_hard",
            "gl_gq002_phone_debrief_hard_reply",
        ),
        make_message(
            handles,
            message_template,
            "04b_msg_careful",
            "gl_gq002_phone_debrief_careful_reply",
        ),
        make_message(
            handles,
            message_template,
            "05_msg_more_work",
            "gl_gq002_phone_debrief_more_work",
        ),
    ]
    cinder["Data"]["entries"] = [
        make_conversation(
            handles,
            conversation_template,
            "gq002_06_relay_decision",
            "gl_gq002_phone_relay_title",
            relay_entries,
        ),
        make_conversation(
            handles,
            conversation_template,
            "gq002_08_debrief",
            "gl_gq002_phone_debrief_title",
            debrief_entries,
        ),
    ]
    contacts_folder["Data"]["entries"] = [patch, cinder]

    onscreen_group = find_entry(journal, "gameJournalOnscreenGroup", "shards")
    shard_template = find_entry(journal, "gameJournalOnscreen", "quiet_spine_01")
    shard = handles.clone(shard_template)
    shard["Data"]["id"] = "hostage_circuit"
    set_loc(shard["Data"], "title", "gl_gq002_shard_hostage_circuit_title")
    set_loc(shard["Data"], "description", "gl_gq002_shard_hostage_circuit_body")
    onscreen_group["Data"]["entries"] = [shard]

    gq_folder = find_entry(journal, "gameJournalFolderEntry", "gq001")
    gq_folder["Data"]["id"] = "gq002"

    poi = find_entry(
        journal, "gameJournalPointOfInterestMappin", "gq001_01_poi_patch_bridge"
    )
    poi["Data"]["id"] = "gq002_01_poi_cinder"
    poi["Data"]["staticNodeRef"]["$storage"] = "string"
    poi["Data"]["staticNodeRef"]["$value"] = "#gq002_01_mp_cinder"
    poi["Data"]["questPath"]["Data"]["realPath"] = "quests/minor_quest/gq002"

    journal["Header"]["ArchiveFileName"] = str(JOURNAL_ARCHIVE.resolve())
    journal["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return journal


ONSCREEN_TEXT = {
    "gl_gq002_title": "The Machine Stops",
    "gl_gq002_01_objective_meet_cinder": "Meet Cinder.",
    "gl_gq002_01_description_meet_cinder": "Patch's client is waiting in Kabuki. Find out what Common Ground wants.",
    "gl_gq002_01_mappin_cinder": "Cinder",
    "gl_gq002_02_objective_reach_relay": "Go to the Kabuki relay.",
    "gl_gq002_02_description_reach_relay": "Common Ground traced the tenant-surveillance network to an old neighborhood relay.",
    "gl_gq002_02_mappin_relay": "Surveillance relay",
    "gl_gq002_03_objective_investigate": "Inspect the relay network.",
    "gl_gq002_03_description_investigate": "Scan the linked antenna access points and determine what the relay controls.",
    "gl_gq002_03_mappin_tenant": "Tenant classifier",
    "gl_gq002_03_mappin_medical": "Clinic telemetry bridge",
    "gl_gq002_03_mappin_invoice": "Failover invoice",
    "gl_gq002_04_objective_read_shard": "Read the archived conversation.",
    "gl_gq002_04_description_read_shard": "The recovered messages explain why the relay was designed to be difficult to remove.",
    "gl_gq002_4b_objective_return_relay": "Return to the target relay.",
    "gl_gq002_4b_description_return_relay": "Go back to the relay and deal with its security.",
    "gl_gq002_4b_mappin_return_relay": "Target relay",
    "gl_gq002_05_objective_clear_security": "Neutralize the relay security.",
    "gl_gq002_05_description_clear_security": "The relay's owners sent Tyger Claw muscle to protect their investment.",
    "gl_gq002_05_mappin_security": "Relay security",
    "gl_gq002_06_objective_operate_relay": "Jack in to the relay.",
    "gl_gq002_06_description_operate_relay": "Carry out the shutdown plan you chose with Cinder.",
    "gl_gq002_06_mappin_operate": "Relay access point",
    "gl_gq002_07_objective_leave_relay": "Leave the relay area.",
    "gl_gq002_07_description_leave_relay": "Put some distance between yourself and the relay while Cinder verifies the result.",
    "gl_gq002_08_objective_respond_cinder": "Respond to Cinder.",
    "gl_gq002_08_description_respond_cinder": "Read Cinder's message and let her know where you stand.",
    "gl_gq002_phone_start_title": "The Machine Stops",
    "gl_gq002_phone_msg_cinder": "Got a client with a machine problem. Common Ground. Meet Cinder in Kabuki and hear her out.",
    "gl_gq002_phone_choice_on_my_way": "On my way.",
    "gl_gq002_phone_relay_title": "Hostage Circuit",
    "gl_gq002_phone_relay_hostage": "Saw the scan. Tenant classifier and clinic telemetry share one relay. Deliberate hostage circuit.",
    "gl_gq002_phone_relay_choose": "Two options: destroy it after I warn the clinic, or blind the classifier and spoof a failure.",
    "gl_gq002_phone_choice_destroy": "Destroy the relay.",
    "gl_gq002_phone_choice_spoof": "Spoof the shutdown.",
    "gl_gq002_phone_relay_destroy_reply": "Hard stop. I'll warn the clinic and reroute what I can before you pull it.",
    "gl_gq002_phone_relay_spoof_reply": "Quiet cut. I'll feed the owners a clean failure report while you blind the classifier.",
    "gl_gq002_phone_relay_proceed": "Make the call real. Jack in.",
    "gl_gq002_phone_debrief_title": "Common Ground",
    "gl_gq002_phone_debrief_outcome": "The relay is off their board. Clinic traffic is stable and the tenant feed is dead.",
    "gl_gq002_phone_debrief_context": "Common Ground owes you. The owners will call it vandalism. The tenants get to call it privacy.",
    "gl_gq002_phone_debrief_destroy_confirm": "Hard shutdown confirmed. The clinic made the reroute; the surveillance relay stayed dead.",
    "gl_gq002_phone_debrief_spoof_confirm": "Spoof held. Their dashboard sees a dead relay while the clinic traffic keeps moving.",
    "gl_gq002_phone_choice_hard": "Machines don't get a vote.",
    "gl_gq002_phone_choice_careful": "Keep the clinic safe.",
    "gl_gq002_phone_debrief_hard_reply": "Neither do landlords who wire medicine to surveillance.",
    "gl_gq002_phone_debrief_careful_reply": "Already watching the reroute. I don't spend lives to make a point.",
    "gl_gq002_phone_debrief_more_work": "There are more hostage circuits in this city. I'll call when we find the next one.",
    "gl_gq002_shard_hostage_circuit_title": "Archived conversation: Sato and Keene",
    "gl_gq002_shard_hostage_circuit_body": (
        "[SATO] Tenant classifier is live. Missed payments, unauthorized occupants, behavioral flags. "
        "All routed through the Kabuki relay.\n\n"
        "[KEENE] And the clinic telemetry?\n\n"
        "[SATO] Same failover bus. If anyone cuts surveillance, the clinic loses remote diagnostics.\n\n"
        "[KEENE] Good. Make removal expensive enough that activists have to choose who gets hurt.\n\n"
        "[SATO] Tyger Claws are billing for on-site security.\n\n"
        "[KEENE] Approve it. Fear is cheaper than rebuilding."
    ),
}


def generate_onscreens() -> dict[str, Any]:
    onscreens = load(ONSCREEN_TEMPLATE)
    entries = onscreens["Data"]["RootChunk"]["root"]["Data"]["entries"]
    entries[:] = [
        {
            "$type": "localizationPersistenceOnScreenEntry",
            "femaleVariant": text,
            "maleVariant": "",
            "primaryKey": "0",
            "secondaryKey": key,
        }
        for key, text in ONSCREEN_TEXT.items()
    ]
    onscreens["Header"]["ArchiveFileName"] = str(ONSCREEN_ARCHIVE.resolve())
    onscreens["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return onscreens


def deserialize(raw_path: Path, archive_path: Path) -> None:
    deserialize_cr2w(raw_path, archive_path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--deserialize", action="store_true", help="Also create packed CR2W resources."
    )
    args = parser.parse_args()
    write(JOURNAL_RAW, generate_journal())
    write(ONSCREEN_RAW, generate_onscreens())
    if args.deserialize:
        deserialize(JOURNAL_RAW, JOURNAL_ARCHIVE)
        deserialize(ONSCREEN_RAW, ONSCREEN_ARCHIVE)
    print(JOURNAL_RAW)
    print(ONSCREEN_RAW)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
