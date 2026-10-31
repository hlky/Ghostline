# base-ma-wat-nid-16

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\community\ma_wat_nid_16_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\community\ma_wat_nid_16_com_workers.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_quest.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 2 |
| `questMiscAICommandNode` | 3 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `95b7458b3ffd83fd4357` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase` / h0 / 0 -> 5 -> 50 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase` / h0 / 49 -> 54 -> 48 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase` / h0 / 5 -> 3 -> 16 |
| `5870e2fba5607932758d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase` / h0 / 5 -> 25 -> 53 |
| `8d10896873df5c62014e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase` / h0 / 0 -> 5 -> 3 |
| `978a69b98137186c49a7` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_quest.quest` / h0 / 1 -> 0 -> 2 |
| `987122e5e2fcd167cf6c` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase` / h0 / 1 -> 0 -> 5 |
| `a3e5f861a4b71433135a` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase` / h0 / 55 -> 43 -> 61 |
| `a75c554a07cd5b4f2c3c` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase` / h0 / 61 -> 44 -> 45 |
| `d2347eb446c8c5230fe1` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase` / h0 / 0 -> 5 -> 21 |
| `e76ef856f84c1bde0646` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase` / h0 / 44 -> 45 -> 2 |
| `f32075b9bd1400071eeb` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase` / h0 / 5 -> 21 -> 56 |
| `f3a269b6a97862bc211c` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase` / h0 / 0 -> 5 -> 25 |
| `f66cfde7fa1a88e1f4a1` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase` / h0 / 21 -> 56 -> 55 |
| `fb88c57a0a8c4def1547` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase` / h0 / 43 -> 61 -> 44 |
| `fee3756653cd083fb28e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase` / h0 / 56 -> 55 -> 43 |
| `ff4c8a828496c45d7dfa` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_16\ma_wat_nid_16_phase.questphase` / h0 / 21 -> 49 -> 54 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
