# base-ma-bls-ina-se1-21

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\community\ma_bls_ina_se1_21_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\community\ma_bls_ina_se1_21_com_victim.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` | content candidate | 5 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_21/shards/ma_bls_ina_se1_21`
- `points_of_interest/minor_activities/ma_bls_ina_se1_21`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 12 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 5 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 7 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `91d8157ebc22771edd99` | 4 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h0 / 19 -> 13 -> 49 |
| `ae26d9b3c8043dedb4cc` | 4 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h0 / 49 -> 47 -> 48 |
| `d30dec206567a53c3ede` | 4 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h0 / 13 -> 49 -> 47 |
| `18df34190d30ba0599e5` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h0 / 19 -> 0 -> 29 |
| `ad7509912d28b3e12b9b` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h0 / 1 -> 19 -> 0 |
| `f2a37207a30c59bac7f0` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h50 / 7 -> 8 -> 9 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h0 / 30 -> 65 -> 63 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h0 / 3 -> 4 -> 28 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h0 / 65 -> 62 -> 61 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h0 / 32 -> 37 -> 31 |
| `1121a7f146103492ac60` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h0 / 63 -> 61 -> 14 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h0 / 36 -> 65 -> 63 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h0 / 20 -> 36 -> 65 |
| `215a811f84fe46cd3cac` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h0 / 42 -> 43 -> 38 |
| `215ca95d939006973a7d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h0 / 15 -> 22 -> 2 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h0 / 65 -> 64 -> 61 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h0 / 62 -> 61 -> 12 |
| `4123636c2b09a02fdc99` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h50 / 9 -> 13 -> 17 |
| `423e38da0596af6a3004` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h304 / 15 -> 18 -> 2 |
| `42d198651597f3c3ac03` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_21\ma_bls_ina_se1_21_phase.questphase` / h304 / 0 -> 4 -> 1 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
