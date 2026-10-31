# base-ma-bls-ina-se5-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\community\ma_bls_ina_se5_03_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/badlands/se5/ma_bls_ina_se5_03/shards/ma_bls_ina_se5_03`
- `points_of_interest/minor_activities/ma_bls_ina_se5_03`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 4 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 5 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `e9f923e47e7820bc498d` | 3 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 64 -> 102 -> 40 |
| `05059c37b6a13b873408` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 102 -> 40 -> 92 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 101 -> 86 -> 79 |
| `ae26d9b3c8043dedb4cc` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 92 -> 90 -> 91 |
| `d30dec206567a53c3ede` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 40 -> 92 -> 90 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 109 -> 105 -> 107 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 105 -> 107 -> 80 |
| `1121a7f146103492ac60` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 106 -> 107 -> 39 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 107 -> 80 -> 87 |
| `159599f19533cfcfe918` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 102 -> 101 -> 41 |
| `180a68060e3b4ce5db3d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 64 -> 102 -> 0 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h44 / 8 -> 4 -> 2 |
| `226ff726bdafe72139a6` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 64 -> 102 -> 101 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 109 -> 108 -> 107 |
| `2e313d31db9a27edb599` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 102 -> 101 -> 86 |
| `2e578fd8f85357f1804f` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 101 -> 109 -> 106 |
| `390915d4be7a3df08eff` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 102 -> 0 -> 89 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 106 -> 107 -> 80 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 108 -> 107 -> 80 |
| `479a11033aba2b8c1ef3` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_03\ma_bls_ina_se5_03_phase.questphase` / h0 / 101 -> 109 -> 105 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
