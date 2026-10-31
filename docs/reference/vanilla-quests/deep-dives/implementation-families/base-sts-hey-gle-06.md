# base-sts-hey-gle-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\community\sts_hey_gle_06_community.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\community\sts_hey_gle_06_jake.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\community\sts_hey_gle_06_reinforcements.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\community\sts_hey_gle_06_reinforcements_001.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_gameplay.questphase; base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_openworld.questphase |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_bugfixing.questphase` | repair | 12 / 0 | base\quest\minor_quests\mq044\phases\mq044_main.questphase |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_gameplay.questphase` | content candidate | 10 / 0 | base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\scenes\sts_hey_gle_06_scene.scene |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_openworld.questphase` | content candidate | 5 / 0 | base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\scenes\sts_hey_gle_06_holocall_debriefs.scene; base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\scenes\sts_hey_gle_06_holocall_prebrief.scene; base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\scenes\sts_hey_gle_06_scene.scene |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_phase.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_gameplay.questphase; base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_openworld.questphase |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_quest.quest` | content candidate | 1 / 0 | base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_phase.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\scenes\sts_hey_gle_06_holocall_debriefs.scene` | content candidate | 0 / 27 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\scenes\sts_hey_gle_06_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\scenes\sts_hey_gle_06_scene.scene` | content candidate | 0 / 21 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\sts_hey_gle_06.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\sts_hey_gle_06_test.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/jake_estevez/sts_hey_gle_06/warning`
- `contacts/sebastian_padre_perez/sts_hey_gle_06/sts_hey_gle_06_brief`
- `contacts/sebastian_padre_perez/sts_hey_gle_06/sts_hey_gle_06_holocall_debrief_fail`
- `contacts/sebastian_padre_perez/sts_hey_gle_06/sts_hey_gle_06_holocall_debrief_success`
- `points_of_interest/street_stories/sts_hey_gle_06`
- `quests/street_stories/heywood/glen/sts_hey_gle_06`
- `quests/street_stories/heywood/glen/sts_hey_gle_06/brief`
- `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/delicer_car`
- `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/delicer_car/car`
- `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/entergarage`
- `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/exit_garage`
- `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/leave`
- `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/reach_car`
- `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/talk`
- `quests/street_stories/heywood/glen/sts_hey_gle_06/retrieving/uploaddata`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 5 |
| `questCheckpointNodeDefinition` | 4 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 2 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 11 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 8 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 8 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 29 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 10 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 43 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 6 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 30 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 19 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 22 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 21 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMappinManagerNodeDefinition` | 6 |
| `questMiscAICommandNode` | 7 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 23 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questTriggerCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 14 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 17 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 15 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleWater_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 23 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 8 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questSpawnManagerNodeDefinition[questLegacy_NodeType,questSpawnManagerNodeActionEntry]` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 12 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 5 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 2 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 5 |
| `questVehicleNodeDefinition[questResetMovement_NodeType]` | 1 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 7 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 3 |
| `questWorldDataManagerNodeDefinition[questManageCollision_NodeType,questManageCollision_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 8 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 9 |
| `scnStartNode[scnNodeId]` | 5 |
| `scnXorNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `ef1f1c4d9ff5cba71b71` | 7 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_bugfixing.questphase` / h0 / 8 -> 11 -> 9 |
| `7c39581d5ffdc0bc4b36` | 4 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_bugfixing.questphase` / h221 / 4 -> 11 -> 1 |
| `808c42396a9735fe3a65` | 4 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_gameplay.questphase` / h469 / 0 -> 33 -> 34 |
| `bb9b68c143e722e3066e` | 4 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_gameplay.questphase` / h187 / 27 -> 26 -> 23 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\scenes\sts_hey_gle_06_holocall_debriefs.scene` / scene / 282 -> 270 -> 258 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\scenes\sts_hey_gle_06_holocall_debriefs.scene` / scene / 293 -> 291 -> 295 |
| `e3846df5cbd6db5c1cd5` | 4 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_bugfixing.questphase` / h535 / 6 -> 7 -> 3 |
| `138cff49923a75e07348` | 3 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_openworld.questphase` / h2 / 9 -> 17 -> 23 |
| `2e362801d31d08a7d108` | 3 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\scenes\sts_hey_gle_06_holocall_debriefs.scene` / scene / 289 -> 88 -> 282 |
| `651a4daef9d91e74cdd9` | 3 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_gameplay.questphase` / h187 / 0 -> 27 -> 26 |
| `6932c21a9c40d1c004a9` | 3 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_gameplay.questphase` / h205 / 0 -> 37 -> 47 |
| `807343801fcd55b219fa` | 3 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_bugfixing.questphase` / h299 / 5 -> 6 -> 1 |
| `996cac8350f4b301e1a9` | 3 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_bugfixing.questphase` / h698 / 12 -> 14 -> 13 |
| `e5742f9794e6583c67cb` | 3 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\scenes\sts_hey_gle_06_holocall_debriefs.scene` / scene / 95 -> 90 -> 91 |
| `002a05b4e460b7130fd2` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_openworld.questphase` / h882 / 52 -> 58 -> 3 |
| `014c2fc5787e90175419` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_bugfixing.questphase` / h535 / 4 -> 6 -> 7 |
| `0172df7336de39189a60` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_openworld.questphase` / h2 / 27 -> 151 -> 152 |
| `0306ed851cf557ba7848` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_bugfixing.questphase` / h299 / 0 -> 3 -> 4 |
| `0781ef00ea04c05ee418` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_openworld.questphase` / h2 / 26 -> 27 -> 193 |
| `08dc573621d3fde2c136` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_openworld.questphase` / h882 / 57 -> 54 -> 52 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
