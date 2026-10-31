# base-mq026

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq026\mq026_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq026\mq026_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq026\mq026_quest_bugfixes.questphase` | repair | 7 / 0 |  |
| `base\quest\minor_quests\mq026\communities\mq026_com_malstrom.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq026\communities\mq026_com_prophet.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq026\communities\mq026_com_smuggler.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq026\mq026.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq026\mq026.quest` | content candidate | 4 / 0 | base\quest\additional_game_elements.questphase; base\quest\bugfixing.questphase; base\quest\minor_quests\mq026\mq026.questphase; base\quest\minor_quests\mq026\phases\mq026_00_chickentest.questphase |
| `base\quest\minor_quests\mq026\mq026.questphase` | content candidate | 5 / 0 | base\quest\minor_quests\mq026\phases\mq026_01_conspiracies.questphase; base\quest\minor_quests\mq026\phases\mq026_02_cargo.questphase; base\quest\minor_quests\mq026\phases\mq026_03_death.questphase |
| `base\quest\minor_quests\mq026\phases\mq026_00_chickentest.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq026\test\mq026_00_chickentest.scene |
| `base\quest\minor_quests\mq026\phases\mq026_01_conspiracies.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene; base\quest\minor_quests\mq026\scenes\mq026_03_nomad.scene |
| `base\quest\minor_quests\mq026\phases\mq026_02_01_gameplay.questphase` | content candidate | 5 / 0 |  |
| `base\quest\minor_quests\mq026\phases\mq026_02_cargo.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq026\scenes\mq026_04_smuggler.scene |
| `base\quest\minor_quests\mq026\phases\mq026_03_death.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq026\scenes\mq026_02_death.scene |
| `base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene` | content candidate | 0 / 355 |  |
| `base\quest\minor_quests\mq026\scenes\mq026_02_death.scene` | content candidate | 0 / 102 |  |
| `base\quest\minor_quests\mq026\scenes\mq026_03_nomad.scene` | content candidate | 0 / 197 |  |
| `base\quest\minor_quests\mq026\scenes\mq026_04_smuggler.scene` | content candidate | 0 / 314 |  |
| `base\quest\minor_quests\mq026\test\mq026_00_chickentest.scene` | test/debug | 0 / 42 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_quest/mq026_prophet/mq026_prophet_shards/mq026_prophet_moon`
- `points_of_interest/minor_quests/mq026_prophet`
- `quests/minor_quest/mq026_conspiracy`
- `quests/minor_quest/mq026_conspiracy/stash/01_01_find_stash`
- `quests/minor_quest/mq026_conspiracy/stash/01_01_find_stash/mq026_desc`
- `quests/minor_quest/mq026_conspiracy/stash/01_02_find_stash`
- `quests/minor_quest/mq026_conspiracy/stash/01_02a_suspicious`
- `quests/minor_quest/mq026_conspiracy/stash/01_03_loot_corpse`
- `quests/minor_quest/mq026_conspiracy/stash/01_03_loot_corpse/01_03_loot`
- `quests/minor_quest/mq026_conspiracy/stash/01_03_loot_corpse/carrier`
- `quests/minor_quest/mq026_conspiracy/stash/01_04_confront`
- `quests/minor_quest/mq026_conspiracy/stash/01_05_hide`
- `quests/minor_quest/mq026_conspiracy/stash/01_05a_talk`
- `quests/minor_quest/mq026_conspiracy/stash/01_05b_wait`
- `quests/minor_quest/mq026_conspiracy/stash/01_06b_take_out_carrier`
- `quests/minor_quest/mq026_conspiracy/stash/01_07_return`
- `quests/minor_quest/mq026_conspiracy/stash/01_07b_disciple`
- `quests/minor_quest/mq026_conspiracy/stash/01_08_what`
- `quests/minor_quest/mq026_conspiracy/stash/01_09_johnny`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 16 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_EquipWeapon,questCharacterManagerCombat_NodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_HealPlayer,questCharacterManagerParameters_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 8 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetLifePath]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 5 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 1 |
| `questCheckpointNodeDefinition` | 9 |
| `questCombatNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 11 |
| `questConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 20 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 5 |
| `questConditionNodeDefinition[questTimeCondition,questTimePeriod_ConditionType]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 6 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 9 |
| `questEndNodeDefinition` | 1 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 2 |
| `questEventManagerNodeDefinition` | 19 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 7 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 107 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 18 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 4 |
| `questInputNodeDefinition` | 34 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 6 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 18 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 37 |
| `questLogicalHubNodeDefinition` | 10 |
| `questMappinManagerNodeDefinition` | 2 |
| `questMovePuppetNodeDefinition[questFollowParams,questUniversalRef]` | 2 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 6 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 6 |
| `questOutputNodeDefinition` | 27 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 5 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questFactsDBCondition,questLogicalCondition,questSystemCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterHit_ConditionType,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterHit_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 23 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questDistanceComparison_ConditionType,questDistanceCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questObjectDistance,questTriggerCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questTriggerCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 22 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questFactsDBCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 14 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questInventory_ConditionType,questLogicalCondition,questObjectCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 15 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questRealtimeDelay_ConditionType,questTimeCondition,questTimePeriod_ConditionType,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTimeCondition,questTimePeriod_ConditionType,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 66 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 12 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpeed_ConditionType]` | 2 |
| `questPhaseNodeDefinition` | 19 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 5 |
| `questRandomizerNodeDefinition` | 1 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 5 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questPlayerLookAt_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 5 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 4 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 33 |
| `questSpawnManagerNodeDefinition[questScene_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 6 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 4 |
| `questTimeManagerNodeDefinition[questSetTime_NodeType]` | 2 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 3 |
| `questUIManagerNodeDefinition[questShowOnscreen_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 43 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 1 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 104 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 9 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 25 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 8 |
| `scnAndNode[scnNodeId]` | 10 |
| `scnChoiceNode[questFactsDBCondition,questInventory_ConditionType,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questObjectCondition,questPaymentBalanced_ConditionType,questPaymentCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questLifePath_ConditionType,questLogicalCondition,questStatsCondition,questUniversalRef,questVarComparison_ConditionType,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questInventory_ConditionType,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questObjectCondition,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questPaymentBalanced_ConditionType,questPaymentCondition,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 9 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 7 |
| `scnCutControlNode[scnNodeId]` | 24 |
| `scnDeletionMarkerNode[scnNodeId]` | 6 |
| `scnEndNode[scnNodeId]` | 14 |
| `scnHubNode[scnNodeId]` | 74 |
| `scnInterruptManagerNode[scnCheckPlayerTargetEntityDistanceInterruptCondition,scnCheckPlayerTargetEntityDistanceInterruptConditionParams,scnCheckPlayerTargetEntityDistanceReturnCondition,scnCheckPlayerTargetEntityDistanceReturnConditionParams,scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideReturnConditions_InterruptionScenarioOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation]` | 1 |
| `scnInterruptManagerNode[scnNodeId,scnToggleInterruption_InterruptionOperation]` | 3 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 137 |
| `scnStartNode[scnNodeId]` | 15 |
| `scnXorNode[scnNodeId]` | 9 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `78ea9520844d28bb30df` | 16 | `base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene` / scene / 1562 -> 1563 -> 976 |
| `43434b99eea0ba28f666` | 8 | `base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene` / scene / 1103 -> 1469 -> 2553 |
| `4e0b5c05d4cdc9f64d6c` | 8 | `base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene` / scene / 1523 -> 198 -> 2516 |
| `fa2be6c52f80275308f0` | 8 | `base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene` / scene / 1523 -> 198 -> 1469 |
| `88494a5d767bd3558989` | 7 | `base\quest\minor_quests\mq026\scenes\mq026_03_nomad.scene` / scene / 696 -> 638 -> 736 |
| `af6c94a57bc0ca13b4d8` | 7 | `base\quest\minor_quests\mq026\scenes\mq026_03_nomad.scene` / scene / 696 -> 638 -> 736 |
| `b656c00028196994ce71` | 7 | `base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene` / scene / 2378 -> 1230 -> 2255 |
| `1fa539921730278ef7fb` | 6 | `base\quest\minor_quests\mq026\scenes\mq026_02_death.scene` / scene / 162 -> 163 -> 167 |
| `361e09201e38b41ce5ec` | 6 | `base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene` / scene / 1703 -> 1711 -> 1710 |
| `9fc024e5cd759f5eb875` | 6 | `base\quest\minor_quests\mq026\scenes\mq026_04_smuggler.scene` / scene / 278 -> 233 -> 234 |
| `c223afd3fae69e16838b` | 6 | `base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene` / scene / 2022 -> 11 -> 2225 |
| `de490f1a1f721f57a0ec` | 6 | `base\quest\minor_quests\mq026\scenes\mq026_02_death.scene` / scene / 162 -> 165 -> 167 |
| `22097681a5824dd77fb1` | 5 | `base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene` / scene / 2532 -> 2372 -> 2383 |
| `276aca4a2dc348a877d5` | 5 | `base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene` / scene / 99 -> 762 -> 2185 |
| `2a9ea5295242751e0f29` | 5 | `base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene` / scene / 976 -> 2477 -> 4 |
| `2beeeaa3b4da5300c035` | 5 | `base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene` / scene / 1 -> 1562 -> 1563 |
| `4af183bb079d0fad7e8f` | 5 | `base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene` / scene / 1613 -> 1614 -> 1703 |
| `5bf3e634b64c8b260560` | 5 | `base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene` / scene / 1614 -> 1703 -> 1711 |
| `80a3c4b5745a6c91ec8b` | 5 | `base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene` / scene / 450 -> 1001 -> 272 |
| `95d4997362b664c5c23b` | 5 | `base\quest\minor_quests\mq026\scenes\mq026_02_death.scene` / scene / 31 -> 162 -> 163 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
