# base-ma-hey-spr-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_01\ma_hey_spr_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_01\ma_hey_spr_01.quest` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_01\ma_hey_spr_01_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questInputNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_01\ma_hey_spr_01_phase.questphase` / h0 / 19 -> 21 -> 18 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_01\ma_hey_spr_01_phase.questphase` / h0 / 0 -> 19 -> 21 |
| `4d6c55ba26916a1e04f1` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_01\ma_hey_spr_01_phase.questphase` / h0 / 19 -> 21 -> 1 |
| `9661fbbfa2ff9c12f5af` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_01\ma_hey_spr_01_phase.questphase` / h0 / 21 -> 18 -> 1 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
