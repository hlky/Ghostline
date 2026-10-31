# base-sts-wbr-hil-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\community\sts_wbr_hil_01.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\community\sts_wbr_hil_01_crowd.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\community\sts_wbr_hil_01_drone.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\community\sts_wbr_hil_01_enemies.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_bugfixing.questphase` | repair | 2 / 0 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_gameplay.questphase` | content candidate | 6 / 0 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase` | content candidate | 6 / 0 | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_chats.scene; base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene; base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_prebrief.scene |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_prestate_control.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_chats.scene` | content candidate | 0 / 8 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` | content candidate | 0 / 28 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\sts_wbr_hil_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\sts_wbr_hil_01.quest` | content candidate | 1 / 0 | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\sts_wbr_hil_01.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\sts_wbr_hil_01.questphase` | content candidate | 3 / 0 | base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_gameplay.questphase; base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase |
| `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\sts_wbr_hil_01_test.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/wakako_okada/sts_wbr_hil_01/brief`
- `contacts/wakako_okada/sts_wbr_hil_01/sts_wbr_hil_01_debrief_non_optional`
- `contacts/wakako_okada/sts_wbr_hil_01/sts_wbr_hil_01_debrief_optional`
- `points_of_interest/street_stories/sts_wbr_hil_01`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/brief`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/be_unseen`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/drop_point`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/escape`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/find`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_councilman_apartment`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_the_top_floor`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/go_to_the_top_floor/elevator`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/take_dps`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 3 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 6 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 1 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 25 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 18 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 5 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 18 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMappinManagerNodeDefinition` | 1 |
| `questMiscAICommandNode[questConstAICommandParams]` | 2 |
| `questOutputNodeDefinition` | 14 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questJournalCondition,questJournalEntry_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckSpeakerDistractedInterruptCondition]` | 2 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 11 |
| `questPhaseNodeDefinition` | 15 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 4 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 8 |
| `questSpawnManagerNodeDefinition[questLegacy_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 2 |
| `scnAndNode[scnNodeId]` | 2 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 7 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 5 |
| `scnStartNode[scnNodeId]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `4e9253a72e6b0134b8dd` | 4 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase` / h314 / 4 -> 49 -> 50 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` / scene / 270 -> 251 -> 249 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` / scene / 87 -> 282 -> 284 |
| `101b60945ddf6f25f378` | 3 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` / scene / 4 -> 86 -> 88 |
| `138cff49923a75e07348` | 3 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase` / h314 / 58 -> 111 -> 59 |
| `3c633c569c15c58dface` | 3 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_gameplay.questphase` / h216 / 0 -> 8 -> 11 |
| `a53561b4c002bc02b58a` | 3 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase` / h314 / 49 -> 50 -> 51 |
| `cd34f2d7c778c6de817e` | 3 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_gameplay.questphase` / h0 / 8 -> 15 -> 9 |
| `d6b7c21f5d2d0ab76fc6` | 3 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` / scene / 282 -> 284 -> 286 |
| `dc8d831ea1b2cdd0082f` | 3 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_gameplay.questphase` / h125 / 29 -> 21 -> 32 |
| `ea22cdac549a6b98a384` | 3 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_gameplay.questphase` / h0 / 14 -> 15 -> 9 |
| `0a31874be03936c47839` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_gameplay.questphase` / h55 / 17 -> 16 -> 14 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` / scene / 251 -> 82 -> 85 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` / scene / 270 -> 251 -> 82 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_prebrief.scene` / scene / 269 -> 273 -> 279 |
| `1d933adb5a617880c93e` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` / scene / 86 -> 88 -> 83 |
| `2beeeaa3b4da5300c035` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` / scene / 1 -> 280 -> 87 |
| `2e362801d31d08a7d108` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene` / scene / 87 -> 81 -> 270 |
| `31b75f883364baef9ba2` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_open_world.questphase` / h122 / 14 -> 30 -> 28 |
| `3921c08e7ed6f9432943` | 2 | `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\phases\sts_wbr_hil_01_gameplay.questphase` / h55 / 12 -> 16 -> 14 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
