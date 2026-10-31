# base-ma-bls-ina-se1-23

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\community\ma_bls_ina_se1_23_junkies_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\community\ma_bls_ina_se5_23.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_23/onscreens/ma_bls_ina_se1_23_onscreen_01`
- `points_of_interest/minor_activities/ma_bls_ina_se1_23`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 8 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 3 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalHubNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `1e253d0fcbd364975401` | 3 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h0 / 15 -> 1 -> 20 |
| `804cb97c944e3c3bf436` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h0 / 16 -> 15 -> 1 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h0 / 26 -> 52 -> 50 |
| `00c3ca0ac0b55db639ca` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h49 / 3 -> 10 -> 13 |
| `07a508d9181a1ec44ac6` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h0 / 8 -> 12 -> 9 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h0 / 52 -> 49 -> 48 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h0 / 28 -> 36 -> 27 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h0 / 49 -> 48 -> 28 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h0 / 35 -> 52 -> 50 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h0 / 48 -> 28 -> 36 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h49 / 14 -> 3 -> 10 |
| `1972a0532f20a107c8bb` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h0 / 1 -> 2 -> 3 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h0 / 13 -> 35 -> 52 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h0 / 52 -> 51 -> 48 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h0 / 49 -> 48 -> 14 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h0 / 50 -> 48 -> 28 |
| `3ed9f5913647622cfa36` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h198 / 4 -> 2 -> 3 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h0 / 51 -> 48 -> 28 |
| `4798537ca16e1216226c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h49 / 10 -> 13 -> 11 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_23\ma_bls_ina_se1_23_questphase.questphase` / h0 / 35 -> 26 -> 52 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
