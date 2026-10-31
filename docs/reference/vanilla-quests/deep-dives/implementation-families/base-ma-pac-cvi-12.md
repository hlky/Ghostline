# base-ma-pac-cvi-12

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\community\ma_pac_cvi_12_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_phase.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_bugfixing.questphase` | repair | 4 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_combat.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_phase.questphase` | content candidate | 2 / 0 | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_combat.questphase; base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\scenes\ma_pac_cvi_12_holocall_brief.scene |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\scenes\ma_pac_cvi_12_holocall_brief.scene` | content candidate | 0 / 15 |  |

## Journal paths observed in these resources

- `contacts/ncpd_dispatcher/outposts/ma_pac_cvi_12`
- `points_of_interest/minor_activities/ma_pac_cvi_12`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 6 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 15 |
| `questInputNodeDefinition` | 8 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questMiscAICommandNode` | 11 |
| `questOutputNodeDefinition` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 6 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 6 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `5c76d3bf7160f29b884f` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_bugfixing.questphase` / h14 / 2 -> 3 -> 6 |
| `e5742f9794e6583c67cb` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\scenes\ma_pac_cvi_12_holocall_brief.scene` / scene / 69 -> 258 -> 256 |
| `eaf5aab427d50e5598b6` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_bugfixing.questphase` / h14 / 0 -> 2 -> 3 |
| `9e5e28ecb38ea2a53a15` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\scenes\ma_pac_cvi_12_holocall_brief.scene` / scene / 254 -> 69 -> 63 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\scenes\ma_pac_cvi_12_holocall_brief.scene` / scene / 258 -> 256 -> 260 |
| `df9a790f8c0e1ffd21ed` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_bugfixing.questphase` / h91 / 3 -> 4 -> 7 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_phase.questphase` / h37 / 12 -> 4 -> 5 |
| `03997a006fcf1f3b4d06` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_phase.questphase` / h0 / 101 -> 107 -> 108 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_phase.questphase` / h0 / 3 -> 16 -> 80 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_phase.questphase` / h0 / 118 -> 113 -> 103 |
| `09546c70dcc2f0968a4e` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_bugfixing.questphase` / h14 / 7 -> 10 -> 8 |
| `101b60945ddf6f25f378` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\scenes\ma_pac_cvi_12_holocall_brief.scene` / scene / 33 -> 68 -> 70 |
| `134488cd8e3fc84d3c9a` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_bugfixing.questphase` / h14 / 3 -> 6 -> 9 |
| `14d7f1f2f390b216461a` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_phase.questphase` / h0 / 105 -> 127 -> 106 |
| `1520ebe4ea0bf9451321` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_phase.questphase` / h0 / 107 -> 108 -> 105 |
| `18f387783b5098eb3c76` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_bugfixing.questphase` / h14 / 10 -> 8 -> 1 |
| `1d933adb5a617880c93e` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\scenes\ma_pac_cvi_12_holocall_brief.scene` / scene / 68 -> 70 -> 65 |
| `26762f051e7728f090ca` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\scenes\ma_pac_cvi_12_holocall_brief.scene` / scene / 64 -> 67 -> 33 |
| `2b247f9d6dcbd113b717` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\ma_pac_cvi_12_bugfixing.questphase` / h151 / 10 -> 2 -> 1 |
| `2beeeaa3b4da5300c035` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\scenes\ma_pac_cvi_12_holocall_brief.scene` / scene / 1 -> 254 -> 69 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
