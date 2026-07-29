#!/usr/bin/env python3
"""Generate GQ003 journal and onscreen-localization authoring resources."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = next(
    parent for parent in Path(__file__).resolve().parents if (parent / "AGENTS.md").is_file()
)
TOOLS = ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from ghostline_red import deserialize as deserialize_cr2w


QUEST_MANIFEST = ROOT / "quests/story/ghostline/gq003/implementation/quest.json"
JOURNAL_TEMPLATE = ROOT / "source/raw/mod/gq002/journal/gq002.journal.json"
ONSCREEN_TEMPLATE = (
    ROOT / "source/raw/mod/gq002/localization/en-us/onscreens/gq002.json.json"
)
JOURNAL_RAW = ROOT / "source/raw/mod/gq003/journal/gq003.journal.json"
JOURNAL_ARCHIVE = ROOT / "source/archive/mod/gq003/journal/gq003.journal"
ONSCREEN_RAW = (
    ROOT / "source/raw/mod/gq003/localization/en-us/onscreens/gq003.json.json"
)
ONSCREEN_ARCHIVE = (
    ROOT / "source/archive/mod/gq003/localization/en-us/onscreens/gq003.json"
)


OBJECTIVE_COPY = {
    "meet_iris_briefing": ("Meet Iris.", "Iris has reconstructed part of Quiet Spine. Meet her and learn who is still trapped inside the route."),
    "read_reconstruction_report": ("Read Iris's reconstruction report.", "Review Iris's analysis of Mara Venn, Pair 07-B, and the Black Lantern transfer route."),
    "reach_freight_yard": ("Reach the Black Lantern freight yard.", "Find the municipal-salvage front Patch identified and locate Pair Seven's transfer records."),
    "remain_undetected": ("Optional: Remain undetected.", "Avoid raising the yard alarm while you identify and mark the expedited shipment."),
    "investigate_yard": ("Investigate the transfer yard.", "Scan the transfer board, neural stabilizers, and conscious-transport restraint case."),
    "read_expedited_handoff": ("Read the archived conversation.", "The restraint case contained a conversation between Sato and K. Morita."),
    "plant_routing_beacon": ("Install the routing beacon.", "Mount Iris's beacon on the Black Lantern routing hardware without interrupting its heartbeat."),
    "breach_dispatch_relay": ("Breach the dispatch relay.", "Use the authenticated route to identify Pair 07-B and Mara's current clinic."),
    "leave_freight_yard": ("Leave the freight yard.", "Clear the yard before Black Lantern can isolate the compromised route."),
    "reach_memory_clinic": ("Reach the memory clinic.", "Go to the clinic holding Mara Venn."),
    "clear_clinic_security": ("Neutralize the clinic security.", "Resolve the armed clinic personnel guarding Mara and the neural jammer."),
    "disable_neural_jammer": ("Disable the neural jammer.", "Shut down the field compressing the foreign memories inside Mara's implant."),
    "release_mara": ("Release Mara.", "Open Mara's restraint and keep the clinic from reclaiming her."),
    "escort_mara": ("Escort Mara out of the clinic.", "Keep Mara with you through the clinic exits and reach the stabilization point."),
    "stabilize_mara": ("Protect Mara while Iris stabilizes her implant.", "Hold the perimeter until Iris isolates the foreign memory loops."),
    "meet_iris_safe_site": ("Meet Iris at the safe site.", "Bring the stabilized Mara to Iris and decide how to recover Pair 07-B's cipher."),
    "enter_patch_vehicle": ("Get in Patch's vehicle.", "Use Patch's temporary van to pass the interchange's first security scan."),
    "ride_with_patch": ("Wait for Patch.", "Let Patch join you before taking the van to the freight interchange."),
    "drive_patch_to_interchange": ("Drive to the freight interchange.", "Take Patch's van to the parking row marked by Iris's beacon."),
    "steal_pair_07b": ("Steal the Black Lantern carrier.", "Find the refrigerated Pair 07-B box truck and take control of it."),
    "drive_carrier_to_relay": ("Drive the carrier to the reconstruction relay.", "Move Pair 07-B to the relay before Black Lantern can revoke its cipher."),
    "enter_reconstruction_relay": ("Enter the reconstruction relay.", "Reach the relay interior and secure the core before the retrieval team does."),
    "defeat_retrieval_team": ("Defeat Morita's retrieval team.", "Resolve the Black Lantern team sent to recover Pair 07-B."),
    "investigate_reconstruction_relay": ("Investigate the reconstruction relay.", "Scan the cipher rack, reconstruction core, and courier ledger."),
    "operate_reconstruction_core": ("Jack in to the reconstruction core.", "Apply your decision to the Black Lantern index and wait for the core to confirm it."),
    "leave_reconstruction_relay": ("Leave the reconstruction relay.", "Clear the site while Ghostline verifies what survived."),
    "deliver_black_lantern_package": ("Deposit the Black Lantern package.", "Deliver the preserved cipher or signed destruction receipt to Ghostline's drop point."),
    "black_lantern_debrief": ("Respond to Ghostline.", "Review the outcome with Morrow, Iris, and Patch."),
}


MAPPIN_COPY = {
    "gq003_02_qmp_iris": "Iris",
    "gq003_06_qmp_yard": "Black Lantern freight yard",
    "gq003_08_qmp_transfer_board": "Expedited transfer board",
    "gq003_08_qmp_neural_stabilizers": "Neural stabilizers",
    "gq003_08_qmp_restraint_case": "Conscious-transport restraint",
    "gq003_10_qmp_beacon_mount": "Routing beacon mount",
    "gq003_11_qmp_dispatch": "Dispatch relay",
    "gq003_14_qmp_clinic": "Memory clinic",
    "gq003_16_qmp_jammer": "Neural jammer",
    "gq003_18_qmp_escort_gate_01": "Clinic exit",
    "gq003_18_qmp_escort_gate_02": "Service corridor",
    "gq003_18_qmp_escort_gate_03": "Stabilization point",
    "gq003_20_qmp_iris": "Iris's safe site",
    "gq003_22_qmp_vehicle": "Patch's vehicle",
    "gq003_24_qmp_interchange": "Freight interchange",
    "gq003_25_qmp_carrier": "Pair 07-B carrier",
    "gq003_26_qmp_relay": "Reconstruction relay",
    "gq003_28_qmp_relay": "Reconstruction relay",
    "gq003_30_qmp_carrier_rack": "Pair 07-B cipher rack",
    "gq003_30_qmp_core": "Mnemonic reconstruction core",
    "gq003_30_qmp_ledger": "Black Lantern courier ledger",
    "gq003_33_qmp_core": "Reconstruction core",
    "gq003_35_qmp_drop_point": "Ghostline drop point",
}


PHONE_COPY = {
    "contacts/patch/gq003_01_offer/01_msg_quiet_spine_opened": "Need you to meet Iris. Quiet Spine finally opened. She says the cache contained a person who is still alive.",
    "contacts/patch/gq003_01_offer/02_ch_respond/02a_ch_send_location": "Send the location.",
    "contacts/patch/gq003_05_yard_identifier/01_msg_yard_alias": "Yard calls itself Kuroda Municipal Salvage. It is neither Kuroda, municipal, nor interested in salvage.",
    "contacts/patch/gq003_05_yard_identifier/02_msg_gate_phrase": "Freight gate phrase is BLACK LANTERN, PAIR SEVEN, PRIORITY WEATHER.",
    "contacts/patch/gq003_05_yard_identifier/03_ch_ack/03a_ch_understood": "Understood.",
    "contacts/patch/gq003_05_yard_identifier/04a_msg_location_sent": "Sending the yard coordinates now.",
    "contacts/patch/gq003_05_yard_identifier/03_ch_ack/03b_ch_repeat_phrase": "Repeat the phrase.",
    "contacts/patch/gq003_05_yard_identifier/04b_msg_phrase_repeated": "BLACK LANTERN, PAIR SEVEN, PRIORITY WEATHER. Look annoyed if anyone asks.",
    "contacts/patch/gq003_05_yard_identifier/05_msg_route_ready": "If anybody asks what it means, tell them Morita changed it twice already.",
    "contacts/iris/gq003_13_clinic_location/01_msg_trace_ready": "The beacon resolved Mara's clinic. I have the location.",
    "contacts/iris/gq003_13_clinic_location/02a_msg_clean_yard": "The beacon authenticated without an alarm. Black Lantern still believes Pair Seven is on schedule.",
    "contacts/iris/gq003_13_clinic_location/02b_msg_detected_yard": "Yard raised an intrusion flag. The beacon is still transmitting, but the clinic will know somebody touched the route.",
    "contacts/patch/gq003_13_clinic_location/01a_msg_clean_yard": "Clean enough to make me jealous. I try that and a door asks for three references.",
    "contacts/patch/gq003_13_clinic_location/01b_msg_detected_yard": "Freight crew is shouting into every channel they own. Clinic will be awake. Probably armed. Definitely rude.",
    "contacts/iris/gq003_13_clinic_location/03_ch_ack/03a_ch_send_location": "Send the location.",
    "contacts/iris/gq003_13_clinic_location/04a_msg_location_sent": "Uploading the clinic coordinates.",
    "contacts/iris/gq003_13_clinic_location/03_ch_ack/03b_ch_jammer": "What about the jammer?",
    "contacts/iris/gq003_13_clinic_location/04b_msg_jammer_warning": "It is stronger than the clinic walls. Disable it before you search for Mara.",
    "contacts/iris/gq003_13_clinic_location/05_msg_clinic_marked": "Clinic marked. Bring Mara out conscious if you can.",
    "contacts/patch/gq003_21_confession/01_msg_iris_told_you": "Iris told you.",
    "contacts/patch/gq003_21_confession/02_ch_confront/02a_ch_knew_couriers": "You knew about the couriers.",
    "contacts/patch/gq003_21_confession/03a_msg_confession": "Knew they used people. Did not know they used the people. I believed not asking kept the route cheap and me alive.",
    "contacts/patch/gq003_21_confession/02_ch_confront/02b_ch_how_many": "How many courier runs did you touch?",
    "contacts/patch/gq003_21_confession/03b_msg_four_runs": "Four sealed cases. Two dead drops. No names.",
    "contacts/patch/gq003_21_confession/04_msg_vehicle_sent": "I have a van at the safe site. Registry clears the first scan. After that, we improvise in person.",
    "contacts/morrow/gq003_31_relay_argument/01_msg_morrow_preserve": "The ledger carries Morita's live attestation. Preserve the route and I can follow the next handshake upstream.",
    "contacts/iris/gq003_31_relay_argument/02_msg_iris_burn": "The same route carries names for every stolen identity. Leave it open and anyone with the cipher can reconstruct them again.",
    "contacts/morrow/gq003_31_relay_argument/03_msg_morrow_future": "Burn it and Morita disappears behind the organization that paid him. We save today's couriers and guarantee replacements tomorrow.",
    "contacts/iris/gq003_31_relay_argument/04_msg_iris_present": "Preserve it and the people already inside remain inventory. A future rescue does not cancel a present weapon.",
    "contacts/morrow/gq003_31_relay_argument/05_msg_morrow_trace": "V, keep the line open. We trace Morita, copy what we need, then close it from the top.",
    "contacts/iris/gq003_31_relay_argument/06_msg_iris_erase": "There is no harmless copy. Erase the index and issue the wipe. Mara keeps her life. The route loses everyone else's.",
    "contacts/morrow/gq003_31_relay_argument/07_ch_outcome/07a_ch_preserve": "Keep the line open. Find Morita.",
    "contacts/morrow/gq003_31_relay_argument/08a_msg_preserve_confirmed": "Confirmed. Authenticate the cipher and leave the uplink intact.",
    "contacts/morrow/gq003_31_relay_argument/07_ch_outcome/07b_ch_burn": "Erase the route. Nobody gets the names.",
    "contacts/iris/gq003_31_relay_argument/08b_msg_burn_confirmed": "Confirmed. Revoke every package, then destroy the local key.",
    "contacts/morrow/gq003_31_relay_argument/09_msg_operate_core": "Decision recorded. Operate the reconstruction core.",
    "contacts/morrow/gq003_36_debrief/01a_msg_route_preserved": "Black Lantern is still carrying traffic. Now it carries our shadow with it.",
    "contacts/iris/gq003_36_debrief/02a_msg_route_preserved": "You gave Morrow a map made of people. Make sure he remembers what the symbols mean.",
    "contacts/morrow/gq003_36_debrief/01b_msg_route_burned": "You protected the couriers and destroyed the only clean path upward. Iris calls that mercy. I call it an expensive preference.",
    "contacts/iris/gq003_36_debrief/02b_msg_route_burned": "Mara remembers one apartment now. Her own. That will have to count as a victory.",
    "contacts/morrow/gq003_36_debrief/03a_msg_stealth_succeeded": "The freight yard still treats Pair Seven as an internal failure. No public description, no bounty. Clean work.",
    "contacts/morrow/gq003_36_debrief/03b_msg_stealth_failed": "Freight security circulated your description. Black Lantern knows the route was attacked, even if it does not know what survived.",
    "contacts/morrow/gq003_36_debrief/04_ch_response/04a_ch_people_not_infrastructure": "People aren't route infrastructure.",
    "contacts/morrow/gq003_36_debrief/05a_msg_leverage": "No. They were leverage. Our disagreement is whether destroying the leverage removes the hand holding it.",
    "contacts/morrow/gq003_36_debrief/04_ch_response/04b_ch_morita_out_there": "Morita is still out there.",
    "contacts/morrow/gq003_36_debrief/05b_msg_adapt": "Correct. You changed the route, not the destination. We adapt.",
    "contacts/morrow/gq003_36_debrief/06_msg_payment": "Payment transferred. Keep the channel open. Black Lantern was a route, not the destination.",
    "contacts/patch/gq003_36_debrief/07_msg_confession_postscript": "Should've told you what I knew. Next time I sell confidence, ask what I'm using as collateral.",
}


CONVERSATION_TITLES = {
    "gq003_01_offer": "Black Lantern",
    "gq003_05_yard_identifier": "Priority Weather",
    "gq003_13_clinic_location": "Lantern 07-A",
    "gq003_21_confession": "Sealed Cases",
    "gq003_31_relay_argument": "The Route",
    "gq003_36_debrief": "Black Lantern",
}


READABLES = {
    "files/reconstruction_report": (
        "QUIET SPINE RECONSTRUCTION / BLACK LANTERN",
        "AUTHOR: IRIS\nSTATUS: PARTIAL RECONSTRUCTION\nSOURCE: QUIET SPINE CACHE\n\nThe source contains indexed mnemonic fragments and the route metadata required to recombine them.\n\nPAIR 07-A\nMNEMONIC SUBJECT: MARA VENN\nFUNCTION: carries autobiographical fragments embedded as personal experience\nCURRENT STATE: active / graft rejection detected\n\nPAIR 07-B\nCIPHER SUBJECT: FREIGHT VEHICLE BL-07B\nFUNCTION: carries reconstruction key, fragment index, and route attestation\nCURRENT STATE: expedited handoff\n\nNeither half is sufficient alone. The mnemonic subject cannot identify the foreign fragments. The cipher can identify them but contains no experiential payload.\n\nROUTING ALIAS: BLACK LANTERN\nDISPATCH AUTHORITY: K. MORITA\nTRIGGER FOR EXPEDITED HANDOFF: KABUKI CLASSIFIER OFFLINE\n\nASSESSMENT:\nQuiet Spine did not move files. It moved the instructions for rebuilding people.",
    ),
    "shards/expedited_handoff": (
        "Archived conversation: Sato and K. Morita",
        "SATO: Kabuki classifier is gone. Pair Seven needs moving tonight.\n\nK. MORITA: Mnemonic subject first. Cipher remains on the freight route.\n\nSATO: Subject is rejecting the graft.\n\nK. MORITA: Rejection proves the original personality is still present.\n\nSATO: Clinic wants authorization to wipe her.\n\nK. MORITA: Denied. An empty courier cannot confirm the reconstruction.\n\nSATO: And after confirmation?\n\nK. MORITA: The clinic has standing disposal terms. Do not ask a question your invoice already answers.",
    ),
    "files/clinic_intake": (
        "Patient intake: Lantern 07-A",
        "PATIENT ALIAS: LANTERN 07-A\nINTAKE CONDITION: ambulatory, disoriented, combative when addressed as MARA\nIMPLANT: obsolete Zetatech mnemonic co-processor, aftermarket maintenance\nGRAFT ACCEPTANCE: 61 percent and declining\n\nREPORTED CONTAMINATION:\n- recalls three apartments under three legal names\n- identifies ventilation faults in buildings not present in employment record\n- responds to the name AKIKO during REM intrusion\n- repeatedly asks whether the hallway has been moved\n\nCLIENT INSTRUCTION:\nMaintain conscious state. Do not wipe without K. MORITA authorization.\n\nCLINIC NOTE:\nPatient keeps repairing the room thermostat. We disconnected it. She repaired the wall sensor instead.",
    ),
    "files/mara_maintenance_ticket": (
        "Mara Venn: unsent maintenance ticket",
        "TENANT: MARA VENN\nBUILDING: H8 SERVICE STACK / UNIT 42\nTICKET: AIR HANDLER CYCLING FALSE HUMIDITY\n\nReplaced the intake sensor again. Controller still reports moisture when the duct is dry. Fault is upstream, probably the building relay copying stale readings into every apartment loop.\n\nIf management closes this as USER ERROR one more time, tell them the system is remembering weather that is not there.\n\nDraft not submitted.",
    ),
    "files/courier_ledger": (
        "Black Lantern courier ledger",
        "BLACK LANTERN / MNEMONIC TRANSPORT LEDGER\nAUTHORIZED VIEW: ROUTE OPERATOR\n\nPAIR 01  VERIFIED      SUBJECT INDEX SEALED\nPAIR 02  VERIFIED      SUBJECT INDEX SEALED\nPAIR 03  PARTIAL       MNEMONIC SUBJECT UNRECOVERABLE\nPAIR 04  VERIFIED      SUBJECT INDEX SEALED\nPAIR 05  REVOKED       CIPHER LOST / SUBJECTS WIPED\nPAIR 06  PARTIAL       DESTINATION IDENTITY UNSTABLE\nPAIR 07  EXPEDITED     MARA VENN / CIPHER INBOUND\n\nACTIVE ROUTE AUTHORITY: K. MORITA\nUPSTREAM AUTHORITY: [EXTERNAL ATTESTATION]\n\nOPERATOR NOTE:\nCourier names are retained until destination reconstruction is confirmed. Deletion before confirmation invalidates route payment and upstream audit.\n\nPENDING SIGNAL:\nPAIR 08 selection suspended -- KABUKI CLASSIFIER OFFLINE",
    ),
}


ITEM_COPY = {
    "gl_gq003_item_route_auth_name": "Black Lantern route authorization",
    "gl_gq003_item_route_beacon_name": "Black Lantern routing beacon",
    "gl_gq003_item_cipher_name": "Black Lantern reconstruction cipher",
    "gl_gq003_item_receipt_name": "Black Lantern destruction receipt",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


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


def loc_key(path: str, suffix: str | None = None) -> str:
    value = "gl_" + path.replace("/", "_")
    return f"{value}_{suffix}" if suffix else value


def make_phase(
    handles: Handles,
    phase_template: dict[str, Any],
    objective_template: dict[str, Any],
    *,
    phase_id: str,
    objective_path: str,
    description_path: str,
    mappins: list[tuple[str, str]],
) -> dict[str, Any]:
    phase = handles.clone(phase_template)
    phase["Data"]["id"] = phase_id
    phase["Data"]["entries"] = []
    objective = handles.clone(objective_template)
    objective["Data"]["id"] = objective_path.rsplit("/", 1)[-1]
    set_loc(objective["Data"], "description", loc_key(objective_path))
    objective["Data"]["entries"] = []
    map_template = next(
        child for child in objective_template["Data"]["entries"]
        if child["Data"]["$type"] == "gameJournalQuestMapPin"
    )
    description_template = next(
        child for child in objective_template["Data"]["entries"]
        if child["Data"]["$type"] == "gameJournalQuestDescription"
    )
    for mappin_path, node_ref in mappins:
        pin = handles.clone(map_template)
        pin_data = pin["Data"]
        pin_data["id"] = mappin_path.rsplit("/", 1)[-1]
        pin_data["mappinData"]["debugCaption"] = MAPPIN_COPY[pin_data["id"]]
        set_loc(pin_data["mappinData"], "localizedCaption", loc_key(mappin_path))
        pin_data["reference"]["reference"]["$storage"] = "string"
        pin_data["reference"]["reference"]["$value"] = node_ref
        objective["Data"]["entries"].append(pin)
    description = handles.clone(description_template)
    description["Data"]["id"] = description_path.rsplit("/", 1)[-1]
    set_loc(description["Data"], "description", loc_key(description_path))
    objective["Data"]["entries"].append(description)
    phase["Data"]["entries"].append(objective)
    return phase


def phone_paths(value: Any) -> list[str]:
    result: list[str] = []

    def visit(child: Any) -> None:
        if isinstance(child, str) and child.startswith("contacts/"):
            if len(child.split("/")) >= 4 and child not in result:
                result.append(child)
        elif isinstance(child, dict):
            for nested in child.values():
                visit(nested)
        elif isinstance(child, list):
            for nested in child:
                visit(nested)

    visit(value)
    return result


def generate_journal() -> dict[str, Any]:
    manifest = load(QUEST_MANIFEST)
    journal = load(JOURNAL_TEMPLATE)
    handles = Handles(journal)
    quest = find_entry(journal, "gameJournalQuest", "gq002")
    phase_template = find_entry(journal, "gameJournalQuestPhase", "gq002_01")
    objective_template = find_entry(
        journal, "gameJournalQuestObjective", "gq002_01_obj_meet_cinder"
    )
    quest["Data"]["id"] = "gq003"
    set_loc(quest["Data"], "title", "gl_gq003_title")
    phases = []
    for stage in manifest["stages"]:
        objective_path = stage.get("objective")
        if not objective_path:
            continue
        phase_id = objective_path.split("/")[3]
        objective_id = objective_path.rsplit("/", 1)[-1]
        description_path = stage.get(
            "description_entry",
            f"{objective_path}/{objective_id.replace('_obj_', '_desc_')}",
        )
        mappins: list[tuple[str, str]] = []
        if stage.get("mappin"):
            mappin_path = stage["mappin"]
            marker = "#" + mappin_path.rsplit("/", 1)[-1].replace("_qmp_", "_mp_")
            mappins.append((mappin_path, marker))
        for clue in stage.get("clues", []):
            if clue.get("mappin"):
                mappins.append((clue["mappin"], clue["object_ref"]))
        for index, mappin_path in enumerate(stage.get("route_mappins", [])):
            mappins.append((mappin_path, stage["destinations"][index]))
        phases.append(
            make_phase(
                handles,
                phase_template,
                objective_template,
                phase_id=phase_id,
                objective_path=objective_path,
                description_path=description_path,
                mappins=mappins,
            )
        )
    quest["Data"]["entries"] = phases

    contacts_folder = find_entry(journal, "gameJournalPrimaryFolderEntry", "contacts")
    contact_template = find_entry(journal, "gameJournalContact", "cinder")
    conversation_template = find_entry(
        journal, "gameJournalPhoneConversation", "gq002_08_debrief"
    )
    message_template = find_entry(
        journal, "gameJournalPhoneMessage", "01_msg_outcome"
    )
    choice_group_template = find_entry(
        journal, "gameJournalPhoneChoiceGroup", "03_ch_response"
    )
    choice_template = find_entry(
        journal, "gameJournalPhoneChoiceEntry", "03a_ch_hard"
    )
    grouped: dict[tuple[str, str], list[str]] = defaultdict(list)
    for path in phone_paths(manifest):
        parts = path.split("/")
        grouped[(parts[1], parts[2])].append(path)
    contacts: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for (contact_id, conversation_id), paths in grouped.items():
        direct_paths = [path for path in paths if len(path.split("/")) == 4]
        child_paths: dict[str, list[str]] = defaultdict(list)
        for path in paths:
            parts = path.split("/")
            if len(parts) == 5:
                child_paths[parts[3]].append(path)
        entries = []
        for path in direct_paths:
            entry_id = path.rsplit("/", 1)[-1]
            if entry_id in child_paths or "_ch_" in entry_id:
                group = handles.clone(choice_group_template)
                group["Data"]["id"] = entry_id
                group["Data"]["entries"] = []
                for choice_path in child_paths[entry_id]:
                    choice = handles.clone(choice_template)
                    choice["Data"]["id"] = choice_path.rsplit("/", 1)[-1]
                    set_loc(choice["Data"], "text", loc_key(choice_path))
                    group["Data"]["entries"].append(choice)
                entries.append(group)
            else:
                message = handles.clone(message_template)
                message["Data"]["id"] = entry_id
                set_loc(message["Data"], "text", loc_key(path))
                entries.append(message)
        conversation = handles.clone(conversation_template)
        conversation["Data"]["id"] = conversation_id
        set_loc(
            conversation["Data"],
            "title",
            f"gl_contacts_{contact_id}_{conversation_id}_title",
        )
        conversation["Data"]["entries"] = entries
        contacts[contact_id].append(conversation)
    contact_entries = []
    contact_names = {"patch": "gq_npc_patch", "iris": "gq_npc_iris", "morrow": "gq_npc_morrow"}
    for contact_id in ("patch", "iris", "morrow"):
        contact = handles.clone(contact_template)
        contact["Data"]["id"] = contact_id
        set_loc(contact["Data"], "name", contact_names[contact_id])
        contact["Data"]["entries"] = contacts[contact_id]
        contact_entries.append(contact)
    contacts_folder["Data"]["entries"] = contact_entries

    onscreen_folder = find_entry(journal, "gameJournalFolderEntry", "gq002")
    group_template = find_entry(journal, "gameJournalOnscreenGroup", "shards")
    entry_template = find_entry(journal, "gameJournalOnscreen", "hostage_circuit")
    onscreen_folder["Data"]["id"] = "gq003"
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for relative_path in READABLES:
        group_id, entry_id = relative_path.split("/", 1)
        entry = handles.clone(entry_template)
        entry["Data"]["id"] = entry_id
        base = f"onscreens/emails/quests/minor_quest/gq003/{relative_path}"
        set_loc(entry["Data"], "title", loc_key(base, "title"))
        set_loc(entry["Data"], "description", loc_key(base, "body"))
        groups[group_id].append(entry)
    onscreen_folder["Data"]["entries"] = []
    for group_id in ("shards", "files"):
        group = handles.clone(group_template)
        group["Data"]["id"] = group_id
        group["Data"]["entries"] = groups[group_id]
        onscreen_folder["Data"]["entries"].append(group)

    poi = find_entry(
        journal, "gameJournalPointOfInterestMappin", "gq002_01_poi_cinder"
    )
    poi["Data"]["id"] = "gq003_02_poi_iris"
    poi["Data"]["staticNodeRef"]["$storage"] = "string"
    poi["Data"]["staticNodeRef"]["$value"] = "#gq003_02_mp_iris"
    poi["Data"]["questPath"]["Data"]["realPath"] = "quests/minor_quest/gq003"

    journal["Header"]["ArchiveFileName"] = str(JOURNAL_ARCHIVE.resolve())
    journal["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return journal


def generate_onscreens() -> dict[str, Any]:
    manifest = load(QUEST_MANIFEST)
    text = {"gl_gq003_title": "Black Lantern"}
    for stage in manifest["stages"]:
        objective_path = stage.get("objective")
        if not objective_path:
            continue
        objective_id = objective_path.rsplit("/", 1)[-1]
        description_path = stage.get(
            "description_entry",
            f"{objective_path}/{objective_id.replace('_obj_', '_desc_')}",
        )
        objective, description = OBJECTIVE_COPY[stage["id"]]
        text[loc_key(objective_path)] = objective
        text[loc_key(description_path)] = description
        if stage.get("mappin"):
            path = stage["mappin"]
            text[loc_key(path)] = MAPPIN_COPY[path.rsplit("/", 1)[-1]]
        for clue in stage.get("clues", []):
            if clue.get("mappin"):
                path = clue["mappin"]
                text[loc_key(path)] = MAPPIN_COPY[path.rsplit("/", 1)[-1]]
        for path in stage.get("route_mappins", []):
            text[loc_key(path)] = MAPPIN_COPY[path.rsplit("/", 1)[-1]]
    for path, value in PHONE_COPY.items():
        text[loc_key(path)] = value
    for path in phone_paths(manifest):
        parts = path.split("/")
        text[f"gl_contacts_{parts[1]}_{parts[2]}_title"] = CONVERSATION_TITLES[parts[2]]
    for relative_path, (title, body) in READABLES.items():
        base = f"onscreens/emails/quests/minor_quest/gq003/{relative_path}"
        text[loc_key(base, "title")] = title
        text[loc_key(base, "body")] = body
    text.update(ITEM_COPY)
    missing = sorted(
        path for path in phone_paths(manifest)
        if len(path.split("/")) >= 4
        and "_ch_" not in path.split("/")[-1]
        and path not in PHONE_COPY
    )
    if missing:
        raise RuntimeError(f"Missing phone copy: {missing}")
    onscreens = load(ONSCREEN_TEMPLATE)
    entries = onscreens["Data"]["RootChunk"]["root"]["Data"]["entries"]
    entries[:] = [
        {
            "$type": "localizationPersistenceOnScreenEntry",
            "femaleVariant": value,
            "maleVariant": "",
            "primaryKey": "0",
            "secondaryKey": key,
        }
        for key, value in text.items()
    ]
    onscreens["Header"]["ArchiveFileName"] = str(ONSCREEN_ARCHIVE.resolve())
    onscreens["Header"]["ExportedDateTime"] = "1970-01-01T00:00:00Z"
    return onscreens


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--deserialize", action="store_true")
    args = parser.parse_args()
    write(JOURNAL_RAW, generate_journal())
    write(ONSCREEN_RAW, generate_onscreens())
    if args.deserialize:
        deserialize_cr2w(JOURNAL_RAW, JOURNAL_ARCHIVE)
        deserialize_cr2w(ONSCREEN_RAW, ONSCREEN_ARCHIVE)
    print(JOURNAL_RAW)
    print(ONSCREEN_RAW)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
