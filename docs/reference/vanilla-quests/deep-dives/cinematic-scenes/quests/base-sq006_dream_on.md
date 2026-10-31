# Dream On: scene presentation

Journal identity: `quests/side_quest/sq006_dream_on`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq006_dream_on.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\media\fluff\scenes\jefferson_peralez_ad\jefferson_peralez_ad.scene`

3 graph nodes, 2 edges; 1 event-bearing sections, 7 events; 7 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: jefferson_peralez (actor 0, findInContext).

Entries: `in` → 1.

Exits: `out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 7 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `5f8cd94de7ab5710ec4fe4847ea60256ec1d21ed4590aa91fbf0d3b75e8eb021`. Binary SHA-256: `be6960ae963648549f18fcb9b0061ef1f4cee0ad3a828d45c2471d88caf5e1a6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\media\fluff\scenes\jefferson_peralez_ad\jefferson_peralez_ad.scene" --events
```

## `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_02_guards.scene`

9 graph nodes, 9 edges; 2 event-bearing sections, 11 events; 11 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: GuardRoom (actor 0, findInWorld); GuardCor (actor 1, findInWorld); GuardStairs (actor 2, findInWorld); Roof (actor 3, findInWorld); Tyger_Claw_Ganger (actor 4, findInWorld); Player (actor 5, findInContext).

Entries: `FluffEntrance` → 10; `GuardRoom` → 6.

Exits: `End1` → 37; `FluffEntranceEnd` → 30.

End nodes: 30: `<omitted>`; 37: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 11 | 7 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `af15546237b06c042c8c1bad462c4a0d22e2d8afc9b621368844ecc904d12bf4`. Binary SHA-256: `8585197745877c57d95d456054c9dcf2ba97881e07e8b5bf277b0a3037c169d0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_02_guards.scene" --events
```

## `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_04_tobias.scene`

25 graph nodes, 26 edges; 2 event-bearing sections, 10 events; 2 screenplay lines, 3 screenplay options, 3 choice nodes.

Actors: 8ug8ear (actor 0, findInWorld); Johnny (actor 1, findInWorld); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `Start_throw` → 26.

Exits: `signal release` → 94; `End_cooled` → 2; `End_throw` → 27; `ChoiceHub` → 65.

End nodes: 2: `NonTerminating`; 27: `<omitted>`; 65: `<omitted>`; 94: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 3 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnChangeIdleAnimEvent` | 1 | 79 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnDialogLineEvent` | 1 | 3 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnPlaySkAnimEvent` | 3 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsAttachPropToNode` | 1 | 3 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scneventsAttachPropToPerformer` | 1 | 3 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsSocket` | 2 | 3 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, props_equipment, audio, socket_signal: 1
- idle_animation, socket_signal: 1

Raw SHA-256: `0f97288026803c745dd82c898b769682a8a09d7a19c62cbcdf8732713775980a`. Binary SHA-256: `de518cad7837988270c5a1ad9a4c786edf38b55f15ad4baee0337d0990b784e5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_04_tobias.scene" --events
```

## `base\quest\side_quests\sq006\scenes\sq006_00a_phonecall.scene`

