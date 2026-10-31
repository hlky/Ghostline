# Cyberpsycho Sighting: Lt. Mower: scene presentation

Journal identity: `quests/minor_quest/ma_wat_kab_08`. Stored type: **CyberPsycho**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-ma_wat_kab_08.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\scenes\ma_wat_kab_08_brief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `ma_wat_kab_08_brief_in` → 1.

Exits: `ma_wat_kab_08_brief_out` → 2; `rejected_out` → 391.

End nodes: 2: `<omitted>`; 391: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 5 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `68541f3625df83b1e16f91648fe9f9de641bce916f25ea6beab14a67d5c082c4`. Binary SHA-256: `d4fa783ee3a8252d90287a9f239cf65f22bb87c1dacd197318c2138962dee090`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\scenes\ma_wat_kab_08_brief.scene" --events
```

## `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\scenes\ma_wat_kab_08_johnny_and_clues.scene`

18 graph nodes, 18 edges; 3 event-bearing sections, 20 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Mower (actor 0, community); Militech_001 (actor 1, community); Militech_002 (actor 2, community); V (actor 3, findInContext).

Entries: `ma_wat_kab_08_militech_in` → 48; `ma_wat_kab_08_mower_throw_in` → 34.

Exits: `ma_wat_kab_08_militech_cleanup_out` → 112; `ma_wat_kab_08_militech_001_out` → 101; `ma_wat_kab_08_militech_002_out` → 103.

End nodes: 101: `NonTerminating`; 103: `NonTerminating`; 112: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnGameplayTransitionEvent` | 2 | 57 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/6` |
| `scnIKEvent` | 4 | 57 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scnPlaySkAnimEvent` | 4 | 35 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnUnmountEvent` | 2 | 57 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 2 | 57 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/7` |
| `scneventsSocket` | 6 | 49 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 1
- socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `f11c02e60f30bffec4608374fc31c5c719282c6aafbd472db3f5dae2a90296bf`. Binary SHA-256: `5953537ca94a81ad95de4b36aca88a3a6a3ce2afc6f0a9e5f46b69c7a51692f2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\scenes\ma_wat_kab_08_johnny_and_clues.scene" --events
```

