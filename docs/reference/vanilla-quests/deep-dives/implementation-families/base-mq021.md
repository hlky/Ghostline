# base-mq021

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq021\mq021_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq021\mq021_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq021\mq021_quest_bugfixes.questphase` | repair | 6 / 0 |  |
| `base\quest\minor_quests\mq021\communities\mq021_com_bob_car.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq021\communities\mq021_com_doctor.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq021\communities\mq021_com_nomads.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq021\communities\mq021_com_security.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq021\mq021.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq021\mq021.quest` | content candidate | 6 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq021\mq021.questphase; base\quest\minor_quests\mq021\scenes\mq021_00_chicken.scene; base\quest\minor_quests\mq021\test\mq021_00_chicken.scene |
| `base\quest\minor_quests\mq021\mq021.questphase` | content candidate | 3 / 0 | base\quest\minor_quests\mq021\phases\mq021_briefing.questphase; base\quest\minor_quests\mq021\phases\mq021_combat_hospital.questphase; base\quest\minor_quests\mq021\phases\mq021_hospital_meeting.questphase; base\quest\minor_quests\mq021\phases\mq021_outcome.questphase |
| `base\quest\minor_quests\mq021\phases\mq021_briefing.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq021\scenes\mq021_01_briefing.scene |
| `base\quest\minor_quests\mq021\phases\mq021_combat_hospital.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene |
| `base\quest\minor_quests\mq021\phases\mq021_hospital_meeting.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene |
| `base\quest\minor_quests\mq021\phases\mq021_outcome.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene; base\quest\minor_quests\mq021\scenes\mq021_03_ending.scene |
| `base\quest\minor_quests\mq021\scenes\mq021_01_briefing.scene` | content candidate | 0 / 23 |  |
| `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene` | content candidate | 0 / 119 |  |
| `base\quest\minor_quests\mq021\scenes\mq021_03_ending.scene` | content candidate | 0 / 31 |  |
| `base\quest\minor_quests\mq021\test\mq021_00_chicken.scene` | test/debug | 0 / 24 |  |

## Journal paths observed in these resources

- `contacts/bob/mq021/mq021_ending_message`
- `points_of_interest/minor_quests/mq021_guide`
- `quests/minor_quest/mq021_guide`
- `quests/minor_quest/mq021_guide/mq021_guide/01_meet_at_hospital`
- `quests/minor_quest/mq021_guide/mq021_guide/04_meeting`
- `quests/minor_quest/mq021_guide/mq021_guide/04_meeting/mq021_description`
- `quests/minor_quest/mq021_guide/mq021_guide/05_participate_meeting`
- `quests/minor_quest/mq021_guide/mq021_guide/06_defend`
- `quests/minor_quest/mq021_guide/mq021_guide/07_1_kill_doctor`
- `quests/minor_quest/mq021_guide/mq021_guide/07_2_get_suitcase`
- `quests/minor_quest/mq021_guide/mq021_guide/07_confront_doctor`
- `quests/minor_quest/mq021_guide/mq021_guide/08_outcome`
- `quests/minor_quest/mq021_guide/mq021_guide/09_ending`
- `quests/minor_quest/mq021_guide/mq021_guide/10_ending_wait`
- `quests/minor_quest/mq021_guide/mq021_guide/11_ending_read`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 7 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 3 |
| `questCheckpointNodeDefinition` | 8 |
| `questCombatNodeDefinition` | 7 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 14 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 6 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 12 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 1 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 2 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 20 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 6 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 2 |
| `questInputNodeDefinition` | 31 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 3 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 55 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 1 |
| `questOutputNodeDefinition` | 27 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType,questCharacterKilled_ConditionType,questCharacterReaction_ConditionType,questCharacterStatusEffect_CondtionType,questComparisonParam,questLogicalCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 8 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 14 |
| `questPhaseNodeDefinition` | 18 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questPhoneManagerNodeDefinition[questSendMessage_NodeType]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 2 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 5 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 10 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 27 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 4 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 6 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 6 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 24 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 2 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 4 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 4 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 8 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 6 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 8 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 5 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 8 |
| `scnEndNode[scnNodeId]` | 19 |
| `scnHubNode[scnNodeId]` | 5 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 33 |
| `scnStartNode[scnNodeId]` | 11 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `c1b6601d2f647c8a694d` | 6 | `base\quest\minor_quests\mq021\scenes\mq021_01_briefing.scene` / scene / 11 -> 13 -> 18 |
| `38efa89ea367b077425d` | 5 | `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene` / scene / 71 -> 119 -> 118 |
| `3fe0ae98a8cf5496b004` | 4 | `base\quest\minor_quests\mq021\phases\mq021_hospital_meeting.questphase` / h0 / 58 -> 55 -> 57 |
| `eb252b7e42db30cea85d` | 4 | `base\quest\minor_quests\mq021\phases\mq021_hospital_meeting.questphase` / h0 / 55 -> 57 -> 56 |
| `ebdaafaddefbc1080fe8` | 4 | `base\quest\minor_quests\mq021\scenes\mq021_01_briefing.scene` / scene / 4 -> 11 -> 53 |
| `0daf125cb5fafa490651` | 3 | `base\quest\minor_quests\mq021\test\mq021_00_chicken.scene` / scene / 56 -> 4 -> 47 |
| `27faccd7b30abbc3add2` | 3 | `base\quest\minor_quests\mq021\scenes\mq021_01_briefing.scene` / scene / 11 -> 13 -> 20 |
| `415aa42f44aad679ae61` | 3 | `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene` / scene / 119 -> 118 -> 124 |
| `81eccc836b758b3852d2` | 3 | `base\quest\minor_quests\mq021\test\mq021_00_chicken.scene` / scene / 56 -> 4 -> 9 |
| `899371acbb5f2755ffcb` | 3 | `base\quest\minor_quests\mq021\test\mq021_00_chicken.scene` / scene / 56 -> 4 -> 34 |
| `d76536c0caf12fbfca4e` | 3 | `base\quest\minor_quests\mq021\test\mq021_00_chicken.scene` / scene / 56 -> 4 -> 33 |
| `0eb6d1bb64fbd2d01e4e` | 2 | `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene` / scene / 105 -> 149 -> 472 |
| `13fa35e9f4f5287bfd32` | 2 | `base\quest\minor_quests\mq021\phases\mq021_combat_hospital.questphase` / h0 / 27 -> 4 -> 45 |
| `178ff9eba50354aed786` | 2 | `base\quest\minor_quests\mq021\mq021.questphase` / h98 / 0 -> 2 -> 3 |
| `1b714a907ccc60bd98e7` | 2 | `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene` / scene / 105 -> 149 -> 104 |
| `2179acd57cd33a158da3` | 2 | `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene` / scene / 105 -> 149 -> 470 |
| `25aae51001db85d5b1fb` | 2 | `base\quest\minor_quests\mq021\mq021.questphase` / h98 / 4 -> 9 -> 10 |
| `27989a991fbce5b0fc5c` | 2 | `base\quest\minor_quests\mq021\mq021.quest` / h70 / 42 -> 45 -> 46 |
| `2b386cf8829ceeca7ecc` | 2 | `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene` / scene / 78 -> 42 -> 355 |
| `2b8291b6d86672a1ab66` | 2 | `base\quest\minor_quests\mq021\scenes\mq021_03_ending.scene` / scene / 20 -> 22 -> 16 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
