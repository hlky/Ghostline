# base-ma-wbr-jpn-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_05\community\ma_wbr_jpn_05_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_05\ma_wbr_jpn_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_05\ma_wbr_jpn_05.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_05\ma_wbr_jpn_05_phase.questphase |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_05\ma_wbr_jpn_05_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questEventManagerNodeDefinition` | 1 |
| `questInputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_05\ma_wbr_jpn_05_phase.questphase` / h0 / 5 -> 3 -> 6 |
| `8d10896873df5c62014e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_05\ma_wbr_jpn_05_phase.questphase` / h0 / 0 -> 5 -> 3 |
| `987122e5e2fcd167cf6c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_05\ma_wbr_jpn_05_phase.questphase` / h0 / 1 -> 0 -> 5 |
| `a7a5fe905bdfb362ca2a` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_05\ma_wbr_jpn_05.quest` / h0 / 2 -> 1 -> 0 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
