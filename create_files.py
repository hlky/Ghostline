import json
import wave
from pathlib import Path
import random

mod_path = Path(__file__).parent

speaker_to_id = {"patch": 0, "v": 1}


def fnv1a64_hash(value: str | bytes | int) -> int:
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        value = value.encode("utf-8")
    hash_value = 0xCBF29CE484222325
    fnv_prime = 0x100000001B3
    for byte in value:
        hash_value ^= byte
        hash_value = (hash_value * fnv_prime) & 0xFFFFFFFFFFFFFFFF
    return hash_value


def create_file(mod_path: Path, filename: str, file_type: str) -> dict:
    return {
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": "2026-04-01T18:33:04.7099264Z",
            "DataType": "CR2W",
            "ArchiveFileName": str(mod_path / "source" / "archive" / filename),
        },
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {
                "$type": "JsonResource",
                "cookingPlatform": "PLATFORM_PC",
                "root": {
                    "HandleId": "0",
                    "Data": {
                        "$type": file_type,
                        "entries": [],
                    },
                },
            },
            "EmbeddedFiles": [],
        },
    }


def add_onscreen(file_data: dict, string_id: str | int, text: str) -> None:
    file_data["Data"]["RootChunk"]["root"]["Data"]["entries"].append(
        {
            "$type": "localizationPersistenceOnScreenEntry",
            "femaleVariant": text,
            "maleVariant": text,
            "primaryKey": str(string_id),
            "secondaryKey": "",
        }
    )


def add_subtitle(file_data: dict, string_id: str | int, text: str) -> None:
    file_data["Data"]["RootChunk"]["root"]["Data"]["entries"].append(
        {
            "$type": "localizationPersistenceSubtitleEntry",
            "femaleVariant": text,
            "maleVariant": text,
            "stringId": str(string_id),
        }
    )


def add_vo(file_data: dict, string_id: str | int, path: str) -> None:
    entry = {
        "$type": "locVoLineEntry",
        "femaleResPath": {
            "DepotPath": {
                "$type": "ResourcePath",
                "$storage": "string",
                "$value": path,
            },
            "Flags": "Soft",
        },
        "maleResPath": {
            "DepotPath": {
                "$type": "ResourcePath",
                "$storage": "string",
                "$value": path,
            },
            "Flags": "Soft",
        },
        "stringId": str(string_id),
    }
    file_data["Data"]["RootChunk"]["root"]["Data"]["entries"].append(entry)


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=0, ensure_ascii=False, separators=(',', ':')).replace("\n", ""), encoding="utf-8")


def load_json(path: Path, filename: str) -> dict:
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    data["Header"]["ArchiveFileName"] = str(mod_path / "source" / "archive" / filename)
    return data


def key_to_id(key: str) -> int:
    return fnv1a64_hash(key)


def get_wav_duration_ms(path: Path) -> int:
    with wave.open(str(path), "rb") as wav_file:
        frames = wav_file.getnframes()
        rate = wav_file.getframerate()
        if rate <= 0:
            raise ValueError(f"Invalid sample rate in {path}")
        duration_ms = round((frames / rate) * 1000)
        return max(duration_ms, 1)


def get_spoken_wav_path(key: str, speaker: str) -> Path:
    string_id = key_to_id(key)
    hex_id = f"{string_id:016x}"
    path = (
        mod_path
        / "source"
        / "archive"
        / "mod"
        / "gq000"
        / "localization"
        / "en-us"
        / "vo"
    )
    key_path = path / f"{key}.wav"
    hex_path = path / f"{speaker.lower()}_i_{hex_id}.wav"
    if key_path.exists():
        key_path.rename(hex_path)
    return hex_path


def build_audio_timing_map(spoken_lines: dict[str, dict]) -> dict[str, int]:
    timing_map = {}
    for key in spoken_lines:
        wav_path = get_spoken_wav_path(key, spoken_lines[key]["speaker"])
        if not wav_path.exists():
            raise FileNotFoundError(f"Missing WAV for {key}: {wav_path}")
        timing_map[key] = get_wav_duration_ms(wav_path)
    return timing_map


