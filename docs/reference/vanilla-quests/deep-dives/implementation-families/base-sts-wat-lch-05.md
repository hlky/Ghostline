# base-sts-wat-lch-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\communities\sts_wat_lch_05_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\communities\sts_wat_lch_05_enemies.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_bugfixing.questphase` | repair | 7 / 0 | base\open_world\vendors\watson\little_china\wat_lch_foodshop_02\wat_lch_foodshop_02.scene |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_combat.questphase` | content candidate | 3 / 0 | base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_chats.scene |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_openworld.questphase` | content candidate | 11 / 0 | base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_holocall_debrief.scene; base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_holocall_prebrief.scene; base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_johnny.scene |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_phase.questphase` | content candidate | 3 / 0 | base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_combat.questphase; base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_openworld.questphase |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_chats.scene` | content candidate | 0 / 9 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_holocall_debrief.scene` | content candidate | 0 / 25 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_johnny.scene` | content candidate | 0 / 21 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\sts_wat_lch_05_def.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\sts_wat_lch_05_quest.quest` | content candidate | 2 / 0 | base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_phase.questphase; base\open_world\vendors\open_world_vendors.questphase |
| `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\sts_wat_lch_05_test_def.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/sts_wat_lch_05/sts_wat_lch_05_brief`
- `contacts/regina_jones/sts_wat_lch_05/sts_wat_lch_05_holocall_debrief_perfect`
- `points_of_interest/service_points/wat_lch_foodshop_02`
- `points_of_interest/street_stories/sts_wat_lch_05`
- `quests/street_stories/watson/little_china/sts_wat_lch_05`
- `quests/street_stories/watson/little_china/sts_wat_lch_05/brief`
- `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/blackmaill`
- `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/card`
- `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/card/card`
- `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/card/card_bar`
- `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/exit`
- `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/exit/mappin`
- `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/exit/mappin_door`
- `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/find`
- `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/inside`
- `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/main`
- `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/retrive`
- `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/retrive/eye`
- `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/retrive/storage`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 14 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 19 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 11 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 36 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 25 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 8 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 3 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 35 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMappinManagerNodeDefinition` | 8 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 27 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterEquippedItem_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 20 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 9 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 7 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckSpeakerDistractedInterruptCondition]` | 2 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 12 |
| `questPhaseNodeDefinition` | 21 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 6 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 7 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 7 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 9 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 10 |
| `scnStartNode[scnNodeId]` | 7 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `d02998377761430f97de` | 6 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_openworld.questphase` / h103 / 61 -> 60 -> 87 |
| `2f4379965793117f7fa5` | 5 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_openworld.questphase` / h103 / 0 -> 248 -> 250 |
| `eaf5aab427d50e5598b6` | 5 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_bugfixing.questphase` / h89 / 0 -> 2 -> 3 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_holocall_debrief.scene` / scene / 263 -> 261 -> 249 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_holocall_debrief.scene` / scene / 286 -> 284 -> 288 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_holocall_debrief.scene` / scene / 77 -> 286 -> 284 |
| `101b60945ddf6f25f378` | 3 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_holocall_debrief.scene` / scene / 26 -> 76 -> 78 |
| `4803de0710dd8d0fcd3d` | 3 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_openworld.questphase` / h103 / 84 -> 60 -> 87 |
| `63cee9fca976b72a4a86` | 3 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_openworld.questphase` / h103 / 61 -> 60 -> 87 |
| `8cd3b647ae3f592ad947` | 3 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_chats.scene` / scene / 1 -> 4 -> 2 |
| `f87a090eb1f6936cdc0d` | 3 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_openworld.questphase` / h103 / 111 -> 60 -> 87 |
| `0b0d9dd210bf43f799ea` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_openworld.questphase` / h103 / 61 -> 60 -> 187 |
| `0bc8f68e59c0b883af0d` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_openworld.questphase` / h103 / 236 -> 192 -> 204 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_holocall_debrief.scene` / scene / 261 -> 72 -> 75 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_holocall_debrief.scene` / scene / 263 -> 261 -> 72 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_holocall_prebrief.scene` / scene / 270 -> 273 -> 279 |
| `167f1346eaf4e836b648` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_openworld.questphase` / h1255 / 22 -> 19 -> 3 |
| `1a9b8893087e174a603f` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_openworld.questphase` / h233 / 4 -> 6 -> 7 |
| `1d933adb5a617880c93e` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\scenes\sts_wat_lch_05_holocall_debrief.scene` / scene / 76 -> 78 -> 73 |
| `22adbd10519df5772f7c` | 2 | `base\open_world\street_stories\watson\little_china\sts_wat_lch_05\phases\sts_wat_lch_05_openworld.questphase` / h103 / 236 -> 192 -> 205 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
