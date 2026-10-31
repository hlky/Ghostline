# Gig: Radar Love: scene presentation

Journal identity: `quests/street_stories/badlands/inland_avenue/sts_bls_ina_04`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_bls_ina_04.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_04\scenes\sts_bls_ina_04_guards_chats.scene`

12 graph nodes, 12 edges; 3 event-bearing sections, 11 events; 11 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: officer (actor 0, findInWorld); guard_02 (actor 1, findInWorld); techie_booth (actor 2, findInWorld).

Entries: `officer_scene` → 1; `office_phone_chat` → 41; `officer_phone_chat` → 30.

Exits: `End1` → 57; `officer_phone_chat_out` → 47; `officer_scene_out` → 23.

End nodes: 23: `<omitted>`; 47: `<omitted>`; 57: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 11 | 3 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3

Raw SHA-256: `66712a50726e33384402d95b5170fa61edd8fbedc57893624ed219a5d6733965`. Binary SHA-256: `f2955f48bfaae41f35b7f3e268f991ca296f9f00a4ed0c606db111aa8cb26b66`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_04\scenes\sts_bls_ina_04_guards_chats.scene" --events
```

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_04\scenes\sts_bls_ina_04_holocall_debriefs.scene`

27 graph nodes, 35 edges; 2 event-bearing sections, 6 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Dakota (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 21.

Exits: `rejected_out` → 289; `End 0` → 26.

End nodes: 26: `<omitted>`; 289: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 6 | 28 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `1695b90b8aba82fe419a7d7c182eb39dec14de7b6af4625ff1a39b4abce343ac`. Binary SHA-256: `6fc16156c247623fe848651a61b49d3dca99dea749316438d9122caa6240ad92`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_04\scenes\sts_bls_ina_04_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_04\scenes\sts_bls_ina_04_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Dakota (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 15.

Exits: `End 0` → 16; `rejected_out` → 260.

End nodes: 16: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 18 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `72415e5b9fbe3e0d018bbe163eed52fc304e0fc739e11441dc8280ddf88da1b5`. Binary SHA-256: `5949af930039fc9a23a3fa758c285bf4dfb7dcdfa5d36b91f0a4f00912d70e24`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_04\scenes\sts_bls_ina_04_holocall_prebrief.scene" --events
```