subtitle_type = "localizationPersistenceSubtitleEntries"
vo_type = "locVoiceoverMap"
onscreen_type = "localizationPersistenceOnScreenEntries"

subtitles_file = create_file(
    mod_path, "mod\\gq000\\localization\\en-us\\subtitles\\gq000_01.json", subtitle_type
)
vo_file = create_file(
    mod_path, "mod\\gq000\\localization\\en-us\\vo\\gq000_01.json", vo_type
)
onscreens_file = create_file(
    mod_path, "mod\\gq000\\localization\\en-us\\onscreens\\gq000_01.json", onscreen_type
)
scene_file = load_json(
    Path("template.scene.json"), "mod\\gq000\\scenes\\gq000_01.scene"
)


def validate_spoken_lines(spoken_lines: dict) -> None:
    for key, data in spoken_lines.items():
        if "text" not in data:
            raise ValueError(f"{key} missing text")
        if "speaker" not in data:
            raise ValueError(f"{key} missing speaker")
        if "addressee" not in data:
            raise ValueError(f"{key} missing addressee")
        if data["speaker"].lower() not in speaker_to_id:
            raise ValueError(f"{key} invalid speaker: {data['speaker']}")
        if data["addressee"].lower() not in speaker_to_id:
            raise ValueError(f"{key} invalid addressee: {data['addressee']}")


def validate_choice_lines(choice_lines: dict) -> None:
    for key, data in choice_lines.items():
        if "text" not in data:
            raise ValueError(f"{key} missing text")


def add_choice(scene_embedded: dict, scene_options: list, string_id: int, text: str):
    vpe_index = len(scene_embedded["vpEntries"])
    item_id = 2 + (len(scene_options) * 256)
    variant_id = string_id + 4
    scene_vd = {
        "$type": "scnlocLocStoreEmbeddedVariantDescriptorEntry",
        "localeId": "db_db",
        "locstringId": {"$type": "scnlocLocstringId", "ruid": f"{string_id}"},
        "signature": {"$type": "scnlocSignature", "val": "3"},
        "variantId": {"$type": "scnlocVariantId", "ruid": f"{variant_id}"},
        "vpeIndex": vpe_index,
    }
    scene_vp = {
        "$type": "scnlocLocStoreEmbeddedVariantPayloadEntry",
        "content": text,
        "variantId": {"$type": "scnlocVariantId", "ruid": f"{variant_id}"},
    }
    scene_option = {
        "$type": "scnscreenplayChoiceOption",
        "itemId": {"$type": "scnscreenplayItemId", "id": item_id},
        "locstringId": {"$type": "scnlocLocstringId", "ruid": f"{string_id}"},
        "usage": {
            "$type": "scnscreenplayOptionUsage",
            "playerGenderMask": {"$type": "scnGenderMask", "mask": 3},
        },
    }
    scene_embedded["vpEntries"].append(scene_vp)
    scene_embedded["vdEntries"].append(scene_vd)
    scene_options.append(scene_option)


def add_dialogue(scene_lines: list, string_id: int, addressee: int, speaker: int):
    item_id = len(scene_lines) * 256
    scene_dialogue_line = {
        "$type": "scnscreenplayDialogLine",
        "addressee": {"$type": "scnActorId", "id": addressee},
        "femaleLipsyncAnimationName": {
            "$type": "CName",
            "$storage": "string",
            "$value": "",
        },
        "itemId": {"$type": "scnscreenplayItemId", "id": item_id},
        "locstringId": {"$type": "scnlocLocstringId", "ruid": str(string_id)},
        "maleLipsyncAnimationName": {
            "$type": "CName",
            "$storage": "string",
            "$value": "",
        },
        "speaker": {"$type": "scnActorId", "id": speaker},
        "usage": {
            "$type": "scnscreenplayLineUsage",
            "playerGenderMask": {"$type": "scnGenderMask", "mask": 3},
        },
    }
    scene_lines.append(scene_dialogue_line)
    return item_id


def resolve_actor(name: str) -> int:
    key = name.lower()
    if key not in speaker_to_id:
        raise ValueError(f"Unknown actor: {name}")
    return speaker_to_id[key]


