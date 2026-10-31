# base-ma-wbr-jpn-14

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_14\ma_wbr_jpn_14.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_14\ma_wbr_jpn_14.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_14\ma_wbr_jpn_14_phase.questphase |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_14\ma_wbr_jpn_14_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questEventManagerNodeDefinition` | 1 |
| `questInputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `978a69b98137186c49a7` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_14\ma_wbr_jpn_14.quest` / h0 / 2 -> 1 -> 0 |
| `b3396120b0ea52314aa7` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_14\ma_wbr_jpn_14_phase.questphase` / h0 / 2 -> 4 -> 6 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
