# Love Like Fire: scene presentation

Journal identity: `quests/main_quest/act_01/q101_01_firestorm`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q101_01_firestorm.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q101\scenes\q101_06c_memories_backalley_p1.scene`

158 graph nodes, 214 edges; 30 event-bearing sections, 235 events; 41 screenplay lines, 7 screenplay options, 5 choice nodes.

Actors: Kerry (actor 0, spawnSet); Rogue (actor 1, spawnSet); netrunner (actor 2, community); shaitan (actor 3, community); punk_fem1 (actor 4, community); punk_fem2 (actor 5, community); backstage_guy (actor 6, community); choppa (actor 7, spawnSet); Johnny (actor 8, findInContext).

Entries: `heli_preview` → 1436; `kerry_scene` → 241; `Start 16` → 1322.

Exits: `kerry_scene_out` → 366.

End nodes: 366: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 14 | 247 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scnChangeIdleAnimEvent` | 18 | 247 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnDialogLineEvent` | 26 | 247 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scnGameplayTransitionEvent` | 3 | 321 / 116 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/24` |
| `scnIKEvent` | 6 | 321 / 97 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/9` |
| `scnLookAtEvent` | 29 | 247 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 41 | 247 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPoseCorrectionEvent` | 2 | 333 / 192 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/5` |
| `scnUnmountEvent` | 3 | 321 / 121 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/28` |
| `scneventsAttachPropToNode` | 3 | 321 / 115 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/23` |
| `scneventsAttachPropToPerformer` | 8 | 247 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scneventsAttachPropToWorld` | 1 | 586 / 272 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/7` |
| `scneventsCameraParamsEvent` | 5 | 247 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 10 | 321 / 119 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/27` |
| `scneventsSocket` | 54 | 247 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/9` |
| `scneventsVFXEvent` | 12 | 287 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 6
- speech: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- speech, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- skeletal_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation: 1
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx: 1

Raw SHA-256: `50f4f1ae1f240fd53660979c893c0b31f5d1aacb0c91ac4123f2b2b661189e9b`. Binary SHA-256: `2a1ca73cf442c198f2267330aeee63d01542b2b10f7a8c8922803baded01c6ec`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q101\scenes\q101_06c_memories_backalley_p1.scene" --events
```

## `base\quest\main_quests\part1\q101\scenes\q101_06c_memories_p1.scene`

164 graph nodes, 173 edges; 15 event-bearing sections, 196 events; 19 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: Kerry (actor 0, spawnSet); Parasite (actor 1, community); Security (actor 2, community); Punk_fem (actor 3, community); Denny (actor 4, spawnSet); Henry (actor 5, spawnSet); Nancy (actor 6, spawnSet); mirror_johnny (actor 7, spawnDespawn); fem1 (actor 8, spawnDespawn); fem2 (actor 9, spawnDespawn); fem3 (actor 10, spawnDespawn); fem4 (actor 11, spawnDespawn); male1 (actor 12, spawnDespawn); male2 (actor 13, spawnDespawn); male3 (actor 14, spawnDespawn); male4 (actor 15, spawnDespawn); Johnny (actor 16, findInContext).

Entries: `Start 15` → 828; `parasite_preview` → 1113; `parasite_in` → 295; `Start 16` → 906.

Exits: `parasite_out` → 296.

End nodes: 296: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 219 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/5` |
| `scnChangeIdleAnimEvent` | 23 | 444 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnDialogLineEvent` | 10 | 219 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/8` |
| `scnLookAtEvent` | 22 | 219 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/6` |
| `scnPlaySkAnimEvent` | 64 | 219 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnPoseCorrectionEvent` | 1 | 680 / 260 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/17` |
| `scneventsAttachPropToPerformer` | 14 | 219 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scneventsCameraParamsEvent` | 2 | 786 / 312 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/11` |
| `scneventsEquipItemToPerformer` | 2 | 1471 / 1113 | `/Data/RootChunk/sceneGraph/Data/graph/135/Data/events/6` |
| `scneventsSocket` | 51 | 219 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/16` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 786 / 335 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/24` |
| `scneventsVFXEvent` | 1 | 219 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/22` |

Presentation families coexisting in an event section (counts are sections, not durations):

- idle_animation, gaze: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, props_equipment, socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- speech, idle_animation: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment: 1
- speech: 1

