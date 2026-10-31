# Gig: Hacking the Hacker: scene presentation

Journal identity: `quests/street_stories/santo_domingo/arroyo/sts_std_arr_11`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_std_arr_11.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene`

25 graph nodes, 33 edges; 2 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 21.

Exits: `End 0` → 22; `rejected_out` → 299.

End nodes: 22: `<omitted>`; 299: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 28 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `d943bc36f4c1502b2206d9d3eebdbd41cbdc9474243c301497f7288768d35692`. Binary SHA-256: `bc4a2e59133ce055008927ae0d90e3fe206c4ba9765732a451777181383c421c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_debrief.scene" --events
```

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_prebiref.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 24 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `335e5ffcce721f880effdbabfa3aaa89d4c44cb237446989860eedb79933db45`. Binary SHA-256: `22cf256630a568c4042e41e290199b9e9f103bbe9c026d9da2e2788dd684ca1d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_holocall_prebiref.scene" --events
```

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_scene.scene`

3 graph nodes, 2 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: enemy_003 (actor 0, community); lucius (actor 1, community); Player (actor 2, findInContext).

Entries: `arr_11_enemy_003_start` → 58.

Exits: `arr_11_enemy_003_end` → 59.

End nodes: 59: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 3. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 60 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `84742027d08da96271995929eef3b97b10e4aced0434eb2f0b7f5e2e38f24c3c`. Binary SHA-256: `71842c67bfb3e0f53ea9aaed7a84cfbd7e565707a8dc39408c8749dccc6ec83b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_11\scenes\sts_std_arr_11_scene.scene" --events
```

