# base-mq048

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\minor_quests\mq048\mq048.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq048\mq048.quest` | content candidate | 1 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq048\mq048.questphase; base\quest\minor_quests\mq048\test\mq048_chickentest.scene |
| `base\quest\minor_quests\mq048\mq048.questphase` | content candidate | 6 / 0 | base\quest\main_quests\part1\q105\phases\q105_complete.questphase; base\quest\main_quests\prologue\q001\q001.questphase; base\quest\main_quests\prologue\q003\q003.questphase; base\quest\minor_quests\mq048\phases\mq048_01_hook.questphase; base\quest\minor_quests\mq048\phases\mq048_02_cyberware_change.questphase |
| `base\quest\minor_quests\mq048\phases\mq048_01_hook.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq048\scenes\mq048_01_hook.scene |
| `base\quest\minor_quests\mq048\phases\mq048_02_cyberware_change.questphase` | content candidate | 18 / 0 |  |
| `base\quest\minor_quests\mq048\scenes\mq048_01_hook.scene` | content candidate | 0 / 24 |  |
| `base\quest\minor_quests\mq048\test\mq048_chickentest.scene` | test/debug | 0 / 18 |  |

## Journal paths observed in these resources

- `contacts/dex`
- `contacts/jackie`
- `contacts/victor_vector/mq048_cw_alt_hook/01_hook`
- `contacts/victor_vector/mq048_cw_alt_hook/01_hook_after_q101`
- `contacts/victor_vector/mq048_cw_alt_hook/02_v_answer`
- `contacts/victor_vector/mq048_cw_alt_hook/02_v_answer/02_v_answer_negative`
- `contacts/victor_vector/mq048_cw_alt_hook/02_v_answer/02_v_answer_positive`
- `contacts/victor_vector/mq048_cw_alt_hook/03_vic_response_negative`
- `contacts/victor_vector/mq048_cw_alt_hook/03_vic_response_positive`
- `contacts/victor_vector/mq048_cw_alt_hook/04_v_ask_for_visit`
- `contacts/victor_vector/mq048_cw_alt_hook/04_v_ask_for_visit/04_v_asks_about_visiting_victor`
- `contacts/victor_vector/mq048_cw_alt_hook/04_v_ask_for_visit/04_v_promise_visiting_ripper`
- `contacts/victor_vector/mq048_cw_alt_hook/04a_ask_visit2`
- `contacts/victor_vector/mq048_cw_alt_hook/04a_ask_visit2/04_copy_visiting_victor`
- `contacts/victor_vector/mq048_cw_alt_hook/05_vic_debt_paid`
- `contacts/victor_vector/mq048_cw_alt_hook/05_vic_debt_unpaid`
- `contacts/victor_vector/mq048_cw_alt_hook/06_vic_very_happy`
- `ep1/quests/main_quest/q307_before_tomorrow`
- `quests/main_quest/prologue/q001_01_victor/ripperdoc/go_to_ripperdoc`
- `quests/main_quest/prologue/q001_02_dex`
- `quests/minor_quest/mq048_cyberware`
- `quests/minor_quest/mq048_cyberware/description`
- `quests/minor_quest/mq048_cyberware/jackie_desc`
- `quests/minor_quest/mq048_cyberware/mq048_cyberware/01a_sms_hook`
- `quests/minor_quest/mq048_cyberware/mq048_cyberware/01a_sms_hook1`
- `quests/minor_quest/mq048_cyberware/mq048_cyberware/04_talk_ripper`
- `quests/minor_quest/mq048_cyberware/mq048_cyberware/04_talk_ripper/wat_kab_ripperdoc_01`
- `quests/minor_quest/mq048_cyberware/mq048_cyberware/04_talk_ripper/wat_kab_ripperdoc_02`
- `quests/minor_quest/mq048_cyberware/mq048_cyberware/04_talk_ripper/wat_kab_ripperdoc_03`
- `quests/minor_quest/mq048_cyberware/mq048_cyberware/04_talk_ripper/wat_lch_ripperdoc_01`
- `quests/minor_quest/mq048_cyberware/mq048_cyberware/04_talk_ripper/wat_nid_ripperdoc_01`
- `quests/minor_quest/mq048_cyberware/mq048_cyberware/04_talk_ripper/wbr_hil_ripdoc_01`
- `quests/minor_quest/mq048_cyberware/mq048_cyberware/04_talk_ripper/wbr_jpn_ripdoc_02`
- `quests/minor_quest/mq048_cyberware/mq048_cyberware/05_find_a_ripper`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 2 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questConditionNodeDefinition[questLanguage_ConditionType,questSystemCondition]` | 1 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 60 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 4 |
| `questInputNodeDefinition` | 30 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 3 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 87 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalHubNodeDefinition` | 8 |
| `questLogicalXorNodeDefinition` | 4 |
| `questOutputNodeDefinition` | 28 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterStatusEffect_CondtionType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questSceneCondition,questSceneTier_ConditionType,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questMenuState_ConditionType,questUICondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 8 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 27 |
| `questPauseConditionNodeDefinition[questUICondition,questUIElement_ConditionType]` | 16 |
| `questPhaseNodeDefinition` | 31 |
| `questPhoneManagerNodeDefinition[questAddRemoveContact_NodeType,questChangeContactList_NodeTypeParams]` | 2 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 6 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 6 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 7 |
| `scnStartNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `9af8a87f20a910659fa8` | 18 | `base\quest\minor_quests\mq048\mq048.questphase` / h32 / 21 -> 18 -> 19 |
| `4e9253a72e6b0134b8dd` | 13 | `base\quest\minor_quests\mq048\phases\mq048_02_cyberware_change.questphase` / h115 / 2 -> 8 -> 4 |
| `7c6b4ed153ff62de2c2b` | 13 | `base\quest\minor_quests\mq048\phases\mq048_02_cyberware_change.questphase` / h115 / 2 -> 3 -> 6 |
| `80e267731f33cc11da6b` | 13 | `base\quest\minor_quests\mq048\phases\mq048_02_cyberware_change.questphase` / h115 / 3 -> 6 -> 5 |
| `cf545f3807e4da42f675` | 13 | `base\quest\minor_quests\mq048\phases\mq048_02_cyberware_change.questphase` / h115 / 3 -> 2 -> 8 |
| `e09e7a57ea65bd0dbc61` | 13 | `base\quest\minor_quests\mq048\phases\mq048_02_cyberware_change.questphase` / h115 / 0 -> 2 -> 8 |
| `f2a344c7d6fe49ec5e9b` | 13 | `base\quest\minor_quests\mq048\phases\mq048_02_cyberware_change.questphase` / h115 / 0 -> 2 -> 3 |
| `b54739889d4d9a0745d2` | 6 | `base\quest\minor_quests\mq048\phases\mq048_01_hook.questphase` / h72 / 9 -> 11 -> 15 |
| `2d73eb28337ecf761033` | 3 | `base\quest\minor_quests\mq048\phases\mq048_02_cyberware_change.questphase` / h12 / 83 -> 82 -> 86 |
| `3e6f03030764fcc75954` | 3 | `base\quest\minor_quests\mq048\phases\mq048_01_hook.questphase` / h72 / 11 -> 15 -> 17 |
| `e5742f9794e6583c67cb` | 3 | `base\quest\minor_quests\mq048\scenes\mq048_01_hook.scene` / scene / 16 -> 134 -> 135 |
| `ea6f36c47ecc914c61e8` | 3 | `base\quest\minor_quests\mq048\phases\mq048_01_hook.questphase` / h72 / 7 -> 10 -> 11 |
| `f592188ae0bb35432245` | 3 | `base\quest\minor_quests\mq048\phases\mq048_01_hook.questphase` / h72 / 9 -> 11 -> 12 |
| `1f1fb4b574e47da29b8c` | 2 | `base\quest\minor_quests\mq048\mq048.questphase` / h32 / 30 -> 29 -> 28 |
| `240148efc76953d1c5d4` | 2 | `base\quest\minor_quests\mq048\phases\mq048_01_hook.questphase` / h72 / 36 -> 46 -> 50 |
| `343c3b3c590c677f4d54` | 2 | `base\quest\minor_quests\mq048\mq048.questphase` / h32 / 25 -> 27 -> 23 |
| `391986f58a211a4333be` | 2 | `base\quest\minor_quests\mq048\mq048.questphase` / h0 / 17 -> 25 -> 29 |
| `39a441338f08723da001` | 2 | `base\quest\minor_quests\mq048\scenes\mq048_01_hook.scene` / scene / 22 -> 26 -> 28 |
| `3c6ca06a33de1c936507` | 2 | `base\quest\minor_quests\mq048\mq048.questphase` / h32 / 20 -> 30 -> 29 |
| `3dedf8c29053fde241f2` | 2 | `base\quest\minor_quests\mq048\mq048.questphase` / h361 / 2 -> 3 -> 8 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
