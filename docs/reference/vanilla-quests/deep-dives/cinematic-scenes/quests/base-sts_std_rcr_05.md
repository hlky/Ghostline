# Gig: Family Matters: scene presentation

Journal identity: `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_std_rcr_05.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene`

89 graph nodes, 83 edges; 8 event-bearing sections, 17 events; 17 screenplay lines, 5 screenplay options, 5 choice nodes.

Actors: johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `safe` → 1; `sedatives` → 4; `photo` → 6; `painting` → 8; `sedatives_no_johnny` → 101; `painting_no_johnny` → 103; `found_out` → 23; `blood` → 28; `medkit` → 34; `rose_room` → 39; `blood_no_johnny` → 150; `medkit_no_johnny` → 160.

Exits: `safe_end` → 2; `sedatives_end` → 5; `painting_end` → 9; `photo_end` → 15; `found_out_end` → 26; `blood_end` → 31; `medkit_end` → 35; `rose_room_end` → 43.

End nodes: 2: `<omitted>`; 5: `<omitted>`; 9: `<omitted>`; 15: `<omitted>`; 26: `<omitted>`; 31: `<omitted>`; 35: `<omitted>`; 43: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 17 | 10 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8

Raw SHA-256: `1549af73c359f9985282a79c4a42c06f0f5e8d33adbd17a9debe07525bbc5e2f`. Binary SHA-256: `8f814e1097fa45e2ab38dd62a10b592a1d5eb82717ee3d3a8972e63dcdef1d2e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_clues.scene" --events
```

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene`

23 graph nodes, 30 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 285.

End nodes: 2: `<omitted>`; 285: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 27 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `bf9f99e88b4df4a606d57c65dce79c1c06b0b69255bb128c381c1a297c8aa8b5`. Binary SHA-256: `c37a6e8262626c0f52202e5219f0519171d242cc0a4f8ec7b17e2f5dd9b562ae`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `f09255a952b0e3d49f845484cd53b03ad1c04888923e7ac1000f832cbddd889f`. Binary SHA-256: `f3041f6ed02abc7d34444e9090eec2a3b3b0c4a6d3d9b62abeacd866e392d490`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_05\scenes\sts_std_rcr_05_holocall_prebrief.scene" --events
```

