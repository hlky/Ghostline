# base-sq032

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\sidequests\sq032\sq032_cinematic_bugfixes.questphase` | repair | 4 / 0 | base\quest\side_quests\sq032\scenes\sq032_05_fifth_episode.scene |
| `base\quest\bugfixing\sidequests\sq032\sq032_quest_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\side_quests\sq032\phases\sq032_episode_3.questphase` | content candidate | 1 / 0 | base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene |
| `base\quest\side_quests\sq032\phases\sq032_episode_4.questphase` | content candidate | 1 / 0 | base\quest\side_quests\sq032\scenes\sq032_04_fourth_episode.scene |
| `base\quest\side_quests\sq032\phases\sq032_episode_5.questphase` | content candidate | 1 / 0 | base\quest\side_quests\sq032\scenes\sq032_05_fifth_episode.scene |
| `base\quest\side_quests\sq032\phases\sq032_episode_6.questphase` | content candidate | 4 / 0 | base\quest\side_quests\sq032\scenes\sq032_06_sixth_episode.scene |
| `base\quest\side_quests\sq032\phases\sq032_finale.questphase` | content candidate | 1 / 0 | base\quest\side_quests\sq032\scenes\sq032_07_finale.scene |
| `base\quest\side_quests\sq032\phases\sq032_sickness.questphase` | content candidate | 2 / 0 | base\quest\side_quests\sq032\scenes\sq032_00_sickness.scene |
| `base\quest\side_quests\sq032\phases\sq032_tapeworm_setup.questphase` | content candidate | 5 / 0 |  |
| `base\quest\side_quests\sq032\scenes\sq032_00_sickness.scene` | content candidate | 0 / 183 |  |
| `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` | content candidate | 0 / 172 |  |
| `base\quest\side_quests\sq032\scenes\sq032_04_fourth_episode.scene` | content candidate | 0 / 248 |  |
| `base\quest\side_quests\sq032\scenes\sq032_05_fifth_episode.scene` | content candidate | 0 / 191 |  |
| `base\quest\side_quests\sq032\scenes\sq032_06_sixth_episode.scene` | content candidate | 0 / 70 |  |
| `base\quest\side_quests\sq032\scenes\sq032_07_finale.scene` | content candidate | 0 / 222 |  |
| `base\quest\side_quests\sq032\sq032.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\side_quests\sq032\sq032.quest` | content candidate | 12 / 0 | base\quest\additional_game_elements.questphase; base\quest\main_quests\part1\q104\q104.questphase; base\quest\main_quests\part1\q105\phases\q105_complete.questphase; base\quest\main_quests\part1\q110\q110b.questphase; base\quest\main_quests\part1\q112\q112_abduction.questphase; base\quest\side_quests\sq032\scenes\sq032_00_sickness.scene; base\quest\side_quests\sq032\sq032.questphase; base\quest\side_quests\sq032\test\sq032_chicken_test.scene |
| `base\quest\side_quests\sq032\sq032.questphase` | content candidate | 3 / 0 | base\quest\side_quests\sq032\phases\sq032_episode_3.questphase; base\quest\side_quests\sq032\phases\sq032_episode_4.questphase; base\quest\side_quests\sq032\phases\sq032_episode_5.questphase; base\quest\side_quests\sq032\phases\sq032_episode_6.questphase; base\quest\side_quests\sq032\phases\sq032_finale.questphase |
| `base\quest\side_quests\sq032\test\sq032_chicken_test.scene` | test/debug | 0 / 65 |  |

## Journal paths observed in these resources

- `quests/meta/02_sickness/q115/00_call_hanako`
- `quests/meta/02_sickness/q115/02_meet_hanako`
- `quests/side_quest/sq031_rogue/afterlife/01_go_to_afterlife`
- `quests/side_quest/sq032_tapeworm`
- `quests/side_quest/sq032_tapeworm/00_johnny/00_take_pill`
- `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny`
- `quests/side_quest/sq032_tapeworm/00_johnny/00_talk_with_johnny/description`
- `quests/side_quest/sq032_tapeworm/00_johnny/01_sit_down`
- `quests/side_quest/sq032_tapeworm/00_johnny/03_break_window`
- `quests/side_quest/sq032_tapeworm/00_johnny/04_open_cache`
- `quests/side_quest/sq032_tapeworm/00_johnny/06_leave_motel_room`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 7 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 8 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAnimset]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGender,questSetGender_NodeTypeParams]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetLifePath]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 59 |
| `questCharacterManagerNodeDefinition[questCharacterManagerVisuals_ChangeEntityAppearance,questCharacterManagerVisuals_EntityAppearanceOperationBaseEntityAppearanceEntry,questCharacterManagerVisuals_NodeType]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerVisuals_EntityAppearanceOperationBaseEntityAppearanceEntry,questCharacterManagerVisuals_NodeType,questCharacterManagerVisuals_PrefetchEntityAppearance]` | 1 |
| `questCheckpointNodeDefinition` | 4 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterGender_CondtionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 36 |
| `questConditionNodeDefinition[questLifePath_ConditionType,questStatsCondition,questUniversalRef]` | 4 |
| `questConditionNodeDefinition[questTriggerCondition]` | 14 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 24 |
| `questDeletionMarkerNodeDefinition` | 25 |
| `questEndNodeDefinition` | 1 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 2 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 4 |
| `questEventManagerNodeDefinition` | 14 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 7 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 117 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 28 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questRemoveToken_NodeSubType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 11 |
| `questGameManagerNodeDefinition[questRumble_NodeType]` | 4 |
| `questInputNodeDefinition` | 41 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 3 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 36 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 7 |
| `questLogicalXorNodeDefinition` | 3 |
| `questOutputNodeDefinition` | 32 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questSceneCondition,questSceneTier_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questFactsDBCondition,questLogicalCondition,questSceneCondition,questSceneTier_ConditionType,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questContentCondition,questContentLock_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questSceneCondition,questSceneTier_ConditionType,questVarComparison_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionFunctionParameter,questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 24 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 69 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 15 |
| `questPhaseNodeDefinition` | 29 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 4 |
| `questRenderFxManagerNodeDefinition[questSetCyberspacePostFX_NodeType]` | 2 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 5 |
| `questSceneManagerNodeDefinition[questPlayerLookAt_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questSetTier2Params_NodeType]` | 6 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 23 |
| `questSceneManagerNodeDefinition[questToggleEventExecutionTag_NodeType]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 36 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questScene_NodeType,questSpawnManagerNodeActionEntry]` | 10 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 8 |
| `questTimeManagerNodeDefinition[questPauseTime_NodeType]` | 2 |
| `questTimeManagerNodeDefinition[questSetTime_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questSetHUDEntryForcedVisibility_NodeType]` | 3 |
| `questUIManagerNodeDefinition[questShowOnscreen_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questWarningMessage_NodeType]` | 15 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 46 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 38 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 136 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 26 |
| `questWorldDataManagerNodeDefinition[questPrefetchStreaming_NodeTypeV2]` | 5 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 5 |
| `scnAndNode[scnNodeId]` | 18 |
| `scnChoiceNode[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 5 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 37 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 5 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 7 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 8 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 3 |
| `scnCutControlNode[scnNodeId]` | 3 |
| `scnDeletionMarkerNode[scnNodeId]` | 9 |
| `scnEndNode[scnNodeId]` | 23 |
| `scnHubNode[scnNodeId]` | 68 |
| `scnRandomizerNode[scnNodeId]` | 17 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 256 |
| `scnStartNode[scnNodeId]` | 38 |
| `scnXorNode[scnNodeId]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `c1b6601d2f647c8a694d` | 29 | `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` / scene / 152 -> 154 -> 150 |
| `27faccd7b30abbc3add2` | 22 | `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` / scene / 152 -> 154 -> 157 |
| `e53af017267e2b173704` | 22 | `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` / scene / 198 -> 139 -> 143 |
| `95d4997362b664c5c23b` | 21 | `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` / scene / 198 -> 139 -> 141 |
| `65e99f81f409743aebe3` | 16 | `base\quest\side_quests\sq032\scenes\sq032_04_fourth_episode.scene` / scene / 16 -> 36 -> 43 |
| `1d4ec6ef90134c9e080e` | 14 | `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` / scene / 107 -> 137 -> 422 |
| `9af8a87f20a910659fa8` | 14 | `base\quest\side_quests\sq032\phases\sq032_episode_3.questphase` / h0 / 48 -> 89 -> 83 |
| `84bfca44950402ede644` | 13 | `base\quest\side_quests\sq032\scenes\sq032_04_fourth_episode.scene` / scene / 872 -> 326 -> 589 |
| `facd1dcb1e61742aa116` | 13 | `base\quest\side_quests\sq032\scenes\sq032_00_sickness.scene` / scene / 1446 -> 1458 -> 1465 |
| `18940bb88414fed7fad4` | 12 | `base\quest\side_quests\sq032\phases\sq032_tapeworm_setup.questphase` / h244 / 2 -> 3 -> 4 |
| `276aca4a2dc348a877d5` | 12 | `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` / scene / 113 -> 193 -> 428 |
| `56baebc755e8a9b366f5` | 11 | `base\quest\side_quests\sq032\scenes\sq032_07_finale.scene` / scene / 184 -> 192 -> 197 |
| `7a6fa556057aeab3256d` | 11 | `base\quest\side_quests\sq032\phases\sq032_episode_3.questphase` / h0 / 66 -> 48 -> 89 |
| `79d80ebf381e75113d0d` | 10 | `base\quest\side_quests\sq032\phases\sq032_episode_3.questphase` / h0 / 74 -> 48 -> 89 |
| `a00e803c56151b175aaf` | 10 | `base\quest\side_quests\sq032\phases\sq032_episode_3.questphase` / h0 / 66 -> 70 -> 91 |
| `be6f2309066016a2fedc` | 10 | `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` / scene / 307 -> 309 -> 314 |
| `eb8179e91d6143a6eaaf` | 10 | `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` / scene / 113 -> 193 -> 178 |
| `16d1d6a285a08b87cd77` | 9 | `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` / scene / 3819 -> 80 -> 656 |
| `34c394727aa919c46d56` | 9 | `base\quest\side_quests\sq032\scenes\sq032_03_third_episode.scene` / scene / 198 -> 139 -> 218 |
| `45cc1ff6a994fc237a6a` | 9 | `base\quest\side_quests\sq032\scenes\sq032_00_sickness.scene` / scene / 25 -> 34 -> 45 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
