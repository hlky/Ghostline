# base-ma-wbr-jpn-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_04\community\ma_wbr_jpn_04_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_04\ma_wbr_jpn_04.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_04\ma_wbr_jpn_04.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_04\ma_wbr_jpn_04_phase.questphase |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_04\ma_wbr_jpn_04_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questInputNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `23171babf504911e54fc` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_04\ma_wbr_jpn_04_phase.questphase` / h0 / 1 -> 25 -> 24 |
| `94c40bd8d94487fa94c2` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_04\ma_wbr_jpn_04_phase.questphase` / h0 / 24 -> 34 -> 33 |
| `9661fbbfa2ff9c12f5af` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_04\ma_wbr_jpn_04_phase.questphase` / h0 / 34 -> 33 -> 20 |
| `978a69b98137186c49a7` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_04\ma_wbr_jpn_04.quest` / h0 / 2 -> 1 -> 0 |
| `c027f7ccfc3f4625137e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_04\ma_wbr_jpn_04_phase.questphase` / h0 / 25 -> 24 -> 34 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
