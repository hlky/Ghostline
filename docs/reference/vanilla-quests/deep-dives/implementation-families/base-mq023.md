# base-mq023

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq023\mq023_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq023\mq023_quest_bugfixes.questphase` | repair | 8 / 0 | base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene |
| `base\quest\minor_quests\mq023\mq023_bootleg.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq023\mq023_bootleg.quest` | content candidate | 2 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq023\mq023_bootleg.questphase; base\quest\minor_quests\mq023\temp\mq023_chicken_test.scene |
| `base\quest\minor_quests\mq023\mq023_bootleg.questphase` | content candidate | 7 / 0 | base\quest\minor_quests\mq023\phases\mq023_bootleg_01_hook.questphase; base\quest\minor_quests\mq023\phases\mq023_bootleg_02_diner.questphase; base\quest\minor_quests\mq023\phases\mq023_bootleg_03_vendor.questphase |
| `base\quest\minor_quests\mq023\phases\mq023_bootleg_01_hook.questphase` | content candidate | 3 / 0 | base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene |
| `base\quest\minor_quests\mq023\phases\mq023_bootleg_02_diner.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq023\scenes\mq023_02_dinner.scene |
| `base\quest\minor_quests\mq023\phases\mq023_bootleg_03_vendor.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene |
| `base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene` | content candidate | 0 / 41 |  |
| `base\quest\minor_quests\mq023\scenes\mq023_02_dinner.scene` | content candidate | 0 / 48 |  |
| `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` | content candidate | 0 / 221 |  |
| `base\quest\minor_quests\mq023\temp\mq023_chicken_test.scene` | test/debug | 0 / 8 |  |

## Journal paths observed in these resources

- `points_of_interest/minor_quests/mq023_bootleg`
- `points_of_interest/service_points/wbr_jpn_cloth_02`
- `quests/minor_quest/mq023_bootleg`
- `quests/minor_quest/mq023_bootleg/description`
- `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny`
- `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny/johnny`
- `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny/johnny1`
- `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny/johnny2`
- `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny/johnny3`
- `quests/minor_quest/mq023_bootleg/mq023_bootleg/02_go_to_venue`
- `quests/minor_quest/mq023_bootleg/mq023_bootleg/03_ask_the_staff`
- `quests/minor_quest/mq023_bootleg/mq023_bootleg/03a_talk_with_waiter`
- `quests/minor_quest/mq023_bootleg/mq023_bootleg/04_find_street_vendor`
- `quests/minor_quest/mq023_bootleg/mq023_bootleg/05_talk_with_karim`
- `quests/minor_quest/mq023_bootleg/mq023_bootleg/05a_obtain_samurai_recording_from_karim`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 4 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterEquippedItem_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 17 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 6 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 47 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 9 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 27 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 7 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 27 |
| `questLogicalHubNodeDefinition` | 10 |
| `questMappinManagerNodeDefinition` | 9 |
| `questOutputNodeDefinition` | 19 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 5 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 8 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 12 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 9 |
| `questPhaseNodeDefinition` | 18 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnCheckFactInterruptCondition,scnCheckFactInterruptConditionParams,scnCheckFactReturnCondition,scnCheckFactReturnConditionParams,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideReturnConditions_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnVarComparison_FactConditionType,scnVarComparison_FactConditionTypeParams,scnWorldMarker]` | 2 |
| `questSceneNodeDefinition[scnInterruptionScenarioId,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questScene_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 10 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 2 |
| `questUIManagerNodeDefinition[questVendorPanel_NodeType]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 15 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 33 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 3 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 6 |
| `scnAndNode[scnNodeId]` | 9 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questLifePath_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 10 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 3 |
| `scnEndNode[scnNodeId]` | 10 |
| `scnHubNode[scnNodeId]` | 26 |
| `scnRandomizerNode[scnNodeId]` | 3 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 70 |
| `scnStartNode[scnNodeId]` | 7 |
| `scnXorNode[scnNodeId]` | 11 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0f65e03c9a119b590711` | 5 | `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` / scene / 110 -> 114 -> 328 |
| `43d1a3cdcdcb1d73aed9` | 5 | `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` / scene / 536 -> 554 -> 544 |
| `99a8b829ee0f3d216442` | 5 | `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` / scene / 110 -> 112 -> 328 |
| `1fa539921730278ef7fb` | 4 | `base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene` / scene / 34 -> 36 -> 40 |
| `27faccd7b30abbc3add2` | 4 | `base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene` / scene / 11 -> 34 -> 38 |
| `2d4b441b83a065c6c296` | 4 | `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` / scene / 167 -> 651 -> 648 |
| `4ca5b66c6dc7e7690880` | 4 | `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` / scene / 672 -> 126 -> 129 |
| `a371bdb82fb1d0b00017` | 4 | `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` / scene / 343 -> 23 -> 1010 |
| `af6c94a57bc0ca13b4d8` | 4 | `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` / scene / 1054 -> 714 -> 730 |
| `b656c00028196994ce71` | 4 | `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` / scene / 343 -> 23 -> 503 |
| `c0bd56f15a35c907b820` | 4 | `base\quest\minor_quests\mq023\phases\mq023_bootleg_01_hook.questphase` / h109 / 5 -> 8 -> 2 |
| `c1b6601d2f647c8a694d` | 4 | `base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene` / scene / 11 -> 34 -> 36 |
| `c357cb47efedf046fb65` | 4 | `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` / scene / 1052 -> 1054 -> 714 |
| `dfd4d7249953e7dc9b66` | 4 | `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` / scene / 10 -> 13 -> 15 |
| `eaf5aab427d50e5598b6` | 4 | `base\quest\bugfixing\minor_quests\mq023\mq023_quest_bugfixes.questphase` / h30 / 0 -> 8 -> 2 |
| `feadb2f02c52e0121a04` | 4 | `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` / scene / 1052 -> 1054 -> 711 |
| `11073b13409b6e716484` | 3 | `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` / scene / 1054 -> 711 -> 1016 |
| `276aca4a2dc348a877d5` | 3 | `base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene` / scene / 46 -> 50 -> 182 |
| `42bd4d0ae29421109919` | 3 | `base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene` / scene / 209 -> 11 -> 237 |
| `6301eecf83656b7e9f6a` | 3 | `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` / scene / 546 -> 552 -> 558 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
