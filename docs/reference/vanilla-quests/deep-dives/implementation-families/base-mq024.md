# base-mq024

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq024\mq024_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq024\mq024_quest_bugfixes.questphase` | repair | 4 / 0 |  |
| `base\quest\minor_quests\mq024\mq024.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq024\mq024.quest` | content candidate | 3 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_05\phases\sts_wat_kab_05.questphase; base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq024\mq024.questphase; base\quest\minor_quests\mq024\phases\mq024_02a_data_carrier.questphase; base\quest\minor_quests\mq024\test\mq024_00_chicken_test.scene |
| `base\quest\minor_quests\mq024\mq024.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq024\phases\mq024_01_hook.questphase; base\quest\minor_quests\mq024\phases\mq024_02_scavengers.questphase; base\quest\minor_quests\mq024\phases\mq024_03_sandra_apartment.questphase; base\quest\minor_quests\mq024\phases\mq024_cleanup.questphase |
| `base\quest\minor_quests\mq024\phases\mq024_01_hook.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq024\phases\mq024_02_scavengers.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq024\phases\mq024_02a_data_carrier.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq024\phases\mq024_03_sandra_apartment.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene; base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene |
| `base\quest\minor_quests\mq024\phases\mq024_cleanup.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene` | content candidate | 0 / 23 |  |
| `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` | content candidate | 0 / 132 |  |
| `base\quest\minor_quests\mq024\test\mq024_00_chicken_test.scene` | test/debug | 0 / 6 |  |

## Journal paths observed in these resources

- `contacts/player`
- `contacts/sandra_dorsett`
- `contacts/sandra_dorsett/mq024_contract/01_sandra_msg_start`
- `quests/minor_quest/mq024_sandra`
- `quests/minor_quest/mq024_sandra/description`
- `quests/minor_quest/mq024_sandra/mq024_sandra/01_find_data_carrier`
- `quests/minor_quest/mq024_sandra/mq024_sandra/02_call_sandra`
- `quests/minor_quest/mq024_sandra/mq024_sandra/02_call_sandra/sandra`
- `quests/minor_quest/mq024_sandra/mq024_sandra/03_meet_sandra`
- `quests/minor_quest/mq024_sandra/mq024_sandra/03_meet_sandra/sandra_mp`
- `quests/minor_quest/mq024_sandra/mq024_sandra/04_defeat_sandra`
- `quests/street_stories/watson/kabuki/sts_wat_kab_05/sts_wat_kab_05/check_signal`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCheckpointNodeDefinition` | 4 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_ShootAt]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 3 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEndNodeDefinition` | 1 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 8 |
| `questEventManagerNodeDefinition` | 2 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 12 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 24 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 16 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 3 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 6 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 5 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 3 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 19 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMappinManagerNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 1 |
| `questOutputNodeDefinition` | 13 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterQuickHacked_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questMenuState_ConditionType,questUICondition]` | 1 |
| `questPauseConditionNodeDefinition[questPhone_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 13 |
| `questPhaseNodeDefinition` | 12 |
| `questPhoneManagerNodeDefinition[questAddRemoveContact_NodeType,questChangeContactList_NodeTypeParams]` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 7 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 11 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 7 |
| `questUIManagerNodeDefinition[questToggleStealthMappinVisibility_NodeSubType]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 7 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 13 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 3 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 5 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 29 |
| `scnStartNode[scnNodeId]` | 5 |
| `scnXorNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2b8291b6d86672a1ab66` | 6 | `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` / scene / 20 -> 181 -> 2 |
| `b7c20e844c13d6462b07` | 6 | `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` / scene / 6 -> 8 -> 115 |
| `f91b7f2fa0c4a59b83d2` | 6 | `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` / scene / 203 -> 209 -> 208 |
| `632ef998480ca34f801e` | 5 | `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` / scene / 492 -> 31 -> 157 |
| `f70c92ca9fc1183a7035` | 5 | `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` / scene / 492 -> 31 -> 181 |
| `2ec03990284c29a11f62` | 4 | `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene` / scene / 23 -> 26 -> 29 |
| `c1b6601d2f647c8a694d` | 4 | `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` / scene / 16 -> 18 -> 20 |
| `c5bfb7f330b80f0cec45` | 4 | `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene` / scene / 23 -> 26 -> 28 |
| `0055fad2e9937ce40ea3` | 3 | `base\quest\bugfixing\minor_quests\mq024\mq024_quest_bugfixes.questphase` / h98 / 9 -> 10 -> 1 |
| `27faccd7b30abbc3add2` | 3 | `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` / scene / 16 -> 18 -> 23 |
| `885e1ccdeb8486d73067` | 3 | `base\quest\minor_quests\mq024\phases\mq024_03_sandra_apartment.questphase` / h0 / 18 -> 35 -> 36 |
| `14b1836c863a92d28d17` | 2 | `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene` / scene / 13 -> 19 -> 62 |
| `25cac6cbea540defffe9` | 2 | `base\quest\minor_quests\mq024\mq024.questphase` / h0 / 14 -> 3 -> 4 |
| `2811d0c2efece7042a76` | 2 | `base\quest\bugfixing\minor_quests\mq024\mq024_quest_bugfixes.questphase` / h98 / 11 -> 5 -> 12 |
| `5dcb52f56d5c59063df0` | 2 | `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` / scene / 480 -> 40 -> 177 |
| `9e2b76729419d8ee1b7a` | 2 | `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene` / scene / 6 -> 23 -> 26 |
| `a845e730f9e487aaa1dd` | 2 | `base\quest\bugfixing\minor_quests\mq024\mq024_quest_bugfixes.questphase` / h98 / 8 -> 9 -> 10 |
| `bf65a2fd4286a52947d7` | 2 | `base\quest\minor_quests\mq024\phases\mq024_03_sandra_apartment.questphase` / h0 / 35 -> 36 -> 37 |
| `c0bfc7aed415a17a751b` | 2 | `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene` / scene / 487 -> 34 -> 160 |
| `d38133a1b05adfe1ed56` | 2 | `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene` / scene / 13 -> 19 -> 114 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
