# base-ma-wat-lch-16

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\ma_wat_lch_16.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\ma_wat_lch_16.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `points_of_interest/minor_activities/ma_wat_lch_16`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questInputNodeDefinition` | 3 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 12 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `390a473190232b036b84` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 0 -> 52 -> 66 |
| `56c5d669bfd77320b774` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 0 -> 53 -> 66 |
| `720b75ee87ebe11fbb99` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 0 -> 48 -> 66 |
| `72fd99cecf8bfca9f18f` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 0 -> 49 -> 66 |
| `78fb258a1e58d15d33c7` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 0 -> 50 -> 66 |
| `a578dd59c1410c9a0e52` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 0 -> 54 -> 66 |
| `04d44032fde67923816a` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h60 / 8 -> 5 -> 6 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 31 -> 68 -> 30 |
| `0c25fb26cf0cf435c0f4` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 66 -> 55 -> 21 |
| `229ecc64af17bf000afa` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 53 -> 66 -> 55 |
| `5a9aea1e5a7af2746018` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 52 -> 66 -> 55 |
| `63f4c0eb4c1a84072d98` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 62 -> 67 -> 55 |
| `720473c9be07a334976b` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 54 -> 66 -> 55 |
| `726009171d642e7ec85f` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 60 -> 67 -> 55 |
| `82eb5d659b4c198816f2` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 67 -> 55 -> 21 |
| `851b1640c46cf4fbe875` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 64 -> 67 -> 55 |
| `89f5f9146f2f314f1dfa` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 50 -> 66 -> 55 |
| `9c4b4ad1c1fb1b17f794` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 63 -> 67 -> 55 |
| `a3e5f861a4b71433135a` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h60 / 2 -> 3 -> 8 |
| `a9170234bc93cf613a2e` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_16\phase\ma_wat_lch_16_phase.questphase` / h0 / 48 -> 66 -> 55 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
