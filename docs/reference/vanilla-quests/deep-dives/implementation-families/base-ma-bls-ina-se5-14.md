# base-ma-bls-ina-se5-14

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\community\ma_bls_ina_se5_14_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\community\ma_bls_ina_se5_14_com_civilian.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/badlands/se5/ma_bls_ina_se5_14/onscreens/ma_bls_ina_se5_14_onscreen_02`
- `points_of_interest/minor_activities/ma_bls_ina_se5_14`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 9 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 3 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questDevice_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 12 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 4 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `20a77143a898bc753a26` | 4 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h0 / 19 -> 76 -> 77 |
| `f5fa8bfbbfb2fb420362` | 3 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h0 / 18 -> 17 -> 51 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h0 / 9 -> 69 -> 42 |
| `27989a991fbce5b0fc5c` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h0 / 51 -> 47 -> 48 |
| `a7629f14706d6b7addef` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h0 / 48 -> 86 -> 87 |
| `bff957bf33a10413a685` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h0 / 17 -> 51 -> 47 |
| `e2f47ae0316d4ceab903` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h0 / 47 -> 48 -> 86 |
| `00c3ca0ac0b55db639ca` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h39 / 8 -> 5 -> 4 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h0 / 96 -> 93 -> 92 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h0 / 93 -> 92 -> 44 |
| `0e55e762d8ff58e5ae49` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h0 / 12 -> 18 -> 17 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h0 / 92 -> 44 -> 70 |
| `1684da3a45630fb3518c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h39 / 6 -> 7 -> 3 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h39 / 10 -> 8 -> 5 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h0 / 9 -> 69 -> 32 |
| `2465cabc5e4b65280bdb` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h0 / 35 -> 9 -> 69 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h0 / 96 -> 95 -> 92 |
| `2e1ee5a1324dbeeb9071` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h0 / 79 -> 80 -> 63 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h0 / 34 -> 96 -> 95 |
| `3377a258157e1b6fcd68` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_14\ma_bls_ina_se5_14_phase.questphase` / h0 / 17 -> 3 -> 4 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