Raw SHA-256: `3403925fb9cf26fec4a25afea2fc4979e52dcd948a4580c30b0862b7e9bb4823`. Binary SHA-256: `cf67115d67493c4657d97145dddb0d0cb3b46670da409c8d7bdcd533c168f4c9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q101\scenes\q101_06c_memories_p1.scene" --events
```

## `base\quest\main_quests\part1\q101\scenes\q101_06c_memories_p2.scene`

489 graph nodes, 561 edges; 58 event-bearing sections, 519 events; 107 screenplay lines, 8 screenplay options, 7 choice nodes.

Actors: Rogue (actor 0, spawnSet); Thompson (actor 1, spawnSet); Smasher (actor 2, spawnSet); shaitan (actor 3, community); thompson_radio (actor 4, findInContext); netrunner (actor 5, community); tv_news (actor 6, findInContext); netrunner_phone (actor 7, findInContext); Pilot (actor 8, community); soldier (actor 9, community); soldier2 (actor 10, community); soldier_hallway5 (actor 11, community); soldier3 (actor 12, community); soldier4 (actor 13, community); soldier5 (actor 14, community); soldier6 (actor 15, community); choppa (actor 16, spawnSet); Johnny (actor 17, findInContext); Player (actor 18, findInContext).

Entries: `Start2` → 3261; `Start 17` → 3278; `Start 16` → 2364; `flight_to_arasaka` → 109; `escape_starts_in` → 124; `saburo_pc` → 146; `kill_forces` → 151; `Start1` → 2462; `enter_av_in` → 178; `rogue_hurry_johnny_in` → 1586; `murphy_about_doors_in` → 1615; `johnny_combat_lines_in` → 1625; `test_from_door` → 2143; `spider_chat_in` → 1273; `Start 15` → 2213.

Exits: `roof_approach_out` → 120; `escape_starts_out` → 125; `saburo_pc_out` → 147; `kill_forces_out` → 152; `enter_av_out` → 179; `rogue_hurry_johnny_out` → 1589; `murphy_about_doors_out` → 1616; `johnny_combat_lines_out` → 1661; `spider_chat_out` → 1274.

End nodes: 120: `NonTerminating`; 125: `<omitted>`; 147: `<omitted>`; 152: `<omitted>`; 179: `<omitted>`; 1274: `<omitted>`; 1589: `<omitted>`; 1616: `<omitted>`; 1661: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 33 | 701 / 283 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/4` |
| `scnChangeIdleAnimEvent` | 27 | 629 / 106 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/16` |
| `scnDialogLineEvent` | 84 | 121 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 3 | 633 / 150 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/5` |
| `scnGameplayTransitionEvent` | 4 | 148 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/21` |
| `scnIKEvent` | 8 | 148 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/17` |
| `scnLookAtAdvancedEvent` | 4 | 963 / 675 | `/Data/RootChunk/sceneGraph/Data/graph/66/Data/events/22` |
| `scnLookAtEvent` | 47 | 629 / 85 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/5` |
| `scnPlaySkAnimEvent` | 101 | 148 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/14` |
| `scnUnmountEvent` | 4 | 148 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/25` |
| `scneventsAttachPropToNode` | 1 | 1103 / 964 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/64` |
| `scneventsAttachPropToPerformer` | 11 | 701 / 298 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/14` |
| `scneventsAttachPropToWorld` | 10 | 148 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/26` |
| `scneventsSetAnimFeatureEvent` | 18 | 148 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/22` |
| `scneventsSocket` | 101 | 148 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/3` |
| `scneventsVFXDurationEvent` | 1 | 1103 / 904 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/15` |
| `scneventsVFXEvent` | 62 | 245 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 17
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, socket_signal: 2
- gaze: 2
- speech, skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state, gameplay_action: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal, animation_state: 1
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, vfx, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- idle_animation, props_equipment, vfx, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, idle_animation, vfx, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal: 1
- idle_animation, gaze, gameplay_action: 1
- idle_animation, vfx, socket_signal, animation_state: 1
- idle_animation: 1
- skeletal_animation, idle_animation: 1
- vfx: 1

Raw SHA-256: `0d20474fb069c464f42940cbb9fec5f9af0ada7fd11b329275dfbefbf56c9b87`. Binary SHA-256: `ba27ef78c443d8a1928db510b8d606d2e9d05b862af09117e50301e74cda2b27`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q101\scenes\q101_06c_memories_p2.scene" --events
```

