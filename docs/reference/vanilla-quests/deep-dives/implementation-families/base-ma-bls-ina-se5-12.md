# base-ma-bls-ina-se5-12

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\community\ma_bls_ina_se5_12_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` | content candidate | 4 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/badlands/se5/ma_bls_ina_se5_12/onscreens/ma_bls_ina_se5_12_onscreen_01`
- `points_of_interest/minor_activities/ma_bls_ina_se5_12`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 4 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 14 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 6 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `7edf0c9b5edb3c65c003` | 14 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h238 / 0 -> 2 -> 1 |
| `27989a991fbce5b0fc5c` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 44 -> 40 -> 49 |
| `a5f6ff0df46f7043f2b5` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 40 -> 49 -> 67 |
| `a7629f14706d6b7addef` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 67 -> 85 -> 86 |
| `c38d48a1933155f131af` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 0 -> 37 -> 44 |
| `e2f47ae0316d4ceab903` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 49 -> 67 -> 85 |
| `ed12ad2a881e4e7643f7` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 0 -> 37 -> 75 |
| `f3c7f02f31411d4070e1` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 37 -> 44 -> 40 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 34 -> 97 -> 95 |
| `02d878a28a675e881f96` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 95 -> 93 -> 14 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 97 -> 94 -> 93 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 35 -> 83 -> 36 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 94 -> 93 -> 35 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 82 -> 97 -> 95 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 93 -> 35 -> 83 |
| `18df34190d30ba0599e5` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 13 -> 0 -> 37 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 28 -> 82 -> 97 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 97 -> 96 -> 93 |
| `338f839dd144ddebb804` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h46 / 8 -> 2 -> 5 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_12\ma_bls_ina_se5_12_phase.questphase` / h0 / 95 -> 93 -> 35 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
