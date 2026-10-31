# base-ma-pac-wwd-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\community\ma_pac_wwd_04_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/pacifica/west_wind_estate/ma_pac_wwd_04/onscreens/ma_pac_wwd_04_onscreen_01`
- `points_of_interest/minor_activities/ma_pac_wwd_04`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 2 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 27 -> 50 -> 26 |
| `95b7458b3ffd83fd4357` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 2 -> 40 -> 41 |
| `987122e5e2fcd167cf6c` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 0 -> 2 -> 40 |
| `a5f6ff0df46f7043f2b5` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 31 -> 32 -> 33 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 61 -> 58 -> 57 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 58 -> 57 -> 27 |
| `1196b65ec43cf9530eeb` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 53 -> 52 -> 46 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 57 -> 27 -> 50 |
| `165a19c1a8ba322a760c` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 52 -> 47 -> 49 |
| `1972a0532f20a107c8bb` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 2 -> 4 -> 6 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 0 -> 10 -> 51 |
| `20038f2b4710db214521` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 56 -> 55 -> 53 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 10 -> 51 -> 19 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 61 -> 60 -> 57 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 21 -> 61 -> 60 |
| `33b4775a6eb91bbc86ae` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 53 -> 52 -> 47 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 58 -> 57 -> 8 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 59 -> 57 -> 27 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 60 -> 57 -> 27 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_04\ma_pac_wwd_04.questphase` / h0 / 51 -> 25 -> 19 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
