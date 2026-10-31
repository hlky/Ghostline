# base-ma-cct-dtn-16

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_16\community\ma_cct_dtn_16_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_16\ma_cct_dtn_16_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questEventManagerNodeDefinition` | 1 |
| `questInputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 1 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_16\ma_cct_dtn_16_phase.questphase` / h0 / 1 -> 4 -> 6 |
| `7ee29249cbf782ce455c` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_16\ma_cct_dtn_16_phase.questphase` / h0 / 1 -> 4 -> 5 |
| `8d10896873df5c62014e` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_16\ma_cct_dtn_16_phase.questphase` / h0 / 0 -> 1 -> 4 |
| `987122e5e2fcd167cf6c` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_16\ma_cct_dtn_16_phase.questphase` / h0 / 2 -> 0 -> 1 |
| `e76c50792d1dee300faa` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_16\ma_cct_dtn_16_phase.questphase` / h0 / 2 -> 7 -> 8 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
