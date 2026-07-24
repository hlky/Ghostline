#!/usr/bin/env python3
"""Generate the GQT001 journal, localization, and owned laptop sector.

The test laptop is a mod-owned copy placed beside a native Kabuki laptop.
Keeping its persistent-state package inside a Ghostline sector avoids mutating
or sharing ownership with a base-world device.
"""

from __future__ import annotations

import argparse
import copy
import json
import subprocess
from pathlib import Path
from typing import Any

from generate_world import DeviceRegistryEntry, Vec3, device_registry, node_ref_hash

ROOT = Path(__file__).resolve().parents[1]
WOLVENKIT = Path(r"H:\WolvenKit.Console-8.17.4\WolvenKit.CLI.exe")
SECTOR_TEMPLATE = (
    ROOT
    / "reference/world/terminal-templates"
    / "exterior_19_-8_0_0.streamingsector.json"
)
JOURNAL_TEMPLATE = ROOT / "source/raw/mod/gq001/journal/gq001.journal.json"
FILE_TEMPLATE = ROOT / "reference/journal/onscreens.emails.journal.json"
ONSCREEN_TEMPLATE = (
    ROOT / "source/raw/mod/gq001/localization/en-us/onscreens/gq001.json.json"
)
INSTANCE_PATCH_RAW = (
    ROOT
    / "source/raw/mod/gqt001/world"
    / "gqt001_laptop_instance.streamingsector.json"
)
INSTANCE_PATCH_ARCHIVE = (
    ROOT
    / "source/archive/mod/gqt001/world"
    / "gqt001_laptop_instance.streamingsector"
)
BLOCK_RAW = (
    ROOT
    / "source/raw/mod/gqt001/world"
    / "gqt001_signal_delay.streamingblock.json"
)
BLOCK_ARCHIVE = (
    ROOT
    / "source/archive/mod/gqt001/world"
    / "gqt001_signal_delay.streamingblock"
)
DEVICE_REGISTRY_RAW = (
    ROOT
    / "source/raw/mod/gqt001/world"
    / "gqt001_custom_devices.devices.json"
)
DEVICE_REGISTRY_ARCHIVE = (
    ROOT
    / "source/archive/mod/gqt001/world"
    / "gqt001_custom_devices.devices"
)
LAPTOP_NODE_REF = (
    "$/03_night_city/se1/#loc_sq021_trailer_park/"
    "loc_sq021_trailer_park_gameplay_prefabV4S2BNI/"
    "#loc_sq021_trailer_park_devices/#sq021_randy_pc"
)
OWNED_LAPTOP_NODE_REF = (
    "$/mod/gqt001/#gqt001_pr_signal_delay/#gqt001_terminal_laptop_r2"
)
OWNED_LAPTOP_POSITION = {
    "X": -1058.3098,
    "Y": 1316.143,
    "Z": 5.98333,
}
OWNED_LAPTOP_ORIENTATION = {
    "i": 0.0,
    "j": 0.0,
    "k": 0.2601109,
    "r": -0.96557885,
}
JOURNAL_RAW = ROOT / "source/raw/mod/gqt001/journal/gqt001.journal.json"
JOURNAL_ARCHIVE = ROOT / "source/archive/mod/gqt001/journal/gqt001.journal"
ONSCREEN_RAW = (
    ROOT / "source/raw/mod/gqt001/localization/en-us/onscreens/gqt001.json.json"
)
ONSCREEN_ARCHIVE = (
    ROOT / "source/archive/mod/gqt001/localization/en-us/onscreens/gqt001.json"
)
DOCUMENT_PATH = (
    "onscreens/emails/quests/minor_quest/gqt001/files/diagnostic"
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
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


def remap_handle_ids(value: Any, start: int) -> int:
    """Give a copied RedPackage chunk its own handle-id namespace."""
    mapping: dict[str, str] = {}
    next_id = start
    for wrapper in wrappers(value):
        old_id = str(wrapper["HandleId"])
        if old_id not in mapping:
            mapping[old_id] = str(next_id)
            next_id += 1
        wrapper["HandleId"] = mapping[old_id]
    return next_id


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


def loc(key: str) -> dict[str, str]:
    return {"unk1": "0", "value": key}


def generate_journal() -> dict[str, Any]:
    journal = load(JOURNAL_TEMPLATE)
    source_files = load(FILE_TEMPLATE)
    handles = Handles(journal)

    quest = find_entry(journal, "gameJournalQuest", "gq001")
    quest["Data"]["id"] = "gqt001"
    quest["Data"]["title"] = loc("gl_gqt001_title")
    phase_template = find_entry(journal, "gameJournalQuestPhase", "gq001_01")
    objective_template = find_entry(
        journal, "gameJournalQuestObjective", "gq001_01_obj_meet_patch"
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

    phases = []
    for index, suffix in ((1, "reach_terminal"), (2, "read_diagnostic")):
        phase = handles.clone(phase_template)
        phase["Data"]["id"] = f"gqt001_0{index}"
        objective = handles.clone(objective_template)
        objective["Data"]["id"] = f"gqt001_0{index}_obj_{suffix}"
        objective["Data"]["description"] = loc(
            f"gl_gqt001_0{index}_objective_{suffix}"
        )
        description = handles.clone(description_template)
        description["Data"]["id"] = f"gqt001_0{index}_desc_{suffix}"
        description["Data"]["description"] = loc(
            f"gl_gqt001_0{index}_description_{suffix}"
        )
        objective["Data"]["entries"] = [description]
        if index == 1:
            pin = handles.clone(map_template)
            pin["Data"]["id"] = "gqt001_01_qmp_terminal"
            pin["Data"]["reference"]["reference"]["$storage"] = "string"
            pin["Data"]["reference"]["reference"]["$value"] = (
                "#gqt001_01_mp_terminal"
            )
            pin["Data"]["mappinData"]["debugCaption"] = (
                "gl_gqt001_01_mappin_terminal"
            )
            pin["Data"]["mappinData"]["localizedCaption"] = loc(
                "gl_gqt001_01_mappin_terminal"
            )
            objective["Data"]["entries"].insert(0, pin)
        phase["Data"]["entries"] = [objective]
        phases.append(phase)
    quest["Data"]["entries"] = phases

    contacts = find_entry(journal, "gameJournalPrimaryFolderEntry", "contacts")
    patch = find_entry(journal, "gameJournalContact", "patch")
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
    conversation = handles.clone(conversation_template)
    conversation["Data"]["id"] = "gqt001_03_confirmation"
    conversation["Data"]["title"] = loc("gl_gqt001_phone_title")
    message = handles.clone(message_template)
    message["Data"]["id"] = "01_msg_signal_received"
    message["Data"]["text"] = loc("gl_gqt001_phone_signal_received")
    choice_group = handles.clone(choice_group_template)
    choice_group["Data"]["id"] = "02_ch_response"
    choices = []
    for entry_id, key in (
        ("02a_ch_clean", "gl_gqt001_phone_choice_clean"),
        ("02b_ch_slow", "gl_gqt001_phone_choice_slow"),
    ):
        choice = handles.clone(choice_template)
        choice["Data"]["id"] = entry_id
        choice["Data"]["text"] = loc(key)
        choices.append(choice)
    choice_group["Data"]["entries"] = choices
    replies = []
    for entry_id, key in (
        ("03a_msg_clean", "gl_gqt001_phone_reply_clean"),
        ("03b_msg_slow", "gl_gqt001_phone_reply_slow"),
        ("04_msg_complete", "gl_gqt001_phone_complete"),
    ):
        reply = handles.clone(message_template)
        reply["Data"]["id"] = entry_id
        reply["Data"]["text"] = loc(key)
        replies.append(reply)
    conversation["Data"]["entries"] = [message, choice_group, *replies]
    patch["Data"]["entries"] = [conversation]
    contacts["Data"]["entries"] = [patch]

    gq_folder = find_entry(journal, "gameJournalFolderEntry", "gq001")
    gq_folder["Data"]["id"] = "gqt001"
    file_group_template = find_entry(
        source_files, "gameJournalFileGroup", "files"
    )
    file_template = next(
        item
        for item in wrappers(file_group_template)
        if item["Data"].get("$type") == "gameJournalFile"
    )
    file_group = handles.clone(file_group_template)
    file_group["Data"]["id"] = "files"
    diagnostic = handles.clone(file_template)
    diagnostic["Data"]["id"] = "diagnostic"
    diagnostic["Data"]["title"] = loc("gl_gqt001_document_title")
    diagnostic["Data"]["content"] = loc("gl_gqt001_document_body")
    file_group["Data"]["entries"] = [diagnostic]
    gq_folder["Data"]["entries"] = [file_group]

    poi = find_entry(
        journal, "gameJournalPointOfInterestMappin", "gq001_01_poi_patch_bridge"
    )
    poi["Data"]["id"] = "gqt001_01_poi_terminal"
    poi["Data"]["staticNodeRef"]["$storage"] = "string"
    poi["Data"]["staticNodeRef"]["$value"] = "#gqt001_01_mp_terminal"
    poi["Data"]["questPath"]["Data"]["realPath"] = (
        "quests/minor_quest/gqt001"
    )
    journal["Header"]["ArchiveFileName"] = str(JOURNAL_ARCHIVE.resolve())
    journal["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return journal


TEXT = {
    "gl_gqt001_title": "Signal Delay",
    "gl_gqt001_01_objective_reach_terminal": "Go to the Kabuki terminal.",
    "gl_gqt001_01_description_reach_terminal": (
        "Patch wants a diagnostic file pulled from an unattended laptop."
    ),
    "gl_gqt001_01_mappin_terminal": "Kabuki terminal",
    "gl_gqt001_02_objective_read_diagnostic": "Read the diagnostic file.",
    "gl_gqt001_02_description_read_diagnostic": (
        "Open Files on the laptop and read SIGNAL DELAY."
    ),
    "gl_gqt001_phone_title": "Signal Delay",
    "gl_gqt001_phone_signal_received": (
        "Got the relay pulse. Ten seconds late, exactly like the diagnostic said."
    ),
    "gl_gqt001_phone_choice_clean": "Clean enough.",
    "gl_gqt001_phone_choice_slow": "Slow enough.",
    "gl_gqt001_phone_reply_clean": "Clean is what matters. Delay gives us a window.",
    "gl_gqt001_phone_reply_slow": "Slow on purpose. Makes the watchdog look away.",
    "gl_gqt001_phone_complete": "Test complete. I'll scrub the route.",
    "gl_gqt001_document_title": "SIGNAL DELAY",
    "gl_gqt001_document_body": (
        "ROUTE: KAB-09 / AUXILIARY\n\n"
        "Observed forwarding delay: 10 seconds.\n"
        "Cause: stale maintenance mirror.\n"
        "Recommendation: preserve the delay. The blind interval is useful."
    ),
}


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


def generate_instance_patch() -> dict[str, Any]:
    sector = load(SECTOR_TEMPLATE)
    root = sector["Data"]["RootChunk"]
    node_data = next(
        entry
        for entry in root["nodeData"]["Data"]
        if entry["QuestPrefabRefHash"].get("$value") == LAPTOP_NODE_REF
    )
    node = copy.deepcopy(root["nodes"][node_data["NodeIndex"]])
    instance_data = node["Data"]["instanceData"]["Data"]
    package = instance_data["buffer"]["Data"]
    # Preserve SQ021's cooked CRUID dictionary. Entries 1 and 2 are the exact
    # component IDs of laptop_1.ent's ComputerController and scanning
    # component; replacing them leaves the RedPackage present but prevents the
    # runtime entity from binding the authored persistent states.
    journal_handle = str(
        max(int(item["HandleId"]) for item in wrappers(node)) + 1
    )
    controller_chunks = [
        chunk
        for chunk in package["Chunks"]
        if chunk.get("persistentState", {}).get("Data", {}).get("$type")
        == "ComputerControllerPS"
    ]
    if len(controller_chunks) != 2:
        raise RuntimeError(
            "SQ021 terminal template must contain two ComputerControllerPS chunks"
        )
    persistent = controller_chunks[1]["persistentState"]["Data"]
    # Unlike the SQ021 source laptop, this standalone test device has no
    # quest scene that sends a device-state activation event before use.
    persistent["deviceState"] = "ON"
    setup = persistent["computerSetup"]
    setup["filesMenu"] = 1
    setup["mailsMenu"] = 0
    setup["mailsStructure"] = []
    setup["internetMenu"] = 0
    setup["internetSubnet"]["startingPage"] = ""
    setup["newsFeedMenu"] = 0
    setup["newsFeed"] = []
    setup["startingMenu"] = "FILES"
    setup["filesStructure"] = [
        {
            "$type": "gamedeviceGenericDataContent",
            "name": "FILES",
            "content": [
                {
                    "$type": "gamedeviceDataElement",
                    "content": TEXT["gl_gqt001_document_body"],
                    "date": "",
                    "documentName": {
                        "$type": "CName",
                        "$storage": "string",
                        "$value": "SIGNAL_DELAY",
                    },
                    "isEnabled": 1,
                    "isEncrypted": 0,
                    "journalPath": {
                        "HandleId": journal_handle,
                        "Data": {
                            "$type": "gameJournalPath",
                            "className": {
                                "$type": "CName",
                                "$storage": "string",
                                "$value": "gameJournalFile",
                            },
                            "editorPath": (
                                "Onscreens/Emails/Quests/Minor_quest/"
                                "Gqt001/Files/Diagnostic"
                            ),
                            "fileEntryIndex": 5,
                            "realPath": DOCUMENT_PATH,
                        },
                    },
                    "owner": "SYSTEM",
                    "questInfo": {
                        "$type": "gamedeviceQuestInfo",
                        "factName": {
                            "$type": "CName",
                            "$storage": "string",
                            "$value": "gqt001_document_read",
                        },
                        "isHighlighted": 1,
                    },
                    "title": TEXT["gl_gqt001_document_title"],
                    "videoPath": {
                        "$type": "redResourceReferenceScriptToken",
                        "resource": {
                            "DepotPath": {
                                "$type": "ResourcePath",
                                "$storage": "uint64",
                                "$value": "0",
                            },
                            "Flags": "Soft",
                        },
                    },
                    "wasRead": 0,
                }
            ],
            "name": "FILES",
        }
    ]
    persistent["contentScale"] = {
        "$type": "TweakDBID",
        "$storage": "uint64",
        "$value": "0",
    }
    # Cooked vanilla quest computers carry a raw/fallback controller followed
    # by a journal-backed controller. Preserve that topology: it controls
    # which package the computer UI binds when it builds its navigation tabs.
    fallback_persistent = controller_chunks[0]["persistentState"]["Data"]
    fallback_persistent["deviceState"] = "ON"
    fallback_persistent["computerSetup"] = copy.deepcopy(setup)
    fallback_persistent["contentScale"] = copy.deepcopy(
        persistent["contentScale"]
    )
    fallback_file = (
        fallback_persistent["computerSetup"]["filesStructure"][0]["content"][0]
    )
    fallback_file["journalPath"] = None
    fallback_file["questInfo"]["isHighlighted"] = 0
    node["Data"]["debugName"]["$value"] = "{gqt001_terminal_laptop}"
    scanner_chunks = [
        chunk
        for chunk in package["Chunks"]
        if chunk.get("$type") == "gameScanningComponent"
    ]
    if len(scanner_chunks) != 1:
        raise RuntimeError(
            "SQ021 terminal template must contain one gameScanningComponent"
        )
    scanner_chunks[0]["clues"] = []
    node_data = copy.deepcopy(node_data)
    node_data["Id"] = "0"
    node_data["NodeIndex"] = 0
    node_data["Position"].update(OWNED_LAPTOP_POSITION)
    node_data["Orientation"].update(OWNED_LAPTOP_ORIENTATION)
    for bound in ("Min", "Max"):
        node_data["Bounds"][bound].update(OWNED_LAPTOP_POSITION)
    node_data["QuestPrefabRefHash"] = {
        "$type": "NodeRef",
        "$storage": "string",
        "$value": OWNED_LAPTOP_NODE_REF,
    }
    node_data["CookedPrefabData"] = {
        "DepotPath": {
            "$type": "ResourcePath",
            "$storage": "uint64",
            "$value": "0",
        },
        "Flags": "Default",
    }
    node_data["MaxStreamingDistance"] = 280.0
    node_data["UkFloat1"] = 240.0
    node_data["Uk10"] = 1024
    node_data["Uk11"] = 512
    root["nodes"] = [node]
    root["nodeData"]["Data"] = [node_data]
    root["nodeData"]["Flags"] = 0
    root["nodeRefs"] = [
        {
            "$type": "NodeRef",
            "$storage": "string",
            "$value": OWNED_LAPTOP_NODE_REF,
        }
    ]
    root["category"] = "AlwaysLoaded"
    root["cookingPlatform"] = "PLATFORM_None"
    root["level"] = 1
    root["externInplaceResource"] = {
        "DepotPath": {
            "$type": "ResourcePath",
            "$storage": "uint64",
            "$value": "0",
        },
        "Flags": "Soft",
    }
    root["localInplaceResource"] = []
    root["variantIndices"] = [0]
    root["variantNodes"] = []
    root["persistentNodeIndex"] = 0
    sector["Data"]["EmbeddedFiles"] = []
    sector["Header"]["ArchiveFileName"] = str(INSTANCE_PATCH_ARCHIVE.resolve())
    sector["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return sector


def generate_block() -> dict[str, Any]:
    block = load(BLOCK_RAW)
    descriptors = block["Data"]["RootChunk"]["descriptors"]
    owned_path = (
        "mod\\gqt001\\world\\gqt001_laptop_instance.streamingsector"
    )
    descriptors[:] = [
        descriptor
        for descriptor in descriptors
        if descriptor["data"]["DepotPath"].get("$value") != owned_path
    ]
    always_loaded_descriptor = next(
        item
        for item in descriptors
        if item["data"]["DepotPath"].get("$value")
        == "mod\\gqt001\\world\\gqt001_always_loaded.streamingsector"
    )
    descriptor = copy.deepcopy(always_loaded_descriptor)
    descriptor["data"]["DepotPath"]["$value"] = owned_path
    descriptor["questPrefabNodeRef"] = {
        "$type": "NodeRef",
        "$storage": "uint64",
        "$value": "0",
    }
    descriptors.append(descriptor)
    block["Header"]["ArchiveFileName"] = str(BLOCK_ARCHIVE.resolve())
    block["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return block


def generate_device_registry() -> dict[str, Any]:
    """Register the owned laptop's persistent controller with Night City.

    The streamed entity can render and offer Use without this entry, but the
    device system cannot reliably resolve its ComputerControllerPS and builds
    the UI from entity defaults instead of the authored files structure.
    """

    return device_registry(
        DEVICE_REGISTRY_ARCHIVE,
        [
            DeviceRegistryEntry(
                node_ref=OWNED_LAPTOP_NODE_REF,
                node_hash=node_ref_hash(OWNED_LAPTOP_NODE_REF),
                controller_class="ComputerControllerPS",
                position=Vec3(
                    OWNED_LAPTOP_POSITION["X"],
                    OWNED_LAPTOP_POSITION["Y"],
                    OWNED_LAPTOP_POSITION["Z"],
                ),
            )
        ],
    )


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
    parser = argparse.ArgumentParser()
    parser.add_argument("--deserialize", action="store_true")
    args = parser.parse_args()
    outputs = (
        (JOURNAL_RAW, JOURNAL_ARCHIVE, generate_journal()),
        (ONSCREEN_RAW, ONSCREEN_ARCHIVE, generate_onscreens()),
        (INSTANCE_PATCH_RAW, INSTANCE_PATCH_ARCHIVE, generate_instance_patch()),
        (BLOCK_RAW, BLOCK_ARCHIVE, generate_block()),
        (
            DEVICE_REGISTRY_RAW,
            DEVICE_REGISTRY_ARCHIVE,
            generate_device_registry(),
        ),
    )
    for raw, archive, document in outputs:
        write(raw, document)
        if args.deserialize:
            deserialize(raw, archive)
        print(raw)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
