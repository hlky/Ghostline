# base-ma-wat-lch-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\community\ma_wat_lch_05_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\community\ma_wat_lch_05_enemies_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/little_china/ma_wat_lch_05/onscreens/ma_wat_lch_05_2`
- `points_of_interest/minor_activities/ma_wat_lch_05`
- `quests/minor_activities/watson/little_china/ma_wat_lch_05`
- `quests/minor_activities/watson/little_china/ma_wat_lch_05/description`
- `quests/minor_activities/watson/little_china/ma_wat_lch_05/ma_wat_lch_03/go_to_spot`
- `quests/minor_activities/watson/little_china/ma_wat_lch_05/ma_wat_lch_03/loot`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 6 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 10 -> 57 -> 36 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 23 -> 24 -> 63 |
| `0d59d5b737ce1451c32f` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 65 -> 60 -> 59 |
| `1258cee37e98f0ae14fe` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 29 -> 33 -> 37 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 21 -> 22 -> 23 |
| `13e54cc7d319bbafaa58` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 32 -> 34 -> 42 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h188 / 4 -> 3 -> 6 |
| `191018f411bf7782f315` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 47 -> 21 -> 22 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 2 -> 10 -> 57 |
| `1d48bd7cbbaeca8257d2` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 25 -> 27 -> 30 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 10 -> 57 -> 32 |
| `2994474f402dacd934b6` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 34 -> 42 -> 44 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 63 -> 62 -> 59 |
| `34df85d6acec759ba07d` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 42 -> 44 -> 52 |
| `45384fad45d3768a409d` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 60 -> 59 -> 25 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 57 -> 36 -> 32 |
| `4e9253a72e6b0134b8dd` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 22 -> 23 -> 24 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 57 -> 32 -> 34 |
| `536dc1d981889e57ea60` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 63 -> 65 -> 60 |
| `53b397a39cc3f9c63a42` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_05\ma_wat_lch_05_phase.questphase` / h0 / 59 -> 25 -> 27 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
