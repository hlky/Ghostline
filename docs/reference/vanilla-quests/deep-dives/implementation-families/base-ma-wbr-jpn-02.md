# base-ma-wbr-jpn-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_02\community\ma_wbr_jpn_02_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_02\ma_wbr_jpn_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_02\ma_wbr_jpn_02.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_02\ma_wbr_jpn_02_phase.questphase |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_02\ma_wbr_jpn_02_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questEventManagerNodeDefinition` | 1 |
| `questInputNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPhaseNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `7ec318e8dc8f99d31f35` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_02\ma_wbr_jpn_02_phase.questphase` / h0 / 8 -> 17 -> 13 |
| `8d10896873df5c62014e` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_02\ma_wbr_jpn_02_phase.questphase` / h0 / 0 -> 5 -> 3 |
| `9cb82fbabfd13bc9dbf8` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_02\ma_wbr_jpn_02_phase.questphase` / h0 / 20 -> 26 -> 27 |
| `2acd877b9c8a443befba` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_02\ma_wbr_jpn_02_phase.questphase` / h0 / 15 -> 22 -> 21 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_02\ma_wbr_jpn_02_phase.questphase` / h0 / 5 -> 3 -> 16 |
| `81768cf0bb7449970d70` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_02\ma_wbr_jpn_02_phase.questphase` / h0 / 15 -> 22 -> 20 |
| `978a69b98137186c49a7` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_02\ma_wbr_jpn_02.quest` / h0 / 2 -> 1 -> 0 |
| `987122e5e2fcd167cf6c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_02\ma_wbr_jpn_02_phase.questphase` / h0 / 1 -> 0 -> 5 |
| `d82136d72c1bc173bf65` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_02\ma_wbr_jpn_02_phase.questphase` / h0 / 22 -> 21 -> 8 |
| `f5f34933e2389cae9cf7` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_02\ma_wbr_jpn_02_phase.questphase` / h0 / 5 -> 15 -> 22 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
