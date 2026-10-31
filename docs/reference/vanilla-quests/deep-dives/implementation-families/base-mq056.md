# base-mq056

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\minor_quests\mq056\community\mq056_01_citycenter.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq056\community\mq056_02_badlands.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq056\community\mq056_03_santodomingo.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq056\community\mq056_04_westbrook.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq056\community\mq056_johnny.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq056\mq056.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq056\mq056.quest` | content candidate | 2 / 0 | base\quest\minor_quests\mq056\mq056.questphase; base\quest\minor_quests\mq056\test\01_chickentest.scene |
| `base\quest\minor_quests\mq056\mq056.questphase` | content candidate | 37 / 0 | base\quest\minor_quests\mq056\phases\mq056_00_main.questphase; base\quest\minor_quests\mq056\phases\mq056_00_prevention_fail.questphase; base\quest\minor_quests\mq056\phases\mq056_01_citycenter.questphase; base\quest\minor_quests\mq056\phases\mq056_02_badlands.questphase; base\quest\minor_quests\mq056\phases\mq056_03_santo_domingo.questphase; base\quest\minor_quests\mq056\phases\mq056_04_big_race.questphase; base\quest\side_quests\sq024\phases\text_messages\sq024_00_msg_city_race.questphase; base\quest\side_quests\sq024\scenes\sq024_04_city_race.scene; base\quest\side_quests\sq024\scenes\sq024_04b_docks_scene.scene |
| `base\quest\minor_quests\mq056\phases\mq056_00_main.questphase` | content candidate | 10 / 0 | base\quest\minor_quests\mq056\scenes\mq056_01_city_race.scene; base\quest\minor_quests\mq056\scenes\mq056_02_badlands.scene; base\quest\minor_quests\mq056\scenes\mq056_03_santo_domingo.scene; base\quest\minor_quests\mq056\scenes\mq056_04_big_race.scene |
| `base\quest\minor_quests\mq056\phases\mq056_00_prevention_fail.questphase` | content candidate | 18 / 0 |  |
| `base\quest\minor_quests\mq056\phases\mq056_01_citycenter.questphase` | content candidate | 45 / 0 | base\quest\minor_quests\mq056\scenes\mq056_00_commentary.scene; base\quest\minor_quests\mq056\scenes\mq056_01_city_race.scene; base\quest\side_quests\sq024\scenes\sq024_04_city_race.scene |
| `base\quest\minor_quests\mq056\phases\mq056_02_badlands.questphase` | content candidate | 49 / 0 | base\quest\minor_quests\mq056\scenes\mq056_00_commentary.scene; base\quest\minor_quests\mq056\scenes\mq056_02_badlands.scene; base\quest\side_quests\sq024\scenes\sq024_03b_badlands_race_end.scene; base\quest\side_quests\sq024\scenes\sq024_04_city_race.scene |
| `base\quest\minor_quests\mq056\phases\mq056_03_santo_domingo.questphase` | content candidate | 44 / 0 | base\quest\minor_quests\mq056\scenes\mq056_00_commentary.scene; base\quest\minor_quests\mq056\scenes\mq056_03_santo_domingo.scene; base\quest\side_quests\sq024\scenes\sq024_04_city_race.scene |
| `base\quest\minor_quests\mq056\phases\mq056_04_big_race.questphase` | content candidate | 54 / 0 | base\quest\minor_quests\mq056\scenes\mq056_00_commentary.scene; base\quest\minor_quests\mq056\scenes\mq056_04_big_race.scene; base\quest\side_quests\sq024\phases\text_messages\sq024_03_msg_big_race.questphase; base\quest\side_quests\sq024\scenes\sq024_04_city_race.scene |
| `base\quest\minor_quests\mq056\scenes\mq056_00_commentary.scene` | content candidate | 0 / 44 |  |
| `base\quest\minor_quests\mq056\scenes\mq056_01_city_race.scene` | content candidate | 0 / 42 |  |
| `base\quest\minor_quests\mq056\scenes\mq056_02_badlands.scene` | content candidate | 0 / 54 |  |
| `base\quest\minor_quests\mq056\scenes\mq056_03_santo_domingo.scene` | content candidate | 0 / 43 |  |
| `base\quest\minor_quests\mq056\scenes\mq056_04_big_race.scene` | content candidate | 0 / 47 |  |
| `base\quest\minor_quests\mq056\test\01_chickentest.scene` | test/debug | 0 / 19 |  |

## Journal paths observed in these resources

- `contacts/announcer_mq056/mq056_hook/00_hi`
- `contacts/announcer_mq056/mq056_hook/01_hook1`
- `contacts/announcer_mq056/mq056_hook/01_hook2`
- `contacts/announcer_mq056/mq056_hook/02_response`
- `contacts/announcer_mq056/mq056_hook/02_response/01_yes`
- `contacts/announcer_mq056/mq056_hook/02_response/02_no`
- `contacts/announcer_mq056/mq056_hook/03_answer_no`
- `contacts/announcer_mq056/mq056_hook/03_answer_yes`
- `contacts/marianne`
- `contacts/player`
- `points_of_interest/street_race/mq056_badlands_poi`
- `points_of_interest/street_race/mq056_big_race_poi`
- `points_of_interest/street_race/mq056_city_center_poi`
- `points_of_interest/street_race/mq056_santo_domingo_poi`
- `quests/meta/07_nc_underground/03_races/00_beat_races`
- `quests/meta/07_nc_underground/03_races/01_complete_big_race/race`
- `quests/minor_quest/mq056_race_replay`
- `quests/minor_quest/mq056_race_replay/00_hook_sms`
- `quests/minor_quest/mq056_race_replay/00_hook_sms/00_hook/message`
- `quests/minor_quest/mq056_race_replay/01_city_center`
- `quests/minor_quest/mq056_race_replay/01_city_center/01_get_in`
- `quests/minor_quest/mq056_race_replay/01_city_center/01a_wait_for_race`
- `quests/minor_quest/mq056_race_replay/01_city_center/01a_wait_for_race1`
- `quests/minor_quest/mq056_race_replay/01_city_center/02_beat_race`
- `quests/minor_quest/mq056_race_replay/01_city_center/02_beat_race/racer_1`
- `quests/minor_quest/mq056_race_replay/01_city_center/02_beat_race/racer_2`
- `quests/minor_quest/mq056_race_replay/01_city_center/02_beat_race/racer_3`
- `quests/minor_quest/mq056_race_replay/01_city_center/02_beat_race/racer_4`
- `quests/minor_quest/mq056_race_replay/01_city_center/02_beat_race/racer_5`
- `quests/minor_quest/mq056_race_replay/01_city_center/04_get_reward`
- `quests/minor_quest/mq056_race_replay/01_city_center/04_get_reward/reward_crate`
- `quests/minor_quest/mq056_race_replay/02_badlands`
- `quests/minor_quest/mq056_race_replay/02_badlands/01_get_in`
- `quests/minor_quest/mq056_race_replay/02_badlands/01a_wait_for_race`
- `quests/minor_quest/mq056_race_replay/02_badlands/02_beat_race`
- `quests/minor_quest/mq056_race_replay/02_badlands/02_beat_race/racer_1`
- `quests/minor_quest/mq056_race_replay/02_badlands/02_beat_race/racer_2`
- `quests/minor_quest/mq056_race_replay/02_badlands/02_beat_race/racer_3`
- `quests/minor_quest/mq056_race_replay/02_badlands/02_beat_race/racer_4`
- `quests/minor_quest/mq056_race_replay/02_badlands/02_beat_race/racer_5`
- `quests/minor_quest/mq056_race_replay/02_badlands/04_get_reward`
- `quests/minor_quest/mq056_race_replay/02_badlands/04_get_reward/reward_crate`
- `quests/minor_quest/mq056_race_replay/03_santo_domingo`
- `quests/minor_quest/mq056_race_replay/03_santo_domingo/01_get_in`
- `quests/minor_quest/mq056_race_replay/03_santo_domingo/01a_wait_for_race`
- `quests/minor_quest/mq056_race_replay/03_santo_domingo/02_beat_race`
- `quests/minor_quest/mq056_race_replay/03_santo_domingo/02_beat_race/racer_1`
- `quests/minor_quest/mq056_race_replay/03_santo_domingo/02_beat_race/racer_2`
- `quests/minor_quest/mq056_race_replay/03_santo_domingo/02_beat_race/racer_3`
- `quests/minor_quest/mq056_race_replay/03_santo_domingo/02_beat_race/racer_4`
- `quests/minor_quest/mq056_race_replay/03_santo_domingo/02_beat_race/racer_5`
- `quests/minor_quest/mq056_race_replay/03_santo_domingo/04_get_reward`
- `quests/minor_quest/mq056_race_replay/03_santo_domingo/04_get_reward/reward_crate`
- `quests/minor_quest/mq056_race_replay/04_big_race`
- `quests/minor_quest/mq056_race_replay/04_big_race/01_get_in`
- `quests/minor_quest/mq056_race_replay/04_big_race/01a_wait_for_race`
- `quests/minor_quest/mq056_race_replay/04_big_race/02_beat_race`
- `quests/minor_quest/mq056_race_replay/04_big_race/02_beat_race/racer_1`
- `quests/minor_quest/mq056_race_replay/04_big_race/02_beat_race/racer_2`
- `quests/minor_quest/mq056_race_replay/04_big_race/02_beat_race/racer_3`
- `quests/minor_quest/mq056_race_replay/04_big_race/02_beat_race/racer_4`
- `quests/minor_quest/mq056_race_replay/04_big_race/02_beat_race/racer_5`
- `quests/minor_quest/mq056_race_replay/04_big_race/04_get_reward`
- `quests/minor_quest/mq056_race_replay/04_big_race/04_get_reward/reward_crate`
- `quests/minor_quest/mq056_race_replay/description`
- `quests/side_quest/sq024_badlands_race/02_santo_domingo_race/04_beat_race`
- `quests/side_quest/sq024_city_race`
- `quests/side_quest/sq024_city_race/02_santo_domingo_race/00_go_to_race`
- `quests/side_quest/sq024_city_race/02_santo_domingo_race/00_go_to_race/description`
- `quests/side_quest/sq024_city_race/02_santo_domingo_race/01_talk_claire`
- `quests/side_quest/sq024_city_race/02_santo_domingo_race/01b_call_claire`
- `quests/side_quest/sq024_city_race/02_santo_domingo_race/01b_call_claire/claire`
- `quests/side_quest/sq024_city_race/02_santo_domingo_race/03_get_in`
- `quests/side_quest/sq024_city_race/02_santo_domingo_race/03b_get_in_v`
- `quests/side_quest/sq024_city_race/02_santo_domingo_race/03c_wait_for_race`
- `quests/side_quest/sq024_city_race/02_santo_domingo_race/04_beat_race`
- `quests/side_quest/sq024_city_race/02_santo_domingo_race/05_stop_at_finish`
- `quests/side_quest/sq024_city_race/02_santo_domingo_race/06_talk_claire`
- `quests/side_quest/sq024_city_race/02_santo_domingo_race/09_talk_claire`
- `quests/side_quest/sq024_city_race/02_santo_domingo_race/10_get_in_drive_garage`
- `quests/side_quest/sq024_city_race/02_santo_domingo_race/11_drive_garage`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 9 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 23 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 195 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 56 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 100 |
| `questCheckpointNodeDefinition` | 11 |
| `questCombatNodeDefinition` | 300 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 145 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 4 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 26 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 20 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 20 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 140 |
| `questConditionNodeDefinition[questInputAction_ConditionType,questSystemCondition]` | 6 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 24 |
| `questCutControlNodeDefinition` | 296 |
| `questDeletionMarkerNodeDefinition` | 127 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerSetAttachment_NodeType,questEntityManagerSetAttachment_ToActor]` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerSetAttachment_NodeType,questEntityManagerSetAttachment_ToWorld]` | 2 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_NodeType,questPlayEnv_NodeTypeParams]` | 4 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 18 |
| `questEventManagerNodeDefinition` | 39 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 24 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 491 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 15 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 4 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 59 |
| `questInputNodeDefinition` | 309 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 9 |
| `questItemManagerNodeDefinition[questReInitContainers_NodeType,questReInitContainers_NodeTypeParams]` | 8 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 149 |
| `questJournalNodeDefinition[questJournalQuestObjectiveCounter_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalTrackQuest_NodeType]` | 4 |
| `questLogicalAndNodeDefinition` | 164 |
| `questLogicalHubNodeDefinition` | 167 |
| `questLogicalXorNodeDefinition` | 146 |
| `questMappinManagerNodeDefinition` | 23 |
| `questMiscAICommandNode` | 15 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 2 |
| `questOutputNodeDefinition` | 271 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 55 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 162 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 35 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition,questVehicleCondition,questVehicleSpawned_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 32 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 54 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 15 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 359 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInputAction_ConditionType,questSystemCondition]` | 7 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 4 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition,questVehicleCondition,questVehicleSpeed_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questPhone_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 543 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 10 |
| `questPauseConditionNodeDefinition[questTimeCondition,questTimePeriod_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 184 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 40 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpeed_ConditionType]` | 4 |
| `questPhaseNodeDefinition` | 242 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 16 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 1 |
| `questRandomizerNodeDefinition` | 40 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 22 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 20 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 4 |
| `questSceneNodeDefinition[scnWorldMarker]` | 66 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 171 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 7 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 53 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 8 |
| `questTimeManagerNodeDefinition[questPauseTime_NodeType]` | 10 |
| `questTimeManagerNodeDefinition[questSetTime_NodeType]` | 6 |
| `questTimeManagerNodeDefinition[questShiftTime_NodeType]` | 4 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 6 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 8 |
| `questUIManagerNodeDefinition[questShowCustomTooltip_NodeType]` | 18 |
| `questUIManagerNodeDefinition[questShowOnscreen_NodeType]` | 4 |
| `questUIManagerNodeDefinition[questWarningMessage_NodeType]` | 55 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 8 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 6 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 318 |
| `questVehicleNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 220 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 22 |
| `questVehicleNodeDefinition[questGoBackToRace_NodeType]` | 6 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 1 |
| `questVehicleNodeDefinition[questRepair_NodeType]` | 8 |
| `questVehicleNodeDefinition[questRequestVehicleCameraPerspective_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSetCanVehicleBeRemoteControlled_NodeType]` | 179 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 15 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 11 |
| `questVehicleNodeDefinition[questStartRace_NodeType]` | 5 |
| `questVehicleNodeDefinition[questStopRace_NodeType]` | 9 |
| `questVehicleNodeDefinition[questTeleportPuppetParams,questTeleport_NodeType,questUniversalRef]` | 13 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 78 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 17 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 5 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 4 |
| `questWorldDataManagerNodeDefinition[questPrefetchStreaming_NodeTypeV2]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 284 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 157 |
| `scnAndNode[scnNodeId]` | 3 |
| `scnChoiceNode[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterMount_ConditionType,questFactsDBCondition,questLogicalCondition,questPaymentCondition,questPaymentFixedAmount_ConditionType,questVarComparison_ConditionType,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questPaymentCondition,questPaymentFixedAmount_ConditionType,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 4 |
| `scnDeletionMarkerNode[scnNodeId]` | 14 |
| `scnEndNode[scnNodeId]` | 33 |
| `scnHubNode[scnNodeId]` | 2 |
| `scnRandomizerNode[scnNodeId]` | 5 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 40 |
| `scnStartNode[scnNodeId]` | 21 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `1c16b560dba43be06e48` | 263 | `base\quest\minor_quests\mq056\mq056.questphase` / h2393 / 8 -> 11 -> 10 |
| `ca13ee814a9081c6e047` | 263 | `base\quest\minor_quests\mq056\mq056.questphase` / h2393 / 11 -> 10 -> 13 |
| `ee6b8aa5c2cf5ddd5af3` | 234 | `base\quest\minor_quests\mq056\mq056.questphase` / h526 / 95 -> 100 -> 50 |
| `a270042bcd7b1bc90a84` | 135 | `base\quest\minor_quests\mq056\mq056.questphase` / h433 / 190 -> 191 -> 192 |
| `8659a4a40b0245a6b139` | 130 | `base\quest\minor_quests\mq056\mq056.questphase` / h526 / 106 -> 95 -> 100 |
| `0f374ac8f753ecdc05b1` | 108 | `base\quest\minor_quests\mq056\mq056.questphase` / h526 / 0 -> 57 -> 114 |
| `18952830090f764da771` | 106 | `base\quest\minor_quests\mq056\mq056.questphase` / h526 / 107 -> 71 -> 76 |
| `3e993cda136a8512fd06` | 106 | `base\quest\minor_quests\mq056\mq056.questphase` / h526 / 57 -> 114 -> 50 |
| `92710f4359397ea0190c` | 106 | `base\quest\minor_quests\mq056\mq056.questphase` / h526 / 66 -> 107 -> 71 |
| `95b57241e4ecf401223e` | 106 | `base\quest\minor_quests\mq056\mq056.questphase` / h526 / 100 -> 71 -> 76 |
| `2885cde30c2ac30e964d` | 105 | `base\quest\minor_quests\mq056\mq056.questphase` / h526 / 57 -> 114 -> 83 |
| `42d8fe4ef95b8242db88` | 105 | `base\quest\minor_quests\mq056\mq056.questphase` / h526 / 105 -> 106 -> 95 |
| `3c1d23e6029fae739e9f` | 91 | `base\quest\minor_quests\mq056\mq056.questphase` / h526 / 114 -> 83 -> 119 |
| `3eb9130586a7dc478884` | 80 | `base\quest\minor_quests\mq056\mq056.questphase` / h526 / 83 -> 66 -> 107 |
| `ef74b9c35af1e1aa18c1` | 80 | `base\quest\minor_quests\mq056\mq056.questphase` / h526 / 114 -> 83 -> 66 |
| `1eb39b7557e061a7db8a` | 75 | `base\quest\minor_quests\mq056\phases\mq056_00_prevention_fail.questphase` / h473 / 0 -> 3 -> 26 |
| `691b9eea6cb58340e82f` | 75 | `base\quest\minor_quests\mq056\phases\mq056_00_prevention_fail.questphase` / h473 / 41 -> 42 -> 11 |
| `9af8a87f20a910659fa8` | 75 | `base\quest\minor_quests\mq056\phases\mq056_01_citycenter.questphase` / h7262 / 9 -> 10 -> 11 |
| `e869fae38e581d82f985` | 67 | `base\quest\minor_quests\mq056\mq056.questphase` / h526 / 83 -> 119 -> 62 |
| `c6658c10a20ba3ee6ef6` | 60 | `base\quest\minor_quests\mq056\mq056.questphase` / h1655 / 54 -> 55 -> 56 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
