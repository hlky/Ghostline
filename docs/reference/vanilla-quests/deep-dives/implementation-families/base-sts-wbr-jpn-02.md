# base-sts-wbr-jpn-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\community\sts_wbr_jpn_02.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\community\sts_wbr_jpn_02_bill.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\community\sts_wbr_jpn_02_enemies_basement_floor.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\community\sts_wbr_jpn_02_enemies_ground_floor.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\community\sts_wbr_jpn_02_reinforcements.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\phases\sts_wbr_jpn_02.questphase` | content candidate | 3 / 0 | base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\phases\sts_wbr_jpn_02_combat.questphase; base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\phases\sts_wbr_jpn_02_streetstory.questphase |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\phases\sts_wbr_jpn_02_combat.questphase` | content candidate | 7 / 0 | base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02.scene |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\phases\sts_wbr_jpn_02_streetstory.questphase` | content candidate | 6 / 0 | base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_debriefs.scene; base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_prebrief.scene; base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_lauren.scene |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02.scene` | content candidate | 0 / 15 |  |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_debriefs.scene` | content candidate | 0 / 23 |  |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_lauren.scene` | content candidate | 0 / 33 |  |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_lauren_voiceset_ovr.scene` | content candidate | 0 / 4 |  |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\sts_wbr_jpn_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\sts_wbr_jpn_02.quest` | content candidate | 1 / 0 | base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\phases\sts_wbr_jpn_02.questphase; base\quest\holocalls\holocall_initializers.questphase |

## Journal paths observed in these resources

- `contacts/wakako_okada/sts_wbr_jpn_02/jpn_02_brief`
- `contacts/wakako_okada/sts_wbr_jpn_02/sts_wbr_jpn_02_holocall_debrief`
- `contacts/wakako_okada/wakako_global_msg/sts_fail_warning_001`
- `contacts/wakako_okada/wakako_global_msg/sts_fail_warning_002`
- `contacts/wakako_okada/wakako_global_msg/sts_fixer_car_transport_003`
- `points_of_interest/street_stories/sts_wbr_jpn_02`
- `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_02`
- `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_02/jpn_02_brief`
- `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_02/sts_wbr_jpn_02/escape_workshop_with_bill`
- `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_02/sts_wbr_jpn_02/find_way_inside`
- `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_02/sts_wbr_jpn_02/get_inside`
- `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_02/sts_wbr_jpn_02/get_to_the_basement`
- `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_02/sts_wbr_jpn_02/rescue_bill1`
- `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_02/sts_wbr_jpn_02/tell_lauren_to_get_to_car`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_NodeType,questCharacterManagerParameters_SetCombatSpace]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 3 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 9 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 28 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 16 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 5 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 17 |
| `questLogicalAndNodeDefinition` | 5 |
| `questLogicalHubNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMiscAICommandNode` | 7 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 2 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 2 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 2 |
| `questOutputNodeDefinition` | 10 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questDevice_ConditionType,questJournalCondition,questJournalEntry_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 10 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 14 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 3 |
| `questPhaseNodeDefinition` | 15 |
| `questRandomizerNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 7 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 10 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questTriggerCondition]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 7 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 4 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 4 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 1 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 15 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 4 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 12 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 23 |
| `scnStartNode[scnNodeId]` | 12 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `081b9dbe9528f984ddca` | 7 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_lauren.scene` / scene / 135 -> 155 -> 159 |
| `0523ee3ed1fe0207d8aa` | 6 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_lauren.scene` / scene / 135 -> 155 -> 164 |
| `8cd3b647ae3f592ad947` | 6 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02.scene` / scene / 24 -> 101 -> 27 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_debriefs.scene` / scene / 249 -> 252 -> 258 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_debriefs.scene` / scene / 287 -> 285 -> 289 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_debriefs.scene` / scene / 66 -> 287 -> 285 |
| `138cff49923a75e07348` | 3 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\phases\sts_wbr_jpn_02_streetstory.questphase` / h118 / 147 -> 149 -> 151 |
| `4e9253a72e6b0134b8dd` | 3 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\phases\sts_wbr_jpn_02_streetstory.questphase` / h118 / 149 -> 151 -> 3 |
| `0095b8734f91eca4c413` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\phases\sts_wbr_jpn_02_streetstory.questphase` / h118 / 59 -> 61 -> 72 |
| `101b60945ddf6f25f378` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_debriefs.scene` / scene / 24 -> 65 -> 67 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_debriefs.scene` / scene / 252 -> 61 -> 64 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_debriefs.scene` / scene / 249 -> 252 -> 61 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_prebrief.scene` / scene / 269 -> 273 -> 279 |
| `1d933adb5a617880c93e` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_debriefs.scene` / scene / 65 -> 67 -> 62 |
| `26762f051e7728f090ca` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_debriefs.scene` / scene / 61 -> 64 -> 24 |
| `2beeeaa3b4da5300c035` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_debriefs.scene` / scene / 1 -> 283 -> 66 |
| `2e362801d31d08a7d108` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_debriefs.scene` / scene / 66 -> 60 -> 249 |
| `3fe0ae98a8cf5496b004` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\phases\sts_wbr_jpn_02_streetstory.questphase` / h118 / 139 -> 136 -> 138 |
| `69a2aad2f79abb156101` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_debriefs.scene` / scene / 60 -> 249 -> 252 |
| `802f4eb25ff04e34147e` | 2 | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\scenes\sts_wbr_jpn_02_holocall_debriefs.scene` / scene / 66 -> 60 -> 258 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
