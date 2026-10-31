# Queen of the Highway: scene presentation

Journal identity: `quests/side_quest/sq027_02_raffen_shiv_attack`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq027_02_raffen_shiv_attack.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\side_quests\sq027\scenes\sq027_05a_transport_delivered.scene`

303 graph nodes, 380 edges; 35 event-bearing sections, 425 events; 64 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: Saul (actor 0, spawnSet); Panam (actor 1, spawnSet); Carol (actor 2, spawnSet); Bob (actor 3, spawnSet); Teddy (actor 4, spawnSet); Cassidy (actor 5, spawnSet); Mitch (actor 6, spawnSet); guard1 (actor 7, community); guard2 (actor 8, community); guard3 (actor 9, community); Panzer_Flatbed_A (actor 10, community); Panzer_Flatbed_B (actor 11, community); V (actor 12, findInContext).

Entries: `sq027_05a_saul_reception_in` → 1; `cinedebug_end` → 1790; `cinedebug_panamend` → 1339.

Exits: `sq027_05a_saul_reception_out` → 2; `sq027_05a_scene_over_out` → 579.

End nodes: 2: `<omitted>`; 579: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 77 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 38 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 13 | 25 / 73 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/36` |
| `scnIKEvent` | 26 | 25 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/18` |
| `scnLookAtEvent` | 70 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 77 | 25 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnUnmountEvent` | 13 | 25 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/34` |
| `scneventsEquipItemToPerformer` | 3 | 350 / 582 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/112` |
| `scneventsSetAnimFeatureEvent` | 13 | 25 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/32` |
| `scneventsSocket` | 93 | 25 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 2 | 338 / 414 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, gaze, socket_signal: 8
- speech, skeletal_animation, idle_animation, socket_signal: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation: 3
- speech, idle_animation, gaze: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation: 1

Raw SHA-256: `1161d3819c6445e6f39ff6f56e8a45629ac1a2b8bc2fbc4aeef1fc3c1fb07c0a`. Binary SHA-256: `07de58be6e6be0cbce17a082dc610f1df8043d525ab01dc7060ad15e213a90e6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_05a_transport_delivered.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_05b_holocall_basilisk_ready.scene`

31 graph nodes, 35 edges; 3 event-bearing sections, 14 events; 7 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Panam (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 11 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 7 | 11 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, idle_animation: 3

Raw SHA-256: `f9fe815b5790246e27d2e6f3257205e8111b0176d77c01713ce5cda39227c9f7`. Binary SHA-256: `69cec76c5fef205e35ec19ced27d2dd20f479fd2179eceba4e9ac70ef425ad2f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_05b_holocall_basilisk_ready.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_06_panzer.scene`

838 graph nodes, 1041 edges; 147 event-bearing sections, 1310 events; 234 screenplay lines, 18 screenplay options, 10 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, findInContext); Mitch (actor 2, spawnSet); Teddy (actor 3, spawnSet); Carol (actor 4, spawnSet); Cassidy (actor 5, spawnSet); Bob (actor 6, spawnSet); Johnny (actor 7, spawnDespawn); TPP_V_Male (actor 8, spawnDespawn); FPP_Panam (actor 9, spawnDespawn); TPP_V_Female (actor 10, spawnDespawn); TPP_V_Male_No_Impostor (actor 11, spawnDespawn); Panzer (actor 12, spawnSet); V (actor 13, findInContext).

Entries: `sq027_06_marauders_in` → 985; `sq027_06_near_panzer_in` → 423; `CineDebug_PanamSex` → 1290; `sq027_06_scene_setup` → 5257; `sq027_06_arrived_in` → 575; `Cinedebug_v_plugin` → 2921; `sq027_06_sex_in` → 592; `sq027_06_testdrive_in` → 595; `CineDebug_PanamSex2` → 1429.

Exits: `sq027_06_sex_out` → 983; `sq027_06_marauders_out` → 986; `sq027_06_basilisk_out` → 568; `sq027_06_arrived_out` → 578; `sq027_06_testdrive_out` → 596; `Quest_Boundaries_Out` → 2248.

End nodes: 568: `NonTerminating`; 578: `<omitted>`; 596: `<omitted>`; 983: `<omitted>`; 986: `<omitted>`; 2248: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 19 | 881 / 691 | `/Data/RootChunk/sceneGraph/Data/graph/81/Data/events/7` |
| `scnChangeIdleAnimEvent` | 132 | 424 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 137 | 424 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayActionEvent` | 6 | 1448 / 1096 | `/Data/RootChunk/sceneGraph/Data/graph/143/Data/events/2` |
| `scnGameplayTransitionEvent` | 2 | 3185 / 3427 | `/Data/RootChunk/sceneGraph/Data/graph/276/Data/events/6` |
| `scnIKEvent` | 6 | 3185 / 3423 | `/Data/RootChunk/sceneGraph/Data/graph/276/Data/events/3` |
| `scnLookAtEvent` | 115 | 424 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 2 | 2045 / 2763 | `/Data/RootChunk/sceneGraph/Data/graph/174/Data/events/11` |
| `scnPlayRidAnimEvent` | 166 | 1448 / 1112 | `/Data/RootChunk/sceneGraph/Data/graph/143/Data/events/7` |
| `scnPlaySkAnimEvent` | 427 | 424 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/16` |
| `scnPoseCorrectionEvent` | 4 | 451 / 127 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnUnmountEvent` | 1 | 6665 / 6394 | `/Data/RootChunk/sceneGraph/Data/graph/832/Data/events/4` |
| `scneventsAttachPropToPerformer` | 3 | 3344 / 3585 | `/Data/RootChunk/sceneGraph/Data/graph/292/Data/events/4` |
| `scneventsAttachPropToWorld` | 1 | 3930 / 4192 | `/Data/RootChunk/sceneGraph/Data/graph/386/Data/events/0` |
| `scneventsEquipItemToPerformer` | 3 | 798 / 446 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/5` |
| `scneventsPlayRidCameraAnimEvent` | 54 | 1448 / 1122 | `/Data/RootChunk/sceneGraph/Data/graph/143/Data/events/11` |
| `scneventsSetAnimFeatureEvent` | 31 | 577 / 205 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |
| `scneventsSocket` | 149 | 424 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 1 | 798 / 449 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/8` |
| `scneventsVFXEvent` | 51 | 1448 / 1218 | `/Data/RootChunk/sceneGraph/Data/graph/143/Data/events/44` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 34
- skeletal_animation: 20
- gaze: 15
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- vfx: 5
- speech, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, idle_animation, gaze, socket_signal: 3
- skeletal_animation, idle_animation, gaze, socket_signal: 3
- skeletal_animation, idle_animation: 3
- socket_signal, animation_state: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 2
- speech, idle_animation: 2
- speech, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- skeletal_animation, idle_animation, rid_actor, camera, rid_camera, vfx, socket_signal: 2
- skeletal_animation, idle_animation, props_equipment: 2
- animation_state: 2
- skeletal_animation, socket_signal, animation_state: 2
- speech, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, rid_actor, camera, rid_camera, audio, vfx, socket_signal, gameplay_action: 1
- skeletal_animation, vfx, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state, gameplay_action: 1
- gaze, socket_signal: 1
- idle_animation, audio, socket_signal, gameplay_action: 1
- skeletal_animation, idle_animation, audio, socket_signal, animation_state: 1
- idle_animation, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- idle_animation, ik, gameplay_transition, socket_signal, animation_state, gameplay_action: 1
- idle_animation, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- idle_animation, gaze: 1
- skeletal_animation, socket_signal: 1
- gaze, socket_signal, animation_state: 1
- props_equipment, vfx: 1
- idle_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal, animation_state: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, ik, audio, socket_signal, animation_state: 1
- speech, audio, socket_signal: 1
- idle_animation, socket_signal, animation_state, gameplay_action: 1
- idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `e513f9bddaefd7a0e03eea910600288d909f2e0a85f2389624d12ddfd6d40c10`. Binary SHA-256: `2e9029faf8b8c8efe612d97bc5ffe7b900a79235e3237c0b9b087bad4ceae68d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_06_panzer.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_07_nomad_camp_attack.scene`

