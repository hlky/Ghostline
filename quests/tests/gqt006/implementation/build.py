#!/usr/bin/env python3
"""Generate the placed GQT006 Goth Baddie Cyberpsycho quest package."""

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

import generate_world as world_builder
import ghostline_red
import quest_compiler
from braindance_pipeline import deserialize_cr2w_json, find_wolvenkit
from quest_content import (
    Handles,
    find_entry,
    load,
    make_choice,
    make_choice_group,
    make_conversation,
    make_message,
    make_phase,
    set_loc,
)


NAME = "gqt006_goth_baddie_cyberpsycho"
WORLD_SPEC = (
    ROOT / "quests/tests/gqt006/implementation/world/goth-baddie-cyberpsycho.world.json"
)
MANIFEST = ROOT / "quests/tests/gqt006_goth_baddie_cyberpsycho.quest.json"
JOURNAL_TEMPLATE = ROOT / "source/raw/mod/gq001/journal/gq001.journal.json"
ONSCREEN_TEMPLATE = (
    ROOT / "source/raw/mod/gq001/localization/en-us/onscreens/gq001.json.json"
)
JOURNAL_RAW = ROOT / "source/raw/mod/gqt006/journal/gqt006.journal.json"
JOURNAL_ARCHIVE = ROOT / "source/archive/mod/gqt006/journal/gqt006.journal"
ONSCREEN_RAW = (
    ROOT / "source/raw/mod/gqt006/localization/en-us/onscreens/gqt006.json.json"
)
ONSCREEN_ARCHIVE = (
    ROOT / "source/archive/mod/gqt006/localization/en-us/onscreens/gqt006.json"
)
ROOT_PHASE_RAW = ROOT / f"source/raw/mod/gqt006/phases/{NAME}.questphase.json"
ROOT_PHASE_ARCHIVE = ROOT / f"source/archive/mod/gqt006/phases/{NAME}.questphase"

