# base-ma-wat-nid-30

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\community\ma_wat_nid_30_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 1 |
| `questMiscAICommandNode` | 2 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `51d78876d4b7cc3025b7` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 1 -> 4 -> 6 |
| `95b7458b3ffd83fd4357` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 15 -> 1 -> 27 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 33 -> 32 -> 34 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 37 -> 31 -> 38 |
| `2252a132cf17333b3476` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 9 -> 14 -> 18 |
| `3c6b36e8c01548f18f31` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 18 -> 20 -> 33 |
| `3de2a161e69ddac9948e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 20 -> 36 -> 37 |
| `4082b9e32a4fa2870fb3` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 1 -> 9 -> 14 |
| `4c86e9d12122e122fabf` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 19 -> 29 -> 23 |
| `5870e2fba5607932758d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 1 -> 11 -> 16 |
| `5d73a2f49ed5d74832e0` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 18 -> 20 -> 36 |
| `6e3b35557bcc40a5d957` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 23 -> 25 -> 30 |
| `75582ae0b4c1620a124c` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 25 -> 30 -> 3 |
| `8d10896873df5c62014e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 15 -> 1 -> 4 |
| `987122e5e2fcd167cf6c` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 2 -> 15 -> 1 |
| `b41539b8d4b918661cc4` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 11 -> 16 -> 17 |
| `d2347eb446c8c5230fe1` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 15 -> 1 -> 9 |
| `d31e002cb3090feda277` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 29 -> 23 -> 25 |
| `de7e57dffb8a1398178a` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 20 -> 33 -> 32 |
| `e7e76532ca5105db2460` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_30\ma_wat_nid_30_phase.questphase` / h0 / 31 -> 38 -> 19 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
