# Gig: Fixer, Merc, Soldier, Spy: scene presentation

Journal identity: `quests/street_stories/watson/kabuki/sts_wat_kab_04`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wat_kab_04.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_04\scenes\sts_wat_kab_04_give_the_shard.scene`

56 graph nodes, 61 edges; 14 event-bearing sections, 119 events; 45 screenplay lines, 6 screenplay options, 4 choice nodes.

Actors: Regina (actor 0, spawnSet); china_guy (actor 1, community); china_guy2 (actor 2, community); china_guy_3 (actor 3, community); limo (actor 4, community); Player (actor 5, findInContext).

Entries: `kab_04_limo_start` → 1; `kab_04_regina_call_start` → 16; `Start1` → 225.

Exits: `kab_04_limo_end` → 2; `kab_04_regina_call_end` → 17.

End nodes: 2: `NonTerminating`; 17: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 70 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |
| `scnDialogLineEvent` | 32 | 5 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 66 / 160 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/11` |
| `scnIKEvent` | 2 | 66 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/4` |
| `scnLookAtEvent` | 27 | 5 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 163 / 202 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scnPlaySkAnimEvent` | 31 | 5 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 1 | 66 / 159 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/10` |
| `scneventsAttachPropToPerformer` | 2 | 255 / 229 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/3` |
| `scneventsAttachPropToWorld` | 1 | 255 / 233 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 2 | 66 / 157 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/9` |
| `scneventsSocket` | 11 | 27 / 101 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/10` |
| `scneventsVFXEvent` | 4 | 12 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 4
- speech, skeletal_animation: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, vfx: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1

Raw SHA-256: `e803b6e4b6eee6ce080cc355279ecde304ab1e17ea725e2bf0abcbdbbe1f4471`. Binary SHA-256: `cf607c56a7b172c5f97f470384dc1d0f575957242dd8484ac6097ba8a863b53a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_04\scenes\sts_wat_kab_04_give_the_shard.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_04\scenes\sts_wat_kab_04_holocall_debriefs.scene`

29 graph nodes, 35 edges; 3 event-bearing sections, 9 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: regina (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `rejected_out` → 291; `End 0` → 2.

End nodes: 2: `<omitted>`; 291: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 6 | 24 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 3 | 24 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 3

Raw SHA-256: `95cf6aea46c5319caf91a710337fe46531f2c1f3374e00c1913ee04aeb4c1a99`. Binary SHA-256: `9c82471ce1c738c867e6082f351d10faa380204a555f79fc68e7f8904846c4c8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_04\scenes\sts_wat_kab_04_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_04\scenes\sts_wat_kab_04_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: regina (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 24 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 1 | 24 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 1

Raw SHA-256: `40cb0b466a3363af489253f0df729fbaf26c73bfe07c2fb378b76cbe84a12521`. Binary SHA-256: `9818c8d10c1e9368aae27fd951b718ad42d118472f99c34a1bc9f56b103c8220`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_04\scenes\sts_wat_kab_04_holocall_prebrief.scene" --events
```

