# base-ma-wbr-jpn-12

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\community\ma_wbr_jpn_12_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\community\ma_wbr_jpn_12_police_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/japantown/ma_wbr_jpn_12/shards/ma_wbr_jpn_12_a`
- `points_of_interest/minor_activities/ma_wbr_jpn_12`
- `quests/main_quest/act_01/q105_dollhouse/05_leave_dollhouse/take_weapons`
- `quests/main_quest/act_01/q105_dollhouse/dollhouse/weapons`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 2 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 3 |
| `questDeletionMarkerNodeDefinition` | 6 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | 3 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h0 / 4 -> 0 -> 1 |
| `feb6a15fa85f92380e8f` | 3 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h0 / 4 -> 0 -> 90 |
| `99c738f69bc472a4bcbf` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h0 / 10 -> 29 -> 30 |
| `01cc762cd06f16743b1c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h38 / 15 -> 16 -> 1 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h0 / 63 -> 6 -> 38 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h0 / 99 -> 96 -> 95 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h0 / 13 -> 50 -> 33 |
| `09342269699c12a2e008` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h0 / 63 -> 21 -> 28 |
| `0976bdf75170c3f46615` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h0 / 1 -> 64 -> 63 |
| `0b387b0e0f2538ab6067` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h38 / 3 -> 5 -> 11 |
| `0e0b0ec1add4154b2d49` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h38 / 5 -> 11 -> 6 |
| `0f660f7484731cdb671e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h0 / 50 -> 10 -> 29 |
| `12b102391853a0e26cba` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h38 / 7 -> 8 -> 9 |
| `1489a2df8e7f98f9c78e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h0 / 0 -> 1 -> 64 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h0 / 4 -> 13 -> 50 |
| `204ca9b8b94427c1ef81` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h0 / 52 -> 51 -> 34 |
| `2d61756ead564fdbaa1f` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h0 / 0 -> 90 -> 37 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h0 / 99 -> 98 -> 95 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h0 / 30 -> 99 -> 98 |
| `2f75f5df6bd0c6d34fe4` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_12\ma_wbr_jpn_12_phase.questphase` / h0 / 21 -> 28 -> 16 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
