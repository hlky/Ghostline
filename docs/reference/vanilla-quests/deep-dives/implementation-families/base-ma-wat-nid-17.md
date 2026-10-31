# base-ma-wat-nid-17

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_17\ma_wat_nid_17_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_17\ma_wat_nid_17_phase.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_17\ma_wat_nid_17_quest.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_17\ma_wat_nid_17_phase.questphase |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_17\ma_wat_nid_17_phase.questphase` / h0 / 31 -> 32 -> 30 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_17\ma_wat_nid_17_phase.questphase` / h0 / 35 -> 28 -> 36 |
| `2bbf5528ada3f00dc747` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_17\ma_wat_nid_17_phase.questphase` / h0 / 2 -> 9 -> 34 |
| `50c0101882435d977f36` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_17\ma_wat_nid_17_phase.questphase` / h0 / 28 -> 36 -> 26 |
| `71892f49b88f7b8bb8be` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_17\ma_wat_nid_17_phase.questphase` / h0 / 2 -> 11 -> 22 |
| `79d5c71726a61b77a50e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_17\ma_wat_nid_17_phase.questphase` / h0 / 2 -> 9 -> 31 |
| `85eb8c605330d1dbd69e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_17\ma_wat_nid_17_phase.questphase` / h0 / 36 -> 26 -> 3 |
| `978a69b98137186c49a7` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_17\ma_wat_nid_17_quest.quest` / h0 / 1 -> 0 -> 2 |
| `f66cfde7fa1a88e1f4a1` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_17\ma_wat_nid_17_phase.questphase` / h0 / 9 -> 34 -> 35 |
| `fee3756653cd083fb28e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_17\ma_wat_nid_17_phase.questphase` / h0 / 34 -> 35 -> 28 |
| `ff4c8a828496c45d7dfa` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_17\ma_wat_nid_17_phase.questphase` / h0 / 9 -> 31 -> 32 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
