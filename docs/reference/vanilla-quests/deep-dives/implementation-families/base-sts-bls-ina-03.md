# base-sts-bls-ina-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\communities\sts_bls_ina_03_comm.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\communities\sts_bls_ina_03_reinforcements.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_gpl.questphase; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_ow.questphase |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_bugfixing.questphase` | repair | 2 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_gpl.questphase` | content candidate | 17 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_guards_chats_oneliners.scene |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_ow.questphase` | content candidate | 7 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_debriefs.scene; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_prebrief.scene; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_interactions.scene |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_guards_chats_oneliners.scene` | content candidate | 0 / 10 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_debriefs.scene` | content candidate | 0 / 25 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_interactions.scene` | content candidate | 0 / 16 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\sts_bls_ina_03.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\sts_bls_ina_03.quest` | content candidate | 1 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\sts_bls_ina_03_testing.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/dakota_smith/sts_bls_ina_03/brief`
- `contacts/dakota_smith/sts_bls_ina_03/sts_bls_ina_03_debrief`
- `contacts/dakota_smith/sts_bls_ina_03/sts_bls_ina_03_debrief_shortcut`
- `points_of_interest/street_stories/sts_bls_ina_03`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/ina_03_brief`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/destroy_antenna`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/find_antenna`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/find_source_of_transmission`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/go_to_the_signal_destination`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/leave_the_outpost`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_03/sts_bls_ina_03/missing_drones`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_RestrictMovementToArea]` | 2 |
| `questConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCutControlNodeDefinition` | 4 |
| `questDeletionMarkerNodeDefinition` | 11 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerSetAttachment_NodeType,questEntityManagerSetAttachment_ToActor]` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 1 |
| `questEventManagerNodeDefinition` | 9 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 40 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 27 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 30 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 5 |
| `questMiscAICommandNode` | 12 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 6 |
| `questOutputNodeDefinition` | 12 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questDevice_ConditionType,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 13 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterWorkspot_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 21 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 13 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckSpeakerDistractedInterruptCondition]` | 2 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 17 |
| `questPhaseNodeDefinition` | 26 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 14 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 4 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVehicleNodeDefinition[questUnassignAll_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 14 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 8 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 9 |
| `scnStartNode[scnNodeId]` | 6 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | 9 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_gpl.questphase` / h821 / 0 -> 12 -> 13 |
| `138cff49923a75e07348` | 5 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_bugfixing.questphase` / h19 / 9 -> 11 -> 10 |
| `973ca27146dd9c8eee04` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_gpl.questphase` / h511 / 5 -> 7 -> 51 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_debriefs.scene` / scene / 272 -> 263 -> 251 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_debriefs.scene` / scene / 151 -> 152 -> 148 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_debriefs.scene` / scene / 156 -> 151 -> 152 |
| `e85b4a6da2c88320c53a` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_gpl.questphase` / h511 / 23 -> 25 -> 5 |
| `101b60945ddf6f25f378` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_debriefs.scene` / scene / 26 -> 154 -> 156 |
| `3f08205082c0c7c632d2` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_bugfixing.questphase` / h19 / 11 -> 10 -> 5 |
| `a53561b4c002bc02b58a` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_bugfixing.questphase` / h19 / 6 -> 9 -> 11 |
| `01ce2408a018a8c31b56` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_bugfixing.questphase` / h19 / 3 -> 12 -> 4 |
| `050c4356d65d551d20d2` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_ow.questphase` / h0 / 3 -> 12 -> 4 |
| `057faf6705431d5dcd46` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_gpl.questphase` / h511 / 25 -> 5 -> 7 |
| `0fdad4c8a8b4964c866f` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_interactions.scene` / scene / 116 -> 153 -> 122 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_debriefs.scene` / scene / 263 -> 150 -> 153 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_debriefs.scene` / scene / 272 -> 263 -> 150 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_prebrief.scene` / scene / 276 -> 271 -> 285 |
| `1666d7526b9bab74f2e2` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_ow.questphase` / h263 / 144 -> 80 -> 74 |
| `1d933adb5a617880c93e` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\scenes\sts_bls_ina_03_holocall_debriefs.scene` / scene / 154 -> 156 -> 151 |
| `1fb1217b6d69ef2494f3` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_03\phases\sts_bls_ina_03_gpl.questphase` / h511 / 32 -> 31 -> 38 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
