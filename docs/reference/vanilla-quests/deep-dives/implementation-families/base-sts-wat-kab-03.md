# base-sts-wat-kab-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\communities\sts_wat_kab_03_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_bugfixing.questphase` | repair | 6 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_combat.questphase` | content candidate | 5 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_scene.scene |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_openworld.questphase` | content candidate | 5 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene; base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_prebrief.scene; base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene; base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_scene.scene |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_phase.questphase` | content candidate | 3 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_combat.questphase; base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_openworld.questphase |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_prestate_control.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene` | content candidate | 0 / 25 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene` | content candidate | 0 / 34 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_scene.scene` | content candidate | 0 / 103 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\sts_wat_kab_03_definition.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\sts_wat_kab_03_quest.quest` | content candidate | 1 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_phase.questphase |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\sts_wat_kab_03_testworld_def.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/sts_wat_kab_03/sts_wat_kab_03_brief`
- `contacts/regina_jones/sts_wat_kab_03/sts_wat_kab_03_holocall_debrief`
- `points_of_interest/street_stories/sts_wat_kab_03`
- `quests/street_stories/watson/kabuki/sts_wat_kab_03`
- `quests/street_stories/watson/kabuki/sts_wat_kab_03/brief`
- `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/enter_solo_house`
- `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/locate_meds`
- `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/retrieve`
- `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/take_meds`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 2 |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 1 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerVisuals_ChangeEntityAppearance,questCharacterManagerVisuals_EntityAppearanceOperationBaseEntityAppearanceEntry,questCharacterManagerVisuals_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 4 |
| `questCombatNodeDefinition` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 15 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 3 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 5 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 1 |
| `questCutControlNodeDefinition` | 5 |
| `questDeletionMarkerNodeDefinition` | 14 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 2 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 3 |
| `questEventManagerNodeDefinition` | 9 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 42 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 6 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 2 |
| `questInputNodeDefinition` | 21 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 4 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 8 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 28 |
| `questLogicalHubNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 20 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterQuickHacked_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 19 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInputAction_ConditionType,questLogicalCondition,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 4 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 25 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 20 |
| `questPhaseNodeDefinition` | 16 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneManagerNodeDefinition[questToggleEventExecutionTag_NodeType]` | 2 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 5 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 18 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 7 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 8 |
| `scnDeletionMarkerNode[scnNodeId]` | 4 |
| `scnEndNode[scnNodeId]` | 12 |
| `scnHubNode[scnNodeId]` | 3 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 35 |
| `scnStartNode[scnNodeId]` | 7 |
| `scnXorNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `84bfca44950402ede644` | 5 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene` / scene / 10 -> 17 -> 226 |
| `bbf9efd740881cf31a37` | 5 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene` / scene / 277 -> 280 -> 261 |
| `c1b6601d2f647c8a694d` | 5 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene` / scene / 4 -> 8 -> 14 |
| `27faccd7b30abbc3add2` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene` / scene / 4 -> 8 -> 20 |
| `4e9e9731cb6665cc2d1c` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_bugfixing.questphase` / h17 / 33 -> 68 -> 50 |
| `5eae52ff40ba9dbd4a8c` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_bugfixing.questphase` / h17 / 52 -> 32 -> 50 |
| `624d47eac987aa67b8fb` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_bugfixing.questphase` / h17 / 34 -> 36 -> 51 |
| `6db8c1a6b27de78dd353` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene` / scene / 214 -> 10 -> 101 |
| `79aee3983ba5df3ce7af` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_bugfixing.questphase` / h17 / 42 -> 34 -> 36 |
| `82a4aecab2b4c4b20c63` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_bugfixing.questphase` / h17 / 68 -> 42 -> 34 |
| `b5e143326c7204a010d9` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene` / scene / 183 -> 214 -> 10 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene` / scene / 299 -> 297 -> 301 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene` / scene / 67 -> 299 -> 297 |
| `eaf5aab427d50e5598b6` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\phases\sts_wat_kab_03_bugfixing.questphase` / h17 / 0 -> 2 -> 3 |
| `03e5cda56e0db76159b6` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_scene.scene` / scene / 757 -> 1116 -> 1147 |
| `05ec9996cc9b4bf20067` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene` / scene / 214 -> 10 -> 17 |
| `1fa539921730278ef7fb` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene` / scene / 8 -> 14 -> 17 |
| `3bfe06739d5bfa31d0df` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_scene.scene` / scene / 554 -> 553 -> 1414 |
| `473d526525c3655d6b1f` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene` / scene / 10 -> 17 -> 110 |
| `606537727d23a7d6787c` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_scene.scene` / scene / 757 -> 1116 -> 748 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
