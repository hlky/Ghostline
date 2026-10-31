# base-ma-std-rcr-12

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\community\ma_std_rcr_12_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\community\ma_std_rcr_12_com_a.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\community\ma_std_rcr_12_homeless_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_12/onscreens/ma_std_rcr_12_onscreen_01`
- `onscreens/emails/quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_12/onscreens/ma_std_rcr_12_onscreen_02`
- `points_of_interest/minor_activities/ma_std_rcr_12`
- `quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_12`
- `quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_12/description`
- `quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_12/ma_std_rcr_12/loot_stash`
- `quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_12/ma_std_rcr_12/reach_stash`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 5 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 7 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `18be198845c90c6bb3c8` | 3 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h196 / 10 -> 6 -> 3 |
| `1d48bd7cbbaeca8257d2` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 43 -> 44 -> 51 |
| `66e17bf07a534afe17b2` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h196 / 10 -> 6 -> 4 |
| `71892f49b88f7b8bb8be` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 2 -> 20 -> 50 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 40 -> 41 -> 179 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 179 -> 176 -> 175 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 20 -> 166 -> 136 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 164 -> 39 -> 40 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 2 -> 20 -> 166 |
| `1e190ae7e8c4809eafc0` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 20 -> 138 -> 163 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 179 -> 178 -> 175 |
| `380e05c8b76fbf6ccaf7` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 22 -> 45 -> 164 |
| `45384fad45d3768a409d` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 176 -> 175 -> 43 |
| `4e9253a72e6b0134b8dd` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 39 -> 40 -> 41 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 1 -> 4 -> 5 |
| `53b397a39cc3f9c63a42` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 175 -> 43 -> 44 |
| `615cf41b6f9a0ec2221d` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 43 -> 44 -> 167 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 179 -> 177 -> 175 |
| `7a88801c0d5664236a9c` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 41 -> 179 -> 178 |
| `7b136ed9620da85cbac6` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_12\ma_std_rcr_12_phase.questphase` / h0 / 176 -> 175 -> 146 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
