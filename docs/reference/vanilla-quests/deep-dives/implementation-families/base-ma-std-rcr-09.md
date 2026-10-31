# base-ma-std-rcr-09

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\community\ma_std_rcr_09_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_09/onscreens/ma_std_rcr_09_onscreen_01`
- `points_of_interest/minor_activities/ma_std_rcr_09`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `71892f49b88f7b8bb8be` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h0 / 0 -> 11 -> 17 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h0 / 30 -> 39 -> 37 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h46 / 11 -> 9 -> 4 |
| `02d878a28a675e881f96` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h0 / 37 -> 35 -> 18 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h0 / 4 -> 5 -> 32 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h0 / 39 -> 36 -> 35 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h0 / 11 -> 33 -> 30 |
| `0b387b0e0f2538ab6067` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h46 / 9 -> 2 -> 7 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h0 / 33 -> 39 -> 37 |
| `136512a6b340968ce236` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h0 / 15 -> 34 -> 1 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h46 / 11 -> 9 -> 3 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h0 / 0 -> 11 -> 33 |
| `1ecc1e1f4c4151a3aba0` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h0 / 11 -> 33 -> 39 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h0 / 39 -> 38 -> 35 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h0 / 36 -> 35 -> 13 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h0 / 35 -> 13 -> 15 |
| `45a0059a97ab5b10fb49` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h0 / 36 -> 35 -> 18 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h0 / 33 -> 30 -> 39 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h0 / 3 -> 4 -> 5 |
| `53e1b61b58de584e4473` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_09\ma_std_rcr_09_phase.questphase` / h0 / 30 -> 39 -> 38 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
