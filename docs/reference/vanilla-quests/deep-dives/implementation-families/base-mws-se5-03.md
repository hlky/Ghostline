# base-mws-se5-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\communities\mws_se5_03_enemies.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\communities\mws_se5_03_enemies_level_2.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\mws_se5_03.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\mws_se5_03.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\badlands\se5\mws_se5_03\mws_se5_03.questphase; base\quest\main_quests\part1\q110\phases\q110_shards.questphase |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\mws_se5_03.questphase` | content candidate | 17 / 0 | base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase; base\open_world\mini_world_stories\badlands\se5\mws_se5_03\scenes\mws_se5_03_arcade.scene |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_elevator.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase` | content candidate | 26 / 0 | base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_elevator.questphase |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\scenes\mws_se5_03_arcade.scene` | content candidate | 0 / 7 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\test\mws_se5_03_03_test.gamedef` | test/debug | 0 / 0 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\test\mws_se5_03_03_test.quest` | test/debug | 1 / 0 | base\open_world\mini_world_stories\badlands\se5\mws_se5_03\mws_se5_03.questphase; base\quest\main_quests\part1\q110\phases\q110_shards.questphase |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 21 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCombatNodeDefinition` | 7 |
| `questCombatNodeDefinition[questCombatNodeParams_PrimaryWeapon]` | 72 |
| `questCombatNodeDefinition[questCombatNodeParams_ShootAt]` | 65 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questCutControlNodeDefinition` | 4 |
| `questDeletionMarkerNodeDefinition` | 10 |
| `questEndNodeDefinition` | 2 |
| `questEntityManagerNodeDefinition[questEntityManagerSetAttachment_NodeType,questEntityManagerSetAttachment_ToActor]` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 1 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_NodeType,questPlayEnv_NodeTypeParams]` | 2 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 2 |
| `questEventManagerNodeDefinition` | 48 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 56 |
| `questFlowControlNodeDefinition` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 10 |
| `questGameManagerNodeDefinition[questReplacer_NodeType]` | 2 |
| `questInputNodeDefinition` | 52 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questLogicalAndNodeDefinition` | 86 |
| `questLogicalHubNodeDefinition` | 77 |
| `questLogicalXorNodeDefinition` | 36 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 65 |
| `questOutputNodeDefinition` | 56 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 90 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterEquippedWeapon_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 74 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 11 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 95 |
| `questPauseConditionNodeDefinition[questInputAction_ConditionType,questLogicalCondition,questRealtimeDelay_ConditionType,questSystemCondition,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInputAction_ConditionType,questSystemCondition]` | 4 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questNewPlayerPuppetAttached_ConditionType,questSceneCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 119 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 7 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 10 |
| `questPhaseNodeDefinition` | 49 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 7 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 79 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 2 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 7 |
| `questUIManagerNodeDefinition[questSetHUDEntryForcedVisibility_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 74 |
| `questWorldDataManagerNodeDefinition[questPrefetchStreaming_NodeTypeV2]` | 8 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 10 |
| `scnEndNode[scnNodeId]` | 3 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 2 |
| `scnStartNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `442238c482da733cda28` | 100 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase` / h540 / 23 -> 110 -> 84 |
| `5e2c47c1fddd7393e727` | 95 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase` / h540 / 0 -> 102 -> 106 |
| `69ebc1f40fd0682a5e9f` | 72 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase` / h19 / 0 -> 1 -> 2 |
| `b33d06eca8b61362a322` | 72 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase` / h19 / 0 -> 1 -> 3 |
| `ee4f197be77cf3410212` | 60 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase` / h4847 / 8 -> 10 -> 15 |
| `987122e5e2fcd167cf6c` | 55 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase` / h19 / 4 -> 0 -> 1 |
| `ca4e1633d0ebcd8e055b` | 54 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase` / h540 / 0 -> 102 -> 20 |
| `654131aaccfd5bd72944` | 53 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase` / h540 / 123 -> 11 -> 121 |
| `be2fc47650311eaf8981` | 34 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase` / h540 / 102 -> 106 -> 103 |
| `2d6b2c00445c86bfa127` | 18 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase` / h6285 / 104 -> 102 -> 186 |
| `9af8a87f20a910659fa8` | 11 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\mws_se5_03.questphase` / h143 / 2 -> 3 -> 4 |
| `58e53be9efa5160bef79` | 7 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\mws_se5_03.questphase` / h914 / 49 -> 13 -> 61 |
| `d7c45735730cd667dcd2` | 7 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\mws_se5_03.questphase` / h914 / 29 -> 28 -> 33 |
| `072241491beaf6604a7b` | 6 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase` / h4168 / 3 -> 6 -> 7 |
| `1e4232b12b72a0e26af6` | 6 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\mws_se5_03.questphase` / h11 / 38 -> 40 -> 39 |
| `56ec1d6e162b0b58447e` | 6 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase` / h0 / 25 -> 3 -> 4 |
| `74dc076b3f628ca067fc` | 6 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase` / h4168 / 0 -> 3 -> 6 |
| `92278d4fd1c84aae94ef` | 6 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase` / h4168 / 6 -> 7 -> 3 |
| `9a1af7d42db8b3f48809` | 6 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase` / h540 / 126 -> 99 -> 153 |
| `b816145de3198c1f80be` | 6 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_03\phases\mws_se5_03_levels.questphase` / h19 / 9 -> 59 -> 72 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
