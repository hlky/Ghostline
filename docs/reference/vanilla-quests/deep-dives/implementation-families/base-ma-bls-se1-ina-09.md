# base-ma-bls-se1-ina-09

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\community\ma_bls_ina_se1_09_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\community\ma_bls_ina_se1_09_com_victim.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_09/onscreens/ma_bls_ina_se1_09_girl`
- `points_of_interest/minor_activities/ma_bls_ina_se1_09`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 13 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `20a77143a898bc753a26` | 5 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 83 -> 0 -> 84 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 11 -> 53 -> 31 |
| `2e1ee5a1324dbeeb9071` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 87 -> 35 -> 14 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 31 -> 98 -> 96 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 98 -> 95 -> 94 |
| `1121a7f146103492ac60` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 96 -> 94 -> 52 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 53 -> 98 -> 96 |
| `12942b757a8097fcda72` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 68 -> 55 -> 56 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 81 -> 27 -> 25 |
| `1e8ddd4b176ae3d7c402` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 16 -> 88 -> 89 |
| `1ecc1e1f4c4151a3aba0` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 11 -> 53 -> 98 |
| `2ab383c070f48fff1203` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 14 -> 37 -> 76 |
| `2cc4f20e16798419f013` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 20 -> 12 -> 82 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 98 -> 97 -> 94 |
| `3b5a6e81dfc083dd3d0a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 40 -> 42 -> 41 |
| `423e38da0596af6a3004` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h312 / 14 -> 17 -> 2 |
| `42d198651597f3c3ac03` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h312 / 0 -> 4 -> 1 |
| `46314d07127e853891b3` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 14 -> 49 -> 21 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 53 -> 31 -> 98 |
| `53e1b61b58de584e4473` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_se1_ina_09\ma_bls_ina_se1_09_phase.questphase` / h0 / 31 -> 98 -> 97 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
