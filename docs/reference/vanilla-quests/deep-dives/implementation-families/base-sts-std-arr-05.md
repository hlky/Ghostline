# base-sts-std-arr-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\community\sts_std_arr_05.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\community\sts_std_arr_05_enemies.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05.questphase` | content candidate | 3 / 0 | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_combat.questphase; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_bugfixing.questphase` | repair | 16 / 0 | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_combat.questphase` | content candidate | 11 / 0 | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\scenes\sts_std_arr_05_guards_talk.scene |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase` | content candidate | 6 / 0 | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\scenes\sts_std_arr_05_fox_talk.scene; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\scenes\sts_std_arr_05_holocall_debriefs.scene; base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\scenes\sts_std_arr_05_holocall_prebrief.scene |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\scenes\sts_std_arr_05_fox_talk.scene` | content candidate | 0 / 116 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\scenes\sts_std_arr_05_guards_talk.scene` | content candidate | 0 / 4 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\scenes\sts_std_arr_05_holocall_debriefs.scene` | content candidate | 0 / 28 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\scenes\sts_std_arr_05_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\sts_std_arr_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\sts_std_arr_05.quest` | content candidate | 1 / 0 | base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\sts_std_arr_05_test.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/muamar_el_capitan_reyes/sts_std_arr_05/brief`
- `contacts/muamar_el_capitan_reyes/sts_std_arr_05/sts_std_arr_05_debrief`
- `contacts/muamar_el_capitan_reyes/sts_std_arr_05/sts_std_arr_05_debrief_failed`
- `contacts/muamar_el_capitan_reyes/sts_std_arr_05/sts_std_arr_05_debrief_non_perfect`
- `points_of_interest/street_stories/sts_std_arr_05`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/brief`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/be_unseen`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/collect_reward`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/escape`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/get_into_car`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/get_to_the_factory_parking`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/go_back_to_parking`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/install_a_tracking_chip`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/meet_with_ted`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/sit_with_ted`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/speak_with_ted`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05/sts_std_arr_05/take_tracking_device`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 6 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 38 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 22 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 3 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 5 |
| `questConditionNodeDefinition[questSpawnerCondition,questSpawnerReady_ConditionType]` | 3 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleCorrectlyPlaced_ConditionType]` | 1 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 33 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 3 |
| `questEventManagerNodeDefinition` | 17 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 69 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 10 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 2 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 2 |
| `questInputNodeDefinition` | 41 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 22 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 50 |
| `questLogicalAndNodeDefinition` | 5 |
| `questLogicalHubNodeDefinition` | 11 |
| `questLogicalXorNodeDefinition` | 4 |
| `questMiscAICommandNode` | 4 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 26 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 5 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 28 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questSceneCondition,questSceneNode_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 18 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckSpeakerDistractedInterruptCondition]` | 1 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 11 |
| `questPhaseNodeDefinition` | 27 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 8 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneNodeDefinition[scnCheckPlayerTargetEntityDistanceInterruptCondition,scnCheckPlayerTargetEntityDistanceInterruptConditionParams,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 25 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 12 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 5 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 13 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 7 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 3 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 6 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 35 |
| `questVehicleNodeDefinition[questToggleWindow_NodeType]` | 3 |
| `questVisionModesManagerNodeDefinition[questForceModule_NodeType,questForceVMModule_NodeTypeParams]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `scnAndNode[scnNodeId]` | 4 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToPropParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnPropId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 4 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 6 |
| `scnHubNode[scnNodeId]` | 13 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnNodeId,scnToggleInterruption_InterruptionOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 19 |
| `scnStartNode[scnNodeId]` | 5 |
| `scnXorNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `f22666c6edee69ab2bcf` | 21 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase` / h1849 / 41 -> 38 -> 35 |
| `1df95a39b365f9f60e15` | 16 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase` / h298 / 126 -> 125 -> 121 |
| `3b6a1bfe5272b3ca2c22` | 16 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase` / h298 / 126 -> 121 -> 120 |
| `dbbeb65ae81a06c8c460` | 16 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase` / h298 / 125 -> 121 -> 120 |
| `2be296de9cd6ded33fbd` | 13 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase` / h298 / 127 -> 126 -> 121 |
| `abbf46d00a7c0ae464b9` | 13 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase` / h298 / 128 -> 126 -> 121 |
| `eaf5aab427d50e5598b6` | 13 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_bugfixing.questphase` / h14 / 0 -> 2 -> 3 |
| `a5f6ff0df46f7043f2b5` | 11 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_bugfixing.questphase` / h621 / 16 -> 15 -> 17 |
| `567af74b7dd6d13a50b6` | 8 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\scenes\sts_std_arr_05_fox_talk.scene` / scene / 1 -> 138 -> 178 |
| `5c76d3bf7160f29b884f` | 8 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_bugfixing.questphase` / h171 / 2 -> 3 -> 6 |
| `dc48f83319851f657887` | 7 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase` / h1849 / 38 -> 35 -> 28 |
| `ef1f1c4d9ff5cba71b71` | 7 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_bugfixing.questphase` / h0 / 4 -> 10 -> 6 |
| `013375374b65a2068b38` | 6 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase` / h12 / 61 -> 29 -> 42 |
| `24f2825e5ba7dcfb8194` | 6 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase` / h12 / 71 -> 40 -> 30 |
| `44dfad7fb561a3101d17` | 6 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase` / h12 / 65 -> 29 -> 42 |
| `47d2d60daf4a94e81e2f` | 6 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\scenes\sts_std_arr_05_fox_talk.scene` / scene / 78 -> 544 -> 548 |
| `a30ab97044b8dba269d9` | 6 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase` / h12 / 40 -> 30 -> 61 |
| `b231fb602f3c750f613b` | 6 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase` / h12 / 62 -> 29 -> 42 |
| `b9625312537655891eec` | 6 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase` / h12 / 64 -> 29 -> 42 |
| `c77daadb30200e5de754` | 6 | `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\phases\sts_std_arr_05_openworld.questphase` / h12 / 39 -> 29 -> 42 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
