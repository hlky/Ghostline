# base-mq049

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\minor_quests\mq049\mq049.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq049\mq049.quest` | content candidate | 1 / 0 | base\quest\minor_quests\mq049\mq049.questphase |
| `base\quest\minor_quests\mq049\mq049.questphase` | content candidate | 4 / 0 | base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase; base\quest\minor_quests\mq049\phases\mq049_messages_reyes.questphase; base\quest\minor_quests\mq049\scenes\mq049_braindance.scene |
| `base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq049\phases\mq049_messages_reyes.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq049\scenes\mq049_braindance.scene` | content candidate | 0 / 94 |  |

## Journal paths observed in these resources

- `contacts/falco`
- `contacts/falco/mq049_about_david/01_asking_around`
- `contacts/falco/mq049_about_david/02_why_asking`
- `contacts/falco/mq049_about_david/03_ch_about_david`
- `contacts/falco/mq049_about_david/03_ch_about_david/03_about_david`
- `contacts/falco/mq049_about_david/03_ch_about_david/03_about_xbd`
- `contacts/falco/mq049_about_david/04_left_the_job`
- `contacts/falco/mq049_about_david/05_skipped_town`
- `contacts/falco/mq049_about_david/06_about_v`
- `contacts/falco/mq049_about_david/07_about_v_2`
- `contacts/falco/mq049_about_david/08_about_v_3`
- `contacts/falco/mq049_about_david/09_about_v_4`
- `contacts/falco/mq049_about_david/10_gift`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/00_about_right_next_to_him`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/01_ch_do_you_know_david`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/01_ch_do_you_know_david/01_braindance_about_david`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/02_about_xbd`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/03_about_david`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/04_about_david_2`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/05_aboud_david_3`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/06_about_david_4`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/07_ch_corpo`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/07_ch_corpo/07_about_arasaka`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/07_ch_corpo/07_wanna_meet`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/07b_ch_street_kid`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/07b_ch_street_kid/07_about_atlanta`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/07b_ch_street_kid/07_wanna_meet_sk`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/07c_nomad`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/07c_nomad/07_wanna_meet_nmd`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/07c_nomad/07c_learn_more_nmd`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/08_try_to_find_out`
- `contacts/muamar_el_capitan_reyes/mq049_about_david_01/09_package`
- `points_of_interest/minor_quests/mq049_edgerunners`
- `quests/minor_quest/mq049_edgerunners`
- `quests/minor_quest/mq049_edgerunners/01_el_captian/01_text_capitan`
- `quests/minor_quest/mq049_edgerunners/01_el_captian/02_wait`
- `quests/minor_quest/mq049_edgerunners/02_falco/01_respond_to_falco`
- `quests/minor_quest/mq049_edgerunners/03_gift/02_pick_up_gift`
- `quests/minor_quest/mq049_edgerunners/desc`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetLifePath]` | 1 |
| `questCheckpointNodeDefinition` | 4 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questDistanceComparison_ConditionType,questDistanceCondition,questFactsDBCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance,questVarComparison_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 9 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 2 |
| `questInputNodeDefinition` | 6 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 32 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 9 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType,questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInputAction_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 9 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 7 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questPhoneManagerNodeDefinition[questAddRemoveContact_NodeType,questChangeContactList_NodeTypeParams]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questLifePath_ConditionType,questStatsCondition,questUniversalRef]` | 1 |
| `questUIManagerNodeDefinition[questBriefingSequencePlayer_NodeType]` | 63 |
| `questUIManagerNodeDefinition[questHUDVideo_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |
| `scnChoiceNode[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 5 |
| `scnStartNode[scnNodeId]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `82efcbc8277c892f8e90` | 61 | `base\quest\minor_quests\mq049\scenes\mq049_braindance.scene` / scene / 24 -> 223 -> 240 |
| `7e7dbbc930b3717fd790` | 9 | `base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase` / h0 / 9 -> 10 -> 11 |
| `4c0aaaa4b072b690a600` | 2 | `base\quest\minor_quests\mq049\phases\mq049_messages_reyes.questphase` / h0 / 32 -> 33 -> 4 |
| `4c72b4a7256f3776df46` | 2 | `base\quest\minor_quests\mq049\phases\mq049_messages_reyes.questphase` / h0 / 31 -> 32 -> 33 |
| `522b070bac1b6d24f9f7` | 2 | `base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase` / h0 / 5 -> 6 -> 8 |
| `b4a0ea15fadec3bacd08` | 2 | `base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase` / h0 / 5 -> 7 -> 8 |
| `b54739889d4d9a0745d2` | 2 | `base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase` / h0 / 4 -> 5 -> 6 |
| `06d9eaceb13cdd234b32` | 1 | `base\quest\minor_quests\mq049\scenes\mq049_braindance.scene` / scene / 119 -> 111 -> 506 |
| `07a508d9181a1ec44ac6` | 1 | `base\quest\minor_quests\mq049\mq049.questphase` / h0 / 17 -> 18 -> 23 |
| `082dd7eba90615a8c6a9` | 1 | `base\quest\minor_quests\mq049\phases\mq049_messages_reyes.questphase` / h0 / 37 -> 22 -> 23 |
| `0d751dfd858368b578dc` | 1 | `base\quest\minor_quests\mq049\mq049.quest` / h0 / 0 -> 3 -> 2 |
| `11e44de79f1708a0c89b` | 1 | `base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase` / h0 / 30 -> 3 -> 4 |
| `1389e62364fbb2bc008f` | 1 | `base\quest\minor_quests\mq049\phases\mq049_messages_reyes.questphase` / h0 / 0 -> 2 -> 3 |
| `14a09e3075b38b5c1b01` | 1 | `base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase` / h0 / 8 -> 9 -> 10 |
| `15d558010c9ee43c21c5` | 1 | `base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase` / h0 / 27 -> 16 -> 17 |
| `1a9b8893087e174a603f` | 1 | `base\quest\minor_quests\mq049\phases\mq049_messages_falco.questphase` / h0 / 25 -> 26 -> 24 |
| `2179acd57cd33a158da3` | 1 | `base\quest\minor_quests\mq049\scenes\mq049_braindance.scene` / scene / 134 -> 57 -> 83 |
| `22bf382198c83f08a3c5` | 1 | `base\quest\minor_quests\mq049\scenes\mq049_braindance.scene` / scene / 38 -> 151 -> 105 |
| `27136cdc3ef8cfc062cc` | 1 | `base\quest\minor_quests\mq049\mq049.questphase` / h0 / 10 -> 6 -> 19 |
| `2aa0f3a3b004f071652f` | 1 | `base\quest\minor_quests\mq049\mq049.questphase` / h178 / 2 -> 3 -> 1 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
