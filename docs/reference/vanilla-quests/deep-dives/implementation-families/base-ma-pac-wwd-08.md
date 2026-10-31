# base-ma-pac-wwd-08

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\community\ma_pac_wwd_08_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/pacifica/west_wind_estate/ma_pac_wwd_08/onscreens/ma_pac_wwd_08_onscreen_01`
- `points_of_interest/minor_activities/ma_pac_wwd_08`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
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
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 9 -> 34 -> 20 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 43 -> 40 -> 39 |
| `0b81e5206696faa510d4` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 27 -> 26 -> 23 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 40 -> 39 -> 22 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 39 -> 22 -> 35 |
| `1972a0532f20a107c8bb` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 2 -> 3 -> 5 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 0 -> 9 -> 34 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 9 -> 34 -> 16 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 43 -> 42 -> 39 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 18 -> 43 -> 42 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 40 -> 39 -> 7 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 41 -> 39 -> 22 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 42 -> 39 -> 22 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 34 -> 20 -> 16 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 34 -> 16 -> 18 |
| `52e256c57c21a40b4b08` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 10 -> 31 -> 32 |
| `598920ee48558917ab4e` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 20 -> 16 -> 18 |
| `6b3e5fe15b7a64a01e21` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 16 -> 18 -> 43 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 43 -> 41 -> 39 |
| `768cb6020e6fbe0d0198` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_08\ma_pac_wwd_08_phase.questphase` / h0 / 0 -> 10 -> 31 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
