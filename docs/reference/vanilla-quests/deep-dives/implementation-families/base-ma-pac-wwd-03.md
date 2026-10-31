# base-ma-pac-wwd-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_03\community\ma_pac_wwd_03_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_03\ma_pac_wwd_03.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_03\ma_pac_wwd_03.quest` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_03\ma_pac_wwd_03_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_03\ma_pac_wwd_03_phase.questphase` / h0 / 34 -> 35 -> 33 |
| `3a03f7cc1e66c1cd23f5` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_03\ma_pac_wwd_03_phase.questphase` / h0 / 32 -> 27 -> 13 |
| `4046f7e0ed1087267da3` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_03\ma_pac_wwd_03_phase.questphase` / h0 / 15 -> 24 -> 18 |
| `48332a9e831fe7284d87` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_03\ma_pac_wwd_03_phase.questphase` / h0 / 28 -> 32 -> 27 |
| `71892f49b88f7b8bb8be` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_03\ma_pac_wwd_03_phase.questphase` / h0 / 12 -> 15 -> 24 |
| `a3e5f861a4b71433135a` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_03\ma_pac_wwd_03_phase.questphase` / h0 / 36 -> 28 -> 32 |
| `a9350e05126ec08a441f` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_03\ma_pac_wwd_03_phase.questphase` / h0 / 24 -> 18 -> 34 |
| `de85a1a08a5312334d23` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_03\ma_pac_wwd_03_phase.questphase` / h0 / 24 -> 18 -> 37 |
| `f66cfde7fa1a88e1f4a1` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_03\ma_pac_wwd_03_phase.questphase` / h0 / 18 -> 37 -> 36 |
| `fee3756653cd083fb28e` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_03\ma_pac_wwd_03_phase.questphase` / h0 / 37 -> 36 -> 28 |
| `ff4c8a828496c45d7dfa` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_03\ma_pac_wwd_03_phase.questphase` / h0 / 18 -> 34 -> 35 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
