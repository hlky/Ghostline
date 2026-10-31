# base-sts-wat-nid-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\community\sts_wat_nid_04.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\community\sts_wat_nid_04_gaf.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\community\sts_wat_nid_04_reinfo.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04_gameplay.questphase; base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04_openworld.questphase |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04_gameplay.questphase` | content candidate | 6 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_gangers.scene |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04_openworld.questphase` | content candidate | 7 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_gottfrid_fredrik.scene; base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_holocall_debriefs.scene; base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_holocall_prebrief.scene |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04_prestate_control.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_gangers.scene` | content candidate | 0 / 10 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_gottfrid_fredrik.scene` | content candidate | 0 / 140 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_holocall_debriefs.scene` | content candidate | 0 / 27 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\sts_wat_nid_04.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\sts_wat_nid_04.quest` | content candidate | 1 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\sts_wat_nid_04_nc.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\sts_wat_nid_04_test.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/regina_global_msg/watson_reward`
- `contacts/regina_jones/sts_wat_nid_04/brief`
- `contacts/regina_jones/sts_wat_nid_04/sts_wat_nid_04_debrief_fail`
- `contacts/regina_jones/sts_wat_nid_04/sts_wat_nid_04_debrief_success`
- `contacts/regina_jones/sts_wat_nid_04/warning_when_leaving`
- `points_of_interest/street_stories/sts_wat_nid_04`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04/brief`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04/sts_wat_nid_04/find_recording`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04/sts_wat_nid_04/get_recording`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04/sts_wat_nid_04/get_to_droppoint`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04/sts_wat_nid_04/get_to_hideout`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04/sts_wat_nid_04/leave_area`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 4 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 3 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 22 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 19 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 37 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 15 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 3 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 17 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 5 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 9 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUICondition,questUIElement_ConditionType,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 13 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 9 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questObjectCondition,questScan_ConditionType,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questUICondition,questUIElement_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 15 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 11 |
| `questPhaseNodeDefinition` | 15 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 3 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 8 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 18 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 8 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 6 |
| `scnAndNode[scnNodeId]` | 3 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 11 |
| `scnDeletionMarkerNode[scnNodeId]` | 3 |
| `scnEndNode[scnNodeId]` | 9 |
| `scnHubNode[scnNodeId]` | 13 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnNodeId,scnToggleInterruption_InterruptionOperation]` | 1 |
| `scnRandomizerNode[scnNodeId]` | 3 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 38 |
| `scnStartNode[scnNodeId]` | 8 |
| `scnXorNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `e72f36ce1236ddc2fc95` | 6 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_gottfrid_fredrik.scene` / scene / 540 -> 543 -> 287 |
| `10ac8cb355f355254ee3` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04_gameplay.questphase` / h227 / 33 -> 40 -> 48 |
| `4b55ae1d10cd75d12e28` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04_gameplay.questphase` / h227 / 37 -> 40 -> 48 |
| `88658eb3ebe1aed6f0ae` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04_gameplay.questphase` / h227 / 35 -> 40 -> 48 |
| `92873b07f7940b86e904` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04_gameplay.questphase` / h227 / 39 -> 40 -> 48 |
| `b80b538bd81c7e6de23c` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04_openworld.questphase` / h650 / 30 -> 29 -> 3 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_holocall_debriefs.scene` / scene / 257 -> 280 -> 260 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_holocall_debriefs.scene` / scene / 294 -> 292 -> 296 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_holocall_debriefs.scene` / scene / 74 -> 294 -> 292 |
| `f802ad66d4ceea2d0aff` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04_gameplay.questphase` / h505 / 0 -> 6 -> 2 |
| `ffd10d268bed77640e68` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04_gameplay.questphase` / h227 / 27 -> 40 -> 48 |
| `01c768f6c581e4e9c39d` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_gottfrid_fredrik.scene` / scene / 38 -> 359 -> 361 |
| `031fc17087e99ad26ab7` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04_gameplay.questphase` / h227 / 70 -> 68 -> 45 |
| `101b60945ddf6f25f378` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_holocall_debriefs.scene` / scene / 28 -> 73 -> 75 |
| `16ab2f22adf511749390` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_gottfrid_fredrik.scene` / scene / 236 -> 482 -> 349 |
| `2daa74ecf234ce336666` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04_gameplay.questphase` / h227 / 21 -> 68 -> 45 |
| `69a2aad2f79abb156101` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_holocall_debriefs.scene` / scene / 68 -> 257 -> 280 |
| `6db8c1a6b27de78dd353` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_gottfrid_fredrik.scene` / scene / 236 -> 33 -> 606 |
| `95b7458b3ffd83fd4357` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04_gameplay.questphase` / h227 / 32 -> 33 -> 51 |
| `9e8a15dd8388aa68b155` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\scenes\sts_wat_nid_04_gottfrid_fredrik.scene` / scene / 236 -> 33 -> 608 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
