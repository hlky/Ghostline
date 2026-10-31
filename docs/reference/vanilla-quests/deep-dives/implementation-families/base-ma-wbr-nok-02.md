# base-ma-wbr-nok-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_02\ma_wbr_nok_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_02\ma_wbr_nok_02.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_02\ma_wbr_nok_02_phase.questphase |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_02\ma_wbr_nok_02_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questInputNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questStartNodeDefinition` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_02\ma_wbr_nok_02_phase.questphase` / h0 / 16 -> 23 -> 15 |
| `4d6c55ba26916a1e04f1` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_02\ma_wbr_nok_02_phase.questphase` / h0 / 16 -> 23 -> 1 |
| `79d5c71726a61b77a50e` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_02\ma_wbr_nok_02_phase.questphase` / h0 / 0 -> 3 -> 16 |
| `9661fbbfa2ff9c12f5af` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_02\ma_wbr_nok_02_phase.questphase` / h0 / 23 -> 15 -> 1 |
| `ff4c8a828496c45d7dfa` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_02\ma_wbr_nok_02_phase.questphase` / h0 / 3 -> 16 -> 23 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
