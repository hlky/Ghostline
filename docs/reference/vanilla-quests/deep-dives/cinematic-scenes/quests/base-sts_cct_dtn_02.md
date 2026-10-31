# Gig: An Inconvenient Killer: scene presentation

Journal identity: `quests/street_stories/city_center/downtown/sts_cct_dtn_02`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_cct_dtn_02.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_02\scenes\sts_cct_dtn_02_chats.scene`

3 graph nodes, 2 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: angry_guest_001 (actor 0, findInWorld); angry_guest_002 (actor 1, findInWorld).

Entries: `dtn_02_angry_start` → 7.

Exits: `dtn_02_angry_end` → 8.

End nodes: 8: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 9 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `34b179db92965a85a37e1cac7c8a023476387d1c0069c70962d96050022b946d`. Binary SHA-256: `6399916d6146df44edf4ab2c2e5f954fa9c9bf88821d35f4f2893bb437f2bc49`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\downtown\sts_cct_dtn_02\scenes\sts_cct_dtn_02_chats.scene" --events
```

## `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_02\scenes\sts_cct_dtn_02_holocall_debriefs.scene`

31 graph nodes, 41 edges; 4 event-bearing sections, 7 events; 7 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Dino (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 289.

End nodes: 2: `<omitted>`; 289: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 7 | 28 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4

Raw SHA-256: `9d9beb7450ef81ac90b624e9a212c71512eb063dbd51e00dca95eee23caae3c5`. Binary SHA-256: `09fa983b740e40b1e3b3a0e33a044682d41734229fea7453706d059180e2bbd0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\downtown\sts_cct_dtn_02\scenes\sts_cct_dtn_02_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_02\scenes\sts_cct_dtn_02_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Dino (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `9a1e221f1ad7334235fef44cb842935cb568ee7fb2f39342dcfdae7f98db1f7f`. Binary SHA-256: `9db049ef4191aad0d250e5feb5407c612b3747788bec42d0c2398bdb24655559`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\downtown\sts_cct_dtn_02\scenes\sts_cct_dtn_02_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_02\scenes\sts_cct_dtn_02_johnny.scene`

16 graph nodes, 18 edges; 3 event-bearing sections, 13 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `Start1` → 47.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 80 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnDialogLineEvent` | 4 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 2 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 3 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsSocket` | 2 | 80 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze: 1

Raw SHA-256: `a3b982ac0116d15142c3b7097e65b7ea33395059ccc93c473b6c651611e0bbaa`. Binary SHA-256: `07d7304913aa42cf8e96209c660e25ef8440bb92476e952c9dc80cfcff277e96`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\downtown\sts_cct_dtn_02\scenes\sts_cct_dtn_02_johnny.scene" --events
```

