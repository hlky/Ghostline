# base-mq041

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq041\mq041_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq041\mq041_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq041\mq041_quest_bugfixes.questphase` | repair | 3 / 0 | base\quest\minor_quests\mq041\phases\mq041_corpo_00_main.questphase; base\quest\minor_quests\mq041\phases\mq041_corpo_02_confrontation.questphase |
| `base\quest\minor_quests\mq041\mq041_corpo.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq041\mq041_corpo.quest` | content candidate | 1 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq041\mq041_corpo.questphase; base\quest\minor_quests\mq041\temp\mq041_corpo_chicken_test.scene |
| `base\quest\minor_quests\mq041\mq041_corpo.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq041\phases\mq041_corpo_00_main.questphase |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_00_main.questphase` | content candidate | 4 / 0 | base\quest\minor_quests\mq041\phases\mq041_corpo_01_hook.questphase; base\quest\minor_quests\mq041\phases\mq041_corpo_02_confrontation.questphase |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_01_hook.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq041\scenes\mq041_corpo_01_deadmans_switch.scene |
| `base\quest\minor_quests\mq041\phases\mq041_corpo_02_confrontation.questphase` | content candidate | 3 / 0 | base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene |
| `base\quest\minor_quests\mq041\scenes\mq041_corpo_01_deadmans_switch.scene` | content candidate | 0 / 17 |  |
| `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` | content candidate | 0 / 167 |  |
| `base\quest\minor_quests\mq041\temp\mq041_corpo_chicken_test.scene` | test/debug | 0 / 11 |  |

## Journal paths observed in these resources

- `contacts/frank`
- `contacts/frank/mq041_gps_message/00_stash_location`
- `contacts/frank/mq041_rejected_holocall/mq041_01_msg_evidence`
- `contacts/frank/mq041_rejected_holocall/mq041_02_msg_stash`
- `quests/minor_quest/mq041_corpo`
- `quests/minor_quest/mq041_corpo/corpo/01_find_the_briefcase`
- `quests/minor_quest/mq041_corpo/corpo/01_find_the_briefcase/description`
- `quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny`
- `quests/minor_quest/mq041_corpo/corpo/01a_talk_with_johnny1`
- `quests/minor_quest/mq041_corpo/corpo/01b_lift_the_dumpster`
- `quests/minor_quest/mq041_corpo/corpo/02_open_the_briefcase`
- `quests/minor_quest/mq041_corpo/corpo/03_talk_with_stranger`
- `quests/minor_quest/mq041_corpo/corpo/04_confront_frank`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 2 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 1 |
| `questCheckpointNodeDefinition` | 3 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterEquippedItem_ConditionType]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 6 |
| `questConditionNodeDefinition[questLifePath_ConditionType,questStatsCondition,questUniversalRef]` | 1 |
| `questConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 7 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 2 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 22 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 1 |
| `questInputNodeDefinition` | 19 |
| `questInteractiveObjectManagerNodeDefinition[questSetInteractionState_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 21 |
| `questLogicalHubNodeDefinition` | 6 |
| `questLogicalXorNodeDefinition` | 1 |
| `questLookAtDrivenTurnsNode` | 2 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 1 |
| `questOutputNodeDefinition` | 14 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterAttack_ConditionType,questCharacterCombat_ConditionType,questCharacterCondition,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType]` | 2 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questPhaseNodeDefinition` | 15 |
| `questPhoneManagerNodeDefinition[questAddRemoveContact_NodeType,questChangeContactList_NodeTypeParams]` | 2 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questPlayerLookAt_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 10 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 2 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 11 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 3 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 2 |
| `scnCutControlNode[scnNodeId]` | 5 |
| `scnDeletionMarkerNode[scnNodeId]` | 8 |
| `scnEndNode[scnNodeId]` | 4 |
| `scnHubNode[scnNodeId]` | 8 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 32 |
| `scnStartNode[scnNodeId]` | 6 |
| `scnXorNode[scnNodeId]` | 5 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `595b0a81e7a7db25430f` | 10 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 906 -> 240 -> 14 |
| `344b844804fd00c676f9` | 6 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 212 -> 966 -> 370 |
| `214bea9fe83b5e6c655e` | 5 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 1373 -> 1028 -> 966 |
| `15d020c80d0d34bb7e54` | 4 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 7 -> 812 -> 147 |
| `27faccd7b30abbc3add2` | 4 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 147 -> 168 -> 171 |
| `2e0a7d7db4cf1ad4fa9a` | 4 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 995 -> 1028 -> 1034 |
| `3696c80562aaec4afbf0` | 4 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 1373 -> 1028 -> 1034 |
| `38a1dbab49b6c9dbf766` | 4 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 1373 -> 1028 -> 1036 |
| `c1b6601d2f647c8a694d` | 4 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 147 -> 168 -> 178 |
| `cc11ee29c780d7d6ad07` | 4 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 1363 -> 1373 -> 1028 |
| `defcf9c06eefcf06bd1e` | 4 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 812 -> 147 -> 168 |
| `17145157f28879f860a0` | 3 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 812 -> 168 -> 171 |
| `24fa8e338241218dd7e2` | 3 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 197 -> 1171 -> 1107 |
| `6bb4b9d408a519eb6376` | 3 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 1363 -> 1373 -> 1377 |
| `7e7dbbc930b3717fd790` | 3 | `base\quest\minor_quests\mq041\phases\mq041_corpo_01_hook.questphase` / h0 / 14 -> 16 -> 5 |
| `942a5f8cec8f69fd2c36` | 3 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 812 -> 168 -> 178 |
| `c11cf4b8fc2f0bbc6f96` | 3 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 240 -> 182 -> 1174 |
| `e5742f9794e6583c67cb` | 3 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_01_deadmans_switch.scene` / scene / 78 -> 264 -> 262 |
| `f6a7b2a76883b53af00c` | 3 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 240 -> 14 -> 1218 |
| `f9fe85ea1049740d0c2c` | 3 | `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene` / scene / 12 -> 14 -> 1218 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