41 graph nodes, 38 edges; 9 event-bearing sections, 33 events; 13 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, spawnDespawn); Panzer (actor 2, spawnSet); V (actor 3, findInContext).

Entries: `sq027_07_marauders_in` → 338; `sq027_07_leave_warning_ambush_reuse_in` → 345; `sq027_07_hit_comment` → 232; `sq027_07_camp_in` → 27; `sq027_07_leave_warning_in` → 332; `sq027_07_reminder_in` → 376.

Exits: `sq027_07_marauders_out` → 340; `sq027_07_leave_warning_ambush_reuse_out` → 347; `sq027_07_camp_out` → 323; `sq027_07_leave_warning_out` → 334.

End nodes: 323: `<omitted>`; 334: `<omitted>`; 340: `<omitted>`; 347: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 10 | 230 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 10 | 230 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnLookAtEvent` | 6 | 230 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnPlaySkAnimEvent` | 6 | 230 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsSocket` | 1 | 230 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- speech, skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, idle_animation: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze: 1

Raw SHA-256: `ed5a9b9ecdfd8f4f3f6eeac5256ce412ad2c27708703b3736121d1e23b8c5235`. Binary SHA-256: `5bee64f652e2a1f3aa5a259604abdaf27676f749dd55ce54cc52a3c09fcddf19`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_07_nomad_camp_attack.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_08_camp_saved.scene`

