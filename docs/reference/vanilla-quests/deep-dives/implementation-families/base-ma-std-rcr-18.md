# base-ma-std-rcr-18

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\community\ma_std_rcr_18_com_bums_civs.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\community\ma_std_rcr_18_com_wraiths.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\ma_std_rcr_18.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\ma_std_rcr_18.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_combat.questphase; base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\scenes\ma_std_rcr_18_chicken_test.scene; base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\scenes\ma_std_rcr_18_holocall_brief.scene; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\ma_std_rcr_18.questphase` | content candidate | 6 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\scenes\ma_std_rcr_18_holocall_brief.scene |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_bugfixing.questphase` | repair | 2 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_combat.questphase` | content candidate | 6 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_openworld.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\scenes\ma_std_rcr_18_chicken_test.scene` | test/debug | 0 / 4 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\scenes\ma_std_rcr_18_holocall_brief.scene` | content candidate | 0 / 15 |  |

## Journal paths observed in these resources

- `contacts/ncpd_dispatcher/outposts/ma_std_rcr_18`
- `points_of_interest/minor_activities/ma_std_rcr_18`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 2 |
| `questCheckpointNodeDefinition` | 4 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 3 |
| `questCutControlNodeDefinition` | 4 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 26 |
| `questFlowControlNodeDefinition` | 3 |
| `questInputNodeDefinition` | 15 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 2 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalHubNodeDefinition` | 2 |
| `questMiscAICommandNode` | 26 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 4 |
| `questOutputNodeDefinition` | 11 |
| `questPauseConditionNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questLogicalCondition,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 15 |
| `questPhaseNodeDefinition` | 13 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 20 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 2 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 4 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 3 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 4 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `71892f49b88f7b8bb8be` | 4 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\ma_std_rcr_18.questphase` / h457 / 0 -> 10 -> 4 |
| `17d00d36922f653f1130` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\ma_std_rcr_18.questphase` / h57 / 0 -> 13 -> 12 |
| `18be198845c90c6bb3c8` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\ma_std_rcr_18.questphase` / h527 / 18 -> 6 -> 2 |
| `423e38da0596af6a3004` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_combat.questphase` / h238 / 14 -> 17 -> 2 |
| `42d198651597f3c3ac03` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_combat.questphase` / h238 / 0 -> 4 -> 1 |
| `60faf7d04cb945080042` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_combat.questphase` / h238 / 17 -> 2 -> 3 |
| `650a7cbe5c601eed263f` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_combat.questphase` / h33 / 0 -> 48 -> 46 |
| `6a86344248d2b9e67699` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_combat.questphase` / h238 / 15 -> 18 -> 20 |
| `6f633a1a8a493edf4436` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\ma_std_rcr_18.questphase` / h457 / 0 -> 30 -> 33 |
| `72a7c9c4ee9d2356e0f7` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_combat.questphase` / h238 / 18 -> 20 -> 2 |
| `8a7f8aea08d8eda24584` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_combat.questphase` / h238 / 18 -> 16 -> 19 |
| `901d299850eb5392fd72` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_combat.questphase` / h238 / 20 -> 2 -> 3 |
| `9467f6661252ed56b5e1` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_combat.questphase` / h238 / 0 -> 14 -> 17 |
| `9cfaec76b59131b706f3` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_combat.questphase` / h238 / 14 -> 17 -> 7 |
| `b47b718b67278cee759d` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_combat.questphase` / h238 / 0 -> 6 -> 17 |
| `b90715b67cb6f4596277` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\ma_std_rcr_18.questphase` / h457 / 30 -> 33 -> 36 |
| `c2d990544e2d9ffb2741` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_combat.questphase` / h238 / 15 -> 18 -> 16 |
| `cd51ded7899f60f62e8a` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_combat.questphase` / h238 / 6 -> 17 -> 2 |
| `e4376999200772159f81` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\phases\ma_std_rcr_18_combat.questphase` / h238 / 14 -> 15 -> 18 |
| `e5742f9794e6583c67cb` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_18\scenes\ma_std_rcr_18_holocall_brief.scene` / scene / 254 -> 258 -> 256 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
