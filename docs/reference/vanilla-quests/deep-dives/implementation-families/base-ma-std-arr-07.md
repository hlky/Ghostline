# base-ma-std-arr-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\community\ma_std_arr_07_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_07/onscreens/ma_std_arr_07_onscreen_01`
- `points_of_interest/minor_activities/ma_std_arr_07`
- `quests/minor_activities/santo_domingo/arroyo/ma_std_arr_07`
- `quests/minor_activities/santo_domingo/arroyo/ma_std_arr_07/ma_description`
- `quests/minor_activities/santo_domingo/arroyo/ma_std_arr_07/ma_std_arr_07/go_to_stash`
- `quests/minor_activities/santo_domingo/arroyo/ma_std_arr_07/ma_std_arr_07/loot_stash`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 4 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 1 |
| `questItemManagerNodeDefinition[questReInitContainers_NodeType,questReInitContainers_NodeTypeParams]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 7 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMiscAICommandNode` | 3 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `1e253d0fcbd364975401` | 3 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 65 -> 24 -> 90 |
| `95b7458b3ffd83fd4357` | 3 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 24 -> 101 -> 100 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 46 -> 109 -> 93 |
| `2e0e3e918dc6fad6b34c` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 127 -> 126 -> 129 |
| `6b3e5fe15b7a64a01e21` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 75 -> 76 -> 112 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 56 -> 60 -> 127 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 139 -> 137 -> 136 |
| `0d59d5b737ce1451c32f` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 133 -> 124 -> 129 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 54 -> 55 -> 56 |
| `14a09e3075b38b5c1b01` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 136 -> 58 -> 59 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 121 -> 116 -> 117 |
| `191018f411bf7782f315` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 50 -> 54 -> 55 |
| `1d48bd7cbbaeca8257d2` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 63 -> 57 -> 86 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 46 -> 109 -> 68 |
| `2465cabc5e4b65280bdb` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 65 -> 46 -> 109 |
| `269c2b32f42c5076c04c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 54 -> 55 -> 114 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 78 -> 139 -> 135 |
| `45384fad45d3768a409d` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 124 -> 129 -> 63 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 109 -> 93 -> 68 |
| `4e9253a72e6b0134b8dd` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_07\ma_std_arr_07_phase.questphase` / h0 / 55 -> 56 -> 60 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
