# I Fought the Law: scene presentation

Journal identity: `quests/side_quest/sq012_lost_girl`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq012_lost_girl.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

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

## `base\quest\side_quests\sq012\scenes\sq012_00_phonecalls.scene`

116 graph nodes, 146 edges; 20 event-bearing sections, 69 events; 45 screenplay lines, 10 screenplay options, 4 choice nodes.

Actors: elizabeth (actor 0, spawnSet); sobchak (actor 1, spawnSet); V (actor 2, findInContext).

Entries: `sq012_00_elizabeth_offers_job_in` → 1; `liz_holo_preview` → 246; `river_holo_preview` → 259; `sq012_river_call_in` → 28; `sq012_00_elizabeth_ready_to_report_in` → 53; `sq012_00_callback_IN` → 89.

Exits: `sq012_00_elizabeth_offers_job_accept_out` → 2; `sq012_river_call_out` → 30; `sq012_00_elizabeth_ready_to_report_out` → 54; `sq012_00_elizabeth_offers_job_reject_out` → 80.

End nodes: 2: `<omitted>`; 30: `<omitted>`; 54: `<omitted>`; 80: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 4. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 9 | 50 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnDialogLineEvent` | 41 | 11 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 2 | 227 / 204 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/1` |
| `scnPlaySkAnimEvent` | 12 | 11 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsCameraEvent` | 2 | 248 / 207 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/0` |
| `scneventsCameraParamsEvent` | 2 | 11 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 1 | 146 / 157 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 7
- speech, idle_animation: 4
- speech, skeletal_animation, idle_animation: 2
- idle_animation, gaze: 2
- camera: 2
- speech, skeletal_animation, camera: 1
- speech: 1
- speech, idle_animation, socket_signal: 1

Raw SHA-256: `7eb2d3f6e3410c76b7f4bbcdff0b9791c49c4badadfd314c0ee629cff8758b16`. Binary SHA-256: `4c923ad391529ed9bffe84ee21abab972a4389cd00b09141e51dd4c279aef4fd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq012\scenes\sq012_00_phonecalls.scene" --events
```

## `base\quest\side_quests\sq012\scenes\sq012_01a_peralez_car.scene`

178 graph nodes, 213 edges; 24 event-bearing sections, 351 events; 68 screenplay lines, 17 screenplay options, 7 choice nodes.

Actors: elizabeth (actor 0, spawnSet); jefferson (actor 1, spawnSet); driver (actor 2, community); peralez_car (actor 3, community); V (actor 4, findInContext).

Entries: `sq012_01a_peralez_car_in` → 1; `Start1` → 507; `sq012_wait_for_peralez_in` → 173; `sq012_peralez_car_prev` → 521.

Exits: `sq012_01a_into_BD_out` → 19; `sq012_wait_for_peralez_out` → 174; `sq012_timelapse_end_to_spawn` → 201; `sq012_01a_time_delay_msg` → 553.

