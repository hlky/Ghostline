# base-sts-wat-nid-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\community\sts_wat_nid_01_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\community\sts_wat_nid_01_com_psycho.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\community\sts_wat_nid_01_dead_bodies.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\phases\sts_wat_nid_01_bugfixing.questphase` | repair | 5 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\phases\sts_wat_nid_01_combat.questphase` | content candidate | 3 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_scene.scene |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\phases\sts_wat_nid_01_openworld.questphase` | content candidate | 8 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_hal.scene; base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_holocall_debrief.scene; base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_holocall_prebrief.scene; base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_lizzie.scene |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\phases\sts_wat_nid_01_phase.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\phases\sts_wat_nid_01_combat.questphase; base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\phases\sts_wat_nid_01_openworld.questphase |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_hal.scene` | content candidate | 0 / 97 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_holocall_debrief.scene` | content candidate | 0 / 29 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_lizzie.scene` | content candidate | 0 / 31 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_scene.scene` | content candidate | 0 / 14 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\sts_wat_nid_01_def.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\sts_wat_nid_01_def_testworld.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\sts_wat_nid_01_quest.quest` | content candidate | 1 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\phases\sts_wat_nid_01_phase.questphase |

## Journal paths observed in these resources

- `contacts/regina_jones/sts_wat_nid_01/sts_wat_nid_01_brief`
- `contacts/regina_jones/sts_wat_nid_01/sts_wat_nid_01_holocall_debrief_notperfect`
- `contacts/regina_jones/sts_wat_nid_01/sts_wat_nid_01_holocall_debrief_perfect`
- `contacts/regina_jones/sts_wat_nid_01/sts_wat_nid_01_player_left_location`
- `points_of_interest/street_stories/sts_wat_nid_01`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01/brief`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01/sts_wat_nid_01/enter`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01/sts_wat_nid_01/find`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01/sts_wat_nid_01/hack`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01/sts_wat_nid_01/kill`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01/sts_wat_nid_01/main/hal`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_01/sts_wat_nid_01/talk`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 3 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 2 |
| `questCheckpointNodeDefinition` | 3 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 15 |
| `questConditionNodeDefinition[questGatherTriggerCondition]` | 1 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 4 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 13 |
| `questEndNodeDefinition` | 1 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 2 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 44 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 11 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 19 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 9 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 4 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 20 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 2 |
| `questMappinManagerNodeDefinition` | 1 |
| `questMiscAICommandNode` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 2 |
| `questOutputNodeDefinition` | 15 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 15 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questRealtimeDelay_ConditionType,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 13 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckSpeakerDistractedInterruptCondition]` | 2 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType]` | 9 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 7 |
| `questPhaseNodeDefinition` | 16 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneNodeDefinition[scnCheckPlayerTargetNodeDistanceInterruptCondition,scnCheckPlayerTargetNodeDistanceInterruptConditionParams,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnInterruptionScenarioId,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 8 |
| `questStartNodeDefinition` | 1 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 9 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 28 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |
| `scnChoiceNode[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnscreenplayItemId]` | 3 |
| `scnCutControlNode[scnNodeId]` | 3 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 8 |
| `scnHubNode[scnNodeId]` | 5 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnNodeId,scnToggleInterruption_InterruptionOperation]` | 1 |
| `scnRandomizerNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 38 |
| `scnStartNode[scnNodeId]` | 6 |
| `scnXorNode[scnNodeId]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `101b60945ddf6f25f378` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_holocall_debrief.scene` / scene / 26 -> 108 -> 110 |
| `3fe0ae98a8cf5496b004` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\phases\sts_wat_nid_01_bugfixing.questphase` / h104 / 8 -> 10 -> 11 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_holocall_debrief.scene` / scene / 279 -> 270 -> 258 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_holocall_debrief.scene` / scene / 105 -> 106 -> 102 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_holocall_debrief.scene` / scene / 110 -> 105 -> 106 |
| `eb252b7e42db30cea85d` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\phases\sts_wat_nid_01_bugfixing.questphase` / h104 / 10 -> 11 -> 9 |
| `0b487c56874911c2ea72` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_scene.scene` / scene / 94 -> 102 -> 3 |
| `14d4f3ada3a2779a6a57` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_hal.scene` / scene / 70 -> 67 -> 415 |
| `258d898cfebab46dfad3` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_hal.scene` / scene / 85 -> 308 -> 316 |
| `4365cb473b16f3e76999` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\phases\sts_wat_nid_01_openworld.questphase` / h642 / 97 -> 47 -> 57 |
| `4e8cfb68507d828083fe` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_lizzie.scene` / scene / 91 -> 110 -> 253 |
| `6cbbca2dbd7486843b33` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_lizzie.scene` / scene / 91 -> 220 -> 223 |
| `918e099696021c85e9c3` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_hal.scene` / scene / 85 -> 308 -> 304 |
| `af13657afd58445a204e` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_hal.scene` / scene / 70 -> 67 -> 73 |
| `b769ade732d21ee6cf4f` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\phases\sts_wat_nid_01_openworld.questphase` / h642 / 97 -> 47 -> 56 |
| `bad946bbee29e66fef71` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_hal.scene` / scene / 546 -> 70 -> 67 |
| `c9386e7e9220cdf771ec` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\phases\sts_wat_nid_01_openworld.questphase` / h642 / 73 -> 64 -> 38 |
| `de1ddfc371f3852883b3` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_lizzie.scene` / scene / 249 -> 106 -> 185 |
| `edd398d6b28dc17bbc98` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_lizzie.scene` / scene / 91 -> 110 -> 249 |
| `fdb8e6839d0e2f558d59` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\scenes\sts_wat_nid_01_lizzie.scene` / scene / 91 -> 110 -> 250 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
