# base-sts-wat-lch-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\community\sts_wat_lch_06_com_combat.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\community\sts_wat_lch_06_com_junkie.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\community\sts_wat_lch_06_com_reinforcements.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_combat.questphase; base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_ow.questphase |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_bugfixing.questphase` | repair | 4 / 0 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_combat.questphase` | content candidate | 6 / 0 | base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_chats.scene |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_openworld.questphase` | content candidate | 4 / 0 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_ow.questphase` | content candidate | 5 / 0 | base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene; base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_prebrief.scene |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_chats.scene` | content candidate | 0 / 13 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` | content candidate | 0 / 23 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\sts_wat_lch_06.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\sts_wat_lch_06.quest` | content candidate | 1 / 0 | base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06.questphase; base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_bugfixing.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\sts_wat_lch_06_test_def.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/sts_wat_lch_06/brief`
- `contacts/regina_jones/sts_wat_lch_06/sts_wat_lch_06_debrief`
- `points_of_interest/street_stories/sts_wat_lch_06`
- `quests/street_stories/watson/little_china/sts_wat_lch_06`
- `quests/street_stories/watson/little_china/sts_wat_lch_06/brief`
- `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_lab`
- `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line`
- `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line/main_room_mappin`
- `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line/mappin_1`
- `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/destroy_production_line/mappin_2`
- `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_basement`
- `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/enter_building`
- `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_out`
- `quests/street_stories/watson/little_china/sts_wat_lch_06/sts_wat_lch_06/get_to_the_main_room`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 4 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 13 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerSetMeshAppearance_NodeType,questEntityManagerSetMeshAppearance_NodeTypeParams]` | 32 |
| `questEventManagerNodeDefinition` | 13 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 31 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 5 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 20 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 17 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 26 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 4 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMappinManagerNodeDefinition` | 6 |
| `questMiscAICommandNode` | 3 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 16 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 2 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 9 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckSpeakerDistractedInterruptCondition]` | 3 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 16 |
| `questPhaseNodeDefinition` | 17 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 11 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 7 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 7 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 5 |
| `scnStartNode[scnNodeId]` | 5 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `68e756d35dc6cceaf74c` | 30 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_ow.questphase` / h427 / 27 -> 29 -> 30 |
| `138cff49923a75e07348` | 5 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_openworld.questphase` / h30 / 18 -> 19 -> 20 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` / scene / 249 -> 272 -> 252 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` / scene / 283 -> 281 -> 285 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` / scene / 61 -> 283 -> 281 |
| `a53561b4c002bc02b58a` | 3 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_openworld.questphase` / h30 / 31 -> 18 -> 19 |
| `bfe95df47bd1ca67330f` | 3 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_ow.questphase` / h427 / 2 -> 60 -> 61 |
| `012d43d45e5730bb5502` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_combat.questphase` / h250 / 12 -> 4 -> 5 |
| `101b60945ddf6f25f378` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` / scene / 26 -> 67 -> 68 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` / scene / 272 -> 59 -> 60 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` / scene / 249 -> 272 -> 59 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_prebrief.scene` / scene / 270 -> 273 -> 279 |
| `1666d7526b9bab74f2e2` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_openworld.questphase` / h30 / 29 -> 7 -> 12 |
| `1d933adb5a617880c93e` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` / scene / 67 -> 68 -> 65 |
| `26762f051e7728f090ca` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` / scene / 59 -> 60 -> 26 |
| `2beeeaa3b4da5300c035` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` / scene / 1 -> 279 -> 61 |
| `2e362801d31d08a7d108` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_holocall_debrief.scene` / scene / 61 -> 58 -> 249 |
| `3b70bb506b872cadfa43` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\scenes\sts_wat_lch_06_chats.scene` / scene / 9 -> 61 -> 10 |
| `3f08205082c0c7c632d2` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_openworld.questphase` / h30 / 19 -> 20 -> 21 |
| `3fe0ae98a8cf5496b004` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_06\phases\sts_wat_lch_06_ow.questphase` / h76 / 72 -> 74 -> 73 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
