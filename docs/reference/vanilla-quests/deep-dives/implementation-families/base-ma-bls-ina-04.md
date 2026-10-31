# base-ma-bls-ina-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\community\ma_bls_ina_se1_04_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\community\ma_bls_ina_se1_04_com_victim.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_04/onscreens/ma_bls_ina_se1_04_onscreen_02`
- `points_of_interest/minor_activities/ma_bls_ina_se1_04`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 3 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 3 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 7 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `fa5824c0efca270073ba` | 4 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h0 / 57 -> 19 -> 43 |
| `95b7458b3ffd83fd4357` | 3 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h0 / 19 -> 43 -> 73 |
| `ef828624d48b06bf49f2` | 3 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h0 / 19 -> 53 -> 20 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h0 / 21 -> 77 -> 49 |
| `900f91d636fcd5f8f228` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h0 / 53 -> 20 -> 101 |
| `02d878a28a675e881f96` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h0 / 104 -> 102 -> 38 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h0 / 106 -> 103 -> 102 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h0 / 103 -> 102 -> 51 |
| `1236b824035f3d3d10f6` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h299 / 7 -> 3 -> 2 |
| `1489a2df8e7f98f9c78e` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h0 / 52 -> 57 -> 89 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h0 / 102 -> 51 -> 78 |
| `178ff9eba50354aed786` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h299 / 0 -> 8 -> 7 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h0 / 21 -> 77 -> 47 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h0 / 106 -> 105 -> 102 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h0 / 46 -> 106 -> 105 |
| `3b5a6e81dfc083dd3d0a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h0 / 64 -> 66 -> 65 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h0 / 104 -> 102 -> 51 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h0 / 105 -> 102 -> 51 |
| `42d198651597f3c3ac03` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h373 / 0 -> 4 -> 1 |
| `45a0059a97ab5b10fb49` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_04\ma_bls_ina_se1_04_phase.questphase` / h0 / 103 -> 102 -> 38 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
