# base-ma-pac-cvi-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\community\ma_pac_cvi_03_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questInputNodeDefinition` | 3 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 6 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `080b445bc4090d559039` | 6 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h0 / 0 -> 10 -> 38 |
| `04d44032fde67923816a` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h51 / 7 -> 10 -> 11 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h0 / 36 -> 49 -> 48 |
| `1d20314efb11e92e1287` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h0 / 41 -> 43 -> 20 |
| `24a5e4c19f1c9c862c02` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h0 / 39 -> 43 -> 20 |
| `34b48742c4257a2c4ed9` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h0 / 16 -> 9 -> 19 |
| `4046f7e0ed1087267da3` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h0 / 10 -> 16 -> 9 |
| `5f50b510abf7ccbb261c` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h0 / 49 -> 47 -> 1 |
| `71892f49b88f7b8bb8be` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h0 / 0 -> 10 -> 16 |
| `8370c76cbc0899b84848` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h0 / 16 -> 9 -> 18 |
| `8bc444681b5129cc73b0` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h0 / 36 -> 49 -> 47 |
| `90cf58434e79ce42af1e` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h51 / 0 -> 13 -> 12 |
| `945a32c9c54fad29d3bc` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h0 / 40 -> 43 -> 20 |
| `a3e5f861a4b71433135a` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h51 / 12 -> 6 -> 7 |
| `aa3fdb3e596454f51c4d` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h0 / 19 -> 47 -> 1 |
| `b0a5b5a10b45d5360585` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h0 / 42 -> 43 -> 20 |
| `b5dcd9fc14a032d8f1a9` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h0 / 37 -> 43 -> 20 |
| `b618b0b2d0cf28dc9cec` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h0 / 10 -> 39 -> 43 |
| `b9d00bebb708df7300a1` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h0 / 49 -> 48 -> 47 |
| `bb3419577cd52e7dd794` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_03\ma_pac_cvi_03_phase.questphase` / h0 / 38 -> 43 -> 20 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
