# base-ma-wat-nid-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\community\ma_wat_nid_01_scavs.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\community\ma_wat_nid_01_victims.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase` | content candidate | 3 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_01\scenes\ma_wat_nid_01_holocall_brief.scene |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_quest.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\scenes\ma_wat_nid_01_holocall_brief.scene` | content candidate | 0 / 22 |  |

## Journal paths observed in these resources

- `contacts/ncpd_dispatcher/outposts/ma_wat_nid_01`
- `points_of_interest/minor_activities/ma_wat_nid_01`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 6 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 5 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 8 |
| `questCutControlNodeDefinition` | 5 |
| `questDeletionMarkerNodeDefinition` | 9 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 19 |
| `questInputNodeDefinition` | 4 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questLogicalHubNodeDefinition` | 4 |
| `questMiscAICommandNode` | 7 |
| `questMovePuppetNodeDefinition` | 3 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 3 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 6 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 3 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 12 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 4 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e414a18dbb28a2f0ff6` | 6 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase` / h681 / 4 -> 13 -> 23 |
| `18940bb88414fed7fad4` | 4 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase` / h0 / 40 -> 175 -> 176 |
| `c7f3fb0479cbced23eb0` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase` / h0 / 226 -> 109 -> 103 |
| `cca3a682ae0ebd5f6d3d` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase` / h0 / 175 -> 176 -> 218 |
| `dc42a58f5079d1c2e5e3` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase` / h0 / 126 -> 143 -> 144 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\scenes\ma_wat_nid_01_holocall_brief.scene` / scene / 285 -> 267 -> 273 |
| `1f1ba65030d457455ea5` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase` / h37 / 12 -> 13 -> 6 |
| `202e7b729f3d8385079e` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase` / h0 / 109 -> 103 -> 120 |
| `4185dd904c413c3ced10` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase` / h0 / 219 -> 216 -> 214 |
| `7cdafd6dc919bead3c29` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase` / h0 / 226 -> 119 -> 123 |
| `ac5b347c9518873a2790` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\scenes\ma_wat_nid_01_holocall_brief.scene` / scene / 267 -> 273 -> 271 |
| `bbf9efd740881cf31a37` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\scenes\ma_wat_nid_01_holocall_brief.scene` / scene / 282 -> 285 -> 267 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\scenes\ma_wat_nid_01_holocall_brief.scene` / scene / 258 -> 256 -> 260 |
| `e25b126fbbe72dac9623` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase` / h0 / 226 -> 216 -> 214 |
| `e5742f9794e6583c67cb` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\scenes\ma_wat_nid_01_holocall_brief.scene` / scene / 254 -> 258 -> 256 |
| `05b55b664997ab6e079f` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase` / h0 / 226 -> 109 -> 127 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase` / h0 / 3 -> 88 -> 89 |
| `07a508d9181a1ec44ac6` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase` / h0 / 25 -> 63 -> 4 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase` / h0 / 101 -> 210 -> 100 |
| `0bef3d9d4a4adf2da8cd` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase` / h0 / 225 -> 226 -> 109 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
