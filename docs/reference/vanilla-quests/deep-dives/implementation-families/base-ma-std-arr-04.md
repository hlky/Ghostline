# base-ma-std-arr-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\community\ma_std_arr_04_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\ma_std_arr_04.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\ma_std_arr_04.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\ma_std_arr_04_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\ma_std_arr_04_phase.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\phases\ma_std_arr_04_bugfixing.questphase` | repair | 1 / 0 |  |

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
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\ma_std_arr_04_phase.questphase` / h0 / 36 -> 37 -> 35 |
| `2aa0f3a3b004f071652f` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\ma_std_arr_04_phase.questphase` / h0 / 23 -> 22 -> 7 |
| `4046f7e0ed1087267da3` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\ma_std_arr_04_phase.questphase` / h0 / 16 -> 28 -> 18 |
| `83a3757c3e54bd269e2e` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\ma_std_arr_04_phase.questphase` / h0 / 21 -> 16 -> 28 |
| `978a69b98137186c49a7` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\ma_std_arr_04.quest` / h0 / 2 -> 1 -> 0 |
| `a3e5f861a4b71433135a` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\ma_std_arr_04_phase.questphase` / h0 / 40 -> 23 -> 22 |
| `a9350e05126ec08a441f` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\ma_std_arr_04_phase.questphase` / h0 / 28 -> 18 -> 36 |
| `de85a1a08a5312334d23` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\ma_std_arr_04_phase.questphase` / h0 / 28 -> 18 -> 39 |
| `f576caab49a2928ada0b` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\ma_std_arr_04_phase.questphase` / h0 / 0 -> 21 -> 16 |
| `f66cfde7fa1a88e1f4a1` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\ma_std_arr_04_phase.questphase` / h0 / 18 -> 39 -> 40 |
| `fee3756653cd083fb28e` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\ma_std_arr_04_phase.questphase` / h0 / 39 -> 40 -> 23 |
| `ff4c8a828496c45d7dfa` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_04\ma_std_arr_04_phase.questphase` / h0 / 18 -> 36 -> 37 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
