# base-ma-wat-nid-21

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\community\ma_wat_nid_21.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 12 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `390a473190232b036b84` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 0 -> 56 -> 49 |
| `56c5d669bfd77320b774` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 0 -> 57 -> 49 |
| `720b75ee87ebe11fbb99` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 0 -> 45 -> 49 |
| `72fd99cecf8bfca9f18f` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 0 -> 47 -> 49 |
| `78fb258a1e58d15d33c7` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 0 -> 48 -> 49 |
| `a578dd59c1410c9a0e52` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 0 -> 58 -> 49 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 40 -> 81 -> 39 |
| `0c25fb26cf0cf435c0f4` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 49 -> 80 -> 46 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 84 -> 70 -> 85 |
| `229ecc64af17bf000afa` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 57 -> 49 -> 80 |
| `264a53a529f59ab477e3` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 80 -> 46 -> 61 |
| `295acc02504244db40db` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 31 -> 41 -> 67 |
| `2bbf5528ada3f00dc747` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 0 -> 4 -> 83 |
| `5a9aea1e5a7af2746018` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 56 -> 49 -> 80 |
| `621ce8c3ce77bfa158b1` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 41 -> 67 -> 20 |
| `63f4c0eb4c1a84072d98` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 77 -> 76 -> 80 |
| `71892f49b88f7b8bb8be` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 0 -> 6 -> 71 |
| `720473c9be07a334976b` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 58 -> 49 -> 80 |
| `726009171d642e7ec85f` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 75 -> 76 -> 80 |
| `79d5c71726a61b77a50e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_21\ma_wat_nid_21_phase.questphase` / h0 / 0 -> 4 -> 40 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
