# base-mq022

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq022\mq022_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq022\mq022_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq022\mq022_quest_bugfixes.questphase` | repair | 4 / 0 |  |
| `base\quest\minor_quests\mq022\communities\mq022_com_diner.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq022\communities\mq022_com_gangers.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq022\mq022.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq022\mq022.quest` | content candidate | 3 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq022\mq022.questphase; base\quest\minor_quests\mq022\test\mq022_00_chicken.scene |
| `base\quest\minor_quests\mq022\mq022.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq022\phases\mq022_beginning.questphase |
| `base\quest\minor_quests\mq022\phases\mq022_beginning.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq022\phases\mq022_combat.questphase; base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene |
| `base\quest\minor_quests\mq022\phases\mq022_combat.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene |
| `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` | content candidate | 0 / 165 |  |
| `base\quest\minor_quests\mq022\test\mq022_00_chicken.scene` | test/debug | 0 / 9 |  |

## Journal paths observed in these resources

- `points_of_interest/minor_quests/mq022_ezekiel`
- `points_of_interest/service_points/std_arr_food_04`
- `quests/minor_quest/mq022_ezekiel`
- `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide`
- `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide/mp_area`
- `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide/mp_goon1`
- `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/02_decide/mq022_description`
- `quests/minor_quest/mq022_ezekiel/mq022_ezekiel/03_outcome`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 7 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 6 |
| `questCheckpointNodeDefinition` | 4 |
| `questCombatNodeDefinition` | 3 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 3 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questDeletionMarkerNodeDefinition` | 8 |
| `questEndNodeDefinition` | 1 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 6 |
| `questEventManagerNodeDefinition` | 5 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 16 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 14 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 11 |
| `questLogicalAndNodeDefinition` | 2 |
| `questMappinManagerNodeDefinition` | 2 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 6 |
| `questOutputNodeDefinition` | 11 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questPhaseNodeDefinition` | 10 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 11 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 12 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questVendorPanel_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 22 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 2 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 23 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questLifePath_ConditionType,questPaymentBalanced_ConditionType,questPaymentCondition,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 3 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 8 |
| `scnHubNode[scnNodeId]` | 13 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 28 |
| `scnStartNode[scnNodeId]` | 7 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `95f94bb99440f1b06321` | 6 | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 454 -> 441 -> 444 |
| `19665e3783f6f51a7337` | 4 | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 178 -> 171 -> 420 |
| `020a1995079767c97be8` | 3 | `base\quest\minor_quests\mq022\phases\mq022_combat.questphase` / h0 / 0 -> 30 -> 15 |
| `10e159686f8596c3cf12` | 3 | `base\quest\minor_quests\mq022\phases\mq022_combat.questphase` / h0 / 37 -> 3 -> 2 |
| `276aca4a2dc348a877d5` | 3 | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 100 -> 105 -> 946 |
| `81eccc836b758b3852d2` | 3 | `base\quest\minor_quests\mq022\test\mq022_00_chicken.scene` / scene / 36 -> 4 -> 9 |
| `859c7585ed8be68e3151` | 3 | `base\quest\minor_quests\mq022\phases\mq022_combat.questphase` / h0 / 8 -> 10 -> 28 |
| `e2f4a84af8e0c503880f` | 3 | `base\quest\minor_quests\mq022\phases\mq022_beginning.questphase` / h0 / 3 -> 6 -> 72 |
| `2609032a7ab1e00ae0fd` | 2 | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 776 -> 204 -> 885 |
| `3d1f28c7331b3765c279` | 2 | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 776 -> 204 -> 357 |
| `4518cc0fb86e98005539` | 2 | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 173 -> 501 -> 512 |
| `8530bf9138e338d3b6fa` | 2 | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 776 -> 204 -> 308 |
| `9c5162f63a419a5d6f46` | 2 | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 776 -> 204 -> 355 |
| `a737198437424e66c57c` | 2 | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 527 -> 246 -> 250 |
| `ac99bebd8eb3aca8fb86` | 2 | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 173 -> 501 -> 516 |
| `bc01b508fd157539b324` | 2 | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 173 -> 501 -> 518 |
| `ceed33220be9a743fcac` | 2 | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 173 -> 501 -> 514 |
| `eaf5aab427d50e5598b6` | 2 | `base\quest\bugfixing\minor_quests\mq022\mq022_quest_bugfixes.questphase` / h30 / 0 -> 8 -> 2 |
| `f6c835bd9f1bc713c842` | 2 | `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene` / scene / 776 -> 204 -> 365 |
| `0071e72430048a0e231e` | 1 | `base\quest\bugfixing\minor_quests\mq022\mq022_quest_bugfixes.questphase` / h30 / 2 -> 9 -> 10 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