41 graph nodes, 40 edges; 6 event-bearing sections, 23 events; 21 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: jefferson (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `sq006_00a_jeff_return_call_IN` → 61; `sq006_00a_jeff_calls_IN` → 31.

Exits: `sq006_00a_callback_no_OUT` → 82; `sq006_00a_jeffcalls_accept_OUT` → 49; `sq006_00a_jeffcalls_later_OUT` → 53; `sq006_00a_callback_yes_OUT` → 76.

End nodes: 49: `<omitted>`; 53: `<omitted>`; 76: `<omitted>`; 82: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 21 | 42 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsSocket` | 2 | 42 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- speech, socket_signal: 2

Raw SHA-256: `71e46af9a2f358297bc7dff194c744ad40f4e2bdb773de527b55c4bc84b39ea3`. Binary SHA-256: `f65388a0dbe9af7b96154063be298048c85409602ba10d62fd69af9474a03e78`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq006\scenes\sq006_00a_phonecall.scene" --events
```

## `base\quest\side_quests\sq006\scenes\sq006_01a_apartment_welcome.scene`

288 graph nodes, 344 edges; 44 event-bearing sections, 602 events; 131 screenplay lines, 22 screenplay options, 6 choice nodes.

Actors: jefferson (actor 0, spawnSet); elizabeth (actor 1, spawnSet); elizabeth_vo (actor 2, spawnDespawn); V (actor 3, findInContext).

Entries: `sq006_01a_eliz_introduction_in` → 6; `sq006_01a_meet_the_family_in` → 11; `JeffPhone_in` → 68; `preview` → 550; `sq006_01a_intercom_in` → 149.

Exits: `sq006_01a_meet_the_family_out` → 12; `sq006_01a_intercom_out_new` → 2793; `sq006_01a_intercom_out` → 151.

End nodes: 12: `NonTerminating`; 151: `<omitted>`; 2793: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 12 | 8 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 117 | 8 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnGameplayTransitionEvent` | 3 | 8 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/17` |
| `scnIKEvent` | 6 | 8 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/11` |
| `scnLookAtEvent` | 156 | 8 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 135 | 8 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPoseCorrectionEvent` | 6 | 199 / 175 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/11` |
| `scnUnmountEvent` | 3 | 8 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/16` |
| `scneventsCameraParamsEvent` | 5 | 226 / 553 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/16` |
| `scneventsSetAnimFeatureEvent` | 3 | 8 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/15` |
| `scneventsSocket` | 156 | 8 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 14
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze: 4
- skeletal_animation, gaze: 4
- speech, gaze, socket_signal: 3
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, socket_signal: 2
- camera: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, camera, socket_signal: 1
- skeletal_animation: 1
- socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1

Raw SHA-256: `32166d805e9d78a9f2342380009710879e1edccc9770e8423d0204e63c0fbce3`. Binary SHA-256: `d5345b83c2d05ebb3ee65f7dc49f97f965c0465202ba82a2d213294ca8656af0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq006\scenes\sq006_01a_apartment_welcome.scene" --events
```

## `base\quest\side_quests\sq006\scenes\sq006_02a_tour.scene`

83 graph nodes, 92 edges; 16 event-bearing sections, 108 events; 40 screenplay lines, 5 screenplay options, 3 choice nodes.

Actors: elizabeth (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `sq006_02a_tour_begin_in` → 1; `sq006_02a_tour_hall_in` → 89; `sq006_02a_tour_chat_01_in` → 18; `sq006_02a_tour_chat_02_in` → 23; `sq006_02a_tour_chat_03_in` → 30; `sq006_02a_tour_bedroom_in` → 33; `sq006_02a_going_to_roof_IN` → 108; `sq006_02a_tour_main_office_in` → 38; `sq006_2a_tour_security_office_in` → 46; `sq006_02a_tour_ask_poster_in` → 139.

Exits: `sq006_02a_tour_begin_out` → 2; `sq006_02a_tour_hall_out` → 90; `sq006_02a_tour_chat_01_out` → 19; `sq006_02a_tour_chat_02_out` → 24; `sq006_02a_tour_chat_03_out` → 29; `sq006_02a_going_to_roof_OUT` → 109; `sq006_02a_tour_bedroom_out` → 35; `sq006_02a_tour_main_office_out` → 43; `sq006_2a_tour_security_office_out` → 48; `sq006_02a_tour_ask_poster_out` → 140.

End nodes: 2: `NonTerminating`; 19: `<omitted>`; 24: `<omitted>`; 29: `<omitted>`; 35: `<omitted>`; 43: `<omitted>`; 48: `<omitted>`; 90: `<omitted>`; 109: `<omitted>`; 140: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 38 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 9 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scnIKEvent` | 4 | 9 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnLookAtEvent` | 22 | 3 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 21 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 2 | 9 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 2 | 9 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/9` |
| `scneventsSocket` | 17 | 3 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation: 1

Raw SHA-256: `ce9fa25083f9b64861c4861eaa181a33d2c215420c650fd473db1b674c4898d4`. Binary SHA-256: `884214df9c014a2795a0b5206c314ea90fb8f8b973529ef45491cf40f848c4af`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq006\scenes\sq006_02a_tour.scene" --events
```

## `base\quest\side_quests\sq006\scenes\sq006_02b_investigation.scene`

342 graph nodes, 439 edges; 46 event-bearing sections, 259 events; 103 screenplay lines, 24 screenplay options, 22 choice nodes.

Actors: elizabeth (actor 0, spawnSet); johnny (actor 1, spawnDespawn); V (actor 2, findInContext).

Entries: `sq006_02b_hidden_room_rem_to` → 1130; `START` → 1837; `sq006_02b_wires_follow_start` → 1147; `sq006_02b_move_furniture_IN` → 880; `Start 28` → 1967; `sq006_02b_investigation_begin` → 253; `Start 26` → 1357; `sq006_elizabeth360_in` → 1753.

Exits: `sq006_elizabeth360_out` → 1779.

End nodes: 1779: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 355 / 288 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/3` |
| `scnChangeIdleAnimEvent` | 4 | 362 / 348 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/7` |
| `scnDialogLineEvent` | 94 | 258 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 362 / 358 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/16` |
| `scnIKEvent` | 2 | 362 / 344 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/3` |
| `scnLookAtEvent` | 49 | 258 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlaySkAnimEvent` | 56 | 258 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnUnmountEvent` | 1 | 362 / 357 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/15` |
| `scneventsEquipItemToPerformer` | 2 | 827 / 1155 | `/Data/RootChunk/sceneGraph/Data/graph/131/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 1 | 362 / 355 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/14` |
| `scneventsSocket` | 39 | 258 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 827 / 1158 | `/Data/RootChunk/sceneGraph/Data/graph/131/Data/events/6` |
| `scneventsVFXEvent` | 7 | 355 / 289 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 10
- speech: 10
- speech, skeletal_animation: 6
- speech, skeletal_animation, gaze: 5
- skeletal_animation: 5
- speech, skeletal_animation, socket_signal: 3
- speech, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, props_equipment, vfx, socket_signal: 1
- socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `ea47961ed119c2b6ed10a8348d232cbbb975a77ff532ca2b9c63fa82079068b0`. Binary SHA-256: `5f477f1bec02d8ab6ec736d23c5fd54e29ad13f9be5770cc9d02cb97b06814bd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq006\scenes\sq006_02b_investigation.scene" --events
```

## `base\quest\side_quests\sq006\scenes\sq006_02c_conclusion.scene`

25 graph nodes, 25 edges; 6 event-bearing sections, 48 events; 17 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: elizabeth (actor 0, spawnSet); johnny (actor 1, spawnDespawn); V (actor 2, findInContext).

Entries: `sq006_02c_conclusion_in` → 1; `sq006_2c_talk_to_eliz_in` → 6.

Exits: `sq006_02c_conclusion_out` → 3; `sq006_2c_talk_to_eliz_out` → 7.

End nodes: 3: `<omitted>`; 7: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 8 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnDialogLineEvent` | 17 | 2 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnLookAtEvent` | 12 | 8 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scnPlaySkAnimEvent` | 4 | 8 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scneventsSocket` | 13 | 8 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze, socket_signal: 2
- speech: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `8eec6cb58c0b6a78735a23002c85cdf9bbadf423292ddd31e3f37c0f963996d3`. Binary SHA-256: `a351cf5368f0243eebc6c9f48b4715061c2d1f3ccc4fe18b22edd0ac6e096cfa`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq006\scenes\sq006_02c_conclusion.scene" --events
```

## `base\quest\side_quests\sq006\scenes\sq006_04a_secret_lab.scene`

133 graph nodes, 136 edges; 18 event-bearing sections, 83 events; 48 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); maelstrom_boss (actor 1, community); pilot (actor 2, community); copilot (actor 3, community); truck (actor 4, community); stealth_AV (actor 5, community); V (actor 6, findInContext).

Entries: `sq006_04a_braindance_unit_in` → 6; `sq006_04a_brainscans_ambush_in` → 11; `sq006_04a_suspicious_truck_in` → 16; `sq006_04a_truck_scanned_in` → 21; `sq006_04a_losing_them_in` → 37; `sq006_04c_truck_moving_in` → 48; `aq006_04a_ambush_gate_IN` → 3700; `sq006_04a_brainscans_attack_in` → 79; `sq006_04a_get_a_car_IN` → 89; `sq006_dont_use_in` → 225; `sq006_04a_ambush_shout_IN` → 94; `chase_start_in` → 103; `chase_2_in` → 107; `truck_down_in` → 111; `sq006_04a_ambush_near_IN` → 117; `sq006_04a_soldiers_depart_IN` → 124; `sq006_04a_mount_johnny_IN` → 268.

Exits: `sq006_04a_mount_johnny00_OUT` → 3915; `sq006_04a_braindance_unit_out` → 7; `sq006_04a_brainscans_out` → 13; `sq006_04a_suspicious_truck_out` → 17; `sq006_04a_truck_scanned_out` → 22; `sq006_04a_losing_them_out` → 38; `aq006_04a_ambush_gate_OUT` → 3701; `sq006_04a_get_a_car_OUT` → 90; `sq006_dont_use_out` → 226; `sq006_04a_ambush_shout_OUT` → 95; `chase_start_out` → 105; `chase_2_out` → 109; `truck_down_out` → 113; `sq006_04a_ambush_near_OUT` → 118.

End nodes: 7: `<omitted>`; 13: `<omitted>`; 17: `<omitted>`; 22: `<omitted>`; 38: `<omitted>`; 90: `<omitted>`; 95: `<omitted>`; 105: `<omitted>`; 109: `<omitted>`; 113: `<omitted>`; 118: `<omitted>`; 226: `<omitted>`; 3701: `<omitted>`; 3915: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 12 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 43 | 12 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnGameplayActionEvent` | 1 | 3871 / 577 | `/Data/RootChunk/sceneGraph/Data/graph/117/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 30 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/23` |
| `scnIKEvent` | 3 | 30 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/15` |
| `scnLookAtEvent` | 12 | 12 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnPlaySkAnimEvent` | 9 | 12 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 1 | 30 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/22` |
| `scneventsSetAnimFeatureEvent` | 2 | 12 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scneventsSocket` | 7 | 12 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 12
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, ik: 1
- skeletal_animation, idle_animation: 1
- idle_animation, gameplay_action: 1

Raw SHA-256: `2ac6d927a28fc7c9d53a4833a60486382f5c0729a3d00849a90159636a1c91c8`. Binary SHA-256: `eebc65e42d1f2bf2a0b64d32515ce0b710fcc65b5a0c0f2bd7eb54e3e1a7f700`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq006\scenes\sq006_04a_secret_lab.scene" --events
```

## `base\quest\side_quests\sq006\scenes\sq006_05a_phonecalls.scene`

68 graph nodes, 71 edges; 12 event-bearing sections, 56 events; 42 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: elizabeth (actor 0, spawnSet); conspirator (actor 1, findInContext); jefferson (actor 2, spawnSet); V (actor 3, findInContext).

Entries: `sq006_05a_phone_call_in` → 1; `sq006_05a_phonecalls_call_jefferson_IN` → 88; `sq006_05a_failed_in` → 23; `sq006_05a_conspiracy_warning_in` → 38.

Exits: `sq006_05a_phone_call_out` → 2; `sq006_05a_phonecalls_call_jefferson_OUT` → 89; `sq006_05a_failed_out` → 24; `sq006_05a_conspiracy_warning_out` → 39.

End nodes: 2: `<omitted>`; 24: `<omitted>`; 39: `<omitted>`; 89: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 42 | 3 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 3 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 3 | 40 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |
| `scneventsSocket` | 6 | 3 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 2 | 40 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, socket_signal: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, gaze: 1

Raw SHA-256: `6d642a0b132bcff8e398df3bbd4ea50a1a28ecfccce194c93c98c577f0d616c7`. Binary SHA-256: `f7edae22b38cecb5413cf0e0a443d187f37737f070ba9ab0780ee841b79884f3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq006\scenes\sq006_05a_phonecalls.scene" --events
```

## `base\quest\side_quests\sq006\scenes\sq006_06a_clandestine.scene`

177 graph nodes, 214 edges; 41 event-bearing sections, 440 events; 122 screenplay lines, 22 screenplay options, 11 choice nodes.

Actors: elizabeth (actor 0, spawnSet); ramen_cook (actor 1, findInWorld); Johnny (actor 2, spawnDespawn); V (actor 3, findInContext).

Entries: `sq006_05a_clandestine_meeting_in` → 1; `sq006_05a_johnny_talk_in` → 13.

Exits: `sq006_05a_clandestine_meeting_out` → 2; `sq006_05a_johnny_talk_out` → 14.

End nodes: 2: `NonTerminating`; 14: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 11 | 36 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scnDialogLineEvent` | 113 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 90 / 440 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/20` |
| `scnIKEvent` | 2 | 90 / 428 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/9` |
| `scnLookAtEvent` | 112 | 3 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 93 | 3 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPoseCorrectionEvent` | 2 | 90 / 433 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/14` |
| `scnUnmountEvent` | 1 | 90 / 439 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/19` |
| `scneventsAttachPropToWorld` | 1 | 125 / 592 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/4` |
| `scneventsCameraParamsEvent` | 8 | 90 / 432 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 1 | 90 / 435 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/16` |
| `scneventsSocket` | 95 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 20
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, gaze: 4
- camera: 4
- skeletal_animation, camera, socket_signal: 3
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- gaze: 1

Raw SHA-256: `cdc978cb4c7a0b59fe99a1924fa99cd02c24f0db5d35e2494cf62302e36f4c31`. Binary SHA-256: `a9a98fa67ce3197a098ab910ccce3f7c15ef43faf7835131b3c402540ef086bd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq006\scenes\sq006_06a_clandestine.scene" --events
```

## `base\quest\side_quests\sq006\scenes\sq006_07a_final_choice.scene`

185 graph nodes, 247 edges; 49 event-bearing sections, 428 events; 128 screenplay lines, 22 screenplay options, 10 choice nodes.

Actors: jefferson (actor 0, spawnSet); elizabeth (actor 1, spawnSet); johnny (actor 2, spawnDespawn); V (actor 3, findInContext).

Entries: `sq006_07a_final_meeting_in` → 6; `Start 6` → 454; `Start 7` → 4821.

Exits: `sq006_07a_final_meeting_end` → 15.

End nodes: 15: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 27 | 90 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scnDialogLineEvent` | 108 | 82 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 2 | 105 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/26` |
| `scnIKEvent` | 4 | 105 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/13` |
| `scnLookAtEvent` | 110 | 82 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 68 | 82 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPoseCorrectionEvent` | 3 | 105 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/21` |
| `scnUnmountEvent` | 2 | 105 / 157 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/25` |
| `scneventsAttachPropToPerformer` | 1 | 176 / 442 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/5` |
| `scneventsAttachPropToWorld` | 1 | 105 / 147 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/16` |
| `scneventsCameraParamsEvent` | 9 | 105 / 150 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/19` |
| `scneventsSetAnimFeatureEvent` | 2 | 105 / 153 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/22` |
| `scneventsSocket` | 90 | 82 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 1 | 221 / 617 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 14
- speech, skeletal_animation, gaze, socket_signal: 8
- gaze: 7
- camera: 6
- skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, camera, socket_signal: 1
- skeletal_animation: 1

Raw SHA-256: `aae1942da1114fa35bead18b21aec80faa89c1a0fde05b94316284ef60ebe130`. Binary SHA-256: `3526a1624191f8acf79b5034371163dd9f50baa425a6d4be6addaac33fe7db24`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq006\scenes\sq006_07a_final_choice.scene" --events
```

## `base\quest\tertiary_characters\default_dialogues\elizabeth_peralez_default.scene`

22 graph nodes, 26 edges; 8 event-bearing sections, 48 events; 31 screenplay lines, 5 screenplay options, 1 choice nodes.

Actors: Elizabeth_Peralez (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `in` → 1.

Exits: `out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 41 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 31 | 12 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnLookAtEvent` | 1 | 12 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 9 | 12 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation: 4
- speech: 2
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation: 1

Raw SHA-256: `035b1657793612e0c9a35dbf4482526991de566d7240b728d91af5f36ec82af4`. Binary SHA-256: `e09087cf91510a164e76e540a7adf90229148accb3ade07941afeee9d075d814`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\tertiary_characters\default_dialogues\elizabeth_peralez_default.scene" --events
```

