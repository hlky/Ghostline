# base-sts-hey-gle-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\community\sts_hey_gle_05.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\community\sts_hey_gle_05_com_after.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\community\sts_hey_gle_05_combat_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\community\sts_hey_gle_05_crowd_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase; base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_bugfixing.questphase` | repair | 4 / 0 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` | content candidate | 12 / 0 | base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_conversation.scene; base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_scene.scene |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` | content candidate | 7 / 0 | base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene; base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_prebrief.scene; base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_opening_scene.scene |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_conversation.scene` | content candidate | 0 / 71 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_scene.scene` | content candidate | 0 / 8 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` | content candidate | 0 / 23 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_opening_scene.scene` | content candidate | 0 / 3 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\sts_hey_gle_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\sts_hey_gle_05.quest` | content candidate | 1 / 0 | base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05.questphase |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\sts_hey_gle_05_test_def.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/sebastian_padre_perez/sts_hey_gle_05/sts_hey_gle_05_brief`
- `contacts/sebastian_padre_perez/sts_hey_gle_05/sts_hey_gle_05_holocall_debriefs`
- `points_of_interest/street_stories/sts_hey_gle_05`
- `quests/street_stories/heywood/glen/sts_hey_gle_05`
- `quests/street_stories/heywood/glen/sts_hey_gle_05/brief`
- `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/deliver`
- `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/find`
- `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/kill`
- `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/leave`
- `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/look_for_cores`
- `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/take_parts`
- `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk`
- `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/talk_el_gallo`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 8 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 4 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 3 |
| `questCombatNodeDefinition[questCombatNodeParams_LookAtTarget]` | 2 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 3 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 4 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 9 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 2 |
| `questEventManagerNodeDefinition` | 14 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 37 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 5 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 24 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 4 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 3 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 28 |
| `questLogicalHubNodeDefinition` | 4 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMiscAICommandNode` | 2 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 18 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterAim_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 14 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 18 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 15 |
| `questPhaseNodeDefinition` | 23 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 8 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 7 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 8 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 9 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 13 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 5 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questInventory_ConditionType,questObjectCondition,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 3 |
| `scnDeletionMarkerNode[scnNodeId]` | 3 |
| `scnEndNode[scnNodeId]` | 10 |
| `scnHubNode[scnNodeId]` | 5 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 21 |
| `scnStartNode[scnNodeId]` | 8 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` / scene / 249 -> 252 -> 255 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` / scene / 284 -> 282 -> 286 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` / scene / 67 -> 284 -> 282 |
| `8cd3b647ae3f592ad947` | 3 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_conversation.scene` / scene / 106 -> 69 -> 103 |
| `a103d4ae3150ecfeb747` | 3 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_bugfixing.questphase` / h17 / 2 -> 3 -> 14 |
| `eaf5aab427d50e5598b6` | 3 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_bugfixing.questphase` / h17 / 0 -> 2 -> 3 |
| `101b60945ddf6f25f378` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` / scene / 25 -> 66 -> 68 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` / scene / 252 -> 62 -> 65 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` / scene / 249 -> 252 -> 62 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_prebrief.scene` / scene / 272 -> 275 -> 281 |
| `1666d7526b9bab74f2e2` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` / h292 / 5 -> 168 -> 112 |
| `1a9b8893087e174a603f` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` / h292 / 85 -> 183 -> 87 |
| `1d933adb5a617880c93e` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` / scene / 66 -> 68 -> 63 |
| `26762f051e7728f090ca` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` / scene / 62 -> 65 -> 25 |
| `276aca4a2dc348a877d5` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_conversation.scene` / scene / 53 -> 65 -> 435 |
| `2beeeaa3b4da5300c035` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` / scene / 1 -> 280 -> 67 |
| `2e362801d31d08a7d108` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene` / scene / 67 -> 61 -> 249 |
| `30d7a03f6406e0206e05` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_bugfixing.questphase` / h17 / 4 -> 5 -> 1 |
| `3fe0ae98a8cf5496b004` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` / h292 / 143 -> 140 -> 142 |
| `400ab17c1f3363cf36e2` | 2 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` / h698 / 2 -> 3 -> 4 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
