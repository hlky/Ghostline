# Dazed and Confused: scene presentation

Journal identity: `ep1/quests/minor_quest/mq303_addict`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-mq303_addict.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\quest\minor_quests\mq303\scenes\mq303_01_hook.scene`

490 graph nodes, 797 edges; 85 event-bearing sections, 649 events; 143 screenplay lines, 27 screenplay options, 12 choice nodes.

Actors: Shank (actor 0, spawnSet); Tool (actor 1, spawnSet); Johnny (actor 2, spawnDespawn); lina (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `Start 0` → 1; `Shank up sit` → 2661; `Johnny` → 2671; `Shank dialogue upstairs` → 3587; `Start 1` → 2404; `Start 5` → 2873.

Exits: `scene_killer` → 1760; `shank_kaput` → 1439; `End 7` → 2353; `follow` → 1591; `fail_out` → 748; `shop` → 844; `basement` → 846; `shank_move` → 849; `lina` → 855.

End nodes: 748: `NonTerminating`; 844: `NonTerminating`; 846: `NonTerminating`; 849: `NonTerminating`; 855: `NonTerminating`; 1439: `NonTerminating`; 1591: `NonTerminating`; 1760: `<omitted>`; 2353: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1225 / 1194 | `/Data/RootChunk/sceneGraph/Data/graph/114/Data/events/7` |
| `scnChangeIdleAnimEvent` | 29 | 163 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 109 | 146 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 12 | 293 / 233 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/13` |
| `scnIKEvent` | 24 | 293 / 226 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/7` |
| `scnLookAtEvent` | 123 | 146 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 169 | 171 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPoseCorrectionEvent` | 4 | 554 / 498 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/6` |
| `scnUnmountEvent` | 12 | 293 / 232 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/12` |
| `scneventsAttachPropToPerformer` | 1 | 4175 / 3807 | `/Data/RootChunk/sceneGraph/Data/graph/488/Data/events/0` |
| `scneventsCameraParamsEvent` | 1 | 1225 / 1176 | `/Data/RootChunk/sceneGraph/Data/graph/114/Data/events/0` |
| `scneventsEquipItemToPerformer` | 3 | 548 / 421 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 12 | 293 / 228 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/9` |
| `scneventsSocket` | 143 | 163 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scneventsUnequipItemFromPerformer` | 2 | 334 / 279 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/4` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 554 / 491 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/4` |
| `scneventsVFXEvent` | 3 | 1225 / 1193 | `/Data/RootChunk/sceneGraph/Data/graph/114/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 9
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- speech: 6
- skeletal_animation, socket_signal: 6
- speech, gaze: 5
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, gaze: 4
- speech, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation: 3
- speech, gaze, socket_signal: 3
- speech, idle_animation, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- socket_signal: 2
- gaze: 2
- gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- props_equipment, socket_signal: 1

Raw SHA-256: `8245de33f7b5919aec676b2020bd19d68476c83ed109c6a0d83f07e793edcbde`. Binary SHA-256: `38889a7942ac7f80b2b16b44d369b8c53d501c48361586b59b97c336b625eddb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq303\scenes\mq303_01_hook.scene" --events
```

## `ep1\quest\minor_quests\mq303\scenes\mq303_02_linas_mansion.scene`

572 graph nodes, 707 edges; 68 event-bearing sections, 548 events; 100 screenplay lines, 21 screenplay options, 11 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Ganger_1__female (actor 1, community); Ganger_2__male (actor 2, community); Lina (actor 3, spawnSet); Ganger_4__male (actor 4, community); Ganger_5_male (actor 5, community); Ganger_6_female (actor 6, community); ganger_car (actor 7, community); Player (actor 8, findInContext).

Entries: `Start 0` → 1; `Start 3` → 3002.

Exits: `scene killer` → 2171; `End 0` → 157.

End nodes: 157: `NonTerminating`; 2171: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 37 | 17 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 79 | 17 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 12 | 107 / 167 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/6` |
| `scnIKEvent` | 24 | 107 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scnLookAtAdvancedEvent` | 2 | 116 / 230 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/4` |
| `scnLookAtEvent` | 100 | 17 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 146 | 17 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnUnmountEvent` | 12 | 107 / 172 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/10` |
| `scneventsEquipItemToPerformer` | 7 | 151 / 550 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/21` |
| `scneventsSetAnimFeatureEvent` | 13 | 107 / 168 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/7` |
| `scneventsSocket` | 111 | 17 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1195 / 1561 | `/Data/RootChunk/sceneGraph/Data/graph/149/Data/events/27` |
| `scneventsVFXEvent` | 4 | 80 / 85 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 15
- speech, skeletal_animation, socket_signal: 6
- skeletal_animation, socket_signal: 6
- speech: 5
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- gaze: 2
- socket_signal: 2
- props_equipment, socket_signal: 2
- speech, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `390e77d25919721256a5b97b8d18fa947e94a435c1c8471249c3d9a587f5f005`. Binary SHA-256: `1b26c26c9a07185dcee971c44c14b3d251a1f6967811695aa9290a2f5a761eab`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq303\scenes\mq303_02_linas_mansion.scene" --events
```

## `ep1\quest\minor_quests\mq303\scenes\mq303_03_finale.scene`

365 graph nodes, 389 edges; 45 event-bearing sections, 957 events; 119 screenplay lines, 16 screenplay options, 10 choice nodes.

Actors: Shank (actor 0, spawnSet); Tool (actor 1, spawnSet); Lina_Malina (actor 2, spawnSet); Johnny (actor 3, spawnDespawn); lina_replacer (actor 4, community); fake_lina (actor 5, community); Player (actor 6, findInContext).

Entries: `epilogue_bd` → 1039; `Keyframes - Script` → 3217; `BD Scene upstairs` → 2018; `bat_gift` → 2747; `epilogue_bike` → 1599; `Keyframes - FIA` → 3111.

Exits: `End_sisters` → 2; `End_fia` → 141; `shank_fluff_twin` → 898; `shank_fluff_cured` → 915; `End_shock` → 197; `shank_fluff_clone` → 956.

End nodes: 2: `<omitted>`; 141: `<omitted>`; 197: `<omitted>`; 898: `NonTerminating`; 915: `NonTerminating`; 956: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 34 | 2024 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/4` |
| `scnDialogLineEvent` | 103 | 2024 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/8` |
| `scnGameplayTransitionEvent` | 20 | 2098 / 524 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/54` |
| `scnIKEvent` | 40 | 2098 / 505 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/45` |
| `scnLookAtAdvancedEvent` | 4 | 2468 / 1361 | `/Data/RootChunk/sceneGraph/Data/graph/97/Data/events/5` |
| `scnLookAtEvent` | 213 | 2024 / 133 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/2` |
| `scnPlaySkAnimEvent` | 295 | 2024 / 121 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/0` |
| `scnPoseCorrectionEvent` | 6 | 2098 / 536 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/61` |
| `scnUnmountEvent` | 20 | 2098 / 525 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/55` |
| `scneventsEquipItemToPerformer` | 4 | 2024 / 136 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 20 | 2098 / 520 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/51` |
| `scneventsSocket` | 196 | 2024 / 143 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/7` |
| `scneventsUnequipItemFromPerformer` | 1 | 2580 / 1576 | `/Data/RootChunk/sceneGraph/Data/graph/117/Data/events/1` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 2026 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/14` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 7
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 6
- speech: 5
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- skeletal_animation, socket_signal: 4
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1

