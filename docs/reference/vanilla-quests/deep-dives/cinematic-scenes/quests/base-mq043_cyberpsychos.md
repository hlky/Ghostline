# Psycho Killer: scene presentation

Journal identity: `quests/minor_quest/mq043_cyberpsychos`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq043_cyberpsychos.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\fixers\reggie\scenes\reggie_default.scene`

151 graph nodes, 161 edges; 25 event-bearing sections, 144 events; 62 screenplay lines, 7 screenplay options, 1 choice nodes.

Actors: regina (actor 0, spawnSet); regina_holo (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `psycho_intro_in` → 290; `reggie_default_holo_in` → 596; `Start 5` → 1014; `all_psychos_one_out` → 325; `welcome` → 82.

Exits: `holo_to_face` → 701; `psycho_intro_out` → 303; `all_psychos_done_out` → 328; `welcome_out` → 765; `reggie_default_holo_out` → 641.

End nodes: 303: `<omitted>`; 328: `<omitted>`; 641: `<omitted>`; 701: `NonTerminating`; 765: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 5. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 9 | 90 / 138 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnDialogLineEvent` | 54 | 62 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 11 | 62 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 30 | 62 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPoseCorrectionEvent` | 6 | 65 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scneventsSocket` | 34 | 62 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 2
- gaze: 2
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, idle_animation, gaze, socket_signal: 1
- gaze, socket_signal: 1
- gaze, socket_signal, animation_state: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, socket_signal, animation_state: 1
- idle_animation, gaze: 1
- socket_signal: 1

Raw SHA-256: `5f207ca732501738d9dfccc670b8b69e086b9273aabf5acdb81fe49e048b50a4`. Binary SHA-256: `0bbce4beb5ef0160a3b98ed4694f4bf9e4914bd76819929e6edf978b6982ebd0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\fixers\reggie\scenes\reggie_default.scene" --events
```

