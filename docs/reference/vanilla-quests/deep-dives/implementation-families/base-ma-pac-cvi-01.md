# base-ma-pac-cvi-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\community\ma_pac_cvi_01_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01_phase.questphase |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEndNodeDefinition` | 1 |
| `questInputNodeDefinition` | 2 |
| `questLogicalAndNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01_phase.questphase` / h0 / 20 -> 21 -> 18 |
| `23171babf504911e54fc` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01_phase.questphase` / h0 / 0 -> 7 -> 6 |
| `2aa0f3a3b004f071652f` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01_phase.questphase` / h22 / 6 -> 7 -> 1 |
| `5f50b510abf7ccbb261c` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01_phase.questphase` / h0 / 21 -> 19 -> 13 |
| `8bc444681b5129cc73b0` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01_phase.questphase` / h0 / 20 -> 21 -> 19 |
| `90cf58434e79ce42af1e` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01_phase.questphase` / h22 / 0 -> 12 -> 10 |
| `a3e5f861a4b71433135a` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01_phase.questphase` / h22 / 10 -> 6 -> 7 |
| `aa3fdb3e596454f51c4d` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01_phase.questphase` / h0 / 11 -> 19 -> 13 |
| `b2a5237925e3bf6d6ce1` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01_phase.questphase` / h0 / 7 -> 6 -> 20 |
| `b9d00bebb708df7300a1` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01_phase.questphase` / h0 / 21 -> 18 -> 19 |
| `cb4cae77969c935b1ba4` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01_phase.questphase` / h0 / 18 -> 19 -> 13 |
| `f930f19660b119a68969` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01_phase.questphase` / h0 / 7 -> 6 -> 11 |
| `f9b4aa69da8797ae40be` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01_phase.questphase` / h0 / 6 -> 11 -> 19 |
| `fee3756653cd083fb28e` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01_phase.questphase` / h22 / 12 -> 10 -> 6 |
| `ff4c8a828496c45d7dfa` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_01\ma_pac_cvi_01_phase.questphase` / h0 / 6 -> 20 -> 21 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
