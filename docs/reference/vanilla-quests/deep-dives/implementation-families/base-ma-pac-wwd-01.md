# base-ma-pac-wwd-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\community\ma_pac_wwd_01_civ.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\community\ma_pac_wwd_01_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/pacifica/west_wind_estate/ma_pac_wwd_01/onscreens/ma_pac_wwd_01_onscreen_01`
- `points_of_interest/minor_activities/ma_pac_wwd_01`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAnimset]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 3 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalHubNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 6 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h0 / 8 -> 57 -> 24 |
| `42d456f68cbe3d8345c3` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h0 / 47 -> 49 -> 50 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h0 / 68 -> 65 -> 64 |
| `0985fc78e580f2f10e14` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h314 / 2 -> 35 -> 37 |
| `0f374ac8f753ecdc05b1` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h0 / 5 -> 46 -> 55 |
| `1121a7f146103492ac60` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h0 / 66 -> 64 -> 16 |
| `12208b60f11caf6d936e` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h0 / 21 -> 61 -> 28 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h0 / 62 -> 34 -> 30 |
| `1972a0532f20a107c8bb` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h0 / 0 -> 1 -> 4 |
| `1b89a735937e920c2637` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h0 / 30 -> 31 -> 35 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h0 / 5 -> 8 -> 57 |
| `1f22b00cd5f6b14c601a` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h254 / 7 -> 2 -> 3 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h0 / 8 -> 57 -> 17 |
| `2be2aaaa8bc7f9d40730` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h254 / 0 -> 2 -> 3 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h0 / 68 -> 67 -> 64 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h0 / 18 -> 68 -> 67 |
| `390f62c11ddf01069a3f` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h0 / 5 -> 40 -> 59 |
| `423e38da0596af6a3004` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h314 / 35 -> 37 -> 8 |
| `427ec60a2eca262e4afc` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h0 / 46 -> 55 -> 47 |
| `482db244d84233ced474` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_01\ma_pac_wwd_01_phase.questphase` / h0 / 55 -> 47 -> 49 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
