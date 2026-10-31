# base-ma-wat-kab-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\community\ma_wat_kab_05.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\community\ma_wat_kab_05_citizen_post_scavs.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\community\ma_wat_kab_05_citizen_post_stash.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\community\ma_wat_kab_05_stash.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `points_of_interest/minor_activities/ma_wat_kab_05`
- `quests/minor_activities/watson/kabuki/ma_wat_kab_05`
- `quests/minor_activities/watson/kabuki/ma_wat_kab_05/description`
- `quests/minor_activities/watson/kabuki/ma_wat_kab_05/ma_wat_kab_05/go_to_coordinates`
- `quests/minor_activities/watson/kabuki/ma_wat_kab_05/ma_wat_kab_05/loot_stash`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 7 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 8 -> 57 -> 42 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 20 -> 41 -> 63 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 11 -> 12 -> 69 |
| `0ccab9398bb1c40a915b` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 26 -> 5 -> 56 |
| `0d59d5b737ce1451c32f` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 70 -> 65 -> 64 |
| `1196b65ec43cf9530eeb` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 59 -> 60 -> 54 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 9 -> 10 -> 11 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 2 -> 8 -> 57 |
| `1d48bd7cbbaeca8257d2` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 14 -> 15 -> 27 |
| `20038f2b4710db214521` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 62 -> 61 -> 59 |
| `215ca95d939006973a7d` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 27 -> 28 -> 3 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 8 -> 57 -> 25 |
| `2d73eb28337ecf761033` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 25 -> 26 -> 5 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 69 -> 67 -> 64 |
| `45384fad45d3768a409d` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 65 -> 64 -> 14 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 57 -> 42 -> 25 |
| `4e9253a72e6b0134b8dd` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 10 -> 11 -> 12 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 57 -> 25 -> 26 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 19 -> 20 -> 41 |
| `536dc1d981889e57ea60` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_05\ma_wat_kab_05_phase.questphase` / h0 / 69 -> 70 -> 65 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