Raw SHA-256: `65e86e322c25350e6dd03b43e8491254e0863a0c87f602fa4d1f1245f25a2c45`. Binary SHA-256: `e4188bbec07025013391af15c700f397c76b95d26116a9f939fc071f9625eca6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq303\scenes\mq303_03_finale.scene" --events
```

## `ep1\quest\minor_quests\mq303\scenes\mq303_04_bdprincess.scene`

69 graph nodes, 72 edges; 15 event-bearing sections, 86 events; 20 screenplay lines, 5 screenplay options, 3 choice nodes.

Actors: Shank (actor 0, spawnSet); Tool (actor 1, spawnSet); Lina_Malina (actor 2, spawnSet); lina_replacer (actor 3, community); Bodyguard (actor 4, community); train_of_thought (actor 5, community); Player (actor 6, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 42.

End nodes: 42: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 208 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnDialogLineEvent` | 14 | 208 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |
| `scnLookAtEvent` | 26 | 40 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 29 | 208 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scneventsEquipItemToPerformer` | 2 | 440 / 453 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/0` |
| `scneventsSocket` | 12 | 208 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, gaze: 2
- speech: 2
- gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation: 1
- idle_animation, props_equipment, socket_signal: 1
- gaze, props_equipment, socket_signal: 1

Raw SHA-256: `147f370c23a7fa697f07425ecbbf86594d991a4783caadb0cd54f026d9e31414`. Binary SHA-256: `c40cf477e27c1af4b8db7feeb357be90f7966d5fe5e17ec83bd1f3b6e3dac487`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq303\scenes\mq303_04_bdprincess.scene" --events
```

## `ep1\quest\minor_quests\mq303\scenes\mq303_06_vendor.scene`

89 graph nodes, 95 edges; 18 event-bearing sections, 115 events; 39 screenplay lines, 13 screenplay options, 8 choice nodes.

Actors: Tool (actor 0, spawnSet); Shank (actor 1, spawnSet); Johnny (actor 2, spawnDespawn); Player (actor 3, findInContext).

Entries: `Start_fia` → 1; `bd_fixed_in` → 86; `Start_tool_shop` → 88; `Start 1` → 14; `Start_fail` → 103; `Start_shock` → 28; `Start_lina_fail` → 124; `start_letter` → 142; `finale_fluff` → 227.

Exits: `End_lina_fail` → 216; `End_fail` → 218.

End nodes: 216: `NonTerminating`; 218: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 8 | 90 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/0` |
| `scnDialogLineEvent` | 36 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnLookAtEvent` | 37 | 6 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 22 | 10 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsSocket` | 12 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- gaze: 2
- speech: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `012b0789710431db54fac17c3dd4d780a0889675ae4fab10572a74ad4392c13e`. Binary SHA-256: `ba43da563c7e8e4ac22f2ef897fadebef1b747a61ebf2e247ef756498661451d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq303\scenes\mq303_06_vendor.scene" --events
```

