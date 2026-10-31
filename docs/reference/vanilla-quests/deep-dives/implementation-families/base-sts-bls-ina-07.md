# base-sts-bls-ina-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\communities\sts_bls_ina_07_bandits_and_cars.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\communities\sts_bls_ina_07_car.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\communities\sts_bls_ina_07_drones.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_gpl.questphase; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_ow.questphase |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_bugfixing.questphase` | repair | 7 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_gpl.questphase` | content candidate | 16 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_ow.questphase` | content candidate | 9 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\scenes\sts_bls_ina_07_comments.scene; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\scenes\sts_bls_ina_07_holocall_debriefs.scene; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\scenes\sts_bls_ina_07_holocall_prebrief.scene |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\scenes\sts_bls_ina_07_comments.scene` | content candidate | 0 / 20 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\scenes\sts_bls_ina_07_holocall_debriefs.scene` | content candidate | 0 / 26 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\scenes\sts_bls_ina_07_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\sts_bls_ina_07.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\sts_bls_ina_07.quest` | content candidate | 1 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\sts_bls_ina_07_test.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/dakota_smith/sts_bls_ina_07/sts_bls_ina_07_brief`
- `contacts/dakota_smith/sts_bls_ina_07/sts_bls_ina_07_debrief_failed`
- `contacts/dakota_smith/sts_bls_ina_07/sts_bls_ina_07_holocall_debriefs_good`
- `points_of_interest/street_stories/sts_bls_ina_07`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_04`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_04/retrieve_the_van/deliver_car`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_04/retrieve_the_van/leave_workshop`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_06/sts_bls_ina_06/park_car_in_garage`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/approach_the_car`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/deliver_car`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/find_car`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/get_inside`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/get_rid_of_chase`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/leave_car`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/optional_investigation`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/get_hdd_from_ghost_car/park_in_garage`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_07/ina_07_briefing`
- `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/get_to_the_van`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 19 |
| `questConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 17 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 4 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 3 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleCorrectlyPlaced_ConditionType]` | 1 |
| `questCutControlNodeDefinition` | 7 |
| `questDeletionMarkerNodeDefinition` | 38 |
| `questDynamicSpawnSystemNodeDefinition[questDynamicVehicleDespawn_NodeType]` | 2 |
| `questDynamicSpawnSystemNodeDefinition[questDynamicVehicleSpawn_NodeType]` | 6 |
| `questEventManagerNodeDefinition` | 15 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 53 |
| `questFlowControlNodeDefinition` | 2 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 7 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 37 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 3 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 9 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 4 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 4 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 39 |
| `questLogicalAndNodeDefinition` | 12 |
| `questLogicalHubNodeDefinition` | 10 |
| `questLogicalXorNodeDefinition` | 6 |
| `questMiscAICommandNode` | 9 |
| `questOutputNodeDefinition` | 32 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterMount_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 15 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 16 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 14 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 17 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questObjectCondition,questScan_ConditionType,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questSceneCondition,questSceneNode_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 18 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 11 |
| `questPhaseNodeDefinition` | 28 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 5 |
| `questRandomizerNodeDefinition` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 17 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 4 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 10 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 1 |
| `questVisionModesManagerNodeDefinition[questSetFocusClueState_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 6 |
| `scnChoiceNode[questCharacterCondition,questCharacterMount_ConditionType,scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 6 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 5 |
| `scnStartNode[scnNodeId]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `a469859c524b8b7714f7` | 15 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_gpl.questphase` / h85 / 0 -> 16 -> 11 |
| `987122e5e2fcd167cf6c` | 12 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_gpl.questphase` / h259 / 0 -> 2 -> 4 |
| `480a010388ce3a487ffb` | 8 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_gpl.questphase` / h259 / 4 -> 7 -> 12 |
| `4ff3abfc2e95448213b9` | 8 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_gpl.questphase` / h259 / 7 -> 12 -> 14 |
| `a36102ceee6fef729c5f` | 8 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_gpl.questphase` / h259 / 5 -> 7 -> 12 |
| `d8ef39870626a261efb0` | 8 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_gpl.questphase` / h259 / 6 -> 7 -> 12 |
| `81867a7f03bd3dc79a1f` | 7 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_ow.questphase` / h1042 / 13 -> 14 -> 17 |
| `2637d11cc89d07560812` | 5 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_ow.questphase` / h837 / 16 -> 21 -> 22 |
| `27f18f1cb76e39cd970a` | 5 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_ow.questphase` / h837 / 16 -> 21 -> 39 |
| `6deffcdb16038324e882` | 5 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_ow.questphase` / h1042 / 13 -> 16 -> 15 |
| `e8fc8e5f68ba8e86b8d3` | 5 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_ow.questphase` / h1042 / 25 -> 27 -> 9 |
| `045316bbf4dc2ccf8aca` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_gpl.questphase` / h259 / 13 -> 15 -> 16 |
| `10c2ecb8df5575125f58` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_ow.questphase` / h1042 / 4 -> 6 -> 8 |
| `13468e250901eef42202` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_gpl.questphase` / h173 / 0 -> 55 -> 56 |
| `146d03d186468f0e231d` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_gpl.questphase` / h259 / 12 -> 14 -> 16 |
| `21100aec4757412cdd42` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_gpl.questphase` / h171 / 133 -> 105 -> 140 |
| `237687944a84dd96b7b5` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_bugfixing.questphase` / h14 / 0 -> 3 -> 2 |
| `3a78e140dfbf902a415b` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_ow.questphase` / h1042 / 14 -> 17 -> 4 |
| `415eb0e0e097f846c0af` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_ow.questphase` / h1042 / 6 -> 8 -> 2 |
| `5a3a5bfa8def6c7de66a` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_07\phases\sts_bls_ina_07_gpl.questphase` / h173 / 56 -> 57 -> 38 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
