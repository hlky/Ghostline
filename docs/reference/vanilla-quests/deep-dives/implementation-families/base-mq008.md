# base-mq008

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq008\mq008_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq008\mq008_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq008\mq008_quest_bugfixes.questphase` | repair | 12 / 0 |  |
| `base\quest\minor_quests\mq008\communities\mq008_6th_street_party.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq008\communities\mq008_background.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq008\communities\mq008_representative.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq008\communities\mq008_shooting_competitors.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq008\mq008.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq008\mq008.quest` | content candidate | 5 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq008\mq008.questphase; base\quest\minor_quests\mq008\test\mq008_chicken_test.scene |
| `base\quest\minor_quests\mq008\mq008.questphase` | content candidate | 15 / 0 | base\quest\minor_quests\mq008\phases\mq008_01_hook.questphase; base\quest\minor_quests\mq008\phases\mq008_02_shooting_contest.questphase; base\quest\minor_quests\mq008\phases\mq008_cleanup.questphase; base\quest\minor_quests\mq008\scenes\mq008_01_party_chats.scene; base\quest\minor_quests\mq008\scenes\mq008_02_shooting_contest.scene |
| `base\quest\minor_quests\mq008\phases\mq008_01_hook.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq008\scenes\mq008_02_shooting_contest.scene |
| `base\quest\minor_quests\mq008\phases\mq008_02_shooting_contest.questphase` | content candidate | 9 / 0 | base\quest\minor_quests\mq008\scenes\mq008_02_shooting_contest.scene |
| `base\quest\minor_quests\mq008\phases\mq008_03_finale.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq008\phases\mq008_cleanup.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq008\scenes\mq008_01_party_chats.scene` | content candidate | 0 / 39 |  |
| `base\quest\minor_quests\mq008\scenes\mq008_02_shooting_contest.scene` | content candidate | 0 / 606 |  |
| `base\quest\minor_quests\mq008\test\mq008_chicken_test.scene` | test/debug | 0 / 16 |  |

## Journal paths observed in these resources

