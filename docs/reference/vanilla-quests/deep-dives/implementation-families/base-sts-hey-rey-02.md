# base-sts-hey-rey-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\community\sts_hey_rey_02.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\community\sts_hey_rey_02_crowd.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\community\sts_hey_rey_02_enemies.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\community\sts_hey_rey_02_reinforcement.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_bugfixing.questphase` | repair | 5 / 0 |  |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` | content candidate | 14 / 0 | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_gangers.scene |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` | content candidate | 7 / 0 | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_civilians.scene; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_prebrief.scene |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_civilians.scene` | content candidate | 0 / 18 |  |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_gangers.scene` | content candidate | 0 / 29 |  |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` | content candidate | 0 / 23 |  |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_johnny.scene` | content candidate | 0 / 7 |  |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest` | content candidate | 2 / 0 | base\open_world\phases\open_world_content.questphase; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.questphase` | content candidate | 3 / 0 | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02_test.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/sebastian_padre_perez/sts_hey_rey_02/brief`
- `contacts/sebastian_padre_perez/sts_hey_rey_02/sts_hey_rey_02_holocall_debriefs`
- `points_of_interest/street_stories/sts_hey_rey_02`
- `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02`
- `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/brief`
- `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/escape`
- `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/find_office_room`
- `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/get_to_the_strip_club`
- `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02/sts_hey_rey_02/take_datapad`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 14 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 12 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 1 |
| `questEventManagerNodeDefinition` | 9 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 32 |
| `questFlowControlNodeDefinition` | 1 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 30 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 32 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 11 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMiscAICommandNode` | 8 |
| `questOutputNodeDefinition` | 19 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questDevice_ConditionType,questJournalCondition,questJournalEntry_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 8 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 14 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 6 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckSpeakerDistractedInterruptCondition]` | 6 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 17 |
| `questPhaseNodeDefinition` | 28 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 2 |
| `questRandomizerNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 7 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 6 |
| `questSpawnManagerNodeDefinition[questLegacy_NodeType,questSpawnManagerNodeActionEntry]` | 6 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 2 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 3 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVisionModesManagerNodeDefinition[questForceModule_NodeType,questForceVMModule_NodeTypeParams]` | 1 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 4 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |
| `scnChoiceNode[questBuild_ConditionType,questPaymentCondition,questPaymentFixedAmount_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 12 |
| `scnHubNode[scnNodeId]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 12 |
| `scnStartNode[scnNodeId]` | 10 |
| `scnXorNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `9380dda43f90ecd62efb` | 16 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` / h12 / 40 -> 41 -> 42 |
| `3b70bb506b872cadfa43` | 4 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_civilians.scene` / scene / 13 -> 93 -> 41 |
| `5c76d3bf7160f29b884f` | 4 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_bugfixing.questphase` / h12 / 5 -> 6 -> 3 |
| `8cd3b647ae3f592ad947` | 4 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_civilians.scene` / scene / 13 -> 23 -> 41 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` / scene / 249 -> 254 -> 251 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` / scene / 293 -> 295 -> 297 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` / scene / 62 -> 293 -> 295 |
| `eaf5aab427d50e5598b6` | 4 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_bugfixing.questphase` / h12 / 0 -> 5 -> 6 |
| `2f42e8df5c81cf29a5fc` | 3 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` / h587 / 0 -> 88 -> 92 |
| `647ea9ce31c01a3e6527` | 3 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` / h28 / 0 -> 25 -> 24 |
| `8dd5c44ffdb3cb8886ef` | 3 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_bugfixing.questphase` / h59 / 3 -> 4 -> 5 |
| `101b60945ddf6f25f378` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` / scene / 33 -> 61 -> 63 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` / scene / 254 -> 57 -> 60 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` / scene / 249 -> 254 -> 57 |
| `12cfab2c016adbb2a2c5` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_gangers.scene` / scene / 12 -> 114 -> 116 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_prebrief.scene` / scene / 270 -> 273 -> 279 |
| `138cff49923a75e07348` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` / h587 / 42 -> 46 -> 49 |
| `1b8a537228bd96355716` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase` / h281 / 72 -> 71 -> 46 |
| `1d933adb5a617880c93e` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene` / scene / 61 -> 63 -> 58 |
| `22eac18957944f0fe71a` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_gameplay.questphase` / h341 / 8 -> 27 -> 28 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
