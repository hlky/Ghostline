# Epistrophy: Northside: scene presentation

Journal identity: `quests/side_quest/sq025c05_scared`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq025c05_scared.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\side_quests\sq025\scenes\sq025_05_scan.scene`

1710 graph nodes, 2004 edges; 75 event-bearing sections, 235 events; 189 screenplay lines, 28 screenplay options, 14 choice nodes.

Actors: Delamain (actor 0, spawnSet); Angry (actor 1, spawnSet); Sad (actor 2, spawnSet); Manic (actor 3, spawnSet); Mean (actor 4, spawnSet); Suicidal (actor 5, spawnSet); Deep (actor 6, spawnSet); Scared (actor 7, spawnSet); GANG_MLS_F_02_ENUS_25 (actor 8, community); GANG_MLS_F_03_ENUS_20 (actor 9, community); GANG_MLS_F_01_ENUS_30 (actor 10, community); GANG_MLS_F_04_ENUS_25 (actor 11, community); cyberpsycho (actor 12, community); Sad_voice (actor 13, findInContext); Deep_vehicle (actor 14, community); Angry_vehicle (actor 15, community); Suicidal_vehicle (actor 16, community); Mean_vehicle (actor 17, community); Scared_vehicle (actor 18, community); Sad_vehicle (actor 19, community); Manic_vehicle (actor 20, community); Player (actor 21, findInContext).

Entries: `angry_in` → 4; `sad_in` → 6; `suicidal_in` → 7; `deep_in` → 8; `scared_in` → 10; `manic_in` → 11; `mean_in` → 12; `Start 12` → 3670; `Start 13` → 3689; `Start 14` → 3706; `Start 15` → 3723; `Start 16` → 3737; `Start 18` → 3758; `Start 26` → 7546; `mobile1` → 7677; `Start 28` → 7801; `beep_in` → 4549; `blasphemer_in` → 6383; `sad_in_talk` → 2926; `angry_in_talk` → 2954; `suicidal_in_talk` → 2955; `deep_in_talk` → 2956; `scared_in_talk` → 2957; `manic_in_talk` → 2958; `mean_in_talk` → 2959; `Start 23` → 6960; `Start 24` → 6967; `Start 25` → 6992.

Exits: `angry_out` → 131; `suicidal_out` → 132; `deep_out` → 133; `scared_out` → 134; `mean_out` → 135; `reward_out` → 136; `manic_out` → 137; `sad_out` → 138; `sad_damage` → 7771; `sad_water` → 7775; `sad_crowd` → 7798; `sad_death` → 7802; `End 9` → 6391.

End nodes: 131: `<omitted>`; 132: `<omitted>`; 133: `<omitted>`; 134: `<omitted>`; 135: `<omitted>`; 136: `<omitted>`; 137: `<omitted>`; 138: `<omitted>`; 6391: `<omitted>`; 7771: `NonTerminating`; 7775: `NonTerminating`; 7798: `NonTerminating`; 7802: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 91 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scnDialogLineEvent` | 169 | 79 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 7933 / 7717 | `/Data/RootChunk/sceneGraph/Data/graph/1279/Data/events/4` |
| `scnIKEvent` | 2 | 7933 / 7715 | `/Data/RootChunk/sceneGraph/Data/graph/1279/Data/events/2` |
| `scnLookAtEvent` | 17 | 79 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/4` |
| `scnPlaySkAnimEvent` | 4 | 1503 / 1464 | `/Data/RootChunk/sceneGraph/Data/graph/245/Data/events/1` |
| `scnUnmountEvent` | 1 | 7933 / 7721 | `/Data/RootChunk/sceneGraph/Data/graph/1279/Data/events/7` |
| `scneventsCameraParamsEvent` | 3 | 6997 / 6162 | `/Data/RootChunk/sceneGraph/Data/graph/1023/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 1 | 7933 / 7719 | `/Data/RootChunk/sceneGraph/Data/graph/1279/Data/events/6` |
| `scneventsSocket` | 33 | 79 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 40
- speech, socket_signal: 19
- speech, gaze, socket_signal: 2
- speech, gaze: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- idle_animation, gaze, socket_signal: 2
- speech, idle_animation, gaze: 1
- speech, skeletal_animation: 1
- idle_animation, gaze: 1
- gaze: 1
- gaze, socket_signal: 1
- camera: 1
- camera, socket_signal: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `249ac0c15568c48faedb121c325c5b673bfe319ccda854d8b28d8ee49cb8859d`. Binary SHA-256: `728ee318df921d11651256032dd465e82c0c8169ddf91bcf326349d842b2366a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_05_scan.scene" --events
```

## `base\quest\side_quests\sq025\scenes\sq025_06b_reward_holocall.scene`

45 graph nodes, 58 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Delamain (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `continue_talk` → 268.

End nodes: 2: `<omitted>`; 268: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `e39c07bf002d623c8d52589fc86ee0359880993c526871f670566ff5438ebd60`. Binary SHA-256: `aa60741a78f8221cecb73416a677ae8b572cf74d8b7475a23b3d9eb3bb1d9895`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_06b_reward_holocall.scene" --events
```

