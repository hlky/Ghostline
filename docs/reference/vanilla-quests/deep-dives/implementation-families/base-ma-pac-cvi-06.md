# base-ma-pac-cvi-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_06\community\ma_pac_cvi_06_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_06\ma_pac_cvi_06.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_06\ma_pac_cvi_06.quest` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_06\ma_pac_cvi_06_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questInputNodeDefinition` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `049529aa809ef7fccdf5` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_06\ma_pac_cvi_06_phase.questphase` / h0 / 6 -> 5 -> 1 |
| `096aaeff70ca3d46fc79` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_06\ma_pac_cvi_06_phase.questphase` / h0 / 0 -> 2 -> 3 |
| `56c86f6019570401f9c3` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_06\ma_pac_cvi_06_phase.questphase` / h0 / 2 -> 3 -> 4 |
| `8108ae2577e14333aa03` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_06\ma_pac_cvi_06_phase.questphase` / h0 / 4 -> 6 -> 5 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
