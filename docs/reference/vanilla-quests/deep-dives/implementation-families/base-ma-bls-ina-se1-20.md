# base-ma-bls-ina-se1-20

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\community\ma_bls_ina_se1_20_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\community\ma_bls_ina_se1_20_com_civilian.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` | content candidate | 5 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_20/onscreens/ma_bls_ina_se1_20_archi`
- `points_of_interest/minor_activities/ma_bls_ina_se1_20`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 8 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 5 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 9 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `20a77143a898bc753a26` | 3 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h0 / 0 -> 54 -> 55 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h0 / 9 -> 12 -> 34 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h0 / 68 -> 65 -> 64 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h0 / 40 -> 47 -> 39 |
| `0b81e5206696faa510d4` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h48 / 4 -> 9 -> 2 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h0 / 65 -> 64 -> 40 |
| `1094980783b061bb3393` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h48 / 8 -> 23 -> 7 |
| `12b102391853a0e26cba` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h48 / 3 -> 4 -> 9 |
| `1489a2df8e7f98f9c78e` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h0 / 41 -> 11 -> 68 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h0 / 64 -> 40 -> 47 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h0 / 68 -> 67 -> 64 |
| `2e1ee5a1324dbeeb9071` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h0 / 56 -> 41 -> 11 |
| `334d3d5e9292145cac5a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h48 / 23 -> 7 -> 1 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h0 / 65 -> 64 -> 16 |
| `3750bdcc2a4bda83d074` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h0 / 11 -> 68 -> 67 |
| `38fa6f831b5b88215432` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h48 / 20 -> 6 -> 8 |
| `3a7f8b9c6d709ceceae1` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h0 / 11 -> 68 -> 65 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h0 / 66 -> 64 -> 40 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h0 / 67 -> 64 -> 40 |
| `42d198651597f3c3ac03` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_20\ma_bls_ina_se1_20_phase.questphase` / h313 / 0 -> 4 -> 1 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
