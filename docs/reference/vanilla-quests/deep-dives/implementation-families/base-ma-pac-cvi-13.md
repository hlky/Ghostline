# base-ma-pac-cvi-13

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\community\ma_pac_cvi_13_civilians_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\community\ma_pac_cvi_13_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_phase.questphase |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_bugfixing.questphase` | repair | 4 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/pacifica/coastview/ma_pac_cvi_13/onscreens/ma_pac_cvi_13b`
- `onscreens/emails/quests/minor_activities/pacifica/coastview/ma_pac_cvi_13/onscreens/ma_pac_cvi_13c`
- `points_of_interest/minor_activities/ma_pac_cvi_13`
- `quests/minor_activities/pacifica/coastview/ma_pac_cvi_13`
- `quests/minor_activities/pacifica/coastview/ma_pac_cvi_13/description`
- `quests/minor_activities/pacifica/coastview/ma_pac_cvi_13/ma_pac_cvi_13`
- `quests/minor_activities/pacifica/coastview/ma_pac_cvi_13/ma_pac_cvi_13/go_to_spot`
- `quests/minor_activities/pacifica/coastview/ma_pac_cvi_13/ma_pac_cvi_13/loot`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 2 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 8 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questInputNodeDefinition` | 8 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 7 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 8 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 8 |
| `questPhaseNodeDefinition` | 4 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 10 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 7 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 7 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `00c3ca0ac0b55db639ca` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_bugfixing.questphase` / h14 / 3 -> 4 -> 5 |
| `18be198845c90c6bb3c8` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_bugfixing.questphase` / h14 / 2 -> 3 -> 4 |
| `23076dbee17c77d6df80` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_bugfixing.questphase` / h14 / 7 -> 8 -> 9 |
| `5074a0e1034ad00fc9b6` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_bugfixing.questphase` / h14 / 6 -> 7 -> 8 |
| `94131c7d0e515be284ef` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_bugfixing.questphase` / h14 / 5 -> 6 -> 7 |
| `abe697defbff91d17846` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_bugfixing.questphase` / h14 / 4 -> 5 -> 6 |
| `05204279a5fdb15c9ce0` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_phase.questphase` / h0 / 69 -> 72 -> 71 |
| `2e1ee5a1324dbeeb9071` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_phase.questphase` / h0 / 34 -> 48 -> 36 |
| `334d3d5e9292145cac5a` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_bugfixing.questphase` / h14 / 8 -> 9 -> 1 |
| `b90715b67cb6f4596277` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_phase.questphase` / h0 / 75 -> 65 -> 67 |
| `d151faf9532075d537c4` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_phase.questphase` / h0 / 11 -> 12 -> 70 |
| `e859ab97f2b647e1afc2` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_bugfixing.questphase` / h105 / 20 -> 22 -> 18 |
| `eaf5aab427d50e5598b6` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_bugfixing.questphase` / h14 / 0 -> 11 -> 12 |
| `f3a269b6a97862bc211c` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_phase.questphase` / h0 / 48 -> 75 -> 65 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_phase.questphase` / h0 / 13 -> 14 -> 124 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_phase.questphase` / h0 / 124 -> 121 -> 120 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_phase.questphase` / h0 / 62 -> 83 -> 63 |
| `0a334602586a3645f219` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_phase.questphase` / h0 / 46 -> 42 -> 118 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_phase.questphase` / h0 / 11 -> 12 -> 13 |
| `178ff9eba50354aed786` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_13\ma_pac_cvi_13_phase.questphase` / h0 / 0 -> 34 -> 48 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
