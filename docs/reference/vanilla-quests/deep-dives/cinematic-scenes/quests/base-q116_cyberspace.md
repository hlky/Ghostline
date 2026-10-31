# Changes: scene presentation

Journal identity: `quests/main_quest/act_01/q116_cyberspace`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q116_cyberspace.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q116\scenes\q116_05_mikoshi.scene`

1293 graph nodes, 1708 edges; 229 event-bearing sections, 1540 events; 684 screenplay lines, 132 screenplay options, 80 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Alt (actor 1, spawnDespawn); v_male (actor 2, spawner); v_female (actor 3, spawner); jackie (actor 4, spawnSet); Alt_02 (actor 5, spawnDespawn); Alt_03 (actor 6, spawnDespawn); Alt_04 (actor 7, spawnDespawn); Alt_05 (actor 8, spawnDespawn); Alt_06 (actor 9, spawnDespawn); Alt_07 (actor 10, spawnDespawn); Alt_08 (actor 11, spawnDespawn); Alt_09 (actor 12, spawnDespawn); V (actor 13, findInContext); johnny_replacer_scene (actor 14, findInContext).

Entries: `q116_05_mikoshi_in` → 1; `Start 69` → 8450; `Start 48` → 3719; `Start 6` → 1365; `Start 49` → 3800; `Start 7` → 1443; `stopping_v0, b1, B` → 6192; `Start 8` → 1516; `Start 50` → 3939; `Start 20` → 2791; `Start 21` → 2799; `Start 22` → 2810; `V1, B1, B` → 2812; `Start 51` → 4006; `chicken_in` → 1663; `Start 24` → 2871; `Start 25` → 2875; `Start 65` → 6453; `V1, B0, AI` → 2897; `V1, B1, AI` → 2908; `Start 0` → 6486; `q115_preview` → 2937; `V0, B0, AI` → 2988; `V0, B0, B` → 3020; `V0, B1, B` → 3022; `V0, B1, AI` → 3025; `V1, B0, B` → 3027; `Start 34` → 3039; `Start 35` → 3056; `Start 36` → 3063; `Start 37` → 3072; `Start 38` → 3117; `Start 39` → 3144; `Start 57` → 5538; `alt_appears` → 3285; `truth_q114` → 3319; `V>1, B>1, +AI` → 2133; `V>A, B<1 + AI` → 2138; `V>1, B>1 + BODY` → 2140; `v_idles` → 4514; `V>1, B<1 + BODY` → 2142; `V<1, B>1 + AI` → 2144; `V<1, B<1 + AI` → 2146; `V<1, B>1 + BODY` → 2148; `V<1, B<1 + BODY` → 2149; `alt_show_bridge` → 3342; `Start 59` → 5726; `whiteroom` → 3356; `Start 60` → 5729; `Start 61` → 5731; `Start 62` → 5733; `q114_V_goes_BODY_SQ31 done, SQ32 didnt want the body` → 2175; `q114_V_goes_AI_SQ031 done, SQ032 wanted body` → 2177; `Start 63` → 5739; `alt_show_well` → 3380; `truth_q115` → 3409; `Start 46` → 3436; `Start 53` → 4660; `q115_whiteroom` → 4664; `Start 66` → 7040; `no_options_agressive` → 4672; `Start 68` → 8269; `body_only` → 7083; `Start 56` → 4723.

Exits: `q116_05_q202_out` → 39; `q116_05_q203_out` → 666; `q116_05_q204_out` → 667.

End nodes: 39: `<omitted>`; 666: `<omitted>`; 667: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 47 | 413 / 193 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/8` |
| `scnDialogLineEvent` | 334 | 306 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnGameplayTransitionEvent` | 9 | 1556 / 1990 | `/Data/RootChunk/sceneGraph/Data/graph/145/Data/events/10` |
| `scnIKEvent` | 18 | 1556 / 1981 | `/Data/RootChunk/sceneGraph/Data/graph/145/Data/events/2` |
| `scnLookAtEvent` | 332 | 319 / 114 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/2` |
| `scnPlaySkAnimEvent` | 372 | 309 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scnUnmountEvent` | 9 | 1556 / 1989 | `/Data/RootChunk/sceneGraph/Data/graph/145/Data/events/9` |
| `scneventsAttachPropToPerformer` | 2 | 471 / 419 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/10` |
| `scneventsAttachPropToWorld` | 1 | 1547 / 1946 | `/Data/RootChunk/sceneGraph/Data/graph/142/Data/events/0` |
| `scneventsCameraParamsEvent` | 2 | 1549 / 1962 | `/Data/RootChunk/sceneGraph/Data/graph/143/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 9 | 1556 / 1983 | `/Data/RootChunk/sceneGraph/Data/graph/145/Data/events/4` |
| `scneventsSocket` | 375 | 306 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/12` |
| `scneventsVFXEvent` | 30 | 547 / 1210 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/32` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 48
- socket_signal: 20
- speech, skeletal_animation, gaze, socket_signal: 19
- skeletal_animation, socket_signal: 16
- speech, skeletal_animation, socket_signal: 13
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 12
- skeletal_animation, gaze, socket_signal: 12
- speech, gaze: 11
- skeletal_animation, vfx, socket_signal: 9
- speech, skeletal_animation, gaze: 6
- vfx, socket_signal: 6
- speech, socket_signal: 5
- speech, skeletal_animation: 5
- skeletal_animation: 5
- speech, skeletal_animation, idle_animation: 4
- gaze, socket_signal: 4
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, gaze, socket_signal: 3
- skeletal_animation, gaze, vfx, socket_signal: 3
- speech, idle_animation: 3
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- gaze, vfx, socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, props_equipment, vfx, socket_signal: 1
- skeletal_animation, camera, socket_signal: 1
- skeletal_animation, ik, camera, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- skeletal_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gaze, socket_signal: 1
- props_equipment, socket_signal: 1

Raw SHA-256: `e950939766a3c52e9ee26c35d95311ff1fc91d63dcc77f368d0a2f3bfb1799f7`. Binary SHA-256: `6a8f9f2be57f1eb06254704eafb673451543129cb9a0314c600c59badcd915cb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q116\scenes\q116_05_mikoshi.scene" --events
```

## `base\quest\main_quests\part1\q116\scenes\q116_05a_ripperdoc_roof.scene`

191 graph nodes, 232 edges; 27 event-bearing sections, 125 events; 72 screenplay lines, 22 screenplay options, 6 choice nodes.

Actors: jackie (actor 0, spawnSet); cat (actor 1, spawner); cat_2 (actor 2, spawner); V (actor 3, findInContext); johnny_replacer_scene (actor 4, findInContext).

Entries: `q116_05a_in` → 1; `Start 2` → 250; `Start 3` → 260; `Start 10` → 913; `Start 4` → 298; `Start 5` → 300; `Start 11` → 3549; `Start 6` → 312; `Start 7` → 751; `Start 8` → 753; `Start 9` → 755; `Start 0` → 765; `Start 1` → 183.

Exits: `q116_05a_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 152 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/4` |
| `scnDialogLineEvent` | 14 | 152 / 119 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/3` |
| `scnGameplayTransitionEvent` | 2 | 918 / 927 | `/Data/RootChunk/sceneGraph/Data/graph/144/Data/events/6` |
| `scnIKEvent` | 4 | 918 / 918 | `/Data/RootChunk/sceneGraph/Data/graph/144/Data/events/1` |
| `scnLookAtEvent` | 22 | 152 / 118 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/2` |
| `scnPlaySkAnimEvent` | 34 | 152 / 112 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/0` |
| `scnUnmountEvent` | 2 | 918 / 932 | `/Data/RootChunk/sceneGraph/Data/graph/144/Data/events/10` |
| `scneventsCameraParamsEvent` | 5 | 162 / 220 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 2 | 918 / 930 | `/Data/RootChunk/sceneGraph/Data/graph/144/Data/events/9` |
| `scneventsSocket` | 31 | 152 / 121 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/5` |
| `scneventsVFXEvent` | 4 | 509 / 625 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- skeletal_animation: 3
- speech, socket_signal: 2
- vfx: 2
- gaze: 2
- camera: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, camera, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, socket_signal: 1
- idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, camera, socket_signal: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `95e3d8688e162a4a5c191bfe584b7dcc88b2a263ff6f4513b64f35a87933d1c1`. Binary SHA-256: `7b7c728ab15e9ec317443b2c30eb825a080dfb653f3c93e169f2c6c83dc99e10`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q116\scenes\q116_05a_ripperdoc_roof.scene" --events
```