def choice_option(optional_choice: bool, item_id: int, caption: str):
    return {
        "$type": "scnChoiceNodeOption",
        "blueline": 0,
        "bluelineCondition": None,
        "caption": {
            "$type": "CName",
            "$storage": "string",
            "$value": caption,
        },
        "emphasisCondition": None,
        "exDataFlags": 0,
        "gameplayAction": {
            "$type": "TweakDBID",
            "$storage": "uint64",
            "$value": "0",
        },
        "iconCondition": None,
        "iconTagIds": [],
        "isFixedAsRead": 0,
        "isSingleChoice": 1 if optional_choice else 0,
        "mappinReferencePointId": {
            "$type": "scnReferencePointId",
            "id": 4294967295,
        },
        "questCondition": None,
        "screenplayOptionId": {"$type": "scnscreenplayItemId", "id": item_id},
        "timedCondition": None,
        "timedParams": None,
        "triggerCondition": None,
        "type": {
            "$type": "gameinteractionsChoiceTypeWrapper",
            "properties": 1,
        },
    }


def choice_output(node_id: int, index: int):
    return {
        "$type": "scnOutputSocket",
        "destinations": [
            {
                "$type": "scnInputSocketId",
                "isockStamp": {
                    "$type": "scnInputSocketStamp",
                    "name": 0,
                    "ordinal": 0,
                },
                "nodeId": {"$type": "scnNodeId", "id": node_id},
            }
        ],
        "stamp": {"$type": "scnOutputSocketStamp", "name": 0, "ordinal": index},
    }


