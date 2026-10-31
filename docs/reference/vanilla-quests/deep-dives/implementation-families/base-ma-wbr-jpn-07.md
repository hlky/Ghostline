# base-ma-wbr-jpn-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\community\ma_wbr_jpn_07_agresive_junkies_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\community\ma_wbr_jpn_07_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\community\ma_wbr_jpn_07_junkie_den_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` | content candidate | 5 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/japantown/ma_wbr_jpn_07/shards/ma_wbr_jpn_07`
- `points_of_interest/minor_activities/ma_wbr_jpn_07`
- `quests/minor_activities/westbrook/japantown/ma_wbr_jpn_07`
- `quests/minor_activities/westbrook/japantown/ma_wbr_jpn_07/description`
- `quests/minor_activities/westbrook/japantown/ma_wbr_jpn_07/ma_wbr_jpn_07/go_to_spot`
- `quests/minor_activities/westbrook/japantown/ma_wbr_jpn_07/ma_wbr_jpn_07/loot`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 5 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 4 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 6 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 3 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 12 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `f802ad66d4ceea2d0aff` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h7 / 0 -> 51 -> 50 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h313 / 4 -> 5 -> 37 |
| `07a508d9181a1ec44ac6` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h313 / 23 -> 25 -> 21 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h7 / 6 -> 52 -> 29 |
| `0985fc78e580f2f10e14` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h176 / 31 -> 10 -> 9 |
| `0b81e5206696faa510d4` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h413 / 4 -> 7 -> 8 |
| `0d59d5b737ce1451c32f` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h313 / 39 -> 38 -> 36 |
| `0f660f7484731cdb671e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h7 / 52 -> 5 -> 23 |
| `16bd8181563a0ab4b081` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h413 / 7 -> 8 -> 11 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h7 / 0 -> 6 -> 52 |
| `23ae0d4630e5c2a0331c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h7 / 11 -> 21 -> 1 |
| `2c20201f171f754c99e0` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h7 / 59 -> 58 -> 55 |
| `2cb6a780f07f49d4270b` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h413 / 11 -> 12 -> 1 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h313 / 37 -> 35 -> 36 |
| `390f62c11ddf01069a3f` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h7 / 0 -> 2 -> 71 |
| `3ba86c71a70bfb0620a5` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h7 / 57 -> 59 -> 58 |
| `423e38da0596af6a3004` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h176 / 10 -> 9 -> 35 |
| `4365e94e7169e2520841` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h313 / 38 -> 36 -> 20 |
| `45384fad45d3768a409d` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h313 / 38 -> 36 -> 7 |
| `48b34908ac4ded0af324` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_07\ma_wbr_jpn_07_phase.questphase` / h313 / 35 -> 36 -> 20 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