End nodes: 19: `NonTerminating`; 174: `<omitted>`; 201: `NonTerminating`; 553: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 6 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnChangeIdleAnimEvent` | 11 | 6 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnDialogLineEvent` | 52 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayActionEvent` | 1 | 142 / 693 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/4` |
| `scnGameplayTransitionEvent` | 1 | 191 / 814 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/6` |
| `scnIKEvent` | 2 | 191 / 808 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/1` |
| `scnLookAtAdvancedEvent` | 2 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnLookAtEvent` | 43 | 6 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 15 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/29` |
| `scnPlaySkAnimEvent` | 81 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPoseCorrectionEvent` | 2 | 6 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |
| `scnUnmountEvent` | 1 | 191 / 813 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/5` |
| `scneventsAttachPropToPerformer` | 5 | 15 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/10` |
| `scneventsAttachPropToWorld` | 1 | 15 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/28` |
| `scneventsCameraParamsEvent` | 1 | 15 / 106 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/24` |
| `scneventsSetAnimFeatureEvent` | 49 | 6 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSocket` | 88 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scneventsVFXEvent` | 3 | 15 / 102 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/20` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal, animation_state: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 4
- gaze: 3
- speech: 2
- speech, skeletal_animation, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `4cc8051529898f01d9ed30ba159771f58448b778632a64c29419b2884ae0d34a`. Binary SHA-256: `6e12ea574d17e31fed1a4f9fff177c3f8349efce2895341489f885e768e21ade`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq012\scenes\sq012_01a_peralez_car.scene" --events
```

## `base\quest\side_quests\sq012\scenes\sq012_02a_braindance.scene`

151 graph nodes, 170 edges; 10 event-bearing sections, 165 events; 58 screenplay lines, 8 screenplay options, 0 choice nodes.

Actors: Lucius_Rhyne (actor 0, community); Lark (actor 1, spawnDespawn); Lucas (actor 2, community); Gate_Security (actor 3, community); Holt (actor 4, community); River_Ward (actor 5, spawnDespawn); Cyberpsycho (actor 6, community); Johnny (actor 7, spawnDespawn); bd_replacer (actor 8, spawnSet); Player (actor 9, findInContext).

Entries: `sq012_braindance_DEBUG_in` → 1; `bd_only_prev` → 1652.

Exits: `sq012_braindance_DEBUG_out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioDurationEvent` | 18 | 20 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/50` |
| `scnDialogLineEvent` | 46 | 20 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/21` |
| `scnGameplayTransitionEvent` | 1 | 56 / 316 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/22` |
| `scnIKEvent` | 2 | 56 / 305 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/14` |
| `scnLookAtEvent` | 3 | 56 / 284 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/2` |
| `scnPlayRidAnimEvent` | 24 | 20 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 29 | 20 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnUnmountEvent` | 1 | 56 / 315 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/21` |
| `scneventsAttachPropToPerformer` | 3 | 20 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsAttachPropToWorld` | 1 | 56 / 298 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/11` |
| `scneventsBraindanceVisibilityEvent` | 2 | 20 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/18` |
| `scneventsClueEvent` | 6 | 20 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/24` |
| `scneventsEquipItemToPerformer` | 1 | 56 / 287 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/5` |
| `scneventsPlayRidCameraAnimEvent` | 3 | 20 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/17` |
| `scneventsSetAnimFeatureEvent` | 1 | 56 / 311 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/18` |
| `scneventsSocket` | 9 | 20 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 1 | 56 / 297 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/10` |
| `scneventsVFXBraindanceEvent` | 10 | 20 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/52` |
| `scneventsVFXEvent` | 4 | 20 / 204 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/99` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, skeletal_animation, rid_actor, camera, rid_camera, props_equipment, audio, vfx, socket_signal, clues, bd_visibility_ui: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx: 1

