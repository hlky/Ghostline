# base-mq042

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq042\mq042_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq042\mq042_quest_bugfixes.questphase` | repair | 6 / 0 |  |
| `base\quest\minor_quests\mq042\mq042_nomad.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq042\mq042_nomad.quest` | content candidate | 2 / 0 | base\quest\minor_quests\mq042\mq042_nomad.questphase; base\quest\minor_quests\mq042\temp\mq042_chicken_test.scene |
| `base\quest\minor_quests\mq042\mq042_nomad.questphase` | content candidate | 4 / 0 | base\quest\minor_quests\mq042\phases\mq042_nomad_01_hook.questphase; base\quest\minor_quests\mq042\phases\mq042_nomad_02_car.questphase |
| `base\quest\minor_quests\mq042\phases\mq042_nomad_01_hook.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq042\scenes\mq042_nomad_01_gps_signal.scene |
| `base\quest\minor_quests\mq042\phases\mq042_nomad_02_car.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene; base\quest\minor_quests\mq042\scenes\mq042_nomad_02_car_found.scene |
| `base\quest\minor_quests\mq042\scenes\mq042_nomad_01_gps_signal.scene` | content candidate | 0 / 3 |  |
| `base\quest\minor_quests\mq042\scenes\mq042_nomad_02_car_found.scene` | content candidate | 0 / 142 |  |
| `base\quest\minor_quests\mq042\temp\mq042_chicken_test.scene` | test/debug | 0 / 6 |  |

## Journal paths observed in these resources

- `contacts/galena_80845/mq042_gps_message/00_system_booted`
- `contacts/galena_80845/mq042_gps_message/01_geolocation_activated`
- `contacts/galena_80845/mq042_gps_message/02_gps_location_sent`
- `quests/minor_quest/mq042_nomad`
- `quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone`
- `quests/minor_quest/mq042_nomad/mq042_nomad/00_check_your_phone/description`
- `quests/minor_quest/mq042_nomad/mq042_nomad/01_go_to_the_location`
- `quests/minor_quest/mq042_nomad/mq042_nomad/02_scan_your_old_car`
- `quests/minor_quest/mq042_nomad/mq042_nomad/02a_open_the_hood`
- `quests/minor_quest/mq042_nomad/mq042_nomad/02b_inspect_the_engine`
- `quests/minor_quest/mq042_nomad/mq042_nomad/03_talk_with_the_stranger`
- `quests/minor_quest/mq042_nomad/mq042_nomad/04_get_inside_the_car`
- `quests/minor_quest/mq042_nomad/mq042_nomad/05_talk_with_johnny`
- `quests/minor_quest/mq042_nomad/mq042_nomad/06_get_back`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 7 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 1 |
| `questCheckpointNodeDefinition` | 3 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 14 |
| `questConditionNodeDefinition[questLifePath_ConditionType,questStatsCondition,questUniversalRef]` | 1 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 3 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 7 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 3 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 12 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 3 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 2 |
| `questInputNodeDefinition` | 16 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 25 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 11 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 3 |
| `questOutputNodeDefinition` | 13 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questTriggerCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 7 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 8 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 4 |
| `questPhaseNodeDefinition` | 10 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questPlayerLookAt_NodeType]` | 1 |
| `questSceneNodeDefinition[scnInterruptionScenarioId,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 3 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questShowOnscreen_NodeType]` | 4 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 7 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 1 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 18 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 1 |
| `questVehicleNodeDefinition[questEnablePlayerVehicle_NodeType]` | 1 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 6 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 5 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 8 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 6 |
| `questVisionModesManagerNodeDefinition[questSetFocusClueState_NodeType]` | 1 |
| `questVisionModesManagerNodeDefinition[questSetScanningState_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 3 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questPaymentBalanced_ConditionType,questPaymentCondition,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 4 |
| `scnHubNode[scnNodeId]` | 8 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 33 |
| `scnStartNode[scnNodeId]` | 7 |
| `scnXorNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `f4c2b3190230913ea05b` | 9 | `base\quest\bugfixing\minor_quests\mq042\mq042_quest_bugfixes.questphase` / h30 / 2 -> 3 -> 4 |
| `0873b5c19806fb9d629a` | 4 | `base\quest\minor_quests\mq042\scenes\mq042_nomad_02_car_found.scene` / scene / 37 -> 115 -> 119 |
| `450070a422af0dc83c00` | 4 | `base\quest\bugfixing\minor_quests\mq042\mq042_quest_bugfixes.questphase` / h30 / 11 -> 12 -> 15 |
| `748959ebbbf9aeab3a8a` | 4 | `base\quest\minor_quests\mq042\scenes\mq042_nomad_02_car_found.scene` / scene / 37 -> 115 -> 117 |
| `d4d2d2448f70adcb9194` | 4 | `base\quest\bugfixing\minor_quests\mq042\mq042_quest_bugfixes.questphase` / h30 / 13 -> 10 -> 11 |
| `f7e3b0e3e23e9bc5908b` | 4 | `base\quest\bugfixing\minor_quests\mq042\mq042_quest_bugfixes.questphase` / h30 / 10 -> 11 -> 12 |
| `fd8aa2e9b9eedb25b31a` | 4 | `base\quest\bugfixing\minor_quests\mq042\mq042_quest_bugfixes.questphase` / h30 / 14 -> 13 -> 10 |
| `1cf9adcdd8714d9f07e3` | 3 | `base\quest\minor_quests\mq042\scenes\mq042_nomad_02_car_found.scene` / scene / 930 -> 924 -> 925 |
| `1f19ca77b00b3e5851f2` | 3 | `base\quest\minor_quests\mq042\scenes\mq042_nomad_02_car_found.scene` / scene / 930 -> 924 -> 928 |
| `38ec111d65a3e6123d1f` | 3 | `base\quest\minor_quests\mq042\scenes\mq042_nomad_02_car_found.scene` / scene / 930 -> 924 -> 1029 |
| `3bfe06739d5bfa31d0df` | 3 | `base\quest\minor_quests\mq042\scenes\mq042_nomad_02_car_found.scene` / scene / 924 -> 1029 -> 1033 |
| `8127228bae2684dab42c` | 3 | `base\quest\minor_quests\mq042\scenes\mq042_nomad_02_car_found.scene` / scene / 37 -> 115 -> 210 |
| `bd44fd6ebe28bd80c073` | 3 | `base\quest\minor_quests\mq042\scenes\mq042_nomad_02_car_found.scene` / scene / 119 -> 475 -> 961 |
| `e2ec57ffd16dba279375` | 3 | `base\quest\bugfixing\minor_quests\mq042\mq042_quest_bugfixes.questphase` / h197 / 15 -> 20 -> 19 |
| `eaf5aab427d50e5598b6` | 3 | `base\quest\bugfixing\minor_quests\mq042\mq042_quest_bugfixes.questphase` / h30 / 0 -> 2 -> 3 |
| `f893697e9c7d424433d8` | 3 | `base\quest\bugfixing\minor_quests\mq042\mq042_quest_bugfixes.questphase` / h323 / 40 -> 37 -> 15 |
| `09ab8874517e792939a0` | 2 | `base\quest\minor_quests\mq042\scenes\mq042_nomad_02_car_found.scene` / scene / 294 -> 17 -> 336 |
| `573a364243a7329e5d69` | 2 | `base\quest\minor_quests\mq042\scenes\mq042_nomad_02_car_found.scene` / scene / 225 -> 532 -> 1055 |
| `6ba544f0539396c4f097` | 2 | `base\quest\minor_quests\mq042\scenes\mq042_nomad_02_car_found.scene` / scene / 172 -> 107 -> 658 |
| `c47f7b0cdf77a4b40760` | 2 | `base\quest\bugfixing\minor_quests\mq042\mq042_quest_bugfixes.questphase` / h30 / 12 -> 15 -> 1 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
