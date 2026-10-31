# base-ma-bls-ina-se5-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\community\ma_bls_ina_se5_07_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase` | content candidate | 3 / 0 | base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\scenes\ma_bls_ina_se5_07_holocall_brief.scene |
| `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\scenes\ma_bls_ina_se5_07_holocall_brief.scene` | content candidate | 0 / 15 |  |

## Journal paths observed in these resources

- `contacts/ncpd_dispatcher/outposts/ma_bls_ina_se5_07`
- `points_of_interest/minor_activities/ma_bls_ina_se5_07`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 3 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 12 |
| `questInputNodeDefinition` | 3 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 6 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `227037b5e7f2d6d4ed0d` | 5 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase` / h0 / 36 -> 25 -> 65 |
| `bff957bf33a10413a685` | 5 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase` / h0 / 25 -> 65 -> 61 |
| `e5742f9794e6583c67cb` | 3 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\scenes\ma_bls_ina_se5_07_holocall_brief.scene` / scene / 79 -> 256 -> 258 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase` / h0 / 42 -> 110 -> 55 |
| `9856eaca0f892fb9852f` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase` / h312 / 12 -> 15 -> 13 |
| `9e5e28ecb38ea2a53a15` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\scenes\ma_bls_ina_se5_07_holocall_brief.scene` / scene / 254 -> 79 -> 73 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\scenes\ma_bls_ina_se5_07_holocall_brief.scene` / scene / 256 -> 258 -> 260 |
| `f89bc035d6c0e83fa340` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase` / h312 / 15 -> 13 -> 14 |
| `02b5b1790eec80cd653e` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase` / h0 / 4 -> 113 -> 11 |
| `07708100a0a35824ab4a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase` / h0 / 114 -> 94 -> 115 |
| `07a508d9181a1ec44ac6` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase` / h0 / 27 -> 26 -> 4 |
| `101b60945ddf6f25f378` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\scenes\ma_bls_ina_se5_07_holocall_brief.scene` / scene / 18 -> 78 -> 80 |
| `14d7f1f2f390b216461a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase` / h0 / 92 -> 114 -> 94 |
| `1520ebe4ea0bf9451321` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase` / h0 / 41 -> 97 -> 92 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase` / h37 / 7 -> 3 -> 4 |
| `1d933adb5a617880c93e` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\scenes\ma_bls_ina_se5_07_holocall_brief.scene` / scene / 78 -> 80 -> 75 |
| `1e253d0fcbd364975401` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase` / h0 / 51 -> 0 -> 80 |
| `234740de04d3a2934680` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase` / h0 / 80 -> 33 -> 42 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\ma_bls_ina_se5_07_phase.questphase` / h0 / 42 -> 110 -> 28 |
| `26762f051e7728f090ca` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_07\scenes\ma_bls_ina_se5_07_holocall_brief.scene` / scene / 74 -> 77 -> 18 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