Raw SHA-256: `c9762a77575d4b6c2e34e300ba402603154ad632db77d74479745cc069014116`. Binary SHA-256: `b633d02d2fa77169a2f32daa25066e24b897e427f3b87f6a667fb5ad1b3ed2fe`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq012\scenes\sq012_02a_braindance.scene" --events
```

## `base\quest\side_quests\sq012\scenes\sq012_03a_av_pad.scene`

150 graph nodes, 165 edges; 23 event-bearing sections, 240 events; 45 screenplay lines, 11 screenplay options, 4 choice nodes.

Actors: elizabeth (actor 0, spawnSet); jefferson (actor 1, spawnSet); driver (actor 2, community); peralez_car (actor 3, community); peralez_av (actor 4, community); V (actor 5, findInContext).

Entries: `sq012_03a_wake_up_in` → 1; `av_takeoff_prev` → 412; `sq12_03_braindance_ended_in` → 82; `wakeup_test` → 89; `Start 3` → 298; `Start1` → 505.

Exits: `driver_departs_out` → 510; `sq012_03a_wake_up_out` → 2; `out` → 250; `sq12_03_braindance_ended_out` → 85.

End nodes: 2: `NonTerminating`; 85: `NonTerminating`; 250: `<omitted>`; 510: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 8 | 43 / 210 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/21` |
| `scnChangeIdleAnimEvent` | 16 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 33 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayActionEvent` | 3 | 43 / 190 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/13` |
| `scnGameplayTransitionEvent` | 2 | 104 / 384 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/9` |
| `scnIKEvent` | 4 | 104 / 377 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/3` |
| `scnLookAtEvent` | 54 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 37 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnUnmountEvent` | 2 | 104 / 383 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/8` |
| `scneventsAttachPropToPerformer` | 4 | 64 / 273 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/0` |
| `scneventsAttachPropToWorld` | 3 | 64 / 302 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/11` |
| `scneventsEquipItemToPerformer` | 2 | 43 / 194 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/15` |
| `scneventsSetAnimFeatureEvent` | 4 | 64 / 276 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/2` |
| `scneventsSocket` | 61 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 1 | 43 / 216 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/25` |
| `scneventsVFXDurationEvent` | 1 | 245 / 537 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/2` |
| `scneventsVFXEvent` | 5 | 43 / 189 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/12` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- gaze: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, gameplay_action: 1
- speech, skeletal_animation: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- idle_animation, props_equipment, vfx, socket_signal, gameplay_action: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, audio, vfx: 1
- idle_animation, gameplay_action: 1
- skeletal_animation, socket_signal, animation_state: 1

Raw SHA-256: `293ffaa79d3b94932e89b49a1a5898b5d8db9e7a2f45e766834d66f2247d33cc`. Binary SHA-256: `9872f23d9200341d9d85f7b2cafa9c5beb9cb227db7a8a9a735b6b17699b7c1a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq012\scenes\sq012_03a_av_pad.scene" --events
```

## `base\quest\side_quests\sq012\scenes\sq012_04a_meet_river.scene`

202 graph nodes, 272 edges; 45 event-bearing sections, 334 events; 94 screenplay lines, 19 screenplay options, 11 choice nodes.

Actors: river (actor 0, spawnSet); det_yu (actor 1, community); rivers_car (actor 2, spawnSet); han_car (actor 3, community); V (actor 4, findInContext).

Entries: `timelapse_in` → 351; `sq012_04a_diner_meeting_in` → 1; `ride_with_river_preview` → 371; `Start 0` → 374; `Start1` → 1018.

Exits: `timelapse_out` → 352; `sq012_04a_to_informant_out` → 2; `End 0` → 375; `sq012_04a_to_market_out` → 83.

End nodes: 2: `NonTerminating`; 83: `NonTerminating`; 352: `<omitted>`; 375: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 10 | 124 / 259 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/2` |
| `scnChangeIdleAnimEvent` | 23 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 73 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 1 | 1025 / 1261 | `/Data/RootChunk/sceneGraph/Data/graph/162/Data/events/2` |
| `scnGameplayTransitionEvent` | 3 | 116 / 235 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/48` |
| `scnIKEvent` | 8 | 116 / 221 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/37` |
| `scnLookAtEvent` | 67 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 76 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPoseCorrectionEvent` | 4 | 116 / 203 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/27` |
| `scnUnmountEvent` | 3 | 116 / 233 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/46` |
| `scneventsAttachPropToPerformer` | 2 | 13 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scneventsAttachPropToWorld` | 2 | 13 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scneventsCameraParamsEvent` | 4 | 163 / 458 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 5 | 116 / 230 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/44` |
| `scneventsSocket` | 51 | 4 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scneventsVFXEvent` | 2 | 353 / 708 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech: 5
- speech, skeletal_animation: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, gaze: 2
- camera: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, audio, socket_signal, animation_state: 1
- skeletal_animation, camera, socket_signal: 1
- socket_signal: 1
- vfx, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, ik, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, animation_state: 1

Raw SHA-256: `dab89ffeea0c9f7f00434963c54dfa8006f6e8b03ad59242f324c5e9df563dfc`. Binary SHA-256: `4b6e28c62e8b69aab080ca0b3ef4c166350ad85854ce5929c809175ba1fad209`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq012\scenes\sq012_04a_meet_river.scene" --events
```

