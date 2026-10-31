# base-mq015

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq015\mq015_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq015\mq015_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq015\mq015_quest_bugfixes.questphase` | repair | 4 / 0 |  |
| `base\quest\minor_quests\mq015\communities\mq015_com_seller.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq015\mq015_wizardbook.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq015\mq015_wizardbook.quest` | content candidate | 2 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq015\mq015_wizardbook.questphase; base\quest\minor_quests\mq015\test\mq015_00_chickentest.scene |
| `base\quest\minor_quests\mq015\mq015_wizardbook.questphase` | content candidate | 5 / 0 | base\quest\minor_quests\mq015\phases\mq015_01_hook.questphase; base\quest\minor_quests\mq015\phases\mq015_02_restaurant.questphase; base\quest\minor_quests\mq015\phases\mq015_03_stash.questphase; base\quest\minor_quests\mq015\phases\mq015_04_afterlife.questphase |
| `base\quest\minor_quests\mq015\phases\mq015_01_hook.questphase` | content candidate | 3 / 0 | base\quest\minor_quests\mq015\scenes\mq015_01_hook.scene; base\quest\minor_quests\mq015\scenes\mq015_02_seller_holocall.scene |
| `base\quest\minor_quests\mq015\phases\mq015_02_restaurant.questphase` | content candidate | 4 / 0 | base\quest\minor_quests\mq015\phases\mq015_02_restaurant_combat.questphase; base\quest\minor_quests\mq015\scenes\mq015_03_restaurant.scene |
| `base\quest\minor_quests\mq015\phases\mq015_02_restaurant_combat.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq015\phases\mq015_03_stash.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq015\scenes\mq015_04_stash.scene |
| `base\quest\minor_quests\mq015\phases\mq015_04_afterlife.questphase` | content candidate | 3 / 0 | base\quest\minor_quests\mq015\scenes\mq015_05_afterlife.scene |
| `base\quest\minor_quests\mq015\scenes\mq015_01_hook.scene` | content candidate | 0 / 61 |  |
| `base\quest\minor_quests\mq015\scenes\mq015_02_seller_holocall.scene` | content candidate | 0 / 17 |  |
| `base\quest\minor_quests\mq015\scenes\mq015_03_restaurant.scene` | content candidate | 0 / 110 |  |
| `base\quest\minor_quests\mq015\scenes\mq015_04_stash.scene` | content candidate | 0 / 40 |  |
| `base\quest\minor_quests\mq015\scenes\mq015_05_afterlife.scene` | content candidate | 0 / 78 |  |
| `base\quest\minor_quests\mq015\test\mq015_00_chickentest.scene` | test/debug | 0 / 20 |  |

## Journal paths observed in these resources

