# base-mq040

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq040\mq040_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq040\mq040_quest_bugfixes.questphase` | repair | 4 / 0 |  |
| `base\quest\minor_quests\mq040\communities\mq040_com_apartment.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq040\communities\mq040_com_corpo.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq040\communities\mq040_com_decoys.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq040\communities\mq040_com_valentinos_coyote.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq040\mq040_biosculpt.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq040\mq040_biosculpt.quest` | content candidate | 1 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq040\mq040_biosculpt.questphase; base\quest\minor_quests\mq040\scenes\mq040_00_chicken_test.scene |
| `base\quest\minor_quests\mq040\mq040_biosculpt.questphase` | content candidate | 6 / 0 | base\quest\minor_quests\mq040\phases\mq040_bar_corpo.questphase; base\quest\minor_quests\mq040\phases\mq040_ripperdoc.questphase; base\quest\minor_quests\mq040\phases\mq040_trail_wife.questphase; base\quest\minor_quests\mq040\scenes\mq040_03_ripperdoc.scene |
| `base\quest\minor_quests\mq040\phases\mq040_bar_corpo.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq040\phases\mq040_bar_fight.questphase; base\quest\minor_quests\mq040\scenes\mq040_01_bar.scene |
| `base\quest\minor_quests\mq040\phases\mq040_bar_fight.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq040\phases\mq040_ripperdoc.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq040\scenes\mq040_03_ripperdoc.scene |
| `base\quest\minor_quests\mq040\phases\mq040_trail_wife.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq040\scenes\mq040_02_trail_wife.scene |
| `base\quest\minor_quests\mq040\scenes\mq040_00_chicken_test.scene` | test/debug | 0 / 17 |  |
| `base\quest\minor_quests\mq040\scenes\mq040_01_bar.scene` | content candidate | 0 / 185 |  |
| `base\quest\minor_quests\mq040\scenes\mq040_02_trail_wife.scene` | content candidate | 0 / 111 |  |
| `base\quest\minor_quests\mq040\scenes\mq040_03_ripperdoc.scene` | content candidate | 0 / 137 |  |

## Journal paths observed in these resources

