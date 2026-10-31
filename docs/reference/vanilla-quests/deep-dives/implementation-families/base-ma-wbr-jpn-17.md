# base-ma-wbr-jpn-17

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_17\ma_wbr_jpn_17.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_17\ma_wbr_jpn_17.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_17\ma_wbr_jpn_17_phase.questphase |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_17\ma_wbr_jpn_17_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questInputNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPhaseNodeDefinition` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_17\ma_wbr_jpn_17_phase.questphase` / h35 / 6 -> 3 -> 4 |
| `90cf58434e79ce42af1e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_17\ma_wbr_jpn_17_phase.questphase` / h35 / 0 -> 7 -> 6 |
| `94c40bd8d94487fa94c2` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_17\ma_wbr_jpn_17_phase.questphase` / h0 / 6 -> 16 -> 13 |
| `978a69b98137186c49a7` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_17\ma_wbr_jpn_17.quest` / h0 / 2 -> 1 -> 0 |
| `9b7bc10066df80da3639` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_17\ma_wbr_jpn_17_phase.questphase` / h35 / 3 -> 4 -> 5 |
| `c027f7ccfc3f4625137e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_17\ma_wbr_jpn_17_phase.questphase` / h0 / 5 -> 6 -> 16 |
| `c96df7fdb4914831a6ab` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_17\ma_wbr_jpn_17_phase.questphase` / h0 / 15 -> 5 -> 6 |
| `d1b51f021ece600131ad` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_17\ma_wbr_jpn_17_phase.questphase` / h0 / 0 -> 15 -> 5 |
| `e4bb62ba97e6304ee1ff` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_17\ma_wbr_jpn_17_phase.questphase` / h0 / 5 -> 6 -> 1 |
| `f930f19660b119a68969` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_17\ma_wbr_jpn_17_phase.questphase` / h0 / 5 -> 6 -> 14 |
| `fee3756653cd083fb28e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_17\ma_wbr_jpn_17_phase.questphase` / h35 / 7 -> 6 -> 3 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
