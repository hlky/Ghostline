# base-sts-hey-gle-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\communities\sts_hey_gle_03_comm.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\communities\sts_hey_gle_03_cs_crime_scene_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_bugfixing.questphase` | repair | 7 / 0 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_gameplay.questphase` | content candidate | 10 / 0 | base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_scene.scene |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_ow.questphase` | content candidate | 6 / 0 | base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_holocall_debriefs.scene; base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_holocall_prebrief.scene; base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_scene.scene |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_phase.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_gameplay.questphase; base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_ow.questphase |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_prestate_control.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_holocall_debriefs.scene` | content candidate | 0 / 23 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_scene.scene` | content candidate | 0 / 133 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\sts_hey_gle_03_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\sts_hey_gle_03_quest.quest` | content candidate | 2 / 0 | base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_bugfixing.questphase; base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_phase.questphase; base\quest\holocalls\holocall_initializers.questphase |

## Journal paths observed in these resources

- `contacts/sebastian_padre_perez/sts_hey_gle_03/sts_hey_gle_03_brief`
- `contacts/sebastian_padre_perez/sts_hey_gle_03/sts_hey_gle_03_holocall_debriefs`
- `contacts/sebastian_padre_perez/sts_hey_gle_03/sts_hey_gle_03_sec_warning`
- `points_of_interest/street_stories/sts_hey_gle_03`
- `quests/street_stories/heywood/glen/sts_hey_gle_03`
- `quests/street_stories/heywood/glen/sts_hey_gle_03/brief`
- `quests/street_stories/heywood/glen/sts_hey_gle_03/sts_hey_gle_03/check_code`
- `quests/street_stories/heywood/glen/sts_hey_gle_03/sts_hey_gle_03/drop`
- `quests/street_stories/heywood/glen/sts_hey_gle_03/sts_hey_gle_03/drop/drop_point1`
- `quests/street_stories/heywood/glen/sts_hey_gle_03/sts_hey_gle_03/find_way`
- `quests/street_stories/heywood/glen/sts_hey_gle_03/sts_hey_gle_03/get_in`
- `quests/street_stories/heywood/glen/sts_hey_gle_03/sts_hey_gle_03/pick_up`
- `quests/street_stories/heywood/glen/sts_hey_gle_03/sts_hey_gle_03/puzzle`
- `quests/street_stories/heywood/glen/sts_hey_gle_03/sts_hey_gle_03/room_get_in`
- `quests/street_stories/heywood/glen/sts_hey_gle_03/sts_hey_gle_03/safe`
- `quests/street_stories/heywood/glen/sts_hey_gle_03/sts_hey_gle_03/safe/safe_mp`
- `quests/street_stories/heywood/glen/sts_hey_gle_03/sts_hey_gle_03/safe/safe_mp1`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 2 |
| `questCheckpointNodeDefinition` | 3 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_ShootAt]` | 2 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 24 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questCutControlNodeDefinition` | 12 |
| `questDeletionMarkerNodeDefinition` | 30 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 1 |
| `questEventManagerNodeDefinition` | 42 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 63 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 5 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 27 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 27 |
| `questInteractiveObjectManagerNodeDefinition[questSetInteractionState_NodeType]` | 1 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 19 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMappinManagerNodeDefinition` | 4 |
| `questMiscAICommandNode` | 4 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 2 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 2 |
| `questOutputNodeDefinition` | 19 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterAttack_ConditionType,questCharacterCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 10 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 26 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questSensesCondition,questVision_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 6 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 24 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckSpeakerDistractedInterruptCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 33 |
| `questPhaseNodeDefinition` | 23 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 30 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 3 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 22 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 4 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 1 |
| `questVisionModesManagerNodeDefinition[questSetFocusClueState_NodeType]` | 6 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 12 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |
| `scnChoiceNode[scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 7 |
| `scnCutControlNode[scnNodeId]` | 4 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 8 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 19 |
| `scnStartNode[scnNodeId]` | 6 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `d0feae257f5e5216f8f9` | 10 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_scene.scene` / scene / 115 -> 302 -> 822 |
| `624d47eac987aa67b8fb` | 7 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_ow.questphase` / h40 / 18 -> 20 -> 120 |
| `a62f17bbd8fda8273c02` | 7 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_scene.scene` / scene / 338 -> 756 -> 305 |
| `e113af3fc5c917de8724` | 7 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_gameplay.questphase` / h426 / 258 -> 257 -> 45 |
| `fe09e851932a690ad62a` | 7 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_scene.scene` / scene / 852 -> 492 -> 326 |
| `02e0f2ad30fdd64812ca` | 6 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_bugfixing.questphase` / h283 / 28 -> 25 -> 27 |
| `237687944a84dd96b7b5` | 6 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_bugfixing.questphase` / h69 / 0 -> 4 -> 3 |
| `34871d2f16db446db7af` | 6 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_scene.scene` / scene / 545 -> 299 -> 863 |
| `a629e87be87848d8d5da` | 5 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_gameplay.questphase` / h355 / 36 -> 40 -> 1 |
| `b5cbb4b69f321db0d6b8` | 5 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_scene.scene` / scene / 299 -> 863 -> 115 |
| `19a5bfbc0b6690f905c3` | 4 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_ow.questphase` / h668 / 29 -> 42 -> 43 |
| `3c47849cedaf539b8171` | 4 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_scene.scene` / scene / 863 -> 115 -> 373 |
| `55b77b1e980d0b05295e` | 4 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_bugfixing.questphase` / h69 / 4 -> 3 -> 7 |
| `6077774245844a01fa9f` | 4 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_scene.scene` / scene / 863 -> 115 -> 302 |
| `6ae8da6c5722ea885b2a` | 4 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_bugfixing.questphase` / h283 / 25 -> 27 -> 26 |
| `aee5db5848aca58bcb31` | 4 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_scene.scene` / scene / 131 -> 118 -> 355 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_holocall_debriefs.scene` / scene / 272 -> 249 -> 251 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_holocall_debriefs.scene` / scene / 287 -> 289 -> 283 |
| `005d784cd70728b8b3df` | 3 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_scene.scene` / scene / 863 -> 115 -> 377 |
| `0067b70700dfd0b24eb8` | 3 | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_scene.scene` / scene / 568 -> 726 -> 729 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