- `contacts/nix/mq015_00_hook/mq015_00_msg_drop_by`
- `contacts/nix/mq015_00_hook/mq015_00_msg_reward`
- `contacts/nix/mq015_00_hook/mq015_01_msg_details`
- `contacts/nix/mq015_00_hook/mq015_01_msg_nix_happy`
- `contacts/nix/mq015_00_hook/mq015_02_ch_got_it`
- `contacts/nix/mq015_00_hook/mq015_02_msg_nix_angry`
- `contacts/nix/mq015_01_contact_details/mq015_02_ch_got_it`
- `contacts/player`
- `contacts/seller`
- `contacts/seller/mq015/01_reno_msg_meeting`
- `contacts/seller/mq015/02_reno_msg_be_alone`
- `contacts/seller/mq015/03_ch_got_it`
- `contacts/seller/mq015/03_ch_got_it/03a_ch_got_it`
- `contacts/seller/mq015/03_ch_got_it/03b_ch_no_games`
- `contacts/seller/mq015/04_reno_msg_i_see_you`
- `contacts/seller/mq015/05_reno_msg_stash`
- `contacts/seller/mq015/06_reno_msg_enjoy`
- `internet_sites/smugglerscache/01_treasures`
- `internet_sites/smugglerscache/01_treasures_before`
- `points_of_interest/minor_quests/mq015_wizardbook`
- `quests/minor_quest/mq015_wizardbook`
- `quests/minor_quest/mq015_wizardbook/01_hook/01_talk_with_nix`
- `quests/minor_quest/mq015_wizardbook/01_hook/01_talk_with_nix/description`
- `quests/minor_quest/mq015_wizardbook/01_hook/03_contact_seller`
- `quests/minor_quest/mq015_wizardbook/01_hook/03_contact_seller/contact`
- `quests/minor_quest/mq015_wizardbook/02_restaurant/00_go_to_coordinates1`
- `quests/minor_quest/mq015_wizardbook/02_restaurant/01_talk_with_seller`
- `quests/minor_quest/mq015_wizardbook/02_restaurant/02_defeat_seller`
- `quests/minor_quest/mq015_wizardbook/02_restaurant/03_check_computer`
- `quests/minor_quest/mq015_wizardbook/02_restaurant/04_steal_data`
- `quests/minor_quest/mq015_wizardbook/03_stash/01_go_to_coordinates`
- `quests/minor_quest/mq015_wizardbook/03_stash/03_open_stash`
- `quests/minor_quest/mq015_wizardbook/03_stash/04_examine_tablet`
- `quests/minor_quest/mq015_wizardbook/03_stash/04_take_wizardbook`
- `quests/minor_quest/mq015_wizardbook/03_stash/05_talk_johnny`
- `quests/minor_quest/mq015_wizardbook/04_afterlife/01_get_back_nix`
- `quests/minor_quest/mq015_wizardbook/04_afterlife/01b_ask_nix`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 12 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetLifePath]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 2 |
| `questCheckpointNodeDefinition` | 9 |
| `questConditionNodeDefinition[questBuild_ConditionType,questStatsCondition,questUniversalRef]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 13 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 7 |
| `questCutControlNodeDefinition` | 7 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 45 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 7 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 3 |
| `questInputNodeDefinition` | 30 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 5 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 5 |
| `questItemManagerNodeDefinition[questDropItemFromSlot_NodeType,questDropItemFromSlot_NodeTypeParams]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 60 |
| `questLogicalHubNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 3 |
| `questOutputNodeDefinition` | 22 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterAim_ConditionType,questCharacterCondition,questCharacterHit_ConditionType,questCharacterKilled_ConditionType,questCharacterQuickHackUploadBegin_ConditionType,questCharacterQuickHacked_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questInteraction_ConditionType,questLogicalCondition,questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questGameTimeDelay_ConditionType,questLogicalCondition,questObjectDistance,questTimeCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questPhone_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 9 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 11 |
| `questPhaseNodeDefinition` | 20 |
| `questPhoneManagerNodeDefinition[questAddRemoveContact_NodeType,questChangeContactList_NodeTypeParams]` | 2 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 7 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 9 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 2 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 1 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 24 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 38 |
| `questVisionModesManagerNodeDefinition[questSetFocusClueState_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |
| `scnAndNode[scnNodeId]` | 4 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[questJournalCondition,questJournalEntry_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questLifePath_ConditionType,questPaymentBalanced_ConditionType,questPaymentCondition,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[questPaymentBalanced_ConditionType,questPaymentCondition,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 4 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 14 |
| `scnHubNode[scnNodeId]` | 23 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnRandomizerNode[scnNodeId]` | 3 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 60 |
| `scnStartNode[scnNodeId]` | 11 |
| `scnXorNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `dfd4d7249953e7dc9b66` | 8 | `base\quest\minor_quests\mq015\scenes\mq015_03_restaurant.scene` / scene / 37 -> 79 -> 173 |
| `19a88caa75dca600f1b3` | 5 | `base\quest\minor_quests\mq015\scenes\mq015_05_afterlife.scene` / scene / 198 -> 208 -> 146 |
| `4eff172f0a4f11db34c7` | 5 | `base\quest\minor_quests\mq015\scenes\mq015_05_afterlife.scene` / scene / 198 -> 208 -> 322 |
| `1d1cd5b9c0bf5db49e08` | 4 | `base\quest\minor_quests\mq015\phases\mq015_02_restaurant.questphase` / h0 / 16 -> 7 -> 6 |
| `43d1a3cdcdcb1d73aed9` | 4 | `base\quest\minor_quests\mq015\scenes\mq015_03_restaurant.scene` / scene / 988 -> 1006 -> 996 |
| `48743e0c05bd9fbed33c` | 4 | `base\quest\minor_quests\mq015\scenes\mq015_01_hook.scene` / scene / 259 -> 252 -> 254 |
| `a81a453a72a390294928` | 4 | `base\quest\minor_quests\mq015\scenes\mq015_01_hook.scene` / scene / 252 -> 254 -> 256 |
| `0608e609d2123f6d6b19` | 3 | `base\quest\minor_quests\mq015\phases\mq015_01_hook.questphase` / h0 / 53 -> 17 -> 9 |
| `14d7b5c40ad1cfca9ca1` | 3 | `base\quest\minor_quests\mq015\scenes\mq015_03_restaurant.scene` / scene / 37 -> 79 -> 6 |
| `2795fc11ef125d24244f` | 3 | `base\quest\minor_quests\mq015\scenes\mq015_05_afterlife.scene` / scene / 242 -> 20 -> 122 |
| `4c19c27e3107f9ae4b13` | 3 | `base\quest\minor_quests\mq015\scenes\mq015_03_restaurant.scene` / scene / 341 -> 319 -> 79 |
| `4fa2901d5baeedde07ac` | 3 | `base\quest\minor_quests\mq015\scenes\mq015_03_restaurant.scene` / scene / 339 -> 341 -> 37 |
| `57869013471bfb52006f` | 3 | `base\quest\minor_quests\mq015\scenes\mq015_05_afterlife.scene` / scene / 23 -> 220 -> 242 |
| `6301eecf83656b7e9f6a` | 3 | `base\quest\minor_quests\mq015\scenes\mq015_03_restaurant.scene` / scene / 998 -> 1004 -> 1010 |
| `8093c8ed97a5833a38b2` | 3 | `base\quest\minor_quests\mq015\scenes\mq015_05_afterlife.scene` / scene / 23 -> 220 -> 326 |
| `8d098751ec13d64f322a` | 3 | `base\quest\minor_quests\mq015\scenes\mq015_05_afterlife.scene` / scene / 11 -> 23 -> 217 |
| `93977b2a92f554edcd12` | 3 | `base\quest\minor_quests\mq015\phases\mq015_01_hook.questphase` / h0 / 53 -> 17 -> 18 |
| `a59399ea0e475a2a2b2b` | 3 | `base\quest\minor_quests\mq015\scenes\mq015_05_afterlife.scene` / scene / 58 -> 11 -> 33 |
| `a6e5d517b583421b908c` | 3 | `base\quest\minor_quests\mq015\scenes\mq015_01_hook.scene` / scene / 31 -> 135 -> 78 |
| `c11cf4b8fc2f0bbc6f96` | 3 | `base\quest\minor_quests\mq015\scenes\mq015_03_restaurant.scene` / scene / 341 -> 319 -> 79 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