426 graph nodes, 507 edges; 78 event-bearing sections, 628 events; 127 screenplay lines, 15 screenplay options, 7 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, spawnSet); Mitch (actor 2, spawnSet); Teddy (actor 3, spawnSet); Bob (actor 4, spawnSet); Carol (actor 5, spawnSet); Cassidy (actor 6, spawnSet); Saul_holocall (actor 7, spawnDespawn); ALDECALDOS_01 (actor 8, community); ALDECALDOS_02 (actor 9, community); ALDECALDOS_03 (actor 10, community); Panzer (actor 11, spawnSet); Teddy_Car (actor 12, community); Bob_Car (actor 13, community); Cassity_Car (actor 14, community); Mitch_Car (actor 15, spawnSet); Carol_Car (actor 16, community); V (actor 17, findInContext).

Entries: `Cinedebug_saulend` → 1217; `RETROFIX_CYB661006` → 3230; `CineDebug_BarScene` → 912; `cinedebug_PanamSaul_end` → 2591; `sq027_08_01_mood_chat_in` → 1456; `Cinedebug_SaulPanam` → 1068; `sq027_08_camp_saved_in` → 702; `cinedebug_walktalk` → 1177.

Exits: `sq027_08_camp_saved_out` → 238; `sq027_08_01_mood_chat_out` → 1457.

End nodes: 238: `<omitted>`; 1457: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 2768 / 2449 | `/Data/RootChunk/sceneGraph/Data/graph/342/Data/events/9` |
| `scnChangeIdleAnimEvent` | 110 | 277 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/5` |
| `scnDialogLineEvent` | 85 | 9 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 11 | 277 / 201 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/93` |
| `scnIKEvent` | 22 | 277 / 186 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/85` |
| `scnLookAtEvent` | 105 | 277 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnPlaySkAnimEvent` | 118 | 277 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scnUnmountEvent` | 11 | 277 / 202 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/94` |
| `scneventsAttachPropToPerformer` | 11 | 492 / 461 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/3` |
| `scneventsAttachPropToWorld` | 9 | 492 / 470 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/10` |
| `scneventsCameraParamsEvent` | 4 | 641 / 648 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/1` |
| `scneventsEquipItemToPerformer` | 2 | 2604 / 2312 | `/Data/RootChunk/sceneGraph/Data/graph/321/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 15 | 277 / 199 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/92` |
| `scneventsSocket` | 111 | 277 / 142 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/55` |
| `scneventsUnequipItemFromPerformer` | 1 | 3120 / 2874 | `/Data/RootChunk/sceneGraph/Data/graph/402/Data/events/2` |
| `scneventsUnequipItemFromPerformerByItem` | 3 | 1129 / 905 | `/Data/RootChunk/sceneGraph/Data/graph/81/Data/events/2` |
| `scneventsVFXEvent` | 8 | 284 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/17` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 12
- skeletal_animation, props_equipment, socket_signal: 6
- idle_animation, gaze: 5
- speech, idle_animation, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- skeletal_animation: 3
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation: 2
- gaze: 2
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, idle_animation, gaze, socket_signal: 2
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- camera: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, camera, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, socket_signal: 1
- vfx: 1
- skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- props_equipment, socket_signal, animation_state: 1
- socket_signal, animation_state: 1

Raw SHA-256: `68694fe08359cac8a4ebcbf4cfd1b8cbe38f192168a5df7548ad698caf67f26d`. Binary SHA-256: `6c5d4682e491207dd70d1aea022b31df8206388decb3534b6cafa95b2300c967`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_08_camp_saved.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_09_new_camp_wakeup.scene`

