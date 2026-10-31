# base-ma-wbr-jpn-09

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` | content candidate | 4 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/japantown/ma_wbr_jpn_09/shards/ma_wbr_jpn_09_a`
- `points_of_interest/minor_activities/ma_wbr_jpn_09`
- `quests/minor_activities/westbrook/japantown/ma_wbr_jpn_09`
- `quests/minor_activities/westbrook/japantown/ma_wbr_jpn_09/description`
- `quests/minor_activities/westbrook/japantown/ma_wbr_jpn_09/ma_wbr_jpn_09/go_to_spot`
- `quests/minor_activities/westbrook/japantown/ma_wbr_jpn_09/ma_wbr_jpn_09/loot`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 4 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 6 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h118 / 4 -> 5 -> 34 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h12 / 6 -> 42 -> 35 |
| `0d59d5b737ce1451c32f` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h118 / 35 -> 31 -> 33 |
| `196b529f62a329051bb7` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h12 / 11 -> 37 -> 21 |
| `1d48bd7cbbaeca8257d2` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h118 / 7 -> 8 -> 19 |
| `204ca9b8b94427c1ef81` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h118 / 27 -> 26 -> 21 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h12 / 6 -> 42 -> 30 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h118 / 34 -> 32 -> 33 |
| `338f839dd144ddebb804` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h209 / 5 -> 6 -> 7 |
| `3aefa7c126d38984e7c5` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h209 / 10 -> 11 -> 5 |
| `45384fad45d3768a409d` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h118 / 31 -> 33 -> 7 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h12 / 42 -> 35 -> 30 |
| `4e9253a72e6b0134b8dd` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h118 / 3 -> 4 -> 5 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h12 / 42 -> 30 -> 31 |
| `517731173927286d20cf` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h118 / 30 -> 29 -> 34 |
| `536dc1d981889e57ea60` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h118 / 34 -> 35 -> 31 |
| `53b397a39cc3f9c63a42` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h118 / 33 -> 7 -> 8 |
| `57acaa7093fc730a69e8` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h12 / 38 -> 6 -> 42 |
| `598920ee48558917ab4e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h12 / 35 -> 30 -> 31 |
| `677d9ef47a99b30a40f7` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_09\ma_wbr_jpn_09_phase.questphase` / h209 / 0 -> 2 -> 10 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
