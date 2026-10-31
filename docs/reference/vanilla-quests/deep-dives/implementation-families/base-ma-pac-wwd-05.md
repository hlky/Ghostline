# base-ma-pac-wwd-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\community\ma_pac_wwd_05_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/pacifica/west_wind_estate/ma_pac_wwd_05/onscreens/ma_pac_wwd_05_onscreen_01`
- `points_of_interest/minor_activities/ma_pac_wwd_05`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 2 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questUniversalRef,questUseWeapon_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 9 -> 50 -> 24 |
| `23fbe7a2f1484acd744d` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h105 / 0 -> 5 -> 1 |
| `02d878a28a675e881f96` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 57 -> 55 -> 18 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 59 -> 56 -> 55 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 56 -> 55 -> 26 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 55 -> 26 -> 51 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 53 -> 39 -> 41 |
| `1972a0532f20a107c8bb` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 12 -> 13 -> 15 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 5 -> 9 -> 50 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 9 -> 50 -> 19 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 59 -> 58 -> 55 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 21 -> 59 -> 58 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 57 -> 55 -> 26 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 58 -> 55 -> 26 |
| `45a0059a97ab5b10fb49` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 56 -> 55 -> 18 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 50 -> 24 -> 19 |
| `4db7f0bc4734094d50f6` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 42 -> 43 -> 49 |
| `4f08b4a4d51559d06963` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 43 -> 49 -> 6 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 50 -> 19 -> 21 |
| `598920ee48558917ab4e` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_05\ma_pac_wwd_05_phase.questphase` / h0 / 24 -> 19 -> 21 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
