# base-ma-cct-dtn-17

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_17\ma_cct_dtn_17.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_17\ma_cct_dtn_17.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_17\ma_cct_dtn_17_phase.questphase |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_17\ma_cct_dtn_17_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questStartNodeDefinition` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `12ebeacaf18b2248e461` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_17\ma_cct_dtn_17_phase.questphase` / h0 / 12 -> 2 -> 1 |
| `4046f7e0ed1087267da3` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_17\ma_cct_dtn_17_phase.questphase` / h0 / 3 -> 12 -> 2 |
| `71892f49b88f7b8bb8be` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_17\ma_cct_dtn_17_phase.questphase` / h0 / 0 -> 3 -> 12 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