- `points_of_interest/minor_quests/mq008_party`
- `quests/minor_quest/mq008_party`
- `quests/minor_quest/mq008_party/mq008_party/01_check_whats_up`
- `quests/minor_quest/mq008_party/mq008_party/01_check_whats_up/description`
- `quests/minor_quest/mq008_party/mq008_party/02_speak_rep`
- `quests/minor_quest/mq008_party/mq008_party/02a_take_gun`
- `quests/minor_quest/mq008_party/mq008_party/03_first_spot`
- `quests/minor_quest/mq008_party/mq008_party/03_first_spot1`
- `quests/minor_quest/mq008_party/mq008_party/03_first_spot2`
- `quests/minor_quest/mq008_party/mq008_party/03_first_spot3`
- `quests/minor_quest/mq008_party/mq008_party/03a_points`
- `quests/minor_quest/mq008_party/mq008_party/04_drink_spot1`
- `quests/minor_quest/mq008_party/mq008_party/04_drink_spot2`
- `quests/minor_quest/mq008_party/mq008_party/04_drink_spot3`
- `quests/minor_quest/mq008_party/mq008_party/04_drink_spot4`
- `quests/minor_quest/mq008_party/mq008_party/05_shoot_bottles1`
- `quests/minor_quest/mq008_party/mq008_party/05_shoot_bottles2`
- `quests/minor_quest/mq008_party/mq008_party/05_shoot_bottles3`
- `quests/minor_quest/mq008_party/mq008_party/05_shoot_bottles4`
- `quests/minor_quest/mq008_party/mq008_party/15_back_to_rep`
- `quests/minor_quest/mq008_party/mq008_party/16_talk_results`
- `quests/minor_quest/mq008_party/mq008_party/17_pick_up_the_reward`
- `quests/side_quest/sq021_sick_dreams/after_bd/after_bd`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 47 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 26 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerVisuals_ChangeEntityAppearance,questCharacterManagerVisuals_EntityAppearanceOperationBaseEntityAppearanceEntry,questCharacterManagerVisuals_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 22 |
| `questCombatNodeDefinition` | 4 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 4 |
| `questCombatNodeDefinition[questCombatNodeParams_ShootAt]` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_UseCover]` | 4 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 46 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 19 |
| `questCutControlNodeDefinition` | 11 |
| `questDeletionMarkerNodeDefinition` | 14 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerChangeAppearance_NodeType]` | 4 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 5 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 15 |
| `questEventManagerNodeDefinition` | 2 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 125 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 7 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 4 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 26 |
| `questInputNodeDefinition` | 55 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 6 |
| `questItemManagerNodeDefinition[questLootTokenManager_NodeType,questLootTokenManager_NodeTypeParams]` | 29 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 6 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 7 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 63 |
| `questJournalNodeDefinition[questJournalQuestObjectiveCounter_NodeType]` | 55 |
| `questJournalNodeDefinition[questJournalTrackQuest_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 15 |
| `questLogicalHubNodeDefinition` | 17 |
| `questLogicalXorNodeDefinition` | 12 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 3 |
| `questOutputNodeDefinition` | 48 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 31 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 100 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 6 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 20 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 5 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 26 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 29 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 24 |
| `questPhaseNodeDefinition` | 39 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 52 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 6 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 3 |
| `questSceneNodeDefinition[scnCheckSpeakersDistanceInterruptCondition,scnCheckSpeakersDistanceInterruptConditionParams,scnCheckSpeakersDistanceReturnCondition,scnCheckSpeakersDistanceReturnConditionParams,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideReturnConditions_InterruptionScenarioOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnCheckSpeakersDistanceInterruptCondition,scnCheckSpeakersDistanceInterruptConditionParams,scnCheckSpeakersDistanceReturnCondition,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideReturnConditions_InterruptionScenarioOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 6 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 67 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 32 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 136 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 5 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 185 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 8 |
| `scnAndNode[scnNodeId]` | 10 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnChoiceNodeNsAttachToPropParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnPropId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsAttachToPropParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnPropId,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 3 |
| `scnCutControlNode[scnNodeId]` | 11 |
| `scnEndNode[scnNodeId]` | 15 |
| `scnHubNode[scnNodeId]` | 6 |
| `scnInterruptManagerNode[scnNodeId,scnToggleInterruption_InterruptionOperation]` | 10 |
| `scnRandomizerNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 89 |
| `scnStartNode[scnNodeId]` | 14 |
| `scnXorNode[scnNodeId]` | 7 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `34eaf4c96a57eecba00f` | 386 | `base\quest\bugfixing\minor_quests\mq008\mq008_quest_bugfixes.questphase` / h323 / 2 -> 13 -> 14 |
| `645735c3bf484e3d63c8` | 46 | `base\quest\minor_quests\mq008\phases\mq008_02_shooting_contest.questphase` / h84 / 0 -> 10 -> 21 |
| `0ef152e51cf02f57ee50` | 34 | `base\quest\bugfixing\minor_quests\mq008\mq008_quest_bugfixes.questphase` / h323 / 0 -> 10 -> 13 |
| `c6658c10a20ba3ee6ef6` | 23 | `base\quest\minor_quests\mq008\mq008.questphase` / h349 / 9 -> 10 -> 11 |
| `6abece444d43357dfc0e` | 22 | `base\quest\minor_quests\mq008\scenes\mq008_02_shooting_contest.scene` / scene / 19 -> 1835 -> 1823 |
| `cd362676c46d8f6c7955` | 22 | `base\quest\minor_quests\mq008\mq008.questphase` / h765 / 19 -> 16 -> 17 |
| `736c79459c75ac6c19e3` | 18 | `base\quest\minor_quests\mq008\mq008.questphase` / h765 / 18 -> 19 -> 16 |
| `5a1eaf3d395cb512f5b1` | 14 | `base\quest\minor_quests\mq008\mq008.questphase` / h127 / 0 -> 36 -> 28 |
| `68ae1d7dab1c54f8eee8` | 14 | `base\quest\bugfixing\minor_quests\mq008\mq008_quest_bugfixes.questphase` / h37 / 15 -> 10 -> 11 |
| `22b8ff11e7e49798423b` | 12 | `base\quest\minor_quests\mq008\phases\mq008_01_hook.questphase` / h0 / 0 -> 72 -> 70 |
| `bf93571076914e7a0919` | 12 | `base\quest\minor_quests\mq008\scenes\mq008_02_shooting_contest.scene` / scene / 224 -> 225 -> 227 |
| `53fcc8df7d3d3f5e7e49` | 10 | `base\quest\minor_quests\mq008\scenes\mq008_02_shooting_contest.scene` / scene / 214 -> 2308 -> 2301 |
| `9d5c6c2231c9f23738c3` | 10 | `base\quest\minor_quests\mq008\mq008.questphase` / h1216 / 0 -> 42 -> 39 |
| `a739cc00f75762c49cb4` | 10 | `base\quest\minor_quests\mq008\scenes\mq008_01_party_chats.scene` / scene / 77 -> 131 -> 125 |
| `85ed96a06d0cb5f6104e` | 9 | `base\quest\minor_quests\mq008\scenes\mq008_02_shooting_contest.scene` / scene / 1203 -> 1253 -> 688 |
| `20a77143a898bc753a26` | 8 | `base\quest\minor_quests\mq008\mq008.quest` / h52 / 31 -> 32 -> 33 |
| `275552dc464a435a7ad4` | 8 | `base\quest\minor_quests\mq008\phases\mq008_01_hook.questphase` / h0 / 75 -> 76 -> 70 |
| `6e66b967a4e71571e809` | 7 | `base\quest\minor_quests\mq008\mq008.questphase` / h765 / 0 -> 10 -> 11 |
| `016828d499c85128303c` | 6 | `base\quest\minor_quests\mq008\scenes\mq008_02_shooting_contest.scene` / scene / 178 -> 213 -> 214 |
| `112d47aac2c5a0d28140` | 6 | `base\quest\minor_quests\mq008\scenes\mq008_02_shooting_contest.scene` / scene / 172 -> 174 -> 640 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
