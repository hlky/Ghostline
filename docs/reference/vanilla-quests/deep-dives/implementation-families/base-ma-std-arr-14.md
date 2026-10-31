# base-ma-std-arr-14

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\community\ma_std_arr_14_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` | content candidate | 2 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\phases\ma_std_arr_14_bugfixing.questphase` | repair | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_14/onscreens/ma_std_arr_14_onscreen_01`
- `onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_14/onscreens/ma_std_arr_14_onscreen_02`
- `points_of_interest/minor_activities/ma_std_arr_14`
- `quests/minor_activities/santo_domingo/arroyo/ma_std_arr_14`
- `quests/minor_activities/santo_domingo/arroyo/ma_std_arr_14/ma_description`
- `quests/minor_activities/santo_domingo/arroyo/ma_std_arr_14/ma_std_arr_14`
- `quests/minor_activities/santo_domingo/arroyo/ma_std_arr_14/ma_std_arr_14/go_to_stash`
- `quests/minor_activities/santo_domingo/arroyo/ma_std_arr_14/ma_std_arr_14/loot_stash`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questFlowControlNodeDefinition` | 14 |
| `questInputNodeDefinition` | 19 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 7 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 6 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 3 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 19 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `64ad97db21c46b588c28` | 14 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h295 / 0 -> 15 -> 14 |
| `968f9de9ccdf7f946240` | 14 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h295 / 9 -> 15 -> 14 |
| `9179341ec3ba560485b0` | 8 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h0 / 32 -> 35 -> 34 |
| `ad737ff35500b5119e6f` | 8 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h0 / 108 -> 109 -> 34 |
| `95b7458b3ffd83fd4357` | 6 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h0 / 32 -> 64 -> 65 |
| `503a9633d9e327e3e117` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h295 / 17 -> 16 -> 10 |
| `05fe886b74a86bbaffdc` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h0 / 82 -> 32 -> 64 |
| `6523fe5417a65b0d5102` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h0 / 123 -> 121 -> 33 |
| `ecef0279d0edfbe1b841` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h0 / 122 -> 123 -> 121 |
| `003ef4975a322c268ae8` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\phases\ma_std_arr_14_bugfixing.questphase` / h19 / 0 -> 2 -> 6 |
| `00c3ca0ac0b55db639ca` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h0 / 126 -> 127 -> 128 |
| `037c4f0a661789674d38` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h0 / 108 -> 109 -> 122 |
| `05e6009c4d1d8f802e1d` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h0 / 76 -> 17 -> 75 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h0 / 25 -> 29 -> 138 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h0 / 138 -> 135 -> 134 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h0 / 70 -> 77 -> 59 |
| `098d32cc0a2a324c8567` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h0 / 82 -> 80 -> 124 |
| `0c6d01edcbc5ca62695a` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\phases\ma_std_arr_14_bugfixing.questphase` / h19 / 30 -> 28 -> 27 |
| `0ea39c90296b8c8c526e` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h0 / 58 -> 17 -> 61 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_14\ma_std_arr_14_phase.questphase` / h0 / 23 -> 24 -> 25 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
