# base-ma-std-rcr-16

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\community\ma_std_rcr_16_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_16/onscreens/ma_std_rcr_16_onscreen_02`
- `points_of_interest/minor_activities/ma_std_rcr_16`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `71892f49b88f7b8bb8be` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h0 / 2 -> 20 -> 48 |
| `02d878a28a675e881f96` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h0 / 66 -> 64 -> 46 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h0 / 68 -> 65 -> 64 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h0 / 20 -> 62 -> 58 |
| `1236b824035f3d3d10f6` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h108 / 2 -> 3 -> 4 |
| `136512a6b340968ce236` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h0 / 36 -> 63 -> 3 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h108 / 9 -> 6 -> 2 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h0 / 2 -> 20 -> 62 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h0 / 68 -> 67 -> 64 |
| `2e578fd8f85357f1804f` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h0 / 20 -> 68 -> 66 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h0 / 65 -> 64 -> 22 |
| `3aaa77554027632f87e9` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h108 / 2 -> 3 -> 8 |
| `3defb6b5bfe82560078d` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h0 / 2 -> 0 -> 39 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h0 / 64 -> 22 -> 36 |
| `45a0059a97ab5b10fb49` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h0 / 65 -> 64 -> 46 |
| `479a11033aba2b8c1ef3` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h0 / 20 -> 68 -> 65 |
| `69ac42d59aa43099e19c` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h0 / 36 -> 63 -> 59 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h0 / 68 -> 66 -> 64 |
| `7b136ed9620da85cbac6` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h0 / 65 -> 64 -> 61 |
| `90cf58434e79ce42af1e` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_16\ma_std_rcr_16_phase.questphase` / h108 / 0 -> 10 -> 9 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