344 graph nodes, 415 edges; 77 event-bearing sections, 647 events; 141 screenplay lines, 21 screenplay options, 10 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, spawnSet); Mitch (actor 2, spawnSet); Teddy (actor 3, spawnSet); Bob (actor 4, spawnSet); Carol (actor 5, spawnSet); Cassidy (actor 6, spawnSet); Johnny (actor 7, spawnDespawn); V (actor 8, findInContext).

Entries: `CineDebug_Car` → 1248; `sq027_09_new_camp_wakeup_in` → 702; `cinedebug_endatcar` → 1319.

Exits: `sq027_09_new_camp_wakeup_out` → 238.

End nodes: 238: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 847 / 703 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/4` |
| `scnChangeIdleAnimEvent` | 113 | 545 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 100 | 545 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnGameplayTransitionEvent` | 7 | 600 / 408 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/9` |
| `scnIKEvent` | 14 | 600 / 400 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/2` |
| `scnLookAtEvent` | 95 | 545 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 179 | 545 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 7 | 600 / 407 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/8` |
| `scneventsCameraParamsEvent` | 7 | 847 / 706 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/7` |
| `scneventsEquipItemToPerformer` | 2 | 3163 / 2676 | `/Data/RootChunk/sceneGraph/Data/graph/331/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 7 | 600 / 405 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/7` |
| `scneventsSocket` | 105 | 545 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |
| `scneventsUnequipItemFromPerformer` | 1 | 3163 / 2678 | `/Data/RootChunk/sceneGraph/Data/graph/331/Data/events/7` |
| `scneventsVFXEvent` | 8 | 615 / 553 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 24
- speech, skeletal_animation, idle_animation, socket_signal: 6
- skeletal_animation: 5
- skeletal_animation, idle_animation, gaze, socket_signal: 4
- gaze: 4
- skeletal_animation, idle_animation, gaze: 4
- skeletal_animation, socket_signal: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, idle_animation, gaze: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, socket_signal: 2
- vfx: 2
- speech: 2
- speech, idle_animation: 2
- skeletal_animation, gaze: 2
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, camera, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, camera, vfx: 1
- skeletal_animation, gaze, camera, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1

Raw SHA-256: `d3cc5af2fc50b4476c53066484dd9eb41c649e4e9cfdf9fba1f45c5c4229834e`. Binary SHA-256: `5cca608d7a3162d361705447d24bce7b1de3257968241a0889505771abd8686f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_09_new_camp_wakeup.scene" --events
```

## `dlc\dlc6_apart\scenes\dlc6_apart_panam_camp_interactions.scene`

86 graph nodes, 96 edges; 8 event-bearing sections, 60 events; 8 screenplay lines, 7 screenplay options, 7 choice nodes.

Actors: v_male_tpp (actor 0, spawnDespawn); v_female_tpp (actor 1, spawnDespawn); johnny_mirror (actor 2, spawnDespawn); Panam (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `in` → 1; `in_romance_bed` → 490; `in_tv` → 493; `in_shower` → 495.

Exits: `out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 8 | 8 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnChangeIdleAnimEvent` | 1 | 12 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnGameplayTransitionEvent` | 3 | 33 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/4` |
| `scnIKEvent` | 6 | 33 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scnLookAtEvent` | 3 | 1476 / 290 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/3` |
| `scnPlaySkAnimEvent` | 8 | 8 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPoseCorrectionEvent` | 1 | 1476 / 293 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/6` |
| `scnUnmountEvent` | 3 | 33 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/7` |
| `scneventsCameraParamsEvent` | 2 | 1476 / 289 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 3 | 33 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/6` |
| `scneventsSocket` | 14 | 8 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsVFXEvent` | 8 | 12 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- skeletal_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, camera, vfx, socket_signal, animation_state: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, vfx, socket_signal: 1

Raw SHA-256: `00df84e681160c573c7518662b6b1fe3421566a50428857f6ad4a3918f6b041c`. Binary SHA-256: `61015a5614650e0c1b63f12bf0c9d501747ac95f872aaa1588c76f8d4456ba1f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "dlc\dlc6_apart\scenes\dlc6_apart_panam_camp_interactions.scene" --events
```