def choice_node(handle_id: int, node_id: int, actor_id: int):
    return {
        "HandleId": str(handle_id),
        "Data": {
            "$type": "scnChoiceNode",
            "alwaysUseBrainGender": 0,
            "ataParams": {
                "$type": "scnChoiceNodeNsAttachToActorParams",
                "actorId": {"$type": "scnActorId", "id": actor_id},
                "visualizerStyle": "onScreen",
            },
            "atgoParams": {
                "$type": "scnChoiceNodeNsAttachToGameObjectParams",
                "nodeRef": {"$type": "NodeRef", "$storage": "uint64", "$value": "0"},
                "visualizerStyle": "inWorld",
            },
            "atpParams": {
                "$type": "scnChoiceNodeNsAttachToPropParams",
                "propId": {"$type": "scnPropId", "id": 4294967295},
                "visualizerStyle": "inWorld",
            },
            "atsParams": {"$type": "scnChoiceNodeNsAttachToScreenParams"},
            "atwParams": {
                "$type": "scnChoiceNodeNsAttachToWorldParams",
                "customEntityRadius": 0,
                "entityOrientation": {
                    "$type": "Quaternion",
                    "i": 0,
                    "j": 0,
                    "k": 0,
                    "r": 1,
                },
                "entityPosition": {"$type": "Vector3", "X": 0, "Y": 0, "Z": 0},
                "visualizerStyle": "onScreen",
            },
            "choiceFlags": "0",
            "choiceGroup": {"$type": "CName", "$storage": "string", "$value": "None"},
            "choicePriority": 0,
            "cpoHoldInputActionSection": 0,
            "customPersistentLine": {"$type": "scnscreenplayItemId", "id": 4294967040},
            "displayNameOverride": "",
            "doNotTurnOffPreventionSystem": 0,
            "ffStrategy": "automatic",
            "forceAttachToScreenCondition": None,
            "hubPriority": 0,
            "interruptCapability": "Interruptable",
            "interruptionSpeakerOverride": {"$type": "scnActorId", "id": 4294967295},
            "localizedDisplayNameOverride": {"unk1": "0", "value": ""},
            "lookAtParams": {
                "HandleId": str(handle_id + 1),
                "Data": {
                    "$type": "scnChoiceNodeNsAdaptiveLookAtParams",
                    "auxiliaryRelativePoint": {
                        "$type": "Vector3",
                        "X": 0,
                        "Y": 0,
                        "Z": 0,
                    },
                    "blendLimit": 0.300000012,
                    "distantSlotName": {
                        "$type": "CName",
                        "$storage": "string",
                        "$value": "Chest",
                    },
                    "nearbySlotName": {
                        "$type": "CName",
                        "$storage": "string",
                        "$value": "Head",
                    },
                    "referencePointFullEffectAngle": 0,
                    "referencePointFullEffectDistance": 5,
                    "referencePointNoEffectAngle": 63,
                    "referencePointNoEffectDistance": 0,
                    "referencePoints": [],
                },
            },
            "mappinParams": {
                "HandleId": str(handle_id + 2),
                "Data": {
                    "$type": "scnChoiceNodeNsMappinParams",
                    "locationType": "Nameplate",
                    "mappinSettings": {
                        "$type": "TweakDBID",
                        "$storage": "string",
                        "$value": "MappinUISettings.SceneDialogNPCSettings",
                    },
                },
            },
            "mode": "attachToActor",
            "nodeId": {"$type": "scnNodeId", "id": node_id},
            "options": [],
            "outputSockets": [],
            "persistentLineEvents": [
                {"$type": "scnSceneEventId", "id": "2001149651622965320"},
                {"$type": "scnSceneEventId", "id": "2001149651622965316"},
            ],
            "reminderCondition": None,
            "reminderParams": {
                "HandleId": str(handle_id + 3),
                "Data": {
                    "$type": "scnChoiceNodeNsActorReminderParams",
                    "cutReminderEnabled": 0,
                    "reminderActor": {"$type": "scnActorId", "id": actor_id},
                    "useCustomReminder": 0,
                    "waitTimeForLooping": {"$type": "scnSceneTime", "stu": 60000},
                    "waitTimeForReminderA": {"$type": "scnSceneTime", "stu": 10000},
                    "waitTimeForReminderB": {"$type": "scnSceneTime", "stu": 20000},
                    "waitTimeForReminderC": {"$type": "scnSceneTime", "stu": 30000},
                    "waitTimeToCutReminder": 0,
                },
            },
            "shapeParams": {
                "HandleId": str(handle_id + 4),
                "Data": {
                    "$type": "scnInteractionShapeParams",
                    "activationBaseLength": 1,
                    "activationHeight": 3,
                    "activationYawLimit": 360,
                    "customActivationRange": 0,
                    "customIndicationRange": 0,
                    "offset": {"$type": "Vector3", "X": 0, "Y": 0, "Z": 0},
                    "preset": "normal",
                    "rotation": {"$type": "Quaternion", "i": 0, "j": 0, "k": 0, "r": 1},
                },
            },
            "timedParams": None,
            "timedSectionCondition": None,
        },
    }


