# base-mq006

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq006\mq006_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq006\mq006_quest_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\minor_quests\mq006\mq006.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq006\mq006.quest` | content candidate | 3 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq006\mq006.questphase; base\quest\minor_quests\mq006\test\mq006_chicken_test.scene |
| `base\quest\minor_quests\mq006\mq006.questphase` | content candidate | 8 / 0 | base\quest\minor_quests\mq006\phases\mq006_rollercoaster_ride_controller.questphase; base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene; base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene |
| `base\quest\minor_quests\mq006\phases\mq006_repeatable_rollercoaster_controller.questphase` | content candidate | 3 / 0 | base\quest\minor_quests\mq006\phases\mq006_rollercoaster_ride_controller.questphase; base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene; base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene |
| `base\quest\minor_quests\mq006\phases\mq006_rollercoaster_ride_controller.questphase` | content candidate | 2 / 0 |  |
| `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` | content candidate | 0 / 159 |  |
| `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene` | content candidate | 0 / 235 |  |
| `base\quest\minor_quests\mq006\test\mq006_chicken_test.scene` | test/debug | 0 / 8 |  |
| `base\quest\minor_quests\mq006\test\mq006_ride_test.gamedef` | test/debug | 0 / 0 |  |
| `base\quest\minor_quests\mq006\test\mq006_ride_test.quest` | test/debug | 2 / 0 |  |

## Journal paths observed in these resources

- `points_of_interest/minor_quests/mq006_rollercoaster`
- `quests/main_quest/act_01/q110_01_voodooboys`
- `quests/minor_quest/mq006_rollercoaster`
- `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster`
- `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/01_locate_the_control_terminal`
- `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/01_locate_the_control_terminal/description`
- `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/01_locate_the_control_terminal/mq006_mp_control_box`
- `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/02_restart_the_rollercoaster`
- `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/03_return_to_jean`
- `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/04_talk_to_jean`
- `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/05_get_into_the_rollercoaster`
- `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/06_enjoy_the_ride`
- `quests/minor_quest/mq006_rollercoaster/mq006_rollercoaster/07_get_out_of_the_rollercoaster`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 4 |
| `questAudioNodeDefinition[questAudioSwitchNodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetLifePath]` | 3 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 16 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 11 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 4 |
| `questEndNodeDefinition` | 2 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 3 |
| `questEventManagerNodeDefinition` | 10 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 36 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 1 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 5 |
| `questInputNodeDefinition` | 20 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 6 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 21 |
| `questLogicalHubNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMappinManagerNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 3 |
| `questOutputNodeDefinition` | 14 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questTriggerCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 14 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 16 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 15 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 31 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 16 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneManagerNodeDefinition[questPlayerLookAt_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 7 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questScene_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 8 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 3 |
| `questStartNodeDefinition` | 2 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 4 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 28 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 6 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 36 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 10 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 6 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 3 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |
| `scnAndNode[scnNodeId]` | 2 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[questLifePath_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 6 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnEndNode[scnNodeId]` | 9 |
| `scnHubNode[scnNodeId]` | 24 |
| `scnRandomizerNode[scnNodeId]` | 5 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 102 |
| `scnStartNode[scnNodeId]` | 18 |
| `scnXorNode[scnNodeId]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0d9e1901453d0aabed97` | 8 | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 442 -> 441 -> 437 |
| `dbeb8824cf54dd13f915` | 6 | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 537 -> 536 -> 534 |
| `19665e3783f6f51a7337` | 5 | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 1 -> 295 -> 301 |
| `7f1e8c62437f340385bf` | 5 | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 1 -> 295 -> 302 |
| `aa0341780e2cb63c048b` | 5 | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 134 -> 136 -> 64 |
| `01c768f6c581e4e9c39d` | 4 | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 101 -> 107 -> 105 |
| `03f3f6f33007cd7740ec` | 4 | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 536 -> 534 -> 542 |
| `0b487c56874911c2ea72` | 4 | `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene` / scene / 415 -> 26 -> 23 |
| `12a72da538d6399f7a5c` | 4 | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 536 -> 537 -> 534 |
| `12cded56991925fc16a7` | 4 | `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene` / scene / 558 -> 1024 -> 1028 |
| `4cffbddf3fb01ca03a0e` | 4 | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 442 -> 441 -> 448 |
| `651e7167bbc4e5206b02` | 4 | `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene` / scene / 558 -> 1024 -> 1022 |
| `6712bb6f081959f599df` | 4 | `base\quest\minor_quests\mq006\test\mq006_ride_test.quest` / h10 / 9 -> 10 -> 11 |
| `8056fbc52431656918e5` | 4 | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 537 -> 534 -> 542 |
| `8bc0e369c0035627a8f0` | 4 | `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene` / scene / 558 -> 1024 -> 1026 |
| `b50e122305bb35a7a0c0` | 4 | `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene` / scene / 1009 -> 165 -> 167 |
| `be6f2309066016a2fedc` | 4 | `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene` / scene / 181 -> 179 -> 185 |
| `1cf9adcdd8714d9f07e3` | 3 | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 221 -> 313 -> 316 |
| `1d4ec6ef90134c9e080e` | 3 | `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene` / scene / 57 -> 60 -> 409 |
| `1e86a2dce4ca34e7c024` | 3 | `base\quest\minor_quests\mq006\phases\mq006_rollercoaster_ride_controller.questphase` / h7 / 2 -> 3 -> 4 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
