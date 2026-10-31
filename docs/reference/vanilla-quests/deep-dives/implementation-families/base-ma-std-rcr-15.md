# base-ma-std-rcr-15

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\community\ma_std_rcr_15_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_RestrictMovementToArea]` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questInputNodeDefinition` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `51d78876d4b7cc3025b7` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 6 -> 3 -> 4 |
| `8d10896873df5c62014e` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 0 -> 6 -> 3 |
| `06af7fe7288edcb74355` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 30 -> 37 -> 33 |
| `177698b91f1699d4927c` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 36 -> 32 -> 37 |
| `18984ccbc145e4fef1a0` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 31 -> 37 -> 34 |
| `24188ec8e05e20e4e7a6` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 35 -> 36 -> 31 |
| `29a99096ea308b54f59e` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 35 -> 36 -> 30 |
| `7576b3e62a6e7713a306` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 36 -> 30 -> 37 |
| `87f748ac5b6090e3ee28` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 29 -> 37 -> 33 |
| `8a462ea9af5bb9325fc8` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 32 -> 37 -> 33 |
| `978a69b98137186c49a7` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15.quest` / h0 / 2 -> 1 -> 0 |
| `987122e5e2fcd167cf6c` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 1 -> 0 -> 6 |
| `999952894b2b547e9107` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 7 -> 8 -> 9 |
| `a3278cd250ea4f049bda` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 32 -> 37 -> 34 |
| `ac018050c793dc3ac1fb` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 29 -> 37 -> 34 |
| `b4cc2db9d1fc1c446ecd` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 35 -> 36 -> 32 |
| `c4f8fa0bede88335c941` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 24 -> 7 -> 8 |
| `c85db10f147df1382d0c` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 31 -> 37 -> 33 |
| `c9170fb2e5c18a121162` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 9 -> 35 -> 36 |
| `cd0897a21972132ec435` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_15\ma_std_rcr_15_phase.questphase` / h0 / 35 -> 36 -> 29 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