## `base\quest\side_quests\sq012\scenes\sq012_05a_sex_shop.scene`

300 graph nodes, 351 edges; 58 event-bearing sections, 449 events; 111 screenplay lines, 24 screenplay options, 10 choice nodes.

Actors: sobchak (actor 0, spawnSet); shop_owner (actor 1, spawnSet); passerby (actor 2, spawnDespawn); river_car (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `sq012_05a_river_explains_in` → 1; `sq012_05a_sex_shop_owner_in` → 9; `sq012_05a_interrogation_in` → 26; `arriving_at_shop_preview` → 510; `sq012_05a_where_now_IN` → 45; `sq012_05a_timelapse_in` → 73; `sq012_05a_sit_car_in` → 1060; `sq012_05a_river_explains_player_drives_in` → 400; `sq021_intuition_in` → 210.

Exits: `sq012_05a_river_explains_out` → 2; `sq012_05a_sex_shop_owner_out` → 13; `sq012_05a_sex_shop_timelapse_msg` → 1205; `sq012_05a_where_now_rqr_with_riverOUT` → 46; `sq012_05a_where_now_market_with_river_IN` → 47; `sq012_05a_where_now_market_alone_IN` → 48; `sq012_05a_where_now_rqr_alone_OUT` → 49; `sq012_05a_timelapse_out` → 74; `sq012_05a_sit_car_out` → 1061; `sq021_intuition_out` → 212.

End nodes: 2: `NonTerminating`; 13: `NonTerminating`; 46: `NonTerminating`; 47: `NonTerminating`; 48: `NonTerminating`; 49: `NonTerminating`; 74: `<omitted>`; 212: `<omitted>`; 1061: `NonTerminating`; 1205: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 120 / 439 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/2` |
| `scnChangeIdleAnimEvent` | 35 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnDialogLineEvent` | 80 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 7 | 12 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/19` |
| `scnIKEvent` | 18 | 12 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/6` |
| `scnLookAtEvent` | 95 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 77 | 4 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scnUnmountEvent` | 7 | 12 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/18` |
| `scneventsEquipItemToPerformer` | 1 | 10 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 15 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsSocket` | 110 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 1 | 10 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |
| `scneventsVFXEvent` | 2 | 408 / 1027 | `/Data/RootChunk/sceneGraph/Data/graph/112/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 12
- speech: 8
- gaze: 7
- skeletal_animation, idle_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation: 2
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- vfx, socket_signal: 1
- socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, ik, socket_signal, animation_state: 1

Raw SHA-256: `f1fc6d7fa738eda26fe889ef2ce42726199719d0cac04edcc6e400e5386c3691`. Binary SHA-256: `224f0dd3b96f2b8a033497ee41171f58024ef4c633533ed46ddd1d986796a02f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq012\scenes\sq012_05a_sex_shop.scene" --events
```

## `base\quest\side_quests\sq012\scenes\sq012_05b_market_interview.scene`

374 graph nodes, 455 edges; 83 event-bearing sections, 588 events; 155 screenplay lines, 26 screenplay options, 15 choice nodes.

Actors: vendor (actor 0, spawnSet); sobchak (actor 1, spawnSet); tyger_01 (actor 2, community); tyger_02 (actor 3, community); random_vendor_01 (actor 4, community); random_vendor_02 (actor 5, community); random_vendor_03 (actor 6, community); random_vendor_04 (actor 7, community); river_car (actor 8, spawnSet); Player (actor 9, findInContext).

Entries: `sq012_05b_vendor_interview_IN` → 1; `sq012_05b_river_arrive_manual_IN` → 9; `sq012_05b_river_after_interview_IN` → 16; `sq012_05b_river_arrive_auto_IN` → 31; `sq012_05b_timelapse_in` → 662; `sq012_05b_after_tygers_IN` → 90; `arrival_testing` → 506; `sq012_05b_find_christine_IN` → 258; `thugs_by_car_prev` → 1170.

Exits: `sq012_05b_vendor_interview_OUT` → 2; `sq012_05b_river_arrive_OUT` → 10; `sq012_05b_river_after_TCs_to_rqr_manual_OUT` → 17; `sq012_05b_timelapse_out` → 663; `sq012_05b_tyger_claws_hostile_OUT` → 75; `sq012_05b_tyger_claws_leave_OUT` → 77; `sq012_05b_river_after_tcs_to_rqr_together_OUT` → 122; `sq012_05b_river_after_tcs_sex_shop_manual_OUT` → 127; `sq012_05b_rivr_after_tcs_sex_shop_together_OUT` → 134; `sq012_05b_market_time_lapse_msg` → 1391; `terminate_scene_OUT` → 846; `sq012_05b_find_christine_OUT` → 259.

End nodes: 2: `NonTerminating`; 10: `NonTerminating`; 17: `NonTerminating`; 75: `<omitted>`; 77: `NonTerminating`; 122: `NonTerminating`; 127: `NonTerminating`; 134: `NonTerminating`; 259: `NonTerminating`; 663: `NonTerminating`; 846: `<omitted>`; 1391: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 36 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnDialogLineEvent` | 113 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 13 | 65 / 249 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/23` |
| `scnIKEvent` | 28 | 65 / 240 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/15` |
| `scnLookAtEvent` | 121 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 122 | 26 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/2` |
| `scnUnmountEvent` | 13 | 65 / 248 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/22` |
| `scneventsAttachPropToPerformer` | 3 | 462 / 1342 | `/Data/RootChunk/sceneGraph/Data/graph/140/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 15 | 65 / 244 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/19` |
| `scneventsSocket` | 119 | 55 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/0` |
| `scneventsVFXEvent` | 5 | 112 / 377 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 10
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 9
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 7
- speech: 6
- skeletal_animation: 6
- socket_signal: 4
- gaze: 4
- speech, skeletal_animation, idle_animation, gaze: 3
- speech, skeletal_animation, idle_animation: 3
- skeletal_animation, idle_animation, gaze, socket_signal: 3
- skeletal_animation, socket_signal: 3
- speech, idle_animation, gaze: 2
- speech, gaze: 2
- speech, skeletal_animation: 2
- speech, skeletal_animation, idle_animation, gaze, vfx: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, props_equipment: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- props_equipment: 1
- vfx, socket_signal: 1
- socket_signal, animation_state: 1

Raw SHA-256: `6a7ec24372870df9ef76d8f9659eca8caa3b7f1f0988d588893f29b1ba3f6161`. Binary SHA-256: `ab61d28cb529af2bb65b3b2fe9b4cadbacd9549646b6d583a9ae5d459d62b7d0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq012\scenes\sq012_05b_market_interview.scene" --events
```

## `base\quest\side_quests\sq012\scenes\sq012_06a_rqr_ext.scene`

156 graph nodes, 201 edges; 30 event-bearing sections, 182 events; 69 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: River (actor 0, spawnSet); 6th_street_boss (actor 1, community); Animal_Ganger_Male (actor 2, community); river_car (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `sq012_06a_entry_please_in` → 1; `sq012_06a_river_into_elevator_IN` → 635; `sq012_06a_arrive_IN` → 25; `sq012_06a_car_setup` → 526; `sq012_06a__lets_look_around_IN` → 30; `sq012_06a_locked_door_IN` → 35; `sq012_06a_look_at_that_IN` → 40; `river_drives_prev` → 544; `sq012_06a_sloppy_IN` → 56; `sq012_06a_rqr_enemy_chat_IN` → 70; `sq012_06a_wait_for_river_IN` → 106.

Exits: `sq012_06a_entry_please_combat_begins` → 2; `sq012_06a_entry_please_playstyles` → 15; `sq012_06a_river_into_elevator_OUT` → 637; `sq012_06a_arrive_OUT` → 26; `sq012_06a__lets_look_around_OUT` → 31; `sq012_06a_locked_door_OUT` → 37; `sq012_06a_look_at_that_OUT` → 41; `sq012_06a_sloppy_OUT` → 57; `sq012_06a_rqr_enemy_chat_OUT` → 71; `sq012_06a_rar_timelapse_msg` → 595; `sq012_06a_wait_for_river_OUT` → 107.

End nodes: 2: `NonTerminating`; 15: `NonTerminating`; 26: `NonTerminating`; 31: `<omitted>`; 37: `<omitted>`; 41: `<omitted>`; 57: `<omitted>`; 71: `<omitted>`; 107: `<omitted>`; 595: `NonTerminating`; 637: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 16 | 3 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 52 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 3 | 141 / 263 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/6` |
| `scnIKEvent` | 10 | 141 / 257 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/1` |
| `scnLookAtEvent` | 19 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 25 | 3 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnPoseCorrectionEvent` | 2 | 96 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/2` |
| `scnUnmountEvent` | 3 | 141 / 262 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 6 | 141 / 260 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/4` |
| `scneventsSocket` | 44 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsVFXEvent` | 2 | 140 / 249 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, vfx, socket_signal: 1
- vfx, socket_signal: 1
- idle_animation, gaze: 1
- ik, socket_signal, animation_state: 1
- gaze: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `665d833f97d14af9fbe9a3c4ac2d9e36910c88d8bb8868ed602948d4bafaa854`. Binary SHA-256: `480821a9b9977951221e80f54937fcf7f719368a88257d3c10c9e4cefe028059`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq012\scenes\sq012_06a_rqr_ext.scene" --events
```

## `base\quest\side_quests\sq012\scenes\sq012_06b_rqr_investigation.scene`

232 graph nodes, 267 edges; 50 event-bearing sections, 258 events; 156 screenplay lines, 44 screenplay options, 19 choice nodes.

Actors: river (actor 0, spawnSet); 6th_street_officer (actor 1, community); 6th_street_ug_boss (actor 2, community); 6th_street_ug_grunt (actor 3, community); river_phone (actor 4, spawnSet); det_yu (actor 5, spawnDespawn); rhyne_body (actor 6, spawnDespawn); animal_thug (actor 7, spawnDespawn); sobchack_car (actor 8, spawnSet); Player (actor 9, findInContext).

Entries: `sq012_06b_arrival_IN` → 1; `sq012_06b_interrogate_IN` → 7; `sq012_06b_interrogate_grapple_IN` → 244; `sq012_06b_enter_office_IN` → 14; `sq012_06b_footage_IN` → 19; `sq012_06b_fried_BD_IN` → 32; `sq012_06b_BD_attack_IN` → 37; `sq012_06b_leave_together_IN` → 746; `sq012_06b_rqr_enemy_chat_IN` → 59; `sq012_06b_river_pick_up_IN` → 751; `sq012_06b_exit_club_IN` → 64; `officer_facial_on` → 1242; `sq012_06b_videotape_IN` → 129.

Exits: `sq012_06b_arrival_OUT` → 2; `sq012_06b_interrogate_OUT` → 8; `sq012_06b_enter_office_OUT` → 15; `sq012_06b_footage_OUT` → 20; `sq012_06b_fried_BD_OUT` → 33; `sq012_06b_BD_attack_OUT` → 38; `sq012_06b_leave_together_OUT` → 744; `sq012_06b_leave_together_prefetch` → 1208; `sq012_06b_footge_found_phone_OUT` → 749; `sq012_06b_rqr_enemy_chat_OUT` → 60; `sq012_06b_exit_club_river_drives_OUT` → 65; `sq012_06b_exit_club_player_drives_OUT` → 71; `sq012_06b_river_pick_up_OUT` → 100; `sq012_06b_interrogate_grapple_OUT` → 793; `sq012_06b_videotape_OUT` → 130.

End nodes: 2: `NonTerminating`; 8: `<omitted>`; 15: `NonTerminating`; 20: `NonTerminating`; 33: `NonTerminating`; 38: `<omitted>`; 60: `<omitted>`; 65: `<omitted>`; 71: `<omitted>`; 100: `<omitted>`; 130: `<omitted>`; 744: `<omitted>`; 749: `<omitted>`; 793: `<omitted>`; 1208: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 16 | 39 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/9` |
| `scnDialogLineEvent` | 142 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 369 / 564 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/3` |
| `scnIKEvent` | 2 | 369 / 562 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/1` |
| `scnLookAtEvent` | 10 | 21 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |
| `scnPlaySkAnimEvent` | 28 | 21 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/3` |
| `scnUnmountEvent` | 1 | 369 / 569 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/7` |
| `scneventsAttachPropToPerformer` | 3 | 39 / 82 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/2` |
| `scneventsAttachPropToWorld` | 1 | 39 / 124 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/34` |
| `scneventsCameraParamsEvent` | 3 | 39 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 1 | 369 / 565 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/4` |
| `scneventsSocket` | 36 | 21 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/7` |
| `scneventsVFXDurationEvent` | 1 | 39 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/20` |
| `scneventsVFXEvent` | 13 | 39 / 84 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 28
- speech, skeletal_animation, idle_animation, socket_signal: 4
- speech, idle_animation, gaze: 2
- speech, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation: 1
- camera: 1
- gaze: 1
- speech, idle_animation: 1
- speech, idle_animation, socket_signal: 1
- idle_animation: 1

Raw SHA-256: `3abe8d1853f974923bc29f15d3f3090a82cfbf676ef9a744be67b729461d6b21`. Binary SHA-256: `25d867a0557cea62042ca8430f8e71ef3da5cd50c10cc2f5ba7377c914c185b0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq012\scenes\sq012_06b_rqr_investigation.scene" --events
```

## `base\quest\side_quests\sq012\scenes\sq012_06c_rqr_phonecalls.scene`

47 graph nodes, 41 edges; 9 event-bearing sections, 23 events; 20 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: river (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `sq012_06c__lets_look_around_IN` → 1; `sq012_06c_sloppy_IN` → 7; `sq012_06a_on_the_line_IN` → 12; `sq012_06a_locked_door_IN` → 17; `sq012_06a_look_at_that_IN` → 22; `sq012_06c_combat_start_IN` → 32; `sq012_06c_join_me_IN` → 37.

Exits: `sq012_06c__lets_look_around_OUT` → 2; `sq012_06c_sloppy_OUT` → 8; `sq012_06a_on_the_line_OUT` → 13; `sq012_06a_locked_door_OUT` → 19; `sq012_06a_look_at_that_OUT` → 23; `sq012_06c_combat_start_OUT` → 33; `sq012_06c_join_me_OUT` → 38.

End nodes: 2: `NonTerminating`; 8: `NonTerminating`; 13: `NonTerminating`; 19: `NonTerminating`; 23: `NonTerminating`; 33: `<omitted>`; 38: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 29 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnDialogLineEvent` | 19 | 9 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnLookAtEvent` | 1 | 135 / 128 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, idle_animation: 3
- gaze: 1

Raw SHA-256: `a1020f8eb793ba1a2d4eb230f4af97f3af95d697e0662bae0b96299fab495d31`. Binary SHA-256: `ed0ec9a07959df155e242b865b1593841c6459ae64c21a197de2913517075a5d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq012\scenes\sq012_06c_rqr_phonecalls.scene" --events
```

## `base\quest\side_quests\sq012\scenes\sq012_07a_conclusions.scene`

146 graph nodes, 169 edges; 35 event-bearing sections, 309 events; 85 screenplay lines, 21 screenplay options, 9 choice nodes.

Actors: sobchak (actor 0, spawnSet); det_yu (actor 1, community); river_car (actor 2, spawnSet); han_car (actor 3, community); Player (actor 4, findInContext).

Entries: `sq012_07a_confront_det_yu_in` → 1; `arriving_prev` → 435; `sq012_07a_river_conclusion_in` → 56; `greeting` → 148; `sq012_07a_get_out_IN` → 247.

Exits: `sq012_07a_confront_det_yu_out` → 2; `sq012_07a_river_dismount_out` → 366; `sq012_07a_river_conclusion_out` → 57; `sq012_river_one_liner_out` → 143; `sq012_07a_get_out_OUT` → 248.

End nodes: 2: `NonTerminating`; 57: `NonTerminating`; 143: `<omitted>`; 248: `NonTerminating`; 366: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 46 / 393 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/41` |
| `scnChangeIdleAnimEvent` | 14 | 5 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 76 | 5 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 3 | 60 / 423 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/10` |
| `scnIKEvent` | 8 | 60 / 412 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/2` |
| `scnLookAtEvent` | 49 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 46 / 398 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/44` |
| `scnPlaySkAnimEvent` | 70 | 5 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 3 | 60 / 422 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/9` |
| `scneventsAttachPropToWorld` | 1 | 46 / 390 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/38` |
| `scneventsEquipItemToPerformer` | 2 | 46 / 373 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/30` |
| `scneventsSetAnimFeatureEvent` | 6 | 46 / 370 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/29` |
| `scneventsSocket` | 73 | 5 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scneventsUnequipItemFromPerformer` | 1 | 46 / 388 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/36` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 9
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, gaze, socket_signal: 3
- speech, skeletal_animation, socket_signal: 3
- speech: 3
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- gaze, socket_signal: 1
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- idle_animation: 1
- socket_signal, animation_state: 1

Raw SHA-256: `3ee05c948153f2239d47f75d85f2c0ff38009fcb8e3bc468b937a16e66724457`. Binary SHA-256: `697911fef45f22c0890b0abe7777327be94da07391233794d4506063f20d95f3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq012\scenes\sq012_07a_conclusions.scene" --events
```

## `base\quest\side_quests\sq012\scenes\sq012_08a_peralez_apartment.scene`

183 graph nodes, 224 edges; 34 event-bearing sections, 299 events; 78 screenplay lines, 18 screenplay options, 7 choice nodes.

Actors: elizabeth (actor 0, spawnSet); jefferson (actor 1, spawnSet); Johnny (actor 2, spawnDespawn); V (actor 3, findInContext).

Entries: `sq012_08a_elizabeth_greeting_in` → 1; `sq012_08a_debrief_in` → 7; `couch_part_prev` → 708; `sq012_08a_johnny_in` → 89; `liz_pouring_drinks_prev` → 732.

Exits: `sq012_08a_elizabeth_greeting_out` → 2; `sq012_08a_johnny_out` → 90; `sq012_signal_kill_end` → 421; `start_piano` → 457.

End nodes: 2: `NonTerminating`; 90: `<omitted>`; 421: `<omitted>`; 457: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 19 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 56 | 4 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnGameplayTransitionEvent` | 4 | 4 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/17` |
| `scnIKEvent` | 8 | 4 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scnLookAtEvent` | 38 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 76 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnUnmountEvent` | 4 | 4 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/16` |
| `scneventsAttachPropToNode` | 2 | 410 / 1105 | `/Data/RootChunk/sceneGraph/Data/graph/128/Data/events/0` |
| `scneventsAttachPropToPerformer` | 4 | 152 / 461 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/2` |
| `scneventsAttachPropToWorld` | 3 | 239 / 636 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/3` |
| `scneventsCameraParamsEvent` | 3 | 122 / 438 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 4 | 4 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |
| `scneventsSocket` | 74 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 4 | 33 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, skeletal_animation, idle_animation, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, vfx, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, camera, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- idle_animation, gaze: 1
- skeletal_animation: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- gaze, props_equipment, socket_signal: 1
- speech, idle_animation, gaze: 1
- gaze: 1

Raw SHA-256: `7539201a659f5c3f1f48a272bd80dbfcbdc2d11499adb71633ba85d7d352eed3`. Binary SHA-256: `0d3bd7ae765065fe6db3484fbcdaddd6ec930fbafaeed61a7508d8ba64445160`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq012\scenes\sq012_08a_peralez_apartment.scene" --events
```

