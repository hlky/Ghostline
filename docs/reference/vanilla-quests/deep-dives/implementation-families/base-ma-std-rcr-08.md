# base-ma-std-rcr-08

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\community\ma_std_rcr_08_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\community\ma_std_rcr_08_miniboss.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\community\ma_std_rcr_08_reinf_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\community\ma_std_rcr_08_women.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase` | content candidate | 3 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\scenes\ma_std_rcr_08_holocall_brief.scene |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\phases\cyb583256.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\phases\ma_std_rcr_08_bugfixing.questphase` | repair | 2 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\scenes\ma_std_rcr_08_holocall_brief.scene` | content candidate | 0 / 15 |  |

## Journal paths observed in these resources

- `contacts/ncpd_dispatcher/outposts/ma_std_rcr_08`
- `onscreens/emails/quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_08/onscreens/ma_std_rcr_08_onscreen_001`
- `points_of_interest/minor_activities/ma_std_rcr_08`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition` | 5 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 5 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 8 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 14 |
| `questInputNodeDefinition` | 5 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMiscAICommandNode` | 3 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 4 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questDevice_ConditionType,questLogicalCondition,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questJournalCondition,questJournalEntry_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 4 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 4 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 8 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 2 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 8 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `6e76fa24955b61b66ee7` | 4 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase` / h0 / 51 -> 34 -> 39 |
| `f6dd78290481637d62aa` | 4 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase` / h0 / 44 -> 58 -> 65 |
| `18be198845c90c6bb3c8` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase` / h56 / 9 -> 6 -> 4 |
| `95b7458b3ffd83fd4357` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase` / h0 / 0 -> 11 -> 13 |
| `e5742f9794e6583c67cb` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\scenes\ma_std_rcr_08_holocall_brief.scene` / scene / 254 -> 258 -> 256 |
| `5506424829d3f5f3a244` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase` / h0 / 1 -> 71 -> 77 |
| `66e17bf07a534afe17b2` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase` / h56 / 9 -> 6 -> 2 |
| `987122e5e2fcd167cf6c` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase` / h0 / 1 -> 0 -> 11 |
| `9e5e28ecb38ea2a53a15` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\scenes\ma_std_rcr_08_holocall_brief.scene` / scene / 84 -> 254 -> 78 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\scenes\ma_std_rcr_08_holocall_brief.scene` / scene / 258 -> 256 -> 260 |
| `e1f20b49ae95bcf13966` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase` / h0 / 134 -> 73 -> 79 |
| `f54eb0b1d1c75c9526e7` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase` / h0 / 48 -> 49 -> 3 |
| `f78c85f90230c14b859c` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase` / h0 / 48 -> 49 -> 23 |
| `016d08a2dc6544fcdfd7` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase` / h0 / 162 -> 158 -> 134 |
| `03c246c9957a2b14e1e4` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase` / h0 / 128 -> 126 -> 127 |
| `0c77f361ab1d011872db` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase` / h0 / 119 -> 137 -> 135 |
| `0d34812e918dfe63b63d` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase` / h0 / 163 -> 162 -> 158 |
| `0d775120d2884a204806` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase` / h0 / 114 -> 154 -> 2 |
| `101b60945ddf6f25f378` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\scenes\ma_std_rcr_08_holocall_brief.scene` / scene / 47 -> 83 -> 85 |
| `14d7f1f2f390b216461a` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\ma_std_rcr_08_phase.questphase` / h0 / 132 -> 155 -> 133 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
