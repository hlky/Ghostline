# base-mq038

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq038\mq038_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq038\mq038_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq038\mq038_quest_bugfixes.questphase` | repair | 4 / 0 |  |
| `base\quest\minor_quests\mq038\communities\mq038_car.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq038\communities\mq038_darryl.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq038\communities\mq038_surgeon.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq038\communities\mq038_tyger.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq038\mq038.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq038\mq038.quest` | content candidate | 3 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq038\mq038.questphase; base\quest\minor_quests\mq038\test\mq038_00_chicken.scene |
| `base\quest\minor_quests\mq038\mq038.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq038\phases\mq038_briefing.questphase; base\quest\minor_quests\mq038\phases\mq038_ending.questphase; base\quest\minor_quests\mq038\phases\mq038_village.questphase |
| `base\quest\minor_quests\mq038\phases\mq038_briefing.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq038\scenes\mq038_01_briefing.scene |
| `base\quest\minor_quests\mq038\phases\mq038_ending.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq038\scenes\mq038_02_ending.scene |
| `base\quest\minor_quests\mq038\phases\mq038_tyger_combat.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq038\scenes\mq038_01b_fisher_village.scene |
| `base\quest\minor_quests\mq038\phases\mq038_village.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq038\phases\mq038_tyger_combat.questphase; base\quest\minor_quests\mq038\scenes\mq038_01b_fisher_village.scene |
| `base\quest\minor_quests\mq038\scenes\mq038_01_briefing.scene` | content candidate | 0 / 31 |  |
| `base\quest\minor_quests\mq038\scenes\mq038_01b_fisher_village.scene` | content candidate | 0 / 42 |  |
| `base\quest\minor_quests\mq038\scenes\mq038_02_ending.scene` | content candidate | 0 / 46 |  |
| `base\quest\minor_quests\mq038\test\mq038_00_chicken.scene` | test/debug | 0 / 8 |  |

## Journal paths observed in these resources

- `contacts/darryl`
- `contacts/darryl/00_msg/00_msg`
- `points_of_interest/minor_quests/mq038_newer_identity`
- `quests/main_quest/act_01/q103_warhead/afterlife/talk_rogue`
- `quests/main_quest/act_01/q103_warhead/afterlife/wait_for_rogue`
- `quests/minor_quest/mq038_neweridentity`
- `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/01_fishing_village`
- `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/01_fishing_village/mq038_description`
- `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/02_find_dumpster`
- `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/02b_call_darryl`
- `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/02b_call_darryl/contact`
- `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/03_recover_body`
- `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/04_deliver_to_car`
- `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/05_hide_trunk`
- `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/06_deliver_northside`
- `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/06_enter_car`
- `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/08_talk_cargo`
- `quests/minor_quest/mq038_neweridentity/mq038_neweridentity/09_leave_car`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 5 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 6 |
| `questCheckpointNodeDefinition` | 6 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 4 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 13 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 21 |
| `questFlowControlNodeDefinition` | 1 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 16 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 4 |
| `questInputNodeDefinition` | 21 |
| `questItemManagerNodeDefinition[questLootTokenManager_NodeType,questLootTokenManager_NodeTypeParams]` | 1 |
| `questItemManagerNodeDefinition[questSetLootInteractionAccess_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 39 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 10 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 17 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 10 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 15 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleTrunk_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleWater_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 13 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPhoneManagerNodeDefinition[questAddRemoveContact_NodeType,questChangeContactList_NodeTypeParams]` | 3 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 1 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 2 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 15 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 4 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 8 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 11 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 4 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 3 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 7 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 6 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 16 |
| `scnHubNode[scnNodeId]` | 2 |
| `scnInterruptManagerNode[scnNodeId,scnToggleInterruption_InterruptionOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 25 |
| `scnStartNode[scnNodeId]` | 11 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `8cd3b647ae3f592ad947` | 6 | `base\quest\minor_quests\mq038\scenes\mq038_01b_fisher_village.scene` / scene / 129 -> 131 -> 263 |
| `95d4997362b664c5c23b` | 6 | `base\quest\minor_quests\mq038\scenes\mq038_01_briefing.scene` / scene / 8 -> 10 -> 15 |
| `4d1fb41a048cfeab6b7d` | 5 | `base\quest\minor_quests\mq038\scenes\mq038_01_briefing.scene` / scene / 8 -> 10 -> 57 |
| `5db090327cb2f56e5c66` | 4 | `base\quest\minor_quests\mq038\mq038.quest` / h47 / 59 -> 60 -> 58 |
| `beb973ec5bf382543b03` | 4 | `base\quest\minor_quests\mq038\phases\mq038_tyger_combat.questphase` / h0 / 1 -> 2 -> 3 |
| `08fabdc4110dabc6ef30` | 3 | `base\quest\minor_quests\mq038\phases\mq038_village.questphase` / h0 / 15 -> 110 -> 108 |
| `1666d7526b9bab74f2e2` | 3 | `base\quest\minor_quests\mq038\phases\mq038_village.questphase` / h0 / 14 -> 15 -> 6 |
| `48743e0c05bd9fbed33c` | 3 | `base\quest\minor_quests\mq038\scenes\mq038_01_briefing.scene` / scene / 68 -> 73 -> 77 |
| `5d7426ec2e9d31972dae` | 3 | `base\quest\bugfixing\minor_quests\mq038\mq038_quest_bugfixes.questphase` / h7 / 8 -> 2 -> 9 |
| `71576e87fda4df75a3d0` | 3 | `base\quest\minor_quests\mq038\scenes\mq038_02_ending.scene` / scene / 8 -> 38 -> 132 |
| `7ad12c5f19ada17bab92` | 3 | `base\quest\minor_quests\mq038\scenes\mq038_01_briefing.scene` / scene / 57 -> 12 -> 10 |
| `cab86e1b14fab21fe85b` | 3 | `base\quest\minor_quests\mq038\mq038.questphase` / h38 / 44 -> 26 -> 24 |
| `e5742f9794e6583c67cb` | 3 | `base\quest\minor_quests\mq038\scenes\mq038_01b_fisher_village.scene` / scene / 143 -> 137 -> 138 |
| `eaf5aab427d50e5598b6` | 3 | `base\quest\bugfixing\minor_quests\mq038\mq038_quest_bugfixes.questphase` / h7 / 0 -> 8 -> 2 |
| `04b2a53bbfa5c622f2c5` | 2 | `base\quest\minor_quests\mq038\phases\mq038_village.questphase` / h0 / 179 -> 49 -> 50 |
| `0e147d9e68a4074ab8c6` | 2 | `base\quest\minor_quests\mq038\mq038.quest` / h47 / 56 -> 57 -> 59 |
| `0fd12d360ba51fd6444b` | 2 | `base\quest\minor_quests\mq038\phases\mq038_tyger_combat.questphase` / h0 / 22 -> 19 -> 15 |
| `135acc6a84f028c67005` | 2 | `base\quest\minor_quests\mq038\phases\mq038_village.questphase` / h494 / 7 -> 6 -> 11 |
| `2b8291b6d86672a1ab66` | 2 | `base\quest\minor_quests\mq038\scenes\mq038_02_ending.scene` / scene / 30 -> 43 -> 27 |
| `3fe0ae98a8cf5496b004` | 2 | `base\quest\minor_quests\mq038\phases\mq038_ending.questphase` / h0 / 58 -> 55 -> 56 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
