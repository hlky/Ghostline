# base-ma-std-arr-13

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13_phase.questphase` / h0 / 34 -> 35 -> 33 |
| `163b243e32c0bb8c4eb7` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13_phase.questphase` / h0 / 31 -> 25 -> 13 |
| `3457629da944eac3b4b2` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13_phase.questphase` / h0 / 0 -> 31 -> 25 |
| `4046f7e0ed1087267da3` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13_phase.questphase` / h0 / 13 -> 17 -> 15 |
| `75582ae0b4c1620a124c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13_phase.questphase` / h0 / 26 -> 32 -> 2 |
| `83a3757c3e54bd269e2e` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13_phase.questphase` / h0 / 25 -> 13 -> 17 |
| `978a69b98137186c49a7` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13.quest` / h0 / 2 -> 1 -> 0 |
| `a3e5f861a4b71433135a` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13_phase.questphase` / h0 / 37 -> 27 -> 26 |
| `a9350e05126ec08a441f` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13_phase.questphase` / h0 / 17 -> 15 -> 34 |
| `de85a1a08a5312334d23` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13_phase.questphase` / h0 / 17 -> 15 -> 36 |
| `effb57f3d4d2c06d7dd2` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13_phase.questphase` / h0 / 27 -> 26 -> 32 |
| `f66cfde7fa1a88e1f4a1` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13_phase.questphase` / h0 / 15 -> 36 -> 37 |
| `fee3756653cd083fb28e` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13_phase.questphase` / h0 / 36 -> 37 -> 27 |
| `ff4c8a828496c45d7dfa` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_13\ma_std_arr_13_phase.questphase` / h0 / 15 -> 34 -> 35 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
