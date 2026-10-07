#!/usr/bin/env python3
"""Generate the GQT001 journal, localization, and owned laptop sector.

The test laptop is a mod-owned copy placed beside a native Kabuki laptop.
Keeping its persistent-state package inside a Ghostline sector avoids mutating
or sharing ownership with a base-world device.
"""

from __future__ import annotations

import argparse
import copy
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

from generate_world import DeviceRegistryEntry, Vec3, device_registry, node_ref_hash
from quest_authoring import compose as compose_quest, resolve_bindings
from quest_compiler import QuestArtifact, compile_manifest_artifacts
from quest_build import publish_build, relocate_artifacts
from quest_content import load, wrappers

MANIFEST = PROJECT / "gqt001_signal_delay.quest.json"
ROOT_RAW = PROJECT / "source/raw/mod/gqt001/phases/gqt001_signal_delay.questphase.json"
ROOT_ARCHIVE = PROJECT / "source/archive/mod/gqt001/phases/gqt001_signal_delay.questphase"

SECTOR_TEMPLATE = (
    ROOT
    / "reference/world/terminal-templates"
    / "exterior_19_-8_0_0.streamingsector.json"
)
INSTANCE_PATCH_RAW = (
    PROJECT / "source/raw/mod/gqt001/world" / "gqt001_laptop_instance.streamingsector.json"
)
INSTANCE_PATCH_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt001/world" / "gqt001_laptop_instance.streamingsector"
)
BLOCK_RAW = (
    PROJECT / "source/raw/mod/gqt001/world" / "gqt001_signal_delay.streamingblock.json"
)
BLOCK_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt001/world" / "gqt001_signal_delay.streamingblock"
)
DEVICE_REGISTRY_RAW = (
    PROJECT / "source/raw/mod/gqt001/world" / "gqt001_custom_devices.devices.json"
)
DEVICE_REGISTRY_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt001/world" / "gqt001_custom_devices.devices"
)
LAPTOP_NODE_REF = (
    "$/03_night_city/se1/#loc_sq021_trailer_park/"
    "loc_sq021_trailer_park_gameplay_prefabV4S2BNI/"
    "#loc_sq021_trailer_park_devices/#sq021_randy_pc"
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
JOURNAL_RAW = PROJECT / "source/raw/mod/gqt001/journal/gqt001.journal.json"
JOURNAL_ARCHIVE = PROJECT / "source/archive/mod/gqt001/journal/gqt001.journal"
ONSCREEN_RAW = (
    PROJECT / "source/raw/mod/gqt001/localization/en-us/onscreens/gqt001.json.json"
)
ONSCREEN_ARCHIVE = (
    PROJECT / "source/archive/mod/gqt001/localization/en-us/onscreens/gqt001.json"
)


def generate_journal() -> dict[str, Any]:
    return compose_quest(load(MANIFEST)).documents[r"mod\gqt001\journal\gqt001.journal"]


def generate_onscreens() -> dict[str, Any]:
    return compose_quest(load(MANIFEST)).documents[
        r"mod\gqt001\localization\en-us\onscreens\gqt001.json"
    ]


def generate_instance_patch(bindings: dict[str, Any] | None = None) -> dict[str, Any]:
    bindings = resolve_bindings(load(MANIFEST)) if bindings is None else bindings
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
    journal_handle = str(max(int(item["HandleId"]) for item in wrappers(node)) + 1)
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
            "content": [
                {
                    "$type": "gamedeviceDataElement",
                    "content": bindings["readables"]["diagnostic"]["text"],
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
                            "realPath": bindings["readables"]["diagnostic"]["path"],
                        },
                    },
                    "owner": "SYSTEM",
                    "questInfo": {
                        "$type": "gamedeviceQuestInfo",
                        "factName": {
                            "$type": "CName",
                            "$storage": "string",
                            "$value": bindings["facts"]["document_read"],
                        },
                        "isHighlighted": 1,
                    },
                    "title": bindings["readables"]["diagnostic"]["title"],
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
    fallback_persistent["contentScale"] = copy.deepcopy(persistent["contentScale"])
    fallback_file = fallback_persistent["computerSetup"]["filesStructure"][0][
        "content"
    ][0]
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
        "$value": bindings["locations"]["terminal"]["owned_device"],
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
            "$value": bindings["locations"]["terminal"]["owned_device"],
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
    owned_path = "mod\\gqt001\\world\\gqt001_laptop_instance.streamingsector"
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


def generate_device_registry(bindings: dict[str, Any] | None = None) -> dict[str, Any]:
    """Register the owned laptop's persistent controller with Night City.

    The streamed entity can render and offer Use without this entry, but the
    device system cannot reliably resolve its ComputerControllerPS and builds
    the UI from entity defaults instead of the authored files structure.
    """
    bindings = resolve_bindings(load(MANIFEST)) if bindings is None else bindings

    return device_registry(
        DEVICE_REGISTRY_ARCHIVE,
        [
            DeviceRegistryEntry(
                node_ref=bindings["locations"]["terminal"]["owned_device"],
                node_hash=node_ref_hash(
                    bindings["locations"]["terminal"]["owned_device"]
                ),
                controller_class="ComputerControllerPS",
                position=Vec3(
                    OWNED_LAPTOP_POSITION["X"],
                    OWNED_LAPTOP_POSITION["Y"],
                    OWNED_LAPTOP_POSITION["Z"],
                ),
            )
        ],
    )


def build_artifacts(output_root: Path | None = None) -> list[QuestArtifact]:
    bindings = resolve_bindings(load(MANIFEST))
    artifacts = compile_manifest_artifacts(MANIFEST, ROOT_RAW, ROOT_ARCHIVE)
    artifacts.extend(
        QuestArtifact(raw, archive, document)
        for raw, archive, document in (
            (
                INSTANCE_PATCH_RAW,
                INSTANCE_PATCH_ARCHIVE,
                generate_instance_patch(bindings),
            ),
            (BLOCK_RAW, BLOCK_ARCHIVE, generate_block()),
            (
                DEVICE_REGISTRY_RAW,
                DEVICE_REGISTRY_ARCHIVE,
                generate_device_registry(bindings),
            ),
        )
    )
    return relocate_artifacts(artifacts, output_root)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-root",
        "--out-root",
        type=Path,
        help="Stage a complete candidate under this root",
    )
    parser.add_argument("--deserialize", action="store_true")
    args = parser.parse_args(argv)
    outputs = publish_build(
        build_artifacts(),
        namespace="gqt001",
        output_root=args.output_root,
        deserialize=args.deserialize,
    )
    for raw, _archive in outputs:
        print(raw)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
