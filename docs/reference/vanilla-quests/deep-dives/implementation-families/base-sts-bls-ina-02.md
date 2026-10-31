# base-sts-bls-ina-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\communities\bls_ina_02_big_pete.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\communities\bls_ina_02_gangers.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_bugfixing.questphase` | repair | 6 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_gpl.questphase` | content candidate | 10 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_fluff_chats.scene |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` | content candidate | 8 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_big_pete_scene.scene; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_prebrief.scene |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_phase.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_gpl.questphase; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_big_pete_scene.scene` | content candidate | 0 / 47 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_fluff_chats.scene` | content candidate | 0 / 5 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene` | content candidate | 0 / 25 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\sts_bls_ina_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\sts_bls_ina_02.quest` | content candidate | 1 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_phase.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\sts_bls_ina_02_testing.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/dakota_smith/sts_bls_ina_02/brief`
- `contacts/dakota_smith/sts_bls_ina_02/sts_bls_ina_02_holocall_debrief_big_pete_dead`
- `contacts/dakota_smith/sts_bls_ina_02/sts_bls_ina_02_holocall_debrief_big_pete_spared`
- `points_of_interest/street_stories/sts_bls_ina_02`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/eliminate_big_pete`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/find_big_pete`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/get_in`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/get_data/leave`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02/ina_02_briefing`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 5 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition` | 3 |
| `questConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 18 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 5 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 5 |
| `questDeletionMarkerNodeDefinition` | 19 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 13 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 44 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 6 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 25 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 40 |
| `questItemManagerNodeDefinition[questSetLootInteractionAccess_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 20 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalHubNodeDefinition` | 12 |
| `questLogicalXorNodeDefinition` | 6 |
| `questMiscAICommandNode` | 5 |
| `questMovePuppetNodeDefinition` | 2 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 15 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 17 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 14 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 27 |
| `questPhaseNodeDefinition` | 25 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 3 |
| `questRandomizerNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 7 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 5 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 8 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 4 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 6 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 14 |
| `scnStartNode[scnNodeId]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `9380dda43f90ecd62efb` | 27 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h1017 / 106 -> 104 -> 105 |
| `9bac626d79ee21ad7335` | 9 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h11 / 81 -> 98 -> 88 |
| `ec41f2c7eab5f54285e2` | 9 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h11 / 83 -> 98 -> 88 |
| `29cb69424d0ff586110c` | 6 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_gpl.questphase` / h135 / 51 -> 52 -> 22 |
| `a53561b4c002bc02b58a` | 5 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h543 / 149 -> 151 -> 68 |
| `eaf5aab427d50e5598b6` | 5 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_bugfixing.questphase` / h14 / 0 -> 8 -> 9 |
| `0000b85fdc719c7265b8` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_gpl.questphase` / h135 / 22 -> 28 -> 32 |
| `03ad46ecaef290402e0f` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_gpl.questphase` / h135 / 52 -> 22 -> 28 |
| `70630fa8a51c71ede2b9` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_gpl.questphase` / h135 / 22 -> 28 -> 33 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene` / scene / 249 -> 271 -> 253 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene` / scene / 282 -> 284 -> 286 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene` / scene / 98 -> 282 -> 284 |
| `101b60945ddf6f25f378` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene` / scene / 66 -> 97 -> 99 |
| `1cae77bdcdd789c2852b` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_big_pete_scene.scene` / scene / 160 -> 21 -> 302 |
| `62e0177d0c41eca20879` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h543 / 151 -> 134 -> 135 |
| `93ddaa4a93b72d573e31` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_big_pete_scene.scene` / scene / 160 -> 21 -> 431 |
| `cf9d1eff3bc903c01028` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_big_pete_scene.scene` / scene / 160 -> 21 -> 435 |
| `d5d062b201c56918d984` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_big_pete_scene.scene` / scene / 160 -> 21 -> 36 |
| `ecef605427439eeaa71f` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\phases\sts_bls_ina_02_ow.questphase` / h543 / 151 -> 68 -> 135 |
| `0609a8a801d44627a27b` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_big_pete_scene.scene` / scene / 197 -> 187 -> 174 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