def add_section_node(
    graph: list,
    line_events: list[dict] | dict,
    tail_padding_ms: int = 150,
):
    if not isinstance(line_events, list):
        line_events = [line_events]

    handle_ids = [int(x["HandleId"]) for x in graph if "HandleId" in x]
    node_ids = [
        int(x["Data"]["nodeId"]["id"])
        for x in graph
        if "Data" in x and "nodeId" in x["Data"]
    ]
    handle_id = (max(handle_ids) + 4) if handle_ids else 1
    node_id = (max(node_ids) + 1) if node_ids else 1

    total_duration = sum(event["duration"] for event in line_events) + sum(
        event["gap"] for event in line_events
    )
    section_duration = total_duration + tail_padding_ms

    scene_node = {
        "HandleId": str(handle_id),
        "Data": {
            "$type": "scnSectionNode",
            "actorBehaviors": [
                {
                    "$type": "scnSectionInternalsActorBehavior",
                    "actorId": {"$type": "scnActorId", "id": 0},
                    "behaviorMode": "OnlyIfAlive",
                },
                {
                    "$type": "scnSectionInternalsActorBehavior",
                    "actorId": {"$type": "scnActorId", "id": 1},
                    "behaviorMode": "OnlyIfAlive",
                },
            ],
            "events": [],
            "ffStrategy": "automatic",
            "isFocusClue": 0,
            "nodeId": {"$type": "scnNodeId", "id": node_id},
            "outputSockets": [
                {
                    "$type": "scnOutputSocket",
                    "destinations": [],
                    "stamp": {"$type": "scnOutputSocketStamp", "name": 0, "ordinal": 0},
                },
                {
                    "$type": "scnOutputSocket",
                    "destinations": [],
                    "stamp": {"$type": "scnOutputSocketStamp", "name": 1, "ordinal": 0},
                },
            ],
            "sectionDuration": {"$type": "scnSceneTime", "stu": section_duration},
        },
    }

    for line_event in line_events:
        handle_id += 1
        scene_node["Data"]["events"].append(
            {
                "HandleId": str(handle_id),
                "Data": {
                    "$type": "scnDialogLineEvent",
                    "additionalSpeakers": {
                        "$type": "scnAdditionalSpeakers",
                        "executionTag": 0,
                        "role": "Full",
                        "speakers": [],
                    },
                    "duration": line_event["duration"],
                    "executionTagFlags": 0,
                    "id": {"$type": "scnSceneEventId", "id": "9223372036854775807"},
                    "scalingData": None,
                    "screenplayLineId": {
                        "$type": "scnscreenplayItemId",
                        "id": line_event["item_id"],
                    },
                    "startTime": line_event["start_time"],
                    "type": "0",
                    "visualStyle": "regular",
                    "voParams": {
                        "$type": "scnDialogLineVoParams",
                        "alwaysUseBrainGender": 0,
                        "customVoEvent": {
                            "$type": "CName",
                            "$storage": "string",
                            "$value": "None",
                        },
                        "disableHeadMovement": 0,
                        "ignoreSpeakerIncapacitation": 0,
                        "isHolocallSpeaker": 0,
                        "voContext": "Vo_Context_Quest",
                        "voExpression": "Vo_Expression_Spoken",
                    },
                },
            }
        )

    graph.append(scene_node)
    return node_id


def get_next_graph_ids(graph: list):
    handle_ids = [int(x["HandleId"]) for x in graph if "HandleId" in x]
    node_ids = [
        int(x["Data"]["nodeId"]["id"])
        for x in graph
        if "Data" in x and "nodeId" in x["Data"]
    ]
    handle_id = (max(handle_ids) + 8) if handle_ids else 1
    node_id = (max(node_ids) + 1) if node_ids else 1
    return handle_id, node_id


def get_choice_screenplay_item_id(choice_key: str) -> int:
    # add_choice() uses 2 + (len(scene_options) * 256)
    # Since options are appended in choice_lines insertion order,
    # derive the same ID here from the current screenplayStore options.
    for option in scene_file["Data"]["RootChunk"]["screenplayStore"]["options"]:
        loc_ruid = option["locstringId"]["ruid"]
        if str(key_to_id(choice_key)) == str(loc_ruid):
            return int(option["itemId"]["id"])
    raise ValueError(f"Could not resolve screenplay option item id for {choice_key}")


def add_choice_graph_node(
    graph: list,
    options: list[dict],
):
    handle_id, node_id = get_next_graph_ids(graph)
    node = choice_node(handle_id=handle_id, node_id=node_id, actor_id=0)
    node["Data"]["options"] = [opt["option"] for opt in options]
    node["Data"]["outputSockets"] = [
        choice_output(node_id=opt["target_node_id"], index=i)
        for i, opt in enumerate(options)
    ]
    graph.append(node)
    return node_id

def make_audio_path(actor: str, string_id: int):
    hex_id = f"{string_id:016x}"
    return f"mod\\gq000\\localization\\en-us\\vo\\{actor}_i_{hex_id}.wem"