TEXT = {
    "gl_gqt006_title": "Cyberpsycho Sighting: Goth Baddie",
    "gl_gqt006_01_objective_neutralize_goth_baddie": "Neutralize Goth Baddie",
    "gl_gqt006_01_description_neutralize_goth_baddie": (
        "A Ghostline netrunner has gone over the edge. Stop her before the "
        "feedback loop spreads."
    ),
    "gl_gqt006_01_mappin_goth_baddie": "Goth Baddie",
    "gl_gqt006_02_objective_read_goth_baddie_shard": "Read Goth Baddie's datashard",
    "gl_gqt006_02_description_read_goth_baddie_shard": (
        "The shard was still recording when Goth Baddie went down."
    ),
    "gl_gqt006_03_objective_leave_goth_baddie_site": "Leave the area",
    "gl_gqt006_03_description_leave_goth_baddie_site": (
        "Get clear while Patch isolates Goth Baddie's combat telemetry."
    ),
    "gl_gqt006_04_objective_report_goth_baddie": "Report to Patch",
    "gl_gqt006_04_description_report_goth_baddie": (
        "Tell Patch what happened to Goth Baddie."
    ),
    "gl_gqt006_shard_goth_baddie_title": "GOTH BADDIE // DEADMAN LOOP",
    "gl_gqt006_shard_goth_baddie_body": (
        "Combat telemetry repeats one instruction: HOLD THE LINE. Friendly "
        "signatures disappear one by one, but the loop keeps assigning new "
        "targets. The final entries are scarred by self-targeting ICE."
    ),
    "gl_gqt006_phone_report_title": "Goth Baddie",
    "gl_gqt006_phone_msg_status": (
        "I saw the spike drop. Tell me Goth Baddie's status."
    ),
    "gl_gqt006_phone_msg_killed": ("She's dead. The shard was still recording."),
    "gl_gqt006_phone_msg_spared": (
        "Alive. Unconscious. The shard was still recording."
    ),
    "gl_gqt006_phone_choice_send_shard": "Sending the shard.",
    "gl_gqt006_phone_choice_ask_context": "What happened to her?",
    "gl_gqt006_phone_reply_shard": (
        "Got it. I'll isolate the deck and scrub your signature."
    ),
    "gl_gqt006_phone_reply_context": (
        "Someone trained her nervous system to treat every connection as an "
        "attack. I'll find out who."
    ),
    "gl_gqt006_phone_msg_complete": "Get clear. Payment's sent.",
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
    quest = find_entry(journal, "gameJournalQuest", "gq001")
    phase_template = find_entry(journal, "gameJournalQuestPhase", "gq001_01")
    objective_template = find_entry(
        journal,
        "gameJournalQuestObjective",
        "gq001_01_obj_meet_patch",
    )

    quest["Data"]["id"] = "gqt006"
    quest["Data"]["type"] = "CyberPsycho"
    set_loc(quest["Data"], "title", "gl_gqt006_title")
    phase_specs = [
        (
            "gqt006_01",
            "gqt006_01_obj_neutralize_goth_baddie",
            "gl_gqt006_01_objective_neutralize_goth_baddie",
            "gqt006_01_desc_neutralize_goth_baddie",
            "gl_gqt006_01_description_neutralize_goth_baddie",
            [
                (
                    "gqt006_01_qmp_goth_baddie",
                    "gl_gqt006_01_mappin_goth_baddie",
                    "#gqt006_mp_goth_baddie",
                )
            ],
        ),
        (
            "gqt006_02",
            "gqt006_02_obj_read_goth_baddie_shard",
            "gl_gqt006_02_objective_read_goth_baddie_shard",
            "gqt006_02_desc_read_goth_baddie_shard",
            "gl_gqt006_02_description_read_goth_baddie_shard",
            [],
        ),
        (
            "gqt006_03",
            "gqt006_03_obj_leave_goth_baddie_site",
            "gl_gqt006_03_objective_leave_goth_baddie_site",
            "gqt006_03_desc_leave_goth_baddie_site",
            "gl_gqt006_03_description_leave_goth_baddie_site",
            [],
        ),
        (
            "gqt006_04",
            "gqt006_04_obj_report_goth_baddie",
            "gl_gqt006_04_objective_report_goth_baddie",
            "gqt006_04_desc_report_goth_baddie",
            "gl_gqt006_04_description_report_goth_baddie",
            [],
        ),
    ]
    quest["Data"]["entries"] = [
        make_phase(
            handles,
            phase_template,
            objective_template,
            phase_id=phase_id,
            objective_id=objective_id,
            objective_loc=objective_loc,
            description_id=description_id,
            description_loc=description_loc,
            mappins=mappins,
        )
        for (
            phase_id,
            objective_id,
            objective_loc,
            description_id,
            description_loc,
            mappins,
        ) in phase_specs
    ]

    contacts = find_entry(journal, "gameJournalPrimaryFolderEntry", "contacts")
    patch_template = find_entry(journal, "gameJournalContact", "patch")
    conversation_template = find_entry(
        journal,
        "gameJournalPhoneConversation",
        "gq001_05_delivery",
    )
    message_template = find_entry(
        journal,
        "gameJournalPhoneMessage",
        "01_msg_cache_authenticated",
    )
    choice_group_template = find_entry(
        journal,
        "gameJournalPhoneChoiceGroup",
        "03_ch_delivery_response",
    )
    choice_template = find_entry(
        journal,
        "gameJournalPhoneChoiceEntry",
        "03a_ch_pay_me",
    )
    patch = handles.clone(patch_template)
    report_entries = [
        make_message(
            handles,
            message_template,
            "01_msg_status",
            "gl_gqt006_phone_msg_status",
        ),
        make_message(
            handles,
            message_template,
            "02a_msg_killed",
            "gl_gqt006_phone_msg_killed",
        ),
        make_message(
            handles,
            message_template,
            "02b_msg_spared",
            "gl_gqt006_phone_msg_spared",
        ),
        make_choice_group(
            handles,
            choice_group_template,
            "03_ch_response",
            [
                make_choice(
                    handles,
                    choice_template,
                    "03a_ch_send_shard",
                    "gl_gqt006_phone_choice_send_shard",
                ),
                make_choice(
                    handles,
                    choice_template,
                    "03b_ch_ask_context",
                    "gl_gqt006_phone_choice_ask_context",
                ),
            ],
        ),
        make_message(
            handles,
            message_template,
            "04a_msg_shard",
            "gl_gqt006_phone_reply_shard",
        ),
        make_message(
            handles,
            message_template,
            "04b_msg_context",
            "gl_gqt006_phone_reply_context",
        ),
        make_message(
            handles,
            message_template,
            "05_msg_complete",
            "gl_gqt006_phone_msg_complete",
        ),
    ]
    patch["Data"]["entries"] = [
        make_conversation(
            handles,
            conversation_template,
            "gqt006_04_report",
            "gl_gqt006_phone_report_title",
            report_entries,
        )
    ]
    contacts["Data"]["entries"] = [patch]

    onscreen_group = find_entry(journal, "gameJournalOnscreenGroup", "shards")
    shard_template = find_entry(journal, "gameJournalOnscreen", "quiet_spine_01")
    shard = handles.clone(shard_template)
    shard["Data"]["id"] = "goth_baddie_datashard"
    set_loc(shard["Data"], "title", "gl_gqt006_shard_goth_baddie_title")
    set_loc(shard["Data"], "description", "gl_gqt006_shard_goth_baddie_body")
    onscreen_group["Data"]["entries"] = [shard]

    quest_folder = find_entry(journal, "gameJournalFolderEntry", "gq001")
    quest_folder["Data"]["id"] = "gqt006"

    poi = find_entry(
        journal,
        "gameJournalPointOfInterestMappin",
        "gq001_01_poi_patch_bridge",
    )
    poi["Data"]["id"] = "gqt006_01_poi_goth_baddie"
    poi["Data"]["staticNodeRef"]["$storage"] = "string"
    poi["Data"]["staticNodeRef"]["$value"] = "#gqt006_mp_goth_baddie"
    poi["Data"]["questPath"]["Data"]["realPath"] = "quests/minor_quest/gqt006"

    journal["Header"]["ArchiveFileName"] = str(JOURNAL_ARCHIVE.resolve())
    journal["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return journal


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
        for key, text in TEXT.items()
    ]
    onscreens["Header"]["ArchiveFileName"] = str(ONSCREEN_ARCHIVE.resolve())
    onscreens["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return onscreens


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
            "Invalid GQT006 manifest: "
            + "; ".join(item.message for item in diagnostics)
        )
    diagnostics.extend(quest_compiler.audit_resources(spec))
    errors = [item for item in diagnostics if item.level == "error"]
    if errors:
        raise ValueError(
            "GQT006 resource audit failed: "
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
    parser.add_argument(
        "--serializer",
        choices=("wolvenkit", "native"),
        default="wolvenkit",
    )
    parser.add_argument("--wolvenkit", type=Path)
    args = parser.parse_args()

    write(JOURNAL_RAW, generate_journal())
    write(ONSCREEN_RAW, generate_onscreens())
    outputs: list[tuple[Path, Path]] = [
        (JOURNAL_RAW, JOURNAL_ARCHIVE),
        (ONSCREEN_RAW, ONSCREEN_ARCHIVE),
    ]
    world_outputs = generate_world()
    outputs.extend((item.raw_path, item.archive_path) for item in world_outputs)
    outputs.extend(compile_quest())

    if args.deserialize:
        if args.serializer == "wolvenkit":
            wolvenkit = find_wolvenkit(args.wolvenkit)
            for raw, archive in outputs:
                deserialize_cr2w_json(raw, archive, wolvenkit=wolvenkit)
        else:
            for raw, archive in outputs:
                if raw == ONSCREEN_RAW:
                    ghostline_red.deserialize_localization(raw, archive)
                else:
                    ghostline_red.deserialize(raw, archive)

    print(
        json.dumps(
            {
                "ok": True,
                "origin": load(WORLD_SPEC)["origin"],
                "registered": True,
                "quest": str(ROOT_PHASE_RAW),
                "children": [
                    str(quest_compiler.resource_paths(stage.phase_resource)[0])
                    for stage in quest_compiler.load_spec(MANIFEST)[0].stages
                ],
                "journal": str(JOURNAL_RAW),
                "world": [str(item.raw_path) for item in world_outputs],
                "packed": bool(args.deserialize),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
