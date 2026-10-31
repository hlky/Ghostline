# NO_TITLE: scene presentation

Journal identity: `quests/minor_quest/mq009_loser`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq009_loser.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene`

47 graph nodes, 49 edges; 24 event-bearing sections, 83 events; 83 screenplay lines, 15 screenplay options, 6 choice nodes.

Actors: Ken_Lee (actor 0, community); Homeless_1 (actor 1, community); Homeless_2 (actor 2, community); Johnny (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `help_in` → 1; `story_pill_in` → 49; `story_nopill_in` → 51; `kicking_in` → 7; `wtf_in` → 12; `kick_ass_in` → 17; `thank_in` → 22.

Exits: `help_out` → 2; `story_pill_out` → 50; `story_nopill_out` → 52; `kicking_out` → 8; `wtf_out` → 13; `kick_ass_out` → 18; `pills_yes_out` → 23; `pills_no_out` → 32.

End nodes: 2: `<omitted>`; 8: `<omitted>`; 13: `<omitted>`; 18: `<omitted>`; 23: `<omitted>`; 32: `<omitted>`; 50: `<omitted>`; 52: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 83 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 24

Raw SHA-256: `119593b30b5dd85032bf2ba844045a172f552d1000b969ff85ae3438aac8bf83`. Binary SHA-256: `5da057e4133892bae69c3b7d3fa85f830d3bc2ed91960c32ebc5f951a5d43248`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene" --events
```

## `base\quest\minor_quests\mq009\scenes\mq009_02_second_meeting.scene`

54 graph nodes, 54 edges; 21 event-bearing sections, 63 events; 63 screenplay lines, 18 screenplay options, 9 choice nodes.

Actors: Ken_Lee (actor 0, community); Player (actor 1, findInContext).

Entries: `meeting_in` → 1; `approaches_in` → 7; `sit_in` → 11; `story_in` → 17; `teleport_in` → 37; `back_in` → 95.

Exits: `meeting_out` → 2; `approaches_out` → 8; `sit_out` → 12; `agree_out` → 25; `refuse_out` → 32; `mq009_suspended` → 90; `teleport_yes` → 38; `teleport_no` → 39; `back_out'` → 96.

End nodes: 2: `<omitted>`; 8: `<omitted>`; 12: `<omitted>`; 25: `<omitted>`; 32: `<omitted>`; 38: `<omitted>`; 39: `<omitted>`; 90: `<omitted>`; 96: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 63 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 21

Raw SHA-256: `918782caab6cdf45cc342b6126108bb3b5a81828a763531ecd7248de129db274`. Binary SHA-256: `92f772218410edd2c37be1dc988880800131b217b36ad518ff5406c32dd44deb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq009\scenes\mq009_02_second_meeting.scene" --events
```

## `base\quest\minor_quests\mq009\scenes\mq009_03_execution.scene`

33 graph nodes, 33 edges; 16 event-bearing sections, 48 events; 48 screenplay lines, 8 screenplay options, 3 choice nodes.

Actors: Ken_Lee (actor 0, community); Player (actor 1, findInContext).

Entries: `leaving_in` → 7; `suicide_in` → 41; `follow_in` → 12; `execution_in` → 17; `death_in` → 22; `cartalk_in` → 28.

Exits: `leaving_out` → 8; `suicide_out` → 42; `follow_out` → 13; `ken_lives_out` → 83; `execution_out` → 18; `death_out` → 24; `cartalk_out` → 29.

End nodes: 8: `<omitted>`; 13: `<omitted>`; 18: `<omitted>`; 24: `<omitted>`; 29: `<omitted>`; 42: `<omitted>`; 83: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 48 | 9 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 16

Raw SHA-256: `b0333197f2a17188249ce9456823667831debd5225932ce9d6fdfbe5c1b46be9`. Binary SHA-256: `06cab08749ffd56d03b7a40968de2b3c317837d55e7dee362bbdb1929fbfa113`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq009\scenes\mq009_03_execution.scene" --events
```