spoken_lines = {
    "gq000_01_patch_intro_01": {
        "speaker": "Patch",
        "addressee": "V",
        "text": "You made it. Good. Keep your voice down.",
    },
    "gq000_01_v_choice_ghostline_line": {
        "speaker": "V",
        "addressee": "Patch",
        "text": "Ghostline. Heard the name float around. Never saw the ghosts.",
    },
    "gq000_01_patch_rsp_ghostline_01": {
        "speaker": "Patch",
        "addressee": "V",
        "text": "That's the point. We're not a gang, not a brand. We listen, collect, move things nobody wants traced.",
    },
    "gq000_01_v_choice_whyyou_line": {
        "speaker": "V",
        "addressee": "Patch",
        "text": "Plenty of mercs in Night City. Why pull me in?",
    },
    "gq000_01_patch_rsp_whyyou_01": {
        "speaker": "Patch",
        "addressee": "V",
        "text": "Because you get in, get out, and don't start asking the wrong questions before the eddies clear.",
    },
    "gq000_01_v_choice_job_line": {
        "speaker": "V",
        "addressee": "Patch",
        "text": "Alright. Talk. What am I doing?",
    },
    "gq000_01_patch_rsp_job_01": {
        "speaker": "Patch",
        "addressee": "V",
        "text": "Tyger Claws are sitting on a relay that looks dead from the street. It isn't. Someone's laundering data through it.",
    },
    "gq000_01_patch_rsp_job_02": {
        "speaker": "Patch",
        "addressee": "V",
        "text": "You jack the node, pull the cache, and drop it where we tell you. Clean job, if nobody gets curious.",
    },
    "gq000_01_v_choice_client_line": {
        "speaker": "V",
        "addressee": "Patch",
        "text": "Tyger Claws don't move like that for free. Who's behind it?",
    },
    "gq000_01_patch_rsp_client_01": {
        "speaker": "Patch",
        "addressee": "V",
        "text": "Someone Arasaka-adjacent. That's all you need. You want names, ask after the job's done.",
    },
    "gq000_01_v_choice_accept_line": {
        "speaker": "V",
        "addressee": "Patch",
        "text": "Fine. Send me the coordinates. I'll get your data.",
    },
    "gq000_01_patch_rsp_accept_01": {
        "speaker": "Patch",
        "addressee": "V",
        "text": "Knew you would. Location's already queued.",
    },
    "gq000_01_patch_rsp_accept_02": {
        "speaker": "Patch",
        "addressee": "V",
        "text": "Pull the cache, use the drop point, and don't improvise unless you have to.",
    },
}

choice_lines = {
    "gq000_01_v_choice_ghostline_short": {"text": "Ghostline?"},
    "gq000_01_v_choice_whyyou_short": {"text": "Why me?"},
    "gq000_01_v_choice_job_short": {"text": "What's the job?"},
    "gq000_01_v_choice_client_short": {"text": "Who's behind it?"},
    "gq000_01_v_choice_accept_short": {"text": "I'm in."},
}

sections = {
    "opening_line": {
        "line_keys": ["gq000_01_patch_intro_01"],
    },
    "optional_branch_1": {
        "choice_key": "gq000_01_v_choice_ghostline_short",
        "line_keys": [
            "gq000_01_v_choice_ghostline_line",
            "gq000_01_patch_rsp_ghostline_01",
        ],
    },
    "optional_branch_2": {
        "choice_key": "gq000_01_v_choice_whyyou_short",
        "line_keys": [
            "gq000_01_v_choice_whyyou_line",
            "gq000_01_patch_rsp_whyyou_01",
        ],
    },
    "main_progression_choice": {
        "choice_key": "gq000_01_v_choice_job_short",
        "line_keys": [
            "gq000_01_v_choice_job_line",
            "gq000_01_patch_rsp_job_01",
            "gq000_01_patch_rsp_job_02",
        ],
    },
    "optional_followup_after_details": {
        "choice_key": "gq000_01_v_choice_client_short",
        "line_keys": [
            "gq000_01_v_choice_client_line",
            "gq000_01_patch_rsp_client_01",
        ],
    },
    "main_close_accept_choice": {
        "choice_key": "gq000_01_v_choice_accept_short",
        "line_keys": [
            "gq000_01_v_choice_accept_line",
            "gq000_01_patch_rsp_accept_01",
            "gq000_01_patch_rsp_accept_02",
        ],
    },
}