- `contacts/pepe_el_coyote`
- `contacts/pepe_el_coyote/mq040/01_pepe_not_at_bar`
- `contacts/pepe_el_coyote/mq040/02_aftermath_forgave_wife`
- `contacts/pepe_el_coyote/mq040/02_aftermath_left_wife`
- `contacts/player`
- `contacts/rachel_joestar_mq040`
- `points_of_interest/minor_quests/mq040_biosculpt`
- `quests/minor_quest/mq040_biosculpt`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/01_bar_encounter`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/01_bar_encounter/description`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/01a_intervene_decide`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/02_fight`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/03_talk_corpo`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/03a_go_to_trail_location`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/03b_talk_pepe`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/04_identify_wife`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/05_trail_wife`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/07_follow_inside`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/07a_find_wife`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/07a_find_wife/apartment_mp`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/07a_find_wife/noise_mp`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/08_confront_wife`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/08a_corpo_report_back`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/08b_report_back`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/08b_report_back/contact`
- `quests/minor_quest/mq040_biosculpt/mq040_biosculpt/09_choose_side`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 8 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetLifePath]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 11 |
| `questCheckpointNodeDefinition` | 8 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 13 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCutControlNodeDefinition` | 9 |
| `questDeletionMarkerNodeDefinition` | 12 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerChangeAppearance_NodeType]` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 4 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 3 |
| `questEventManagerNodeDefinition` | 5 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 63 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 12 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 4 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 5 |
| `questInputNodeDefinition` | 23 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 8 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 4 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 43 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 12 |
| `questLogicalXorNodeDefinition` | 4 |
| `questLookAtDrivenTurnsNode` | 8 |
| `questMappinManagerNodeDefinition` | 2 |
| `questMovePuppetNodeDefinition[questFollowParams,questUniversalRef]` | 3 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 3 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 2 |
| `questOutputNodeDefinition` | 18 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 13 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterEquippedItem_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PuppetSubType]` | 2 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType,questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questTriggerCondition,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 10 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questObjectCondition,questScan_ConditionType,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 16 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questPhone_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 34 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 37 |
| `questPhaseNodeDefinition` | 15 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 3 |
| `questPhoneManagerNodeDefinition[questAddRemoveContact_NodeType,questChangeContactList_NodeTypeParams]` | 5 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 2 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 4 |
| `questSceneNodeDefinition[scnCheckSpeakersDistanceInterruptCondition,scnCheckSpeakersDistanceInterruptConditionParams,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 15 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 25 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 7 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 5 |
| `questTimeManagerNodeDefinition[questPauseTime_NodeType]` | 1 |
| `questTimeManagerNodeDefinition[questSetTime_NodeType]` | 3 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questSwitchNameplate_NodeType]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 34 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 4 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 75 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |
| `scnAndNode[scnNodeId]` | 3 |
| `scnChoiceNode[questBuild_ConditionType,questFactsDBCondition,questLifePath_ConditionType,questStatsCondition,questUniversalRef,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 4 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 29 |
| `scnHubNode[scnNodeId]` | 3 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 3 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 3 |
| `scnInterruptManagerNode[scnNodeId,scnToggleInterruption_InterruptionOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 77 |
| `scnStartNode[scnNodeId]` | 20 |
| `scnXorNode[scnNodeId]` | 5 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0fdad4c8a8b4964c866f` | 14 | `base\quest\minor_quests\mq040\scenes\mq040_02_trail_wife.scene` / scene / 43 -> 377 -> 380 |
| `51f8c44d9fad8914cd26` | 7 | `base\quest\minor_quests\mq040\scenes\mq040_02_trail_wife.scene` / scene / 377 -> 380 -> 369 |
| `30e79df3cfe49066a39b` | 6 | `base\quest\minor_quests\mq040\phases\mq040_bar_fight.questphase` / h0 / 33 -> 51 -> 52 |
| `de0cd7501c5c65092241` | 6 | `base\quest\minor_quests\mq040\phases\mq040_bar_fight.questphase` / h0 / 30 -> 44 -> 46 |
| `e5742f9794e6583c67cb` | 6 | `base\quest\minor_quests\mq040\scenes\mq040_03_ripperdoc.scene` / scene / 768 -> 761 -> 762 |
| `3c47849cedaf539b8171` | 5 | `base\quest\minor_quests\mq040\scenes\mq040_02_trail_wife.scene` / scene / 260 -> 30 -> 257 |
| `84bfca44950402ede644` | 5 | `base\quest\minor_quests\mq040\scenes\mq040_01_bar.scene` / scene / 218 -> 100 -> 511 |
| `f6adbdb6fc4cc4cb7d31` | 5 | `base\quest\minor_quests\mq040\scenes\mq040_02_trail_wife.scene` / scene / 260 -> 30 -> 161 |
| `088071139c04172c3ffc` | 4 | `base\quest\minor_quests\mq040\scenes\mq040_02_trail_wife.scene` / scene / 1 -> 312 -> 230 |
| `08d6763cef9d08453eab` | 4 | `base\quest\minor_quests\mq040\phases\mq040_trail_wife.questphase` / h0 / 159 -> 102 -> 115 |
| `101b60945ddf6f25f378` | 4 | `base\quest\minor_quests\mq040\scenes\mq040_03_ripperdoc.scene` / scene / 89 -> 766 -> 769 |
| `34e9486aa08e0d0d2303` | 4 | `base\quest\minor_quests\mq040\scenes\mq040_02_trail_wife.scene` / scene / 231 -> 341 -> 389 |
| `5304e0a14a358a069e82` | 4 | `base\quest\minor_quests\mq040\scenes\mq040_02_trail_wife.scene` / scene / 231 -> 341 -> 342 |
| `61f09677c83cec936502` | 4 | `base\quest\minor_quests\mq040\phases\mq040_trail_wife.questphase` / h0 / 106 -> 159 -> 13 |
| `70df93ff84fab455175b` | 4 | `base\quest\minor_quests\mq040\scenes\mq040_02_trail_wife.scene` / scene / 312 -> 230 -> 4 |
| `821f71c412872f03c27d` | 4 | `base\quest\minor_quests\mq040\scenes\mq040_01_bar.scene` / scene / 358 -> 359 -> 363 |
| `8e7d1b475eef6f30c261` | 4 | `base\quest\minor_quests\mq040\scenes\mq040_02_trail_wife.scene` / scene / 30 -> 161 -> 174 |
| `918280456b225f32ac0d` | 4 | `base\quest\minor_quests\mq040\scenes\mq040_02_trail_wife.scene` / scene / 30 -> 171 -> 174 |
| `93b8ecf4246bafdea8bf` | 4 | `base\quest\minor_quests\mq040\phases\mq040_bar_fight.questphase` / h0 / 51 -> 52 -> 54 |
| `abad188fec995176539e` | 4 | `base\quest\minor_quests\mq040\scenes\mq040_01_bar.scene` / scene / 60 -> 409 -> 680 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
