# base-mq016

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq016\mq016_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq016\mq016_quest_bugfixes.questphase` | repair | 3 / 0 |  |
| `base\quest\minor_quests\mq016\mq016_bartmoss.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq016\mq016_bartmoss.quest` | content candidate | 3 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq016\mq016_bartmoss.questphase; base\quest\minor_quests\mq016\test\mq016_00_chickentest.scene |
| `base\quest\minor_quests\mq016\mq016_bartmoss.questphase` | content candidate | 4 / 0 | base\quest\minor_quests\mq016\phases\mq016_00_shard.questphase; base\quest\minor_quests\mq016\phases\mq016_01_freezer.questphase; base\quest\minor_quests\mq016\phases\mq016_02_afterlife.questphase |
| `base\quest\minor_quests\mq016\phases\mq016_00_shard.questphase` | content candidate | 2 / 0 |  |
| `base\quest\minor_quests\mq016\phases\mq016_01_freezer.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq016\scenes\mq016_01_freezer.scene |
| `base\quest\minor_quests\mq016\phases\mq016_02_afterlife.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene |
| `base\quest\minor_quests\mq016\scenes\mq016_01_freezer.scene` | content candidate | 0 / 97 |  |
| `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` | content candidate | 0 / 138 |  |
| `base\quest\minor_quests\mq016\test\mq016_00_chickentest.scene` | test/debug | 0 / 20 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_quest/mq015_wizardbook/mq015_wizardbook_files`
- `onscreens/emails/quests/minor_quest/mq016_bartmoss/mq016_data_shard/mq016_00_data_shard`
- `points_of_interest/minor_quests/mq016_bartmoss`
- `quests/minor_quest/mq016_bartmoss`
- `quests/minor_quest/mq016_bartmoss/01_warehouse/00_explore_landfill`
- `quests/minor_quest/mq016_bartmoss/01_warehouse/01_open_coffin`
- `quests/minor_quest/mq016_bartmoss/01_warehouse/01_open_coffin/description`
- `quests/minor_quest/mq016_bartmoss/01_warehouse/02_talk_with_johnny`
- `quests/minor_quest/mq016_bartmoss/01_warehouse/03_scan_coffin`
- `quests/minor_quest/mq016_bartmoss/01_warehouse/04_take_cyberdeck`
- `quests/minor_quest/mq016_bartmoss/02_afterlife/01_talk_with_nix`
- `quests/minor_quest/mq016_bartmoss/02_afterlife/01_talk_with_nix/nix`
- `quests/minor_quest/mq016_bartmoss/02_afterlife/01_talk_with_nix1`
- `quests/minor_quest/mq016_bartmoss/02_afterlife/03_give_nix`
- `quests/minor_quest/mq016_bartmoss/02_afterlife/04_wait_for_nix`
- `quests/minor_quest/mq016_bartmoss/02_afterlife/05_find_way_to_help`
- `quests/minor_quest/mq016_bartmoss/02_afterlife/06_talk_with_nix`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 3 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 5 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetLifePath]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 4 |
| `questCheckpointNodeDefinition` | 6 |
| `questConditionNodeDefinition[questBuild_ConditionType,questStatsCondition,questUniversalRef]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 13 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questConditionNodeDefinition[questStat_ConditionType,questStatsCondition,questUniversalRef]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questDeletionMarkerNodeDefinition` | 7 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 2 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 1 |
| `questEventManagerNodeDefinition` | 6 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 11 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 27 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 3 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 2 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 1 |
| `questInputNodeDefinition` | 19 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 3 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 10 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 7 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 33 |
| `questLogicalHubNodeDefinition` | 2 |
| `questMappinManagerNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 15 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 4 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance,questVisionMode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questTriggerCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questObjectCondition,questScan_ConditionType,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questPhaseNodeDefinition` | 12 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 4 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questScene_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 3 |
| `questTimeManagerNodeDefinition[questPauseTime_NodeType]` | 1 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 4 |
| `questUIManagerNodeDefinition[questSetHUDEntryForcedVisibility_NodeType]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 8 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 10 |
| `questVisionModesManagerNodeDefinition[questEnableScanning_NodeType]` | 3 |
| `questVisionModesManagerNodeDefinition[questSetFocusClueState_NodeType]` | 5 |
| `questVisionModesManagerNodeDefinition[questToggleVisionMode_NodeType]` | 7 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 3 |
| `scnAndNode[scnNodeId]` | 2 |
| `scnChoiceNode[questBuild_ConditionType,questFactsDBCondition,questStatsCondition,questUniversalRef,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 5 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 7 |
| `scnHubNode[scnNodeId]` | 5 |
| `scnInterruptManagerNode[scnNodeId,scnToggleInterruption_InterruptionOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 42 |
| `scnStartNode[scnNodeId]` | 3 |
| `scnXorNode[scnNodeId]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `c1b6601d2f647c8a694d` | 5 | `base\quest\minor_quests\mq016\scenes\mq016_01_freezer.scene` / scene / 93 -> 88 -> 90 |
| `45008f44dc6eb4225434` | 4 | `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` / scene / 1090 -> 471 -> 413 |
| `b79fc2a07aec350ea9c7` | 4 | `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` / scene / 1090 -> 471 -> 413 |
| `016828d499c85128303c` | 3 | `base\quest\minor_quests\mq016\scenes\mq016_01_freezer.scene` / scene / 98 -> 104 -> 106 |
| `1fa539921730278ef7fb` | 3 | `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` / scene / 302 -> 304 -> 23 |
| `27faccd7b30abbc3add2` | 3 | `base\quest\minor_quests\mq016\scenes\mq016_01_freezer.scene` / scene / 284 -> 88 -> 93 |
| `7ff0eae411231e617b77` | 3 | `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` / scene / 368 -> 375 -> 383 |
| `82a8d18c045a74e97a4d` | 3 | `base\quest\minor_quests\mq016\test\mq016_00_chickentest.scene` / scene / 55 -> 20 -> 4 |
| `8ffc6ec591a46dedc685` | 3 | `base\quest\minor_quests\mq016\test\mq016_00_chickentest.scene` / scene / 20 -> 4 -> 9 |
| `9966b93a0ad6f5e7618d` | 3 | `base\quest\minor_quests\mq016\test\mq016_00_chickentest.scene` / scene / 20 -> 4 -> 12 |
| `bafa84009ee9ebd6bda6` | 3 | `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` / scene / 471 -> 413 -> 331 |
| `c95d278fffc97763b3fc` | 3 | `base\quest\minor_quests\mq016\test\mq016_00_chickentest.scene` / scene / 20 -> 4 -> 41 |
| `de490f1a1f721f57a0ec` | 3 | `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` / scene / 302 -> 306 -> 23 |
| `eccf96b8f72c4f645c0c` | 3 | `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` / scene / 471 -> 413 -> 331 |
| `0b5e2d5be50c61791656` | 2 | `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` / scene / 507 -> 413 -> 331 |
| `1b52ac99cfd3dee91d44` | 2 | `base\quest\minor_quests\mq016\scenes\mq016_02_afterlife.scene` / scene / 471 -> 507 -> 413 |
| `28040ca8e450266795cd` | 2 | `base\quest\minor_quests\mq016\phases\mq016_00_shard.questphase` / h44 / 0 -> 11 -> 12 |
| `30fd9bc5316c9cca9b4a` | 2 | `base\quest\minor_quests\mq016\test\mq016_00_chickentest.scene` / scene / 18 -> 49 -> 23 |
| `39fdcb1b28a47606d4bf` | 2 | `base\quest\minor_quests\mq016\scenes\mq016_01_freezer.scene` / scene / 108 -> 620 -> 312 |
| `40aa0dddb5f517500320` | 2 | `base\quest\bugfixing\minor_quests\mq016\mq016_quest_bugfixes.questphase` / h78 / 2 -> 36 -> 28 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