choice_groups = {
    "choice_group_intro": [
        {"choice_key": "gq000_01_v_choice_ghostline_short", "section_key": "optional_branch_1", "optional": True},
        {"choice_key": "gq000_01_v_choice_whyyou_short", "section_key": "optional_branch_2", "optional": True},
        {"choice_key": "gq000_01_v_choice_job_short", "section_key": "main_progression_choice", "optional": False},
    ],
    "choice_group_after_job": [
        {"choice_key": "gq000_01_v_choice_client_short", "section_key": "optional_followup_after_details", "optional": True},
        {"choice_key": "gq000_01_v_choice_accept_short", "section_key": "main_close_accept_choice", "optional": False},
    ],
}

validate_spoken_lines(spoken_lines)
validate_choice_lines(choice_lines)

audio_durations_ms = build_audio_timing_map(spoken_lines)

manifest = {
    "spoken_lines": [],
    "choice_lines": [],
    "audio_durations_ms": audio_durations_ms,
    "section_node_ids": {},
    "choice_node_ids": {},
}

line_item_ids = {}

for key, data in spoken_lines.items():
    string_id = key_to_id(key)
    audio_path = make_audio_path(data["speaker"].lower(), string_id)
    manifest["spoken_lines"].append(
        {
            "key": key,
            "string_id": str(string_id),
            "speaker": data["speaker"],
            "addressee": data["addressee"],
            "text": data["text"],
            "audio_path": audio_path,
            "duration_ms": audio_durations_ms[key],
        }
    )
    add_subtitle(subtitles_file, string_id, data["text"])
    add_vo(vo_file, string_id, audio_path)
    item_id = add_dialogue(
        scene_file["Data"]["RootChunk"]["screenplayStore"]["lines"],
        string_id,
        speaker_to_id[data["addressee"].lower()],
        speaker_to_id[data["speaker"].lower()],
    )
    line_item_ids[key] = item_id

for key, data in choice_lines.items():
    string_id = key_to_id(key)
    manifest["choice_lines"].append(
        {
            "key": key,
            "string_id": str(string_id),
            "text": data["text"],
        }
    )
    add_choice(
        scene_embedded=scene_file["Data"]["RootChunk"]["locStore"],
        scene_options=scene_file["Data"]["RootChunk"]["screenplayStore"]["options"],
        string_id=string_id,
        text=data["text"],
    )
   
section_node_ids = {}

for section_name, section_data in sections.items():
    start_time = 0
    line_events = []
    for key in section_data["line_keys"]:
        duration = audio_durations_ms[key]
        gap = random.randint(450, 850)
        line_events.append(
            {
                "item_id": line_item_ids[key],
                "duration": duration,
                "start_time": start_time,
                "gap": gap,
            }
        )
        start_time += duration + gap
    node_id = add_section_node(
        scene_file["Data"]["RootChunk"]["sceneGraph"]["Data"]["graph"],
        line_events,
    )
    section_node_ids[section_name] = node_id


choice_node_ids = {}

for group_name, group_options in choice_groups.items():
    built_options = []
    for group_option in group_options:
        screenplay_item_id = get_choice_screenplay_item_id(group_option["choice_key"])
        built_options.append(
            {
                "option": choice_option(
                    optional_choice=group_option["optional"],
                    item_id=screenplay_item_id,
                    caption=choice_lines[group_option["choice_key"]]["text"],
                ),
                "target_node_id": section_node_ids[group_option["section_key"]],
            }
        )
    node_id = add_choice_graph_node(
        scene_file["Data"]["RootChunk"]["sceneGraph"]["Data"]["graph"],
        built_options,
    )
    choice_node_ids[group_name] = node_id

manifest["section_node_ids"] = section_node_ids
manifest["choice_node_ids"] = choice_node_ids

write_json(mod_path / "source" / "raw" / "gq000_01_manifest.json", manifest)

write_json(
    mod_path
    / "source"
    / "raw"
    / "mod\\gq000\\localization\\en-us\\subtitles\\gq000_01.json.json",
    subtitles_file,
)

write_json(
    mod_path
    / "source"
    / "raw"
    / "mod\\gq000\\localization\\en-us\\vo\\gq000_01.json.json",
    vo_file,
)

write_json(
    mod_path / "source" / "raw" / "mod\\gq000\\scenes\\gq000_01.scene.json",
    scene_file,
)
