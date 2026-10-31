# Gig: Dancing on a Minefield: scene presentation

Journal identity: `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_bls_ina_07.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\scenes\sts_bls_ina_07_comments.scene`

20 graph nodes, 18 edges; 2 event-bearing sections, 7 events; 5 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: dakota (actor 0, findInWorld); johnny (actor 1, spawnDespawn); smuggler (actor 2, findInWorld); car (actor 3, community); v (actor 4, findInContext).

Entries: `js_on_chase` → 266; `body_choice_hub` → 183.

Exits: `body_choice_out` → 342; `js_on_chase_out` → 269.

End nodes: 269: `<omitted>`; 342: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 5 | 188 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnLookAtEvent` | 2 | 267 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1
- speech, gaze: 1

Raw SHA-256: `441359fece7369bb8b42d949ded1eec939b6e3aa09874ac391a29ef92435f498`. Binary SHA-256: `33d5515239c9e822169b610831a7da1be721ec32fa047aa233bf49fa00cb15c3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\scenes\sts_bls_ina_07_comments.scene" --events
```

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\scenes\sts_bls_ina_07_holocall_debriefs.scene`

26 graph nodes, 34 edges; 2 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: dakota (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 290.

End nodes: 2: `<omitted>`; 290: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 29 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `0e980d925ee4ddf1bb425126e4f261f45e61494b9e3e0582eaf8b8e5acba1383`. Binary SHA-256: `24392838cb12f6247f940053f7bf93910bc85f579df858fed4f4c36d09ebc09f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\scenes\sts_bls_ina_07_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\scenes\sts_bls_ina_07_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: dakota (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `53d96fde5486975d34f5599193bd1a53faa5bc72f1a9fbcac551e8e411a75569`. Binary SHA-256: `58bc7e609cea6496b407371a8f49833319db7483af17595b6fb7d0c0a6d3c495`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\scenes\sts_bls_ina_07_holocall_prebrief.scene" --events
```

