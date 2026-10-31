# Where Eagles Dare: scene presentation

Journal identity: `quests/minor_quest/mq058_semimaru_crystalcoat`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq058_semimaru_crystalcoat.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq058\scenes\mq058_scene_test.scene`

39 graph nodes, 37 edges; 2 event-bearing sections, 33 events; 7 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: Player (actor 0, findInContext).

Entries: `Start_Extract_Computer_Data` → 1; `Start_Transfer_Semimaru_Data` → 97.

Exits: `End_Extract_Computer_Data` → 2; `End_Transfer_Semimaru_Data` → 102.

End nodes: 2: `<omitted>`; 102: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 16 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 16 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |
| `scnIKEvent` | 4 | 16 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scnPlaySkAnimEvent` | 6 | 16 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 1 | 16 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |
| `scneventsSetAnimFeatureEvent` | 2 | 16 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scneventsSocket` | 14 | 16 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state: 1

Raw SHA-256: `a69d0b1dd658a48a4fabdf9bdb865da71cb355afead0e5c0b0e0763624d5e389`. Binary SHA-256: `cb813b0822d95866c3265851b40c99366d870e1e477efef23efcde9f586b3eb0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq058\scenes\mq058_scene_test.scene" --events
```

## `base\quest\minor_quests\mq058\scenes\mq058_voicelines.scene`

9 graph nodes, 8 edges; 4 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Player (actor 0, findInContext).

Entries: `Start_01_Mint_Hideout_Enemies` → 9; `Start_00_Semimaru_CrystalCoat_Bug` → 1; `Start_03_Semimaru_CrystalCoat_Unlocked` → 11; `Start_02_Mint_Computer_Extracted_Data` → 14.

Exits: `End_Test` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4

Raw SHA-256: `72ae26f3b32946f20b3cc8b14be8cc0ad6c58cd01c3408b74373f67aef0de7c9`. Binary SHA-256: `1bdb8c7cdb14431d092c39f47216435b8cc12054c21e3ed01875c15471a08818`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq058\scenes\mq058_voicelines.scene" --events
```

