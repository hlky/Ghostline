# base-sts-bls-ina-11

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\communities\ina_11_com_guards.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\communities\ina_11_com_robot.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\communities\ina_11_com_techies.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_gpl.questphase; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_ow.questphase |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_bugfixing.questphase` | repair | 5 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\scenes\sts_bls_ina_11_robot_fake_scene.scene |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_gpl.questphase` | content candidate | 11 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\scenes\sts_bls_ina_11_mood_scenes_chats.scene |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_ow.questphase` | content candidate | 9 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\scenes\sts_bls_ina_11_holocall_debriefs.scene; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\scenes\sts_bls_ina_11_holocall_prebrief.scene; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\scenes\sts_bls_ina_11_robot_fake_scene.scene |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\scenes\sts_bls_ina_11_gate_guard.scene` | content candidate | 0 / 3 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\scenes\sts_bls_ina_11_holocall_debriefs.scene` | content candidate | 0 / 25 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\scenes\sts_bls_ina_11_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\scenes\sts_bls_ina_11_mood_scenes_chats.scene` | content candidate | 0 / 3 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\scenes\sts_bls_ina_11_robot_fake_scene.scene` | content candidate | 0 / 5 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\sts_bls_ina_11.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\sts_bls_ina_11.quest` | content candidate | 2 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11.questphase; base\open_world\vendors\open_world_vendors.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\sts_bls_ina_11_test.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/dakota_smith/sts_bls_ina_11/sts_bls_ina_11_brief`
- `contacts/dakota_smith/sts_bls_ina_11/sts_bls_ina_11_holocall_debrief_ok`
- `contacts/dakota_smith/sts_bls_ina_11/sts_bls_ina_11_holocall_debrief_ppl_killed`
- `points_of_interest/street_stories/sts_bls_ina_11`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/brief`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/buy_robot`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/deliver_chip`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/extract_data`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/find_robot`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/get_to_landfill`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/go_to_robot`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/playstyles`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/wait_for_robot`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition` | 8 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 16 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 8 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questConditionNodeDefinition[questSpawnerCondition,questSpawnerReady_ConditionType]` | 1 |
| `questConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questCutControlNodeDefinition` | 11 |
| `questDeletionMarkerNodeDefinition` | 15 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 22 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 45 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 27 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 24 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questSetLootInteractionAccess_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 28 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 5 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMiscAICommandNode` | 8 |
| `questOutputNodeDefinition` | 17 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 4 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSceneCondition,questSceneNode_ConditionType,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType]` | 2 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 25 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 14 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 10 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleDoor_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 25 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 7 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 7 |
| `questSpawnManagerNodeDefinition[questLegacy_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 7 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 1 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 4 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 5 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 7 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 7 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 5 |
| `scnStartNode[scnNodeId]` | 5 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `9380dda43f90ecd62efb` | 13 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_gpl.questphase` / h531 / 10 -> 11 -> 12 |
| `415c2c7ab8d34be7e55a` | 9 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_ow.questphase` / h437 / 15 -> 16 -> 6 |
| `4d51b376e33439a8c9e4` | 9 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_ow.questphase` / h437 / 22 -> 15 -> 16 |
| `1666d7526b9bab74f2e2` | 5 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_ow.questphase` / h647 / 144 -> 145 -> 146 |
| `b25aa493ae49696e88da` | 5 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_ow.questphase` / h647 / 4 -> 131 -> 35 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\scenes\sts_bls_ina_11_holocall_debriefs.scene` / scene / 268 -> 272 -> 249 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\scenes\sts_bls_ina_11_holocall_debriefs.scene` / scene / 281 -> 283 -> 285 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\scenes\sts_bls_ina_11_holocall_debriefs.scene` / scene / 97 -> 281 -> 283 |
| `eaf5aab427d50e5598b6` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_bugfixing.questphase` / h7 / 0 -> 8 -> 9 |
| `0f462544288e80999427` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_ow.questphase` / h647 / 48 -> 47 -> 53 |
| `0fc319d37562369c3765` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_gpl.questphase` / h87 / 0 -> 2 -> 7 |
| `101b60945ddf6f25f378` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\scenes\sts_bls_ina_11_holocall_debriefs.scene` / scene / 68 -> 96 -> 98 |
| `138cff49923a75e07348` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_ow.questphase` / h647 / 37 -> 38 -> 39 |
| `6076134131f54580c7f1` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_bugfixing.questphase` / h117 / 22 -> 23 -> 25 |
| `65b19b442f66ff9107ec` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_ow.questphase` / h1198 / 8 -> 12 -> 13 |
| `a909c836470d2b0e7fbc` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_gpl.questphase` / h7 / 0 -> 21 -> 1 |
| `d5afa9feac9f3a3ee49f` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_bugfixing.questphase` / h117 / 22 -> 23 -> 24 |
| `02e0f2ad30fdd64812ca` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_gpl.questphase` / h452 / 38 -> 36 -> 35 |
| `082dd7eba90615a8c6a9` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\phases\sts_bls_ina_11_ow.questphase` / h647 / 53 -> 90 -> 91 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_11\scenes\sts_bls_ina_11_holocall_debriefs.scene` / scene / 272 -> 92 -> 95 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
